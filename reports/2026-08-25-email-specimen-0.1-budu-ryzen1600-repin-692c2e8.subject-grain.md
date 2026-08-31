# pcrec-bench report

reporter: v10 (2026-08-31)

## Query

- filters: subbench=email-specimen, version=0.1
- record source: store/index.tsv (68 candidate file(s))
- records included: 9
    - `email-specimen@0.1__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260825T221651Z` (store/records/email-specimen@0.1/libpcre2_10.46_interp-caps-simdna/email-specimen@0.1__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260825T221651Z.jsonl) — agreement: n/a (v1.2)
    - `email-specimen@0.1__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260825T174132Z` (store/records/email-specimen@0.1/libpcre2_10.46_jit-caps-simdna/email-specimen@0.1__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260825T174132Z.jsonl) — agreement: n/a (v1.1)
    - `email-specimen@0.1__pcrec_692c2e8_auto-caps-simdna__budu-ryzen1600__20260825T222422Z` (store/records/email-specimen@0.1/pcrec_692c2e8_auto-caps-simdna/email-specimen@0.1__pcrec_692c2e8_auto-caps-simdna__budu-ryzen1600__20260825T222422Z.jsonl) — agreement: n/a (v1.2)
    - `email-specimen@0.1__pcrec_692c2e8_auto-nocaps-simdna__budu-ryzen1600__20260825T222840Z` (store/records/email-specimen@0.1/pcrec_692c2e8_auto-nocaps-simdna/email-specimen@0.1__pcrec_692c2e8_auto-nocaps-simdna__budu-ryzen1600__20260825T222840Z.jsonl) — agreement: n/a (v1.2)
    - `email-specimen@0.1__pcrec_692c2e8_vm-caps-simdna__budu-ryzen1600__20260825T175933Z` (store/records/email-specimen@0.1/pcrec_692c2e8_vm-caps-simdna/email-specimen@0.1__pcrec_692c2e8_vm-caps-simdna__budu-ryzen1600__20260825T175933Z.jsonl) — agreement: n/a (v1.1)
    - `email-specimen@0.1__pcrec_692c2e8_vm-in-caps-simdna__budu-ryzen1600__20260825T180451Z` (store/records/email-specimen@0.1/pcrec_692c2e8_vm-in-caps-simdna/email-specimen@0.1__pcrec_692c2e8_vm-in-caps-simdna__budu-ryzen1600__20260825T180451Z.jsonl) — agreement: n/a (v1.1)
    - `email-specimen@0.1__pcrec_8da6120_auto-caps-simdna__budu-ryzen1600__20260825T065046Z` (store/records/email-specimen@0.1/pcrec_8da6120_auto-caps-simdna/email-specimen@0.1__pcrec_8da6120_auto-caps-simdna__budu-ryzen1600__20260825T065046Z.jsonl) — agreement: n/a (v1.1)
    - `email-specimen@0.1__pcrec_8da6120_auto-nocaps-simdna__budu-ryzen1600__20260825T063943Z` (store/records/email-specimen@0.1/pcrec_8da6120_auto-nocaps-simdna/email-specimen@0.1__pcrec_8da6120_auto-nocaps-simdna__budu-ryzen1600__20260825T063943Z.jsonl) — agreement: n/a (v1.1)
    - `email-specimen@0.1__pcrec_8da6120_vm-caps-simdna__budu-ryzen1600__20260825T064436Z` (store/records/email-specimen@0.1/pcrec_8da6120_vm-caps-simdna/email-specimen@0.1__pcrec_8da6120_vm-caps-simdna__budu-ryzen1600__20260825T064436Z.jsonl) — agreement: n/a (v1.1)
- superseded: 5 record(s) (OD-B15; --all-records lists them)
- sub-bench version(s): email-specimen@0.1
- machine(s): budu-ryzen1600
- schema version(s): 1.1, 1.2
- grain: subject (per pattern x subject x regime; the drill-down)
- reduction: median/min/max/stddev (population) over per-trial `elapsed_ns / iterations`; lazy-JIT compile cost is DERIVED as first-match-row-minus-steady-state (lowest `seq` timed row for the pattern, minus the median of every other timed row), one value per (pattern, testee), never pooled with another execution-model class's compile cost
- `form`: this report includes a `whole-subject` artifact beside `plain` for at least one cell (schema v1.1: a testee with no end-anchored mode compiles and times a SEPARATE artifact for match-compliance, e.g. `(?:pattern)\z`, where another testee reaches the same regime via runtime flags on its ordinary artifact) -- shown as a per-row COLUMN, not a split: both forms answer the same regime and RANK TOGETHER in one table (`form` is a key only for compile-cost rows, where a whole-subject artifact is genuinely a separate compile with its own cost); `fact` restates it as 'same program' / 'separate artifact' (R4)
- status policy (OD-B14): a ranking row whose record `status` is not `measured` is excluded from ranking by default, listed under its table as `not ranked: <testee> -- <status> (<status_detail excerpt>)`; `--include-unmeasured` ranks it instead, with `status` shown
- trial-agreement policy (schema v1.4, rule v1.4-group, X31-X33): a record's five trials must agree to within k=1.5 on every group of its rows — one slow trial of five tolerated; two, or one fast, is a disagreeing row; a group disagrees at >= 2 disagreeing rows reaching a third of it (d_min=2, c=3); a record with a disagreeing group, or with fewer than five odd trials, is `inconclusive-spread` and unranked like `inconclusive-load`; the after-run load/occupancy samples are provenance (v1.4 X13), shown under --include-provenance
- status rule: v1.1-1.3 X13 (both samples quiet) on 9 record(s)
- tier policy (R3, schema v1.2 `tier`, absent = `pinned`): a `scratch`-tier row is excluded from ranking by default, listed as `scratch: <testee>`; `--include-scratch` ranks it instead, with a `tier` column
- duplicate-record policy (OD-B15, amended 2026-08-25): the NEWEST MEASURED record per (subbench@version, testee_id, machine) ranks by default -- a newer record that is NOT measured does not supersede a measured one of the same testee and version (listed as "newer, not measured" instead); only when no record in the group is measured does the newest record overall stand (itself unranked per the status policy above, unless --include-unmeasured). `--all-records` shows every record as its own row, its testee id suffixed `@<timestamp>`

## Ranking (per pattern x subject x regime; best median first)

### `factored` / `s-000` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 111.6 | 111.2 | 112.2 | 0.3 | 0.128x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 131.1 | 130.5 | 131.7 | 0.4 | 0.150x | 1.174x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 148.9 | 147.4 | 149.6 | 0.9 | 0.171x | 1.333x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 320.6 | 307.5 | 329.7 | 9.4 | 0.367x | 2.871x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 466.9 | 421.0 | 495.7 | 25.2 | 0.535x | 4.182x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 490.2 | 483.1 | 536.9 | 20.1 | 0.562x | 4.390x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 500.9 | 494.5 | 502.4 | 3.0 | 0.574x | 4.486x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 862.1 | 861.7 | 879.0 | 7.5 | 0.988x | 7.722x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 872.7 | 868.0 | 875.9 | 3.3 | 1.000x | 7.817x |

### `factored` / `s-000` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 103.6 | 103.2 | 104.4 | 0.4 | 0.120x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 107.3 | 107.0 | 109.1 | 0.8 | 0.124x | 1.035x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 153.1 | 152.2 | 153.3 | 0.4 | 0.177x | 1.477x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 155.0 | 154.3 | 156.5 | 0.8 | 0.179x | 1.496x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 330.5 | 321.2 | 338.9 | 6.4 | 0.382x | 3.190x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 430.7 | 416.6 | 504.6 | 31.6 | 0.498x | 4.157x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 464.5 | 445.4 | 495.6 | 17.8 | 0.537x | 4.483x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 467.6 | 450.4 | 488.3 | 13.3 | 0.540x | 4.513x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 865.7 | 857.6 | 871.9 | 5.2 | 1.000x | 8.355x |

### `factored` / `s-001` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 144.2 | 143.8 | 144.4 | 0.2 | 0.118x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 164.5 | 163.9 | 164.6 | 0.3 | 0.134x | 1.141x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 203.5 | 201.8 | 207.1 | 1.8 | 0.166x | 1.412x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 379.2 | 369.0 | 402.7 | 13.0 | 0.310x | 2.630x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 506.6 | 493.4 | 538.1 | 15.3 | 0.414x | 3.514x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 584.4 | 572.0 | 619.1 | 16.2 | 0.477x | 4.054x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 600.3 | 562.6 | 692.0 | 46.5 | 0.490x | 4.164x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,218.9 | 1,212.4 | 1,234.3 | 9.2 | 0.995x | 8.454x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,224.4 | 1,212.7 | 1,229.6 | 6.2 | 1.000x | 8.493x |

### `factored` / `s-001` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 135.6 | 135.3 | 136.4 | 0.4 | 0.112x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 139.3 | 139.2 | 169.5 | 12.0 | 0.115x | 1.027x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 175.6 | 175.4 | 176.3 | 0.4 | 0.144x | 1.294x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 208.4 | 208.0 | 210.5 | 1.1 | 0.172x | 1.536x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 392.5 | 374.8 | 402.2 | 10.5 | 0.323x | 2.894x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 520.6 | 492.6 | 536.5 | 19.3 | 0.428x | 3.838x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 551.7 | 511.9 | 579.7 | 29.3 | 0.454x | 4.067x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 563.7 | 533.3 | 597.8 | 26.8 | 0.464x | 4.156x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,215.1 | 1,204.9 | 1,225.4 | 7.5 | 1.000x | 8.959x |

### `factored` / `s-002` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 46.3 | 46.0 | 46.5 | 0.2 | 0.061x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 67.0 | 66.3 | 67.1 | 0.3 | 0.089x | 1.448x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 103.0 | 102.8 | 103.7 | 0.3 | 0.137x | 2.223x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 279.0 | 274.8 | 302.6 | 12.1 | 0.370x | 6.023x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 430.1 | 380.9 | 443.6 | 22.1 | 0.571x | 9.287x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 431.3 | 408.0 | 454.4 | 17.8 | 0.572x | 9.312x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 452.3 | 402.1 | 485.4 | 31.1 | 0.600x | 9.767x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 750.8 | 744.0 | 756.2 | 4.4 | 0.997x | 16.211x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 753.4 | 751.1 | 761.9 | 4.0 | 1.000x | 16.266x |

### `factored` / `s-002` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 38.7 | 38.1 | 38.8 | 0.2 | 0.051x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 42.2 | 42.0 | 42.5 | 0.2 | 0.056x | 1.090x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 106.5 | 106.4 | 109.6 | 1.3 | 0.141x | 2.751x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 121.0 | 119.9 | 122.8 | 1.1 | 0.160x | 3.125x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 269.7 | 264.1 | 292.4 | 10.0 | 0.357x | 6.964x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 350.0 | 299.7 | 478.7 | 64.0 | 0.464x | 9.038x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 375.7 | 371.4 | 488.0 | 48.1 | 0.498x | 9.703x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 390.2 | 355.6 | 453.4 | 33.1 | 0.517x | 10.077x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 755.1 | 746.2 | 761.7 | 5.2 | 1.000x | 19.499x |

### `factored` / `s-003` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 157.2 | 156.8 | 158.5 | 0.6 | 0.120x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 176.5 | 176.3 | 176.8 | 0.2 | 0.134x | 1.123x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 215.8 | 214.2 | 219.0 | 1.6 | 0.164x | 1.372x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 428.8 | 379.5 | 445.9 | 23.3 | 0.326x | 2.727x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 590.8 | 545.4 | 621.1 | 27.6 | 0.450x | 3.758x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 652.5 | 596.4 | 727.2 | 43.3 | 0.496x | 4.150x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 660.6 | 595.4 | 709.3 | 47.2 | 0.503x | 4.202x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,314.2 | 1,310.1 | 1,340.1 | 11.2 | 1.000x | 8.359x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,324.6 | 1,315.1 | 1,340.3 | 9.8 | 1.008x | 8.425x |

### `factored` / `s-003` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 148.3 | 147.8 | 148.8 | 0.4 | 0.113x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 151.6 | 151.4 | 152.1 | 0.3 | 0.115x | 1.023x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 185.1 | 184.7 | 185.6 | 0.3 | 0.140x | 1.248x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 219.0 | 218.6 | 223.6 | 1.9 | 0.166x | 1.477x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 411.6 | 381.9 | 425.4 | 14.3 | 0.312x | 2.776x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 566.9 | 558.6 | 680.0 | 46.1 | 0.430x | 3.823x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 581.7 | 557.8 | 636.4 | 27.8 | 0.441x | 3.923x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 626.4 | 601.0 | 665.6 | 22.0 | 0.475x | 4.225x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,317.6 | 1,307.7 | 1,325.5 | 7.0 | 1.000x | 8.886x |

### `factored` / `s-004` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 167.3 | 167.1 | 168.1 | 0.4 | 0.189x | 1.000x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 222.2 | 221.4 | 223.4 | 0.7 | 0.252x | 1.328x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 241.9 | 240.9 | 244.5 | 1.2 | 0.274x | 1.446x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 375.5 | 369.8 | 378.2 | 2.7 | 0.425x | 2.245x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 529.9 | 476.0 | 572.3 | 34.4 | 0.600x | 3.168x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 572.3 | 517.2 | 584.7 | 27.5 | 0.648x | 3.421x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 611.8 | 531.7 | 657.6 | 46.0 | 0.693x | 3.657x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 883.3 | 878.6 | 889.9 | 3.8 | 1.000x | 5.280x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 887.0 | 870.4 | 892.6 | 9.9 | 1.004x | 5.302x |

### `factored` / `s-004` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 167.3 | 166.6 | 175.7 | 3.4 | 0.190x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 171.9 | 171.3 | 172.2 | 0.4 | 0.195x | 1.028x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 214.2 | 214.1 | 214.8 | 0.3 | 0.243x | 1.280x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 217.0 | 216.8 | 225.1 | 3.2 | 0.246x | 1.297x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 365.7 | 346.7 | 371.5 | 11.0 | 0.414x | 2.186x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 508.5 | 458.7 | 540.8 | 31.9 | 0.576x | 3.040x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 511.9 | 467.4 | 559.7 | 31.3 | 0.580x | 3.059x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 544.3 | 524.8 | 550.2 | 10.3 | 0.617x | 3.253x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 882.9 | 865.8 | 893.7 | 9.1 | 1.000x | 5.277x |

### `factored` / `s-005` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 46.0 | 45.3 | 46.5 | 0.4 | 0.061x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 66.7 | 66.5 | 67.0 | 0.2 | 0.089x | 1.451x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 102.8 | 102.7 | 103.1 | 0.1 | 0.137x | 2.236x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 299.0 | 270.4 | 325.7 | 17.7 | 0.398x | 6.504x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 429.2 | 380.7 | 544.8 | 55.3 | 0.571x | 9.335x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 451.3 | 416.5 | 483.3 | 24.7 | 0.601x | 9.817x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 453.9 | 404.4 | 469.4 | 22.6 | 0.604x | 9.872x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 749.7 | 740.7 | 756.1 | 5.4 | 0.998x | 16.307x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 751.5 | 741.9 | 761.2 | 7.2 | 1.000x | 16.345x |

### `factored` / `s-005` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 38.9 | 38.7 | 39.0 | 0.1 | 0.052x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 42.1 | 41.9 | 42.2 | 0.1 | 0.056x | 1.082x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 106.7 | 106.3 | 107.1 | 0.3 | 0.142x | 2.744x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 121.5 | 120.0 | 123.5 | 1.2 | 0.162x | 3.122x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 298.4 | 283.9 | 327.3 | 14.3 | 0.397x | 7.669x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 384.6 | 316.6 | 486.6 | 54.4 | 0.511x | 9.884x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 398.4 | 358.1 | 585.4 | 82.4 | 0.530x | 10.239x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 413.5 | 346.1 | 452.2 | 36.5 | 0.550x | 10.628x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 752.0 | 742.8 | 756.7 | 5.8 | 1.000x | 19.328x |

### `factored` / `s-006` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 103.8 | 103.5 | 105.5 | 0.7 | 0.077x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 124.0 | 123.7 | 124.0 | 0.1 | 0.092x | 1.194x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 221.4 | 220.5 | 250.1 | 11.4 | 0.165x | 2.133x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 442.7 | 424.2 | 443.0 | 7.2 | 0.330x | 4.264x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 610.4 | 599.5 | 768.3 | 64.3 | 0.455x | 5.878x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 643.7 | 620.7 | 699.9 | 29.3 | 0.480x | 6.200x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 681.0 | 603.5 | 692.3 | 32.1 | 0.508x | 6.559x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,340.8 | 1,330.0 | 1,361.3 | 10.4 | 1.000x | 12.913x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,356.0 | 1,350.4 | 1,453.0 | 39.1 | 1.011x | 13.059x |

### `factored` / `s-006` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 96.6 | 96.3 | 99.9 | 1.4 | 0.072x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 99.9 | 99.5 | 101.0 | 0.5 | 0.074x | 1.034x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 165.5 | 164.5 | 173.6 | 3.3 | 0.123x | 1.713x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 227.7 | 226.7 | 229.3 | 1.0 | 0.170x | 2.357x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 440.5 | 410.8 | 444.6 | 12.6 | 0.328x | 4.559x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 603.5 | 597.0 | 676.6 | 36.1 | 0.449x | 6.246x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 618.0 | 585.7 | 699.6 | 37.9 | 0.460x | 6.397x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 671.0 | 665.0 | 695.0 | 12.3 | 0.500x | 6.946x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,342.6 | 1,334.0 | 1,362.0 | 9.3 | 1.000x | 13.897x |

### `factored` / `s-007` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 168.0 | 167.8 | 168.4 | 0.2 | 0.173x | 1.000x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 169.6 | 169.6 | 174.1 | 1.7 | 0.174x | 1.010x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 190.0 | 189.3 | 191.0 | 0.6 | 0.195x | 1.131x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 387.9 | 332.0 | 398.3 | 23.9 | 0.399x | 2.310x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 517.4 | 491.2 | 596.9 | 36.0 | 0.532x | 3.080x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 582.5 | 531.6 | 641.0 | 35.6 | 0.599x | 3.468x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 609.1 | 544.9 | 655.3 | 42.1 | 0.626x | 3.626x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 971.5 | 968.3 | 1,010.9 | 16.1 | 0.998x | 5.784x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 973.0 | 960.7 | 977.8 | 6.0 | 1.000x | 5.793x |

### `factored` / `s-007` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 162.4 | 161.7 | 162.4 | 0.3 | 0.167x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 165.4 | 165.3 | 166.5 | 0.5 | 0.170x | 1.019x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 172.8 | 172.3 | 175.4 | 1.1 | 0.178x | 1.064x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 173.5 | 172.5 | 190.9 | 7.1 | 0.179x | 1.069x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 383.4 | 370.8 | 388.9 | 6.5 | 0.395x | 2.362x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 512.1 | 492.5 | 573.0 | 30.3 | 0.527x | 3.154x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 567.2 | 546.3 | 586.4 | 14.4 | 0.584x | 3.493x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 576.3 | 496.7 | 595.9 | 41.2 | 0.593x | 3.549x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 971.0 | 961.1 | 980.8 | 7.2 | 1.000x | 5.981x |

### `factored` / `s-008` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 129.9 | 129.3 | 130.8 | 0.6 | 0.150x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 149.7 | 148.5 | 150.0 | 0.6 | 0.173x | 1.153x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 150.2 | 149.8 | 150.3 | 0.2 | 0.173x | 1.156x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 354.2 | 310.7 | 375.8 | 22.9 | 0.409x | 2.727x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 512.8 | 495.3 | 524.7 | 11.8 | 0.592x | 3.948x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 570.0 | 494.9 | 615.3 | 40.3 | 0.658x | 4.388x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 602.6 | 525.3 | 629.6 | 35.5 | 0.696x | 4.639x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 865.9 | 854.9 | 869.7 | 5.1 | 1.000x | 6.666x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 866.9 | 853.5 | 870.6 | 6.5 | 1.001x | 6.674x |

### `factored` / `s-008` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 122.9 | 122.7 | 123.2 | 0.2 | 0.142x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 126.7 | 126.5 | 127.0 | 0.2 | 0.146x | 1.031x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 154.6 | 153.9 | 154.9 | 0.3 | 0.178x | 1.259x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 158.6 | 158.1 | 159.7 | 0.5 | 0.183x | 1.291x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 368.2 | 357.5 | 382.3 | 8.3 | 0.425x | 2.996x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 486.7 | 461.1 | 548.0 | 29.5 | 0.561x | 3.961x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 499.0 | 440.8 | 545.0 | 39.9 | 0.576x | 4.061x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 531.7 | 460.3 | 603.6 | 50.1 | 0.613x | 4.327x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 867.0 | 862.2 | 873.2 | 3.8 | 1.000x | 7.057x |

### `factored` / `s-009` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 96.8 | 96.7 | 101.3 | 1.8 | 0.112x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 118.3 | 117.8 | 121.4 | 1.3 | 0.137x | 1.222x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 146.1 | 145.3 | 153.7 | 3.1 | 0.169x | 1.509x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 352.7 | 320.6 | 370.9 | 16.9 | 0.409x | 3.644x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 484.3 | 472.8 | 535.7 | 27.8 | 0.562x | 5.003x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 557.6 | 496.0 | 607.5 | 38.4 | 0.647x | 5.760x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 582.2 | 541.5 | 597.9 | 21.1 | 0.675x | 6.014x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 860.5 | 857.3 | 870.4 | 4.8 | 0.998x | 8.889x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 862.3 | 850.1 | 870.8 | 8.6 | 1.000x | 8.908x |

### `factored` / `s-009` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 90.1 | 89.7 | 90.2 | 0.2 | 0.105x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 93.5 | 93.4 | 95.1 | 0.6 | 0.109x | 1.038x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 148.4 | 147.5 | 151.1 | 1.3 | 0.174x | 1.646x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 150.4 | 150.2 | 152.1 | 0.7 | 0.176x | 1.668x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 362.6 | 353.5 | 374.8 | 7.5 | 0.424x | 4.023x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 469.9 | 421.4 | 507.0 | 32.2 | 0.550x | 5.213x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 472.8 | 462.0 | 541.1 | 29.7 | 0.553x | 5.246x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 529.4 | 501.8 | 566.8 | 22.6 | 0.619x | 5.873x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 854.6 | 848.3 | 858.2 | 3.5 | 1.000x | 9.481x |

### `factored` / `s-010` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 96.9 | 96.6 | 98.2 | 0.6 | 0.137x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 100.6 | 100.3 | 107.6 | 2.8 | 0.142x | 1.038x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 118.4 | 118.2 | 118.4 | 0.1 | 0.167x | 1.221x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 314.1 | 291.6 | 318.1 | 9.8 | 0.444x | 3.241x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 446.3 | 387.6 | 452.9 | 23.9 | 0.630x | 4.604x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 460.8 | 410.4 | 488.6 | 26.1 | 0.651x | 4.755x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 465.9 | 444.5 | 501.5 | 20.7 | 0.658x | 4.807x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 708.1 | 705.7 | 721.3 | 5.8 | 1.000x | 7.306x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 712.6 | 704.3 | 723.8 | 7.1 | 1.006x | 7.352x |

### `factored` / `s-010` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 90.2 | 89.8 | 90.7 | 0.3 | 0.127x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 93.5 | 93.4 | 94.3 | 0.4 | 0.131x | 1.037x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 106.4 | 106.3 | 106.7 | 0.1 | 0.149x | 1.180x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 121.0 | 120.4 | 121.7 | 0.5 | 0.170x | 1.341x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 296.5 | 252.0 | 332.4 | 26.5 | 0.416x | 3.288x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 388.8 | 361.6 | 476.7 | 40.5 | 0.546x | 4.312x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 417.0 | 340.2 | 472.0 | 44.3 | 0.585x | 4.623x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 428.2 | 406.4 | 516.4 | 38.8 | 0.601x | 4.748x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 712.6 | 700.1 | 723.7 | 7.5 | 1.000x | 7.901x |

### `factored` / `s-011` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 69.8 | 69.4 | 73.5 | 1.5 | 0.113x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 71.4 | 70.6 | 71.9 | 0.5 | 0.115x | 1.023x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 224.5 | 218.0 | 225.8 | 2.7 | 0.363x | 3.218x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 431.8 | 408.2 | 435.5 | 10.3 | 0.698x | 6.188x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 531.0 | 469.5 | 594.4 | 44.2 | 0.859x | 7.610x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 555.3 | 516.0 | 609.9 | 29.9 | 0.898x | 7.958x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 568.9 | 535.2 | 597.2 | 22.3 | 0.920x | 8.154x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 618.3 | 611.1 | 631.0 | 7.2 | 1.000x | 8.861x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 624.8 | 611.2 | 641.4 | 11.2 | 1.011x | 8.954x |

### `factored` / `s-011` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 64.0 | 63.8 | 64.5 | 0.3 | 0.014x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 64.4 | 64.0 | 64.6 | 0.2 | 0.014x | 1.006x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 443.5 | 438.3 | 459.2 | 7.2 | 0.094x | 6.926x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 2,031.7 | 2,008.1 | 2,256.0 | 92.0 | 0.433x | 31.728x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 2,223.9 | 2,184.4 | 2,277.3 | 31.4 | 0.474x | 34.730x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 2,346.9 | 2,332.0 | 2,382.0 | 17.9 | 0.500x | 36.652x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 2,380.1 | 2,342.9 | 2,515.8 | 60.6 | 0.507x | 37.169x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 2,383.6 | 2,352.9 | 2,427.3 | 26.6 | 0.508x | 37.224x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,695.2 | 4,675.7 | 4,762.3 | 29.9 | 1.000x | 73.324x |

### `factored` / `s-012` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 123.3 | 123.2 | 123.8 | 0.2 | 0.114x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 143.8 | 143.4 | 144.5 | 0.4 | 0.133x | 1.166x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 204.2 | 203.6 | 205.7 | 0.7 | 0.188x | 1.656x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 421.3 | 394.7 | 436.5 | 13.8 | 0.389x | 3.417x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 580.5 | 563.8 | 604.2 | 13.2 | 0.535x | 4.707x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 640.8 | 603.9 | 662.7 | 22.2 | 0.591x | 5.197x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 650.6 | 601.5 | 696.0 | 30.1 | 0.600x | 5.276x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,084.3 | 1,080.8 | 1,099.0 | 6.5 | 1.000x | 8.793x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,089.5 | 1,074.0 | 1,117.1 | 14.0 | 1.005x | 8.835x |

### `factored` / `s-012` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 115.8 | 115.1 | 117.9 | 1.0 | 0.105x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 119.5 | 119.3 | 119.7 | 0.1 | 0.109x | 1.032x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 173.8 | 172.1 | 175.0 | 1.2 | 0.158x | 1.501x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 208.9 | 208.8 | 210.1 | 0.5 | 0.190x | 1.804x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 425.9 | 405.3 | 471.0 | 22.7 | 0.387x | 3.679x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 612.3 | 519.2 | 639.6 | 42.7 | 0.557x | 5.289x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 615.4 | 573.0 | 630.7 | 19.7 | 0.560x | 5.316x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 629.0 | 607.1 | 659.4 | 20.2 | 0.572x | 5.433x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,099.1 | 1,094.1 | 1,116.7 | 7.8 | 1.000x | 9.495x |

### `factored` / `s-013` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 123.1 | 122.9 | 124.6 | 0.6 | 0.112x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 143.3 | 143.1 | 143.6 | 0.2 | 0.131x | 1.164x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 204.2 | 203.2 | 206.9 | 1.7 | 0.186x | 1.660x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 422.4 | 410.8 | 451.5 | 14.0 | 0.385x | 3.433x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 602.2 | 554.6 | 609.6 | 20.3 | 0.549x | 4.894x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 619.7 | 594.1 | 649.6 | 20.0 | 0.565x | 5.036x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 647.5 | 605.1 | 716.7 | 37.1 | 0.591x | 5.261x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,095.3 | 1,091.0 | 1,129.2 | 14.0 | 0.999x | 8.900x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,096.4 | 1,087.0 | 1,106.2 | 7.0 | 1.000x | 8.910x |

### `factored` / `s-013` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 115.7 | 115.7 | 119.2 | 1.4 | 0.105x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 119.5 | 119.2 | 120.3 | 0.4 | 0.108x | 1.033x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 173.8 | 170.4 | 176.1 | 2.1 | 0.157x | 1.502x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 209.3 | 208.7 | 212.1 | 1.2 | 0.189x | 1.808x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 429.8 | 412.8 | 465.6 | 17.4 | 0.389x | 3.714x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 604.9 | 430.6 | 636.1 | 73.8 | 0.547x | 5.227x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 610.4 | 569.7 | 661.0 | 32.1 | 0.552x | 5.274x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 622.1 | 602.8 | 651.4 | 16.2 | 0.563x | 5.375x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,105.7 | 1,091.6 | 1,109.8 | 7.7 | 1.000x | 9.553x |

### `factored` / `s-014` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 97.0 | 96.6 | 99.0 | 0.9 | 0.112x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 117.6 | 117.1 | 118.3 | 0.4 | 0.136x | 1.212x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 159.5 | 158.1 | 163.6 | 2.0 | 0.184x | 1.644x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 377.4 | 376.8 | 394.5 | 7.4 | 0.435x | 3.890x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 595.0 | 591.5 | 625.5 | 12.9 | 0.686x | 6.134x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 597.9 | 544.4 | 703.5 | 56.9 | 0.689x | 6.164x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 608.4 | 574.9 | 634.0 | 21.6 | 0.701x | 6.272x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 867.6 | 860.7 | 884.2 | 8.1 | 1.000x | 8.944x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 874.9 | 857.1 | 911.0 | 19.4 | 1.008x | 9.019x |

### `factored` / `s-014` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 90.0 | 89.4 | 90.0 | 0.2 | 0.103x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 94.1 | 93.5 | 98.2 | 1.8 | 0.108x | 1.045x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 155.5 | 153.6 | 156.4 | 0.9 | 0.178x | 1.728x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 169.2 | 168.5 | 169.4 | 0.3 | 0.194x | 1.881x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 383.1 | 368.1 | 397.5 | 12.5 | 0.439x | 4.257x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 517.3 | 497.5 | 575.7 | 27.6 | 0.592x | 5.748x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 523.7 | 502.5 | 563.8 | 20.4 | 0.599x | 5.819x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 547.2 | 531.0 | 629.9 | 35.6 | 0.626x | 6.080x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 873.7 | 867.2 | 877.7 | 3.8 | 1.000x | 9.708x |

### `factored` / `s-015` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 117.9 | 116.9 | 118.3 | 0.5 | 0.111x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 137.6 | 137.1 | 137.8 | 0.2 | 0.130x | 1.167x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 201.7 | 201.3 | 202.4 | 0.5 | 0.191x | 1.711x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 426.5 | 399.5 | 436.7 | 12.5 | 0.403x | 3.617x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 623.6 | 592.9 | 715.3 | 45.2 | 0.589x | 5.289x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 629.7 | 586.1 | 643.4 | 20.6 | 0.595x | 5.341x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 639.8 | 577.5 | 700.2 | 42.0 | 0.604x | 5.426x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,058.6 | 1,047.0 | 1,073.7 | 8.8 | 1.000x | 8.978x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,060.1 | 1,055.8 | 1,113.6 | 21.8 | 1.001x | 8.991x |

### `factored` / `s-015` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 110.5 | 109.8 | 111.0 | 0.4 | 0.103x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 113.5 | 113.0 | 114.6 | 0.5 | 0.106x | 1.027x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 174.3 | 173.1 | 178.4 | 2.2 | 0.163x | 1.577x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 208.0 | 207.9 | 208.8 | 0.4 | 0.195x | 1.882x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 430.2 | 410.6 | 438.8 | 10.2 | 0.403x | 3.893x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 601.7 | 596.6 | 639.3 | 18.7 | 0.564x | 5.445x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 609.7 | 509.9 | 644.2 | 47.3 | 0.571x | 5.517x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 641.3 | 613.6 | 661.5 | 17.4 | 0.601x | 5.803x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,067.7 | 1,048.3 | 1,072.5 | 10.8 | 1.000x | 9.662x |

### `factored` / `s-016` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 53.0 | 52.9 | 53.2 | 0.1 | 0.146x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 54.7 | 54.5 | 55.0 | 0.2 | 0.151x | 1.032x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 107.9 | 107.4 | 110.4 | 1.1 | 0.298x | 2.036x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 333.0 | 316.8 | 350.3 | 11.3 | 0.919x | 6.281x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 362.4 | 359.6 | 366.1 | 2.5 | 1.000x | 6.837x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 363.7 | 361.9 | 383.4 | 8.1 | 1.003x | 6.860x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 450.0 | 420.2 | 506.3 | 29.4 | 1.242x | 8.489x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 467.6 | 453.0 | 511.3 | 22.5 | 1.290x | 8.822x |
| 9 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 479.7 | 424.5 | 532.7 | 39.7 | 1.324x | 9.049x |

### `factored` / `s-016` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 47.4 | 47.3 | 47.9 | 0.2 | 0.020x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 48.0 | 47.7 | 48.7 | 0.3 | 0.020x | 1.012x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 259.5 | 259.0 | 266.3 | 2.7 | 0.109x | 5.476x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 1,440.2 | 1,414.0 | 1,513.6 | 35.2 | 0.604x | 30.385x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,671.5 | 1,643.5 | 1,736.4 | 32.8 | 0.701x | 35.265x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,806.7 | 1,778.3 | 1,866.6 | 30.2 | 0.758x | 38.117x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,813.5 | 1,752.2 | 1,835.7 | 34.2 | 0.761x | 38.261x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,829.7 | 1,768.5 | 1,867.0 | 34.1 | 0.767x | 38.603x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,384.2 | 2,367.9 | 2,421.4 | 18.1 | 1.000x | 50.303x |

### `factored` / `s-017` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 123.3 | 123.2 | 125.4 | 0.8 | 0.112x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 143.4 | 143.2 | 143.7 | 0.2 | 0.131x | 1.163x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 205.1 | 203.5 | 206.5 | 1.2 | 0.187x | 1.664x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 428.6 | 419.3 | 447.7 | 9.7 | 0.390x | 3.477x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 597.0 | 548.2 | 657.6 | 39.2 | 0.544x | 4.844x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 615.4 | 566.5 | 726.4 | 62.4 | 0.560x | 4.993x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 648.3 | 610.7 | 698.3 | 31.9 | 0.590x | 5.260x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,090.1 | 1,084.8 | 1,105.0 | 8.4 | 0.993x | 8.844x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,098.0 | 1,088.3 | 1,110.1 | 7.4 | 1.000x | 8.908x |

### `factored` / `s-017` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 115.4 | 115.1 | 117.1 | 0.7 | 0.106x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 120.1 | 119.6 | 120.5 | 0.3 | 0.110x | 1.040x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 170.7 | 170.5 | 184.1 | 5.2 | 0.156x | 1.479x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 209.3 | 208.9 | 214.5 | 2.2 | 0.191x | 1.813x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 414.0 | 402.2 | 425.9 | 8.7 | 0.379x | 3.587x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 576.3 | 545.8 | 654.8 | 41.2 | 0.527x | 4.992x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 614.3 | 592.7 | 638.0 | 16.3 | 0.562x | 5.322x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 643.5 | 590.7 | 700.1 | 36.5 | 0.589x | 5.575x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,093.3 | 1,091.4 | 1,108.0 | 6.1 | 1.000x | 9.472x |

### `factored` / `s-018` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 117.0 | 116.7 | 122.5 | 2.2 | 0.110x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 137.8 | 137.6 | 142.1 | 1.7 | 0.130x | 1.178x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 201.8 | 200.8 | 202.6 | 0.7 | 0.190x | 1.726x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 432.5 | 415.5 | 436.0 | 7.4 | 0.407x | 3.698x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 618.1 | 592.2 | 657.7 | 27.5 | 0.581x | 5.285x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 620.8 | 587.8 | 708.5 | 41.0 | 0.584x | 5.308x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 651.0 | 622.5 | 698.6 | 25.1 | 0.612x | 5.567x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,058.1 | 1,048.7 | 1,077.5 | 10.2 | 0.995x | 9.047x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,063.0 | 1,061.1 | 1,071.7 | 3.8 | 1.000x | 9.090x |

