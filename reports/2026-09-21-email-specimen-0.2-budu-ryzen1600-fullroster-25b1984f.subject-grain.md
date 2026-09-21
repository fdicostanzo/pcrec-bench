# pcrec-bench report

reporter: v18 (2026-09-18)

## Query

- filters: subbench=email-specimen, version=0.2, testee=libpcre2_10.46_interp-caps-simdna, testee=libpcre2_10.46_jit-caps-simdna, testee=pcrec_25b1984f_auto-caps-simdna, testee=pcrec_25b1984f_auto-nocaps-simdna, testee=pcrec_25b1984f_vm-caps-simdna, testee=pcrec_25b1984f_vm-in-caps-simdna, testee=rust_1.13.1_default-caps-simdna
- record source: store/index.tsv (14 record(s) matching this query)
- records included: 7
- worst other-core busy: 10.81% (`rust_1.13.1_default-caps-simdna` / `orig` / `large-subject-throughput`)
    - `email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260902T075326Z` (store/records/email-specimen@0.2/libpcre2_10.46_interp-caps-simdna/email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260902T075326Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260902T080213Z` (store/records/email-specimen@0.2/libpcre2_10.46_jit-caps-simdna/email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260902T080213Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 500 rows; 1 unjudged (1 all-timed-out); k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_25b1984f_auto-caps-simdna__budu-ryzen1600__20260921T065926Z` (store/records/email-specimen@0.2/pcrec_25b1984f_auto-caps-simdna/email-specimen@0.2__pcrec_25b1984f_auto-caps-simdna__budu-ryzen1600__20260921T065926Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_25b1984f_auto-nocaps-simdna__budu-ryzen1600__20260921T070439Z` (store/records/email-specimen@0.2/pcrec_25b1984f_auto-nocaps-simdna/email-specimen@0.2__pcrec_25b1984f_auto-nocaps-simdna__budu-ryzen1600__20260921T070439Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_25b1984f_vm-caps-simdna__budu-ryzen1600__20260921T070947Z` (store/records/email-specimen@0.2/pcrec_25b1984f_vm-caps-simdna/email-specimen@0.2__pcrec_25b1984f_vm-caps-simdna__budu-ryzen1600__20260921T070947Z.jsonl) — agreement: agree (0 of 8 groups; 0 of 490 rows; 11 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_25b1984f_vm-in-caps-simdna__budu-ryzen1600__20260921T071628Z` (store/records/email-specimen@0.2/pcrec_25b1984f_vm-in-caps-simdna/email-specimen@0.2__pcrec_25b1984f_vm-in-caps-simdna__budu-ryzen1600__20260921T071628Z.jsonl) — agreement: agree (0 of 8 groups; 0 of 495 rows; 6 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__rust_1.13.1_default-caps-simdna__budu-ryzen1600__20260920T164034Z` (store/records/email-specimen@0.2/rust_1.13.1_default-caps-simdna/email-specimen@0.2__rust_1.13.1_default-caps-simdna__budu-ryzen1600__20260920T164034Z.jsonl) — agreement: agree (0 of 6 groups; 0 of 334 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
- superseded: 7 record(s) (OD-B15; --all-records lists them)
- sub-bench version(s): email-specimen@0.2
- machine(s): budu-ryzen1600
- schema version(s): 1.4, 1.6
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
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.4 | 32.3 | 32.6 | 0.1 | 0.037x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.7 | 34.5 | 34.8 | 0.1 | 0.040x | 1.071x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 147.7 | 146.6 | 161.0 | 5.5 | 0.169x | 4.555x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 149.4 | 149.1 | 154.8 | 2.2 | 0.171x | 4.608x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 863.9 | 857.9 | 884.2 | 9.0 | 0.991x | 26.640x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 871.6 | 865.8 | 882.8 | 6.0 | 1.000x | 26.879x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-000` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 58.5 | 58.5 | 58.7 | 0.1 | 0.068x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 62.8 | 62.7 | 63.1 | 0.1 | 0.073x | 1.073x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 143.4 | 142.8 | 143.9 | 0.4 | 0.166x | 2.450x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 144.6 | 144.4 | 145.1 | 0.3 | 0.167x | 2.470x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 154.1 | 153.9 | 154.6 | 0.3 | 0.178x | 2.634x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 863.8 | 854.6 | 872.1 | 6.6 | 1.000x | 14.759x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-001` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 39.8 | 39.7 | 39.9 | 0.0 | 0.033x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 42.9 | 42.8 | 43.0 | 0.1 | 0.035x | 1.076x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 195.5 | 194.3 | 206.8 | 4.7 | 0.160x | 4.908x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 212.1 | 210.9 | 214.2 | 1.1 | 0.174x | 5.326x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,217.2 | 1,214.6 | 1,229.8 | 5.5 | 0.997x | 30.568x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,220.7 | 1,210.7 | 1,258.3 | 17.5 | 1.000x | 30.655x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-001` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 78.3 | 77.9 | 78.4 | 0.2 | 0.064x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 80.4 | 80.4 | 81.0 | 0.3 | 0.066x | 1.028x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 175.4 | 175.0 | 176.0 | 0.3 | 0.144x | 2.240x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 202.3 | 200.3 | 202.7 | 0.9 | 0.166x | 2.584x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 208.3 | 207.7 | 208.9 | 0.4 | 0.171x | 2.661x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,219.9 | 1,219.7 | 1,231.7 | 5.8 | 1.000x | 15.584x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-002` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 18.1 | 18.1 | 18.2 | 0.1 | 0.024x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.5 | 20.3 | 20.6 | 0.1 | 0.027x | 1.132x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 102.1 | 101.9 | 102.5 | 0.2 | 0.136x | 5.628x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 103.1 | 101.3 | 111.0 | 4.3 | 0.138x | 5.686x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 747.6 | 744.6 | 764.3 | 7.0 | 1.000x | 41.231x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 752.1 | 743.8 | 753.1 | 3.9 | 1.006x | 41.478x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-002` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 26.0 | 25.8 | 27.2 | 0.5 | 0.035x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.1 | 0.2 | 0.038x | 1.105x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 95.8 | 95.6 | 96.5 | 0.3 | 0.127x | 3.689x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 97.5 | 96.3 | 98.3 | 0.7 | 0.130x | 3.755x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 123.3 | 121.4 | 124.5 | 1.2 | 0.164x | 4.746x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 752.1 | 747.7 | 765.2 | 5.9 | 1.000x | 28.959x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-003` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 43.2 | 43.0 | 43.2 | 0.1 | 0.033x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 46.4 | 46.3 | 46.7 | 0.1 | 0.035x | 1.075x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 210.2 | 209.9 | 221.8 | 4.7 | 0.158x | 4.868x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 219.3 | 219.2 | 220.1 | 0.3 | 0.165x | 5.080x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,327.5 | 1,316.0 | 1,336.1 | 6.9 | 1.000x | 30.743x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,335.8 | 1,327.9 | 1,342.2 | 5.0 | 1.006x | 30.936x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-003` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 86.9 | 86.6 | 87.3 | 0.2 | 0.066x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 88.5 | 87.8 | 88.9 | 0.4 | 0.067x | 1.018x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 184.4 | 183.4 | 185.1 | 0.6 | 0.140x | 2.124x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 218.3 | 217.5 | 221.3 | 1.3 | 0.166x | 2.514x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 221.0 | 220.9 | 221.2 | 0.1 | 0.168x | 2.545x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,318.5 | 1,309.2 | 1,328.7 | 6.7 | 1.000x | 15.180x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-004` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 60.9 | 60.7 | 61.8 | 0.4 | 0.069x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 65.0 | 64.9 | 65.4 | 0.2 | 0.074x | 1.067x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 160.6 | 159.6 | 170.3 | 4.0 | 0.183x | 2.637x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 161.3 | 160.7 | 161.7 | 0.3 | 0.183x | 2.649x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 876.9 | 867.2 | 884.9 | 6.8 | 0.997x | 14.400x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 879.8 | 865.0 | 881.1 | 6.1 | 1.000x | 14.449x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-004` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 120.2 | 120.2 | 120.5 | 0.1 | 0.137x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 124.0 | 123.6 | 128.6 | 1.9 | 0.141x | 1.032x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 158.4 | 158.1 | 159.0 | 0.3 | 0.181x | 1.317x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 160.1 | 159.0 | 161.0 | 0.8 | 0.183x | 1.331x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 167.2 | 166.1 | 169.0 | 1.0 | 0.191x | 1.391x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 877.0 | 872.0 | 886.0 | 5.8 | 1.000x | 7.294x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-005` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 18.2 | 18.1 | 18.2 | 0.1 | 0.024x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.5 | 20.4 | 20.6 | 0.1 | 0.027x | 1.128x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 101.4 | 101.2 | 111.0 | 4.2 | 0.135x | 5.581x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 101.8 | 101.7 | 101.9 | 0.1 | 0.136x | 5.600x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 750.0 | 731.8 | 758.4 | 8.9 | 1.000x | 41.273x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 750.8 | 741.8 | 754.9 | 4.6 | 1.001x | 41.319x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-005` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 26.0 | 25.9 | 26.0 | 0.0 | 0.034x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 28.6 | 28.4 | 28.8 | 0.2 | 0.038x | 1.100x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 95.7 | 95.5 | 95.7 | 0.1 | 0.127x | 3.683x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 97.0 | 96.9 | 97.3 | 0.2 | 0.129x | 3.736x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 123.5 | 122.5 | 124.5 | 0.8 | 0.164x | 4.757x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 753.3 | 745.7 | 754.4 | 3.5 | 1.000x | 29.002x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-006` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 30.9 | 30.8 | 31.1 | 0.1 | 0.023x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.1 | 33.0 | 33.2 | 0.1 | 0.025x | 1.072x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 222.1 | 221.8 | 234.5 | 5.0 | 0.165x | 7.192x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 223.7 | 223.0 | 225.2 | 0.8 | 0.167x | 7.246x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,342.6 | 1,332.9 | 1,348.7 | 5.3 | 1.000x | 43.481x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,351.8 | 1,348.6 | 1,360.8 | 4.9 | 1.007x | 43.779x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-006` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 55.7 | 55.6 | 55.9 | 0.1 | 0.042x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 59.1 | 59.0 | 59.2 | 0.1 | 0.044x | 1.060x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 164.1 | 163.7 | 171.5 | 2.9 | 0.122x | 2.944x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 228.0 | 226.8 | 233.8 | 2.6 | 0.170x | 4.091x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 229.8 | 229.0 | 231.0 | 0.6 | 0.171x | 4.122x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,341.0 | 1,339.3 | 1,349.0 | 3.4 | 1.000x | 24.059x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-007` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 46.4 | 46.4 | 46.6 | 0.1 | 0.048x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 50.2 | 50.0 | 50.3 | 0.1 | 0.052x | 1.081x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 169.6 | 168.5 | 180.6 | 4.6 | 0.174x | 3.651x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 175.5 | 175.4 | 176.1 | 0.3 | 0.180x | 3.779x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 970.7 | 964.5 | 972.0 | 2.8 | 0.998x | 20.900x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 972.6 | 967.5 | 977.1 | 3.3 | 1.000x | 20.942x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-007` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 91.9 | 91.8 | 92.0 | 0.1 | 0.094x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 94.4 | 94.1 | 94.6 | 0.2 | 0.097x | 1.027x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 172.8 | 171.9 | 174.2 | 0.8 | 0.178x | 1.880x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 173.7 | 171.3 | 180.9 | 3.3 | 0.179x | 1.891x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 176.6 | 176.5 | 176.7 | 0.1 | 0.182x | 1.922x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 972.5 | 959.3 | 979.6 | 6.7 | 1.000x | 10.584x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-008` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 36.6 | 36.5 | 36.9 | 0.1 | 0.042x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 38.7 | 38.7 | 39.0 | 0.1 | 0.045x | 1.057x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 153.4 | 152.9 | 166.6 | 5.3 | 0.178x | 4.190x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 156.3 | 156.0 | 156.8 | 0.3 | 0.181x | 4.269x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 859.2 | 854.5 | 872.4 | 6.0 | 0.996x | 23.470x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 862.5 | 848.8 | 881.0 | 10.3 | 1.000x | 23.562x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-008` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 69.6 | 69.4 | 103.4 | 13.5 | 0.081x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 73.4 | 73.4 | 75.2 | 0.8 | 0.085x | 1.054x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 145.5 | 145.2 | 148.0 | 1.0 | 0.169x | 2.089x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 147.1 | 146.9 | 147.9 | 0.4 | 0.171x | 2.112x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 157.8 | 157.7 | 158.0 | 0.1 | 0.184x | 2.265x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 859.4 | 853.9 | 863.0 | 3.3 | 1.000x | 12.338x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-009` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.5 | 29.4 | 29.6 | 0.1 | 0.034x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.6 | 31.5 | 31.7 | 0.1 | 0.037x | 1.069x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 144.8 | 144.5 | 157.9 | 5.3 | 0.168x | 4.905x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 147.0 | 146.0 | 149.0 | 1.0 | 0.171x | 4.980x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 855.1 | 854.3 | 868.6 | 5.6 | 0.995x | 28.957x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 859.7 | 847.1 | 873.7 | 9.9 | 1.000x | 29.113x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-009` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 51.7 | 51.6 | 51.8 | 0.1 | 0.060x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 55.5 | 55.4 | 55.8 | 0.2 | 0.065x | 1.073x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 140.7 | 140.4 | 168.1 | 10.9 | 0.164x | 2.720x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 142.9 | 142.1 | 146.2 | 1.4 | 0.167x | 2.762x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 147.4 | 147.3 | 147.9 | 0.2 | 0.172x | 2.849x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 858.2 | 849.6 | 864.9 | 5.6 | 1.000x | 16.589x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-010` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.5 | 29.4 | 29.6 | 0.1 | 0.041x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.7 | 31.5 | 31.7 | 0.1 | 0.045x | 1.075x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 101.3 | 100.9 | 108.9 | 3.1 | 0.142x | 3.436x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 101.5 | 101.4 | 101.8 | 0.1 | 0.143x | 3.445x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 710.7 | 703.7 | 715.5 | 4.1 | 0.999x | 24.115x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 711.7 | 701.7 | 717.9 | 6.0 | 1.000x | 24.150x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-010` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 51.7 | 51.5 | 51.8 | 0.1 | 0.073x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 55.6 | 55.4 | 55.8 | 0.1 | 0.078x | 1.076x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 95.4 | 95.3 | 95.5 | 0.1 | 0.134x | 1.847x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 96.7 | 96.6 | 96.8 | 0.1 | 0.136x | 1.873x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 119.3 | 118.4 | 119.7 | 0.5 | 0.168x | 2.309x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 709.6 | 708.2 | 713.2 | 1.7 | 1.000x | 13.736x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-011` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.0 | 12.0 | 13.0 | 0.4 | 0.019x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.8 | 12.6 | 13.9 | 0.5 | 0.021x | 1.063x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 215.3 | 211.1 | 225.7 | 5.1 | 0.347x | 17.885x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 221.6 | 219.6 | 225.2 | 2.2 | 0.357x | 18.408x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 612.6 | 609.0 | 614.2 | 2.0 | 0.988x | 50.889x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 620.0 | 609.9 | 625.0 | 5.0 | 1.000x | 51.501x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-011` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 34.6 | 34.6 | 34.8 | 0.1 | 0.007x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 34.9 | 34.4 | 35.1 | 0.2 | 0.007x | 1.007x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 437.2 | 433.4 | 440.1 | 2.6 | 0.093x | 12.621x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 2,021.0 | 1,978.6 | 2,082.9 | 34.6 | 0.429x | 58.345x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 2,029.4 | 1,863.1 | 2,053.5 | 70.5 | 0.431x | 58.588x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,706.6 | 4,685.1 | 4,746.1 | 22.6 | 1.000x | 135.877x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-012` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.2 | 35.2 | 36.1 | 0.3 | 0.032x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.8 | 37.6 | 37.8 | 0.1 | 0.035x | 1.073x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 201.3 | 200.5 | 201.4 | 0.4 | 0.184x | 5.714x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 203.4 | 201.4 | 206.7 | 1.8 | 0.186x | 5.772x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,090.9 | 1,084.9 | 1,120.3 | 12.7 | 0.996x | 30.964x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,095.8 | 1,088.7 | 1,099.9 | 4.0 | 1.000x | 31.103x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-012` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 66.0 | 65.8 | 67.6 | 0.7 | 0.060x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 69.2 | 68.9 | 69.7 | 0.3 | 0.063x | 1.049x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 170.6 | 170.0 | 174.3 | 1.6 | 0.155x | 2.584x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 208.0 | 207.6 | 209.8 | 0.8 | 0.189x | 3.150x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 208.0 | 208.0 | 209.7 | 0.7 | 0.189x | 3.151x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,100.5 | 1,085.6 | 1,108.0 | 8.6 | 1.000x | 16.671x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-013` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.3 | 35.0 | 35.3 | 0.1 | 0.032x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.6 | 37.3 | 37.7 | 0.2 | 0.035x | 1.065x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 200.9 | 200.6 | 206.5 | 2.3 | 0.185x | 5.696x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 201.3 | 200.1 | 204.0 | 1.3 | 0.185x | 5.708x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,087.4 | 1,080.2 | 1,100.2 | 7.0 | 1.000x | 30.839x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,097.3 | 1,084.6 | 1,106.9 | 7.7 | 1.009x | 31.120x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-013` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 65.8 | 65.7 | 65.8 | 0.0 | 0.060x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 69.3 | 69.2 | 69.5 | 0.1 | 0.063x | 1.054x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 170.2 | 169.9 | 174.2 | 1.6 | 0.155x | 2.589x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 208.0 | 207.2 | 209.0 | 0.6 | 0.189x | 3.163x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 208.1 | 208.0 | 210.1 | 0.8 | 0.189x | 3.165x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,101.9 | 1,093.7 | 1,110.4 | 5.5 | 1.000x | 16.757x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-014` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.4 | 29.4 | 30.3 | 0.3 | 0.034x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.6 | 31.5 | 31.9 | 0.1 | 0.036x | 1.074x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 155.2 | 155.0 | 155.3 | 0.1 | 0.179x | 5.270x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 162.1 | 162.0 | 162.8 | 0.3 | 0.187x | 5.505x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 868.0 | 857.9 | 875.6 | 7.3 | 1.000x | 29.480x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 868.3 | 853.2 | 881.5 | 10.6 | 1.000x | 29.490x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-014` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 51.7 | 51.5 | 52.0 | 0.2 | 0.059x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 55.4 | 55.3 | 56.6 | 0.5 | 0.064x | 1.072x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 154.2 | 154.0 | 156.5 | 0.9 | 0.177x | 2.983x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 163.8 | 160.2 | 164.5 | 1.8 | 0.188x | 3.168x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 165.1 | 163.0 | 166.6 | 1.5 | 0.189x | 3.193x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 871.3 | 861.9 | 881.8 | 7.5 | 1.000x | 16.855x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-015` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33.6 | 33.6 | 37.0 | 1.4 | 0.032x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.9 | 35.5 | 36.0 | 0.2 | 0.034x | 1.066x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 199.9 | 199.2 | 206.3 | 2.6 | 0.190x | 5.944x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 200.1 | 199.5 | 201.3 | 0.6 | 0.190x | 5.948x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,050.5 | 1,045.1 | 1,057.8 | 4.3 | 1.000x | 31.230x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,059.9 | 1,047.0 | 1,065.3 | 6.7 | 1.009x | 31.510x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-015` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 62.6 | 62.5 | 65.2 | 1.0 | 0.059x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 65.4 | 65.4 | 65.6 | 0.1 | 0.062x | 1.045x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 173.6 | 172.9 | 174.0 | 0.4 | 0.164x | 2.773x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 206.9 | 206.7 | 207.5 | 0.3 | 0.196x | 3.305x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 207.1 | 206.4 | 208.7 | 0.9 | 0.196x | 3.308x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,055.6 | 1,047.9 | 1,069.8 | 8.8 | 1.000x | 16.861x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-016` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.1 | 11.0 | 11.2 | 0.1 | 0.031x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 11.5 | 11.2 | 11.8 | 0.2 | 0.032x | 1.038x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 103.6 | 102.2 | 105.4 | 1.1 | 0.290x | 9.323x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 104.9 | 104.3 | 106.9 | 0.9 | 0.293x | 9.438x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 358.0 | 354.6 | 363.5 | 3.0 | 1.000x | 32.200x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 362.1 | 357.4 | 363.6 | 2.1 | 1.012x | 32.572x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-016` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 26.3 | 26.1 | 26.6 | 0.2 | 0.011x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 26.3 | 25.8 | 26.8 | 0.4 | 0.011x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 260.9 | 257.9 | 275.4 | 6.5 | 0.109x | 9.939x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 1,462.5 | 1,365.2 | 1,499.5 | 45.4 | 0.613x | 55.706x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 1,501.3 | 1,467.9 | 1,537.7 | 23.6 | 0.630x | 57.186x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,384.8 | 2,372.2 | 2,393.7 | 7.9 | 1.000x | 90.837x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-017` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.2 | 35.1 | 35.9 | 0.3 | 0.032x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.3 | 37.3 | 37.5 | 0.1 | 0.034x | 1.060x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 201.0 | 200.0 | 201.5 | 0.5 | 0.184x | 5.708x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 203.2 | 200.4 | 203.8 | 1.5 | 0.186x | 5.768x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,093.6 | 1,084.3 | 1,097.7 | 5.6 | 1.000x | 31.048x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,104.8 | 1,084.9 | 1,118.4 | 11.0 | 1.010x | 31.366x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-017` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 65.8 | 65.7 | 65.8 | 0.0 | 0.060x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 69.4 | 69.1 | 69.7 | 0.2 | 0.064x | 1.054x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 170.4 | 170.3 | 174.3 | 1.6 | 0.156x | 2.591x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 208.0 | 207.8 | 214.0 | 2.4 | 0.191x | 3.161x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 208.6 | 207.9 | 209.7 | 0.6 | 0.191x | 3.172x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,091.4 | 1,083.1 | 1,119.1 | 12.3 | 1.000x | 16.591x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-018` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33.7 | 33.6 | 33.7 | 0.0 | 0.032x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.7 | 35.5 | 36.0 | 0.2 | 0.034x | 1.061x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 200.1 | 199.1 | 200.3 | 0.4 | 0.189x | 5.946x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 200.4 | 199.5 | 201.3 | 0.6 | 0.189x | 5.953x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,057.9 | 1,049.8 | 1,059.0 | 3.7 | 1.000x | 31.432x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,065.4 | 1,049.8 | 1,067.3 | 6.5 | 1.007x | 31.653x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-018` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 62.6 | 62.0 | 62.6 | 0.2 | 0.059x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 65.5 | 65.4 | 65.8 | 0.2 | 0.062x | 1.046x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 173.1 | 172.4 | 173.9 | 0.5 | 0.163x | 2.767x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 206.8 | 206.2 | 207.2 | 0.3 | 0.195x | 3.305x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 207.3 | 206.7 | 222.8 | 6.3 | 0.195x | 3.313x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,061.8 | 1,054.2 | 1,063.1 | 3.2 | 1.000x | 16.970x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-019` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.3 | 11.3 | 12.3 | 0.5 | 0.029x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.0 | 11.9 | 12.3 | 0.1 | 0.031x | 1.061x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 104.9 | 104.5 | 105.8 | 0.5 | 0.272x | 9.267x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 107.1 | 106.0 | 108.7 | 1.1 | 0.277x | 9.457x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 386.2 | 381.4 | 392.7 | 4.3 | 1.000x | 34.098x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 388.8 | 386.9 | 390.6 | 1.5 | 1.007x | 34.329x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-019` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 27.6 | 27.5 | 27.9 | 0.1 | 0.011x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 27.9 | 27.7 | 28.2 | 0.2 | 0.011x | 1.013x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 264.0 | 260.1 | 271.3 | 3.8 | 0.104x | 9.567x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 1,438.4 | 1,386.4 | 1,561.9 | 73.6 | 0.566x | 52.132x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 1,492.0 | 1,427.2 | 1,587.5 | 59.1 | 0.587x | 54.075x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,543.0 | 2,529.9 | 2,546.0 | 6.0 | 1.000x | 92.168x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-020` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 38.2 | 38.1 | 38.3 | 0.1 | 0.034x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 41.0 | 40.9 | 41.2 | 0.1 | 0.037x | 1.072x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 223.5 | 221.2 | 224.2 | 1.0 | 0.201x | 5.847x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 225.3 | 224.6 | 229.1 | 1.7 | 0.203x | 5.893x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,111.3 | 1,102.1 | 1,116.1 | 5.1 | 1.000x | 29.074x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,114.8 | 1,104.3 | 1,119.3 | 5.9 | 1.003x | 29.167x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-020` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 72.6 | 72.4 | 73.1 | 0.3 | 0.065x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 76.7 | 76.6 | 77.1 | 0.2 | 0.069x | 1.057x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 175.9 | 174.7 | 177.5 | 1.1 | 0.157x | 2.424x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 212.0 | 211.5 | 213.5 | 0.7 | 0.190x | 2.921x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 212.6 | 211.5 | 219.7 | 3.0 | 0.190x | 2.930x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,117.3 | 1,112.7 | 1,128.4 | 6.4 | 1.000x | 15.397x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-021` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.4 | 29.7 | 0.1 | 0.026x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.6 | 31.5 | 31.8 | 0.1 | 0.028x | 1.068x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 167.4 | 167.3 | 168.6 | 0.5 | 0.147x | 5.653x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 168.2 | 166.9 | 168.7 | 0.8 | 0.147x | 5.680x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,142.4 | 1,134.5 | 1,163.8 | 9.8 | 1.000x | 38.578x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,142.4 | 1,138.1 | 1,158.8 | 7.7 | 1.000x | 38.579x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-021` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 51.8 | 51.4 | 52.3 | 0.4 | 0.045x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 55.4 | 55.4 | 57.3 | 0.7 | 0.048x | 1.070x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 109.6 | 109.4 | 112.5 | 1.3 | 0.095x | 2.117x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 168.5 | 168.3 | 168.6 | 0.1 | 0.147x | 3.253x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 173.8 | 173.6 | 184.3 | 4.1 | 0.151x | 3.356x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,148.5 | 1,146.2 | 1,159.2 | 4.9 | 1.000x | 22.178x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-022` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 41.5 | 41.5 | 41.9 | 0.1 | 0.061x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 44.7 | 44.5 | 44.7 | 0.1 | 0.065x | 1.075x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 140.5 | 140.5 | 147.9 | 2.9 | 0.205x | 3.383x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 142.0 | 140.9 | 149.0 | 3.0 | 0.207x | 3.420x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 684.9 | 682.6 | 690.0 | 2.4 | 1.000x | 16.492x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 686.0 | 675.7 | 692.9 | 5.5 | 1.002x | 16.518x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-022` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 80.6 | 80.6 | 80.8 | 0.1 | 0.119x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 84.5 | 84.2 | 89.5 | 2.0 | 0.125x | 1.049x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 98.3 | 98.1 | 98.5 | 0.1 | 0.145x | 1.219x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 139.4 | 139.3 | 140.2 | 0.3 | 0.206x | 1.729x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 140.4 | 139.7 | 144.8 | 1.8 | 0.207x | 1.741x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 677.1 | 674.1 | 687.8 | 5.6 | 1.000x | 8.397x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-023` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.2 | 35.1 | 35.3 | 0.1 | 0.031x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.4 | 37.2 | 37.5 | 0.1 | 0.033x | 1.064x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 168.2 | 167.3 | 168.4 | 0.4 | 0.149x | 4.784x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 171.4 | 171.1 | 173.7 | 1.0 | 0.152x | 4.874x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,129.8 | 1,119.5 | 1,131.9 | 4.6 | 1.000x | 32.129x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,130.3 | 1,121.2 | 1,145.5 | 9.8 | 1.000x | 32.143x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-023` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 65.8 | 65.6 | 66.4 | 0.3 | 0.058x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 69.2 | 69.1 | 69.4 | 0.1 | 0.061x | 1.052x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 107.2 | 106.5 | 108.1 | 0.6 | 0.095x | 1.629x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 169.3 | 168.9 | 183.0 | 5.4 | 0.150x | 2.574x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 170.5 | 170.5 | 171.1 | 0.3 | 0.151x | 2.591x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,129.1 | 1,126.6 | 1,134.3 | 2.7 | 1.000x | 17.165x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-024` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.5 | 29.4 | 29.6 | 0.1 | 0.026x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.6 | 31.5 | 31.8 | 0.1 | 0.027x | 1.072x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 171.5 | 171.5 | 174.2 | 1.0 | 0.149x | 5.823x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 172.6 | 172.3 | 172.9 | 0.2 | 0.150x | 5.858x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,148.5 | 1,137.8 | 1,154.1 | 5.3 | 0.999x | 38.985x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,149.7 | 1,143.9 | 1,171.8 | 10.6 | 1.000x | 39.026x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-024` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 51.6 | 51.4 | 51.7 | 0.1 | 0.045x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 55.5 | 55.3 | 56.0 | 0.2 | 0.048x | 1.075x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 108.8 | 108.4 | 114.2 | 2.2 | 0.095x | 2.108x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 173.2 | 172.1 | 187.0 | 5.7 | 0.151x | 3.355x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 177.5 | 177.4 | 177.9 | 0.2 | 0.154x | 3.438x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,148.7 | 1,141.7 | 1,157.2 | 5.1 | 1.000x | 22.252x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-025` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.2 | 35.1 | 39.1 | 1.6 | 0.031x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.3 | 37.3 | 37.4 | 0.0 | 0.033x | 1.060x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 175.5 | 175.2 | 175.5 | 0.1 | 0.154x | 4.987x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 176.1 | 176.1 | 178.2 | 0.8 | 0.155x | 5.005x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,136.6 | 1,132.6 | 1,146.8 | 5.1 | 1.000x | 32.303x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,136.9 | 1,131.5 | 1,154.4 | 8.2 | 1.000x | 32.314x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-025` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 66.1 | 65.8 | 67.3 | 0.6 | 0.058x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 69.3 | 69.0 | 69.4 | 0.2 | 0.061x | 1.049x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 106.6 | 106.4 | 106.9 | 0.2 | 0.094x | 1.613x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 176.6 | 176.5 | 183.8 | 2.9 | 0.156x | 2.671x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 178.0 | 177.9 | 179.0 | 0.4 | 0.157x | 2.694x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,134.4 | 1,133.5 | 1,147.7 | 5.3 | 1.000x | 17.163x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-026` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 41.6 | 41.4 | 41.6 | 0.1 | 0.061x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 44.7 | 44.6 | 44.7 | 0.0 | 0.065x | 1.075x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 140.5 | 140.5 | 140.9 | 0.2 | 0.205x | 3.382x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 141.0 | 140.9 | 148.9 | 3.1 | 0.206x | 3.393x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 680.4 | 675.6 | 684.3 | 3.6 | 0.994x | 16.375x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 684.8 | 678.3 | 688.0 | 3.3 | 1.000x | 16.480x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-026` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 80.6 | 80.2 | 85.3 | 1.9 | 0.119x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 84.4 | 84.3 | 85.1 | 0.3 | 0.124x | 1.047x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 98.4 | 98.2 | 100.9 | 1.0 | 0.145x | 1.221x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 139.3 | 138.4 | 140.2 | 0.6 | 0.205x | 1.729x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 140.4 | 140.1 | 140.9 | 0.3 | 0.207x | 1.741x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 679.5 | 678.9 | 684.4 | 2.1 | 1.000x | 8.430x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-027` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 41.5 | 41.3 | 41.6 | 0.1 | 0.038x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 44.6 | 44.6 | 44.7 | 0.1 | 0.041x | 1.076x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 169.0 | 168.2 | 170.6 | 0.8 | 0.157x | 4.074x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 172.4 | 171.0 | 174.6 | 1.2 | 0.160x | 4.155x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,073.9 | 1,067.5 | 1,083.2 | 5.1 | 0.996x | 25.882x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,077.9 | 1,060.7 | 1,091.5 | 11.7 | 1.000x | 25.980x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-027` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 80.4 | 80.0 | 80.7 | 0.2 | 0.075x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 84.6 | 84.2 | 89.4 | 2.0 | 0.078x | 1.052x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 104.3 | 104.1 | 104.4 | 0.1 | 0.097x | 1.297x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 171.8 | 171.5 | 174.5 | 1.1 | 0.159x | 2.136x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 173.4 | 173.0 | 173.4 | 0.2 | 0.161x | 2.156x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,078.2 | 1,072.2 | 1,083.9 | 3.9 | 1.000x | 13.407x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-028` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.2 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.6 | 13.1 | 13.9 | 0.3 | 0.017x | 1.031x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 181.4 | 173.7 | 194.7 | 7.0 | 0.231x | 13.783x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 190.5 | 181.5 | 192.3 | 3.9 | 0.242x | 14.474x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 779.0 | 775.2 | 784.0 | 2.8 | 0.991x | 59.197x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 786.1 | 779.8 | 788.9 | 3.2 | 1.000x | 59.729x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-028` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 22.2 | 22.1 | 22.9 | 0.3 | 0.008x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 22.4 | 22.2 | 23.0 | 0.3 | 0.008x | 1.011x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 219.1 | 213.5 | 236.8 | 8.2 | 0.082x | 9.866x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 936.8 | 889.8 | 954.8 | 23.4 | 0.351x | 42.189x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 989.4 | 911.7 | 1,061.6 | 50.8 | 0.370x | 44.560x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,672.2 | 2,664.8 | 2,724.5 | 21.9 | 1.000x | 120.348x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-029` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.1 | 13.1 | 13.6 | 0.2 | 0.017x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.2 | 0.0 | 0.017x | 1.004x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 182.7 | 179.2 | 197.0 | 6.2 | 0.231x | 13.913x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 189.9 | 182.4 | 196.7 | 4.6 | 0.240x | 14.456x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 780.5 | 771.4 | 783.5 | 4.1 | 0.987x | 59.423x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 790.5 | 778.9 | 809.5 | 10.9 | 1.000x | 60.181x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-029` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 45.3 | 45.3 | 45.6 | 0.1 | 0.017x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 45.4 | 45.4 | 45.6 | 0.1 | 0.017x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 235.0 | 229.5 | 236.2 | 2.4 | 0.088x | 5.183x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,663.5 | 2,654.4 | 2,701.7 | 16.5 | 1.000x | 58.738x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 3,261.3 | 3,149.2 | 3,354.0 | 65.4 | 1.224x | 71.920x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 3,309.6 | 3,195.4 | 3,403.3 | 83.4 | 1.243x | 72.986x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-030` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.1 | 13.1 | 13.2 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.2 | 0.0 | 0.017x | 1.001x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 182.1 | 181.3 | 196.1 | 5.7 | 0.234x | 13.861x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 190.0 | 181.6 | 197.1 | 5.2 | 0.244x | 14.465x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 778.3 | 774.4 | 792.8 | 7.0 | 1.000x | 59.255x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 779.9 | 773.4 | 781.0 | 2.7 | 1.002x | 59.377x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-030` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 22.2 | 22.0 | 22.4 | 0.1 | 0.008x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 22.4 | 22.3 | 23.6 | 0.5 | 0.008x | 1.007x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 218.9 | 214.4 | 220.1 | 2.1 | 0.082x | 9.850x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 961.1 | 864.6 | 1,027.5 | 57.3 | 0.360x | 43.256x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 977.9 | 874.1 | 1,010.9 | 57.3 | 0.367x | 44.012x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,667.6 | 2,657.4 | 2,687.5 | 10.9 | 1.000x | 120.057x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-031` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.1 | 13.1 | 13.2 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.2 | 0.0 | 0.017x | 1.002x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 182.3 | 177.7 | 196.7 | 6.5 | 0.233x | 13.865x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 190.7 | 181.6 | 191.9 | 3.8 | 0.244x | 14.503x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 778.6 | 771.1 | 782.9 | 4.1 | 0.996x | 59.215x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 781.7 | 777.5 | 789.0 | 3.8 | 1.000x | 59.456x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-031` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 29.8 | 29.7 | 30.0 | 0.1 | 0.011x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 30.0 | 29.8 | 30.0 | 0.1 | 0.011x | 1.006x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 233.8 | 229.1 | 235.8 | 2.5 | 0.088x | 7.838x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 1,488.6 | 1,355.8 | 1,685.8 | 105.4 | 0.558x | 49.908x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 1,508.8 | 1,284.9 | 1,551.3 | 96.7 | 0.566x | 50.584x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,667.5 | 2,648.2 | 2,674.4 | 8.9 | 1.000x | 89.433x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-032` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.0 | 16.0 | 16.1 | 0.1 | 0.017x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.0 | 16.0 | 16.1 | 0.0 | 0.017x | 1.001x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 278.2 | 271.4 | 296.2 | 9.9 | 0.300x | 17.347x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 300.5 | 255.6 | 461.8 | 75.7 | 0.325x | 18.736x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 921.5 | 918.9 | 931.7 | 5.0 | 0.995x | 57.464x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 925.8 | 919.6 | 931.8 | 4.1 | 1.000x | 57.731x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-032` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 26.1 | 26.0 | 26.3 | 0.1 | 0.008x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 26.5 | 26.0 | 26.8 | 0.3 | 0.008x | 1.015x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 321.9 | 316.3 | 324.4 | 3.0 | 0.098x | 12.342x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 1,721.4 | 1,701.2 | 1,796.8 | 35.7 | 0.526x | 65.995x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 1,754.3 | 1,733.0 | 1,871.4 | 51.6 | 0.536x | 67.257x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,270.2 | 3,237.5 | 3,336.2 | 32.9 | 1.000x | 125.373x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-033` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.0 | 15.9 | 16.1 | 0.1 | 0.018x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.0 | 16.0 | 16.1 | 0.1 | 0.018x | 1.002x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 269.3 | 227.2 | 405.8 | 62.3 | 0.308x | 16.839x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 301.6 | 298.9 | 314.8 | 5.8 | 0.345x | 18.857x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 874.2 | 871.2 | 880.7 | 3.3 | 1.000x | 54.653x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 875.4 | 869.8 | 880.2 | 3.5 | 1.001x | 54.732x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-033` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 26.0 | 25.9 | 26.7 | 0.3 | 0.009x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 26.3 | 26.1 | 26.9 | 0.3 | 0.009x | 1.010x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 322.4 | 315.7 | 336.2 | 7.0 | 0.106x | 12.377x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 1,733.1 | 1,715.7 | 1,793.9 | 27.7 | 0.571x | 66.540x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 1,744.0 | 1,718.6 | 1,845.3 | 46.7 | 0.575x | 66.959x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,032.6 | 3,026.0 | 3,039.4 | 5.6 | 1.000x | 116.438x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-034` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.1 | 20.0 | 20.3 | 0.1 | 0.016x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 20.2 | 20.1 | 20.3 | 0.1 | 0.016x | 1.003x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.5 | 145.0 | 146.6 | 0.5 | 0.116x | 7.220x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 149.1 | 147.9 | 151.7 | 1.2 | 0.119x | 7.403x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,254.6 | 1,246.1 | 1,280.1 | 12.6 | 1.000x | 62.272x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,254.9 | 1,244.7 | 1,268.0 | 7.8 | 1.000x | 62.287x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-034` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 19.1 | 19.0 | 19.1 | 0.0 | 0.004x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 19.2 | 18.9 | 19.4 | 0.2 | 0.004x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 387.1 | 381.6 | 392.8 | 4.2 | 0.084x | 20.285x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 630.9 | 597.3 | 743.1 | 60.6 | 0.137x | 33.064x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 721.8 | 617.3 | 840.1 | 73.7 | 0.156x | 37.826x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,621.5 | 4,601.2 | 4,628.4 | 11.8 | 1.000x | 242.199x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-035` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.0 | 22.9 | 23.1 | 0.1 | 0.014x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 23.0 | 23.0 | 23.6 | 0.3 | 0.014x | 1.001x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 406.7 | 384.8 | 486.4 | 37.1 | 0.256x | 17.712x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 466.8 | 391.0 | 477.3 | 32.6 | 0.294x | 20.328x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,581.8 | 1,579.2 | 1,643.6 | 24.4 | 0.995x | 68.878x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,589.1 | 1,573.4 | 1,592.3 | 6.7 | 1.000x | 69.195x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-035` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 25.1 | 25.1 | 25.6 | 0.2 | 0.004x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 25.3 | 25.1 | 25.4 | 0.1 | 0.004x | 1.006x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 477.9 | 474.7 | 501.6 | 11.0 | 0.081x | 19.003x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 1,761.7 | 1,758.1 | 2,384.9 | 249.8 | 0.300x | 70.054x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 1,763.1 | 1,757.3 | 1,778.0 | 7.0 | 0.300x | 70.109x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 5,867.4 | 5,866.0 | 5,911.6 | 19.5 | 1.000x | 233.318x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-036` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.1 | 11.9 | 12.3 | 0.1 | 0.019x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.6 | 12.5 | 12.9 | 0.1 | 0.020x | 1.044x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.5 | 143.4 | 146.1 | 1.0 | 0.231x | 12.026x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 148.2 | 147.5 | 149.2 | 0.6 | 0.236x | 12.247x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 628.9 | 626.0 | 639.5 | 5.5 | 1.000x | 51.990x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 633.8 | 630.9 | 643.0 | 4.2 | 1.008x | 52.389x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-036` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 26.8 | 26.6 | 27.2 | 0.2 | 0.013x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 27.0 | 27.0 | 27.8 | 0.3 | 0.013x | 1.008x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 194.0 | 187.9 | 195.1 | 2.6 | 0.093x | 7.230x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 1,493.7 | 1,465.6 | 1,541.6 | 28.4 | 0.719x | 55.679x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 1,511.2 | 1,484.7 | 1,727.7 | 91.1 | 0.727x | 56.330x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,077.7 | 2,061.7 | 2,099.7 | 12.7 | 1.000x | 77.447x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-037` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 14.5 | 14.4 | 14.6 | 0.1 | 0.017x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.6 | 14.4 | 14.7 | 0.1 | 0.017x | 1.011x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 208.5 | 206.1 | 211.5 | 1.8 | 0.246x | 14.431x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 211.0 | 210.1 | 211.3 | 0.4 | 0.249x | 14.600x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 846.0 | 839.5 | 847.9 | 3.4 | 0.997x | 58.545x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 848.6 | 843.5 | 854.9 | 4.0 | 1.000x | 58.722x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-037` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 21.0 | 20.8 | 21.2 | 0.1 | 0.007x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 21.1 | 20.8 | 21.3 | 0.2 | 0.007x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 282.8 | 279.5 | 306.2 | 10.0 | 0.097x | 13.480x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 1,320.1 | 1,311.4 | 1,333.1 | 8.1 | 0.453x | 62.930x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 1,359.2 | 1,343.0 | 1,370.3 | 9.2 | 0.466x | 64.792x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,914.4 | 2,902.0 | 2,937.3 | 12.3 | 1.000x | 138.928x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-038` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.0 | 23.0 | 23.1 | 0.0 | 0.023x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 23.0 | 22.9 | 23.0 | 0.0 | 0.023x | 1.001x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 488.6 | 444.7 | 504.7 | 21.1 | 0.485x | 21.259x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 494.1 | 467.6 | 508.8 | 13.8 | 0.491x | 21.501x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,006.6 | 994.3 | 1,029.1 | 11.3 | 1.000x | 43.800x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,009.0 | 1,002.1 | 1,021.5 | 6.3 | 1.002x | 43.906x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-038` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 26.8 | 26.7 | 27.9 | 0.5 | 0.007x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 26.9 | 26.8 | 27.0 | 0.1 | 0.007x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 569.0 | 561.9 | 576.0 | 4.8 | 0.158x | 21.223x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 2,866.7 | 2,846.3 | 2,895.7 | 16.6 | 0.797x | 106.921x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 2,928.2 | 2,853.0 | 3,025.5 | 72.2 | 0.815x | 109.213x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,594.7 | 3,549.9 | 3,615.4 | 25.2 | 1.000x | 134.072x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-039` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.3 | 11.2 | 11.5 | 0.1 | 0.030x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.0 | 11.8 | 12.3 | 0.2 | 0.032x | 1.061x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 104.8 | 103.6 | 105.3 | 0.6 | 0.278x | 9.263x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 105.2 | 104.8 | 108.1 | 1.2 | 0.279x | 9.300x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 376.5 | 374.4 | 379.8 | 1.8 | 0.999x | 33.292x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 377.0 | 375.5 | 381.6 | 2.1 | 1.000x | 33.338x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-039` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 59.1 | 58.9 | 59.8 | 0.3 | 0.038x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 62.3 | 62.2 | 63.1 | 0.3 | 0.040x | 1.054x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 209.5 | 208.6 | 211.7 | 1.0 | 0.135x | 3.543x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 299.4 | 296.5 | 300.0 | 1.3 | 0.193x | 5.065x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 302.6 | 301.1 | 308.9 | 3.5 | 0.196x | 5.119x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,547.8 | 1,538.0 | 1,562.7 | 9.8 | 1.000x | 26.181x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-040` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 26.0 | 25.9 | 26.0 | 0.0 | 0.787x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 26.0 | 25.9 | 26.0 | 0.0 | 0.787x | 1.001x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 33.0 | 32.7 | 33.7 | 0.4 | 1.000x | 1.271x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 34.0 | 33.3 | 35.0 | 0.5 | 1.029x | 1.308x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 255.2 | 253.9 | 255.8 | 0.6 | 7.738x | 9.835x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 256.5 | 255.5 | 257.4 | 0.7 | 7.776x | 9.884x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-040` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 23.6 | 23.5 | 23.9 | 0.1 | 0.691x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 23.8 | 23.7 | 24.1 | 0.2 | 0.698x | 1.009x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 34.1 | 33.9 | 35.1 | 0.4 | 1.000x | 1.447x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.4 | 44.3 | 44.4 | 0.0 | 1.301x | 1.882x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 1,816.4 | 1,727.6 | 1,852.9 | 46.3 | 53.277x | 77.082x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 1,849.4 | 1,764.1 | 1,897.4 | 43.8 | 54.248x | 78.486x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-041` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 9.8 | 10.3 | 0.2 | 0.062x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.5 | 10.3 | 10.8 | 0.2 | 0.064x | 1.041x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 47.8 | 47.6 | 48.2 | 0.3 | 0.295x | 4.764x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 49.6 | 49.4 | 49.7 | 0.1 | 0.306x | 4.940x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 162.2 | 161.1 | 164.0 | 0.9 | 1.000x | 16.156x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 162.9 | 161.6 | 167.7 | 2.1 | 1.004x | 16.222x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-041` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.4 | 18.4 | 18.8 | 0.2 | 0.104x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.7 | 18.5 | 19.1 | 0.2 | 0.105x | 1.012x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 54.7 | 54.6 | 54.7 | 0.0 | 0.309x | 2.964x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 177.1 | 177.0 | 179.9 | 1.3 | 1.000x | 9.604x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 986.1 | 901.7 | 995.1 | 41.9 | 5.567x | 53.470x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 1,019.3 | 832.5 | 1,058.7 | 82.4 | 5.755x | 55.270x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-042` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.1 | 13.0 | 13.1 | 0.0 | 0.022x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.6 | 13.6 | 17.1 | 1.4 | 0.022x | 1.041x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 96.2 | 74.7 | 98.6 | 8.9 | 0.158x | 7.342x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 97.4 | 78.1 | 98.3 | 7.8 | 0.160x | 7.432x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 608.9 | 607.3 | 617.2 | 3.8 | 1.000x | 46.464x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 611.9 | 604.7 | 614.7 | 3.5 | 1.005x | 46.694x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-042` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 11.6 | 11.5 | 12.1 | 0.2 | 0.019x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 12.0 | 11.9 | 12.0 | 0.0 | 0.019x | 1.031x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 84.2 | 83.5 | 85.0 | 0.5 | 0.135x | 7.255x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 172.0 | 170.7 | 187.9 | 6.4 | 0.275x | 14.816x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 172.5 | 171.7 | 194.5 | 8.7 | 0.276x | 14.860x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 624.7 | 620.6 | 627.7 | 2.5 | 1.000x | 53.826x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-043` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.2 | 11.9 | 12.4 | 0.2 | 0.021x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.6 | 12.5 | 12.8 | 0.1 | 0.022x | 1.031x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.3 | 144.1 | 147.1 | 1.1 | 0.253x | 11.907x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 153.1 | 148.2 | 154.9 | 2.5 | 0.266x | 12.545x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 575.2 | 571.8 | 582.2 | 3.7 | 1.000x | 47.136x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 575.5 | 574.1 | 594.4 | 7.7 | 1.000x | 47.153x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-043` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 71.3 | 71.0 | 71.7 | 0.2 | 0.026x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 74.0 | 73.5 | 75.4 | 0.7 | 0.027x | 1.039x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 292.5 | 290.5 | 293.0 | 1.0 | 0.105x | 4.104x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 711.6 | 688.6 | 744.4 | 19.7 | 0.255x | 9.983x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 744.2 | 696.4 | 781.9 | 29.9 | 0.266x | 10.441x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,793.1 | 2,776.7 | 2,800.6 | 8.7 | 1.000x | 39.185x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-044` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.9 | 9.8 | 10.4 | 0.3 | 0.061x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.3 | 10.7 | 0.1 | 0.065x | 1.054x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 47.9 | 47.8 | 48.6 | 0.3 | 0.297x | 4.840x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 49.4 | 49.0 | 49.5 | 0.2 | 0.307x | 4.998x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 161.1 | 159.1 | 166.5 | 2.5 | 1.000x | 16.289x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 162.5 | 161.7 | 166.1 | 1.6 | 1.009x | 16.429x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-044` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 61.9 | 61.7 | 63.1 | 0.5 | 0.061x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 63.8 | 63.5 | 63.9 | 0.1 | 0.063x | 1.032x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 158.3 | 157.8 | 160.1 | 0.9 | 0.156x | 2.559x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 162.0 | 161.5 | 162.9 | 0.5 | 0.160x | 2.618x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 164.4 | 163.4 | 165.3 | 0.7 | 0.162x | 2.657x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,014.3 | 1,007.7 | 1,027.6 | 6.8 | 1.000x | 16.394x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-045` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.2 | 12.1 | 12.3 | 0.1 | 0.021x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.5 | 12.4 | 12.9 | 0.2 | 0.022x | 1.028x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 146.2 | 145.2 | 159.3 | 5.3 | 0.253x | 11.975x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 150.7 | 149.5 | 151.2 | 0.6 | 0.261x | 12.347x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 572.8 | 571.6 | 580.1 | 3.3 | 0.993x | 46.927x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 577.0 | 569.8 | 577.4 | 2.9 | 1.000x | 47.276x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-045` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 25.5 | 25.5 | 25.8 | 0.1 | 0.013x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 25.7 | 25.5 | 26.0 | 0.2 | 0.013x | 1.007x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 199.6 | 187.5 | 200.0 | 4.9 | 0.100x | 7.818x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 1,394.8 | 1,380.5 | 1,799.6 | 159.3 | 0.701x | 54.620x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 1,501.2 | 1,404.6 | 1,620.2 | 76.4 | 0.755x | 58.788x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,989.4 | 1,956.6 | 1,997.6 | 14.6 | 1.000x | 77.907x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-046` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.7 | 21.7 | 22.9 | 0.5 | 0.022x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.7 | 21.6 | 21.8 | 0.1 | 0.022x | 1.000x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 374.0 | 346.8 | 413.7 | 26.2 | 0.372x | 17.253x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 391.1 | 380.9 | 404.4 | 7.9 | 0.389x | 18.041x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 998.5 | 990.6 | 1,013.8 | 8.5 | 0.994x | 46.061x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,004.2 | 989.0 | 1,018.7 | 10.9 | 1.000x | 46.326x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-046` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 19.1 | 18.8 | 19.4 | 0.2 | 0.005x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 19.8 | 19.7 | 19.9 | 0.1 | 0.006x | 1.039x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 533.5 | 528.2 | 537.1 | 2.9 | 0.151x | 27.946x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 1,726.9 | 1,707.8 | 1,816.0 | 40.0 | 0.490x | 90.465x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 1,744.6 | 1,704.8 | 1,819.5 | 40.5 | 0.495x | 91.397x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,525.7 | 3,516.8 | 3,538.9 | 7.1 | 1.000x | 184.703x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-047` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 23.0 | 23.0 | 23.1 | 0.1 | 0.014x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.0 | 23.0 | 23.1 | 0.0 | 0.014x | 1.000x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 144.7 | 144.5 | 145.6 | 0.4 | 0.089x | 6.297x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 147.9 | 146.6 | 149.3 | 1.0 | 0.091x | 6.436x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,614.4 | 1,603.2 | 1,635.6 | 10.7 | 0.998x | 70.250x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,617.7 | 1,603.4 | 1,628.1 | 9.7 | 1.000x | 70.393x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-047` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 20.5 | 20.4 | 20.8 | 0.2 | 0.003x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 20.6 | 20.4 | 20.6 | 0.1 | 0.003x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 466.5 | 464.0 | 471.2 | 2.4 | 0.077x | 22.756x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 760.0 | 698.3 | 898.3 | 71.2 | 0.125x | 37.073x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 900.8 | 738.8 | 1,004.4 | 92.3 | 0.149x | 43.940x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 6,063.9 | 6,004.3 | 6,176.9 | 61.1 | 1.000x | 295.784x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-048` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.1 | 13.1 | 13.1 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.2 | 0.0 | 0.017x | 1.005x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 105.6 | 103.8 | 109.8 | 2.0 | 0.136x | 8.048x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 108.3 | 107.9 | 110.5 | 0.9 | 0.140x | 8.254x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 774.2 | 773.1 | 784.9 | 5.2 | 1.000x | 59.000x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 778.0 | 775.8 | 792.8 | 6.3 | 1.005x | 59.288x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-048` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 12.0 | 11.9 | 12.1 | 0.1 | 0.006x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 12.5 | 12.2 | 13.0 | 0.3 | 0.006x | 1.036x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 183.1 | 181.3 | 186.4 | 1.8 | 0.090x | 15.221x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 336.3 | 302.9 | 388.9 | 32.7 | 0.166x | 27.958x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 385.5 | 318.9 | 399.0 | 31.2 | 0.190x | 32.050x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,027.1 | 2,020.1 | 2,096.4 | 33.4 | 1.000x | 168.534x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-049` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.7 | 11.5 | 11.9 | 0.2 | 0.022x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.4 | 12.1 | 12.5 | 0.1 | 0.023x | 1.062x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 129.3 | 127.0 | 140.9 | 5.0 | 0.239x | 11.053x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 132.2 | 130.7 | 313.0 | 72.6 | 0.244x | 11.301x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 541.8 | 540.1 | 578.0 | 14.5 | 1.000x | 46.317x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 549.6 | 546.1 | 556.3 | 3.6 | 1.014x | 46.982x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-049` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 68.8 | 68.5 | 69.0 | 0.2 | 0.027x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 71.6 | 71.3 | 72.7 | 0.5 | 0.028x | 1.041x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 271.3 | 270.7 | 274.6 | 1.8 | 0.106x | 3.945x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 596.5 | 581.3 | 606.6 | 8.2 | 0.233x | 8.673x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 613.5 | 594.6 | 668.7 | 26.0 | 0.240x | 8.920x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,559.3 | 2,541.1 | 2,580.9 | 13.4 | 1.000x | 37.211x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-050` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.5 | 14.4 | 14.6 | 0.1 | 0.019x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 14.5 | 14.3 | 14.7 | 0.1 | 0.019x | 1.002x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 253.2 | 233.7 | 280.3 | 15.4 | 0.331x | 17.495x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 269.7 | 236.7 | 335.6 | 34.1 | 0.352x | 18.634x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 765.4 | 762.2 | 802.1 | 14.8 | 1.000x | 52.889x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 765.8 | 763.2 | 772.6 | 3.6 | 1.000x | 52.914x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-050` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 53.7 | 53.3 | 54.9 | 0.6 | 0.015x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 57.0 | 56.7 | 57.2 | 0.2 | 0.016x | 1.062x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 378.3 | 372.4 | 381.5 | 3.4 | 0.107x | 7.050x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 1,001.5 | 993.3 | 1,085.3 | 34.5 | 0.285x | 18.664x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 1,023.6 | 1,010.8 | 1,099.7 | 32.1 | 0.291x | 19.075x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,519.7 | 3,513.1 | 3,537.6 | 8.7 | 1.000x | 65.591x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-051` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.7 | 11.6 | 11.9 | 0.1 | 0.021x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.3 | 12.1 | 12.6 | 0.2 | 0.023x | 1.052x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 128.5 | 127.3 | 129.4 | 0.8 | 0.235x | 10.973x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 130.6 | 129.9 | 131.0 | 0.4 | 0.239x | 11.152x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 546.6 | 538.1 | 547.8 | 3.6 | 1.000x | 46.679x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 548.6 | 545.3 | 552.4 | 2.7 | 1.004x | 46.847x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-051` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 68.6 | 68.5 | 69.1 | 0.2 | 0.027x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 71.8 | 71.7 | 72.2 | 0.2 | 0.028x | 1.047x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 273.3 | 270.8 | 283.7 | 4.6 | 0.107x | 3.983x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 593.4 | 542.8 | 612.0 | 23.1 | 0.231x | 8.650x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 593.7 | 588.0 | 644.0 | 21.0 | 0.231x | 8.654x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,564.9 | 2,544.1 | 2,577.3 | 10.9 | 1.000x | 37.388x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-052` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.2 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.0 | 0.017x | 1.008x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.9 | 143.9 | 146.5 | 0.9 | 0.188x | 11.087x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 147.9 | 146.8 | 148.3 | 0.5 | 0.190x | 11.241x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 777.2 | 766.6 | 785.4 | 8.1 | 1.000x | 59.051x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 787.0 | 773.9 | 792.2 | 6.5 | 1.013x | 59.791x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-052` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 19.6 | 19.5 | 19.9 | 0.1 | 0.007x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 20.0 | 19.8 | 20.2 | 0.1 | 0.007x | 1.020x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 220.3 | 213.4 | 228.1 | 4.9 | 0.082x | 11.220x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 627.8 | 622.2 | 774.3 | 66.5 | 0.234x | 31.979x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 676.0 | 614.3 | 750.0 | 46.9 | 0.252x | 34.437x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,687.4 | 2,658.3 | 2,692.7 | 12.7 | 1.000x | 136.897x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-053` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.2 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 0.017x | 1.002x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.4 | 144.0 | 145.8 | 0.7 | 0.187x | 11.036x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 148.2 | 145.8 | 149.5 | 1.5 | 0.191x | 11.247x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 776.4 | 769.5 | 787.0 | 5.9 | 1.000x | 58.942x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 779.0 | 770.3 | 799.3 | 11.3 | 1.003x | 59.140x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-053` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 14.3 | 14.2 | 14.4 | 0.1 | 0.005x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 14.4 | 14.2 | 14.8 | 0.2 | 0.005x | 1.011x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 217.9 | 215.0 | 221.4 | 2.3 | 0.082x | 15.246x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 614.1 | 568.0 | 620.7 | 20.6 | 0.231x | 42.968x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 638.4 | 611.8 | 815.6 | 73.1 | 0.240x | 44.667x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,663.7 | 2,651.0 | 2,690.4 | 13.7 | 1.000x | 186.373x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-054` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.1 | 13.1 | 13.2 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.1 | 0.017x | 1.008x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 144.3 | 142.3 | 146.6 | 1.6 | 0.187x | 10.979x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 148.2 | 146.4 | 153.5 | 2.5 | 0.192x | 11.270x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 771.8 | 763.4 | 784.8 | 7.5 | 1.000x | 58.702x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 782.1 | 770.5 | 785.3 | 5.5 | 1.013x | 59.486x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-054` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 14.4 | 14.1 | 14.7 | 0.2 | 0.005x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 14.5 | 14.2 | 14.6 | 0.2 | 0.005x | 1.008x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 217.5 | 215.3 | 220.7 | 2.0 | 0.082x | 15.126x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 629.0 | 577.3 | 736.6 | 54.8 | 0.236x | 43.744x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 655.0 | 579.8 | 665.8 | 33.8 | 0.246x | 45.550x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,660.0 | 2,652.5 | 2,670.4 | 6.1 | 1.000x | 184.990x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-055` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.3 | 0.1 | 0.017x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 0.017x | 1.006x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 144.8 | 141.6 | 147.8 | 2.0 | 0.188x | 10.999x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 147.4 | 146.7 | 154.4 | 2.8 | 0.191x | 11.196x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 772.1 | 770.4 | 781.3 | 4.7 | 1.000x | 58.633x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 778.5 | 772.8 | 787.2 | 4.7 | 1.008x | 59.115x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-055` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 14.2 | 14.0 | 14.4 | 0.1 | 0.005x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 14.4 | 14.3 | 14.8 | 0.2 | 0.005x | 1.008x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 214.2 | 211.5 | 220.0 | 3.2 | 0.080x | 15.042x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 653.6 | 527.0 | 720.7 | 73.2 | 0.245x | 45.890x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 671.8 | 621.3 | 700.9 | 26.7 | 0.252x | 47.168x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,666.4 | 2,641.5 | 2,686.6 | 14.6 | 1.000x | 187.204x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-056` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.2 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 0.017x | 1.004x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 144.9 | 143.6 | 145.8 | 0.8 | 0.187x | 11.015x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 148.4 | 146.7 | 149.4 | 1.0 | 0.192x | 11.276x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 773.8 | 767.3 | 785.3 | 5.9 | 1.000x | 58.803x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 780.0 | 778.1 | 819.8 | 16.0 | 1.008x | 59.274x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-056` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 16.3 | 16.3 | 16.5 | 0.1 | 0.006x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 16.5 | 16.5 | 16.6 | 0.1 | 0.006x | 1.010x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 218.6 | 209.8 | 221.9 | 4.5 | 0.082x | 13.397x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 634.4 | 575.8 | 832.0 | 89.7 | 0.237x | 38.887x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 649.7 | 550.1 | 741.3 | 60.5 | 0.243x | 39.825x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,674.0 | 2,643.3 | 2,679.8 | 13.6 | 1.000x | 163.915x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-057` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7,744.6 | 7,738.8 | 7,772.7 | 12.3 | 0.762x | 1.000x |
| 2 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 7,762.8 | 7,735.5 | 7,844.2 | 38.5 | 0.764x | 1.002x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 10,167.1 | 10,130.0 | 10,215.3 | 28.3 | 1.000x | 1.313x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 10,206.4 | 10,113.3 | 10,239.2 | 44.8 | 1.004x | 1.318x |
| 5 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 19,083.4 | 19,067.9 | 19,205.9 | 50.0 | 1.877x | 2.464x |
| 6 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19,086.6 | 19,068.8 | 19,090.5 | 9.2 | 1.877x | 2.464x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-058` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 7,467.0 | 7,463.4 | 7,473.0 | 3.1 | 0.041x | 1.000x | 5 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7,467.8 | 7,467.0 | 7,477.2 | 3.8 | 0.041x | 1.000x | 5 | 100% |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 29,373.6 | 29,072.6 | 30,294.1 | 428.9 | 0.162x | 3.934x | 5 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 181,474.8 | 180,540.0 | 186,600.1 | 2,137.3 | 1.000x | 24.304x | 5 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 181,728.2 | 180,968.3 | 183,515.5 | 889.0 | 1.001x | 24.338x | 5 | 100% |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-059` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9,555.4 | 9,549.0 | 9,559.9 | 3.5 | 0.033x | 1.000x | 5 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9,564.5 | 9,558.2 | 9,580.5 | 7.9 | 0.033x | 1.001x | 5 | 100% |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 72,209.7 | 72,044.9 | 73,450.0 | 635.1 | 0.248x | 7.557x | 5 | 100% |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 290,683.7 | 289,035.8 | 293,222.9 | 1,369.0 | 0.999x | 30.421x | 5 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 290,975.4 | 289,240.3 | 291,726.3 | 875.3 | 1.000x | 30.451x | 5 | 100% |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-060` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19,057.2 | 19,042.2 | 19,174.6 | 48.8 | 0.022x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 19,060.8 | 19,052.8 | 19,100.2 | 17.1 | 0.022x | 1.000x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 193,996.6 | 193,885.0 | 221,546.0 | 11,027.6 | 0.227x | 10.180x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 194,149.4 | 193,974.4 | 194,810.9 | 344.5 | 0.227x | 10.188x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 853,818.0 | 846,089.0 | 884,443.3 | 16,079.4 | 1.000x | 44.803x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 856,424.9 | 843,206.8 | 891,748.0 | 17,490.2 | 1.003x | 44.940x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-061` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 3,739.3 | 3,739.2 | 3,741.9 | 1.1 | 0.052x | 1.000x | 5 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 3,743.9 | 3,737.3 | 3,744.8 | 2.8 | 0.052x | 1.001x | 5 | 100% |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 10,953.1 | 10,931.0 | 10,972.3 | 16.5 | 0.151x | 2.929x | 5 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 72,436.0 | 71,551.3 | 73,986.6 | 791.3 | 1.000x | 19.371x | 5 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 73,033.2 | 71,908.1 | 74,142.9 | 802.6 | 1.008x | 19.531x | 5 | 100% |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-062` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.0 | 15.9 | 16.1 | 0.1 | 0.018x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.0 | 16.0 | 16.1 | 0.1 | 0.018x | 1.002x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 294.7 | 276.8 | 312.6 | 12.7 | 0.335x | 18.460x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 306.2 | 284.1 | 310.7 | 9.5 | 0.349x | 19.177x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 878.5 | 874.3 | 904.1 | 13.2 | 1.000x | 55.022x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 904.1 | 874.6 | 941.5 | 22.2 | 1.029x | 56.626x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-063` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4,790.8 | 4,789.7 | 4,928.2 | 54.8 | 0.023x | 1.000x | 5 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 4,793.7 | 4,791.2 | 4,811.2 | 7.5 | 0.023x | 1.001x | 5 | 100% |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 94,672.7 | 94,075.5 | 100,355.3 | 2,488.4 | 0.447x | 19.761x | 5 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 211,624.0 | 211,459.2 | 213,818.0 | 912.0 | 1.000x | 44.173x | 5 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 212,821.7 | 211,105.6 | 215,922.3 | 1,579.6 | 1.006x | 44.423x | 5 | 100% |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-064` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 7,650.9 | 7,649.3 | 7,675.8 | 10.1 | 0.052x | 1.000x | 5 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7,652.7 | 7,646.4 | 7,668.7 | 7.7 | 0.052x | 1.000x | 5 | 100% |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 32,744.3 | 32,653.2 | 32,878.8 | 82.4 | 0.221x | 4.280x | 5 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 148,371.8 | 148,032.4 | 149,375.9 | 456.4 | 1.000x | 19.393x | 5 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 148,600.9 | 147,906.3 | 150,185.6 | 811.3 | 1.002x | 19.423x | 5 | 100% |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-065` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.0 | 9.7 | 10.1 | 0.2 | 0.062x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.3 | 10.8 | 0.2 | 0.064x | 1.040x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 47.7 | 47.4 | 48.3 | 0.3 | 0.293x | 4.768x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 49.8 | 49.6 | 50.2 | 0.2 | 0.307x | 4.982x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 162.5 | 161.0 | 167.3 | 2.2 | 1.000x | 16.249x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 165.1 | 162.0 | 168.9 | 2.4 | 1.016x | 16.504x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-065` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 21.2 | 21.0 | 21.8 | 0.3 | 0.013x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 21.2 | 21.1 | 21.3 | 0.1 | 0.013x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 141.8 | 141.4 | 142.5 | 0.4 | 0.088x | 6.687x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 1,201.5 | 1,176.5 | 1,272.7 | 38.6 | 0.743x | 56.672x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 1,240.8 | 1,115.7 | 1,288.0 | 60.3 | 0.767x | 58.523x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,616.9 | 1,602.1 | 1,626.3 | 7.8 | 1.000x | 76.261x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-066` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33.8 | 33.7 | 33.8 | 0.0 | 0.032x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 36.0 | 35.8 | 36.4 | 0.2 | 0.034x | 1.067x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 200.1 | 198.9 | 200.3 | 0.5 | 0.187x | 5.928x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 201.9 | 201.2 | 202.8 | 0.5 | 0.189x | 5.982x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,067.2 | 1,057.1 | 1,077.7 | 6.5 | 1.000x | 31.620x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,071.4 | 1,055.1 | 1,089.6 | 11.0 | 1.004x | 31.744x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-066` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 62.6 | 62.3 | 63.2 | 0.3 | 0.059x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 65.5 | 65.3 | 65.9 | 0.2 | 0.061x | 1.047x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 172.8 | 172.3 | 174.2 | 0.7 | 0.162x | 2.760x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 207.1 | 206.2 | 207.7 | 0.6 | 0.194x | 3.309x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 207.4 | 206.8 | 208.5 | 0.7 | 0.194x | 3.313x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,067.5 | 1,058.4 | 1,078.4 | 7.8 | 1.000x | 17.054x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-067` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.2 | 32.1 | 32.5 | 0.1 | 0.032x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.5 | 34.4 | 34.6 | 0.1 | 0.034x | 1.071x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 171.7 | 171.2 | 173.3 | 0.7 | 0.171x | 5.335x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 175.6 | 175.5 | 178.2 | 1.0 | 0.175x | 5.457x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,003.9 | 997.4 | 1,012.1 | 4.8 | 1.000x | 31.195x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,008.2 | 1,001.2 | 1,021.6 | 6.7 | 1.004x | 31.330x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-067` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 58.2 | 58.2 | 58.5 | 0.1 | 0.058x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 62.7 | 62.6 | 63.4 | 0.3 | 0.062x | 1.076x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 159.6 | 157.9 | 160.8 | 1.1 | 0.158x | 2.741x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 170.2 | 169.6 | 174.8 | 1.9 | 0.168x | 2.922x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 171.0 | 170.6 | 171.3 | 0.2 | 0.169x | 2.936x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,010.9 | 1,002.4 | 1,013.2 | 3.8 | 1.000x | 17.355x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-068` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.6 | 16.6 | 16.6 | 0.0 | 0.024x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.9 | 18.8 | 19.1 | 0.1 | 0.028x | 1.139x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 76.1 | 75.9 | 77.1 | 0.4 | 0.112x | 4.583x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 77.6 | 77.5 | 77.7 | 0.1 | 0.114x | 4.673x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 682.0 | 681.3 | 690.2 | 3.5 | 1.000x | 41.087x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 687.9 | 678.3 | 702.4 | 8.7 | 1.009x | 41.446x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-068` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 23.1 | 22.9 | 23.5 | 0.2 | 0.034x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 25.8 | 25.5 | 26.0 | 0.2 | 0.038x | 1.115x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 82.1 | 82.1 | 82.3 | 0.1 | 0.120x | 3.546x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 83.5 | 83.4 | 84.0 | 0.2 | 0.122x | 3.609x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 104.1 | 103.7 | 109.3 | 2.1 | 0.152x | 4.499x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 684.2 | 681.2 | 690.1 | 2.9 | 1.000x | 29.562x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-069` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.2 | 12.0 | 14.5 | 1.0 | 0.019x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.7 | 12.2 | 13.2 | 0.3 | 0.020x | 1.046x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 145.3 | 144.7 | 146.8 | 0.9 | 0.228x | 11.942x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 147.8 | 146.7 | 151.4 | 1.8 | 0.232x | 12.145x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 636.6 | 633.0 | 642.3 | 3.2 | 1.000x | 52.317x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 637.4 | 630.9 | 663.8 | 12.7 | 1.001x | 52.386x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-069` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 27.0 | 27.0 | 27.4 | 0.2 | 0.012x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 27.2 | 27.1 | 27.8 | 0.3 | 0.012x | 1.005x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 203.3 | 203.3 | 204.7 | 0.5 | 0.091x | 7.519x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 1,476.7 | 1,335.8 | 1,542.6 | 73.3 | 0.660x | 54.606x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 1,519.2 | 1,435.5 | 1,582.4 | 54.6 | 0.679x | 56.177x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,235.9 | 2,223.6 | 2,246.5 | 7.9 | 1.000x | 82.680x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-070` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 27.8 | 27.8 | 28.0 | 0.1 | 0.033x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 30.1 | 30.0 | 36.1 | 2.4 | 0.035x | 1.082x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 141.6 | 140.8 | 142.0 | 0.4 | 0.166x | 5.088x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 142.6 | 141.9 | 143.2 | 0.5 | 0.167x | 5.125x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 853.5 | 845.8 | 870.3 | 9.2 | 1.000x | 30.673x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 865.2 | 846.2 | 884.5 | 13.0 | 1.014x | 31.095x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-070` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 48.3 | 48.1 | 49.7 | 0.6 | 0.057x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 51.7 | 51.7 | 51.7 | 0.0 | 0.061x | 1.069x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 140.0 | 139.8 | 141.5 | 0.6 | 0.165x | 2.895x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 142.0 | 141.4 | 150.2 | 3.4 | 0.167x | 2.937x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 147.8 | 147.4 | 148.8 | 0.5 | 0.174x | 3.058x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 849.3 | 843.4 | 854.4 | 3.7 | 1.000x | 17.568x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-071` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 55.6 | 55.5 | 55.8 | 0.1 | 0.064x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 59.6 | 59.5 | 59.7 | 0.1 | 0.069x | 1.072x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 158.2 | 157.8 | 158.7 | 0.3 | 0.182x | 2.847x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 158.2 | 157.7 | 162.4 | 1.8 | 0.182x | 2.847x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 868.6 | 857.3 | 873.0 | 5.5 | 1.000x | 15.631x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 876.1 | 864.3 | 890.4 | 9.6 | 1.009x | 15.766x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-071` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 109.4 | 109.4 | 109.5 | 0.0 | 0.124x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 112.8 | 112.5 | 114.2 | 0.6 | 0.128x | 1.031x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 156.1 | 155.7 | 157.9 | 0.8 | 0.178x | 1.427x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 157.4 | 156.5 | 157.9 | 0.5 | 0.179x | 1.439x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 164.7 | 163.8 | 165.8 | 0.8 | 0.187x | 1.506x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 878.9 | 868.1 | 887.8 | 6.4 | 1.000x | 8.033x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-072` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 42.6 | 42.5 | 43.7 | 0.4 | 0.019x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 42.7 | 42.6 | 42.8 | 0.1 | 0.019x | 1.003x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 735.9 | 728.0 | 740.2 | 4.4 | 0.332x | 17.266x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 1,053.4 | 1,021.4 | 1,078.4 | 20.4 | 0.475x | 24.715x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,218.2 | 2,206.5 | 2,255.4 | 18.6 | 1.000x | 52.043x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,232.4 | 2,215.9 | 2,275.5 | 21.7 | 1.006x | 52.375x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-072` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 89.3 | 88.8 | 89.6 | 0.3 | 0.029x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 93.3 | 93.1 | 97.6 | 1.7 | 0.030x | 1.044x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 407.1 | 404.3 | 409.5 | 1.8 | 0.131x | 4.557x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 917.6 | 851.7 | 920.3 | 26.3 | 0.295x | 10.269x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 1,230.7 | 1,206.9 | 1,246.4 | 15.1 | 0.395x | 13.774x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,113.9 | 3,110.2 | 3,161.3 | 19.7 | 1.000x | 34.851x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-073` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.2 | 0.1 | 0.017x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.3 | 0.1 | 0.017x | 1.007x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 146.7 | 144.4 | 146.9 | 1.0 | 0.186x | 11.147x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 148.1 | 146.6 | 151.5 | 1.8 | 0.188x | 11.254x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 785.4 | 771.4 | 828.1 | 22.0 | 0.997x | 59.681x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 788.1 | 778.9 | 798.9 | 6.6 | 1.000x | 59.886x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-073` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 20.5 | 20.4 | 21.0 | 0.2 | 0.008x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 20.5 | 20.5 | 20.6 | 0.0 | 0.008x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 220.4 | 214.6 | 221.5 | 2.5 | 0.082x | 10.775x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 872.0 | 733.4 | 949.2 | 70.5 | 0.324x | 42.627x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 877.4 | 805.3 | 918.6 | 46.4 | 0.326x | 42.888x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,690.5 | 2,676.0 | 2,708.5 | 11.1 | 1.000x | 131.518x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-074` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.1 | 16.6 | 1.4 | 0.017x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.5 | 0.1 | 0.017x | 1.005x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 189.8 | 188.3 | 199.6 | 4.4 | 0.240x | 14.418x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 193.7 | 178.8 | 194.4 | 6.0 | 0.245x | 14.717x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 785.2 | 770.6 | 814.9 | 16.0 | 0.995x | 59.656x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 789.2 | 782.2 | 798.4 | 5.9 | 1.000x | 59.960x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-074` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 26.7 | 26.6 | 26.8 | 0.1 | 0.010x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 26.9 | 26.6 | 26.9 | 0.1 | 0.010x | 1.009x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 231.5 | 226.5 | 238.2 | 3.8 | 0.087x | 8.680x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 1,173.1 | 1,142.9 | 1,305.6 | 68.5 | 0.440x | 43.984x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 1,236.6 | 1,088.7 | 1,290.3 | 86.7 | 0.463x | 46.365x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,669.1 | 2,648.7 | 2,691.8 | 13.7 | 1.000x | 100.077x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-075` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.2 | 32.1 | 32.3 | 0.1 | 0.031x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.5 | 34.3 | 37.4 | 1.2 | 0.033x | 1.073x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 177.3 | 177.3 | 177.4 | 0.0 | 0.171x | 5.514x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 179.9 | 179.9 | 184.3 | 1.7 | 0.174x | 5.597x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,036.7 | 1,021.5 | 1,039.9 | 6.7 | 1.000x | 32.244x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,046.2 | 1,036.9 | 1,062.5 | 8.3 | 1.009x | 32.541x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-075` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 58.3 | 58.3 | 58.4 | 0.0 | 0.056x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 62.7 | 62.5 | 63.2 | 0.3 | 0.060x | 1.076x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 108.0 | 106.9 | 109.0 | 0.9 | 0.104x | 1.853x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 176.3 | 176.0 | 178.0 | 0.7 | 0.170x | 3.025x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 176.8 | 175.2 | 180.7 | 1.8 | 0.171x | 3.033x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,036.4 | 1,021.5 | 1,048.5 | 8.7 | 1.000x | 17.779x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-076` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.1 | 32.0 | 32.5 | 0.2 | 0.031x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.6 | 34.3 | 35.2 | 0.3 | 0.033x | 1.079x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 177.3 | 175.7 | 177.4 | 0.7 | 0.171x | 5.524x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 179.9 | 179.5 | 180.5 | 0.3 | 0.174x | 5.605x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,034.7 | 1,018.8 | 1,040.0 | 7.5 | 1.000x | 32.238x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,049.6 | 1,042.0 | 1,060.1 | 6.3 | 1.014x | 32.702x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-076` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 58.2 | 58.1 | 58.6 | 0.2 | 0.056x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 62.6 | 62.5 | 62.7 | 0.1 | 0.061x | 1.076x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 107.7 | 106.4 | 111.5 | 1.9 | 0.104x | 1.852x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 176.0 | 176.0 | 177.8 | 0.7 | 0.171x | 3.026x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 176.9 | 176.8 | 176.9 | 0.0 | 0.171x | 3.040x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,031.5 | 1,018.0 | 1,043.8 | 8.3 | 1.000x | 17.731x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-077` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.1 | 32.1 | 32.2 | 0.0 | 0.028x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.4 | 34.3 | 34.7 | 0.1 | 0.030x | 1.070x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 168.2 | 167.6 | 169.1 | 0.5 | 0.147x | 5.232x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 170.6 | 170.5 | 175.0 | 1.8 | 0.149x | 5.309x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,142.7 | 1,128.7 | 1,158.3 | 10.1 | 1.000x | 35.554x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,155.2 | 1,138.4 | 1,173.7 | 11.2 | 1.011x | 35.942x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-077` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 58.3 | 58.2 | 58.7 | 0.2 | 0.051x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 62.9 | 62.2 | 64.4 | 0.7 | 0.055x | 1.080x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 108.3 | 107.3 | 111.9 | 1.6 | 0.095x | 1.860x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 168.6 | 168.5 | 168.6 | 0.1 | 0.148x | 2.894x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 170.5 | 170.1 | 172.2 | 0.8 | 0.150x | 2.926x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,139.6 | 1,128.3 | 1,142.1 | 4.9 | 1.000x | 19.563x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-078` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.2 | 32.1 | 32.3 | 0.1 | 0.030x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.5 | 34.3 | 35.5 | 0.4 | 0.032x | 1.072x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 164.0 | 163.1 | 164.1 | 0.4 | 0.152x | 5.100x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 164.6 | 164.2 | 167.4 | 1.2 | 0.153x | 5.117x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,077.5 | 1,071.5 | 1,091.5 | 6.7 | 1.000x | 33.504x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,092.1 | 1,084.8 | 1,106.2 | 8.6 | 1.014x | 33.956x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-078` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 58.3 | 58.2 | 59.2 | 0.4 | 0.054x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 62.6 | 62.2 | 62.7 | 0.2 | 0.058x | 1.075x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 107.4 | 107.2 | 115.8 | 3.3 | 0.100x | 1.843x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 165.6 | 165.3 | 166.5 | 0.4 | 0.154x | 2.842x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 167.1 | 165.4 | 167.7 | 0.8 | 0.155x | 2.867x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,075.1 | 1,069.2 | 1,095.0 | 10.1 | 1.000x | 18.448x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-079` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.1 | 32.0 | 32.9 | 0.3 | 0.030x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.7 | 34.5 | 34.7 | 0.1 | 0.032x | 1.080x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 164.0 | 163.2 | 165.8 | 0.8 | 0.153x | 5.109x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 164.6 | 164.3 | 167.2 | 1.1 | 0.154x | 5.128x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,072.1 | 1,070.5 | 1,082.2 | 4.3 | 1.000x | 33.399x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,088.9 | 1,085.9 | 1,102.1 | 6.1 | 1.016x | 33.924x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-079` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 58.3 | 58.2 | 63.3 | 2.0 | 0.054x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 62.8 | 62.5 | 63.6 | 0.4 | 0.058x | 1.077x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 107.6 | 107.0 | 115.6 | 3.3 | 0.099x | 1.846x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 165.6 | 165.3 | 165.8 | 0.2 | 0.153x | 2.842x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 167.1 | 166.8 | 167.2 | 0.1 | 0.154x | 2.868x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,081.8 | 1,073.1 | 1,091.8 | 7.6 | 1.000x | 18.561x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-080` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.0 | 16.0 | 16.0 | 0.0 | 0.017x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.0 | 15.9 | 16.1 | 0.1 | 0.018x | 1.002x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 300.7 | 292.3 | 312.0 | 7.8 | 0.328x | 18.786x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 306.3 | 282.3 | 309.0 | 11.8 | 0.334x | 19.134x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 914.0 | 907.6 | 948.5 | 17.7 | 0.998x | 57.107x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 915.7 | 900.8 | 923.9 | 8.7 | 1.000x | 57.213x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-080` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 26.2 | 26.0 | 27.4 | 0.5 | 0.008x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 26.4 | 26.4 | 26.5 | 0.1 | 0.008x | 1.008x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 309.8 | 306.4 | 323.5 | 7.7 | 0.097x | 11.832x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 1,728.0 | 1,711.9 | 1,792.2 | 33.2 | 0.540x | 65.988x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 1,745.8 | 1,714.5 | 1,801.6 | 29.4 | 0.545x | 66.667x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,201.4 | 3,179.1 | 3,208.6 | 10.6 | 1.000x | 122.254x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-081` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.1 | 10.6 | 11.3 | 0.2 | 0.366x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 11.2 | 11.0 | 11.8 | 0.3 | 0.370x | 1.011x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.3 | 30.3 | 32.1 | 0.7 | 1.000x | 2.732x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 30.4 | 30.3 | 30.8 | 0.2 | 1.002x | 2.738x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 47.0 | 46.2 | 47.2 | 0.4 | 1.551x | 4.236x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 48.2 | 47.8 | 48.4 | 0.2 | 1.589x | 4.342x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-081` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 5.1 | 5.0 | 5.2 | 0.1 | 0.168x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 5.4 | 5.3 | 5.9 | 0.2 | 0.176x | 1.047x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.5 | 30.4 | 30.9 | 0.2 | 1.000x | 5.939x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 40.3 | 39.9 | 40.6 | 0.3 | 1.321x | 7.846x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 48.8 | 48.5 | 49.0 | 0.2 | 1.601x | 9.507x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 50.0 | 49.7 | 50.3 | 0.2 | 1.640x | 9.741x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-082` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9.9 | 9.8 | 10.0 | 0.1 | 0.326x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.6 | 10.5 | 11.4 | 0.3 | 0.351x | 1.079x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.3 | 30.3 | 32.1 | 0.7 | 1.000x | 3.070x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 30.3 | 30.3 | 30.7 | 0.2 | 1.000x | 3.070x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 46.7 | 46.4 | 47.0 | 0.2 | 1.540x | 4.729x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 48.6 | 48.3 | 49.4 | 0.4 | 1.605x | 4.927x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-082` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 6.0 | 5.9 | 6.0 | 0.0 | 0.196x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 6.0 | 5.9 | 6.0 | 0.0 | 0.196x | 1.001x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.4 | 30.4 | 30.8 | 0.1 | 1.000x | 5.112x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 40.1 | 39.9 | 40.4 | 0.2 | 1.318x | 6.740x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 65.9 | 64.9 | 66.2 | 0.5 | 2.166x | 11.074x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 67.5 | 67.0 | 68.1 | 0.4 | 2.219x | 11.345x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-083` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.3 | 11.2 | 11.5 | 0.1 | 0.334x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.1 | 11.8 | 12.1 | 0.1 | 0.356x | 1.068x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 33.9 | 33.8 | 34.6 | 0.3 | 1.000x | 2.996x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 34.7 | 33.9 | 35.3 | 0.5 | 1.025x | 3.070x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 111.7 | 108.9 | 160.8 | 20.0 | 3.297x | 9.877x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 112.9 | 111.2 | 114.0 | 1.0 | 3.333x | 9.986x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-083` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 36.3 | 35.4 | 37.3 | 0.7 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.4 | 46.3 | 46.4 | 0.0 | 1.276x | 1.276x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 72.7 | 72.3 | 72.8 | 0.2 | 2.002x | 2.002x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 73.6 | 73.5 | 73.9 | 0.1 | 2.028x | 2.028x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 2,859.4 | 2,786.6 | 2,906.5 | 44.6 | 78.745x | 78.745x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 3,005.9 | 2,938.1 | 3,193.7 | 98.0 | 82.781x | 82.781x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-084` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19.0 | 19.0 | 20.9 | 0.7 | 0.577x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 19.1 | 19.1 | 21.7 | 1.0 | 0.579x | 1.003x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 33.0 | 32.7 | 34.7 | 0.8 | 1.000x | 1.733x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 34.4 | 34.3 | 35.2 | 0.3 | 1.043x | 1.807x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 164.0 | 162.8 | 166.2 | 1.3 | 4.967x | 8.608x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 165.2 | 163.9 | 168.3 | 1.5 | 5.005x | 8.672x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `s-084` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 16.0 | 15.8 | 16.5 | 0.2 | 0.468x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 16.3 | 16.3 | 17.4 | 0.4 | 0.479x | 1.024x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 34.1 | 34.0 | 35.1 | 0.4 | 1.000x | 2.138x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.3 | 44.3 | 44.4 | 0.1 | 1.299x | 2.777x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 815.4 | 772.4 | 851.4 | 26.1 | 23.911x | 51.111x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 842.0 | 769.9 | 845.8 | 36.3 | 24.689x | 52.775x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 4,140,798.8 | 4,133,472.9 | 4,184,189.7 | 18,329.6 | 0.080x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 4,143,287.4 | 4,142,292.4 | 4,146,861.8 | 1,633.7 | 0.080x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 7,031,195.0 | 6,979,358.0 | 7,057,785.3 | 28,652.1 | 0.136x | 1.698x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 10,980,424.0 | 10,462,461.0 | 13,519,987.0 | 1,116,300.0 | 0.213x | 2.652x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11,087,724.0 | 11,009,823.0 | 11,700,627.0 | 253,607.7 | 0.215x | 2.678x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 51,615,885.8 | 51,304,264.0 | 52,022,538.5 | 284,120.8 | 1.000x | 12.465x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 18,798.8 | 18,672.9 | 18,972.7 | 113.2 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,875,632.0 | 1,874,754.4 | 1,898,357.1 | 9,297.8 | 99.774x | 99.774x |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,881,351.0 | 1,879,508.0 | 1,885,303.4 | 2,060.3 | 100.078x | 100.078x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 17,589,931.3 | 17,552,497.7 | 17,676,695.0 | 42,309.9 | 935.693x | 935.693x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 84,961,954.0 | 83,849,908.0 | 88,090,189.0 | 1,440,720.3 | 4519.536x | 4519.536x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 94,105,654.0 | 85,369,132.0 | 103,842,743.0 | 6,749,964.1 | 5005.934x | 5005.934x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 18,761.9 | 18,621.4 | 18,785.8 | 71.3 | 1.000x | 1.000x | 5 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,875,092.7 | 1,874,774.4 | 1,875,780.4 | 334.2 | 99.941x | 99.941x | 5 | 100% |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,876,063.9 | 1,874,596.9 | 1,877,846.4 | 1,060.4 | 99.993x | 99.993x | 5 | 100% |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `t-d-prose-sparse-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 3,142,816.5 | 3,132,265.9 | 3,148,231.3 | 5,362.7 | 0.007x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 3,195,106.6 | 3,191,717.9 | 3,298,983.4 | 41,691.5 | 0.007x | 1.017x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 42,743,471.0 | 42,677,077.0 | 43,235,138.3 | 205,178.3 | 0.096x | 13.600x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 98,689,631.0 | 98,026,927.0 | 104,258,018.0 | 2,671,888.6 | 0.221x | 31.402x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 99,131,190.0 | 97,790,823.0 | 119,069,229.0 | 8,149,397.4 | 0.222x | 31.542x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 447,267,822.4 | 446,157,442.5 | 452,012,100.1 | 2,246,381.8 | 1.000x | 142.314x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `t-e-prose-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 18,846.0 | 18,750.9 | 19,031.6 | 94.9 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 3,098,133.9 | 3,077,227.9 | 3,108,016.9 | 10,322.4 | 164.392x | 164.392x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 3,151,717.6 | 3,144,476.9 | 3,168,624.0 | 9,113.0 | 167.235x | 167.235x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 22,545,364.0 | 22,516,477.0 | 23,129,297.3 | 250,645.8 | 1196.294x | 1196.294x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 97,155,164.0 | 96,571,070.0 | 99,886,946.0 | 1,234,256.3 | 5155.214x | 5155.214x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 99,067,999.0 | 96,846,878.0 | 101,612,672.0 | 1,559,583.1 | 5256.712x | 5256.712x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `floor` / `s-000` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.7 | 5.6 | 5.8 | 0.1 | 0.200x | 1.022x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 6.1 | 0.1 | 0.206x | 1.055x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.3 | 0.1 | 0.358x | 1.827x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.358x | 1.831x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 29.3 | 0.3 | 1.000x | 5.109x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 29.2 | 0.2 | 1.003x | 5.124x |

### `floor` / `s-000` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.5 | 11.4 | 11.6 | 0.1 | 0.114x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.8 | 12.7 | 13.0 | 0.1 | 0.127x | 1.118x |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 19.0 | 0.3 | 0.180x | 1.589x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.5 | 18.2 | 18.6 | 0.1 | 0.183x | 1.611x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.0 | 43.7 | 44.3 | 0.2 | 0.435x | 3.830x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.2 | 68.6 | 69.6 | 0.4 | 0.685x | 6.030x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.0 | 99.7 | 105.6 | 2.1 | 1.000x | 8.803x |

### `floor` / `s-001` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.194x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.7 | 5.6 | 5.8 | 0.1 | 0.196x | 1.010x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.204x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.353x | 1.819x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.1 | 10.4 | 0.2 | 0.359x | 1.851x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 30.5 | 0.7 | 0.994x | 5.125x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 29.7 | 0.4 | 1.000x | 5.158x |

### `floor` / `s-001` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.8 | 11.8 | 12.1 | 0.1 | 0.118x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 13.9 | 13.3 | 14.0 | 0.3 | 0.139x | 1.179x |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.9 | 0.3 | 0.182x | 1.540x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.5 | 18.3 | 19.2 | 0.3 | 0.185x | 1.565x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.9 | 43.8 | 44.5 | 0.3 | 0.439x | 3.714x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.7 | 68.6 | 69.1 | 0.2 | 0.688x | 5.813x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.9 | 98.7 | 101.4 | 1.0 | 1.000x | 8.455x |

### `floor` / `s-002` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.195x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.8 | 5.6 | 5.9 | 0.1 | 0.200x | 1.025x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.205x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.3 | 0.1 | 0.357x | 1.836x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.1 | 10.4 | 0.2 | 0.359x | 1.847x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.8 | 0.1 | 0.997x | 5.121x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.3 | 0.2 | 1.000x | 5.138x |

### `floor` / `s-002` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 10.6 | 10.6 | 10.7 | 0.0 | 0.106x | 1.000x |
| 2 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.5 | 11.5 | 11.5 | 0.0 | 0.116x | 1.087x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.5 | 0.1 | 0.183x | 1.718x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.8 | 0.2 | 0.183x | 1.720x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.6 | 44.6 | 0.4 | 0.440x | 4.135x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 67.9 | 67.3 | 69.4 | 0.8 | 0.682x | 6.407x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 99.1 | 101.4 | 0.8 | 1.000x | 9.393x |

### `floor` / `s-003` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.197x | 1.002x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.207x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.360x | 1.830x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.1 | 10.5 | 0.2 | 0.364x | 1.853x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.9 | 0.2 | 1.000x | 5.089x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.1 | 1.007x | 5.125x |

### `floor` / `s-003` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 15.7 | 15.4 | 16.3 | 0.3 | 0.155x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 16.8 | 16.8 | 16.9 | 0.0 | 0.167x | 1.074x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.8 | 0.2 | 0.180x | 1.161x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.4 | 0.1 | 0.181x | 1.165x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.7 | 44.5 | 0.3 | 0.433x | 2.792x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.9 | 68.5 | 70.0 | 0.7 | 0.682x | 4.394x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 101.0 | 96.0 | 101.4 | 2.3 | 1.000x | 6.442x |

### `floor` / `s-004` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.197x | 1.004x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 6.0 | 0.0 | 0.206x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.360x | 1.834x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.0 | 10.4 | 0.2 | 0.363x | 1.850x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 32.2 | 1.4 | 1.000x | 5.101x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.3 | 29.0 | 0.3 | 1.003x | 5.115x |

### `floor` / `s-004` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.3 | 20.0 | 0.7 | 0.184x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.4 | 18.2 | 19.0 | 0.3 | 0.185x | 1.004x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 22.5 | 22.3 | 22.7 | 0.1 | 0.226x | 1.229x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 24.1 | 23.5 | 24.2 | 0.2 | 0.242x | 1.315x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.9 | 44.5 | 45.4 | 0.3 | 0.450x | 2.450x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 71.8 | 71.5 | 72.1 | 0.2 | 0.720x | 3.917x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.6 | 97.9 | 101.6 | 1.2 | 1.000x | 5.438x |

### `floor` / `s-005` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.197x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.198x | 1.005x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.207x | 1.052x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.359x | 1.824x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.1 | 10.5 | 0.2 | 0.363x | 1.846x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.8 | 0.1 | 1.000x | 5.087x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.1 | 29.1 | 0.3 | 1.008x | 5.131x |

### `floor` / `s-005` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 10.6 | 10.6 | 10.6 | 0.0 | 0.106x | 1.000x |
| 2 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.5 | 11.4 | 11.5 | 0.0 | 0.115x | 1.088x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.3 | 18.1 | 18.6 | 0.2 | 0.183x | 1.730x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.9 | 0.3 | 0.183x | 1.730x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.9 | 43.6 | 44.4 | 0.3 | 0.440x | 4.151x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 67.1 | 66.6 | 67.6 | 0.4 | 0.672x | 6.344x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.8 | 97.3 | 101.0 | 1.3 | 1.000x | 9.434x |

### `floor` / `s-006` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.8 | 5.6 | 5.9 | 0.1 | 0.202x | 1.032x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.052x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.358x | 1.823x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.1 | 10.5 | 0.2 | 0.362x | 1.845x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.4 | 28.8 | 0.1 | 1.000x | 5.097x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.2 | 0.2 | 1.003x | 5.113x |

### `floor` / `s-006` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 10.6 | 10.5 | 10.6 | 0.0 | 0.106x | 1.000x |
| 2 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.5 | 11.5 | 11.5 | 0.0 | 0.116x | 1.089x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.5 | 0.1 | 0.183x | 1.725x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.3 | 0.1 | 0.184x | 1.728x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.7 | 43.6 | 44.8 | 0.4 | 0.440x | 4.134x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 67.7 | 67.2 | 70.7 | 1.3 | 0.681x | 6.403x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.4 | 97.5 | 101.4 | 1.4 | 1.000x | 9.405x |

### `floor` / `s-007` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.8 | 0.1 | 0.197x | 1.005x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.054x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.358x | 1.828x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.1 | 10.5 | 0.2 | 0.361x | 1.846x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.7 | 0.0 | 1.000x | 5.108x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.0 | 0.1 | 1.002x | 5.119x |

### `floor` / `s-007` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 16.0 | 15.5 | 16.6 | 0.5 | 0.161x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 16.8 | 16.8 | 16.9 | 0.0 | 0.169x | 1.053x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.182x | 1.135x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.183x | 1.140x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.0 | 43.7 | 47.8 | 1.5 | 0.443x | 2.753x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.9 | 68.3 | 69.4 | 0.4 | 0.692x | 4.305x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 97.8 | 101.2 | 1.2 | 1.000x | 6.221x |

### `floor` / `s-008` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.195x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.7 | 5.6 | 5.9 | 0.1 | 0.197x | 1.009x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.053x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.5 | 0.2 | 0.357x | 1.828x |
| 5 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.357x | 1.830x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.8 | 0.1 | 1.000x | 5.117x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.0 | 0.2 | 1.000x | 5.119x |

### `floor` / `s-008` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.3 | 11.3 | 11.9 | 0.2 | 0.114x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.7 | 0.0 | 0.128x | 1.121x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.5 | 0.1 | 0.183x | 1.604x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.6 | 0.1 | 0.183x | 1.612x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.6 | 45.5 | 0.7 | 0.440x | 3.867x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.8 | 68.6 | 70.4 | 0.7 | 0.692x | 6.076x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 97.5 | 100.2 | 1.0 | 1.000x | 8.786x |

### `floor` / `s-009` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.8 | 0.1 | 0.197x | 1.004x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.207x | 1.052x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.358x | 1.824x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.1 | 10.5 | 0.2 | 0.362x | 1.845x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 29.0 | 0.2 | 1.000x | 5.094x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.3 | 28.8 | 0.2 | 1.007x | 5.128x |

### `floor` / `s-009` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.3 | 11.2 | 11.5 | 0.1 | 0.114x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.8 | 0.0 | 0.128x | 1.123x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.183x | 1.606x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 19.2 | 0.4 | 0.184x | 1.613x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.9 | 43.8 | 44.4 | 0.2 | 0.442x | 3.877x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 70.0 | 69.4 | 70.2 | 0.3 | 0.704x | 6.181x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.4 | 97.7 | 100.6 | 1.0 | 1.000x | 8.780x |

### `floor` / `s-010` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 6.1 | 0.2 | 0.197x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.197x | 1.000x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.050x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 0.359x | 1.824x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.4 | 0.1 | 0.361x | 1.836x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.9 | 0.1 | 1.000x | 5.086x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 29.3 | 0.2 | 1.006x | 5.114x |

### `floor` / `s-010` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.3 | 11.2 | 11.5 | 0.1 | 0.113x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.8 | 0.0 | 0.127x | 1.128x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.182x | 1.613x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.182x | 1.616x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.7 | 43.7 | 44.4 | 0.3 | 0.437x | 3.879x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.7 | 69.1 | 96.6 | 10.8 | 0.697x | 6.194x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.0 | 97.8 | 101.2 | 1.2 | 1.000x | 8.882x |

### `floor` / `s-011` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.197x | 1.004x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 6.0 | 0.0 | 0.206x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.358x | 1.830x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.361x | 1.844x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.6 | 28.8 | 0.1 | 1.000x | 5.104x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.7 | 0.1 | 1.002x | 5.113x |

### `floor` / `s-011` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 14.9 | 14.9 | 15.3 | 0.2 | 0.150x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 16.3 | 16.2 | 16.5 | 0.1 | 0.164x | 1.089x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.5 | 0.1 | 0.183x | 1.217x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.183x | 1.219x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.7 | 43.6 | 44.7 | 0.4 | 0.439x | 2.924x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.9 | 68.6 | 69.4 | 0.3 | 0.693x | 4.612x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 97.8 | 100.7 | 1.0 | 1.000x | 6.656x |

### `floor` / `s-012` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 6.7 | 0.4 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.8 | 0.1 | 0.197x | 1.003x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 6.2 | 0.1 | 0.207x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.358x | 1.824x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.5 | 0.1 | 0.361x | 1.843x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.9 | 0.1 | 1.000x | 5.101x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 30.5 | 0.7 | 1.007x | 5.139x |

### `floor` / `s-012` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 12.4 | 12.4 | 13.6 | 0.5 | 0.125x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 13.9 | 13.9 | 13.9 | 0.0 | 0.140x | 1.118x |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.184x | 1.468x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.184x | 1.468x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.7 | 43.6 | 44.5 | 0.4 | 0.441x | 3.521x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.7 | 68.2 | 81.7 | 5.2 | 0.694x | 5.535x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.0 | 98.1 | 101.0 | 1.1 | 1.000x | 7.978x |

### `floor` / `s-013` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.9 | 0.1 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.197x | 1.002x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.207x | 1.052x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.6 | 0.2 | 0.358x | 1.822x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.0 | 10.4 | 0.2 | 0.363x | 1.849x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.9 | 0.1 | 1.000x | 5.090x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.7 | 0.4 | 1.006x | 5.122x |

### `floor` / `s-013` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 12.4 | 12.4 | 13.6 | 0.5 | 0.125x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 13.9 | 13.9 | 13.9 | 0.0 | 0.140x | 1.119x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.183x | 1.464x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 19.0 | 0.3 | 0.184x | 1.472x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.7 | 43.6 | 44.7 | 0.4 | 0.440x | 3.522x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.4 | 68.1 | 68.9 | 0.3 | 0.689x | 5.516x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.3 | 98.0 | 100.9 | 1.1 | 1.000x | 8.004x |

### `floor` / `s-014` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.9 | 0.1 | 0.197x | 1.003x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.052x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.4 | 0.1 | 0.357x | 1.822x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.0 | 10.6 | 0.2 | 0.362x | 1.845x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.7 | 0.1 | 1.000x | 5.098x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.6 | 28.9 | 0.1 | 1.009x | 5.142x |

### `floor` / `s-014` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 10.4 | 10.1 | 11.5 | 0.6 | 0.104x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 11.5 | 11.5 | 11.5 | 0.0 | 0.115x | 1.105x |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.183x | 1.749x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.1 | 0.183x | 1.750x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.0 | 43.6 | 45.9 | 0.8 | 0.441x | 4.226x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 67.9 | 67.9 | 69.3 | 0.5 | 0.680x | 6.520x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.8 | 97.7 | 101.0 | 1.2 | 1.000x | 9.583x |

### `floor` / `s-015` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.001x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 0.358x | 1.829x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.1 | 10.5 | 0.2 | 0.364x | 1.857x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 30.3 | 0.7 | 1.000x | 5.108x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.2 | 0.2 | 1.003x | 5.123x |

### `floor` / `s-015` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.8 | 11.8 | 12.7 | 0.3 | 0.119x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 14.1 | 0.3 | 0.134x | 1.123x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.0 | 0.182x | 1.535x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.5 | 0.1 | 0.183x | 1.543x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.1 | 43.7 | 45.9 | 0.8 | 0.442x | 3.721x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.5 | 68.4 | 75.4 | 2.5 | 0.697x | 5.865x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.7 | 98.3 | 101.4 | 1.1 | 1.000x | 8.414x |

### `floor` / `s-016` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.196x | 1.004x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 0.358x | 1.831x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.0 | 10.6 | 0.2 | 0.362x | 1.849x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.8 | 0.1 | 1.000x | 5.112x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.4 | 28.8 | 0.1 | 1.001x | 5.116x |

### `floor` / `s-016` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.9 | 11.8 | 12.2 | 0.1 | 0.119x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.3 | 0.0 | 0.133x | 1.119x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.182x | 1.530x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 20.1 | 0.7 | 0.183x | 1.536x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.0 | 43.7 | 46.0 | 1.0 | 0.441x | 3.702x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.9 | 68.4 | 69.1 | 0.3 | 0.691x | 5.794x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.7 | 97.3 | 101.0 | 1.3 | 1.000x | 8.389x |

### `floor` / `s-017` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 6.1 | 0.2 | 0.196x | 1.004x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 0.358x | 1.831x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.6 | 0.2 | 0.360x | 1.838x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.3 | 0.3 | 1.000x | 5.108x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.0 | 0.1 | 1.004x | 5.129x |

### `floor` / `s-017` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 12.4 | 12.4 | 13.0 | 0.2 | 0.125x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 13.9 | 13.9 | 13.9 | 0.0 | 0.140x | 1.119x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.5 | 0.1 | 0.183x | 1.467x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.3 | 0.0 | 0.184x | 1.471x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.7 | 45.4 | 0.6 | 0.441x | 3.533x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.8 | 68.5 | 73.8 | 2.0 | 0.692x | 5.546x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.4 | 97.7 | 100.8 | 1.1 | 1.000x | 8.013x |

### `floor` / `s-018` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 6.0 | 0.2 | 0.195x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.195x | 1.002x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.205x | 1.052x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.3 | 0.1 | 0.357x | 1.830x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.5 | 0.2 | 0.359x | 1.842x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 28.9 | 0.1 | 0.999x | 5.120x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 29.4 | 0.3 | 1.000x | 5.126x |

### `floor` / `s-018` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.8 | 11.8 | 11.9 | 0.0 | 0.119x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.4 | 0.1 | 0.134x | 1.125x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.6 | 0.2 | 0.183x | 1.538x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.1 | 0.183x | 1.538x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.7 | 45.1 | 0.6 | 0.440x | 3.700x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.8 | 68.4 | 69.1 | 0.3 | 0.692x | 5.817x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.4 | 97.7 | 100.8 | 1.1 | 1.000x | 8.402x |

### `floor` / `s-019` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 6.2 | 0.2 | 0.196x | 1.001x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.053x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.5 | 0.1 | 0.359x | 1.833x |
| 5 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.359x | 1.834x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.4 | 29.0 | 0.2 | 1.000x | 5.111x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.8 | 0.1 | 1.002x | 5.121x |

### `floor` / `s-019` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 12.4 | 12.4 | 13.0 | 0.2 | 0.125x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 13.9 | 13.9 | 13.9 | 0.0 | 0.140x | 1.117x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.183x | 1.464x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.3 | 0.0 | 0.184x | 1.472x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.1 | 43.7 | 45.4 | 0.6 | 0.445x | 3.555x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.5 | 68.2 | 69.3 | 0.4 | 0.691x | 5.515x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.2 | 97.3 | 101.0 | 1.3 | 1.000x | 7.985x |

### `floor` / `s-020` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.197x | 1.003x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.207x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 0.360x | 1.832x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.5 | 0.1 | 0.362x | 1.845x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.4 | 28.9 | 0.2 | 1.000x | 5.090x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 28.7 | 0.0 | 1.005x | 5.114x |

### `floor` / `s-020` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 13.9 | 13.7 | 14.5 | 0.3 | 0.140x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 15.1 | 15.1 | 15.6 | 0.2 | 0.151x | 1.083x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.1 | 0.183x | 1.307x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.1 | 0.183x | 1.310x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.9 | 43.7 | 44.9 | 0.5 | 0.441x | 3.152x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.0 | 68.1 | 69.1 | 0.4 | 0.693x | 4.956x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.6 | 97.3 | 100.6 | 1.1 | 1.000x | 7.155x |

### `floor` / `s-021` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.9 | 0.1 | 0.196x | 1.003x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.053x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.6 | 0.2 | 0.357x | 1.826x |
| 5 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.5 | 0.1 | 0.358x | 1.830x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.4 | 28.8 | 0.1 | 1.000x | 5.111x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 29.0 | 0.1 | 1.003x | 5.124x |

### `floor` / `s-021` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.3 | 11.3 | 12.7 | 0.6 | 0.114x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.7 | 0.0 | 0.128x | 1.122x |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.4 | 0.1 | 0.183x | 1.612x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.1 | 0.183x | 1.612x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.2 | 43.8 | 49.5 | 2.2 | 0.445x | 3.910x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.9 | 68.9 | 71.6 | 0.9 | 0.703x | 6.178x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.4 | 97.6 | 101.0 | 1.2 | 1.000x | 8.787x |

### `floor` / `s-022` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.195x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.9 | 0.1 | 0.196x | 1.002x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.356x | 1.823x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.5 | 0.2 | 0.357x | 1.829x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.1 | 0.2 | 1.000x | 5.120x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.1 | 1.003x | 5.136x |

### `floor` / `s-022` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.5 | 11.3 | 12.5 | 0.4 | 0.116x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.7 | 0.0 | 0.128x | 1.105x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.1 | 0.183x | 1.582x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.1 | 18.3 | 0.1 | 0.184x | 1.590x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.9 | 43.6 | 44.5 | 0.3 | 0.443x | 3.825x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.0 | 68.7 | 69.1 | 0.1 | 0.695x | 6.004x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.2 | 98.0 | 99.9 | 0.6 | 1.000x | 8.638x |

### `floor` / `s-023` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.198x | 1.007x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.207x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.357x | 1.820x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.5 | 0.2 | 0.362x | 1.843x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.4 | 28.8 | 0.1 | 1.000x | 5.093x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.0 | 29.7 | 0.5 | 1.005x | 5.119x |

### `floor` / `s-023` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.3 | 11.3 | 11.9 | 0.2 | 0.113x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.7 | 0.0 | 0.128x | 1.127x |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.1 | 18.5 | 0.1 | 0.184x | 1.619x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.3 | 18.0 | 18.5 | 0.2 | 0.184x | 1.620x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.7 | 43.7 | 44.3 | 0.3 | 0.440x | 3.880x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.9 | 68.1 | 69.8 | 0.6 | 0.694x | 6.113x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.3 | 97.7 | 99.9 | 0.9 | 1.000x | 8.812x |

### `floor` / `s-024` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.9 | 0.1 | 0.196x | 1.002x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.356x | 1.820x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.0 | 10.6 | 0.2 | 0.357x | 1.824x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.3 | 28.7 | 0.1 | 1.000x | 5.111x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 30.0 | 0.5 | 1.003x | 5.129x |

### `floor` / `s-024` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.3 | 11.3 | 11.5 | 0.1 | 0.114x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.7 | 0.0 | 0.128x | 1.123x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.4 | 0.1 | 0.183x | 1.608x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.183x | 1.614x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.4 | 43.9 | 44.6 | 0.3 | 0.447x | 3.932x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 70.0 | 69.7 | 71.1 | 0.6 | 0.704x | 6.193x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 98.3 | 101.1 | 0.9 | 1.000x | 8.801x |

### `floor` / `s-025` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.8 | 0.1 | 0.198x | 1.006x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.207x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.3 | 0.1 | 0.359x | 1.827x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.5 | 0.2 | 0.362x | 1.841x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.8 | 0.1 | 1.000x | 5.090x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 29.0 | 0.2 | 1.008x | 5.130x |

### `floor` / `s-025` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.3 | 11.2 | 11.5 | 0.1 | 0.113x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.7 | 0.0 | 0.128x | 1.125x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.1 | 0.183x | 1.614x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 20.0 | 0.7 | 0.184x | 1.622x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.7 | 44.3 | 0.3 | 0.441x | 3.884x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.0 | 68.2 | 69.2 | 0.4 | 0.694x | 6.116x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 97.8 | 100.9 | 1.1 | 1.000x | 8.817x |

### `floor` / `s-026` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.9 | 0.1 | 0.197x | 1.005x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.051x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.358x | 1.821x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.4 | 0.1 | 0.360x | 1.832x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.8 | 0.1 | 1.000x | 5.091x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.0 | 1.005x | 5.118x |

### `floor` / `s-026` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.3 | 11.2 | 11.5 | 0.1 | 0.113x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.9 | 0.1 | 0.127x | 1.123x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.1 | 0.182x | 1.611x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 19.0 | 0.3 | 0.182x | 1.615x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.7 | 45.3 | 0.6 | 0.437x | 3.872x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.5 | 68.2 | 69.2 | 0.4 | 0.683x | 6.055x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.3 | 97.4 | 103.1 | 1.8 | 1.000x | 8.868x |

### `floor` / `s-027` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.8 | 5.6 | 5.9 | 0.1 | 0.202x | 1.032x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.054x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.357x | 1.826x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.357x | 1.827x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 31.6 | 1.2 | 1.000x | 5.111x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 28.8 | 0.1 | 1.004x | 5.130x |

### `floor` / `s-027` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.3 | 11.2 | 11.5 | 0.1 | 0.114x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.8 | 0.1 | 0.128x | 1.126x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.1 | 0.184x | 1.613x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.3 | 18.3 | 0.0 | 0.185x | 1.620x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.6 | 47.4 | 1.5 | 0.443x | 3.880x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.8 | 68.6 | 69.3 | 0.2 | 0.696x | 6.103x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 98.8 | 97.4 | 104.3 | 2.4 | 1.000x | 8.764x |

### `floor` / `s-028` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.9 | 0.1 | 0.196x | 1.002x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 6.1 | 0.1 | 0.206x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.357x | 1.824x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.2 | 0.358x | 1.826x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.6 | 29.0 | 0.1 | 1.000x | 5.103x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 28.8 | 0.1 | 1.004x | 5.124x |

### `floor` / `s-028` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.3 | 11.2 | 11.5 | 0.1 | 0.115x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.7 | 0.0 | 0.129x | 1.122x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.4 | 0.1 | 0.185x | 1.610x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.3 | 0.0 | 0.185x | 1.615x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.0 | 43.6 | 44.8 | 0.4 | 0.446x | 3.888x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.8 | 68.8 | 70.1 | 0.5 | 0.708x | 6.167x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 98.6 | 97.3 | 104.5 | 2.6 | 1.000x | 8.714x |

### `floor` / `s-029` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.1 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.197x | 1.002x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.357x | 1.819x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.5 | 0.2 | 0.361x | 1.839x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.8 | 0.1 | 1.000x | 5.098x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.9 | 0.1 | 1.005x | 5.124x |

### `floor` / `s-029` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.3 | 11.2 | 11.5 | 0.1 | 0.114x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.8 | 0.0 | 0.128x | 1.124x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.1 | 0.183x | 1.609x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.4 | 18.3 | 18.5 | 0.1 | 0.185x | 1.625x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.7 | 44.4 | 0.3 | 0.442x | 3.875x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.7 | 68.5 | 69.2 | 0.3 | 0.694x | 6.086x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.1 | 97.7 | 104.6 | 2.4 | 1.000x | 8.775x |

### `floor` / `s-030` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.7 | 5.6 | 5.7 | 0.0 | 0.197x | 1.007x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.052x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.357x | 1.821x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.5 | 0.2 | 0.361x | 1.843x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 29.1 | 0.2 | 1.000x | 5.104x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.1 | 1.006x | 5.133x |

### `floor` / `s-030` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.4 | 11.2 | 11.5 | 0.1 | 0.114x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.7 | 0.0 | 0.127x | 1.115x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.5 | 0.1 | 0.182x | 1.598x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.1 | 18.3 | 0.1 | 0.182x | 1.603x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.9 | 43.7 | 44.4 | 0.3 | 0.438x | 3.852x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 70.2 | 69.4 | 71.0 | 0.5 | 0.701x | 6.160x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.0 | 97.8 | 104.7 | 2.4 | 1.000x | 8.785x |

### `floor` / `s-031` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.197x | 1.001x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.207x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.359x | 1.826x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.0 | 10.5 | 0.2 | 0.363x | 1.847x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.9 | 0.1 | 1.000x | 5.091x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.1 | 1.008x | 5.134x |

### `floor` / `s-031` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.3 | 11.2 | 11.5 | 0.1 | 0.114x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.7 | 0.0 | 0.128x | 1.124x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.1 | 0.183x | 1.611x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.1 | 0.183x | 1.616x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.2 | 43.6 | 45.1 | 0.6 | 0.445x | 3.918x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.6 | 68.4 | 69.2 | 0.3 | 0.690x | 6.079x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.4 | 97.3 | 104.8 | 2.6 | 1.000x | 8.804x |

### `floor` / `s-032` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.197x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.197x | 1.001x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.207x | 1.054x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.359x | 1.825x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.1 | 10.5 | 0.2 | 0.364x | 1.853x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.5 | 28.5 | 29.1 | 0.2 | 1.000x | 5.088x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.9 | 0.1 | 1.007x | 5.123x |

### `floor` / `s-032` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.5 | 11.2 | 11.5 | 0.1 | 0.117x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.9 | 0.1 | 0.129x | 1.103x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.1 | 0.184x | 1.578x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.185x | 1.584x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.6 | 44.4 | 0.3 | 0.444x | 3.806x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.2 | 68.2 | 69.7 | 0.6 | 0.701x | 6.008x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 98.7 | 97.3 | 104.9 | 2.8 | 1.000x | 8.576x |

### `floor` / `s-033` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.196x | 1.002x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.052x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.357x | 1.822x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.0 | 10.5 | 0.2 | 0.362x | 1.846x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.9 | 0.1 | 1.000x | 5.107x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 29.3 | 0.2 | 1.002x | 5.119x |

### `floor` / `s-033` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.3 | 11.2 | 11.5 | 0.1 | 0.115x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.8 | 0.0 | 0.129x | 1.122x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.7 | 0.2 | 0.185x | 1.606x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.1 | 19.0 | 0.3 | 0.185x | 1.614x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.4 | 43.7 | 44.6 | 0.3 | 0.450x | 3.920x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.8 | 68.3 | 70.7 | 0.8 | 0.699x | 6.081x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 98.5 | 97.6 | 104.1 | 2.4 | 1.000x | 8.704x |

### `floor` / `s-034` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 7.5 | 0.7 | 0.193x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 6.0 | 0.1 | 0.194x | 1.005x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.204x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.5 | 0.1 | 0.354x | 1.828x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 11.4 | 0.5 | 0.356x | 1.839x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.5 | 0.3 | 0.990x | 5.121x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.0 | 28.5 | 29.4 | 0.3 | 1.000x | 5.171x |

### `floor` / `s-034` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.3 | 11.2 | 11.5 | 0.1 | 0.114x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.7 | 0.0 | 0.128x | 1.120x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.183x | 1.604x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.1 | 0.184x | 1.610x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.7 | 44.5 | 0.3 | 0.442x | 3.868x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.8 | 69.2 | 70.3 | 0.4 | 0.703x | 6.157x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.2 | 97.4 | 104.4 | 2.4 | 1.000x | 8.754x |

### `floor` / `s-035` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.195x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.8 | 0.1 | 0.196x | 1.005x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.3 | 0.1 | 0.357x | 1.830x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.5 | 0.2 | 0.360x | 1.844x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 29.4 | 0.3 | 1.000x | 5.119x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.1 | 0.2 | 1.000x | 5.120x |

### `floor` / `s-035` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.3 | 11.3 | 11.5 | 0.1 | 0.114x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.7 | 0.0 | 0.127x | 1.119x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.183x | 1.604x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.1 | 0.183x | 1.609x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.0 | 43.7 | 44.4 | 0.3 | 0.442x | 3.879x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.0 | 68.5 | 70.5 | 0.8 | 0.693x | 6.083x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.6 | 97.6 | 102.1 | 1.5 | 1.000x | 8.784x |

### `floor` / `s-036` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 6.0 | 0.1 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.9 | 0.1 | 0.197x | 1.006x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.052x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.356x | 1.819x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.5 | 0.2 | 0.361x | 1.844x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.1 | 0.2 | 1.000x | 5.109x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 28.9 | 0.2 | 1.006x | 5.138x |

### `floor` / `s-036` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.4 | 11.2 | 11.5 | 0.1 | 0.114x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.7 | 0.0 | 0.128x | 1.118x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.4 | 0.1 | 0.183x | 1.603x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.1 | 0.183x | 1.603x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.7 | 44.4 | 0.3 | 0.441x | 3.851x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.6 | 68.4 | 113.4 | 17.9 | 0.691x | 6.039x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.3 | 97.2 | 99.9 | 1.0 | 1.000x | 8.742x |

### `floor` / `s-037` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 6.9 | 0.5 | 0.195x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.9 | 0.1 | 0.195x | 1.001x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.205x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.357x | 1.834x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.5 | 0.2 | 0.359x | 1.843x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 29.4 | 0.3 | 0.997x | 5.125x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.8 | 28.9 | 0.0 | 1.000x | 5.139x |

### `floor` / `s-037` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.3 | 11.3 | 11.5 | 0.1 | 0.114x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.7 | 0.0 | 0.128x | 1.122x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.183x | 1.607x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 19.8 | 0.6 | 0.184x | 1.616x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.7 | 44.6 | 0.4 | 0.441x | 3.870x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.6 | 69.4 | 72.8 | 1.3 | 0.702x | 6.155x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.2 | 97.4 | 100.7 | 1.2 | 1.000x | 8.772x |

### `floor` / `s-038` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.195x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.8 | 0.1 | 0.196x | 1.002x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.205x | 1.052x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.3 | 0.1 | 0.357x | 1.831x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.6 | 0.2 | 0.359x | 1.838x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 28.9 | 0.1 | 1.000x | 5.123x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 29.1 | 0.1 | 1.000x | 5.123x |

### `floor` / `s-038` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.3 | 11.2 | 11.6 | 0.1 | 0.114x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.7 | 0.0 | 0.129x | 1.126x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.184x | 1.611x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.3 | 0.0 | 0.185x | 1.619x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 43.7 | 44.4 | 0.3 | 0.444x | 3.883x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.7 | 68.6 | 69.2 | 0.2 | 0.695x | 6.086x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 98.8 | 97.4 | 100.7 | 1.2 | 1.000x | 8.754x |

### `floor` / `s-039` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.197x | 1.003x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.207x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.358x | 1.825x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.1 | 10.6 | 0.2 | 0.363x | 1.852x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.4 | 29.0 | 0.2 | 1.000x | 5.097x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.2 | 0.2 | 1.005x | 5.123x |

### `floor` / `s-039` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.8 | 11.8 | 12.6 | 0.3 | 0.118x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 13.6 | 13.3 | 13.9 | 0.3 | 0.136x | 1.153x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.9 | 0.3 | 0.182x | 1.540x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.3 | 0.0 | 0.183x | 1.544x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.1 | 43.6 | 47.9 | 1.6 | 0.441x | 3.730x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.4 | 68.3 | 69.0 | 0.3 | 0.684x | 5.782x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.0 | 97.2 | 100.5 | 1.2 | 1.000x | 8.456x |

### `floor` / `s-040` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.194x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.195x | 1.005x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.204x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.3 | 0.0 | 0.355x | 1.833x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.5 | 0.2 | 0.357x | 1.844x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.8 | 28.9 | 0.0 | 0.996x | 5.142x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.0 | 28.7 | 29.1 | 0.2 | 1.000x | 5.165x |

### `floor` / `s-040` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 8.6 | 8.6 | 8.6 | 0.0 | 0.264x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 8.6 | 8.6 | 8.8 | 0.1 | 0.266x | 1.008x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 13.6 | 13.6 | 13.7 | 0.0 | 0.418x | 1.584x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 13.9 | 13.9 | 14.7 | 0.4 | 0.427x | 1.621x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.7 | 0.3 | 0.552x | 2.093x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 32.5 | 32.5 | 35.0 | 1.0 | 1.000x | 3.794x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 37.4 | 36.3 | 40.1 | 1.3 | 1.151x | 4.368x |

### `floor` / `s-041` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.9 | 0.1 | 0.065x | 1.000x |
| 2 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.068x | 1.051x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 6.2 | 6.2 | 6.2 | 0.0 | 0.071x | 1.102x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.7 | 10.6 | 10.9 | 0.1 | 0.123x | 1.901x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.7 | 10.5 | 10.9 | 0.1 | 0.124x | 1.909x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 86.8 | 86.4 | 88.4 | 0.7 | 1.000x | 15.436x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 88.7 | 86.5 | 90.1 | 1.1 | 1.021x | 15.765x |

### `floor` / `s-041` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 9.5 | 9.4 | 9.5 | 0.0 | 0.095x | 1.000x |
| 2 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.5 | 11.5 | 11.6 | 0.0 | 0.115x | 1.218x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 17.2 | 17.1 | 17.3 | 0.1 | 0.172x | 1.816x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 17.5 | 17.1 | 18.3 | 0.4 | 0.176x | 1.853x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.2 | 43.7 | 52.2 | 3.2 | 0.443x | 4.678x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 66.9 | 66.5 | 67.9 | 0.6 | 0.671x | 7.077x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.8 | 98.1 | 101.2 | 1.2 | 1.000x | 10.554x |

### `floor` / `s-042` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 6.2 | 0.2 | 0.195x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.8 | 5.6 | 6.5 | 0.3 | 0.200x | 1.026x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.204x | 1.049x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 0.357x | 1.829x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.4 | 0.2 | 0.358x | 1.836x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.8 | 0.0 | 0.996x | 5.109x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 29.1 | 0.2 | 1.000x | 5.129x |

### `floor` / `s-042` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.5 | 11.3 | 11.8 | 0.3 | 0.116x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.7 | 0.0 | 0.128x | 1.100x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 17.4 | 17.4 | 17.6 | 0.1 | 0.176x | 1.512x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 17.5 | 17.4 | 18.6 | 0.5 | 0.177x | 1.517x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.5 | 43.7 | 46.1 | 0.8 | 0.449x | 3.854x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.9 | 69.1 | 71.1 | 0.7 | 0.705x | 6.053x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.1 | 98.0 | 101.8 | 1.5 | 1.000x | 8.587x |

### `floor` / `s-043` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.195x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.8 | 0.1 | 0.196x | 1.004x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.358x | 1.829x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.1 | 10.5 | 0.2 | 0.362x | 1.853x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.9 | 0.1 | 1.000x | 5.116x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 28.8 | 0.0 | 1.001x | 5.121x |

### `floor` / `s-043` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 15.0 | 14.9 | 15.5 | 0.3 | 0.151x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 16.8 | 16.3 | 16.8 | 0.2 | 0.169x | 1.118x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.9 | 0.3 | 0.183x | 1.212x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.6 | 18.2 | 19.2 | 0.4 | 0.187x | 1.234x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.4 | 43.7 | 45.4 | 0.6 | 0.446x | 2.948x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.4 | 68.2 | 69.7 | 0.6 | 0.697x | 4.609x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 97.5 | 101.0 | 1.2 | 1.000x | 6.612x |

### `floor` / `s-044` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.197x | 1.006x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.052x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.359x | 1.832x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.5 | 0.2 | 0.361x | 1.841x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.7 | 0.1 | 1.000x | 5.099x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.8 | 28.9 | 0.1 | 1.006x | 5.130x |

### `floor` / `s-044` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.8 | 11.8 | 11.9 | 0.0 | 0.119x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.9 | 0.3 | 0.134x | 1.126x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.9 | 0.3 | 0.183x | 1.538x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 19.1 | 0.3 | 0.184x | 1.546x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.8 | 44.1 | 45.8 | 0.6 | 0.450x | 3.783x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.4 | 68.2 | 68.9 | 0.3 | 0.688x | 5.781x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 97.0 | 101.6 | 1.6 | 1.000x | 8.402x |

### `floor` / `s-045` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.194x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.8 | 0.1 | 0.194x | 1.002x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 6.0 | 0.0 | 0.204x | 1.054x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.354x | 1.827x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.5 | 0.2 | 0.358x | 1.843x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 29.0 | 0.1 | 0.996x | 5.133x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.9 | 28.5 | 29.0 | 0.2 | 1.000x | 5.155x |

### `floor` / `s-045` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.8 | 11.8 | 11.8 | 0.0 | 0.118x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 13.3 | 13.3 | 13.9 | 0.2 | 0.133x | 1.125x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.8 | 0.3 | 0.182x | 1.540x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.6 | 0.1 | 0.183x | 1.548x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.7 | 43.6 | 45.1 | 0.5 | 0.448x | 3.781x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.0 | 68.4 | 69.9 | 0.6 | 0.691x | 5.838x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.8 | 98.3 | 101.0 | 1.1 | 1.000x | 8.444x |

### `floor` / `s-046` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.8 | 0.1 | 0.197x | 1.004x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 6.0 | 0.0 | 0.207x | 1.052x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.359x | 1.829x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.5 | 0.2 | 0.360x | 1.835x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 29.0 | 0.2 | 1.000x | 5.092x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 28.9 | 0.2 | 1.006x | 5.123x |

### `floor` / `s-046` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.4 | 11.2 | 11.5 | 0.1 | 0.115x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.9 | 0.1 | 0.128x | 1.119x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.9 | 0.3 | 0.184x | 1.604x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 19.9 | 0.7 | 0.185x | 1.611x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.4 | 43.8 | 45.4 | 0.6 | 0.449x | 3.910x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.6 | 69.0 | 70.4 | 0.5 | 0.704x | 6.135x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 98.9 | 97.6 | 100.7 | 1.2 | 1.000x | 8.715x |

### `floor` / `s-047` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.196x | 1.003x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 6.2 | 0.1 | 0.206x | 1.054x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.4 | 0.1 | 0.356x | 1.820x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.5 | 0.2 | 0.359x | 1.834x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.1 | 0.2 | 1.000x | 5.111x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.7 | 28.9 | 0.1 | 1.008x | 5.153x |

### `floor` / `s-047` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.4 | 11.3 | 11.5 | 0.1 | 0.114x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.8 | 0.1 | 0.127x | 1.116x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.9 | 0.3 | 0.183x | 1.601x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.3 | 18.9 | 0.2 | 0.184x | 1.610x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.6 | 43.6 | 47.1 | 1.2 | 0.448x | 3.919x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.6 | 69.4 | 70.2 | 0.3 | 0.699x | 6.116x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.6 | 97.5 | 100.8 | 1.2 | 1.000x | 8.750x |

### `floor` / `s-048` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.9 | 0.1 | 0.196x | 1.002x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.357x | 1.826x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.5 | 0.2 | 0.360x | 1.839x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.2 | 0.3 | 1.000x | 5.110x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.1 | 0.2 | 1.003x | 5.128x |

### `floor` / `s-048` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.3 | 11.2 | 11.5 | 0.1 | 0.114x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.7 | 0.0 | 0.128x | 1.126x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.9 | 0.3 | 0.183x | 1.613x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.6 | 0.1 | 0.184x | 1.621x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.5 | 43.7 | 46.0 | 0.8 | 0.449x | 3.952x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.4 | 68.7 | 69.9 | 0.4 | 0.699x | 6.156x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.2 | 97.4 | 101.0 | 1.3 | 1.000x | 8.801x |

### `floor` / `s-049` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.7 | 5.6 | 5.8 | 0.1 | 0.198x | 1.012x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.358x | 1.831x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.5 | 0.2 | 0.361x | 1.843x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.0 | 0.2 | 1.000x | 5.111x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 28.9 | 0.1 | 1.003x | 5.125x |

### `floor` / `s-049` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 14.4 | 14.3 | 14.4 | 0.0 | 0.145x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 15.7 | 15.6 | 15.8 | 0.0 | 0.158x | 1.088x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 19.3 | 0.4 | 0.183x | 1.264x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.3 | 0.0 | 0.184x | 1.269x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.5 | 43.6 | 45.2 | 0.5 | 0.449x | 3.092x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.9 | 68.5 | 69.1 | 0.2 | 0.695x | 4.787x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.2 | 97.5 | 101.8 | 1.5 | 1.000x | 6.889x |

### `floor` / `s-050` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.7 | 5.6 | 5.8 | 0.1 | 0.197x | 1.008x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.052x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.359x | 1.832x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.6 | 0.2 | 0.359x | 1.835x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.8 | 0.1 | 1.000x | 5.107x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.0 | 0.2 | 1.002x | 5.120x |

### `floor` / `s-050` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.3 | 11.2 | 11.5 | 0.1 | 0.114x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.7 | 0.0 | 0.128x | 1.123x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.184x | 1.610x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.4 | 0.1 | 0.184x | 1.614x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.5 | 43.7 | 47.1 | 1.2 | 0.448x | 3.931x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.8 | 68.4 | 69.4 | 0.4 | 0.693x | 6.080x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.2 | 97.6 | 101.7 | 1.4 | 1.000x | 8.772x |

### `floor` / `s-051` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.8 | 5.6 | 5.9 | 0.1 | 0.204x | 1.039x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.207x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.359x | 1.827x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.4 | 0.1 | 0.362x | 1.845x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.7 | 0.1 | 1.000x | 5.095x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.2 | 28.9 | 0.2 | 1.005x | 5.123x |

### `floor` / `s-051` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 14.5 | 14.2 | 14.8 | 0.2 | 0.146x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 15.6 | 15.6 | 15.8 | 0.1 | 0.157x | 1.078x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.182x | 1.253x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.3 | 18.4 | 0.1 | 0.183x | 1.259x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.5 | 43.7 | 47.6 | 1.4 | 0.447x | 3.066x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.8 | 68.0 | 70.6 | 0.9 | 0.690x | 4.737x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.7 | 97.8 | 100.9 | 1.1 | 1.000x | 6.863x |

### `floor` / `s-052` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.195x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.7 | 5.6 | 5.9 | 0.1 | 0.196x | 1.009x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.205x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 0.356x | 1.829x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.0 | 10.5 | 0.2 | 0.360x | 1.852x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 29.0 | 0.1 | 0.996x | 5.120x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 28.9 | 0.2 | 1.000x | 5.139x |

### `floor` / `s-052` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.3 | 11.2 | 11.5 | 0.1 | 0.113x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.8 | 0.1 | 0.128x | 1.127x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.1 | 0.183x | 1.616x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.3 | 0.0 | 0.184x | 1.621x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.6 | 43.6 | 47.3 | 1.3 | 0.448x | 3.958x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.7 | 69.2 | 70.1 | 0.4 | 0.701x | 6.184x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 98.3 | 100.4 | 0.8 | 1.000x | 8.826x |

### `floor` / `s-053` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.195x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.002x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.205x | 1.052x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.357x | 1.830x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.5 | 0.2 | 0.358x | 1.834x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 28.8 | 0.0 | 0.999x | 5.119x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.9 | 0.2 | 1.000x | 5.122x |

### `floor` / `s-053` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.3 | 11.2 | 11.7 | 0.2 | 0.114x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.7 | 0.0 | 0.128x | 1.122x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.184x | 1.606x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.3 | 18.3 | 0.0 | 0.185x | 1.615x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.3 | 43.7 | 47.2 | 1.3 | 0.448x | 3.913x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.4 | 69.1 | 69.8 | 0.2 | 0.701x | 6.132x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 98.9 | 97.6 | 101.0 | 1.1 | 1.000x | 8.741x |

### `floor` / `s-054` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.8 | 0.1 | 0.197x | 1.003x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.207x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.359x | 1.825x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.5 | 0.2 | 0.362x | 1.843x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.4 | 28.9 | 0.2 | 1.000x | 5.091x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.1 | 1.008x | 5.131x |

### `floor` / `s-054` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.2 | 11.2 | 11.5 | 0.1 | 0.113x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.7 | 0.0 | 0.128x | 1.130x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.0 | 0.183x | 1.615x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.7 | 0.2 | 0.184x | 1.625x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.3 | 43.7 | 45.3 | 0.5 | 0.447x | 3.937x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.3 | 69.0 | 70.0 | 0.4 | 0.699x | 6.159x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.2 | 97.8 | 100.6 | 0.9 | 1.000x | 8.815x |

### `floor` / `s-055` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.197x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.197x | 1.001x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.207x | 1.051x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.359x | 1.825x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.6 | 0.2 | 0.362x | 1.838x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.5 | 28.5 | 29.0 | 0.2 | 1.000x | 5.079x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.8 | 0.1 | 1.005x | 5.106x |

### `floor` / `s-055` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.4 | 11.3 | 11.5 | 0.1 | 0.114x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.7 | 0.0 | 0.127x | 1.115x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.1 | 0.182x | 1.598x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 19.1 | 0.3 | 0.184x | 1.607x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.4 | 43.8 | 45.9 | 0.8 | 0.446x | 3.902x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.6 | 69.4 | 69.6 | 0.1 | 0.698x | 6.114x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.7 | 97.8 | 101.5 | 1.2 | 1.000x | 8.758x |

### `floor` / `s-056` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.7 | 5.6 | 5.9 | 0.1 | 0.197x | 1.007x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.357x | 1.822x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.2 | 10.7 | 0.2 | 0.362x | 1.848x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.6 | 28.4 | 28.7 | 0.1 | 0.999x | 5.102x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.3 | 28.7 | 0.1 | 1.000x | 5.104x |

### `floor` / `s-056` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.3 | 11.3 | 11.8 | 0.2 | 0.114x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.7 | 0.0 | 0.128x | 1.125x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.183x | 1.611x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.3 | 0.0 | 0.184x | 1.616x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.7 | 43.7 | 51.8 | 3.0 | 0.451x | 3.959x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.7 | 69.1 | 72.5 | 1.2 | 0.703x | 6.174x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.2 | 97.3 | 100.1 | 1.1 | 1.000x | 8.781x |

### `floor` / `s-057` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.195x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.9 | 0.1 | 0.195x | 1.003x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.205x | 1.053x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.2 | 0.356x | 1.825x |
| 5 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 0.357x | 1.831x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.1 | 0.999x | 5.128x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 28.9 | 0.1 | 1.000x | 5.132x |

### `floor` / `s-058` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.195x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.9 | 0.1 | 0.195x | 1.001x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.055x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.5 | 0.2 | 0.357x | 1.833x |
| 5 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 0.359x | 1.839x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.8 | 0.1 | 0.997x | 5.114x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 29.5 | 0.3 | 1.000x | 5.130x |

### `floor` / `s-059` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.7 | 5.6 | 5.8 | 0.1 | 0.197x | 1.007x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.052x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.4 | 0.1 | 0.356x | 1.819x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.5 | 0.1 | 0.358x | 1.827x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.4 | 29.1 | 0.2 | 1.000x | 5.104x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.8 | 0.1 | 1.002x | 5.114x |

### `floor` / `s-060` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.1 | 0.196x | 1.004x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.054x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.4 | 0.1 | 0.357x | 1.824x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.1 | 10.5 | 0.2 | 0.361x | 1.845x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.3 | 0.3 | 1.000x | 5.114x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 28.9 | 0.1 | 1.001x | 5.117x |

### `floor` / `s-061` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.8 | 0.1 | 0.196x | 1.002x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.356x | 1.822x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.5 | 0.2 | 0.360x | 1.841x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.0 | 0.1 | 1.000x | 5.112x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.8 | 28.9 | 0.0 | 1.005x | 5.136x |

### `floor` / `s-062` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.1 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.7 | 5.6 | 5.7 | 0.0 | 0.197x | 1.007x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.357x | 1.825x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.1 | 10.6 | 0.2 | 0.361x | 1.848x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.9 | 0.1 | 1.000x | 5.114x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.9 | 0.1 | 1.002x | 5.124x |

### `floor` / `s-063` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.195x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.196x | 1.001x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 6.1 | 0.1 | 0.207x | 1.058x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.5 | 0.1 | 0.356x | 1.823x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.6 | 0.2 | 0.360x | 1.843x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.1 | 0.2 | 1.000x | 5.116x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.7 | 28.9 | 0.1 | 1.003x | 5.133x |

### `floor` / `s-064` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.196x | 1.003x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.356x | 1.823x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.6 | 0.2 | 0.360x | 1.844x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.9 | 0.1 | 1.000x | 5.115x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.3 | 32.0 | 1.3 | 1.003x | 5.129x |

### `floor` / `s-065` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.9 | 0.1 | 0.196x | 1.001x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 0.357x | 1.826x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.1 | 11.1 | 0.4 | 0.361x | 1.846x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.1 | 0.2 | 1.000x | 5.114x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.0 | 28.8 | 0.3 | 1.002x | 5.124x |

### `floor` / `s-065` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.3 | 11.2 | 11.5 | 0.1 | 0.113x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 14.2 | 0.6 | 0.127x | 1.125x |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.3 | 0.0 | 0.183x | 1.619x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.3 | 18.1 | 18.8 | 0.2 | 0.184x | 1.624x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.7 | 44.0 | 45.4 | 0.6 | 0.448x | 3.961x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.7 | 68.4 | 69.1 | 0.3 | 0.689x | 6.092x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.8 | 97.5 | 100.6 | 1.2 | 1.000x | 8.847x |

### `floor` / `s-066` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.197x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.7 | 5.6 | 5.8 | 0.1 | 0.198x | 1.006x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.207x | 1.049x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.358x | 1.816x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.6 | 0.2 | 0.363x | 1.839x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.5 | 28.3 | 28.6 | 0.1 | 1.000x | 5.072x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.9 | 0.5 | 1.005x | 5.097x |

### `floor` / `s-066` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 12.0 | 11.8 | 12.2 | 0.1 | 0.120x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 13.9 | 13.3 | 14.1 | 0.3 | 0.139x | 1.159x |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.3 | 0.0 | 0.184x | 1.527x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.4 | 18.1 | 18.9 | 0.3 | 0.185x | 1.537x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.6 | 43.7 | 45.1 | 0.5 | 0.448x | 3.726x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.6 | 68.5 | 69.8 | 0.5 | 0.690x | 5.735x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 97.9 | 100.8 | 1.0 | 1.000x | 8.314x |

### `floor` / `s-067` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.197x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.9 | 0.1 | 0.197x | 1.000x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.207x | 1.052x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.357x | 1.814x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.5 | 0.2 | 0.361x | 1.836x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.5 | 28.5 | 28.9 | 0.2 | 1.000x | 5.080x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.4 | 29.0 | 0.2 | 1.009x | 5.128x |

### `floor` / `s-067` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.3 | 11.3 | 11.5 | 0.1 | 0.114x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.7 | 0.0 | 0.128x | 1.121x |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.3 | 18.6 | 0.1 | 0.184x | 1.617x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.4 | 0.1 | 0.185x | 1.618x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.1 | 43.8 | 47.5 | 1.3 | 0.454x | 3.980x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.1 | 68.5 | 69.8 | 0.4 | 0.695x | 6.098x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.4 | 98.4 | 100.5 | 0.9 | 1.000x | 8.771x |

### `floor` / `s-068` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.196x | 1.004x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.053x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.6 | 0.2 | 0.359x | 1.834x |
| 5 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.5 | 0.1 | 0.359x | 1.835x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.2 | 0.3 | 1.000x | 5.109x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.0 | 0.2 | 1.002x | 5.119x |

### `floor` / `s-068` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 10.5 | 10.5 | 10.6 | 0.0 | 0.105x | 1.000x |
| 2 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.5 | 11.5 | 11.5 | 0.0 | 0.115x | 1.093x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.4 | 0.1 | 0.182x | 1.728x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.1 | 19.6 | 0.5 | 0.183x | 1.736x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.9 | 43.8 | 45.7 | 0.6 | 0.449x | 4.257x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 67.6 | 67.2 | 68.8 | 0.5 | 0.677x | 6.415x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.9 | 97.9 | 101.2 | 1.2 | 1.000x | 9.482x |

### `floor` / `s-069` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.195x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.196x | 1.003x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.5 | 0.1 | 0.357x | 1.828x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.6 | 0.2 | 0.359x | 1.838x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.1 | 0.2 | 1.000x | 5.115x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.4 | 28.8 | 0.1 | 1.002x | 5.123x |

### `floor` / `s-069` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.3 | 11.3 | 11.5 | 0.1 | 0.114x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.7 | 0.0 | 0.127x | 1.120x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.5 | 0.1 | 0.183x | 1.610x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.7 | 0.2 | 0.183x | 1.610x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.6 | 43.6 | 47.0 | 1.2 | 0.447x | 3.933x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.8 | 68.3 | 69.3 | 0.3 | 0.690x | 6.072x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.7 | 97.6 | 101.3 | 1.2 | 1.000x | 8.797x |

### `floor` / `s-070` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.197x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.197x | 1.001x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.051x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.6 | 0.1 | 0.357x | 1.819x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.6 | 0.2 | 0.359x | 1.827x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.8 | 0.1 | 1.000x | 5.088x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 28.9 | 0.1 | 1.006x | 5.117x |

### `floor` / `s-070` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 10.6 | 10.5 | 10.6 | 0.0 | 0.106x | 1.000x |
| 2 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.5 | 11.5 | 11.8 | 0.1 | 0.116x | 1.092x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 20.0 | 0.7 | 0.183x | 1.725x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.1 | 0.183x | 1.728x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.9 | 43.6 | 45.0 | 0.5 | 0.450x | 4.248x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 67.2 | 67.0 | 69.0 | 0.7 | 0.674x | 6.366x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.7 | 97.4 | 101.1 | 1.3 | 1.000x | 9.444x |

### `floor` / `s-071` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.000x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.357x | 1.825x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.7 | 0.2 | 0.361x | 1.844x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.9 | 0.1 | 1.000x | 5.110x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 28.9 | 0.1 | 1.002x | 5.118x |

### `floor` / `s-071` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.182x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.4 | 0.1 | 0.183x | 1.003x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 20.9 | 20.5 | 21.4 | 0.3 | 0.209x | 1.147x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 22.1 | 22.0 | 22.2 | 0.1 | 0.221x | 1.213x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.8 | 44.6 | 52.4 | 2.8 | 0.460x | 2.522x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.9 | 69.5 | 70.1 | 0.2 | 0.701x | 3.845x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.6 | 97.1 | 101.8 | 1.6 | 1.000x | 5.482x |

### `floor` / `s-072` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.195x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.9 | 0.1 | 0.195x | 1.002x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.205x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.355x | 1.823x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.0 | 10.6 | 0.2 | 0.360x | 1.848x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.1 | 0.2 | 0.996x | 5.113x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.5 | 29.0 | 0.2 | 1.000x | 5.132x |

### `floor` / `s-072` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 16.8 | 16.6 | 16.8 | 0.1 | 0.168x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 18.0 | 18.0 | 18.0 | 0.0 | 0.181x | 1.074x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.183x | 1.084x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.1 | 18.3 | 0.1 | 0.184x | 1.090x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.8 | 43.7 | 45.4 | 0.6 | 0.450x | 2.670x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.4 | 67.8 | 69.1 | 0.5 | 0.688x | 4.081x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 97.8 | 101.8 | 1.5 | 1.000x | 5.935x |

### `floor` / `s-073` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.195x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.6 | 5.9 | 0.1 | 0.204x | 1.043x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.356x | 1.823x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.1 | 10.4 | 0.2 | 0.361x | 1.846x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 28.9 | 0.1 | 0.998x | 5.109x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.9 | 0.1 | 1.000x | 5.118x |

### `floor` / `s-073` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.3 | 11.2 | 11.5 | 0.1 | 0.114x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.9 | 0.1 | 0.128x | 1.119x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.1 | 18.1 | 18.2 | 0.0 | 0.182x | 1.600x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 20.1 | 0.8 | 0.183x | 1.609x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.7 | 44.1 | 45.1 | 0.3 | 0.449x | 3.937x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.9 | 69.6 | 70.8 | 0.4 | 0.703x | 6.162x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.4 | 98.2 | 101.2 | 1.2 | 1.000x | 8.769x |

### `floor` / `s-074` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.195x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.196x | 1.001x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.205x | 1.051x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.356x | 1.823x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.5 | 0.2 | 0.360x | 1.842x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 29.0 | 0.1 | 0.999x | 5.114x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.0 | 0.1 | 1.000x | 5.117x |

### `floor` / `s-074` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.3 | 11.2 | 11.5 | 0.1 | 0.114x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.7 | 0.0 | 0.128x | 1.126x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.184x | 1.614x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.1 | 18.8 | 0.2 | 0.184x | 1.618x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.5 | 43.7 | 49.5 | 2.1 | 0.449x | 3.944x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.9 | 68.3 | 70.0 | 0.6 | 0.694x | 6.103x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.2 | 98.0 | 102.6 | 1.6 | 1.000x | 8.791x |

### `floor` / `s-075` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.197x | 1.001x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.207x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.359x | 1.827x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.5 | 0.2 | 0.362x | 1.843x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.7 | 0.0 | 1.000x | 5.092x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.1 | 0.2 | 1.006x | 5.124x |

### `floor` / `s-075` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.3 | 11.3 | 11.5 | 0.1 | 0.113x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.9 | 0.1 | 0.128x | 1.127x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.2 | 0.0 | 0.183x | 1.613x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 19.9 | 0.6 | 0.184x | 1.624x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.5 | 43.9 | 45.6 | 0.6 | 0.447x | 3.947x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.0 | 68.1 | 69.6 | 0.6 | 0.694x | 6.125x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 97.7 | 104.7 | 2.4 | 1.000x | 8.826x |

### `floor` / `s-076` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 6.2 | 0.2 | 0.197x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.7 | 0.0 | 0.197x | 1.000x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.207x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.2 | 0.359x | 1.824x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.5 | 0.2 | 0.362x | 1.842x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.5 | 28.4 | 28.5 | 0.1 | 1.000x | 5.083x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.1 | 0.2 | 1.007x | 5.119x |

### `floor` / `s-076` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.3 | 11.3 | 11.5 | 0.1 | 0.114x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.7 | 0.0 | 0.128x | 1.120x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.4 | 0.1 | 0.183x | 1.608x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.3 | 0.0 | 0.183x | 1.610x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.8 | 43.7 | 45.7 | 0.7 | 0.450x | 3.952x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.7 | 68.2 | 69.1 | 0.3 | 0.691x | 6.062x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.5 | 97.7 | 104.6 | 2.5 | 1.000x | 8.778x |

### `floor` / `s-077` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.7 | 5.6 | 5.9 | 0.1 | 0.200x | 1.016x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.207x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.8 | 0.3 | 0.358x | 1.824x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.4 | 0.1 | 0.361x | 1.836x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.8 | 0.1 | 1.000x | 5.089x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 29.5 | 0.3 | 1.006x | 5.121x |

### `floor` / `s-077` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.3 | 11.2 | 11.5 | 0.1 | 0.113x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.7 | 0.0 | 0.128x | 1.127x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 0.183x | 1.616x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.3 | 0.0 | 0.183x | 1.619x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.7 | 43.7 | 44.8 | 0.4 | 0.449x | 3.964x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.7 | 67.8 | 69.0 | 0.4 | 0.691x | 6.093x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.4 | 97.5 | 102.5 | 1.8 | 1.000x | 8.823x |

### `floor` / `s-078` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.7 | 5.6 | 6.0 | 0.1 | 0.199x | 1.013x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.207x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.357x | 1.819x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.5 | 0.2 | 0.360x | 1.836x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 28.8 | 0.1 | 1.000x | 5.096x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.5 | 0.3 | 1.009x | 5.140x |

### `floor` / `s-078` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.3 | 11.2 | 11.5 | 0.1 | 0.114x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.8 | 0.0 | 0.128x | 1.124x |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.2 | 18.2 | 18.4 | 0.1 | 0.184x | 1.615x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.5 | 0.1 | 0.184x | 1.617x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.9 | 43.7 | 46.2 | 1.0 | 0.453x | 3.980x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.9 | 68.6 | 69.1 | 0.2 | 0.693x | 6.098x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 99.3 | 97.5 | 100.6 | 1.1 | 1.000x | 8.794x |

### `floor` / `s-079` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.195x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.9 | 0.1 | 0.196x | 1.003x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.053x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.3 | 0.1 | 0.357x | 1.826x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.5 | 0.1 | 0.360x | 1.843x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.6 | 29.1 | 0.2 | 1.000x | 5.122x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.7 | 29.0 | 0.1 | 1.001x | 5.126x |

### `floor` / `s-079` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.4 | 11.2 | 11.5 | 0.1 | 0.115x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.8 | 0.1 | 0.128x | 1.116x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.3 | 0.1 | 0.184x | 1.599x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.1 | 18.8 | 0.2 | 0.185x | 1.607x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 45.1 | 43.9 | 46.7 | 1.0 | 0.457x | 3.969x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.5 | 68.3 | 68.9 | 0.3 | 0.694x | 6.025x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 98.8 | 97.5 | 100.6 | 1.2 | 1.000x | 8.688x |

### `floor` / `s-080` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.195x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.8 | 5.6 | 5.9 | 0.1 | 0.201x | 1.032x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 6.1 | 0.1 | 0.205x | 1.054x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.4 | 0.1 | 0.355x | 1.821x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 0.358x | 1.835x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 28.9 | 0.1 | 0.998x | 5.120x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.0 | 0.2 | 1.000x | 5.131x |

### `floor` / `s-080` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.3 | 11.2 | 11.5 | 0.1 | 0.113x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12.7 | 12.7 | 12.7 | 0.0 | 0.127x | 1.122x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.2 | 18.1 | 18.9 | 0.3 | 0.181x | 1.606x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.4 | 0.1 | 0.182x | 1.615x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.7 | 43.6 | 45.3 | 0.6 | 0.445x | 3.946x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 68.6 | 68.2 | 68.9 | 0.3 | 0.684x | 6.060x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.4 | 97.7 | 100.8 | 1.3 | 1.000x | 8.866x |

### `floor` / `s-081` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.198x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.198x | 1.001x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.208x | 1.052x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.7 | 10.5 | 10.8 | 0.1 | 0.376x | 1.903x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.8 | 10.5 | 10.9 | 0.1 | 0.380x | 1.923x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.4 | 28.2 | 28.7 | 0.2 | 1.000x | 5.063x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.5 | 28.5 | 28.6 | 0.0 | 1.004x | 5.084x |

### `floor` / `s-081` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4.7 | 4.7 | 4.7 | 0.0 | 0.147x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 5.0 | 5.0 | 5.0 | 0.0 | 0.156x | 1.062x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 5.6 | 5.6 | 5.6 | 0.0 | 0.175x | 1.193x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 5.9 | 5.9 | 6.1 | 0.1 | 0.183x | 1.250x |
| 5 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 5.9 | 5.9 | 6.1 | 0.1 | 0.184x | 1.252x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 32.2 | 32.2 | 34.9 | 1.1 | 1.000x | 6.814x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 39.0 | 37.1 | 39.2 | 0.7 | 1.210x | 8.245x |

### `floor` / `s-082` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 9.7 | 9.1 | 10.2 | 0.3 | 0.099x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 10.1 | 9.7 | 11.0 | 0.4 | 0.103x | 1.041x |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.4 | 12.4 | 12.5 | 0.0 | 0.127x | 1.278x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.4 | 12.4 | 12.6 | 0.1 | 0.127x | 1.278x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 97.6 | 96.6 | 99.3 | 0.9 | 1.000x | 10.061x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 98.3 | 96.9 | 100.2 | 1.1 | 1.008x | 10.137x |
| 7 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 116.1 | 115.8 | 116.1 | 0.1 | 1.189x | 11.966x |

### `floor` / `s-082` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 9.4 | 9.4 | 9.5 | 0.0 | 0.094x | 1.000x |
| 2 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11.5 | 11.5 | 11.5 | 0.0 | 0.115x | 1.219x |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 16.9 | 16.9 | 17.0 | 0.0 | 0.168x | 1.787x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 17.0 | 16.8 | 17.1 | 0.1 | 0.169x | 1.800x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.6 | 43.7 | 45.7 | 0.7 | 0.444x | 4.716x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 66.5 | 66.4 | 67.5 | 0.4 | 0.662x | 7.035x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 100.5 | 97.7 | 101.5 | 1.4 | 1.000x | 10.632x |

### `floor` / `s-083` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.000x |
| 2 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.049x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 6.2 | 6.2 | 6.5 | 0.1 | 0.216x | 1.102x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.4 | 0.1 | 0.356x | 1.819x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.5 | 10.1 | 10.5 | 0.2 | 0.364x | 1.858x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.7 | 28.5 | 29.2 | 0.3 | 1.000x | 5.105x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 29.2 | 0.2 | 1.001x | 5.109x |

### `floor` / `s-083` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 10.3 | 9.3 | 11.2 | 0.7 | 0.306x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 10.5 | 9.8 | 11.4 | 0.6 | 0.310x | 1.015x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 17.2 | 17.2 | 17.3 | 0.0 | 0.509x | 1.664x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 33.8 | 33.7 | 34.9 | 0.5 | 1.000x | 3.272x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 39.1 | 38.5 | 44.6 | 2.3 | 1.156x | 3.782x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 41.1 | 41.1 | 43.0 | 0.7 | 1.217x | 3.982x |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 41.3 | 41.1 | 41.4 | 0.1 | 1.223x | 4.001x |

### `floor` / `s-084` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.196x | 1.000x |
| 2 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5.9 | 5.9 | 5.9 | 0.0 | 0.206x | 1.052x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 6.2 | 6.2 | 6.2 | 0.0 | 0.217x | 1.104x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.2 | 10.2 | 10.3 | 0.1 | 0.356x | 1.817x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.4 | 10.1 | 11.0 | 0.3 | 0.362x | 1.848x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28.6 | 28.5 | 29.1 | 0.2 | 1.000x | 5.101x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.8 | 28.6 | 34.3 | 2.2 | 1.005x | 5.128x |

### `floor` / `s-084` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 9.4 | 9.2 | 11.7 | 1.0 | 0.288x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 9.4 | 9.2 | 10.1 | 0.4 | 0.289x | 1.002x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 10.6 | 10.5 | 10.6 | 0.0 | 0.324x | 1.124x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 11.0 | 10.9 | 11.0 | 0.0 | 0.336x | 1.166x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 16.5 | 16.3 | 16.9 | 0.2 | 0.507x | 1.758x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 32.6 | 32.5 | 35.0 | 1.0 | 1.000x | 3.467x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 37.8 | 36.3 | 41.3 | 2.1 | 1.160x | 4.022x |

### `floor` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 761,325.9 | 760,775.6 | 762,127.3 | 573.2 | 0.212x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 817,493.5 | 812,447.9 | 828,067.7 | 5,192.8 | 0.228x | 1.074x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 855,355.9 | 849,277.8 | 865,388.1 | 5,737.1 | 0.239x | 1.124x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 880,810.7 | 879,933.4 | 886,688.7 | 2,486.9 | 0.246x | 1.157x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 881,323.3 | 879,763.5 | 885,098.8 | 2,091.5 | 0.246x | 1.158x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,728,929.7 | 1,671,641.0 | 1,736,029.1 | 27,268.7 | 0.482x | 2.271x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,585,463.7 | 3,561,821.5 | 3,642,459.6 | 36,446.1 | 1.000x | 4.709x |

### `floor` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 17,701.8 | 17,656.8 | 24,508.5 | 2,729.4 | 0.999x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,720.1 | 17,679.0 | 17,806.5 | 42.2 | 1.000x | 1.001x |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 17,761.2 | 17,677.7 | 17,787.2 | 39.0 | 1.002x | 1.003x |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 17,933.5 | 17,881.8 | 17,998.2 | 42.2 | 1.012x | 1.013x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 39,676.1 | 39,138.6 | 39,809.0 | 239.0 | 2.239x | 2.241x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 620,441.9 | 620,201.0 | 646,341.0 | 10,367.3 | 35.013x | 35.050x |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 620,919.4 | 620,063.4 | 622,247.7 | 783.3 | 35.040x | 35.077x |

### `floor` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 17,683.4 | 17,658.5 | 24,011.3 | 2,533.7 | 0.996x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 17,695.8 | 17,668.6 | 17,732.9 | 20.5 | 0.997x | 1.001x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,749.3 | 17,679.5 | 17,781.5 | 38.4 | 1.000x | 1.004x |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 18,076.5 | 17,887.1 | 18,123.6 | 85.0 | 1.018x | 1.022x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 39,337.4 | 39,223.7 | 40,015.7 | 287.4 | 2.216x | 2.225x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 620,386.8 | 619,808.7 | 660,160.9 | 15,944.8 | 34.953x | 35.083x |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 620,408.6 | 619,920.0 | 637,695.1 | 6,958.1 | 34.954x | 35.084x |

### `floor` / `t-d-prose-sparse-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 33,253.8 | 33,173.7 | 33,356.8 | 60.6 | 0.471x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 33,341.7 | 33,317.9 | 34,963.8 | 652.3 | 0.472x | 1.003x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 34,679.3 | 34,666.8 | 35,416.4 | 288.4 | 0.491x | 1.043x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 69,317.0 | 68,798.6 | 69,580.9 | 260.6 | 0.982x | 2.084x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 70,617.0 | 70,422.3 | 70,889.1 | 166.8 | 1.000x | 2.124x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 630,340.5 | 629,875.7 | 631,578.4 | 611.1 | 8.926x | 18.955x |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 632,526.5 | 629,952.0 | 642,248.1 | 4,506.6 | 8.957x | 19.021x |

### `floor` / `t-e-prose-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 17,679.2 | 17,669.1 | 17,730.8 | 22.8 | 0.996x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 17,686.1 | 17,654.2 | 22,330.1 | 1,859.0 | 0.997x | 1.000x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,747.4 | 17,718.3 | 17,791.3 | 24.5 | 1.000x | 1.004x |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 18,053.0 | 17,864.5 | 18,150.3 | 100.8 | 1.017x | 1.021x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 39,612.0 | 39,513.1 | 40,068.9 | 198.9 | 2.232x | 2.241x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 620,430.1 | 619,815.7 | 629,158.3 | 3,608.6 | 34.959x | 35.094x |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 620,977.6 | 620,088.6 | 621,144.9 | 471.7 | 34.990x | 35.125x |

### `orig` / `s-000` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.3 | 32.2 | 32.4 | 0.1 | 0.058x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.4 | 32.4 | 32.5 | 0.0 | 0.059x | 1.001x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 44.5 | 44.4 | 44.6 | 0.1 | 0.080x | 1.377x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 46.8 | 46.7 | 47.0 | 0.1 | 0.085x | 1.447x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 170.5 | 170.0 | 171.5 | 0.5 | 0.308x | 5.273x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 545.3 | 540.1 | 551.4 | 4.2 | 0.985x | 16.861x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 553.4 | 545.4 | 558.0 | 4.5 | 1.000x | 17.110x |

### `orig` / `s-000` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 58.4 | 58.3 | 58.6 | 0.1 | 0.107x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 58.5 | 58.5 | 58.8 | 0.1 | 0.107x | 1.001x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 71.6 | 71.6 | 71.9 | 0.1 | 0.131x | 1.225x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 73.4 | 73.2 | 74.2 | 0.4 | 0.134x | 1.255x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 77.3 | 77.2 | 80.5 | 1.3 | 0.141x | 1.322x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 248.2 | 247.0 | 267.0 | 7.6 | 0.453x | 4.246x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 547.5 | 539.0 | 553.7 | 5.4 | 1.000x | 9.367x |

### `orig` / `s-001` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 39.9 | 39.8 | 40.0 | 0.1 | 0.052x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 39.9 | 39.7 | 40.1 | 0.1 | 0.052x | 1.001x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 90.5 | 90.4 | 90.9 | 0.2 | 0.118x | 2.269x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 91.7 | 91.4 | 92.9 | 0.5 | 0.120x | 2.300x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 186.5 | 186.3 | 186.8 | 0.2 | 0.244x | 4.678x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 764.0 | 759.3 | 782.6 | 8.8 | 1.000x | 19.165x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 768.1 | 746.8 | 771.8 | 9.3 | 1.005x | 19.268x |

### `orig` / `s-001` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 78.0 | 77.8 | 95.7 | 7.1 | 0.102x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 78.1 | 77.8 | 82.5 | 1.8 | 0.102x | 1.001x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 92.3 | 90.4 | 106.1 | 5.7 | 0.120x | 1.183x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 92.5 | 92.2 | 94.7 | 1.1 | 0.121x | 1.186x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 93.9 | 90.6 | 95.8 | 1.8 | 0.122x | 1.204x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 318.1 | 315.5 | 341.5 | 9.8 | 0.414x | 4.076x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 767.8 | 761.8 | 780.8 | 6.9 | 1.000x | 9.838x |

### `orig` / `s-002` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 18.2 | 18.1 | 18.3 | 0.1 | 0.037x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.2 | 18.1 | 18.2 | 0.1 | 0.037x | 1.000x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 30.2 | 30.0 | 30.4 | 0.1 | 0.062x | 1.660x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 33.3 | 32.8 | 33.6 | 0.3 | 0.069x | 1.833x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 133.7 | 133.4 | 135.4 | 0.8 | 0.275x | 7.356x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 483.8 | 473.4 | 487.4 | 4.8 | 0.997x | 26.610x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 485.4 | 478.3 | 503.1 | 8.8 | 1.000x | 26.702x |

### `orig` / `s-002` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 26.0 | 25.9 | 26.2 | 0.1 | 0.054x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 26.0 | 25.9 | 27.2 | 0.5 | 0.054x | 1.003x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 55.5 | 55.5 | 55.6 | 0.0 | 0.115x | 2.137x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 56.4 | 53.7 | 57.0 | 1.2 | 0.117x | 2.173x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 64.6 | 64.2 | 68.5 | 1.7 | 0.134x | 2.487x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 192.6 | 191.4 | 193.9 | 0.9 | 0.400x | 7.414x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 481.8 | 472.6 | 490.3 | 6.4 | 1.000x | 18.551x |

### `orig` / `s-003` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 43.1 | 43.0 | 43.3 | 0.1 | 0.055x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 43.2 | 43.0 | 43.6 | 0.2 | 0.056x | 1.002x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 58.4 | 58.1 | 59.1 | 0.3 | 0.075x | 1.354x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 59.9 | 59.5 | 60.5 | 0.4 | 0.077x | 1.390x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 194.8 | 194.6 | 196.2 | 0.6 | 0.251x | 4.518x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 771.2 | 760.1 | 781.3 | 8.3 | 0.992x | 17.892x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 777.4 | 767.8 | 785.7 | 6.7 | 1.000x | 18.036x |

### `orig` / `s-003` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 83.2 | 82.9 | 83.5 | 0.2 | 0.108x | 1.000x |
| 2 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 84.2 | 83.0 | 85.0 | 0.6 | 0.109x | 1.012x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 86.4 | 86.3 | 86.6 | 0.1 | 0.112x | 1.039x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 86.8 | 86.7 | 90.1 | 1.3 | 0.112x | 1.043x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 93.6 | 92.8 | 94.2 | 0.5 | 0.121x | 1.125x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 314.7 | 313.6 | 340.8 | 10.5 | 0.408x | 3.782x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 771.5 | 770.3 | 782.3 | 4.5 | 1.000x | 9.271x |

### `orig` / `s-004` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 57.7 | 57.2 | 58.6 | 0.4 | 0.102x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 60.8 | 60.7 | 62.1 | 0.5 | 0.107x | 1.054x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 61.1 | 60.9 | 61.3 | 0.2 | 0.108x | 1.059x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 61.2 | 60.6 | 61.8 | 0.4 | 0.108x | 1.061x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 229.0 | 228.3 | 231.9 | 1.3 | 0.404x | 3.969x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 567.1 | 561.7 | 570.8 | 3.1 | 1.000x | 9.828x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 572.0 | 554.8 | 575.2 | 7.6 | 1.009x | 9.913x |

### `orig` / `s-004` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 88.5 | 87.8 | 96.6 | 3.4 | 0.156x | 1.000x |
| 2 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 89.8 | 89.6 | 89.9 | 0.1 | 0.158x | 1.014x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 92.7 | 91.1 | 94.1 | 1.1 | 0.164x | 1.047x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 120.1 | 119.9 | 120.6 | 0.2 | 0.212x | 1.357x |
| 5 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 120.5 | 120.2 | 122.0 | 0.9 | 0.213x | 1.361x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 420.4 | 418.0 | 429.1 | 3.9 | 0.742x | 4.748x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 566.7 | 561.3 | 573.1 | 4.3 | 1.000x | 6.401x |

### `orig` / `s-005` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 18.1 | 18.1 | 18.2 | 0.0 | 0.037x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.2 | 18.1 | 18.4 | 0.1 | 0.037x | 1.002x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 30.2 | 30.1 | 30.3 | 0.1 | 0.061x | 1.664x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 33.3 | 33.1 | 33.4 | 0.1 | 0.067x | 1.835x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 133.7 | 133.0 | 134.9 | 0.6 | 0.270x | 7.377x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 481.8 | 471.6 | 494.3 | 7.8 | 0.971x | 26.581x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 496.2 | 473.9 | 530.0 | 18.9 | 1.000x | 27.371x |

### `orig` / `s-005` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 26.0 | 25.9 | 26.1 | 0.1 | 0.054x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 26.1 | 26.0 | 26.1 | 0.1 | 0.054x | 1.004x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 55.5 | 55.5 | 55.6 | 0.0 | 0.116x | 2.139x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 57.0 | 55.9 | 57.0 | 0.4 | 0.119x | 2.195x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 65.2 | 63.9 | 69.5 | 2.1 | 0.136x | 2.513x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 193.5 | 192.1 | 195.9 | 1.4 | 0.403x | 7.457x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 480.6 | 473.6 | 483.7 | 3.5 | 1.000x | 18.518x |

### `orig` / `s-006` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 30.9 | 30.8 | 30.9 | 0.0 | 0.038x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 30.9 | 30.9 | 30.9 | 0.0 | 0.038x | 1.001x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 97.3 | 96.2 | 99.6 | 1.2 | 0.121x | 3.152x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 104.6 | 104.4 | 106.9 | 1.0 | 0.130x | 3.387x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 167.0 | 166.6 | 168.6 | 0.7 | 0.208x | 5.409x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 779.0 | 771.8 | 800.2 | 10.8 | 0.969x | 25.235x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 803.9 | 775.8 | 843.0 | 24.7 | 1.000x | 26.042x |

### `orig` / `s-006` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 55.6 | 55.5 | 58.3 | 1.1 | 0.070x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 55.7 | 55.4 | 56.2 | 0.3 | 0.070x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 85.2 | 84.0 | 91.2 | 3.2 | 0.108x | 1.533x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 130.9 | 129.1 | 132.1 | 1.1 | 0.165x | 2.353x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 136.6 | 135.0 | 141.8 | 2.5 | 0.172x | 2.457x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 281.4 | 280.8 | 284.5 | 1.3 | 0.355x | 5.061x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 792.6 | 778.7 | 794.9 | 5.9 | 1.000x | 14.253x |

### `orig` / `s-007` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 46.5 | 46.1 | 47.1 | 0.4 | 0.074x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 46.5 | 46.2 | 46.9 | 0.2 | 0.074x | 1.001x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 53.2 | 52.4 | 53.4 | 0.4 | 0.085x | 1.144x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 55.7 | 54.9 | 56.5 | 0.6 | 0.089x | 1.198x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 199.9 | 199.0 | 201.0 | 0.7 | 0.319x | 4.301x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 618.2 | 603.0 | 623.1 | 7.0 | 0.986x | 13.303x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 627.3 | 613.0 | 635.7 | 9.0 | 1.000x | 13.498x |

### `orig` / `s-007` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 75.7 | 75.3 | 76.0 | 0.2 | 0.122x | 1.000x |
| 2 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 78.0 | 77.0 | 79.6 | 0.8 | 0.125x | 1.031x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 91.8 | 85.6 | 96.3 | 4.1 | 0.147x | 1.213x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 91.9 | 91.8 | 93.1 | 0.5 | 0.148x | 1.214x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 91.9 | 91.8 | 91.9 | 0.0 | 0.148x | 1.214x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 324.7 | 321.0 | 353.5 | 11.9 | 0.522x | 4.291x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 622.3 | 612.9 | 629.0 | 5.5 | 1.000x | 8.226x |

### `orig` / `s-008` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 36.5 | 36.5 | 36.6 | 0.0 | 0.067x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 36.7 | 36.4 | 37.0 | 0.2 | 0.067x | 1.003x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 46.4 | 46.2 | 47.4 | 0.4 | 0.085x | 1.270x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 48.9 | 48.5 | 49.3 | 0.2 | 0.089x | 1.340x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 179.5 | 179.0 | 180.5 | 0.5 | 0.328x | 4.914x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 542.1 | 534.1 | 544.5 | 3.6 | 0.990x | 14.840x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 547.4 | 542.6 | 556.1 | 4.4 | 1.000x | 14.984x |

### `orig` / `s-008` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 69.7 | 69.6 | 69.7 | 0.0 | 0.128x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 69.7 | 69.6 | 69.7 | 0.0 | 0.128x | 1.000x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 73.5 | 73.2 | 73.8 | 0.2 | 0.135x | 1.055x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 75.3 | 75.2 | 75.6 | 0.1 | 0.138x | 1.081x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 79.3 | 78.7 | 87.4 | 3.2 | 0.146x | 1.138x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 264.6 | 262.6 | 276.1 | 4.9 | 0.487x | 3.799x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 543.7 | 538.4 | 551.3 | 4.8 | 1.000x | 7.805x |

### `orig` / `s-009` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.5 | 29.5 | 29.5 | 0.0 | 0.054x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.5 | 29.5 | 29.5 | 0.0 | 0.054x | 1.001x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 42.5 | 42.2 | 42.7 | 0.2 | 0.078x | 1.444x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 45.3 | 44.8 | 45.4 | 0.2 | 0.083x | 1.538x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 162.4 | 162.0 | 162.7 | 0.3 | 0.298x | 5.511x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 535.2 | 532.1 | 542.0 | 3.4 | 0.982x | 18.163x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 544.9 | 537.2 | 549.6 | 4.4 | 1.000x | 18.492x |

### `orig` / `s-009` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 51.4 | 51.4 | 51.5 | 0.1 | 0.095x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 51.7 | 51.5 | 52.0 | 0.2 | 0.095x | 1.004x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 69.1 | 68.9 | 77.6 | 3.4 | 0.127x | 1.343x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 70.9 | 70.6 | 71.2 | 0.2 | 0.130x | 1.378x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 75.4 | 74.6 | 83.2 | 3.2 | 0.139x | 1.465x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 236.5 | 235.0 | 271.2 | 14.0 | 0.435x | 4.597x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 543.3 | 536.2 | 544.0 | 2.9 | 1.000x | 10.560x |

### `orig` / `s-010` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.5 | 29.5 | 29.9 | 0.2 | 0.067x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.6 | 29.5 | 29.8 | 0.1 | 0.067x | 1.003x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 31.7 | 31.1 | 32.2 | 0.4 | 0.071x | 1.075x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 32.8 | 32.5 | 33.4 | 0.3 | 0.074x | 1.113x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 162.1 | 162.0 | 163.2 | 0.5 | 0.366x | 5.498x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 437.6 | 433.4 | 443.8 | 3.9 | 0.987x | 14.841x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 443.4 | 439.3 | 445.4 | 2.2 | 1.000x | 15.037x |

### `orig` / `s-010` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 36.7 | 36.2 | 37.1 | 0.3 | 0.084x | 1.000x |
| 2 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 37.6 | 37.3 | 37.8 | 0.2 | 0.086x | 1.024x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 51.6 | 51.3 | 51.7 | 0.1 | 0.118x | 1.406x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 51.7 | 51.5 | 52.0 | 0.2 | 0.119x | 1.410x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 69.4 | 67.3 | 75.8 | 2.9 | 0.159x | 1.891x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 231.3 | 231.0 | 239.5 | 3.2 | 0.531x | 6.303x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 435.5 | 431.9 | 444.6 | 5.4 | 1.000x | 11.867x |

### `orig` / `s-011` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.7 | 12.6 | 13.6 | 0.4 | 0.036x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.6 | 12.7 | 13.9 | 0.5 | 0.039x | 1.071x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 29.2 | 29.1 | 29.5 | 0.2 | 0.083x | 2.304x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 31.0 | 30.8 | 31.2 | 0.1 | 0.088x | 2.440x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 33.5 | 33.4 | 33.5 | 0.0 | 0.095x | 2.637x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 346.0 | 338.3 | 350.5 | 4.0 | 0.987x | 27.262x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 350.6 | 341.0 | 365.6 | 8.5 | 1.000x | 27.627x |

### `orig` / `s-011` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 34.6 | 34.5 | 34.7 | 0.1 | 0.020x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 34.6 | 34.4 | 34.9 | 0.2 | 0.020x | 1.001x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 59.7 | 58.9 | 70.7 | 4.5 | 0.034x | 1.728x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 141.9 | 140.3 | 146.1 | 2.6 | 0.081x | 4.104x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 313.8 | 312.7 | 314.5 | 0.8 | 0.180x | 9.078x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 317.7 | 314.9 | 320.2 | 1.8 | 0.182x | 9.192x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,745.6 | 1,732.2 | 1,776.7 | 14.9 | 1.000x | 50.502x |

### `orig` / `s-012` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.3 | 35.3 | 35.4 | 0.1 | 0.052x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.4 | 35.3 | 35.9 | 0.2 | 0.052x | 1.003x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 57.8 | 57.6 | 60.5 | 1.2 | 0.085x | 1.640x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 60.3 | 60.1 | 63.6 | 1.3 | 0.088x | 1.710x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 176.8 | 176.2 | 177.6 | 0.5 | 0.259x | 5.014x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 670.1 | 665.2 | 686.4 | 8.0 | 0.983x | 18.997x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 681.9 | 670.9 | 694.9 | 7.9 | 1.000x | 19.333x |

### `orig` / `s-012` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 65.8 | 65.6 | 70.2 | 1.8 | 0.097x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 65.8 | 65.4 | 66.2 | 0.3 | 0.098x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 82.4 | 82.3 | 89.7 | 2.8 | 0.122x | 1.253x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 90.7 | 90.1 | 91.4 | 0.5 | 0.134x | 1.380x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 92.7 | 91.2 | 93.8 | 0.9 | 0.137x | 1.410x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 255.2 | 254.2 | 266.2 | 4.6 | 0.378x | 3.880x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 674.9 | 664.4 | 691.4 | 9.9 | 1.000x | 10.264x |

### `orig` / `s-013` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.2 | 35.1 | 35.2 | 0.0 | 0.052x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.2 | 35.0 | 35.4 | 0.1 | 0.052x | 1.002x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 57.7 | 57.4 | 58.6 | 0.4 | 0.085x | 1.639x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 60.4 | 60.2 | 60.5 | 0.1 | 0.089x | 1.716x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 176.3 | 175.9 | 176.7 | 0.3 | 0.259x | 5.013x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 668.1 | 663.7 | 683.5 | 8.5 | 0.981x | 18.993x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 681.2 | 670.4 | 697.5 | 9.0 | 1.000x | 19.367x |

### `orig` / `s-013` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 65.8 | 65.7 | 65.9 | 0.1 | 0.097x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 65.8 | 65.6 | 70.3 | 1.8 | 0.097x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 82.5 | 81.9 | 87.1 | 1.9 | 0.122x | 1.254x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 89.6 | 85.1 | 91.9 | 2.3 | 0.132x | 1.362x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 90.2 | 89.5 | 92.7 | 1.1 | 0.133x | 1.372x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 258.5 | 255.3 | 303.7 | 18.6 | 0.382x | 3.930x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 676.5 | 666.1 | 691.6 | 8.5 | 1.000x | 10.288x |

### `orig` / `s-014` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.5 | 29.4 | 29.7 | 0.1 | 0.054x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.5 | 29.5 | 29.6 | 0.0 | 0.055x | 1.001x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 47.5 | 47.3 | 49.1 | 0.7 | 0.088x | 1.610x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 50.3 | 50.0 | 50.4 | 0.1 | 0.093x | 1.706x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 162.0 | 161.6 | 163.2 | 0.6 | 0.299x | 5.492x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 537.2 | 522.8 | 542.2 | 6.7 | 0.992x | 18.207x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 541.4 | 537.1 | 546.1 | 3.4 | 1.000x | 18.350x |

### `orig` / `s-014` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 51.5 | 51.3 | 56.4 | 2.0 | 0.096x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 51.5 | 51.3 | 52.9 | 0.6 | 0.096x | 1.002x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 71.1 | 70.7 | 71.8 | 0.4 | 0.133x | 1.382x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 72.8 | 72.5 | 73.3 | 0.3 | 0.136x | 1.414x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 77.0 | 76.7 | 84.8 | 3.1 | 0.144x | 1.497x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 236.6 | 235.8 | 245.8 | 3.9 | 0.443x | 4.597x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 534.4 | 529.4 | 549.7 | 7.2 | 1.000x | 10.383x |

### `orig` / `s-015` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.6 | 33.6 | 33.7 | 0.1 | 0.051x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33.7 | 33.7 | 33.7 | 0.0 | 0.051x | 1.002x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 55.0 | 55.0 | 55.7 | 0.3 | 0.084x | 1.638x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 57.8 | 57.8 | 57.8 | 0.0 | 0.088x | 1.720x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 171.6 | 170.9 | 172.1 | 0.4 | 0.262x | 5.109x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 650.4 | 645.3 | 663.3 | 6.9 | 0.994x | 19.357x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 654.3 | 652.0 | 665.4 | 5.0 | 1.000x | 19.472x |

### `orig` / `s-015` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 62.6 | 62.5 | 62.7 | 0.0 | 0.096x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 62.6 | 62.4 | 67.0 | 1.8 | 0.096x | 1.001x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 78.3 | 78.1 | 91.9 | 5.5 | 0.120x | 1.251x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 80.3 | 79.7 | 81.3 | 0.6 | 0.123x | 1.283x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 81.0 | 80.7 | 88.9 | 3.2 | 0.124x | 1.295x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 250.9 | 249.6 | 288.7 | 15.2 | 0.384x | 4.010x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 653.8 | 640.4 | 671.3 | 10.0 | 1.000x | 10.447x |

### `orig` / `s-016` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.7 | 11.2 | 11.8 | 0.2 | 0.062x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 11.8 | 11.3 | 12.6 | 0.4 | 0.062x | 1.005x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 24.7 | 24.3 | 24.9 | 0.2 | 0.130x | 2.106x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 25.7 | 25.6 | 25.8 | 0.1 | 0.136x | 2.197x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 26.0 | 25.1 | 27.2 | 0.8 | 0.137x | 2.217x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 187.0 | 185.2 | 187.3 | 0.8 | 0.987x | 15.963x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 189.5 | 185.1 | 203.3 | 6.2 | 1.000x | 16.176x |

### `orig` / `s-016` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 26.2 | 25.9 | 26.5 | 0.2 | 0.024x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 26.4 | 26.3 | 26.5 | 0.1 | 0.024x | 1.008x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 50.7 | 50.4 | 51.2 | 0.3 | 0.047x | 1.939x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 109.4 | 108.4 | 115.8 | 3.1 | 0.102x | 4.184x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 228.4 | 227.0 | 230.3 | 1.1 | 0.212x | 8.732x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 230.6 | 226.7 | 233.0 | 2.1 | 0.214x | 8.815x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,076.7 | 1,063.5 | 1,091.4 | 9.9 | 1.000x | 41.165x |

### `orig` / `s-017` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.2 | 35.0 | 35.2 | 0.1 | 0.052x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.2 | 35.1 | 35.3 | 0.1 | 0.052x | 1.001x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 57.7 | 57.7 | 59.3 | 0.6 | 0.085x | 1.641x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 60.3 | 60.3 | 60.5 | 0.1 | 0.089x | 1.716x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 175.9 | 175.6 | 176.3 | 0.2 | 0.260x | 5.001x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 668.7 | 662.3 | 676.7 | 5.4 | 0.987x | 19.009x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 677.7 | 669.4 | 685.4 | 5.1 | 1.000x | 19.267x |

### `orig` / `s-017` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 65.8 | 65.7 | 70.3 | 1.8 | 0.098x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 65.8 | 65.7 | 68.0 | 0.9 | 0.098x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 83.8 | 81.1 | 148.5 | 25.8 | 0.125x | 1.275x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 87.0 | 85.5 | 91.2 | 2.6 | 0.129x | 1.323x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 92.0 | 88.4 | 92.8 | 1.9 | 0.137x | 1.399x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 256.7 | 255.2 | 326.6 | 28.0 | 0.382x | 3.904x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 672.4 | 662.1 | 689.5 | 9.6 | 1.000x | 10.225x |

### `orig` / `s-018` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33.6 | 33.6 | 33.7 | 0.0 | 0.052x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.7 | 33.6 | 33.7 | 0.1 | 0.052x | 1.002x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 55.2 | 54.9 | 56.5 | 0.6 | 0.085x | 1.642x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 57.7 | 57.6 | 57.9 | 0.1 | 0.089x | 1.716x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 172.1 | 171.3 | 172.7 | 0.5 | 0.264x | 5.116x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 651.7 | 645.3 | 665.8 | 7.3 | 1.000x | 19.378x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 655.1 | 645.7 | 663.0 | 5.9 | 1.005x | 19.479x |

### `orig` / `s-018` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 62.6 | 62.5 | 62.6 | 0.1 | 0.096x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 62.6 | 62.5 | 67.4 | 1.9 | 0.096x | 1.000x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 78.6 | 78.2 | 90.9 | 5.0 | 0.121x | 1.256x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 80.4 | 80.0 | 81.0 | 0.3 | 0.124x | 1.285x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 82.7 | 80.5 | 141.0 | 23.2 | 0.127x | 1.322x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 251.7 | 250.0 | 268.8 | 7.2 | 0.387x | 4.023x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 650.4 | 648.0 | 670.7 | 8.2 | 1.000x | 10.397x |

### `orig` / `s-019` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.0 | 11.9 | 12.5 | 0.2 | 0.061x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.0 | 12.0 | 13.2 | 0.5 | 0.061x | 1.007x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 25.5 | 25.2 | 26.7 | 0.6 | 0.130x | 2.137x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 26.0 | 25.3 | 27.3 | 0.8 | 0.133x | 2.171x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.3 | 26.2 | 26.5 | 0.1 | 0.135x | 2.204x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 192.5 | 192.0 | 195.2 | 1.3 | 0.983x | 16.105x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 195.8 | 188.5 | 199.8 | 4.1 | 1.000x | 16.380x |

### `orig` / `s-019` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 27.6 | 27.3 | 27.9 | 0.2 | 0.025x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 27.6 | 27.4 | 27.7 | 0.1 | 0.025x | 1.000x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 52.6 | 52.5 | 62.0 | 3.8 | 0.048x | 1.907x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 111.0 | 109.4 | 119.3 | 4.4 | 0.102x | 4.020x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 238.6 | 237.3 | 240.4 | 1.2 | 0.219x | 8.645x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 239.8 | 237.9 | 240.4 | 0.9 | 0.220x | 8.687x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,088.1 | 1,080.5 | 1,101.5 | 7.7 | 1.000x | 39.416x |

### `orig` / `s-020` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 38.2 | 38.1 | 38.7 | 0.2 | 0.056x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 38.3 | 38.1 | 40.4 | 0.9 | 0.056x | 1.001x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 63.7 | 62.9 | 66.6 | 1.3 | 0.093x | 1.667x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 65.8 | 65.7 | 66.4 | 0.3 | 0.096x | 1.721x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 183.9 | 183.7 | 184.3 | 0.2 | 0.269x | 4.811x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 681.8 | 675.2 | 692.2 | 5.7 | 0.998x | 17.836x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 683.3 | 682.5 | 696.6 | 5.3 | 1.000x | 17.875x |

### `orig` / `s-020` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 72.9 | 72.8 | 73.2 | 0.1 | 0.107x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 72.9 | 72.8 | 77.3 | 1.8 | 0.107x | 1.000x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 84.9 | 84.8 | 85.6 | 0.3 | 0.125x | 1.165x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 86.3 | 84.9 | 158.3 | 28.5 | 0.127x | 1.183x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 87.6 | 87.2 | 88.1 | 0.3 | 0.128x | 1.202x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 274.5 | 273.3 | 289.8 | 6.3 | 0.402x | 3.765x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 682.0 | 679.3 | 697.0 | 6.5 | 1.000x | 9.354x |

### `orig` / `s-021` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.5 | 29.5 | 29.6 | 0.0 | 0.042x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.5 | 29.4 | 29.7 | 0.1 | 0.042x | 1.002x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 75.7 | 75.3 | 76.0 | 0.2 | 0.107x | 2.567x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 83.6 | 83.0 | 83.8 | 0.3 | 0.118x | 2.834x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 162.4 | 161.8 | 163.6 | 0.6 | 0.229x | 5.506x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 703.4 | 700.4 | 712.0 | 4.1 | 0.994x | 23.851x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 707.8 | 703.1 | 739.1 | 13.7 | 1.000x | 24.002x |

### `orig` / `s-021` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 51.5 | 51.4 | 54.5 | 1.2 | 0.073x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 51.7 | 51.4 | 52.3 | 0.3 | 0.073x | 1.003x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 61.8 | 61.2 | 67.8 | 2.5 | 0.088x | 1.200x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 62.4 | 61.2 | 66.6 | 2.0 | 0.088x | 1.212x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 90.1 | 89.9 | 97.0 | 2.8 | 0.128x | 1.750x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 233.9 | 230.8 | 253.2 | 8.3 | 0.331x | 4.543x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 705.9 | 696.9 | 709.2 | 4.9 | 1.000x | 13.707x |

### `orig` / `s-022` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 36.0 | 35.9 | 36.2 | 0.1 | 0.080x | 1.000x |
| 2 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 38.1 | 38.0 | 41.7 | 1.4 | 0.085x | 1.058x |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 41.5 | 41.4 | 41.6 | 0.1 | 0.092x | 1.153x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 41.5 | 41.5 | 41.7 | 0.1 | 0.092x | 1.153x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 190.6 | 190.2 | 191.7 | 0.5 | 0.423x | 5.287x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 445.6 | 444.5 | 451.6 | 2.8 | 0.989x | 12.365x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 450.7 | 449.8 | 465.6 | 6.0 | 1.000x | 12.505x |

### `orig` / `s-022` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 40.2 | 39.6 | 41.1 | 0.5 | 0.089x | 1.000x |
| 2 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 42.0 | 41.5 | 42.0 | 0.2 | 0.093x | 1.044x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 71.4 | 70.0 | 76.4 | 2.3 | 0.158x | 1.775x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 80.6 | 80.5 | 80.6 | 0.0 | 0.179x | 2.002x |
| 5 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 80.6 | 80.4 | 80.7 | 0.1 | 0.179x | 2.003x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 280.1 | 278.7 | 289.8 | 4.0 | 0.621x | 6.959x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 450.8 | 443.3 | 454.7 | 4.0 | 1.000x | 11.203x |

### `orig` / `s-023` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.1 | 35.1 | 35.2 | 0.0 | 0.052x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.2 | 35.1 | 35.3 | 0.1 | 0.052x | 1.001x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 77.8 | 77.6 | 78.6 | 0.4 | 0.116x | 2.213x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 85.6 | 85.4 | 86.1 | 0.3 | 0.127x | 2.437x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 176.7 | 175.4 | 185.8 | 3.8 | 0.263x | 5.027x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 670.2 | 665.6 | 674.6 | 2.9 | 0.997x | 19.067x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 672.0 | 670.1 | 688.4 | 7.8 | 1.000x | 19.119x |

### `orig` / `s-023` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 65.7 | 65.7 | 66.0 | 0.1 | 0.099x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 65.8 | 65.7 | 68.0 | 0.9 | 0.099x | 1.001x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 67.5 | 61.4 | 70.8 | 3.6 | 0.101x | 1.026x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 70.6 | 62.4 | 72.5 | 3.7 | 0.106x | 1.074x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 83.5 | 82.8 | 90.7 | 3.0 | 0.125x | 1.271x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 253.6 | 252.5 | 259.3 | 2.5 | 0.380x | 3.857x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 667.2 | 661.9 | 675.6 | 4.7 | 1.000x | 10.148x |

### `orig` / `s-024` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.5 | 29.4 | 29.5 | 0.0 | 0.041x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 29.5 | 29.5 | 29.5 | 0.0 | 0.041x | 1.001x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 78.1 | 77.7 | 78.9 | 0.4 | 0.108x | 2.651x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 86.3 | 85.9 | 86.4 | 0.2 | 0.120x | 2.930x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 162.2 | 161.7 | 188.9 | 10.8 | 0.225x | 5.506x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 707.6 | 701.3 | 713.3 | 4.4 | 0.981x | 24.025x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 721.4 | 714.7 | 742.4 | 9.8 | 1.000x | 24.493x |

### `orig` / `s-024` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 51.5 | 51.1 | 51.5 | 0.1 | 0.073x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 51.6 | 51.5 | 51.7 | 0.1 | 0.073x | 1.004x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 72.5 | 66.1 | 73.5 | 3.4 | 0.102x | 1.409x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 87.7 | 86.9 | 89.1 | 0.9 | 0.124x | 1.704x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 89.7 | 89.1 | 96.3 | 2.8 | 0.127x | 1.744x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 231.6 | 231.1 | 232.8 | 0.7 | 0.327x | 4.501x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 708.0 | 703.5 | 720.2 | 5.7 | 1.000x | 13.759x |

### `orig` / `s-025` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.2 | 35.1 | 35.2 | 0.0 | 0.047x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 35.3 | 35.0 | 35.4 | 0.2 | 0.047x | 1.003x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 78.9 | 78.3 | 79.8 | 0.5 | 0.106x | 2.245x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 87.4 | 86.7 | 88.6 | 0.6 | 0.118x | 2.485x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 176.0 | 175.7 | 177.2 | 0.6 | 0.237x | 5.005x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 724.6 | 722.5 | 733.9 | 4.3 | 0.974x | 20.603x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 743.6 | 727.3 | 750.5 | 7.9 | 1.000x | 21.143x |

### `orig` / `s-025` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 65.8 | 65.6 | 70.7 | 2.0 | 0.090x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 65.8 | 65.6 | 65.8 | 0.1 | 0.090x | 1.000x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 66.5 | 65.7 | 66.6 | 0.4 | 0.091x | 1.011x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 82.6 | 82.4 | 88.4 | 2.3 | 0.113x | 1.256x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 84.1 | 83.9 | 100.7 | 6.6 | 0.115x | 1.279x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 255.3 | 253.6 | 255.8 | 0.8 | 0.350x | 3.882x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 730.1 | 725.0 | 734.2 | 2.9 | 1.000x | 11.103x |

### `orig` / `s-026` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 35.9 | 35.8 | 36.3 | 0.2 | 0.079x | 1.000x |
| 2 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 38.1 | 38.0 | 38.2 | 0.1 | 0.084x | 1.061x |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 41.5 | 41.3 | 43.3 | 0.7 | 0.092x | 1.158x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 41.6 | 41.3 | 41.7 | 0.2 | 0.092x | 1.160x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 190.4 | 190.3 | 191.5 | 0.5 | 0.422x | 5.306x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 446.8 | 442.5 | 453.2 | 3.7 | 0.989x | 12.449x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 451.7 | 445.1 | 464.8 | 7.0 | 1.000x | 12.584x |

### `orig` / `s-026` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 40.3 | 40.0 | 41.6 | 0.6 | 0.090x | 1.000x |
| 2 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 41.7 | 41.5 | 42.2 | 0.3 | 0.093x | 1.034x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 71.2 | 69.9 | 77.1 | 2.7 | 0.159x | 1.767x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 80.6 | 80.5 | 80.6 | 0.0 | 0.180x | 1.999x |
| 5 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 80.6 | 80.5 | 84.2 | 1.4 | 0.180x | 1.999x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 280.8 | 278.9 | 288.5 | 3.5 | 0.628x | 6.966x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 446.9 | 443.5 | 455.2 | 3.9 | 1.000x | 11.088x |

### `orig` / `s-027` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 41.4 | 41.4 | 41.7 | 0.1 | 0.065x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 41.5 | 41.4 | 42.6 | 0.4 | 0.065x | 1.004x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 77.4 | 77.3 | 77.9 | 0.2 | 0.121x | 1.870x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 83.4 | 82.9 | 83.7 | 0.2 | 0.130x | 2.015x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 190.4 | 190.0 | 196.9 | 2.6 | 0.297x | 4.600x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 628.6 | 623.0 | 637.1 | 4.7 | 0.981x | 15.191x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 640.5 | 626.2 | 654.9 | 10.7 | 1.000x | 15.479x |

### `orig` / `s-027` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 61.8 | 61.5 | 62.5 | 0.3 | 0.098x | 1.000x |
| 2 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 63.3 | 63.0 | 64.2 | 0.4 | 0.100x | 1.024x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 80.6 | 80.5 | 80.8 | 0.1 | 0.127x | 1.303x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 80.6 | 80.1 | 80.9 | 0.3 | 0.127x | 1.304x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 81.5 | 81.3 | 90.8 | 3.7 | 0.128x | 1.317x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 280.4 | 278.5 | 285.4 | 2.5 | 0.442x | 4.534x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 633.9 | 625.9 | 639.5 | 4.6 | 1.000x | 10.252x |

### `orig` / `s-028` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.3 | 0.1 | 0.044x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.7 | 0.2 | 0.044x | 1.008x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 31.0 | 30.9 | 32.1 | 0.5 | 0.102x | 2.347x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 33.6 | 32.6 | 49.5 | 6.4 | 0.111x | 2.547x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 35.3 | 34.6 | 35.4 | 0.3 | 0.117x | 2.673x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 295.7 | 292.9 | 302.4 | 3.4 | 0.977x | 22.405x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 302.6 | 295.3 | 322.3 | 9.6 | 1.000x | 22.929x |

### `orig` / `s-028` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 22.3 | 22.1 | 22.8 | 0.3 | 0.021x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 22.3 | 22.2 | 22.9 | 0.3 | 0.021x | 1.003x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 45.7 | 45.6 | 46.4 | 0.3 | 0.043x | 2.052x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 69.0 | 67.5 | 76.8 | 3.3 | 0.064x | 3.094x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 255.3 | 252.8 | 259.2 | 2.3 | 0.238x | 11.456x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 255.6 | 252.5 | 258.2 | 2.0 | 0.238x | 11.470x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,073.1 | 1,066.8 | 1,085.8 | 7.1 | 1.000x | 48.152x |

### `orig` / `s-029` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.2 | 0.0 | 0.044x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 0.044x | 1.007x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 31.0 | 30.8 | 31.1 | 0.1 | 0.103x | 2.351x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 32.6 | 32.6 | 33.4 | 0.3 | 0.108x | 2.475x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 34.8 | 34.8 | 35.1 | 0.1 | 0.115x | 2.645x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 295.8 | 294.8 | 299.7 | 1.8 | 0.980x | 22.457x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 301.8 | 296.3 | 316.5 | 7.4 | 1.000x | 22.914x |

### `orig` / `s-029` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 45.3 | 45.3 | 45.6 | 0.1 | 0.042x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 45.5 | 45.4 | 45.6 | 0.1 | 0.043x | 1.003x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 69.2 | 69.1 | 73.7 | 1.8 | 0.065x | 1.527x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 71.9 | 70.2 | 77.6 | 2.6 | 0.067x | 1.587x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 531.8 | 528.9 | 533.2 | 1.4 | 0.499x | 11.733x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 533.0 | 531.4 | 539.2 | 2.7 | 0.500x | 11.759x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,066.4 | 1,062.8 | 1,089.0 | 9.6 | 1.000x | 23.530x |

### `orig` / `s-030` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.2 | 0.0 | 0.044x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.4 | 0.0 | 0.044x | 1.005x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 30.9 | 30.9 | 31.2 | 0.1 | 0.103x | 2.338x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 32.8 | 32.6 | 33.5 | 0.3 | 0.109x | 2.482x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 35.2 | 34.6 | 35.4 | 0.3 | 0.117x | 2.665x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 298.5 | 294.8 | 299.4 | 1.8 | 0.992x | 22.592x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 300.9 | 295.8 | 317.0 | 7.5 | 1.000x | 22.779x |

### `orig` / `s-030` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 22.1 | 22.0 | 22.5 | 0.2 | 0.021x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 22.1 | 22.0 | 22.2 | 0.1 | 0.021x | 1.001x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 46.2 | 45.8 | 46.4 | 0.3 | 0.043x | 2.093x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.7 | 68.6 | 76.6 | 3.1 | 0.064x | 3.115x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 252.2 | 247.0 | 253.9 | 2.9 | 0.236x | 11.435x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 264.5 | 250.1 | 267.8 | 7.5 | 0.247x | 11.994x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,069.9 | 1,057.0 | 1,090.1 | 12.0 | 1.000x | 48.514x |

### `orig` / `s-031` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.4 | 0.1 | 0.044x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.4 | 0.1 | 0.044x | 1.001x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 31.0 | 30.9 | 31.4 | 0.2 | 0.103x | 2.346x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 32.8 | 32.6 | 33.5 | 0.3 | 0.109x | 2.479x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 34.8 | 34.7 | 35.1 | 0.1 | 0.116x | 2.634x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 295.6 | 294.0 | 298.7 | 1.7 | 0.981x | 22.356x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 301.2 | 297.0 | 314.7 | 6.4 | 1.000x | 22.782x |

### `orig` / `s-031` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 29.6 | 29.2 | 30.9 | 0.6 | 0.028x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 29.7 | 29.4 | 30.4 | 0.3 | 0.028x | 1.001x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 54.3 | 54.1 | 63.6 | 3.8 | 0.051x | 1.831x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 72.2 | 70.4 | 77.9 | 2.5 | 0.068x | 2.437x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 330.3 | 328.6 | 339.3 | 3.9 | 0.311x | 11.145x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 330.9 | 326.8 | 334.0 | 2.7 | 0.312x | 11.165x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,062.0 | 1,057.5 | 1,080.6 | 8.0 | 1.000x | 35.829x |

### `orig` / `s-032` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.0 | 16.0 | 16.2 | 0.1 | 0.045x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.2 | 0.1 | 0.045x | 1.005x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 34.8 | 34.6 | 35.1 | 0.2 | 0.097x | 2.169x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 45.4 | 44.9 | 47.4 | 0.9 | 0.126x | 2.830x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 53.5 | 53.1 | 56.5 | 1.3 | 0.149x | 3.334x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 356.8 | 352.4 | 361.4 | 2.9 | 0.993x | 22.244x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 359.4 | 349.7 | 380.0 | 10.1 | 1.000x | 22.405x |

### `orig` / `s-032` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 26.4 | 26.2 | 26.8 | 0.2 | 0.020x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 26.4 | 26.0 | 26.5 | 0.2 | 0.020x | 1.003x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 48.4 | 48.2 | 48.6 | 0.1 | 0.037x | 1.837x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 71.6 | 71.1 | 79.1 | 3.0 | 0.055x | 2.717x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 379.5 | 374.2 | 382.8 | 3.1 | 0.292x | 14.396x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 393.6 | 390.9 | 402.3 | 4.3 | 0.303x | 14.931x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,299.4 | 1,294.6 | 1,301.5 | 2.4 | 1.000x | 49.288x |

### `orig` / `s-033` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.0 | 16.0 | 16.1 | 0.0 | 0.050x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.0 | 15.9 | 16.0 | 0.0 | 0.050x | 1.000x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 34.8 | 34.6 | 35.1 | 0.2 | 0.110x | 2.174x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 42.7 | 41.3 | 47.5 | 2.2 | 0.134x | 2.666x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 52.4 | 49.0 | 53.8 | 1.7 | 0.165x | 3.275x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 312.6 | 307.9 | 318.2 | 3.9 | 0.984x | 19.533x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 317.6 | 312.5 | 334.9 | 8.1 | 1.000x | 19.842x |

### `orig` / `s-033` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 26.0 | 25.8 | 26.2 | 0.1 | 0.023x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 26.3 | 25.9 | 26.5 | 0.2 | 0.023x | 1.012x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 48.4 | 48.3 | 52.9 | 1.8 | 0.043x | 1.859x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 71.0 | 70.7 | 78.7 | 3.1 | 0.063x | 2.729x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 357.2 | 354.9 | 362.0 | 2.5 | 0.315x | 13.736x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 361.0 | 356.3 | 364.6 | 3.1 | 0.319x | 13.879x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,133.0 | 1,129.5 | 1,140.8 | 3.7 | 1.000x | 43.563x |

### `orig` / `s-034` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 20.1 | 20.1 | 20.2 | 0.1 | 0.034x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 20.2 | 20.0 | 20.3 | 0.1 | 0.034x | 1.005x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.6 | 25.4 | 26.6 | 0.4 | 0.043x | 1.271x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.0 | 25.9 | 26.5 | 0.3 | 0.044x | 1.291x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 39.9 | 39.8 | 40.0 | 0.1 | 0.068x | 1.983x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 570.5 | 565.7 | 587.3 | 7.9 | 0.970x | 28.373x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 588.2 | 573.0 | 598.6 | 8.8 | 1.000x | 29.251x |

### `orig` / `s-034` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 19.0 | 19.0 | 19.0 | 0.0 | 0.009x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 19.0 | 18.9 | 19.5 | 0.2 | 0.009x | 1.001x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 41.5 | 41.2 | 42.1 | 0.3 | 0.019x | 2.181x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 98.1 | 97.4 | 101.1 | 1.4 | 0.045x | 5.157x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 172.7 | 171.5 | 175.4 | 1.3 | 0.080x | 9.083x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 176.3 | 175.2 | 181.4 | 2.3 | 0.081x | 9.274x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,170.6 | 2,151.6 | 2,185.1 | 10.7 | 1.000x | 114.154x |

### `orig` / `s-035` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.0 | 22.9 | 24.5 | 0.7 | 0.029x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 23.0 | 22.9 | 23.1 | 0.1 | 0.029x | 1.001x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 43.8 | 43.6 | 44.8 | 0.4 | 0.055x | 1.908x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 118.6 | 106.4 | 120.8 | 5.2 | 0.148x | 5.161x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 126.9 | 124.0 | 131.1 | 2.5 | 0.159x | 5.523x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 791.9 | 790.9 | 794.5 | 1.3 | 0.992x | 34.471x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 798.4 | 786.8 | 815.9 | 10.2 | 1.000x | 34.756x |

### `orig` / `s-035` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 25.3 | 25.2 | 25.4 | 0.1 | 0.008x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 25.3 | 25.0 | 25.5 | 0.2 | 0.008x | 1.001x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 48.5 | 48.3 | 52.8 | 1.8 | 0.016x | 1.915x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 133.2 | 133.0 | 134.5 | 0.6 | 0.044x | 5.260x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 702.5 | 655.1 | 712.6 | 22.0 | 0.234x | 27.748x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 706.5 | 704.7 | 708.4 | 1.3 | 0.235x | 27.906x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,007.1 | 2,991.5 | 3,018.2 | 9.6 | 1.000x | 118.783x |

### `orig` / `s-036` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.7 | 12.6 | 13.0 | 0.1 | 0.061x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.7 | 12.5 | 13.2 | 0.2 | 0.061x | 1.004x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.5 | 25.3 | 26.9 | 0.6 | 0.123x | 2.014x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 25.9 | 25.8 | 27.4 | 0.6 | 0.125x | 2.048x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 29.2 | 29.1 | 29.5 | 0.2 | 0.141x | 2.304x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 205.7 | 204.6 | 216.4 | 4.4 | 0.990x | 16.235x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 207.7 | 206.1 | 221.5 | 6.0 | 1.000x | 16.394x |

### `orig` / `s-036` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 26.7 | 26.6 | 26.8 | 0.1 | 0.036x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 26.8 | 26.6 | 26.9 | 0.1 | 0.037x | 1.003x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 50.6 | 50.1 | 50.8 | 0.2 | 0.069x | 1.893x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 69.2 | 65.7 | 72.5 | 2.7 | 0.094x | 2.589x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 239.8 | 237.5 | 243.1 | 1.9 | 0.327x | 8.971x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 240.7 | 236.8 | 241.9 | 1.8 | 0.328x | 9.005x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 733.5 | 721.7 | 738.0 | 6.6 | 1.000x | 27.438x |

### `orig` / `s-037` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 14.5 | 14.4 | 14.7 | 0.1 | 0.042x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.6 | 14.4 | 15.9 | 0.6 | 0.042x | 1.004x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 32.5 | 32.4 | 32.9 | 0.2 | 0.094x | 2.237x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 39.9 | 39.6 | 40.6 | 0.4 | 0.115x | 2.750x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 40.9 | 39.9 | 41.3 | 0.5 | 0.118x | 2.816x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 337.5 | 336.0 | 339.8 | 1.4 | 0.975x | 23.244x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 346.1 | 334.1 | 360.6 | 9.4 | 1.000x | 23.837x |

### `orig` / `s-037` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 20.9 | 20.7 | 21.8 | 0.4 | 0.017x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 21.0 | 20.8 | 21.4 | 0.3 | 0.017x | 1.004x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 44.2 | 43.9 | 53.0 | 3.6 | 0.036x | 2.113x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 67.8 | 66.2 | 76.2 | 3.5 | 0.056x | 3.239x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 293.0 | 291.6 | 303.5 | 5.2 | 0.241x | 14.005x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 295.1 | 294.2 | 298.3 | 1.4 | 0.243x | 14.106x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,215.0 | 1,204.7 | 1,222.0 | 6.7 | 1.000x | 58.079x |

### `orig` / `s-038` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 22.9 | 22.9 | 23.0 | 0.0 | 0.046x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 23.0 | 23.0 | 23.2 | 0.1 | 0.047x | 1.004x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 44.1 | 43.6 | 44.2 | 0.2 | 0.089x | 1.924x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 71.5 | 71.3 | 71.9 | 0.2 | 0.145x | 3.118x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 73.9 | 73.4 | 76.1 | 0.9 | 0.150x | 3.222x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 485.4 | 484.5 | 502.3 | 6.8 | 0.983x | 21.153x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 494.0 | 486.1 | 495.4 | 3.6 | 1.000x | 21.527x |

### `orig` / `s-038` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 26.8 | 26.7 | 26.8 | 0.0 | 0.015x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 26.9 | 26.5 | 27.1 | 0.2 | 0.015x | 1.003x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 50.6 | 50.5 | 50.8 | 0.1 | 0.028x | 1.888x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 95.7 | 90.3 | 98.6 | 2.9 | 0.053x | 3.575x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 566.9 | 565.7 | 618.8 | 20.6 | 0.313x | 21.169x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 575.6 | 564.0 | 589.7 | 9.5 | 0.317x | 21.493x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,813.6 | 1,799.7 | 1,818.1 | 6.8 | 1.000x | 67.719x |

### `orig` / `s-039` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.0 | 11.9 | 12.2 | 0.1 | 0.059x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.1 | 11.9 | 12.2 | 0.1 | 0.059x | 1.010x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 25.9 | 26.8 | 0.3 | 0.128x | 2.179x |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 25.9 | 26.8 | 0.3 | 0.129x | 2.186x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 27.5 | 26.6 | 28.3 | 0.6 | 0.135x | 2.293x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 204.2 | 198.6 | 211.9 | 4.5 | 1.000x | 17.010x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 205.0 | 202.1 | 207.7 | 1.8 | 1.004x | 17.081x |

### `orig` / `s-039` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 59.0 | 58.9 | 59.1 | 0.1 | 0.063x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 59.1 | 58.9 | 63.8 | 1.9 | 0.063x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 107.4 | 105.7 | 112.6 | 2.5 | 0.115x | 1.819x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 111.5 | 110.5 | 112.9 | 0.9 | 0.119x | 1.888x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 113.3 | 108.7 | 114.0 | 2.0 | 0.121x | 1.920x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 244.5 | 243.3 | 278.8 | 13.8 | 0.261x | 4.140x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 937.3 | 927.6 | 939.4 | 4.5 | 1.000x | 15.875x |

### `orig` / `s-040` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 23.2 | 22.7 | 23.6 | 0.3 | 0.665x | 1.000x |
| 2 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 25.1 | 24.9 | 25.2 | 0.1 | 0.719x | 1.082x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 26.0 | 25.9 | 26.0 | 0.0 | 0.745x | 1.121x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 26.0 | 25.9 | 26.1 | 0.1 | 0.746x | 1.121x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 34.1 | 33.6 | 35.0 | 0.5 | 0.977x | 1.470x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 34.9 | 34.2 | 38.8 | 2.0 | 1.000x | 1.504x |
| 7 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 48.4 | 47.1 | 48.7 | 0.6 | 1.387x | 2.085x |

### `orig` / `s-040` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 23.6 | 23.5 | 24.1 | 0.2 | 0.650x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 23.8 | 23.7 | 24.1 | 0.2 | 0.656x | 1.009x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 36.3 | 35.0 | 39.0 | 1.4 | 1.000x | 1.539x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 36.5 | 36.2 | 47.6 | 4.5 | 1.005x | 1.547x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 47.8 | 47.6 | 48.5 | 0.4 | 1.317x | 2.027x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 196.0 | 194.2 | 198.2 | 1.5 | 5.396x | 8.306x |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 198.2 | 197.1 | 201.7 | 1.6 | 5.457x | 8.400x |

### `orig` / `s-041` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.5 | 10.5 | 11.5 | 0.4 | 0.350x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.6 | 10.5 | 10.8 | 0.1 | 0.352x | 1.008x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 14.8 | 14.8 | 15.0 | 0.1 | 0.492x | 1.408x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.3 | 0.0 | 0.539x | 1.541x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 22.9 | 23.1 | 0.1 | 0.766x | 2.192x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.3 | 28.9 | 29.6 | 0.3 | 0.972x | 2.781x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.1 | 28.9 | 30.4 | 0.5 | 1.000x | 2.861x |

### `orig` / `s-041` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.7 | 18.6 | 18.8 | 0.1 | 0.504x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.8 | 18.6 | 19.1 | 0.2 | 0.505x | 1.002x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 37.2 | 36.3 | 40.7 | 1.6 | 1.000x | 1.984x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 37.4 | 37.1 | 47.8 | 4.2 | 1.007x | 1.998x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 41.3 | 41.3 | 41.5 | 0.1 | 1.113x | 2.207x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 142.6 | 141.8 | 143.8 | 0.7 | 3.837x | 7.612x |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 144.0 | 142.6 | 144.5 | 0.7 | 3.874x | 7.687x |

### `orig` / `s-042` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.8 | 13.7 | 13.9 | 0.1 | 0.066x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.9 | 13.7 | 13.9 | 0.1 | 0.066x | 1.003x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 17.2 | 16.5 | 17.5 | 0.4 | 0.082x | 1.246x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 18.5 | 18.4 | 18.7 | 0.1 | 0.088x | 1.338x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 29.3 | 29.0 | 29.5 | 0.2 | 0.140x | 2.116x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 208.5 | 205.9 | 217.9 | 4.2 | 0.994x | 15.075x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 209.7 | 208.1 | 212.7 | 1.7 | 1.000x | 15.161x |

### `orig` / `s-042` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 12.0 | 11.9 | 12.0 | 0.0 | 0.055x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 12.0 | 11.9 | 12.3 | 0.1 | 0.055x | 1.003x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 28.9 | 28.5 | 29.5 | 0.3 | 0.133x | 2.413x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 53.2 | 51.3 | 58.2 | 2.4 | 0.245x | 4.435x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 61.4 | 61.3 | 61.7 | 0.2 | 0.283x | 5.125x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 62.8 | 62.4 | 64.0 | 0.5 | 0.289x | 5.242x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 217.4 | 214.8 | 218.1 | 1.1 | 1.000x | 18.130x |

### `orig` / `s-043` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.7 | 12.5 | 12.9 | 0.1 | 0.083x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.8 | 12.7 | 13.1 | 0.2 | 0.084x | 1.004x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 23.6 | 23.4 | 24.6 | 0.4 | 0.155x | 1.853x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 23.9 | 23.8 | 24.5 | 0.3 | 0.157x | 1.880x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 29.2 | 29.1 | 29.5 | 0.2 | 0.192x | 2.297x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 152.4 | 150.8 | 158.2 | 2.6 | 1.000x | 11.985x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 153.6 | 148.5 | 155.1 | 2.3 | 1.008x | 12.082x |

### `orig` / `s-043` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 71.1 | 70.8 | 71.6 | 0.3 | 0.066x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 71.2 | 70.8 | 71.7 | 0.3 | 0.067x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 100.4 | 98.9 | 107.0 | 3.1 | 0.094x | 1.411x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 159.7 | 158.8 | 164.6 | 2.2 | 0.149x | 2.245x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 160.4 | 159.5 | 160.8 | 0.4 | 0.150x | 2.255x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 268.3 | 267.3 | 302.6 | 13.6 | 0.251x | 3.773x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,070.4 | 1,060.9 | 1,071.8 | 4.1 | 1.000x | 15.049x |

### `orig` / `s-044` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.6 | 10.4 | 10.8 | 0.2 | 0.351x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.6 | 10.5 | 10.7 | 0.1 | 0.352x | 1.002x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 15.3 | 14.8 | 15.7 | 0.3 | 0.508x | 1.447x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.2 | 0.0 | 0.536x | 1.526x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 22.9 | 22.8 | 23.1 | 0.1 | 0.761x | 2.165x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.5 | 29.2 | 29.5 | 0.1 | 0.978x | 2.784x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.1 | 29.2 | 30.8 | 0.5 | 1.000x | 2.847x |

### `orig` / `s-044` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 61.8 | 61.7 | 62.1 | 0.2 | 0.115x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 62.0 | 61.7 | 62.2 | 0.2 | 0.115x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 77.7 | 77.2 | 87.3 | 3.8 | 0.144x | 1.258x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 83.8 | 81.8 | 84.7 | 1.2 | 0.155x | 1.355x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 86.7 | 84.4 | 87.4 | 1.1 | 0.161x | 1.402x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 250.9 | 250.5 | 253.9 | 1.3 | 0.466x | 4.059x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 538.8 | 538.2 | 546.0 | 3.5 | 1.000x | 8.718x |

### `orig` / `s-045` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.7 | 12.6 | 12.9 | 0.1 | 0.083x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.7 | 12.6 | 13.0 | 0.1 | 0.084x | 1.003x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 23.4 | 23.4 | 23.6 | 0.1 | 0.155x | 1.852x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 23.9 | 23.6 | 24.5 | 0.3 | 0.158x | 1.890x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 29.1 | 29.1 | 29.2 | 0.0 | 0.192x | 2.301x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 151.6 | 150.0 | 157.9 | 2.9 | 1.000x | 11.985x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 152.5 | 147.8 | 155.3 | 2.4 | 1.006x | 12.057x |

### `orig` / `s-045` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 25.5 | 25.4 | 25.8 | 0.1 | 0.051x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 25.5 | 25.4 | 26.3 | 0.3 | 0.051x | 1.002x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 50.5 | 50.1 | 61.4 | 4.4 | 0.101x | 1.980x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.1 | 65.5 | 73.0 | 2.5 | 0.137x | 2.673x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 224.3 | 222.2 | 231.0 | 3.2 | 0.450x | 8.801x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 224.3 | 223.4 | 227.2 | 1.4 | 0.450x | 8.802x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 499.0 | 497.7 | 510.5 | 4.8 | 1.000x | 19.576x |

### `orig` / `s-046` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 21.7 | 21.7 | 21.8 | 0.1 | 0.046x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 21.8 | 21.5 | 22.1 | 0.2 | 0.046x | 1.005x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 41.3 | 41.1 | 41.9 | 0.3 | 0.087x | 1.901x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 51.4 | 50.1 | 51.9 | 0.6 | 0.108x | 2.366x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 52.2 | 51.8 | 53.1 | 0.5 | 0.110x | 2.406x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 467.4 | 464.4 | 472.3 | 2.8 | 0.987x | 21.530x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 473.7 | 468.1 | 486.2 | 7.6 | 1.000x | 21.820x |

### `orig` / `s-046` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 19.0 | 18.8 | 20.2 | 0.5 | 0.011x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 19.1 | 19.0 | 19.3 | 0.1 | 0.011x | 1.004x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 41.5 | 41.4 | 41.7 | 0.1 | 0.024x | 2.186x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 85.5 | 85.0 | 93.1 | 3.1 | 0.049x | 4.505x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 349.7 | 347.0 | 352.2 | 1.7 | 0.200x | 18.422x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 350.1 | 348.0 | 352.0 | 1.6 | 0.201x | 18.444x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,745.8 | 1,737.9 | 1,758.3 | 7.0 | 1.000x | 91.980x |

### `orig` / `s-047` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.0 | 23.0 | 23.0 | 0.0 | 0.029x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 23.0 | 23.0 | 23.0 | 0.0 | 0.029x | 1.001x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 26.0 | 25.7 | 26.4 | 0.2 | 0.033x | 1.131x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 25.9 | 26.7 | 0.3 | 0.033x | 1.138x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 43.8 | 43.5 | 44.3 | 0.3 | 0.055x | 1.905x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 785.7 | 780.8 | 800.2 | 7.6 | 0.989x | 34.171x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 794.5 | 783.2 | 807.3 | 9.0 | 1.000x | 34.556x |

### `orig` / `s-047` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 20.4 | 20.4 | 20.8 | 0.1 | 0.007x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 20.5 | 20.4 | 21.1 | 0.3 | 0.007x | 1.001x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 43.7 | 43.4 | 44.1 | 0.3 | 0.014x | 2.137x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 118.3 | 116.7 | 119.8 | 1.0 | 0.039x | 5.787x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 185.8 | 184.0 | 190.7 | 2.3 | 0.061x | 9.089x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 186.1 | 182.8 | 192.1 | 3.3 | 0.061x | 9.101x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,034.5 | 3,008.6 | 3,060.5 | 19.5 | 1.000x | 148.428x |

### `orig` / `s-048` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 0.044x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.0 | 0.044x | 1.005x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 16.9 | 16.7 | 17.2 | 0.2 | 0.056x | 1.278x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 18.6 | 18.5 | 18.6 | 0.0 | 0.062x | 1.406x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 31.9 | 31.1 | 32.2 | 0.4 | 0.106x | 2.417x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 297.5 | 290.4 | 299.5 | 3.1 | 0.987x | 22.537x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 301.4 | 293.1 | 317.7 | 8.7 | 1.000x | 22.831x |

### `orig` / `s-048` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 12.5 | 12.1 | 12.6 | 0.2 | 0.016x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 12.6 | 12.4 | 12.7 | 0.1 | 0.016x | 1.005x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 33.6 | 32.9 | 34.0 | 0.4 | 0.042x | 2.680x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 61.6 | 60.0 | 68.7 | 3.1 | 0.077x | 4.918x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 87.1 | 86.5 | 89.1 | 0.9 | 0.108x | 6.957x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 91.8 | 90.1 | 94.2 | 1.4 | 0.114x | 7.332x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 803.6 | 801.4 | 812.2 | 3.7 | 1.000x | 64.175x |

### `orig` / `s-049` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.4 | 12.2 | 12.8 | 0.2 | 0.086x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.5 | 12.2 | 12.6 | 0.1 | 0.087x | 1.005x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 22.2 | 22.1 | 22.3 | 0.1 | 0.154x | 1.790x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 22.5 | 22.1 | 24.7 | 1.0 | 0.156x | 1.812x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 27.6 | 27.4 | 27.9 | 0.2 | 0.192x | 2.224x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 143.8 | 142.0 | 145.1 | 1.3 | 1.000x | 11.592x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 143.8 | 142.6 | 148.1 | 2.0 | 1.000x | 11.593x |

### `orig` / `s-049` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 68.5 | 68.4 | 68.7 | 0.1 | 0.066x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 68.5 | 68.5 | 70.7 | 0.9 | 0.066x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 98.6 | 97.2 | 105.6 | 3.1 | 0.096x | 1.439x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 139.0 | 137.9 | 144.1 | 2.3 | 0.135x | 2.029x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 139.6 | 138.9 | 139.8 | 0.4 | 0.135x | 2.037x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 264.8 | 263.7 | 293.0 | 11.4 | 0.257x | 3.865x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,031.5 | 1,019.9 | 1,039.8 | 7.3 | 1.000x | 15.055x |

### `orig` / `s-050` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.4 | 14.4 | 14.5 | 0.0 | 0.048x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 14.5 | 14.3 | 14.6 | 0.1 | 0.048x | 1.004x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 32.6 | 32.4 | 32.7 | 0.1 | 0.108x | 2.260x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 40.1 | 39.4 | 40.4 | 0.3 | 0.132x | 2.777x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 41.0 | 40.2 | 42.7 | 0.8 | 0.135x | 2.840x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 300.0 | 298.6 | 301.4 | 1.1 | 0.990x | 20.803x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 303.1 | 296.8 | 309.7 | 4.4 | 1.000x | 21.021x |

### `orig` / `s-050` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 53.8 | 53.7 | 54.1 | 0.2 | 0.033x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 53.8 | 53.5 | 54.4 | 0.3 | 0.033x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 103.9 | 102.5 | 112.1 | 3.5 | 0.064x | 1.933x |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 233.3 | 232.5 | 244.9 | 4.6 | 0.143x | 4.339x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 294.0 | 291.0 | 378.2 | 34.1 | 0.180x | 5.469x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 298.6 | 289.6 | 335.4 | 15.9 | 0.183x | 5.554x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,632.5 | 1,617.5 | 1,637.8 | 7.4 | 1.000x | 30.364x |

### `orig` / `s-051` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.3 | 12.2 | 12.5 | 0.1 | 0.085x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.3 | 12.2 | 12.5 | 0.1 | 0.085x | 1.004x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 22.2 | 21.0 | 23.4 | 0.8 | 0.153x | 1.804x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 22.2 | 22.1 | 24.7 | 1.0 | 0.153x | 1.804x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 27.4 | 27.3 | 27.9 | 0.2 | 0.189x | 2.229x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 142.2 | 138.7 | 145.1 | 2.1 | 0.984x | 11.573x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 144.6 | 143.7 | 148.0 | 1.5 | 1.000x | 11.766x |

### `orig` / `s-051` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 68.5 | 68.4 | 68.8 | 0.1 | 0.068x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 68.7 | 68.5 | 69.0 | 0.2 | 0.068x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 98.8 | 97.1 | 106.7 | 3.4 | 0.097x | 1.442x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 137.8 | 136.3 | 147.8 | 4.1 | 0.136x | 2.011x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 139.6 | 138.9 | 142.0 | 1.1 | 0.138x | 2.037x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 265.1 | 263.0 | 292.5 | 11.3 | 0.261x | 3.870x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,014.0 | 1,006.3 | 1,023.0 | 6.1 | 1.000x | 14.800x |

### `orig` / `s-052` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.1 | 0.045x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.6 | 0.1 | 0.045x | 1.009x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.9 | 25.8 | 25.9 | 0.0 | 0.087x | 1.956x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.0 | 25.9 | 26.6 | 0.2 | 0.087x | 1.965x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 31.0 | 30.9 | 31.2 | 0.1 | 0.104x | 2.342x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 295.8 | 294.2 | 302.0 | 2.9 | 0.996x | 22.356x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 297.2 | 293.1 | 316.4 | 8.3 | 1.000x | 22.457x |

### `orig` / `s-052` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 19.6 | 19.4 | 20.0 | 0.2 | 0.018x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 19.8 | 19.5 | 21.0 | 0.5 | 0.018x | 1.011x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 41.4 | 41.3 | 42.4 | 0.4 | 0.039x | 2.113x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.8 | 68.2 | 81.1 | 5.0 | 0.064x | 3.511x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 176.6 | 173.9 | 178.7 | 1.6 | 0.165x | 9.020x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 178.3 | 177.1 | 180.6 | 1.3 | 0.166x | 9.103x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,071.8 | 1,066.7 | 1,085.4 | 6.5 | 1.000x | 54.730x |

### `orig` / `s-053` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 0.045x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.5 | 0.1 | 0.045x | 1.005x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.8 | 25.7 | 26.4 | 0.2 | 0.087x | 1.951x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.0 | 25.9 | 26.3 | 0.1 | 0.088x | 1.965x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 31.0 | 30.7 | 34.0 | 1.2 | 0.105x | 2.342x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 295.9 | 294.2 | 316.3 | 8.3 | 1.000x | 22.369x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 296.0 | 292.8 | 300.2 | 2.8 | 1.000x | 22.375x |

### `orig` / `s-053` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 14.4 | 14.4 | 14.6 | 0.1 | 0.014x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 14.5 | 14.2 | 14.7 | 0.2 | 0.014x | 1.005x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 38.1 | 37.9 | 38.3 | 0.1 | 0.036x | 2.639x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 67.5 | 67.2 | 74.9 | 2.9 | 0.063x | 4.672x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 164.3 | 162.0 | 164.7 | 1.0 | 0.154x | 11.377x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 167.2 | 166.5 | 168.9 | 0.8 | 0.157x | 11.578x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,067.9 | 1,056.4 | 1,080.2 | 7.8 | 1.000x | 73.925x |

### `orig` / `s-054` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 0.045x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.5 | 0.1 | 0.045x | 1.003x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.9 | 25.8 | 26.0 | 0.1 | 0.087x | 1.956x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.0 | 26.0 | 26.2 | 0.1 | 0.088x | 1.967x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 30.9 | 30.6 | 33.1 | 0.9 | 0.104x | 2.334x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 295.5 | 291.6 | 302.0 | 3.5 | 0.994x | 22.317x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 297.3 | 294.9 | 315.0 | 7.5 | 1.000x | 22.446x |

### `orig` / `s-054` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 14.3 | 14.1 | 14.4 | 0.1 | 0.013x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 14.4 | 14.1 | 14.5 | 0.1 | 0.014x | 1.010x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 38.2 | 38.0 | 38.3 | 0.1 | 0.036x | 2.672x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 67.3 | 67.1 | 75.4 | 3.3 | 0.063x | 4.716x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 165.8 | 165.2 | 167.9 | 0.9 | 0.155x | 11.615x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 168.0 | 164.8 | 171.5 | 2.4 | 0.157x | 11.768x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,068.4 | 1,057.2 | 1,078.9 | 7.5 | 1.000x | 74.820x |

### `orig` / `s-055` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 0.045x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 0.045x | 1.003x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.9 | 25.7 | 25.9 | 0.1 | 0.087x | 1.962x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.0 | 25.9 | 26.0 | 0.0 | 0.088x | 1.966x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 31.0 | 30.6 | 31.2 | 0.2 | 0.104x | 2.344x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 294.6 | 292.6 | 297.2 | 1.8 | 0.993x | 22.294x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 296.6 | 295.2 | 315.8 | 7.8 | 1.000x | 22.446x |

### `orig` / `s-055` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 14.4 | 14.2 | 14.5 | 0.1 | 0.013x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 14.5 | 14.2 | 14.7 | 0.2 | 0.014x | 1.010x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 37.9 | 37.9 | 38.1 | 0.1 | 0.036x | 2.637x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 67.5 | 66.9 | 77.0 | 3.9 | 0.063x | 4.692x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 163.6 | 161.4 | 164.1 | 1.0 | 0.153x | 11.372x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 167.4 | 166.7 | 171.6 | 1.8 | 0.157x | 11.637x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,067.9 | 1,048.7 | 1,075.0 | 10.3 | 1.000x | 74.235x |

### `orig` / `s-056` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.0 | 0.044x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.2 | 13.6 | 0.1 | 0.045x | 1.009x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.9 | 25.7 | 26.0 | 0.1 | 0.087x | 1.957x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.0 | 26.0 | 26.7 | 0.3 | 0.087x | 1.964x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 31.0 | 30.7 | 31.2 | 0.2 | 0.104x | 2.340x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 294.3 | 293.6 | 302.6 | 3.4 | 0.985x | 22.205x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 298.7 | 294.7 | 310.8 | 5.8 | 1.000x | 22.541x |

### `orig` / `s-056` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 16.4 | 16.2 | 16.5 | 0.1 | 0.015x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 16.4 | 16.2 | 16.7 | 0.2 | 0.015x | 1.001x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 38.1 | 38.1 | 38.3 | 0.1 | 0.036x | 2.326x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 67.4 | 67.2 | 77.1 | 3.8 | 0.063x | 4.117x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 157.6 | 156.3 | 158.5 | 0.7 | 0.148x | 9.625x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 159.0 | 155.0 | 162.7 | 2.5 | 0.149x | 9.706x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,064.0 | 1,056.1 | 1,075.7 | 6.7 | 1.000x | 64.964x |

### `orig` / `s-057` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7,672.6 | 7,664.0 | 7,676.3 | 5.3 | 0.779x | 1.000x |
| 2 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 7,677.7 | 7,673.9 | 7,683.3 | 3.2 | 0.779x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 9,807.6 | 9,803.5 | 9,928.5 | 48.1 | 0.995x | 1.278x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 9,855.2 | 9,806.5 | 12,656.5 | 1,195.4 | 1.000x | 1.284x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19,081.1 | 19,064.9 | 19,085.7 | 7.5 | 1.936x | 2.487x |
| 6 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 19,087.9 | 19,066.1 | 19,148.9 | 28.0 | 1.937x | 2.488x |
| 7 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 36,469.8 | 36,450.4 | 36,525.9 | 27.0 | 3.701x | 4.753x |

### `orig` / `s-058` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5,906.3 | 5,900.6 | 6,042.8 | 57.0 | 0.081x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 6,275.9 | 6,245.6 | 6,293.8 | 16.9 | 0.086x | 1.063x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7,465.7 | 7,462.3 | 7,591.0 | 50.3 | 0.103x | 1.264x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 7,468.3 | 7,465.6 | 7,521.7 | 22.5 | 0.103x | 1.264x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 14,333.4 | 14,326.6 | 14,342.3 | 6.1 | 0.197x | 2.427x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 72,378.4 | 72,269.0 | 74,027.3 | 754.0 | 0.996x | 12.254x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 72,689.9 | 72,672.9 | 73,928.7 | 484.2 | 1.000x | 12.307x |

### `orig` / `s-059` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 9,554.8 | 9,553.6 | 9,557.8 | 1.5 | 0.060x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 9,555.3 | 9,553.6 | 9,557.7 | 1.6 | 0.060x | 1.000x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 13,692.3 | 13,680.7 | 13,797.8 | 43.8 | 0.086x | 1.433x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 13,695.8 | 13,683.1 | 13,814.6 | 48.8 | 0.086x | 1.433x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 18,308.2 | 18,303.8 | 18,315.8 | 4.4 | 0.115x | 1.916x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 158,736.5 | 158,161.5 | 159,418.1 | 434.7 | 1.000x | 16.613x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 159,127.1 | 157,791.5 | 162,247.5 | 1,654.8 | 1.002x | 16.654x |

### `orig` / `s-060` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 7,644.1 | 7,630.3 | 7,648.0 | 7.4 | 0.812x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7,648.4 | 7,636.2 | 7,660.3 | 9.9 | 0.812x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 9,415.1 | 9,403.1 | 9,437.9 | 11.6 | 1.000x | 1.232x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 9,419.3 | 9,412.3 | 9,426.6 | 4.7 | 1.000x | 1.232x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 18,172.2 | 18,164.9 | 18,198.1 | 11.7 | 1.929x | 2.377x |
| 6 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 19,065.6 | 19,054.8 | 19,161.5 | 39.9 | 2.024x | 2.494x |
| 7 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19,066.8 | 19,060.8 | 19,125.8 | 24.8 | 2.024x | 2.494x |

### `orig` / `s-061` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 3,737.9 | 3,736.4 | 3,744.4 | 2.8 | 0.084x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 3,741.6 | 3,738.4 | 3,743.2 | 1.6 | 0.084x | 1.001x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6,137.7 | 6,129.9 | 6,143.7 | 5.3 | 0.138x | 1.642x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 6,568.3 | 6,519.9 | 6,656.7 | 45.7 | 0.148x | 1.757x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 7,234.0 | 7,227.8 | 7,261.0 | 12.0 | 0.163x | 1.935x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 44,486.7 | 44,477.2 | 45,695.2 | 497.0 | 1.000x | 11.901x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44,565.1 | 44,446.3 | 44,670.6 | 90.2 | 1.002x | 11.922x |

### `orig` / `s-062` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.0 | 16.0 | 16.1 | 0.0 | 0.049x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.2 | 0.0 | 0.050x | 1.008x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 35.6 | 34.8 | 36.3 | 0.6 | 0.109x | 2.221x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 41.4 | 41.3 | 47.4 | 2.3 | 0.128x | 2.587x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 53.7 | 52.3 | 53.9 | 0.6 | 0.165x | 3.353x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 321.3 | 320.1 | 328.3 | 2.9 | 0.989x | 20.055x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 325.0 | 317.0 | 333.0 | 5.1 | 1.000x | 20.283x |

### `orig` / `s-063` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 4,577.9 | 4,575.3 | 4,607.8 | 12.4 | 0.042x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 4,792.1 | 4,787.6 | 4,800.5 | 4.3 | 0.043x | 1.047x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 4,794.0 | 4,787.1 | 4,797.3 | 3.6 | 0.043x | 1.047x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6,850.3 | 6,845.1 | 6,853.1 | 2.7 | 0.062x | 1.496x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 6,851.2 | 6,849.3 | 6,872.9 | 10.4 | 0.062x | 1.497x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 109,919.6 | 108,684.5 | 110,183.5 | 547.2 | 0.997x | 24.011x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 110,242.2 | 109,781.6 | 110,939.9 | 446.6 | 1.000x | 24.082x |

### `orig` / `s-064` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 7,650.3 | 7,643.6 | 7,654.3 | 3.8 | 0.080x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 7,653.8 | 7,649.5 | 7,664.9 | 6.6 | 0.080x | 1.000x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 10,589.8 | 10,577.3 | 10,594.3 | 5.7 | 0.111x | 1.384x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 10,600.5 | 10,586.3 | 10,653.4 | 29.7 | 0.111x | 1.386x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 14,686.5 | 14,675.7 | 14,918.9 | 94.4 | 0.154x | 1.920x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 94,708.6 | 94,592.0 | 95,802.6 | 542.7 | 0.994x | 12.380x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 95,310.1 | 94,721.9 | 95,982.9 | 470.3 | 1.000x | 12.458x |

### `orig` / `s-065` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.6 | 10.5 | 12.1 | 0.6 | 0.360x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.6 | 10.5 | 11.8 | 0.5 | 0.361x | 1.002x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 15.2 | 15.0 | 16.2 | 0.5 | 0.520x | 1.442x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.3 | 0.1 | 0.553x | 1.535x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 23.3 | 22.9 | 23.9 | 0.3 | 0.794x | 2.203x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.0 | 29.0 | 29.8 | 0.4 | 0.991x | 2.749x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.3 | 29.1 | 29.7 | 0.2 | 1.000x | 2.775x |

### `orig` / `s-065` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 21.2 | 21.0 | 21.8 | 0.3 | 0.038x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 21.5 | 20.9 | 21.5 | 0.2 | 0.038x | 1.010x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 48.3 | 48.2 | 48.5 | 0.1 | 0.086x | 2.272x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 62.0 | 61.4 | 71.4 | 3.8 | 0.110x | 2.919x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 226.8 | 225.7 | 232.0 | 2.3 | 0.403x | 10.676x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 228.6 | 227.3 | 229.5 | 0.8 | 0.407x | 10.760x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 562.1 | 553.4 | 580.2 | 8.8 | 1.000x | 26.460x |

### `orig` / `s-066` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33.5 | 33.5 | 33.6 | 0.0 | 0.051x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33.6 | 33.5 | 33.7 | 0.1 | 0.051x | 1.002x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 55.4 | 55.2 | 55.7 | 0.2 | 0.085x | 1.653x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 57.9 | 57.7 | 58.0 | 0.1 | 0.089x | 1.725x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 171.9 | 171.2 | 172.6 | 0.5 | 0.263x | 5.124x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 653.3 | 647.6 | 667.6 | 7.8 | 1.000x | 19.476x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 659.4 | 653.3 | 669.0 | 5.5 | 1.009x | 19.660x |

### `orig` / `s-066` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 62.6 | 62.5 | 67.3 | 1.9 | 0.094x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 62.6 | 62.4 | 63.1 | 0.2 | 0.094x | 1.000x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 78.9 | 78.4 | 79.4 | 0.4 | 0.119x | 1.260x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 80.6 | 80.3 | 81.0 | 0.3 | 0.121x | 1.288x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 83.4 | 79.1 | 88.9 | 3.5 | 0.125x | 1.332x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 250.4 | 249.3 | 258.2 | 3.3 | 0.377x | 3.999x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 664.9 | 659.9 | 667.4 | 2.5 | 1.000x | 10.620x |

### `orig` / `s-067` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.1 | 32.1 | 32.5 | 0.2 | 0.050x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.2 | 32.1 | 32.3 | 0.0 | 0.050x | 1.000x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 76.5 | 76.4 | 76.7 | 0.1 | 0.120x | 2.379x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 82.0 | 80.0 | 83.4 | 1.2 | 0.129x | 2.551x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 169.9 | 169.8 | 170.5 | 0.3 | 0.266x | 5.285x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 637.8 | 635.0 | 644.5 | 3.2 | 0.999x | 19.839x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 638.2 | 630.8 | 645.8 | 6.5 | 1.000x | 19.850x |

### `orig` / `s-067` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 58.3 | 58.2 | 58.6 | 0.2 | 0.090x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 58.4 | 58.2 | 63.2 | 1.9 | 0.091x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 80.8 | 79.9 | 88.9 | 4.1 | 0.125x | 1.388x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 88.4 | 88.3 | 102.8 | 5.7 | 0.137x | 1.518x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 90.3 | 90.1 | 90.6 | 0.2 | 0.140x | 1.550x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 276.4 | 273.6 | 295.1 | 7.9 | 0.429x | 4.745x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 644.7 | 635.0 | 647.7 | 5.2 | 1.000x | 11.066x |

### `orig` / `s-068` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.6 | 16.5 | 16.7 | 0.1 | 0.040x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.6 | 16.5 | 16.8 | 0.1 | 0.040x | 1.001x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 18.2 | 17.8 | 19.1 | 0.5 | 0.044x | 1.096x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 20.8 | 20.7 | 21.0 | 0.1 | 0.050x | 1.249x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 129.3 | 128.8 | 129.8 | 0.3 | 0.312x | 7.773x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 414.2 | 410.3 | 424.4 | 4.9 | 1.000x | 24.909x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 418.6 | 412.3 | 422.2 | 3.2 | 1.011x | 25.172x |

### `orig` / `s-068` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 23.1 | 23.1 | 23.6 | 0.2 | 0.056x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 23.2 | 22.9 | 23.5 | 0.2 | 0.056x | 1.002x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 23.8 | 23.6 | 23.9 | 0.1 | 0.058x | 1.027x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 26.0 | 26.0 | 26.9 | 0.4 | 0.063x | 1.125x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 59.0 | 56.3 | 67.5 | 3.9 | 0.144x | 2.551x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 179.0 | 178.7 | 188.0 | 3.6 | 0.436x | 7.737x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 410.9 | 406.6 | 415.6 | 3.2 | 1.000x | 17.762x |

### `orig` / `s-069` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.5 | 12.2 | 12.8 | 0.2 | 0.059x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.7 | 12.2 | 14.2 | 0.8 | 0.060x | 1.019x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 25.8 | 25.5 | 26.9 | 0.5 | 0.122x | 2.065x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.3 | 26.1 | 27.1 | 0.4 | 0.125x | 2.105x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 29.2 | 29.1 | 29.4 | 0.1 | 0.139x | 2.337x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 210.6 | 205.8 | 212.6 | 2.4 | 1.000x | 16.871x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 212.7 | 206.5 | 223.5 | 6.0 | 1.010x | 17.039x |

### `orig` / `s-069` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 27.0 | 26.9 | 27.5 | 0.2 | 0.037x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 27.1 | 27.0 | 27.8 | 0.3 | 0.037x | 1.002x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 50.6 | 50.3 | 50.8 | 0.2 | 0.070x | 1.871x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 69.5 | 68.3 | 73.8 | 2.0 | 0.096x | 2.570x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 243.1 | 239.1 | 249.3 | 3.7 | 0.336x | 8.995x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 244.7 | 241.0 | 246.1 | 1.9 | 0.338x | 9.052x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 723.0 | 711.0 | 737.7 | 9.4 | 1.000x | 26.746x |

### `orig` / `s-070` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 27.9 | 27.8 | 28.0 | 0.0 | 0.052x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 27.9 | 27.8 | 28.0 | 0.1 | 0.052x | 1.000x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 43.1 | 42.1 | 43.4 | 0.5 | 0.080x | 1.545x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 44.6 | 44.4 | 44.8 | 0.1 | 0.082x | 1.598x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 158.2 | 157.9 | 158.5 | 0.2 | 0.292x | 5.669x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 540.6 | 533.2 | 545.8 | 4.6 | 0.999x | 19.369x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 541.0 | 537.4 | 547.8 | 3.8 | 1.000x | 19.383x |

### `orig` / `s-070` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 48.2 | 48.2 | 48.4 | 0.1 | 0.089x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 48.2 | 48.2 | 48.7 | 0.2 | 0.089x | 1.001x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 69.1 | 68.7 | 74.4 | 2.2 | 0.127x | 1.433x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 70.7 | 70.4 | 70.9 | 0.2 | 0.130x | 1.467x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 77.7 | 74.6 | 86.1 | 4.2 | 0.143x | 1.611x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 228.3 | 227.1 | 252.8 | 9.9 | 0.421x | 4.737x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 542.4 | 538.1 | 543.6 | 2.1 | 1.000x | 11.253x |

### `orig` / `s-071` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 55.5 | 55.2 | 56.1 | 0.3 | 0.100x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 55.6 | 55.5 | 55.8 | 0.1 | 0.100x | 1.001x |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 55.6 | 55.4 | 55.7 | 0.1 | 0.100x | 1.002x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 58.0 | 57.8 | 58.3 | 0.2 | 0.104x | 1.045x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 217.5 | 216.8 | 221.4 | 1.6 | 0.390x | 3.917x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 557.3 | 555.8 | 565.7 | 3.6 | 1.000x | 10.037x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 561.5 | 550.1 | 568.4 | 7.0 | 1.008x | 10.112x |

### `orig` / `s-071` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 86.6 | 86.4 | 100.3 | 5.5 | 0.155x | 1.000x |
| 2 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 88.2 | 87.8 | 88.8 | 0.4 | 0.158x | 1.019x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 90.4 | 88.4 | 97.4 | 3.1 | 0.162x | 1.044x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 109.5 | 109.4 | 109.7 | 0.1 | 0.196x | 1.264x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 109.5 | 109.4 | 109.8 | 0.1 | 0.196x | 1.265x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 375.3 | 374.1 | 384.1 | 3.7 | 0.673x | 4.335x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 558.0 | 554.1 | 566.5 | 4.2 | 1.000x | 6.444x |

### `orig` / `s-072` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 42.6 | 42.6 | 42.7 | 0.1 | 0.035x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 42.8 | 42.5 | 43.0 | 0.2 | 0.035x | 1.003x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 64.8 | 64.2 | 65.8 | 0.6 | 0.053x | 1.520x |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 65.1 | 64.7 | 65.6 | 0.3 | 0.054x | 1.528x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 67.0 | 66.9 | 67.3 | 0.1 | 0.055x | 1.571x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,212.7 | 1,178.7 | 1,220.6 | 17.0 | 1.000x | 28.443x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,224.0 | 1,180.2 | 1,271.5 | 29.8 | 1.009x | 28.706x |

### `orig` / `s-072` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 89.2 | 89.1 | 89.6 | 0.2 | 0.052x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 89.2 | 89.1 | 89.3 | 0.1 | 0.052x | 1.000x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 148.0 | 146.9 | 157.7 | 4.0 | 0.085x | 1.659x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 149.1 | 148.3 | 150.1 | 0.6 | 0.086x | 1.672x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 171.8 | 169.2 | 178.6 | 3.2 | 0.099x | 1.926x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 327.8 | 323.8 | 346.0 | 7.9 | 0.189x | 3.674x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,731.7 | 1,725.9 | 1,740.8 | 5.6 | 1.000x | 19.411x |

### `orig` / `s-073` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.1 | 13.1 | 13.2 | 0.1 | 0.044x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 14.1 | 0.4 | 0.045x | 1.007x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 26.0 | 25.9 | 26.7 | 0.3 | 0.088x | 1.980x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 26.0 | 27.3 | 0.5 | 0.088x | 1.985x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 30.9 | 30.6 | 31.0 | 0.1 | 0.104x | 2.351x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 296.9 | 296.5 | 305.7 | 3.5 | 1.000x | 22.627x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 301.0 | 296.9 | 305.1 | 2.9 | 1.014x | 22.936x |

### `orig` / `s-073` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 20.4 | 20.4 | 20.5 | 0.1 | 0.019x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 20.5 | 20.3 | 20.6 | 0.1 | 0.019x | 1.003x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 44.0 | 43.4 | 44.1 | 0.3 | 0.041x | 2.152x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.6 | 68.0 | 76.6 | 3.2 | 0.064x | 3.358x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 191.2 | 189.0 | 196.0 | 2.5 | 0.177x | 9.351x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 191.6 | 188.7 | 194.4 | 2.2 | 0.178x | 9.371x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,078.6 | 1,068.6 | 1,092.8 | 8.3 | 1.000x | 52.759x |

### `orig` / `s-074` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.1 | 13.1 | 13.2 | 0.0 | 0.044x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 0.044x | 1.005x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 30.9 | 30.6 | 31.2 | 0.2 | 0.104x | 2.353x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 33.4 | 32.5 | 35.2 | 0.9 | 0.112x | 2.538x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 34.8 | 34.7 | 35.1 | 0.1 | 0.117x | 2.648x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 297.9 | 295.6 | 302.4 | 2.5 | 1.000x | 22.656x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 302.1 | 296.0 | 304.2 | 3.4 | 1.014x | 22.974x |

### `orig` / `s-074` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 26.8 | 26.8 | 26.9 | 0.0 | 0.025x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 26.9 | 26.6 | 27.8 | 0.5 | 0.025x | 1.003x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 50.5 | 50.4 | 50.7 | 0.1 | 0.047x | 1.885x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 73.2 | 70.7 | 77.7 | 2.5 | 0.068x | 2.733x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 302.2 | 300.0 | 308.0 | 3.2 | 0.281x | 11.280x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 305.1 | 302.9 | 312.0 | 3.8 | 0.283x | 11.385x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,077.1 | 1,055.2 | 1,080.5 | 9.1 | 1.000x | 40.197x |

### `orig` / `s-075` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.1 | 32.1 | 32.2 | 0.1 | 0.050x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.2 | 32.1 | 32.2 | 0.0 | 0.051x | 1.002x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 83.3 | 83.2 | 83.7 | 0.2 | 0.131x | 2.594x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 89.2 | 89.1 | 89.5 | 0.1 | 0.140x | 2.778x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 170.1 | 169.1 | 180.1 | 4.1 | 0.267x | 5.296x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 631.8 | 625.6 | 638.4 | 4.4 | 0.993x | 19.676x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 636.4 | 628.8 | 639.5 | 3.8 | 1.000x | 19.822x |

### `orig` / `s-075` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 58.4 | 58.2 | 59.0 | 0.3 | 0.091x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 58.4 | 58.3 | 60.7 | 0.9 | 0.091x | 1.001x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 68.1 | 67.8 | 68.6 | 0.3 | 0.106x | 1.167x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 87.4 | 87.3 | 97.4 | 4.0 | 0.136x | 1.498x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 93.0 | 93.0 | 93.1 | 0.0 | 0.144x | 1.594x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 231.9 | 231.5 | 240.6 | 3.4 | 0.360x | 3.973x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 643.9 | 636.7 | 657.9 | 7.5 | 1.000x | 11.033x |

### `orig` / `s-076` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.1 | 32.1 | 32.4 | 0.1 | 0.051x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.2 | 32.1 | 32.2 | 0.0 | 0.051x | 1.001x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 83.3 | 83.2 | 83.5 | 0.1 | 0.131x | 2.590x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 89.1 | 89.1 | 89.3 | 0.1 | 0.140x | 2.773x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 170.1 | 170.0 | 179.2 | 3.6 | 0.267x | 5.290x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 633.6 | 624.8 | 641.1 | 5.9 | 0.996x | 19.710x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 636.2 | 625.6 | 638.0 | 4.4 | 1.000x | 19.789x |

### `orig` / `s-076` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 58.3 | 58.2 | 59.9 | 0.7 | 0.091x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 58.5 | 58.3 | 60.9 | 1.0 | 0.091x | 1.004x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 68.0 | 67.9 | 68.4 | 0.2 | 0.106x | 1.168x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 87.4 | 87.3 | 93.4 | 2.4 | 0.136x | 1.500x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 93.0 | 93.0 | 93.2 | 0.1 | 0.145x | 1.596x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 231.9 | 230.9 | 239.6 | 3.5 | 0.361x | 3.981x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 641.6 | 634.3 | 653.9 | 6.7 | 1.000x | 11.013x |

### `orig` / `s-077` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.1 | 32.1 | 32.2 | 0.0 | 0.046x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.2 | 32.1 | 32.7 | 0.2 | 0.046x | 1.000x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 75.8 | 75.5 | 76.2 | 0.2 | 0.109x | 2.356x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 83.5 | 83.1 | 83.9 | 0.3 | 0.120x | 2.597x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 171.1 | 169.7 | 180.1 | 4.8 | 0.245x | 5.321x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 696.2 | 690.0 | 707.4 | 6.4 | 0.998x | 21.655x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 697.7 | 690.4 | 704.1 | 4.9 | 1.000x | 21.703x |

### `orig` / `s-077` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 58.3 | 58.2 | 58.5 | 0.1 | 0.083x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 58.5 | 58.3 | 63.1 | 1.8 | 0.084x | 1.002x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 61.5 | 60.4 | 68.1 | 2.8 | 0.088x | 1.054x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 68.2 | 64.5 | 72.2 | 3.2 | 0.098x | 1.170x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 88.8 | 88.3 | 93.5 | 2.0 | 0.127x | 1.522x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 232.2 | 231.0 | 240.9 | 3.6 | 0.332x | 3.981x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 699.8 | 695.3 | 711.8 | 7.1 | 1.000x | 11.998x |

### `orig` / `s-078` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.1 | 32.0 | 32.2 | 0.0 | 0.044x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.2 | 32.1 | 32.2 | 0.0 | 0.044x | 1.002x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 54.4 | 54.0 | 55.9 | 0.7 | 0.075x | 1.695x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 70.5 | 69.9 | 71.5 | 0.5 | 0.097x | 2.196x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 169.8 | 169.3 | 179.3 | 3.8 | 0.235x | 5.287x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 721.4 | 714.8 | 732.3 | 5.8 | 0.996x | 22.462x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 724.1 | 711.0 | 728.9 | 6.6 | 1.000x | 22.544x |

### `orig` / `s-078` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 58.4 | 58.2 | 58.5 | 0.1 | 0.080x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 58.4 | 58.3 | 63.4 | 2.0 | 0.080x | 1.000x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 65.2 | 59.3 | 76.2 | 6.4 | 0.090x | 1.118x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 66.3 | 62.0 | 68.6 | 2.1 | 0.091x | 1.136x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 83.4 | 82.9 | 93.3 | 4.9 | 0.115x | 1.429x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 232.0 | 230.9 | 240.5 | 3.6 | 0.320x | 3.974x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 725.5 | 723.7 | 726.3 | 1.0 | 1.000x | 12.429x |

### `orig` / `s-079` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.1 | 32.0 | 34.1 | 0.8 | 0.044x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 32.2 | 32.1 | 32.3 | 0.1 | 0.044x | 1.002x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 54.4 | 53.6 | 55.9 | 0.9 | 0.075x | 1.695x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 70.3 | 70.0 | 71.2 | 0.5 | 0.097x | 2.189x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 170.0 | 169.6 | 178.7 | 3.5 | 0.235x | 5.296x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 723.2 | 715.7 | 729.5 | 5.0 | 0.999x | 22.536x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 724.0 | 714.6 | 730.6 | 5.8 | 1.000x | 22.560x |

### `orig` / `s-079` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 58.3 | 58.2 | 58.4 | 0.1 | 0.081x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 58.5 | 58.3 | 63.3 | 2.0 | 0.081x | 1.002x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 61.9 | 58.8 | 67.9 | 3.1 | 0.086x | 1.060x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 66.2 | 66.1 | 73.3 | 2.9 | 0.091x | 1.134x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 83.2 | 83.0 | 94.3 | 4.6 | 0.115x | 1.427x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 231.6 | 230.0 | 240.8 | 4.0 | 0.320x | 3.971x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 723.4 | 721.7 | 726.2 | 1.7 | 1.000x | 12.400x |

### `orig` / `s-080` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 16.0 | 16.0 | 16.1 | 0.0 | 0.046x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.1 | 0.0 | 0.046x | 1.003x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 34.7 | 34.5 | 34.8 | 0.2 | 0.099x | 2.163x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 45.2 | 44.3 | 51.1 | 2.5 | 0.129x | 2.824x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 57.1 | 53.9 | 57.7 | 1.4 | 0.163x | 3.564x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 350.8 | 345.6 | 364.4 | 6.6 | 1.000x | 21.895x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 352.6 | 349.8 | 358.5 | 3.0 | 1.005x | 22.008x |

### `orig` / `s-080` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 26.2 | 26.0 | 26.3 | 0.1 | 0.020x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 26.2 | 26.1 | 26.8 | 0.3 | 0.020x | 1.000x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 48.3 | 48.3 | 48.4 | 0.0 | 0.038x | 1.842x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 71.7 | 70.9 | 79.0 | 3.0 | 0.056x | 2.733x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 377.9 | 376.2 | 383.6 | 3.2 | 0.295x | 14.401x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 392.1 | 387.7 | 396.6 | 3.0 | 0.306x | 14.945x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,280.1 | 1,263.2 | 1,288.8 | 8.8 | 1.000x | 48.790x |

### `orig` / `s-081` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.193x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 11.2 | 11.2 | 11.3 | 0.0 | 0.384x | 1.996x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 11.2 | 11.2 | 13.3 | 0.8 | 0.385x | 1.996x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 13.7 | 13.6 | 13.9 | 0.1 | 0.470x | 2.442x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 15.5 | 15.5 | 15.7 | 0.1 | 0.530x | 2.753x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 28.9 | 28.9 | 29.1 | 0.1 | 0.991x | 5.141x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.2 | 29.2 | 29.3 | 0.0 | 1.000x | 5.191x |

### `orig` / `s-081` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 5.1 | 5.0 | 5.1 | 0.0 | 0.166x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 5.1 | 5.1 | 5.1 | 0.0 | 0.169x | 1.014x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 5.6 | 5.6 | 5.6 | 0.0 | 0.185x | 1.113x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 16.1 | 15.4 | 17.0 | 0.5 | 0.528x | 3.179x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 17.2 | 17.1 | 17.3 | 0.1 | 0.566x | 3.403x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.4 | 30.2 | 31.0 | 0.4 | 1.000x | 6.017x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 37.5 | 34.9 | 48.5 | 4.8 | 1.230x | 7.403x |

### `orig` / `s-082` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 5.6 | 5.6 | 5.6 | 0.0 | 0.188x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 10.5 | 10.3 | 10.7 | 0.1 | 0.349x | 1.860x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 10.6 | 10.3 | 11.2 | 0.3 | 0.354x | 1.886x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 14.9 | 14.8 | 16.1 | 0.5 | 0.496x | 2.642x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.2 | 0.0 | 0.538x | 2.867x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.6 | 28.9 | 29.8 | 0.3 | 0.987x | 5.256x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.0 | 29.6 | 30.2 | 0.2 | 1.000x | 5.327x |

### `orig` / `s-082` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 5.6 | 5.6 | 5.6 | 0.0 | 0.182x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 5.9 | 5.9 | 6.0 | 0.0 | 0.190x | 1.049x |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 5.9 | 5.6 | 6.0 | 0.2 | 0.191x | 1.052x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 24.0 | 23.9 | 24.9 | 0.4 | 0.773x | 4.256x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 24.6 | 24.5 | 24.7 | 0.1 | 0.792x | 4.362x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 31.0 | 31.0 | 35.1 | 1.6 | 1.000x | 5.509x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 38.8 | 36.4 | 49.7 | 4.9 | 1.250x | 6.887x |

### `orig` / `s-083` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.0 | 12.0 | 12.2 | 0.1 | 0.312x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.3 | 11.9 | 13.0 | 0.4 | 0.319x | 1.024x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 21.4 | 21.1 | 21.5 | 0.1 | 0.553x | 1.775x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 21.5 | 21.3 | 21.9 | 0.2 | 0.558x | 1.789x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 26.0 | 25.3 | 26.9 | 0.6 | 0.674x | 2.161x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 36.3 | 35.2 | 40.6 | 1.9 | 0.939x | 3.013x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 38.6 | 35.7 | 41.6 | 2.4 | 1.000x | 3.208x |

### `orig` / `s-083` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 37.0 | 36.6 | 40.7 | 1.5 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 38.4 | 37.0 | 50.0 | 5.1 | 1.038x | 1.038x |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 73.2 | 72.7 | 91.2 | 7.3 | 1.981x | 1.981x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 73.5 | 73.0 | 74.0 | 0.3 | 1.989x | 1.989x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 97.3 | 96.7 | 97.6 | 0.4 | 2.631x | 2.631x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 631.4 | 612.7 | 634.3 | 8.4 | 17.083x | 17.083x |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 631.5 | 615.5 | 636.3 | 7.1 | 17.086x | 17.086x |

### `orig` / `s-084` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 19.1 | 19.0 | 19.3 | 0.1 | 0.505x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 19.1 | 19.1 | 19.1 | 0.0 | 0.506x | 1.001x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 20.6 | 20.6 | 20.7 | 0.1 | 0.545x | 1.078x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 22.8 | 22.8 | 22.8 | 0.0 | 0.603x | 1.193x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 34.6 | 34.1 | 35.2 | 0.4 | 0.915x | 1.811x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 37.8 | 35.2 | 40.1 | 1.8 | 1.000x | 1.978x |
| 7 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 38.2 | 38.2 | 39.0 | 0.3 | 1.010x | 1.998x |

### `orig` / `s-084` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 16.3 | 16.2 | 16.8 | 0.2 | 0.448x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 16.3 | 16.1 | 21.8 | 2.2 | 0.450x | 1.005x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 36.3 | 35.7 | 40.3 | 1.7 | 1.000x | 2.231x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 36.5 | 36.1 | 49.7 | 5.2 | 1.006x | 2.245x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 38.2 | 38.2 | 38.5 | 0.1 | 1.053x | 2.351x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 122.4 | 122.0 | 123.4 | 0.5 | 3.376x | 7.532x |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 125.2 | 124.2 | 125.7 | 0.5 | 3.452x | 7.702x |

### `orig` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,700,507.0 | 3,619,299.0 | 3,704,156.4 | 32,418.7 | 0.129x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 4,143,067.6 | 4,138,287.6 | 4,145,910.0 | 2,566.5 | 0.145x | 1.120x |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 4,145,504.2 | 4,138,451.8 | 4,155,651.3 | 5,811.2 | 0.145x | 1.120x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 5,163,530.0 | 5,147,967.5 | 5,354,426.0 | 95,486.8 | 0.180x | 1.395x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 5,212,747.8 | 5,161,372.5 | 5,280,790.8 | 38,070.8 | 0.182x | 1.409x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 6,366,900.5 | 6,355,186.0 | 6,407,762.0 | 20,748.8 | 0.222x | 1.721x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28,638,016.7 | 28,601,379.1 | 29,677,306.8 | 409,825.4 | 1.000x | 7.739x |

### `orig` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,983.0 | 17,950.2 | 18,048.6 | 35.9 | 1.000x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,865,231.4 | 1,861,637.8 | 1,865,867.4 | 1,625.3 | 103.722x | 103.722x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,886,626.1 | 1,884,160.2 | 1,893,248.5 | 3,282.7 | 104.911x | 104.911x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,888,425.7 | 1,882,099.8 | 1,895,233.4 | 4,283.3 | 105.012x | 105.012x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,559,712.1 | 2,540,969.5 | 2,565,705.2 | 11,254.9 | 142.340x | 142.340x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 15,952,602.5 | 15,917,725.0 | 16,155,096.2 | 94,524.8 | 887.092x | 887.092x |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 16,016,333.2 | 15,937,597.8 | 16,137,634.0 | 70,453.1 | 890.636x | 890.636x |

### `orig` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,933.2 | 17,893.8 | 18,022.1 | 43.7 | 1.000x | 1.000x | 5 | 100% |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,868,705.8 | 1,868,221.4 | 1,869,819.8 | 555.3 | 104.204x | 104.204x | 5 | 100% |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,874,718.0 | 1,873,042.1 | 1,877,736.8 | 1,559.0 | 104.539x | 104.539x | 5 | 100% |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,875,434.8 | 1,874,578.9 | 1,878,094.8 | 1,286.7 | 104.579x | 104.579x | 5 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,818,428.0 | 2,816,233.6 | 2,822,301.8 | 2,573.3 | 157.163x | 157.163x | 5 | 100% |

### `orig` / `t-d-prose-sparse-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,942,459.5 | 1,939,161.1 | 1,946,073.1 | 2,539.5 | 0.021x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 3,132,783.4 | 3,123,338.6 | 3,158,184.1 | 12,869.3 | 0.033x | 1.613x |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 3,137,025.9 | 3,127,305.3 | 3,169,706.7 | 14,761.9 | 0.033x | 1.615x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 5,966,791.7 | 5,961,199.2 | 6,000,178.1 | 14,414.3 | 0.064x | 3.072x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 16,455,517.8 | 16,410,732.5 | 16,633,663.5 | 80,630.8 | 0.175x | 8.471x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 16,565,636.5 | 16,520,533.8 | 16,597,341.8 | 28,027.7 | 0.176x | 8.528x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 93,901,018.6 | 93,759,164.2 | 99,292,858.2 | 2,164,943.1 | 1.000x | 48.341x |

### `orig` / `t-e-prose-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,971.3 | 17,957.5 | 17,984.6 | 10.9 | 1.000x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,869,164.2 | 1,866,891.0 | 1,876,262.2 | 3,331.0 | 104.008x | 104.008x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 3,083,466.1 | 3,077,274.2 | 3,122,459.8 | 16,433.7 | 171.577x | 171.577x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 3,094,842.2 | 3,082,737.4 | 3,099,917.5 | 5,819.4 | 172.210x | 172.210x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,159,050.0 | 3,155,013.8 | 3,180,387.1 | 9,183.7 | 175.783x | 175.783x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 16,539,120.5 | 16,498,440.2 | 16,567,440.8 | 25,302.1 | 920.306x | 920.306x |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 16,544,026.5 | 16,521,651.2 | 16,598,829.2 | 28,000.0 | 920.579x | 920.579x |

## Excluded from ranking (expectation-failing cells)

| pattern | subject | regime | form | testee | n | pass-rate | gave-up | wrong | outcomes |
|---|---|---|---|---|---|---|---|---|---|
| `factored` | `s-058` | `match-compliance` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-059` | `match-compliance` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-061` | `match-compliance` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-063` | `match-compliance` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-064` | `match-compliance` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 5 | 0% | 0 | 0 | timed-out=5 |
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `orig` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `orig` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |

## Compile cost (by execution-model class; never pooled across classes)

### `compiled-aot`

- `pcrec_25b1984f_auto-caps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_vm-caps-simdna` / `factored` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 39,546 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `factored` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 39,654 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `floor` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 236 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `floor` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 339 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `orig` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 28,839 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `orig` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 28,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `factored` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 39,546 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `factored` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 39,654 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `floor` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 236 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `floor` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 339 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `orig` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 28,839 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `orig` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 28,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
    - sel = pcrec's `RX_ENGINE_SEL`; `DFA fallback tripped` = sel not in (selected, forced), and NOTHING else -- since pcrec 263b013 ([LIM-1] / [OPT-4.1]) every fallback has its own token (`overflowed-dfa`, `overflowed-prefilter`, `collapsed-prefilter`, `declined-nullable`, `size-cap-retry`), the size-cap rescue included; at pcrec 96e44c2 that rescue stamped `sel=selected` and only its `lang=count-collapsed (size cap retry, ...)` clause says so.
    - K = pcrec's `RX_UNROLL_K`/`_WHY`: the VM counter rung's unroll factor and who chose it (default / option / denied / size-model / size-model-declined / cap-rescue / capacity-declined -- limits.md 8); caps = the EFFECTIVE `RX_MAX_EMIT_CODE_BYTES`/`RX_MAX_EMIT_BYTES` the artifact was built under (raise-only; 500,000/1,000,000 by default). VM artifacts only: a DFA artifact has no counter rung and stamps no code cap.
    - edge = pcrec's `RX_DFA_SCAN_EDGE` ([OPT-5] STEP 1, abi 13+), how a DFA scan tests a SCAN EDGE's byte class: `range` = a contiguous run (subtract-and-compare against two immediates); `bitmap` = a non-contiguous class (a 256-byte membership read); `mixed` = one artifact whose machines took both forms; `none` = no collapsible run (an attempt/empty scan, or -fno-scan-edge).
    - edges = pcrec's `scan_edges` ([B32]): how many [OPT-5] SCAN EDGES this artifact's SEARCH-side machines carry (`rx_search`/`rx_prefilter`), the per-scan-iteration compare-count covariate `edge`'s single shape token cannot separate (I-33: the cost is one compare per edge per iteration); the `(match: M)` parenthetical, when carried, is the SAME count on the anchored `rx_match` machine, kept apart because the measured [OPT-EDGE] regression is search-band only. `0` is a real, recorded value.
    - start = pcrec's `RX_DFA_START` ([OPT-5] STEP 2, abi 16+), how the SEARCH entry recovers the match START: `pinned` = the forward machine's start state accepts unconditionally, so the match provably begins at `search_from` and THE ARTIFACT CARRIES NO REVERSE MACHINE at all (no reverse tables, accessor block or scan loop); `reverse-pass` = it carries one and walks it backwards from the match end. The two forms are ANSWER-IDENTICAL by contract -- `caps[0][0]`'s absolute offsets and the zero-length-match convention hold under both -- so this explains a row's SIZE and pass count, never its answer.
    - frameless = pcrec's `RX_VM_FRAMELESS` ([OPT-VMFL], abi 16+): `1` iff this VM program emits NO push site and no linked call, so its fail label carries no pop-and-resume dispatch; `0` otherwise. VM artifacts only, hybrids included -- a DIFFERENT scope from `start=`, though the two stamps arrived at one abi. It is NOT `buffers=`'s resume-frame CAPACITY and the two can disagree: the capacity is what the artifact was SIZED for, this is what its program CONTAINS. `0` is a real, recorded value.
    - folds = pcrec's `RX_DFA_UNIFORM_FOLDS` ([CC-DIFF] STEP 1, abi 17+): how many of this artifact's DFA tables (two per machine it contains -- forward always, reverse unless `start=pinned`, anchored under `match=unwrapped`; so 0..6) had ALL-EQUAL cells and were NOT EMITTED, the accessor returning the constant. `table=` keeps naming the encoding that was SELECTED, so `premultiplied` beside `folds=4` is an artifact carrying NO transition table at all -- a SIZE fact, never an answer one. `0` is a real, recorded value.
    - islands = pcrec's `RX_VM_ALT_ISLANDS` ([ENG-ISL] STEP 1, abi 18+): how many of this VM program's flat alternations were lowered as an ALTERNATION ISLAND -- a trie dispatch over the alternatives' literal bytes -- instead of vm_alt's serial resume chain (one frame per untried branch). Selected per alternation on its LANGUAGE (a finite literal set), so a COUNT; a caseless, prefix-bearing-under-four-words or over-budget alternation is declined as a selection outcome. This is what removes the branch-ORDER effect (altwide srt-256 vs w-256) at the source; `-fno-alt-island` is the sibling that reads `0` at the same pin. `0` is a real, recorded value.
    - shape = pcrec's `RX_VM_ENTRY_SHAPE` with `RX_VM_PROGRAM_BYTES` in the parenthetical ([CC-DIFF] STEP 2, abi 22+): the entry-chain rung the emitter TOOK for the six entries -- `plain` (one body, six framed entries), `shared` (one out-of-line body behind three forwarding entries), `forward` (three bodies in the three `_in` entries, no canary anywhere), `inline` (six bodies) -- and the program size AUTO compared against VM_INLINE_CHAIN_MAX_BYTES (4,096 B) to choose it: `forward` at or below, `shared` above; `inline`/`plain` where a forward rung is illegal (the program writes its storage); a FRAMED program (`frameless=0`) is `plain` whatever the size. ANSWER-IDENTICAL across every value -- only the scaffolding above the first label moves -- so a COST and SIZE fact; the number is what makes the token checkable. `prog: N B` is the VM PROGRAM REGION with its COMMENTS INCLUDED (the raw length of the emitter's program buffer; the island trie writes a per-node comment), NOT the `code bytes` columns' quantity -- those and `--max-emit-code-bytes` count the whole .c+.h with every comment EXCLUDED -- so the program stamp can exceed the code bytes (w-256: 305,686 vs 292,043) and neither is wrong; for cap reasoning use the code bytes (pcrec I-50 1).
    - clsfolds = pcrec's `RX_VM_CLS_FOLDS` ([FORM-CHAR] STEP 1, abi 23+): how many of this VM program's class-pool entries take the ASCII-FOLD membership test -- a two-member set differing only in bit 0x20, both letters (what `(?i)` makes of a letter at parse time), tested as `(byte | 0x20) == lower` with NO 32-byte bitmap table emitted for it. Chosen per pool class, so a COUNT; a set that is not exactly two members, not a 0x20 pair, or a 0x20 pair of non-letters keeps its bitmap. A SIZE fact (one table per fold class gone, plus the test text), never an answer one: the fold compare and the bitmap read are the same predicate over the pair's two bytes. VM route only -- an `auto` row that selected the DFA prints no clause even on a `(?i)` pattern; `-fno-cls-fold` is the sibling that reads `0` at the same pin. `0` is a real, recorded value.

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | emit bytes | code bytes | jitter | outcomes | emit-c ns | gcc ns | load ns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 173,526,814.0 | 164,766,687.0 | 181,490,745.0 | 6,338,789.0 | 5 | 48,128 | 82,643 | 13,949 | 0.037 (max is trial 1) | compiled=5 | 10,395,046.0 | 160,879,176.0 | 189,471.0 |
| `factored` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 186,029,821.0 | 170,466,739.0 | 206,000,837.0 | 11,357,854.9 | 5 | 48,264 | 94,854 | 15,865 | 0.061 | compiled=5 | 12,996,749.0 | 172,858,711.0 | 174,361.0 |
| `factored` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 168,681,429.0 | 156,403,863.0 | 181,503,177.0 | 8,812,007.3 | 5 | 48,128 | 82,460 | 13,762 | 0.052 (max is trial 1) | compiled=5 | 10,525,176.0 | 156,384,723.0 | 189,021.0 |
| `factored` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 181,271,647.0 | 178,884,604.0 | 182,453,363.0 | 1,282,469.9 | 5 | 48,264 | 94,671 | 15,678 | 0.007 (max is trial 1) | compiled=5 | 12,978,020.0 | 166,770,179.0 | 110,180.0 |
| `factored` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 571,637,701.0 | 557,575,008.0 | 575,374,422.0 | 6,300,976.6 | 5 | 39,936 | 58,762 | 57,208 | 0.011 | compiled=5 | 2,270,593.0 | 566,253,219.0 | 193,121.0 |
| `factored` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 566,462,271.0 | 562,968,250.0 | 594,057,801.0 | 12,339,418.7 | 5 | 39,936 | 58,878 | 57,324 | 0.022 | compiled=5 | 4,766,337.0 | 561,527,712.0 | 92,481.0 |
| `factored` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 573,406,753.0 | 560,698,170.0 | 588,568,428.0 | 9,061,480.9 | 5 | 39,936 | 58,762 | 57,208 | 0.016 | compiled=5 | 2,286,311.0 | 570,885,651.0 | 195,401.0 |
| `factored` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 573,429,854.0 | 568,076,198.0 | 577,436,234.0 | 3,411,473.3 | 5 | 39,936 | 58,878 | 57,324 | 0.006 | compiled=5 | 2,301,011.0 | 571,018,422.0 | 110,421.0 |
| `floor` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 150,392,660.0 | 141,045,572.0 | 152,132,871.0 | 3,925,733.9 | 5 | 27,608 | 18,294 | 13,297 | 0.026 | compiled=5 | 1,681,089.0 | 148,544,911.0 | 113,721.0 |
| `floor` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 159,682,441.0 | 152,028,068.0 | 176,186,068.0 | 8,194,139.2 | 5 | 27,752 | 20,637 | 15,314 | 0.051 | compiled=5 | 1,710,609.0 | 155,587,679.0 | 187,651.0 |
| `floor` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 147,937,338.0 | 140,196,106.0 | 153,161,896.0 | 4,472,283.5 | 5 | 27,608 | 18,294 | 13,297 | 0.030 | compiled=5 | 1,665,219.0 | 146,008,117.0 | 98,841.0 |
| `floor` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 159,648,271.0 | 149,105,894.0 | 164,562,937.0 | 5,277,252.6 | 5 | 27,752 | 20,637 | 15,314 | 0.033 | compiled=5 | 1,797,069.0 | 157,121,978.0 | 187,311.0 |
| `floor` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 134,754,625.0 | 125,109,458.0 | 141,177,793.0 | 6,732,611.9 | 5 | 23,072 | 17,837 | 17,837 | 0.050 | compiled=5 | 1,447,328.0 | 133,138,416.0 | 107,971.0 |
| `floor` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 137,947,814.0 | 128,667,100.0 | 144,615,432.0 | 5,824,084.4 | 5 | 23,072 | 17,948 | 17,948 | 0.042 | compiled=5 | 1,440,808.0 | 136,275,634.0 | 105,560.0 |
| `floor` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 136,660,116.0 | 131,490,790.0 | 142,668,874.0 | 4,334,978.6 | 5 | 23,072 | 17,837 | 17,837 | 0.032 | compiled=5 | 1,643,548.0 | 133,541,640.0 | 192,511.0 |
| `floor` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 133,836,271.0 | 129,480,890.0 | 139,214,469.0 | 4,000,255.9 | 5 | 23,072 | 17,948 | 17,948 | 0.030 (max is trial 1) | compiled=5 | 1,446,067.0 | 132,247,174.0 | 187,101.0 |
| `orig` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 173,309,253.0 | 165,686,853.0 | 178,341,950.0 | 4,878,175.1 | 5 | 48,088 | 82,236 | 13,709 | 0.028 | compiled=5 | 9,909,873.0 | 156,121,711.0 | 185,431.0 |
| `orig` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 183,255,716.0 | 172,385,108.0 | 186,693,395.0 | 4,956,690.6 | 5 | 48,224 | 94,447 | 15,625 | 0.027 (max is trial 1) | compiled=5 | 12,300,625.0 | 167,948,045.0 | 116,710.0 |
| `orig` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 179,676,289.0 | 159,232,408.0 | 190,602,777.0 | 12,059,362.9 | 5 | 48,088 | 82,236 | 13,709 | 0.067 (max is trial 1) | compiled=5 | 12,042,185.0 | 166,726,229.0 | 186,401.0 |
| `orig` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 180,355,242.0 | 172,212,788.0 | 196,159,277.0 | 7,844,183.0 | 5 | 48,224 | 94,447 | 15,625 | 0.043 (max is trial 1) | compiled=5 | 12,109,145.0 | 166,968,820.0 | 190,301.0 |
| `orig` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 446,696,252.0 | 442,685,129.0 | 449,710,861.0 | 2,531,966.7 | 5 | 35,760 | 47,591 | 46,204 | 0.006 (max is trial 1) | compiled=5 | 3,780,542.0 | 442,800,800.0 | 190,731.0 |
| `orig` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 439,876,962.0 | 429,616,723.0 | 446,978,854.0 | 5,741,717.6 | 5 | 35,760 | 47,709 | 46,322 | 0.013 (max is trial 1) | compiled=5 | 2,021,122.0 | 437,670,750.0 | 105,661.0 |
| `orig` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 439,646,101.0 | 432,618,487.0 | 448,206,325.0 | 5,990,601.0 | 5 | 35,760 | 47,591 | 46,204 | 0.014 | compiled=5 | 2,315,571.0 | 435,607,032.0 | 109,971.0 |
| `orig` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 438,950,479.0 | 438,450,046.0 | 441,788,012.0 | 1,181,345.0 | 5 | 35,760 | 47,709 | 46,322 | 0.003 | compiled=5 | 2,027,140.0 | 436,816,828.0 | 109,560.0 |

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

