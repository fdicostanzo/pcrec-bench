# pcrec-bench report

reporter: v9 (2026-08-30)

## Query

- filters: subbench=email-specimen, version=0.2, until=2026-08-30T11:00:00Z
- record source: store/index.tsv (68 candidate file(s))
- records included: 10
    - `email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260829T203945Z` (store/records/email-specimen@0.2/libpcre2_10.46_interp-caps-simdna/email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260829T203945Z.jsonl) — agreement: n/a (v1.3)
    - `email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260829T190658Z` (store/records/email-specimen@0.2/libpcre2_10.46_jit-caps-simdna/email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260829T190658Z.jsonl) — agreement: n/a (v1.3)
    - `email-specimen@0.2__pcrec_35e1ab1_auto-caps-simdna__budu-ryzen1600__20260828T142809Z` (store/records/email-specimen@0.2/pcrec_35e1ab1_auto-caps-simdna/email-specimen@0.2__pcrec_35e1ab1_auto-caps-simdna__budu-ryzen1600__20260828T142809Z.jsonl) — agreement: n/a (v1.3)
    - `email-specimen@0.2__pcrec_35e1ab1_auto-nocaps-simdna__budu-ryzen1600__20260828T143259Z` (store/records/email-specimen@0.2/pcrec_35e1ab1_auto-nocaps-simdna/email-specimen@0.2__pcrec_35e1ab1_auto-nocaps-simdna__budu-ryzen1600__20260828T143259Z.jsonl) — agreement: n/a (v1.3)
    - `email-specimen@0.2__pcrec_35e1ab1_vm-caps-simdna__budu-ryzen1600__20260828T143810Z` (store/records/email-specimen@0.2/pcrec_35e1ab1_vm-caps-simdna/email-specimen@0.2__pcrec_35e1ab1_vm-caps-simdna__budu-ryzen1600__20260828T143810Z.jsonl) — agreement: n/a (v1.3)
    - `email-specimen@0.2__pcrec_35e1ab1_vm-in-caps-simdna__budu-ryzen1600__20260828T144426Z` (store/records/email-specimen@0.2/pcrec_35e1ab1_vm-in-caps-simdna/email-specimen@0.2__pcrec_35e1ab1_vm-in-caps-simdna__budu-ryzen1600__20260828T144426Z.jsonl) — agreement: n/a (v1.3)
    - `email-specimen@0.2__pcrec_36d5963_auto-caps-simdna__budu-ryzen1600__20260829T191837Z` (store/records/email-specimen@0.2/pcrec_36d5963_auto-caps-simdna/email-specimen@0.2__pcrec_36d5963_auto-caps-simdna__budu-ryzen1600__20260829T191837Z.jsonl) — agreement: n/a (v1.3)
    - `email-specimen@0.2__pcrec_36d5963_auto-nocaps-simdna__budu-ryzen1600__20260829T192412Z` (store/records/email-specimen@0.2/pcrec_36d5963_auto-nocaps-simdna/email-specimen@0.2__pcrec_36d5963_auto-nocaps-simdna__budu-ryzen1600__20260829T192412Z.jsonl) — agreement: n/a (v1.3)
    - `email-specimen@0.2__pcrec_36d5963_vm-caps-simdna__budu-ryzen1600__20260829T204855Z` (store/records/email-specimen@0.2/pcrec_36d5963_vm-caps-simdna/email-specimen@0.2__pcrec_36d5963_vm-caps-simdna__budu-ryzen1600__20260829T204855Z.jsonl) — agreement: n/a (v1.3)
    - `email-specimen@0.2__pcrec_36d5963_vm-in-caps-simdna__budu-ryzen1600__20260829T193713Z` (store/records/email-specimen@0.2/pcrec_36d5963_vm-in-caps-simdna/email-specimen@0.2__pcrec_36d5963_vm-in-caps-simdna__budu-ryzen1600__20260829T193713Z.jsonl) — agreement: n/a (v1.3)
- superseded: 4 record(s) (OD-B15; --all-records lists them)
- sub-bench version(s): email-specimen@0.2
- machine(s): budu-ryzen1600
- schema version(s): 1.3
- grain: subject (per pattern x subject x regime; the drill-down)
- reduction: median/min/max/stddev (population) over per-trial `elapsed_ns / iterations`; lazy-JIT compile cost is DERIVED as first-match-row-minus-steady-state (lowest `seq` timed row for the pattern, minus the median of every other timed row), one value per (pattern, testee), never pooled with another execution-model class's compile cost
- `form`: this report includes a `whole-subject` artifact beside `plain` for at least one cell (schema v1.1: a testee with no end-anchored mode compiles and times a SEPARATE artifact for match-compliance, e.g. `(?:pattern)\z`, where another testee reaches the same regime via runtime flags on its ordinary artifact) -- shown as a per-row COLUMN, not a split: both forms answer the same regime and RANK TOGETHER in one table (`form` is a key only for compile-cost rows, where a whole-subject artifact is genuinely a separate compile with its own cost); `fact` restates it as 'same program' / 'separate artifact' (R4)
- status policy (OD-B14): a ranking row whose record `status` is not `measured` is excluded from ranking by default, listed under its table as `not ranked: <testee> -- <status> (<status_detail excerpt>)`; `--include-unmeasured` ranks it instead, with `status` shown
- trial-agreement policy (schema v1.4, rule v1.4-group, X31-X33): a record's five trials must agree to within k=1.5 on every group of its rows — one slow trial of five tolerated; two, or one fast, is a disagreeing row; a group disagrees at >= 2 disagreeing rows reaching a third of it (d_min=2, c=3); a record with a disagreeing group, or with fewer than five odd trials, is `inconclusive-spread` and unranked like `inconclusive-load`; the after-run load/occupancy samples are provenance (v1.4 X13), shown under --include-provenance
- status rule: v1.1-1.3 X13 (both samples quiet) on 10 record(s)
- tier policy (R3, schema v1.2 `tier`, absent = `pinned`): a `scratch`-tier row is excluded from ranking by default, listed as `scratch: <testee>`; `--include-scratch` ranks it instead, with a `tier` column
- duplicate-record policy (OD-B15, amended 2026-08-25): the NEWEST MEASURED record per (subbench@version, testee_id, machine) ranks by default -- a newer record that is NOT measured does not supersede a measured one of the same testee and version (listed as "newer, not measured" instead); only when no record in the group is measured does the newest record overall stand (itself unranked per the status policy above, unless --include-unmeasured). `--all-records` shows every record as its own row, its testee id suffixed `@<timestamp>`

## Ranking (per pattern x subject x regime; best median first)

### `factored` / `s-000` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.5 | 32.4 | 32.7 | 0.1 | 0.037x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.7 | 34.4 | 35.1 | 0.2 | 0.040x | 1.067x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 69.5 | 69.4 | 70.4 | 0.4 | 0.080x | 2.139x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 86.0 | 85.7 | 86.5 | 0.3 | 0.099x | 2.648x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 143.4 | 142.5 | 144.6 | 0.7 | 0.165x | 4.413x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 145.4 | 144.5 | 146.7 | 0.9 | 0.167x | 4.475x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 148.5 | 147.8 | 149.5 | 0.6 | 0.171x | 4.572x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 148.8 | 147.6 | 149.2 | 0.6 | 0.171x | 4.582x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 866.0 | 849.6 | 872.3 | 7.7 | 0.997x | 26.660x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 868.2 | 857.9 | 890.0 | 11.4 | 1.000x | 26.728x |

### `factored` / `s-000` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 58.7 | 58.5 | 59.2 | 0.3 | 0.068x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 58.7 | 58.6 | 59.9 | 0.5 | 0.068x | 1.000x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 62.7 | 62.5 | 63.1 | 0.2 | 0.073x | 1.068x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 62.8 | 62.6 | 63.3 | 0.3 | 0.073x | 1.071x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 148.0 | 147.9 | 148.4 | 0.2 | 0.173x | 2.524x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 148.9 | 147.9 | 151.3 | 1.1 | 0.174x | 2.538x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 150.2 | 149.5 | 159.7 | 3.9 | 0.175x | 2.561x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 152.5 | 152.4 | 153.3 | 0.3 | 0.178x | 2.599x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 155.7 | 153.6 | 168.2 | 5.4 | 0.182x | 2.654x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 857.7 | 852.9 | 867.3 | 6.4 | 1.000x | 14.621x |

### `factored` / `s-001` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 40.0 | 39.8 | 40.1 | 0.1 | 0.033x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 43.1 | 42.8 | 43.9 | 0.4 | 0.035x | 1.077x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 89.9 | 89.6 | 90.5 | 0.3 | 0.073x | 2.247x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 104.9 | 104.0 | 105.2 | 0.5 | 0.085x | 2.624x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 197.6 | 197.2 | 199.3 | 0.7 | 0.161x | 4.941x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 201.7 | 200.8 | 207.1 | 2.3 | 0.164x | 5.042x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 203.6 | 202.8 | 204.1 | 0.5 | 0.166x | 5.091x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 214.9 | 212.7 | 223.4 | 3.8 | 0.175x | 5.372x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,222.8 | 1,212.3 | 1,236.6 | 8.5 | 0.994x | 30.572x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,230.0 | 1,214.2 | 1,240.2 | 9.9 | 1.000x | 30.754x |

### `factored` / `s-001` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 77.8 | 77.7 | 78.3 | 0.2 | 0.064x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 77.8 | 77.7 | 78.1 | 0.1 | 0.064x | 1.000x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 80.3 | 79.9 | 80.6 | 0.2 | 0.066x | 1.032x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 80.6 | 80.4 | 80.7 | 0.1 | 0.066x | 1.036x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 177.7 | 175.2 | 183.1 | 3.2 | 0.145x | 2.285x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 205.1 | 204.6 | 205.3 | 0.3 | 0.168x | 2.637x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 207.3 | 206.1 | 209.5 | 1.2 | 0.170x | 2.665x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 207.6 | 206.8 | 209.6 | 0.9 | 0.170x | 2.668x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 210.0 | 209.9 | 213.9 | 1.5 | 0.172x | 2.699x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,222.6 | 1,218.6 | 1,229.3 | 3.5 | 1.000x | 15.715x |

### `factored` / `s-002` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 18.2 | 18.2 | 18.3 | 0.0 | 0.024x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.6 | 20.6 | 21.0 | 0.2 | 0.027x | 1.131x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33.2 | 32.9 | 33.3 | 0.1 | 0.044x | 1.822x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 49.4 | 49.2 | 50.1 | 0.3 | 0.065x | 2.710x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 104.3 | 104.2 | 104.6 | 0.1 | 0.138x | 5.723x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 104.9 | 104.7 | 105.0 | 0.1 | 0.138x | 5.753x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 105.3 | 105.0 | 107.7 | 1.0 | 0.139x | 5.778x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 105.7 | 105.6 | 106.4 | 0.3 | 0.139x | 5.799x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 751.0 | 735.0 | 753.2 | 6.7 | 0.990x | 41.204x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 758.5 | 749.1 | 764.4 | 5.7 | 1.000x | 41.615x |

### `factored` / `s-002` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 26.1 | 26.1 | 26.5 | 0.2 | 0.035x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 26.4 | 26.1 | 26.6 | 0.2 | 0.035x | 1.011x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 28.4 | 28.2 | 29.0 | 0.3 | 0.038x | 1.088x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 28.6 | 28.3 | 29.0 | 0.2 | 0.038x | 1.094x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 103.6 | 103.3 | 103.9 | 0.2 | 0.138x | 3.963x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 105.0 | 104.9 | 108.3 | 1.3 | 0.140x | 4.016x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 107.4 | 107.0 | 109.1 | 0.9 | 0.143x | 4.107x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 108.7 | 108.4 | 116.9 | 3.3 | 0.145x | 4.159x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 122.2 | 119.9 | 125.8 | 2.2 | 0.163x | 4.673x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 749.4 | 738.4 | 755.2 | 5.7 | 1.000x | 28.666x |

### `factored` / `s-003` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 43.3 | 43.1 | 43.4 | 0.1 | 0.033x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 46.5 | 46.2 | 46.9 | 0.2 | 0.035x | 1.075x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 97.4 | 97.3 | 97.6 | 0.1 | 0.074x | 2.251x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 111.2 | 110.9 | 111.6 | 0.3 | 0.085x | 2.569x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 209.5 | 209.5 | 215.1 | 2.2 | 0.159x | 4.842x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 216.7 | 216.2 | 217.4 | 0.4 | 0.165x | 5.009x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 216.8 | 216.2 | 228.4 | 4.6 | 0.165x | 5.009x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 220.2 | 220.1 | 227.4 | 3.1 | 0.167x | 5.090x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,315.1 | 1,312.8 | 1,336.8 | 9.8 | 1.000x | 30.390x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,323.0 | 1,312.2 | 1,355.9 | 16.6 | 1.006x | 30.572x |

### `factored` / `s-003` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 86.4 | 86.2 | 86.7 | 0.1 | 0.065x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 86.5 | 86.3 | 87.3 | 0.4 | 0.066x | 1.000x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 87.7 | 87.4 | 88.3 | 0.3 | 0.066x | 1.015x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 87.9 | 87.2 | 88.4 | 0.4 | 0.067x | 1.016x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 186.7 | 183.0 | 203.6 | 7.3 | 0.141x | 2.160x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 220.9 | 219.9 | 222.6 | 1.0 | 0.167x | 2.556x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 222.5 | 221.7 | 224.0 | 1.0 | 0.169x | 2.575x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 225.7 | 225.0 | 235.3 | 4.0 | 0.171x | 2.611x |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 228.2 | 227.1 | 230.1 | 1.0 | 0.173x | 2.640x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,320.2 | 1,311.8 | 1,333.8 | 8.2 | 1.000x | 15.274x |

### `factored` / `s-004` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 61.2 | 60.8 | 61.4 | 0.2 | 0.070x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 65.4 | 65.0 | 66.5 | 0.5 | 0.075x | 1.070x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 131.8 | 131.4 | 132.2 | 0.3 | 0.150x | 2.155x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 147.1 | 146.5 | 148.2 | 0.5 | 0.168x | 2.404x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 162.0 | 161.1 | 163.0 | 0.6 | 0.185x | 2.648x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 162.3 | 162.0 | 162.7 | 0.2 | 0.185x | 2.653x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 162.9 | 162.6 | 163.8 | 0.4 | 0.186x | 2.663x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 164.6 | 163.7 | 174.4 | 4.8 | 0.188x | 2.690x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 874.2 | 868.3 | 897.2 | 10.7 | 0.998x | 14.291x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 876.2 | 866.9 | 889.3 | 9.2 | 1.000x | 14.323x |

### `factored` / `s-004` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 120.5 | 120.1 | 120.7 | 0.2 | 0.137x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 120.5 | 120.3 | 120.9 | 0.2 | 0.137x | 1.000x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 123.6 | 123.4 | 123.8 | 0.1 | 0.140x | 1.025x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 123.9 | 123.3 | 123.9 | 0.2 | 0.140x | 1.028x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 166.7 | 166.3 | 167.9 | 0.6 | 0.189x | 1.383x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 167.6 | 167.1 | 173.4 | 2.4 | 0.190x | 1.391x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 168.0 | 167.8 | 168.0 | 0.1 | 0.190x | 1.394x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 169.4 | 168.7 | 174.7 | 2.2 | 0.192x | 1.405x |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 171.4 | 171.1 | 172.3 | 0.4 | 0.194x | 1.423x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 882.8 | 877.0 | 889.0 | 4.4 | 1.000x | 7.326x |

### `factored` / `s-005` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 18.3 | 18.2 | 18.3 | 0.0 | 0.024x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.7 | 20.5 | 20.9 | 0.1 | 0.027x | 1.133x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33.0 | 32.7 | 33.2 | 0.2 | 0.044x | 1.806x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 49.3 | 49.1 | 49.6 | 0.2 | 0.065x | 2.698x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 104.5 | 104.3 | 104.9 | 0.2 | 0.138x | 5.718x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 104.8 | 104.5 | 105.0 | 0.2 | 0.139x | 5.733x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 104.9 | 104.7 | 105.1 | 0.1 | 0.139x | 5.738x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 105.7 | 105.2 | 105.9 | 0.3 | 0.140x | 5.784x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 748.1 | 737.2 | 752.9 | 5.2 | 0.989x | 40.930x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 756.5 | 742.5 | 761.3 | 6.5 | 1.000x | 41.389x |

### `factored` / `s-005` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 26.1 | 26.0 | 26.2 | 0.1 | 0.035x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 26.6 | 26.1 | 27.2 | 0.4 | 0.036x | 1.018x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 28.5 | 28.3 | 31.2 | 1.1 | 0.038x | 1.094x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 29.0 | 28.3 | 29.9 | 0.6 | 0.039x | 1.112x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 103.4 | 103.4 | 103.7 | 0.1 | 0.139x | 3.964x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 105.1 | 104.9 | 115.2 | 4.1 | 0.141x | 4.026x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 107.1 | 107.0 | 107.3 | 0.1 | 0.144x | 4.104x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 108.8 | 108.4 | 110.4 | 0.7 | 0.146x | 4.171x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 121.8 | 120.7 | 126.8 | 2.3 | 0.163x | 4.668x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 745.9 | 742.1 | 752.3 | 3.4 | 1.000x | 28.584x |

### `factored` / `s-006` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 31.0 | 30.9 | 31.1 | 0.1 | 0.023x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.1 | 33.0 | 33.2 | 0.1 | 0.025x | 1.069x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 65.5 | 65.2 | 65.9 | 0.2 | 0.049x | 2.115x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 81.7 | 81.7 | 81.9 | 0.1 | 0.061x | 2.638x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 221.6 | 220.3 | 230.2 | 3.6 | 0.165x | 7.155x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 222.1 | 220.8 | 223.3 | 0.9 | 0.165x | 7.170x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 229.0 | 227.9 | 232.8 | 1.7 | 0.170x | 7.396x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 230.2 | 229.5 | 230.7 | 0.5 | 0.171x | 7.434x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,344.9 | 1,334.9 | 1,372.4 | 13.2 | 1.000x | 43.430x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,346.1 | 1,344.0 | 1,362.8 | 6.9 | 1.001x | 43.468x |

### `factored` / `s-006` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 55.8 | 55.7 | 56.0 | 0.1 | 0.042x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 55.8 | 55.8 | 57.8 | 0.8 | 0.042x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 59.1 | 59.0 | 59.3 | 0.1 | 0.044x | 1.060x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 59.3 | 59.3 | 59.4 | 0.1 | 0.044x | 1.064x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 164.7 | 162.6 | 167.4 | 1.6 | 0.123x | 2.954x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 227.8 | 227.3 | 228.4 | 0.4 | 0.170x | 4.087x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 229.2 | 227.9 | 231.1 | 1.1 | 0.171x | 4.111x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 230.0 | 228.6 | 231.0 | 0.7 | 0.172x | 4.125x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 232.5 | 232.0 | 240.5 | 3.6 | 0.174x | 4.171x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,340.0 | 1,328.1 | 1,352.0 | 8.6 | 1.000x | 24.035x |

### `factored` / `s-007` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 46.8 | 46.7 | 46.9 | 0.1 | 0.048x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 50.4 | 50.1 | 50.8 | 0.2 | 0.051x | 1.077x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 102.5 | 102.2 | 102.9 | 0.2 | 0.104x | 2.189x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 118.2 | 117.8 | 118.4 | 0.2 | 0.120x | 2.524x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 167.1 | 166.5 | 169.6 | 1.1 | 0.170x | 3.569x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 168.4 | 167.0 | 168.9 | 0.7 | 0.172x | 3.596x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 170.3 | 170.1 | 174.4 | 1.8 | 0.174x | 3.638x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 172.2 | 170.6 | 173.7 | 1.0 | 0.175x | 3.679x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 976.7 | 967.5 | 983.2 | 6.3 | 0.995x | 20.858x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 981.6 | 960.3 | 988.0 | 11.1 | 1.000x | 20.964x |

### `factored` / `s-007` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 92.0 | 91.9 | 92.0 | 0.0 | 0.095x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 92.1 | 91.9 | 92.6 | 0.2 | 0.095x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 94.8 | 94.2 | 95.5 | 0.5 | 0.098x | 1.031x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 94.8 | 94.3 | 95.4 | 0.4 | 0.098x | 1.031x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 170.6 | 170.1 | 174.0 | 1.4 | 0.177x | 1.855x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 172.5 | 171.7 | 175.4 | 1.4 | 0.178x | 1.876x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 175.0 | 174.7 | 175.9 | 0.4 | 0.181x | 1.903x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 175.7 | 174.9 | 177.1 | 0.8 | 0.182x | 1.911x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 179.0 | 178.0 | 185.4 | 2.8 | 0.185x | 1.946x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 966.5 | 959.4 | 969.1 | 3.3 | 1.000x | 10.511x |

### `factored` / `s-008` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 36.7 | 36.6 | 36.7 | 0.0 | 0.042x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 39.3 | 39.2 | 39.7 | 0.2 | 0.045x | 1.072x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 80.3 | 80.0 | 80.6 | 0.2 | 0.092x | 2.190x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 96.0 | 95.8 | 96.2 | 0.1 | 0.110x | 2.617x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 149.4 | 149.0 | 149.8 | 0.2 | 0.172x | 4.076x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 150.5 | 150.3 | 151.2 | 0.3 | 0.173x | 4.106x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 153.8 | 153.5 | 154.4 | 0.3 | 0.177x | 4.196x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 154.7 | 154.2 | 155.2 | 0.4 | 0.178x | 4.220x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 864.0 | 854.9 | 875.1 | 7.2 | 0.992x | 23.564x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 871.0 | 851.2 | 880.5 | 10.1 | 1.000x | 23.756x |

### `factored` / `s-008` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 69.6 | 69.5 | 69.7 | 0.1 | 0.081x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 69.7 | 69.5 | 70.1 | 0.2 | 0.081x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 73.4 | 73.2 | 73.6 | 0.1 | 0.085x | 1.054x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 73.6 | 73.5 | 73.6 | 0.0 | 0.086x | 1.057x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 150.5 | 149.7 | 154.0 | 1.5 | 0.175x | 2.163x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 152.9 | 152.9 | 153.6 | 0.3 | 0.178x | 2.197x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 154.0 | 153.4 | 154.9 | 0.6 | 0.179x | 2.212x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 155.8 | 154.8 | 188.0 | 12.9 | 0.181x | 2.239x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 158.0 | 157.7 | 158.6 | 0.3 | 0.184x | 2.269x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 859.2 | 850.3 | 863.1 | 4.4 | 1.000x | 12.343x |

### `factored` / `s-009` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.5 | 29.5 | 29.7 | 0.1 | 0.034x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.8 | 31.7 | 31.8 | 0.0 | 0.037x | 1.075x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 61.7 | 61.6 | 62.2 | 0.2 | 0.072x | 2.090x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 78.3 | 78.2 | 78.3 | 0.0 | 0.091x | 2.650x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 140.9 | 140.7 | 141.1 | 0.1 | 0.163x | 4.770x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 142.2 | 140.8 | 142.7 | 0.7 | 0.165x | 4.814x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.8 | 145.4 | 146.3 | 0.3 | 0.169x | 4.935x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 146.6 | 146.0 | 147.1 | 0.4 | 0.170x | 4.961x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 856.1 | 851.2 | 860.8 | 3.2 | 0.993x | 28.977x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 862.2 | 843.7 | 867.5 | 8.7 | 1.000x | 29.184x |

### `factored` / `s-009` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 51.5 | 51.3 | 52.1 | 0.3 | 0.060x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 51.5 | 51.5 | 51.8 | 0.1 | 0.060x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 55.5 | 55.2 | 56.0 | 0.3 | 0.065x | 1.078x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 55.8 | 55.7 | 55.9 | 0.1 | 0.065x | 1.085x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 146.6 | 146.4 | 148.8 | 0.9 | 0.171x | 2.848x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 146.9 | 146.3 | 151.9 | 2.1 | 0.172x | 2.855x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 147.7 | 147.4 | 149.5 | 0.8 | 0.172x | 2.870x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 148.3 | 147.9 | 154.8 | 2.6 | 0.173x | 2.881x |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 150.0 | 149.6 | 150.5 | 0.3 | 0.175x | 2.914x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 856.6 | 844.6 | 860.6 | 5.8 | 1.000x | 16.643x |

### `factored` / `s-010` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.6 | 0.0 | 0.042x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.7 | 31.5 | 31.7 | 0.1 | 0.045x | 1.070x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 61.9 | 61.5 | 62.0 | 0.2 | 0.087x | 2.090x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 78.4 | 78.2 | 79.5 | 0.5 | 0.110x | 2.646x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 106.9 | 104.8 | 109.0 | 1.4 | 0.150x | 3.609x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 107.2 | 105.5 | 111.2 | 1.9 | 0.151x | 3.619x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 107.3 | 105.7 | 107.6 | 0.7 | 0.151x | 3.624x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 107.8 | 105.7 | 110.1 | 1.4 | 0.152x | 3.639x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 709.4 | 699.3 | 716.6 | 6.1 | 0.998x | 23.953x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 710.6 | 700.6 | 729.5 | 9.7 | 1.000x | 23.994x |

### `factored` / `s-010` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 51.4 | 51.4 | 51.9 | 0.2 | 0.072x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 51.5 | 51.5 | 51.9 | 0.2 | 0.072x | 1.002x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 55.6 | 55.3 | 56.0 | 0.3 | 0.078x | 1.081x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 55.6 | 55.5 | 56.0 | 0.2 | 0.078x | 1.082x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 102.1 | 102.0 | 102.2 | 0.1 | 0.143x | 1.984x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 104.1 | 103.7 | 104.5 | 0.3 | 0.146x | 2.024x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 106.8 | 106.5 | 110.4 | 1.5 | 0.150x | 2.075x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 108.1 | 107.9 | 124.0 | 6.4 | 0.152x | 2.102x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 119.3 | 118.8 | 121.0 | 0.7 | 0.168x | 2.319x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 711.7 | 707.2 | 713.7 | 2.7 | 1.000x | 13.835x |

### `factored` / `s-011` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.4 | 12.1 | 12.4 | 0.1 | 0.020x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.7 | 12.6 | 13.2 | 0.2 | 0.021x | 1.029x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 41.4 | 41.1 | 45.8 | 1.8 | 0.067x | 3.351x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 43.3 | 43.1 | 43.6 | 0.2 | 0.071x | 3.507x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 211.9 | 210.4 | 222.3 | 4.4 | 0.345x | 17.157x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 212.2 | 210.7 | 213.8 | 1.1 | 0.346x | 17.180x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 219.7 | 210.9 | 224.5 | 5.3 | 0.358x | 17.790x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 221.7 | 217.3 | 225.9 | 3.2 | 0.361x | 17.947x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 613.0 | 604.9 | 619.8 | 5.7 | 0.998x | 49.634x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 614.0 | 609.6 | 619.6 | 4.1 | 1.000x | 49.711x |

### `factored` / `s-011` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 34.6 | 34.4 | 34.9 | 0.2 | 0.007x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 34.7 | 34.5 | 35.1 | 0.2 | 0.007x | 1.002x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 34.8 | 34.7 | 35.2 | 0.2 | 0.007x | 1.005x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 34.9 | 34.4 | 36.2 | 0.6 | 0.007x | 1.010x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 437.5 | 433.9 | 442.8 | 2.9 | 0.093x | 12.649x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 2,010.4 | 1,941.6 | 2,094.4 | 50.5 | 0.427x | 58.121x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 2,023.3 | 1,942.5 | 2,060.8 | 41.9 | 0.430x | 58.492x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 2,042.4 | 1,955.5 | 2,074.6 | 42.7 | 0.434x | 59.046x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 2,052.9 | 1,953.0 | 2,178.9 | 74.7 | 0.436x | 59.349x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,704.2 | 4,663.3 | 4,709.6 | 16.7 | 1.000x | 135.996x |

### `factored` / `s-012` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.4 | 35.3 | 35.6 | 0.1 | 0.032x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.6 | 37.5 | 38.0 | 0.2 | 0.035x | 1.063x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 76.9 | 76.3 | 78.8 | 0.9 | 0.071x | 2.175x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 92.5 | 92.5 | 94.7 | 0.8 | 0.085x | 2.615x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 197.6 | 196.2 | 205.2 | 3.2 | 0.181x | 5.587x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 200.4 | 199.0 | 201.2 | 0.7 | 0.184x | 5.666x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 200.8 | 200.7 | 206.8 | 2.8 | 0.184x | 5.676x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 201.2 | 200.7 | 205.7 | 1.9 | 0.185x | 5.689x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,085.3 | 1,079.8 | 1,093.7 | 5.4 | 0.996x | 30.680x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,089.8 | 1,084.1 | 1,104.5 | 7.7 | 1.000x | 30.807x |

### `factored` / `s-012` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 65.8 | 65.6 | 66.1 | 0.2 | 0.060x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 65.9 | 65.6 | 67.8 | 0.8 | 0.060x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 69.3 | 69.0 | 70.1 | 0.4 | 0.063x | 1.053x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 69.5 | 69.0 | 71.5 | 0.8 | 0.064x | 1.057x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 172.7 | 169.9 | 178.7 | 3.0 | 0.158x | 2.625x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 200.0 | 199.9 | 202.6 | 1.1 | 0.183x | 3.039x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 204.3 | 203.7 | 215.0 | 4.3 | 0.187x | 3.106x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 206.1 | 204.9 | 206.5 | 0.6 | 0.189x | 3.132x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 209.2 | 207.5 | 226.0 | 7.0 | 0.192x | 3.180x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,091.7 | 1,091.1 | 1,095.4 | 1.7 | 1.000x | 16.593x |

### `factored` / `s-013` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.4 | 35.3 | 36.3 | 0.4 | 0.032x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.3 | 37.2 | 37.5 | 0.1 | 0.034x | 1.055x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 76.6 | 76.1 | 78.7 | 0.9 | 0.070x | 2.163x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 92.5 | 92.4 | 92.5 | 0.0 | 0.085x | 2.612x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 197.8 | 196.6 | 198.9 | 0.8 | 0.181x | 5.587x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 200.6 | 199.3 | 202.1 | 0.9 | 0.184x | 5.666x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 201.4 | 200.1 | 207.2 | 2.9 | 0.184x | 5.688x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 201.5 | 200.6 | 202.1 | 0.5 | 0.185x | 5.693x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,086.6 | 1,081.0 | 1,098.7 | 7.1 | 0.996x | 30.698x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,091.5 | 1,085.8 | 1,106.4 | 7.0 | 1.000x | 30.836x |

### `factored` / `s-013` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 65.8 | 65.8 | 66.9 | 0.4 | 0.060x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 65.9 | 65.4 | 66.1 | 0.3 | 0.060x | 1.000x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 69.0 | 68.9 | 69.2 | 0.1 | 0.063x | 1.048x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 69.3 | 69.1 | 69.5 | 0.2 | 0.063x | 1.052x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 173.3 | 169.9 | 190.3 | 7.5 | 0.157x | 2.632x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 202.0 | 200.1 | 202.4 | 1.0 | 0.183x | 3.067x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 204.1 | 203.8 | 218.7 | 5.9 | 0.185x | 3.100x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 205.8 | 204.6 | 206.9 | 0.8 | 0.187x | 3.125x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 207.1 | 206.5 | 211.3 | 1.7 | 0.188x | 3.146x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,101.9 | 1,085.5 | 1,116.5 | 11.1 | 1.000x | 16.735x |

### `factored` / `s-014` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.8 | 29.6 | 31.4 | 0.7 | 0.034x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.7 | 31.6 | 31.7 | 0.0 | 0.036x | 1.064x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 62.3 | 62.1 | 64.8 | 1.0 | 0.071x | 2.095x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 78.3 | 78.2 | 78.4 | 0.1 | 0.089x | 2.633x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 155.5 | 155.3 | 155.8 | 0.2 | 0.177x | 5.228x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 155.7 | 155.2 | 155.9 | 0.2 | 0.178x | 5.232x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 155.8 | 155.3 | 156.7 | 0.4 | 0.178x | 5.238x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 157.7 | 157.5 | 158.3 | 0.3 | 0.180x | 5.301x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 876.5 | 870.4 | 877.8 | 2.9 | 1.000x | 29.461x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 876.5 | 855.2 | 883.8 | 10.5 | 1.000x | 29.462x |

### `factored` / `s-014` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 51.4 | 51.3 | 51.6 | 0.1 | 0.059x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 51.5 | 51.4 | 52.1 | 0.3 | 0.059x | 1.002x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 55.5 | 55.4 | 55.7 | 0.1 | 0.064x | 1.079x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 55.8 | 55.6 | 55.9 | 0.1 | 0.064x | 1.086x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 154.5 | 153.8 | 167.9 | 5.8 | 0.178x | 3.007x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 157.5 | 156.9 | 159.4 | 0.9 | 0.181x | 3.066x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 162.2 | 161.6 | 162.9 | 0.5 | 0.187x | 3.158x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 162.3 | 161.3 | 164.2 | 1.0 | 0.187x | 3.159x |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 163.7 | 163.3 | 163.8 | 0.2 | 0.188x | 3.186x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 869.0 | 866.8 | 876.1 | 3.5 | 1.000x | 16.915x |

### `factored` / `s-015` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33.9 | 33.8 | 34.7 | 0.3 | 0.032x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 36.0 | 35.8 | 36.1 | 0.1 | 0.034x | 1.061x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 72.9 | 72.5 | 75.4 | 1.1 | 0.069x | 2.148x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 89.2 | 89.1 | 89.6 | 0.2 | 0.084x | 2.630x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 198.8 | 198.1 | 198.9 | 0.3 | 0.188x | 5.859x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 199.5 | 198.3 | 203.5 | 2.2 | 0.188x | 5.879x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 200.6 | 199.6 | 204.3 | 1.7 | 0.189x | 5.911x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 201.1 | 200.2 | 201.5 | 0.5 | 0.190x | 5.929x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,058.1 | 1,055.6 | 1,067.2 | 4.0 | 0.999x | 31.187x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,059.1 | 1,045.0 | 1,070.9 | 8.7 | 1.000x | 31.215x |

### `factored` / `s-015` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 62.6 | 62.3 | 62.8 | 0.2 | 0.059x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 62.6 | 62.6 | 62.8 | 0.1 | 0.059x | 1.000x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 66.0 | 65.1 | 66.6 | 0.5 | 0.062x | 1.054x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 66.0 | 65.8 | 66.4 | 0.2 | 0.062x | 1.055x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 173.9 | 172.5 | 187.3 | 5.5 | 0.164x | 2.778x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 200.6 | 199.8 | 213.4 | 5.2 | 0.190x | 3.203x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 203.2 | 203.0 | 215.2 | 4.8 | 0.192x | 3.246x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 205.1 | 204.4 | 206.1 | 0.6 | 0.194x | 3.276x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 206.2 | 205.8 | 208.7 | 1.4 | 0.195x | 3.293x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,057.6 | 1,052.2 | 1,075.9 | 8.1 | 1.000x | 16.892x |

### `factored` / `s-016` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.0 | 10.7 | 12.0 | 0.5 | 0.030x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 11.7 | 11.6 | 12.0 | 0.2 | 0.032x | 1.071x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.5 | 32.3 | 36.5 | 1.6 | 0.090x | 2.967x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.7 | 34.8 | 35.7 | 0.3 | 0.099x | 3.257x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 104.4 | 102.2 | 105.9 | 1.2 | 0.289x | 9.534x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 104.5 | 103.2 | 106.0 | 0.9 | 0.289x | 9.540x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 106.2 | 105.9 | 109.2 | 1.5 | 0.294x | 9.699x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 107.0 | 106.7 | 108.0 | 0.4 | 0.296x | 9.768x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 361.5 | 358.8 | 367.1 | 3.2 | 1.000x | 33.000x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 361.5 | 359.1 | 365.7 | 2.3 | 1.000x | 33.002x |

### `factored` / `s-016` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 26.1 | 25.8 | 26.3 | 0.2 | 0.011x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 26.2 | 26.0 | 26.3 | 0.1 | 0.011x | 1.002x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 26.2 | 26.1 | 26.3 | 0.1 | 0.011x | 1.004x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 26.2 | 26.0 | 26.8 | 0.3 | 0.011x | 1.004x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 260.4 | 257.5 | 285.8 | 10.4 | 0.109x | 9.976x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 1,450.9 | 1,411.2 | 1,533.2 | 41.2 | 0.606x | 55.591x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 1,489.8 | 1,441.9 | 1,524.2 | 34.8 | 0.622x | 57.084x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 1,495.0 | 1,423.4 | 1,531.2 | 45.1 | 0.625x | 57.281x |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 1,522.3 | 1,402.8 | 1,561.0 | 56.0 | 0.636x | 58.329x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,393.8 | 2,346.3 | 2,398.8 | 21.4 | 1.000x | 91.720x |

### `factored` / `s-017` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.4 | 35.3 | 38.3 | 1.2 | 0.032x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.5 | 37.3 | 38.0 | 0.2 | 0.034x | 1.062x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 76.8 | 76.5 | 78.1 | 0.6 | 0.070x | 2.171x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 93.3 | 92.3 | 94.1 | 0.7 | 0.085x | 2.637x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 197.9 | 197.8 | 198.8 | 0.4 | 0.181x | 5.598x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 200.7 | 200.2 | 202.8 | 1.1 | 0.184x | 5.678x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 200.9 | 200.7 | 207.2 | 2.8 | 0.184x | 5.681x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 201.0 | 200.8 | 201.6 | 0.3 | 0.184x | 5.684x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,092.0 | 1,075.6 | 1,110.4 | 11.5 | 1.000x | 30.885x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,093.3 | 1,078.6 | 1,100.6 | 7.7 | 1.001x | 30.920x |

### `factored` / `s-017` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 65.7 | 65.3 | 65.9 | 0.2 | 0.059x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 65.7 | 65.6 | 66.1 | 0.2 | 0.060x | 1.000x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 69.1 | 68.9 | 69.5 | 0.2 | 0.063x | 1.051x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 69.3 | 69.1 | 69.4 | 0.1 | 0.063x | 1.054x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 171.5 | 169.9 | 180.6 | 3.9 | 0.155x | 2.611x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 200.5 | 200.0 | 202.2 | 0.8 | 0.182x | 3.052x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 205.0 | 204.2 | 218.5 | 5.5 | 0.186x | 3.120x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 206.9 | 204.8 | 208.1 | 1.1 | 0.187x | 3.148x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 207.9 | 207.5 | 209.1 | 0.6 | 0.188x | 3.165x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,104.4 | 1,087.0 | 1,115.8 | 9.8 | 1.000x | 16.808x |

### `factored` / `s-018` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33.8 | 33.7 | 36.7 | 1.2 | 0.032x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.9 | 35.9 | 36.3 | 0.1 | 0.034x | 1.062x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 72.7 | 72.1 | 73.0 | 0.3 | 0.069x | 2.151x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 89.6 | 89.4 | 92.4 | 1.1 | 0.085x | 2.649x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 198.0 | 197.5 | 206.2 | 3.3 | 0.187x | 5.854x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 198.9 | 198.4 | 200.0 | 0.5 | 0.188x | 5.880x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 199.6 | 199.1 | 203.4 | 1.5 | 0.189x | 5.902x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 200.5 | 199.8 | 204.7 | 1.9 | 0.190x | 5.929x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,050.2 | 1,045.0 | 1,142.2 | 37.2 | 0.994x | 31.049x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,056.6 | 1,042.0 | 1,072.1 | 9.5 | 1.000x | 31.239x |

### `factored` / `s-018` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 62.6 | 62.5 | 63.1 | 0.2 | 0.059x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 62.6 | 62.6 | 62.8 | 0.1 | 0.059x | 1.000x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 65.8 | 65.8 | 66.6 | 0.3 | 0.062x | 1.051x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 66.0 | 65.8 | 66.7 | 0.3 | 0.062x | 1.054x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 173.7 | 172.5 | 179.2 | 2.6 | 0.164x | 2.774x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 200.2 | 198.8 | 223.5 | 9.5 | 0.188x | 3.197x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 204.1 | 203.1 | 214.9 | 4.5 | 0.192x | 3.258x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 205.4 | 203.8 | 205.9 | 0.8 | 0.193x | 3.280x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 208.5 | 205.4 | 210.6 | 1.7 | 0.196x | 3.329x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,062.6 | 1,053.7 | 1,101.5 | 17.1 | 1.000x | 16.964x |

### `factored` / `s-019` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.4 | 11.2 | 11.5 | 0.1 | 0.029x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 11.9 | 11.9 | 13.1 | 0.5 | 0.030x | 1.045x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 34.3 | 34.1 | 34.7 | 0.2 | 0.088x | 3.003x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 36.8 | 36.2 | 38.9 | 0.9 | 0.094x | 3.220x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 104.8 | 104.5 | 106.8 | 0.8 | 0.268x | 9.177x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 105.8 | 104.3 | 106.1 | 0.8 | 0.270x | 9.268x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 106.6 | 106.0 | 110.0 | 1.5 | 0.272x | 9.336x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 108.4 | 107.4 | 109.8 | 0.9 | 0.277x | 9.495x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 387.6 | 386.1 | 393.1 | 2.5 | 0.990x | 33.944x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 391.7 | 387.7 | 393.4 | 1.9 | 1.000x | 34.299x |

### `factored` / `s-019` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 27.6 | 27.5 | 28.7 | 0.5 | 0.011x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 27.7 | 27.6 | 28.0 | 0.1 | 0.011x | 1.003x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 28.0 | 27.9 | 28.1 | 0.0 | 0.011x | 1.015x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 28.0 | 27.8 | 28.2 | 0.1 | 0.011x | 1.016x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 267.8 | 262.6 | 269.9 | 2.6 | 0.105x | 9.704x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 1,482.2 | 1,436.9 | 1,541.4 | 43.8 | 0.584x | 53.716x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 1,521.2 | 1,406.4 | 1,546.8 | 49.7 | 0.599x | 55.132x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 1,527.8 | 1,485.2 | 1,579.5 | 31.3 | 0.602x | 55.370x |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 1,554.3 | 1,463.9 | 1,578.7 | 41.3 | 0.612x | 56.330x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,539.1 | 2,529.6 | 2,542.5 | 4.9 | 1.000x | 92.024x |

### `factored` / `s-020` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 38.3 | 38.3 | 43.4 | 2.0 | 0.035x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 41.2 | 41.1 | 41.4 | 0.1 | 0.037x | 1.074x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 83.5 | 83.4 | 84.2 | 0.3 | 0.075x | 2.179x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 100.2 | 100.0 | 101.1 | 0.4 | 0.090x | 2.612x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 220.9 | 220.8 | 222.4 | 0.6 | 0.199x | 5.762x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 223.1 | 221.5 | 223.4 | 0.7 | 0.201x | 5.819x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 224.4 | 222.8 | 225.0 | 0.8 | 0.202x | 5.854x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 225.5 | 222.4 | 230.8 | 2.9 | 0.203x | 5.882x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,109.5 | 1,105.2 | 1,117.5 | 4.4 | 1.000x | 28.935x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,117.6 | 1,107.2 | 1,135.2 | 10.4 | 1.007x | 29.147x |

### `factored` / `s-020` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 73.0 | 72.8 | 74.0 | 0.5 | 0.066x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 73.1 | 73.0 | 73.3 | 0.1 | 0.066x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 76.9 | 76.8 | 77.3 | 0.2 | 0.069x | 1.054x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 77.0 | 76.9 | 77.3 | 0.2 | 0.069x | 1.054x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 176.7 | 174.7 | 183.8 | 3.3 | 0.159x | 2.421x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 204.2 | 203.7 | 206.0 | 0.8 | 0.184x | 2.797x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 208.6 | 208.1 | 209.4 | 0.5 | 0.188x | 2.858x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 210.2 | 208.9 | 224.4 | 5.9 | 0.190x | 2.879x |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 211.3 | 210.0 | 216.5 | 2.3 | 0.191x | 2.895x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,108.0 | 1,098.4 | 1,117.9 | 7.1 | 1.000x | 15.179x |

### `factored` / `s-021` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.5 | 30.1 | 0.2 | 0.026x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.6 | 31.5 | 33.5 | 0.7 | 0.028x | 1.070x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 61.9 | 61.8 | 62.1 | 0.1 | 0.054x | 2.094x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 78.3 | 78.2 | 78.4 | 0.1 | 0.068x | 2.646x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 164.6 | 164.4 | 165.1 | 0.2 | 0.144x | 5.567x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 164.9 | 164.8 | 177.8 | 5.2 | 0.144x | 5.575x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 168.9 | 168.0 | 170.0 | 0.7 | 0.147x | 5.712x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 170.9 | 168.5 | 174.4 | 2.1 | 0.149x | 5.777x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,142.0 | 1,132.6 | 1,158.2 | 8.3 | 0.995x | 38.616x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,147.2 | 1,129.5 | 1,162.7 | 10.8 | 1.000x | 38.793x |

### `factored` / `s-021` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 51.5 | 51.4 | 51.8 | 0.2 | 0.045x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 51.6 | 51.3 | 52.7 | 0.5 | 0.045x | 1.003x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 55.4 | 55.3 | 56.3 | 0.4 | 0.049x | 1.076x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 55.7 | 55.5 | 57.9 | 0.9 | 0.049x | 1.082x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 110.5 | 108.7 | 112.4 | 1.3 | 0.097x | 2.146x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 166.2 | 166.0 | 166.3 | 0.1 | 0.146x | 3.228x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 170.2 | 170.1 | 170.3 | 0.1 | 0.149x | 3.304x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 171.5 | 171.3 | 172.5 | 0.5 | 0.150x | 3.329x |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 171.5 | 171.2 | 172.6 | 0.5 | 0.150x | 3.330x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,142.1 | 1,134.5 | 1,150.3 | 5.4 | 1.000x | 22.175x |

### `factored` / `s-022` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 41.7 | 41.4 | 41.8 | 0.1 | 0.061x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 44.8 | 44.7 | 45.1 | 0.1 | 0.065x | 1.075x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 91.4 | 91.2 | 91.7 | 0.2 | 0.133x | 2.192x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 107.1 | 106.9 | 107.3 | 0.1 | 0.156x | 2.567x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 137.4 | 137.3 | 145.8 | 3.3 | 0.201x | 3.294x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 137.7 | 137.6 | 141.0 | 1.4 | 0.201x | 3.303x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 138.3 | 137.8 | 139.2 | 0.5 | 0.202x | 3.316x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 138.4 | 138.3 | 145.8 | 3.0 | 0.202x | 3.319x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 681.7 | 672.9 | 690.6 | 6.0 | 0.995x | 16.344x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 685.0 | 680.4 | 689.8 | 3.3 | 1.000x | 16.423x |

### `factored` / `s-022` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 80.4 | 79.4 | 80.9 | 0.5 | 0.118x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 80.6 | 80.4 | 81.0 | 0.2 | 0.119x | 1.003x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 83.1 | 83.0 | 83.9 | 0.4 | 0.122x | 1.034x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 84.1 | 83.8 | 86.1 | 0.9 | 0.124x | 1.046x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 98.9 | 98.4 | 114.0 | 6.0 | 0.146x | 1.230x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 139.8 | 138.5 | 140.1 | 0.5 | 0.206x | 1.738x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 140.0 | 139.8 | 141.3 | 0.5 | 0.206x | 1.741x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 141.2 | 141.2 | 142.0 | 0.3 | 0.208x | 1.756x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 143.0 | 141.2 | 145.0 | 1.2 | 0.211x | 1.778x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 678.6 | 674.0 | 682.1 | 2.6 | 1.000x | 8.440x |

### `factored` / `s-023` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.3 | 35.3 | 35.5 | 0.1 | 0.031x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.4 | 37.2 | 37.6 | 0.1 | 0.033x | 1.058x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 76.9 | 76.9 | 77.1 | 0.1 | 0.068x | 2.177x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 92.7 | 92.5 | 93.0 | 0.2 | 0.082x | 2.624x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 165.6 | 163.9 | 165.7 | 0.7 | 0.147x | 4.685x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 166.1 | 165.8 | 178.3 | 4.9 | 0.147x | 4.700x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 169.8 | 168.5 | 172.6 | 1.4 | 0.151x | 4.804x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 170.1 | 169.6 | 172.9 | 1.2 | 0.151x | 4.812x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,123.1 | 1,113.3 | 1,151.8 | 13.2 | 0.996x | 31.775x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,127.8 | 1,117.1 | 1,186.1 | 25.1 | 1.000x | 31.908x |

### `factored` / `s-023` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 65.8 | 65.5 | 65.9 | 0.1 | 0.058x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 65.8 | 65.7 | 65.9 | 0.1 | 0.058x | 1.000x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 69.1 | 68.9 | 69.1 | 0.1 | 0.061x | 1.051x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 69.9 | 69.1 | 71.7 | 1.1 | 0.062x | 1.064x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 106.6 | 106.3 | 123.3 | 6.5 | 0.095x | 1.621x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 166.9 | 166.8 | 167.3 | 0.2 | 0.148x | 2.538x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 171.1 | 170.9 | 171.2 | 0.1 | 0.152x | 2.602x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 172.2 | 172.1 | 172.7 | 0.2 | 0.153x | 2.618x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 172.7 | 172.5 | 173.3 | 0.3 | 0.153x | 2.626x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,127.5 | 1,119.6 | 1,211.7 | 34.8 | 1.000x | 17.145x |

### `factored` / `s-024` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.6 | 31.3 | 0.7 | 0.026x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.7 | 31.6 | 32.1 | 0.2 | 0.028x | 1.070x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 62.1 | 61.7 | 62.6 | 0.3 | 0.054x | 2.097x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 78.3 | 78.1 | 78.6 | 0.1 | 0.068x | 2.643x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 168.9 | 168.6 | 173.5 | 1.8 | 0.147x | 5.703x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 169.0 | 168.8 | 169.4 | 0.2 | 0.147x | 5.705x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 172.6 | 172.5 | 174.4 | 0.7 | 0.150x | 5.828x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 172.9 | 172.7 | 175.6 | 1.3 | 0.151x | 5.838x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,142.4 | 1,139.3 | 1,155.7 | 5.8 | 0.995x | 38.574x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,148.2 | 1,139.0 | 1,152.1 | 5.1 | 1.000x | 38.767x |

### `factored` / `s-024` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 51.5 | 51.3 | 51.6 | 0.1 | 0.045x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 51.7 | 51.4 | 51.8 | 0.1 | 0.045x | 1.004x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 55.5 | 55.3 | 55.7 | 0.2 | 0.048x | 1.078x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 55.9 | 55.9 | 57.9 | 0.8 | 0.049x | 1.086x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 111.6 | 109.2 | 139.1 | 11.5 | 0.097x | 2.168x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 170.0 | 169.8 | 172.1 | 0.8 | 0.148x | 3.301x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 174.3 | 174.2 | 174.4 | 0.1 | 0.152x | 3.386x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 175.2 | 175.1 | 175.4 | 0.1 | 0.153x | 3.403x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 175.4 | 175.2 | 175.9 | 0.3 | 0.153x | 3.406x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,148.6 | 1,138.7 | 1,156.5 | 6.5 | 1.000x | 22.306x |

### `factored` / `s-025` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.4 | 35.3 | 35.5 | 0.1 | 0.031x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.4 | 37.3 | 37.6 | 0.1 | 0.033x | 1.057x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 76.6 | 76.5 | 76.8 | 0.1 | 0.067x | 2.165x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 92.4 | 92.4 | 92.7 | 0.1 | 0.081x | 2.614x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 171.3 | 171.3 | 176.1 | 1.9 | 0.151x | 4.846x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 171.6 | 171.6 | 172.2 | 0.2 | 0.151x | 4.853x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 175.7 | 175.3 | 176.3 | 0.3 | 0.155x | 4.968x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 176.0 | 175.8 | 178.1 | 0.9 | 0.155x | 4.978x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,135.1 | 1,127.2 | 1,146.0 | 6.5 | 1.000x | 32.102x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,135.4 | 1,123.8 | 1,153.5 | 10.7 | 1.000x | 32.110x |

### `factored` / `s-025` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 65.8 | 65.6 | 65.9 | 0.1 | 0.058x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 65.8 | 65.7 | 65.9 | 0.1 | 0.058x | 1.000x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 69.0 | 68.9 | 69.2 | 0.1 | 0.061x | 1.049x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 69.6 | 69.1 | 73.1 | 1.6 | 0.061x | 1.058x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 108.8 | 106.7 | 136.0 | 13.8 | 0.096x | 1.655x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 172.3 | 172.1 | 173.8 | 0.6 | 0.151x | 2.621x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 176.7 | 176.4 | 179.6 | 1.2 | 0.155x | 2.686x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 177.9 | 177.4 | 178.2 | 0.2 | 0.156x | 2.705x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 178.3 | 173.8 | 178.5 | 1.8 | 0.157x | 2.711x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,138.6 | 1,124.2 | 1,154.3 | 10.0 | 1.000x | 17.313x |

### `factored` / `s-026` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 41.7 | 41.5 | 41.9 | 0.1 | 0.061x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 44.9 | 44.7 | 46.7 | 0.8 | 0.066x | 1.077x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 91.4 | 91.3 | 91.7 | 0.1 | 0.135x | 2.195x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 107.1 | 107.0 | 107.3 | 0.1 | 0.158x | 2.571x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 138.2 | 137.3 | 141.3 | 1.8 | 0.204x | 3.317x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 138.2 | 137.3 | 138.9 | 0.5 | 0.204x | 3.317x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 138.2 | 136.9 | 145.2 | 3.1 | 0.204x | 3.317x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 138.4 | 138.0 | 146.6 | 3.3 | 0.204x | 3.323x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 675.5 | 673.1 | 680.0 | 2.7 | 0.995x | 16.214x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 678.8 | 677.4 | 680.5 | 1.1 | 1.000x | 16.293x |

### `factored` / `s-026` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 80.4 | 80.2 | 81.4 | 0.4 | 0.118x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 80.5 | 80.4 | 81.0 | 0.2 | 0.119x | 1.002x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 83.7 | 83.2 | 84.2 | 0.4 | 0.123x | 1.041x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 84.2 | 83.8 | 86.3 | 0.9 | 0.124x | 1.048x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 99.8 | 98.3 | 119.9 | 8.2 | 0.147x | 1.241x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 139.9 | 138.8 | 150.7 | 4.4 | 0.206x | 1.739x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 140.1 | 139.9 | 140.5 | 0.2 | 0.206x | 1.742x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 141.2 | 141.0 | 141.6 | 0.2 | 0.208x | 1.756x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 142.6 | 141.3 | 142.8 | 0.6 | 0.210x | 1.773x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 679.4 | 676.5 | 680.0 | 1.3 | 1.000x | 8.449x |

### `factored` / `s-027` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 41.7 | 41.6 | 41.8 | 0.1 | 0.039x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 44.7 | 44.6 | 48.1 | 1.3 | 0.042x | 1.071x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 91.4 | 91.2 | 91.5 | 0.1 | 0.085x | 2.189x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 107.3 | 107.1 | 107.4 | 0.1 | 0.100x | 2.570x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 166.6 | 165.7 | 167.2 | 0.5 | 0.156x | 3.992x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 167.3 | 166.8 | 188.1 | 8.7 | 0.157x | 4.008x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 170.9 | 169.9 | 173.2 | 1.2 | 0.160x | 4.095x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 174.0 | 170.7 | 174.4 | 1.4 | 0.163x | 4.168x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,068.9 | 1,056.7 | 1,088.2 | 11.0 | 1.000x | 25.604x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,072.8 | 1,066.2 | 1,086.5 | 7.3 | 1.004x | 25.698x |

### `factored` / `s-027` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 80.6 | 80.1 | 80.8 | 0.2 | 0.075x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 81.1 | 80.6 | 82.9 | 0.9 | 0.075x | 1.006x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 83.6 | 83.1 | 84.8 | 0.6 | 0.078x | 1.038x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 83.9 | 83.8 | 85.9 | 0.8 | 0.078x | 1.041x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 105.4 | 103.6 | 118.1 | 5.4 | 0.098x | 1.308x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 167.8 | 167.4 | 170.9 | 1.3 | 0.156x | 2.082x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 171.7 | 171.6 | 172.0 | 0.1 | 0.160x | 2.131x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 173.2 | 173.0 | 173.5 | 0.2 | 0.161x | 2.150x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 173.5 | 173.2 | 173.9 | 0.3 | 0.161x | 2.153x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,074.5 | 1,068.1 | 1,075.9 | 2.8 | 1.000x | 13.335x |

### `factored` / `s-028` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.5 | 0.1 | 0.017x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.2 | 14.2 | 0.4 | 0.017x | 1.009x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 26.9 | 26.8 | 27.7 | 0.4 | 0.034x | 2.031x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.5 | 31.9 | 34.0 | 0.7 | 0.042x | 2.529x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 180.4 | 179.0 | 203.8 | 9.9 | 0.229x | 13.641x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 185.8 | 181.2 | 197.1 | 6.7 | 0.235x | 14.049x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 192.7 | 180.9 | 196.0 | 5.3 | 0.244x | 14.571x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 193.1 | 191.5 | 195.9 | 1.6 | 0.245x | 14.598x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 782.7 | 780.6 | 788.7 | 3.0 | 0.992x | 59.173x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 789.2 | 776.6 | 792.3 | 6.3 | 1.000x | 59.667x |

### `factored` / `s-028` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 22.1 | 22.1 | 22.3 | 0.1 | 0.008x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 22.1 | 22.0 | 22.3 | 0.1 | 0.008x | 1.001x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 22.4 | 22.2 | 23.1 | 0.3 | 0.008x | 1.014x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 22.5 | 22.2 | 22.7 | 0.2 | 0.008x | 1.015x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 218.3 | 212.4 | 223.3 | 4.1 | 0.082x | 9.864x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 918.3 | 859.3 | 986.9 | 42.1 | 0.344x | 41.499x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 933.1 | 887.7 | 976.1 | 35.2 | 0.349x | 42.165x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 950.6 | 867.0 | 1,019.5 | 51.5 | 0.356x | 42.957x |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 1,077.8 | 917.6 | 1,230.1 | 124.7 | 0.403x | 48.704x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,671.9 | 2,658.4 | 2,684.8 | 8.7 | 1.000x | 120.741x |

### `factored` / `s-029` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.1 | 0.017x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.4 | 0.0 | 0.017x | 1.008x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 51.1 | 50.7 | 51.6 | 0.3 | 0.066x | 3.857x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 53.5 | 53.4 | 53.7 | 0.1 | 0.069x | 4.034x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 181.4 | 177.8 | 193.7 | 6.5 | 0.233x | 13.687x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 184.3 | 182.3 | 198.3 | 6.7 | 0.237x | 13.902x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 190.6 | 181.3 | 197.2 | 5.8 | 0.245x | 14.381x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 195.2 | 190.5 | 197.0 | 2.4 | 0.251x | 14.726x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 778.2 | 775.3 | 788.2 | 5.8 | 1.000x | 58.709x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 784.4 | 780.4 | 788.4 | 2.8 | 1.008x | 59.179x |

### `factored` / `s-029` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 45.5 | 45.3 | 45.6 | 0.1 | 0.017x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 45.5 | 45.1 | 45.6 | 0.2 | 0.017x | 1.000x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 45.5 | 45.3 | 45.8 | 0.2 | 0.017x | 1.001x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 45.6 | 45.4 | 45.7 | 0.1 | 0.017x | 1.002x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 233.2 | 230.4 | 233.9 | 1.4 | 0.087x | 5.130x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,668.0 | 2,665.2 | 2,672.7 | 2.6 | 1.000x | 58.697x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 3,198.1 | 3,148.9 | 3,471.1 | 122.4 | 1.199x | 70.360x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 3,209.7 | 3,174.7 | 3,416.6 | 90.8 | 1.203x | 70.614x |
| 9 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 3,290.1 | 3,163.7 | 3,408.8 | 79.1 | 1.233x | 72.383x |
| 10 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 3,299.0 | 3,230.5 | 3,365.9 | 50.6 | 1.237x | 72.580x |

### `factored` / `s-030` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 0.017x | 1.012x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 26.8 | 26.7 | 27.1 | 0.1 | 0.034x | 2.030x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.2 | 31.6 | 34.6 | 1.3 | 0.041x | 2.442x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 182.2 | 181.5 | 198.0 | 6.5 | 0.234x | 13.810x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 190.4 | 182.0 | 192.3 | 3.8 | 0.245x | 14.430x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 192.6 | 179.5 | 197.0 | 7.4 | 0.247x | 14.596x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 196.1 | 189.3 | 199.2 | 3.3 | 0.252x | 14.862x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 778.6 | 773.8 | 786.2 | 4.8 | 1.000x | 59.011x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 780.5 | 774.3 | 782.8 | 3.0 | 1.002x | 59.157x |

### `factored` / `s-030` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 22.1 | 22.0 | 22.6 | 0.2 | 0.008x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 22.2 | 22.1 | 22.3 | 0.1 | 0.008x | 1.005x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 22.3 | 22.2 | 22.4 | 0.1 | 0.008x | 1.009x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 22.4 | 22.3 | 22.4 | 0.0 | 0.008x | 1.011x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 217.4 | 212.2 | 220.1 | 2.6 | 0.081x | 9.832x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 828.9 | 823.8 | 896.2 | 27.0 | 0.311x | 37.489x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 829.1 | 774.7 | 1,003.1 | 99.3 | 0.311x | 37.497x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 905.8 | 851.2 | 936.6 | 30.6 | 0.340x | 40.964x |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 910.3 | 823.4 | 931.5 | 40.0 | 0.341x | 41.169x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,667.8 | 2,658.8 | 2,676.2 | 6.6 | 1.000x | 120.652x |

### `factored` / `s-031` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.1 | 0.017x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.4 | 0.0 | 0.017x | 1.012x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.5 | 35.3 | 35.6 | 0.1 | 0.045x | 2.684x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 38.6 | 38.0 | 39.8 | 0.7 | 0.049x | 2.921x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 180.3 | 178.0 | 194.1 | 7.1 | 0.231x | 13.652x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 183.4 | 181.0 | 198.7 | 7.3 | 0.235x | 13.885x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 194.9 | 190.8 | 199.2 | 3.1 | 0.250x | 14.757x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 195.5 | 179.9 | 199.0 | 6.8 | 0.251x | 14.802x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 780.1 | 771.7 | 789.1 | 5.6 | 1.000x | 59.059x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 780.2 | 775.2 | 782.9 | 2.9 | 1.000x | 59.063x |

### `factored` / `s-031` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 29.6 | 29.4 | 29.9 | 0.2 | 0.011x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 29.7 | 29.3 | 29.8 | 0.2 | 0.011x | 1.003x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 29.8 | 29.6 | 30.0 | 0.2 | 0.011x | 1.006x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 29.8 | 29.6 | 29.9 | 0.1 | 0.011x | 1.006x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 234.8 | 233.4 | 236.4 | 1.1 | 0.088x | 7.934x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 1,378.1 | 1,328.7 | 1,454.5 | 43.4 | 0.517x | 46.573x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 1,386.0 | 1,348.3 | 1,480.6 | 47.7 | 0.519x | 46.840x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 1,393.8 | 1,329.8 | 1,477.1 | 53.3 | 0.522x | 47.106x |
| 9 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 1,410.4 | 1,286.5 | 1,470.4 | 71.5 | 0.529x | 47.667x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,668.1 | 2,652.9 | 2,677.5 | 8.6 | 1.000x | 90.170x |

### `factored` / `s-032` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.2 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.2 | 16.2 | 16.4 | 0.1 | 0.017x | 1.008x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 31.5 | 31.3 | 32.0 | 0.3 | 0.034x | 1.961x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 36.9 | 36.3 | 38.1 | 0.7 | 0.040x | 2.293x |
| 5 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 290.5 | 278.0 | 306.0 | 9.7 | 0.312x | 18.053x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 299.4 | 259.8 | 308.8 | 18.9 | 0.322x | 18.605x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 301.8 | 244.4 | 319.0 | 26.0 | 0.325x | 18.758x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 301.9 | 287.5 | 316.4 | 9.4 | 0.325x | 18.761x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 929.9 | 921.1 | 931.0 | 3.7 | 1.000x | 57.794x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 931.6 | 912.3 | 954.0 | 15.3 | 1.002x | 57.899x |

### `factored` / `s-032` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 26.2 | 26.1 | 26.5 | 0.1 | 0.008x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 26.3 | 26.2 | 26.4 | 0.1 | 0.008x | 1.004x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 26.3 | 26.1 | 26.8 | 0.2 | 0.008x | 1.006x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 26.4 | 26.0 | 27.0 | 0.3 | 0.008x | 1.009x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 329.6 | 319.7 | 358.8 | 13.7 | 0.101x | 12.594x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 1,721.8 | 1,707.1 | 1,733.0 | 10.0 | 0.527x | 65.797x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 1,727.5 | 1,726.3 | 1,747.3 | 8.0 | 0.529x | 66.013x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 1,727.9 | 1,700.1 | 1,756.2 | 18.5 | 0.529x | 66.029x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 1,737.2 | 1,731.0 | 1,756.0 | 9.9 | 0.532x | 66.386x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,265.4 | 3,252.7 | 3,277.9 | 8.8 | 1.000x | 124.783x |

### `factored` / `s-033` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.0 | 16.0 | 16.7 | 0.3 | 0.018x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.1 | 0.0 | 0.018x | 1.002x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 31.2 | 31.1 | 31.7 | 0.2 | 0.036x | 1.947x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.7 | 36.6 | 38.1 | 0.6 | 0.043x | 2.351x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 273.4 | 220.9 | 322.5 | 35.2 | 0.312x | 17.038x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 283.8 | 216.0 | 311.5 | 34.3 | 0.324x | 17.686x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 302.2 | 259.0 | 309.6 | 20.2 | 0.345x | 18.836x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 310.4 | 253.6 | 335.2 | 27.8 | 0.354x | 19.346x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 868.4 | 866.0 | 876.2 | 3.6 | 0.991x | 54.120x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 876.0 | 869.2 | 913.3 | 16.4 | 1.000x | 54.596x |

### `factored` / `s-033` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 26.0 | 25.9 | 26.2 | 0.1 | 0.009x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 26.0 | 25.9 | 26.8 | 0.4 | 0.009x | 1.002x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 26.2 | 26.0 | 26.3 | 0.1 | 0.009x | 1.008x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 26.2 | 26.0 | 26.3 | 0.1 | 0.009x | 1.009x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 329.3 | 322.6 | 338.5 | 5.9 | 0.109x | 12.690x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 1,724.5 | 1,714.5 | 1,741.8 | 10.9 | 0.568x | 66.447x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 1,725.9 | 1,704.1 | 1,740.4 | 12.8 | 0.569x | 66.505x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 1,727.7 | 1,700.9 | 1,734.6 | 11.7 | 0.569x | 66.572x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 1,733.3 | 1,727.0 | 1,746.3 | 7.2 | 0.571x | 66.790x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,035.3 | 3,017.2 | 3,045.8 | 9.4 | 1.000x | 116.957x |

### `factored` / `s-034` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.2 | 20.2 | 20.3 | 0.0 | 0.016x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 20.3 | 20.2 | 20.3 | 0.1 | 0.016x | 1.002x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 23.3 | 23.3 | 23.4 | 0.0 | 0.019x | 1.152x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 27.7 | 27.2 | 29.7 | 1.0 | 0.022x | 1.369x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 146.3 | 146.2 | 147.3 | 0.4 | 0.116x | 7.227x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 146.4 | 145.7 | 147.8 | 0.7 | 0.116x | 7.235x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 148.4 | 146.5 | 151.3 | 1.6 | 0.118x | 7.333x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 148.8 | 146.6 | 150.3 | 1.2 | 0.118x | 7.352x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,247.0 | 1,238.1 | 1,258.5 | 7.2 | 0.992x | 61.605x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,257.1 | 1,246.9 | 1,270.4 | 8.5 | 1.000x | 62.107x |

### `factored` / `s-034` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.9 | 18.9 | 19.3 | 0.2 | 0.004x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 19.2 | 19.0 | 19.2 | 0.1 | 0.004x | 1.012x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 19.2 | 19.0 | 19.4 | 0.1 | 0.004x | 1.012x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 19.2 | 19.2 | 19.3 | 0.1 | 0.004x | 1.015x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 390.2 | 382.9 | 395.4 | 4.8 | 0.084x | 20.620x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 610.1 | 601.2 | 734.6 | 50.2 | 0.132x | 32.236x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 636.1 | 599.5 | 741.2 | 49.5 | 0.137x | 33.612x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 641.5 | 628.2 | 659.3 | 11.3 | 0.138x | 33.894x |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 651.3 | 625.0 | 661.0 | 13.3 | 0.140x | 34.413x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,637.2 | 4,607.8 | 4,686.2 | 26.4 | 1.000x | 245.029x |

### `factored` / `s-035` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.0 | 23.0 | 23.2 | 0.1 | 0.015x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.0 | 24.4 | 0.5 | 0.015x | 1.003x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 30.6 | 29.9 | 30.7 | 0.3 | 0.019x | 1.328x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.6 | 33.1 | 35.3 | 0.8 | 0.021x | 1.462x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 382.7 | 381.3 | 487.7 | 49.1 | 0.242x | 16.626x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 397.8 | 384.2 | 488.1 | 47.4 | 0.251x | 17.282x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 480.1 | 473.9 | 487.4 | 4.7 | 0.303x | 20.857x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 485.8 | 382.2 | 489.3 | 41.2 | 0.307x | 21.107x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,579.1 | 1,564.6 | 1,590.0 | 9.1 | 0.998x | 68.604x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,583.0 | 1,564.5 | 1,624.2 | 20.8 | 1.000x | 68.774x |

### `factored` / `s-035` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 25.2 | 25.2 | 25.3 | 0.1 | 0.004x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 25.3 | 25.3 | 25.4 | 0.0 | 0.004x | 1.005x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 25.3 | 25.2 | 25.8 | 0.2 | 0.004x | 1.005x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 25.4 | 25.3 | 25.7 | 0.1 | 0.004x | 1.008x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 489.1 | 483.0 | 515.8 | 11.6 | 0.083x | 19.393x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 1,759.2 | 1,757.0 | 1,764.3 | 3.0 | 0.298x | 69.757x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 1,764.6 | 1,759.8 | 1,788.6 | 10.6 | 0.298x | 69.972x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 1,769.3 | 1,764.2 | 2,014.6 | 98.1 | 0.299x | 70.156x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 1,771.9 | 1,762.2 | 1,787.2 | 10.2 | 0.300x | 70.260x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 5,913.1 | 5,856.0 | 5,923.7 | 24.1 | 1.000x | 234.471x |

### `factored` / `s-036` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.3 | 12.0 | 12.5 | 0.2 | 0.020x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.7 | 12.4 | 13.3 | 0.3 | 0.020x | 1.030x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33.1 | 33.0 | 33.4 | 0.2 | 0.053x | 2.686x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.0 | 34.6 | 37.0 | 0.8 | 0.056x | 2.845x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.7 | 144.9 | 147.5 | 0.9 | 0.232x | 11.830x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.8 | 144.3 | 146.9 | 0.9 | 0.232x | 11.845x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 147.5 | 147.0 | 148.7 | 0.7 | 0.235x | 11.977x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 149.3 | 148.4 | 150.8 | 0.9 | 0.238x | 12.122x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 627.7 | 625.8 | 634.8 | 4.0 | 1.000x | 50.976x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 627.9 | 624.7 | 632.2 | 2.5 | 1.000x | 50.993x |

### `factored` / `s-036` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 26.9 | 26.8 | 27.1 | 0.1 | 0.013x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 26.9 | 26.8 | 27.3 | 0.2 | 0.013x | 1.000x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 27.0 | 26.8 | 27.0 | 0.1 | 0.013x | 1.003x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 27.1 | 26.9 | 27.8 | 0.3 | 0.013x | 1.006x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 195.2 | 194.3 | 196.1 | 0.6 | 0.094x | 7.257x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 1,488.9 | 1,447.8 | 1,598.8 | 55.6 | 0.716x | 55.358x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 1,512.7 | 1,428.6 | 1,546.2 | 39.6 | 0.727x | 56.246x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 1,547.8 | 1,517.1 | 1,571.5 | 19.8 | 0.744x | 57.548x |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 1,567.8 | 1,535.4 | 1,665.5 | 47.1 | 0.754x | 58.293x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,080.3 | 2,064.7 | 2,085.9 | 7.3 | 1.000x | 77.350x |

### `factored` / `s-037` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 14.6 | 14.4 | 14.8 | 0.1 | 0.017x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.8 | 14.5 | 15.0 | 0.2 | 0.018x | 1.013x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 26.9 | 26.7 | 27.3 | 0.2 | 0.032x | 1.841x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 30.6 | 30.3 | 33.2 | 1.1 | 0.036x | 2.092x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 210.6 | 209.8 | 221.3 | 4.4 | 0.250x | 14.415x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 214.0 | 211.9 | 214.7 | 1.0 | 0.254x | 14.646x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 218.4 | 217.3 | 223.1 | 2.1 | 0.259x | 14.951x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 221.3 | 220.7 | 223.7 | 1.1 | 0.263x | 15.149x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 842.6 | 837.7 | 842.7 | 2.0 | 1.000x | 57.681x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 843.1 | 839.4 | 844.0 | 1.6 | 1.001x | 57.715x |

### `factored` / `s-037` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 20.9 | 20.8 | 21.2 | 0.2 | 0.007x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 21.0 | 20.7 | 21.4 | 0.2 | 0.007x | 1.005x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 21.1 | 20.8 | 21.5 | 0.3 | 0.007x | 1.010x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 21.1 | 20.9 | 21.2 | 0.1 | 0.007x | 1.011x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 287.4 | 277.0 | 351.2 | 27.5 | 0.099x | 13.750x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 1,306.0 | 1,246.3 | 1,339.8 | 34.5 | 0.449x | 62.476x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 1,323.5 | 1,319.3 | 1,346.8 | 9.9 | 0.455x | 63.314x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 1,326.9 | 1,307.9 | 1,331.9 | 10.0 | 0.456x | 63.474x |
| 9 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 1,341.5 | 1,299.8 | 1,344.2 | 16.8 | 0.461x | 64.173x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,908.5 | 2,906.4 | 2,973.5 | 25.8 | 1.000x | 139.136x |

### `factored` / `s-038` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.1 | 0.0 | 0.023x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.1 | 33.2 | 4.0 | 0.023x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.9 | 32.6 | 33.2 | 0.2 | 0.033x | 1.423x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.2 | 34.7 | 36.2 | 0.5 | 0.035x | 1.524x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 460.4 | 435.3 | 488.3 | 18.6 | 0.459x | 19.936x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 477.1 | 472.9 | 498.9 | 9.6 | 0.475x | 20.662x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 481.3 | 454.3 | 498.7 | 14.2 | 0.479x | 20.841x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 490.6 | 476.9 | 498.5 | 8.7 | 0.489x | 21.246x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,001.8 | 994.9 | 1,009.4 | 5.6 | 0.998x | 43.381x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,003.8 | 995.2 | 1,010.5 | 4.9 | 1.000x | 43.469x |

### `factored` / `s-038` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 26.8 | 26.7 | 27.3 | 0.2 | 0.007x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 27.0 | 26.8 | 27.0 | 0.1 | 0.008x | 1.007x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 27.0 | 26.9 | 27.7 | 0.3 | 0.008x | 1.009x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 27.1 | 27.0 | 27.3 | 0.1 | 0.008x | 1.010x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 570.5 | 563.7 | 670.8 | 40.5 | 0.159x | 21.287x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 2,794.8 | 2,743.6 | 2,829.0 | 31.8 | 0.779x | 104.290x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 2,870.5 | 2,835.7 | 2,893.0 | 19.9 | 0.800x | 107.115x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 2,876.1 | 2,855.0 | 2,988.6 | 57.0 | 0.802x | 107.323x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 2,887.0 | 2,874.1 | 2,992.0 | 44.4 | 0.805x | 107.732x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,587.8 | 3,562.6 | 3,614.0 | 18.2 | 1.000x | 133.881x |

### `factored` / `s-039` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.3 | 11.2 | 11.6 | 0.1 | 0.030x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.0 | 11.8 | 12.1 | 0.1 | 0.031x | 1.059x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 66.3 | 66.2 | 67.1 | 0.3 | 0.174x | 5.856x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 66.6 | 66.5 | 66.8 | 0.1 | 0.175x | 5.885x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 104.1 | 102.7 | 105.3 | 1.0 | 0.273x | 9.195x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 105.1 | 100.6 | 106.0 | 1.9 | 0.276x | 9.285x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 105.7 | 104.2 | 109.1 | 1.8 | 0.277x | 9.336x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 106.3 | 104.7 | 107.1 | 0.8 | 0.279x | 9.389x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 378.3 | 373.1 | 381.3 | 2.7 | 0.993x | 33.426x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 381.0 | 378.4 | 384.2 | 2.1 | 1.000x | 33.659x |

### `factored` / `s-039` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 59.0 | 58.9 | 59.1 | 0.1 | 0.038x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 59.1 | 58.9 | 59.2 | 0.1 | 0.038x | 1.002x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 62.3 | 62.1 | 63.7 | 0.6 | 0.040x | 1.055x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 62.5 | 62.3 | 62.7 | 0.2 | 0.040x | 1.060x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 216.1 | 209.3 | 227.8 | 6.2 | 0.140x | 3.663x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 298.0 | 296.9 | 298.8 | 0.8 | 0.193x | 5.051x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 299.1 | 298.8 | 299.7 | 0.3 | 0.193x | 5.071x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 299.2 | 296.1 | 299.5 | 1.4 | 0.194x | 5.073x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 302.0 | 301.2 | 302.6 | 0.5 | 0.195x | 5.120x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,546.0 | 1,539.3 | 1,559.6 | 6.8 | 1.000x | 26.210x |

### `factored` / `s-040` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 26.0 | 26.7 | 0.2 | 0.772x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 26.0 | 26.2 | 0.1 | 0.772x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 30.1 | 29.7 | 30.7 | 0.3 | 0.890x | 1.153x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.2 | 32.7 | 34.6 | 0.7 | 0.982x | 1.272x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 33.8 | 32.7 | 35.2 | 0.9 | 1.000x | 1.296x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 34.7 | 33.5 | 35.2 | 0.7 | 1.028x | 1.332x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 254.6 | 252.9 | 261.6 | 3.1 | 7.536x | 9.766x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 255.4 | 254.3 | 256.1 | 0.7 | 7.561x | 9.798x |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 256.9 | 255.5 | 270.1 | 5.6 | 7.604x | 9.854x |
| 10 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 257.1 | 256.3 | 257.2 | 0.3 | 7.609x | 9.860x |

### `factored` / `s-040` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 23.7 | 23.6 | 23.9 | 0.1 | 0.680x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 23.7 | 23.7 | 23.9 | 0.1 | 0.682x | 1.003x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 23.8 | 23.7 | 23.9 | 0.1 | 0.684x | 1.006x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 23.9 | 23.7 | 24.4 | 0.2 | 0.687x | 1.010x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 34.8 | 34.0 | 35.3 | 0.5 | 1.000x | 1.470x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.4 | 44.3 | 50.2 | 2.3 | 1.275x | 1.874x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 1,774.8 | 1,640.9 | 1,831.3 | 67.0 | 50.992x | 74.960x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 1,785.1 | 1,780.5 | 1,857.7 | 29.1 | 51.288x | 75.395x |
| 9 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 1,797.3 | 1,710.0 | 1,833.1 | 43.4 | 51.641x | 75.913x |
| 10 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 1,852.9 | 1,741.1 | 1,875.7 | 49.8 | 53.237x | 78.259x |

### `factored` / `s-041` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.063x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.6 | 10.5 | 10.7 | 0.1 | 0.066x | 1.038x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 27.4 | 25.5 | 28.5 | 1.0 | 0.169x | 2.676x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.4 | 29.2 | 31.7 | 0.9 | 0.182x | 2.874x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 48.0 | 47.7 | 48.5 | 0.2 | 0.297x | 4.694x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 48.1 | 47.3 | 48.2 | 0.3 | 0.297x | 4.701x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 49.4 | 49.3 | 49.6 | 0.1 | 0.305x | 4.833x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 49.7 | 48.9 | 49.9 | 0.4 | 0.307x | 4.861x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 161.9 | 158.6 | 169.0 | 3.4 | 1.000x | 15.828x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 163.4 | 162.2 | 164.9 | 1.1 | 1.010x | 15.979x |

### `factored` / `s-041` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.6 | 18.6 | 18.7 | 0.1 | 0.104x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.8 | 18.8 | 18.8 | 0.0 | 0.105x | 1.008x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.9 | 18.3 | 19.3 | 0.4 | 0.106x | 1.014x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 20.0 | 19.1 | 20.3 | 0.4 | 0.112x | 1.072x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 54.9 | 54.7 | 64.6 | 3.9 | 0.307x | 2.949x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 178.7 | 176.6 | 180.1 | 1.2 | 1.000x | 9.594x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 939.1 | 884.8 | 1,039.9 | 50.2 | 5.256x | 50.426x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 963.0 | 918.1 | 1,003.8 | 29.0 | 5.390x | 51.711x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 964.0 | 900.9 | 1,018.0 | 44.3 | 5.396x | 51.767x |
| 10 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 1,019.2 | 905.3 | 1,054.6 | 55.8 | 5.705x | 54.730x |

### `factored` / `s-042` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.9 | 12.8 | 13.1 | 0.1 | 0.021x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.5 | 13.4 | 13.7 | 0.1 | 0.022x | 1.049x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 19.6 | 18.6 | 20.4 | 0.7 | 0.032x | 1.522x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.1 | 20.1 | 22.3 | 0.8 | 0.033x | 1.561x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 97.9 | 73.8 | 99.6 | 12.2 | 0.159x | 7.590x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 98.3 | 74.0 | 99.0 | 9.8 | 0.160x | 7.624x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 99.4 | 97.0 | 101.5 | 1.5 | 0.162x | 7.709x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 99.7 | 98.4 | 100.1 | 0.6 | 0.162x | 7.733x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 613.6 | 603.0 | 617.1 | 4.9 | 1.000x | 47.588x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 613.6 | 608.7 | 617.2 | 3.0 | 1.000x | 47.593x |

### `factored` / `s-042` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 11.7 | 11.5 | 11.8 | 0.1 | 0.019x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 12.1 | 11.9 | 12.2 | 0.1 | 0.020x | 1.040x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 12.5 | 12.4 | 12.5 | 0.0 | 0.020x | 1.073x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 13.9 | 12.5 | 15.1 | 0.9 | 0.023x | 1.195x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 84.0 | 83.4 | 112.7 | 11.3 | 0.136x | 7.207x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 169.7 | 168.5 | 172.2 | 1.2 | 0.275x | 14.568x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 173.9 | 168.7 | 177.6 | 3.5 | 0.281x | 14.923x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 174.0 | 171.0 | 176.5 | 1.9 | 0.281x | 14.934x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 175.8 | 174.4 | 180.7 | 2.3 | 0.284x | 15.086x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 618.4 | 608.7 | 628.7 | 7.1 | 1.000x | 53.070x |

### `factored` / `s-043` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.2 | 12.0 | 12.3 | 0.1 | 0.021x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.8 | 12.6 | 13.3 | 0.2 | 0.022x | 1.055x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 78.6 | 78.3 | 78.9 | 0.2 | 0.137x | 6.459x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 78.7 | 78.5 | 79.1 | 0.2 | 0.137x | 6.472x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.5 | 144.8 | 147.8 | 1.0 | 0.253x | 11.968x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 146.9 | 142.9 | 147.9 | 1.8 | 0.256x | 12.079x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 147.9 | 147.7 | 150.0 | 0.9 | 0.257x | 12.165x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 149.3 | 146.8 | 150.2 | 1.2 | 0.260x | 12.274x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 574.8 | 571.0 | 579.0 | 2.7 | 1.000x | 47.271x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 578.5 | 570.2 | 580.2 | 4.1 | 1.006x | 47.570x |

### `factored` / `s-043` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 71.2 | 71.2 | 71.3 | 0.0 | 0.026x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 71.3 | 71.2 | 71.9 | 0.2 | 0.026x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 73.7 | 73.7 | 74.3 | 0.2 | 0.026x | 1.034x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 73.8 | 73.8 | 74.3 | 0.2 | 0.026x | 1.036x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 290.7 | 286.6 | 300.4 | 4.6 | 0.104x | 4.081x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 718.6 | 689.5 | 735.1 | 18.5 | 0.258x | 10.086x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 730.0 | 726.2 | 745.3 | 6.7 | 0.262x | 10.246x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 731.5 | 680.5 | 742.5 | 27.1 | 0.262x | 10.267x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 740.4 | 730.9 | 802.2 | 26.6 | 0.266x | 10.392x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,787.0 | 2,767.6 | 2,824.4 | 21.2 | 1.000x | 39.116x |

### `factored` / `s-044` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.3 | 0.1 | 0.062x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.3 | 10.6 | 0.1 | 0.064x | 1.028x |
| 3 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 47.9 | 47.6 | 48.4 | 0.2 | 0.295x | 4.728x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 48.1 | 47.9 | 48.3 | 0.1 | 0.296x | 4.747x |
| 5 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 49.3 | 49.0 | 49.6 | 0.2 | 0.303x | 4.866x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 49.7 | 48.6 | 50.1 | 0.5 | 0.305x | 4.898x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 67.5 | 67.3 | 67.9 | 0.3 | 0.415x | 6.652x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 68.6 | 66.9 | 68.7 | 0.7 | 0.422x | 6.760x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 162.6 | 159.2 | 167.1 | 2.9 | 1.000x | 16.038x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 162.7 | 159.9 | 163.6 | 1.4 | 1.001x | 16.046x |

### `factored` / `s-044` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 61.8 | 61.8 | 62.1 | 0.1 | 0.061x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 62.3 | 62.0 | 62.8 | 0.3 | 0.061x | 1.007x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 64.2 | 64.1 | 64.5 | 0.2 | 0.063x | 1.038x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 64.2 | 64.1 | 64.7 | 0.2 | 0.063x | 1.039x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 159.3 | 158.2 | 164.3 | 2.3 | 0.157x | 2.577x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 162.9 | 162.6 | 163.6 | 0.3 | 0.161x | 2.636x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 163.9 | 162.9 | 164.8 | 0.7 | 0.162x | 2.651x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 170.9 | 170.6 | 171.5 | 0.3 | 0.169x | 2.765x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 172.1 | 171.8 | 172.3 | 0.2 | 0.170x | 2.784x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,013.0 | 1,003.7 | 1,018.0 | 6.1 | 1.000x | 16.386x |

### `factored` / `s-045` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.1 | 12.0 | 12.4 | 0.2 | 0.021x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.7 | 12.6 | 12.8 | 0.1 | 0.022x | 1.052x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 31.8 | 31.6 | 32.4 | 0.3 | 0.055x | 2.638x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.6 | 36.6 | 39.5 | 1.0 | 0.065x | 3.115x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.6 | 144.8 | 148.0 | 1.2 | 0.252x | 12.068x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 147.3 | 145.8 | 147.7 | 0.7 | 0.255x | 12.210x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 147.8 | 146.9 | 148.4 | 0.6 | 0.256x | 12.249x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 148.0 | 147.7 | 149.4 | 0.7 | 0.256x | 12.266x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 576.8 | 569.9 | 582.7 | 4.4 | 1.000x | 47.823x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 577.7 | 570.9 | 580.6 | 3.4 | 1.001x | 47.893x |

### `factored` / `s-045` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 25.5 | 25.5 | 26.0 | 0.2 | 0.013x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 25.6 | 25.5 | 26.2 | 0.2 | 0.013x | 1.003x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 25.7 | 25.6 | 26.2 | 0.2 | 0.013x | 1.004x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 25.9 | 25.7 | 26.2 | 0.2 | 0.013x | 1.016x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 199.0 | 194.1 | 201.6 | 2.6 | 0.100x | 7.787x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 1,392.4 | 1,362.1 | 1,625.6 | 96.9 | 0.700x | 54.498x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 1,403.3 | 1,279.4 | 1,534.9 | 87.2 | 0.706x | 54.925x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 1,406.1 | 1,324.3 | 1,437.6 | 38.9 | 0.707x | 55.034x |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 1,416.1 | 1,330.2 | 1,550.0 | 81.3 | 0.712x | 55.427x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,988.6 | 1,967.1 | 1,999.0 | 10.7 | 1.000x | 77.834x |

### `factored` / `s-046` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.7 | 21.7 | 21.8 | 0.0 | 0.022x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.8 | 21.7 | 21.9 | 0.1 | 0.022x | 1.002x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 24.7 | 24.7 | 24.9 | 0.1 | 0.025x | 1.138x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 28.2 | 27.4 | 29.6 | 0.8 | 0.028x | 1.297x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 374.3 | 364.0 | 395.7 | 12.5 | 0.377x | 17.226x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 378.8 | 360.6 | 432.7 | 26.0 | 0.381x | 17.435x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 380.9 | 350.7 | 405.1 | 18.0 | 0.383x | 17.532x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 383.3 | 364.2 | 395.5 | 11.6 | 0.386x | 17.640x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 993.7 | 986.2 | 999.5 | 5.5 | 1.000x | 45.735x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 995.5 | 993.1 | 1,006.9 | 5.8 | 1.002x | 45.821x |

### `factored` / `s-046` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 19.3 | 19.3 | 19.7 | 0.2 | 0.005x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 19.3 | 18.9 | 19.6 | 0.3 | 0.006x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 19.9 | 19.9 | 20.0 | 0.0 | 0.006x | 1.031x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 19.9 | 19.8 | 20.0 | 0.1 | 0.006x | 1.032x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 538.8 | 531.9 | 542.1 | 3.4 | 0.153x | 27.885x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 1,691.4 | 1,667.1 | 1,700.3 | 12.8 | 0.481x | 87.536x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 1,721.8 | 1,717.3 | 1,730.4 | 4.6 | 0.490x | 89.111x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 1,724.7 | 1,707.7 | 1,784.9 | 27.0 | 0.491x | 89.263x |
| 9 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 1,740.2 | 1,713.9 | 1,786.2 | 23.7 | 0.495x | 90.065x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,515.3 | 3,499.0 | 3,525.8 | 9.9 | 1.000x | 181.933x |

### `factored` / `s-047` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.2 | 0.1 | 0.014x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.4 | 0.1 | 0.014x | 1.000x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 26.0 | 25.9 | 26.2 | 0.1 | 0.016x | 1.128x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.0 | 28.1 | 30.7 | 0.8 | 0.018x | 1.256x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.6 | 145.1 | 148.3 | 1.2 | 0.090x | 6.315x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 146.4 | 144.4 | 148.0 | 1.2 | 0.091x | 6.349x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 147.5 | 146.3 | 162.6 | 6.2 | 0.091x | 6.396x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 148.2 | 147.2 | 149.4 | 0.8 | 0.092x | 6.426x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,603.9 | 1,595.3 | 1,630.1 | 12.1 | 0.994x | 69.551x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,613.2 | 1,611.1 | 1,628.3 | 6.4 | 1.000x | 69.956x |

### `factored` / `s-047` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 20.5 | 20.4 | 20.7 | 0.1 | 0.003x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 20.5 | 20.4 | 20.8 | 0.2 | 0.003x | 1.002x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 20.5 | 20.5 | 20.6 | 0.1 | 0.003x | 1.003x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 20.6 | 20.5 | 20.7 | 0.1 | 0.003x | 1.007x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 479.9 | 462.5 | 507.8 | 15.6 | 0.079x | 23.463x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 699.9 | 697.3 | 801.1 | 47.5 | 0.116x | 34.220x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 756.7 | 708.5 | 796.1 | 29.5 | 0.125x | 36.998x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 786.6 | 700.8 | 864.0 | 61.4 | 0.130x | 38.459x |
| 9 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 794.2 | 753.2 | 831.6 | 26.7 | 0.132x | 38.831x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 6,037.0 | 6,003.3 | 6,238.0 | 87.3 | 1.000x | 295.175x |

### `factored` / `s-048` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.1 | 0.017x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.5 | 0.1 | 0.017x | 1.002x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 17.4 | 17.4 | 17.4 | 0.0 | 0.022x | 1.321x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 22.1 | 21.7 | 24.3 | 0.9 | 0.028x | 1.679x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 105.7 | 104.7 | 113.1 | 3.1 | 0.136x | 8.014x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 107.1 | 104.0 | 107.7 | 1.4 | 0.137x | 8.121x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 108.8 | 107.3 | 111.3 | 1.5 | 0.140x | 8.248x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 109.2 | 107.3 | 109.7 | 1.0 | 0.140x | 8.278x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 779.2 | 774.2 | 787.0 | 4.6 | 1.000x | 59.088x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 781.6 | 772.7 | 810.5 | 13.6 | 1.003x | 59.273x |

### `factored` / `s-048` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 12.3 | 12.2 | 12.4 | 0.1 | 0.006x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 12.6 | 12.1 | 12.7 | 0.2 | 0.006x | 1.025x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 12.7 | 12.5 | 12.9 | 0.1 | 0.006x | 1.037x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 12.9 | 12.5 | 14.0 | 0.6 | 0.006x | 1.053x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 185.1 | 179.5 | 187.6 | 2.8 | 0.092x | 15.072x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 314.8 | 310.1 | 345.7 | 13.1 | 0.156x | 25.631x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 318.5 | 305.3 | 398.1 | 35.9 | 0.157x | 25.931x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 323.3 | 311.4 | 344.6 | 11.3 | 0.160x | 26.323x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 339.5 | 316.8 | 389.5 | 24.0 | 0.168x | 27.640x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,022.9 | 2,012.1 | 2,031.0 | 6.7 | 1.000x | 164.702x |

### `factored` / `s-049` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.7 | 11.6 | 12.0 | 0.2 | 0.022x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.3 | 12.1 | 12.4 | 0.1 | 0.023x | 1.051x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 75.7 | 75.6 | 76.5 | 0.3 | 0.140x | 6.485x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 76.1 | 75.8 | 76.5 | 0.3 | 0.140x | 6.519x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 128.9 | 127.5 | 166.4 | 15.2 | 0.238x | 11.038x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 129.9 | 128.2 | 131.3 | 1.1 | 0.239x | 11.120x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 130.5 | 129.7 | 132.2 | 0.9 | 0.241x | 11.172x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 131.5 | 130.4 | 132.3 | 0.7 | 0.242x | 11.257x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 542.5 | 540.2 | 549.2 | 3.2 | 1.000x | 46.454x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 545.6 | 542.2 | 549.3 | 2.3 | 1.006x | 46.713x |

### `factored` / `s-049` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 68.6 | 68.6 | 68.8 | 0.1 | 0.027x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 68.9 | 68.6 | 69.4 | 0.3 | 0.027x | 1.004x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 72.0 | 71.9 | 72.3 | 0.1 | 0.028x | 1.048x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 72.2 | 72.0 | 72.6 | 0.2 | 0.028x | 1.052x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 272.3 | 271.7 | 311.8 | 15.4 | 0.106x | 3.967x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 588.2 | 558.1 | 609.6 | 16.5 | 0.230x | 8.569x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 593.0 | 583.3 | 606.5 | 8.0 | 0.232x | 8.639x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 593.6 | 588.9 | 597.8 | 3.6 | 0.232x | 8.648x |
| 9 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 595.5 | 582.8 | 606.7 | 8.2 | 0.233x | 8.675x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,559.3 | 2,551.8 | 2,565.3 | 4.3 | 1.000x | 37.285x |

### `factored` / `s-050` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.6 | 14.4 | 14.7 | 0.1 | 0.019x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 14.6 | 14.6 | 14.7 | 0.0 | 0.019x | 1.004x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 60.7 | 60.4 | 61.0 | 0.2 | 0.079x | 4.161x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 61.1 | 61.1 | 61.4 | 0.1 | 0.080x | 4.193x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 257.9 | 241.6 | 273.2 | 11.6 | 0.336x | 17.683x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 265.3 | 255.1 | 299.9 | 16.5 | 0.345x | 18.196x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 275.0 | 222.2 | 318.9 | 36.3 | 0.358x | 18.858x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 275.9 | 256.3 | 304.4 | 20.7 | 0.359x | 18.921x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 763.7 | 761.7 | 767.6 | 2.2 | 0.994x | 52.374x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 768.3 | 757.6 | 776.7 | 6.2 | 1.000x | 52.693x |

### `factored` / `s-050` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 54.0 | 53.8 | 54.2 | 0.2 | 0.015x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 54.0 | 53.8 | 54.1 | 0.1 | 0.015x | 1.001x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 56.9 | 56.7 | 57.0 | 0.1 | 0.016x | 1.055x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 57.0 | 56.7 | 57.3 | 0.2 | 0.016x | 1.057x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 386.1 | 379.2 | 401.1 | 7.9 | 0.110x | 7.156x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 1,015.3 | 995.8 | 1,023.9 | 11.7 | 0.289x | 18.817x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 1,021.7 | 1,005.9 | 1,037.3 | 12.2 | 0.291x | 18.935x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 1,023.8 | 1,008.8 | 1,039.9 | 12.2 | 0.291x | 18.975x |
| 9 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 1,034.8 | 1,007.1 | 1,046.5 | 14.3 | 0.294x | 19.180x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,515.0 | 3,506.1 | 3,532.5 | 9.0 | 1.000x | 65.148x |

### `factored` / `s-051` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.6 | 11.6 | 11.9 | 0.1 | 0.021x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.3 | 12.1 | 12.4 | 0.1 | 0.022x | 1.056x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 75.9 | 75.6 | 76.7 | 0.4 | 0.139x | 6.530x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 76.3 | 75.7 | 76.6 | 0.3 | 0.140x | 6.566x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 128.6 | 127.1 | 131.0 | 1.3 | 0.235x | 11.070x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 128.9 | 127.4 | 131.8 | 1.6 | 0.236x | 11.093x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 130.1 | 129.1 | 131.0 | 0.7 | 0.238x | 11.197x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 130.2 | 128.3 | 130.9 | 0.9 | 0.238x | 11.208x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 546.3 | 544.5 | 550.6 | 2.2 | 1.000x | 47.015x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 546.4 | 543.8 | 561.9 | 6.5 | 1.000x | 47.027x |

### `factored` / `s-051` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 68.6 | 68.5 | 68.9 | 0.1 | 0.027x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 68.7 | 68.2 | 71.3 | 1.1 | 0.027x | 1.001x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 72.2 | 72.0 | 74.6 | 1.0 | 0.028x | 1.053x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 72.2 | 72.1 | 72.6 | 0.2 | 0.028x | 1.053x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 275.8 | 272.8 | 280.0 | 2.7 | 0.108x | 4.023x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 585.0 | 563.2 | 592.0 | 10.6 | 0.228x | 8.532x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 589.6 | 574.9 | 601.8 | 10.3 | 0.230x | 8.600x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 591.1 | 534.3 | 602.8 | 24.6 | 0.231x | 8.622x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 594.4 | 583.0 | 598.5 | 5.3 | 0.232x | 8.670x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,563.5 | 2,538.8 | 2,578.9 | 14.5 | 1.000x | 37.391x |

### `factored` / `s-052` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.9 | 0.2 | 0.017x | 1.012x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 25.8 | 24.8 | 26.7 | 0.7 | 0.033x | 1.943x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.5 | 30.7 | 33.1 | 0.8 | 0.041x | 2.376x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.6 | 144.6 | 147.2 | 0.9 | 0.187x | 10.986x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.9 | 145.6 | 147.7 | 0.8 | 0.188x | 11.012x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 148.3 | 147.4 | 149.7 | 0.8 | 0.191x | 11.194x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 148.4 | 146.9 | 149.4 | 0.9 | 0.191x | 11.199x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 776.9 | 769.0 | 786.0 | 5.4 | 1.000x | 58.625x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 779.0 | 776.8 | 781.8 | 1.7 | 1.003x | 58.784x |

### `factored` / `s-052` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 19.6 | 19.5 | 19.8 | 0.1 | 0.007x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 19.6 | 19.6 | 19.9 | 0.1 | 0.007x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 19.8 | 19.7 | 19.9 | 0.1 | 0.007x | 1.008x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 19.9 | 19.7 | 20.2 | 0.2 | 0.007x | 1.014x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 220.5 | 215.2 | 225.6 | 3.8 | 0.083x | 11.235x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 623.7 | 594.9 | 734.8 | 50.2 | 0.233x | 31.779x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 636.3 | 612.2 | 688.0 | 27.8 | 0.238x | 32.422x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 667.9 | 623.4 | 726.2 | 41.6 | 0.250x | 34.028x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 697.8 | 607.1 | 706.6 | 37.8 | 0.261x | 35.551x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,671.8 | 2,654.0 | 2,678.6 | 8.6 | 1.000x | 136.127x |

### `factored` / `s-053` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.8 | 0.2 | 0.017x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.2 | 13.4 | 0.1 | 0.017x | 1.011x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 22.0 | 20.6 | 22.9 | 0.8 | 0.028x | 1.668x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 27.2 | 25.9 | 27.8 | 0.6 | 0.035x | 2.061x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.1 | 144.5 | 148.2 | 1.4 | 0.187x | 10.982x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 146.8 | 144.8 | 148.3 | 1.2 | 0.189x | 11.111x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 148.3 | 147.7 | 148.9 | 0.4 | 0.191x | 11.222x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 148.9 | 146.2 | 149.8 | 1.2 | 0.192x | 11.268x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 775.9 | 770.5 | 788.2 | 6.4 | 1.000x | 58.708x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 777.8 | 773.8 | 780.5 | 2.1 | 1.002x | 58.851x |

### `factored` / `s-053` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 14.3 | 14.3 | 14.5 | 0.1 | 0.005x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 14.4 | 14.4 | 14.6 | 0.1 | 0.005x | 1.006x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 14.7 | 14.6 | 15.5 | 0.3 | 0.005x | 1.023x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 14.7 | 14.6 | 14.8 | 0.1 | 0.006x | 1.026x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 217.3 | 216.6 | 229.9 | 5.1 | 0.081x | 15.150x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 582.6 | 551.7 | 644.2 | 32.1 | 0.218x | 40.616x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 612.9 | 574.4 | 645.0 | 27.6 | 0.230x | 42.730x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 619.0 | 587.6 | 643.5 | 21.3 | 0.232x | 43.155x |
| 9 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 619.4 | 554.2 | 659.1 | 36.2 | 0.232x | 43.188x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,668.0 | 2,660.8 | 2,683.9 | 8.9 | 1.000x | 186.011x |

### `factored` / `s-054` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 0.017x | 1.010x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.5 | 20.8 | 22.8 | 0.7 | 0.028x | 1.631x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 27.2 | 25.9 | 28.1 | 0.8 | 0.035x | 2.056x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.1 | 144.9 | 146.8 | 0.7 | 0.186x | 10.985x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 146.1 | 144.7 | 177.3 | 12.6 | 0.187x | 11.058x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 148.4 | 146.5 | 150.4 | 1.3 | 0.190x | 11.233x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 148.9 | 148.0 | 151.6 | 1.4 | 0.191x | 11.274x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 779.0 | 771.0 | 786.0 | 5.7 | 1.000x | 58.979x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 779.6 | 775.2 | 783.4 | 3.4 | 1.001x | 59.021x |

### `factored` / `s-054` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 14.4 | 14.4 | 14.8 | 0.1 | 0.005x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 14.4 | 14.3 | 14.5 | 0.1 | 0.005x | 1.004x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 14.6 | 14.5 | 14.7 | 0.1 | 0.005x | 1.017x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 14.7 | 14.5 | 15.5 | 0.4 | 0.005x | 1.019x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 221.6 | 219.3 | 223.9 | 1.6 | 0.083x | 15.391x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 603.5 | 544.1 | 618.3 | 26.5 | 0.226x | 41.916x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 609.2 | 552.1 | 643.4 | 30.9 | 0.228x | 42.315x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 609.2 | 528.7 | 724.5 | 68.4 | 0.228x | 42.317x |
| 9 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 642.0 | 567.1 | 697.9 | 42.3 | 0.241x | 44.593x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,668.3 | 2,655.9 | 2,670.1 | 5.8 | 1.000x | 185.339x |

### `factored` / `s-055` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.4 | 0.1 | 0.017x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.0 | 0.017x | 1.004x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.5 | 20.8 | 22.3 | 0.5 | 0.028x | 1.628x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 27.1 | 26.1 | 27.9 | 0.6 | 0.035x | 2.048x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.4 | 144.9 | 146.3 | 0.5 | 0.187x | 10.979x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.6 | 143.9 | 146.9 | 1.0 | 0.188x | 10.999x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 147.9 | 147.4 | 149.0 | 0.6 | 0.191x | 11.169x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 149.2 | 148.5 | 151.3 | 1.1 | 0.192x | 11.269x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 775.4 | 771.4 | 783.1 | 4.1 | 1.000x | 58.563x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 776.1 | 772.3 | 784.4 | 4.0 | 1.001x | 58.616x |

### `factored` / `s-055` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 14.4 | 14.3 | 14.4 | 0.0 | 0.005x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 14.5 | 14.4 | 14.6 | 0.1 | 0.005x | 1.006x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 14.6 | 14.6 | 15.5 | 0.4 | 0.006x | 1.019x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 14.7 | 14.6 | 15.7 | 0.4 | 0.006x | 1.023x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 221.0 | 216.4 | 227.8 | 3.8 | 0.083x | 15.379x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 590.1 | 535.9 | 638.0 | 32.5 | 0.222x | 41.058x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 591.8 | 533.3 | 649.9 | 41.6 | 0.222x | 41.178x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 618.9 | 563.1 | 681.5 | 41.1 | 0.233x | 43.067x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 624.0 | 535.3 | 645.5 | 45.3 | 0.234x | 43.423x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,661.8 | 2,656.3 | 2,671.9 | 5.6 | 1.000x | 185.212x |

### `factored` / `s-056` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.0 | 0.017x | 1.004x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.9 | 21.6 | 23.7 | 0.8 | 0.028x | 1.659x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 28.2 | 27.2 | 29.2 | 0.7 | 0.036x | 2.131x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.8 | 144.4 | 146.6 | 0.9 | 0.188x | 11.032x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 146.0 | 144.5 | 148.8 | 1.5 | 0.188x | 11.045x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 148.4 | 146.1 | 151.1 | 1.6 | 0.191x | 11.230x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 148.8 | 147.9 | 149.1 | 0.5 | 0.192x | 11.256x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 775.5 | 772.1 | 782.8 | 3.5 | 1.000x | 58.670x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 776.3 | 772.7 | 777.2 | 1.6 | 1.001x | 58.728x |

### `factored` / `s-056` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 16.4 | 16.3 | 16.4 | 0.1 | 0.006x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 16.5 | 16.2 | 16.6 | 0.1 | 0.006x | 1.003x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 16.5 | 16.4 | 17.1 | 0.3 | 0.006x | 1.006x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 16.5 | 16.4 | 16.6 | 0.1 | 0.006x | 1.006x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 219.2 | 214.5 | 220.7 | 2.2 | 0.082x | 13.357x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 555.7 | 534.8 | 643.5 | 40.3 | 0.208x | 33.859x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 583.4 | 577.0 | 640.8 | 23.4 | 0.219x | 35.546x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 608.0 | 574.0 | 645.4 | 24.7 | 0.228x | 37.048x |
| 9 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 631.0 | 549.3 | 664.6 | 40.1 | 0.236x | 38.452x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,668.7 | 2,659.0 | 2,679.2 | 7.9 | 1.000x | 162.615x |

### `factored` / `s-057` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7,747.2 | 7,746.1 | 7,795.6 | 19.4 | 0.764x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 7,752.2 | 7,738.9 | 7,762.6 | 10.1 | 0.764x | 1.001x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7,757.0 | 7,741.1 | 7,768.3 | 10.3 | 0.765x | 1.001x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 7,761.2 | 7,747.0 | 7,961.1 | 81.2 | 0.765x | 1.002x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 10,146.0 | 10,138.2 | 10,330.2 | 72.8 | 1.000x | 1.310x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 10,182.3 | 10,158.3 | 10,441.3 | 107.4 | 1.004x | 1.314x |
| 7 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19,088.8 | 19,086.0 | 19,124.8 | 14.9 | 1.881x | 2.464x |
| 8 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 19,097.4 | 19,096.2 | 19,100.8 | 1.6 | 1.882x | 2.465x |
| 9 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37,071.8 | 37,062.4 | 37,121.6 | 24.4 | 3.654x | 4.785x |
| 10 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 38,209.7 | 38,203.8 | 38,350.3 | 55.9 | 3.766x | 4.932x |

### `factored` / `s-058` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 7,469.3 | 7,468.1 | 7,486.6 | 7.0 | 0.041x | 1.000x | 5 | 100% |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7,474.8 | 7,467.9 | 7,483.5 | 5.8 | 0.041x | 1.001x | 5 | 100% |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14,531.6 | 14,526.2 | 14,545.5 | 6.4 | 0.080x | 1.946x | 5 | 100% |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 14,846.1 | 14,790.1 | 14,920.7 | 44.6 | 0.082x | 1.988x | 5 | 100% |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 29,074.4 | 29,006.7 | 29,172.2 | 58.3 | 0.160x | 3.893x | 5 | 100% |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 29,480.6 | 29,346.9 | 29,912.4 | 205.2 | 0.162x | 3.947x | 5 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 181,510.3 | 180,815.2 | 182,635.7 | 616.0 | 1.000x | 24.301x | 5 | 100% |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 182,705.2 | 180,866.7 | 186,386.3 | 2,072.1 | 1.007x | 24.461x | 5 | 100% |

### `factored` / `s-059` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9,559.7 | 9,557.3 | 9,589.8 | 12.2 | 0.033x | 1.000x | 5 | 100% |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9,566.0 | 9,561.0 | 9,613.7 | 20.0 | 0.033x | 1.001x | 5 | 100% |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18,577.8 | 18,570.0 | 18,581.5 | 4.4 | 0.064x | 1.943x | 5 | 100% |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 19,159.4 | 19,122.0 | 19,220.4 | 31.8 | 0.066x | 2.004x | 5 | 100% |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 72,046.7 | 71,915.3 | 72,336.1 | 167.5 | 0.248x | 7.536x | 5 | 100% |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 72,344.6 | 72,076.8 | 72,625.0 | 194.1 | 0.249x | 7.568x | 5 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 290,374.1 | 289,889.5 | 290,890.9 | 352.9 | 1.000x | 30.375x | 5 | 100% |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 291,183.4 | 289,645.5 | 292,712.3 | 1,007.6 | 1.003x | 30.459x | 5 | 100% |

### `factored` / `s-060` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18,163.6 | 18,161.6 | 18,267.8 | 40.7 | 0.021x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 19,073.5 | 19,059.3 | 19,102.4 | 14.2 | 0.023x | 1.050x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19,075.4 | 19,068.8 | 19,094.2 | 9.5 | 0.023x | 1.050x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 19,334.7 | 19,298.0 | 19,364.8 | 27.3 | 0.023x | 1.064x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 193,955.6 | 193,774.3 | 194,597.3 | 299.7 | 0.229x | 10.678x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 194,410.1 | 194,109.0 | 196,004.7 | 674.6 | 0.230x | 10.703x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 194,444.0 | 193,977.8 | 194,831.0 | 292.3 | 0.230x | 10.705x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 194,625.8 | 194,341.1 | 194,993.5 | 228.1 | 0.230x | 10.715x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 846,534.5 | 843,288.0 | 879,313.6 | 14,795.4 | 1.000x | 46.606x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 869,991.9 | 845,671.5 | 887,716.9 | 13,409.7 | 1.028x | 47.897x |

### `factored` / `s-061` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 3,743.5 | 3,741.3 | 3,749.8 | 3.7 | 0.052x | 1.000x | 5 | 100% |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 3,752.6 | 3,738.3 | 3,753.1 | 6.7 | 0.052x | 1.002x | 5 | 100% |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7,294.7 | 7,282.0 | 7,298.9 | 7.0 | 0.101x | 1.949x | 5 | 100% |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 7,483.1 | 7,479.0 | 7,498.5 | 7.0 | 0.103x | 1.999x | 5 | 100% |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 10,981.0 | 10,959.6 | 11,560.9 | 230.0 | 0.152x | 2.933x | 5 | 100% |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 10,983.7 | 10,955.7 | 11,385.0 | 164.9 | 0.152x | 2.934x | 5 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 72,458.7 | 72,026.8 | 73,809.5 | 623.9 | 1.000x | 19.356x | 5 | 100% |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 73,234.8 | 72,361.7 | 74,074.7 | 570.9 | 1.011x | 19.563x | 5 | 100% |

### `factored` / `s-062` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.1 | 0.0 | 0.018x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.3 | 0.1 | 0.018x | 1.007x |
| 3 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 288.4 | 264.6 | 303.8 | 14.3 | 0.325x | 17.959x |
| 4 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 301.4 | 274.6 | 314.4 | 15.7 | 0.340x | 18.766x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 309.0 | 284.1 | 318.7 | 12.5 | 0.348x | 19.237x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 318.8 | 273.6 | 320.4 | 20.2 | 0.359x | 19.852x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 882.5 | 869.2 | 893.1 | 9.8 | 0.994x | 54.947x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 887.5 | 871.1 | 907.6 | 13.0 | 1.000x | 55.260x |
| 9 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 934.9 | 933.8 | 936.6 | 1.1 | 1.053x | 58.210x |
| 10 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 979.1 | 977.8 | 982.6 | 1.6 | 1.103x | 60.961x |

### `factored` / `s-063` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4,795.0 | 4,787.4 | 4,806.7 | 6.6 | 0.023x | 1.000x | 5 | 100% |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 4,811.2 | 4,794.5 | 4,829.2 | 12.1 | 0.023x | 1.003x | 5 | 100% |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13,871.4 | 13,869.8 | 13,881.5 | 4.4 | 0.065x | 2.893x | 5 | 100% |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 14,419.3 | 14,388.7 | 14,570.3 | 66.7 | 0.068x | 3.007x | 5 | 100% |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 95,399.0 | 93,778.8 | 101,828.2 | 3,184.7 | 0.448x | 19.895x | 5 | 100% |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 100,957.4 | 98,122.9 | 101,947.6 | 1,501.9 | 0.474x | 21.055x | 5 | 100% |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 212,190.5 | 210,447.4 | 212,852.6 | 848.2 | 0.997x | 44.252x | 5 | 100% |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 212,930.3 | 210,666.9 | 214,976.5 | 1,429.3 | 1.000x | 44.406x | 5 | 100% |

### `factored` / `s-064` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 7,653.2 | 7,651.6 | 7,667.7 | 6.0 | 0.051x | 1.000x | 5 | 100% |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7,665.6 | 7,658.9 | 7,698.7 | 16.0 | 0.052x | 1.002x | 5 | 100% |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14,883.4 | 14,875.9 | 14,911.4 | 12.9 | 0.100x | 1.945x | 5 | 100% |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 15,329.0 | 15,307.4 | 15,359.1 | 19.1 | 0.103x | 2.003x | 5 | 100% |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 32,733.6 | 32,663.7 | 32,793.9 | 41.3 | 0.220x | 4.277x | 5 | 100% |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 32,972.9 | 32,828.8 | 33,200.6 | 119.3 | 0.222x | 4.308x | 5 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 148,691.5 | 148,315.8 | 151,763.8 | 1,280.5 | 1.000x | 19.429x | 5 | 100% |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 148,849.4 | 148,549.6 | 149,711.3 | 425.0 | 1.001x | 19.449x | 5 | 100% |

### `factored` / `s-065` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.061x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.4 | 10.5 | 0.0 | 0.062x | 1.019x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 28.1 | 27.0 | 29.7 | 1.0 | 0.168x | 2.742x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.6 | 33.5 | 34.7 | 0.5 | 0.207x | 3.381x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 48.1 | 47.9 | 48.5 | 0.2 | 0.288x | 4.703x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 48.2 | 47.8 | 48.4 | 0.2 | 0.288x | 4.713x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 49.0 | 48.7 | 49.5 | 0.3 | 0.293x | 4.790x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 50.1 | 49.7 | 52.7 | 1.1 | 0.300x | 4.899x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 163.8 | 162.9 | 166.6 | 1.3 | 0.980x | 16.008x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 167.2 | 162.3 | 168.6 | 2.4 | 1.000x | 16.340x |

### `factored` / `s-065` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 21.2 | 21.1 | 21.3 | 0.1 | 0.013x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 21.3 | 21.1 | 21.6 | 0.2 | 0.013x | 1.008x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 21.4 | 21.3 | 21.5 | 0.0 | 0.013x | 1.010x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 21.5 | 21.4 | 21.9 | 0.2 | 0.013x | 1.014x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 147.7 | 140.7 | 149.5 | 3.6 | 0.092x | 6.984x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 1,195.8 | 1,129.9 | 1,239.5 | 39.1 | 0.741x | 56.536x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 1,195.8 | 1,123.4 | 1,251.5 | 50.0 | 0.741x | 56.536x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 1,214.8 | 1,173.8 | 1,242.3 | 22.2 | 0.753x | 57.432x |
| 9 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 1,230.7 | 1,137.0 | 1,258.9 | 44.1 | 0.763x | 58.183x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,613.5 | 1,610.1 | 1,623.0 | 5.4 | 1.000x | 76.282x |

### `factored` / `s-066` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33.8 | 33.5 | 33.9 | 0.1 | 0.031x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 36.0 | 35.9 | 36.4 | 0.2 | 0.033x | 1.067x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73.0 | 72.6 | 73.1 | 0.2 | 0.068x | 2.162x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 89.0 | 89.0 | 89.3 | 0.1 | 0.083x | 2.637x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 199.5 | 198.6 | 199.8 | 0.4 | 0.185x | 5.908x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 199.8 | 199.3 | 201.2 | 0.7 | 0.186x | 5.919x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 199.9 | 198.6 | 205.7 | 2.5 | 0.186x | 5.920x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 201.4 | 200.3 | 207.3 | 2.6 | 0.187x | 5.964x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,065.7 | 1,061.1 | 1,090.1 | 11.2 | 0.990x | 31.566x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,077.0 | 1,070.0 | 1,079.7 | 4.1 | 1.000x | 31.900x |

### `factored` / `s-066` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 62.4 | 62.2 | 62.9 | 0.2 | 0.059x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 62.6 | 62.6 | 62.7 | 0.1 | 0.059x | 1.004x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 66.0 | 65.7 | 66.4 | 0.2 | 0.062x | 1.057x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 66.0 | 65.9 | 66.4 | 0.2 | 0.062x | 1.058x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 173.4 | 172.9 | 180.9 | 3.1 | 0.163x | 2.778x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 199.3 | 198.5 | 199.6 | 0.4 | 0.187x | 3.194x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 203.4 | 203.1 | 203.6 | 0.2 | 0.191x | 3.259x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 205.1 | 203.9 | 206.2 | 0.8 | 0.192x | 3.287x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 206.2 | 205.8 | 206.6 | 0.3 | 0.193x | 3.305x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,066.2 | 1,062.8 | 1,072.4 | 3.5 | 1.000x | 17.088x |

### `factored` / `s-067` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.3 | 32.4 | 0.0 | 0.032x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.5 | 34.3 | 34.8 | 0.2 | 0.034x | 1.068x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 69.4 | 68.7 | 70.0 | 0.5 | 0.068x | 2.149x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 85.7 | 85.5 | 86.7 | 0.4 | 0.084x | 2.653x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 171.6 | 170.4 | 178.6 | 3.0 | 0.169x | 5.311x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 171.9 | 171.3 | 172.0 | 0.2 | 0.169x | 5.320x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 174.3 | 173.7 | 176.5 | 0.9 | 0.171x | 5.394x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 177.3 | 176.9 | 178.4 | 0.5 | 0.174x | 5.487x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,003.7 | 999.0 | 1,018.4 | 7.4 | 0.987x | 31.069x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,016.5 | 1,012.4 | 1,020.6 | 2.9 | 1.000x | 31.466x |

### `factored` / `s-067` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 58.3 | 58.3 | 58.5 | 0.1 | 0.058x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 58.4 | 58.4 | 59.2 | 0.3 | 0.058x | 1.002x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 62.2 | 62.1 | 62.3 | 0.0 | 0.062x | 1.066x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 62.8 | 62.2 | 63.0 | 0.3 | 0.062x | 1.076x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 161.2 | 160.7 | 169.6 | 3.4 | 0.160x | 2.763x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 169.0 | 168.1 | 169.3 | 0.4 | 0.168x | 2.897x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 170.7 | 170.4 | 172.9 | 0.9 | 0.170x | 2.927x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 174.2 | 173.4 | 174.8 | 0.5 | 0.173x | 2.986x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 176.3 | 175.1 | 177.2 | 0.8 | 0.175x | 3.022x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,007.1 | 1,001.5 | 1,016.6 | 5.9 | 1.000x | 17.265x |

### `factored` / `s-068` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.8 | 16.7 | 17.5 | 0.3 | 0.024x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19.2 | 19.0 | 19.3 | 0.1 | 0.028x | 1.144x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.7 | 29.5 | 30.2 | 0.3 | 0.043x | 1.770x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 46.3 | 46.2 | 46.4 | 0.1 | 0.067x | 2.765x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 78.1 | 77.4 | 80.2 | 1.2 | 0.113x | 4.661x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 82.3 | 82.2 | 83.3 | 0.4 | 0.120x | 4.911x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 86.3 | 86.2 | 91.2 | 1.9 | 0.125x | 5.152x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 87.8 | 87.7 | 88.6 | 0.3 | 0.128x | 5.244x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 688.4 | 683.0 | 701.6 | 6.8 | 1.000x | 41.093x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 689.9 | 681.5 | 695.5 | 5.7 | 1.002x | 41.183x |

### `factored` / `s-068` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 23.1 | 23.0 | 23.1 | 0.0 | 0.034x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 23.2 | 23.1 | 23.5 | 0.2 | 0.034x | 1.007x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 25.6 | 25.6 | 25.8 | 0.1 | 0.038x | 1.112x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 25.7 | 25.5 | 26.8 | 0.5 | 0.038x | 1.113x |
| 5 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 82.7 | 82.6 | 83.5 | 0.4 | 0.121x | 3.585x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 82.8 | 82.6 | 84.6 | 0.8 | 0.121x | 3.590x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 84.3 | 84.2 | 84.4 | 0.1 | 0.123x | 3.655x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 86.6 | 86.2 | 87.0 | 0.3 | 0.127x | 3.758x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 104.1 | 103.7 | 111.5 | 3.0 | 0.152x | 4.516x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 683.2 | 675.7 | 689.9 | 5.7 | 1.000x | 29.634x |

### `factored` / `s-069` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.0 | 11.8 | 13.7 | 0.7 | 0.019x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.6 | 12.2 | 12.8 | 0.2 | 0.019x | 1.047x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33.7 | 33.3 | 33.8 | 0.2 | 0.052x | 2.795x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 39.2 | 37.2 | 41.6 | 1.6 | 0.060x | 3.255x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.9 | 145.4 | 153.6 | 3.1 | 0.225x | 12.114x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 146.6 | 145.3 | 147.3 | 0.8 | 0.226x | 12.175x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 149.3 | 148.0 | 149.9 | 0.7 | 0.230x | 12.395x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 149.9 | 147.8 | 150.6 | 1.0 | 0.231x | 12.447x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 645.2 | 637.0 | 652.5 | 5.2 | 0.994x | 53.572x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 648.8 | 639.8 | 668.2 | 9.7 | 1.000x | 53.872x |

### `factored` / `s-069` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 27.2 | 27.2 | 27.5 | 0.1 | 0.012x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 27.2 | 27.0 | 27.5 | 0.2 | 0.012x | 1.000x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 27.3 | 27.0 | 27.3 | 0.1 | 0.012x | 1.001x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 27.3 | 27.1 | 27.4 | 0.1 | 0.012x | 1.004x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 204.9 | 200.9 | 209.1 | 3.0 | 0.092x | 7.523x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 1,381.2 | 1,263.4 | 1,559.4 | 94.9 | 0.617x | 50.716x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 1,389.9 | 1,338.9 | 1,427.9 | 28.5 | 0.621x | 51.034x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 1,414.0 | 1,329.5 | 1,555.0 | 87.8 | 0.632x | 51.920x |
| 9 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 1,436.5 | 1,317.6 | 1,464.1 | 61.3 | 0.642x | 52.744x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,238.6 | 2,227.3 | 2,303.0 | 26.9 | 1.000x | 82.199x |

### `factored` / `s-070` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 28.0 | 27.9 | 28.1 | 0.1 | 0.032x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 30.2 | 30.0 | 30.4 | 0.1 | 0.035x | 1.080x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 58.4 | 58.4 | 59.5 | 0.4 | 0.068x | 2.089x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 75.9 | 75.1 | 76.2 | 0.4 | 0.088x | 2.712x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 139.6 | 138.8 | 146.0 | 2.7 | 0.162x | 4.991x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 140.1 | 138.9 | 143.7 | 1.7 | 0.163x | 5.007x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 141.4 | 141.1 | 141.6 | 0.2 | 0.164x | 5.056x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 141.4 | 139.4 | 142.0 | 1.0 | 0.164x | 5.056x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 853.5 | 840.0 | 872.8 | 11.8 | 0.991x | 30.512x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 861.7 | 853.9 | 881.0 | 9.3 | 1.000x | 30.804x |

### `factored` / `s-070` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 48.5 | 48.3 | 48.7 | 0.1 | 0.056x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 48.6 | 48.4 | 48.8 | 0.1 | 0.056x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 52.0 | 51.8 | 52.6 | 0.3 | 0.060x | 1.072x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 52.1 | 51.8 | 52.3 | 0.2 | 0.061x | 1.073x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 144.8 | 144.6 | 146.7 | 1.0 | 0.168x | 2.983x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 145.0 | 144.7 | 145.5 | 0.3 | 0.169x | 2.987x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 147.2 | 145.8 | 147.9 | 0.8 | 0.171x | 3.031x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 148.4 | 148.0 | 156.5 | 3.3 | 0.173x | 3.057x |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 149.3 | 148.8 | 149.6 | 0.3 | 0.174x | 3.076x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 860.2 | 846.9 | 865.5 | 6.2 | 1.000x | 17.719x |

### `factored` / `s-071` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 55.6 | 55.5 | 55.9 | 0.2 | 0.063x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 59.9 | 59.8 | 60.0 | 0.1 | 0.068x | 1.078x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 120.5 | 120.0 | 121.2 | 0.5 | 0.136x | 2.168x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 136.7 | 135.9 | 137.0 | 0.4 | 0.155x | 2.461x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 154.9 | 154.5 | 155.4 | 0.3 | 0.176x | 2.788x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 155.0 | 154.4 | 165.4 | 4.2 | 0.176x | 2.789x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 156.3 | 155.6 | 157.5 | 0.6 | 0.177x | 2.814x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 157.1 | 156.4 | 157.3 | 0.4 | 0.178x | 2.827x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 877.3 | 864.4 | 890.3 | 8.5 | 0.994x | 15.790x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 882.6 | 870.4 | 889.1 | 6.5 | 1.000x | 15.885x |

### `factored` / `s-071` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 109.8 | 109.4 | 110.8 | 0.5 | 0.125x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 110.0 | 109.6 | 121.0 | 4.5 | 0.125x | 1.002x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 113.3 | 113.1 | 113.8 | 0.3 | 0.128x | 1.032x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 113.6 | 112.9 | 114.3 | 0.5 | 0.129x | 1.034x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 159.9 | 159.6 | 160.5 | 0.4 | 0.181x | 1.456x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 160.4 | 160.1 | 161.2 | 0.4 | 0.182x | 1.461x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 161.7 | 161.5 | 163.5 | 0.8 | 0.183x | 1.473x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 164.4 | 164.2 | 170.3 | 2.3 | 0.186x | 1.497x |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 164.4 | 164.2 | 165.8 | 0.6 | 0.186x | 1.497x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 881.6 | 866.1 | 892.5 | 8.4 | 1.000x | 8.029x |

### `factored` / `s-072` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 42.7 | 42.6 | 42.8 | 0.0 | 0.019x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 42.8 | 42.7 | 42.9 | 0.1 | 0.019x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 96.9 | 96.8 | 97.2 | 0.1 | 0.044x | 2.269x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 99.6 | 98.2 | 100.1 | 0.6 | 0.045x | 2.330x |
| 5 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 737.7 | 735.9 | 742.7 | 2.4 | 0.332x | 17.266x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 738.1 | 727.7 | 742.2 | 4.9 | 0.333x | 17.276x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 1,061.6 | 1,051.1 | 1,086.2 | 12.9 | 0.478x | 24.847x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 1,074.1 | 1,048.1 | 1,100.2 | 17.7 | 0.484x | 25.140x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,219.0 | 2,210.0 | 2,260.0 | 17.7 | 1.000x | 51.938x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,233.8 | 2,220.1 | 2,279.1 | 21.0 | 1.007x | 52.286x |

### `factored` / `s-072` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 89.4 | 89.2 | 89.5 | 0.1 | 0.029x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 89.7 | 89.4 | 89.8 | 0.2 | 0.029x | 1.003x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 93.2 | 93.1 | 93.5 | 0.2 | 0.030x | 1.043x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 93.3 | 93.1 | 94.3 | 0.4 | 0.030x | 1.044x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 409.6 | 405.2 | 414.3 | 3.0 | 0.132x | 4.584x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 916.9 | 908.2 | 922.4 | 4.7 | 0.296x | 10.261x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 919.4 | 915.8 | 927.9 | 4.1 | 0.296x | 10.288x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 1,246.0 | 1,237.9 | 1,293.7 | 20.7 | 0.402x | 13.944x |
| 9 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 1,268.7 | 1,256.0 | 1,289.4 | 11.7 | 0.409x | 14.198x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,101.5 | 3,091.3 | 3,122.9 | 12.0 | 1.000x | 34.708x |

### `factored` / `s-073` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 14.7 | 0.6 | 0.017x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.6 | 0.1 | 0.017x | 1.009x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 25.1 | 24.7 | 25.9 | 0.4 | 0.032x | 1.903x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 28.9 | 28.0 | 30.1 | 0.8 | 0.036x | 2.189x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 146.2 | 143.9 | 147.7 | 1.3 | 0.183x | 11.067x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 147.3 | 145.6 | 147.5 | 0.8 | 0.185x | 11.149x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 148.7 | 148.2 | 150.9 | 1.0 | 0.187x | 11.256x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 149.8 | 147.5 | 150.5 | 1.1 | 0.188x | 11.340x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 790.3 | 776.1 | 805.7 | 11.5 | 0.991x | 59.838x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 797.1 | 776.5 | 823.2 | 15.8 | 1.000x | 60.353x |

### `factored` / `s-073` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 20.4 | 20.4 | 20.6 | 0.1 | 0.008x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 20.6 | 20.5 | 20.7 | 0.1 | 0.008x | 1.007x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 20.7 | 20.6 | 21.0 | 0.2 | 0.008x | 1.014x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 21.0 | 20.6 | 21.8 | 0.4 | 0.008x | 1.029x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 221.2 | 215.9 | 224.4 | 3.1 | 0.083x | 10.822x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 819.1 | 795.3 | 901.5 | 38.5 | 0.306x | 40.081x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 823.3 | 779.1 | 885.7 | 39.9 | 0.308x | 40.289x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 860.0 | 716.7 | 894.7 | 62.4 | 0.322x | 42.085x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 867.2 | 762.4 | 869.3 | 44.5 | 0.324x | 42.436x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,673.4 | 2,659.0 | 2,691.3 | 10.9 | 1.000x | 130.819x |

### `factored` / `s-074` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.6 | 0.1 | 0.017x | 1.006x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 31.9 | 31.7 | 32.5 | 0.3 | 0.040x | 2.410x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.4 | 36.8 | 41.3 | 1.8 | 0.047x | 2.818x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 188.9 | 178.3 | 191.8 | 4.8 | 0.237x | 14.249x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 190.4 | 179.1 | 194.1 | 5.4 | 0.239x | 14.368x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 193.5 | 178.2 | 196.2 | 6.5 | 0.243x | 14.603x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 193.7 | 189.9 | 194.6 | 1.7 | 0.244x | 14.611x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 791.7 | 774.7 | 803.2 | 10.4 | 0.996x | 59.731x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 795.2 | 774.0 | 823.3 | 16.4 | 1.000x | 60.001x |

### `factored` / `s-074` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 26.6 | 26.6 | 26.9 | 0.1 | 0.010x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 26.8 | 26.7 | 27.0 | 0.1 | 0.010x | 1.007x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 26.8 | 26.7 | 26.9 | 0.1 | 0.010x | 1.007x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 26.9 | 26.7 | 27.0 | 0.1 | 0.010x | 1.010x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 233.3 | 231.9 | 237.6 | 2.2 | 0.087x | 8.760x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 1,105.9 | 1,090.1 | 1,193.9 | 40.8 | 0.414x | 41.522x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 1,124.1 | 1,108.4 | 1,211.3 | 42.3 | 0.420x | 42.207x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 1,143.2 | 1,108.3 | 1,221.7 | 40.7 | 0.427x | 42.922x |
| 9 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 1,164.1 | 1,140.2 | 1,165.3 | 11.0 | 0.435x | 43.709x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,674.1 | 2,652.4 | 2,692.9 | 14.1 | 1.000x | 100.403x |

### `factored` / `s-075` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.4 | 32.3 | 32.9 | 0.2 | 0.031x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.8 | 34.5 | 35.6 | 0.4 | 0.033x | 1.073x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 69.4 | 68.8 | 70.3 | 0.5 | 0.066x | 2.141x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 85.4 | 85.4 | 85.8 | 0.2 | 0.081x | 2.635x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 172.4 | 172.4 | 172.7 | 0.1 | 0.163x | 5.319x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 173.4 | 173.2 | 175.8 | 1.0 | 0.164x | 5.348x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 174.7 | 174.5 | 178.2 | 1.5 | 0.166x | 5.388x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 176.1 | 175.8 | 188.2 | 4.8 | 0.167x | 5.432x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,032.6 | 1,019.1 | 1,051.2 | 11.9 | 0.978x | 31.851x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,055.4 | 1,036.0 | 1,078.0 | 14.9 | 1.000x | 32.556x |

### `factored` / `s-075` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 58.4 | 58.2 | 58.6 | 0.1 | 0.057x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 58.5 | 58.4 | 58.7 | 0.1 | 0.057x | 1.002x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 62.3 | 62.1 | 66.7 | 1.7 | 0.060x | 1.067x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 62.3 | 62.1 | 62.7 | 0.2 | 0.060x | 1.067x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 110.1 | 106.3 | 111.7 | 2.2 | 0.107x | 1.887x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 173.9 | 173.8 | 174.1 | 0.1 | 0.169x | 2.980x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 175.5 | 175.4 | 177.3 | 0.7 | 0.170x | 3.007x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 176.1 | 176.0 | 176.7 | 0.3 | 0.171x | 3.017x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 177.7 | 177.4 | 190.0 | 4.9 | 0.172x | 3.044x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,032.1 | 1,024.9 | 1,040.5 | 5.0 | 1.000x | 17.681x |

### `factored` / `s-076` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.3 | 33.7 | 0.6 | 0.031x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.5 | 34.5 | 34.7 | 0.1 | 0.033x | 1.069x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 69.1 | 68.9 | 70.4 | 0.5 | 0.065x | 2.138x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 85.4 | 85.0 | 85.8 | 0.3 | 0.081x | 2.645x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 172.7 | 172.2 | 172.8 | 0.2 | 0.163x | 5.346x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 173.3 | 173.1 | 175.6 | 0.9 | 0.164x | 5.364x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 174.6 | 174.5 | 178.5 | 1.6 | 0.165x | 5.405x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 176.4 | 175.6 | 189.2 | 5.3 | 0.167x | 5.463x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,036.2 | 1,019.5 | 1,054.7 | 11.5 | 0.980x | 32.084x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,056.9 | 1,035.7 | 1,080.6 | 16.7 | 1.000x | 32.725x |

### `factored` / `s-076` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 58.4 | 58.3 | 58.5 | 0.1 | 0.057x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 58.6 | 58.3 | 59.0 | 0.2 | 0.057x | 1.002x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 62.5 | 62.2 | 62.9 | 0.2 | 0.061x | 1.069x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 62.7 | 62.3 | 69.2 | 2.7 | 0.061x | 1.073x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 107.3 | 106.2 | 111.9 | 2.0 | 0.104x | 1.836x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 173.9 | 173.8 | 174.1 | 0.1 | 0.169x | 2.976x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 175.5 | 175.4 | 176.9 | 0.6 | 0.171x | 3.003x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 176.3 | 176.0 | 176.6 | 0.2 | 0.171x | 3.016x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 177.5 | 177.4 | 185.7 | 3.3 | 0.173x | 3.037x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,028.9 | 1,028.0 | 1,039.6 | 5.1 | 1.000x | 17.604x |

### `factored` / `s-077` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.3 | 32.4 | 0.0 | 0.027x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.6 | 34.4 | 35.5 | 0.4 | 0.029x | 1.071x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 69.1 | 68.8 | 70.2 | 0.5 | 0.059x | 2.138x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 85.6 | 85.3 | 87.1 | 0.8 | 0.073x | 2.647x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 164.2 | 163.3 | 165.1 | 0.7 | 0.139x | 5.080x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 165.5 | 165.2 | 177.5 | 4.7 | 0.140x | 5.119x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 169.5 | 168.4 | 172.2 | 1.3 | 0.144x | 5.243x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 171.1 | 169.3 | 172.7 | 1.3 | 0.145x | 5.294x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,137.6 | 1,126.0 | 1,163.9 | 15.0 | 0.965x | 35.193x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,178.7 | 1,137.5 | 1,191.9 | 20.8 | 1.000x | 36.465x |

### `factored` / `s-077` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 58.5 | 58.4 | 59.3 | 0.3 | 0.052x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 58.6 | 58.4 | 69.2 | 4.3 | 0.052x | 1.002x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 62.4 | 62.1 | 62.5 | 0.2 | 0.055x | 1.067x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 62.6 | 62.2 | 64.6 | 0.9 | 0.055x | 1.071x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 110.1 | 107.6 | 111.7 | 1.5 | 0.097x | 1.884x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 167.2 | 166.8 | 168.4 | 0.7 | 0.147x | 2.859x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 170.9 | 170.7 | 171.2 | 0.1 | 0.151x | 2.923x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 172.0 | 171.9 | 172.5 | 0.3 | 0.152x | 2.942x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 172.8 | 172.6 | 178.8 | 2.4 | 0.152x | 2.956x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,134.1 | 1,125.2 | 1,144.4 | 7.5 | 1.000x | 19.400x |

### `factored` / `s-078` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.4 | 32.3 | 32.4 | 0.1 | 0.030x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.6 | 34.4 | 34.7 | 0.1 | 0.032x | 1.068x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 69.3 | 69.0 | 70.3 | 0.5 | 0.064x | 2.139x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 85.4 | 85.3 | 87.9 | 1.0 | 0.079x | 2.637x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 159.7 | 159.5 | 160.8 | 0.5 | 0.147x | 4.935x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 159.9 | 159.7 | 173.8 | 5.5 | 0.147x | 4.941x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 160.0 | 159.7 | 163.8 | 1.5 | 0.147x | 4.943x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 160.3 | 160.0 | 164.7 | 1.8 | 0.148x | 4.952x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,080.2 | 1,071.4 | 1,100.9 | 11.6 | 0.995x | 33.371x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,086.1 | 1,070.5 | 1,125.7 | 23.5 | 1.000x | 33.553x |

### `factored` / `s-078` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 58.4 | 58.3 | 58.8 | 0.2 | 0.055x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 58.6 | 58.4 | 58.7 | 0.1 | 0.055x | 1.003x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 62.4 | 62.1 | 62.7 | 0.2 | 0.058x | 1.068x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 62.5 | 62.3 | 64.9 | 1.0 | 0.058x | 1.070x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 107.3 | 106.5 | 112.0 | 2.0 | 0.100x | 1.837x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 161.3 | 161.3 | 161.8 | 0.2 | 0.151x | 2.763x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 161.5 | 161.3 | 162.3 | 0.4 | 0.151x | 2.765x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 162.9 | 162.7 | 163.2 | 0.2 | 0.152x | 2.790x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 164.0 | 163.4 | 170.3 | 2.7 | 0.153x | 2.809x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,070.2 | 1,067.8 | 1,072.9 | 2.1 | 1.000x | 18.327x |

### `factored` / `s-079` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.2 | 32.4 | 0.0 | 0.030x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.8 | 34.4 | 35.8 | 0.5 | 0.032x | 1.077x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 69.4 | 69.2 | 76.2 | 2.7 | 0.063x | 2.149x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 86.8 | 85.4 | 87.8 | 0.9 | 0.079x | 2.686x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 159.6 | 159.4 | 159.7 | 0.1 | 0.146x | 4.941x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 159.8 | 159.8 | 173.6 | 5.5 | 0.146x | 4.947x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 159.9 | 159.7 | 164.1 | 1.7 | 0.146x | 4.949x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 160.4 | 159.7 | 164.6 | 1.8 | 0.147x | 4.963x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,085.5 | 1,080.8 | 1,123.6 | 15.9 | 0.993x | 33.595x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,093.5 | 1,069.7 | 1,127.6 | 25.2 | 1.000x | 33.840x |

### `factored` / `s-079` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 58.4 | 58.3 | 58.9 | 0.3 | 0.054x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 58.5 | 58.3 | 59.2 | 0.3 | 0.054x | 1.002x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 62.5 | 62.1 | 62.9 | 0.3 | 0.058x | 1.069x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 62.7 | 62.1 | 64.8 | 1.2 | 0.058x | 1.073x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 107.1 | 106.8 | 111.2 | 1.7 | 0.100x | 1.834x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 161.3 | 161.2 | 162.7 | 0.6 | 0.150x | 2.761x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 161.4 | 161.2 | 161.8 | 0.2 | 0.150x | 2.763x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 162.8 | 162.8 | 163.3 | 0.2 | 0.151x | 2.787x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 163.5 | 163.3 | 170.4 | 2.8 | 0.152x | 2.799x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,075.6 | 1,064.1 | 1,085.9 | 8.6 | 1.000x | 18.413x |

### `factored` / `s-080` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.3 | 0.1 | 0.017x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.2 | 0.0 | 0.017x | 1.004x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 31.5 | 31.2 | 48.5 | 6.8 | 0.034x | 1.959x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.1 | 36.6 | 37.8 | 0.5 | 0.040x | 2.304x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 289.3 | 267.5 | 319.4 | 22.2 | 0.309x | 17.966x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 290.4 | 270.8 | 320.0 | 16.9 | 0.310x | 18.035x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 297.1 | 249.7 | 328.7 | 26.5 | 0.317x | 18.450x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 309.4 | 292.4 | 328.6 | 14.7 | 0.331x | 19.217x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 911.8 | 904.0 | 941.5 | 14.7 | 0.974x | 56.629x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 936.2 | 908.5 | 950.1 | 13.8 | 1.000x | 58.143x |

### `factored` / `s-080` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 26.0 | 26.0 | 26.3 | 0.2 | 0.008x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 26.2 | 26.2 | 26.5 | 0.1 | 0.008x | 1.006x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 26.3 | 26.3 | 26.8 | 0.2 | 0.008x | 1.011x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 26.4 | 26.1 | 26.5 | 0.1 | 0.008x | 1.012x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 320.7 | 308.5 | 325.0 | 6.5 | 0.101x | 12.314x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 1,734.0 | 1,721.5 | 1,775.4 | 19.1 | 0.546x | 66.588x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 1,735.2 | 1,725.3 | 1,770.6 | 16.0 | 0.547x | 66.632x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 1,739.2 | 1,717.9 | 1,773.0 | 19.5 | 0.548x | 66.784x |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 1,740.2 | 1,711.1 | 1,776.5 | 21.4 | 0.548x | 66.823x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,173.1 | 3,122.9 | 3,201.7 | 29.6 | 1.000x | 121.846x |

### `factored` / `s-081` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.9 | 9.9 | 14.9 | 1.9 | 0.323x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.6 | 10.3 | 11.2 | 0.4 | 0.347x | 1.073x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.9 | 10.9 | 11.1 | 0.1 | 0.357x | 1.105x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.6 | 11.5 | 12.0 | 0.2 | 0.379x | 1.173x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 30.3 | 30.3 | 30.7 | 0.2 | 0.990x | 3.064x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.6 | 30.3 | 30.9 | 0.2 | 1.000x | 3.094x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 46.6 | 46.0 | 46.8 | 0.3 | 1.520x | 4.701x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 46.9 | 46.6 | 63.9 | 6.7 | 1.532x | 4.739x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 48.3 | 47.9 | 48.4 | 0.2 | 1.575x | 4.873x |
| 10 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 48.6 | 48.2 | 49.7 | 0.5 | 1.586x | 4.908x |

### `factored` / `s-081` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 5.4 | 5.3 | 5.4 | 0.0 | 0.177x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 5.6 | 5.6 | 6.0 | 0.2 | 0.186x | 1.048x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 5.7 | 5.7 | 6.5 | 0.4 | 0.187x | 1.054x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 5.9 | 5.9 | 6.1 | 0.1 | 0.195x | 1.100x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.4 | 30.4 | 35.5 | 2.0 | 1.000x | 5.649x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 42.1 | 39.8 | 50.7 | 4.0 | 1.382x | 7.808x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 49.2 | 48.3 | 78.7 | 11.8 | 1.617x | 9.138x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 49.2 | 49.0 | 49.7 | 0.2 | 1.618x | 9.139x |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 49.9 | 49.6 | 50.5 | 0.3 | 1.641x | 9.273x |
| 10 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 50.1 | 49.9 | 50.2 | 0.1 | 1.647x | 9.307x |

### `factored` / `s-082` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 11.1 | 0.4 | 0.336x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.5 | 10.3 | 10.7 | 0.2 | 0.345x | 1.025x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.7 | 12.4 | 16.6 | 1.6 | 0.415x | 1.235x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.4 | 13.9 | 15.5 | 0.6 | 0.472x | 1.403x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 30.3 | 30.3 | 30.6 | 0.1 | 0.990x | 2.946x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.6 | 30.3 | 30.7 | 0.1 | 1.000x | 2.975x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 47.6 | 47.4 | 50.6 | 1.2 | 1.555x | 4.627x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 47.7 | 47.2 | 61.4 | 5.6 | 1.558x | 4.633x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 48.2 | 47.9 | 49.4 | 0.5 | 1.576x | 4.687x |
| 10 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 48.8 | 48.6 | 50.8 | 0.8 | 1.596x | 4.747x |

### `factored` / `s-082` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 5.9 | 5.9 | 6.5 | 0.2 | 0.194x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 5.9 | 5.9 | 7.4 | 0.6 | 0.194x | 1.002x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 6.3 | 6.2 | 6.7 | 0.2 | 0.206x | 1.061x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 6.3 | 6.3 | 7.0 | 0.3 | 0.206x | 1.064x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.5 | 30.4 | 36.0 | 2.2 | 1.000x | 5.156x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 41.9 | 39.7 | 50.7 | 4.0 | 1.373x | 7.078x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 66.5 | 66.0 | 67.7 | 0.6 | 2.180x | 11.241x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 66.7 | 66.4 | 69.1 | 1.0 | 2.188x | 11.281x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 68.0 | 67.2 | 73.8 | 2.4 | 2.232x | 11.509x |
| 10 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 68.4 | 67.2 | 69.3 | 0.7 | 2.243x | 11.564x |

### `factored` / `s-083` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.4 | 11.3 | 11.4 | 0.0 | 0.333x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 11.9 | 11.5 | 12.0 | 0.2 | 0.349x | 1.048x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 34.2 | 33.8 | 35.9 | 0.8 | 1.000x | 3.004x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 34.2 | 33.5 | 34.8 | 0.6 | 1.001x | 3.006x |
| 5 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 81.3 | 80.9 | 107.3 | 10.4 | 2.379x | 7.147x |
| 6 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 107.0 | 99.5 | 107.5 | 3.3 | 3.132x | 9.407x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 110.0 | 108.6 | 111.7 | 1.1 | 3.219x | 9.668x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 110.2 | 109.5 | 124.4 | 5.7 | 3.225x | 9.688x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 111.5 | 110.8 | 113.6 | 1.2 | 3.263x | 9.799x |
| 10 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 113.6 | 111.7 | 114.1 | 1.0 | 3.325x | 9.988x |

### `factored` / `s-083` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 34.9 | 34.7 | 36.3 | 0.6 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.4 | 46.1 | 50.5 | 1.7 | 1.329x | 1.329x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 72.6 | 72.4 | 72.8 | 0.1 | 2.079x | 2.079x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 72.6 | 72.4 | 72.7 | 0.1 | 2.080x | 2.080x |
| 5 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 73.4 | 73.3 | 73.8 | 0.2 | 2.101x | 2.101x |
| 6 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 73.6 | 73.3 | 74.8 | 0.6 | 2.107x | 2.107x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 2,847.3 | 2,821.3 | 2,865.9 | 14.7 | 81.540x | 81.540x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 2,858.4 | 2,844.9 | 2,876.9 | 11.9 | 81.860x | 81.860x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 2,892.2 | 2,876.0 | 2,920.2 | 17.7 | 82.829x | 82.829x |
| 10 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 2,932.2 | 2,884.2 | 3,166.3 | 104.0 | 83.973x | 83.973x |

### `factored` / `s-084` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 19.2 | 19.1 | 19.2 | 0.0 | 0.557x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19.3 | 19.2 | 19.3 | 0.1 | 0.560x | 1.007x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.8 | 21.7 | 22.9 | 0.5 | 0.633x | 1.137x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 25.8 | 25.7 | 26.0 | 0.1 | 0.750x | 1.347x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 33.9 | 33.3 | 34.9 | 0.5 | 0.984x | 1.768x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 34.4 | 33.3 | 35.8 | 0.8 | 1.000x | 1.797x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 164.1 | 161.5 | 170.6 | 3.1 | 4.767x | 8.566x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 164.2 | 162.6 | 166.5 | 1.5 | 4.768x | 8.567x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 165.1 | 164.1 | 168.0 | 1.4 | 4.794x | 8.615x |
| 10 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 165.7 | 161.9 | 167.6 | 1.9 | 4.811x | 8.645x |

### `factored` / `s-084` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 16.3 | 16.3 | 16.6 | 0.1 | 0.478x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 16.3 | 16.3 | 16.4 | 0.0 | 0.479x | 1.002x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 16.4 | 16.3 | 17.3 | 0.4 | 0.480x | 1.004x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 16.5 | 16.2 | 17.1 | 0.3 | 0.483x | 1.011x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 34.1 | 34.0 | 36.0 | 0.7 | 1.000x | 2.093x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.5 | 44.3 | 50.1 | 2.3 | 1.303x | 2.728x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 776.6 | 768.6 | 824.2 | 23.0 | 22.746x | 47.612x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 803.8 | 759.8 | 856.8 | 32.2 | 23.542x | 49.277x |
| 9 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 807.4 | 783.4 | 826.5 | 16.2 | 23.648x | 49.500x |
| 10 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 816.4 | 790.9 | 829.2 | 13.8 | 23.912x | 50.052x |

### `factored` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 3,578,231.1 | 3,576,317.9 | 3,602,224.3 | 11,669.5 | 0.069x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 3,585,869.9 | 3,583,427.0 | 3,597,682.4 | 5,181.3 | 0.069x | 1.002x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 3,591,987.4 | 3,590,797.4 | 3,601,594.9 | 4,116.6 | 0.069x | 1.004x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 3,592,664.3 | 3,587,951.2 | 3,593,528.1 | 2,115.4 | 0.069x | 1.004x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 7,035,795.3 | 7,009,352.0 | 8,001,058.7 | 387,307.0 | 0.136x | 1.966x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 11,005,527.0 | 10,855,866.0 | 11,201,808.0 | 126,814.2 | 0.212x | 3.076x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 11,133,526.0 | 10,950,764.0 | 13,188,808.0 | 986,462.8 | 0.215x | 3.111x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 11,720,858.0 | 10,879,342.0 | 13,357,267.0 | 1,041,552.1 | 0.226x | 3.276x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 12,383,226.0 | 10,986,287.0 | 13,367,952.0 | 1,052,785.8 | 0.239x | 3.461x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 51,904,436.8 | 51,152,324.8 | 56,038,510.3 | 1,779,597.1 | 1.000x | 14.506x |

### `factored` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 18,840.6 | 18,811.9 | 19,033.4 | 100.2 | 1.000x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 1,877,191.1 | 1,876,531.7 | 1,886,882.3 | 3,884.7 | 99.635x | 99.635x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 1,877,260.8 | 1,875,439.5 | 1,881,882.7 | 2,244.1 | 99.639x | 99.639x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 1,890,786.8 | 1,887,656.8 | 1,902,865.6 | 5,443.4 | 100.357x | 100.357x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 1,891,036.2 | 1,889,788.5 | 1,910,932.2 | 8,040.5 | 100.370x | 100.370x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 17,613,765.0 | 17,607,798.7 | 17,660,250.3 | 19,680.2 | 934.881x | 934.881x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 84,131,626.0 | 82,952,790.0 | 85,889,048.0 | 986,617.8 | 4465.433x | 4465.433x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 84,475,069.0 | 83,381,293.0 | 137,755,930.0 | 21,408,303.4 | 4483.662x | 4483.662x |
| 9 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 85,165,258.0 | 83,972,671.0 | 86,437,576.0 | 826,733.0 | 4520.295x | 4520.295x |
| 10 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 85,541,423.0 | 85,288,921.0 | 87,301,653.0 | 877,599.0 | 4540.261x | 4540.261x |

### `factored` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 18,719.6 | 18,627.0 | 18,844.5 | 71.8 | 1.000x | 1.000x | 5 | 100% |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 1,875,979.8 | 1,874,635.4 | 1,880,736.7 | 2,227.7 | 100.215x | 100.215x | 5 | 100% |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 1,876,102.3 | 1,873,857.9 | 1,887,917.3 | 5,159.3 | 100.221x | 100.221x | 5 | 100% |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 1,877,576.4 | 1,875,791.4 | 1,894,424.6 | 7,003.2 | 100.300x | 100.300x | 5 | 100% |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 1,877,691.4 | 1,875,385.5 | 1,889,728.5 | 5,203.4 | 100.306x | 100.306x | 5 | 100% |

### `factored` / `t-d-prose-sparse-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 3,141,066.7 | 3,134,696.6 | 3,150,577.9 | 5,694.4 | 0.007x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 3,143,556.6 | 3,128,195.2 | 3,210,853.9 | 29,187.7 | 0.007x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 3,194,847.5 | 3,173,328.7 | 3,326,101.4 | 55,577.2 | 0.007x | 1.017x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 3,208,442.6 | 3,192,828.8 | 3,224,604.6 | 10,193.8 | 0.007x | 1.021x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43,153,515.3 | 42,815,546.0 | 43,984,667.7 | 388,386.7 | 0.096x | 13.738x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 107,359,111.0 | 102,345,462.0 | 138,607,445.0 | 13,043,775.8 | 0.239x | 34.179x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 111,230,777.0 | 102,887,930.0 | 114,878,508.0 | 4,158,171.7 | 0.247x | 35.412x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 111,477,194.0 | 101,006,710.0 | 129,685,566.0 | 10,438,595.4 | 0.248x | 35.490x |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 118,280,183.0 | 115,794,518.0 | 165,329,947.0 | 19,225,323.5 | 0.263x | 37.656x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 450,017,052.5 | 446,457,267.8 | 484,180,930.8 | 13,977,884.6 | 1.000x | 143.269x |

### `factored` / `t-e-prose-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 19,062.9 | 18,738.8 | 19,146.0 | 150.3 | 1.000x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 3,098,348.9 | 3,071,619.9 | 3,136,325.3 | 23,587.5 | 162.533x | 162.533x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 3,101,481.2 | 3,087,192.8 | 3,117,223.1 | 9,692.4 | 162.697x | 162.697x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 3,146,368.5 | 3,120,215.9 | 3,174,738.1 | 21,273.0 | 165.052x | 165.052x |
| 5 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 3,163,082.9 | 3,136,677.8 | 3,169,746.1 | 11,706.9 | 165.929x | 165.929x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 22,702,180.3 | 22,559,286.0 | 23,013,833.3 | 155,844.7 | 1190.908x | 1190.908x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 100,999,221.0 | 97,231,368.0 | 116,770,738.0 | 6,936,122.6 | 5298.202x | 5298.202x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 101,786,173.0 | 98,546,615.0 | 124,415,552.0 | 9,311,747.7 | 5339.484x | 5339.484x |
| 9 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 103,654,980.0 | 97,605,454.0 | 128,461,846.0 | 11,381,593.6 | 5437.518x | 5437.518x |
| 10 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 110,435,166.0 | 100,536,856.0 | 173,919,428.0 | 26,454,553.1 | 5793.192x | 5793.192x |

### `floor` / `s-000` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.246x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.0 | 0.258x | 1.045x |
| 3 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.318x | 1.292x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.319x | 1.296x |
| 5 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.352x | 1.430x |
| 6 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.0 | 0.353x | 1.433x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.7 | 21.6 | 22.4 | 0.3 | 0.753x | 3.055x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 22.0 | 21.7 | 22.3 | 0.2 | 0.764x | 3.098x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.8 | 29.2 | 0.2 | 1.000x | 4.058x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.0 | 28.9 | 35.2 | 2.4 | 1.007x | 4.085x |

### `floor` / `s-000` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.4 | 0.1 | 0.177x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.6 | 18.4 | 19.1 | 0.2 | 0.180x | 1.018x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.6 | 18.4 | 19.0 | 0.2 | 0.180x | 1.019x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.6 | 18.4 | 23.5 | 2.0 | 0.180x | 1.019x |
| 5 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.5 | 26.2 | 27.5 | 0.5 | 0.257x | 1.451x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.6 | 26.3 | 26.9 | 0.2 | 0.258x | 1.457x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.3 | 27.0 | 30.4 | 1.5 | 0.265x | 1.494x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.7 | 27.6 | 32.7 | 2.0 | 0.269x | 1.517x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.1 | 44.0 | 46.6 | 1.0 | 0.428x | 2.418x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 103.1 | 101.4 | 119.8 | 6.9 | 1.000x | 5.648x |

### `floor` / `s-001` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.3 | 0.1 | 0.249x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.1 | 0.258x | 1.039x |
| 3 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.287x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.321x | 1.289x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.0 | 0.354x | 1.422x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.355x | 1.426x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.754x | 3.033x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.7 | 21.6 | 21.8 | 0.1 | 0.759x | 3.053x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 29.1 | 0.2 | 1.000x | 4.022x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 30.6 | 0.8 | 1.006x | 4.045x |

### `floor` / `s-001` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.4 | 0.1 | 0.178x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.178x | 1.001x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.178x | 1.003x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.3 | 0.0 | 0.179x | 1.004x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 29.6 | 0.4 | 0.282x | 1.585x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 29.0 | 28.8 | 29.4 | 0.2 | 0.284x | 1.597x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 30.1 | 30.1 | 30.4 | 0.1 | 0.294x | 1.655x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 30.4 | 29.4 | 32.4 | 1.3 | 0.298x | 1.673x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.0 | 43.9 | 46.7 | 1.1 | 0.431x | 2.423x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 102.2 | 100.4 | 119.5 | 7.2 | 1.000x | 5.622x |

### `floor` / `s-002` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.248x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.258x | 1.041x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.292x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.6 | 0.2 | 0.321x | 1.294x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.0 | 0.355x | 1.430x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.3 | 0.1 | 0.355x | 1.433x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.1 | 0.754x | 3.039x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.1 | 0.755x | 3.042x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.6 | 29.0 | 0.2 | 1.000x | 4.032x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 30.6 | 0.7 | 1.007x | 4.058x |

### `floor` / `s-002` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 16.9 | 16.8 | 17.5 | 0.2 | 0.166x | 1.000x |
| 2 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 17.4 | 17.4 | 17.5 | 0.0 | 0.171x | 1.031x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 17.8 | 17.7 | 21.6 | 1.8 | 0.175x | 1.054x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 19.0 | 0.4 | 0.178x | 1.075x |
| 5 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.178x | 1.076x |
| 6 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.178x | 1.077x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 19.7 | 0.6 | 0.179x | 1.079x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 18.3 | 18.3 | 18.3 | 0.0 | 0.179x | 1.084x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.2 | 43.8 | 53.6 | 3.8 | 0.433x | 2.613x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 102.1 | 100.2 | 119.0 | 7.1 | 1.000x | 6.039x |

### `floor` / `s-003` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.248x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.038x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.287x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.289x |
| 5 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.4 | 0.1 | 0.354x | 1.425x |
| 6 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.2 | 0.1 | 0.354x | 1.427x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.752x | 3.032x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.753x | 3.035x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.8 | 0.1 | 1.000x | 4.031x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.4 | 30.6 | 0.8 | 1.003x | 4.044x |

### `floor` / `s-003` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.179x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.179x | 1.000x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.1 | 0.179x | 1.000x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.8 | 0.2 | 0.180x | 1.005x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.1 | 43.7 | 50.6 | 2.6 | 0.435x | 2.427x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 53.2 | 53.0 | 53.4 | 0.2 | 0.524x | 2.923x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 53.5 | 53.4 | 53.9 | 0.2 | 0.528x | 2.942x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 54.7 | 54.7 | 59.1 | 1.8 | 0.540x | 3.009x |
| 9 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 55.4 | 54.1 | 57.7 | 1.6 | 0.547x | 3.049x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.4 | 99.0 | 120.7 | 8.2 | 1.000x | 5.577x |

### `floor` / `s-004` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.2 | 0.0 | 0.246x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.042x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.318x | 1.293x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.6 | 0.2 | 0.318x | 1.296x |
| 5 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.4 | 0.1 | 0.351x | 1.429x |
| 6 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.2 | 0.1 | 0.353x | 1.435x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 23.4 | 23.4 | 23.9 | 0.2 | 0.810x | 3.299x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.6 | 23.4 | 24.3 | 0.3 | 0.817x | 3.327x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 29.0 | 0.1 | 1.000x | 4.071x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.0 | 28.7 | 30.6 | 0.7 | 1.002x | 4.081x |

### `floor` / `s-004` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.1 | 18.1 | 18.5 | 0.2 | 0.178x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.1 | 0.179x | 1.007x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.4 | 18.2 | 18.6 | 0.1 | 0.181x | 1.015x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.4 | 18.2 | 18.8 | 0.2 | 0.181x | 1.018x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.7 | 44.6 | 47.7 | 1.2 | 0.439x | 2.466x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 80.7 | 80.4 | 80.8 | 0.2 | 0.794x | 4.454x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 81.1 | 81.0 | 81.5 | 0.2 | 0.798x | 4.477x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 81.8 | 81.5 | 85.1 | 1.7 | 0.805x | 4.516x |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 82.2 | 82.1 | 82.3 | 0.1 | 0.808x | 4.536x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.7 | 100.1 | 119.8 | 7.4 | 1.000x | 5.612x |

### `floor` / `s-005` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.246x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.041x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.291x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.294x |
| 5 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.5 | 0.2 | 0.350x | 1.422x |
| 6 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.1 | 0.351x | 1.425x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.8 | 0.1 | 0.750x | 3.044x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 22.0 | 0.2 | 0.751x | 3.049x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.0 | 0.2 | 1.000x | 4.059x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 30.7 | 0.8 | 1.003x | 4.070x |

### `floor` / `s-005` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 17.0 | 16.8 | 18.6 | 0.7 | 0.166x | 1.000x |
| 2 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 17.4 | 17.4 | 17.6 | 0.0 | 0.170x | 1.028x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 17.8 | 17.7 | 21.6 | 1.9 | 0.174x | 1.048x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.178x | 1.071x |
| 5 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.0 | 0.178x | 1.071x |
| 6 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.178x | 1.072x |
| 7 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.1 | 0.178x | 1.074x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 18.3 | 18.3 | 18.3 | 0.0 | 0.179x | 1.079x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.1 | 43.8 | 47.4 | 1.4 | 0.431x | 2.600x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 102.3 | 100.2 | 119.3 | 7.1 | 1.000x | 6.029x |

### `floor` / `s-006` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.2 | 0.0 | 0.247x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.0 | 0.257x | 1.041x |
| 3 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.291x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.320x | 1.293x |
| 5 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.3 | 0.1 | 0.353x | 1.426x |
| 6 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.8 | 0.3 | 0.355x | 1.436x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.752x | 3.041x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.7 | 21.6 | 21.7 | 0.0 | 0.754x | 3.051x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.2 | 0.3 | 1.000x | 4.044x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.1 | 28.8 | 30.6 | 0.8 | 1.012x | 4.094x |

### `floor` / `s-006` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 16.9 | 16.8 | 17.0 | 0.1 | 0.165x | 1.000x |
| 2 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 17.4 | 17.4 | 17.4 | 0.0 | 0.170x | 1.034x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 17.7 | 17.7 | 21.6 | 1.9 | 0.173x | 1.053x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.178x | 1.078x |
| 5 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.0 | 0.178x | 1.081x |
| 6 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.4 | 0.1 | 0.178x | 1.081x |
| 7 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 19.6 | 0.5 | 0.178x | 1.083x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 18.3 | 18.3 | 18.9 | 0.2 | 0.179x | 1.087x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.9 | 43.8 | 45.4 | 0.6 | 0.429x | 2.608x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 102.3 | 100.5 | 118.9 | 7.0 | 1.000x | 6.071x |

### `floor` / `s-007` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.247x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.040x |
| 3 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.292x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.319x | 1.292x |
| 5 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.0 | 10.5 | 0.2 | 0.351x | 1.420x |
| 6 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.0 | 0.352x | 1.424x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.1 | 0.751x | 3.037x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.751x | 3.038x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.3 | 0.3 | 1.000x | 4.046x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.1 | 28.8 | 30.7 | 0.8 | 1.014x | 4.101x |

### `floor` / `s-007` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.178x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.178x | 1.000x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.178x | 1.000x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 19.9 | 0.7 | 0.178x | 1.001x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.1 | 43.8 | 45.1 | 0.5 | 0.431x | 2.425x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 53.1 | 52.9 | 54.1 | 0.5 | 0.519x | 2.923x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 53.5 | 53.5 | 54.3 | 0.3 | 0.524x | 2.946x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 54.3 | 54.1 | 57.7 | 1.7 | 0.531x | 2.987x |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 54.7 | 54.7 | 56.4 | 0.7 | 0.535x | 3.012x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 102.3 | 100.3 | 119.0 | 7.0 | 1.000x | 5.627x |

### `floor` / `s-008` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.2 | 0.0 | 0.246x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.041x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.293x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.6 | 0.2 | 0.319x | 1.297x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.0 | 0.350x | 1.425x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.352x | 1.432x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.747x | 3.041x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.8 | 0.1 | 0.748x | 3.044x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 29.0 | 0.2 | 1.000x | 4.068x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.6 | 28.7 | 30.6 | 0.7 | 1.027x | 4.180x |

### `floor` / `s-008` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.180x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.180x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 22.9 | 1.9 | 0.180x | 1.001x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.180x | 1.001x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.1 | 26.0 | 26.6 | 0.2 | 0.258x | 1.434x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.3 | 26.2 | 26.7 | 0.2 | 0.260x | 1.448x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.2 | 26.8 | 30.8 | 1.6 | 0.269x | 1.495x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.5 | 27.4 | 27.6 | 0.1 | 0.271x | 1.510x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.0 | 43.8 | 45.3 | 0.5 | 0.435x | 2.421x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.1 | 100.1 | 119.3 | 7.3 | 1.000x | 5.565x |

### `floor` / `s-009` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.2 | 0.0 | 0.245x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.255x | 1.040x |
| 3 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.317x | 1.291x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.318x | 1.295x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.1 | 0.350x | 1.424x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.0 | 10.2 | 0.1 | 0.351x | 1.429x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.746x | 3.039x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.1 | 0.747x | 3.043x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 30.7 | 0.7 | 0.997x | 4.064x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 29.2 | 0.2 | 1.000x | 4.075x |

### `floor` / `s-009` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.179x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.179x | 1.000x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 21.3 | 1.2 | 0.179x | 1.001x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.4 | 0.1 | 0.179x | 1.001x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.1 | 25.7 | 26.6 | 0.3 | 0.257x | 1.435x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.5 | 26.1 | 27.0 | 0.3 | 0.261x | 1.460x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.1 | 27.0 | 29.6 | 1.2 | 0.267x | 1.490x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.4 | 27.2 | 29.9 | 1.0 | 0.270x | 1.508x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.1 | 43.8 | 45.5 | 0.6 | 0.435x | 2.427x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.5 | 100.8 | 119.2 | 7.1 | 1.000x | 5.584x |

### `floor` / `s-010` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.9 | 0.3 | 0.246x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.041x |
| 3 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.293x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.319x | 1.294x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.0 | 0.351x | 1.428x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.352x | 1.431x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.9 | 0.1 | 0.750x | 3.045x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.750x | 3.046x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 30.9 | 0.8 | 1.000x | 4.061x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 29.1 | 0.1 | 1.000x | 4.062x |

### `floor` / `s-010` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.0 | 0.178x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.5 | 0.1 | 0.179x | 1.001x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.179x | 1.001x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.179x | 1.002x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 25.9 | 25.8 | 26.4 | 0.2 | 0.254x | 1.424x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.4 | 26.1 | 26.6 | 0.2 | 0.260x | 1.456x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.0 | 26.8 | 30.0 | 1.4 | 0.266x | 1.489x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.4 | 27.2 | 27.5 | 0.1 | 0.269x | 1.508x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.0 | 43.8 | 45.7 | 0.7 | 0.432x | 2.421x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.8 | 100.5 | 119.4 | 7.2 | 1.000x | 5.606x |

### `floor` / `s-011` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.3 | 0.1 | 0.246x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.255x | 1.040x |
| 3 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.317x | 1.291x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.317x | 1.292x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.3 | 0.1 | 0.349x | 1.422x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.352x | 1.433x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.9 | 0.1 | 0.746x | 3.039x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.8 | 0.1 | 0.747x | 3.041x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.4 | 30.7 | 1.0 | 0.996x | 4.054x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 29.1 | 0.2 | 1.000x | 4.072x |

### `floor` / `s-011` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.177x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.4 | 0.1 | 0.177x | 1.000x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.5 | 0.1 | 0.177x | 1.001x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.178x | 1.003x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.0 | 43.8 | 45.7 | 0.7 | 0.429x | 2.422x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 50.3 | 50.2 | 50.5 | 0.1 | 0.490x | 2.767x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 50.9 | 50.9 | 51.1 | 0.1 | 0.496x | 2.801x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 51.6 | 51.4 | 55.1 | 1.8 | 0.502x | 2.836x |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 52.0 | 52.0 | 52.2 | 0.1 | 0.507x | 2.862x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 102.6 | 100.7 | 118.8 | 6.8 | 1.000x | 5.647x |

### `floor` / `s-012` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.2 | 0.1 | 0.247x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.041x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.7 | 0.2 | 0.319x | 1.293x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.3 | 9.2 | 10.1 | 0.4 | 0.322x | 1.304x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.1 | 0.352x | 1.426x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.353x | 1.431x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 22.0 | 0.2 | 0.750x | 3.040x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.751x | 3.041x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 30.7 | 0.8 | 0.999x | 4.045x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 29.0 | 0.1 | 1.000x | 4.051x |

### `floor` / `s-012` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.6 | 0.2 | 0.179x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.5 | 0.1 | 0.179x | 1.000x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.5 | 0.1 | 0.179x | 1.000x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.179x | 1.000x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 31.1 | 31.0 | 31.6 | 0.2 | 0.305x | 1.708x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 31.7 | 31.6 | 31.7 | 0.1 | 0.311x | 1.741x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 32.1 | 32.0 | 35.7 | 1.7 | 0.316x | 1.766x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 33.1 | 32.8 | 33.2 | 0.1 | 0.325x | 1.818x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.3 | 43.9 | 45.3 | 0.6 | 0.435x | 2.435x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.7 | 100.2 | 103.2 | 1.0 | 1.000x | 5.593x |

### `floor` / `s-013` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.2 | 0.0 | 0.246x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.041x |
| 3 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.292x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.6 | 0.2 | 0.319x | 1.293x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.0 | 0.352x | 1.428x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.2 | 0.1 | 0.353x | 1.434x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.749x | 3.038x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.1 | 0.749x | 3.040x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 30.7 | 0.8 | 0.998x | 4.050x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.8 | 29.1 | 0.1 | 1.000x | 4.057x |

### `floor` / `s-013` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.178x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.0 | 0.178x | 1.000x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.178x | 1.000x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 20.0 | 0.7 | 0.178x | 1.001x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 31.0 | 31.0 | 31.3 | 0.1 | 0.304x | 1.704x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 31.6 | 31.5 | 31.8 | 0.1 | 0.309x | 1.736x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 32.1 | 32.0 | 35.5 | 1.7 | 0.314x | 1.763x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 32.9 | 32.8 | 33.3 | 0.2 | 0.322x | 1.810x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.9 | 43.7 | 46.2 | 0.9 | 0.430x | 2.414x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 102.1 | 100.3 | 103.4 | 1.2 | 1.000x | 5.613x |

### `floor` / `s-014` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.2 | 0.1 | 0.246x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.039x |
| 3 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.292x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.3 | 9.2 | 10.0 | 0.3 | 0.321x | 1.303x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.353x | 1.431x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.2 | 0.1 | 0.353x | 1.434x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.1 | 0.749x | 3.039x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.749x | 3.040x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 30.7 | 0.8 | 0.999x | 4.054x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.0 | 0.2 | 1.000x | 4.059x |

### `floor` / `s-014` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.180x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.8 | 0.3 | 0.180x | 1.002x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.4 | 0.1 | 0.180x | 1.002x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.5 | 0.1 | 0.180x | 1.004x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 19.5 | 19.5 | 20.0 | 0.2 | 0.193x | 1.073x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 20.1 | 20.1 | 20.4 | 0.1 | 0.198x | 1.105x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 20.7 | 20.7 | 24.5 | 1.9 | 0.204x | 1.138x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 21.0 | 21.0 | 21.0 | 0.0 | 0.207x | 1.154x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.9 | 43.8 | 45.6 | 0.7 | 0.434x | 2.414x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.3 | 100.2 | 102.5 | 0.8 | 1.000x | 5.568x |

### `floor` / `s-015` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.3 | 0.1 | 0.249x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.0 | 0.258x | 1.037x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.8 | 0.2 | 0.321x | 1.287x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.321x | 1.288x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.0 | 0.355x | 1.424x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.2 | 0.0 | 0.356x | 1.429x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.754x | 3.026x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.754x | 3.027x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 29.0 | 0.2 | 1.000x | 4.012x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.8 | 30.6 | 0.7 | 1.011x | 4.057x |

### `floor` / `s-015` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.7 | 0.2 | 0.179x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.179x | 1.000x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.179x | 1.000x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.179x | 1.001x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.8 | 0.1 | 0.282x | 1.570x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 28.9 | 28.9 | 29.0 | 0.0 | 0.285x | 1.591x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 29.4 | 29.4 | 32.1 | 1.2 | 0.290x | 1.619x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 30.1 | 30.1 | 34.4 | 1.7 | 0.297x | 1.654x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.9 | 43.7 | 50.3 | 2.6 | 0.433x | 2.415x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.4 | 101.2 | 103.0 | 0.8 | 1.000x | 5.578x |

### `floor` / `s-016` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.247x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.040x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.6 | 0.2 | 0.319x | 1.291x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.320x | 1.293x |
| 5 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.2 | 0.1 | 0.354x | 1.432x |
| 6 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.2 | 0.1 | 0.354x | 1.433x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.751x | 3.037x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.1 | 0.753x | 3.043x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.4 | 0.4 | 1.000x | 4.043x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 30.1 | 28.7 | 30.6 | 0.8 | 1.047x | 4.233x |

### `floor` / `s-016` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.5 | 0.1 | 0.179x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.8 | 0.2 | 0.179x | 1.000x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.179x | 1.000x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.4 | 0.1 | 0.179x | 1.001x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 28.5 | 28.4 | 28.6 | 0.1 | 0.280x | 1.566x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 29.0 | 28.8 | 34.8 | 2.3 | 0.285x | 1.594x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 29.4 | 29.4 | 32.1 | 1.3 | 0.289x | 1.618x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 30.0 | 29.9 | 30.1 | 0.1 | 0.295x | 1.650x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.4 | 44.0 | 45.9 | 0.8 | 0.446x | 2.497x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.7 | 100.2 | 103.1 | 1.0 | 1.000x | 5.593x |

### `floor` / `s-017` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.2 | 0.1 | 0.246x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.042x |
| 3 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.293x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.3 | 9.2 | 10.3 | 0.4 | 0.322x | 1.307x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.1 | 0.351x | 1.426x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.2 | 0.1 | 0.353x | 1.433x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.750x | 3.041x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.8 | 0.1 | 0.750x | 3.043x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.7 | 0.4 | 1.000x | 4.058x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 30.5 | 0.7 | 1.002x | 4.068x |

### `floor` / `s-017` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.179x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.1 | 0.179x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.179x | 1.002x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.180x | 1.002x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 31.0 | 30.9 | 31.3 | 0.1 | 0.306x | 1.709x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 31.5 | 31.4 | 31.6 | 0.1 | 0.311x | 1.736x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 32.0 | 32.0 | 35.7 | 1.7 | 0.316x | 1.764x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 33.0 | 32.7 | 33.1 | 0.2 | 0.326x | 1.817x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.4 | 43.8 | 52.1 | 3.1 | 0.448x | 2.500x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.3 | 100.6 | 103.0 | 1.0 | 1.000x | 5.582x |

### `floor` / `s-018` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.248x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.0 | 0.258x | 1.041x |
| 3 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.291x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 10.2 | 0.4 | 0.320x | 1.293x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.0 | 10.2 | 0.1 | 0.352x | 1.419x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.2 | 0.1 | 0.356x | 1.436x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.754x | 3.040x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.754x | 3.041x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 29.0 | 0.2 | 1.000x | 4.034x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.0 | 28.7 | 30.6 | 0.7 | 1.014x | 4.091x |

### `floor` / `s-018` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.179x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.1 | 0.179x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.5 | 0.1 | 0.180x | 1.004x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.6 | 0.2 | 0.180x | 1.007x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 28.5 | 28.4 | 28.6 | 0.1 | 0.281x | 1.567x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 28.9 | 28.8 | 29.6 | 0.3 | 0.284x | 1.588x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 29.6 | 29.3 | 32.0 | 1.2 | 0.292x | 1.632x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 30.1 | 29.9 | 30.1 | 0.1 | 0.297x | 1.657x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.3 | 44.0 | 46.0 | 0.7 | 0.447x | 2.496x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.4 | 100.3 | 102.5 | 0.7 | 1.000x | 5.584x |

### `floor` / `s-019` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.246x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.0 | 0.256x | 1.041x |
| 3 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.291x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 10.3 | 0.4 | 0.318x | 1.292x |
| 5 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.2 | 0.1 | 0.354x | 1.435x |
| 6 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.3 | 0.1 | 0.354x | 1.437x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.749x | 3.038x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.749x | 3.040x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.3 | 0.3 | 1.000x | 4.058x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 30.6 | 0.7 | 1.001x | 4.063x |

### `floor` / `s-019` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.5 | 0.1 | 0.179x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.179x | 1.000x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.7 | 0.2 | 0.179x | 1.000x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.179x | 1.001x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 31.0 | 30.9 | 31.7 | 0.3 | 0.305x | 1.704x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 31.5 | 31.3 | 32.1 | 0.3 | 0.310x | 1.734x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 32.4 | 32.0 | 35.6 | 1.6 | 0.318x | 1.780x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 32.9 | 32.7 | 33.1 | 0.2 | 0.324x | 1.811x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.0 | 44.0 | 45.9 | 0.6 | 0.443x | 2.475x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.6 | 100.7 | 102.4 | 0.6 | 1.000x | 5.589x |

### `floor` / `s-020` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.3 | 0.1 | 0.247x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.040x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.6 | 0.2 | 0.319x | 1.290x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.6 | 0.2 | 0.319x | 1.291x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.1 | 0.352x | 1.424x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.2 | 0.1 | 0.354x | 1.432x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.0 | 0.751x | 3.037x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.1 | 0.751x | 3.038x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.4 | 29.0 | 0.2 | 1.000x | 4.045x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 30.7 | 0.8 | 1.005x | 4.066x |

### `floor` / `s-020` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.4 | 0.1 | 0.177x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 19.3 | 0.4 | 0.177x | 1.000x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.1 | 0.177x | 1.001x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.178x | 1.002x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.4 | 43.8 | 46.7 | 0.9 | 0.442x | 2.495x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 47.9 | 47.7 | 48.6 | 0.3 | 0.467x | 2.635x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 48.9 | 47.8 | 49.6 | 0.7 | 0.476x | 2.686x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 49.1 | 48.5 | 51.2 | 1.0 | 0.478x | 2.697x |
| 9 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 49.2 | 48.5 | 54.4 | 2.2 | 0.480x | 2.708x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 102.5 | 100.5 | 103.1 | 1.1 | 1.000x | 5.639x |

### `floor` / `s-021` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.248x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.0 | 0.258x | 1.041x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.6 | 0.2 | 0.320x | 1.293x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.293x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.0 | 0.353x | 1.427x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.1 | 0.354x | 1.428x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.753x | 3.041x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.753x | 3.042x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.6 | 29.0 | 0.1 | 1.000x | 4.037x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 30.9 | 0.9 | 1.005x | 4.056x |

### `floor` / `s-021` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.7 | 0.2 | 0.179x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.179x | 1.000x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.179x | 1.001x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.5 | 0.1 | 0.179x | 1.003x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.2 | 25.9 | 26.7 | 0.3 | 0.258x | 1.443x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.4 | 26.2 | 27.2 | 0.4 | 0.260x | 1.452x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.0 | 26.8 | 29.8 | 1.4 | 0.266x | 1.486x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.5 | 27.5 | 28.5 | 0.4 | 0.271x | 1.514x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.4 | 44.0 | 47.2 | 1.1 | 0.447x | 2.497x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.6 | 100.6 | 102.6 | 0.8 | 1.000x | 5.591x |

### `floor` / `s-022` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.2 | 0.1 | 0.248x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.0 | 0.258x | 1.041x |
| 3 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.291x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.7 | 0.2 | 0.320x | 1.292x |
| 5 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.1 | 0.353x | 1.428x |
| 6 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.2 | 0.1 | 0.354x | 1.431x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.753x | 3.041x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.754x | 3.045x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.0 | 0.1 | 1.000x | 4.040x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 30.8 | 0.8 | 1.006x | 4.066x |

### `floor` / `s-022` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.5 | 0.1 | 0.179x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.179x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 19.1 | 0.4 | 0.179x | 1.001x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.179x | 1.001x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.2 | 25.7 | 26.8 | 0.4 | 0.257x | 1.439x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.5 | 26.3 | 26.9 | 0.2 | 0.261x | 1.459x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.0 | 26.8 | 29.6 | 1.3 | 0.266x | 1.486x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.6 | 27.5 | 27.8 | 0.1 | 0.271x | 1.516x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.1 | 43.9 | 47.6 | 1.3 | 0.443x | 2.478x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.6 | 100.0 | 102.1 | 0.9 | 1.000x | 5.589x |

### `floor` / `s-023` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.4 | 0.1 | 0.246x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.040x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.290x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.291x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.3 | 0.1 | 0.349x | 1.420x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.5 | 0.2 | 0.351x | 1.426x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.747x | 3.036x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.7 | 21.6 | 27.4 | 2.3 | 0.751x | 3.051x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 30.9 | 0.8 | 0.997x | 4.053x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 28.9 | 0.1 | 1.000x | 4.064x |

### `floor` / `s-023` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.179x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.179x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.7 | 0.2 | 0.179x | 1.002x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.4 | 0.1 | 0.180x | 1.005x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.1 | 25.6 | 26.9 | 0.4 | 0.256x | 1.434x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.4 | 26.2 | 26.9 | 0.3 | 0.259x | 1.451x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.0 | 26.9 | 29.1 | 1.0 | 0.265x | 1.485x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.7 | 27.4 | 27.9 | 0.2 | 0.272x | 1.522x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.2 | 44.3 | 46.7 | 0.9 | 0.444x | 2.486x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.7 | 100.2 | 102.3 | 0.9 | 1.000x | 5.597x |

### `floor` / `s-024` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.2 | 0.0 | 0.247x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.0 | 0.256x | 1.040x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.290x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.6 | 0.2 | 0.320x | 1.297x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.1 | 0.352x | 1.426x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.2 | 0.1 | 0.353x | 1.433x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.9 | 0.1 | 0.749x | 3.039x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.0 | 0.750x | 3.040x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.2 | 0.2 | 1.000x | 4.055x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.8 | 30.6 | 0.7 | 1.000x | 4.055x |

### `floor` / `s-024` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.178x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.178x | 1.000x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 19.0 | 0.3 | 0.178x | 1.001x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.0 | 0.178x | 1.001x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.0 | 25.5 | 26.4 | 0.3 | 0.254x | 1.427x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.3 | 26.3 | 26.6 | 0.1 | 0.258x | 1.448x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.0 | 26.9 | 29.8 | 1.3 | 0.265x | 1.485x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.6 | 27.3 | 32.4 | 2.0 | 0.270x | 1.518x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.3 | 44.2 | 48.0 | 1.4 | 0.443x | 2.489x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 102.1 | 100.8 | 103.1 | 0.8 | 1.000x | 5.613x |

### `floor` / `s-025` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.246x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.041x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.317x | 1.292x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.317x | 1.292x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.0 | 0.350x | 1.423x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.2 | 0.1 | 0.351x | 1.431x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.747x | 3.040x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.8 | 0.1 | 0.749x | 3.050x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 29.0 | 0.1 | 1.000x | 4.072x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.8 | 30.6 | 0.7 | 1.000x | 4.074x |

### `floor` / `s-025` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.179x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.180x | 1.001x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.1 | 0.180x | 1.003x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.4 | 0.1 | 0.180x | 1.003x |
| 5 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.2 | 26.1 | 26.5 | 0.1 | 0.259x | 1.443x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.3 | 26.3 | 26.8 | 0.2 | 0.260x | 1.449x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.2 | 26.7 | 29.7 | 1.3 | 0.269x | 1.496x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.5 | 27.3 | 27.7 | 0.1 | 0.271x | 1.512x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.7 | 43.9 | 47.7 | 1.4 | 0.452x | 2.516x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.2 | 100.7 | 103.2 | 0.9 | 1.000x | 5.572x |

### `floor` / `s-026` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.247x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.041x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.291x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.1 | 9.2 | 0.0 | 0.320x | 1.293x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.3 | 0.1 | 0.352x | 1.424x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.0 | 10.2 | 0.0 | 0.353x | 1.427x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.1 | 0.752x | 3.041x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.7 | 21.6 | 21.8 | 0.1 | 0.758x | 3.063x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 29.0 | 0.2 | 1.000x | 4.042x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 30.7 | 0.7 | 1.009x | 4.077x |

### `floor` / `s-026` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.179x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.1 | 0.179x | 1.000x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.4 | 0.1 | 0.179x | 1.002x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.179x | 1.003x |
| 5 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.3 | 26.2 | 26.6 | 0.2 | 0.258x | 1.446x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.3 | 25.7 | 26.7 | 0.3 | 0.259x | 1.449x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.0 | 26.7 | 30.9 | 1.8 | 0.265x | 1.484x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.5 | 27.4 | 27.7 | 0.1 | 0.270x | 1.512x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.5 | 43.9 | 47.5 | 1.3 | 0.448x | 2.507x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.6 | 99.9 | 103.1 | 1.3 | 1.000x | 5.596x |

### `floor` / `s-027` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.248x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.258x | 1.041x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.291x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.292x |
| 5 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.3 | 0.1 | 0.354x | 1.432x |
| 6 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.2 | 0.1 | 0.355x | 1.434x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.752x | 3.040x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.7 | 21.6 | 21.9 | 0.1 | 0.757x | 3.057x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.8 | 0.1 | 1.000x | 4.040x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.1 | 28.8 | 30.7 | 0.7 | 1.014x | 4.096x |

### `floor` / `s-027` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.179x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.179x | 1.000x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.4 | 0.1 | 0.179x | 1.001x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.0 | 0.179x | 1.001x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.4 | 25.7 | 26.6 | 0.3 | 0.259x | 1.452x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.5 | 26.1 | 26.6 | 0.2 | 0.260x | 1.457x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.0 | 26.7 | 30.1 | 1.5 | 0.265x | 1.485x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.6 | 27.4 | 30.8 | 1.3 | 0.271x | 1.517x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.7 | 43.8 | 47.8 | 1.5 | 0.449x | 2.514x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.7 | 100.8 | 103.7 | 1.1 | 1.000x | 5.595x |

### `floor` / `s-028` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.247x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.036x |
| 3 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.318x | 1.288x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.4 | 0.1 | 0.318x | 1.288x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.0 | 0.351x | 1.423x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.9 | 0.3 | 0.352x | 1.425x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.9 | 0.1 | 0.748x | 3.031x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.748x | 3.032x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 29.1 | 0.2 | 1.000x | 4.053x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.0 | 28.8 | 30.6 | 0.7 | 1.002x | 4.062x |

### `floor` / `s-028` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.178x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.4 | 0.1 | 0.178x | 1.000x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.5 | 0.1 | 0.179x | 1.001x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 21.2 | 1.2 | 0.179x | 1.002x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.4 | 25.8 | 26.5 | 0.3 | 0.259x | 1.453x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.4 | 26.1 | 26.6 | 0.2 | 0.259x | 1.454x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 26.9 | 26.7 | 30.6 | 1.6 | 0.264x | 1.482x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.4 | 27.4 | 27.6 | 0.1 | 0.269x | 1.509x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.6 | 43.9 | 48.2 | 1.5 | 0.447x | 2.508x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.9 | 99.6 | 103.2 | 1.2 | 1.000x | 5.607x |

### `floor` / `s-029` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.2 | 0.0 | 0.245x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.0 | 0.255x | 1.041x |
| 3 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.5 | 0.1 | 0.317x | 1.291x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.317x | 1.292x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.0 | 0.350x | 1.429x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.2 | 0.1 | 0.351x | 1.433x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.9 | 0.1 | 0.746x | 3.043x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.746x | 3.044x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 31.0 | 0.9 | 0.995x | 4.059x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 29.3 | 0.3 | 1.000x | 4.078x |

### `floor` / `s-029` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.180x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 22.2 | 1.6 | 0.180x | 1.000x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.1 | 0.180x | 1.000x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.4 | 0.1 | 0.180x | 1.001x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.3 | 25.8 | 26.6 | 0.3 | 0.260x | 1.448x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.4 | 26.2 | 26.6 | 0.1 | 0.261x | 1.452x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.0 | 26.8 | 31.0 | 1.8 | 0.268x | 1.488x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.5 | 27.3 | 27.6 | 0.1 | 0.272x | 1.512x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.1 | 43.9 | 46.9 | 1.1 | 0.446x | 2.480x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.0 | 100.2 | 103.3 | 1.1 | 1.000x | 5.557x |

### `floor` / `s-030` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.246x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.042x |
| 3 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.317x | 1.293x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.294x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.0 | 0.351x | 1.429x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.352x | 1.434x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.747x | 3.043x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.1 | 0.747x | 3.044x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 29.0 | 0.2 | 1.000x | 4.073x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.1 | 28.7 | 30.7 | 0.7 | 1.007x | 4.100x |

### `floor` / `s-030` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.4 | 0.1 | 0.180x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.180x | 1.002x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.4 | 0.1 | 0.180x | 1.003x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.7 | 0.2 | 0.180x | 1.003x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.0 | 25.6 | 26.6 | 0.3 | 0.257x | 1.430x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.3 | 26.2 | 26.7 | 0.2 | 0.260x | 1.448x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.0 | 26.8 | 30.0 | 1.5 | 0.267x | 1.486x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.6 | 27.2 | 27.7 | 0.2 | 0.273x | 1.519x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.0 | 43.9 | 54.2 | 3.8 | 0.445x | 2.476x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.1 | 100.0 | 102.9 | 1.0 | 1.000x | 5.569x |

### `floor` / `s-031` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.247x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.041x |
| 3 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.1 | 9.2 | 0.0 | 0.319x | 1.292x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 12.6 | 1.4 | 0.320x | 1.293x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.0 | 0.353x | 1.427x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.354x | 1.431x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.752x | 3.040x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.8 | 0.1 | 0.752x | 3.040x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.9 | 0.1 | 1.000x | 4.044x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.8 | 30.7 | 0.8 | 1.003x | 4.056x |

### `floor` / `s-031` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.9 | 0.3 | 0.178x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.178x | 1.000x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.178x | 1.001x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.4 | 0.1 | 0.178x | 1.002x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.0 | 25.8 | 26.2 | 0.1 | 0.254x | 1.429x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.4 | 26.0 | 27.0 | 0.3 | 0.258x | 1.453x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.1 | 26.8 | 30.8 | 1.6 | 0.265x | 1.491x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.5 | 27.4 | 27.6 | 0.0 | 0.269x | 1.512x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.4 | 44.3 | 47.0 | 1.0 | 0.444x | 2.499x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 102.2 | 100.4 | 104.9 | 1.6 | 1.000x | 5.623x |

### `floor` / `s-032` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.2 | 0.0 | 0.248x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.039x |
| 3 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.4 | 0.1 | 0.319x | 1.288x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.289x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.3 | 0.1 | 0.353x | 1.425x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.2 | 0.1 | 0.355x | 1.432x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.0 | 0.752x | 3.036x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.1 | 0.752x | 3.036x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 28.9 | 0.1 | 1.000x | 4.039x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.0 | 28.8 | 30.8 | 0.7 | 1.010x | 4.080x |

### `floor` / `s-032` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.6 | 0.2 | 0.179x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.179x | 1.000x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.4 | 0.1 | 0.179x | 1.001x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.179x | 1.004x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.3 | 25.8 | 26.7 | 0.3 | 0.258x | 1.445x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.5 | 26.2 | 26.7 | 0.2 | 0.260x | 1.457x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.1 | 26.9 | 31.0 | 1.7 | 0.267x | 1.494x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.6 | 27.4 | 27.7 | 0.1 | 0.271x | 1.516x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.6 | 43.9 | 47.3 | 1.3 | 0.449x | 2.512x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.6 | 100.1 | 102.7 | 0.9 | 1.000x | 5.594x |

### `floor` / `s-033` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.248x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.258x | 1.041x |
| 3 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.4 | 0.1 | 0.320x | 1.293x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.293x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.1 | 0.353x | 1.428x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.2 | 0.1 | 0.354x | 1.430x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.0 | 0.752x | 3.039x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.0 | 0.753x | 3.043x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.3 | 0.3 | 1.000x | 4.040x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 30.7 | 0.8 | 1.000x | 4.041x |

### `floor` / `s-033` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.179x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.1 | 0.179x | 1.001x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.7 | 0.2 | 0.179x | 1.002x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.179x | 1.002x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.0 | 25.7 | 27.1 | 0.5 | 0.255x | 1.428x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.3 | 26.2 | 26.7 | 0.2 | 0.258x | 1.446x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.1 | 26.9 | 31.1 | 1.6 | 0.267x | 1.493x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.7 | 27.7 | 29.9 | 0.9 | 0.273x | 1.527x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.8 | 43.9 | 47.4 | 1.2 | 0.450x | 2.517x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.7 | 100.7 | 102.0 | 0.5 | 1.000x | 5.596x |

### `floor` / `s-034` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.2 | 0.0 | 0.246x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.041x |
| 3 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.292x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.293x |
| 5 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.3 | 0.1 | 0.350x | 1.424x |
| 6 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.1 | 0.351x | 1.427x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.0 | 0.747x | 3.041x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.749x | 3.047x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 30.3 | 0.6 | 1.000x | 4.068x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.4 | 30.7 | 0.8 | 1.002x | 4.076x |

### `floor` / `s-034` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.178x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.5 | 0.1 | 0.179x | 1.001x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.179x | 1.001x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.1 | 0.179x | 1.004x |
| 5 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.4 | 26.3 | 27.2 | 0.3 | 0.259x | 1.454x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.6 | 26.2 | 26.9 | 0.2 | 0.261x | 1.464x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.0 | 26.8 | 30.7 | 1.6 | 0.265x | 1.488x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.5 | 27.2 | 27.7 | 0.2 | 0.270x | 1.516x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.5 | 44.0 | 46.8 | 1.1 | 0.446x | 2.502x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.8 | 100.8 | 102.7 | 0.8 | 1.000x | 5.605x |

### `floor` / `s-035` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.2 | 0.0 | 0.245x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.255x | 1.040x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.317x | 1.290x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.317x | 1.291x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.0 | 0.350x | 1.426x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.351x | 1.430x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.9 | 0.1 | 0.746x | 3.041x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.746x | 3.041x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 30.7 | 0.8 | 0.996x | 4.059x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.5 | 33.4 | 1.9 | 1.000x | 4.075x |

### `floor` / `s-035` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.179x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.179x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.179x | 1.001x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.4 | 0.1 | 0.179x | 1.003x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.3 | 25.8 | 26.7 | 0.3 | 0.259x | 1.446x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.4 | 26.2 | 26.9 | 0.3 | 0.260x | 1.451x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.0 | 26.8 | 29.8 | 1.4 | 0.265x | 1.483x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.4 | 27.4 | 27.6 | 0.1 | 0.270x | 1.509x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.4 | 43.9 | 46.9 | 1.1 | 0.447x | 2.497x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.5 | 100.4 | 102.8 | 0.8 | 1.000x | 5.589x |

### `floor` / `s-036` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.2 | 0.0 | 0.248x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.259x | 1.042x |
| 3 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.321x | 1.294x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.322x | 1.297x |
| 5 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.3 | 0.1 | 0.353x | 1.425x |
| 6 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.3 | 0.1 | 0.355x | 1.430x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.9 | 0.2 | 0.754x | 3.041x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.755x | 3.045x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 30.7 | 0.8 | 1.000x | 4.031x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.8 | 30.6 | 0.7 | 1.012x | 4.080x |

### `floor` / `s-036` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.179x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.179x | 1.000x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 19.1 | 0.4 | 0.180x | 1.000x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.180x | 1.002x |
| 5 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.4 | 26.1 | 26.5 | 0.2 | 0.261x | 1.452x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.4 | 26.1 | 26.7 | 0.3 | 0.261x | 1.454x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.0 | 26.9 | 29.8 | 1.3 | 0.267x | 1.485x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.8 | 27.4 | 29.4 | 0.7 | 0.275x | 1.531x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.3 | 43.9 | 46.9 | 1.1 | 0.447x | 2.491x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.3 | 99.8 | 102.7 | 1.0 | 1.000x | 5.572x |

### `floor` / `s-037` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.247x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.0 | 0.257x | 1.040x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.291x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.319x | 1.292x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.1 | 0.351x | 1.421x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.4 | 0.1 | 0.352x | 1.423x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.750x | 3.037x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.1 | 0.751x | 3.039x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 29.0 | 0.1 | 1.000x | 4.047x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 30.7 | 0.8 | 1.003x | 4.057x |

### `floor` / `s-037` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.5 | 0.1 | 0.179x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 19.1 | 0.4 | 0.179x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.179x | 1.002x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.179x | 1.002x |
| 5 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.3 | 26.2 | 26.7 | 0.2 | 0.259x | 1.448x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.3 | 25.8 | 26.5 | 0.2 | 0.259x | 1.448x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 26.9 | 26.8 | 30.2 | 1.5 | 0.265x | 1.483x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.4 | 27.3 | 27.6 | 0.1 | 0.270x | 1.509x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.3 | 44.2 | 48.3 | 1.5 | 0.446x | 2.495x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.6 | 100.5 | 108.3 | 2.8 | 1.000x | 5.590x |

### `floor` / `s-038` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.246x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.0 | 0.256x | 1.041x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.317x | 1.290x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.317x | 1.292x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.1 | 0.349x | 1.421x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.1 | 0.349x | 1.421x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.8 | 0.1 | 0.747x | 3.040x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.747x | 3.041x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 29.2 | 0.2 | 1.000x | 4.072x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 30.9 | 0.8 | 1.001x | 4.078x |

### `floor` / `s-038` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.178x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.0 | 0.178x | 1.001x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.4 | 0.1 | 0.178x | 1.001x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.5 | 0.1 | 0.179x | 1.002x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.3 | 26.0 | 26.5 | 0.1 | 0.258x | 1.449x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.4 | 26.1 | 26.7 | 0.2 | 0.259x | 1.453x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 26.9 | 26.8 | 29.4 | 1.2 | 0.264x | 1.481x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.6 | 27.2 | 27.7 | 0.2 | 0.271x | 1.519x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.2 | 43.9 | 47.9 | 1.5 | 0.443x | 2.486x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.9 | 100.2 | 102.8 | 1.0 | 1.000x | 5.611x |

### `floor` / `s-039` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.245x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.255x | 1.041x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.316x | 1.292x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.317x | 1.294x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.1 | 0.348x | 1.422x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.2 | 0.1 | 0.351x | 1.432x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.745x | 3.041x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.745x | 3.041x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 30.6 | 0.7 | 0.994x | 4.058x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.0 | 28.6 | 29.1 | 0.2 | 1.000x | 4.084x |

### `floor` / `s-039` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.178x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.178x | 1.001x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.178x | 1.002x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.179x | 1.003x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 28.6 | 28.4 | 29.2 | 0.3 | 0.280x | 1.573x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 28.8 | 28.8 | 29.0 | 0.1 | 0.283x | 1.587x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 29.4 | 29.4 | 32.3 | 1.4 | 0.289x | 1.621x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 30.2 | 30.0 | 31.3 | 0.5 | 0.296x | 1.661x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.2 | 43.9 | 47.3 | 1.2 | 0.443x | 2.486x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 102.0 | 100.7 | 102.6 | 0.7 | 1.000x | 5.614x |

### `floor` / `s-040` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 9.2 | 0.8 | 0.247x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.041x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.291x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.320x | 1.294x |
| 5 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.353x | 1.431x |
| 6 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.2 | 0.0 | 0.354x | 1.432x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.8 | 16.8 | 16.8 | 0.0 | 0.584x | 2.366x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.8 | 16.8 | 16.9 | 0.0 | 0.586x | 2.373x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.8 | 0.1 | 1.000x | 4.048x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 30.7 | 0.8 | 1.001x | 4.052x |

### `floor` / `s-040` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 8.6 | 8.6 | 8.7 | 0.1 | 0.264x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 8.8 | 8.7 | 8.8 | 0.0 | 0.270x | 1.023x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 8.9 | 8.9 | 8.9 | 0.0 | 0.272x | 1.031x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 8.9 | 8.9 | 8.9 | 0.0 | 0.273x | 1.031x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 32.5 | 32.5 | 33.3 | 0.3 | 1.000x | 3.784x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 38.7 | 37.4 | 43.6 | 2.6 | 1.191x | 4.505x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 59.2 | 58.9 | 60.3 | 0.6 | 1.821x | 6.889x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 62.2 | 60.1 | 66.6 | 2.3 | 1.911x | 7.231x |
| 9 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 64.1 | 59.4 | 64.4 | 2.0 | 1.970x | 7.452x |
| 10 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 64.7 | 63.5 | 66.2 | 1.0 | 1.987x | 7.520x |

### `floor` / `s-041` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.3 | 8.3 | 8.4 | 0.0 | 0.094x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.104x | 1.103x |
| 3 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.5 | 0.1 | 0.104x | 1.107x |
| 4 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.6 | 0.1 | 0.105x | 1.113x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.7 | 10.7 | 10.8 | 0.1 | 0.121x | 1.290x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.8 | 10.7 | 10.9 | 0.1 | 0.122x | 1.295x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.8 | 0.1 | 0.244x | 2.599x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.245x | 2.601x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 87.3 | 86.8 | 88.4 | 0.6 | 0.989x | 10.508x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 88.3 | 87.3 | 88.8 | 0.5 | 1.000x | 10.630x |

### `floor` / `s-041` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 14.2 | 14.2 | 14.2 | 0.0 | 0.140x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 14.2 | 14.2 | 16.9 | 1.3 | 0.140x | 1.004x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 16.5 | 16.5 | 16.6 | 0.0 | 0.163x | 1.166x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 16.6 | 16.5 | 16.7 | 0.0 | 0.163x | 1.166x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 17.3 | 17.2 | 17.6 | 0.1 | 0.171x | 1.220x |
| 6 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 17.4 | 17.2 | 17.5 | 0.1 | 0.172x | 1.229x |
| 7 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 17.5 | 17.3 | 18.3 | 0.3 | 0.173x | 1.236x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 17.9 | 17.4 | 22.8 | 2.0 | 0.176x | 1.259x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.1 | 43.9 | 51.4 | 2.7 | 0.444x | 3.178x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.5 | 99.8 | 102.7 | 1.1 | 1.000x | 7.155x |

### `floor` / `s-042` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.247x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.258x | 1.041x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.291x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.295x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.1 | 0.352x | 1.423x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.354x | 1.431x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 20.0 | 19.9 | 20.2 | 0.1 | 0.696x | 2.814x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.0 | 19.9 | 20.4 | 0.2 | 0.698x | 2.821x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.1 | 0.2 | 1.000x | 4.041x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 37.4 | 3.5 | 1.002x | 4.048x |

### `floor` / `s-042` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 17.6 | 17.5 | 18.0 | 0.2 | 0.174x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 17.6 | 17.4 | 17.6 | 0.1 | 0.174x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.1 | 0.174x | 1.001x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 17.7 | 17.6 | 18.3 | 0.3 | 0.175x | 1.008x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.3 | 25.5 | 28.2 | 1.0 | 0.261x | 1.499x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.6 | 26.4 | 28.9 | 0.9 | 0.264x | 1.517x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.8 | 27.4 | 33.1 | 2.2 | 0.275x | 1.583x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 29.8 | 26.9 | 37.4 | 3.9 | 0.295x | 1.695x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.9 | 44.1 | 51.5 | 2.4 | 0.464x | 2.671x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.1 | 100.6 | 102.1 | 0.6 | 1.000x | 5.754x |

### `floor` / `s-043` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.246x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.040x |
| 3 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.317x | 1.292x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.293x |
| 5 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.3 | 0.1 | 0.349x | 1.421x |
| 6 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.1 | 0.351x | 1.428x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.746x | 3.037x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.747x | 3.040x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 30.7 | 0.8 | 0.991x | 4.032x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 29.1 | 0.2 | 1.000x | 4.070x |

### `floor` / `s-043` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.3 | 18.1 | 18.6 | 0.2 | 0.180x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.4 | 18.2 | 18.6 | 0.2 | 0.181x | 1.008x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.7 | 18.4 | 19.0 | 0.2 | 0.184x | 1.027x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.9 | 18.3 | 19.2 | 0.3 | 0.186x | 1.033x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.9 | 44.0 | 47.1 | 1.0 | 0.452x | 2.515x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 50.3 | 50.2 | 51.3 | 0.4 | 0.495x | 2.754x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 50.9 | 50.8 | 51.0 | 0.1 | 0.500x | 2.785x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 51.9 | 51.5 | 55.2 | 1.7 | 0.510x | 2.841x |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 52.1 | 52.0 | 52.1 | 0.0 | 0.512x | 2.851x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.7 | 100.5 | 102.5 | 0.8 | 1.000x | 5.568x |

### `floor` / `s-044` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.2 | 0.0 | 0.246x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.040x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.317x | 1.291x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.294x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.0 | 10.2 | 0.1 | 0.350x | 1.424x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.4 | 0.1 | 0.352x | 1.430x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.748x | 3.040x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.749x | 3.044x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 30.7 | 0.8 | 0.998x | 4.059x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.5 | 29.0 | 0.2 | 1.000x | 4.066x |

### `floor` / `s-044` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.179x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.9 | 0.3 | 0.179x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.180x | 1.003x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.7 | 0.2 | 0.181x | 1.008x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 28.4 | 28.3 | 28.7 | 0.1 | 0.280x | 1.561x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 28.8 | 28.8 | 29.1 | 0.1 | 0.284x | 1.585x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 29.8 | 29.3 | 32.7 | 1.5 | 0.294x | 1.639x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 30.0 | 29.9 | 30.2 | 0.1 | 0.296x | 1.651x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.6 | 44.0 | 47.3 | 1.2 | 0.459x | 2.563x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.5 | 100.9 | 102.4 | 0.5 | 1.000x | 5.579x |

### `floor` / `s-045` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.247x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.041x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.291x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.6 | 0.2 | 0.320x | 1.295x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.1 | 0.352x | 1.426x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.1 | 0.353x | 1.426x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.0 | 0.752x | 3.043x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.7 | 21.6 | 22.9 | 0.5 | 0.756x | 3.061x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 32.9 | 1.7 | 1.000x | 4.046x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 30.7 | 0.7 | 1.006x | 4.071x |

### `floor` / `s-045` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.178x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.4 | 0.1 | 0.178x | 1.000x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.8 | 0.2 | 0.178x | 1.001x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.1 | 18.9 | 0.3 | 0.179x | 1.005x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 28.4 | 28.2 | 28.6 | 0.1 | 0.278x | 1.561x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 29.1 | 0.1 | 0.282x | 1.583x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 29.4 | 29.3 | 33.3 | 1.6 | 0.288x | 1.618x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 30.0 | 29.9 | 30.1 | 0.1 | 0.294x | 1.648x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.8 | 44.2 | 47.5 | 1.2 | 0.459x | 2.575x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.9 | 100.1 | 102.4 | 0.8 | 1.000x | 5.610x |

### `floor` / `s-046` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.246x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.0 | 0.256x | 1.041x |
| 3 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.293x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.318x | 1.293x |
| 5 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.1 | 0.350x | 1.423x |
| 6 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.2 | 0.1 | 0.352x | 1.433x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.749x | 3.044x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 22.4 | 0.3 | 0.751x | 3.051x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 29.3 | 0.2 | 1.000x | 4.065x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.0 | 28.8 | 31.0 | 0.8 | 1.005x | 4.083x |

### `floor` / `s-046` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.4 | 0.1 | 0.178x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.178x | 1.000x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.8 | 0.2 | 0.179x | 1.003x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.5 | 0.1 | 0.179x | 1.003x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.1 | 26.0 | 26.7 | 0.3 | 0.256x | 1.434x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.6 | 26.2 | 27.2 | 0.3 | 0.261x | 1.464x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 26.8 | 26.8 | 29.3 | 1.1 | 0.263x | 1.476x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.7 | 27.3 | 27.8 | 0.2 | 0.272x | 1.526x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 47.4 | 43.9 | 48.6 | 1.7 | 0.465x | 2.608x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.9 | 100.3 | 102.6 | 0.8 | 1.000x | 5.606x |

### `floor` / `s-047` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.245x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.255x | 1.041x |
| 3 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.317x | 1.293x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.317x | 1.294x |
| 5 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.1 | 0.351x | 1.431x |
| 6 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.2 | 0.0 | 0.351x | 1.433x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.1 | 0.746x | 3.040x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 22.0 | 0.2 | 0.747x | 3.045x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 30.6 | 0.7 | 0.996x | 4.063x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 29.1 | 0.2 | 1.000x | 4.077x |

### `floor` / `s-047` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.178x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.179x | 1.000x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 22.9 | 1.9 | 0.179x | 1.001x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.5 | 0.1 | 0.179x | 1.003x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.2 | 25.8 | 26.4 | 0.2 | 0.258x | 1.444x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.4 | 26.3 | 27.1 | 0.3 | 0.259x | 1.452x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.0 | 26.8 | 30.1 | 1.3 | 0.265x | 1.483x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.7 | 27.4 | 30.8 | 1.3 | 0.272x | 1.526x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 47.0 | 44.0 | 48.4 | 1.6 | 0.461x | 2.585x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.9 | 101.3 | 102.3 | 0.4 | 1.000x | 5.602x |

### `floor` / `s-048` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.2 | 0.0 | 0.248x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.258x | 1.040x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.289x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.291x |
| 5 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.1 | 0.352x | 1.422x |
| 6 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.1 | 0.354x | 1.427x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.6 | 18.5 | 19.1 | 0.2 | 0.650x | 2.623x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 19.1 | 18.9 | 20.2 | 0.5 | 0.665x | 2.681x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.9 | 0.1 | 1.000x | 4.034x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.8 | 30.7 | 0.8 | 1.006x | 4.059x |

### `floor` / `s-048` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.178x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.178x | 1.002x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.8 | 0.2 | 0.178x | 1.002x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.178x | 1.003x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.4 | 25.8 | 26.5 | 0.3 | 0.258x | 1.455x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.5 | 26.2 | 27.1 | 0.3 | 0.259x | 1.458x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.0 | 26.6 | 30.7 | 1.5 | 0.264x | 1.485x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.6 | 27.5 | 27.8 | 0.1 | 0.269x | 1.517x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.1 | 43.8 | 47.1 | 1.2 | 0.451x | 2.538x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 102.3 | 100.9 | 109.5 | 3.2 | 1.000x | 5.633x |

### `floor` / `s-049` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.2 | 0.0 | 0.246x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.040x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.4 | 0.1 | 0.318x | 1.293x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.6 | 0.2 | 0.318x | 1.294x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.1 | 0.350x | 1.424x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.1 | 0.350x | 1.425x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.8 | 0.1 | 0.747x | 3.039x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.7 | 21.6 | 22.5 | 0.4 | 0.750x | 3.052x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 30.8 | 0.8 | 0.998x | 4.062x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 31.4 | 1.0 | 1.000x | 4.068x |

### `floor` / `s-049` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.6 | 0.2 | 0.178x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.7 | 0.2 | 0.178x | 1.000x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 19.8 | 0.6 | 0.178x | 1.001x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.5 | 0.1 | 0.178x | 1.001x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.7 | 43.9 | 47.0 | 1.3 | 0.458x | 2.571x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 47.6 | 47.6 | 50.1 | 1.0 | 0.466x | 2.619x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 48.3 | 47.9 | 48.7 | 0.4 | 0.473x | 2.658x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 48.8 | 48.7 | 52.3 | 1.7 | 0.478x | 2.682x |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 49.1 | 48.8 | 49.3 | 0.1 | 0.481x | 2.699x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 102.1 | 100.0 | 103.3 | 1.1 | 1.000x | 5.616x |

### `floor` / `s-050` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.247x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.041x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.293x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.294x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.0 | 0.352x | 1.425x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.354x | 1.435x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 26.3 | 26.3 | 26.3 | 0.0 | 0.915x | 3.707x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 26.4 | 26.3 | 27.2 | 0.4 | 0.918x | 3.717x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 30.9 | 0.9 | 1.000x | 4.050x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 30.6 | 0.7 | 1.003x | 4.064x |

### `floor` / `s-050` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.178x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.7 | 0.2 | 0.178x | 1.002x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.178x | 1.003x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.8 | 0.2 | 0.179x | 1.004x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.1 | 25.5 | 26.3 | 0.3 | 0.256x | 1.439x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.2 | 26.1 | 26.3 | 0.1 | 0.256x | 1.441x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.2 | 26.8 | 30.9 | 1.8 | 0.266x | 1.496x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.5 | 27.4 | 27.7 | 0.1 | 0.270x | 1.515x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.3 | 44.1 | 46.8 | 0.9 | 0.444x | 2.495x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 102.1 | 100.1 | 102.1 | 0.8 | 1.000x | 5.622x |

### `floor` / `s-051` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.247x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.041x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.291x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.293x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.0 | 0.353x | 1.426x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.354x | 1.431x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.751x | 3.040x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.1 | 0.752x | 3.042x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.4 | 0.3 | 1.000x | 4.046x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.8 | 30.6 | 0.7 | 1.003x | 4.059x |

### `floor` / `s-051` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.0 | 0.179x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.7 | 0.2 | 0.179x | 1.000x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.179x | 1.001x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 19.5 | 0.5 | 0.179x | 1.002x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.4 | 43.9 | 46.7 | 0.9 | 0.446x | 2.497x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 47.6 | 47.4 | 47.8 | 0.1 | 0.468x | 2.617x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 47.9 | 47.8 | 48.1 | 0.1 | 0.471x | 2.633x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 48.9 | 48.7 | 52.7 | 1.8 | 0.480x | 2.686x |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 49.0 | 48.9 | 49.4 | 0.2 | 0.482x | 2.694x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.8 | 100.4 | 103.4 | 1.2 | 1.000x | 5.595x |

### `floor` / `s-052` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.246x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.0 | 0.256x | 1.040x |
| 3 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.317x | 1.290x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.317x | 1.291x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.0 | 0.350x | 1.423x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.3 | 0.1 | 0.351x | 1.429x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.747x | 3.039x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.748x | 3.042x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 30.7 | 0.8 | 0.995x | 4.046x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 29.6 | 0.4 | 1.000x | 4.068x |

### `floor` / `s-052` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.178x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.178x | 1.001x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.5 | 0.1 | 0.178x | 1.001x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.7 | 0.2 | 0.179x | 1.001x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.1 | 25.7 | 26.4 | 0.3 | 0.256x | 1.437x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.3 | 26.1 | 28.6 | 0.9 | 0.258x | 1.448x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.1 | 26.9 | 30.0 | 1.4 | 0.266x | 1.492x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.5 | 27.3 | 27.8 | 0.2 | 0.270x | 1.515x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.4 | 44.4 | 46.7 | 0.8 | 0.446x | 2.499x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.9 | 100.9 | 102.4 | 0.6 | 1.000x | 5.608x |

### `floor` / `s-053` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.2 | 0.0 | 0.247x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.040x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.291x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.6 | 0.2 | 0.319x | 1.294x |
| 5 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.0 | 0.351x | 1.423x |
| 6 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.1 | 0.351x | 1.424x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.749x | 3.037x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.749x | 3.039x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 30.7 | 0.8 | 1.000x | 4.055x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 29.3 | 0.3 | 1.000x | 4.056x |

### `floor` / `s-053` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.4 | 0.1 | 0.178x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.178x | 1.001x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.7 | 0.2 | 0.178x | 1.001x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.8 | 0.2 | 0.178x | 1.001x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.1 | 25.7 | 26.6 | 0.3 | 0.255x | 1.434x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.3 | 26.2 | 26.7 | 0.2 | 0.257x | 1.447x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 26.9 | 26.8 | 29.7 | 1.4 | 0.263x | 1.481x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.4 | 27.3 | 30.5 | 1.2 | 0.268x | 1.510x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.7 | 44.1 | 47.2 | 1.2 | 0.447x | 2.515x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 102.3 | 101.2 | 112.2 | 4.2 | 1.000x | 5.628x |

### `floor` / `s-054` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.247x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.040x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.319x | 1.291x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.1 | 9.2 | 0.0 | 0.320x | 1.293x |
| 5 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.4 | 0.1 | 0.352x | 1.424x |
| 6 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.0 | 0.353x | 1.426x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.0 | 0.752x | 3.039x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.9 | 0.1 | 0.752x | 3.041x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.8 | 0.1 | 1.000x | 4.043x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 30.5 | 0.7 | 1.008x | 4.075x |

### `floor` / `s-054` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.178x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.178x | 1.001x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 20.1 | 0.8 | 0.178x | 1.001x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 19.0 | 0.3 | 0.178x | 1.001x |
| 5 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.3 | 26.2 | 26.4 | 0.1 | 0.257x | 1.447x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.5 | 25.9 | 26.6 | 0.2 | 0.259x | 1.457x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.0 | 26.8 | 30.7 | 1.7 | 0.264x | 1.489x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.5 | 27.3 | 27.8 | 0.2 | 0.269x | 1.513x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.8 | 44.1 | 48.1 | 1.4 | 0.448x | 2.522x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 102.2 | 100.7 | 106.2 | 2.0 | 1.000x | 5.630x |

### `floor` / `s-055` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.248x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.1 | 0.258x | 1.042x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.321x | 1.293x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.321x | 1.295x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.0 | 0.354x | 1.426x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.3 | 0.1 | 0.355x | 1.432x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.755x | 3.043x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 27.2 | 2.2 | 0.755x | 3.043x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 29.0 | 0.2 | 1.000x | 4.031x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 30.9 | 0.9 | 1.006x | 4.055x |

### `floor` / `s-055` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.5 | 0.1 | 0.178x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.178x | 1.000x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 20.2 | 0.8 | 0.179x | 1.001x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.7 | 0.2 | 0.179x | 1.003x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.4 | 25.6 | 26.8 | 0.5 | 0.259x | 1.452x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.5 | 26.1 | 26.7 | 0.2 | 0.260x | 1.458x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.4 | 27.3 | 27.7 | 0.1 | 0.269x | 1.508x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.6 | 27.0 | 29.5 | 1.1 | 0.271x | 1.518x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.3 | 44.6 | 49.2 | 1.7 | 0.445x | 2.493x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.9 | 100.6 | 102.5 | 0.6 | 1.000x | 5.606x |

### `floor` / `s-056` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.246x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.041x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.293x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.294x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.1 | 0.349x | 1.422x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.352x | 1.431x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.747x | 3.041x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.747x | 3.042x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 30.7 | 0.7 | 0.999x | 4.066x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 29.0 | 0.1 | 1.000x | 4.070x |

### `floor` / `s-056` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.9 | 0.3 | 0.178x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.178x | 1.000x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.8 | 0.2 | 0.178x | 1.002x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.178x | 1.002x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.0 | 25.5 | 26.4 | 0.3 | 0.254x | 1.428x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.5 | 26.1 | 26.7 | 0.2 | 0.259x | 1.455x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.2 | 26.9 | 30.3 | 1.6 | 0.266x | 1.497x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.5 | 27.2 | 29.6 | 0.9 | 0.269x | 1.511x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.2 | 43.9 | 46.4 | 0.8 | 0.442x | 2.486x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 102.2 | 101.4 | 102.4 | 0.4 | 1.000x | 5.623x |

### `floor` / `s-057` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.2 | 0.0 | 0.247x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.040x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.4 | 0.1 | 0.319x | 1.292x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.319x | 1.293x |
| 5 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.4 | 0.1 | 0.351x | 1.425x |
| 6 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.353x | 1.432x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 29.0 | 0.2 | 1.000x | 4.055x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.9 | 30.7 | 0.7 | 1.005x | 4.075x |
| 9 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 160.0 | 159.8 | 160.8 | 0.3 | 5.555x | 22.526x |
| 10 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 160.1 | 159.7 | 160.6 | 0.3 | 5.559x | 22.544x |

### `floor` / `s-058` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.247x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.041x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.290x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.293x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.1 | 0.352x | 1.425x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.2 | 0.1 | 0.354x | 1.432x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 30.0 | 0.5 | 1.000x | 4.049x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.0 | 28.8 | 30.6 | 0.7 | 1.008x | 4.081x |
| 9 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 70.4 | 70.2 | 70.6 | 0.1 | 2.447x | 9.910x |
| 10 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 70.5 | 70.3 | 70.5 | 0.1 | 2.451x | 9.923x |

### `floor` / `s-059` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.246x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.041x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 10.7 | 0.6 | 0.318x | 1.290x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.295x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.1 | 0.352x | 1.428x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.3 | 0.1 | 0.352x | 1.429x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.8 | 30.6 | 0.7 | 1.000x | 4.057x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 29.2 | 0.3 | 1.000x | 4.058x |
| 9 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 91.1 | 90.8 | 92.5 | 0.7 | 3.162x | 12.833x |
| 10 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 91.4 | 91.0 | 91.7 | 0.3 | 3.172x | 12.872x |

### `floor` / `s-060` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.2 | 0.0 | 0.246x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.040x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.317x | 1.290x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.293x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.0 | 10.2 | 0.1 | 0.350x | 1.422x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 11.5 | 0.5 | 0.352x | 1.430x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.8 | 30.7 | 0.7 | 1.000x | 4.065x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 29.0 | 0.1 | 1.000x | 4.066x |
| 9 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 151.3 | 151.3 | 151.4 | 0.1 | 5.240x | 21.304x |
| 10 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 151.6 | 151.1 | 155.5 | 1.6 | 5.249x | 21.344x |

### `floor` / `s-061` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.248x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.0 | 0.258x | 1.041x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.290x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.4 | 0.1 | 0.322x | 1.298x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.3 | 0.1 | 0.354x | 1.426x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.355x | 1.433x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.6 | 29.0 | 0.2 | 1.000x | 4.034x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 30.7 | 0.7 | 1.007x | 4.061x |
| 9 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 43.0 | 42.9 | 43.1 | 0.1 | 1.502x | 6.061x |
| 10 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 43.4 | 42.9 | 44.4 | 0.6 | 1.515x | 6.110x |

### `floor` / `s-062` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.247x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.038x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.288x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.319x | 1.292x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.0 | 10.3 | 0.1 | 0.351x | 1.424x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.353x | 1.429x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 25.9 | 25.8 | 26.0 | 0.1 | 0.898x | 3.641x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 26.0 | 25.8 | 26.1 | 0.1 | 0.900x | 3.649x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.8 | 30.7 | 0.7 | 0.999x | 4.050x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 29.0 | 0.1 | 1.000x | 4.053x |

### `floor` / `s-063` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.246x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.041x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.291x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.293x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.3 | 0.1 | 0.351x | 1.427x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.353x | 1.434x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 30.7 | 0.8 | 1.000x | 4.059x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.4 | 0.3 | 1.000x | 4.060x |
| 9 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 92.6 | 92.3 | 93.3 | 0.4 | 3.213x | 13.047x |
| 10 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 92.9 | 91.7 | 93.3 | 0.6 | 3.226x | 13.100x |

### `floor` / `s-064` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.247x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.040x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.289x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.292x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.1 | 0.352x | 1.425x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.4 | 0.1 | 0.352x | 1.426x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.4 | 30.6 | 0.8 | 0.999x | 4.049x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 30.1 | 0.5 | 1.000x | 4.054x |
| 9 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 70.3 | 70.2 | 71.3 | 0.4 | 2.443x | 9.905x |
| 10 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 70.5 | 70.3 | 70.6 | 0.1 | 2.447x | 9.921x |

### `floor` / `s-065` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.2 | 0.0 | 0.246x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.255x | 1.039x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.317x | 1.289x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.6 | 0.2 | 0.317x | 1.290x |
| 5 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.5 | 0.2 | 0.351x | 1.427x |
| 6 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.2 | 0.0 | 0.352x | 1.430x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.9 | 21.6 | 23.5 | 0.8 | 0.758x | 3.086x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 22.8 | 22.6 | 23.0 | 0.2 | 0.789x | 3.210x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 31.0 | 0.9 | 0.996x | 4.052x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 30.1 | 0.6 | 1.000x | 4.068x |

### `floor` / `s-065` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.178x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.5 | 0.1 | 0.178x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.178x | 1.001x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.8 | 0.2 | 0.178x | 1.002x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.0 | 25.8 | 26.4 | 0.2 | 0.255x | 1.430x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.3 | 26.1 | 26.5 | 0.1 | 0.258x | 1.449x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.5 | 27.4 | 27.7 | 0.1 | 0.269x | 1.512x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.6 | 26.8 | 29.5 | 1.2 | 0.271x | 1.519x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.1 | 44.0 | 45.8 | 0.6 | 0.442x | 2.484x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 102.0 | 100.6 | 102.2 | 0.6 | 1.000x | 5.615x |

### `floor` / `s-066` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.244x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.254x | 1.040x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.315x | 1.290x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.315x | 1.291x |
| 5 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.0 | 10.4 | 0.1 | 0.348x | 1.425x |
| 6 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.351x | 1.437x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 23.4 | 0.8 | 0.744x | 3.044x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 22.5 | 21.9 | 22.6 | 0.2 | 0.774x | 3.168x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.8 | 30.7 | 0.7 | 0.992x | 4.062x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.1 | 28.9 | 29.4 | 0.2 | 1.000x | 4.094x |

### `floor` / `s-066` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.1 | 18.1 | 18.2 | 0.0 | 0.178x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.178x | 1.002x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.7 | 0.2 | 0.178x | 1.002x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.178x | 1.003x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 28.5 | 28.3 | 30.1 | 0.7 | 0.279x | 1.569x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.1 | 0.282x | 1.585x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 29.4 | 29.3 | 32.8 | 1.5 | 0.289x | 1.623x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 29.9 | 29.9 | 30.0 | 0.0 | 0.293x | 1.648x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.0 | 43.9 | 46.1 | 0.7 | 0.442x | 2.481x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 102.0 | 100.2 | 102.3 | 0.9 | 1.000x | 5.618x |

### `floor` / `s-067` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.247x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.039x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.288x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.289x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.1 | 0.353x | 1.427x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.0 | 0.353x | 1.427x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 23.0 | 0.6 | 0.751x | 3.040x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 22.4 | 21.6 | 22.5 | 0.4 | 0.780x | 3.157x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 29.0 | 0.2 | 1.000x | 4.046x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.8 | 30.7 | 0.8 | 1.002x | 4.053x |

### `floor` / `s-067` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.8 | 0.2 | 0.178x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.5 | 0.1 | 0.178x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.1 | 0.178x | 1.001x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.178x | 1.001x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.0 | 25.8 | 26.5 | 0.3 | 0.255x | 1.432x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.3 | 26.1 | 26.5 | 0.2 | 0.258x | 1.448x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.3 | 26.7 | 29.6 | 1.2 | 0.267x | 1.501x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.7 | 27.5 | 28.1 | 0.3 | 0.271x | 1.524x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.9 | 43.8 | 45.4 | 0.6 | 0.440x | 2.472x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 102.0 | 100.8 | 103.0 | 0.7 | 1.000x | 5.614x |

### `floor` / `s-068` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.246x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.0 | 0.257x | 1.041x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.292x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.294x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.0 | 0.351x | 1.425x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.3 | 0.1 | 0.352x | 1.428x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.8 | 0.1 | 0.750x | 3.044x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.8 | 21.6 | 22.5 | 0.4 | 0.758x | 3.076x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 28.9 | 0.1 | 1.000x | 4.057x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 30.7 | 0.7 | 1.001x | 4.060x |

### `floor` / `s-068` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 16.8 | 16.8 | 16.9 | 0.0 | 0.166x | 1.000x |
| 2 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 17.5 | 17.4 | 17.6 | 0.1 | 0.172x | 1.036x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.179x | 1.078x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.9 | 0.3 | 0.179x | 1.080x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.7 | 0.2 | 0.179x | 1.080x |
| 6 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.179x | 1.081x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 18.3 | 18.3 | 18.4 | 0.0 | 0.180x | 1.088x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 18.8 | 17.7 | 22.0 | 1.8 | 0.185x | 1.116x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.9 | 43.9 | 45.7 | 0.6 | 0.442x | 2.664x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.6 | 100.4 | 102.2 | 0.7 | 1.000x | 6.032x |

### `floor` / `s-069` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.2 | 0.0 | 0.245x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.0 | 0.257x | 1.048x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.317x | 1.293x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.6 | 0.2 | 0.318x | 1.294x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.0 | 0.351x | 1.429x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.353x | 1.437x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.2 | 0.1 | 0.798x | 3.251x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.1 | 23.1 | 0.0 | 0.798x | 3.252x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 30.7 | 0.7 | 1.000x | 4.072x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.4 | 29.1 | 0.2 | 1.000x | 4.074x |

### `floor` / `s-069` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.178x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.8 | 0.2 | 0.178x | 1.001x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.7 | 0.2 | 0.178x | 1.001x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.7 | 0.2 | 0.179x | 1.002x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 25.9 | 25.5 | 26.3 | 0.3 | 0.254x | 1.425x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.4 | 26.2 | 26.9 | 0.2 | 0.259x | 1.451x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 26.9 | 26.7 | 30.2 | 1.5 | 0.263x | 1.478x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.7 | 27.5 | 27.8 | 0.1 | 0.271x | 1.523x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.4 | 43.8 | 46.1 | 0.8 | 0.445x | 2.497x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 102.0 | 101.6 | 104.3 | 1.0 | 1.000x | 5.610x |

### `floor` / `s-070` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.2 | 0.0 | 0.247x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.040x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.319x | 1.290x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.293x |
| 5 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.3 | 0.1 | 0.351x | 1.421x |
| 6 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.2 | 0.1 | 0.353x | 1.430x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 22.3 | 0.3 | 0.752x | 3.043x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 22.0 | 21.6 | 22.6 | 0.4 | 0.766x | 3.098x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.9 | 0.1 | 1.000x | 4.046x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.8 | 30.6 | 0.7 | 1.007x | 4.075x |

### `floor` / `s-070` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 16.9 | 16.8 | 17.0 | 0.1 | 0.166x | 1.000x |
| 2 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 17.4 | 17.4 | 17.6 | 0.1 | 0.172x | 1.034x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.8 | 0.2 | 0.179x | 1.079x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.179x | 1.079x |
| 5 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.5 | 0.1 | 0.180x | 1.080x |
| 6 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.5 | 0.1 | 0.180x | 1.081x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 18.3 | 18.3 | 22.8 | 1.7 | 0.181x | 1.087x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 18.6 | 17.9 | 22.1 | 1.8 | 0.184x | 1.105x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.0 | 43.9 | 45.9 | 0.8 | 0.444x | 2.670x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.4 | 100.5 | 101.8 | 0.5 | 1.000x | 6.014x |

### `floor` / `s-071` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.247x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.041x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.1 | 0.319x | 1.291x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.296x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.0 | 0.352x | 1.428x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.2 | 0.0 | 0.353x | 1.432x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.9 | 0.1 | 0.752x | 3.045x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 22.4 | 21.6 | 22.5 | 0.4 | 0.780x | 3.162x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 29.1 | 0.2 | 1.000x | 4.052x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 30.7 | 0.8 | 1.007x | 4.079x |

### `floor` / `s-071` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.7 | 0.2 | 0.178x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.178x | 1.001x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.4 | 0.1 | 0.178x | 1.002x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.5 | 0.1 | 0.179x | 1.006x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.2 | 44.6 | 46.5 | 0.8 | 0.453x | 2.542x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 72.5 | 72.4 | 73.2 | 0.3 | 0.710x | 3.989x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 73.6 | 73.2 | 75.0 | 0.7 | 0.721x | 4.047x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 73.6 | 73.5 | 77.3 | 1.8 | 0.721x | 4.049x |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 74.1 | 74.0 | 74.3 | 0.1 | 0.726x | 4.078x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 102.1 | 100.9 | 102.8 | 0.7 | 1.000x | 5.617x |

### `floor` / `s-072` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.246x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.041x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.293x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.318x | 1.293x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.1 | 0.350x | 1.423x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.353x | 1.436x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.1 | 0.747x | 3.042x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.8 | 21.6 | 28.2 | 2.6 | 0.755x | 3.073x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.8 | 30.6 | 0.7 | 0.997x | 4.059x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.8 | 29.3 | 0.2 | 1.000x | 4.072x |

### `floor` / `s-072` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.6 | 0.1 | 0.179x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.8 | 0.2 | 0.179x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.179x | 1.001x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 19.5 | 0.5 | 0.180x | 1.004x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.5 | 43.9 | 46.1 | 1.0 | 0.449x | 2.505x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 58.6 | 58.5 | 59.1 | 0.2 | 0.578x | 3.224x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 59.7 | 59.2 | 60.3 | 0.4 | 0.589x | 3.285x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 60.0 | 59.7 | 63.5 | 1.7 | 0.591x | 3.297x |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 60.7 | 60.3 | 60.9 | 0.2 | 0.598x | 3.338x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.5 | 100.6 | 102.4 | 0.7 | 1.000x | 5.580x |

### `floor` / `s-073` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.2 | 0.0 | 0.247x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.041x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.290x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.6 | 0.2 | 0.319x | 1.294x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.1 | 0.352x | 1.425x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.2 | 0.1 | 0.355x | 1.436x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 22.5 | 0.3 | 0.751x | 3.041x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.751x | 3.042x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.2 | 0.2 | 1.000x | 4.050x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 30.6 | 0.7 | 1.004x | 4.067x |

### `floor` / `s-073` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.7 | 0.2 | 0.179x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.180x | 1.001x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.180x | 1.001x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.4 | 0.1 | 0.180x | 1.001x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 25.9 | 25.6 | 26.7 | 0.4 | 0.256x | 1.424x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.4 | 26.2 | 26.6 | 0.2 | 0.260x | 1.450x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.5 | 27.3 | 28.4 | 0.4 | 0.271x | 1.511x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 29.1 | 26.9 | 30.1 | 1.2 | 0.287x | 1.601x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.3 | 43.8 | 45.9 | 0.9 | 0.447x | 2.490x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.3 | 99.9 | 102.6 | 0.9 | 1.000x | 5.572x |

### `floor` / `s-074` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.246x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.256x | 1.040x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.292x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.293x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.3 | 0.1 | 0.350x | 1.424x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.353x | 1.435x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.8 | 0.1 | 0.748x | 3.040x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 22.5 | 0.4 | 0.748x | 3.043x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 30.9 | 0.9 | 0.999x | 4.063x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.5 | 29.5 | 0.4 | 1.000x | 4.066x |

### `floor` / `s-074` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.179x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.180x | 1.000x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.8 | 0.2 | 0.180x | 1.001x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.180x | 1.001x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.0 | 25.5 | 26.6 | 0.4 | 0.257x | 1.431x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.3 | 26.1 | 26.5 | 0.1 | 0.259x | 1.445x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.0 | 26.7 | 30.5 | 1.6 | 0.267x | 1.486x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.6 | 27.2 | 27.7 | 0.2 | 0.273x | 1.519x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.9 | 43.9 | 45.8 | 0.8 | 0.444x | 2.471x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.3 | 100.2 | 103.2 | 1.0 | 1.000x | 5.572x |

### `floor` / `s-075` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.247x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.040x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.290x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.294x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.3 | 0.1 | 0.352x | 1.422x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.355x | 1.436x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 22.5 | 0.4 | 0.752x | 3.040x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.752x | 3.041x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.3 | 0.3 | 1.000x | 4.042x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 30.7 | 0.8 | 1.005x | 4.064x |

### `floor` / `s-075` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.1 | 0.178x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.178x | 1.002x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.178x | 1.002x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.8 | 0.2 | 0.178x | 1.002x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.2 | 25.9 | 27.4 | 0.5 | 0.256x | 1.440x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.6 | 26.2 | 27.0 | 0.2 | 0.260x | 1.464x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.5 | 27.4 | 27.5 | 0.1 | 0.269x | 1.513x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 29.0 | 26.7 | 30.6 | 1.6 | 0.284x | 1.595x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.3 | 44.0 | 46.2 | 0.8 | 0.443x | 2.492x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 102.1 | 100.9 | 102.8 | 0.7 | 1.000x | 5.623x |

### `floor` / `s-076` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.247x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.041x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.293x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.295x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.1 | 0.351x | 1.424x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.4 | 0.1 | 0.352x | 1.428x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.0 | 0.751x | 3.045x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 22.0 | 0.2 | 0.752x | 3.046x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.2 | 0.2 | 1.000x | 4.053x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.5 | 30.6 | 0.7 | 1.005x | 4.072x |

### `floor` / `s-076` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.180x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.8 | 0.2 | 0.180x | 1.000x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.180x | 1.001x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.1 | 0.180x | 1.001x |
| 5 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.2 | 26.1 | 26.6 | 0.2 | 0.259x | 1.441x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.3 | 26.0 | 26.8 | 0.3 | 0.260x | 1.445x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.3 | 26.7 | 30.2 | 1.4 | 0.271x | 1.504x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.5 | 27.3 | 27.7 | 0.1 | 0.272x | 1.513x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.1 | 43.9 | 46.8 | 1.1 | 0.447x | 2.483x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.0 | 100.4 | 102.3 | 0.7 | 1.000x | 5.557x |

### `floor` / `s-077` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.2 | 0.0 | 0.248x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.258x | 1.040x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.290x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.321x | 1.294x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.1 | 0.353x | 1.422x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.4 | 0.1 | 0.354x | 1.426x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.754x | 3.038x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.8 | 0.1 | 0.754x | 3.039x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.6 | 29.0 | 0.2 | 1.000x | 4.031x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.5 | 30.6 | 0.8 | 1.009x | 4.067x |

### `floor` / `s-077` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.179x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.0 | 0.179x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 19.5 | 0.5 | 0.179x | 1.001x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.8 | 0.2 | 0.180x | 1.002x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.4 | 26.0 | 26.4 | 0.2 | 0.260x | 1.453x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.7 | 26.1 | 26.8 | 0.3 | 0.263x | 1.471x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 26.9 | 26.7 | 30.0 | 1.5 | 0.265x | 1.478x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.4 | 27.3 | 27.8 | 0.2 | 0.271x | 1.511x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.0 | 43.8 | 45.7 | 0.7 | 0.444x | 2.476x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.5 | 100.6 | 103.0 | 0.8 | 1.000x | 5.583x |

### `floor` / `s-078` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.246x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.0 | 0.256x | 1.040x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.292x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.318x | 1.294x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.1 | 0.351x | 1.425x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.2 | 0.353x | 1.436x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.0 | 0.747x | 3.037x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.0 | 0.749x | 3.042x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 30.6 | 0.7 | 0.998x | 4.058x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.5 | 30.2 | 0.6 | 1.000x | 4.064x |

### `floor` / `s-078` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.178x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.7 | 0.2 | 0.178x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.1 | 0.178x | 1.002x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 21.1 | 1.2 | 0.178x | 1.002x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.3 | 25.9 | 27.3 | 0.5 | 0.258x | 1.448x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.4 | 26.1 | 26.6 | 0.2 | 0.259x | 1.452x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 27.0 | 26.8 | 30.4 | 1.7 | 0.264x | 1.483x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.6 | 27.3 | 27.8 | 0.2 | 0.271x | 1.519x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.0 | 43.9 | 45.8 | 0.8 | 0.441x | 2.476x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 102.1 | 100.2 | 102.5 | 0.9 | 1.000x | 5.615x |

### `floor` / `s-079` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.247x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.257x | 1.041x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.295x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.4 | 0.1 | 0.320x | 1.297x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.1 | 0.352x | 1.427x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.354x | 1.435x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.750x | 3.039x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.751x | 3.043x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 29.0 | 0.2 | 1.000x | 4.055x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.8 | 30.8 | 0.8 | 1.002x | 4.061x |

### `floor` / `s-079` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.179x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.179x | 1.001x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.8 | 0.2 | 0.179x | 1.001x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.180x | 1.002x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.2 | 26.0 | 27.0 | 0.3 | 0.259x | 1.443x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.4 | 26.3 | 28.7 | 0.9 | 0.260x | 1.452x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 26.9 | 26.8 | 30.2 | 1.6 | 0.266x | 1.482x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.5 | 27.3 | 27.7 | 0.1 | 0.271x | 1.514x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.1 | 43.8 | 46.0 | 0.9 | 0.445x | 2.483x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.4 | 100.9 | 102.6 | 0.7 | 1.000x | 5.578x |

### `floor` / `s-080` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.1 | 0.0 | 0.248x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.258x | 1.040x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.320x | 1.292x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.320x | 1.292x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.2 | 0.0 | 0.353x | 1.428x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.355x | 1.435x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.6 | 0.0 | 0.752x | 3.039x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.7 | 0.1 | 0.753x | 3.041x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.1 | 0.2 | 1.000x | 4.040x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.8 | 30.5 | 0.7 | 1.006x | 4.064x |

### `floor` / `s-080` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.179x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.0 | 0.179x | 1.001x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.7 | 0.2 | 0.179x | 1.001x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.1 | 18.6 | 0.2 | 0.180x | 1.004x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 26.3 | 25.9 | 26.7 | 0.3 | 0.258x | 1.444x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.5 | 26.1 | 26.7 | 0.2 | 0.260x | 1.456x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 26.9 | 26.7 | 30.6 | 1.7 | 0.264x | 1.478x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 27.6 | 27.3 | 28.0 | 0.2 | 0.271x | 1.518x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.0 | 43.9 | 46.5 | 0.9 | 0.443x | 2.477x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.6 | 100.1 | 102.4 | 0.8 | 1.000x | 5.591x |

### `floor` / `s-081` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.0 | 8.0 | 8.0 | 0.0 | 0.279x | 1.000x |
| 2 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8.1 | 8.1 | 8.2 | 0.0 | 0.285x | 1.020x |
| 3 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 8.9 | 8.9 | 9.0 | 0.0 | 0.310x | 1.112x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.0 | 8.9 | 10.1 | 0.5 | 0.314x | 1.125x |
| 5 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.6 | 10.6 | 11.3 | 0.3 | 0.371x | 1.330x |
| 6 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.6 | 10.6 | 11.5 | 0.4 | 0.371x | 1.330x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.7 | 10.7 | 10.8 | 0.0 | 0.374x | 1.341x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.8 | 10.7 | 10.8 | 0.1 | 0.377x | 1.350x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 30.4 | 0.7 | 0.999x | 3.579x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 29.9 | 0.5 | 1.000x | 3.583x |

### `floor` / `s-081` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 6.3 | 6.3 | 6.5 | 0.1 | 0.197x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 6.4 | 6.3 | 6.5 | 0.1 | 0.198x | 1.004x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 6.7 | 6.6 | 6.7 | 0.0 | 0.207x | 1.049x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 6.7 | 6.6 | 6.7 | 0.0 | 0.208x | 1.056x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 10.0 | 9.9 | 10.9 | 0.4 | 0.311x | 1.579x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 10.2 | 10.2 | 12.2 | 0.8 | 0.317x | 1.609x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 10.2 | 10.2 | 10.9 | 0.3 | 0.318x | 1.613x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 13.9 | 9.2 | 14.2 | 2.3 | 0.431x | 2.186x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 32.2 | 32.2 | 32.3 | 0.0 | 1.000x | 5.071x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 40.2 | 37.4 | 45.1 | 3.0 | 1.249x | 6.335x |

### `floor` / `s-082` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 10.8 | 10.8 | 10.9 | 0.0 | 0.111x | 1.000x |
| 2 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 10.8 | 10.8 | 11.0 | 0.1 | 0.111x | 1.000x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 10.9 | 10.9 | 10.9 | 0.0 | 0.112x | 1.010x |
| 4 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 11.0 | 10.9 | 11.5 | 0.2 | 0.112x | 1.013x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.4 | 12.4 | 12.7 | 0.1 | 0.127x | 1.148x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.5 | 12.4 | 12.9 | 0.2 | 0.128x | 1.152x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 17.8 | 17.6 | 17.9 | 0.1 | 0.182x | 1.640x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.0 | 17.5 | 19.0 | 0.5 | 0.184x | 1.659x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 97.7 | 95.7 | 111.8 | 6.0 | 1.000x | 9.023x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 98.2 | 96.2 | 99.4 | 1.1 | 1.006x | 9.072x |

### `floor` / `s-082` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 14.2 | 14.2 | 16.9 | 1.3 | 0.139x | 1.000x |
| 2 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 14.4 | 14.2 | 14.6 | 0.1 | 0.142x | 1.016x |
| 3 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 16.5 | 16.5 | 16.6 | 0.0 | 0.162x | 1.166x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 16.5 | 16.5 | 16.5 | 0.0 | 0.163x | 1.166x |
| 5 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 16.9 | 16.8 | 17.1 | 0.1 | 0.166x | 1.191x |
| 6 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 17.0 | 17.0 | 17.0 | 0.0 | 0.167x | 1.199x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 17.1 | 16.9 | 17.3 | 0.1 | 0.168x | 1.205x |
| 8 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 17.1 | 17.0 | 17.3 | 0.1 | 0.168x | 1.208x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.8 | 43.9 | 45.6 | 0.6 | 0.440x | 3.156x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.8 | 100.0 | 102.6 | 0.9 | 1.000x | 7.175x |

### `floor` / `s-083` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.7 | 0.2 | 0.248x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.5 | 0.0 | 0.258x | 1.043x |
| 3 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.319x | 1.289x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.3 | 0.0 | 0.319x | 1.290x |
| 5 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.5 | 0.2 | 0.353x | 1.425x |
| 6 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.355x | 1.435x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 17.4 | 17.4 | 17.5 | 0.0 | 0.607x | 2.450x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 17.4 | 17.4 | 17.5 | 0.0 | 0.607x | 2.451x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.2 | 0.2 | 1.000x | 4.040x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.0 | 28.8 | 30.7 | 0.7 | 1.008x | 4.071x |

### `floor` / `s-083` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 9.5 | 9.5 | 10.1 | 0.3 | 0.282x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 9.7 | 9.5 | 10.1 | 0.3 | 0.288x | 1.021x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 9.9 | 9.7 | 10.1 | 0.1 | 0.294x | 1.042x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 10.1 | 10.0 | 10.1 | 0.0 | 0.300x | 1.062x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 33.6 | 33.2 | 33.7 | 0.2 | 1.000x | 3.547x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 38.2 | 36.0 | 45.1 | 3.1 | 1.138x | 4.035x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 134.1 | 132.9 | 135.4 | 0.8 | 3.992x | 14.161x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 136.7 | 135.1 | 157.5 | 9.6 | 4.068x | 14.430x |
| 9 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 139.2 | 134.7 | 154.6 | 6.9 | 4.144x | 14.697x |
| 10 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 139.6 | 135.7 | 154.3 | 6.8 | 4.156x | 14.739x |

### `floor` / `s-084` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.1 | 7.1 | 7.4 | 0.1 | 0.245x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7.4 | 7.4 | 7.4 | 0.0 | 0.255x | 1.041x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.316x | 1.292x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 0.317x | 1.294x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 10.1 | 10.4 | 0.1 | 0.350x | 1.428x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.2 | 0.1 | 0.351x | 1.431x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.8 | 16.8 | 17.3 | 0.2 | 0.582x | 2.374x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.9 | 16.9 | 17.6 | 0.3 | 0.584x | 2.384x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 30.7 | 0.8 | 0.995x | 4.062x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.0 | 28.6 | 29.5 | 0.3 | 1.000x | 4.081x |

### `floor` / `s-084` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 8.6 | 8.6 | 9.4 | 0.3 | 0.265x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 8.8 | 8.7 | 9.3 | 0.2 | 0.269x | 1.015x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 8.9 | 8.9 | 9.0 | 0.1 | 0.273x | 1.031x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 9.2 | 8.9 | 9.2 | 0.1 | 0.282x | 1.062x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 32.5 | 32.5 | 32.5 | 0.0 | 1.000x | 3.771x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 37.7 | 36.6 | 43.9 | 2.7 | 1.161x | 4.378x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 45.8 | 45.6 | 51.0 | 2.1 | 1.409x | 5.312x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 45.8 | 45.8 | 46.0 | 0.1 | 1.409x | 5.314x |
| 9 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 46.0 | 45.9 | 47.4 | 0.6 | 1.416x | 5.337x |
| 10 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 49.9 | 45.2 | 50.5 | 2.5 | 1.536x | 5.793x |

### `floor` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 627,186.7 | 627,062.8 | 630,211.1 | 1,203.0 | 0.175x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 628,359.3 | 627,435.5 | 630,542.6 | 1,091.9 | 0.175x | 1.002x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 628,374.4 | 627,772.5 | 628,485.8 | 314.7 | 0.175x | 1.002x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 628,561.1 | 627,369.0 | 629,963.1 | 844.7 | 0.176x | 1.002x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,702,577.5 | 1,672,784.2 | 1,736,745.3 | 24,047.7 | 0.475x | 2.715x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,580,885.0 | 3,554,626.1 | 3,658,302.9 | 36,816.2 | 1.000x | 5.709x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 3,908,618.9 | 3,903,859.5 | 3,957,670.5 | 20,438.8 | 1.092x | 6.232x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 3,943,119.2 | 3,876,429.5 | 3,959,099.3 | 31,217.6 | 1.101x | 6.287x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 4,021,540.8 | 4,009,753.5 | 4,048,849.3 | 13,352.4 | 1.123x | 6.412x |
| 10 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 4,074,182.9 | 4,050,733.8 | 4,079,345.7 | 10,216.0 | 1.138x | 6.496x |

### `floor` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 17,675.4 | 17,639.8 | 17,680.1 | 14.9 | 0.993x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 17,692.3 | 17,667.4 | 17,717.5 | 19.4 | 0.993x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 17,705.1 | 17,661.1 | 17,974.2 | 113.6 | 0.994x | 1.002x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 17,720.6 | 17,691.9 | 17,756.5 | 22.8 | 0.995x | 1.003x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,808.9 | 17,727.2 | 17,827.0 | 39.8 | 1.000x | 1.008x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 39,329.9 | 38,994.9 | 39,949.1 | 362.3 | 2.208x | 2.225x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 2,790,208.5 | 2,789,990.7 | 2,793,229.1 | 1,208.0 | 156.675x | 157.859x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 2,793,280.9 | 2,790,804.1 | 2,834,053.8 | 16,716.0 | 156.848x | 158.032x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 2,857,535.9 | 2,802,809.4 | 3,408,016.5 | 251,332.5 | 160.456x | 161.668x |
| 10 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 3,409,032.7 | 3,033,678.5 | 3,410,841.4 | 172,512.0 | 191.423x | 192.869x |

### `floor` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 17,662.8 | 17,621.9 | 17,702.3 | 25.9 | 0.993x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 17,679.6 | 17,662.7 | 17,715.0 | 18.7 | 0.994x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 17,705.9 | 17,663.6 | 17,910.7 | 89.5 | 0.995x | 1.002x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 17,715.6 | 17,690.9 | 17,733.2 | 16.3 | 0.996x | 1.003x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,791.6 | 17,732.2 | 17,851.2 | 43.3 | 1.000x | 1.007x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 39,953.9 | 39,160.5 | 40,201.3 | 369.9 | 2.246x | 2.262x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 2,790,569.1 | 2,789,820.2 | 2,812,500.8 | 8,845.5 | 156.847x | 157.991x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 2,790,950.1 | 2,790,291.5 | 2,816,695.7 | 10,419.9 | 156.869x | 158.013x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 2,799,047.8 | 2,788,267.1 | 2,846,918.1 | 21,810.6 | 157.324x | 158.471x |
| 10 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 2,811,404.5 | 2,791,783.1 | 3,411,658.7 | 237,500.1 | 158.018x | 159.171x |

### `floor` / `t-d-prose-sparse-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 30,813.1 | 30,673.5 | 30,904.7 | 75.0 | 0.437x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 30,857.2 | 30,793.9 | 31,189.8 | 145.9 | 0.438x | 1.001x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 30,868.6 | 30,835.5 | 30,908.6 | 26.9 | 0.438x | 1.002x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 30,873.3 | 30,758.4 | 30,996.8 | 81.5 | 0.438x | 1.002x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 69,364.2 | 68,840.2 | 70,092.1 | 491.3 | 0.985x | 2.251x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 70,450.4 | 70,112.1 | 70,796.6 | 216.5 | 1.000x | 2.286x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 3,345,865.5 | 3,336,187.4 | 3,370,228.3 | 12,544.3 | 47.493x | 108.586x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 3,359,601.7 | 3,335,541.6 | 3,521,136.1 | 69,182.3 | 47.687x | 109.031x |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 3,371,357.6 | 3,351,732.4 | 3,382,219.3 | 10,609.7 | 47.854x | 109.413x |
| 10 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 3,378,161.3 | 3,323,300.4 | 3,389,864.1 | 25,590.7 | 47.951x | 109.634x |

### `floor` / `t-e-prose-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 17,686.9 | 17,632.4 | 17,694.7 | 23.5 | 0.992x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 17,687.2 | 17,657.9 | 17,778.4 | 44.2 | 0.992x | 1.000x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 17,700.7 | 17,669.5 | 17,931.5 | 102.7 | 0.993x | 1.001x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 17,711.8 | 17,647.0 | 17,760.4 | 39.7 | 0.993x | 1.001x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,829.2 | 17,766.0 | 17,852.0 | 35.2 | 1.000x | 1.008x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 39,673.0 | 39,231.8 | 40,199.7 | 352.8 | 2.225x | 2.243x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 2,793,313.5 | 2,789,369.1 | 2,821,194.2 | 11,634.5 | 156.670x | 157.931x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 2,823,491.0 | 2,790,294.9 | 3,213,887.3 | 163,265.3 | 158.363x | 159.637x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 3,210,584.2 | 2,894,852.8 | 3,294,433.0 | 156,686.2 | 180.074x | 181.523x |
| 10 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 3,411,499.4 | 3,230,465.7 | 3,412,547.4 | 72,246.8 | 191.343x | 192.883x |

### `orig` / `s-000` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.5 | 32.4 | 32.7 | 0.1 | 0.059x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.7 | 32.6 | 36.5 | 1.5 | 0.059x | 1.004x |
| 3 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 44.4 | 43.8 | 44.8 | 0.3 | 0.081x | 1.363x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 44.4 | 44.4 | 44.8 | 0.2 | 0.081x | 1.366x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 47.0 | 46.8 | 49.9 | 1.2 | 0.085x | 1.445x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 62.5 | 62.0 | 63.1 | 0.4 | 0.114x | 1.921x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 69.3 | 69.2 | 69.7 | 0.2 | 0.126x | 2.131x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 69.8 | 69.2 | 70.3 | 0.4 | 0.127x | 2.144x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 550.7 | 546.8 | 596.4 | 19.4 | 1.000x | 16.924x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 555.2 | 543.5 | 557.1 | 6.0 | 1.008x | 17.062x |

### `orig` / `s-000` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 53.2 | 52.9 | 54.1 | 0.4 | 0.096x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 55.0 | 54.1 | 55.4 | 0.5 | 0.099x | 1.034x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 58.5 | 58.5 | 58.7 | 0.1 | 0.106x | 1.100x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 58.6 | 58.5 | 59.4 | 0.3 | 0.106x | 1.102x |
| 5 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 58.6 | 58.4 | 58.8 | 0.2 | 0.106x | 1.102x |
| 6 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 58.7 | 58.6 | 59.3 | 0.3 | 0.106x | 1.103x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 69.9 | 69.8 | 70.7 | 0.3 | 0.126x | 1.313x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 74.0 | 73.8 | 74.3 | 0.2 | 0.134x | 1.391x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 78.1 | 76.5 | 83.3 | 2.4 | 0.141x | 1.468x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 553.7 | 541.1 | 559.5 | 6.3 | 1.000x | 10.408x |

### `orig` / `s-001` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 40.0 | 39.9 | 41.7 | 0.7 | 0.052x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 40.1 | 39.9 | 40.3 | 0.1 | 0.052x | 1.002x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 84.5 | 84.4 | 84.9 | 0.2 | 0.110x | 2.109x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 85.4 | 84.3 | 85.8 | 0.6 | 0.111x | 2.133x |
| 5 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 89.9 | 89.7 | 90.4 | 0.3 | 0.117x | 2.246x |
| 6 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 90.3 | 89.6 | 90.6 | 0.3 | 0.118x | 2.254x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 91.0 | 90.4 | 91.1 | 0.2 | 0.119x | 2.272x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 95.9 | 94.9 | 96.3 | 0.5 | 0.125x | 2.395x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 765.4 | 756.8 | 772.3 | 5.3 | 0.997x | 19.112x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 767.6 | 763.1 | 791.2 | 10.1 | 1.000x | 19.168x |

### `orig` / `s-001` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 77.7 | 77.6 | 77.7 | 0.1 | 0.102x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 77.7 | 77.7 | 77.9 | 0.1 | 0.102x | 1.000x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 77.9 | 77.7 | 78.2 | 0.2 | 0.102x | 1.002x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 77.9 | 77.7 | 78.1 | 0.1 | 0.102x | 1.002x |
| 5 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 86.8 | 85.3 | 88.0 | 0.9 | 0.114x | 1.116x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 87.2 | 86.8 | 87.7 | 0.3 | 0.114x | 1.122x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 90.7 | 90.6 | 90.9 | 0.1 | 0.119x | 1.167x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 92.9 | 92.7 | 93.0 | 0.1 | 0.122x | 1.195x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 94.0 | 91.7 | 96.3 | 1.7 | 0.123x | 1.210x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 763.1 | 756.4 | 775.4 | 7.4 | 1.000x | 9.819x |

### `orig` / `s-002` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 18.3 | 18.2 | 18.3 | 0.0 | 0.038x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.3 | 18.3 | 18.4 | 0.0 | 0.038x | 1.001x |
| 3 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 30.3 | 30.1 | 30.8 | 0.2 | 0.063x | 1.661x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 30.4 | 30.1 | 30.5 | 0.1 | 0.063x | 1.666x |
| 5 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.9 | 32.7 | 35.4 | 1.0 | 0.068x | 1.803x |
| 6 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.2 | 33.1 | 33.5 | 0.1 | 0.068x | 1.819x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 33.3 | 33.1 | 35.4 | 0.9 | 0.069x | 1.822x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 33.3 | 33.1 | 33.5 | 0.1 | 0.069x | 1.827x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 479.3 | 470.7 | 530.4 | 21.5 | 0.988x | 26.254x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 485.1 | 477.8 | 549.3 | 26.9 | 1.000x | 26.574x |

### `orig` / `s-002` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 26.0 | 25.9 | 26.2 | 0.1 | 0.054x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 26.0 | 26.0 | 26.6 | 0.2 | 0.054x | 1.001x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 26.2 | 26.0 | 26.5 | 0.2 | 0.054x | 1.008x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 26.2 | 26.0 | 26.5 | 0.2 | 0.054x | 1.008x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 37.9 | 37.9 | 38.0 | 0.1 | 0.079x | 1.459x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 38.4 | 38.4 | 38.9 | 0.2 | 0.080x | 1.479x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 45.3 | 45.2 | 45.7 | 0.2 | 0.094x | 1.743x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 54.8 | 54.6 | 54.9 | 0.1 | 0.114x | 2.109x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 63.9 | 62.4 | 70.6 | 3.0 | 0.132x | 2.458x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 482.5 | 477.8 | 495.6 | 6.3 | 1.000x | 18.564x |

### `orig` / `s-003` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 43.3 | 43.2 | 43.5 | 0.1 | 0.056x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 43.5 | 43.1 | 44.2 | 0.4 | 0.056x | 1.004x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 57.8 | 57.5 | 59.7 | 0.8 | 0.075x | 1.333x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 59.8 | 59.2 | 61.9 | 1.1 | 0.077x | 1.380x |
| 5 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 76.2 | 75.8 | 76.6 | 0.3 | 0.098x | 1.758x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 77.8 | 77.4 | 78.5 | 0.4 | 0.101x | 1.796x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 97.3 | 96.6 | 99.6 | 1.1 | 0.126x | 2.244x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 97.3 | 97.0 | 98.1 | 0.4 | 0.126x | 2.245x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 763.4 | 760.1 | 778.3 | 7.4 | 0.987x | 17.614x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 773.6 | 756.6 | 793.7 | 16.1 | 1.000x | 17.848x |

### `orig` / `s-003` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 65.9 | 63.6 | 66.8 | 1.2 | 0.086x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 67.4 | 67.3 | 70.4 | 1.2 | 0.088x | 1.023x |
| 3 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 75.2 | 74.3 | 80.0 | 2.1 | 0.098x | 1.142x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 85.3 | 84.8 | 87.5 | 0.9 | 0.111x | 1.295x |
| 5 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 86.4 | 86.2 | 87.2 | 0.4 | 0.113x | 1.311x |
| 6 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 86.6 | 86.2 | 87.4 | 0.5 | 0.113x | 1.313x |
| 7 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 86.6 | 86.6 | 88.0 | 0.5 | 0.113x | 1.314x |
| 8 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 86.9 | 86.6 | 87.1 | 0.2 | 0.113x | 1.318x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 94.4 | 91.9 | 98.0 | 2.0 | 0.123x | 1.432x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 766.6 | 761.2 | 822.8 | 22.9 | 1.000x | 11.632x |

### `orig` / `s-004` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 57.9 | 57.8 | 58.2 | 0.2 | 0.103x | 1.000x |
| 2 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 58.1 | 57.1 | 59.2 | 0.7 | 0.103x | 1.003x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 61.1 | 61.0 | 63.0 | 0.8 | 0.109x | 1.056x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 61.1 | 60.2 | 62.4 | 0.7 | 0.109x | 1.056x |
| 5 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 61.4 | 61.0 | 65.5 | 1.7 | 0.109x | 1.061x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 75.7 | 75.3 | 75.9 | 0.2 | 0.134x | 1.307x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 131.9 | 131.1 | 132.5 | 0.5 | 0.234x | 2.278x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 132.5 | 131.7 | 132.6 | 0.3 | 0.235x | 2.289x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 562.0 | 556.9 | 569.4 | 4.0 | 0.998x | 9.706x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 563.3 | 559.0 | 592.8 | 12.5 | 1.000x | 9.729x |

### `orig` / `s-004` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 66.2 | 64.4 | 66.4 | 0.8 | 0.118x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 68.8 | 67.5 | 69.4 | 0.6 | 0.122x | 1.038x |
| 3 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 79.7 | 78.3 | 88.5 | 3.7 | 0.142x | 1.204x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 92.1 | 91.1 | 99.3 | 3.0 | 0.164x | 1.391x |
| 5 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 93.0 | 92.8 | 93.7 | 0.3 | 0.165x | 1.405x |
| 6 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 120.1 | 119.8 | 120.3 | 0.2 | 0.214x | 1.814x |
| 7 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 120.2 | 119.9 | 121.1 | 0.4 | 0.214x | 1.815x |
| 8 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 120.4 | 120.3 | 121.5 | 0.4 | 0.214x | 1.819x |
| 9 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 120.5 | 119.8 | 120.8 | 0.4 | 0.214x | 1.820x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 562.1 | 558.3 | 567.8 | 3.2 | 1.000x | 8.490x |

### `orig` / `s-005` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 18.3 | 18.2 | 19.2 | 0.4 | 0.038x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.4 | 18.3 | 19.3 | 0.4 | 0.038x | 1.004x |
| 3 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 30.3 | 30.3 | 30.6 | 0.1 | 0.063x | 1.655x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 30.5 | 30.3 | 31.1 | 0.4 | 0.064x | 1.666x |
| 5 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.0 | 32.9 | 33.3 | 0.2 | 0.069x | 1.804x |
| 6 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33.2 | 32.9 | 35.1 | 0.8 | 0.069x | 1.812x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 33.3 | 33.3 | 35.3 | 0.8 | 0.070x | 1.821x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 33.3 | 33.2 | 33.7 | 0.2 | 0.070x | 1.822x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 477.0 | 471.9 | 478.8 | 2.9 | 0.998x | 26.068x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 478.2 | 471.5 | 545.5 | 27.3 | 1.000x | 26.133x |

### `orig` / `s-005` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 26.0 | 25.9 | 26.6 | 0.2 | 0.054x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 26.1 | 25.9 | 26.2 | 0.1 | 0.054x | 1.002x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 26.1 | 26.1 | 26.2 | 0.0 | 0.054x | 1.005x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 26.2 | 26.1 | 27.0 | 0.4 | 0.054x | 1.006x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 38.1 | 37.7 | 38.9 | 0.4 | 0.079x | 1.466x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 38.7 | 38.5 | 39.1 | 0.3 | 0.080x | 1.486x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 45.3 | 45.2 | 47.7 | 1.0 | 0.094x | 1.741x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 54.8 | 54.7 | 55.2 | 0.2 | 0.113x | 2.107x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 64.8 | 62.8 | 70.8 | 2.8 | 0.134x | 2.490x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 483.3 | 476.7 | 488.4 | 4.0 | 1.000x | 18.582x |

### `orig` / `s-006` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 31.0 | 30.9 | 31.0 | 0.0 | 0.039x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.1 | 30.9 | 32.4 | 0.5 | 0.040x | 1.004x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 65.5 | 65.0 | 66.1 | 0.4 | 0.083x | 2.113x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 65.8 | 65.4 | 67.2 | 0.6 | 0.084x | 2.123x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 95.5 | 94.6 | 98.1 | 1.2 | 0.122x | 3.081x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 95.8 | 95.1 | 96.4 | 0.4 | 0.122x | 3.090x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 110.9 | 110.6 | 112.6 | 0.7 | 0.141x | 3.578x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 113.1 | 111.8 | 114.1 | 0.8 | 0.144x | 3.648x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 780.2 | 770.5 | 794.6 | 7.7 | 0.993x | 25.170x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 785.6 | 774.7 | 854.2 | 28.6 | 1.000x | 25.344x |

### `orig` / `s-006` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 55.5 | 55.2 | 55.8 | 0.2 | 0.071x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 55.6 | 55.6 | 55.8 | 0.1 | 0.071x | 1.002x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 55.8 | 55.8 | 56.0 | 0.1 | 0.071x | 1.005x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 55.8 | 55.8 | 55.9 | 0.1 | 0.071x | 1.006x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 84.2 | 82.8 | 89.8 | 2.5 | 0.107x | 1.517x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 132.3 | 131.1 | 133.8 | 0.9 | 0.169x | 2.383x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 133.4 | 132.2 | 134.8 | 0.8 | 0.170x | 2.403x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 138.0 | 137.0 | 141.8 | 1.8 | 0.176x | 2.486x |
| 9 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 139.3 | 136.5 | 158.4 | 8.0 | 0.177x | 2.510x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 785.0 | 775.5 | 797.5 | 7.7 | 1.000x | 14.140x |

### `orig` / `s-007` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 46.8 | 46.6 | 46.9 | 0.1 | 0.075x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 46.9 | 46.8 | 51.1 | 1.6 | 0.075x | 1.002x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 53.1 | 52.6 | 53.7 | 0.4 | 0.085x | 1.135x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 55.5 | 55.1 | 58.1 | 1.1 | 0.089x | 1.185x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 65.4 | 65.2 | 66.9 | 0.6 | 0.104x | 1.397x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 71.0 | 70.0 | 71.7 | 0.5 | 0.114x | 1.518x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 102.4 | 101.9 | 103.2 | 0.5 | 0.164x | 2.188x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 102.8 | 102.6 | 103.1 | 0.2 | 0.164x | 2.197x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 621.4 | 611.6 | 634.5 | 8.0 | 0.993x | 13.282x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 625.9 | 613.8 | 640.0 | 10.0 | 1.000x | 13.377x |

### `orig` / `s-007` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 61.8 | 61.6 | 62.4 | 0.3 | 0.100x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 64.3 | 63.7 | 65.5 | 0.7 | 0.104x | 1.041x |
| 3 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 76.5 | 75.8 | 76.8 | 0.4 | 0.124x | 1.237x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 78.9 | 78.3 | 79.5 | 0.4 | 0.128x | 1.276x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 90.0 | 86.8 | 98.7 | 4.5 | 0.146x | 1.455x |
| 6 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 92.0 | 91.6 | 92.4 | 0.3 | 0.149x | 1.488x |
| 7 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 92.0 | 91.9 | 92.8 | 0.3 | 0.149x | 1.489x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 92.1 | 91.8 | 92.1 | 0.1 | 0.149x | 1.489x |
| 9 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 92.2 | 92.0 | 93.0 | 0.4 | 0.150x | 1.491x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 616.1 | 612.7 | 627.1 | 5.3 | 1.000x | 9.968x |

### `orig` / `s-008` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 36.7 | 36.7 | 36.8 | 0.0 | 0.068x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.5 | 36.7 | 46.7 | 3.7 | 0.069x | 1.022x |
| 3 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 46.4 | 46.0 | 46.5 | 0.2 | 0.085x | 1.264x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 46.5 | 46.2 | 46.6 | 0.1 | 0.086x | 1.267x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 48.9 | 48.7 | 51.6 | 1.1 | 0.090x | 1.335x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 64.3 | 63.6 | 66.0 | 0.9 | 0.118x | 1.752x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 80.5 | 80.3 | 80.9 | 0.2 | 0.148x | 2.195x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 80.5 | 80.3 | 80.6 | 0.1 | 0.148x | 2.196x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 540.6 | 538.4 | 548.0 | 3.5 | 0.996x | 14.741x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 542.6 | 537.9 | 562.2 | 9.7 | 1.000x | 14.794x |

### `orig` / `s-008` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 55.6 | 54.0 | 56.4 | 0.8 | 0.102x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 56.8 | 56.4 | 57.9 | 0.5 | 0.104x | 1.022x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 69.6 | 69.3 | 70.0 | 0.2 | 0.128x | 1.251x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 69.6 | 69.4 | 69.7 | 0.1 | 0.128x | 1.251x |
| 5 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 69.7 | 69.6 | 71.6 | 0.7 | 0.128x | 1.254x |
| 6 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 70.2 | 69.6 | 72.4 | 1.0 | 0.129x | 1.262x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 71.9 | 71.5 | 72.5 | 0.4 | 0.132x | 1.294x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 75.9 | 75.5 | 76.6 | 0.4 | 0.140x | 1.365x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 79.7 | 79.0 | 85.5 | 2.4 | 0.147x | 1.434x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 543.6 | 532.6 | 545.4 | 5.2 | 1.000x | 9.776x |

### `orig` / `s-009` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.7 | 0.1 | 0.055x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.7 | 29.6 | 32.2 | 1.0 | 0.056x | 1.003x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 42.5 | 42.3 | 42.9 | 0.2 | 0.079x | 1.436x |
| 4 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 42.7 | 42.5 | 42.7 | 0.1 | 0.080x | 1.441x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 45.3 | 45.3 | 47.5 | 0.8 | 0.085x | 1.531x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 61.0 | 60.2 | 64.7 | 1.6 | 0.114x | 2.061x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 61.8 | 61.6 | 61.9 | 0.1 | 0.116x | 2.087x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 62.0 | 61.8 | 62.2 | 0.1 | 0.116x | 2.094x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 535.2 | 534.5 | 560.0 | 11.9 | 1.000x | 18.072x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 536.8 | 529.4 | 548.7 | 6.4 | 1.003x | 18.129x |

### `orig` / `s-009` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 50.9 | 49.0 | 51.3 | 0.8 | 0.095x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 51.3 | 51.3 | 51.6 | 0.1 | 0.095x | 1.009x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 51.4 | 51.3 | 52.2 | 0.3 | 0.096x | 1.010x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 51.5 | 51.4 | 51.6 | 0.0 | 0.096x | 1.011x |
| 5 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 51.5 | 51.4 | 51.9 | 0.2 | 0.096x | 1.012x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 52.6 | 52.3 | 53.0 | 0.2 | 0.098x | 1.034x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 67.6 | 67.4 | 70.5 | 1.1 | 0.126x | 1.329x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 71.6 | 71.1 | 72.6 | 0.5 | 0.133x | 1.407x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 74.4 | 74.1 | 81.3 | 2.7 | 0.138x | 1.462x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 537.9 | 530.7 | 541.5 | 3.7 | 1.000x | 10.570x |

### `orig` / `s-010` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.6 | 0.0 | 0.067x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.5 | 32.9 | 1.3 | 0.067x | 1.001x |
| 3 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 30.9 | 30.8 | 33.8 | 1.2 | 0.070x | 1.043x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 31.0 | 30.8 | 32.2 | 0.5 | 0.071x | 1.048x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 32.9 | 32.5 | 34.7 | 0.8 | 0.075x | 1.113x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 32.9 | 32.9 | 36.5 | 1.4 | 0.075x | 1.114x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 62.1 | 62.0 | 62.2 | 0.1 | 0.142x | 2.101x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 62.1 | 61.7 | 62.9 | 0.4 | 0.142x | 2.101x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 434.0 | 425.4 | 563.1 | 53.3 | 0.989x | 14.676x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 438.7 | 429.3 | 479.1 | 17.7 | 1.000x | 14.835x |

### `orig` / `s-010` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 36.3 | 35.8 | 38.6 | 1.0 | 0.083x | 1.000x |
| 2 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 36.6 | 36.2 | 37.6 | 0.5 | 0.084x | 1.008x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 37.8 | 37.6 | 38.3 | 0.3 | 0.086x | 1.041x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 51.5 | 51.3 | 51.7 | 0.1 | 0.118x | 1.417x |
| 5 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 51.5 | 51.3 | 51.7 | 0.1 | 0.118x | 1.417x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 51.5 | 51.4 | 51.8 | 0.1 | 0.118x | 1.418x |
| 7 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 51.6 | 51.5 | 52.2 | 0.3 | 0.118x | 1.421x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 58.1 | 58.0 | 58.9 | 0.4 | 0.133x | 1.599x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 69.9 | 68.1 | 74.1 | 2.5 | 0.160x | 1.925x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 437.2 | 434.9 | 439.3 | 1.5 | 1.000x | 12.036x |

### `orig` / `s-011` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.7 | 12.5 | 12.7 | 0.1 | 0.037x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.7 | 12.6 | 13.9 | 0.5 | 0.037x | 1.003x |
| 3 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 31.2 | 31.1 | 31.3 | 0.1 | 0.090x | 2.464x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 31.8 | 31.2 | 36.0 | 1.7 | 0.092x | 2.511x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 33.7 | 33.6 | 33.8 | 0.1 | 0.097x | 2.661x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 33.8 | 33.6 | 34.1 | 0.2 | 0.098x | 2.669x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 41.4 | 41.2 | 41.5 | 0.2 | 0.120x | 3.272x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 41.4 | 40.9 | 43.2 | 0.8 | 0.120x | 3.272x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 345.4 | 335.7 | 420.6 | 30.8 | 0.999x | 27.300x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 345.7 | 342.2 | 350.4 | 2.9 | 1.000x | 27.326x |

### `orig` / `s-011` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 34.6 | 34.5 | 34.9 | 0.1 | 0.020x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 34.6 | 34.4 | 39.9 | 2.1 | 0.020x | 1.002x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 34.7 | 34.5 | 34.7 | 0.1 | 0.020x | 1.003x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 34.7 | 34.7 | 34.9 | 0.1 | 0.020x | 1.004x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 139.6 | 136.1 | 142.6 | 2.3 | 0.079x | 4.038x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 318.5 | 314.3 | 319.6 | 1.9 | 0.181x | 9.215x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 320.0 | 315.7 | 328.4 | 4.3 | 0.182x | 9.258x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 320.9 | 317.0 | 321.6 | 1.8 | 0.182x | 9.283x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 326.2 | 323.8 | 337.5 | 4.9 | 0.185x | 9.437x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,762.0 | 1,735.4 | 1,780.9 | 15.7 | 1.000x | 50.977x |

### `orig` / `s-012` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.4 | 35.3 | 35.6 | 0.1 | 0.052x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.5 | 35.3 | 43.1 | 3.1 | 0.052x | 1.002x |
| 3 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 58.6 | 58.1 | 62.4 | 1.6 | 0.087x | 1.656x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 58.7 | 57.7 | 63.1 | 2.0 | 0.087x | 1.660x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 60.3 | 60.1 | 62.8 | 1.0 | 0.089x | 1.705x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 76.0 | 75.3 | 77.3 | 0.7 | 0.112x | 2.147x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 76.7 | 76.2 | 77.3 | 0.3 | 0.114x | 2.167x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 76.9 | 76.4 | 77.8 | 0.5 | 0.114x | 2.174x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 675.6 | 670.0 | 693.0 | 7.8 | 1.000x | 19.093x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 681.0 | 671.1 | 684.4 | 5.7 | 1.008x | 19.245x |

### `orig` / `s-012` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 64.9 | 62.9 | 67.2 | 1.4 | 0.096x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 65.6 | 65.4 | 65.9 | 0.1 | 0.097x | 1.011x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 65.7 | 65.4 | 66.0 | 0.2 | 0.097x | 1.012x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 65.7 | 65.6 | 65.8 | 0.1 | 0.097x | 1.013x |
| 5 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 66.1 | 65.7 | 66.2 | 0.2 | 0.098x | 1.018x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 67.2 | 67.2 | 67.7 | 0.2 | 0.099x | 1.036x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 80.0 | 79.8 | 82.2 | 0.9 | 0.118x | 1.233x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 82.7 | 82.2 | 83.0 | 0.3 | 0.122x | 1.274x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 83.6 | 81.8 | 88.5 | 2.4 | 0.124x | 1.288x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 675.9 | 671.4 | 689.5 | 7.2 | 1.000x | 10.411x |

### `orig` / `s-013` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.3 | 35.3 | 35.6 | 0.1 | 0.052x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.4 | 35.3 | 42.6 | 2.9 | 0.052x | 1.000x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 58.0 | 57.6 | 58.2 | 0.2 | 0.086x | 1.641x |
| 4 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 59.2 | 58.0 | 60.8 | 1.0 | 0.088x | 1.677x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 60.6 | 60.4 | 62.6 | 0.9 | 0.090x | 1.715x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 76.1 | 75.7 | 79.4 | 1.4 | 0.113x | 2.152x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 76.2 | 75.9 | 76.7 | 0.3 | 0.113x | 2.156x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 76.8 | 76.7 | 77.1 | 0.2 | 0.114x | 2.174x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 673.8 | 661.7 | 679.5 | 5.9 | 0.999x | 19.066x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 674.6 | 672.2 | 691.1 | 7.1 | 1.000x | 19.088x |

### `orig` / `s-013` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 65.0 | 64.2 | 65.2 | 0.4 | 0.095x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 65.7 | 65.4 | 66.2 | 0.3 | 0.096x | 1.011x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 65.8 | 65.7 | 66.3 | 0.2 | 0.096x | 1.012x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 65.8 | 65.6 | 65.9 | 0.1 | 0.096x | 1.013x |
| 5 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 66.0 | 65.8 | 66.1 | 0.1 | 0.096x | 1.015x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 67.4 | 67.1 | 72.9 | 2.2 | 0.098x | 1.037x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 79.8 | 79.3 | 81.4 | 0.7 | 0.116x | 1.228x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 83.1 | 82.1 | 93.2 | 4.2 | 0.121x | 1.278x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 85.2 | 82.0 | 88.7 | 2.5 | 0.124x | 1.310x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 687.8 | 670.1 | 692.3 | 7.8 | 1.000x | 10.579x |

### `orig` / `s-014` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.7 | 0.1 | 0.056x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.7 | 29.6 | 35.3 | 2.3 | 0.056x | 1.005x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 47.7 | 47.6 | 50.2 | 1.0 | 0.090x | 1.613x |
| 4 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 49.4 | 47.5 | 49.8 | 1.0 | 0.093x | 1.670x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 50.3 | 50.2 | 52.6 | 0.9 | 0.094x | 1.699x |
| 6 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 61.9 | 61.9 | 62.7 | 0.3 | 0.116x | 2.094x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 62.1 | 61.9 | 62.3 | 0.2 | 0.117x | 2.101x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 64.0 | 63.9 | 66.9 | 1.2 | 0.120x | 2.165x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 532.5 | 527.5 | 539.0 | 3.9 | 1.000x | 18.001x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 532.6 | 528.2 | 542.7 | 5.8 | 1.000x | 18.005x |

### `orig` / `s-014` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 51.3 | 51.3 | 51.7 | 0.1 | 0.096x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 51.3 | 51.3 | 51.5 | 0.1 | 0.096x | 1.000x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 51.5 | 51.4 | 53.2 | 0.7 | 0.096x | 1.004x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 51.7 | 51.5 | 52.4 | 0.3 | 0.096x | 1.007x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 56.7 | 55.9 | 57.5 | 0.6 | 0.106x | 1.105x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 56.7 | 54.8 | 58.4 | 1.4 | 0.106x | 1.105x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 70.6 | 70.4 | 71.0 | 0.2 | 0.131x | 1.375x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 74.0 | 73.6 | 74.1 | 0.2 | 0.138x | 1.441x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 78.4 | 75.9 | 83.0 | 2.9 | 0.146x | 1.528x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 537.3 | 534.5 | 541.0 | 2.4 | 1.000x | 10.467x |

### `orig` / `s-015` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33.8 | 33.8 | 33.9 | 0.0 | 0.052x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.0 | 33.8 | 40.4 | 2.6 | 0.052x | 1.004x |
| 3 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 55.4 | 55.0 | 56.5 | 0.5 | 0.085x | 1.637x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 55.5 | 55.3 | 58.5 | 1.3 | 0.085x | 1.640x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 57.9 | 57.8 | 59.7 | 0.7 | 0.088x | 1.711x |
| 6 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 72.8 | 72.7 | 73.7 | 0.4 | 0.111x | 2.150x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73.2 | 72.9 | 73.4 | 0.2 | 0.112x | 2.162x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 73.3 | 72.7 | 76.1 | 1.2 | 0.112x | 2.167x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 650.9 | 647.6 | 657.7 | 3.5 | 0.993x | 19.228x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 655.7 | 647.2 | 663.6 | 6.4 | 1.000x | 19.371x |

### `orig` / `s-015` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 62.0 | 61.4 | 62.7 | 0.4 | 0.095x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 62.6 | 62.5 | 62.8 | 0.1 | 0.096x | 1.008x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 62.6 | 62.5 | 62.7 | 0.0 | 0.096x | 1.009x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 62.7 | 62.5 | 63.3 | 0.3 | 0.096x | 1.011x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 62.8 | 62.4 | 62.8 | 0.2 | 0.096x | 1.012x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 64.4 | 64.1 | 64.6 | 0.2 | 0.099x | 1.038x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 78.3 | 77.9 | 79.4 | 0.5 | 0.120x | 1.263x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 81.3 | 79.4 | 87.0 | 3.2 | 0.125x | 1.311x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 81.4 | 81.0 | 81.6 | 0.2 | 0.125x | 1.311x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 652.1 | 647.3 | 660.0 | 4.7 | 1.000x | 10.511x |

### `orig` / `s-016` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.7 | 11.6 | 11.8 | 0.1 | 0.063x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 11.9 | 11.6 | 12.6 | 0.3 | 0.064x | 1.017x |
| 3 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 24.9 | 24.8 | 25.0 | 0.1 | 0.134x | 2.133x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 25.8 | 25.8 | 26.7 | 0.4 | 0.139x | 2.215x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 25.9 | 25.8 | 26.0 | 0.1 | 0.139x | 2.217x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 25.2 | 27.5 | 0.8 | 0.140x | 2.233x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.5 | 32.4 | 33.3 | 0.3 | 0.174x | 2.787x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.7 | 32.4 | 32.9 | 0.2 | 0.176x | 2.805x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 186.4 | 184.7 | 186.9 | 0.8 | 1.000x | 15.972x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 186.4 | 184.3 | 189.1 | 1.7 | 1.000x | 15.975x |

### `orig` / `s-016` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 26.1 | 25.9 | 26.2 | 0.1 | 0.024x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 26.4 | 26.4 | 26.6 | 0.1 | 0.024x | 1.013x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 26.4 | 26.2 | 27.0 | 0.3 | 0.024x | 1.013x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 26.5 | 26.3 | 26.9 | 0.2 | 0.024x | 1.015x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 108.5 | 107.4 | 114.2 | 2.9 | 0.100x | 4.160x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 226.6 | 226.0 | 230.8 | 2.0 | 0.209x | 8.687x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 228.3 | 224.7 | 232.5 | 2.5 | 0.210x | 8.753x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 229.4 | 228.3 | 230.8 | 0.9 | 0.211x | 8.795x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 232.5 | 229.7 | 235.1 | 2.2 | 0.214x | 8.912x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,086.3 | 1,078.4 | 1,091.9 | 5.2 | 1.000x | 41.638x |

### `orig` / `s-017` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.3 | 35.2 | 35.4 | 0.1 | 0.053x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.4 | 35.3 | 42.5 | 2.8 | 0.053x | 1.004x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 57.7 | 57.5 | 58.1 | 0.2 | 0.086x | 1.636x |
| 4 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 58.0 | 57.9 | 58.7 | 0.3 | 0.087x | 1.642x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 60.3 | 60.3 | 61.7 | 0.6 | 0.090x | 1.708x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 76.0 | 75.1 | 76.8 | 0.6 | 0.113x | 2.153x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 76.5 | 75.5 | 77.2 | 0.6 | 0.114x | 2.167x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 76.8 | 76.4 | 77.3 | 0.3 | 0.115x | 2.175x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 670.0 | 663.1 | 682.5 | 7.5 | 1.000x | 18.977x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 671.2 | 667.0 | 679.9 | 4.6 | 1.002x | 19.011x |

### `orig` / `s-017` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 64.8 | 63.9 | 67.2 | 1.1 | 0.096x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 65.6 | 65.3 | 66.1 | 0.3 | 0.097x | 1.012x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 65.7 | 65.5 | 66.2 | 0.2 | 0.097x | 1.015x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 65.8 | 65.6 | 66.5 | 0.3 | 0.097x | 1.016x |
| 5 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 66.2 | 65.7 | 67.6 | 0.7 | 0.098x | 1.022x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 66.9 | 66.8 | 67.5 | 0.3 | 0.099x | 1.032x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 79.9 | 79.4 | 88.2 | 3.4 | 0.118x | 1.234x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 82.4 | 81.6 | 87.7 | 2.8 | 0.122x | 1.271x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 83.0 | 82.3 | 84.5 | 0.7 | 0.123x | 1.281x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 676.8 | 670.2 | 678.5 | 3.3 | 1.000x | 10.444x |

### `orig` / `s-018` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.9 | 33.8 | 40.5 | 2.7 | 0.052x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33.9 | 33.8 | 33.9 | 0.0 | 0.052x | 1.000x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 55.3 | 55.2 | 55.5 | 0.1 | 0.085x | 1.635x |
| 4 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 55.4 | 55.0 | 55.6 | 0.2 | 0.085x | 1.635x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 57.9 | 57.7 | 60.1 | 0.9 | 0.089x | 1.710x |
| 6 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 72.9 | 72.8 | 73.5 | 0.3 | 0.112x | 2.152x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 72.9 | 72.7 | 73.1 | 0.2 | 0.112x | 2.154x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 73.1 | 72.9 | 73.4 | 0.2 | 0.112x | 2.159x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 651.0 | 649.8 | 665.4 | 6.3 | 1.000x | 19.230x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 651.8 | 647.7 | 652.9 | 1.9 | 1.001x | 19.254x |

### `orig` / `s-018` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 62.3 | 61.7 | 63.0 | 0.5 | 0.095x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 62.6 | 62.4 | 63.5 | 0.4 | 0.095x | 1.004x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 62.6 | 62.6 | 62.9 | 0.1 | 0.095x | 1.005x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 62.7 | 62.4 | 63.0 | 0.2 | 0.095x | 1.006x |
| 5 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 62.7 | 62.5 | 63.0 | 0.2 | 0.096x | 1.007x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 64.2 | 63.9 | 64.5 | 0.2 | 0.098x | 1.031x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 78.2 | 77.9 | 78.2 | 0.1 | 0.119x | 1.255x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 81.1 | 81.0 | 81.4 | 0.1 | 0.124x | 1.301x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 81.9 | 79.6 | 104.6 | 9.2 | 0.125x | 1.314x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 656.4 | 651.0 | 658.3 | 2.4 | 1.000x | 10.534x |

### `orig` / `s-019` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 11.8 | 11.5 | 11.9 | 0.2 | 0.061x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.9 | 11.7 | 12.7 | 0.3 | 0.061x | 1.006x |
| 3 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.5 | 25.4 | 26.6 | 0.5 | 0.131x | 2.163x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 26.4 | 25.2 | 27.6 | 0.9 | 0.136x | 2.246x |
| 5 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.5 | 26.5 | 26.7 | 0.1 | 0.137x | 2.254x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.6 | 26.5 | 29.0 | 1.0 | 0.137x | 2.260x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.5 | 34.2 | 34.6 | 0.2 | 0.178x | 2.928x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 34.5 | 33.7 | 35.9 | 0.8 | 0.178x | 2.932x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 192.1 | 190.6 | 194.2 | 1.4 | 0.989x | 16.309x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 194.1 | 191.5 | 197.7 | 2.1 | 1.000x | 16.484x |

### `orig` / `s-019` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 27.6 | 27.3 | 27.8 | 0.2 | 0.025x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 27.6 | 27.3 | 27.8 | 0.2 | 0.025x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 27.7 | 27.6 | 27.9 | 0.1 | 0.025x | 1.003x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 27.7 | 27.5 | 28.2 | 0.3 | 0.025x | 1.004x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 110.3 | 108.9 | 121.5 | 4.8 | 0.101x | 3.998x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 237.7 | 236.8 | 241.4 | 1.7 | 0.218x | 8.612x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 237.8 | 236.5 | 240.8 | 1.5 | 0.218x | 8.618x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 238.2 | 237.1 | 238.7 | 0.6 | 0.219x | 8.630x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 242.3 | 241.8 | 246.0 | 1.6 | 0.222x | 8.778x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,089.3 | 1,083.5 | 1,097.0 | 4.9 | 1.000x | 39.470x |

### `orig` / `s-020` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 38.4 | 38.4 | 38.5 | 0.0 | 0.056x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 38.5 | 38.3 | 45.8 | 2.9 | 0.056x | 1.003x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 63.2 | 63.1 | 63.3 | 0.1 | 0.092x | 1.644x |
| 4 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 63.4 | 63.0 | 63.8 | 0.3 | 0.092x | 1.652x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 66.2 | 65.9 | 67.4 | 0.5 | 0.096x | 1.724x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 80.4 | 80.1 | 81.2 | 0.4 | 0.117x | 2.092x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 83.4 | 83.3 | 86.5 | 1.2 | 0.121x | 2.171x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 84.1 | 83.9 | 86.5 | 1.0 | 0.122x | 2.191x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 682.9 | 678.1 | 688.0 | 3.6 | 0.990x | 17.780x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 689.8 | 678.0 | 699.0 | 7.1 | 1.000x | 17.961x |

### `orig` / `s-020` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 70.5 | 68.5 | 73.8 | 1.9 | 0.103x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 71.4 | 70.8 | 71.5 | 0.3 | 0.104x | 1.012x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 72.7 | 72.4 | 73.4 | 0.4 | 0.106x | 1.030x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 73.0 | 72.8 | 73.9 | 0.4 | 0.106x | 1.035x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 73.1 | 72.9 | 73.4 | 0.2 | 0.107x | 1.037x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 73.1 | 72.6 | 74.0 | 0.5 | 0.107x | 1.037x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 85.6 | 83.8 | 96.7 | 5.3 | 0.125x | 1.214x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 85.7 | 85.6 | 86.6 | 0.4 | 0.125x | 1.215x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 88.1 | 87.9 | 89.0 | 0.5 | 0.128x | 1.249x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 686.1 | 679.3 | 696.5 | 5.7 | 1.000x | 9.730x |

### `orig` / `s-021` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.7 | 0.1 | 0.042x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.6 | 32.4 | 1.1 | 0.042x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 62.0 | 61.7 | 62.5 | 0.3 | 0.087x | 2.091x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 62.1 | 61.9 | 62.4 | 0.2 | 0.087x | 2.095x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 70.3 | 67.9 | 72.4 | 1.5 | 0.099x | 2.371x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 75.8 | 75.4 | 75.9 | 0.2 | 0.107x | 2.559x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 78.4 | 78.2 | 78.9 | 0.2 | 0.111x | 2.647x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 82.5 | 80.9 | 83.6 | 1.0 | 0.116x | 2.784x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 701.8 | 700.2 | 708.9 | 3.5 | 0.989x | 23.689x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 709.4 | 699.5 | 738.6 | 14.4 | 1.000x | 23.942x |

### `orig` / `s-021` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 51.4 | 51.3 | 51.7 | 0.2 | 0.072x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 51.4 | 51.3 | 51.5 | 0.1 | 0.072x | 1.000x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 51.5 | 51.4 | 52.1 | 0.3 | 0.073x | 1.002x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 51.6 | 51.4 | 52.1 | 0.2 | 0.073x | 1.004x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 74.8 | 74.1 | 76.1 | 0.7 | 0.105x | 1.456x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 76.0 | 75.1 | 79.7 | 1.7 | 0.107x | 1.479x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 83.3 | 83.3 | 85.6 | 0.9 | 0.117x | 1.621x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 84.7 | 84.6 | 84.8 | 0.1 | 0.119x | 1.648x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 91.5 | 89.9 | 100.0 | 3.7 | 0.129x | 1.781x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 709.8 | 708.2 | 712.2 | 1.4 | 1.000x | 13.810x |

### `orig` / `s-022` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 36.0 | 35.8 | 38.2 | 0.9 | 0.080x | 1.000x |
| 2 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 36.1 | 35.7 | 37.2 | 0.5 | 0.080x | 1.001x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 38.1 | 37.8 | 40.2 | 0.9 | 0.085x | 1.058x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 38.4 | 38.3 | 38.7 | 0.1 | 0.085x | 1.065x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 41.7 | 41.6 | 42.0 | 0.2 | 0.093x | 1.158x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 41.8 | 41.5 | 45.9 | 1.7 | 0.093x | 1.160x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 91.3 | 91.2 | 91.5 | 0.1 | 0.203x | 2.534x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 91.5 | 91.4 | 92.5 | 0.4 | 0.203x | 2.539x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 450.6 | 446.8 | 474.9 | 10.3 | 1.000x | 12.503x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 450.7 | 444.7 | 451.8 | 2.6 | 1.000x | 12.506x |

### `orig` / `s-022` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 40.3 | 40.1 | 41.3 | 0.5 | 0.089x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 41.0 | 39.7 | 41.3 | 0.7 | 0.090x | 1.018x |
| 3 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 41.6 | 41.2 | 41.8 | 0.2 | 0.092x | 1.032x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 42.0 | 41.6 | 42.2 | 0.3 | 0.093x | 1.044x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 71.8 | 70.7 | 76.0 | 1.9 | 0.158x | 1.782x |
| 6 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 80.3 | 80.0 | 80.4 | 0.2 | 0.177x | 1.994x |
| 7 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 80.3 | 80.2 | 80.8 | 0.2 | 0.177x | 1.994x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 80.5 | 80.4 | 80.6 | 0.1 | 0.177x | 1.999x |
| 9 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 80.6 | 80.5 | 80.7 | 0.1 | 0.178x | 2.001x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 453.9 | 450.6 | 458.7 | 2.8 | 1.000x | 11.271x |

### `orig` / `s-023` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.4 | 35.3 | 35.4 | 0.1 | 0.053x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.4 | 35.4 | 38.5 | 1.2 | 0.053x | 1.003x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 64.3 | 57.1 | 74.4 | 7.2 | 0.096x | 1.818x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 76.8 | 76.4 | 77.0 | 0.3 | 0.114x | 2.172x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 77.0 | 76.6 | 79.3 | 1.0 | 0.115x | 2.177x |
| 6 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 77.1 | 76.3 | 77.9 | 0.6 | 0.115x | 2.181x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 80.5 | 80.4 | 112.5 | 12.8 | 0.120x | 2.277x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 84.0 | 83.9 | 85.8 | 0.7 | 0.125x | 2.376x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 670.8 | 665.6 | 676.1 | 3.5 | 0.999x | 18.976x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 671.7 | 664.4 | 694.9 | 12.2 | 1.000x | 19.000x |

### `orig` / `s-023` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 65.7 | 65.5 | 66.5 | 0.4 | 0.098x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 65.7 | 65.3 | 65.9 | 0.2 | 0.098x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 65.7 | 65.6 | 65.8 | 0.1 | 0.098x | 1.001x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 65.8 | 65.6 | 66.1 | 0.2 | 0.098x | 1.002x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 74.6 | 74.3 | 76.7 | 0.9 | 0.112x | 1.136x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 77.8 | 76.3 | 87.5 | 4.1 | 0.116x | 1.184x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 82.7 | 82.5 | 86.1 | 1.4 | 0.124x | 1.260x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 84.7 | 82.8 | 90.2 | 2.7 | 0.127x | 1.290x |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 86.0 | 85.9 | 86.1 | 0.1 | 0.129x | 1.309x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 668.6 | 664.8 | 673.4 | 3.0 | 1.000x | 10.182x |

### `orig` / `s-024` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.6 | 0.0 | 0.041x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.6 | 32.2 | 1.0 | 0.041x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 61.9 | 61.5 | 62.3 | 0.3 | 0.085x | 2.093x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 61.9 | 61.6 | 62.1 | 0.2 | 0.085x | 2.094x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 73.2 | 61.4 | 74.6 | 4.9 | 0.100x | 2.476x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 78.4 | 78.2 | 87.4 | 3.5 | 0.108x | 2.652x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 80.6 | 80.0 | 82.9 | 1.1 | 0.110x | 2.724x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 84.1 | 80.9 | 89.4 | 2.8 | 0.115x | 2.844x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 717.6 | 710.2 | 786.6 | 29.0 | 0.984x | 24.263x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 729.4 | 707.9 | 752.7 | 16.7 | 1.000x | 24.664x |

### `orig` / `s-024` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 51.4 | 51.3 | 51.8 | 0.2 | 0.072x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 51.4 | 51.2 | 51.7 | 0.2 | 0.072x | 1.001x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 51.5 | 51.2 | 53.4 | 0.8 | 0.072x | 1.002x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 51.8 | 51.6 | 63.0 | 4.5 | 0.073x | 1.009x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 86.5 | 85.2 | 88.5 | 1.1 | 0.122x | 1.684x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 87.7 | 87.6 | 89.5 | 0.7 | 0.123x | 1.706x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 87.8 | 85.7 | 91.2 | 2.0 | 0.123x | 1.709x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 89.9 | 89.4 | 92.7 | 1.5 | 0.126x | 1.750x |
| 9 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 90.4 | 90.0 | 93.0 | 1.2 | 0.127x | 1.759x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 711.3 | 706.4 | 720.9 | 4.8 | 1.000x | 13.842x |

### `orig` / `s-025` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.4 | 35.4 | 38.4 | 1.2 | 0.048x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.4 | 35.3 | 35.6 | 0.1 | 0.048x | 1.002x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 62.5 | 61.3 | 73.0 | 4.4 | 0.085x | 1.766x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 76.8 | 76.7 | 77.1 | 0.1 | 0.105x | 2.171x |
| 5 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 77.0 | 76.5 | 78.0 | 0.5 | 0.105x | 2.177x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 79.1 | 78.4 | 89.0 | 4.0 | 0.108x | 2.235x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 82.7 | 82.4 | 82.8 | 0.2 | 0.113x | 2.337x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 84.3 | 82.2 | 85.5 | 1.2 | 0.115x | 2.384x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 724.4 | 716.9 | 730.9 | 4.7 | 0.988x | 20.480x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 733.2 | 722.0 | 759.2 | 13.1 | 1.000x | 20.730x |

### `orig` / `s-025` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 65.7 | 65.4 | 65.8 | 0.1 | 0.090x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 65.7 | 65.6 | 66.1 | 0.2 | 0.090x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 65.8 | 65.5 | 65.9 | 0.1 | 0.090x | 1.002x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 65.9 | 65.8 | 66.5 | 0.3 | 0.090x | 1.003x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 85.0 | 83.8 | 90.4 | 2.5 | 0.116x | 1.294x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 86.0 | 81.3 | 91.1 | 3.5 | 0.118x | 1.309x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 86.7 | 86.6 | 86.7 | 0.0 | 0.119x | 1.320x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 89.6 | 89.6 | 89.8 | 0.1 | 0.123x | 1.365x |
| 9 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 92.0 | 90.7 | 93.5 | 1.0 | 0.126x | 1.400x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 731.2 | 721.9 | 739.0 | 5.5 | 1.000x | 11.134x |

### `orig` / `s-026` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 36.0 | 35.9 | 36.4 | 0.2 | 0.080x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 36.6 | 35.9 | 37.4 | 0.6 | 0.082x | 1.018x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 38.0 | 37.4 | 40.6 | 1.1 | 0.085x | 1.055x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 38.4 | 38.3 | 38.7 | 0.1 | 0.086x | 1.067x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 41.7 | 41.5 | 42.1 | 0.2 | 0.093x | 1.159x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 41.7 | 41.7 | 45.8 | 1.6 | 0.093x | 1.161x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 91.4 | 91.2 | 92.0 | 0.3 | 0.204x | 2.541x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 91.6 | 91.3 | 95.7 | 1.7 | 0.205x | 2.545x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 445.1 | 441.7 | 461.2 | 7.0 | 0.994x | 12.372x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 447.7 | 444.3 | 473.8 | 10.7 | 1.000x | 12.446x |

### `orig` / `s-026` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 40.3 | 39.7 | 42.2 | 0.9 | 0.090x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 41.0 | 39.7 | 41.2 | 0.6 | 0.091x | 1.019x |
| 3 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 41.5 | 40.6 | 41.5 | 0.4 | 0.092x | 1.029x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 41.9 | 41.0 | 42.2 | 0.4 | 0.093x | 1.041x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 71.2 | 70.3 | 75.2 | 1.9 | 0.158x | 1.767x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 80.3 | 80.3 | 80.7 | 0.2 | 0.179x | 1.993x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 80.4 | 80.3 | 80.5 | 0.1 | 0.179x | 1.996x |
| 8 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 80.5 | 80.4 | 81.1 | 0.2 | 0.179x | 1.999x |
| 9 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 80.5 | 80.5 | 80.6 | 0.0 | 0.179x | 1.999x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 449.2 | 445.5 | 453.9 | 2.7 | 1.000x | 11.152x |

### `orig` / `s-027` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 41.7 | 41.4 | 41.8 | 0.1 | 0.066x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 41.9 | 41.5 | 46.0 | 1.7 | 0.066x | 1.003x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 66.9 | 57.9 | 72.1 | 6.3 | 0.106x | 1.602x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 73.7 | 72.5 | 75.4 | 1.0 | 0.117x | 1.765x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 79.8 | 79.8 | 80.9 | 0.4 | 0.127x | 1.911x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 84.7 | 84.1 | 89.0 | 1.8 | 0.134x | 2.029x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 91.3 | 91.2 | 91.7 | 0.2 | 0.145x | 2.188x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 91.5 | 91.1 | 91.7 | 0.2 | 0.145x | 2.191x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 630.2 | 626.4 | 661.8 | 13.3 | 1.000x | 15.096x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 634.1 | 628.0 | 640.4 | 4.3 | 1.006x | 15.190x |

### `orig` / `s-027` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 74.5 | 74.4 | 74.7 | 0.1 | 0.118x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 76.6 | 76.3 | 77.3 | 0.4 | 0.121x | 1.028x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 80.3 | 80.3 | 80.9 | 0.3 | 0.127x | 1.078x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 80.4 | 80.1 | 81.5 | 0.5 | 0.128x | 1.079x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 80.5 | 80.0 | 80.8 | 0.3 | 0.128x | 1.081x |
| 6 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 80.6 | 80.3 | 80.6 | 0.1 | 0.128x | 1.082x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 82.2 | 81.5 | 88.2 | 2.7 | 0.130x | 1.104x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 83.7 | 83.6 | 84.1 | 0.2 | 0.133x | 1.124x |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 86.5 | 86.4 | 86.5 | 0.0 | 0.137x | 1.161x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 630.2 | 622.4 | 634.6 | 4.1 | 1.000x | 8.461x |

### `orig` / `s-028` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.4 | 0.0 | 0.045x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.3 | 15.2 | 0.8 | 0.045x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 27.0 | 26.9 | 28.6 | 0.7 | 0.090x | 2.022x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 27.1 | 26.8 | 27.2 | 0.2 | 0.091x | 2.031x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 34.0 | 33.6 | 35.7 | 0.8 | 0.114x | 2.547x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 34.8 | 34.7 | 34.9 | 0.1 | 0.116x | 2.603x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 34.8 | 34.1 | 39.4 | 2.3 | 0.116x | 2.603x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 34.8 | 34.8 | 35.0 | 0.1 | 0.116x | 2.607x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 295.1 | 292.9 | 304.0 | 4.2 | 0.985x | 22.098x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 299.6 | 294.3 | 319.4 | 9.7 | 1.000x | 22.435x |

### `orig` / `s-028` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 22.2 | 22.1 | 22.5 | 0.1 | 0.021x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 22.2 | 22.1 | 22.5 | 0.2 | 0.021x | 1.003x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 22.3 | 22.2 | 23.1 | 0.3 | 0.021x | 1.006x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 22.4 | 22.3 | 22.7 | 0.1 | 0.021x | 1.011x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.3 | 67.4 | 76.6 | 3.5 | 0.064x | 3.080x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 256.5 | 255.4 | 259.4 | 1.4 | 0.239x | 11.569x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 256.6 | 255.4 | 261.3 | 2.1 | 0.239x | 11.574x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 256.7 | 256.0 | 259.2 | 1.2 | 0.239x | 11.580x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 260.6 | 259.0 | 263.9 | 1.7 | 0.243x | 11.755x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,073.2 | 1,065.2 | 1,077.1 | 4.3 | 1.000x | 48.408x |

### `orig` / `s-029` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.2 | 13.4 | 0.0 | 0.045x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.2 | 15.1 | 0.7 | 0.045x | 1.000x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 33.4 | 33.4 | 34.9 | 0.7 | 0.113x | 2.504x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 35.0 | 34.9 | 35.2 | 0.1 | 0.118x | 2.620x |
| 5 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 35.1 | 35.1 | 37.1 | 0.8 | 0.119x | 2.630x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 35.2 | 32.8 | 37.7 | 1.6 | 0.119x | 2.636x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 51.2 | 50.4 | 52.1 | 0.6 | 0.173x | 3.832x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 51.3 | 51.0 | 51.7 | 0.3 | 0.174x | 3.842x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 295.4 | 293.8 | 327.7 | 12.9 | 1.000x | 22.121x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 295.4 | 293.2 | 304.2 | 4.2 | 1.000x | 22.123x |

### `orig` / `s-029` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 45.3 | 45.2 | 45.3 | 0.0 | 0.042x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 45.4 | 45.3 | 46.6 | 0.5 | 0.042x | 1.003x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 45.5 | 45.3 | 45.8 | 0.2 | 0.042x | 1.004x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 45.7 | 45.4 | 46.0 | 0.2 | 0.043x | 1.009x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 70.9 | 69.3 | 78.1 | 3.3 | 0.066x | 1.567x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 528.2 | 526.6 | 534.1 | 2.6 | 0.493x | 11.666x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 531.8 | 527.3 | 541.8 | 4.8 | 0.497x | 11.746x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 533.3 | 529.1 | 537.4 | 2.8 | 0.498x | 11.779x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 534.1 | 530.7 | 534.7 | 1.4 | 0.499x | 11.797x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,070.6 | 1,065.3 | 1,082.4 | 6.1 | 1.000x | 23.646x |

### `orig` / `s-030` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.4 | 0.1 | 0.045x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.2 | 15.2 | 0.8 | 0.045x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 26.8 | 26.5 | 27.0 | 0.1 | 0.091x | 2.004x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 26.9 | 26.6 | 29.5 | 1.1 | 0.091x | 2.009x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 34.0 | 32.9 | 38.4 | 2.4 | 0.115x | 2.546x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 34.1 | 33.7 | 35.0 | 0.5 | 0.115x | 2.549x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 34.8 | 34.7 | 34.9 | 0.1 | 0.118x | 2.601x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 34.8 | 34.7 | 34.9 | 0.1 | 0.118x | 2.601x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 293.9 | 291.4 | 303.5 | 4.2 | 0.994x | 21.987x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 295.7 | 293.6 | 320.7 | 10.2 | 1.000x | 22.116x |

### `orig` / `s-030` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 22.1 | 22.0 | 22.1 | 0.0 | 0.021x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 22.1 | 22.1 | 22.3 | 0.1 | 0.021x | 1.002x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 22.2 | 22.1 | 22.3 | 0.1 | 0.021x | 1.007x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 22.2 | 22.1 | 22.3 | 0.1 | 0.021x | 1.007x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.9 | 67.5 | 77.3 | 3.9 | 0.064x | 3.125x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 258.4 | 249.9 | 264.0 | 4.9 | 0.241x | 11.714x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 264.5 | 255.1 | 267.7 | 5.4 | 0.247x | 11.993x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 265.8 | 255.9 | 272.4 | 5.5 | 0.248x | 12.051x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 268.0 | 256.9 | 270.2 | 5.9 | 0.250x | 12.151x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,072.5 | 1,059.4 | 1,080.4 | 7.0 | 1.000x | 48.622x |

### `orig` / `s-031` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.3 | 15.1 | 0.7 | 0.045x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.4 | 0.0 | 0.045x | 1.002x |
| 3 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 33.4 | 32.8 | 35.8 | 1.1 | 0.113x | 2.499x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 33.5 | 33.4 | 35.3 | 0.7 | 0.113x | 2.506x |
| 5 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 35.0 | 35.0 | 35.1 | 0.0 | 0.118x | 2.620x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 35.1 | 34.9 | 35.1 | 0.1 | 0.118x | 2.622x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.5 | 35.1 | 35.6 | 0.2 | 0.120x | 2.656x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.5 | 35.0 | 37.2 | 0.8 | 0.120x | 2.656x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 296.2 | 293.2 | 319.8 | 9.7 | 1.000x | 22.153x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 296.7 | 292.3 | 302.8 | 3.4 | 1.002x | 22.191x |

### `orig` / `s-031` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 29.6 | 29.5 | 31.3 | 0.8 | 0.028x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 29.7 | 29.6 | 30.2 | 0.2 | 0.028x | 1.004x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 29.7 | 29.6 | 30.0 | 0.1 | 0.028x | 1.004x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 29.7 | 29.7 | 29.8 | 0.1 | 0.028x | 1.005x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 71.0 | 70.2 | 77.5 | 3.1 | 0.066x | 2.400x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 329.3 | 325.5 | 338.2 | 4.4 | 0.308x | 11.126x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 330.5 | 328.2 | 332.2 | 1.4 | 0.309x | 11.169x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 331.3 | 327.3 | 332.7 | 2.3 | 0.310x | 11.193x |
| 9 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 331.6 | 324.9 | 332.3 | 2.7 | 0.311x | 11.206x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,068.0 | 1,056.0 | 1,072.0 | 5.4 | 1.000x | 36.087x |

### `orig` / `s-032` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.2 | 0.1 | 0.045x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.2 | 16.1 | 18.5 | 0.9 | 0.045x | 1.004x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.3 | 30.9 | 31.5 | 0.2 | 0.087x | 1.944x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 31.4 | 31.3 | 33.6 | 0.9 | 0.087x | 1.948x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 45.0 | 44.8 | 49.4 | 1.8 | 0.125x | 2.792x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 54.4 | 52.8 | 55.6 | 1.2 | 0.151x | 3.381x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 64.4 | 63.9 | 64.4 | 0.2 | 0.178x | 3.996x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 64.7 | 63.2 | 65.9 | 0.9 | 0.179x | 4.020x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 353.9 | 348.6 | 360.1 | 4.1 | 0.981x | 21.976x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 360.8 | 351.6 | 387.0 | 12.4 | 1.000x | 22.407x |

### `orig` / `s-032` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 26.2 | 26.0 | 26.4 | 0.1 | 0.020x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 26.3 | 26.2 | 26.6 | 0.2 | 0.020x | 1.004x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 26.3 | 26.1 | 26.3 | 0.1 | 0.020x | 1.006x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 26.4 | 26.2 | 26.6 | 0.2 | 0.020x | 1.011x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 71.1 | 70.0 | 79.7 | 3.9 | 0.054x | 2.720x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 384.7 | 381.9 | 392.2 | 3.5 | 0.294x | 14.709x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 387.4 | 381.8 | 391.7 | 4.2 | 0.296x | 14.814x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 388.8 | 384.3 | 390.8 | 2.3 | 0.297x | 14.866x |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 389.4 | 383.8 | 396.8 | 4.5 | 0.298x | 14.891x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,306.9 | 1,300.5 | 1,321.2 | 7.3 | 1.000x | 49.973x |

### `orig` / `s-033` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.0 | 16.0 | 16.2 | 0.1 | 0.051x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.0 | 18.2 | 0.8 | 0.051x | 1.006x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.0 | 30.7 | 31.4 | 0.2 | 0.098x | 1.929x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 31.3 | 30.8 | 33.2 | 0.8 | 0.099x | 1.951x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 41.8 | 41.6 | 42.7 | 0.4 | 0.133x | 2.603x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 50.7 | 49.1 | 53.2 | 1.3 | 0.161x | 3.158x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 50.9 | 48.9 | 52.1 | 1.3 | 0.162x | 3.169x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 52.0 | 49.5 | 53.7 | 1.6 | 0.165x | 3.243x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 311.0 | 306.9 | 317.4 | 3.4 | 0.988x | 19.383x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 314.7 | 310.7 | 335.8 | 9.7 | 1.000x | 19.613x |

### `orig` / `s-033` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 26.2 | 26.0 | 26.6 | 0.2 | 0.023x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 26.2 | 26.0 | 26.3 | 0.1 | 0.023x | 1.000x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 26.3 | 26.1 | 26.4 | 0.1 | 0.023x | 1.004x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 26.4 | 26.1 | 26.6 | 0.2 | 0.023x | 1.008x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 71.0 | 69.9 | 78.5 | 3.5 | 0.062x | 2.716x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 360.7 | 356.7 | 365.0 | 2.9 | 0.317x | 13.792x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 362.4 | 358.6 | 364.8 | 2.1 | 0.319x | 13.855x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 362.6 | 360.1 | 365.4 | 1.9 | 0.319x | 13.864x |
| 9 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 363.1 | 353.4 | 365.7 | 4.8 | 0.319x | 13.881x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,137.7 | 1,133.0 | 1,145.8 | 4.4 | 1.000x | 43.499x |

### `orig` / `s-034` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 20.3 | 20.2 | 20.5 | 0.1 | 0.035x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.3 | 20.2 | 23.2 | 1.2 | 0.035x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.2 | 23.1 | 23.6 | 0.2 | 0.040x | 1.141x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 23.4 | 23.1 | 25.0 | 0.7 | 0.040x | 1.149x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.7 | 25.6 | 26.0 | 0.1 | 0.044x | 1.264x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 25.6 | 27.2 | 0.6 | 0.045x | 1.282x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 26.1 | 26.3 | 0.1 | 0.045x | 1.287x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.3 | 26.1 | 26.4 | 0.1 | 0.045x | 1.292x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 571.3 | 567.0 | 590.6 | 8.6 | 0.980x | 28.101x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 583.0 | 570.2 | 613.2 | 15.1 | 1.000x | 28.678x |

### `orig` / `s-034` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 19.0 | 19.0 | 19.6 | 0.3 | 0.009x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 19.2 | 19.0 | 19.3 | 0.1 | 0.009x | 1.009x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 19.2 | 19.0 | 19.4 | 0.1 | 0.009x | 1.009x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 19.3 | 19.1 | 19.3 | 0.1 | 0.009x | 1.014x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 97.5 | 97.4 | 100.9 | 1.4 | 0.045x | 5.133x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 178.4 | 175.9 | 178.7 | 1.0 | 0.082x | 9.390x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 178.5 | 177.3 | 181.3 | 1.5 | 0.082x | 9.393x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 180.7 | 177.3 | 181.2 | 1.7 | 0.083x | 9.511x |
| 9 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 183.4 | 175.1 | 188.4 | 4.9 | 0.084x | 9.652x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,188.2 | 2,187.2 | 2,196.0 | 4.0 | 1.000x | 115.147x |

### `orig` / `s-035` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.0 | 26.3 | 1.3 | 0.029x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.0 | 24.5 | 0.6 | 0.029x | 1.000x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 30.1 | 29.9 | 31.9 | 0.8 | 0.038x | 1.302x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 30.2 | 30.1 | 30.3 | 0.1 | 0.038x | 1.306x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 115.2 | 103.4 | 119.9 | 5.8 | 0.144x | 4.988x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 118.4 | 113.1 | 122.6 | 3.3 | 0.148x | 5.124x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 126.8 | 122.5 | 127.6 | 2.0 | 0.158x | 5.487x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 129.9 | 128.7 | 130.2 | 0.6 | 0.162x | 5.623x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 790.5 | 779.3 | 803.8 | 9.2 | 0.986x | 34.217x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 801.8 | 785.7 | 845.3 | 20.7 | 1.000x | 34.707x |

### `orig` / `s-035` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 25.3 | 25.2 | 25.8 | 0.2 | 0.008x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 25.3 | 25.1 | 25.8 | 0.3 | 0.008x | 1.002x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 25.4 | 25.3 | 26.6 | 0.5 | 0.008x | 1.005x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 25.4 | 25.2 | 27.8 | 1.0 | 0.008x | 1.005x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 133.1 | 133.0 | 134.6 | 0.6 | 0.044x | 5.270x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 696.9 | 695.0 | 698.5 | 1.3 | 0.229x | 27.588x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 698.8 | 691.1 | 705.4 | 5.2 | 0.229x | 27.665x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 713.3 | 703.7 | 748.8 | 17.7 | 0.234x | 28.238x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 716.9 | 713.5 | 725.2 | 4.3 | 0.235x | 28.382x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,046.4 | 2,994.3 | 3,058.5 | 22.6 | 1.000x | 120.603x |

### `orig` / `s-036` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.7 | 12.5 | 13.3 | 0.3 | 0.061x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 12.5 | 13.7 | 0.4 | 0.064x | 1.055x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.2 | 25.1 | 26.9 | 0.7 | 0.121x | 1.986x |
| 4 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.6 | 25.6 | 25.8 | 0.1 | 0.123x | 2.023x |
| 5 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 26.0 | 26.8 | 0.3 | 0.125x | 2.059x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 26.0 | 26.2 | 0.1 | 0.126x | 2.063x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33.0 | 32.7 | 34.5 | 0.6 | 0.159x | 2.607x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.2 | 33.0 | 33.2 | 0.1 | 0.159x | 2.616x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 205.6 | 203.7 | 212.2 | 3.0 | 0.988x | 16.222x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 208.2 | 206.8 | 225.6 | 7.8 | 1.000x | 16.423x |

### `orig` / `s-036` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 26.8 | 26.7 | 27.1 | 0.2 | 0.037x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 26.9 | 26.8 | 27.5 | 0.3 | 0.037x | 1.004x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 27.0 | 26.8 | 27.2 | 0.1 | 0.037x | 1.009x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 27.1 | 26.7 | 27.2 | 0.2 | 0.037x | 1.010x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 66.9 | 65.6 | 74.6 | 3.9 | 0.092x | 2.496x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 239.4 | 238.9 | 241.8 | 1.1 | 0.329x | 8.925x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 239.4 | 239.1 | 242.6 | 1.3 | 0.329x | 8.927x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 241.0 | 239.9 | 242.3 | 0.8 | 0.331x | 8.987x |
| 9 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 241.4 | 237.9 | 244.8 | 2.4 | 0.331x | 9.001x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 728.3 | 713.6 | 736.7 | 8.0 | 1.000x | 27.158x |

### `orig` / `s-037` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 14.6 | 14.4 | 14.7 | 0.1 | 0.043x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.8 | 14.6 | 16.4 | 0.7 | 0.044x | 1.009x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 26.9 | 26.8 | 28.2 | 0.6 | 0.080x | 1.836x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 27.3 | 26.7 | 27.5 | 0.3 | 0.081x | 1.861x |
| 5 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 40.0 | 39.5 | 41.1 | 0.6 | 0.118x | 2.729x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 40.1 | 39.6 | 40.8 | 0.5 | 0.119x | 2.741x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 40.2 | 39.5 | 40.7 | 0.4 | 0.119x | 2.743x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 41.0 | 39.6 | 41.9 | 0.8 | 0.121x | 2.802x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 338.2 | 337.0 | 379.1 | 16.1 | 1.000x | 23.091x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 339.7 | 332.6 | 341.8 | 3.3 | 1.004x | 23.191x |

### `orig` / `s-037` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 21.0 | 20.9 | 21.2 | 0.1 | 0.017x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 21.0 | 20.7 | 21.2 | 0.2 | 0.017x | 1.002x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 21.3 | 20.9 | 21.6 | 0.2 | 0.018x | 1.016x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 21.5 | 21.4 | 21.7 | 0.1 | 0.018x | 1.024x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 67.9 | 67.0 | 77.3 | 4.2 | 0.056x | 3.236x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 296.0 | 292.9 | 300.2 | 2.4 | 0.243x | 14.095x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 310.6 | 309.0 | 316.9 | 2.8 | 0.255x | 14.790x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 310.6 | 306.5 | 313.0 | 2.3 | 0.255x | 14.792x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 310.9 | 310.1 | 314.7 | 1.6 | 0.255x | 14.807x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,217.9 | 1,199.4 | 1,224.3 | 8.8 | 1.000x | 57.991x |

### `orig` / `s-038` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.0 | 26.3 | 1.3 | 0.047x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 23.2 | 23.0 | 24.8 | 0.7 | 0.047x | 1.002x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33.0 | 32.6 | 34.4 | 0.6 | 0.067x | 1.431x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.1 | 32.7 | 33.3 | 0.2 | 0.067x | 1.434x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 71.8 | 71.4 | 71.9 | 0.2 | 0.146x | 3.107x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 71.9 | 71.6 | 72.0 | 0.2 | 0.146x | 3.111x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 74.1 | 74.0 | 74.2 | 0.1 | 0.150x | 3.207x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 74.2 | 73.9 | 74.4 | 0.2 | 0.151x | 3.213x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 493.0 | 490.4 | 511.7 | 9.2 | 1.000x | 21.342x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 499.6 | 489.0 | 504.6 | 5.8 | 1.013x | 21.630x |

### `orig` / `s-038` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 26.8 | 26.7 | 26.9 | 0.1 | 0.015x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 26.9 | 26.7 | 27.2 | 0.2 | 0.015x | 1.004x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 27.0 | 26.8 | 27.1 | 0.1 | 0.015x | 1.006x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 27.1 | 26.9 | 27.3 | 0.1 | 0.015x | 1.012x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 91.8 | 90.8 | 101.3 | 4.3 | 0.051x | 3.421x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 585.5 | 572.7 | 614.0 | 14.4 | 0.324x | 21.816x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 595.7 | 576.0 | 607.9 | 10.4 | 0.330x | 22.195x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 598.5 | 593.3 | 636.6 | 18.0 | 0.331x | 22.298x |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 607.5 | 597.9 | 621.3 | 9.7 | 0.336x | 22.635x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,806.2 | 1,803.6 | 1,822.8 | 7.1 | 1.000x | 67.293x |

### `orig` / `s-039` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.0 | 11.9 | 12.9 | 0.4 | 0.058x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.1 | 11.8 | 20.7 | 3.5 | 0.059x | 1.006x |
| 3 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 25.9 | 26.4 | 0.2 | 0.127x | 2.175x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.3 | 26.2 | 27.1 | 0.3 | 0.128x | 2.190x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 26.4 | 26.4 | 27.6 | 0.5 | 0.128x | 2.197x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 28.3 | 26.4 | 30.1 | 1.4 | 0.138x | 2.359x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 66.8 | 66.5 | 67.6 | 0.4 | 0.324x | 5.560x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 66.9 | 66.6 | 66.9 | 0.1 | 0.325x | 5.569x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 206.1 | 202.7 | 207.7 | 2.0 | 1.000x | 17.159x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 207.9 | 201.0 | 209.5 | 3.6 | 1.009x | 17.312x |

### `orig` / `s-039` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 59.0 | 58.9 | 59.0 | 0.0 | 0.062x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 59.0 | 58.9 | 59.2 | 0.1 | 0.063x | 1.001x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 59.0 | 58.9 | 59.3 | 0.1 | 0.063x | 1.001x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 59.2 | 58.9 | 59.4 | 0.2 | 0.063x | 1.004x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 101.0 | 99.8 | 101.6 | 0.6 | 0.107x | 1.714x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 101.5 | 100.9 | 102.5 | 0.6 | 0.108x | 1.721x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 107.4 | 104.9 | 121.2 | 5.9 | 0.114x | 1.822x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 111.3 | 110.3 | 112.4 | 0.7 | 0.118x | 1.887x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 114.0 | 113.5 | 132.0 | 7.2 | 0.121x | 1.934x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 943.5 | 932.0 | 946.1 | 5.3 | 1.000x | 16.004x |

### `orig` / `s-040` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 22.9 | 22.8 | 23.3 | 0.2 | 0.642x | 1.000x |
| 2 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 23.2 | 23.0 | 23.5 | 0.2 | 0.653x | 1.016x |
| 3 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 25.3 | 25.2 | 25.4 | 0.1 | 0.712x | 1.108x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 25.3 | 25.3 | 25.4 | 0.0 | 0.712x | 1.108x |
| 5 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 26.0 | 26.0 | 28.1 | 0.8 | 0.732x | 1.139x |
| 6 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 26.0 | 26.1 | 0.1 | 0.733x | 1.141x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 30.0 | 29.9 | 30.5 | 0.2 | 0.842x | 1.310x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 30.2 | 29.8 | 31.1 | 0.5 | 0.848x | 1.319x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 34.2 | 33.7 | 35.1 | 0.5 | 0.960x | 1.494x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 35.6 | 34.2 | 35.7 | 0.7 | 1.000x | 1.557x |

### `orig` / `s-040` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 23.9 | 23.8 | 24.1 | 0.1 | 0.686x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 24.0 | 23.7 | 24.0 | 0.1 | 0.687x | 1.002x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 24.2 | 23.9 | 24.4 | 0.2 | 0.693x | 1.010x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 24.2 | 23.8 | 24.5 | 0.3 | 0.694x | 1.012x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 34.9 | 34.8 | 34.9 | 0.0 | 1.000x | 1.458x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 39.4 | 36.5 | 47.5 | 4.3 | 1.130x | 1.647x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 196.0 | 194.3 | 197.4 | 1.1 | 5.623x | 8.198x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 197.7 | 196.7 | 200.1 | 1.4 | 5.670x | 8.267x |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 198.5 | 196.4 | 200.2 | 1.4 | 5.694x | 8.301x |
| 10 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 198.5 | 197.9 | 198.9 | 0.4 | 5.694x | 8.302x |

### `orig` / `s-041` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.5 | 10.4 | 11.3 | 0.3 | 0.361x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.6 | 10.4 | 11.3 | 0.3 | 0.364x | 1.009x |
| 3 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 14.8 | 14.8 | 14.9 | 0.1 | 0.506x | 1.404x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 15.2 | 14.8 | 15.3 | 0.2 | 0.522x | 1.448x |
| 5 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 16.4 | 16.3 | 17.1 | 0.3 | 0.561x | 1.556x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 16.4 | 16.3 | 16.5 | 0.1 | 0.562x | 1.559x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 26.4 | 26.0 | 28.0 | 0.7 | 0.906x | 2.512x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 26.7 | 25.6 | 27.6 | 0.7 | 0.914x | 2.535x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.2 | 28.9 | 30.5 | 0.6 | 1.000x | 2.773x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.6 | 29.2 | 30.2 | 0.3 | 1.013x | 2.810x |

### `orig` / `s-041` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 19.0 | 18.5 | 19.3 | 0.3 | 0.518x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 19.0 | 18.7 | 19.9 | 0.4 | 0.520x | 1.002x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 19.5 | 18.6 | 20.1 | 0.6 | 0.532x | 1.026x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 19.9 | 18.9 | 20.3 | 0.6 | 0.542x | 1.045x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 36.7 | 36.3 | 37.2 | 0.3 | 1.000x | 1.929x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.1 | 37.3 | 48.3 | 4.0 | 1.230x | 2.372x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 143.6 | 142.9 | 145.1 | 0.8 | 3.918x | 7.558x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 143.9 | 143.6 | 146.8 | 1.3 | 3.927x | 7.574x |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 144.3 | 143.2 | 144.8 | 0.5 | 3.938x | 7.597x |
| 10 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 150.0 | 148.0 | 159.8 | 4.1 | 4.092x | 7.893x |

### `orig` / `s-042` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.3 | 14.5 | 0.5 | 0.063x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.6 | 0.1 | 0.063x | 1.005x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 16.9 | 16.7 | 17.4 | 0.3 | 0.080x | 1.262x |
| 4 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 17.2 | 16.9 | 17.9 | 0.4 | 0.081x | 1.285x |
| 5 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 18.6 | 18.6 | 19.6 | 0.5 | 0.088x | 1.393x |
| 6 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.7 | 18.7 | 20.2 | 0.6 | 0.088x | 1.400x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 18.7 | 18.6 | 18.9 | 0.1 | 0.088x | 1.400x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 18.7 | 18.6 | 18.8 | 0.1 | 0.089x | 1.401x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 205.9 | 204.1 | 209.6 | 1.9 | 0.973x | 15.413x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 211.6 | 204.7 | 217.2 | 4.8 | 1.000x | 15.832x |

### `orig` / `s-042` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 12.4 | 12.4 | 13.2 | 0.3 | 0.057x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 12.5 | 12.5 | 12.8 | 0.1 | 0.058x | 1.004x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 12.6 | 12.4 | 13.3 | 0.4 | 0.058x | 1.011x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 12.9 | 12.5 | 15.9 | 1.3 | 0.060x | 1.040x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 52.3 | 51.8 | 61.0 | 3.9 | 0.241x | 4.199x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 62.4 | 61.6 | 67.9 | 2.4 | 0.287x | 5.013x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 62.5 | 62.0 | 63.1 | 0.5 | 0.288x | 5.017x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 66.8 | 66.8 | 67.4 | 0.2 | 0.308x | 5.370x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 66.9 | 66.5 | 68.2 | 0.6 | 0.308x | 5.373x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 217.1 | 213.6 | 221.4 | 2.6 | 1.000x | 17.440x |

### `orig` / `s-043` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.9 | 12.6 | 13.4 | 0.3 | 0.082x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.5 | 12.7 | 14.6 | 0.6 | 0.086x | 1.049x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 23.5 | 23.4 | 25.1 | 0.7 | 0.150x | 1.824x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 23.6 | 23.5 | 23.7 | 0.1 | 0.151x | 1.828x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 23.7 | 23.6 | 24.9 | 0.5 | 0.152x | 1.839x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 24.0 | 23.6 | 24.5 | 0.3 | 0.154x | 1.863x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 78.8 | 78.5 | 79.8 | 0.5 | 0.503x | 6.108x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 78.8 | 78.7 | 79.0 | 0.1 | 0.504x | 6.109x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 155.1 | 150.3 | 156.0 | 2.1 | 0.991x | 12.019x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 156.6 | 151.6 | 165.0 | 4.6 | 1.000x | 12.133x |

### `orig` / `s-043` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 71.2 | 70.9 | 71.8 | 0.3 | 0.067x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 71.2 | 71.1 | 71.7 | 0.2 | 0.067x | 1.000x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 71.5 | 71.1 | 71.6 | 0.2 | 0.067x | 1.004x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 71.5 | 71.1 | 72.1 | 0.4 | 0.067x | 1.005x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 100.0 | 99.8 | 109.3 | 4.6 | 0.094x | 1.404x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 147.5 | 147.2 | 149.6 | 1.0 | 0.138x | 2.072x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 150.8 | 149.9 | 152.9 | 1.1 | 0.141x | 2.118x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 156.1 | 155.3 | 158.5 | 1.1 | 0.146x | 2.192x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 160.6 | 159.8 | 162.7 | 1.0 | 0.150x | 2.255x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,069.1 | 1,058.1 | 1,084.1 | 9.0 | 1.000x | 15.012x |

### `orig` / `s-044` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.3 | 11.4 | 0.4 | 0.349x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.5 | 10.3 | 11.2 | 0.3 | 0.354x | 1.015x |
| 3 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 14.8 | 14.8 | 15.0 | 0.1 | 0.499x | 1.431x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 15.4 | 14.8 | 16.2 | 0.5 | 0.518x | 1.487x |
| 5 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 16.3 | 16.3 | 17.1 | 0.3 | 0.550x | 1.578x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 16.4 | 16.4 | 16.4 | 0.0 | 0.551x | 1.582x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.6 | 29.4 | 30.6 | 0.4 | 0.995x | 2.853x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.7 | 29.0 | 30.2 | 0.4 | 1.000x | 2.869x |
| 9 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 67.6 | 67.2 | 68.2 | 0.3 | 2.274x | 6.526x |
| 10 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 67.8 | 67.3 | 67.9 | 0.2 | 2.281x | 6.545x |

### `orig` / `s-044` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 61.8 | 61.7 | 62.0 | 0.1 | 0.114x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 61.8 | 61.7 | 63.3 | 0.6 | 0.114x | 1.001x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 61.9 | 61.7 | 62.5 | 0.3 | 0.114x | 1.001x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 61.9 | 61.7 | 62.5 | 0.3 | 0.114x | 1.002x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 70.5 | 68.1 | 71.8 | 1.3 | 0.130x | 1.142x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 73.3 | 72.7 | 73.4 | 0.2 | 0.135x | 1.186x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 79.4 | 77.7 | 88.0 | 4.0 | 0.146x | 1.286x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 84.5 | 84.4 | 84.8 | 0.2 | 0.156x | 1.368x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 88.1 | 87.6 | 89.3 | 0.5 | 0.162x | 1.426x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 543.1 | 536.1 | 559.3 | 8.1 | 1.000x | 8.793x |

### `orig` / `s-045` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.6 | 12.5 | 13.4 | 0.4 | 0.081x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.5 | 12.6 | 13.7 | 0.4 | 0.087x | 1.071x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 23.5 | 23.4 | 23.7 | 0.1 | 0.151x | 1.868x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 23.6 | 23.5 | 23.6 | 0.0 | 0.152x | 1.876x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 23.7 | 23.6 | 23.9 | 0.1 | 0.153x | 1.882x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 23.7 | 23.7 | 23.9 | 0.1 | 0.153x | 1.884x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.8 | 31.6 | 32.6 | 0.3 | 0.205x | 2.528x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.0 | 31.8 | 33.7 | 0.7 | 0.206x | 2.541x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 153.1 | 148.3 | 154.9 | 2.2 | 0.986x | 12.166x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 155.2 | 150.6 | 164.7 | 4.7 | 1.000x | 12.333x |

### `orig` / `s-045` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 25.6 | 25.4 | 25.9 | 0.2 | 0.051x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 25.6 | 25.5 | 26.0 | 0.2 | 0.051x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 25.7 | 25.5 | 25.7 | 0.1 | 0.051x | 1.002x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 26.0 | 25.8 | 27.2 | 0.5 | 0.052x | 1.016x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 67.3 | 63.2 | 74.6 | 4.4 | 0.134x | 2.627x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 225.9 | 225.1 | 231.3 | 2.2 | 0.451x | 8.822x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 226.4 | 224.9 | 226.5 | 0.6 | 0.452x | 8.842x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 226.4 | 226.0 | 227.4 | 0.5 | 0.453x | 8.844x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 226.6 | 223.7 | 228.6 | 1.7 | 0.453x | 8.852x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 500.4 | 493.7 | 508.0 | 5.2 | 1.000x | 19.544x |

### `orig` / `s-046` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.8 | 21.7 | 24.6 | 1.1 | 0.046x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.8 | 21.7 | 21.9 | 0.1 | 0.046x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 25.0 | 24.6 | 25.1 | 0.2 | 0.052x | 1.148x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 25.2 | 24.8 | 26.3 | 0.6 | 0.053x | 1.157x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 50.7 | 50.2 | 56.4 | 2.4 | 0.106x | 2.327x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 50.9 | 50.0 | 54.2 | 1.5 | 0.107x | 2.336x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 52.1 | 51.9 | 52.4 | 0.2 | 0.109x | 2.390x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 52.4 | 52.0 | 53.4 | 0.5 | 0.110x | 2.403x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 475.1 | 468.2 | 476.9 | 3.5 | 0.995x | 21.796x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 477.6 | 467.1 | 488.0 | 7.7 | 1.000x | 21.913x |

### `orig` / `s-046` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 19.2 | 19.1 | 19.6 | 0.2 | 0.011x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 19.2 | 18.9 | 19.7 | 0.2 | 0.011x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 19.3 | 19.1 | 19.4 | 0.1 | 0.011x | 1.008x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 19.5 | 19.2 | 19.6 | 0.2 | 0.011x | 1.017x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 87.0 | 83.8 | 93.7 | 3.8 | 0.050x | 4.541x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 350.2 | 348.3 | 351.8 | 1.4 | 0.201x | 18.272x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 358.2 | 357.6 | 359.3 | 0.6 | 0.205x | 18.690x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 359.4 | 358.1 | 361.1 | 1.1 | 0.206x | 18.755x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 371.4 | 367.5 | 377.5 | 4.3 | 0.213x | 19.380x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,743.9 | 1,733.7 | 1,749.4 | 5.6 | 1.000x | 91.004x |

### `orig` / `s-047` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 23.1 | 26.4 | 1.3 | 0.029x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 23.3 | 23.0 | 26.8 | 1.5 | 0.029x | 1.006x |
| 3 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.8 | 25.7 | 27.4 | 0.7 | 0.032x | 1.118x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.9 | 25.8 | 27.0 | 0.5 | 0.032x | 1.120x |
| 5 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 26.0 | 26.5 | 0.2 | 0.033x | 1.130x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 26.0 | 26.3 | 0.1 | 0.033x | 1.133x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 26.1 | 32.6 | 2.5 | 0.033x | 1.134x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 26.0 | 26.5 | 0.2 | 0.033x | 1.135x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 781.5 | 774.9 | 808.1 | 12.0 | 0.973x | 33.794x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 803.0 | 772.1 | 840.7 | 23.7 | 1.000x | 34.720x |

### `orig` / `s-047` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 20.7 | 20.6 | 21.0 | 0.2 | 0.007x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 20.7 | 20.4 | 21.0 | 0.2 | 0.007x | 1.002x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 20.8 | 20.6 | 20.8 | 0.1 | 0.007x | 1.004x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 20.8 | 20.5 | 21.1 | 0.2 | 0.007x | 1.004x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 118.9 | 118.1 | 121.5 | 1.2 | 0.039x | 5.750x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 186.0 | 184.2 | 187.8 | 1.2 | 0.061x | 8.994x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 186.5 | 185.3 | 188.9 | 1.4 | 0.061x | 9.019x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 186.6 | 185.5 | 190.6 | 1.8 | 0.061x | 9.022x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 186.9 | 183.8 | 189.0 | 1.8 | 0.061x | 9.040x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,044.2 | 3,031.8 | 3,057.5 | 8.8 | 1.000x | 147.208x |

### `orig` / `s-048` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 21.6 | 3.3 | 0.044x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.5 | 13.2 | 15.3 | 0.8 | 0.045x | 1.017x |
| 3 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 16.9 | 16.9 | 17.5 | 0.3 | 0.057x | 1.278x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 17.0 | 16.9 | 17.6 | 0.2 | 0.057x | 1.283x |
| 5 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 17.5 | 17.5 | 18.0 | 0.2 | 0.059x | 1.321x |
| 6 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 17.6 | 17.4 | 18.9 | 0.6 | 0.059x | 1.328x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 18.8 | 18.7 | 18.8 | 0.0 | 0.063x | 1.416x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 18.8 | 18.8 | 18.9 | 0.0 | 0.063x | 1.419x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 295.9 | 294.0 | 301.5 | 2.7 | 0.993x | 22.326x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 298.1 | 294.3 | 321.5 | 10.2 | 1.000x | 22.492x |

### `orig` / `s-048` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 12.5 | 12.5 | 13.2 | 0.3 | 0.015x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 12.7 | 12.5 | 13.1 | 0.2 | 0.016x | 1.010x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 12.7 | 12.6 | 12.9 | 0.1 | 0.016x | 1.017x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 13.0 | 12.9 | 13.3 | 0.2 | 0.016x | 1.040x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 65.0 | 60.8 | 69.8 | 3.5 | 0.080x | 5.188x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 90.5 | 90.3 | 96.7 | 2.4 | 0.112x | 7.226x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 90.7 | 88.0 | 93.5 | 2.1 | 0.112x | 7.242x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 92.0 | 90.9 | 96.0 | 1.8 | 0.114x | 7.348x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 97.2 | 95.5 | 98.9 | 1.1 | 0.120x | 7.757x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 810.6 | 802.6 | 811.3 | 3.9 | 1.000x | 64.708x |

### `orig` / `s-049` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.3 | 12.2 | 12.4 | 0.1 | 0.085x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.4 | 12.2 | 18.4 | 2.4 | 0.085x | 1.008x |
| 3 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 21.3 | 21.3 | 21.7 | 0.2 | 0.147x | 1.737x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 22.0 | 21.5 | 22.6 | 0.4 | 0.151x | 1.788x |
| 5 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 22.3 | 22.2 | 22.3 | 0.0 | 0.153x | 1.813x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 22.3 | 22.3 | 22.4 | 0.1 | 0.154x | 1.818x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 75.9 | 75.7 | 77.0 | 0.5 | 0.523x | 6.179x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 76.2 | 76.1 | 76.4 | 0.1 | 0.525x | 6.205x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 142.8 | 142.4 | 148.2 | 2.1 | 0.984x | 11.629x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 145.2 | 144.2 | 154.8 | 3.9 | 1.000x | 11.821x |

### `orig` / `s-049` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 68.5 | 68.5 | 68.9 | 0.1 | 0.067x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 68.6 | 68.5 | 68.8 | 0.1 | 0.067x | 1.002x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 68.7 | 68.2 | 69.1 | 0.3 | 0.067x | 1.003x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 68.8 | 68.7 | 68.9 | 0.1 | 0.067x | 1.004x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 98.9 | 97.9 | 107.7 | 3.7 | 0.096x | 1.443x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 128.0 | 127.1 | 128.6 | 0.6 | 0.125x | 1.868x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 128.9 | 128.5 | 129.5 | 0.4 | 0.126x | 1.881x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 136.6 | 136.4 | 136.9 | 0.2 | 0.133x | 1.993x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 139.5 | 139.1 | 140.6 | 0.5 | 0.136x | 2.035x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,027.2 | 1,019.4 | 1,029.7 | 3.8 | 1.000x | 14.988x |

### `orig` / `s-050` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.7 | 14.6 | 16.5 | 0.7 | 0.048x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 14.7 | 14.6 | 15.8 | 0.4 | 0.048x | 1.001x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 41.5 | 41.1 | 42.6 | 0.5 | 0.135x | 2.827x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 41.8 | 41.6 | 43.0 | 0.5 | 0.137x | 2.849x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 42.6 | 41.1 | 43.0 | 0.7 | 0.139x | 2.901x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 43.7 | 42.2 | 49.0 | 2.4 | 0.143x | 2.979x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 60.7 | 60.5 | 67.6 | 2.7 | 0.198x | 4.140x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 61.1 | 60.9 | 62.0 | 0.4 | 0.200x | 4.167x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 300.0 | 296.9 | 300.6 | 1.4 | 0.980x | 20.447x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 306.1 | 298.3 | 324.4 | 9.2 | 1.000x | 20.867x |

### `orig` / `s-050` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 53.7 | 53.7 | 53.9 | 0.1 | 0.033x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 53.8 | 53.7 | 54.2 | 0.2 | 0.033x | 1.002x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 53.9 | 53.7 | 54.1 | 0.2 | 0.033x | 1.003x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 53.9 | 53.7 | 54.1 | 0.1 | 0.033x | 1.004x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 104.5 | 103.9 | 113.6 | 3.7 | 0.064x | 1.947x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 291.6 | 290.3 | 294.8 | 1.5 | 0.179x | 5.431x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 297.2 | 296.2 | 299.1 | 1.2 | 0.182x | 5.535x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 301.9 | 298.5 | 304.0 | 1.9 | 0.185x | 5.622x |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 304.7 | 303.9 | 307.5 | 1.5 | 0.187x | 5.674x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,629.6 | 1,627.6 | 1,640.2 | 5.5 | 1.000x | 30.349x |

### `orig` / `s-051` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.3 | 12.2 | 12.4 | 0.1 | 0.085x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.3 | 12.1 | 12.5 | 0.1 | 0.085x | 1.005x |
| 3 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 22.2 | 21.3 | 22.4 | 0.5 | 0.154x | 1.814x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 22.3 | 22.2 | 23.6 | 0.5 | 0.155x | 1.819x |
| 5 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 22.3 | 22.3 | 22.4 | 0.0 | 0.155x | 1.822x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 22.5 | 21.5 | 23.0 | 0.5 | 0.156x | 1.837x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 76.4 | 76.0 | 80.6 | 1.8 | 0.531x | 6.238x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 76.6 | 76.3 | 76.7 | 0.2 | 0.532x | 6.251x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 141.6 | 139.9 | 147.5 | 2.6 | 0.983x | 11.554x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 144.0 | 139.8 | 156.0 | 5.5 | 1.000x | 11.752x |

### `orig` / `s-051` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 68.7 | 68.5 | 68.8 | 0.1 | 0.067x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 68.7 | 68.6 | 69.1 | 0.2 | 0.067x | 1.000x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 68.7 | 68.4 | 69.1 | 0.2 | 0.067x | 1.001x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 68.7 | 68.6 | 69.0 | 0.1 | 0.067x | 1.001x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 99.5 | 97.2 | 107.1 | 3.6 | 0.097x | 1.449x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 127.0 | 126.6 | 127.9 | 0.5 | 0.124x | 1.849x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 128.8 | 128.6 | 130.2 | 0.6 | 0.126x | 1.876x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 136.3 | 135.9 | 140.7 | 1.9 | 0.133x | 1.985x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 139.6 | 139.3 | 140.5 | 0.4 | 0.136x | 2.034x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,025.9 | 1,015.6 | 1,027.5 | 4.4 | 1.000x | 14.940x |

### `orig` / `s-052` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.5 | 13.4 | 13.9 | 0.2 | 0.045x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.6 | 13.3 | 15.0 | 0.6 | 0.045x | 1.008x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 25.6 | 24.7 | 27.1 | 0.9 | 0.086x | 1.899x |
| 4 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.8 | 25.7 | 25.9 | 0.1 | 0.086x | 1.916x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 26.0 | 25.5 | 27.1 | 0.5 | 0.087x | 1.930x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 26.2 | 26.3 | 0.1 | 0.088x | 1.945x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.3 | 26.2 | 26.4 | 0.1 | 0.088x | 1.947x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 26.9 | 25.7 | 28.6 | 1.0 | 0.090x | 1.995x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 293.8 | 292.8 | 300.8 | 2.9 | 0.981x | 21.792x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 299.4 | 293.1 | 319.6 | 9.7 | 1.000x | 22.204x |

### `orig` / `s-052` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 19.5 | 19.4 | 20.2 | 0.3 | 0.018x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 19.7 | 19.5 | 19.9 | 0.1 | 0.018x | 1.009x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 19.7 | 19.6 | 20.3 | 0.3 | 0.018x | 1.009x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 19.7 | 19.6 | 20.3 | 0.3 | 0.018x | 1.010x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 69.2 | 67.3 | 76.9 | 3.5 | 0.064x | 3.543x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 177.6 | 175.7 | 181.1 | 2.3 | 0.164x | 9.094x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 179.2 | 175.5 | 184.7 | 3.4 | 0.166x | 9.177x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 179.6 | 178.0 | 181.5 | 1.3 | 0.166x | 9.197x |
| 9 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 180.2 | 176.7 | 182.8 | 2.0 | 0.167x | 9.225x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,079.8 | 1,062.5 | 1,084.7 | 8.2 | 1.000x | 55.290x |

### `orig` / `s-053` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.3 | 15.1 | 0.7 | 0.045x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.5 | 0.1 | 0.045x | 1.006x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.7 | 20.6 | 22.2 | 0.6 | 0.070x | 1.557x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 20.6 | 23.7 | 1.1 | 0.073x | 1.620x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.8 | 25.7 | 26.2 | 0.2 | 0.087x | 1.941x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 26.0 | 26.4 | 0.1 | 0.088x | 1.963x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 26.0 | 26.4 | 0.1 | 0.089x | 1.973x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 26.3 | 25.5 | 26.8 | 0.4 | 0.089x | 1.978x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 295.3 | 293.5 | 303.7 | 4.1 | 0.998x | 22.199x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 295.9 | 293.3 | 317.7 | 9.1 | 1.000x | 22.242x |

### `orig` / `s-053` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 14.7 | 14.6 | 14.9 | 0.1 | 0.014x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 14.7 | 14.6 | 15.5 | 0.3 | 0.014x | 1.003x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 14.9 | 14.7 | 15.0 | 0.1 | 0.014x | 1.011x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 14.9 | 14.9 | 15.6 | 0.3 | 0.014x | 1.016x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.6 | 65.8 | 75.4 | 3.4 | 0.064x | 4.665x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 167.7 | 166.7 | 174.6 | 3.0 | 0.157x | 11.411x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 168.2 | 167.0 | 171.4 | 1.7 | 0.158x | 11.441x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 168.4 | 164.3 | 170.7 | 2.2 | 0.158x | 11.458x |
| 9 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 169.1 | 166.3 | 170.8 | 1.7 | 0.158x | 11.504x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,067.1 | 1,061.5 | 1,075.5 | 4.5 | 1.000x | 72.590x |

### `orig` / `s-054` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.3 | 13.9 | 0.2 | 0.044x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.6 | 13.3 | 15.2 | 0.7 | 0.045x | 1.015x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.7 | 20.6 | 21.4 | 0.3 | 0.069x | 1.549x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.3 | 20.6 | 22.0 | 0.6 | 0.071x | 1.595x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.8 | 25.7 | 26.0 | 0.1 | 0.086x | 1.930x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 26.0 | 25.5 | 26.3 | 0.3 | 0.086x | 1.945x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 26.1 | 26.3 | 0.1 | 0.087x | 1.957x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 26.1 | 26.2 | 0.0 | 0.087x | 1.958x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 295.5 | 289.6 | 304.5 | 4.8 | 0.980x | 22.096x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 301.6 | 293.8 | 319.8 | 9.3 | 1.000x | 22.554x |

### `orig` / `s-054` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 14.6 | 14.5 | 14.9 | 0.1 | 0.014x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 14.7 | 14.6 | 14.7 | 0.0 | 0.014x | 1.006x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 14.8 | 14.4 | 15.5 | 0.4 | 0.014x | 1.008x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 14.8 | 14.8 | 15.0 | 0.1 | 0.014x | 1.014x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.2 | 66.1 | 75.3 | 3.3 | 0.064x | 4.658x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 168.6 | 165.5 | 169.6 | 1.4 | 0.158x | 11.514x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 168.7 | 167.6 | 169.7 | 0.7 | 0.158x | 11.518x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 169.8 | 167.3 | 175.2 | 2.7 | 0.159x | 11.595x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 171.3 | 165.7 | 172.5 | 2.6 | 0.160x | 11.697x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,068.6 | 1,059.8 | 1,077.3 | 5.6 | 1.000x | 72.977x |

### `orig` / `s-055` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.4 | 0.0 | 0.045x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.2 | 17.0 | 1.5 | 0.045x | 1.005x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 20.7 | 20.5 | 21.9 | 0.6 | 0.069x | 1.551x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.7 | 20.7 | 21.4 | 0.3 | 0.069x | 1.555x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.8 | 25.5 | 26.3 | 0.3 | 0.086x | 1.934x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.8 | 25.7 | 25.8 | 0.1 | 0.086x | 1.935x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 26.1 | 26.3 | 0.1 | 0.087x | 1.964x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 26.0 | 26.5 | 0.2 | 0.088x | 1.968x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 296.1 | 291.1 | 299.2 | 2.6 | 0.990x | 22.234x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 299.2 | 294.6 | 320.9 | 9.8 | 1.000x | 22.462x |

### `orig` / `s-055` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 14.6 | 14.5 | 14.7 | 0.1 | 0.014x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 14.7 | 14.5 | 15.2 | 0.3 | 0.014x | 1.008x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 14.7 | 14.6 | 14.7 | 0.1 | 0.014x | 1.010x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 14.9 | 14.7 | 15.3 | 0.2 | 0.014x | 1.020x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.2 | 64.9 | 75.3 | 3.7 | 0.064x | 4.683x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 167.5 | 165.6 | 172.1 | 2.7 | 0.157x | 11.502x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 168.3 | 165.6 | 175.7 | 3.5 | 0.157x | 11.552x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 168.3 | 168.0 | 170.1 | 0.7 | 0.158x | 11.556x |
| 9 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 169.7 | 168.1 | 171.1 | 1.2 | 0.159x | 11.652x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,068.5 | 1,067.6 | 1,071.7 | 1.7 | 1.000x | 73.354x |

### `orig` / `s-056` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.5 | 0.1 | 0.045x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.3 | 16.1 | 1.1 | 0.045x | 1.003x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 22.1 | 21.3 | 22.7 | 0.4 | 0.074x | 1.657x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 22.5 | 21.4 | 22.9 | 0.6 | 0.076x | 1.691x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.7 | 25.4 | 26.3 | 0.3 | 0.086x | 1.929x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.9 | 25.6 | 27.5 | 0.7 | 0.087x | 1.939x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 26.1 | 26.4 | 0.1 | 0.088x | 1.956x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 26.1 | 26.6 | 0.2 | 0.088x | 1.961x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 293.7 | 290.6 | 298.4 | 3.0 | 0.986x | 22.021x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 297.7 | 290.8 | 319.8 | 10.6 | 1.000x | 22.327x |

### `orig` / `s-056` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 16.3 | 16.2 | 16.9 | 0.3 | 0.015x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 16.3 | 16.2 | 16.5 | 0.1 | 0.015x | 1.002x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 16.5 | 16.4 | 19.3 | 1.1 | 0.015x | 1.013x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 16.6 | 16.3 | 17.0 | 0.2 | 0.016x | 1.019x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.2 | 65.3 | 75.3 | 3.6 | 0.064x | 4.188x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 158.8 | 155.0 | 161.1 | 2.1 | 0.149x | 9.749x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 159.4 | 157.8 | 164.5 | 2.4 | 0.150x | 9.788x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 161.0 | 157.0 | 162.5 | 1.9 | 0.151x | 9.886x |
| 9 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 161.4 | 157.7 | 171.0 | 4.7 | 0.152x | 9.913x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,065.5 | 1,061.9 | 1,068.2 | 2.1 | 1.000x | 65.429x |

### `orig` / `s-057` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7,669.5 | 7,664.9 | 7,678.1 | 5.1 | 0.779x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 7,685.2 | 7,675.4 | 7,730.7 | 20.2 | 0.781x | 1.002x |
| 3 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7,687.3 | 7,674.7 | 7,782.4 | 40.2 | 0.781x | 1.002x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 7,699.0 | 7,683.5 | 7,701.2 | 6.9 | 0.782x | 1.004x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 9,843.7 | 9,804.9 | 10,041.6 | 85.8 | 1.000x | 1.283x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 9,881.0 | 9,849.1 | 9,926.6 | 32.5 | 1.004x | 1.288x |
| 7 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19,097.0 | 19,088.9 | 19,124.3 | 12.2 | 1.940x | 2.490x |
| 8 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 19,097.0 | 19,084.5 | 19,114.0 | 10.4 | 1.940x | 2.490x |
| 9 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 38,207.4 | 38,199.0 | 38,218.0 | 6.3 | 3.881x | 4.982x |
| 10 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 38,209.5 | 38,196.4 | 38,417.8 | 85.1 | 3.882x | 4.982x |

### `orig` / `s-058` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5,977.4 | 5,907.7 | 5,984.6 | 29.2 | 0.082x | 1.000x |
| 2 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6,022.5 | 6,003.8 | 6,065.3 | 21.3 | 0.083x | 1.008x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 6,271.7 | 6,235.2 | 6,323.1 | 28.5 | 0.086x | 1.049x |
| 4 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 6,329.1 | 6,133.4 | 6,404.6 | 93.8 | 0.087x | 1.059x |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 7,469.8 | 7,465.9 | 7,478.7 | 4.2 | 0.103x | 1.250x |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7,478.3 | 7,465.9 | 7,515.2 | 18.1 | 0.103x | 1.251x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 14,798.6 | 14,776.9 | 14,822.6 | 16.8 | 0.203x | 2.476x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14,819.1 | 14,774.9 | 14,856.1 | 29.6 | 0.204x | 2.479x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 72,740.3 | 72,232.6 | 78,864.7 | 2,541.2 | 1.000x | 12.169x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 72,920.0 | 72,661.7 | 73,373.1 | 267.1 | 1.002x | 12.199x |

### `orig` / `s-059` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9,565.9 | 9,557.7 | 9,569.5 | 4.0 | 0.060x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9,569.7 | 9,556.2 | 9,577.5 | 7.6 | 0.060x | 1.000x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 13,696.0 | 13,694.5 | 13,914.5 | 85.8 | 0.086x | 1.432x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 13,711.8 | 13,679.6 | 13,737.8 | 21.3 | 0.086x | 1.433x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 13,721.9 | 13,699.7 | 13,784.8 | 31.0 | 0.086x | 1.434x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 13,749.7 | 13,733.8 | 13,823.4 | 33.0 | 0.086x | 1.437x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19,124.1 | 19,117.7 | 19,125.4 | 3.1 | 0.120x | 1.999x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 19,125.7 | 19,122.4 | 19,134.1 | 4.2 | 0.120x | 1.999x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 158,848.8 | 158,747.6 | 159,514.8 | 283.8 | 0.997x | 16.606x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 159,273.9 | 158,639.9 | 161,064.3 | 814.7 | 1.000x | 16.650x |

### `orig` / `s-060` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7,644.3 | 7,634.5 | 7,652.7 | 6.4 | 0.811x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 7,648.7 | 7,645.9 | 7,724.8 | 29.9 | 0.812x | 1.001x |
| 3 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7,650.9 | 7,639.3 | 7,657.0 | 6.4 | 0.812x | 1.001x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 7,654.5 | 7,635.3 | 7,769.2 | 47.8 | 0.812x | 1.001x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 9,422.4 | 9,421.2 | 9,474.9 | 20.7 | 1.000x | 1.233x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 9,424.9 | 9,418.5 | 9,436.0 | 7.4 | 1.000x | 1.233x |
| 7 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19,068.4 | 19,059.8 | 19,178.4 | 44.6 | 2.023x | 2.494x |
| 8 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 19,107.8 | 19,076.2 | 19,152.9 | 28.2 | 2.027x | 2.500x |
| 9 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 19,303.3 | 19,298.1 | 19,315.6 | 6.0 | 2.048x | 2.525x |
| 10 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19,309.9 | 19,299.1 | 19,317.6 | 6.7 | 2.049x | 2.526x |

### `orig` / `s-061` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 3,741.0 | 3,738.9 | 3,747.3 | 3.6 | 0.084x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 3,748.6 | 3,740.0 | 3,758.4 | 6.8 | 0.084x | 1.002x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6,134.8 | 6,132.9 | 6,174.2 | 15.8 | 0.138x | 1.640x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6,146.7 | 6,138.6 | 6,214.9 | 29.1 | 0.138x | 1.643x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 6,550.6 | 6,546.3 | 6,658.3 | 45.3 | 0.147x | 1.751x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 6,554.1 | 6,526.1 | 6,561.2 | 12.7 | 0.147x | 1.752x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 7,480.2 | 7,476.1 | 7,483.8 | 2.8 | 0.168x | 2.000x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7,483.2 | 7,477.2 | 7,488.3 | 3.9 | 0.168x | 2.000x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 44,512.8 | 44,482.3 | 45,296.2 | 314.0 | 1.000x | 11.899x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44,622.2 | 44,533.8 | 45,309.4 | 286.4 | 1.002x | 11.928x |

### `orig` / `s-062` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.0 | 16.0 | 18.2 | 0.9 | 0.050x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.2 | 0.1 | 0.051x | 1.005x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 43.2 | 42.4 | 45.5 | 1.1 | 0.136x | 2.697x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 51.5 | 48.9 | 52.6 | 1.5 | 0.162x | 3.209x |
| 5 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 53.0 | 50.2 | 53.2 | 1.1 | 0.167x | 3.305x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 53.7 | 51.1 | 53.9 | 1.1 | 0.169x | 3.353x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 313.8 | 310.1 | 319.0 | 3.0 | 0.988x | 19.576x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 317.6 | 312.9 | 331.4 | 6.8 | 1.000x | 19.813x |
| 9 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 977.5 | 972.5 | 978.9 | 2.3 | 3.077x | 60.970x |
| 10 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 979.4 | 978.4 | 986.7 | 3.1 | 3.083x | 61.090x |

### `orig` / `s-063` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 4,794.4 | 4,791.6 | 4,799.2 | 2.6 | 0.044x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4,801.2 | 4,790.8 | 4,825.8 | 13.0 | 0.044x | 1.001x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 6,850.3 | 6,848.7 | 6,860.3 | 4.2 | 0.062x | 1.429x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6,856.5 | 6,849.4 | 6,880.9 | 11.4 | 0.062x | 1.430x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 6,858.6 | 6,853.9 | 6,886.8 | 13.2 | 0.062x | 1.431x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6,861.3 | 6,853.9 | 6,870.0 | 5.7 | 0.062x | 1.431x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 14,399.2 | 14,390.9 | 14,462.2 | 28.1 | 0.131x | 3.003x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14,401.8 | 14,394.8 | 14,429.7 | 12.3 | 0.131x | 3.004x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 109,959.2 | 108,760.6 | 110,805.2 | 663.2 | 1.000x | 22.935x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 110,153.7 | 109,925.7 | 110,455.1 | 192.0 | 1.002x | 22.976x |

### `orig` / `s-064` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 7,655.8 | 7,651.2 | 7,665.5 | 5.2 | 0.081x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7,662.2 | 7,654.4 | 7,743.9 | 33.3 | 0.081x | 1.001x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 10,588.5 | 10,578.9 | 10,657.6 | 28.8 | 0.111x | 1.383x |
| 4 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 10,601.5 | 10,581.1 | 10,681.3 | 38.0 | 0.111x | 1.385x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 10,636.5 | 10,577.7 | 10,765.6 | 67.1 | 0.112x | 1.389x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 10,658.7 | 10,648.9 | 10,707.9 | 21.5 | 0.112x | 1.392x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 15,312.5 | 15,307.6 | 15,336.1 | 10.1 | 0.161x | 2.000x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 15,313.1 | 15,305.6 | 15,323.5 | 6.6 | 0.161x | 2.000x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 95,095.4 | 94,725.1 | 97,599.3 | 1,055.3 | 1.000x | 12.421x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 95,261.5 | 94,844.0 | 95,374.2 | 206.7 | 1.002x | 12.443x |

### `orig` / `s-065` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.3 | 10.6 | 0.1 | 0.356x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.4 | 10.6 | 0.1 | 0.357x | 1.002x |
| 3 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 14.9 | 14.9 | 15.0 | 0.1 | 0.508x | 1.427x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 15.6 | 15.2 | 16.4 | 0.4 | 0.533x | 1.497x |
| 5 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 16.4 | 16.3 | 17.2 | 0.3 | 0.560x | 1.572x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 16.5 | 16.4 | 17.9 | 0.6 | 0.563x | 1.581x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 27.1 | 26.9 | 29.3 | 0.9 | 0.925x | 2.600x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 28.3 | 26.6 | 29.2 | 1.0 | 0.966x | 2.713x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.2 | 28.9 | 29.4 | 0.2 | 1.000x | 2.809x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.3 | 29.1 | 29.6 | 0.2 | 1.002x | 2.815x |

### `orig` / `s-065` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 21.4 | 21.1 | 22.0 | 0.3 | 0.038x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 21.5 | 21.4 | 22.4 | 0.4 | 0.038x | 1.001x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 21.5 | 21.2 | 22.4 | 0.4 | 0.038x | 1.003x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 21.8 | 21.1 | 22.1 | 0.4 | 0.039x | 1.015x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 63.0 | 60.7 | 70.1 | 3.5 | 0.112x | 2.938x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 227.5 | 227.0 | 231.4 | 1.6 | 0.404x | 10.614x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 228.6 | 226.1 | 242.3 | 5.8 | 0.406x | 10.666x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 229.9 | 229.2 | 230.3 | 0.4 | 0.408x | 10.726x |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 230.4 | 227.7 | 231.4 | 1.4 | 0.409x | 10.750x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 563.5 | 555.5 | 565.2 | 3.5 | 1.000x | 26.287x |

### `orig` / `s-066` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33.8 | 33.7 | 33.9 | 0.0 | 0.051x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.8 | 33.7 | 40.3 | 2.6 | 0.051x | 1.000x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 55.3 | 55.2 | 55.4 | 0.1 | 0.083x | 1.636x |
| 4 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 55.6 | 55.3 | 56.0 | 0.3 | 0.084x | 1.646x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 57.9 | 57.9 | 60.2 | 0.9 | 0.087x | 1.714x |
| 6 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 72.9 | 72.7 | 73.1 | 0.2 | 0.110x | 2.157x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73.0 | 72.6 | 74.1 | 0.5 | 0.110x | 2.161x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 73.3 | 73.0 | 73.4 | 0.1 | 0.110x | 2.169x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 659.7 | 643.8 | 667.6 | 8.4 | 0.992x | 19.528x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 665.2 | 658.5 | 673.3 | 6.2 | 1.000x | 19.691x |

### `orig` / `s-066` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 62.1 | 61.6 | 62.4 | 0.3 | 0.094x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 62.5 | 62.4 | 62.7 | 0.1 | 0.094x | 1.007x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 62.5 | 62.5 | 70.5 | 3.2 | 0.094x | 1.007x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 62.7 | 62.7 | 63.1 | 0.1 | 0.095x | 1.010x |
| 5 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 62.8 | 62.4 | 62.9 | 0.2 | 0.095x | 1.011x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 64.6 | 64.1 | 65.0 | 0.3 | 0.097x | 1.039x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 78.7 | 78.1 | 80.0 | 0.7 | 0.119x | 1.268x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 81.2 | 80.8 | 82.0 | 0.4 | 0.122x | 1.308x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 81.6 | 78.1 | 93.3 | 5.4 | 0.123x | 1.315x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 663.5 | 660.9 | 667.4 | 2.1 | 1.000x | 10.683x |

### `orig` / `s-067` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.3 | 32.4 | 0.1 | 0.050x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.5 | 32.3 | 35.3 | 1.2 | 0.050x | 1.005x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 69.0 | 68.9 | 69.5 | 0.2 | 0.106x | 2.136x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 69.3 | 68.9 | 72.3 | 1.2 | 0.107x | 2.145x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 73.7 | 72.6 | 74.1 | 0.6 | 0.113x | 2.279x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 74.4 | 71.9 | 75.8 | 1.3 | 0.115x | 2.303x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 75.8 | 73.6 | 77.5 | 1.4 | 0.117x | 2.346x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 81.7 | 81.2 | 83.2 | 0.7 | 0.126x | 2.527x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 633.5 | 621.0 | 647.4 | 8.5 | 0.975x | 19.600x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 649.7 | 639.7 | 650.4 | 4.4 | 1.000x | 20.100x |

### `orig` / `s-067` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 58.3 | 58.2 | 58.4 | 0.1 | 0.091x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 58.5 | 58.4 | 62.4 | 1.6 | 0.091x | 1.003x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 58.5 | 58.2 | 59.1 | 0.3 | 0.091x | 1.004x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 58.5 | 58.2 | 59.1 | 0.3 | 0.091x | 1.004x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 82.2 | 81.1 | 92.5 | 4.3 | 0.128x | 1.411x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 84.6 | 84.5 | 86.3 | 0.7 | 0.131x | 1.452x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 87.3 | 87.1 | 89.6 | 0.9 | 0.136x | 1.498x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 88.3 | 88.2 | 88.9 | 0.3 | 0.137x | 1.514x |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 90.3 | 90.1 | 90.4 | 0.1 | 0.140x | 1.548x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 643.8 | 635.0 | 647.3 | 4.7 | 1.000x | 11.044x |

### `orig` / `s-068` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.8 | 16.8 | 16.8 | 0.0 | 0.040x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.8 | 16.7 | 16.8 | 0.0 | 0.041x | 1.000x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 18.0 | 17.9 | 18.4 | 0.2 | 0.043x | 1.072x |
| 4 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 18.0 | 17.9 | 18.2 | 0.1 | 0.044x | 1.074x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 20.8 | 20.8 | 23.3 | 1.0 | 0.050x | 1.238x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 20.8 | 20.7 | 21.4 | 0.3 | 0.050x | 1.239x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.5 | 29.4 | 32.7 | 1.3 | 0.071x | 1.758x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.7 | 29.5 | 29.9 | 0.1 | 0.072x | 1.770x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 414.3 | 410.4 | 422.6 | 4.3 | 1.000x | 24.695x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 414.5 | 409.2 | 417.4 | 3.1 | 1.001x | 24.710x |

### `orig` / `s-068` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 23.2 | 23.0 | 23.8 | 0.3 | 0.056x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 23.2 | 23.1 | 23.3 | 0.1 | 0.056x | 1.001x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 23.2 | 22.9 | 25.0 | 0.7 | 0.056x | 1.001x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 23.3 | 23.1 | 23.3 | 0.1 | 0.056x | 1.006x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 23.7 | 23.6 | 24.0 | 0.1 | 0.057x | 1.025x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 23.7 | 23.6 | 24.3 | 0.2 | 0.058x | 1.025x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 26.0 | 26.0 | 26.1 | 0.0 | 0.063x | 1.125x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 26.1 | 26.0 | 52.2 | 10.4 | 0.063x | 1.126x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 62.0 | 56.8 | 71.3 | 4.9 | 0.150x | 2.678x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 412.9 | 405.2 | 418.8 | 4.6 | 1.000x | 17.831x |

### `orig` / `s-069` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.6 | 12.6 | 12.8 | 0.1 | 0.059x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.8 | 12.7 | 13.9 | 0.5 | 0.060x | 1.012x |
| 3 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.5 | 25.2 | 26.0 | 0.3 | 0.120x | 2.020x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 25.2 | 27.9 | 1.0 | 0.122x | 2.066x |
| 5 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 26.2 | 26.8 | 0.3 | 0.123x | 2.072x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 26.0 | 26.7 | 0.2 | 0.123x | 2.077x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.4 | 33.3 | 34.3 | 0.4 | 0.156x | 2.641x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33.4 | 33.0 | 34.5 | 0.5 | 0.157x | 2.646x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 207.0 | 205.5 | 212.0 | 2.3 | 0.970x | 16.385x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 213.5 | 205.6 | 215.7 | 3.8 | 1.000x | 16.897x |

### `orig` / `s-069` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 27.2 | 27.1 | 28.6 | 0.6 | 0.037x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 27.2 | 27.2 | 27.3 | 0.0 | 0.037x | 1.003x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 27.3 | 27.1 | 27.9 | 0.3 | 0.037x | 1.005x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 27.3 | 27.1 | 27.9 | 0.3 | 0.037x | 1.005x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 71.3 | 65.2 | 86.8 | 7.7 | 0.098x | 2.626x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 236.1 | 233.1 | 239.1 | 2.2 | 0.324x | 8.691x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 238.3 | 234.5 | 242.8 | 2.8 | 0.327x | 8.774x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 238.5 | 234.9 | 250.0 | 5.4 | 0.327x | 8.779x |
| 9 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 242.4 | 236.3 | 257.5 | 7.1 | 0.332x | 8.923x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 729.1 | 725.5 | 732.5 | 2.4 | 1.000x | 26.844x |

### `orig` / `s-070` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 28.0 | 27.9 | 28.2 | 0.1 | 0.051x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 28.1 | 27.9 | 28.1 | 0.1 | 0.051x | 1.003x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 42.0 | 42.0 | 45.7 | 1.4 | 0.077x | 1.501x |
| 4 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 42.1 | 41.9 | 42.8 | 0.3 | 0.077x | 1.505x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 44.7 | 44.5 | 47.7 | 1.2 | 0.082x | 1.599x |
| 6 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 58.2 | 57.9 | 58.4 | 0.2 | 0.107x | 2.080x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 58.3 | 58.2 | 59.7 | 0.5 | 0.107x | 2.083x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 63.0 | 62.4 | 63.1 | 0.3 | 0.116x | 2.252x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 535.1 | 532.8 | 543.7 | 4.1 | 0.981x | 19.118x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 545.4 | 543.3 | 553.9 | 4.4 | 1.000x | 19.489x |

### `orig` / `s-070` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 48.4 | 48.3 | 48.8 | 0.2 | 0.089x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 48.5 | 48.5 | 48.9 | 0.2 | 0.089x | 1.001x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 48.5 | 48.3 | 52.8 | 1.7 | 0.089x | 1.002x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 48.6 | 48.3 | 52.8 | 1.7 | 0.090x | 1.004x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 50.5 | 50.0 | 50.9 | 0.3 | 0.093x | 1.043x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 52.3 | 51.7 | 52.6 | 0.3 | 0.096x | 1.080x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 60.1 | 57.8 | 62.8 | 1.8 | 0.111x | 1.241x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 71.2 | 70.8 | 71.5 | 0.3 | 0.131x | 1.469x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 75.3 | 72.9 | 85.4 | 4.8 | 0.139x | 1.555x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 542.9 | 542.0 | 544.0 | 0.7 | 1.000x | 11.209x |

### `orig` / `s-071` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 55.5 | 55.2 | 55.9 | 0.2 | 0.098x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 55.6 | 55.5 | 56.7 | 0.5 | 0.098x | 1.001x |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 55.7 | 55.6 | 57.5 | 0.7 | 0.099x | 1.003x |
| 4 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 55.7 | 55.6 | 56.1 | 0.2 | 0.099x | 1.004x |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 58.3 | 58.0 | 60.8 | 1.0 | 0.103x | 1.050x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 73.0 | 72.7 | 74.1 | 0.5 | 0.129x | 1.315x |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 120.1 | 119.7 | 121.0 | 0.5 | 0.213x | 2.164x |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 120.8 | 120.0 | 121.5 | 0.5 | 0.214x | 2.176x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 559.5 | 558.2 | 565.6 | 2.7 | 0.991x | 10.077x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 564.4 | 556.6 | 578.9 | 8.8 | 1.000x | 10.165x |

### `orig` / `s-071` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 64.7 | 63.5 | 65.0 | 0.6 | 0.115x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 65.0 | 64.4 | 66.5 | 0.7 | 0.115x | 1.005x |
| 3 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 78.2 | 76.8 | 82.0 | 1.7 | 0.139x | 1.209x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 81.3 | 81.0 | 81.8 | 0.3 | 0.144x | 1.257x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 89.7 | 88.6 | 99.6 | 4.4 | 0.159x | 1.387x |
| 6 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 109.6 | 109.6 | 109.9 | 0.1 | 0.194x | 1.694x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 109.6 | 109.6 | 112.8 | 1.3 | 0.194x | 1.695x |
| 8 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 109.7 | 109.7 | 110.1 | 0.2 | 0.194x | 1.696x |
| 9 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 109.7 | 109.5 | 110.1 | 0.2 | 0.194x | 1.696x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 564.2 | 561.1 | 565.2 | 1.4 | 1.000x | 8.722x |

### `orig` / `s-072` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 42.7 | 42.6 | 43.0 | 0.1 | 0.035x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 43.4 | 42.6 | 44.9 | 0.9 | 0.036x | 1.016x |
| 3 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 65.3 | 65.2 | 65.4 | 0.1 | 0.054x | 1.528x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 65.3 | 65.1 | 65.4 | 0.1 | 0.054x | 1.529x |
| 5 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 67.1 | 67.0 | 67.2 | 0.1 | 0.055x | 1.570x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 67.2 | 67.0 | 67.3 | 0.1 | 0.055x | 1.573x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 98.6 | 97.5 | 99.1 | 0.5 | 0.081x | 2.309x |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 98.7 | 98.3 | 99.1 | 0.3 | 0.081x | 2.309x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,181.0 | 1,177.9 | 1,187.4 | 3.1 | 0.970x | 27.648x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,217.3 | 1,183.2 | 1,241.9 | 22.2 | 1.000x | 28.498x |

### `orig` / `s-072` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 89.3 | 89.0 | 90.3 | 0.5 | 0.051x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 89.4 | 89.3 | 93.0 | 1.5 | 0.051x | 1.001x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 89.5 | 89.4 | 89.8 | 0.2 | 0.051x | 1.002x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 89.5 | 89.5 | 95.0 | 2.2 | 0.051x | 1.003x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 135.2 | 130.8 | 141.3 | 3.4 | 0.077x | 1.514x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 143.9 | 143.1 | 146.3 | 1.3 | 0.082x | 1.611x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 147.2 | 146.9 | 150.0 | 1.2 | 0.084x | 1.648x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 150.6 | 150.0 | 151.0 | 0.4 | 0.086x | 1.686x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 170.4 | 167.5 | 180.3 | 5.0 | 0.097x | 1.908x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,750.8 | 1,738.0 | 1,765.4 | 9.4 | 1.000x | 19.607x |

### `orig` / `s-073` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.3 | 15.0 | 0.7 | 0.044x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.5 | 13.3 | 18.9 | 2.2 | 0.045x | 1.007x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 24.8 | 24.6 | 25.1 | 0.2 | 0.082x | 1.857x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 25.2 | 24.6 | 26.3 | 0.6 | 0.083x | 1.885x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.8 | 25.7 | 27.6 | 0.8 | 0.085x | 1.930x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 26.0 | 25.6 | 27.4 | 0.6 | 0.086x | 1.943x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 26.1 | 26.2 | 0.0 | 0.087x | 1.958x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.3 | 26.2 | 26.5 | 0.1 | 0.087x | 1.967x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 299.8 | 296.0 | 301.6 | 1.9 | 0.993x | 22.429x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 301.9 | 294.6 | 312.8 | 7.4 | 1.000x | 22.590x |

### `orig` / `s-073` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 20.5 | 20.4 | 20.8 | 0.1 | 0.019x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 20.5 | 20.4 | 21.1 | 0.3 | 0.019x | 1.002x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 20.6 | 20.4 | 25.1 | 1.8 | 0.019x | 1.004x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 20.6 | 20.5 | 20.8 | 0.1 | 0.019x | 1.004x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 69.0 | 67.5 | 77.2 | 3.9 | 0.064x | 3.372x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 190.0 | 189.0 | 192.7 | 1.3 | 0.177x | 9.279x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 191.2 | 190.1 | 193.3 | 1.1 | 0.178x | 9.340x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 195.5 | 191.7 | 198.2 | 2.2 | 0.182x | 9.549x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 200.7 | 196.4 | 209.3 | 4.4 | 0.187x | 9.803x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,075.6 | 1,071.7 | 1,123.8 | 24.9 | 1.000x | 52.535x |

### `orig` / `s-074` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.4 | 0.1 | 0.044x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.3 | 15.1 | 0.7 | 0.044x | 1.003x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.0 | 31.8 | 33.3 | 0.6 | 0.106x | 2.398x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.0 | 31.6 | 32.1 | 0.2 | 0.106x | 2.399x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 32.9 | 32.7 | 33.6 | 0.4 | 0.109x | 2.461x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 35.1 | 35.0 | 35.3 | 0.1 | 0.116x | 2.629x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 35.2 | 35.1 | 35.6 | 0.2 | 0.117x | 2.637x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 35.9 | 34.2 | 36.5 | 0.8 | 0.119x | 2.690x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 299.2 | 294.9 | 299.9 | 1.9 | 0.993x | 22.418x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 301.4 | 295.0 | 311.4 | 6.3 | 1.000x | 22.584x |

### `orig` / `s-074` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 26.8 | 26.7 | 27.4 | 0.2 | 0.025x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 26.9 | 26.7 | 27.7 | 0.3 | 0.025x | 1.003x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 26.9 | 26.7 | 27.1 | 0.2 | 0.025x | 1.003x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 27.3 | 26.7 | 32.8 | 2.3 | 0.025x | 1.016x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 72.2 | 69.7 | 78.1 | 3.3 | 0.068x | 2.691x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 301.7 | 299.9 | 303.5 | 1.2 | 0.282x | 11.247x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 302.0 | 300.2 | 309.7 | 3.5 | 0.282x | 11.256x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 303.4 | 300.8 | 307.9 | 2.3 | 0.284x | 11.308x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 303.9 | 301.9 | 309.1 | 2.5 | 0.284x | 11.327x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,069.1 | 1,062.2 | 1,077.9 | 5.5 | 1.000x | 39.850x |

### `orig` / `s-075` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.3 | 35.1 | 1.1 | 0.050x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.3 | 32.4 | 0.0 | 0.050x | 1.002x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 63.9 | 63.8 | 66.1 | 0.9 | 0.099x | 1.979x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 69.4 | 69.1 | 69.8 | 0.2 | 0.108x | 2.149x |
| 5 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 69.4 | 69.2 | 70.6 | 0.6 | 0.108x | 2.149x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 89.2 | 89.2 | 89.6 | 0.1 | 0.139x | 2.763x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 90.7 | 90.6 | 90.9 | 0.1 | 0.141x | 2.810x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 95.8 | 95.6 | 96.0 | 0.1 | 0.149x | 2.967x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 630.8 | 628.7 | 636.4 | 2.8 | 0.983x | 19.542x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 642.0 | 639.3 | 660.4 | 8.0 | 1.000x | 19.889x |

### `orig` / `s-075` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 58.4 | 58.2 | 59.0 | 0.3 | 0.091x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 58.5 | 58.2 | 58.8 | 0.2 | 0.091x | 1.001x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 58.5 | 58.3 | 60.5 | 0.9 | 0.091x | 1.001x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 58.7 | 58.3 | 59.6 | 0.5 | 0.091x | 1.004x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 87.6 | 87.4 | 88.2 | 0.3 | 0.136x | 1.499x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 88.3 | 88.0 | 88.9 | 0.3 | 0.137x | 1.512x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 88.8 | 87.3 | 91.8 | 1.9 | 0.138x | 1.519x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 91.8 | 91.7 | 91.8 | 0.1 | 0.143x | 1.572x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 101.2 | 101.1 | 101.6 | 0.2 | 0.158x | 1.732x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 642.4 | 635.5 | 650.1 | 4.8 | 1.000x | 10.997x |

### `orig` / `s-076` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.2 | 35.7 | 1.3 | 0.050x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.2 | 33.1 | 0.3 | 0.050x | 1.001x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 63.8 | 63.6 | 66.2 | 1.0 | 0.099x | 1.976x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 69.2 | 69.1 | 69.9 | 0.3 | 0.107x | 2.142x |
| 5 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 69.4 | 68.9 | 70.3 | 0.6 | 0.108x | 2.149x |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 89.2 | 89.2 | 89.7 | 0.2 | 0.139x | 2.762x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 90.8 | 90.6 | 92.3 | 0.6 | 0.141x | 2.811x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 95.9 | 95.7 | 96.4 | 0.3 | 0.149x | 2.968x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 628.4 | 625.2 | 633.7 | 3.1 | 0.976x | 19.452x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 643.7 | 637.5 | 656.4 | 7.4 | 1.000x | 19.928x |

### `orig` / `s-076` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 58.3 | 58.3 | 59.4 | 0.4 | 0.091x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 58.3 | 58.2 | 58.4 | 0.1 | 0.091x | 1.000x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 58.4 | 58.3 | 58.7 | 0.1 | 0.092x | 1.002x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 58.5 | 58.3 | 58.8 | 0.2 | 0.092x | 1.003x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 87.5 | 86.9 | 87.8 | 0.3 | 0.137x | 1.500x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 88.0 | 87.3 | 91.5 | 2.0 | 0.138x | 1.509x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 88.5 | 87.3 | 89.2 | 0.6 | 0.139x | 1.517x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 91.8 | 91.6 | 92.2 | 0.2 | 0.144x | 1.574x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 101.3 | 101.0 | 102.2 | 0.4 | 0.159x | 1.736x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 638.6 | 633.1 | 640.8 | 2.7 | 1.000x | 10.945x |

### `orig` / `s-077` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.3 | 32.6 | 0.1 | 0.046x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.3 | 35.1 | 1.1 | 0.046x | 1.000x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 61.9 | 57.6 | 72.9 | 5.1 | 0.087x | 1.914x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 69.1 | 68.9 | 69.2 | 0.1 | 0.098x | 2.137x |
| 5 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 69.2 | 69.1 | 69.5 | 0.1 | 0.098x | 2.141x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 75.2 | 74.9 | 75.6 | 0.2 | 0.106x | 2.324x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 78.8 | 78.8 | 79.2 | 0.1 | 0.111x | 2.438x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 84.2 | 81.6 | 84.9 | 1.2 | 0.119x | 2.605x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 695.2 | 686.0 | 698.0 | 4.3 | 0.981x | 21.497x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 708.4 | 687.8 | 718.8 | 11.7 | 1.000x | 21.905x |

### `orig` / `s-077` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 58.3 | 58.2 | 58.6 | 0.1 | 0.083x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 58.4 | 58.3 | 58.5 | 0.1 | 0.083x | 1.001x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 58.4 | 58.2 | 58.9 | 0.3 | 0.084x | 1.003x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 58.5 | 58.4 | 59.0 | 0.2 | 0.084x | 1.003x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 75.1 | 74.7 | 75.3 | 0.2 | 0.107x | 1.289x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 76.1 | 75.8 | 77.4 | 0.7 | 0.109x | 1.306x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 82.6 | 82.1 | 83.3 | 0.5 | 0.118x | 1.417x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 85.6 | 85.5 | 85.6 | 0.1 | 0.122x | 1.468x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 88.9 | 88.6 | 92.9 | 1.6 | 0.127x | 1.526x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 699.6 | 696.1 | 708.1 | 4.5 | 1.000x | 12.002x |

### `orig` / `s-078` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.4 | 32.3 | 32.7 | 0.1 | 0.044x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.4 | 32.3 | 35.5 | 1.3 | 0.044x | 1.001x |
| 3 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 54.0 | 53.9 | 54.4 | 0.2 | 0.074x | 1.668x |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 54.1 | 54.1 | 56.7 | 1.0 | 0.074x | 1.672x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 55.5 | 54.6 | 55.8 | 0.5 | 0.076x | 1.716x |
| 6 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 69.2 | 68.8 | 69.3 | 0.2 | 0.094x | 2.137x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 69.5 | 69.0 | 69.6 | 0.2 | 0.095x | 2.147x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 74.6 | 74.5 | 74.8 | 0.1 | 0.102x | 2.307x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 718.1 | 714.3 | 723.5 | 3.4 | 0.981x | 22.188x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 732.0 | 715.2 | 754.9 | 13.2 | 1.000x | 22.618x |

### `orig` / `s-078` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 58.4 | 58.2 | 58.5 | 0.1 | 0.081x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 58.5 | 58.4 | 58.8 | 0.2 | 0.081x | 1.002x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 58.5 | 58.3 | 58.8 | 0.2 | 0.081x | 1.002x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 58.5 | 58.4 | 58.6 | 0.1 | 0.081x | 1.002x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 72.7 | 72.2 | 83.2 | 4.3 | 0.101x | 1.246x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 73.6 | 71.7 | 76.3 | 1.6 | 0.102x | 1.261x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 79.6 | 78.5 | 83.7 | 1.8 | 0.110x | 1.364x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 81.9 | 80.1 | 82.1 | 0.7 | 0.114x | 1.404x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 84.4 | 83.1 | 90.1 | 2.8 | 0.117x | 1.446x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 721.2 | 719.4 | 723.4 | 1.3 | 1.000x | 12.357x |

### `orig` / `s-079` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.4 | 32.2 | 35.2 | 1.2 | 0.044x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.4 | 32.3 | 32.4 | 0.1 | 0.044x | 1.000x |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 54.1 | 53.9 | 56.5 | 1.0 | 0.074x | 1.673x |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 54.2 | 54.1 | 55.5 | 0.5 | 0.074x | 1.677x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 55.6 | 54.6 | 55.9 | 0.5 | 0.076x | 1.718x |
| 6 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 69.4 | 69.2 | 69.4 | 0.1 | 0.095x | 2.144x |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 69.4 | 69.1 | 70.9 | 0.7 | 0.095x | 2.145x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 74.6 | 74.6 | 74.8 | 0.1 | 0.102x | 2.305x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 719.9 | 715.7 | 736.5 | 7.3 | 0.985x | 22.253x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 730.8 | 722.2 | 755.5 | 12.2 | 1.000x | 22.589x |

### `orig` / `s-079` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 58.3 | 58.3 | 58.9 | 0.3 | 0.081x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 58.3 | 58.3 | 58.4 | 0.1 | 0.081x | 1.000x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 58.5 | 58.3 | 59.2 | 0.3 | 0.081x | 1.002x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 58.7 | 58.6 | 59.0 | 0.2 | 0.081x | 1.006x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 71.9 | 70.6 | 78.0 | 2.6 | 0.100x | 1.233x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 74.3 | 72.2 | 77.6 | 2.0 | 0.103x | 1.274x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 80.8 | 79.2 | 86.8 | 2.8 | 0.112x | 1.386x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 81.9 | 73.3 | 82.0 | 3.4 | 0.113x | 1.405x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 84.0 | 83.1 | 89.9 | 2.8 | 0.116x | 1.440x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 722.3 | 715.6 | 726.3 | 4.2 | 1.000x | 12.383x |

### `orig` / `s-080` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.2 | 16.0 | 16.3 | 0.1 | 0.045x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.2 | 16.0 | 18.1 | 0.8 | 0.045x | 1.000x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 31.5 | 31.1 | 32.4 | 0.5 | 0.088x | 1.951x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.5 | 31.4 | 32.3 | 0.4 | 0.088x | 1.952x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 46.8 | 44.4 | 49.3 | 1.8 | 0.131x | 2.897x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 54.1 | 52.8 | 92.4 | 15.4 | 0.151x | 3.347x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 63.4 | 63.2 | 63.8 | 0.2 | 0.177x | 3.926x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 64.2 | 63.4 | 65.7 | 0.8 | 0.179x | 3.972x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 349.2 | 344.5 | 356.1 | 3.7 | 0.974x | 21.615x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 358.5 | 352.0 | 364.7 | 4.1 | 1.000x | 22.189x |

### `orig` / `s-080` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 26.1 | 25.9 | 26.8 | 0.3 | 0.020x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 26.2 | 26.1 | 26.6 | 0.2 | 0.021x | 1.004x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 26.4 | 26.1 | 26.6 | 0.2 | 0.021x | 1.012x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 26.5 | 26.2 | 28.3 | 0.8 | 0.021x | 1.013x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 71.2 | 70.0 | 79.5 | 3.7 | 0.056x | 2.726x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 380.5 | 378.9 | 384.7 | 2.4 | 0.298x | 14.567x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 381.2 | 380.2 | 381.6 | 0.5 | 0.298x | 14.591x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 383.2 | 377.3 | 386.5 | 3.1 | 0.300x | 14.667x |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 388.5 | 381.0 | 389.3 | 3.1 | 0.304x | 14.871x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,277.1 | 1,270.1 | 1,292.6 | 8.3 | 1.000x | 48.888x |

### `orig` / `s-081` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9.9 | 9.9 | 9.9 | 0.0 | 0.339x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 9.9 | 10.0 | 0.0 | 0.341x | 1.006x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.9 | 10.9 | 11.0 | 0.0 | 0.374x | 1.104x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 11.0 | 10.9 | 11.2 | 0.1 | 0.378x | 1.115x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 13.6 | 13.6 | 13.7 | 0.0 | 0.465x | 1.374x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 15.1 | 13.8 | 15.8 | 0.7 | 0.515x | 1.521x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 15.6 | 15.6 | 17.2 | 0.7 | 0.533x | 1.573x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 15.6 | 15.6 | 18.3 | 1.1 | 0.535x | 1.578x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.0 | 29.0 | 29.3 | 0.1 | 0.992x | 2.931x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.2 | 29.2 | 29.4 | 0.1 | 1.000x | 2.953x |

### `orig` / `s-081` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 5.9 | 5.9 | 6.9 | 0.4 | 0.196x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 5.9 | 5.9 | 6.2 | 0.1 | 0.196x | 1.002x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 6.1 | 5.6 | 6.8 | 0.5 | 0.201x | 1.027x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 6.2 | 5.6 | 6.7 | 0.4 | 0.207x | 1.055x |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 15.0 | 14.9 | 17.9 | 1.2 | 0.497x | 2.537x |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 15.7 | 15.5 | 16.7 | 0.5 | 0.519x | 2.649x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 17.2 | 17.1 | 17.6 | 0.2 | 0.571x | 2.910x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 17.3 | 17.3 | 17.5 | 0.1 | 0.575x | 2.935x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.1 | 30.1 | 31.3 | 0.5 | 1.000x | 5.101x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 37.1 | 36.1 | 46.5 | 4.7 | 1.233x | 6.287x |

### `orig` / `s-082` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.4 | 10.5 | 0.0 | 0.354x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.3 | 10.6 | 0.1 | 0.355x | 1.003x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.8 | 12.5 | 13.9 | 0.5 | 0.436x | 1.231x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.8 | 12.4 | 13.6 | 0.4 | 0.437x | 1.234x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 14.9 | 14.8 | 15.7 | 0.3 | 0.506x | 1.430x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 15.3 | 14.9 | 16.5 | 0.6 | 0.522x | 1.475x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 16.4 | 16.4 | 17.2 | 0.3 | 0.558x | 1.576x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 16.4 | 16.4 | 16.5 | 0.0 | 0.559x | 1.580x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.3 | 28.9 | 31.5 | 0.9 | 1.000x | 2.824x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.4 | 28.9 | 29.9 | 0.3 | 1.000x | 2.825x |

### `orig` / `s-082` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 5.9 | 5.9 | 6.5 | 0.2 | 0.191x | 1.000x |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 6.4 | 6.3 | 6.6 | 0.1 | 0.205x | 1.077x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 6.4 | 6.2 | 6.9 | 0.3 | 0.207x | 1.087x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 6.5 | 6.1 | 6.5 | 0.1 | 0.209x | 1.097x |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 23.3 | 23.3 | 25.1 | 0.7 | 0.752x | 3.944x |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 23.5 | 23.4 | 27.7 | 1.6 | 0.758x | 3.972x |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 24.2 | 24.1 | 24.3 | 0.0 | 0.778x | 4.080x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 24.6 | 24.5 | 24.7 | 0.1 | 0.792x | 4.154x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 31.0 | 31.0 | 33.0 | 0.8 | 1.000x | 5.244x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 39.1 | 36.0 | 45.9 | 3.8 | 1.259x | 6.604x |

### `orig` / `s-083` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.0 | 11.9 | 12.0 | 0.1 | 0.326x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.0 | 11.9 | 12.1 | 0.1 | 0.326x | 1.000x |
| 3 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 21.0 | 21.0 | 21.8 | 0.3 | 0.569x | 1.747x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 21.1 | 21.1 | 21.7 | 0.2 | 0.573x | 1.760x |
| 5 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.6 | 21.8 | 0.1 | 0.585x | 1.797x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.5 | 31.0 | 3.8 | 0.586x | 1.798x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 35.3 | 34.5 | 35.4 | 0.4 | 0.956x | 2.935x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 36.9 | 34.8 | 38.8 | 1.5 | 1.000x | 3.069x |
| 9 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 81.1 | 80.9 | 81.6 | 0.3 | 2.198x | 6.748x |
| 10 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 81.4 | 80.4 | 83.2 | 0.9 | 2.208x | 6.777x |

### `orig` / `s-083` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 36.4 | 35.5 | 38.7 | 1.2 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 40.6 | 37.6 | 48.2 | 4.3 | 1.114x | 1.114x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 73.1 | 73.0 | 73.6 | 0.2 | 2.008x | 2.008x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 73.7 | 73.2 | 75.7 | 0.9 | 2.024x | 2.024x |
| 5 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 73.8 | 72.9 | 74.0 | 0.4 | 2.026x | 2.026x |
| 6 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 74.1 | 73.3 | 75.4 | 0.8 | 2.035x | 2.035x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 613.1 | 612.2 | 614.5 | 0.7 | 16.845x | 16.845x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 617.9 | 616.6 | 626.4 | 3.6 | 16.976x | 16.976x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 619.4 | 613.3 | 625.8 | 4.0 | 17.017x | 17.017x |
| 10 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 620.4 | 614.1 | 621.8 | 3.0 | 17.046x | 17.046x |

### `orig` / `s-084` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19.2 | 19.1 | 19.2 | 0.0 | 0.556x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 19.2 | 19.1 | 19.3 | 0.1 | 0.556x | 1.000x |
| 3 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 21.0 | 20.6 | 21.1 | 0.2 | 0.609x | 1.095x |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 21.1 | 20.7 | 21.1 | 0.2 | 0.610x | 1.099x |
| 5 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.7 | 21.6 | 23.4 | 0.7 | 0.629x | 1.132x |
| 6 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 22.1 | 21.9 | 22.5 | 0.2 | 0.640x | 1.152x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 23.0 | 22.9 | 23.0 | 0.1 | 0.665x | 1.198x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 22.9 | 23.1 | 0.1 | 0.668x | 1.202x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 34.5 | 34.2 | 39.2 | 1.9 | 1.000x | 1.800x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 34.6 | 33.7 | 36.6 | 1.0 | 1.003x | 1.805x |

### `orig` / `s-084` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 16.2 | 16.1 | 16.5 | 0.1 | 0.453x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 16.3 | 16.2 | 17.1 | 0.3 | 0.457x | 1.007x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 16.6 | 16.2 | 17.0 | 0.3 | 0.463x | 1.021x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 16.8 | 16.2 | 17.1 | 0.4 | 0.468x | 1.033x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 35.8 | 34.8 | 38.9 | 1.5 | 1.000x | 2.205x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.0 | 36.4 | 47.5 | 4.1 | 1.230x | 2.712x |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 123.1 | 122.1 | 124.4 | 0.8 | 3.438x | 7.582x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 123.2 | 122.3 | 126.5 | 1.6 | 3.442x | 7.590x |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 125.1 | 124.4 | 125.2 | 0.3 | 3.493x | 7.704x |
| 10 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 127.7 | 127.1 | 128.6 | 0.5 | 3.568x | 7.868x |

### `orig` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 3,579,415.8 | 3,575,433.9 | 3,603,762.4 | 10,110.6 | 0.124x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 3,582,024.1 | 3,576,296.9 | 3,583,027.0 | 2,770.2 | 0.124x | 1.001x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 3,583,346.1 | 3,580,016.1 | 3,584,412.4 | 1,815.2 | 0.124x | 1.001x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 3,584,658.7 | 3,575,104.0 | 3,586,034.6 | 4,028.9 | 0.124x | 1.001x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,704,618.8 | 3,661,060.9 | 3,783,190.6 | 39,920.9 | 0.128x | 1.035x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 4,952,397.5 | 4,938,169.8 | 5,070,578.0 | 48,902.7 | 0.171x | 1.384x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 5,187,813.0 | 5,167,982.8 | 5,283,798.5 | 42,018.8 | 0.179x | 1.449x |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 5,260,892.7 | 5,234,222.7 | 5,316,530.0 | 27,527.4 | 0.182x | 1.470x |
| 9 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 5,531,008.3 | 5,527,525.0 | 5,571,145.3 | 19,605.8 | 0.191x | 1.545x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28,917,610.5 | 28,669,211.7 | 29,395,213.2 | 253,760.3 | 1.000x | 8.079x |

### `orig` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 18,007.3 | 17,872.8 | 18,095.0 | 71.1 | 1.000x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 1,888,829.9 | 1,881,203.5 | 1,893,663.5 | 5,030.3 | 104.892x | 104.892x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 1,890,919.6 | 1,887,987.1 | 1,893,149.0 | 1,883.1 | 105.008x | 105.008x |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 1,892,116.2 | 1,889,408.5 | 1,911,218.1 | 7,959.1 | 105.075x | 105.075x |
| 5 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 1,895,118.8 | 1,894,398.2 | 1,897,418.8 | 1,068.3 | 105.242x | 105.242x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,542,172.6 | 2,525,185.0 | 2,595,716.1 | 24,530.3 | 141.174x | 141.174x |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 15,993,661.2 | 15,950,363.5 | 16,052,184.2 | 35,301.5 | 888.175x | 888.175x |
| 8 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 16,028,449.2 | 15,949,076.5 | 16,407,209.0 | 167,845.6 | 890.107x | 890.107x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 16,031,857.0 | 15,975,010.0 | 16,403,539.3 | 157,668.1 | 890.296x | 890.296x |
| 10 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 16,134,132.3 | 15,975,058.3 | 16,277,283.3 | 97,434.9 | 895.976x | 895.976x |

### `orig` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,981.2 | 17,863.9 | 18,019.2 | 55.1 | 1.000x | 1.000x | 5 | 100% |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 1,876,578.1 | 1,874,686.4 | 1,878,387.5 | 1,353.4 | 104.364x | 104.364x | 5 | 100% |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 1,877,410.1 | 1,875,670.2 | 1,882,685.2 | 2,496.4 | 104.410x | 104.410x | 5 | 100% |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 1,878,493.8 | 1,876,461.9 | 1,898,502.1 | 9,216.3 | 104.470x | 104.470x | 5 | 100% |
| 5 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 1,878,612.2 | 1,877,528.1 | 1,885,089.9 | 2,736.3 | 104.477x | 104.477x | 5 | 100% |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,820,397.6 | 2,817,704.5 | 2,887,324.3 | 26,355.5 | 156.853x | 156.853x | 5 | 100% |

### `orig` / `t-d-prose-sparse-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 3,133,275.5 | 3,115,636.0 | 3,185,429.9 | 24,613.2 | 0.033x | 1.000x |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 3,138,982.6 | 3,117,745.4 | 3,172,171.6 | 18,815.0 | 0.033x | 1.002x |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 3,140,389.6 | 3,132,141.9 | 3,241,542.6 | 41,012.8 | 0.033x | 1.002x |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 3,145,599.7 | 3,130,582.1 | 3,161,450.4 | 11,299.7 | 0.033x | 1.004x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 5,968,396.9 | 5,959,626.2 | 6,594,772.5 | 250,553.1 | 0.063x | 1.905x |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 16,858,436.8 | 16,493,784.5 | 17,140,340.8 | 217,073.2 | 0.178x | 5.380x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 16,947,207.0 | 16,690,895.8 | 17,749,694.2 | 397,480.3 | 0.179x | 5.409x |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 17,161,655.0 | 16,634,872.0 | 17,755,071.7 | 364,477.7 | 0.181x | 5.477x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 17,464,392.7 | 16,765,368.3 | 17,496,556.0 | 309,307.2 | 0.184x | 5.574x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 94,897,024.5 | 94,050,245.2 | 96,424,265.8 | 868,092.4 | 1.000x | 30.287x |

### `orig` / `t-e-prose-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 18,063.1 | 17,931.0 | 18,163.9 | 96.5 | 1.000x | 1.000x |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 3,091,404.0 | 3,083,561.6 | 3,117,264.8 | 12,389.9 | 171.145x | 171.145x |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 3,094,151.3 | 3,070,672.4 | 3,105,844.5 | 12,122.6 | 171.297x | 171.297x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 3,106,092.4 | 3,082,235.2 | 3,130,096.1 | 15,514.6 | 171.958x | 171.958x |
| 5 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 3,113,753.6 | 3,071,198.1 | 3,125,737.8 | 22,466.6 | 172.382x | 172.382x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,157,766.2 | 3,155,562.4 | 3,279,750.2 | 48,963.7 | 174.819x | 174.819x |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 16,600,912.8 | 16,570,925.0 | 17,639,683.8 | 411,577.1 | 919.053x | 919.053x |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 16,604,260.0 | 16,567,004.8 | 16,641,547.8 | 24,321.2 | 919.238x | 919.238x |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 16,634,137.3 | 16,582,910.3 | 17,345,205.3 | 293,538.4 | 920.892x | 920.892x |
| 10 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 16,765,799.3 | 16,641,588.7 | 17,768,221.7 | 417,136.8 | 928.181x | 928.181x |

## Excluded from ranking (expectation-failing cells)

| pattern | subject | regime | form | testee | n | pass-rate | gave-up | wrong | outcomes |
|---|---|---|---|---|---|---|---|---|---|
| `factored` | `s-058` | `match-compliance` | `whole-subject` | `pcrec_35e1ab1_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-058` | `match-compliance` | `whole-subject` | `pcrec_36d5963_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-059` | `match-compliance` | `whole-subject` | `pcrec_35e1ab1_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-059` | `match-compliance` | `whole-subject` | `pcrec_36d5963_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-061` | `match-compliance` | `whole-subject` | `pcrec_35e1ab1_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-061` | `match-compliance` | `whole-subject` | `pcrec_36d5963_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-063` | `match-compliance` | `whole-subject` | `pcrec_35e1ab1_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-063` | `match-compliance` | `whole-subject` | `pcrec_36d5963_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-064` | `match-compliance` | `whole-subject` | `pcrec_35e1ab1_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-064` | `match-compliance` | `whole-subject` | `pcrec_36d5963_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 5 | 0% | 0 | 0 | timed-out=5 |
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_35e1ab1_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_35e1ab1_vm-in-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_36d5963_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_36d5963_vm-in-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `orig` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_35e1ab1_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `orig` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_35e1ab1_vm-in-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `orig` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_36d5963_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `orig` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_36d5963_vm-in-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |

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
- `pcrec_36d5963_auto-caps-simdna` / `factored` / `plain`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_36d5963_auto-caps-simdna` / `factored` / `whole-subject`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_36d5963_auto-caps-simdna` / `floor` / `plain`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_36d5963_auto-caps-simdna` / `floor` / `whole-subject`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_36d5963_auto-caps-simdna` / `orig` / `plain`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_36d5963_auto-caps-simdna` / `orig` / `whole-subject`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_36d5963_auto-nocaps-simdna` / `factored` / `plain`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_36d5963_auto-nocaps-simdna` / `factored` / `whole-subject`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_36d5963_auto-nocaps-simdna` / `floor` / `plain`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_36d5963_auto-nocaps-simdna` / `floor` / `whole-subject`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_36d5963_auto-nocaps-simdna` / `orig` / `plain`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_36d5963_auto-nocaps-simdna` / `orig` / `whole-subject`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_36d5963_vm-caps-simdna` / `factored` / `plain`: engine=vm, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_36d5963_vm-caps-simdna` / `factored` / `whole-subject`: engine=vm, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_36d5963_vm-caps-simdna` / `floor` / `plain`: engine=vm, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_36d5963_vm-caps-simdna` / `floor` / `whole-subject`: engine=vm, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_36d5963_vm-caps-simdna` / `orig` / `plain`: engine=vm, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_36d5963_vm-caps-simdna` / `orig` / `whole-subject`: engine=vm, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_36d5963_vm-in-caps-simdna` / `factored` / `plain`: engine=vm, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_36d5963_vm-in-caps-simdna` / `factored` / `whole-subject`: engine=vm, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_36d5963_vm-in-caps-simdna` / `floor` / `plain`: engine=vm, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_36d5963_vm-in-caps-simdna` / `floor` / `whole-subject`: engine=vm, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_36d5963_vm-in-caps-simdna` / `orig` / `plain`: engine=vm, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_36d5963_vm-in-caps-simdna` / `orig` / `whole-subject`: engine=vm, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
    - K = pcrec's `RX_UNROLL_K`/`_WHY`: the VM counter rung's unroll factor and who chose it (default / option / denied / size-model / size-model-declined / cap-rescue / capacity-declined -- limits.md 8); caps = the EFFECTIVE `RX_MAX_EMIT_CODE_BYTES`/`RX_MAX_EMIT_BYTES` the artifact was built under (raise-only; 500,000/1,000,000 by default). VM artifacts only: a DFA artifact has no counter rung and stamps no code cap.

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
| `factored` | `plain` | `pcrec_36d5963_auto-caps-simdna` | 163,173,581.0 | 148,043,728.0 | 165,355,524.0 | 6,230,940.4 | 5 | 43,000 | 0.038 | compiled=5 | 9,712,969.0 | 151,485,660.0 | 186,221.0 |
| `factored` | `whole-subject` | `pcrec_36d5963_auto-caps-simdna` | 172,018,683.0 | 169,330,388.0 | 187,531,128.0 | 6,850,899.9 | 5 | 47,240 | 0.040 (max is trial 1) | compiled=5 | 11,935,272.0 | 160,085,781.0 | 190,281.0 |
| `factored` | `plain` | `pcrec_36d5963_auto-nocaps-simdna` | 158,379,641.0 | 144,622,938.0 | 160,943,538.0 | 6,230,002.9 | 5 | 43,000 | 0.039 (max is trial 1) | compiled=5 | 9,574,438.0 | 140,183,871.0 | 190,981.0 |
| `factored` | `whole-subject` | `pcrec_36d5963_auto-nocaps-simdna` | 163,254,961.0 | 156,661,801.0 | 182,598,618.0 | 9,464,812.7 | 5 | 47,240 | 0.058 (max is trial 1) | compiled=5 | 11,943,713.0 | 151,211,278.0 | 192,071.0 |
| `factored` | `plain` | `pcrec_36d5963_vm-caps-simdna` | 567,703,383.0 | 559,754,886.0 | 571,675,245.0 | 4,062,965.4 | 5 | 34,816 | 0.007 | compiled=5 | 2,253,513.0 | 564,927,396.0 | 125,381.0 |
| `factored` | `whole-subject` | `pcrec_36d5963_vm-caps-simdna` | 559,242,744.0 | 556,895,190.0 | 570,217,336.0 | 4,711,477.0 | 5 | 34,816 | 0.008 | compiled=5 | 2,213,983.0 | 556,877,430.0 | 212,661.0 |
| `factored` | `plain` | `pcrec_36d5963_vm-in-caps-simdna` | 555,700,975.0 | 548,732,151.0 | 561,291,690.0 | 5,165,541.3 | 5 | 34,816 | 0.009 | compiled=5 | 2,286,274.0 | 553,427,801.0 | 190,972.0 |
| `factored` | `whole-subject` | `pcrec_36d5963_vm-in-caps-simdna` | 551,792,261.0 | 547,407,994.0 | 564,315,969.0 | 6,285,963.3 | 5 | 34,816 | 0.011 | compiled=5 | 2,263,684.0 | 548,875,712.0 | 118,861.0 |
| `floor` | `plain` | `pcrec_35e1ab1_auto-caps-simdna` | 128,124,003.0 | 121,815,237.0 | 132,250,058.0 | 3,741,734.5 | 5 | 17,816 | 0.029 | compiled=5 | 1,563,309.0 | 126,608,855.0 | 112,481.0 |
| `floor` | `whole-subject` | `pcrec_35e1ab1_auto-caps-simdna` | 136,601,994.0 | 125,250,527.0 | 138,196,622.0 | 6,006,842.3 | 5 | 17,904 | 0.044 (max is trial 1) | compiled=5 | 1,463,518.0 | 134,997,154.0 | 200,402.0 |
| `floor` | `plain` | `pcrec_35e1ab1_auto-nocaps-simdna` | 125,053,645.0 | 118,093,685.0 | 130,520,689.0 | 4,812,299.8 | 5 | 17,816 | 0.038 (max is trial 1) | compiled=5 | 1,404,458.0 | 123,415,805.0 | 99,061.0 |
| `floor` | `whole-subject` | `pcrec_35e1ab1_auto-nocaps-simdna` | 135,198,375.0 | 124,770,805.0 | 136,922,336.0 | 4,667,899.5 | 5 | 17,904 | 0.035 | compiled=5 | 1,432,719.0 | 132,068,647.0 | 199,521.0 |
| `floor` | `plain` | `pcrec_35e1ab1_vm-caps-simdna` | 143,839,405.0 | 133,489,685.0 | 145,996,357.0 | 4,499,436.2 | 5 | 17,600 | 0.031 | compiled=5 | 1,470,958.0 | 142,085,106.0 | 104,780.0 |
| `floor` | `whole-subject` | `pcrec_35e1ab1_vm-caps-simdna` | 131,485,234.0 | 130,493,468.0 | 152,939,310.0 | 9,269,487.4 | 5 | 17,600 | 0.070 | compiled=5 | 1,303,697.0 | 130,010,745.0 | 190,152.0 |
| `floor` | `plain` | `pcrec_35e1ab1_vm-in-caps-simdna` | 143,130,173.0 | 127,595,569.0 | 148,446,484.0 | 7,271,673.7 | 5 | 17,600 | 0.051 (max is trial 1) | compiled=5 | 1,367,788.0 | 141,680,644.0 | 107,271.0 |
| `floor` | `whole-subject` | `pcrec_35e1ab1_vm-in-caps-simdna` | 136,645,873.0 | 127,325,307.0 | 145,517,016.0 | 6,966,108.5 | 5 | 17,600 | 0.051 | compiled=5 | 1,317,248.0 | 135,247,565.0 | 93,341.0 |
| `floor` | `plain` | `pcrec_36d5963_auto-caps-simdna` | 137,975,417.0 | 130,154,820.0 | 142,913,866.0 | 4,140,189.2 | 5 | 22,488 | 0.030 | compiled=5 | 3,055,408.0 | 135,445,562.0 | 190,461.0 |
| `floor` | `whole-subject` | `pcrec_36d5963_auto-caps-simdna` | 144,611,468.0 | 133,599,301.0 | 149,537,718.0 | 6,141,196.3 | 5 | 22,632 | 0.042 | compiled=5 | 1,661,280.0 | 142,664,806.0 | 196,431.0 |
| `floor` | `plain` | `pcrec_36d5963_auto-nocaps-simdna` | 137,161,193.0 | 131,844,181.0 | 140,083,190.0 | 2,832,113.2 | 5 | 22,488 | 0.021 (max is trial 1) | compiled=5 | 1,624,910.0 | 133,667,721.0 | 187,942.0 |
| `floor` | `whole-subject` | `pcrec_36d5963_auto-nocaps-simdna` | 146,188,127.0 | 137,551,574.0 | 148,622,902.0 | 3,782,109.1 | 5 | 22,632 | 0.026 | compiled=5 | 1,755,770.0 | 142,880,468.0 | 105,240.0 |
| `floor` | `plain` | `pcrec_36d5963_vm-caps-simdna` | 149,341,986.0 | 137,028,735.0 | 150,343,371.0 | 4,944,844.8 | 5 | 22,120 | 0.033 | compiled=5 | 1,696,930.0 | 147,530,796.0 | 176,811.0 |
| `floor` | `whole-subject` | `pcrec_36d5963_vm-caps-simdna` | 146,819,080.0 | 139,205,948.0 | 153,194,038.0 | 4,814,096.7 | 5 | 22,120 | 0.033 | compiled=5 | 1,431,778.0 | 145,203,761.0 | 187,691.0 |
| `floor` | `plain` | `pcrec_36d5963_vm-in-caps-simdna` | 143,224,196.0 | 133,623,356.0 | 149,166,282.0 | 5,314,418.2 | 5 | 22,120 | 0.037 | compiled=5 | 1,870,712.0 | 141,694,146.0 | 108,651.0 |
| `floor` | `whole-subject` | `pcrec_36d5963_vm-in-caps-simdna` | 139,422,771.0 | 137,041,307.0 | 155,827,535.0 | 7,167,340.5 | 5 | 22,120 | 0.051 | compiled=5 | 2,750,817.0 | 137,806,721.0 | 199,131.0 |
| `orig` | `plain` | `pcrec_35e1ab1_auto-caps-simdna` | 143,041,582.0 | 133,638,077.0 | 152,605,977.0 | 7,423,117.4 | 5 | 38,288 | 0.052 | compiled=5 | 8,399,070.0 | 133,049,073.0 | 97,811.0 |
| `orig` | `whole-subject` | `pcrec_35e1ab1_auto-caps-simdna` | 161,003,156.0 | 144,668,771.0 | 174,001,693.0 | 9,821,090.4 | 5 | 38,376 | 0.061 | compiled=5 | 18,044,156.0 | 141,891,755.0 | 186,281.0 |
| `orig` | `plain` | `pcrec_35e1ab1_auto-nocaps-simdna` | 148,731,375.0 | 133,116,513.0 | 154,306,767.0 | 7,366,531.2 | 5 | 38,288 | 0.050 | compiled=5 | 8,303,388.0 | 134,495,101.0 | 190,511.0 |
| `orig` | `whole-subject` | `pcrec_35e1ab1_auto-nocaps-simdna` | 148,766,935.0 | 141,953,955.0 | 157,360,185.0 | 5,601,770.9 | 5 | 38,376 | 0.038 (max is trial 1) | compiled=5 | 10,395,781.0 | 138,189,823.0 | 191,472.0 |
| `orig` | `plain` | `pcrec_35e1ab1_vm-caps-simdna` | 425,700,355.0 | 418,138,020.0 | 433,200,719.0 | 5,739,473.7 | 5 | 26,112 | 0.013 | compiled=5 | 3,573,812.0 | 423,604,592.0 | 98,321.0 |
| `orig` | `whole-subject` | `pcrec_35e1ab1_vm-caps-simdna` | 418,219,710.0 | 416,284,479.0 | 424,829,349.0 | 3,247,138.2 | 5 | 26,112 | 0.008 | compiled=5 | 1,887,041.0 | 416,182,378.0 | 101,761.0 |
| `orig` | `plain` | `pcrec_35e1ab1_vm-in-caps-simdna` | 426,965,172.0 | 417,563,868.0 | 436,633,782.0 | 6,421,511.5 | 5 | 26,112 | 0.015 | compiled=5 | 3,456,131.0 | 422,794,938.0 | 94,571.0 |
| `orig` | `whole-subject` | `pcrec_35e1ab1_vm-in-caps-simdna` | 416,505,570.0 | 410,439,183.0 | 436,855,013.0 | 9,723,201.5 | 5 | 26,112 | 0.023 (max is trial 1) | compiled=5 | 3,768,522.0 | 414,571,809.0 | 91,591.0 |
| `orig` | `plain` | `pcrec_36d5963_auto-caps-simdna` | 160,234,903.0 | 142,502,585.0 | 170,930,038.0 | 9,452,596.4 | 5 | 42,960 | 0.059 (max is trial 1) | compiled=5 | 9,209,996.0 | 144,087,044.0 | 215,871.0 |
| `orig` | `whole-subject` | `pcrec_36d5963_auto-caps-simdna` | 166,290,610.0 | 163,930,325.0 | 182,586,678.0 | 6,746,131.3 | 5 | 47,200 | 0.041 | compiled=5 | 11,352,189.0 | 154,132,576.0 | 207,132.0 |
| `orig` | `plain` | `pcrec_36d5963_auto-nocaps-simdna` | 152,456,135.0 | 144,069,245.0 | 174,208,458.0 | 10,143,322.1 | 5 | 42,960 | 0.067 | compiled=5 | 9,225,456.0 | 143,266,640.0 | 102,641.0 |
| `orig` | `whole-subject` | `pcrec_36d5963_auto-nocaps-simdna` | 163,517,013.0 | 155,667,265.0 | 165,485,665.0 | 4,206,358.8 | 5 | 47,200 | 0.026 | compiled=5 | 11,363,629.0 | 151,287,019.0 | 199,952.0 |
| `orig` | `plain` | `pcrec_36d5963_vm-caps-simdna` | 429,171,779.0 | 423,947,059.0 | 447,217,713.0 | 8,229,989.8 | 5 | 30,632 | 0.019 (max is trial 1) | compiled=5 | 1,931,061.0 | 427,170,727.0 | 194,501.0 |
| `orig` | `whole-subject` | `pcrec_36d5963_vm-caps-simdna` | 435,901,317.0 | 424,067,939.0 | 452,243,691.0 | 11,235,002.5 | 5 | 30,632 | 0.026 | compiled=5 | 2,212,242.0 | 431,366,691.0 | 196,301.0 |
| `orig` | `plain` | `pcrec_36d5963_vm-in-caps-simdna` | 430,350,492.0 | 428,462,499.0 | 435,167,061.0 | 2,401,459.0 | 5 | 30,632 | 0.006 (max is trial 1) | compiled=5 | 2,006,842.0 | 428,298,358.0 | 184,621.0 |
| `orig` | `whole-subject` | `pcrec_36d5963_vm-in-caps-simdna` | 429,422,065.0 | 424,291,654.0 | 437,092,543.0 | 4,553,396.7 | 5 | 30,632 | 0.011 | compiled=5 | 4,000,955.0 | 425,227,189.0 | 186,951.0 |

### `eager-jit`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 79,241.0 | 65,550.0 | 161,422.0 | 35,427.1 | 5 | 951 | 0.447 (max is trial 1) | compiled=5 |
| `floor` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 6,180.0 | 4,820.0 | 57,130.0 | 20,468.0 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `orig` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 148,601.0 | 139,231.0 | 367,712.0 | 87,829.9 | 5 | 1,609 | 0.591 (max is trial 1) | compiled=5 |

### `interpretive`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 14,540.0 | 13,051.0 | 45,860.0 | 12,622.0 | 5 | 951 | timer-floor (max is trial 1) | compiled=5 |
| `floor` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 360.0 | 310.0 | 15,270.0 | 5,961.3 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `orig` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 13,430.0 | 12,301.0 | 43,590.0 | 12,093.7 | 5 | 1,609 | timer-floor (max is trial 1) | compiled=5 |