### `factored` / `s-018` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 110.0 | 109.7 | 110.9 | 0.4 | 0.104x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 113.7 | 113.3 | 114.5 | 0.4 | 0.107x | 1.034x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 173.4 | 172.6 | 177.6 | 1.8 | 0.164x | 1.576x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 208.2 | 207.9 | 208.9 | 0.4 | 0.196x | 1.892x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 416.4 | 403.8 | 432.7 | 9.9 | 0.393x | 3.786x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 588.0 | 558.4 | 608.3 | 18.4 | 0.555x | 5.345x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 623.8 | 609.8 | 660.7 | 18.9 | 0.589x | 5.671x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 638.6 | 610.8 | 662.3 | 17.7 | 0.603x | 5.805x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,059.8 | 1,050.7 | 1,074.6 | 8.5 | 1.000x | 9.635x |

### `factored` / `s-019` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 56.7 | 56.6 | 57.0 | 0.2 | 0.147x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 57.8 | 57.6 | 58.2 | 0.2 | 0.150x | 1.020x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 109.4 | 109.0 | 111.5 | 0.9 | 0.284x | 1.931x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 336.1 | 315.7 | 355.8 | 13.6 | 0.871x | 5.929x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 385.7 | 384.7 | 393.2 | 3.1 | 1.000x | 6.804x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 386.5 | 382.4 | 398.6 | 5.6 | 1.002x | 6.819x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 481.4 | 472.2 | 528.3 | 20.0 | 1.248x | 8.493x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 490.3 | 475.9 | 497.3 | 8.7 | 1.271x | 8.650x |
| 9 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 506.0 | 462.8 | 519.1 | 21.4 | 1.312x | 8.927x |

### `factored` / `s-019` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 50.8 | 50.7 | 50.8 | 0.1 | 0.020x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 51.0 | 51.0 | 51.4 | 0.1 | 0.020x | 1.005x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 265.6 | 264.2 | 268.1 | 1.5 | 0.103x | 5.229x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 1,450.3 | 1,410.7 | 1,532.1 | 41.0 | 0.565x | 28.549x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,641.1 | 1,553.6 | 1,748.0 | 62.4 | 0.639x | 32.305x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,834.6 | 1,767.6 | 1,853.1 | 30.6 | 0.715x | 36.112x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,856.0 | 1,805.3 | 1,875.9 | 25.1 | 0.723x | 36.535x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,865.9 | 1,816.2 | 1,885.9 | 27.0 | 0.727x | 36.730x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,567.6 | 2,544.6 | 2,572.8 | 10.3 | 1.000x | 50.541x |

### `factored` / `s-020` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 136.4 | 136.1 | 136.5 | 0.1 | 0.122x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 157.3 | 156.5 | 157.6 | 0.4 | 0.141x | 1.153x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 224.2 | 223.3 | 235.1 | 4.4 | 0.200x | 1.644x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 452.2 | 438.9 | 466.1 | 8.6 | 0.404x | 3.316x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 619.6 | 606.8 | 763.4 | 58.8 | 0.554x | 4.544x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 665.6 | 612.3 | 700.1 | 31.2 | 0.595x | 4.881x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 669.1 | 631.5 | 675.1 | 16.6 | 0.598x | 4.906x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,109.3 | 1,099.7 | 1,148.2 | 17.0 | 0.991x | 8.134x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,119.1 | 1,106.4 | 1,137.1 | 12.4 | 1.000x | 8.206x |

### `factored` / `s-020` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 129.4 | 129.0 | 129.9 | 0.4 | 0.116x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 133.1 | 132.5 | 134.1 | 0.5 | 0.120x | 1.029x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 175.2 | 174.7 | 179.2 | 1.7 | 0.157x | 1.354x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 214.2 | 213.6 | 223.5 | 3.8 | 0.192x | 1.655x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 419.1 | 410.0 | 424.4 | 5.2 | 0.376x | 3.238x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 623.3 | 562.9 | 634.5 | 26.2 | 0.560x | 4.816x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 650.8 | 638.1 | 670.9 | 10.6 | 0.584x | 5.028x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 654.1 | 599.2 | 682.5 | 27.6 | 0.588x | 5.054x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,113.4 | 1,101.2 | 1,125.1 | 8.0 | 1.000x | 8.603x |

### `factored` / `s-021` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 97.1 | 96.8 | 97.4 | 0.2 | 0.085x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 118.1 | 117.5 | 118.3 | 0.3 | 0.104x | 1.216x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 169.9 | 169.3 | 173.8 | 1.7 | 0.149x | 1.750x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 387.5 | 337.2 | 400.6 | 22.8 | 0.340x | 3.991x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 573.8 | 555.6 | 624.5 | 23.4 | 0.504x | 5.911x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 587.3 | 502.4 | 627.7 | 41.2 | 0.516x | 6.050x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 589.7 | 587.4 | 643.0 | 21.4 | 0.518x | 6.075x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,138.5 | 1,128.6 | 1,149.7 | 6.8 | 1.000x | 11.728x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,145.5 | 1,137.8 | 1,167.5 | 10.5 | 1.006x | 11.800x |

### `factored` / `s-021` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 90.3 | 89.8 | 90.9 | 0.4 | 0.079x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 93.2 | 92.8 | 94.0 | 0.4 | 0.081x | 1.032x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 110.8 | 110.0 | 112.5 | 0.9 | 0.097x | 1.227x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 171.9 | 171.5 | 172.4 | 0.3 | 0.150x | 1.905x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 378.7 | 356.0 | 421.3 | 21.7 | 0.330x | 4.195x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 579.0 | 549.3 | 615.6 | 24.9 | 0.505x | 6.415x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 590.9 | 574.4 | 612.8 | 14.8 | 0.516x | 6.546x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 603.5 | 560.5 | 682.1 | 44.6 | 0.527x | 6.686x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,146.1 | 1,141.6 | 1,212.1 | 26.3 | 1.000x | 12.697x |

### `factored` / `s-022` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 138.8 | 137.3 | 154.1 | 6.2 | 0.204x | 1.000x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 150.2 | 149.9 | 150.4 | 0.2 | 0.221x | 1.082x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 169.9 | 169.7 | 170.2 | 0.1 | 0.250x | 1.224x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 333.5 | 295.2 | 368.3 | 24.5 | 0.491x | 2.402x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 537.8 | 458.9 | 584.8 | 45.2 | 0.792x | 3.875x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 564.8 | 520.9 | 693.4 | 58.5 | 0.832x | 4.069x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 572.4 | 525.2 | 628.4 | 32.9 | 0.843x | 4.124x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 679.1 | 670.6 | 685.0 | 5.5 | 1.000x | 4.892x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 680.8 | 677.8 | 691.2 | 4.7 | 1.003x | 4.905x |

### `factored` / `s-022` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 99.4 | 98.3 | 99.6 | 0.6 | 0.146x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 141.4 | 141.1 | 141.8 | 0.2 | 0.207x | 1.422x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 142.8 | 142.0 | 144.4 | 0.9 | 0.209x | 1.437x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 145.9 | 145.5 | 146.0 | 0.2 | 0.214x | 1.467x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 355.9 | 324.9 | 366.3 | 15.2 | 0.521x | 3.581x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 530.8 | 480.7 | 583.3 | 34.9 | 0.777x | 5.339x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 538.2 | 516.9 | 640.6 | 43.6 | 0.788x | 5.415x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 548.8 | 493.2 | 585.9 | 32.8 | 0.803x | 5.521x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 683.0 | 676.0 | 701.9 | 9.2 | 1.000x | 6.871x |

### `factored` / `s-023` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 123.4 | 122.9 | 123.6 | 0.3 | 0.110x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 143.3 | 143.3 | 144.0 | 0.3 | 0.128x | 1.162x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 170.6 | 170.0 | 172.0 | 0.7 | 0.152x | 1.383x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 390.9 | 344.7 | 402.3 | 20.3 | 0.348x | 3.168x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 552.4 | 443.6 | 577.8 | 47.0 | 0.492x | 4.478x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 555.0 | 467.7 | 571.8 | 37.9 | 0.494x | 4.499x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 558.7 | 550.1 | 630.6 | 31.3 | 0.497x | 4.529x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,123.5 | 1,118.0 | 1,166.4 | 17.6 | 1.000x | 9.107x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,123.6 | 1,121.4 | 1,134.1 | 5.0 | 1.000x | 9.108x |

### `factored` / `s-023` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 106.9 | 106.5 | 107.4 | 0.3 | 0.095x | 1.000x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 116.0 | 115.2 | 122.6 | 2.7 | 0.103x | 1.085x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 119.6 | 119.2 | 119.6 | 0.2 | 0.106x | 1.118x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 172.7 | 172.4 | 172.9 | 0.2 | 0.153x | 1.615x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 380.0 | 356.2 | 422.4 | 21.7 | 0.337x | 3.554x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 570.7 | 560.1 | 621.0 | 22.0 | 0.506x | 5.337x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 576.8 | 558.3 | 691.1 | 51.8 | 0.511x | 5.394x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 589.0 | 541.4 | 613.1 | 24.1 | 0.522x | 5.508x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,127.7 | 1,116.8 | 1,160.3 | 15.1 | 1.000x | 10.547x |

### `factored` / `s-024` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 96.7 | 96.5 | 97.1 | 0.2 | 0.085x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 118.1 | 116.9 | 123.1 | 2.2 | 0.103x | 1.221x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 173.4 | 173.4 | 173.5 | 0.1 | 0.152x | 1.793x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 393.4 | 377.5 | 401.0 | 8.4 | 0.344x | 4.067x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 512.9 | 466.1 | 545.4 | 28.4 | 0.448x | 5.302x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 546.5 | 512.8 | 605.9 | 36.6 | 0.478x | 5.650x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 560.5 | 504.1 | 594.4 | 29.7 | 0.490x | 5.795x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,143.9 | 1,139.0 | 1,158.3 | 6.9 | 1.000x | 11.826x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,154.8 | 1,150.8 | 1,162.0 | 4.0 | 1.010x | 11.939x |

### `factored` / `s-024` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 90.1 | 89.8 | 91.0 | 0.4 | 0.078x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 93.6 | 93.1 | 94.7 | 0.5 | 0.082x | 1.040x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 109.9 | 108.6 | 111.9 | 1.2 | 0.096x | 1.220x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 176.0 | 175.7 | 176.5 | 0.3 | 0.153x | 1.955x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 381.7 | 360.1 | 387.5 | 9.7 | 0.332x | 4.238x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 590.9 | 518.2 | 645.9 | 41.9 | 0.514x | 6.561x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 591.3 | 513.3 | 631.4 | 48.7 | 0.515x | 6.565x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 612.6 | 565.1 | 690.5 | 46.0 | 0.533x | 6.801x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,148.7 | 1,140.3 | 1,168.6 | 9.5 | 1.000x | 12.753x |

### `factored` / `s-025` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 123.1 | 123.0 | 124.0 | 0.4 | 0.109x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 143.3 | 143.3 | 146.8 | 1.4 | 0.127x | 1.165x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 175.9 | 175.6 | 176.1 | 0.2 | 0.156x | 1.429x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 418.7 | 388.7 | 429.4 | 15.5 | 0.371x | 3.402x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 486.9 | 432.4 | 528.0 | 35.4 | 0.431x | 3.957x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 526.1 | 455.2 | 655.5 | 65.1 | 0.466x | 4.275x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 529.2 | 486.7 | 539.9 | 21.3 | 0.468x | 4.300x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,129.9 | 1,124.6 | 1,173.1 | 17.8 | 1.000x | 9.182x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,137.9 | 1,123.3 | 1,141.9 | 6.7 | 1.007x | 9.247x |

### `factored` / `s-025` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 107.1 | 106.3 | 107.5 | 0.4 | 0.095x | 1.000x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 115.9 | 115.5 | 116.4 | 0.3 | 0.103x | 1.082x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 119.8 | 119.5 | 120.1 | 0.2 | 0.106x | 1.119x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 178.4 | 178.0 | 180.2 | 0.8 | 0.158x | 1.665x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 390.7 | 370.1 | 412.0 | 13.3 | 0.346x | 3.647x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 562.2 | 499.5 | 618.4 | 42.4 | 0.497x | 5.248x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 581.4 | 524.1 | 658.0 | 48.5 | 0.515x | 5.428x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 585.1 | 561.8 | 643.9 | 32.6 | 0.518x | 5.463x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,130.1 | 1,124.0 | 1,137.4 | 4.9 | 1.000x | 10.550x |

### `factored` / `s-026` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 138.6 | 137.6 | 141.0 | 1.3 | 0.205x | 1.000x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 150.4 | 149.9 | 152.4 | 0.9 | 0.222x | 1.085x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 169.6 | 169.5 | 169.8 | 0.1 | 0.251x | 1.224x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 354.9 | 297.0 | 387.5 | 29.8 | 0.525x | 2.560x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 509.5 | 453.8 | 571.6 | 40.5 | 0.753x | 3.676x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 535.4 | 448.0 | 648.9 | 67.3 | 0.792x | 3.864x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 546.9 | 527.9 | 624.2 | 33.8 | 0.809x | 3.946x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 676.3 | 673.3 | 687.5 | 5.1 | 1.000x | 4.880x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 679.6 | 674.3 | 684.4 | 3.5 | 1.005x | 4.904x |

### `factored` / `s-026` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 98.5 | 98.3 | 99.1 | 0.3 | 0.146x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 141.8 | 141.1 | 142.1 | 0.3 | 0.210x | 1.439x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 142.6 | 142.1 | 143.1 | 0.4 | 0.211x | 1.448x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 145.8 | 145.2 | 146.4 | 0.4 | 0.216x | 1.480x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 357.5 | 299.8 | 403.2 | 35.3 | 0.529x | 3.629x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 530.1 | 509.0 | 601.9 | 34.5 | 0.784x | 5.381x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 552.1 | 525.9 | 582.3 | 18.9 | 0.817x | 5.604x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 562.1 | 522.0 | 615.9 | 35.9 | 0.831x | 5.706x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 676.0 | 673.7 | 681.9 | 3.1 | 1.000x | 6.862x |

### `factored` / `s-027` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 150.1 | 149.6 | 150.3 | 0.3 | 0.140x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 169.8 | 169.5 | 170.3 | 0.3 | 0.159x | 1.131x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 171.5 | 170.9 | 175.8 | 1.8 | 0.160x | 1.142x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 410.1 | 384.3 | 428.0 | 16.3 | 0.383x | 2.732x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 504.7 | 477.0 | 568.0 | 30.5 | 0.471x | 3.362x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 527.4 | 484.3 | 556.5 | 26.6 | 0.492x | 3.513x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 538.0 | 515.0 | 628.3 | 39.8 | 0.502x | 3.584x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,070.9 | 1,065.9 | 1,105.3 | 14.4 | 1.000x | 7.133x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,073.3 | 1,066.4 | 1,076.8 | 4.4 | 1.002x | 7.149x |

### `factored` / `s-027` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 104.8 | 104.0 | 105.3 | 0.5 | 0.098x | 1.000x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 142.3 | 142.2 | 143.0 | 0.3 | 0.132x | 1.358x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 145.7 | 145.2 | 147.2 | 0.7 | 0.136x | 1.390x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 173.4 | 172.9 | 173.6 | 0.2 | 0.161x | 1.654x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 385.5 | 377.2 | 405.5 | 9.4 | 0.359x | 3.678x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 560.5 | 520.8 | 609.5 | 30.4 | 0.522x | 5.348x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 564.4 | 548.6 | 590.6 | 17.5 | 0.525x | 5.385x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 609.1 | 551.0 | 681.8 | 45.6 | 0.567x | 5.811x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,074.4 | 1,061.8 | 1,077.3 | 5.7 | 1.000x | 10.251x |

### `factored` / `s-028` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 43.9 | 43.7 | 44.1 | 0.1 | 0.056x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 45.4 | 44.8 | 45.5 | 0.2 | 0.058x | 1.034x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 187.9 | 185.9 | 189.9 | 1.4 | 0.241x | 4.281x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 430.1 | 412.8 | 448.3 | 11.6 | 0.551x | 9.802x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 554.4 | 542.5 | 581.7 | 15.3 | 0.711x | 12.633x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 555.1 | 534.4 | 604.5 | 23.8 | 0.712x | 12.651x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 572.6 | 555.8 | 622.2 | 22.7 | 0.734x | 13.049x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 779.9 | 775.8 | 796.9 | 7.4 | 1.000x | 17.773x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 780.1 | 775.1 | 797.4 | 8.0 | 1.000x | 17.779x |

### `factored` / `s-028` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 37.9 | 37.8 | 38.1 | 0.1 | 0.014x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 38.5 | 38.2 | 38.8 | 0.2 | 0.014x | 1.017x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 221.3 | 211.0 | 229.5 | 5.9 | 0.083x | 5.844x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 934.3 | 902.9 | 1,079.8 | 62.5 | 0.351x | 24.674x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,103.3 | 1,076.8 | 1,138.0 | 20.0 | 0.414x | 29.136x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,419.9 | 1,409.4 | 1,436.4 | 10.9 | 0.533x | 37.496x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,427.2 | 1,379.3 | 1,448.9 | 23.6 | 0.536x | 37.689x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,429.5 | 1,392.0 | 1,528.8 | 45.9 | 0.537x | 37.752x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,662.5 | 2,657.0 | 2,710.5 | 20.6 | 1.000x | 70.313x |

### `factored` / `s-029` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 89.8 | 89.5 | 94.3 | 1.9 | 0.115x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 90.8 | 90.7 | 91.0 | 0.1 | 0.116x | 1.012x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 189.4 | 183.2 | 190.8 | 2.9 | 0.243x | 2.110x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 428.7 | 419.7 | 438.6 | 7.5 | 0.549x | 4.776x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 553.4 | 540.8 | 592.4 | 20.1 | 0.709x | 6.165x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 553.9 | 531.4 | 563.7 | 13.2 | 0.709x | 6.171x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 564.8 | 555.1 | 613.9 | 20.9 | 0.723x | 6.293x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 779.1 | 763.3 | 805.4 | 13.9 | 0.998x | 8.681x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 780.8 | 771.3 | 798.5 | 9.2 | 1.000x | 8.699x |

### `factored` / `s-029` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 83.5 | 83.3 | 84.0 | 0.3 | 0.031x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 83.6 | 83.4 | 83.7 | 0.1 | 0.031x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 235.1 | 232.2 | 237.8 | 2.1 | 0.088x | 2.817x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,667.3 | 2,662.9 | 2,691.6 | 11.7 | 1.000x | 31.960x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 3,330.5 | 3,291.4 | 3,432.4 | 57.7 | 1.249x | 39.907x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 3,345.6 | 3,284.5 | 3,384.5 | 32.4 | 1.254x | 40.089x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 4,412.9 | 4,402.6 | 4,447.4 | 15.7 | 1.654x | 52.877x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 4,423.8 | 4,355.4 | 4,445.3 | 33.3 | 1.659x | 53.008x |
| 9 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 4,456.4 | 4,346.2 | 4,548.4 | 71.4 | 1.671x | 53.398x |

### `factored` / `s-030` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 43.9 | 43.5 | 44.2 | 0.3 | 0.056x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 44.9 | 44.8 | 45.2 | 0.2 | 0.057x | 1.022x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 186.9 | 186.4 | 188.5 | 0.8 | 0.238x | 4.254x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 426.7 | 416.0 | 429.9 | 5.0 | 0.543x | 9.714x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 557.0 | 531.4 | 570.4 | 15.1 | 0.709x | 12.680x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 568.4 | 554.5 | 589.5 | 14.4 | 0.724x | 12.939x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 574.6 | 550.8 | 616.8 | 26.0 | 0.732x | 13.081x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 783.3 | 772.3 | 804.2 | 11.7 | 0.997x | 17.832x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 785.3 | 769.9 | 796.5 | 10.0 | 1.000x | 17.879x |

### `factored` / `s-030` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 37.7 | 37.7 | 38.6 | 0.4 | 0.014x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 38.1 | 38.0 | 38.7 | 0.3 | 0.014x | 1.011x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 218.9 | 216.5 | 222.5 | 2.1 | 0.082x | 5.808x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 872.6 | 842.3 | 902.4 | 20.0 | 0.327x | 23.159x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,047.5 | 962.9 | 1,095.6 | 45.5 | 0.393x | 27.800x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,447.1 | 1,409.9 | 1,531.8 | 41.7 | 0.543x | 38.405x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,450.7 | 1,440.5 | 1,503.3 | 23.9 | 0.544x | 38.501x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,488.1 | 1,340.5 | 1,520.2 | 64.8 | 0.558x | 39.492x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,666.4 | 2,647.1 | 2,688.0 | 15.5 | 1.000x | 70.765x |

### `factored` / `s-031` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 60.0 | 59.7 | 63.8 | 1.6 | 0.076x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 61.7 | 61.5 | 61.8 | 0.1 | 0.079x | 1.027x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 189.6 | 187.0 | 190.6 | 1.3 | 0.242x | 3.159x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 423.7 | 411.5 | 433.4 | 8.0 | 0.540x | 7.061x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 554.7 | 546.4 | 563.4 | 6.2 | 0.707x | 9.243x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 567.0 | 553.3 | 617.6 | 25.9 | 0.723x | 9.449x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 577.4 | 553.8 | 584.0 | 11.1 | 0.736x | 9.621x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 780.1 | 771.7 | 803.7 | 11.6 | 0.994x | 13.000x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 784.7 | 771.1 | 808.8 | 12.9 | 1.000x | 13.077x |

### `factored` / `s-031` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 53.7 | 53.7 | 54.6 | 0.3 | 0.020x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 54.1 | 54.1 | 54.2 | 0.1 | 0.020x | 1.006x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 230.7 | 229.7 | 235.2 | 2.1 | 0.086x | 4.294x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 1,410.3 | 1,381.0 | 1,550.0 | 60.5 | 0.527x | 26.241x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,558.2 | 1,539.8 | 1,605.6 | 22.2 | 0.582x | 28.993x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 2,029.2 | 1,989.0 | 2,113.6 | 44.2 | 0.758x | 37.758x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 2,051.3 | 1,992.1 | 2,109.4 | 38.1 | 0.766x | 38.169x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 2,079.6 | 1,997.4 | 2,176.5 | 58.9 | 0.776x | 38.696x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,678.5 | 2,653.8 | 2,721.5 | 22.9 | 1.000x | 49.840x |

### `factored` / `s-032` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 50.8 | 50.5 | 51.0 | 0.2 | 0.055x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 52.5 | 52.1 | 53.0 | 0.3 | 0.057x | 1.033x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 303.9 | 266.3 | 321.7 | 19.6 | 0.329x | 5.981x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 527.3 | 490.7 | 560.8 | 23.1 | 0.571x | 10.379x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 594.5 | 564.5 | 639.2 | 24.7 | 0.644x | 11.703x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 610.8 | 597.9 | 615.1 | 7.2 | 0.662x | 12.024x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 634.0 | 591.0 | 647.5 | 20.4 | 0.687x | 12.479x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 923.1 | 913.4 | 938.2 | 9.0 | 1.000x | 18.170x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 934.3 | 923.0 | 964.9 | 14.3 | 1.012x | 18.392x |

### `factored` / `s-032` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 44.1 | 44.0 | 44.6 | 0.2 | 0.013x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 44.9 | 44.6 | 45.1 | 0.2 | 0.014x | 1.016x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 323.4 | 314.0 | 325.4 | 4.7 | 0.099x | 7.328x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 1,742.4 | 1,735.8 | 1,750.6 | 5.0 | 0.532x | 39.477x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,746.4 | 1,722.4 | 1,856.2 | 52.7 | 0.533x | 39.567x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,771.6 | 1,739.3 | 1,793.5 | 20.2 | 0.541x | 40.137x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,786.6 | 1,707.7 | 1,827.8 | 45.8 | 0.545x | 40.476x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,930.6 | 1,920.3 | 1,943.1 | 8.0 | 0.589x | 43.740x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,276.2 | 3,241.0 | 3,399.2 | 57.5 | 1.000x | 74.226x |

### `factored` / `s-033` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 50.2 | 50.2 | 50.9 | 0.3 | 0.058x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 52.1 | 51.9 | 52.7 | 0.3 | 0.060x | 1.038x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 268.8 | 255.5 | 298.7 | 15.9 | 0.310x | 5.351x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 513.0 | 507.4 | 551.9 | 16.7 | 0.592x | 10.213x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 600.9 | 574.8 | 621.8 | 17.5 | 0.693x | 11.961x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 610.4 | 577.4 | 638.2 | 20.1 | 0.704x | 12.151x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 611.1 | 590.1 | 637.0 | 16.7 | 0.705x | 12.164x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 867.2 | 865.8 | 876.4 | 3.9 | 1.000x | 17.262x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 872.9 | 872.4 | 896.1 | 9.1 | 1.007x | 17.375x |

### `factored` / `s-033` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 44.2 | 44.0 | 44.4 | 0.1 | 0.014x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 44.7 | 44.5 | 44.8 | 0.1 | 0.015x | 1.013x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 326.2 | 316.7 | 335.9 | 7.4 | 0.107x | 7.386x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 1,726.9 | 1,719.7 | 1,740.3 | 7.3 | 0.567x | 39.101x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,756.7 | 1,714.1 | 1,781.6 | 25.9 | 0.577x | 39.777x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,767.7 | 1,715.8 | 1,805.5 | 31.6 | 0.580x | 40.026x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,780.4 | 1,716.8 | 1,802.8 | 35.0 | 0.584x | 40.313x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,924.4 | 1,898.8 | 1,977.8 | 26.4 | 0.632x | 43.574x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,046.6 | 3,021.5 | 3,057.1 | 12.4 | 1.000x | 68.984x |

### `factored` / `s-034` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 37.1 | 36.9 | 37.2 | 0.1 | 0.030x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 39.2 | 38.8 | 40.4 | 0.6 | 0.031x | 1.056x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 153.4 | 152.1 | 153.7 | 0.6 | 0.122x | 4.136x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 375.4 | 348.9 | 380.0 | 11.4 | 0.299x | 10.117x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 520.4 | 488.8 | 579.5 | 29.7 | 0.414x | 14.026x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 535.8 | 504.5 | 568.8 | 22.2 | 0.427x | 14.441x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 536.8 | 500.6 | 557.1 | 20.5 | 0.427x | 14.466x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,253.4 | 1,245.3 | 1,290.0 | 15.6 | 0.998x | 33.781x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,256.0 | 1,253.0 | 1,273.2 | 7.2 | 1.000x | 33.851x |

### `factored` / `s-034` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 31.3 | 31.2 | 31.3 | 0.0 | 0.007x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 31.8 | 31.7 | 32.0 | 0.1 | 0.007x | 1.017x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 385.8 | 383.4 | 390.1 | 2.2 | 0.082x | 12.344x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 682.7 | 664.0 | 728.8 | 24.9 | 0.145x | 21.844x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 860.2 | 810.2 | 901.9 | 31.9 | 0.183x | 27.526x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,034.4 | 1,006.6 | 1,133.9 | 47.1 | 0.220x | 33.100x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,045.1 | 998.1 | 1,076.8 | 29.7 | 0.223x | 33.443x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,065.5 | 1,032.4 | 1,091.0 | 20.1 | 0.227x | 34.093x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,694.9 | 4,597.4 | 4,813.4 | 78.2 | 1.000x | 150.227x |

### `factored` / `s-035` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 50.3 | 50.1 | 50.6 | 0.2 | 0.032x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 51.6 | 51.2 | 51.9 | 0.2 | 0.033x | 1.026x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 387.6 | 385.4 | 391.0 | 2.0 | 0.245x | 7.700x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 708.9 | 703.6 | 712.0 | 2.8 | 0.449x | 14.083x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 731.3 | 707.9 | 793.0 | 29.1 | 0.463x | 14.528x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 752.5 | 739.4 | 831.3 | 33.6 | 0.477x | 14.949x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 767.8 | 698.3 | 793.0 | 31.8 | 0.486x | 15.253x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,579.0 | 1,572.8 | 1,585.2 | 4.0 | 1.000x | 31.367x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,586.1 | 1,579.9 | 1,618.9 | 14.0 | 1.005x | 31.509x |

### `factored` / `s-035` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 44.1 | 44.0 | 44.2 | 0.1 | 0.008x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 44.6 | 44.4 | 45.0 | 0.2 | 0.008x | 1.011x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 486.7 | 472.9 | 523.3 | 17.4 | 0.083x | 11.023x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 1,776.0 | 1,763.2 | 1,791.0 | 8.8 | 0.302x | 40.227x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,966.7 | 1,949.6 | 2,006.1 | 21.2 | 0.334x | 44.547x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 2,285.0 | 2,243.8 | 2,352.5 | 36.6 | 0.388x | 51.756x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 2,289.2 | 2,218.5 | 2,367.3 | 58.8 | 0.389x | 51.851x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 2,291.2 | 2,217.7 | 2,301.8 | 31.6 | 0.389x | 51.897x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 5,885.4 | 5,850.6 | 5,927.8 | 28.5 | 1.000x | 133.307x |

### `factored` / `s-036` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 53.4 | 53.0 | 55.4 | 0.8 | 0.085x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 54.8 | 54.1 | 55.0 | 0.3 | 0.087x | 1.026x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 153.3 | 152.0 | 156.2 | 1.5 | 0.244x | 2.872x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 377.2 | 363.4 | 383.3 | 6.8 | 0.600x | 7.068x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 545.2 | 524.6 | 568.4 | 16.6 | 0.867x | 10.214x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 549.7 | 535.4 | 561.7 | 9.8 | 0.874x | 10.298x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 564.2 | 538.7 | 618.5 | 26.6 | 0.897x | 10.569x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 628.7 | 626.5 | 633.9 | 3.1 | 1.000x | 11.778x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 632.1 | 624.7 | 652.4 | 9.5 | 1.005x | 11.842x |

### `factored` / `s-036` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 48.0 | 47.8 | 49.3 | 0.6 | 0.023x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 48.1 | 48.0 | 48.4 | 0.2 | 0.023x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 195.0 | 194.4 | 195.4 | 0.4 | 0.093x | 4.063x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 1,506.0 | 1,491.2 | 1,601.6 | 39.5 | 0.720x | 31.380x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,682.0 | 1,621.0 | 1,767.1 | 47.5 | 0.804x | 35.046x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,964.5 | 1,947.4 | 2,031.3 | 29.0 | 0.939x | 40.934x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,970.7 | 1,967.2 | 2,012.3 | 19.0 | 0.942x | 41.062x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,983.5 | 1,906.7 | 2,002.5 | 35.9 | 0.948x | 41.329x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,092.4 | 2,074.9 | 2,096.0 | 9.0 | 1.000x | 43.598x |

### `factored` / `s-037` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 40.4 | 40.1 | 42.9 | 1.0 | 0.048x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 41.9 | 41.6 | 47.7 | 2.4 | 0.050x | 1.038x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 214.9 | 213.6 | 216.1 | 0.9 | 0.255x | 5.321x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 438.4 | 431.9 | 455.9 | 8.4 | 0.520x | 10.855x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 585.7 | 569.5 | 630.3 | 21.3 | 0.695x | 14.502x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 589.5 | 571.7 | 640.2 | 26.9 | 0.699x | 14.597x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 608.1 | 526.8 | 642.4 | 39.7 | 0.721x | 15.058x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 840.7 | 836.3 | 850.2 | 4.8 | 0.997x | 20.818x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 843.0 | 835.9 | 931.3 | 36.1 | 1.000x | 20.875x |

### `factored` / `s-037` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 35.0 | 34.8 | 35.6 | 0.3 | 0.012x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 36.3 | 36.2 | 36.7 | 0.2 | 0.012x | 1.036x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 287.0 | 285.8 | 289.5 | 1.3 | 0.098x | 8.195x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 1,226.7 | 1,155.4 | 1,242.3 | 31.9 | 0.420x | 35.022x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,503.4 | 1,446.5 | 1,570.2 | 40.8 | 0.515x | 42.923x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,510.7 | 1,461.9 | 1,558.1 | 32.8 | 0.517x | 43.130x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,514.4 | 1,433.5 | 1,521.9 | 37.0 | 0.518x | 43.236x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,524.5 | 1,483.7 | 1,532.7 | 17.9 | 0.522x | 43.522x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,921.2 | 2,906.6 | 2,944.1 | 15.2 | 1.000x | 83.399x |

### `factored` / `s-038` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 53.4 | 53.2 | 54.0 | 0.3 | 0.053x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 54.7 | 54.0 | 55.1 | 0.5 | 0.055x | 1.026x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 473.1 | 354.4 | 493.9 | 50.8 | 0.474x | 8.865x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 645.7 | 614.6 | 665.0 | 17.4 | 0.647x | 12.099x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 676.8 | 623.7 | 687.6 | 25.1 | 0.678x | 12.682x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 697.9 | 637.7 | 727.9 | 34.3 | 0.699x | 13.078x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 698.6 | 692.3 | 732.6 | 14.8 | 0.700x | 13.090x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 998.7 | 993.1 | 1,000.9 | 3.2 | 1.000x | 18.713x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 999.8 | 995.7 | 1,043.2 | 17.8 | 1.001x | 18.733x |

### `factored` / `s-038` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 47.8 | 47.7 | 51.1 | 1.3 | 0.013x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 48.3 | 48.0 | 49.4 | 0.5 | 0.013x | 1.010x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 569.9 | 565.0 | 572.4 | 2.6 | 0.159x | 11.915x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 2,453.6 | 2,449.3 | 2,520.2 | 32.4 | 0.683x | 51.297x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 2,501.9 | 2,481.9 | 2,548.1 | 24.7 | 0.696x | 52.306x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 2,507.4 | 2,486.5 | 2,517.1 | 11.1 | 0.698x | 52.423x |
| 7 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 2,869.1 | 2,862.9 | 2,924.6 | 22.7 | 0.799x | 59.984x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 3,089.5 | 3,049.7 | 3,169.4 | 41.6 | 0.860x | 64.592x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,592.2 | 3,541.8 | 3,618.6 | 29.6 | 1.000x | 75.102x |

### `factored` / `s-039` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 108.0 | 107.3 | 110.1 | 1.0 | 0.287x | 1.000x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 110.7 | 110.5 | 110.8 | 0.1 | 0.294x | 1.025x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 112.3 | 111.8 | 112.7 | 0.3 | 0.299x | 1.040x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 325.8 | 311.8 | 340.1 | 10.8 | 0.866x | 3.017x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 376.2 | 371.4 | 378.6 | 2.7 | 1.000x | 3.484x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 381.9 | 374.9 | 401.3 | 9.5 | 1.015x | 3.537x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 473.6 | 436.1 | 493.7 | 19.2 | 1.259x | 4.386x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 480.7 | 444.8 | 524.4 | 31.9 | 1.278x | 4.451x |
| 9 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 500.0 | 436.8 | 515.3 | 28.6 | 1.329x | 4.630x |

### `factored` / `s-039` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 105.8 | 105.4 | 107.8 | 0.9 | 0.068x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 109.2 | 109.2 | 109.4 | 0.1 | 0.071x | 1.032x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 211.8 | 211.1 | 214.0 | 1.0 | 0.137x | 2.002x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 305.2 | 299.9 | 346.0 | 17.1 | 0.197x | 2.885x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 496.5 | 486.9 | 500.7 | 4.9 | 0.321x | 4.692x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 698.7 | 671.1 | 719.9 | 16.6 | 0.451x | 6.603x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 706.4 | 656.3 | 759.8 | 36.0 | 0.456x | 6.676x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 748.1 | 672.6 | 775.8 | 35.7 | 0.483x | 7.070x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,547.7 | 1,535.3 | 1,603.9 | 24.0 | 1.000x | 14.625x |

### `factored` / `s-040` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 33.2 | 32.7 | 34.6 | 0.8 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 34.6 | 34.1 | 35.3 | 0.5 | 1.043x | 1.043x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 47.0 | 46.7 | 47.4 | 0.3 | 1.415x | 1.415x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 48.5 | 48.3 | 53.8 | 2.1 | 1.462x | 1.462x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 262.8 | 258.8 | 273.7 | 5.0 | 7.918x | 7.918x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 482.7 | 480.2 | 484.0 | 1.4 | 14.545x | 14.545x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 644.3 | 623.7 | 682.0 | 22.5 | 19.418x | 19.418x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 668.5 | 645.5 | 690.6 | 17.5 | 20.144x | 20.144x |
| 9 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 707.1 | 638.4 | 724.9 | 37.0 | 21.309x | 21.309x |

### `factored` / `s-040` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 34.2 | 33.9 | 34.8 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 40.6 | 40.5 | 41.2 | 0.3 | 1.186x | 1.186x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 41.0 | 40.9 | 41.1 | 0.1 | 1.199x | 1.199x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.3 | 44.3 | 44.6 | 0.1 | 1.296x | 1.296x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 1,827.1 | 1,752.0 | 1,865.2 | 39.7 | 53.384x | 53.384x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,965.6 | 1,848.9 | 2,066.3 | 87.9 | 57.432x | 57.432x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 2,193.6 | 2,189.2 | 2,204.8 | 5.9 | 64.094x | 64.094x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 2,214.4 | 2,211.8 | 2,245.4 | 13.1 | 64.700x | 64.700x |
| 9 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 2,224.4 | 2,124.1 | 2,352.7 | 89.9 | 64.994x | 64.994x |

### `factored` / `s-041` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 34.5 | 33.4 | 34.6 | 0.5 | 0.212x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 35.7 | 35.6 | 36.1 | 0.2 | 0.220x | 1.037x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 54.8 | 54.5 | 54.9 | 0.2 | 0.337x | 1.590x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 162.7 | 160.6 | 164.6 | 1.5 | 1.000x | 4.718x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 164.3 | 160.1 | 164.9 | 1.7 | 1.010x | 4.765x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 277.7 | 270.0 | 293.1 | 8.0 | 1.707x | 8.054x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 418.1 | 401.8 | 456.7 | 21.1 | 2.570x | 12.125x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 428.8 | 422.0 | 455.5 | 13.9 | 2.636x | 12.435x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 429.6 | 409.5 | 451.9 | 14.6 | 2.640x | 12.456x |

### `factored` / `s-041` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 29.8 | 29.5 | 37.4 | 3.1 | 0.166x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 29.9 | 29.8 | 30.9 | 0.5 | 0.167x | 1.006x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 54.8 | 54.7 | 64.6 | 3.9 | 0.305x | 1.841x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 179.7 | 178.4 | 183.2 | 1.7 | 1.000x | 6.036x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 949.6 | 924.5 | 1,024.5 | 38.4 | 5.286x | 31.902x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,183.8 | 1,079.5 | 1,246.3 | 64.5 | 6.589x | 39.769x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,342.9 | 1,289.5 | 1,407.5 | 40.5 | 7.474x | 45.111x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,359.6 | 1,344.5 | 1,379.8 | 12.6 | 7.567x | 45.673x |
| 9 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,371.7 | 1,359.5 | 1,408.8 | 16.9 | 7.635x | 46.082x |

### `factored` / `s-042` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 17.7 | 17.5 | 17.9 | 0.1 | 0.029x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 18.7 | 18.6 | 18.8 | 0.1 | 0.031x | 1.056x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 82.9 | 79.7 | 103.2 | 10.6 | 0.136x | 4.690x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 291.5 | 283.9 | 320.4 | 13.3 | 0.477x | 16.501x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 504.3 | 485.4 | 581.2 | 35.2 | 0.825x | 28.543x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 517.4 | 415.0 | 536.9 | 46.7 | 0.847x | 29.286x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 530.1 | 471.9 | 549.7 | 27.1 | 0.867x | 30.005x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 611.2 | 602.8 | 680.9 | 29.1 | 1.000x | 34.595x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 612.4 | 610.0 | 623.7 | 4.8 | 1.002x | 34.662x |

### `factored` / `s-042` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 12.9 | 12.9 | 13.7 | 0.3 | 0.021x | 1.000x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 13.0 | 12.6 | 13.3 | 0.3 | 0.021x | 1.007x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 84.0 | 83.6 | 129.7 | 18.3 | 0.135x | 6.504x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 176.5 | 174.1 | 180.6 | 2.1 | 0.284x | 13.660x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 370.1 | 369.0 | 383.3 | 5.5 | 0.597x | 28.654x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 620.5 | 617.8 | 621.8 | 1.4 | 1.000x | 48.036x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 712.9 | 705.4 | 802.1 | 35.9 | 1.149x | 55.186x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 737.3 | 704.8 | 742.0 | 15.3 | 1.188x | 57.081x |
| 9 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 740.5 | 695.8 | 772.1 | 25.4 | 1.193x | 57.326x |

### `factored` / `s-043` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 130.4 | 130.2 | 131.0 | 0.3 | 0.227x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 132.5 | 132.1 | 138.2 | 2.3 | 0.231x | 1.016x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 151.6 | 150.7 | 153.4 | 0.9 | 0.264x | 1.162x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 379.8 | 369.3 | 417.5 | 17.5 | 0.661x | 2.912x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 522.2 | 506.5 | 566.0 | 20.3 | 0.909x | 4.004x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 562.0 | 503.7 | 574.5 | 25.7 | 0.978x | 4.309x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 571.1 | 463.8 | 584.6 | 49.9 | 0.994x | 4.379x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 574.6 | 572.0 | 769.7 | 78.2 | 1.000x | 4.406x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 576.3 | 571.5 | 584.8 | 4.6 | 1.003x | 4.419x |

### `factored` / `s-043` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 124.7 | 124.6 | 125.2 | 0.2 | 0.045x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 128.4 | 128.0 | 129.3 | 0.5 | 0.046x | 1.029x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 290.1 | 289.6 | 292.5 | 1.1 | 0.104x | 2.325x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 722.6 | 668.4 | 751.2 | 29.4 | 0.258x | 5.793x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 955.0 | 924.2 | 988.0 | 20.8 | 0.341x | 7.656x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 998.8 | 945.8 | 1,026.1 | 28.5 | 0.357x | 8.008x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,001.7 | 980.7 | 1,040.1 | 22.7 | 0.358x | 8.031x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,012.3 | 969.5 | 1,046.1 | 27.2 | 0.362x | 8.115x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,799.5 | 2,785.9 | 2,827.4 | 14.0 | 1.000x | 22.443x |

### `factored` / `s-044` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 54.6 | 54.5 | 55.3 | 0.3 | 0.332x | 1.000x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 112.2 | 111.9 | 113.3 | 0.5 | 0.682x | 2.054x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 113.5 | 113.2 | 113.7 | 0.2 | 0.690x | 2.077x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 161.9 | 158.6 | 163.4 | 1.7 | 0.984x | 2.963x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 164.5 | 161.1 | 231.9 | 27.4 | 1.000x | 3.010x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 287.0 | 280.3 | 306.7 | 9.8 | 1.745x | 5.251x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 419.6 | 389.7 | 467.6 | 26.1 | 2.551x | 7.678x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 424.5 | 371.3 | 432.2 | 22.1 | 2.581x | 7.768x |
| 9 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 428.1 | 392.2 | 459.5 | 22.8 | 2.602x | 7.833x |

### `factored` / `s-044` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 107.4 | 107.1 | 108.0 | 0.3 | 0.105x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 110.6 | 110.6 | 111.3 | 0.3 | 0.108x | 1.030x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 160.1 | 159.0 | 160.8 | 0.7 | 0.156x | 1.491x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 172.2 | 171.8 | 173.8 | 0.7 | 0.168x | 1.604x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 385.4 | 366.2 | 398.8 | 12.2 | 0.377x | 3.589x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 533.0 | 472.7 | 583.9 | 37.9 | 0.521x | 4.964x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 549.5 | 501.4 | 566.0 | 23.0 | 0.537x | 5.118x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 568.6 | 535.4 | 640.6 | 38.5 | 0.556x | 5.296x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,023.2 | 1,015.6 | 1,043.1 | 9.7 | 1.000x | 9.530x |

### `factored` / `s-045` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 49.9 | 49.7 | 50.1 | 0.2 | 0.086x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 52.1 | 50.9 | 52.4 | 0.6 | 0.090x | 1.043x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 150.9 | 149.8 | 152.1 | 0.9 | 0.261x | 3.025x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 368.1 | 363.8 | 418.1 | 20.3 | 0.637x | 7.377x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 530.6 | 460.8 | 573.5 | 40.4 | 0.918x | 10.633x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 542.5 | 521.8 | 601.5 | 27.0 | 0.939x | 10.872x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 565.8 | 537.6 | 607.1 | 23.8 | 0.979x | 11.339x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 575.6 | 573.6 | 602.9 | 11.5 | 0.996x | 11.534x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 578.0 | 575.3 | 787.5 | 81.8 | 1.000x | 11.583x |

### `factored` / `s-045` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 44.1 | 44.0 | 51.0 | 2.8 | 0.022x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 44.5 | 44.4 | 45.0 | 0.2 | 0.022x | 1.010x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 197.5 | 196.0 | 199.8 | 1.4 | 0.099x | 4.482x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 1,405.0 | 1,296.7 | 1,600.0 | 104.9 | 0.706x | 31.883x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,596.6 | 1,501.8 | 1,783.2 | 108.5 | 0.802x | 36.232x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,804.6 | 1,790.8 | 1,828.1 | 13.0 | 0.907x | 40.952x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,819.9 | 1,796.6 | 1,844.0 | 15.9 | 0.915x | 41.300x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,823.7 | 1,798.6 | 1,844.7 | 16.1 | 0.917x | 41.385x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,989.7 | 1,984.0 | 2,026.7 | 15.8 | 1.000x | 45.153x |

### `factored` / `s-046` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 36.9 | 36.7 | 37.0 | 0.1 | 0.037x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 38.9 | 38.3 | 39.6 | 0.4 | 0.039x | 1.052x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 378.2 | 354.2 | 414.8 | 21.3 | 0.381x | 10.241x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 597.5 | 585.8 | 633.8 | 17.3 | 0.603x | 16.180x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 666.3 | 641.0 | 687.0 | 15.1 | 0.672x | 18.044x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 671.0 | 637.4 | 705.9 | 27.3 | 0.677x | 18.172x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 688.3 | 638.3 | 707.5 | 27.9 | 0.694x | 18.641x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 991.3 | 987.1 | 1,025.9 | 15.2 | 1.000x | 26.846x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 998.1 | 993.4 | 1,018.2 | 9.9 | 1.007x | 27.030x |

### `factored` / `s-046` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 31.1 | 31.1 | 32.2 | 0.4 | 0.009x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 31.7 | 31.6 | 32.5 | 0.3 | 0.009x | 1.018x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 538.3 | 535.8 | 543.2 | 2.5 | 0.152x | 17.288x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 1,731.2 | 1,717.7 | 1,776.5 | 21.3 | 0.490x | 55.599x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,908.3 | 1,889.9 | 1,944.9 | 19.2 | 0.540x | 61.289x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,967.0 | 1,883.7 | 2,010.0 | 45.3 | 0.556x | 63.173x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,969.6 | 1,960.7 | 1,982.3 | 8.0 | 0.557x | 63.258x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,971.3 | 1,927.4 | 1,996.9 | 29.1 | 0.558x | 63.312x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,535.8 | 3,499.8 | 3,583.5 | 29.6 | 1.000x | 113.558x |

### `factored` / `s-047` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 40.1 | 39.8 | 59.0 | 7.6 | 0.025x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 42.4 | 41.7 | 42.6 | 0.3 | 0.026x | 1.058x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 152.6 | 151.7 | 154.6 | 1.0 | 0.094x | 3.807x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 387.1 | 380.6 | 389.5 | 3.1 | 0.239x | 9.657x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 524.4 | 493.6 | 564.7 | 24.8 | 0.324x | 13.086x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 527.0 | 499.6 | 570.7 | 29.9 | 0.325x | 13.150x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 562.0 | 518.5 | 587.1 | 23.9 | 0.347x | 14.022x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,620.3 | 1,610.5 | 1,628.6 | 7.0 | 1.000x | 40.429x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,627.9 | 1,598.9 | 1,660.0 | 20.1 | 1.005x | 40.618x |

### `factored` / `s-047` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 34.5 | 34.4 | 35.4 | 0.4 | 0.006x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 35.0 | 34.8 | 35.5 | 0.3 | 0.006x | 1.016x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 474.0 | 464.6 | 485.2 | 6.8 | 0.078x | 13.751x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 716.3 | 715.3 | 795.3 | 33.6 | 0.119x | 20.779x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 981.5 | 929.3 | 1,039.0 | 40.0 | 0.162x | 28.475x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,127.6 | 1,077.0 | 1,158.3 | 27.4 | 0.187x | 32.712x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,130.6 | 1,122.5 | 1,163.5 | 15.6 | 0.187x | 32.800x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,133.5 | 1,108.0 | 1,196.4 | 31.0 | 0.188x | 32.882x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 6,042.5 | 5,974.9 | 6,077.1 | 34.8 | 1.000x | 175.295x |

### `factored` / `s-048` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 22.4 | 22.3 | 22.4 | 0.0 | 0.029x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 23.9 | 23.8 | 24.3 | 0.2 | 0.031x | 1.069x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 110.0 | 109.7 | 111.4 | 0.6 | 0.141x | 4.917x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 345.5 | 342.6 | 347.4 | 2.0 | 0.442x | 15.446x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 494.5 | 427.4 | 527.2 | 34.1 | 0.632x | 22.107x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 528.8 | 495.9 | 559.5 | 23.3 | 0.676x | 23.636x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 529.7 | 480.2 | 550.1 | 23.9 | 0.677x | 23.677x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 779.6 | 773.4 | 806.5 | 12.1 | 0.996x | 34.849x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 782.4 | 775.2 | 789.3 | 5.0 | 1.000x | 34.973x |

### `factored` / `s-048` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.5 | 0.1 | 0.009x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 18.6 | 18.6 | 19.6 | 0.4 | 0.009x | 1.018x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 187.1 | 178.9 | 188.6 | 3.7 | 0.092x | 10.238x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 312.3 | 310.8 | 325.1 | 5.3 | 0.154x | 17.087x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 555.3 | 528.5 | 599.0 | 24.8 | 0.273x | 30.384x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 751.4 | 750.3 | 777.4 | 11.8 | 0.369x | 41.112x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 773.0 | 744.6 | 847.8 | 35.4 | 0.380x | 42.292x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 791.9 | 753.2 | 810.8 | 19.4 | 0.389x | 43.327x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,033.8 | 2,006.5 | 2,037.7 | 11.8 | 1.000x | 111.273x |

### `factored` / `s-049` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 127.0 | 126.5 | 133.9 | 2.8 | 0.232x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 129.0 | 128.5 | 130.9 | 0.8 | 0.235x | 1.016x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 134.8 | 132.9 | 137.0 | 1.3 | 0.246x | 1.062x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 368.1 | 348.5 | 375.8 | 9.5 | 0.672x | 2.899x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 516.9 | 464.7 | 539.4 | 25.4 | 0.944x | 4.071x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 528.4 | 494.5 | 632.1 | 56.5 | 0.965x | 4.162x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 546.7 | 545.1 | 554.8 | 3.6 | 0.998x | 4.306x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 547.6 | 544.3 | 550.2 | 2.0 | 1.000x | 4.313x |
| 9 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 559.4 | 541.4 | 584.5 | 15.4 | 1.022x | 4.406x |

### `factored` / `s-049` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 122.1 | 121.5 | 123.4 | 0.7 | 0.048x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 125.1 | 124.9 | 125.7 | 0.3 | 0.049x | 1.025x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 271.9 | 271.5 | 275.0 | 1.3 | 0.106x | 2.227x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 591.0 | 587.3 | 608.8 | 7.8 | 0.231x | 4.841x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 802.6 | 787.6 | 836.3 | 16.7 | 0.313x | 6.574x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 836.5 | 794.4 | 867.2 | 25.7 | 0.326x | 6.852x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 872.4 | 839.7 | 932.8 | 31.6 | 0.340x | 7.145x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 896.6 | 837.1 | 901.7 | 26.0 | 0.350x | 7.344x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,562.5 | 2,558.5 | 2,570.5 | 4.1 | 1.000x | 20.990x |

### `factored` / `s-050` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 101.2 | 100.8 | 101.6 | 0.3 | 0.132x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 102.6 | 102.4 | 103.0 | 0.3 | 0.134x | 1.013x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 247.5 | 232.8 | 262.6 | 10.1 | 0.322x | 2.444x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 483.7 | 473.0 | 529.5 | 20.9 | 0.630x | 4.778x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 546.5 | 510.6 | 619.4 | 41.9 | 0.712x | 5.398x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 572.6 | 526.5 | 591.2 | 24.1 | 0.746x | 5.656x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 601.6 | 551.0 | 655.7 | 39.6 | 0.783x | 5.943x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 767.9 | 763.6 | 776.5 | 4.6 | 1.000x | 7.585x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 769.2 | 758.2 | 774.7 | 6.9 | 1.002x | 7.599x |

### `factored` / `s-050` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 95.6 | 95.5 | 96.7 | 0.4 | 0.027x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 99.5 | 98.9 | 99.9 | 0.4 | 0.028x | 1.041x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 381.8 | 374.9 | 388.6 | 4.3 | 0.109x | 3.993x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 1,035.9 | 1,023.5 | 1,043.6 | 7.7 | 0.294x | 10.833x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,164.0 | 1,076.4 | 1,177.1 | 41.3 | 0.331x | 12.171x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,194.0 | 1,146.4 | 1,201.8 | 23.6 | 0.339x | 12.486x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,199.4 | 1,084.9 | 1,229.9 | 49.7 | 0.341x | 12.542x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,203.9 | 1,186.7 | 1,246.7 | 21.5 | 0.342x | 12.590x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,519.0 | 3,498.2 | 3,536.6 | 13.6 | 1.000x | 36.797x |

### `factored` / `s-051` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 126.8 | 126.6 | 127.0 | 0.1 | 0.232x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 128.8 | 128.8 | 129.3 | 0.2 | 0.236x | 1.016x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 133.0 | 131.1 | 135.2 | 1.3 | 0.243x | 1.049x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 365.7 | 362.1 | 383.5 | 7.6 | 0.669x | 2.885x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 504.6 | 478.3 | 556.9 | 31.1 | 0.923x | 3.980x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 546.8 | 541.0 | 549.8 | 3.0 | 1.000x | 4.313x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 547.4 | 518.0 | 575.6 | 21.9 | 1.001x | 4.317x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 548.8 | 544.4 | 605.7 | 23.3 | 1.004x | 4.329x |
| 9 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 558.9 | 482.5 | 613.8 | 44.5 | 1.022x | 4.409x |

### `factored` / `s-051` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 121.9 | 121.6 | 123.7 | 0.8 | 0.047x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 125.0 | 124.9 | 125.5 | 0.2 | 0.049x | 1.025x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 273.2 | 272.7 | 275.1 | 0.8 | 0.106x | 2.241x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 593.9 | 549.8 | 602.7 | 21.1 | 0.231x | 4.871x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 814.2 | 802.1 | 820.9 | 6.6 | 0.317x | 6.678x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 825.8 | 751.8 | 855.8 | 35.1 | 0.322x | 6.773x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 883.0 | 822.9 | 888.7 | 24.9 | 0.344x | 7.243x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 886.3 | 843.0 | 892.6 | 18.8 | 0.345x | 7.270x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,567.1 | 2,546.1 | 2,583.7 | 15.6 | 1.000x | 21.057x |

### `factored` / `s-052` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 37.6 | 37.0 | 37.9 | 0.3 | 0.048x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 39.1 | 38.9 | 39.3 | 0.1 | 0.050x | 1.039x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 153.0 | 151.3 | 154.4 | 1.2 | 0.197x | 4.068x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 384.9 | 376.8 | 397.6 | 7.3 | 0.496x | 10.235x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 521.4 | 495.6 | 536.5 | 18.0 | 0.671x | 13.863x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 526.5 | 505.2 | 577.8 | 28.3 | 0.678x | 13.999x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 532.4 | 482.6 | 552.4 | 23.7 | 0.686x | 14.156x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 776.5 | 775.3 | 791.3 | 6.5 | 1.000x | 20.647x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 780.8 | 771.8 | 792.0 | 7.3 | 1.006x | 20.762x |

### `factored` / `s-052` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 31.5 | 31.5 | 31.6 | 0.0 | 0.012x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 32.4 | 32.3 | 32.8 | 0.2 | 0.012x | 1.027x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 218.8 | 214.2 | 221.2 | 2.7 | 0.082x | 6.941x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 666.9 | 613.8 | 722.7 | 40.8 | 0.249x | 21.157x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 843.2 | 820.2 | 941.9 | 48.7 | 0.314x | 26.750x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,037.6 | 980.6 | 1,059.1 | 28.7 | 0.387x | 32.916x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,054.8 | 1,036.4 | 1,095.0 | 20.1 | 0.393x | 33.463x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,069.2 | 1,015.0 | 1,077.0 | 23.1 | 0.399x | 33.919x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,681.7 | 2,662.4 | 2,701.3 | 14.0 | 1.000x | 85.071x |

### `factored` / `s-053` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 28.1 | 27.9 | 28.1 | 0.1 | 0.036x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.4 | 29.2 | 30.9 | 0.6 | 0.038x | 1.046x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 153.4 | 151.7 | 156.3 | 1.5 | 0.198x | 5.451x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 380.2 | 377.6 | 393.2 | 5.7 | 0.491x | 13.512x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 521.8 | 479.2 | 530.7 | 18.7 | 0.673x | 18.545x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 538.6 | 507.1 | 556.7 | 20.0 | 0.695x | 19.143x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 544.6 | 519.3 | 564.2 | 18.0 | 0.703x | 19.358x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 774.4 | 773.8 | 782.4 | 3.2 | 1.000x | 27.524x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 774.8 | 773.7 | 788.3 | 5.5 | 1.000x | 27.538x |

### `factored` / `s-053` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 21.4 | 21.3 | 21.7 | 0.1 | 0.008x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 21.7 | 21.6 | 22.2 | 0.2 | 0.008x | 1.011x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 218.9 | 215.6 | 221.0 | 1.9 | 0.082x | 10.211x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 626.1 | 559.4 | 645.1 | 30.2 | 0.234x | 29.204x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 866.7 | 807.3 | 885.9 | 35.6 | 0.324x | 40.423x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 963.8 | 949.9 | 1,000.8 | 17.5 | 0.361x | 44.954x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 987.0 | 925.0 | 1,004.0 | 28.9 | 0.369x | 46.037x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,026.6 | 951.7 | 1,145.8 | 72.1 | 0.384x | 47.883x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,672.3 | 2,667.5 | 2,674.3 | 2.3 | 1.000x | 124.643x |

### `factored` / `s-054` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 28.2 | 28.0 | 28.3 | 0.1 | 0.036x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.4 | 29.2 | 30.6 | 0.5 | 0.038x | 1.043x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 153.0 | 151.9 | 154.7 | 1.0 | 0.196x | 5.435x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 384.5 | 366.1 | 417.1 | 16.6 | 0.493x | 13.656x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 517.0 | 492.4 | 517.5 | 10.2 | 0.663x | 18.361x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 542.4 | 497.5 | 574.1 | 30.9 | 0.695x | 19.266x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 550.3 | 522.8 | 567.2 | 14.4 | 0.705x | 19.547x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 780.3 | 771.5 | 784.6 | 4.8 | 1.000x | 27.715x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 782.3 | 774.0 | 900.7 | 49.1 | 1.003x | 27.787x |

### `factored` / `s-054` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 21.4 | 21.3 | 22.6 | 0.5 | 0.008x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 21.7 | 21.6 | 21.8 | 0.1 | 0.008x | 1.012x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 217.7 | 216.4 | 221.0 | 1.8 | 0.081x | 10.159x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 618.0 | 539.0 | 634.2 | 37.7 | 0.231x | 28.839x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 830.2 | 777.7 | 898.4 | 40.1 | 0.311x | 38.736x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 956.6 | 939.0 | 975.3 | 12.8 | 0.358x | 44.636x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 993.6 | 939.4 | 1,021.4 | 27.6 | 0.372x | 46.364x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 999.8 | 915.6 | 1,021.5 | 38.8 | 0.374x | 46.652x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,672.0 | 2,659.5 | 2,676.4 | 5.9 | 1.000x | 124.678x |

### `factored` / `s-055` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 28.2 | 27.8 | 28.9 | 0.4 | 0.036x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 29.4 | 29.2 | 29.8 | 0.2 | 0.038x | 1.041x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 153.0 | 151.6 | 154.0 | 0.9 | 0.196x | 5.419x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 389.6 | 372.6 | 403.8 | 10.6 | 0.500x | 13.798x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 514.4 | 459.1 | 541.2 | 27.7 | 0.661x | 18.220x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 532.3 | 499.1 | 568.8 | 22.3 | 0.684x | 18.856x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 546.2 | 510.3 | 582.1 | 26.8 | 0.702x | 19.346x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 778.6 | 772.7 | 821.1 | 18.0 | 1.000x | 27.578x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 782.2 | 771.0 | 790.7 | 6.5 | 1.005x | 27.704x |

### `factored` / `s-055` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 21.4 | 21.3 | 21.5 | 0.1 | 0.008x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 21.6 | 21.6 | 21.7 | 0.0 | 0.008x | 1.010x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 219.4 | 218.1 | 223.5 | 2.0 | 0.082x | 10.232x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 634.7 | 620.1 | 650.7 | 11.0 | 0.238x | 29.602x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 849.2 | 838.2 | 934.0 | 34.9 | 0.318x | 39.606x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 980.4 | 924.3 | 1,062.0 | 45.1 | 0.368x | 45.729x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 981.3 | 957.7 | 1,016.7 | 19.8 | 0.368x | 45.769x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 994.7 | 950.2 | 1,014.5 | 23.6 | 0.373x | 46.395x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,666.5 | 2,659.6 | 2,705.0 | 16.4 | 1.000x | 124.370x |

### `factored` / `s-056` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 30.7 | 30.6 | 31.2 | 0.3 | 0.039x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.6 | 31.8 | 36.4 | 1.6 | 0.042x | 1.062x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 153.1 | 151.6 | 153.7 | 0.7 | 0.197x | 4.995x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 385.0 | 357.9 | 389.0 | 11.2 | 0.494x | 12.559x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 523.5 | 511.5 | 552.9 | 15.6 | 0.672x | 17.075x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 523.7 | 490.4 | 559.6 | 23.3 | 0.672x | 17.081x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 552.5 | 525.7 | 559.0 | 11.6 | 0.709x | 18.019x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 778.8 | 769.5 | 787.0 | 5.5 | 1.000x | 25.400x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 780.1 | 768.5 | 814.3 | 15.8 | 1.002x | 25.444x |

### `factored` / `s-056` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 25.6 | 25.4 | 26.6 | 0.4 | 0.010x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 25.8 | 25.7 | 26.1 | 0.1 | 0.010x | 1.010x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 219.2 | 212.0 | 219.9 | 2.9 | 0.082x | 8.571x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 631.8 | 592.5 | 680.3 | 31.1 | 0.237x | 24.706x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 871.3 | 790.0 | 885.4 | 35.4 | 0.326x | 34.073x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 963.0 | 955.7 | 1,035.0 | 29.8 | 0.361x | 37.657x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 979.1 | 965.2 | 1,013.2 | 17.5 | 0.367x | 38.285x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 994.4 | 971.7 | 1,031.0 | 21.8 | 0.373x | 38.885x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,669.3 | 2,652.2 | 2,702.7 | 16.5 | 1.000x | 104.381x |

### `factored` / `s-057` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 7,760.7 | 7,745.9 | 7,830.2 | 31.7 | 0.765x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7,956.4 | 7,935.7 | 8,054.4 | 43.8 | 0.784x | 1.025x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 8,184.1 | 8,180.3 | 8,248.8 | 28.3 | 0.806x | 1.055x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 8,202.1 | 8,134.9 | 8,275.5 | 44.9 | 0.808x | 1.057x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8,249.6 | 8,134.0 | 8,379.3 | 89.4 | 0.813x | 1.063x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 10,149.5 | 10,140.0 | 10,173.8 | 12.2 | 1.000x | 1.308x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 10,267.2 | 10,140.6 | 10,337.4 | 77.2 | 1.012x | 1.323x |
| 8 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 67,161.3 | 67,090.1 | 67,295.7 | 72.6 | 6.617x | 8.654x |
| 9 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 67,169.7 | 67,110.7 | 67,233.5 | 46.8 | 6.618x | 8.655x |

### `factored` / `s-058` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 26,288.5 | 26,266.4 | 26,353.5 | 30.1 | 0.144x | 1.000x | 5 | 100% |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 26,289.3 | 26,277.3 | 26,292.1 | 5.2 | 0.144x | 1.000x | 5 | 100% |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 29,394.6 | 29,113.7 | 29,479.6 | 143.2 | 0.161x | 1.118x | 5 | 100% |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 182,464.9 | 180,436.3 | 184,232.2 | 1,367.9 | 0.998x | 6.941x | 5 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 182,792.7 | 181,071.8 | 186,008.7 | 1,617.0 | 1.000x | 6.953x | 5 | 100% |

### `factored` / `s-059` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33,604.9 | 33,581.9 | 33,704.5 | 44.2 | 0.115x | 1.000x | 5 | 100% |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33,655.9 | 33,623.0 | 33,866.9 | 89.0 | 0.116x | 1.002x | 5 | 100% |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 72,651.8 | 71,878.3 | 73,309.0 | 508.4 | 0.250x | 2.162x | 5 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 290,974.9 | 290,500.0 | 294,274.1 | 1,771.6 | 1.000x | 8.659x | 5 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 291,546.0 | 290,559.2 | 295,500.6 | 1,854.9 | 1.002x | 8.676x | 5 | 100% |

### `factored` / `s-060` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33,344.7 | 33,340.6 | 33,469.8 | 49.9 | 0.039x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33,383.5 | 33,372.6 | 33,407.3 | 12.1 | 0.039x | 1.001x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 194,929.3 | 194,669.2 | 195,582.5 | 342.7 | 0.229x | 5.846x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 195,025.4 | 194,449.5 | 206,100.3 | 4,460.5 | 0.229x | 5.849x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 199,473.7 | 198,611.8 | 199,797.7 | 414.8 | 0.235x | 5.982x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 199,566.3 | 198,383.9 | 203,457.6 | 1,727.6 | 0.235x | 5.985x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 200,221.4 | 199,199.0 | 201,995.0 | 1,009.4 | 0.235x | 6.005x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 849,449.9 | 845,906.9 | 876,087.2 | 11,038.7 | 0.999x | 25.475x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 850,421.0 | 848,684.8 | 877,287.6 | 13,515.1 | 1.000x | 25.504x |

### `factored` / `s-061` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 10,994.4 | 10,961.8 | 11,270.8 | 117.0 | 0.151x | 1.000x | 5 | 100% |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13,149.9 | 13,149.2 | 13,263.6 | 44.5 | 0.181x | 1.196x | 5 | 100% |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13,169.2 | 13,163.1 | 13,220.7 | 22.9 | 0.181x | 1.198x | 5 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 72,660.9 | 72,336.3 | 72,936.1 | 213.1 | 1.000x | 6.609x | 5 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 72,983.8 | 72,564.0 | 74,111.1 | 563.9 | 1.004x | 6.638x | 5 | 100% |

### `factored` / `s-062` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 315.4 | 298.4 | 324.5 | 10.6 | 0.360x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 482.2 | 471.4 | 518.2 | 16.4 | 0.551x | 1.529x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 510.9 | 497.2 | 544.4 | 16.3 | 0.584x | 1.620x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 516.0 | 495.3 | 549.3 | 17.3 | 0.590x | 1.636x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 525.2 | 492.2 | 559.7 | 28.9 | 0.600x | 1.665x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 874.6 | 872.7 | 889.5 | 6.3 | 0.999x | 2.773x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 875.3 | 873.6 | 896.7 | 9.8 | 1.000x | 2.776x |
| 8 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 1,684.0 | 1,681.4 | 1,686.7 | 1.8 | 1.924x | 5.340x |
| 9 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 1,684.9 | 1,681.1 | 1,693.7 | 4.6 | 1.925x | 5.342x |

### `factored` / `s-063` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 25,222.3 | 25,212.3 | 25,291.4 | 29.0 | 0.118x | 1.000x | 5 | 100% |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 25,241.6 | 25,211.5 | 25,267.5 | 20.2 | 0.119x | 1.001x | 5 | 100% |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 101,057.8 | 99,678.4 | 101,371.7 | 596.2 | 0.475x | 4.007x | 5 | 100% |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 212,552.9 | 211,742.0 | 214,033.1 | 962.1 | 0.998x | 8.427x | 5 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 212,891.8 | 212,348.9 | 215,976.8 | 1,314.0 | 1.000x | 8.441x | 5 | 100% |

### `factored` / `s-064` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 26,908.3 | 26,895.2 | 27,019.3 | 49.9 | 0.179x | 1.000x | 5 | 100% |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 26,954.2 | 26,913.2 | 26,973.2 | 23.2 | 0.179x | 1.002x | 5 | 100% |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 33,003.8 | 32,878.4 | 33,105.0 | 84.6 | 0.220x | 1.227x | 5 | 100% |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 150,177.3 | 148,436.4 | 150,779.1 | 796.2 | 0.999x | 5.581x | 5 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 150,253.1 | 148,576.4 | 150,944.1 | 917.7 | 1.000x | 5.584x | 5 | 100% |

### `factored` / `s-065` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 41.3 | 41.1 | 41.7 | 0.2 | 0.251x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 43.1 | 42.6 | 43.4 | 0.3 | 0.262x | 1.043x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 55.1 | 54.9 | 55.3 | 0.1 | 0.336x | 1.336x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 164.4 | 158.4 | 168.9 | 3.8 | 1.000x | 3.980x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 165.7 | 159.4 | 170.9 | 4.1 | 1.008x | 4.013x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 245.8 | 222.1 | 275.8 | 17.3 | 1.495x | 5.952x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 353.9 | 264.6 | 395.1 | 43.8 | 2.153x | 8.571x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 365.8 | 316.0 | 395.3 | 29.1 | 2.225x | 8.858x |
| 9 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 391.5 | 302.8 | 447.7 | 47.2 | 2.382x | 9.483x |

### `factored` / `s-065` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 34.1 | 33.9 | 38.0 | 1.6 | 0.021x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 34.3 | 34.2 | 34.7 | 0.2 | 0.021x | 1.007x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 141.6 | 140.5 | 142.3 | 0.7 | 0.088x | 4.158x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 1,148.4 | 1,084.9 | 1,216.1 | 48.8 | 0.712x | 33.723x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,396.9 | 1,372.0 | 1,473.7 | 34.5 | 0.866x | 41.022x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,406.4 | 1,316.2 | 1,441.6 | 44.1 | 0.872x | 41.300x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,437.8 | 1,395.7 | 1,498.3 | 33.2 | 0.892x | 42.222x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,438.1 | 1,373.1 | 1,475.3 | 37.9 | 0.892x | 42.231x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,612.8 | 1,599.8 | 1,637.9 | 13.0 | 1.000x | 47.360x |

### `factored` / `s-066` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 117.4 | 117.1 | 118.1 | 0.4 | 0.109x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 137.9 | 137.7 | 138.3 | 0.2 | 0.128x | 1.175x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 203.5 | 203.1 | 205.1 | 0.8 | 0.188x | 1.734x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 399.4 | 370.0 | 429.1 | 23.1 | 0.370x | 3.403x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 540.4 | 533.0 | 593.1 | 22.4 | 0.500x | 4.604x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 552.5 | 541.8 | 651.9 | 41.2 | 0.511x | 4.706x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 586.4 | 543.1 | 617.0 | 24.6 | 0.543x | 4.995x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,073.1 | 1,060.9 | 1,079.6 | 6.8 | 0.993x | 9.142x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,080.7 | 1,068.1 | 1,110.9 | 14.5 | 1.000x | 9.207x |

### `factored` / `s-066` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 109.8 | 109.7 | 117.1 | 2.9 | 0.103x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 113.3 | 113.3 | 114.8 | 0.6 | 0.106x | 1.032x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 173.4 | 172.8 | 176.2 | 1.2 | 0.162x | 1.578x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 208.7 | 208.1 | 209.5 | 0.5 | 0.195x | 1.900x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 424.2 | 409.7 | 431.0 | 7.4 | 0.396x | 3.862x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 618.3 | 596.3 | 639.4 | 14.4 | 0.578x | 5.629x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 623.1 | 593.0 | 634.7 | 14.6 | 0.582x | 5.673x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 638.0 | 592.8 | 658.0 | 27.1 | 0.596x | 5.808x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,070.3 | 1,062.9 | 1,083.7 | 6.8 | 1.000x | 9.743x |

### `factored` / `s-067` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 110.6 | 110.4 | 114.4 | 1.5 | 0.110x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 130.3 | 130.0 | 130.4 | 0.1 | 0.129x | 1.178x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 165.7 | 165.4 | 169.7 | 1.6 | 0.164x | 1.499x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 361.7 | 333.8 | 385.0 | 16.7 | 0.359x | 3.271x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 540.3 | 509.9 | 592.2 | 28.1 | 0.536x | 4.887x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 545.8 | 511.7 | 562.7 | 16.9 | 0.541x | 4.936x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 551.9 | 528.7 | 627.2 | 33.5 | 0.547x | 4.991x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,008.7 | 1,001.2 | 1,035.5 | 13.7 | 1.000x | 9.123x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,010.0 | 996.8 | 1,219.4 | 86.2 | 1.001x | 9.135x |

### `factored` / `s-067` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 103.5 | 103.3 | 104.2 | 0.3 | 0.102x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 106.6 | 106.5 | 108.3 | 0.7 | 0.105x | 1.029x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 160.4 | 159.5 | 161.3 | 0.6 | 0.158x | 1.549x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 176.3 | 175.7 | 178.5 | 1.0 | 0.174x | 1.703x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 392.3 | 378.6 | 425.9 | 15.9 | 0.388x | 3.789x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 542.0 | 539.2 | 549.2 | 3.7 | 0.535x | 5.234x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 542.0 | 519.4 | 559.0 | 12.7 | 0.535x | 5.235x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 579.4 | 542.7 | 595.0 | 18.3 | 0.572x | 5.596x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,012.2 | 1,005.2 | 1,019.8 | 5.0 | 1.000x | 9.776x |

### `factored` / `s-068` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 39.9 | 39.6 | 40.5 | 0.3 | 0.058x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 58.9 | 58.5 | 59.2 | 0.2 | 0.085x | 1.476x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 84.7 | 84.0 | 85.9 | 0.7 | 0.123x | 2.123x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 278.1 | 243.7 | 293.8 | 20.7 | 0.402x | 6.966x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 401.1 | 377.4 | 435.4 | 19.6 | 0.580x | 10.048x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 423.2 | 415.2 | 507.5 | 37.9 | 0.612x | 10.603x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 449.3 | 366.1 | 472.1 | 41.8 | 0.650x | 11.257x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 687.2 | 685.7 | 691.6 | 2.1 | 0.994x | 17.217x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 691.7 | 678.1 | 701.8 | 9.1 | 1.000x | 17.328x |

### `factored` / `s-068` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 32.7 | 32.6 | 33.3 | 0.3 | 0.047x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 36.0 | 35.8 | 44.9 | 3.6 | 0.052x | 1.100x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 84.5 | 84.3 | 84.7 | 0.1 | 0.122x | 2.583x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 104.9 | 103.9 | 105.2 | 0.5 | 0.152x | 3.206x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 289.1 | 282.1 | 302.3 | 7.2 | 0.419x | 8.839x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 419.2 | 375.9 | 580.3 | 71.5 | 0.607x | 12.819x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 425.0 | 329.7 | 460.3 | 51.4 | 0.616x | 12.995x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 450.7 | 434.1 | 477.5 | 14.2 | 0.653x | 13.783x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 690.3 | 682.2 | 693.5 | 4.1 | 1.000x | 21.109x |

### `factored` / `s-069` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 53.2 | 53.0 | 53.2 | 0.1 | 0.083x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 55.1 | 54.4 | 55.7 | 0.4 | 0.086x | 1.035x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 152.6 | 152.2 | 155.0 | 1.1 | 0.239x | 2.867x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 361.3 | 328.0 | 369.1 | 16.1 | 0.566x | 6.787x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 504.4 | 491.5 | 518.9 | 10.0 | 0.790x | 9.475x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 511.4 | 429.4 | 534.4 | 39.5 | 0.801x | 9.606x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 533.2 | 493.2 | 540.6 | 18.8 | 0.835x | 10.016x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 638.4 | 634.0 | 668.9 | 13.0 | 1.000x | 11.992x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 640.4 | 632.7 | 655.4 | 7.6 | 1.003x | 12.029x |

### `factored` / `s-069` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 47.4 | 47.2 | 47.5 | 0.1 | 0.021x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 47.8 | 47.4 | 48.0 | 0.2 | 0.021x | 1.010x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 203.3 | 202.4 | 203.5 | 0.4 | 0.091x | 4.292x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 1,460.0 | 1,348.8 | 1,512.5 | 66.8 | 0.653x | 30.832x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,626.2 | 1,589.7 | 1,695.0 | 34.6 | 0.727x | 34.340x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,817.7 | 1,757.4 | 1,839.1 | 27.5 | 0.813x | 38.384x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,819.6 | 1,773.2 | 1,847.9 | 24.2 | 0.814x | 38.425x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,820.6 | 1,804.2 | 1,848.9 | 16.4 | 0.814x | 38.445x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,236.4 | 2,231.6 | 2,272.3 | 15.2 | 1.000x | 47.226x |

### `factored` / `s-070` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 91.1 | 90.7 | 91.2 | 0.2 | 0.106x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 111.3 | 111.1 | 111.6 | 0.2 | 0.129x | 1.221x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 144.2 | 143.8 | 148.9 | 1.9 | 0.168x | 1.583x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 372.9 | 323.4 | 384.1 | 21.7 | 0.434x | 4.094x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 525.4 | 516.7 | 544.9 | 11.9 | 0.611x | 5.768x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 565.7 | 497.5 | 598.6 | 38.4 | 0.658x | 6.211x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 568.6 | 514.9 | 679.0 | 53.7 | 0.661x | 6.243x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 856.2 | 848.0 | 869.0 | 7.2 | 0.996x | 9.400x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 859.7 | 853.7 | 891.6 | 13.3 | 1.000x | 9.438x |

### `factored` / `s-070` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 83.5 | 83.3 | 84.4 | 0.4 | 0.098x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 86.7 | 86.5 | 91.8 | 2.1 | 0.101x | 1.038x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 148.4 | 148.1 | 149.6 | 0.7 | 0.173x | 1.777x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 149.5 | 149.1 | 149.7 | 0.2 | 0.175x | 1.791x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 355.8 | 350.6 | 372.7 | 8.1 | 0.416x | 4.262x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 506.7 | 432.6 | 563.6 | 42.9 | 0.592x | 6.070x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 512.7 | 478.9 | 567.1 | 29.8 | 0.599x | 6.141x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 514.3 | 470.9 | 527.5 | 23.7 | 0.601x | 6.160x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 855.7 | 841.7 | 886.9 | 16.0 | 1.000x | 10.250x |

### `factored` / `s-071` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 159.8 | 159.3 | 160.1 | 0.3 | 0.182x | 1.000x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 202.3 | 202.1 | 204.1 | 0.7 | 0.230x | 1.266x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 221.6 | 221.5 | 222.7 | 0.5 | 0.252x | 1.387x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 379.2 | 344.5 | 404.5 | 19.1 | 0.431x | 2.374x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 552.9 | 481.5 | 567.5 | 31.3 | 0.629x | 3.461x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 588.7 | 496.5 | 621.3 | 46.4 | 0.669x | 3.685x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 611.8 | 552.8 | 650.3 | 32.0 | 0.696x | 3.829x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 879.5 | 868.6 | 906.3 | 12.8 | 1.000x | 5.505x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 886.1 | 865.4 | 888.0 | 8.4 | 1.007x | 5.546x |

### `factored` / `s-071` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 164.3 | 163.9 | 164.6 | 0.2 | 0.187x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 164.6 | 164.1 | 175.3 | 4.3 | 0.187x | 1.002x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 198.0 | 197.7 | 202.8 | 1.9 | 0.225x | 1.205x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 201.4 | 200.8 | 202.0 | 0.4 | 0.229x | 1.226x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 379.6 | 370.2 | 392.5 | 8.8 | 0.431x | 2.311x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 488.5 | 462.7 | 514.9 | 16.6 | 0.555x | 2.973x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 525.8 | 460.2 | 544.4 | 31.0 | 0.597x | 3.200x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 526.6 | 473.0 | 570.9 | 37.7 | 0.598x | 3.206x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 880.6 | 867.3 | 885.3 | 7.3 | 1.000x | 5.361x |

### `factored` / `s-072` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 166.4 | 166.3 | 167.2 | 0.3 | 0.075x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 168.0 | 167.8 | 169.9 | 0.8 | 0.075x | 1.010x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 739.7 | 729.6 | 744.7 | 5.2 | 0.332x | 4.446x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 949.5 | 933.9 | 958.6 | 8.9 | 0.426x | 5.707x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 962.9 | 934.7 | 987.9 | 22.4 | 0.432x | 5.788x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 974.6 | 926.1 | 1,119.7 | 67.3 | 0.437x | 5.858x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 987.3 | 944.4 | 1,014.1 | 23.3 | 0.443x | 5.934x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,230.8 | 2,206.8 | 2,273.7 | 24.2 | 1.000x | 13.408x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,245.8 | 2,228.1 | 2,270.6 | 16.1 | 1.007x | 13.499x |

### `factored` / `s-072` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 161.0 | 160.6 | 161.3 | 0.3 | 0.052x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 164.3 | 163.8 | 164.7 | 0.3 | 0.053x | 1.020x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 407.6 | 406.2 | 409.9 | 1.2 | 0.131x | 2.532x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 912.1 | 862.8 | 919.3 | 20.6 | 0.293x | 5.664x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,123.3 | 1,103.8 | 1,135.1 | 10.7 | 0.361x | 6.976x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,176.2 | 1,140.1 | 1,215.7 | 24.1 | 0.378x | 7.304x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,201.6 | 1,178.0 | 1,249.2 | 23.2 | 0.386x | 7.462x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,205.6 | 1,185.0 | 1,263.4 | 27.0 | 0.387x | 7.487x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,115.0 | 3,098.1 | 3,177.6 | 29.3 | 1.000x | 19.345x |

### `factored` / `s-073` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 40.3 | 40.1 | 40.4 | 0.1 | 0.051x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 42.1 | 41.7 | 42.3 | 0.2 | 0.053x | 1.046x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 153.2 | 150.3 | 155.1 | 1.9 | 0.193x | 3.804x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 382.0 | 373.1 | 393.2 | 7.9 | 0.482x | 9.488x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 499.6 | 456.5 | 538.5 | 30.1 | 0.630x | 12.409x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 514.7 | 465.9 | 565.8 | 33.4 | 0.649x | 12.785x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 543.9 | 497.0 | 576.1 | 25.7 | 0.686x | 13.510x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 792.5 | 782.3 | 821.6 | 13.7 | 1.000x | 19.685x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 795.6 | 769.1 | 983.4 | 79.5 | 1.004x | 19.761x |

### `factored` / `s-073` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 34.6 | 34.4 | 34.8 | 0.2 | 0.013x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 35.1 | 35.0 | 35.2 | 0.1 | 0.013x | 1.015x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 218.2 | 215.9 | 222.6 | 2.3 | 0.081x | 6.305x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 914.3 | 802.0 | 948.9 | 54.9 | 0.341x | 26.411x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,069.3 | 941.4 | 1,127.9 | 77.4 | 0.398x | 30.888x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,396.4 | 1,376.5 | 1,415.7 | 12.6 | 0.520x | 40.337x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,418.5 | 1,384.2 | 1,434.9 | 17.7 | 0.528x | 40.978x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,423.8 | 1,407.5 | 1,448.9 | 14.3 | 0.530x | 41.130x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,684.4 | 2,668.5 | 2,723.1 | 18.3 | 1.000x | 77.544x |

### `factored` / `s-074` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 53.4 | 53.3 | 54.0 | 0.2 | 0.068x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 54.9 | 54.6 | 55.0 | 0.2 | 0.070x | 1.027x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 199.9 | 184.6 | 205.6 | 7.1 | 0.255x | 3.742x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 425.8 | 410.0 | 443.4 | 11.7 | 0.543x | 7.971x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 526.9 | 505.2 | 569.0 | 20.9 | 0.672x | 9.863x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 551.7 | 490.5 | 582.4 | 32.2 | 0.704x | 10.326x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 558.8 | 539.2 | 601.2 | 24.0 | 0.713x | 10.459x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 782.3 | 767.8 | 801.2 | 14.2 | 0.998x | 14.643x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 783.6 | 775.3 | 814.8 | 13.7 | 1.000x | 14.668x |

### `factored` / `s-074` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 47.5 | 47.3 | 48.2 | 0.3 | 0.018x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 47.7 | 47.7 | 47.9 | 0.1 | 0.018x | 1.006x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 230.1 | 228.8 | 238.6 | 3.6 | 0.086x | 4.849x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 1,185.1 | 1,108.3 | 1,267.1 | 52.0 | 0.442x | 24.975x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,299.3 | 1,270.4 | 1,381.2 | 43.7 | 0.485x | 27.382x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,781.8 | 1,732.5 | 1,794.4 | 23.3 | 0.665x | 37.550x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,782.2 | 1,685.6 | 1,823.5 | 48.2 | 0.665x | 37.559x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,790.7 | 1,739.1 | 1,812.7 | 26.5 | 0.668x | 37.739x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,680.5 | 2,666.3 | 2,685.2 | 7.3 | 1.000x | 56.491x |

### `factored` / `s-075` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 110.5 | 109.8 | 116.0 | 2.3 | 0.106x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 130.1 | 129.9 | 130.6 | 0.2 | 0.125x | 1.177x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 176.0 | 175.9 | 180.0 | 1.7 | 0.169x | 1.593x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 381.1 | 360.8 | 413.1 | 20.6 | 0.366x | 3.448x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 509.1 | 491.3 | 519.3 | 11.1 | 0.489x | 4.606x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 521.6 | 509.9 | 561.4 | 17.6 | 0.501x | 4.720x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 607.9 | 563.0 | 617.8 | 19.9 | 0.584x | 5.500x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,034.4 | 1,026.1 | 1,045.5 | 6.2 | 0.994x | 9.359x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,040.3 | 1,030.1 | 1,075.5 | 15.8 | 1.000x | 9.412x |

### `factored` / `s-075` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 103.4 | 103.2 | 104.3 | 0.4 | 0.100x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 106.5 | 105.9 | 106.9 | 0.3 | 0.103x | 1.030x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 108.0 | 106.6 | 111.1 | 1.7 | 0.104x | 1.045x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 177.2 | 177.0 | 179.8 | 1.1 | 0.171x | 1.714x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 385.3 | 362.7 | 394.7 | 10.7 | 0.372x | 3.727x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 553.5 | 466.5 | 619.4 | 49.2 | 0.534x | 5.353x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 579.0 | 545.5 | 701.5 | 54.8 | 0.559x | 5.600x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 619.7 | 601.6 | 626.1 | 9.8 | 0.598x | 5.993x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,036.3 | 1,022.5 | 1,042.7 | 8.8 | 1.000x | 10.023x |

### `factored` / `s-076` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 110.7 | 110.3 | 138.9 | 11.3 | 0.107x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 130.5 | 130.0 | 131.1 | 0.4 | 0.126x | 1.178x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 176.2 | 176.0 | 187.5 | 4.5 | 0.170x | 1.592x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 391.7 | 357.6 | 425.2 | 26.9 | 0.377x | 3.537x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 510.7 | 491.5 | 519.1 | 11.5 | 0.492x | 4.612x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 516.7 | 502.2 | 561.6 | 21.0 | 0.498x | 4.667x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 607.5 | 559.6 | 629.2 | 24.4 | 0.585x | 5.487x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,031.3 | 1,027.6 | 1,050.5 | 9.5 | 0.993x | 9.314x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,038.4 | 1,026.7 | 1,064.7 | 14.6 | 1.000x | 9.379x |

### `factored` / `s-076` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 103.5 | 103.3 | 103.7 | 0.1 | 0.101x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 106.5 | 106.5 | 106.6 | 0.0 | 0.104x | 1.030x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 106.7 | 106.6 | 110.2 | 1.4 | 0.104x | 1.032x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 177.4 | 177.1 | 179.5 | 0.9 | 0.173x | 1.715x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 386.3 | 374.9 | 400.5 | 9.8 | 0.377x | 3.733x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 535.0 | 522.5 | 634.4 | 40.9 | 0.522x | 5.171x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 598.3 | 542.1 | 627.2 | 35.0 | 0.583x | 5.782x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 601.4 | 569.4 | 643.6 | 24.6 | 0.586x | 5.812x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,025.4 | 1,025.2 | 1,038.9 | 6.5 | 1.000x | 9.910x |

### `factored` / `s-077` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 110.0 | 109.7 | 135.7 | 10.3 | 0.096x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 130.3 | 130.0 | 132.9 | 1.1 | 0.113x | 1.185x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 170.2 | 169.5 | 174.6 | 1.9 | 0.148x | 1.548x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 380.8 | 364.9 | 418.5 | 18.9 | 0.331x | 3.464x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 501.3 | 460.0 | 513.3 | 19.5 | 0.436x | 4.559x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 513.0 | 489.1 | 536.4 | 16.6 | 0.446x | 4.665x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 565.6 | 534.6 | 592.0 | 19.9 | 0.492x | 5.144x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,136.9 | 1,133.8 | 1,162.6 | 10.6 | 0.989x | 10.340x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,149.3 | 1,128.9 | 1,186.1 | 20.9 | 1.000x | 10.453x |

### `factored` / `s-077` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 103.3 | 103.2 | 105.0 | 0.7 | 0.092x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 106.6 | 105.9 | 107.7 | 0.6 | 0.094x | 1.032x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 108.1 | 107.5 | 109.3 | 0.6 | 0.096x | 1.046x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 172.5 | 172.4 | 172.7 | 0.1 | 0.153x | 1.670x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 374.6 | 350.8 | 412.7 | 24.3 | 0.332x | 3.627x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 576.2 | 535.9 | 597.6 | 23.6 | 0.511x | 5.578x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 593.0 | 514.6 | 686.8 | 58.2 | 0.525x | 5.741x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 605.3 | 548.6 | 611.3 | 23.5 | 0.536x | 5.860x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,128.5 | 1,128.0 | 1,133.9 | 2.2 | 1.000x | 10.926x |

### `factored` / `s-078` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 110.8 | 109.5 | 137.0 | 10.6 | 0.101x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 130.3 | 129.9 | 131.0 | 0.4 | 0.119x | 1.176x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 160.1 | 159.9 | 165.0 | 2.0 | 0.146x | 1.445x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 374.9 | 334.9 | 420.4 | 31.9 | 0.342x | 3.384x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 543.2 | 511.1 | 572.1 | 22.5 | 0.495x | 4.902x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 558.2 | 528.3 | 563.0 | 13.4 | 0.509x | 5.038x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 579.3 | 550.0 | 601.1 | 17.8 | 0.528x | 5.229x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,081.6 | 1,070.9 | 1,098.0 | 9.6 | 0.985x | 9.761x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,097.5 | 1,065.5 | 1,117.8 | 18.3 | 1.000x | 9.906x |

### `factored` / `s-078` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 103.5 | 103.3 | 103.8 | 0.2 | 0.096x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 106.6 | 106.4 | 107.4 | 0.4 | 0.098x | 1.030x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 107.4 | 107.3 | 109.8 | 1.0 | 0.099x | 1.037x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 163.1 | 162.8 | 164.4 | 0.6 | 0.151x | 1.576x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 365.5 | 346.9 | 432.1 | 31.1 | 0.337x | 3.531x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 563.9 | 500.6 | 661.2 | 57.8 | 0.521x | 5.448x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 572.8 | 545.5 | 594.7 | 16.0 | 0.529x | 5.534x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 589.9 | 562.7 | 598.4 | 15.5 | 0.545x | 5.700x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,083.2 | 1,065.2 | 1,090.6 | 8.7 | 1.000x | 10.465x |

### `factored` / `s-079` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 111.0 | 110.4 | 128.0 | 6.7 | 0.102x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 130.1 | 129.9 | 130.3 | 0.2 | 0.119x | 1.172x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 160.5 | 160.0 | 169.2 | 3.6 | 0.147x | 1.446x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 380.2 | 329.8 | 401.0 | 25.2 | 0.349x | 3.426x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 528.9 | 504.6 | 569.7 | 22.2 | 0.486x | 4.766x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 557.9 | 549.7 | 578.3 | 10.9 | 0.512x | 5.027x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 584.7 | 564.4 | 589.4 | 9.8 | 0.537x | 5.268x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,075.1 | 1,070.8 | 1,101.9 | 11.4 | 0.987x | 9.688x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,089.2 | 1,066.7 | 1,117.1 | 19.1 | 1.000x | 9.814x |

### `factored` / `s-079` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 103.3 | 103.2 | 103.7 | 0.2 | 0.096x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 106.6 | 106.4 | 107.5 | 0.4 | 0.099x | 1.032x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 107.4 | 107.1 | 108.9 | 0.7 | 0.099x | 1.040x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 163.5 | 162.9 | 163.8 | 0.4 | 0.151x | 1.583x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 370.1 | 341.4 | 436.2 | 33.3 | 0.343x | 3.583x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 564.4 | 492.7 | 650.0 | 52.6 | 0.522x | 5.465x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 582.8 | 536.7 | 619.4 | 29.0 | 0.539x | 5.643x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 593.3 | 570.9 | 612.5 | 14.1 | 0.549x | 5.745x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,080.3 | 1,077.6 | 1,095.8 | 8.3 | 1.000x | 10.461x |

### `factored` / `s-080` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 50.3 | 50.0 | 50.7 | 0.3 | 0.054x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 52.4 | 51.5 | 53.1 | 0.5 | 0.057x | 1.042x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 279.1 | 261.0 | 306.7 | 16.4 | 0.302x | 5.546x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 534.0 | 520.3 | 552.8 | 12.5 | 0.578x | 10.612x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 581.7 | 569.8 | 628.6 | 20.8 | 0.629x | 11.559x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 604.8 | 559.0 | 622.7 | 21.4 | 0.654x | 12.019x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 626.0 | 574.3 | 663.2 | 33.9 | 0.677x | 12.439x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 924.5 | 903.0 | 950.1 | 16.6 | 1.000x | 18.370x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 925.4 | 902.3 | 947.6 | 17.0 | 1.001x | 18.389x |

### `factored` / `s-080` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 44.1 | 43.9 | 44.9 | 0.3 | 0.014x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 44.7 | 44.4 | 45.6 | 0.4 | 0.014x | 1.014x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 321.0 | 307.5 | 325.1 | 6.2 | 0.101x | 7.280x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 1,745.3 | 1,732.9 | 1,788.3 | 19.6 | 0.548x | 39.582x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,756.0 | 1,728.4 | 1,842.0 | 39.1 | 0.551x | 39.824x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,771.1 | 1,713.9 | 2,167.9 | 165.0 | 0.556x | 40.166x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,782.9 | 1,726.8 | 1,866.7 | 44.9 | 0.560x | 40.434x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,939.2 | 1,936.5 | 1,958.0 | 9.3 | 0.609x | 43.978x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,186.6 | 3,136.7 | 3,205.7 | 30.2 | 1.000x | 72.267x |

### `factored` / `s-081` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.4 | 12.1 | 13.5 | 0.5 | 0.407x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.1 | 15.4 | 0.9 | 0.432x | 1.060x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.4 | 30.3 | 30.7 | 0.2 | 1.000x | 2.455x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 30.8 | 30.3 | 33.6 | 1.2 | 1.011x | 2.481x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 51.4 | 51.1 | 52.4 | 0.5 | 1.689x | 4.147x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 290.7 | 258.9 | 292.4 | 13.1 | 9.547x | 23.434x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 387.3 | 365.4 | 417.4 | 20.1 | 12.720x | 31.222x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 432.8 | 415.7 | 454.5 | 13.4 | 14.213x | 34.888x |
| 9 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 436.3 | 390.0 | 482.8 | 30.0 | 14.329x | 35.170x |

### `factored` / `s-081` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 4.7 | 4.7 | 4.9 | 0.1 | 0.156x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 5.1 | 5.0 | 5.9 | 0.3 | 0.166x | 1.065x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.4 | 30.4 | 30.5 | 0.0 | 1.000x | 6.409x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 40.9 | 40.1 | 44.0 | 1.4 | 1.345x | 8.620x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 50.2 | 49.9 | 50.5 | 0.2 | 1.651x | 10.584x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 270.0 | 263.9 | 291.2 | 9.7 | 8.874x | 56.878x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 434.6 | 410.8 | 467.6 | 22.7 | 14.285x | 91.555x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 440.4 | 417.8 | 471.3 | 18.6 | 14.477x | 92.785x |
| 9 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 445.0 | 392.8 | 491.2 | 36.1 | 14.628x | 93.749x |

### `factored` / `s-082` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.2 | 13.0 | 13.6 | 0.2 | 0.434x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 14.0 | 13.9 | 17.0 | 1.2 | 0.462x | 1.065x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.3 | 30.3 | 30.7 | 0.2 | 1.000x | 2.303x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 30.7 | 30.3 | 32.3 | 0.8 | 1.012x | 2.331x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 51.3 | 51.2 | 52.8 | 0.6 | 1.692x | 3.897x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 284.2 | 266.3 | 306.3 | 13.1 | 9.380x | 21.605x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 412.8 | 306.7 | 437.7 | 45.9 | 13.625x | 31.383x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 438.8 | 405.0 | 455.1 | 16.7 | 14.483x | 33.359x |
| 9 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 449.1 | 415.6 | 459.2 | 15.0 | 14.821x | 34.138x |

### `factored` / `s-082` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 5.6 | 5.3 | 5.6 | 0.1 | 0.185x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 5.6 | 5.6 | 5.8 | 0.1 | 0.185x | 1.001x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.4 | 30.4 | 30.7 | 0.1 | 1.000x | 5.402x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 40.4 | 40.2 | 43.9 | 1.4 | 1.330x | 7.187x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 67.8 | 67.5 | 69.3 | 0.8 | 2.231x | 12.055x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 286.9 | 278.9 | 305.7 | 9.6 | 9.438x | 50.987x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 454.5 | 450.9 | 473.3 | 8.1 | 14.952x | 80.781x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 456.9 | 412.6 | 512.6 | 32.1 | 15.033x | 81.218x |
| 9 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 468.2 | 430.4 | 496.4 | 27.4 | 15.404x | 83.221x |

### `factored` / `s-083` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 34.1 | 33.6 | 35.3 | 0.6 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 34.4 | 33.5 | 35.4 | 0.8 | 1.006x | 1.006x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 115.4 | 113.3 | 116.1 | 0.9 | 3.380x | 3.380x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 138.4 | 138.0 | 140.2 | 0.8 | 4.055x | 4.055x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 139.4 | 139.0 | 140.1 | 0.4 | 4.085x | 4.085x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 340.2 | 334.1 | 350.5 | 5.7 | 9.966x | 9.966x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 476.3 | 445.6 | 616.2 | 59.8 | 13.953x | 13.953x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 495.6 | 451.7 | 523.8 | 24.0 | 14.518x | 14.518x |
| 9 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 530.0 | 459.6 | 571.3 | 37.8 | 15.527x | 15.527x |

### `factored` / `s-083` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 34.7 | 34.6 | 35.7 | 0.4 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.4 | 46.2 | 46.6 | 0.2 | 1.337x | 1.337x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 132.4 | 132.1 | 132.9 | 0.3 | 3.814x | 3.814x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 133.4 | 132.6 | 134.1 | 0.5 | 3.843x | 3.843x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 2,889.6 | 2,868.4 | 3,035.0 | 62.0 | 83.241x | 83.241x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 3,129.7 | 3,018.7 | 3,181.6 | 57.1 | 90.156x | 90.156x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 3,395.1 | 3,371.3 | 3,485.3 | 41.6 | 97.802x | 97.802x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 3,402.5 | 3,328.7 | 3,482.9 | 48.9 | 98.017x | 98.017x |
| 9 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 3,437.5 | 3,405.4 | 3,452.8 | 19.5 | 99.024x | 99.024x |

### `factored` / `s-084` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 30.5 | 30.0 | 30.5 | 0.3 | 0.920x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 32.0 | 31.9 | 32.1 | 0.1 | 0.967x | 1.051x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 33.1 | 32.7 | 33.4 | 0.3 | 1.000x | 1.087x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 34.7 | 34.3 | 35.5 | 0.4 | 1.048x | 1.140x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 169.6 | 164.6 | 175.9 | 3.8 | 5.123x | 5.570x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 392.6 | 389.3 | 402.1 | 5.0 | 11.859x | 12.893x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 596.3 | 570.5 | 655.3 | 31.9 | 18.012x | 19.583x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 622.9 | 611.6 | 646.8 | 12.4 | 18.815x | 20.456x |
| 9 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 636.2 | 568.5 | 662.4 | 33.0 | 19.218x | 20.893x |

### `factored` / `s-084` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 25.4 | 25.3 | 25.4 | 0.1 | 0.739x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 25.7 | 25.6 | 25.9 | 0.1 | 0.749x | 1.014x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 34.3 | 33.9 | 35.2 | 0.5 | 1.000x | 1.353x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.4 | 44.3 | 45.4 | 0.4 | 1.296x | 1.752x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 811.1 | 763.1 | 839.1 | 25.9 | 23.645x | 31.980x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 998.5 | 971.7 | 1,048.5 | 25.3 | 29.108x | 39.370x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,581.2 | 1,541.0 | 1,659.0 | 42.0 | 46.097x | 62.348x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,632.7 | 1,596.8 | 1,697.4 | 35.4 | 47.595x | 64.375x |
| 9 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,636.8 | 1,579.9 | 1,672.1 | 32.8 | 47.716x | 64.538x |

### `factored` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 6,539,817.9 | 6,535,168.5 | 6,583,374.8 | 18,132.0 | 0.127x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 6,570,736.9 | 6,559,306.8 | 6,578,083.4 | 6,035.8 | 0.127x | 1.005x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 7,045,186.7 | 6,964,179.7 | 7,172,586.3 | 77,777.1 | 0.136x | 1.077x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 10,975,556.0 | 10,898,005.0 | 11,025,015.0 | 46,442.2 | 0.212x | 1.678x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 18,612,288.0 | 17,644,272.0 | 19,618,594.0 | 627,811.6 | 0.360x | 2.846x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 23,646,430.0 | 22,861,735.0 | 26,823,629.0 | 1,442,212.7 | 0.458x | 3.616x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 24,010,552.0 | 22,722,773.0 | 25,261,380.0 | 825,072.6 | 0.465x | 3.671x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 24,014,597.0 | 22,956,700.0 | 26,418,041.0 | 1,195,438.1 | 0.465x | 3.672x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 51,683,548.2 | 51,604,416.3 | 51,711,641.4 | 43,484.2 | 1.000x | 7.903x |

### `factored` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,806.7 | 17,772.2 | 18,838.0 | 414.9 | 1.000x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 3,419,441.5 | 3,418,725.1 | 3,426,328.7 | 2,853.8 | 192.031x | 192.031x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 3,421,484.3 | 3,416,567.5 | 4,724,445.7 | 521,176.7 | 192.146x | 192.146x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 17,718,011.3 | 17,676,191.0 | 17,781,863.7 | 38,931.5 | 995.020x | 995.020x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 84,138,418.0 | 83,753,954.0 | 84,516,340.0 | 281,935.0 | 4725.104x | 4725.104x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 87,151,691.0 | 87,056,790.0 | 87,870,905.0 | 296,577.9 | 4894.325x | 4894.325x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 88,138,127.0 | 87,017,010.0 | 91,290,196.0 | 1,439,973.1 | 4949.722x | 4949.722x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 88,760,543.0 | 87,217,943.0 | 92,820,847.0 | 1,915,173.9 | 4984.676x | 4984.676x |
| 9 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 89,148,076.0 | 82,492,434.0 | 90,456,955.0 | 3,365,895.9 | 5006.439x | 5006.439x |

### `factored` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,846.9 | 17,758.3 | 17,884.5 | 46.4 | 1.000x | 1.000x | 5 | 100% |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 3,415,366.5 | 3,415,030.1 | 3,423,255.1 | 3,131.4 | 191.371x | 191.371x | 5 | 100% |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 3,420,959.6 | 3,414,692.2 | 3,453,153.8 | 14,149.7 | 191.684x | 191.684x | 5 | 100% |

### `orig` / `s-000` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 47.2 | 46.6 | 48.7 | 0.8 | 0.086x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 111.2 | 110.8 | 112.9 | 0.7 | 0.203x | 2.356x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 111.3 | 110.9 | 111.4 | 0.2 | 0.203x | 2.358x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 111.5 | 111.2 | 112.1 | 0.3 | 0.203x | 2.363x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 111.7 | 110.8 | 120.8 | 3.7 | 0.204x | 2.368x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 236.1 | 223.8 | 252.6 | 10.6 | 0.431x | 5.005x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 244.1 | 220.6 | 275.8 | 17.7 | 0.445x | 5.174x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 548.2 | 544.4 | 670.5 | 48.5 | 1.000x | 11.620x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 552.3 | 541.5 | 588.1 | 17.0 | 1.007x | 11.705x |

### `orig` / `s-000` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 54.4 | 54.1 | 55.2 | 0.4 | 0.099x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 77.4 | 76.8 | 78.4 | 0.7 | 0.141x | 1.424x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 103.1 | 102.7 | 103.7 | 0.4 | 0.187x | 1.897x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 103.5 | 103.3 | 110.1 | 2.7 | 0.188x | 1.903x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 103.6 | 103.4 | 113.8 | 4.1 | 0.188x | 1.905x |
| 6 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 103.7 | 103.4 | 103.9 | 0.2 | 0.188x | 1.907x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 230.2 | 223.7 | 244.6 | 7.4 | 0.418x | 4.235x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 254.2 | 250.8 | 258.6 | 2.6 | 0.462x | 4.675x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 550.6 | 544.2 | 558.9 | 4.9 | 1.000x | 10.128x |

### `orig` / `s-001` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 97.3 | 97.2 | 105.6 | 3.3 | 0.128x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 143.8 | 143.5 | 153.3 | 3.8 | 0.189x | 1.478x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 143.9 | 143.8 | 144.8 | 0.4 | 0.189x | 1.479x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 144.1 | 143.6 | 146.4 | 1.0 | 0.189x | 1.481x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 144.4 | 143.9 | 144.7 | 0.3 | 0.190x | 1.484x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 271.7 | 251.3 | 306.7 | 19.4 | 0.357x | 2.791x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 281.3 | 260.5 | 307.1 | 15.4 | 0.370x | 2.890x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 760.5 | 755.6 | 773.2 | 6.4 | 1.000x | 7.814x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 772.7 | 759.0 | 810.7 | 18.0 | 1.016x | 7.939x |

### `orig` / `s-001` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 92.4 | 92.3 | 92.5 | 0.1 | 0.121x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 92.9 | 92.2 | 93.4 | 0.5 | 0.121x | 1.005x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 135.4 | 135.0 | 136.1 | 0.3 | 0.177x | 1.466x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 135.9 | 135.4 | 136.3 | 0.3 | 0.177x | 1.470x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 136.0 | 135.7 | 138.5 | 1.1 | 0.178x | 1.471x |
| 6 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 136.1 | 136.0 | 148.7 | 4.9 | 0.178x | 1.473x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 243.6 | 217.8 | 284.7 | 24.0 | 0.318x | 2.636x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 265.5 | 237.4 | 280.0 | 14.8 | 0.347x | 2.872x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 765.7 | 757.5 | 777.0 | 7.2 | 1.000x | 8.286x |

### `orig` / `s-002` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 33.4 | 33.1 | 35.0 | 0.7 | 0.069x | 1.000x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 46.0 | 45.5 | 46.1 | 0.2 | 0.095x | 1.377x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 46.2 | 46.1 | 52.5 | 2.6 | 0.095x | 1.382x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 46.2 | 46.0 | 55.8 | 3.8 | 0.095x | 1.384x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 46.2 | 46.2 | 46.7 | 0.2 | 0.095x | 1.384x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 235.6 | 220.9 | 251.2 | 11.4 | 0.487x | 7.056x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 241.2 | 221.1 | 266.4 | 16.5 | 0.498x | 7.222x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 482.1 | 475.8 | 503.8 | 10.2 | 0.996x | 14.437x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 484.2 | 474.9 | 496.3 | 7.1 | 1.000x | 14.499x |

### `orig` / `s-002` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 38.5 | 38.4 | 39.0 | 0.2 | 0.080x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 38.5 | 38.4 | 38.8 | 0.2 | 0.080x | 1.002x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 38.6 | 38.4 | 38.6 | 0.1 | 0.080x | 1.003x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 38.7 | 38.5 | 39.2 | 0.2 | 0.080x | 1.007x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 38.9 | 38.7 | 39.6 | 0.4 | 0.080x | 1.012x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 63.9 | 61.4 | 64.7 | 1.2 | 0.132x | 1.662x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 228.4 | 206.3 | 259.3 | 16.9 | 0.472x | 5.939x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 246.9 | 238.6 | 297.3 | 21.9 | 0.510x | 6.418x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 483.7 | 476.3 | 486.2 | 3.5 | 1.000x | 12.574x |

### `orig` / `s-003` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 60.9 | 60.1 | 76.4 | 6.2 | 0.079x | 1.000x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 156.9 | 156.9 | 159.4 | 1.0 | 0.203x | 2.575x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 157.1 | 156.8 | 157.7 | 0.4 | 0.203x | 2.577x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 157.5 | 157.1 | 170.6 | 5.2 | 0.203x | 2.584x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 157.5 | 156.6 | 166.9 | 3.9 | 0.203x | 2.585x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 247.4 | 244.9 | 301.2 | 22.1 | 0.320x | 4.059x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 258.5 | 251.3 | 276.4 | 10.0 | 0.334x | 4.242x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 768.2 | 761.8 | 796.8 | 12.6 | 0.992x | 12.605x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 774.2 | 762.6 | 775.2 | 4.7 | 1.000x | 12.704x |

### `orig` / `s-003` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 67.9 | 67.1 | 68.5 | 0.5 | 0.089x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 92.4 | 90.6 | 97.6 | 2.5 | 0.120x | 1.360x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 147.6 | 146.9 | 147.7 | 0.3 | 0.192x | 2.172x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 147.8 | 147.6 | 150.9 | 1.2 | 0.193x | 2.176x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 148.1 | 147.9 | 149.6 | 0.6 | 0.193x | 2.180x |
| 6 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 148.2 | 147.6 | 148.4 | 0.3 | 0.193x | 2.181x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 255.5 | 236.4 | 295.6 | 21.3 | 0.333x | 3.761x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 277.2 | 254.3 | 337.0 | 27.6 | 0.361x | 4.080x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 767.6 | 764.5 | 776.9 | 4.4 | 1.000x | 11.299x |

### `orig` / `s-004` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 61.8 | 60.7 | 76.6 | 6.1 | 0.109x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 222.3 | 221.8 | 224.5 | 1.0 | 0.392x | 3.597x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 222.4 | 221.4 | 222.7 | 0.5 | 0.392x | 3.598x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 222.4 | 221.6 | 231.5 | 3.7 | 0.392x | 3.598x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 222.6 | 221.6 | 227.4 | 2.1 | 0.392x | 3.602x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 256.1 | 228.2 | 280.4 | 17.0 | 0.451x | 4.144x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 261.4 | 252.2 | 274.1 | 8.8 | 0.461x | 4.230x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 560.9 | 557.0 | 585.3 | 10.1 | 0.988x | 9.075x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 567.5 | 562.0 | 576.0 | 5.6 | 1.000x | 9.182x |

### `orig` / `s-004` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 68.1 | 67.2 | 69.1 | 0.6 | 0.120x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 92.8 | 91.4 | 96.3 | 1.6 | 0.163x | 1.362x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 213.5 | 213.0 | 214.2 | 0.4 | 0.376x | 3.133x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 213.7 | 213.3 | 217.8 | 1.7 | 0.376x | 3.137x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 214.2 | 213.9 | 214.8 | 0.4 | 0.377x | 3.144x |
| 6 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 214.8 | 214.0 | 215.2 | 0.4 | 0.378x | 3.153x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 272.8 | 245.9 | 318.3 | 24.1 | 0.480x | 4.004x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 276.1 | 232.0 | 295.0 | 22.4 | 0.486x | 4.053x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 568.1 | 563.3 | 572.4 | 3.0 | 1.000x | 8.338x |

### `orig` / `s-005` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 33.5 | 33.3 | 33.9 | 0.2 | 0.070x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 45.9 | 45.5 | 46.6 | 0.3 | 0.096x | 1.372x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 46.0 | 45.9 | 48.2 | 0.9 | 0.096x | 1.375x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 46.1 | 45.8 | 46.6 | 0.3 | 0.096x | 1.378x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 46.2 | 46.1 | 55.6 | 3.8 | 0.096x | 1.379x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 242.7 | 232.2 | 250.0 | 6.5 | 0.506x | 7.250x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 253.0 | 221.8 | 279.5 | 23.4 | 0.528x | 7.558x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 479.1 | 474.5 | 503.3 | 10.4 | 0.999x | 14.314x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 479.4 | 474.1 | 483.0 | 2.9 | 1.000x | 14.322x |

### `orig` / `s-005` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 38.3 | 38.2 | 38.5 | 0.1 | 0.080x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 38.6 | 38.3 | 49.8 | 4.4 | 0.080x | 1.006x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 38.6 | 38.6 | 40.1 | 0.6 | 0.080x | 1.008x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 38.7 | 38.5 | 38.8 | 0.1 | 0.080x | 1.009x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 38.8 | 38.6 | 38.9 | 0.1 | 0.081x | 1.011x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 64.2 | 63.0 | 64.8 | 0.6 | 0.134x | 1.675x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 263.8 | 211.1 | 282.8 | 27.5 | 0.549x | 6.879x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 275.7 | 250.2 | 289.2 | 15.2 | 0.573x | 7.189x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 480.9 | 476.3 | 490.5 | 5.3 | 1.000x | 12.539x |

### `orig` / `s-006` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 103.8 | 103.6 | 104.0 | 0.1 | 0.133x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 104.0 | 104.0 | 115.5 | 4.5 | 0.133x | 1.002x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 104.2 | 103.4 | 105.0 | 0.6 | 0.133x | 1.004x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 104.3 | 104.1 | 104.5 | 0.1 | 0.133x | 1.004x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 121.5 | 121.1 | 122.5 | 0.4 | 0.155x | 1.171x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 303.6 | 282.5 | 315.6 | 10.9 | 0.388x | 2.924x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 314.0 | 300.3 | 316.2 | 5.7 | 0.402x | 3.024x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 781.2 | 776.3 | 829.0 | 20.0 | 0.999x | 7.523x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 781.7 | 773.7 | 808.5 | 11.8 | 1.000x | 7.529x |

### `orig` / `s-006` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 84.2 | 83.7 | 85.2 | 0.6 | 0.107x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 96.4 | 96.4 | 98.4 | 0.8 | 0.122x | 1.145x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 96.8 | 96.6 | 97.1 | 0.1 | 0.123x | 1.150x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 96.9 | 96.4 | 98.8 | 0.9 | 0.123x | 1.151x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 97.4 | 97.0 | 97.6 | 0.2 | 0.124x | 1.157x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 133.1 | 131.7 | 133.2 | 0.6 | 0.169x | 1.581x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 335.9 | 296.4 | 364.4 | 23.7 | 0.426x | 3.989x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 352.6 | 293.4 | 396.7 | 33.3 | 0.447x | 4.188x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 788.2 | 780.2 | 792.2 | 4.8 | 1.000x | 9.360x |

### `orig` / `s-007` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 55.6 | 55.4 | 59.7 | 1.6 | 0.090x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 169.8 | 169.3 | 170.3 | 0.3 | 0.275x | 3.055x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 169.9 | 169.2 | 179.1 | 3.7 | 0.275x | 3.056x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 169.9 | 169.5 | 174.0 | 1.7 | 0.275x | 3.057x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 170.1 | 169.6 | 170.2 | 0.2 | 0.275x | 3.060x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 261.1 | 258.3 | 270.6 | 4.6 | 0.423x | 4.698x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 283.1 | 242.7 | 288.7 | 18.4 | 0.458x | 5.093x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 617.8 | 611.9 | 624.9 | 4.4 | 1.000x | 11.113x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 618.6 | 613.0 | 641.3 | 9.9 | 1.001x | 11.129x |

### `orig` / `s-007` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 65.0 | 63.7 | 65.8 | 0.7 | 0.104x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 91.2 | 89.7 | 95.0 | 1.9 | 0.146x | 1.402x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 161.9 | 161.7 | 162.4 | 0.3 | 0.259x | 2.489x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 162.0 | 161.7 | 164.0 | 0.8 | 0.260x | 2.492x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 162.1 | 161.2 | 162.8 | 0.5 | 0.260x | 2.493x |
| 6 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 162.2 | 162.2 | 164.7 | 1.0 | 0.260x | 2.495x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 279.9 | 234.4 | 291.7 | 19.8 | 0.449x | 4.304x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 302.5 | 275.2 | 323.3 | 16.4 | 0.485x | 4.653x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 624.0 | 616.9 | 629.2 | 5.2 | 1.000x | 9.596x |

### `orig` / `s-008` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 49.5 | 48.9 | 53.7 | 1.8 | 0.091x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 129.5 | 129.4 | 133.5 | 1.6 | 0.239x | 2.619x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 129.8 | 129.3 | 130.3 | 0.4 | 0.240x | 2.624x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 130.0 | 129.8 | 143.8 | 5.5 | 0.240x | 2.629x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 130.2 | 129.6 | 130.6 | 0.4 | 0.240x | 2.633x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 262.0 | 260.4 | 268.0 | 2.8 | 0.484x | 5.297x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 293.5 | 267.5 | 298.2 | 12.4 | 0.542x | 5.935x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 538.0 | 534.1 | 566.6 | 11.7 | 0.993x | 10.879x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 541.7 | 539.7 | 547.7 | 3.3 | 1.000x | 10.954x |

### `orig` / `s-008` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 56.4 | 56.1 | 57.2 | 0.4 | 0.103x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 79.6 | 78.7 | 80.6 | 0.6 | 0.146x | 1.411x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 122.4 | 122.0 | 122.7 | 0.3 | 0.224x | 2.168x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 122.6 | 122.3 | 123.1 | 0.3 | 0.225x | 2.172x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 123.2 | 122.0 | 131.8 | 3.6 | 0.226x | 2.183x |
| 6 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 123.5 | 122.6 | 125.9 | 1.2 | 0.226x | 2.188x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 282.0 | 230.1 | 290.5 | 21.6 | 0.517x | 4.997x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 285.1 | 261.1 | 313.0 | 18.8 | 0.522x | 5.051x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 545.7 | 537.2 | 553.7 | 5.5 | 1.000x | 9.668x |

### `orig` / `s-009` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 45.5 | 45.2 | 61.0 | 6.1 | 0.084x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 96.9 | 96.7 | 97.5 | 0.3 | 0.180x | 2.132x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 97.0 | 96.7 | 111.8 | 6.0 | 0.180x | 2.135x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 97.1 | 96.7 | 97.6 | 0.3 | 0.180x | 2.136x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 97.5 | 97.3 | 98.0 | 0.3 | 0.181x | 2.145x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 258.5 | 255.3 | 259.8 | 1.6 | 0.480x | 5.686x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 288.4 | 262.1 | 296.1 | 12.4 | 0.536x | 6.346x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 538.2 | 532.7 | 541.2 | 3.1 | 1.000x | 11.840x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 543.5 | 533.2 | 567.6 | 14.4 | 1.010x | 11.957x |

### `orig` / `s-009` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 52.6 | 51.8 | 52.9 | 0.4 | 0.098x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 75.0 | 72.4 | 79.1 | 2.2 | 0.139x | 1.426x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 89.8 | 89.5 | 90.2 | 0.3 | 0.167x | 1.708x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 90.0 | 89.8 | 90.4 | 0.2 | 0.167x | 1.712x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 90.1 | 89.9 | 91.1 | 0.5 | 0.167x | 1.713x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 90.2 | 89.8 | 90.8 | 0.3 | 0.167x | 1.715x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 277.0 | 228.1 | 282.1 | 20.2 | 0.514x | 5.269x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 284.9 | 255.7 | 308.0 | 16.7 | 0.529x | 5.418x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 538.9 | 533.2 | 552.0 | 6.9 | 1.000x | 10.250x |

### `orig` / `s-010` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 32.9 | 32.4 | 34.3 | 0.7 | 0.075x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 97.1 | 96.7 | 97.7 | 0.3 | 0.222x | 2.949x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 97.1 | 96.7 | 98.2 | 0.5 | 0.222x | 2.950x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 97.3 | 96.9 | 107.5 | 4.2 | 0.222x | 2.955x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 97.7 | 97.2 | 102.7 | 2.5 | 0.224x | 2.969x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 247.6 | 240.4 | 252.1 | 4.3 | 0.566x | 7.523x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 264.9 | 258.3 | 270.5 | 4.0 | 0.606x | 8.050x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 437.2 | 435.3 | 442.0 | 2.8 | 1.000x | 13.283x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 439.5 | 433.5 | 454.6 | 7.0 | 1.005x | 13.354x |

### `orig` / `s-010` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 37.7 | 37.2 | 38.0 | 0.3 | 0.087x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 69.2 | 68.2 | 71.5 | 1.1 | 0.159x | 1.833x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 89.6 | 89.5 | 90.0 | 0.2 | 0.206x | 2.372x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 89.8 | 89.5 | 90.0 | 0.2 | 0.206x | 2.380x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 90.2 | 89.8 | 90.8 | 0.3 | 0.207x | 2.391x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 90.8 | 89.3 | 91.6 | 0.8 | 0.209x | 2.404x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 244.4 | 232.4 | 253.7 | 9.1 | 0.562x | 6.476x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 254.4 | 213.4 | 266.8 | 18.7 | 0.585x | 6.739x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 435.1 | 431.8 | 446.6 | 5.3 | 1.000x | 11.526x |

### `orig` / `s-011` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 33.8 | 33.6 | 35.6 | 0.7 | 0.098x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 69.5 | 69.4 | 70.1 | 0.3 | 0.201x | 2.057x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 69.5 | 69.3 | 70.0 | 0.2 | 0.201x | 2.057x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 69.6 | 69.3 | 81.9 | 4.9 | 0.201x | 2.059x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 69.6 | 69.5 | 75.8 | 2.5 | 0.202x | 2.061x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 255.3 | 254.0 | 262.3 | 3.0 | 0.739x | 7.556x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 308.4 | 273.8 | 328.8 | 18.1 | 0.893x | 9.128x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 340.5 | 338.4 | 358.9 | 7.4 | 0.986x | 10.080x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 345.4 | 341.6 | 352.0 | 3.4 | 1.000x | 10.223x |

### `orig` / `s-011` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 63.6 | 63.4 | 64.9 | 0.6 | 0.036x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 63.7 | 63.4 | 64.7 | 0.5 | 0.036x | 1.001x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 63.8 | 63.8 | 64.6 | 0.3 | 0.036x | 1.003x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 64.0 | 63.8 | 64.1 | 0.1 | 0.036x | 1.006x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 140.2 | 138.7 | 150.5 | 4.3 | 0.078x | 2.203x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 317.0 | 315.4 | 320.7 | 2.2 | 0.177x | 4.981x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 536.4 | 493.8 | 547.9 | 19.2 | 0.300x | 8.429x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 583.5 | 550.3 | 590.8 | 14.8 | 0.327x | 9.168x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,786.5 | 1,746.7 | 1,799.1 | 19.5 | 1.000x | 28.071x |

### `orig` / `s-012` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 80.3 | 80.1 | 81.0 | 0.3 | 0.117x | 1.000x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 123.3 | 122.9 | 124.4 | 0.5 | 0.180x | 1.535x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 123.3 | 123.3 | 127.1 | 1.5 | 0.180x | 1.536x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 123.6 | 123.4 | 126.9 | 1.3 | 0.181x | 1.539x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 123.8 | 123.3 | 134.5 | 5.0 | 0.181x | 1.541x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 279.3 | 274.8 | 283.3 | 3.1 | 0.408x | 3.477x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 306.5 | 274.5 | 356.2 | 27.4 | 0.448x | 3.815x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 676.7 | 671.9 | 697.8 | 9.3 | 0.989x | 8.425x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 684.4 | 676.1 | 688.4 | 4.3 | 1.000x | 8.520x |

### `orig` / `s-012` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 82.2 | 81.1 | 84.0 | 1.0 | 0.120x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 82.6 | 82.1 | 85.1 | 1.1 | 0.121x | 1.005x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 115.1 | 114.9 | 120.2 | 2.0 | 0.169x | 1.401x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 115.3 | 115.2 | 115.9 | 0.3 | 0.169x | 1.403x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 115.4 | 115.3 | 115.7 | 0.1 | 0.169x | 1.404x |
| 6 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 115.5 | 115.4 | 115.7 | 0.1 | 0.169x | 1.406x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 296.0 | 270.1 | 333.2 | 20.4 | 0.434x | 3.603x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 307.5 | 286.1 | 329.4 | 14.5 | 0.450x | 3.742x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 682.7 | 674.1 | 683.1 | 3.6 | 1.000x | 8.309x |

### `orig` / `s-013` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 80.5 | 80.4 | 80.7 | 0.1 | 0.118x | 1.000x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 123.1 | 122.7 | 123.8 | 0.4 | 0.180x | 1.529x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 123.4 | 123.0 | 124.0 | 0.3 | 0.181x | 1.533x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 123.5 | 123.4 | 134.2 | 4.3 | 0.181x | 1.534x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 123.6 | 123.5 | 123.7 | 0.1 | 0.181x | 1.535x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 278.5 | 274.2 | 284.6 | 3.5 | 0.407x | 3.458x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 306.7 | 268.7 | 348.1 | 25.9 | 0.449x | 3.809x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 680.8 | 678.4 | 699.7 | 7.8 | 0.996x | 8.454x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 683.6 | 677.0 | 687.6 | 3.9 | 1.000x | 8.490x |

### `orig` / `s-013` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 81.7 | 80.9 | 85.1 | 1.5 | 0.119x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 82.2 | 82.0 | 82.5 | 0.2 | 0.120x | 1.006x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 115.2 | 114.9 | 116.8 | 0.7 | 0.168x | 1.410x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 115.5 | 115.3 | 119.5 | 1.6 | 0.169x | 1.414x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 115.5 | 115.2 | 116.0 | 0.3 | 0.169x | 1.414x |
| 6 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 115.6 | 115.5 | 116.1 | 0.2 | 0.169x | 1.414x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 299.2 | 291.3 | 312.3 | 6.9 | 0.437x | 3.662x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 309.6 | 278.9 | 332.4 | 17.2 | 0.452x | 3.789x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 684.5 | 679.3 | 691.0 | 4.2 | 1.000x | 8.379x |

### `orig` / `s-014` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 50.2 | 50.1 | 50.5 | 0.1 | 0.093x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 96.7 | 96.7 | 97.6 | 0.4 | 0.179x | 1.926x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 97.0 | 96.7 | 97.5 | 0.3 | 0.180x | 1.932x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 97.2 | 97.1 | 98.0 | 0.3 | 0.180x | 1.934x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 97.3 | 97.0 | 113.6 | 6.5 | 0.180x | 1.937x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 265.8 | 262.8 | 275.2 | 4.4 | 0.493x | 5.293x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 293.9 | 267.8 | 298.7 | 11.3 | 0.544x | 5.851x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 538.2 | 535.4 | 550.2 | 5.3 | 0.997x | 10.717x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 539.7 | 536.2 | 558.0 | 7.7 | 1.000x | 10.746x |

### `orig` / `s-014` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 66.3 | 66.1 | 67.3 | 0.4 | 0.122x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 75.9 | 75.0 | 79.3 | 1.6 | 0.140x | 1.145x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 89.9 | 89.6 | 90.2 | 0.2 | 0.166x | 1.356x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 89.9 | 89.8 | 90.8 | 0.4 | 0.166x | 1.356x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 89.9 | 89.8 | 90.9 | 0.4 | 0.166x | 1.357x |
| 6 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 90.2 | 89.9 | 90.7 | 0.3 | 0.166x | 1.360x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 287.4 | 282.0 | 290.4 | 2.8 | 0.530x | 4.335x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 327.4 | 292.0 | 372.6 | 26.6 | 0.604x | 4.938x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 542.2 | 532.1 | 549.4 | 5.9 | 1.000x | 8.177x |

### `orig` / `s-015` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 74.7 | 74.6 | 75.8 | 0.5 | 0.113x | 1.000x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 117.0 | 116.8 | 117.3 | 0.2 | 0.177x | 1.566x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 117.0 | 116.7 | 117.6 | 0.3 | 0.177x | 1.567x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 117.2 | 116.9 | 118.5 | 0.6 | 0.177x | 1.569x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 118.5 | 117.0 | 128.2 | 5.1 | 0.179x | 1.587x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 276.0 | 275.5 | 294.5 | 7.3 | 0.418x | 3.695x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 301.6 | 285.1 | 323.9 | 14.6 | 0.457x | 4.038x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 655.5 | 654.9 | 667.7 | 5.9 | 0.992x | 8.776x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 660.5 | 656.4 | 664.9 | 3.2 | 1.000x | 8.843x |

### `orig` / `s-015` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 80.2 | 79.3 | 82.9 | 1.3 | 0.123x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 80.3 | 80.2 | 80.6 | 0.2 | 0.123x | 1.001x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 109.7 | 109.4 | 110.0 | 0.2 | 0.168x | 1.368x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 109.8 | 109.6 | 109.9 | 0.1 | 0.168x | 1.369x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 109.9 | 109.6 | 112.1 | 0.9 | 0.168x | 1.370x |
| 6 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 110.0 | 109.9 | 111.5 | 0.7 | 0.168x | 1.371x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 293.9 | 288.9 | 305.8 | 6.0 | 0.450x | 3.665x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 303.2 | 281.3 | 325.2 | 14.8 | 0.464x | 3.780x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 653.3 | 652.4 | 659.4 | 3.1 | 1.000x | 8.146x |

### `orig` / `s-016` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.0 | 25.8 | 27.4 | 0.6 | 0.139x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 52.9 | 52.7 | 58.9 | 2.4 | 0.283x | 2.037x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 53.0 | 52.4 | 54.9 | 0.9 | 0.284x | 2.043x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 53.1 | 52.9 | 53.3 | 0.1 | 0.284x | 2.044x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 53.1 | 53.0 | 53.4 | 0.1 | 0.284x | 2.045x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 185.9 | 184.9 | 194.6 | 3.7 | 0.995x | 7.156x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 186.7 | 185.5 | 190.2 | 1.6 | 1.000x | 7.189x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 248.5 | 246.9 | 255.3 | 3.1 | 1.331x | 9.567x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 291.5 | 271.4 | 307.1 | 11.6 | 1.561x | 11.225x |

### `orig` / `s-016` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 47.3 | 47.1 | 48.0 | 0.3 | 0.044x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 47.4 | 47.2 | 48.2 | 0.4 | 0.044x | 1.002x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 47.4 | 47.3 | 47.6 | 0.1 | 0.044x | 1.002x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 47.4 | 47.3 | 62.3 | 6.0 | 0.044x | 1.003x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 108.7 | 106.6 | 109.4 | 1.0 | 0.100x | 2.299x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 226.9 | 226.3 | 229.9 | 1.3 | 0.210x | 4.799x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 446.4 | 431.5 | 453.3 | 7.2 | 0.412x | 9.439x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 470.8 | 447.0 | 490.7 | 14.2 | 0.435x | 9.956x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,082.9 | 1,077.7 | 1,094.8 | 6.1 | 1.000x | 22.900x |

### `orig` / `s-017` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 80.6 | 80.2 | 80.7 | 0.2 | 0.119x | 1.000x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 123.1 | 122.9 | 123.2 | 0.1 | 0.182x | 1.528x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 123.3 | 123.1 | 123.7 | 0.2 | 0.182x | 1.530x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 123.7 | 123.3 | 124.5 | 0.4 | 0.183x | 1.535x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 123.7 | 123.2 | 139.4 | 6.3 | 0.183x | 1.535x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 284.3 | 279.1 | 285.5 | 2.3 | 0.420x | 3.528x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 321.5 | 292.8 | 339.6 | 17.6 | 0.475x | 3.990x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 674.6 | 669.8 | 688.8 | 7.0 | 0.997x | 8.371x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 676.4 | 666.8 | 696.1 | 9.7 | 1.000x | 8.394x |

### `orig` / `s-017` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 82.1 | 82.0 | 82.8 | 0.3 | 0.121x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 82.3 | 81.3 | 85.1 | 1.3 | 0.121x | 1.001x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 115.2 | 115.1 | 116.1 | 0.4 | 0.170x | 1.402x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 115.6 | 115.3 | 116.9 | 0.6 | 0.170x | 1.408x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 115.8 | 115.2 | 116.9 | 0.6 | 0.171x | 1.409x |
| 6 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 116.5 | 115.7 | 123.3 | 2.8 | 0.172x | 1.418x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 305.8 | 286.8 | 319.2 | 11.4 | 0.451x | 3.723x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 307.6 | 295.2 | 325.7 | 10.5 | 0.453x | 3.745x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 678.7 | 669.7 | 687.7 | 6.2 | 1.000x | 8.262x |

### `orig` / `s-018` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 74.4 | 74.3 | 74.8 | 0.2 | 0.113x | 1.000x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 117.0 | 116.9 | 117.5 | 0.2 | 0.177x | 1.572x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 117.2 | 116.7 | 122.3 | 2.1 | 0.178x | 1.575x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 117.5 | 117.3 | 140.9 | 9.3 | 0.178x | 1.579x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 117.8 | 116.9 | 123.8 | 2.6 | 0.179x | 1.583x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 281.2 | 280.4 | 283.8 | 1.2 | 0.427x | 3.778x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 312.3 | 268.1 | 331.3 | 21.9 | 0.474x | 4.196x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 655.3 | 651.3 | 665.3 | 4.9 | 0.994x | 8.805x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 659.3 | 657.7 | 674.4 | 6.3 | 1.000x | 8.859x |

### `orig` / `s-018` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 80.0 | 79.0 | 83.6 | 1.6 | 0.122x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 80.6 | 80.3 | 80.9 | 0.2 | 0.123x | 1.008x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 109.6 | 109.5 | 112.4 | 1.1 | 0.167x | 1.371x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 109.7 | 109.6 | 110.1 | 0.2 | 0.167x | 1.372x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 109.7 | 109.6 | 111.2 | 0.6 | 0.167x | 1.373x |
| 6 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 110.0 | 109.8 | 113.1 | 1.3 | 0.168x | 1.376x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 291.5 | 287.3 | 301.9 | 5.9 | 0.444x | 3.646x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 306.0 | 279.9 | 323.8 | 14.3 | 0.466x | 3.827x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 656.5 | 650.5 | 665.6 | 5.0 | 1.000x | 8.211x |

### `orig` / `s-019` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.6 | 26.5 | 27.4 | 0.4 | 0.138x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 56.3 | 56.2 | 57.0 | 0.3 | 0.292x | 2.116x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 56.4 | 56.2 | 56.7 | 0.1 | 0.292x | 2.122x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 56.7 | 56.4 | 57.0 | 0.2 | 0.294x | 2.133x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 56.8 | 56.4 | 60.0 | 1.3 | 0.294x | 2.136x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 193.0 | 191.4 | 196.0 | 1.6 | 1.000x | 7.258x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 193.2 | 190.1 | 196.9 | 2.4 | 1.001x | 7.267x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 253.8 | 244.3 | 254.3 | 4.1 | 1.316x | 9.548x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 288.9 | 241.3 | 310.6 | 24.4 | 1.497x | 10.865x |

### `orig` / `s-019` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 50.5 | 50.4 | 50.7 | 0.1 | 0.046x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 50.7 | 50.3 | 52.1 | 0.7 | 0.047x | 1.003x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 50.8 | 50.4 | 51.3 | 0.3 | 0.047x | 1.005x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 51.2 | 50.7 | 52.1 | 0.5 | 0.047x | 1.014x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 110.2 | 109.1 | 110.9 | 0.7 | 0.101x | 2.182x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 236.6 | 235.3 | 238.6 | 1.2 | 0.217x | 4.684x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 451.8 | 444.5 | 466.9 | 7.7 | 0.415x | 8.944x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 483.1 | 474.1 | 498.5 | 8.8 | 0.444x | 9.564x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,087.9 | 1,084.0 | 1,100.9 | 6.3 | 1.000x | 21.538x |

### `orig` / `s-020` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 87.6 | 87.3 | 87.9 | 0.2 | 0.128x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 136.4 | 136.1 | 137.4 | 0.5 | 0.199x | 1.558x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 136.5 | 136.1 | 137.0 | 0.3 | 0.199x | 1.559x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 136.9 | 136.5 | 138.2 | 0.6 | 0.199x | 1.563x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 136.9 | 136.7 | 146.5 | 3.9 | 0.199x | 1.563x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 287.6 | 286.3 | 290.7 | 1.7 | 0.419x | 3.284x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 333.3 | 318.0 | 351.2 | 11.4 | 0.486x | 3.806x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 683.0 | 681.6 | 698.1 | 6.2 | 0.995x | 7.800x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 686.2 | 685.7 | 689.4 | 1.3 | 1.000x | 7.837x |

### `orig` / `s-020` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 84.6 | 84.0 | 88.3 | 1.8 | 0.123x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 93.5 | 93.2 | 95.1 | 0.7 | 0.136x | 1.105x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 129.1 | 129.0 | 130.3 | 0.5 | 0.188x | 1.525x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 129.3 | 129.2 | 129.6 | 0.2 | 0.188x | 1.528x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 129.3 | 129.0 | 131.3 | 1.0 | 0.188x | 1.528x |
| 6 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 129.5 | 129.4 | 131.3 | 0.7 | 0.188x | 1.530x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 303.1 | 290.1 | 310.5 | 7.2 | 0.441x | 3.581x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 324.7 | 286.3 | 331.9 | 16.8 | 0.472x | 3.837x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 688.1 | 684.6 | 699.7 | 5.3 | 1.000x | 8.130x |

### `orig` / `s-021` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 85.7 | 85.6 | 87.1 | 0.6 | 0.122x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 96.9 | 96.6 | 96.9 | 0.1 | 0.138x | 1.131x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 97.1 | 96.9 | 111.9 | 5.9 | 0.138x | 1.133x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 97.2 | 96.4 | 107.3 | 4.1 | 0.138x | 1.134x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 97.2 | 96.8 | 97.7 | 0.3 | 0.138x | 1.134x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 274.1 | 262.1 | 283.1 | 6.8 | 0.389x | 3.198x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 294.0 | 268.5 | 307.8 | 12.9 | 0.417x | 3.431x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 704.4 | 700.2 | 711.6 | 3.8 | 1.000x | 8.220x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 706.2 | 700.8 | 734.3 | 12.4 | 1.003x | 8.241x |

### `orig` / `s-021` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 62.8 | 62.2 | 64.1 | 0.7 | 0.089x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 89.7 | 89.4 | 90.4 | 0.4 | 0.127x | 1.428x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 89.8 | 89.6 | 90.0 | 0.1 | 0.127x | 1.430x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 89.9 | 89.8 | 90.4 | 0.2 | 0.127x | 1.431x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 90.1 | 90.0 | 91.5 | 0.6 | 0.127x | 1.434x |
| 6 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 90.1 | 89.5 | 90.3 | 0.3 | 0.127x | 1.435x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 279.4 | 275.7 | 288.5 | 4.5 | 0.394x | 4.449x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 286.2 | 261.8 | 307.7 | 15.5 | 0.404x | 4.557x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 708.5 | 703.1 | 739.4 | 13.3 | 1.000x | 11.279x |

### `orig` / `s-022` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 37.8 | 37.6 | 39.7 | 0.8 | 0.084x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 149.9 | 149.8 | 163.8 | 5.5 | 0.334x | 3.967x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 150.3 | 149.9 | 150.6 | 0.2 | 0.335x | 3.977x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 150.4 | 150.0 | 155.6 | 2.1 | 0.335x | 3.980x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 150.5 | 150.2 | 150.7 | 0.2 | 0.335x | 3.984x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 250.3 | 242.6 | 260.3 | 6.2 | 0.558x | 6.624x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 286.9 | 254.5 | 296.4 | 14.4 | 0.639x | 7.592x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 446.4 | 444.3 | 466.4 | 8.2 | 0.994x | 11.815x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 448.9 | 442.9 | 456.2 | 5.3 | 1.000x | 11.881x |

### `orig` / `s-022` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 42.0 | 41.4 | 42.2 | 0.3 | 0.093x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 70.7 | 70.4 | 72.0 | 0.7 | 0.157x | 1.685x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 142.1 | 142.0 | 143.3 | 0.5 | 0.315x | 3.387x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 142.3 | 142.0 | 142.4 | 0.1 | 0.316x | 3.392x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 142.4 | 142.3 | 143.1 | 0.3 | 0.316x | 3.394x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 142.5 | 142.1 | 142.8 | 0.2 | 0.316x | 3.395x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 263.2 | 256.0 | 274.4 | 6.8 | 0.584x | 6.273x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 283.2 | 250.2 | 287.8 | 16.0 | 0.628x | 6.749x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 450.6 | 449.7 | 459.8 | 3.8 | 1.000x | 10.740x |

### `orig` / `s-023` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 86.6 | 86.2 | 90.1 | 1.5 | 0.129x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 123.3 | 123.2 | 124.0 | 0.3 | 0.184x | 1.423x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 123.5 | 123.3 | 125.8 | 0.9 | 0.184x | 1.425x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 124.5 | 123.5 | 132.9 | 3.6 | 0.186x | 1.437x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 124.9 | 123.4 | 128.6 | 1.8 | 0.186x | 1.442x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 281.4 | 268.3 | 288.5 | 6.7 | 0.420x | 3.249x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 293.2 | 267.8 | 296.2 | 10.9 | 0.437x | 3.385x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 670.5 | 665.1 | 679.1 | 4.9 | 1.000x | 7.741x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 672.8 | 663.2 | 684.1 | 7.1 | 1.003x | 7.768x |

### `orig` / `s-023` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 64.6 | 62.5 | 70.0 | 2.8 | 0.096x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 83.1 | 82.9 | 88.4 | 2.1 | 0.123x | 1.286x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 115.4 | 115.0 | 119.5 | 1.7 | 0.172x | 1.787x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 115.5 | 115.4 | 115.6 | 0.1 | 0.172x | 1.788x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 115.7 | 115.0 | 116.3 | 0.5 | 0.172x | 1.791x |
| 6 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 115.8 | 115.4 | 117.1 | 0.6 | 0.172x | 1.792x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 281.9 | 273.3 | 292.4 | 7.1 | 0.419x | 4.362x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 304.3 | 287.9 | 310.1 | 8.2 | 0.452x | 4.709x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 673.1 | 669.2 | 681.8 | 4.3 | 1.000x | 10.417x |

### `orig` / `s-024` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 90.6 | 87.7 | 91.2 | 1.5 | 0.127x | 1.000x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 96.9 | 96.9 | 97.4 | 0.2 | 0.136x | 1.070x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 97.1 | 96.7 | 104.0 | 2.8 | 0.136x | 1.072x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 97.4 | 96.9 | 111.4 | 5.6 | 0.137x | 1.075x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 97.8 | 96.8 | 106.6 | 3.6 | 0.137x | 1.080x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 278.9 | 262.3 | 289.4 | 9.3 | 0.392x | 3.078x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 292.5 | 270.0 | 294.8 | 9.2 | 0.411x | 3.228x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 711.5 | 697.8 | 714.3 | 6.4 | 1.000x | 7.853x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 711.8 | 706.3 | 724.7 | 7.7 | 1.000x | 7.857x |

### `orig` / `s-024` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 87.5 | 87.5 | 90.8 | 1.3 | 0.122x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 89.0 | 88.9 | 89.7 | 0.3 | 0.124x | 1.017x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 90.1 | 89.6 | 90.3 | 0.2 | 0.125x | 1.029x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 90.1 | 89.8 | 92.7 | 1.1 | 0.125x | 1.029x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 90.1 | 89.3 | 94.1 | 1.7 | 0.125x | 1.029x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 90.3 | 89.6 | 93.6 | 1.4 | 0.125x | 1.032x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 306.6 | 295.5 | 323.1 | 10.0 | 0.426x | 3.502x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 313.9 | 264.9 | 325.1 | 21.9 | 0.436x | 3.586x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 720.0 | 707.8 | 724.3 | 5.6 | 1.000x | 8.226x |

### `orig` / `s-025` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 88.4 | 88.2 | 88.6 | 0.1 | 0.120x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 123.4 | 123.2 | 126.5 | 1.2 | 0.168x | 1.397x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 123.5 | 123.3 | 124.0 | 0.3 | 0.168x | 1.397x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 123.7 | 123.3 | 124.9 | 0.6 | 0.169x | 1.400x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 123.8 | 123.4 | 132.9 | 3.7 | 0.169x | 1.400x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 284.0 | 270.3 | 285.5 | 6.0 | 0.387x | 3.213x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 298.1 | 276.3 | 306.6 | 10.4 | 0.406x | 3.373x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 730.0 | 720.4 | 747.6 | 10.6 | 0.995x | 8.260x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 733.7 | 728.8 | 740.7 | 4.1 | 1.000x | 8.302x |

### `orig` / `s-025` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 84.0 | 83.9 | 84.9 | 0.4 | 0.114x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 89.1 | 84.6 | 89.3 | 1.8 | 0.121x | 1.060x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 115.3 | 115.0 | 117.5 | 0.9 | 0.157x | 1.373x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 115.3 | 115.2 | 117.7 | 0.9 | 0.157x | 1.373x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 116.3 | 115.3 | 117.0 | 0.6 | 0.158x | 1.385x |
| 6 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 116.6 | 115.2 | 117.0 | 0.7 | 0.159x | 1.389x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 288.9 | 267.9 | 337.4 | 24.7 | 0.393x | 3.440x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 296.2 | 293.8 | 320.4 | 10.5 | 0.403x | 3.527x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 734.5 | 731.1 | 741.0 | 4.0 | 1.000x | 8.746x |

### `orig` / `s-026` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 38.1 | 37.6 | 38.2 | 0.2 | 0.085x | 1.000x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 150.2 | 149.7 | 150.5 | 0.3 | 0.336x | 3.948x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 150.3 | 149.7 | 152.2 | 0.9 | 0.336x | 3.951x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 150.4 | 149.5 | 155.8 | 2.3 | 0.337x | 3.952x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 150.7 | 150.1 | 154.7 | 1.7 | 0.337x | 3.959x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 253.7 | 236.2 | 259.7 | 8.3 | 0.568x | 6.667x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 282.9 | 254.2 | 287.4 | 11.9 | 0.633x | 7.434x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 446.9 | 444.7 | 453.1 | 2.9 | 1.000x | 11.743x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 453.8 | 448.4 | 461.3 | 4.4 | 1.015x | 11.924x |

### `orig` / `s-026` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 41.7 | 40.7 | 41.9 | 0.4 | 0.092x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 70.3 | 70.3 | 71.7 | 0.6 | 0.156x | 1.685x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 142.9 | 142.2 | 159.0 | 6.5 | 0.317x | 3.424x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 143.1 | 141.9 | 147.4 | 1.9 | 0.317x | 3.429x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 143.1 | 142.6 | 143.7 | 0.4 | 0.317x | 3.429x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 143.8 | 142.7 | 144.1 | 0.5 | 0.319x | 3.447x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 272.3 | 253.4 | 279.8 | 10.0 | 0.604x | 6.525x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 290.2 | 257.3 | 299.4 | 14.8 | 0.643x | 6.954x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 451.1 | 447.6 | 457.2 | 3.2 | 1.000x | 10.811x |

### `orig` / `s-027` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 86.7 | 86.5 | 96.9 | 4.1 | 0.138x | 1.000x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 150.2 | 150.0 | 150.4 | 0.2 | 0.239x | 1.733x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 150.3 | 150.1 | 153.2 | 1.2 | 0.239x | 1.734x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 150.3 | 149.8 | 159.5 | 3.7 | 0.239x | 1.734x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 150.4 | 150.1 | 150.6 | 0.2 | 0.239x | 1.735x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 273.5 | 267.8 | 292.8 | 8.7 | 0.435x | 3.156x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 295.7 | 272.9 | 311.4 | 12.4 | 0.470x | 3.411x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 629.5 | 625.9 | 638.2 | 4.2 | 1.000x | 7.263x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 634.3 | 630.1 | 648.7 | 6.4 | 1.008x | 7.318x |

### `orig` / `s-027` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 62.9 | 62.8 | 63.2 | 0.1 | 0.099x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 81.5 | 81.4 | 82.0 | 0.2 | 0.129x | 1.294x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 142.4 | 142.2 | 144.1 | 0.7 | 0.225x | 2.262x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 142.5 | 142.5 | 149.6 | 2.8 | 0.225x | 2.265x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 142.6 | 142.0 | 143.0 | 0.4 | 0.225x | 2.266x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 143.4 | 142.2 | 144.6 | 0.9 | 0.226x | 2.279x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 277.8 | 271.8 | 297.5 | 9.3 | 0.438x | 4.414x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 283.6 | 272.4 | 305.9 | 12.1 | 0.447x | 4.505x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 633.8 | 631.9 | 639.2 | 2.5 | 1.000x | 10.069x |

### `orig` / `s-028` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 34.8 | 34.8 | 35.5 | 0.3 | 0.117x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 43.7 | 43.7 | 44.2 | 0.2 | 0.148x | 1.257x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 43.8 | 43.7 | 44.3 | 0.2 | 0.148x | 1.259x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 43.9 | 43.7 | 44.3 | 0.2 | 0.148x | 1.262x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 44.0 | 43.7 | 48.5 | 1.8 | 0.148x | 1.264x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 250.1 | 247.6 | 254.3 | 2.2 | 0.844x | 7.192x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 287.6 | 262.7 | 295.1 | 11.0 | 0.970x | 8.268x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 296.4 | 294.9 | 301.0 | 2.2 | 1.000x | 8.521x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 298.0 | 289.7 | 309.9 | 6.5 | 1.005x | 8.568x |

### `orig` / `s-028` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 37.7 | 37.7 | 38.5 | 0.3 | 0.035x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 37.8 | 37.5 | 37.8 | 0.1 | 0.035x | 1.002x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 37.8 | 37.7 | 38.1 | 0.1 | 0.035x | 1.002x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 38.0 | 37.8 | 39.6 | 0.7 | 0.035x | 1.006x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.0 | 67.5 | 68.8 | 0.5 | 0.063x | 1.801x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 255.6 | 253.2 | 257.8 | 1.7 | 0.237x | 6.774x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 483.4 | 457.8 | 508.2 | 16.1 | 0.448x | 12.809x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 503.9 | 490.8 | 526.6 | 12.2 | 0.466x | 13.351x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,080.1 | 1,066.1 | 1,089.3 | 8.3 | 1.000x | 28.621x |

### `orig` / `s-029` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 35.0 | 35.0 | 35.1 | 0.1 | 0.118x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 89.5 | 89.1 | 89.5 | 0.2 | 0.302x | 2.555x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 89.6 | 89.2 | 94.0 | 1.8 | 0.302x | 2.557x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 89.7 | 89.4 | 89.9 | 0.2 | 0.302x | 2.560x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 89.7 | 89.3 | 90.3 | 0.4 | 0.302x | 2.562x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 252.3 | 246.0 | 253.2 | 2.7 | 0.850x | 7.205x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 283.5 | 254.2 | 294.7 | 13.9 | 0.956x | 8.095x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 296.7 | 294.4 | 307.1 | 4.7 | 1.000x | 8.472x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 298.3 | 289.8 | 309.8 | 7.2 | 1.005x | 8.517x |

### `orig` / `s-029` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 69.9 | 69.3 | 71.1 | 0.7 | 0.065x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 83.1 | 82.9 | 83.2 | 0.1 | 0.077x | 1.189x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 83.2 | 83.0 | 83.4 | 0.1 | 0.077x | 1.191x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 83.3 | 83.2 | 84.2 | 0.4 | 0.077x | 1.193x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 83.4 | 83.1 | 83.5 | 0.1 | 0.077x | 1.193x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 534.0 | 530.3 | 548.8 | 7.0 | 0.493x | 7.642x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 760.1 | 724.7 | 767.9 | 15.3 | 0.702x | 10.878x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 847.1 | 838.8 | 955.4 | 44.4 | 0.782x | 12.123x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,083.2 | 1,067.7 | 1,088.3 | 7.4 | 1.000x | 15.503x |

### `orig` / `s-030` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 34.8 | 34.6 | 35.1 | 0.2 | 0.118x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 43.5 | 43.4 | 43.9 | 0.2 | 0.147x | 1.251x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 43.8 | 43.6 | 44.0 | 0.1 | 0.148x | 1.257x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 43.8 | 43.5 | 44.1 | 0.2 | 0.148x | 1.259x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 44.0 | 43.4 | 48.1 | 1.7 | 0.149x | 1.266x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 250.6 | 245.5 | 257.7 | 4.2 | 0.849x | 7.203x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 286.8 | 257.5 | 294.0 | 12.9 | 0.972x | 8.243x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 295.1 | 292.8 | 302.0 | 3.1 | 1.000x | 8.482x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 295.9 | 291.8 | 311.8 | 7.3 | 1.003x | 8.505x |

### `orig` / `s-030` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 37.3 | 37.3 | 37.5 | 0.1 | 0.034x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 37.5 | 37.3 | 37.9 | 0.2 | 0.035x | 1.004x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 37.5 | 37.4 | 37.6 | 0.1 | 0.035x | 1.006x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 37.6 | 37.6 | 37.7 | 0.1 | 0.035x | 1.009x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 67.6 | 67.4 | 69.1 | 0.6 | 0.062x | 1.812x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 263.6 | 255.6 | 269.9 | 5.4 | 0.244x | 7.063x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 475.0 | 458.7 | 491.9 | 11.3 | 0.439x | 12.728x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 526.2 | 521.4 | 550.1 | 11.0 | 0.486x | 14.101x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,082.4 | 1,066.0 | 1,083.6 | 6.7 | 1.000x | 29.002x |

### `orig` / `s-031` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 35.0 | 34.8 | 35.1 | 0.1 | 0.119x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 59.9 | 59.6 | 64.8 | 2.0 | 0.204x | 1.714x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 59.9 | 59.9 | 60.0 | 0.0 | 0.204x | 1.714x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 60.0 | 59.5 | 60.3 | 0.2 | 0.204x | 1.716x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 60.1 | 59.9 | 60.2 | 0.1 | 0.204x | 1.718x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 251.7 | 243.7 | 257.7 | 4.9 | 0.857x | 7.197x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 286.4 | 256.7 | 291.3 | 12.7 | 0.975x | 8.189x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 293.9 | 293.1 | 301.3 | 3.0 | 1.000x | 8.403x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 296.6 | 290.7 | 321.9 | 11.4 | 1.009x | 8.481x |

### `orig` / `s-031` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 53.4 | 53.2 | 53.7 | 0.2 | 0.050x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 53.6 | 53.2 | 53.9 | 0.3 | 0.050x | 1.003x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 53.8 | 53.6 | 54.3 | 0.2 | 0.050x | 1.006x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 53.8 | 53.6 | 54.0 | 0.1 | 0.050x | 1.007x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 69.9 | 69.0 | 70.1 | 0.4 | 0.065x | 1.307x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 328.7 | 327.7 | 329.9 | 0.8 | 0.305x | 6.151x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 550.3 | 531.3 | 571.4 | 14.6 | 0.510x | 10.298x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 608.0 | 589.8 | 632.5 | 17.4 | 0.564x | 11.376x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,078.7 | 1,077.5 | 1,087.7 | 3.8 | 1.000x | 20.185x |

### `orig` / `s-032` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 48.7 | 47.0 | 51.5 | 1.8 | 0.138x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 50.6 | 50.2 | 50.7 | 0.2 | 0.143x | 1.038x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 50.6 | 50.5 | 50.6 | 0.1 | 0.143x | 1.038x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 50.6 | 49.9 | 54.7 | 1.7 | 0.143x | 1.039x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 50.7 | 50.4 | 51.1 | 0.3 | 0.144x | 1.040x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 263.2 | 259.9 | 270.9 | 4.3 | 0.746x | 5.401x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 283.1 | 258.2 | 294.1 | 12.4 | 0.802x | 5.809x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 352.9 | 351.9 | 358.8 | 3.1 | 1.000x | 7.242x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 356.0 | 353.6 | 395.8 | 16.0 | 1.009x | 7.304x |

### `orig` / `s-032` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 43.9 | 43.7 | 45.2 | 0.6 | 0.033x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 44.0 | 43.7 | 44.3 | 0.2 | 0.033x | 1.001x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 44.1 | 44.0 | 44.2 | 0.1 | 0.033x | 1.004x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 44.2 | 44.1 | 44.7 | 0.2 | 0.034x | 1.005x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 71.9 | 70.8 | 73.0 | 0.9 | 0.055x | 1.637x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 387.9 | 380.5 | 394.2 | 4.8 | 0.294x | 8.830x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 612.3 | 586.6 | 617.3 | 11.4 | 0.465x | 13.939x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 620.3 | 607.5 | 632.2 | 8.7 | 0.471x | 14.120x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,317.6 | 1,314.7 | 1,330.2 | 5.4 | 1.000x | 29.994x |

### `orig` / `s-033` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 44.0 | 43.7 | 48.4 | 1.8 | 0.141x | 1.000x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 50.4 | 50.1 | 51.0 | 0.3 | 0.162x | 1.145x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 50.4 | 50.0 | 51.5 | 0.5 | 0.162x | 1.146x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 50.6 | 49.8 | 54.3 | 1.6 | 0.162x | 1.149x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 50.7 | 50.3 | 54.7 | 1.7 | 0.163x | 1.152x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 261.2 | 251.1 | 268.8 | 6.1 | 0.838x | 5.934x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 288.5 | 255.6 | 302.2 | 16.0 | 0.925x | 6.554x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 311.7 | 308.8 | 316.6 | 2.8 | 1.000x | 7.083x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 313.3 | 309.2 | 354.4 | 17.0 | 1.005x | 7.118x |

### `orig` / `s-033` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 43.7 | 43.7 | 44.4 | 0.3 | 0.038x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 43.9 | 43.9 | 44.2 | 0.1 | 0.038x | 1.005x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 44.0 | 43.9 | 44.2 | 0.1 | 0.038x | 1.007x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 44.0 | 44.0 | 44.3 | 0.1 | 0.038x | 1.008x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 69.9 | 69.5 | 71.9 | 0.9 | 0.061x | 1.601x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 363.2 | 359.8 | 364.3 | 1.7 | 0.316x | 8.314x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 584.1 | 559.1 | 595.3 | 13.7 | 0.508x | 13.370x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 602.4 | 575.9 | 624.2 | 15.9 | 0.523x | 13.790x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,150.8 | 1,137.5 | 1,155.1 | 6.9 | 1.000x | 26.342x |

### `orig` / `s-034` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 26.0 | 26.6 | 0.2 | 0.045x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 36.8 | 36.5 | 39.9 | 1.3 | 0.064x | 1.410x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 36.8 | 36.7 | 37.3 | 0.2 | 0.064x | 1.411x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 37.0 | 36.7 | 37.0 | 0.1 | 0.064x | 1.416x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.1 | 36.8 | 37.6 | 0.3 | 0.064x | 1.420x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 246.8 | 237.7 | 251.2 | 5.1 | 0.428x | 9.452x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 285.3 | 259.0 | 295.8 | 12.9 | 0.494x | 10.926x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 577.2 | 570.2 | 588.0 | 5.8 | 1.000x | 22.104x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 577.2 | 575.7 | 618.7 | 16.8 | 1.000x | 22.105x |

### `orig` / `s-034` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 30.9 | 30.9 | 31.4 | 0.2 | 0.014x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 31.2 | 31.1 | 31.4 | 0.1 | 0.014x | 1.008x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 31.3 | 31.2 | 31.4 | 0.1 | 0.014x | 1.011x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 31.7 | 31.0 | 32.0 | 0.4 | 0.014x | 1.025x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 97.5 | 97.2 | 98.8 | 0.6 | 0.044x | 3.153x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 177.2 | 173.5 | 182.1 | 2.9 | 0.080x | 5.731x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 401.6 | 381.9 | 416.5 | 11.6 | 0.182x | 12.992x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 425.2 | 383.3 | 431.7 | 18.1 | 0.193x | 13.755x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,203.8 | 2,183.4 | 2,223.3 | 14.5 | 1.000x | 71.286x |

### `orig` / `s-035` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 50.2 | 49.9 | 50.5 | 0.2 | 0.063x | 1.000x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 50.4 | 50.3 | 50.7 | 0.1 | 0.063x | 1.004x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 50.4 | 50.2 | 59.0 | 3.4 | 0.063x | 1.004x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 50.5 | 50.2 | 50.6 | 0.2 | 0.063x | 1.007x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 116.5 | 116.3 | 117.0 | 0.3 | 0.146x | 2.320x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 318.9 | 317.5 | 339.0 | 8.7 | 0.400x | 6.354x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 356.4 | 322.0 | 382.4 | 21.6 | 0.447x | 7.100x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 794.0 | 783.9 | 841.6 | 20.5 | 0.996x | 15.819x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 797.1 | 781.9 | 801.7 | 7.7 | 1.000x | 15.881x |

### `orig` / `s-035` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 43.9 | 43.7 | 45.8 | 0.8 | 0.015x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 44.0 | 43.3 | 45.2 | 0.6 | 0.015x | 1.002x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 44.0 | 44.0 | 44.3 | 0.1 | 0.015x | 1.004x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 44.1 | 44.0 | 44.2 | 0.1 | 0.015x | 1.004x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 133.2 | 131.3 | 133.6 | 0.9 | 0.044x | 3.036x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 700.3 | 697.1 | 702.0 | 1.6 | 0.232x | 15.966x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 911.3 | 895.7 | 921.0 | 8.8 | 0.302x | 20.775x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 920.7 | 895.3 | 945.9 | 21.0 | 0.305x | 20.989x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,015.3 | 2,992.6 | 3,100.2 | 37.3 | 1.000x | 68.741x |

### `orig` / `s-036` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 26.0 | 26.7 | 0.3 | 0.125x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 53.1 | 53.0 | 53.4 | 0.2 | 0.255x | 2.031x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 53.1 | 52.7 | 61.0 | 3.2 | 0.255x | 2.031x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 53.2 | 53.0 | 54.4 | 0.5 | 0.255x | 2.037x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 53.3 | 53.1 | 53.6 | 0.2 | 0.256x | 2.040x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 205.8 | 203.1 | 221.7 | 6.9 | 0.987x | 7.876x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 208.5 | 204.7 | 214.2 | 3.2 | 1.000x | 7.978x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 248.7 | 235.1 | 256.0 | 7.8 | 1.193x | 9.517x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 286.3 | 257.3 | 291.7 | 12.3 | 1.373x | 10.957x |

### `orig` / `s-036` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 47.3 | 47.3 | 48.6 | 0.5 | 0.064x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 47.6 | 47.3 | 48.2 | 0.3 | 0.064x | 1.006x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 47.7 | 47.6 | 48.0 | 0.1 | 0.065x | 1.009x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 47.8 | 47.7 | 48.5 | 0.3 | 0.065x | 1.010x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 65.8 | 64.2 | 68.7 | 1.6 | 0.089x | 1.391x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 239.5 | 237.8 | 240.8 | 1.0 | 0.324x | 5.060x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 444.2 | 439.9 | 469.2 | 11.2 | 0.601x | 9.385x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 475.1 | 453.5 | 498.2 | 16.4 | 0.643x | 10.040x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 738.7 | 716.4 | 747.1 | 10.8 | 1.000x | 15.609x |

### `orig` / `s-037` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 39.7 | 39.6 | 41.0 | 0.5 | 0.118x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 40.1 | 39.9 | 40.7 | 0.4 | 0.119x | 1.008x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 40.4 | 40.3 | 40.8 | 0.2 | 0.120x | 1.016x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 40.5 | 40.3 | 40.8 | 0.2 | 0.120x | 1.019x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 40.7 | 40.4 | 48.0 | 2.9 | 0.121x | 1.025x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 254.6 | 249.2 | 271.7 | 8.7 | 0.753x | 6.407x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 280.4 | 240.7 | 300.4 | 20.5 | 0.830x | 7.057x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 334.9 | 334.3 | 364.7 | 11.8 | 0.991x | 8.428x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 337.9 | 333.7 | 338.4 | 1.7 | 1.000x | 8.503x |

### `orig` / `s-037` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 34.6 | 34.5 | 34.9 | 0.2 | 0.028x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 34.7 | 34.6 | 34.9 | 0.1 | 0.029x | 1.005x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 34.9 | 34.7 | 35.4 | 0.2 | 0.029x | 1.010x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 35.0 | 34.8 | 35.0 | 0.1 | 0.029x | 1.012x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.3 | 67.3 | 72.4 | 1.9 | 0.056x | 1.978x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 294.0 | 293.2 | 298.6 | 2.0 | 0.242x | 8.510x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 502.1 | 501.0 | 531.2 | 11.4 | 0.413x | 14.532x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 529.9 | 526.0 | 559.9 | 12.6 | 0.436x | 15.337x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,214.6 | 1,213.2 | 1,226.7 | 5.0 | 1.000x | 35.152x |

### `orig` / `s-038` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 53.1 | 53.0 | 55.3 | 0.9 | 0.109x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 53.2 | 52.4 | 53.4 | 0.3 | 0.109x | 1.001x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 53.3 | 52.9 | 62.1 | 3.6 | 0.109x | 1.003x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 53.4 | 53.0 | 53.8 | 0.3 | 0.109x | 1.006x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 74.2 | 73.8 | 74.4 | 0.2 | 0.152x | 1.398x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 297.1 | 288.1 | 301.4 | 5.1 | 0.609x | 5.594x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 307.6 | 275.6 | 320.7 | 15.5 | 0.630x | 5.790x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 487.9 | 483.4 | 492.3 | 3.6 | 1.000x | 9.186x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 491.1 | 482.2 | 525.3 | 15.0 | 1.007x | 9.246x |

### `orig` / `s-038` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 47.5 | 47.3 | 51.0 | 1.4 | 0.026x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 47.6 | 47.4 | 48.4 | 0.4 | 0.026x | 1.002x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 47.8 | 47.7 | 47.9 | 0.1 | 0.026x | 1.005x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 47.9 | 47.7 | 48.1 | 0.2 | 0.026x | 1.008x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 95.2 | 91.4 | 96.0 | 1.8 | 0.052x | 2.004x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 590.4 | 575.6 | 602.1 | 8.9 | 0.325x | 12.421x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 685.6 | 660.8 | 726.2 | 21.7 | 0.377x | 14.422x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 814.1 | 787.5 | 828.0 | 14.2 | 0.448x | 17.125x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,817.5 | 1,808.8 | 1,863.7 | 19.5 | 1.000x | 38.235x |

### `orig` / `s-039` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 26.0 | 28.1 | 0.8 | 0.128x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 110.5 | 110.4 | 121.6 | 4.4 | 0.540x | 4.234x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 110.6 | 110.4 | 110.7 | 0.1 | 0.541x | 4.237x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 110.7 | 110.6 | 111.1 | 0.2 | 0.541x | 4.241x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 110.9 | 110.6 | 119.6 | 3.5 | 0.542x | 4.250x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 204.6 | 201.0 | 212.0 | 3.8 | 1.000x | 7.839x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 205.2 | 198.5 | 211.2 | 4.5 | 1.003x | 7.861x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 253.8 | 247.8 | 271.2 | 8.0 | 1.241x | 9.724x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 291.8 | 255.0 | 298.5 | 15.8 | 1.426x | 11.178x |

### `orig` / `s-039` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 105.4 | 105.1 | 106.1 | 0.4 | 0.112x | 1.000x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 105.6 | 105.4 | 105.9 | 0.2 | 0.112x | 1.002x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 105.7 | 105.6 | 106.0 | 0.2 | 0.112x | 1.003x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 105.7 | 104.9 | 109.5 | 1.6 | 0.112x | 1.003x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 105.9 | 105.2 | 111.0 | 2.2 | 0.112x | 1.004x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 109.3 | 105.5 | 110.1 | 1.7 | 0.116x | 1.037x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 334.7 | 325.4 | 350.9 | 10.0 | 0.354x | 3.174x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 351.5 | 330.7 | 374.7 | 15.3 | 0.372x | 3.334x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 944.5 | 934.0 | 953.7 | 7.3 | 1.000x | 8.958x |

### `orig` / `s-040` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 25.2 | 25.2 | 25.3 | 0.0 | 0.736x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 34.3 | 33.7 | 40.9 | 2.8 | 0.999x | 1.359x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 34.3 | 34.2 | 35.1 | 0.3 | 1.000x | 1.359x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 46.8 | 46.4 | 46.9 | 0.2 | 1.363x | 1.852x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 46.8 | 46.7 | 47.0 | 0.1 | 1.365x | 1.856x |
| 6 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 46.8 | 46.6 | 47.3 | 0.3 | 1.365x | 1.856x |
| 7 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 46.9 | 46.7 | 47.2 | 0.2 | 1.368x | 1.859x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 241.6 | 228.7 | 254.6 | 10.4 | 7.042x | 9.572x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 244.9 | 230.2 | 263.9 | 12.2 | 7.138x | 9.703x |

### `orig` / `s-040` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 35.0 | 34.8 | 35.3 | 0.2 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 39.3 | 36.7 | 41.6 | 1.6 | 1.121x | 1.121x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 40.3 | 40.1 | 40.7 | 0.2 | 1.151x | 1.151x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 40.4 | 40.0 | 43.0 | 1.1 | 1.154x | 1.154x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 40.8 | 40.7 | 41.3 | 0.2 | 1.166x | 1.166x |
| 6 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 41.0 | 40.8 | 41.8 | 0.4 | 1.171x | 1.171x |
| 7 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 200.5 | 199.3 | 200.8 | 0.5 | 5.722x | 5.722x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 411.8 | 409.0 | 438.4 | 11.2 | 11.755x | 11.755x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 457.2 | 442.8 | 481.3 | 13.3 | 13.050x | 13.050x |

### `orig` / `s-041` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 16.5 | 16.3 | 18.7 | 0.9 | 0.565x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.2 | 28.9 | 29.7 | 0.3 | 1.000x | 1.769x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.3 | 29.2 | 29.7 | 0.2 | 1.005x | 1.777x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.2 | 33.7 | 34.7 | 0.4 | 1.173x | 2.076x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 34.3 | 33.5 | 34.5 | 0.4 | 1.175x | 2.078x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 34.3 | 33.9 | 35.1 | 0.4 | 1.176x | 2.081x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.5 | 34.2 | 39.2 | 1.9 | 1.185x | 2.095x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 253.3 | 237.1 | 269.9 | 11.1 | 8.689x | 15.368x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 261.3 | 246.8 | 263.0 | 7.3 | 8.962x | 15.852x |

### `orig` / `s-041` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 29.2 | 29.2 | 29.5 | 0.1 | 0.807x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 29.4 | 29.3 | 30.2 | 0.3 | 0.812x | 1.007x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 29.7 | 29.5 | 30.1 | 0.2 | 0.820x | 1.016x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 29.7 | 29.5 | 29.8 | 0.1 | 0.821x | 1.017x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 36.2 | 35.7 | 36.6 | 0.4 | 1.000x | 1.240x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 40.3 | 37.2 | 43.0 | 1.8 | 1.113x | 1.380x |
| 7 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 144.1 | 143.2 | 144.9 | 0.6 | 3.982x | 4.936x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 357.9 | 344.4 | 373.4 | 9.6 | 9.891x | 12.260x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 370.8 | 358.4 | 446.5 | 31.7 | 10.247x | 12.702x |

### `orig` / `s-042` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 17.3 | 17.3 | 17.5 | 0.1 | 0.084x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 17.4 | 17.3 | 18.9 | 0.6 | 0.085x | 1.005x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 17.7 | 17.5 | 18.2 | 0.2 | 0.086x | 1.018x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 17.8 | 17.6 | 17.8 | 0.1 | 0.086x | 1.024x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 18.7 | 18.7 | 19.2 | 0.2 | 0.091x | 1.079x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 205.3 | 204.4 | 211.3 | 2.6 | 1.000x | 11.836x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 207.4 | 206.8 | 213.5 | 2.5 | 1.010x | 11.955x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 249.2 | 215.6 | 268.9 | 17.5 | 1.214x | 14.363x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 264.2 | 240.2 | 277.2 | 13.6 | 1.287x | 15.229x |

### `orig` / `s-042` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 12.6 | 12.5 | 12.7 | 0.1 | 0.058x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 12.7 | 12.6 | 12.7 | 0.0 | 0.059x | 1.003x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 12.7 | 12.6 | 13.0 | 0.1 | 0.059x | 1.005x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 12.7 | 12.6 | 14.9 | 0.9 | 0.059x | 1.007x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 52.8 | 51.9 | 54.9 | 1.2 | 0.245x | 4.186x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 64.3 | 63.6 | 64.7 | 0.4 | 0.298x | 5.092x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 215.9 | 215.0 | 219.4 | 1.5 | 1.000x | 17.096x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 279.6 | 273.8 | 291.2 | 7.6 | 1.296x | 22.148x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 312.8 | 289.0 | 334.9 | 16.3 | 1.449x | 24.771x |

### `orig` / `s-043` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 23.5 | 23.4 | 24.7 | 0.6 | 0.155x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 130.2 | 130.1 | 130.5 | 0.2 | 0.855x | 5.530x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 130.2 | 130.0 | 138.9 | 3.5 | 0.855x | 5.532x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 130.3 | 130.0 | 130.6 | 0.2 | 0.855x | 5.534x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 130.4 | 130.1 | 130.7 | 0.2 | 0.856x | 5.538x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 152.4 | 151.0 | 156.0 | 1.8 | 1.000x | 6.472x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 153.0 | 152.3 | 162.1 | 3.7 | 1.004x | 6.498x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 238.7 | 235.8 | 250.7 | 5.5 | 1.567x | 10.139x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 264.7 | 253.3 | 270.5 | 6.2 | 1.737x | 11.243x |

### `orig` / `s-043` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 101.9 | 98.9 | 103.8 | 1.7 | 0.095x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 124.3 | 124.0 | 124.4 | 0.2 | 0.116x | 1.220x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 124.5 | 124.3 | 125.4 | 0.4 | 0.116x | 1.222x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 124.9 | 124.7 | 125.4 | 0.3 | 0.117x | 1.225x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 125.1 | 124.7 | 146.6 | 8.6 | 0.117x | 1.228x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 150.7 | 147.5 | 151.6 | 1.7 | 0.141x | 1.479x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 369.0 | 351.6 | 393.5 | 13.7 | 0.345x | 3.621x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 369.9 | 352.9 | 378.6 | 9.2 | 0.346x | 3.630x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,070.1 | 1,064.8 | 1,079.5 | 5.7 | 1.000x | 10.501x |

### `orig` / `s-044` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 16.4 | 16.3 | 18.4 | 0.8 | 0.560x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.2 | 28.9 | 29.4 | 0.2 | 1.000x | 1.784x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.5 | 29.2 | 29.7 | 0.2 | 1.009x | 1.800x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 111.9 | 111.1 | 112.2 | 0.4 | 3.829x | 6.833x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 112.0 | 111.6 | 112.8 | 0.4 | 3.833x | 6.839x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 112.2 | 111.4 | 120.4 | 3.4 | 3.838x | 6.848x |
| 7 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 112.4 | 111.6 | 113.1 | 0.5 | 3.846x | 6.862x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 255.2 | 226.4 | 265.4 | 13.5 | 8.729x | 15.576x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 256.3 | 241.4 | 285.9 | 14.6 | 8.766x | 15.641x |

### `orig` / `s-044` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 73.0 | 71.6 | 75.9 | 1.5 | 0.134x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 79.3 | 77.4 | 83.3 | 2.1 | 0.145x | 1.086x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 107.2 | 106.7 | 110.9 | 1.5 | 0.196x | 1.469x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 107.3 | 106.9 | 107.7 | 0.3 | 0.197x | 1.470x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 107.5 | 107.4 | 107.6 | 0.1 | 0.197x | 1.474x |
| 6 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 107.6 | 107.2 | 107.8 | 0.2 | 0.197x | 1.474x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 286.0 | 283.1 | 310.0 | 9.8 | 0.524x | 3.920x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 298.4 | 269.2 | 309.6 | 13.4 | 0.547x | 4.090x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 545.7 | 539.6 | 549.1 | 3.2 | 1.000x | 7.479x |

### `orig` / `s-045` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 23.5 | 23.3 | 25.0 | 0.6 | 0.154x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 49.7 | 49.6 | 50.2 | 0.2 | 0.325x | 2.109x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 49.8 | 49.7 | 50.6 | 0.3 | 0.325x | 2.113x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 49.8 | 49.7 | 51.2 | 0.6 | 0.326x | 2.115x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 50.0 | 49.9 | 50.1 | 0.1 | 0.327x | 2.124x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 151.7 | 151.5 | 159.9 | 3.3 | 0.992x | 6.444x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 152.9 | 148.8 | 161.9 | 4.4 | 1.000x | 6.495x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 242.1 | 232.1 | 249.7 | 6.0 | 1.583x | 10.284x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 265.5 | 252.3 | 278.9 | 9.9 | 1.736x | 11.277x |

### `orig` / `s-045` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 43.9 | 43.7 | 45.0 | 0.4 | 0.087x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 44.0 | 43.9 | 45.3 | 0.5 | 0.087x | 1.003x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 44.2 | 44.0 | 44.2 | 0.1 | 0.088x | 1.006x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 44.3 | 44.1 | 44.6 | 0.2 | 0.088x | 1.008x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 65.1 | 62.7 | 65.5 | 1.3 | 0.129x | 1.483x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 225.5 | 224.9 | 226.9 | 0.8 | 0.447x | 5.136x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 424.9 | 420.4 | 448.7 | 10.4 | 0.843x | 9.677x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 467.0 | 435.7 | 472.2 | 13.2 | 0.926x | 10.637x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 504.1 | 497.1 | 507.6 | 3.5 | 1.000x | 11.482x |

### `orig` / `s-046` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 36.5 | 36.3 | 36.7 | 0.1 | 0.077x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 36.6 | 36.2 | 38.9 | 1.0 | 0.077x | 1.002x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 36.8 | 36.6 | 37.1 | 0.2 | 0.078x | 1.007x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 36.9 | 36.7 | 37.3 | 0.2 | 0.078x | 1.010x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 52.2 | 51.9 | 52.5 | 0.2 | 0.110x | 1.427x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 270.8 | 258.1 | 280.6 | 8.0 | 0.572x | 7.411x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 292.4 | 257.5 | 298.7 | 14.9 | 0.618x | 8.002x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 471.8 | 462.6 | 489.5 | 9.2 | 0.997x | 12.912x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 473.0 | 469.0 | 477.5 | 3.3 | 1.000x | 12.945x |

### `orig` / `s-046` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 31.1 | 31.0 | 31.7 | 0.3 | 0.018x | 1.000x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 31.1 | 31.0 | 31.3 | 0.1 | 0.018x | 1.002x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 31.1 | 30.9 | 31.4 | 0.2 | 0.018x | 1.002x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 31.2 | 31.1 | 31.3 | 0.0 | 0.018x | 1.003x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 88.5 | 84.8 | 91.6 | 2.6 | 0.051x | 2.848x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 348.1 | 347.1 | 349.7 | 0.8 | 0.199x | 11.204x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 545.0 | 523.4 | 549.8 | 9.5 | 0.312x | 17.542x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 570.1 | 543.7 | 582.1 | 13.6 | 0.326x | 18.348x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,748.1 | 1,734.5 | 1,767.2 | 10.7 | 1.000x | 56.262x |

### `orig` / `s-047` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.0 | 26.0 | 26.2 | 0.1 | 0.033x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 39.8 | 39.7 | 40.3 | 0.2 | 0.050x | 1.530x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 40.0 | 39.9 | 40.1 | 0.1 | 0.051x | 1.537x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 40.1 | 39.9 | 40.9 | 0.3 | 0.051x | 1.541x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 40.6 | 39.6 | 45.9 | 2.3 | 0.051x | 1.559x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 242.6 | 233.3 | 258.5 | 8.5 | 0.307x | 9.318x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 285.4 | 256.3 | 291.7 | 12.6 | 0.361x | 10.963x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 785.1 | 779.1 | 841.1 | 22.8 | 0.993x | 30.158x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 790.4 | 789.2 | 795.3 | 2.1 | 1.000x | 30.360x |

### `orig` / `s-047` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 34.4 | 34.3 | 34.6 | 0.1 | 0.011x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 34.4 | 34.3 | 34.8 | 0.2 | 0.011x | 1.001x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 34.4 | 34.4 | 34.5 | 0.1 | 0.011x | 1.003x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 34.5 | 34.3 | 35.2 | 0.3 | 0.011x | 1.005x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 120.4 | 118.3 | 120.6 | 0.9 | 0.040x | 3.505x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 185.1 | 183.0 | 187.5 | 1.5 | 0.061x | 5.389x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 411.5 | 385.9 | 414.6 | 12.5 | 0.135x | 11.980x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 414.7 | 400.7 | 418.1 | 6.3 | 0.137x | 12.073x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,037.8 | 3,027.0 | 3,048.0 | 6.8 | 1.000x | 88.433x |

### `orig` / `s-048` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 18.8 | 18.6 | 18.9 | 0.1 | 0.064x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 22.2 | 22.1 | 22.4 | 0.1 | 0.075x | 1.180x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 22.3 | 22.3 | 24.2 | 0.8 | 0.076x | 1.186x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 22.5 | 22.3 | 22.5 | 0.1 | 0.076x | 1.193x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 22.5 | 22.2 | 22.6 | 0.1 | 0.076x | 1.194x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 244.1 | 222.3 | 259.1 | 13.3 | 0.830x | 12.967x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 272.5 | 236.7 | 284.6 | 16.7 | 0.926x | 14.471x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 294.2 | 290.5 | 296.5 | 2.0 | 1.000x | 15.629x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 296.1 | 292.6 | 313.6 | 7.5 | 1.006x | 15.726x |

### `orig` / `s-048` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.8 | 0.3 | 0.022x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 18.1 | 17.9 | 18.7 | 0.3 | 0.022x | 1.008x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.5 | 0.1 | 0.023x | 1.018x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 18.3 | 18.2 | 18.4 | 0.1 | 0.023x | 1.021x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 62.2 | 60.5 | 64.0 | 1.3 | 0.077x | 3.469x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 90.3 | 89.4 | 94.2 | 1.6 | 0.112x | 5.036x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 321.2 | 257.1 | 343.9 | 30.7 | 0.397x | 17.905x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 322.3 | 286.3 | 336.8 | 16.9 | 0.398x | 17.966x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 809.1 | 804.9 | 815.7 | 4.1 | 1.000x | 45.098x |

### `orig` / `s-049` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 22.3 | 22.1 | 22.5 | 0.1 | 0.157x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 126.6 | 126.5 | 127.1 | 0.2 | 0.891x | 5.682x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 127.0 | 126.4 | 135.9 | 3.6 | 0.894x | 5.699x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 127.0 | 126.9 | 127.2 | 0.1 | 0.894x | 5.700x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 127.0 | 126.7 | 127.1 | 0.2 | 0.894x | 5.700x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 142.1 | 141.6 | 146.3 | 1.9 | 1.000x | 6.378x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 143.0 | 141.2 | 161.5 | 7.5 | 1.007x | 6.420x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 242.4 | 231.9 | 255.3 | 8.6 | 1.706x | 10.881x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 273.4 | 254.4 | 280.0 | 8.7 | 1.924x | 12.272x |

### `orig` / `s-049` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 98.8 | 97.1 | 104.2 | 2.5 | 0.096x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 121.2 | 120.8 | 125.5 | 1.8 | 0.118x | 1.227x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 121.5 | 121.0 | 122.1 | 0.4 | 0.118x | 1.230x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 121.7 | 121.5 | 121.8 | 0.1 | 0.118x | 1.232x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 121.8 | 121.6 | 123.9 | 0.8 | 0.118x | 1.234x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 129.5 | 128.1 | 148.4 | 7.7 | 0.126x | 1.311x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 351.0 | 328.4 | 356.8 | 10.2 | 0.341x | 3.554x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 353.7 | 334.7 | 359.6 | 11.2 | 0.343x | 3.581x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,030.0 | 1,019.5 | 1,034.2 | 5.6 | 1.000x | 10.428x |

### `orig` / `s-050` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 41.8 | 40.3 | 43.0 | 1.0 | 0.139x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 100.6 | 100.3 | 101.2 | 0.3 | 0.335x | 2.409x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 100.7 | 100.6 | 100.7 | 0.1 | 0.335x | 2.412x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 101.1 | 100.7 | 101.4 | 0.2 | 0.337x | 2.420x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 102.0 | 100.7 | 110.0 | 3.5 | 0.340x | 2.443x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 257.1 | 248.6 | 270.2 | 7.1 | 0.856x | 6.158x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 288.3 | 252.3 | 293.4 | 14.9 | 0.960x | 6.905x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 300.3 | 295.3 | 304.5 | 3.1 | 1.000x | 7.192x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 300.7 | 297.8 | 325.1 | 10.2 | 1.001x | 7.201x |

### `orig` / `s-050` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 95.2 | 94.9 | 96.0 | 0.4 | 0.058x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 95.2 | 94.8 | 95.4 | 0.2 | 0.058x | 1.000x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 95.4 | 95.3 | 95.5 | 0.1 | 0.058x | 1.002x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 95.9 | 95.5 | 97.4 | 0.7 | 0.058x | 1.007x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 105.1 | 103.5 | 109.3 | 2.0 | 0.064x | 1.104x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 304.1 | 302.4 | 305.6 | 1.1 | 0.185x | 3.194x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 457.2 | 440.6 | 487.9 | 18.8 | 0.278x | 4.803x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 506.4 | 495.2 | 517.4 | 7.3 | 0.308x | 5.319x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,642.9 | 1,622.0 | 1,659.6 | 13.3 | 1.000x | 17.259x |

### `orig` / `s-051` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 22.3 | 22.2 | 23.7 | 0.6 | 0.157x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 126.6 | 126.5 | 127.0 | 0.2 | 0.892x | 5.675x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 126.9 | 126.8 | 127.1 | 0.1 | 0.894x | 5.686x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 127.0 | 126.8 | 127.2 | 0.1 | 0.895x | 5.693x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 127.2 | 126.5 | 135.6 | 3.4 | 0.896x | 5.701x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 141.9 | 140.0 | 143.6 | 1.3 | 1.000x | 6.360x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 143.1 | 140.8 | 158.9 | 6.7 | 1.008x | 6.412x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 239.5 | 232.4 | 254.4 | 8.1 | 1.688x | 10.735x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 271.1 | 253.9 | 279.5 | 8.8 | 1.910x | 12.150x |

### `orig` / `s-051` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 98.6 | 97.7 | 103.1 | 2.0 | 0.096x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 121.1 | 120.9 | 124.9 | 1.5 | 0.118x | 1.229x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 121.2 | 121.1 | 122.3 | 0.5 | 0.118x | 1.229x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 121.7 | 121.6 | 121.7 | 0.1 | 0.119x | 1.235x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 121.9 | 121.5 | 123.8 | 0.8 | 0.119x | 1.237x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 128.3 | 127.9 | 129.5 | 0.6 | 0.125x | 1.302x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 343.1 | 336.8 | 355.8 | 7.3 | 0.334x | 3.481x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 350.5 | 329.6 | 356.8 | 9.7 | 0.342x | 3.556x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,026.4 | 1,022.5 | 1,045.0 | 9.5 | 1.000x | 10.412x |

### `orig` / `s-052` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 26.0 | 27.1 | 0.4 | 0.088x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 37.2 | 37.1 | 37.4 | 0.1 | 0.126x | 1.423x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.4 | 37.2 | 38.2 | 0.4 | 0.126x | 1.430x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.6 | 37.4 | 40.6 | 1.2 | 0.127x | 1.436x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 37.7 | 37.4 | 37.9 | 0.2 | 0.127x | 1.441x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 243.8 | 233.8 | 250.5 | 6.2 | 0.824x | 9.318x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 287.7 | 258.6 | 297.0 | 13.2 | 0.973x | 10.999x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 294.1 | 291.7 | 313.1 | 7.9 | 0.994x | 11.241x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 295.8 | 293.8 | 299.3 | 1.9 | 1.000x | 11.307x |

### `orig` / `s-052` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 31.3 | 31.2 | 32.6 | 0.5 | 0.029x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 31.5 | 31.5 | 33.0 | 0.6 | 0.029x | 1.008x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 31.6 | 31.4 | 31.8 | 0.1 | 0.029x | 1.009x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 31.6 | 31.6 | 31.7 | 0.0 | 0.029x | 1.010x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.7 | 67.3 | 71.5 | 1.7 | 0.063x | 2.196x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 176.7 | 174.0 | 178.3 | 1.6 | 0.161x | 5.644x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 404.9 | 393.9 | 445.4 | 17.7 | 0.369x | 12.933x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 406.3 | 383.3 | 410.5 | 11.4 | 0.370x | 12.978x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,098.2 | 1,079.7 | 1,105.0 | 10.1 | 1.000x | 35.079x |

### `orig` / `s-053` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 26.1 | 27.2 | 0.4 | 0.088x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 28.2 | 27.8 | 28.3 | 0.2 | 0.094x | 1.074x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 28.2 | 28.2 | 28.3 | 0.1 | 0.094x | 1.076x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 28.3 | 28.1 | 28.4 | 0.1 | 0.095x | 1.078x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 28.4 | 28.2 | 29.9 | 0.6 | 0.095x | 1.082x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 245.3 | 234.8 | 251.4 | 6.2 | 0.820x | 9.355x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 288.2 | 255.0 | 303.5 | 16.3 | 0.964x | 10.993x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 294.7 | 292.4 | 312.2 | 7.5 | 0.986x | 11.240x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 299.0 | 294.6 | 300.3 | 2.1 | 1.000x | 11.403x |

### `orig` / `s-053` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 21.3 | 21.0 | 21.6 | 0.2 | 0.020x | 1.000x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 21.3 | 21.3 | 21.4 | 0.0 | 0.020x | 1.002x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 21.3 | 21.1 | 22.7 | 0.6 | 0.020x | 1.003x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 21.3 | 21.3 | 21.5 | 0.1 | 0.020x | 1.004x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.4 | 65.8 | 69.6 | 1.5 | 0.064x | 3.218x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 166.8 | 164.9 | 169.1 | 1.5 | 0.155x | 7.847x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 394.7 | 389.4 | 404.9 | 5.1 | 0.368x | 18.572x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 400.8 | 375.0 | 414.4 | 15.0 | 0.373x | 18.860x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,073.6 | 1,064.1 | 1,078.4 | 4.9 | 1.000x | 50.522x |

### `orig` / `s-054` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 26.0 | 26.5 | 0.2 | 0.087x | 1.000x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 28.0 | 27.7 | 28.2 | 0.2 | 0.094x | 1.075x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 28.0 | 27.9 | 28.1 | 0.1 | 0.094x | 1.076x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 28.1 | 28.0 | 28.4 | 0.1 | 0.094x | 1.078x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 28.2 | 28.0 | 30.4 | 0.9 | 0.094x | 1.081x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 247.3 | 233.7 | 253.9 | 7.2 | 0.826x | 9.494x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 286.8 | 255.7 | 287.5 | 12.4 | 0.958x | 11.009x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 295.2 | 292.8 | 313.9 | 7.9 | 0.986x | 11.332x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 299.5 | 293.1 | 306.7 | 5.2 | 1.000x | 11.497x |

### `orig` / `s-054` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 21.2 | 21.0 | 21.5 | 0.2 | 0.020x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 21.3 | 21.1 | 21.6 | 0.2 | 0.020x | 1.007x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 21.3 | 21.3 | 21.4 | 0.0 | 0.020x | 1.009x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 21.7 | 21.3 | 22.5 | 0.5 | 0.020x | 1.025x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 66.8 | 64.9 | 69.7 | 1.8 | 0.062x | 3.158x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 170.3 | 165.5 | 170.5 | 2.0 | 0.159x | 8.048x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 393.8 | 377.9 | 405.3 | 9.4 | 0.367x | 18.611x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 397.3 | 379.0 | 438.2 | 22.9 | 0.370x | 18.774x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,074.1 | 1,061.2 | 1,075.2 | 5.5 | 1.000x | 50.761x |

### `orig` / `s-055` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 26.1 | 26.6 | 0.2 | 0.089x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 28.1 | 27.8 | 29.7 | 0.7 | 0.095x | 1.071x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 28.1 | 28.0 | 28.8 | 0.3 | 0.096x | 1.072x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 28.1 | 27.8 | 28.7 | 0.3 | 0.096x | 1.073x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 28.2 | 28.0 | 30.6 | 1.0 | 0.096x | 1.078x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 249.5 | 234.4 | 254.8 | 7.6 | 0.849x | 9.524x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 283.3 | 256.5 | 286.7 | 11.3 | 0.964x | 10.818x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 293.9 | 293.1 | 301.0 | 3.5 | 1.000x | 11.222x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 294.5 | 293.4 | 312.7 | 7.3 | 1.002x | 11.245x |

### `orig` / `s-055` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 21.2 | 21.0 | 23.3 | 0.9 | 0.020x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 21.2 | 21.2 | 21.3 | 0.0 | 0.020x | 1.003x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 21.3 | 21.3 | 21.6 | 0.1 | 0.020x | 1.007x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 21.4 | 21.3 | 22.8 | 0.5 | 0.020x | 1.012x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 67.1 | 65.3 | 69.3 | 1.5 | 0.063x | 3.169x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 168.9 | 165.6 | 170.5 | 1.7 | 0.157x | 7.977x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 398.3 | 385.5 | 412.1 | 9.5 | 0.371x | 18.811x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 405.1 | 361.3 | 433.9 | 25.9 | 0.378x | 19.131x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,072.5 | 1,054.0 | 1,088.8 | 12.9 | 1.000x | 50.655x |

### `orig` / `s-056` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 26.0 | 27.7 | 0.6 | 0.089x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 30.9 | 30.7 | 32.4 | 0.6 | 0.105x | 1.181x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 31.0 | 30.8 | 32.3 | 0.6 | 0.105x | 1.183x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 31.0 | 30.5 | 31.2 | 0.3 | 0.105x | 1.183x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 31.2 | 30.8 | 31.6 | 0.3 | 0.106x | 1.190x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 251.2 | 237.2 | 258.0 | 8.5 | 0.855x | 9.589x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 283.6 | 253.3 | 286.7 | 12.3 | 0.965x | 10.827x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 293.9 | 290.6 | 299.0 | 2.8 | 1.000x | 11.221x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 294.5 | 293.6 | 310.9 | 6.6 | 1.002x | 11.242x |

### `orig` / `s-056` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 25.4 | 25.3 | 28.2 | 1.1 | 0.024x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 25.4 | 25.4 | 25.6 | 0.1 | 0.024x | 1.001x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 25.5 | 25.4 | 29.6 | 1.6 | 0.024x | 1.005x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 25.6 | 25.4 | 25.8 | 0.1 | 0.024x | 1.007x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 67.2 | 65.1 | 69.8 | 1.7 | 0.063x | 2.648x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 158.4 | 156.7 | 165.1 | 3.0 | 0.148x | 6.238x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 386.8 | 379.2 | 398.3 | 6.5 | 0.362x | 15.237x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 397.3 | 355.8 | 409.9 | 20.5 | 0.371x | 15.650x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,069.8 | 1,064.7 | 1,070.6 | 2.2 | 1.000x | 42.142x |

### `orig` / `s-057` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 7,695.9 | 7,688.4 | 7,744.5 | 20.4 | 0.779x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7,871.4 | 7,859.3 | 7,894.1 | 13.3 | 0.797x | 1.023x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7,918.3 | 7,863.2 | 8,002.2 | 48.2 | 0.802x | 1.029x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 9,859.2 | 9,827.4 | 9,878.4 | 16.9 | 0.998x | 1.281x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 9,874.6 | 9,834.3 | 10,165.3 | 124.9 | 1.000x | 1.283x |
| 6 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 67,097.9 | 67,070.2 | 67,245.7 | 65.3 | 6.795x | 8.719x |
| 7 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 67,142.7 | 67,124.1 | 67,363.0 | 89.3 | 6.800x | 8.724x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 67,298.3 | 67,249.2 | 67,361.6 | 38.9 | 6.815x | 8.745x |
| 9 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 67,491.2 | 67,374.7 | 67,996.4 | 226.6 | 6.835x | 8.770x |

### `orig` / `s-058` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5,971.4 | 5,913.7 | 6,151.8 | 86.0 | 0.082x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 6,145.7 | 6,081.6 | 6,201.2 | 44.7 | 0.084x | 1.029x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 6,675.3 | 6,669.3 | 6,695.3 | 9.0 | 0.092x | 1.118x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 26,276.4 | 26,269.5 | 26,332.0 | 25.0 | 0.361x | 4.400x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 26,294.3 | 26,264.3 | 26,326.8 | 23.9 | 0.361x | 4.403x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 26,316.1 | 26,297.5 | 26,343.4 | 15.2 | 0.361x | 4.407x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 26,352.1 | 26,306.2 | 26,422.6 | 39.2 | 0.362x | 4.413x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 72,884.2 | 72,361.3 | 73,429.0 | 376.6 | 1.000x | 12.206x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 72,970.1 | 72,674.5 | 78,811.0 | 2,379.3 | 1.001x | 12.220x |

### `orig` / `s-059` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 13,749.4 | 13,740.5 | 13,818.2 | 29.1 | 0.086x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 13,907.4 | 13,872.5 | 14,000.9 | 44.2 | 0.087x | 1.011x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 26,064.0 | 26,020.4 | 26,117.0 | 35.4 | 0.163x | 1.896x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33,580.3 | 33,570.4 | 33,606.8 | 14.4 | 0.210x | 2.442x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33,604.3 | 33,598.6 | 33,715.0 | 44.3 | 0.210x | 2.444x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33,713.1 | 33,688.7 | 33,802.2 | 42.9 | 0.211x | 2.452x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33,735.5 | 33,683.9 | 33,776.5 | 39.3 | 0.211x | 2.454x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 159,044.0 | 158,732.5 | 161,263.0 | 966.9 | 0.994x | 11.567x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 159,957.9 | 158,455.0 | 161,577.8 | 1,091.4 | 1.000x | 11.634x |

### `orig` / `s-060` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 7,664.6 | 7,656.8 | 7,691.1 | 11.9 | 0.812x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7,818.9 | 7,785.7 | 7,841.9 | 20.4 | 0.828x | 1.020x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7,867.9 | 7,833.5 | 7,936.9 | 34.1 | 0.833x | 1.027x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 9,438.7 | 9,419.2 | 9,538.3 | 47.0 | 0.999x | 1.231x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 9,444.6 | 9,422.5 | 9,548.4 | 46.5 | 1.000x | 1.232x |
| 6 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33,375.9 | 33,328.7 | 33,425.7 | 35.2 | 3.534x | 4.355x |
| 7 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33,388.9 | 33,320.7 | 33,487.7 | 62.4 | 3.535x | 4.356x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33,480.3 | 33,462.8 | 33,575.0 | 42.0 | 3.545x | 4.368x |
| 9 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33,536.1 | 33,522.2 | 33,827.7 | 117.7 | 3.551x | 4.375x |

### `orig` / `s-061` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5,391.2 | 5,373.8 | 5,452.7 | 27.2 | 0.121x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6,158.0 | 6,137.2 | 6,577.2 | 189.1 | 0.138x | 1.142x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 6,305.0 | 6,296.9 | 6,414.4 | 44.7 | 0.141x | 1.169x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13,151.8 | 13,137.8 | 13,163.5 | 8.8 | 0.294x | 2.439x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13,169.0 | 13,152.2 | 13,207.9 | 19.3 | 0.295x | 2.443x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13,196.0 | 13,179.0 | 13,238.8 | 20.3 | 0.295x | 2.448x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13,197.4 | 13,174.8 | 13,210.4 | 12.5 | 0.295x | 2.448x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44,625.9 | 44,550.6 | 45,315.0 | 301.9 | 0.999x | 8.277x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 44,681.4 | 44,532.7 | 44,970.8 | 145.6 | 1.000x | 8.288x |

### `orig` / `s-062` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 43.7 | 43.7 | 44.6 | 0.3 | 0.138x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 224.8 | 206.7 | 269.3 | 24.6 | 0.707x | 5.141x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 245.4 | 238.7 | 281.9 | 15.9 | 0.772x | 5.612x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 317.9 | 311.3 | 335.4 | 9.2 | 1.000x | 7.269x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 321.7 | 318.6 | 333.2 | 5.5 | 1.012x | 7.356x |
| 6 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 1,683.4 | 1,682.1 | 1,683.7 | 0.7 | 5.295x | 38.491x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 1,686.2 | 1,682.8 | 1,700.4 | 6.2 | 5.304x | 38.554x |
| 8 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 1,687.0 | 1,682.9 | 1,691.8 | 2.9 | 5.307x | 38.573x |
| 9 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 1,690.2 | 1,683.4 | 1,702.9 | 6.3 | 5.317x | 38.646x |

### `orig` / `s-063` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6,877.5 | 6,857.1 | 6,937.4 | 29.1 | 0.063x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7,041.6 | 7,024.9 | 7,114.8 | 32.0 | 0.064x | 1.024x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 13,122.7 | 13,112.7 | 13,128.9 | 5.8 | 0.119x | 1.908x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 25,210.9 | 25,188.3 | 25,276.3 | 33.9 | 0.229x | 3.666x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 25,217.7 | 25,197.3 | 25,244.7 | 17.2 | 0.229x | 3.667x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 25,279.6 | 25,276.9 | 25,357.2 | 31.2 | 0.230x | 3.676x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 25,351.7 | 25,280.8 | 25,394.7 | 42.0 | 0.230x | 3.686x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 110,016.9 | 109,164.5 | 110,418.8 | 428.8 | 1.000x | 15.997x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 110,103.9 | 109,391.1 | 111,391.7 | 701.5 | 1.001x | 16.009x |

### `orig` / `s-064` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 10,640.7 | 10,624.5 | 10,649.9 | 10.8 | 0.112x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 10,799.0 | 10,772.3 | 10,869.6 | 34.6 | 0.113x | 1.015x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 11,644.1 | 11,605.0 | 12,777.2 | 455.9 | 0.122x | 1.094x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 26,888.2 | 26,876.1 | 26,902.8 | 10.0 | 0.282x | 2.527x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 26,892.2 | 26,883.0 | 26,906.1 | 7.4 | 0.282x | 2.527x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 27,033.2 | 27,014.2 | 27,185.9 | 70.3 | 0.284x | 2.541x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 27,036.7 | 26,989.2 | 27,561.3 | 212.5 | 0.284x | 2.541x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 95,112.6 | 94,870.7 | 97,338.8 | 917.3 | 0.999x | 8.939x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 95,201.2 | 94,869.4 | 96,222.9 | 524.5 | 1.000x | 8.947x |

### `orig` / `s-065` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 16.4 | 16.3 | 19.5 | 1.3 | 0.550x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.4 | 29.3 | 29.6 | 0.1 | 0.989x | 1.797x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.7 | 29.3 | 29.9 | 0.2 | 1.000x | 1.817x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 41.3 | 41.2 | 41.4 | 0.1 | 1.389x | 2.523x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 41.3 | 41.1 | 41.4 | 0.1 | 1.390x | 2.526x |
| 6 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 41.5 | 41.3 | 41.5 | 0.1 | 1.396x | 2.536x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 41.6 | 41.1 | 41.7 | 0.2 | 1.400x | 2.543x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 209.5 | 204.8 | 228.4 | 9.6 | 7.049x | 12.807x |
| 9 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 226.1 | 178.6 | 244.2 | 23.5 | 7.606x | 13.817x |

### `orig` / `s-065` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 33.7 | 33.7 | 36.2 | 1.0 | 0.059x | 1.000x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 33.8 | 33.4 | 34.1 | 0.2 | 0.060x | 1.002x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 34.1 | 33.6 | 34.4 | 0.3 | 0.060x | 1.010x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 34.6 | 33.7 | 42.2 | 3.1 | 0.061x | 1.026x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 63.3 | 61.0 | 65.8 | 1.6 | 0.112x | 1.877x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 230.0 | 228.5 | 233.7 | 1.7 | 0.405x | 6.820x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 454.9 | 444.0 | 473.6 | 10.8 | 0.802x | 13.488x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 460.4 | 434.4 | 469.0 | 13.9 | 0.812x | 13.652x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 567.2 | 561.4 | 572.4 | 4.2 | 1.000x | 16.818x |

### `orig` / `s-066` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 74.6 | 74.6 | 74.8 | 0.1 | 0.114x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 117.1 | 116.9 | 117.6 | 0.3 | 0.178x | 1.569x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 117.2 | 117.1 | 117.3 | 0.1 | 0.178x | 1.570x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 117.2 | 116.8 | 118.0 | 0.5 | 0.178x | 1.571x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 118.6 | 117.4 | 135.5 | 7.1 | 0.180x | 1.589x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 271.1 | 250.8 | 281.1 | 10.8 | 0.413x | 3.632x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 275.5 | 269.2 | 316.5 | 19.6 | 0.419x | 3.691x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 657.0 | 654.0 | 661.0 | 2.5 | 1.000x | 8.803x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 660.0 | 651.3 | 666.3 | 5.1 | 1.005x | 8.843x |

### `orig` / `s-066` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 80.4 | 80.3 | 80.8 | 0.2 | 0.120x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 82.2 | 81.3 | 84.9 | 1.3 | 0.123x | 1.021x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 109.9 | 109.6 | 115.7 | 2.4 | 0.164x | 1.366x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 110.0 | 109.5 | 111.0 | 0.5 | 0.164x | 1.367x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 110.4 | 109.7 | 110.6 | 0.3 | 0.165x | 1.373x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 111.5 | 109.7 | 114.7 | 1.8 | 0.167x | 1.386x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 295.4 | 286.8 | 298.9 | 4.8 | 0.442x | 3.672x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 313.8 | 295.5 | 326.8 | 10.6 | 0.469x | 3.901x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 668.9 | 656.9 | 676.3 | 7.3 | 1.000x | 8.314x |

### `orig` / `s-067` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 77.7 | 77.7 | 79.6 | 0.8 | 0.121x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 110.5 | 110.5 | 110.8 | 0.1 | 0.173x | 1.423x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 110.7 | 110.4 | 112.5 | 0.8 | 0.173x | 1.424x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 110.8 | 110.2 | 120.0 | 3.8 | 0.173x | 1.427x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 110.9 | 110.2 | 111.1 | 0.3 | 0.173x | 1.428x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 279.4 | 271.6 | 296.7 | 9.2 | 0.437x | 3.597x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 284.0 | 275.8 | 292.6 | 5.8 | 0.444x | 3.656x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 639.8 | 633.9 | 655.3 | 8.3 | 1.000x | 8.235x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 648.4 | 635.2 | 656.9 | 7.1 | 1.013x | 8.346x |

### `orig` / `s-067` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 81.7 | 80.9 | 86.1 | 1.9 | 0.127x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 90.0 | 89.8 | 90.1 | 0.1 | 0.140x | 1.102x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 103.2 | 102.3 | 104.6 | 0.7 | 0.161x | 1.264x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 103.3 | 103.3 | 103.8 | 0.2 | 0.161x | 1.265x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 103.4 | 102.8 | 103.7 | 0.3 | 0.161x | 1.266x |
| 6 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 104.3 | 103.4 | 104.4 | 0.4 | 0.162x | 1.277x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 286.9 | 254.3 | 299.4 | 15.3 | 0.447x | 3.513x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 291.4 | 285.0 | 320.7 | 12.9 | 0.454x | 3.569x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 642.3 | 637.8 | 651.3 | 4.5 | 1.000x | 7.866x |

### `orig` / `s-068` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 20.8 | 20.6 | 21.0 | 0.1 | 0.050x | 1.000x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 39.8 | 39.5 | 40.0 | 0.2 | 0.096x | 1.915x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 40.2 | 39.8 | 40.4 | 0.2 | 0.097x | 1.934x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 40.3 | 39.9 | 40.6 | 0.2 | 0.097x | 1.940x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 40.4 | 39.8 | 49.6 | 3.7 | 0.097x | 1.947x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 258.6 | 221.8 | 261.8 | 14.8 | 0.623x | 12.451x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 261.1 | 241.1 | 273.7 | 11.0 | 0.629x | 12.572x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 414.8 | 405.1 | 446.0 | 14.1 | 1.000x | 19.973x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 416.2 | 408.8 | 425.0 | 5.4 | 1.004x | 20.043x |

### `orig` / `s-068` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 26.2 | 25.5 | 27.1 | 0.5 | 0.063x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 32.6 | 32.4 | 32.9 | 0.2 | 0.078x | 1.246x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 32.6 | 32.4 | 34.4 | 0.7 | 0.078x | 1.247x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 32.8 | 32.7 | 36.3 | 1.4 | 0.079x | 1.253x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 32.8 | 32.7 | 33.1 | 0.2 | 0.079x | 1.254x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 58.9 | 54.1 | 64.9 | 3.8 | 0.142x | 2.252x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 262.8 | 257.4 | 282.5 | 8.8 | 0.632x | 10.041x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 264.5 | 248.6 | 271.5 | 7.7 | 0.636x | 10.106x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 415.9 | 409.8 | 421.2 | 3.6 | 1.000x | 15.891x |

### `orig` / `s-069` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 26.0 | 27.2 | 0.4 | 0.125x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 53.1 | 52.6 | 53.4 | 0.2 | 0.255x | 2.033x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 53.2 | 52.9 | 53.6 | 0.2 | 0.255x | 2.034x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 53.3 | 52.9 | 54.0 | 0.4 | 0.256x | 2.038x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 54.1 | 53.5 | 54.4 | 0.4 | 0.260x | 2.071x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 206.2 | 206.0 | 223.2 | 6.6 | 0.989x | 7.889x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 208.4 | 205.8 | 248.4 | 16.5 | 1.000x | 7.974x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 244.5 | 224.4 | 261.5 | 12.1 | 1.173x | 9.356x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 283.0 | 241.7 | 299.4 | 19.2 | 1.358x | 10.830x |

### `orig` / `s-069` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 47.0 | 47.0 | 48.3 | 0.5 | 0.064x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 47.2 | 47.1 | 47.4 | 0.1 | 0.064x | 1.004x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 47.5 | 47.2 | 47.5 | 0.1 | 0.064x | 1.009x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 47.8 | 47.3 | 48.0 | 0.3 | 0.065x | 1.016x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 66.2 | 65.4 | 68.6 | 1.3 | 0.089x | 1.408x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 236.5 | 235.7 | 241.4 | 2.1 | 0.320x | 5.028x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 455.5 | 442.6 | 469.0 | 9.7 | 0.615x | 9.685x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 455.8 | 441.9 | 478.7 | 12.1 | 0.616x | 9.691x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 740.2 | 727.9 | 740.7 | 5.4 | 1.000x | 15.736x |

### `orig` / `s-070` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 44.7 | 44.2 | 46.1 | 0.7 | 0.081x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 90.7 | 90.3 | 90.8 | 0.2 | 0.165x | 2.030x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 90.9 | 90.6 | 92.5 | 0.7 | 0.165x | 2.034x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 91.0 | 90.6 | 100.7 | 3.9 | 0.165x | 2.037x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 91.0 | 90.6 | 91.5 | 0.3 | 0.165x | 2.037x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 262.9 | 251.6 | 292.8 | 14.5 | 0.478x | 5.883x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 287.6 | 247.3 | 292.2 | 16.4 | 0.523x | 6.436x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 542.3 | 536.1 | 578.9 | 15.9 | 0.986x | 12.136x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 550.1 | 544.1 | 559.2 | 5.2 | 1.000x | 12.311x |

### `orig` / `s-070` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 51.3 | 51.0 | 52.1 | 0.4 | 0.095x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 75.1 | 74.0 | 79.1 | 1.9 | 0.138x | 1.462x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 82.9 | 82.7 | 83.4 | 0.3 | 0.153x | 1.614x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 83.4 | 83.2 | 83.5 | 0.1 | 0.154x | 1.624x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 83.8 | 82.7 | 84.7 | 0.8 | 0.155x | 1.633x |
| 6 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 83.9 | 83.2 | 85.2 | 0.7 | 0.155x | 1.635x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 273.0 | 262.6 | 284.5 | 6.9 | 0.503x | 5.317x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 282.8 | 268.4 | 289.3 | 7.8 | 0.522x | 5.509x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 542.3 | 540.7 | 546.8 | 2.5 | 1.000x | 10.561x |

### `orig` / `s-071` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 58.4 | 57.8 | 60.6 | 1.0 | 0.103x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 202.0 | 201.8 | 202.6 | 0.3 | 0.357x | 3.459x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 202.2 | 201.9 | 202.4 | 0.2 | 0.358x | 3.462x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 202.6 | 202.4 | 203.6 | 0.4 | 0.358x | 3.469x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 204.5 | 202.7 | 213.3 | 4.7 | 0.362x | 3.502x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 271.8 | 269.9 | 276.6 | 2.4 | 0.481x | 4.654x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 278.7 | 244.0 | 288.8 | 16.4 | 0.493x | 4.773x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 561.8 | 557.3 | 580.0 | 7.8 | 0.994x | 9.622x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 565.4 | 559.4 | 578.9 | 6.7 | 1.000x | 9.684x |

### `orig` / `s-071` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 65.4 | 65.2 | 67.6 | 0.9 | 0.117x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 89.7 | 89.1 | 94.9 | 2.2 | 0.160x | 1.371x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 194.4 | 194.2 | 195.1 | 0.3 | 0.347x | 2.973x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 194.7 | 194.2 | 194.9 | 0.3 | 0.347x | 2.977x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 200.8 | 200.6 | 202.2 | 0.6 | 0.358x | 3.069x |
| 6 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 201.1 | 200.7 | 202.6 | 0.7 | 0.359x | 3.074x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 281.7 | 272.8 | 295.4 | 7.4 | 0.502x | 4.307x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 286.9 | 265.0 | 293.8 | 10.4 | 0.512x | 4.387x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 560.8 | 560.3 | 570.5 | 3.9 | 1.000x | 8.574x |

### `orig` / `s-072` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 67.1 | 66.9 | 68.0 | 0.4 | 0.056x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 166.0 | 165.8 | 166.9 | 0.4 | 0.138x | 2.474x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 166.0 | 165.9 | 166.1 | 0.1 | 0.138x | 2.475x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 166.1 | 165.9 | 166.6 | 0.3 | 0.138x | 2.476x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 166.3 | 166.0 | 174.8 | 3.4 | 0.138x | 2.479x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 300.0 | 285.2 | 306.2 | 7.4 | 0.249x | 4.472x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 386.8 | 324.0 | 394.8 | 26.0 | 0.321x | 5.766x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,194.3 | 1,183.1 | 1,241.6 | 21.1 | 0.990x | 17.804x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,206.0 | 1,185.9 | 1,207.6 | 8.3 | 1.000x | 17.979x |

### `orig` / `s-072` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 153.6 | 153.1 | 154.8 | 0.6 | 0.088x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 160.8 | 160.7 | 161.1 | 0.1 | 0.092x | 1.046x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 160.8 | 160.4 | 161.4 | 0.4 | 0.093x | 1.047x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 160.8 | 160.7 | 162.1 | 0.5 | 0.093x | 1.047x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 161.0 | 160.8 | 161.6 | 0.3 | 0.093x | 1.048x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 171.4 | 168.1 | 186.7 | 6.6 | 0.099x | 1.116x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 368.4 | 350.2 | 380.0 | 11.0 | 0.212x | 2.398x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 424.0 | 400.5 | 426.5 | 10.6 | 0.244x | 2.760x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,738.3 | 1,731.1 | 1,780.0 | 17.5 | 1.000x | 11.313x |

### `orig` / `s-073` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 26.0 | 26.9 | 0.3 | 0.087x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 40.2 | 40.1 | 40.5 | 0.1 | 0.134x | 1.540x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 40.2 | 40.0 | 40.6 | 0.2 | 0.135x | 1.541x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 40.3 | 40.2 | 44.9 | 1.9 | 0.135x | 1.543x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 40.5 | 40.3 | 40.6 | 0.1 | 0.135x | 1.551x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 246.7 | 231.9 | 248.2 | 6.1 | 0.825x | 9.452x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 285.9 | 242.5 | 291.5 | 17.9 | 0.956x | 10.953x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 298.5 | 292.3 | 312.5 | 6.7 | 0.998x | 11.434x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 299.1 | 292.8 | 323.8 | 11.5 | 1.000x | 11.457x |

### `orig` / `s-073` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 34.5 | 34.3 | 35.0 | 0.2 | 0.032x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 34.5 | 34.3 | 35.6 | 0.5 | 0.032x | 1.000x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 34.6 | 34.5 | 34.6 | 0.1 | 0.032x | 1.003x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 34.6 | 34.5 | 35.0 | 0.2 | 0.032x | 1.003x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.5 | 67.4 | 71.9 | 1.6 | 0.063x | 1.988x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 190.0 | 188.8 | 190.7 | 0.6 | 0.175x | 5.512x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 406.4 | 385.4 | 426.1 | 13.6 | 0.374x | 11.793x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 420.2 | 411.0 | 458.6 | 17.6 | 0.387x | 12.192x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,086.0 | 1,064.4 | 1,092.2 | 10.0 | 1.000x | 31.513x |

### `orig` / `s-074` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 35.1 | 35.0 | 35.1 | 0.0 | 0.116x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 53.3 | 53.1 | 54.9 | 0.7 | 0.177x | 1.519x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 53.4 | 53.2 | 53.8 | 0.2 | 0.177x | 1.523x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 53.5 | 52.9 | 58.6 | 2.1 | 0.177x | 1.525x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 53.6 | 53.4 | 54.4 | 0.3 | 0.178x | 1.530x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 253.0 | 236.4 | 253.9 | 6.7 | 0.840x | 7.217x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 285.3 | 247.8 | 291.0 | 16.0 | 0.947x | 8.137x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 295.4 | 295.0 | 312.7 | 6.9 | 0.981x | 8.426x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 301.2 | 294.7 | 319.4 | 9.1 | 1.000x | 8.592x |

### `orig` / `s-074` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 47.1 | 46.9 | 48.7 | 0.7 | 0.044x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 47.3 | 46.9 | 47.8 | 0.4 | 0.044x | 1.004x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 47.5 | 47.4 | 48.3 | 0.3 | 0.044x | 1.007x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 47.5 | 47.4 | 47.7 | 0.1 | 0.044x | 1.009x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 70.1 | 69.5 | 72.1 | 1.0 | 0.065x | 1.488x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 303.6 | 301.5 | 304.6 | 1.2 | 0.282x | 6.443x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 531.2 | 504.6 | 550.2 | 16.9 | 0.494x | 11.273x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 578.4 | 546.6 | 597.8 | 18.7 | 0.538x | 12.276x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,075.6 | 1,066.8 | 1,079.9 | 4.8 | 1.000x | 22.828x |

### `orig` / `s-075` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 88.4 | 88.3 | 90.1 | 0.7 | 0.138x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 110.5 | 110.3 | 111.0 | 0.2 | 0.172x | 1.250x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 110.7 | 110.0 | 112.2 | 0.7 | 0.172x | 1.252x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 110.7 | 109.7 | 111.7 | 0.6 | 0.172x | 1.252x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 111.2 | 110.6 | 119.9 | 3.6 | 0.173x | 1.257x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 280.6 | 270.4 | 286.7 | 6.1 | 0.437x | 3.174x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 292.4 | 271.6 | 297.6 | 9.0 | 0.455x | 3.306x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 641.3 | 633.6 | 662.4 | 10.1 | 0.998x | 7.253x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 642.8 | 630.2 | 699.7 | 24.8 | 1.000x | 7.269x |

### `orig` / `s-075` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 69.2 | 68.9 | 69.6 | 0.2 | 0.108x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 87.5 | 87.2 | 87.9 | 0.3 | 0.136x | 1.264x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 102.7 | 102.5 | 103.8 | 0.4 | 0.160x | 1.486x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 103.2 | 102.9 | 103.3 | 0.2 | 0.161x | 1.492x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 103.2 | 103.0 | 103.4 | 0.1 | 0.161x | 1.493x |
| 6 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 103.5 | 103.2 | 106.4 | 1.2 | 0.161x | 1.496x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 278.8 | 265.6 | 290.1 | 9.9 | 0.435x | 4.032x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 292.0 | 281.4 | 303.0 | 7.7 | 0.456x | 4.222x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 641.0 | 637.2 | 643.6 | 2.4 | 1.000x | 9.268x |

### `orig` / `s-076` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 88.6 | 88.2 | 89.2 | 0.4 | 0.139x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 110.6 | 110.2 | 110.8 | 0.2 | 0.173x | 1.248x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 110.7 | 110.6 | 111.3 | 0.3 | 0.173x | 1.249x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 110.7 | 110.5 | 111.4 | 0.3 | 0.173x | 1.249x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 111.2 | 110.4 | 119.6 | 3.5 | 0.174x | 1.255x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 277.5 | 267.7 | 282.2 | 5.0 | 0.434x | 3.131x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 292.4 | 270.6 | 298.9 | 10.4 | 0.457x | 3.299x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 636.7 | 628.2 | 652.6 | 8.4 | 0.995x | 7.183x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 640.0 | 630.1 | 661.1 | 10.2 | 1.000x | 7.220x |

### `orig` / `s-076` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 69.2 | 69.1 | 69.3 | 0.1 | 0.108x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 87.8 | 87.3 | 88.0 | 0.3 | 0.138x | 1.269x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 102.9 | 102.7 | 105.6 | 1.1 | 0.161x | 1.487x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 103.2 | 102.2 | 103.6 | 0.5 | 0.162x | 1.491x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 103.5 | 103.1 | 105.1 | 0.7 | 0.162x | 1.495x |
| 6 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 103.5 | 103.1 | 103.7 | 0.2 | 0.162x | 1.496x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 280.7 | 265.6 | 290.5 | 8.9 | 0.440x | 4.057x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 293.8 | 277.7 | 303.6 | 9.1 | 0.461x | 4.246x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 637.8 | 632.4 | 645.5 | 4.2 | 1.000x | 9.219x |

### `orig` / `s-077` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 87.3 | 86.5 | 88.4 | 0.6 | 0.124x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 110.5 | 109.6 | 111.0 | 0.5 | 0.156x | 1.265x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 110.6 | 110.5 | 111.2 | 0.3 | 0.157x | 1.267x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 110.9 | 110.7 | 111.7 | 0.4 | 0.157x | 1.270x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 110.9 | 110.5 | 119.6 | 3.5 | 0.157x | 1.270x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 275.0 | 269.5 | 287.8 | 6.4 | 0.389x | 3.148x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 298.0 | 272.1 | 300.6 | 10.6 | 0.422x | 3.412x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 706.9 | 693.2 | 729.5 | 11.7 | 1.000x | 8.093x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 716.3 | 698.5 | 854.4 | 57.4 | 1.013x | 8.202x |

### `orig` / `s-077` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 62.8 | 62.3 | 69.7 | 2.8 | 0.090x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 88.7 | 88.3 | 89.1 | 0.3 | 0.126x | 1.411x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 103.0 | 102.8 | 103.3 | 0.2 | 0.147x | 1.639x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 103.4 | 102.7 | 103.8 | 0.4 | 0.147x | 1.645x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 103.4 | 103.2 | 125.6 | 8.9 | 0.147x | 1.646x |
| 6 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 103.5 | 103.3 | 103.6 | 0.1 | 0.147x | 1.647x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 286.5 | 249.0 | 320.6 | 27.0 | 0.408x | 4.559x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 291.4 | 273.9 | 310.4 | 12.3 | 0.415x | 4.637x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 701.7 | 696.2 | 707.2 | 3.7 | 1.000x | 11.167x |

### `orig` / `s-078` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 74.0 | 73.8 | 74.1 | 0.1 | 0.102x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 110.3 | 109.9 | 110.7 | 0.3 | 0.152x | 1.491x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 110.6 | 110.2 | 111.5 | 0.5 | 0.152x | 1.494x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 110.8 | 110.4 | 111.1 | 0.2 | 0.153x | 1.497x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 110.9 | 110.8 | 117.2 | 2.5 | 0.153x | 1.498x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 271.0 | 267.3 | 273.5 | 2.4 | 0.373x | 3.662x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 289.1 | 268.1 | 297.4 | 10.2 | 0.398x | 3.906x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 724.8 | 720.4 | 768.0 | 17.5 | 0.999x | 9.793x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 725.8 | 724.3 | 797.7 | 28.3 | 1.000x | 9.806x |

### `orig` / `s-078` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 64.7 | 60.0 | 72.1 | 4.2 | 0.088x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 83.7 | 83.1 | 85.5 | 0.9 | 0.114x | 1.294x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 103.2 | 103.0 | 103.6 | 0.2 | 0.141x | 1.594x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 103.3 | 103.2 | 121.5 | 7.2 | 0.141x | 1.597x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 103.4 | 103.3 | 128.7 | 10.1 | 0.141x | 1.599x |
| 6 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 103.5 | 103.2 | 104.1 | 0.4 | 0.141x | 1.599x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 277.5 | 263.8 | 296.3 | 11.2 | 0.378x | 4.289x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 284.6 | 239.8 | 321.1 | 29.3 | 0.388x | 4.399x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 733.6 | 723.3 | 739.7 | 5.4 | 1.000x | 11.338x |

### `orig` / `s-079` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 73.9 | 73.8 | 74.0 | 0.1 | 0.102x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 110.6 | 109.5 | 110.8 | 0.5 | 0.152x | 1.495x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 110.6 | 110.3 | 114.9 | 1.7 | 0.152x | 1.496x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 110.9 | 110.7 | 111.3 | 0.2 | 0.153x | 1.499x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 111.0 | 110.3 | 111.9 | 0.5 | 0.153x | 1.501x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 270.8 | 267.2 | 281.1 | 4.8 | 0.372x | 3.662x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 283.5 | 263.9 | 309.9 | 17.0 | 0.390x | 3.834x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 722.8 | 721.8 | 764.6 | 16.4 | 0.994x | 9.776x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 727.0 | 724.8 | 818.2 | 36.4 | 1.000x | 9.832x |

### `orig` / `s-079` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 64.9 | 62.1 | 67.9 | 2.2 | 0.089x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 83.3 | 83.1 | 84.5 | 0.6 | 0.115x | 1.284x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 103.0 | 102.6 | 103.1 | 0.2 | 0.142x | 1.588x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 103.1 | 102.6 | 103.8 | 0.4 | 0.142x | 1.590x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 103.2 | 103.2 | 103.4 | 0.1 | 0.142x | 1.591x |
| 6 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 103.3 | 103.2 | 103.8 | 0.2 | 0.142x | 1.593x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 285.7 | 268.5 | 306.5 | 13.4 | 0.393x | 4.404x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 297.0 | 249.2 | 320.4 | 24.9 | 0.408x | 4.578x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 727.3 | 722.0 | 738.9 | 6.1 | 1.000x | 11.211x |

### `orig` / `s-080` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 46.8 | 46.6 | 47.5 | 0.3 | 0.132x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 50.4 | 50.0 | 54.8 | 1.8 | 0.142x | 1.076x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 50.4 | 50.3 | 50.4 | 0.1 | 0.142x | 1.077x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 50.5 | 50.3 | 51.0 | 0.3 | 0.143x | 1.078x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 50.5 | 49.7 | 54.9 | 1.9 | 0.143x | 1.080x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 265.9 | 261.8 | 273.7 | 4.2 | 0.751x | 5.681x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 284.1 | 254.5 | 287.4 | 12.3 | 0.803x | 6.070x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 353.9 | 343.7 | 377.9 | 12.3 | 1.000x | 7.562x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 355.5 | 347.6 | 388.0 | 14.5 | 1.004x | 7.595x |

### `orig` / `s-080` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 43.9 | 43.7 | 44.4 | 0.3 | 0.034x | 1.000x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 44.0 | 43.8 | 44.2 | 0.2 | 0.034x | 1.002x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 44.2 | 44.0 | 44.2 | 0.1 | 0.034x | 1.006x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 44.4 | 43.7 | 46.1 | 0.8 | 0.034x | 1.011x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 70.8 | 70.3 | 74.0 | 1.4 | 0.055x | 1.613x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 378.5 | 377.2 | 379.4 | 0.8 | 0.294x | 8.623x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 598.9 | 590.0 | 600.5 | 3.9 | 0.465x | 13.644x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 611.2 | 603.0 | 638.0 | 12.5 | 0.475x | 13.924x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,287.1 | 1,274.9 | 1,299.3 | 9.4 | 1.000x | 29.321x |

### `orig` / `s-081` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 11.9 | 11.8 | 12.3 | 0.2 | 0.404x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.1 | 11.9 | 12.1 | 0.1 | 0.408x | 1.011x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 12.4 | 12.1 | 12.4 | 0.1 | 0.420x | 1.040x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.4 | 12.3 | 13.7 | 0.5 | 0.422x | 1.045x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 15.6 | 15.5 | 16.8 | 0.5 | 0.528x | 1.307x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.3 | 28.9 | 34.2 | 2.1 | 0.991x | 2.455x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.5 | 29.2 | 29.7 | 0.2 | 1.000x | 2.477x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 247.4 | 224.7 | 268.2 | 13.8 | 8.380x | 20.757x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 262.5 | 250.8 | 272.2 | 7.2 | 8.891x | 22.022x |

### `orig` / `s-081` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 4.6 | 4.5 | 5.3 | 0.3 | 0.151x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 4.8 | 4.7 | 4.9 | 0.1 | 0.157x | 1.037x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 4.9 | 4.4 | 5.5 | 0.4 | 0.160x | 1.058x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 4.9 | 4.7 | 4.9 | 0.1 | 0.160x | 1.062x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 17.2 | 17.1 | 18.9 | 0.7 | 0.565x | 3.743x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.4 | 30.1 | 31.3 | 0.4 | 1.000x | 6.621x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 37.4 | 37.1 | 38.0 | 0.3 | 1.232x | 8.157x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 209.2 | 204.4 | 235.5 | 11.5 | 6.887x | 45.600x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 247.9 | 239.0 | 271.2 | 12.3 | 8.163x | 54.046x |

### `orig` / `s-082` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.0 | 12.7 | 15.4 | 1.0 | 0.438x | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.1 | 13.0 | 13.3 | 0.1 | 0.440x | 1.005x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.4 | 13.0 | 15.8 | 1.0 | 0.451x | 1.031x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.5 | 12.8 | 14.8 | 0.7 | 0.453x | 1.035x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 16.4 | 16.3 | 18.7 | 0.9 | 0.552x | 1.260x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.5 | 29.3 | 31.5 | 0.9 | 0.992x | 2.266x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.8 | 29.4 | 30.2 | 0.3 | 1.000x | 2.283x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 248.7 | 229.0 | 268.5 | 12.5 | 8.360x | 19.089x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 263.1 | 251.1 | 271.3 | 6.9 | 8.844x | 20.193x |

### `orig` / `s-082` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 5.1 | 5.1 | 6.8 | 0.7 | 0.163x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 5.1 | 5.0 | 6.2 | 0.4 | 0.165x | 1.013x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 5.3 | 5.3 | 5.7 | 0.2 | 0.171x | 1.047x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 5.6 | 5.3 | 6.7 | 0.5 | 0.180x | 1.104x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 24.0 | 23.9 | 26.9 | 1.1 | 0.772x | 4.729x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 31.1 | 31.0 | 31.5 | 0.2 | 1.000x | 6.129x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 40.1 | 38.8 | 40.6 | 0.6 | 1.287x | 7.886x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 245.4 | 217.0 | 261.2 | 16.5 | 7.881x | 48.305x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 261.6 | 239.0 | 298.0 | 22.9 | 8.403x | 51.500x |

### `orig` / `s-083` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.5 | 22.6 | 0.4 | 0.597x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 36.1 | 35.7 | 37.5 | 0.7 | 1.000x | 1.676x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 36.9 | 35.0 | 38.1 | 1.2 | 1.021x | 1.711x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 138.0 | 137.6 | 138.2 | 0.2 | 3.819x | 6.400x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 138.2 | 137.9 | 138.7 | 0.3 | 3.825x | 6.410x |
| 6 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 138.4 | 138.1 | 158.1 | 7.8 | 3.831x | 6.421x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 138.5 | 138.2 | 139.1 | 0.4 | 3.835x | 6.427x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 244.7 | 240.3 | 248.0 | 2.5 | 6.775x | 11.354x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 272.3 | 257.7 | 282.2 | 7.8 | 7.539x | 12.634x |

### `orig` / `s-083` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 35.8 | 35.6 | 36.4 | 0.4 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 40.3 | 39.9 | 44.7 | 1.8 | 1.127x | 1.127x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 132.0 | 131.8 | 132.6 | 0.3 | 3.689x | 3.689x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 132.1 | 132.0 | 134.3 | 1.0 | 3.693x | 3.693x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 132.2 | 132.1 | 132.5 | 0.1 | 3.696x | 3.696x |
| 6 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 132.4 | 132.3 | 133.7 | 0.5 | 3.701x | 3.701x |
| 7 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 616.6 | 613.7 | 630.9 | 6.1 | 17.237x | 17.237x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 839.0 | 809.0 | 845.9 | 13.6 | 23.455x | 23.455x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 863.7 | 841.5 | 868.4 | 12.1 | 24.146x | 24.146x |

### `orig` / `s-084` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 22.9 | 24.4 | 0.6 | 0.652x | 1.000x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 30.1 | 30.1 | 30.9 | 0.3 | 0.851x | 1.307x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 30.3 | 30.3 | 31.2 | 0.4 | 0.857x | 1.315x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 30.3 | 30.1 | 31.3 | 0.4 | 0.857x | 1.315x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 30.4 | 30.2 | 30.5 | 0.1 | 0.859x | 1.318x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 35.4 | 35.3 | 35.8 | 0.2 | 1.000x | 1.535x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 35.4 | 34.0 | 37.1 | 1.0 | 1.000x | 1.535x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 237.2 | 225.7 | 246.4 | 6.7 | 6.700x | 10.283x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 260.4 | 233.4 | 264.2 | 11.5 | 7.355x | 11.289x |

### `orig` / `s-084` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 24.9 | 24.9 | 27.0 | 0.8 | 0.711x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 25.0 | 24.9 | 26.6 | 0.6 | 0.714x | 1.004x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 25.3 | 25.2 | 25.8 | 0.2 | 0.722x | 1.015x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 25.3 | 25.2 | 25.8 | 0.2 | 0.723x | 1.017x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 35.0 | 34.8 | 35.7 | 0.3 | 1.000x | 1.406x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 39.5 | 39.1 | 40.7 | 0.5 | 1.129x | 1.588x |
| 7 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 125.0 | 124.2 | 126.9 | 0.9 | 3.572x | 5.021x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 328.6 | 325.1 | 353.0 | 10.5 | 9.387x | 13.197x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 353.9 | 350.0 | 375.6 | 9.4 | 10.110x | 14.213x |

### `orig` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,716,942.6 | 3,676,996.1 | 3,962,741.4 | 105,028.8 | 0.129x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 5,514,810.0 | 5,497,894.8 | 5,886,715.0 | 151,500.9 | 0.192x | 1.484x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 6,541,863.4 | 6,539,115.4 | 6,572,639.6 | 12,638.2 | 0.228x | 1.760x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 6,542,380.1 | 6,533,295.3 | 6,549,917.4 | 5,888.6 | 0.228x | 1.760x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 6,546,166.5 | 6,539,666.5 | 6,727,763.7 | 72,449.7 | 0.228x | 1.761x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 6,546,199.3 | 6,535,898.5 | 6,599,885.0 | 23,271.6 | 0.228x | 1.761x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 12,112,463.0 | 11,459,356.0 | 13,238,110.3 | 652,907.4 | 0.422x | 3.259x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 12,594,527.0 | 11,540,583.2 | 12,999,718.2 | 513,274.6 | 0.438x | 3.388x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28,731,331.9 | 28,603,066.0 | 29,052,861.7 | 149,674.6 | 1.000x | 7.730x |

### `orig` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,769.8 | 17,708.5 | 17,783.9 | 26.2 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,570,591.8 | 2,567,361.8 | 2,586,428.6 | 7,774.1 | 144.661x | 144.661x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 3,421,147.7 | 3,420,171.1 | 3,427,300.4 | 3,287.9 | 192.526x | 192.526x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 3,422,728.9 | 3,417,862.9 | 3,433,973.0 | 5,935.9 | 192.615x | 192.615x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 3,428,525.6 | 3,418,886.9 | 3,463,530.5 | 15,999.0 | 192.941x | 192.941x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 3,433,874.3 | 3,419,820.9 | 3,458,171.2 | 14,923.8 | 193.242x | 193.242x |
| 7 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 16,029,994.2 | 15,803,482.8 | 16,746,954.0 | 323,159.8 | 902.091x | 902.091x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 16,153,819.5 | 15,986,018.8 | 16,494,018.2 | 181,111.1 | 909.059x | 909.059x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 16,968,804.0 | 16,819,943.0 | 17,133,175.0 | 99,216.8 | 954.923x | 954.923x |

### `orig` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,698.8 | 17,678.3 | 18,149.8 | 177.8 | 1.000x | 1.000x | 5 | 100% |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,830,238.0 | 2,828,751.3 | 2,842,780.3 | 5,188.6 | 159.911x | 159.911x | 5 | 100% |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | measured | `plain` | same program | 3,419,119.1 | 3,413,361.7 | 3,436,569.1 | 8,266.1 | 193.183x | 193.183x | 5 | 100% |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | measured | `plain` | same program | 3,419,393.6 | 3,415,914.2 | 3,434,266.3 | 6,378.6 | 193.199x | 193.199x | 5 | 100% |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 3,422,799.6 | 3,414,990.9 | 3,436,319.7 | 8,063.5 | 193.391x | 193.391x | 5 | 100% |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 3,424,102.3 | 3,415,649.6 | 3,511,766.2 | 35,973.8 | 193.465x | 193.465x | 5 | 100% |

## Excluded from ranking (expectation-failing cells)

| pattern | subject | regime | form | testee | n | pass-rate | gave-up | wrong | outcomes |
|---|---|---|---|---|---|---|---|---|---|
| `factored` | `s-058` | `match-compliance` | `whole-subject` | `pcrec_692c2e8_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-058` | `match-compliance` | `whole-subject` | `pcrec_8da6120_auto-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-058` | `match-compliance` | `whole-subject` | `pcrec_8da6120_auto-nocaps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-058` | `match-compliance` | `whole-subject` | `pcrec_8da6120_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-059` | `match-compliance` | `whole-subject` | `pcrec_692c2e8_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-059` | `match-compliance` | `whole-subject` | `pcrec_8da6120_auto-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-059` | `match-compliance` | `whole-subject` | `pcrec_8da6120_auto-nocaps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-059` | `match-compliance` | `whole-subject` | `pcrec_8da6120_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-061` | `match-compliance` | `whole-subject` | `pcrec_692c2e8_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-061` | `match-compliance` | `whole-subject` | `pcrec_8da6120_auto-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-061` | `match-compliance` | `whole-subject` | `pcrec_8da6120_auto-nocaps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-061` | `match-compliance` | `whole-subject` | `pcrec_8da6120_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-063` | `match-compliance` | `whole-subject` | `pcrec_692c2e8_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-063` | `match-compliance` | `whole-subject` | `pcrec_8da6120_auto-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-063` | `match-compliance` | `whole-subject` | `pcrec_8da6120_auto-nocaps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-063` | `match-compliance` | `whole-subject` | `pcrec_8da6120_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-064` | `match-compliance` | `whole-subject` | `pcrec_692c2e8_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-064` | `match-compliance` | `whole-subject` | `pcrec_8da6120_auto-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-064` | `match-compliance` | `whole-subject` | `pcrec_8da6120_auto-nocaps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-064` | `match-compliance` | `whole-subject` | `pcrec_8da6120_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 5 | 0% | 0 | 0 | timed-out=5 |
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_692c2e8_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_692c2e8_vm-in-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_8da6120_auto-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_8da6120_auto-nocaps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_8da6120_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `orig` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_692c2e8_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `orig` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_692c2e8_vm-in-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `orig` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_8da6120_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |

## Compile cost (by execution-model class; never pooled across classes)

### `compiled-aot`

- `pcrec_692c2e8_auto-caps-simdna`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: n/s (pcrec abi 3, before the DFA stamps landed at abi 4), rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
    - (identical on all 4 (pattern, form) cells of this testee)
- `pcrec_692c2e8_auto-nocaps-simdna`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: n/s (pcrec abi 3, before the DFA stamps landed at abi 4), rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
    - (identical on all 4 (pattern, form) cells of this testee)
- `pcrec_692c2e8_vm-caps-simdna`: engine=vm, entry=plain entry, vm_prefilter=none, dfa: n/s (pcrec abi 3, before the DFA stamps landed at abi 4), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, fast tier=n/a (pcrec abi 3: no tier existed before abi 5), buffers=2048/3072 (stamped default), frame=24
    - (identical on all 4 (pattern, form) cells of this testee)
- `pcrec_692c2e8_vm-in-caps-simdna`: engine=vm, entry=_in, vm_prefilter=none, dfa: n/s (pcrec abi 3, before the DFA stamps landed at abi 4), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, fast tier=n/a (pcrec abi 3: no tier existed before abi 5), buffers=32768/131072 (caller-provided), frame=24
    - (identical on all 4 (pattern, form) cells of this testee)
- `pcrec_8da6120_auto-caps-simdna` / `factored` / `plain`: engine=vm, entry=plain entry, vm_prefilter=none, dfa: n/s (pcrec abi 2, before the DFA stamps landed at abi 4), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, fast tier=n/a (pcrec abi 2: no tier existed before abi 5), buffers=n/s, frame=n/s
- `pcrec_8da6120_auto-caps-simdna` / `factored` / `whole-subject`: engine=vm, entry=plain entry, vm_prefilter=none, dfa: n/s (pcrec abi 2, before the DFA stamps landed at abi 4), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, fast tier=n/a (pcrec abi 2: no tier existed before abi 5), buffers=n/s, frame=n/s
- `pcrec_8da6120_auto-caps-simdna` / `orig` / `plain`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: n/s (pcrec abi 2, before the DFA stamps landed at abi 4), rungs=-, fast tier=n/a (DFA: no tier), buffers=n/s, frame=n/s
- `pcrec_8da6120_auto-caps-simdna` / `orig` / `whole-subject`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: n/s (pcrec abi 2, before the DFA stamps landed at abi 4), rungs=-, fast tier=n/a (DFA: no tier), buffers=n/s, frame=n/s
- `pcrec_8da6120_auto-nocaps-simdna` / `factored` / `plain`: engine=vm, entry=plain entry, vm_prefilter=none, dfa: n/s (pcrec abi 2, before the DFA stamps landed at abi 4), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, fast tier=n/a (pcrec abi 2: no tier existed before abi 5), buffers=n/s, frame=n/s
- `pcrec_8da6120_auto-nocaps-simdna` / `factored` / `whole-subject`: engine=vm, entry=plain entry, vm_prefilter=none, dfa: n/s (pcrec abi 2, before the DFA stamps landed at abi 4), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, fast tier=n/a (pcrec abi 2: no tier existed before abi 5), buffers=n/s, frame=n/s
- `pcrec_8da6120_auto-nocaps-simdna` / `orig` / `plain`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: n/s (pcrec abi 2, before the DFA stamps landed at abi 4), rungs=-, fast tier=n/a (DFA: no tier), buffers=n/s, frame=n/s
- `pcrec_8da6120_auto-nocaps-simdna` / `orig` / `whole-subject`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: n/s (pcrec abi 2, before the DFA stamps landed at abi 4), rungs=-, fast tier=n/a (DFA: no tier), buffers=n/s, frame=n/s
- `pcrec_8da6120_vm-caps-simdna`: engine=vm, entry=plain entry, vm_prefilter=none, dfa: n/s (pcrec abi 2, before the DFA stamps landed at abi 4), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, fast tier=n/a (pcrec abi 2: no tier existed before abi 5), buffers=n/s, frame=n/s
    - (identical on all 4 (pattern, form) cells of this testee)

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes | emit-c ns | gcc ns | load ns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `pcrec_692c2e8_auto-caps-simdna` | 142,807,131.0 | 139,685,262.0 | 150,876,967.0 | 3,735,406.7 | 5 | 29,744 | 0.026 | compiled=5 | 7,857,473.0 | 134,841,708.0 | 204,181.0 |
| `factored` | `whole-subject` | `pcrec_692c2e8_auto-caps-simdna` | 149,988,921.0 | 135,107,620.0 | 165,256,163.0 | 9,876,531.6 | 5 | 33,928 | 0.066 (max is trial 1) | compiled=5 | 9,990,487.0 | 139,767,912.0 | 176,401.0 |
| `factored` | `plain` | `pcrec_692c2e8_auto-nocaps-simdna` | 135,540,698.0 | 123,865,500.0 | 143,299,140.0 | 6,749,928.0 | 5 | 29,744 | 0.050 (max is trial 1) | compiled=5 | 9,481,694.0 | 124,395,424.0 | 189,771.0 |
| `factored` | `whole-subject` | `pcrec_692c2e8_auto-nocaps-simdna` | 143,875,264.0 | 137,191,200.0 | 153,344,718.0 | 6,267,042.3 | 5 | 33,928 | 0.044 | compiled=5 | 9,966,287.0 | 133,033,592.0 | 169,271.0 |
| `factored` | `plain` | `pcrec_692c2e8_vm-caps-simdna` | 535,765,380.0 | 526,468,518.0 | 537,513,576.0 | 4,046,565.0 | 5 | 29,776 | 0.008 | compiled=5 | 2,136,698.0 | 532,659,209.0 | 99,420.0 |
| `factored` | `whole-subject` | `pcrec_692c2e8_vm-caps-simdna` | 538,961,373.0 | 537,787,867.0 | 542,941,905.0 | 1,841,075.2 | 5 | 29,776 | 0.003 | compiled=5 | 2,024,237.0 | 536,246,952.0 | 108,041.0 |
| `factored` | `plain` | `pcrec_692c2e8_vm-in-caps-simdna` | 533,212,035.0 | 528,952,948.0 | 535,271,359.0 | 2,613,095.7 | 5 | 29,776 | 0.005 | compiled=5 | 2,036,853.0 | 529,840,444.0 | 108,041.0 |
| `factored` | `whole-subject` | `pcrec_692c2e8_vm-in-caps-simdna` | 542,331,633.0 | 530,896,401.0 | 545,425,863.0 | 5,487,425.3 | 5 | 29,776 | 0.010 | compiled=5 | 2,076,533.0 | 539,578,846.0 | 115,011.0 |
| `factored` | `plain` | `pcrec_8da6120_auto-caps-simdna` | 420,465,289.0 | 414,985,073.0 | 428,903,342.0 | 4,893,507.9 | 5 | 25,128 | 0.012 (max is trial 1) | compiled=5 | 1,880,342.0 | 418,531,336.0 | 110,891.0 |
| `factored` | `whole-subject` | `pcrec_8da6120_auto-caps-simdna` | 430,387,601.0 | 417,874,860.0 | 443,938,027.0 | 8,743,376.0 | 5 | 25,128 | 0.020 | compiled=5 | 1,903,072.0 | 428,382,468.0 | 199,551.0 |
| `factored` | `plain` | `pcrec_8da6120_auto-nocaps-simdna` | 427,493,516.0 | 422,008,523.0 | 434,926,485.0 | 4,492,879.1 | 5 | 25,128 | 0.011 | compiled=5 | 3,458,012.0 | 423,761,643.0 | 190,832.0 |
| `factored` | `whole-subject` | `pcrec_8da6120_auto-nocaps-simdna` | 420,974,905.0 | 413,095,565.0 | 432,864,330.0 | 7,311,852.8 | 5 | 25,128 | 0.017 | compiled=5 | 1,773,151.0 | 419,081,683.0 | 189,551.0 |
| `factored` | `plain` | `pcrec_8da6120_vm-caps-simdna` | 424,762,944.0 | 423,664,078.0 | 432,708,304.0 | 3,362,545.9 | 5 | 25,128 | 0.008 | compiled=5 | 1,716,071.0 | 422,822,902.0 | 193,901.0 |
| `factored` | `whole-subject` | `pcrec_8da6120_vm-caps-simdna` | 427,987,625.0 | 424,012,201.0 | 439,228,106.0 | 5,642,429.0 | 5 | 25,128 | 0.013 | compiled=5 | 1,699,401.0 | 426,211,414.0 | 190,301.0 |
| `orig` | `plain` | `pcrec_692c2e8_auto-caps-simdna` | 135,961,026.0 | 124,634,780.0 | 158,511,788.0 | 11,404,316.3 | 5 | 29,704 | 0.084 | compiled=5 | 7,764,922.0 | 124,249,427.0 | 189,141.0 |
| `orig` | `whole-subject` | `pcrec_692c2e8_auto-caps-simdna` | 143,586,237.0 | 136,043,026.0 | 153,833,077.0 | 6,389,203.0 | 5 | 33,888 | 0.044 (max is trial 1) | compiled=5 | 9,405,903.0 | 127,932,222.0 | 195,571.0 |
| `orig` | `plain` | `pcrec_692c2e8_auto-nocaps-simdna` | 135,528,237.0 | 125,544,052.0 | 139,877,347.0 | 5,078,626.5 | 5 | 29,704 | 0.037 (max is trial 1) | compiled=5 | 7,857,602.0 | 124,941,538.0 | 101,821.0 |
| `orig` | `whole-subject` | `pcrec_692c2e8_auto-nocaps-simdna` | 138,953,371.0 | 131,250,210.0 | 148,817,548.0 | 6,791,912.1 | 5 | 33,888 | 0.049 | compiled=5 | 9,635,665.0 | 126,301,027.0 | 96,901.0 |
| `orig` | `plain` | `pcrec_692c2e8_vm-caps-simdna` | 406,687,295.0 | 398,252,896.0 | 413,024,068.0 | 5,798,706.7 | 5 | 25,592 | 0.014 | compiled=5 | 1,943,277.0 | 401,723,407.0 | 195,001.0 |
| `orig` | `whole-subject` | `pcrec_692c2e8_vm-caps-simdna` | 404,607,847.0 | 391,192,410.0 | 416,889,170.0 | 8,332,820.0 | 5 | 25,592 | 0.021 | compiled=5 | 1,846,257.0 | 402,667,491.0 | 102,910.0 |
| `orig` | `plain` | `pcrec_692c2e8_vm-in-caps-simdna` | 406,593,912.0 | 392,519,313.0 | 419,969,716.0 | 9,292,650.8 | 5 | 25,592 | 0.023 | compiled=5 | 1,944,632.0 | 404,648,530.0 | 100,580.0 |
| `orig` | `whole-subject` | `pcrec_692c2e8_vm-in-caps-simdna` | 401,511,589.0 | 398,264,420.0 | 408,501,273.0 | 3,919,558.6 | 5 | 25,592 | 0.010 | compiled=5 | 2,046,133.0 | 399,354,875.0 | 110,581.0 |
| `orig` | `plain` | `pcrec_8da6120_auto-caps-simdna` | 118,056,825.0 | 103,621,896.0 | 120,772,314.0 | 6,366,891.3 | 5 | 29,232 | 0.054 | compiled=5 | 7,414,687.0 | 110,543,728.0 | 98,410.0 |
| `orig` | `whole-subject` | `pcrec_8da6120_auto-caps-simdna` | 117,555,053.0 | 109,696,744.0 | 130,533,016.0 | 9,212,004.5 | 5 | 33,424 | 0.078 | compiled=5 | 9,605,031.0 | 107,535,020.0 | 194,121.0 |
| `orig` | `plain` | `pcrec_8da6120_auto-nocaps-simdna` | 113,739,182.0 | 110,959,754.0 | 143,108,420.0 | 11,988,842.7 | 5 | 29,232 | 0.105 | compiled=5 | 7,620,208.0 | 106,465,166.0 | 107,390.0 |
| `orig` | `whole-subject` | `pcrec_8da6120_auto-nocaps-simdna` | 135,300,201.0 | 122,043,665.0 | 137,739,956.0 | 6,730,911.2 | 5 | 33,424 | 0.050 (max is trial 1) | compiled=5 | 19,767,436.0 | 115,433,954.0 | 101,750.0 |
| `orig` | `plain` | `pcrec_8da6120_vm-caps-simdna` | 382,875,770.0 | 372,878,556.0 | 389,967,264.0 | 6,557,411.6 | 5 | 25,088 | 0.017 | compiled=5 | 1,976,132.0 | 380,961,488.0 | 196,851.0 |
| `orig` | `whole-subject` | `pcrec_8da6120_vm-caps-simdna` | 374,587,618.0 | 362,494,710.0 | 389,369,562.0 | 9,692,150.1 | 5 | 25,088 | 0.026 | compiled=5 | 2,358,745.0 | 372,141,432.0 | 101,580.0 |

### `eager-jit`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 68,951.0 | 62,961.0 | 164,202.0 | 38,343.6 | 5 | 951 | 0.556 (max is trial 1) | compiled=5 |
| `orig` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 148,341.0 | 133,921.0 | 384,633.0 | 95,697.6 | 5 | 1,609 | 0.645 (max is trial 1) | compiled=5 |

### `interpretive`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 14,590.0 | 13,061.0 | 45,140.0 | 12,302.5 | 5 | 951 | timer-floor (max is trial 1) | compiled=5 |
| `orig` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 13,550.0 | 12,290.0 | 44,861.0 | 12,584.5 | 5 | 1,609 | timer-floor (max is trial 1) | compiled=5 |

