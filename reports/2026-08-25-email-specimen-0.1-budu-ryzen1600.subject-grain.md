# pcrec-bench report

reporter: v3 (2026-08-25)

## Query

- filters: subbench=email-specimen, until=2026-08-25T07:00:00Z
- record source: store/index.tsv (14 candidate file(s))
- records included: 5
    - `email-specimen@0.1__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260825T062213Z` (store/records/email-specimen@0.1/libpcre2_10.46_interp-caps-simdna/email-specimen@0.1__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260825T062213Z.jsonl)
    - `email-specimen@0.1__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260825T062944Z` (store/records/email-specimen@0.1/libpcre2_10.46_jit-caps-simdna/email-specimen@0.1__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260825T062944Z.jsonl)
    - `email-specimen@0.1__pcrec_8da6120_auto-caps-simdna__budu-ryzen1600__20260825T065046Z` (store/records/email-specimen@0.1/pcrec_8da6120_auto-caps-simdna/email-specimen@0.1__pcrec_8da6120_auto-caps-simdna__budu-ryzen1600__20260825T065046Z.jsonl)
    - `email-specimen@0.1__pcrec_8da6120_auto-nocaps-simdna__budu-ryzen1600__20260825T063943Z` (store/records/email-specimen@0.1/pcrec_8da6120_auto-nocaps-simdna/email-specimen@0.1__pcrec_8da6120_auto-nocaps-simdna__budu-ryzen1600__20260825T063943Z.jsonl)
    - `email-specimen@0.1__pcrec_8da6120_vm-caps-simdna__budu-ryzen1600__20260825T064436Z` (store/records/email-specimen@0.1/pcrec_8da6120_vm-caps-simdna/email-specimen@0.1__pcrec_8da6120_vm-caps-simdna__budu-ryzen1600__20260825T064436Z.jsonl)
- sub-bench version(s): email-specimen@0.1
- machine(s): budu-ryzen1600
- schema version(s): 1.1
- grain: subject (per pattern x subject x regime; the drill-down)
- reduction: median/min/max/stddev (population) over per-trial `elapsed_ns / iterations`; lazy-JIT compile cost is DERIVED as first-match-row-minus-steady-state (lowest `seq` timed row for the pattern, minus the median of every other timed row), one value per (pattern, testee), never pooled with another execution-model class's compile cost
- `form`: this report includes a `whole-subject` artifact beside `plain` for at least one cell (schema v1.1: a testee with no end-anchored mode compiles and times a SEPARATE artifact for match-compliance, e.g. `(?:pattern)\z`, where another testee reaches the same regime via runtime flags on its ordinary artifact) -- shown as a per-row COLUMN, not a split: both forms answer the same regime and RANK TOGETHER in one table (`form` is a key only for compile-cost rows, where a whole-subject artifact is genuinely a separate compile with its own cost); `fact` restates it as 'same program' / 'separate artifact' (R4)
- status policy (OD-B14): a ranking row whose record `status` is not `measured` is excluded from ranking by default, listed under its table as `not ranked: <testee> -- <status> (<status_detail excerpt>)`; `--include-unmeasured` ranks it instead, with `status` shown
- tier policy (R3, schema v1.2 `tier`, absent = `pinned`): a `scratch`-tier row is excluded from ranking by default, listed as `scratch: <testee>`; `--include-scratch` ranks it instead, with a `tier` column
- duplicate-record policy (OD-B15, amended 2026-08-25): the NEWEST MEASURED record per (subbench@version, testee_id, machine) ranks by default -- a newer record that is NOT measured does not supersede a measured one of the same testee and version (listed as "newer, not measured" instead); only when no record in the group is measured does the newest record overall stand (itself unranked per the status policy above, unless --include-unmeasured). `--all-records` shows every record as its own row, its testee id suffixed `@<timestamp>`

## Ranking (per pattern x subject x regime; best median first)

### `factored` / `s-000` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 466.9 | 421.0 | 495.7 | 25.2 | 0.537x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 490.2 | 483.1 | 536.9 | 20.1 | 0.563x | 1.050x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 500.9 | 494.5 | 502.4 | 3.0 | 0.576x | 1.073x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 870.0 | 862.1 | 878.4 | 6.0 | 1.000x | 1.863x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 870.9 | 859.8 | 888.2 | 9.7 | 1.001x | 1.865x |

### `factored` / `s-000` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 154.8 | 154.2 | 156.5 | 0.9 | 0.180x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 430.7 | 416.6 | 504.6 | 31.6 | 0.500x | 2.783x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 464.5 | 445.4 | 495.6 | 17.8 | 0.539x | 3.001x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 467.6 | 450.4 | 488.3 | 13.3 | 0.543x | 3.021x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 861.1 | 856.8 | 878.9 | 8.1 | 1.000x | 5.563x |

### `factored` / `s-001` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 506.6 | 493.4 | 538.1 | 15.3 | 0.412x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 584.4 | 572.0 | 619.1 | 16.2 | 0.475x | 1.154x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 600.3 | 562.6 | 692.0 | 46.5 | 0.488x | 1.185x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,228.5 | 1,220.9 | 1,232.7 | 4.7 | 0.998x | 2.425x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,230.3 | 1,222.3 | 1,234.8 | 4.8 | 1.000x | 2.428x |

### `factored` / `s-001` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 175.8 | 175.5 | 177.3 | 0.8 | 0.143x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 520.6 | 492.6 | 536.5 | 19.3 | 0.424x | 2.961x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 551.7 | 511.9 | 579.7 | 29.3 | 0.449x | 3.138x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 563.7 | 533.3 | 597.8 | 26.8 | 0.459x | 3.207x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,228.7 | 1,220.2 | 1,256.0 | 13.4 | 1.000x | 6.989x |

### `factored` / `s-002` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 430.1 | 380.9 | 443.6 | 22.1 | 0.567x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 431.3 | 408.0 | 454.4 | 17.8 | 0.569x | 1.003x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 452.3 | 402.1 | 485.4 | 31.1 | 0.597x | 1.052x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 757.9 | 742.3 | 759.8 | 7.2 | 1.000x | 1.762x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 758.3 | 746.0 | 768.9 | 7.9 | 1.000x | 1.763x |

### `factored` / `s-002` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 122.5 | 120.8 | 125.7 | 1.6 | 0.161x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 350.0 | 299.7 | 478.7 | 64.0 | 0.461x | 2.858x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 375.7 | 371.4 | 488.0 | 48.1 | 0.495x | 3.068x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 390.2 | 355.6 | 453.4 | 33.1 | 0.514x | 3.186x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 759.6 | 744.8 | 776.2 | 10.1 | 1.000x | 6.202x |

### `factored` / `s-003` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 590.8 | 545.4 | 621.1 | 27.6 | 0.446x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 652.5 | 596.4 | 727.2 | 43.3 | 0.493x | 1.104x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 660.6 | 595.4 | 709.3 | 47.2 | 0.499x | 1.118x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,323.4 | 1,322.1 | 1,348.5 | 10.0 | 1.000x | 2.240x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,328.9 | 1,315.7 | 1,334.1 | 7.3 | 1.004x | 2.249x |

### `factored` / `s-003` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 185.5 | 183.6 | 187.4 | 1.4 | 0.138x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 566.9 | 558.6 | 680.0 | 46.1 | 0.422x | 3.057x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 581.7 | 557.8 | 636.4 | 27.8 | 0.433x | 3.137x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 626.4 | 601.0 | 665.6 | 22.0 | 0.466x | 3.378x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,344.9 | 1,332.0 | 1,440.4 | 41.0 | 1.000x | 7.251x |

### `factored` / `s-004` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 529.9 | 476.0 | 572.3 | 34.4 | 0.601x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 572.3 | 517.2 | 584.7 | 27.5 | 0.650x | 1.080x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 611.8 | 531.7 | 657.6 | 46.0 | 0.695x | 1.155x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 879.4 | 878.5 | 889.1 | 3.9 | 0.998x | 1.660x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 881.0 | 875.5 | 898.3 | 9.3 | 1.000x | 1.663x |

### `factored` / `s-004` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 168.5 | 167.0 | 169.2 | 0.9 | 0.191x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 508.5 | 458.7 | 540.8 | 31.9 | 0.576x | 3.019x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 511.9 | 467.4 | 559.7 | 31.3 | 0.580x | 3.038x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 544.3 | 524.8 | 550.2 | 10.3 | 0.617x | 3.231x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 882.5 | 861.9 | 899.0 | 13.6 | 1.000x | 5.238x |

### `factored` / `s-005` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 429.2 | 380.7 | 544.8 | 55.3 | 0.572x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 451.3 | 416.5 | 483.3 | 24.7 | 0.602x | 1.052x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 453.9 | 404.4 | 469.4 | 22.6 | 0.605x | 1.058x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 747.1 | 744.8 | 764.2 | 7.1 | 0.996x | 1.741x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 750.3 | 743.5 | 756.6 | 4.9 | 1.000x | 1.748x |

### `factored` / `s-005` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 123.6 | 121.9 | 126.1 | 1.5 | 0.163x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 384.6 | 316.6 | 486.6 | 54.4 | 0.506x | 3.112x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 398.4 | 358.1 | 585.4 | 82.4 | 0.524x | 3.223x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 413.5 | 346.1 | 452.2 | 36.5 | 0.544x | 3.346x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 760.3 | 742.3 | 775.1 | 13.2 | 1.000x | 6.152x |

### `factored` / `s-006` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 610.4 | 599.5 | 768.3 | 64.3 | 0.453x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 643.7 | 620.7 | 699.9 | 29.3 | 0.478x | 1.055x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 681.0 | 603.5 | 692.3 | 32.1 | 0.505x | 1.116x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,347.9 | 1,335.0 | 1,367.6 | 10.7 | 1.000x | 2.208x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,353.3 | 1,344.2 | 1,358.3 | 4.6 | 1.004x | 2.217x |

### `factored` / `s-006` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 166.0 | 165.1 | 168.6 | 1.2 | 0.123x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 603.5 | 597.0 | 676.6 | 36.1 | 0.449x | 3.636x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 618.0 | 585.7 | 699.6 | 37.9 | 0.459x | 3.723x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 671.0 | 665.0 | 695.0 | 12.3 | 0.499x | 4.043x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,345.0 | 1,332.7 | 1,372.3 | 13.4 | 1.000x | 8.104x |

### `factored` / `s-007` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 517.4 | 491.2 | 596.9 | 36.0 | 0.533x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 582.5 | 531.6 | 641.0 | 35.6 | 0.600x | 1.126x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 609.1 | 544.9 | 655.3 | 42.1 | 0.627x | 1.177x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 971.2 | 952.5 | 978.3 | 8.9 | 1.000x | 1.877x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 972.5 | 962.8 | 975.6 | 4.3 | 1.001x | 1.880x |

### `factored` / `s-007` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 171.6 | 170.9 | 198.5 | 10.8 | 0.174x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 512.1 | 492.5 | 573.0 | 30.3 | 0.519x | 2.984x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 567.2 | 546.3 | 586.4 | 14.4 | 0.574x | 3.305x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 576.3 | 496.7 | 595.9 | 41.2 | 0.584x | 3.358x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 987.5 | 985.4 | 997.8 | 4.5 | 1.000x | 5.754x |

### `factored` / `s-008` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 512.8 | 495.3 | 524.7 | 11.8 | 0.592x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 570.0 | 494.9 | 615.3 | 40.3 | 0.658x | 1.112x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 602.6 | 525.3 | 629.6 | 35.5 | 0.696x | 1.175x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 865.7 | 860.7 | 872.0 | 4.3 | 1.000x | 1.688x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 866.5 | 862.6 | 869.7 | 2.3 | 1.001x | 1.690x |

### `factored` / `s-008` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 158.0 | 157.6 | 165.6 | 3.2 | 0.181x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 486.7 | 461.1 | 548.0 | 29.5 | 0.558x | 3.080x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 499.0 | 440.8 | 545.0 | 39.9 | 0.572x | 3.158x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 531.7 | 460.3 | 603.6 | 50.1 | 0.609x | 3.365x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 872.8 | 860.3 | 896.9 | 11.9 | 1.000x | 5.524x |

### `factored` / `s-009` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 484.3 | 472.8 | 535.7 | 27.8 | 0.563x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 557.6 | 496.0 | 607.5 | 38.4 | 0.648x | 1.151x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 582.2 | 541.5 | 597.9 | 21.1 | 0.676x | 1.202x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 859.2 | 858.8 | 862.8 | 1.6 | 0.998x | 1.774x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 860.7 | 847.6 | 873.4 | 9.8 | 1.000x | 1.777x |

### `factored` / `s-009` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 149.9 | 147.3 | 151.4 | 1.6 | 0.170x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 469.9 | 421.4 | 507.0 | 32.2 | 0.533x | 3.134x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 472.8 | 462.0 | 541.1 | 29.7 | 0.536x | 3.154x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 529.4 | 501.8 | 566.8 | 22.6 | 0.600x | 3.531x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 881.8 | 853.9 | 886.0 | 11.7 | 1.000x | 5.882x |

### `factored` / `s-010` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 446.3 | 387.6 | 452.9 | 23.9 | 0.628x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 460.8 | 410.4 | 488.6 | 26.1 | 0.649x | 1.033x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 465.9 | 444.5 | 501.5 | 20.7 | 0.656x | 1.044x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 710.1 | 705.8 | 715.9 | 3.5 | 1.000x | 1.591x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 712.3 | 698.2 | 713.7 | 5.9 | 1.003x | 1.596x |

### `factored` / `s-010` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 118.8 | 118.5 | 120.9 | 1.1 | 0.163x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 388.8 | 361.6 | 476.7 | 40.5 | 0.533x | 3.274x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 417.0 | 340.2 | 472.0 | 44.3 | 0.572x | 3.510x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 428.2 | 406.4 | 516.4 | 38.8 | 0.587x | 3.605x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 729.5 | 712.7 | 731.7 | 8.8 | 1.000x | 6.141x |

### `factored` / `s-011` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 531.0 | 469.5 | 594.4 | 44.2 | 0.857x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 555.3 | 516.0 | 609.9 | 29.9 | 0.896x | 1.046x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 568.9 | 535.2 | 597.2 | 22.3 | 0.918x | 1.071x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 616.2 | 609.4 | 623.4 | 4.5 | 0.994x | 1.160x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 619.8 | 617.9 | 642.2 | 10.1 | 1.000x | 1.167x |

### `factored` / `s-011` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 438.9 | 434.7 | 450.4 | 5.3 | 0.092x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 2,346.9 | 2,332.0 | 2,382.0 | 17.9 | 0.495x | 5.348x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 2,380.1 | 2,342.9 | 2,515.8 | 60.6 | 0.502x | 5.423x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 2,383.6 | 2,352.9 | 2,427.3 | 26.6 | 0.502x | 5.431x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,745.1 | 4,703.2 | 4,804.0 | 33.5 | 1.000x | 10.812x |

### `factored` / `s-012` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 580.5 | 563.8 | 604.2 | 13.2 | 0.523x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 640.8 | 603.9 | 662.7 | 22.2 | 0.577x | 1.104x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 650.6 | 601.5 | 696.0 | 30.1 | 0.586x | 1.121x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,093.5 | 1,080.6 | 1,097.6 | 6.4 | 0.985x | 1.884x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,110.4 | 1,092.4 | 1,119.9 | 10.3 | 1.000x | 1.913x |

### `factored` / `s-012` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 170.4 | 170.0 | 179.2 | 3.6 | 0.154x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 612.3 | 519.2 | 639.6 | 42.7 | 0.552x | 3.594x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 615.4 | 573.0 | 630.7 | 19.7 | 0.555x | 3.612x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 629.0 | 607.1 | 659.4 | 20.2 | 0.567x | 3.692x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,109.6 | 1,095.7 | 1,128.6 | 10.8 | 1.000x | 6.513x |

### `factored` / `s-013` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 602.2 | 554.6 | 609.6 | 20.3 | 0.544x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 619.7 | 594.1 | 649.6 | 20.0 | 0.559x | 1.029x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 647.5 | 605.1 | 716.7 | 37.1 | 0.584x | 1.075x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,095.8 | 1,086.6 | 1,128.0 | 15.1 | 0.989x | 1.820x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,107.9 | 1,075.2 | 1,129.3 | 17.3 | 1.000x | 1.840x |

### `factored` / `s-013` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 170.5 | 170.1 | 179.2 | 3.5 | 0.153x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 604.9 | 430.6 | 636.1 | 73.8 | 0.544x | 3.549x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 610.4 | 569.7 | 661.0 | 32.1 | 0.549x | 3.581x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 622.1 | 602.8 | 651.4 | 16.2 | 0.559x | 3.649x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,112.3 | 1,092.6 | 1,124.6 | 10.9 | 1.000x | 6.526x |

### `factored` / `s-014` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 595.0 | 591.5 | 625.5 | 12.9 | 0.675x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 597.9 | 544.4 | 703.5 | 56.9 | 0.679x | 1.005x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 608.4 | 574.9 | 634.0 | 21.6 | 0.691x | 1.022x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 881.0 | 864.7 | 906.7 | 14.4 | 1.000x | 1.481x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 881.8 | 875.3 | 959.9 | 31.9 | 1.001x | 1.482x |

### `factored` / `s-014` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 155.3 | 154.0 | 158.8 | 1.7 | 0.176x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 517.3 | 497.5 | 575.7 | 27.6 | 0.587x | 3.331x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 523.7 | 502.5 | 563.8 | 20.4 | 0.594x | 3.372x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 547.2 | 531.0 | 629.9 | 35.6 | 0.620x | 3.523x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 881.9 | 875.7 | 894.3 | 6.6 | 1.000x | 5.679x |

### `factored` / `s-015` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 623.6 | 592.9 | 715.3 | 45.2 | 0.580x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 629.7 | 586.1 | 643.4 | 20.6 | 0.586x | 1.010x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 639.8 | 577.5 | 700.2 | 42.0 | 0.596x | 1.026x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,069.5 | 1,059.9 | 1,071.1 | 4.4 | 0.996x | 1.715x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,074.3 | 1,051.5 | 1,086.3 | 13.1 | 1.000x | 1.723x |

### `factored` / `s-015` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 175.7 | 172.3 | 177.8 | 2.1 | 0.165x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 601.7 | 596.6 | 639.3 | 18.7 | 0.566x | 3.424x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 609.7 | 509.9 | 644.2 | 47.3 | 0.574x | 3.469x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 641.3 | 613.6 | 661.5 | 17.4 | 0.604x | 3.649x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,062.4 | 1,052.5 | 1,070.7 | 6.0 | 1.000x | 6.045x |

### `factored` / `s-016` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 361.4 | 359.0 | 370.3 | 4.1 | 0.988x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 365.9 | 358.0 | 377.3 | 7.6 | 1.000x | 1.012x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 450.0 | 420.2 | 506.3 | 29.4 | 1.230x | 1.245x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 467.6 | 453.0 | 511.3 | 22.5 | 1.278x | 1.294x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 479.7 | 424.5 | 532.7 | 39.7 | 1.311x | 1.327x |

### `factored` / `s-016` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 259.9 | 259.2 | 267.4 | 3.1 | 0.107x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,806.7 | 1,778.3 | 1,866.6 | 30.2 | 0.745x | 6.951x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,813.5 | 1,752.2 | 1,835.7 | 34.2 | 0.748x | 6.977x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,829.7 | 1,768.5 | 1,867.0 | 34.1 | 0.755x | 7.040x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,424.0 | 2,393.9 | 2,460.6 | 23.7 | 1.000x | 9.326x |

### `factored` / `s-017` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 597.0 | 548.2 | 657.6 | 39.2 | 0.540x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 615.4 | 566.5 | 726.4 | 62.4 | 0.556x | 1.031x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 648.3 | 610.7 | 698.3 | 31.9 | 0.586x | 1.086x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,095.6 | 1,090.1 | 1,118.6 | 10.6 | 0.990x | 1.835x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,106.1 | 1,091.0 | 1,127.2 | 12.5 | 1.000x | 1.853x |

### `factored` / `s-017` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 170.8 | 170.3 | 173.3 | 1.1 | 0.155x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 576.3 | 545.8 | 654.8 | 41.2 | 0.524x | 3.374x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 614.3 | 592.7 | 638.0 | 16.3 | 0.559x | 3.597x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 643.5 | 590.7 | 700.1 | 36.5 | 0.585x | 3.768x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,099.2 | 1,093.9 | 1,116.2 | 10.0 | 1.000x | 6.436x |

### `factored` / `s-018` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 618.1 | 592.2 | 657.7 | 27.5 | 0.580x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 620.8 | 587.8 | 708.5 | 41.0 | 0.583x | 1.004x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 651.0 | 622.5 | 698.6 | 25.1 | 0.611x | 1.053x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,062.6 | 1,046.4 | 1,067.7 | 7.6 | 0.997x | 1.719x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,065.8 | 1,060.7 | 1,103.3 | 15.5 | 1.000x | 1.724x |

### `factored` / `s-018` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 174.3 | 173.0 | 178.5 | 2.1 | 0.165x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 588.0 | 558.4 | 608.3 | 18.4 | 0.557x | 3.374x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 623.8 | 609.8 | 660.7 | 18.9 | 0.591x | 3.580x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 638.6 | 610.8 | 662.3 | 17.7 | 0.605x | 3.664x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,056.2 | 1,050.8 | 1,073.5 | 8.4 | 1.000x | 6.061x |

### `factored` / `s-019` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 388.9 | 385.2 | 390.9 | 2.4 | 0.993x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 391.5 | 389.0 | 392.4 | 1.2 | 1.000x | 1.007x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 481.4 | 472.2 | 528.3 | 20.0 | 1.230x | 1.238x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 490.3 | 475.9 | 497.3 | 8.7 | 1.252x | 1.261x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 506.0 | 462.8 | 519.1 | 21.4 | 1.292x | 1.301x |

### `factored` / `s-019` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 265.1 | 264.2 | 266.1 | 0.7 | 0.103x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,834.6 | 1,767.6 | 1,853.1 | 30.6 | 0.716x | 6.921x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,856.0 | 1,805.3 | 1,875.9 | 25.1 | 0.724x | 7.002x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,865.9 | 1,816.2 | 1,885.9 | 27.0 | 0.728x | 7.039x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,563.0 | 2,544.4 | 2,622.8 | 26.6 | 1.000x | 9.669x |

### `factored` / `s-020` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 619.6 | 606.8 | 763.4 | 58.8 | 0.553x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 665.6 | 612.3 | 700.1 | 31.2 | 0.594x | 1.074x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 669.1 | 631.5 | 675.1 | 16.6 | 0.597x | 1.080x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,118.8 | 1,103.1 | 1,127.8 | 8.5 | 0.998x | 1.806x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,121.0 | 1,107.4 | 1,173.1 | 23.1 | 1.000x | 1.809x |

### `factored` / `s-020` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 177.4 | 175.3 | 179.0 | 1.5 | 0.159x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 623.3 | 562.9 | 634.5 | 26.2 | 0.557x | 3.514x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 650.8 | 638.1 | 670.9 | 10.6 | 0.582x | 3.668x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 654.1 | 599.2 | 682.5 | 27.6 | 0.585x | 3.687x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,119.1 | 1,109.6 | 1,165.7 | 20.5 | 1.000x | 6.308x |

### `factored` / `s-021` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 573.8 | 555.6 | 624.5 | 23.4 | 0.502x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 587.3 | 502.4 | 627.7 | 41.2 | 0.513x | 1.024x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 589.7 | 587.4 | 643.0 | 21.4 | 0.516x | 1.028x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,143.8 | 1,132.6 | 1,167.0 | 12.4 | 1.000x | 1.993x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,146.2 | 1,130.0 | 1,152.5 | 8.0 | 1.002x | 1.998x |

### `factored` / `s-021` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 110.7 | 109.0 | 113.1 | 1.4 | 0.097x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 579.0 | 549.3 | 615.6 | 24.9 | 0.505x | 5.230x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 590.9 | 574.4 | 612.8 | 14.8 | 0.515x | 5.336x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 603.5 | 560.5 | 682.1 | 44.6 | 0.526x | 5.451x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,147.2 | 1,143.8 | 1,196.9 | 22.1 | 1.000x | 10.362x |

### `factored` / `s-022` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 537.8 | 458.9 | 584.8 | 45.2 | 0.792x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 564.8 | 520.9 | 693.4 | 58.5 | 0.832x | 1.050x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 572.4 | 525.2 | 628.4 | 32.9 | 0.843x | 1.064x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 679.0 | 677.5 | 692.7 | 5.7 | 1.000x | 1.263x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 683.3 | 679.2 | 695.0 | 5.6 | 1.006x | 1.270x |

### `factored` / `s-022` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 99.2 | 98.3 | 106.5 | 3.0 | 0.144x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 530.8 | 480.7 | 583.3 | 34.9 | 0.770x | 5.350x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 538.2 | 516.9 | 640.6 | 43.6 | 0.781x | 5.425x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 548.8 | 493.2 | 585.9 | 32.8 | 0.796x | 5.532x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 689.3 | 678.3 | 708.9 | 10.9 | 1.000x | 6.949x |

### `factored` / `s-023` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 552.4 | 443.6 | 577.8 | 47.0 | 0.487x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 555.0 | 467.7 | 571.8 | 37.9 | 0.490x | 1.005x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 558.7 | 550.1 | 630.6 | 31.3 | 0.493x | 1.011x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,128.4 | 1,126.3 | 1,138.2 | 4.8 | 0.996x | 2.043x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,133.3 | 1,124.5 | 1,173.3 | 17.3 | 1.000x | 2.052x |

### `factored` / `s-023` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 108.1 | 106.6 | 112.4 | 2.3 | 0.095x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 570.7 | 560.1 | 621.0 | 22.0 | 0.501x | 5.279x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 576.8 | 558.3 | 691.1 | 51.8 | 0.506x | 5.335x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 589.0 | 541.4 | 613.1 | 24.1 | 0.517x | 5.447x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,138.9 | 1,121.7 | 1,201.5 | 29.3 | 1.000x | 10.534x |

### `factored` / `s-024` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 512.9 | 466.1 | 545.4 | 28.4 | 0.448x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 546.5 | 512.8 | 605.9 | 36.6 | 0.477x | 1.066x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 560.5 | 504.1 | 594.4 | 29.7 | 0.489x | 1.093x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,145.3 | 1,138.9 | 1,156.9 | 5.9 | 1.000x | 2.233x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,148.6 | 1,139.1 | 1,167.6 | 9.5 | 1.003x | 2.240x |

### `factored` / `s-024` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 108.9 | 108.4 | 110.6 | 0.7 | 0.093x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 590.9 | 518.2 | 645.9 | 41.9 | 0.503x | 5.425x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 591.3 | 513.3 | 631.4 | 48.7 | 0.504x | 5.428x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 612.6 | 565.1 | 690.5 | 46.0 | 0.522x | 5.624x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,173.8 | 1,150.1 | 1,181.1 | 12.5 | 1.000x | 10.775x |

### `factored` / `s-025` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 486.9 | 432.4 | 528.0 | 35.4 | 0.430x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 526.1 | 455.2 | 655.5 | 65.1 | 0.464x | 1.080x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 529.2 | 486.7 | 539.9 | 21.3 | 0.467x | 1.087x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,132.9 | 1,126.8 | 1,154.0 | 9.2 | 1.000x | 2.327x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,148.1 | 1,126.3 | 1,172.7 | 18.1 | 1.013x | 2.358x |

### `factored` / `s-025` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 106.7 | 106.5 | 108.1 | 0.6 | 0.093x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 562.2 | 499.5 | 618.4 | 42.4 | 0.491x | 5.268x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 581.4 | 524.1 | 658.0 | 48.5 | 0.508x | 5.448x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 585.1 | 561.8 | 643.9 | 32.6 | 0.511x | 5.483x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,145.5 | 1,128.7 | 1,177.2 | 17.5 | 1.000x | 10.733x |

### `factored` / `s-026` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 509.5 | 453.8 | 571.6 | 40.5 | 0.753x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 535.4 | 448.0 | 648.9 | 67.3 | 0.791x | 1.051x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 546.9 | 527.9 | 624.2 | 33.8 | 0.808x | 1.073x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 676.6 | 673.6 | 688.8 | 5.5 | 1.000x | 1.328x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 678.1 | 672.5 | 751.0 | 29.3 | 1.002x | 1.331x |

### `factored` / `s-026` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 98.8 | 98.3 | 100.3 | 0.7 | 0.144x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 530.1 | 509.0 | 601.9 | 34.5 | 0.771x | 5.368x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 552.1 | 525.9 | 582.3 | 18.9 | 0.803x | 5.590x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 562.1 | 522.0 | 615.9 | 35.9 | 0.818x | 5.692x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 687.4 | 675.9 | 694.0 | 6.6 | 1.000x | 6.960x |

### `factored` / `s-027` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 504.7 | 477.0 | 568.0 | 30.5 | 0.470x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 527.4 | 484.3 | 556.5 | 26.6 | 0.491x | 1.045x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 538.0 | 515.0 | 628.3 | 39.8 | 0.501x | 1.066x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,074.2 | 1,056.1 | 1,089.9 | 12.7 | 1.000x | 2.128x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,082.1 | 1,059.0 | 1,093.0 | 14.0 | 1.007x | 2.144x |

### `factored` / `s-027` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 104.2 | 103.9 | 105.4 | 0.5 | 0.096x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 560.5 | 520.8 | 609.5 | 30.4 | 0.514x | 5.381x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 564.4 | 548.6 | 590.6 | 17.5 | 0.518x | 5.418x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 609.1 | 551.0 | 681.8 | 45.6 | 0.559x | 5.847x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,090.2 | 1,070.2 | 1,106.4 | 11.7 | 1.000x | 10.465x |

### `factored` / `s-028` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 554.4 | 542.5 | 581.7 | 15.3 | 0.714x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 555.1 | 534.4 | 604.5 | 23.8 | 0.715x | 1.001x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 572.6 | 555.8 | 622.2 | 22.7 | 0.737x | 1.033x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 776.9 | 772.5 | 816.0 | 16.1 | 1.000x | 1.402x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 777.4 | 770.9 | 787.4 | 6.0 | 1.001x | 1.402x |

### `factored` / `s-028` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 220.0 | 216.4 | 222.3 | 2.6 | 0.082x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,419.9 | 1,409.4 | 1,436.4 | 10.9 | 0.527x | 6.452x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,427.2 | 1,379.3 | 1,448.9 | 23.6 | 0.530x | 6.486x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,429.5 | 1,392.0 | 1,528.8 | 45.9 | 0.530x | 6.496x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,695.2 | 2,680.2 | 2,824.8 | 54.3 | 1.000x | 12.248x |

### `factored` / `s-029` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 553.4 | 540.8 | 592.4 | 20.1 | 0.708x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 553.9 | 531.4 | 563.7 | 13.2 | 0.709x | 1.001x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 564.8 | 555.1 | 613.9 | 20.9 | 0.723x | 1.021x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 779.6 | 775.2 | 792.8 | 6.4 | 0.998x | 1.409x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 781.1 | 774.9 | 789.3 | 5.1 | 1.000x | 1.412x |

### `factored` / `s-029` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 232.1 | 231.4 | 237.5 | 2.2 | 0.086x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,707.1 | 2,668.0 | 2,794.6 | 49.4 | 1.000x | 11.664x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 4,412.9 | 4,402.6 | 4,447.4 | 15.7 | 1.630x | 19.013x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 4,423.8 | 4,355.4 | 4,445.3 | 33.3 | 1.634x | 19.060x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 4,456.4 | 4,346.2 | 4,548.4 | 71.4 | 1.646x | 19.200x |

### `factored` / `s-030` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 557.0 | 531.4 | 570.4 | 15.1 | 0.712x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 568.4 | 554.5 | 589.5 | 14.4 | 0.726x | 1.020x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 574.6 | 550.8 | 616.8 | 26.0 | 0.734x | 1.032x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 777.5 | 770.3 | 787.5 | 5.9 | 0.993x | 1.396x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 782.7 | 772.1 | 801.7 | 10.0 | 1.000x | 1.405x |

### `factored` / `s-030` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 218.6 | 213.3 | 228.9 | 5.2 | 0.081x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,447.1 | 1,409.9 | 1,531.8 | 41.7 | 0.533x | 6.621x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,450.7 | 1,440.5 | 1,503.3 | 23.9 | 0.535x | 6.638x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,488.1 | 1,340.5 | 1,520.2 | 64.8 | 0.548x | 6.809x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,713.4 | 2,677.4 | 2,785.1 | 44.1 | 1.000x | 12.415x |

### `factored` / `s-031` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 554.7 | 546.4 | 563.4 | 6.2 | 0.709x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 567.0 | 553.3 | 617.6 | 25.9 | 0.725x | 1.022x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 577.4 | 553.8 | 584.0 | 11.1 | 0.738x | 1.041x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 782.2 | 774.7 | 800.8 | 9.8 | 1.000x | 1.410x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 782.3 | 770.2 | 816.8 | 16.3 | 1.000x | 1.410x |

### `factored` / `s-031` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 234.9 | 231.2 | 238.3 | 2.3 | 0.088x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 2,029.2 | 1,989.0 | 2,113.6 | 44.2 | 0.759x | 8.639x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 2,051.3 | 1,992.1 | 2,109.4 | 38.1 | 0.767x | 8.733x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 2,079.6 | 1,997.4 | 2,176.5 | 58.9 | 0.778x | 8.853x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,673.9 | 2,666.6 | 2,807.1 | 55.0 | 1.000x | 11.384x |

### `factored` / `s-032` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 594.5 | 564.5 | 639.2 | 24.7 | 0.642x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 610.8 | 597.9 | 615.1 | 7.2 | 0.660x | 1.027x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 634.0 | 591.0 | 647.5 | 20.4 | 0.685x | 1.066x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 923.3 | 912.3 | 966.5 | 18.6 | 0.997x | 1.553x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 925.8 | 915.9 | 953.5 | 12.7 | 1.000x | 1.557x |

### `factored` / `s-032` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 328.4 | 314.1 | 332.2 | 7.3 | 0.100x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,746.4 | 1,722.4 | 1,856.2 | 52.7 | 0.532x | 5.318x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,771.6 | 1,739.3 | 1,793.5 | 20.2 | 0.539x | 5.394x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,786.6 | 1,707.7 | 1,827.8 | 45.8 | 0.544x | 5.440x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,284.0 | 3,255.3 | 3,414.3 | 59.2 | 1.000x | 9.999x |

### `factored` / `s-033` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 600.9 | 574.8 | 621.8 | 17.5 | 0.691x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 610.4 | 577.4 | 638.2 | 20.1 | 0.702x | 1.016x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 611.1 | 590.1 | 637.0 | 16.7 | 0.703x | 1.017x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 867.8 | 861.9 | 889.4 | 9.7 | 0.998x | 1.444x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 869.7 | 868.0 | 913.9 | 17.7 | 1.000x | 1.447x |

### `factored` / `s-033` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 329.3 | 328.7 | 346.8 | 7.5 | 0.108x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,756.7 | 1,714.1 | 1,781.6 | 25.9 | 0.576x | 5.334x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,767.7 | 1,715.8 | 1,805.5 | 31.6 | 0.580x | 5.368x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,780.4 | 1,716.8 | 1,802.8 | 35.0 | 0.584x | 5.406x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,048.6 | 3,027.0 | 3,186.7 | 69.7 | 1.000x | 9.257x |

### `factored` / `s-034` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 520.4 | 488.8 | 579.5 | 29.7 | 0.416x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 535.8 | 504.5 | 568.8 | 22.2 | 0.428x | 1.030x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 536.8 | 500.6 | 557.1 | 20.5 | 0.429x | 1.031x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,250.8 | 1,242.9 | 1,286.5 | 15.2 | 1.000x | 2.403x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,251.9 | 1,245.8 | 1,311.8 | 24.9 | 1.001x | 2.405x |

### `factored` / `s-034` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 390.3 | 377.1 | 390.7 | 5.3 | 0.083x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,034.4 | 1,006.6 | 1,133.9 | 47.1 | 0.220x | 2.650x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,045.1 | 998.1 | 1,076.8 | 29.7 | 0.222x | 2.678x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,065.5 | 1,032.4 | 1,091.0 | 20.1 | 0.226x | 2.730x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,704.2 | 4,611.0 | 4,784.4 | 64.8 | 1.000x | 12.053x |

### `factored` / `s-035` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 731.3 | 707.9 | 793.0 | 29.1 | 0.465x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 752.5 | 739.4 | 831.3 | 33.6 | 0.479x | 1.029x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 767.8 | 698.3 | 793.0 | 31.8 | 0.489x | 1.050x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,571.2 | 1,569.0 | 1,604.5 | 13.4 | 1.000x | 2.149x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,579.3 | 1,567.9 | 1,607.1 | 14.8 | 1.005x | 2.160x |

### `factored` / `s-035` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 487.8 | 474.6 | 494.3 | 7.0 | 0.082x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 2,285.0 | 2,243.8 | 2,352.5 | 36.6 | 0.386x | 4.684x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 2,289.2 | 2,218.5 | 2,367.3 | 58.8 | 0.387x | 4.693x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 2,291.2 | 2,217.7 | 2,301.8 | 31.6 | 0.387x | 4.697x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 5,913.8 | 5,883.7 | 6,023.9 | 57.7 | 1.000x | 12.123x |

### `factored` / `s-036` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 545.2 | 524.6 | 568.4 | 16.6 | 0.866x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 549.7 | 535.4 | 561.7 | 9.8 | 0.873x | 1.008x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 564.2 | 538.7 | 618.5 | 26.6 | 0.896x | 1.035x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 629.3 | 623.2 | 643.5 | 6.9 | 1.000x | 1.154x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 630.4 | 622.0 | 640.4 | 6.0 | 1.002x | 1.156x |

### `factored` / `s-036` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 195.5 | 194.9 | 197.7 | 1.0 | 0.094x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,964.5 | 1,947.4 | 2,031.3 | 29.0 | 0.941x | 10.049x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,970.7 | 1,967.2 | 2,012.3 | 19.0 | 0.944x | 10.081x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,983.5 | 1,906.7 | 2,002.5 | 35.9 | 0.950x | 10.146x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,088.1 | 2,062.7 | 2,171.6 | 41.1 | 1.000x | 10.681x |

### `factored` / `s-037` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 585.7 | 569.5 | 630.3 | 21.3 | 0.687x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 589.5 | 571.7 | 640.2 | 26.9 | 0.691x | 1.006x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 608.1 | 526.8 | 642.4 | 39.7 | 0.713x | 1.038x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 844.6 | 834.8 | 847.8 | 4.5 | 0.991x | 1.442x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 852.5 | 844.8 | 859.4 | 4.9 | 1.000x | 1.456x |

### `factored` / `s-037` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 286.1 | 281.1 | 316.1 | 12.7 | 0.097x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,503.4 | 1,446.5 | 1,570.2 | 40.8 | 0.511x | 5.254x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,510.7 | 1,461.9 | 1,558.1 | 32.8 | 0.514x | 5.280x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,524.5 | 1,483.7 | 1,532.7 | 17.9 | 0.518x | 5.328x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,940.2 | 2,913.6 | 3,070.2 | 55.4 | 1.000x | 10.275x |

### `factored` / `s-038` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 645.7 | 614.6 | 665.0 | 17.4 | 0.640x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 676.8 | 623.7 | 687.6 | 25.1 | 0.671x | 1.048x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 697.9 | 637.7 | 727.9 | 34.3 | 0.691x | 1.081x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,004.0 | 998.6 | 1,025.2 | 9.5 | 0.995x | 1.555x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,009.4 | 995.2 | 1,056.9 | 22.5 | 1.000x | 1.563x |

### `factored` / `s-038` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 569.2 | 565.5 | 581.0 | 5.3 | 0.158x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 2,453.6 | 2,449.3 | 2,520.2 | 32.4 | 0.683x | 4.310x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 2,501.9 | 2,481.9 | 2,548.1 | 24.7 | 0.696x | 4.395x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 2,507.4 | 2,486.5 | 2,517.1 | 11.1 | 0.698x | 4.405x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,593.5 | 3,585.7 | 4,022.8 | 169.0 | 1.000x | 6.313x |

### `factored` / `s-039` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 379.9 | 372.3 | 420.9 | 17.3 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 380.0 | 378.6 | 395.1 | 6.3 | 1.000x | 1.000x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 473.6 | 436.1 | 493.7 | 19.2 | 1.246x | 1.247x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 480.7 | 444.8 | 524.4 | 31.9 | 1.265x | 1.265x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 500.0 | 436.8 | 515.3 | 28.6 | 1.316x | 1.316x |

### `factored` / `s-039` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 211.8 | 210.0 | 216.7 | 2.3 | 0.135x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 698.7 | 671.1 | 719.9 | 16.6 | 0.444x | 3.299x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 706.4 | 656.3 | 759.8 | 36.0 | 0.449x | 3.335x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 748.1 | 672.6 | 775.8 | 35.7 | 0.476x | 3.532x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,572.3 | 1,551.9 | 1,637.2 | 30.7 | 1.000x | 7.423x |

### `factored` / `s-040` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 33.3 | 33.1 | 35.3 | 0.8 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 34.2 | 33.5 | 35.3 | 0.7 | 1.028x | 1.028x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 644.3 | 623.7 | 682.0 | 22.5 | 19.357x | 19.357x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 668.5 | 645.5 | 690.6 | 17.5 | 20.082x | 20.082x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 707.1 | 638.4 | 724.9 | 37.0 | 21.243x | 21.243x |

### `factored` / `s-040` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 35.2 | 34.7 | 52.3 | 6.7 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.4 | 44.4 | 48.5 | 1.6 | 1.261x | 1.261x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 2,193.6 | 2,189.2 | 2,204.8 | 5.9 | 62.341x | 62.341x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 2,214.4 | 2,211.8 | 2,245.4 | 13.1 | 62.930x | 62.930x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 2,224.4 | 2,124.1 | 2,352.7 | 89.9 | 63.215x | 63.215x |

### `factored` / `s-041` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 161.9 | 159.3 | 168.9 | 3.2 | 0.995x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 162.7 | 161.9 | 165.8 | 1.4 | 1.000x | 1.005x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 418.1 | 401.8 | 456.7 | 21.1 | 2.569x | 2.582x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 428.8 | 422.0 | 455.5 | 13.9 | 2.635x | 2.649x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 429.6 | 409.5 | 451.9 | 14.6 | 2.639x | 2.653x |

### `factored` / `s-041` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 54.7 | 54.6 | 55.4 | 0.3 | 0.285x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 192.0 | 178.7 | 197.2 | 7.0 | 1.000x | 3.511x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,342.9 | 1,289.5 | 1,407.5 | 40.5 | 6.993x | 24.555x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,359.6 | 1,344.5 | 1,379.8 | 12.6 | 7.080x | 24.860x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,371.7 | 1,359.5 | 1,408.8 | 16.9 | 7.144x | 25.083x |

### `factored` / `s-042` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 504.3 | 485.4 | 581.2 | 35.2 | 0.829x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 517.4 | 415.0 | 536.9 | 46.7 | 0.851x | 1.026x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 530.1 | 471.9 | 549.7 | 27.1 | 0.871x | 1.051x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 608.3 | 602.7 | 624.2 | 7.2 | 1.000x | 1.206x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 613.9 | 603.8 | 620.5 | 6.6 | 1.009x | 1.217x |

### `factored` / `s-042` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 84.7 | 83.2 | 91.5 | 3.2 | 0.134x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 632.1 | 617.9 | 1,078.8 | 179.5 | 1.000x | 7.464x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 712.9 | 705.4 | 802.1 | 35.9 | 1.128x | 8.417x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 737.3 | 704.8 | 742.0 | 15.3 | 1.166x | 8.706x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 740.5 | 695.8 | 772.1 | 25.4 | 1.171x | 8.743x |

### `factored` / `s-043` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 522.2 | 506.5 | 566.0 | 20.3 | 0.906x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 562.0 | 503.7 | 574.5 | 25.7 | 0.976x | 1.076x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 571.1 | 463.8 | 584.6 | 49.9 | 0.991x | 1.094x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 573.0 | 567.6 | 584.8 | 6.9 | 0.995x | 1.097x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 576.1 | 569.9 | 600.1 | 11.8 | 1.000x | 1.103x |

### `factored` / `s-043` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 291.0 | 285.7 | 293.5 | 2.6 | 0.103x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 998.8 | 945.8 | 1,026.1 | 28.5 | 0.352x | 3.432x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,001.7 | 980.7 | 1,040.1 | 22.7 | 0.353x | 3.442x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,012.3 | 969.5 | 1,046.1 | 27.2 | 0.357x | 3.478x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,838.6 | 2,800.5 | 2,875.0 | 28.7 | 1.000x | 9.754x |

### `factored` / `s-044` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 161.6 | 161.1 | 168.8 | 2.9 | 0.987x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 163.7 | 161.3 | 165.8 | 1.9 | 1.000x | 1.013x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 419.6 | 389.7 | 467.6 | 26.1 | 2.562x | 2.596x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 424.5 | 371.3 | 432.2 | 22.1 | 2.593x | 2.627x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 428.1 | 392.2 | 459.5 | 22.8 | 2.614x | 2.648x |

### `factored` / `s-044` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 159.1 | 158.0 | 166.0 | 2.9 | 0.156x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 533.0 | 472.7 | 583.9 | 37.9 | 0.523x | 3.349x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 549.5 | 501.4 | 566.0 | 23.0 | 0.540x | 3.453x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 568.6 | 535.4 | 640.6 | 38.5 | 0.558x | 3.573x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,018.5 | 1,012.3 | 1,038.0 | 8.8 | 1.000x | 6.400x |

### `factored` / `s-045` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 530.6 | 460.8 | 573.5 | 40.4 | 0.915x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 542.5 | 521.8 | 601.5 | 27.0 | 0.936x | 1.022x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 565.8 | 537.6 | 607.1 | 23.8 | 0.976x | 1.066x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 578.2 | 572.4 | 583.7 | 3.8 | 0.997x | 1.090x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 579.8 | 569.5 | 653.3 | 30.8 | 1.000x | 1.093x |

### `factored` / `s-045` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 200.4 | 198.0 | 201.8 | 1.4 | 0.097x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,804.6 | 1,790.8 | 1,828.1 | 13.0 | 0.873x | 9.005x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,819.9 | 1,796.6 | 1,844.0 | 15.9 | 0.881x | 9.081x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,823.7 | 1,798.6 | 1,844.7 | 16.1 | 0.883x | 9.100x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,066.4 | 1,985.6 | 2,259.9 | 99.9 | 1.000x | 10.311x |

### `factored` / `s-046` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 666.3 | 641.0 | 687.0 | 15.1 | 0.664x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 671.0 | 637.4 | 705.9 | 27.3 | 0.669x | 1.007x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 688.3 | 638.3 | 707.5 | 27.9 | 0.686x | 1.033x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 998.1 | 987.6 | 999.8 | 4.8 | 0.995x | 1.498x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,002.9 | 991.0 | 1,009.0 | 6.9 | 1.000x | 1.505x |

### `factored` / `s-046` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 537.9 | 535.9 | 543.8 | 3.0 | 0.150x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,967.0 | 1,883.7 | 2,010.0 | 45.3 | 0.550x | 3.657x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,969.6 | 1,960.7 | 1,982.3 | 8.0 | 0.551x | 3.662x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,971.3 | 1,927.4 | 1,996.9 | 29.1 | 0.551x | 3.665x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,576.8 | 3,497.5 | 3,605.1 | 37.9 | 1.000x | 6.649x |

### `factored` / `s-047` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 524.4 | 493.6 | 564.7 | 24.8 | 0.324x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 527.0 | 499.6 | 570.7 | 29.9 | 0.325x | 1.005x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 562.0 | 518.5 | 587.1 | 23.9 | 0.347x | 1.072x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,615.6 | 1,598.4 | 1,632.1 | 11.6 | 0.997x | 3.081x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,620.4 | 1,606.5 | 1,655.1 | 16.5 | 1.000x | 3.090x |

### `factored` / `s-047` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 468.8 | 466.6 | 479.6 | 5.8 | 0.077x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,127.6 | 1,077.0 | 1,158.3 | 27.4 | 0.185x | 2.405x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,130.6 | 1,122.5 | 1,163.5 | 15.6 | 0.186x | 2.412x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,133.5 | 1,108.0 | 1,196.4 | 31.0 | 0.186x | 2.418x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 6,090.9 | 6,019.8 | 6,203.6 | 67.0 | 1.000x | 12.992x |

### `factored` / `s-048` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 494.5 | 427.4 | 527.2 | 34.1 | 0.637x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 528.8 | 495.9 | 559.5 | 23.3 | 0.681x | 1.069x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 529.7 | 480.2 | 550.1 | 23.9 | 0.682x | 1.071x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 776.3 | 774.3 | 801.9 | 10.5 | 1.000x | 1.570x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 779.0 | 775.4 | 788.3 | 4.5 | 1.003x | 1.575x |

### `factored` / `s-048` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 186.5 | 183.3 | 191.5 | 2.7 | 0.091x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 751.4 | 750.3 | 777.4 | 11.8 | 0.368x | 4.028x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 773.0 | 744.6 | 847.8 | 35.4 | 0.379x | 4.144x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 791.9 | 753.2 | 810.8 | 19.4 | 0.388x | 4.245x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,042.0 | 2,025.7 | 2,116.1 | 33.8 | 1.000x | 10.947x |

### `factored` / `s-049` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 516.9 | 464.7 | 539.4 | 25.4 | 0.950x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 528.4 | 494.5 | 632.1 | 56.5 | 0.971x | 1.022x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 544.2 | 542.6 | 550.9 | 3.4 | 1.000x | 1.053x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 547.2 | 537.9 | 548.6 | 3.9 | 1.006x | 1.059x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 559.4 | 541.4 | 584.5 | 15.4 | 1.028x | 1.082x |

### `factored` / `s-049` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 272.7 | 270.0 | 275.9 | 2.0 | 0.105x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 836.5 | 794.4 | 867.2 | 25.7 | 0.323x | 3.067x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 872.4 | 839.7 | 932.8 | 31.6 | 0.337x | 3.199x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 896.6 | 837.1 | 901.7 | 26.0 | 0.346x | 3.288x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,588.8 | 2,546.1 | 2,632.3 | 29.1 | 1.000x | 9.493x |

### `factored` / `s-050` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 546.5 | 510.6 | 619.4 | 41.9 | 0.716x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 572.6 | 526.5 | 591.2 | 24.1 | 0.750x | 1.048x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 601.6 | 551.0 | 655.7 | 39.6 | 0.788x | 1.101x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 763.2 | 762.0 | 785.3 | 9.5 | 0.999x | 1.397x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 763.7 | 760.6 | 801.8 | 15.7 | 1.000x | 1.398x |

### `factored` / `s-050` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 379.5 | 374.5 | 392.7 | 6.3 | 0.106x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,164.0 | 1,076.4 | 1,177.1 | 41.3 | 0.325x | 3.067x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,194.0 | 1,146.4 | 1,201.8 | 23.6 | 0.333x | 3.146x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,199.4 | 1,084.9 | 1,229.9 | 49.7 | 0.335x | 3.161x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,581.4 | 3,492.4 | 3,625.9 | 51.9 | 1.000x | 9.437x |

### `factored` / `s-051` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 504.6 | 478.3 | 556.9 | 31.1 | 0.920x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 547.4 | 518.0 | 575.6 | 21.9 | 0.998x | 1.085x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 548.6 | 540.1 | 550.2 | 3.7 | 1.000x | 1.087x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 549.4 | 546.8 | 555.5 | 2.9 | 1.001x | 1.089x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 558.9 | 482.5 | 613.8 | 44.5 | 1.019x | 1.108x |

### `factored` / `s-051` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 276.0 | 272.6 | 277.9 | 1.8 | 0.107x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 825.8 | 751.8 | 855.8 | 35.1 | 0.319x | 2.992x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 883.0 | 822.9 | 888.7 | 24.9 | 0.342x | 3.200x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 886.3 | 843.0 | 892.6 | 18.8 | 0.343x | 3.212x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,585.0 | 2,554.3 | 2,639.2 | 32.8 | 1.000x | 9.368x |

### `factored` / `s-052` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 521.4 | 495.6 | 536.5 | 18.0 | 0.670x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 526.5 | 505.2 | 577.8 | 28.3 | 0.676x | 1.010x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 532.4 | 482.6 | 552.4 | 23.7 | 0.684x | 1.021x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 778.7 | 772.5 | 808.0 | 15.4 | 1.000x | 1.494x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 782.8 | 771.6 | 790.6 | 6.7 | 1.005x | 1.502x |

### `factored` / `s-052` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 216.2 | 213.5 | 221.2 | 2.8 | 0.080x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,037.6 | 980.6 | 1,059.1 | 28.7 | 0.385x | 4.800x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,054.8 | 1,036.4 | 1,095.0 | 20.1 | 0.391x | 4.880x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,069.2 | 1,015.0 | 1,077.0 | 23.1 | 0.396x | 4.946x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,698.5 | 2,654.8 | 2,807.6 | 56.9 | 1.000x | 12.483x |

### `factored` / `s-053` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 521.8 | 479.2 | 530.7 | 18.7 | 0.675x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 538.6 | 507.1 | 556.7 | 20.0 | 0.697x | 1.032x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 544.6 | 519.3 | 564.2 | 18.0 | 0.704x | 1.044x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 773.2 | 769.7 | 799.0 | 10.7 | 1.000x | 1.482x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 778.8 | 772.6 | 779.6 | 2.6 | 1.007x | 1.493x |

### `factored` / `s-053` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 217.7 | 212.6 | 218.5 | 2.2 | 0.081x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 963.8 | 949.9 | 1,000.8 | 17.5 | 0.359x | 4.428x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 987.0 | 925.0 | 1,004.0 | 28.9 | 0.367x | 4.535x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,026.6 | 951.7 | 1,145.8 | 72.1 | 0.382x | 4.717x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,687.5 | 2,667.5 | 2,804.0 | 50.3 | 1.000x | 12.348x |

### `factored` / `s-054` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 517.0 | 492.4 | 517.5 | 10.2 | 0.669x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 542.4 | 497.5 | 574.1 | 30.9 | 0.702x | 1.049x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 550.3 | 522.8 | 567.2 | 14.4 | 0.712x | 1.065x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 772.9 | 770.6 | 794.4 | 9.2 | 1.000x | 1.495x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 780.1 | 769.1 | 793.9 | 8.0 | 1.009x | 1.509x |

### `factored` / `s-054` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 216.6 | 214.8 | 226.9 | 4.4 | 0.080x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 956.6 | 939.0 | 975.3 | 12.8 | 0.353x | 4.417x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 993.6 | 939.4 | 1,021.4 | 27.6 | 0.367x | 4.588x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 999.8 | 915.6 | 1,021.5 | 38.8 | 0.369x | 4.616x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,706.8 | 2,658.3 | 2,807.3 | 53.0 | 1.000x | 12.498x |

### `factored` / `s-055` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 514.4 | 459.1 | 541.2 | 27.7 | 0.662x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 532.3 | 499.1 | 568.8 | 22.3 | 0.686x | 1.035x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 546.2 | 510.3 | 582.1 | 26.8 | 0.703x | 1.062x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 776.5 | 774.0 | 792.4 | 6.6 | 1.000x | 1.509x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 779.1 | 772.5 | 780.6 | 3.3 | 1.003x | 1.515x |

### `factored` / `s-055` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 221.2 | 212.4 | 224.4 | 4.4 | 0.082x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 980.4 | 924.3 | 1,062.0 | 45.1 | 0.365x | 4.432x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 981.3 | 957.7 | 1,016.7 | 19.8 | 0.365x | 4.436x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 994.7 | 950.2 | 1,014.5 | 23.6 | 0.370x | 4.497x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,687.5 | 2,665.8 | 2,783.2 | 45.8 | 1.000x | 12.150x |

### `factored` / `s-056` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 523.5 | 511.5 | 552.9 | 15.6 | 0.675x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 523.7 | 490.4 | 559.6 | 23.3 | 0.675x | 1.000x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 552.5 | 525.7 | 559.0 | 11.6 | 0.712x | 1.055x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 775.7 | 772.4 | 786.9 | 5.2 | 1.000x | 1.482x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 779.0 | 771.3 | 836.1 | 24.0 | 1.004x | 1.488x |

### `factored` / `s-056` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 222.5 | 219.9 | 223.2 | 1.2 | 0.083x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 963.0 | 955.7 | 1,035.0 | 29.8 | 0.361x | 4.328x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 979.1 | 965.2 | 1,013.2 | 17.5 | 0.367x | 4.400x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 994.4 | 971.7 | 1,031.0 | 21.8 | 0.373x | 4.469x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,669.1 | 2,660.0 | 2,799.8 | 54.7 | 1.000x | 11.996x |

### `factored` / `s-057` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 8,184.1 | 8,180.3 | 8,248.8 | 28.3 | 0.805x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 8,202.1 | 8,134.9 | 8,275.5 | 44.9 | 0.806x | 1.002x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8,249.6 | 8,134.0 | 8,379.3 | 89.4 | 0.811x | 1.008x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 10,160.2 | 10,142.3 | 10,318.3 | 65.0 | 0.999x | 1.241x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 10,171.8 | 10,133.1 | 10,563.1 | 161.2 | 1.000x | 1.243x |

### `factored` / `s-058` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 182,009.3 | 181,190.4 | 183,835.9 | 919.4 | 0.998x | 1.000x | 5 | 100% |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 182,311.8 | 181,881.6 | 188,510.3 | 2,531.1 | 1.000x | 1.002x | 5 | 100% |

### `factored` / `s-059` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 291,822.9 | 289,946.2 | 292,888.1 | 1,142.7 | 0.998x | 1.000x | 5 | 100% |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 292,306.7 | 291,197.0 | 294,026.7 | 1,097.3 | 1.000x | 1.002x | 5 | 100% |

### `factored` / `s-060` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 199,473.7 | 198,611.8 | 199,797.7 | 414.8 | 0.230x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 199,566.3 | 198,383.9 | 203,457.6 | 1,727.6 | 0.230x | 1.000x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 200,221.4 | 199,199.0 | 201,995.0 | 1,009.4 | 0.231x | 1.004x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 852,929.2 | 849,242.9 | 880,374.1 | 11,662.3 | 0.984x | 4.276x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 866,970.7 | 848,569.5 | 887,969.5 | 13,530.6 | 1.000x | 4.346x |

### `factored` / `s-061` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 72,491.5 | 72,186.8 | 73,160.9 | 342.1 | 0.983x | 1.000x | 5 | 100% |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 73,745.5 | 72,822.0 | 75,219.3 | 841.4 | 1.000x | 1.017x | 5 | 100% |

### `factored` / `s-062` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 510.9 | 497.2 | 544.4 | 16.3 | 0.560x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 516.0 | 495.3 | 549.3 | 17.3 | 0.565x | 1.010x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 525.2 | 492.2 | 559.7 | 28.9 | 0.575x | 1.028x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 882.8 | 881.9 | 895.2 | 5.0 | 0.967x | 1.728x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 912.8 | 869.8 | 917.0 | 17.3 | 1.000x | 1.787x |

### `factored` / `s-063` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 213,286.2 | 211,072.4 | 215,032.2 | 1,389.9 | 1.000x | 1.000x | 5 | 100% |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 213,785.2 | 213,185.8 | 214,359.5 | 374.6 | 1.002x | 1.002x | 5 | 100% |

### `factored` / `s-064` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 149,161.6 | 148,973.9 | 150,280.6 | 471.5 | 0.993x | 1.000x | 5 | 100% |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 150,255.4 | 149,104.6 | 150,677.2 | 581.5 | 1.000x | 1.007x | 5 | 100% |

### `factored` / `s-065` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 164.0 | 160.1 | 166.9 | 2.4 | 0.973x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 168.5 | 162.7 | 172.5 | 3.2 | 1.000x | 1.027x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 353.9 | 264.6 | 395.1 | 43.8 | 2.100x | 2.158x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 365.8 | 316.0 | 395.3 | 29.1 | 2.171x | 2.230x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 391.5 | 302.8 | 447.7 | 47.2 | 2.324x | 2.388x |

### `factored` / `s-065` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 143.4 | 142.0 | 145.1 | 1.1 | 0.088x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,396.9 | 1,372.0 | 1,473.7 | 34.5 | 0.853x | 9.745x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,437.8 | 1,395.7 | 1,498.3 | 33.2 | 0.878x | 10.030x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,438.1 | 1,373.1 | 1,475.3 | 37.9 | 0.878x | 10.032x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,637.1 | 1,632.4 | 1,683.4 | 19.6 | 1.000x | 11.420x |

### `factored` / `s-066` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 540.4 | 533.0 | 593.1 | 22.4 | 0.505x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 552.5 | 541.8 | 651.9 | 41.2 | 0.516x | 1.022x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 586.4 | 543.1 | 617.0 | 24.6 | 0.548x | 1.085x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,065.8 | 1,059.6 | 1,083.1 | 8.0 | 0.995x | 1.972x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,070.9 | 1,059.7 | 1,091.1 | 10.5 | 1.000x | 1.982x |

### `factored` / `s-066` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 173.7 | 172.6 | 178.2 | 2.0 | 0.161x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 618.3 | 596.3 | 639.4 | 14.4 | 0.574x | 3.561x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 623.1 | 593.0 | 634.7 | 14.6 | 0.579x | 3.588x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 638.0 | 592.8 | 658.0 | 27.1 | 0.593x | 3.674x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,076.5 | 1,057.3 | 1,083.2 | 9.7 | 1.000x | 6.199x |

### `factored` / `s-067` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 540.3 | 509.9 | 592.2 | 28.1 | 0.534x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 545.8 | 511.7 | 562.7 | 16.9 | 0.539x | 1.010x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 551.9 | 528.7 | 627.2 | 33.5 | 0.545x | 1.021x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,012.5 | 1,004.3 | 1,023.5 | 6.1 | 1.000x | 1.874x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,015.3 | 1,002.9 | 1,027.0 | 7.9 | 1.003x | 1.879x |

### `factored` / `s-067` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 161.1 | 160.4 | 163.1 | 0.9 | 0.159x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 542.0 | 539.2 | 549.2 | 3.7 | 0.535x | 3.364x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 542.0 | 519.4 | 559.0 | 12.7 | 0.535x | 3.364x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 579.4 | 542.7 | 595.0 | 18.3 | 0.572x | 3.596x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,012.8 | 1,001.9 | 1,047.7 | 15.7 | 1.000x | 6.286x |

### `factored` / `s-068` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 401.1 | 377.4 | 435.4 | 19.6 | 0.578x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 423.2 | 415.2 | 507.5 | 37.9 | 0.610x | 1.055x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 449.3 | 366.1 | 472.1 | 41.8 | 0.647x | 1.120x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 692.3 | 688.2 | 699.0 | 4.6 | 0.997x | 1.726x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 694.1 | 688.6 | 707.8 | 6.5 | 1.000x | 1.731x |

### `factored` / `s-068` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 104.4 | 104.2 | 107.3 | 1.2 | 0.151x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 419.2 | 375.9 | 580.3 | 71.5 | 0.605x | 4.016x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 425.0 | 329.7 | 460.3 | 51.4 | 0.613x | 4.071x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 450.7 | 434.1 | 477.5 | 14.2 | 0.650x | 4.318x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 693.1 | 681.8 | 720.6 | 14.6 | 1.000x | 6.640x |

### `factored` / `s-069` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 504.4 | 491.5 | 518.9 | 10.0 | 0.772x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 511.4 | 429.4 | 534.4 | 39.5 | 0.783x | 1.014x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 533.2 | 493.2 | 540.6 | 18.8 | 0.816x | 1.057x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 647.5 | 637.6 | 649.9 | 5.5 | 0.991x | 1.284x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 653.1 | 631.6 | 660.0 | 9.9 | 1.000x | 1.295x |

### `factored` / `s-069` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 203.6 | 201.2 | 203.8 | 1.2 | 0.090x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,817.7 | 1,757.4 | 1,839.1 | 27.5 | 0.803x | 8.927x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,819.6 | 1,773.2 | 1,847.9 | 24.2 | 0.804x | 8.936x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,820.6 | 1,804.2 | 1,848.9 | 16.4 | 0.805x | 8.941x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,262.7 | 2,236.7 | 2,316.2 | 31.6 | 1.000x | 11.112x |

### `factored` / `s-070` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 525.4 | 516.7 | 544.9 | 11.9 | 0.604x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 565.7 | 497.5 | 598.6 | 38.4 | 0.650x | 1.077x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 568.6 | 514.9 | 679.0 | 53.7 | 0.654x | 1.082x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 858.5 | 851.5 | 867.6 | 6.8 | 0.987x | 1.634x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 869.9 | 857.4 | 922.0 | 23.1 | 1.000x | 1.656x |

### `factored` / `s-070` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 148.4 | 147.4 | 153.2 | 2.0 | 0.170x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 506.7 | 432.6 | 563.6 | 42.9 | 0.582x | 3.416x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 512.7 | 478.9 | 567.1 | 29.8 | 0.589x | 3.456x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 514.3 | 470.9 | 527.5 | 23.7 | 0.591x | 3.467x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 870.6 | 849.8 | 886.1 | 12.4 | 1.000x | 5.868x |

### `factored` / `s-071` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 552.9 | 481.5 | 567.5 | 31.3 | 0.623x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 588.7 | 496.5 | 621.3 | 46.4 | 0.663x | 1.065x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 611.8 | 552.8 | 650.3 | 32.0 | 0.689x | 1.106x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 881.8 | 874.4 | 883.2 | 3.8 | 0.993x | 1.595x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 888.2 | 865.0 | 900.3 | 12.0 | 1.000x | 1.606x |

### `factored` / `s-071` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 167.4 | 164.2 | 168.4 | 1.7 | 0.190x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 488.5 | 462.7 | 514.9 | 16.6 | 0.555x | 2.919x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 525.8 | 460.2 | 544.4 | 31.0 | 0.597x | 3.141x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 526.6 | 473.0 | 570.9 | 37.7 | 0.598x | 3.147x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 880.1 | 868.9 | 900.2 | 10.9 | 1.000x | 5.259x |

### `factored` / `s-072` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 962.9 | 934.7 | 987.9 | 22.4 | 0.425x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 974.6 | 926.1 | 1,119.7 | 67.3 | 0.430x | 1.012x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 987.3 | 944.4 | 1,014.1 | 23.3 | 0.436x | 1.025x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,232.8 | 2,215.8 | 2,257.6 | 14.3 | 0.985x | 2.319x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,265.7 | 2,231.0 | 2,300.4 | 24.4 | 1.000x | 2.353x |

### `factored` / `s-072` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 407.9 | 406.6 | 415.3 | 3.2 | 0.130x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,176.2 | 1,140.1 | 1,215.7 | 24.1 | 0.375x | 2.884x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,201.6 | 1,178.0 | 1,249.2 | 23.2 | 0.383x | 2.946x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,205.6 | 1,185.0 | 1,263.4 | 27.0 | 0.385x | 2.956x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,133.7 | 3,110.0 | 3,181.5 | 24.8 | 1.000x | 7.684x |

### `factored` / `s-073` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 499.6 | 456.5 | 538.5 | 30.1 | 0.622x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 514.7 | 465.9 | 565.8 | 33.4 | 0.640x | 1.030x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 543.9 | 497.0 | 576.1 | 25.7 | 0.677x | 1.089x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 792.2 | 782.6 | 926.0 | 54.0 | 0.986x | 1.586x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 803.6 | 770.5 | 825.5 | 17.9 | 1.000x | 1.609x |

### `factored` / `s-073` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 216.2 | 213.9 | 223.6 | 3.6 | 0.080x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,396.4 | 1,376.5 | 1,415.7 | 12.6 | 0.515x | 6.459x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,418.5 | 1,384.2 | 1,434.9 | 17.7 | 0.523x | 6.562x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,423.8 | 1,407.5 | 1,448.9 | 14.3 | 0.525x | 6.586x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,711.3 | 2,673.2 | 3,291.5 | 233.1 | 1.000x | 12.542x |

### `factored` / `s-074` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 526.9 | 505.2 | 569.0 | 20.9 | 0.654x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 551.7 | 490.5 | 582.4 | 32.2 | 0.684x | 1.047x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 558.8 | 539.2 | 601.2 | 24.0 | 0.693x | 1.060x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 787.1 | 783.4 | 807.6 | 9.0 | 0.977x | 1.494x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 806.1 | 768.6 | 807.5 | 14.9 | 1.000x | 1.530x |

### `factored` / `s-074` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 233.8 | 231.7 | 234.3 | 1.1 | 0.087x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,781.8 | 1,732.5 | 1,794.4 | 23.3 | 0.663x | 7.620x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,782.2 | 1,685.6 | 1,823.5 | 48.2 | 0.663x | 7.622x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,790.7 | 1,739.1 | 1,812.7 | 26.5 | 0.666x | 7.659x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,688.9 | 2,675.5 | 2,804.9 | 51.4 | 1.000x | 11.500x |

### `factored` / `s-075` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 509.1 | 491.3 | 519.3 | 11.1 | 0.493x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 521.6 | 509.9 | 561.4 | 17.6 | 0.505x | 1.025x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 607.9 | 563.0 | 617.8 | 19.9 | 0.588x | 1.194x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,033.7 | 1,028.0 | 1,067.8 | 16.5 | 1.000x | 2.030x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,058.3 | 1,035.0 | 1,074.3 | 15.2 | 1.024x | 2.079x |

### `factored` / `s-075` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 107.6 | 106.8 | 110.5 | 1.4 | 0.103x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 553.5 | 466.5 | 619.4 | 49.2 | 0.530x | 5.143x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 579.0 | 545.5 | 701.5 | 54.8 | 0.554x | 5.380x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 619.7 | 601.6 | 626.1 | 9.8 | 0.593x | 5.758x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,044.4 | 1,024.2 | 1,084.3 | 23.0 | 1.000x | 9.705x |

### `factored` / `s-076` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 510.7 | 491.5 | 519.1 | 11.5 | 0.490x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 516.7 | 502.2 | 561.6 | 21.0 | 0.496x | 1.012x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 607.5 | 559.6 | 629.2 | 24.4 | 0.583x | 1.190x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,041.3 | 1,024.5 | 1,078.0 | 18.5 | 1.000x | 2.039x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,056.6 | 1,029.2 | 1,072.1 | 15.1 | 1.015x | 2.069x |

### `factored` / `s-076` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 107.1 | 106.3 | 107.6 | 0.4 | 0.104x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 535.0 | 522.5 | 634.4 | 40.9 | 0.518x | 4.997x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 598.3 | 542.1 | 627.2 | 35.0 | 0.579x | 5.588x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 601.4 | 569.4 | 643.6 | 24.6 | 0.583x | 5.617x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,032.4 | 1,021.1 | 1,068.6 | 16.6 | 1.000x | 9.642x |

### `factored` / `s-077` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 501.3 | 460.0 | 513.3 | 19.5 | 0.433x | 1.000x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 513.0 | 489.1 | 536.4 | 16.6 | 0.443x | 1.023x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 565.6 | 534.6 | 592.0 | 19.9 | 0.488x | 1.128x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,158.8 | 1,127.8 | 1,165.4 | 14.7 | 1.000x | 2.312x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,170.3 | 1,134.3 | 1,175.7 | 19.0 | 1.010x | 2.334x |

### `factored` / `s-077` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 108.1 | 107.2 | 116.0 | 3.2 | 0.096x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 576.2 | 535.9 | 597.6 | 23.6 | 0.510x | 5.329x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 593.0 | 514.6 | 686.8 | 58.2 | 0.525x | 5.485x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 605.3 | 548.6 | 611.3 | 23.5 | 0.536x | 5.599x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,129.4 | 1,123.6 | 1,160.7 | 15.2 | 1.000x | 10.446x |

### `factored` / `s-078` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 543.2 | 511.1 | 572.1 | 22.5 | 0.500x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 558.2 | 528.3 | 563.0 | 13.4 | 0.514x | 1.028x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 579.3 | 550.0 | 601.1 | 17.8 | 0.534x | 1.067x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,085.5 | 1,073.4 | 1,102.7 | 10.5 | 1.000x | 1.998x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,101.5 | 1,067.2 | 1,108.3 | 15.6 | 1.015x | 2.028x |

### `factored` / `s-078` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 107.9 | 107.0 | 109.3 | 0.8 | 0.100x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 563.9 | 500.6 | 661.2 | 57.8 | 0.525x | 5.225x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 572.8 | 545.5 | 594.7 | 16.0 | 0.533x | 5.307x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 589.9 | 562.7 | 598.4 | 15.5 | 0.549x | 5.466x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,074.9 | 1,069.4 | 1,100.7 | 12.8 | 1.000x | 9.960x |

### `factored` / `s-079` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 528.9 | 504.6 | 569.7 | 22.2 | 0.488x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 557.9 | 549.7 | 578.3 | 10.9 | 0.515x | 1.055x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 584.7 | 564.4 | 589.4 | 9.8 | 0.540x | 1.105x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,083.2 | 1,074.7 | 1,099.1 | 9.9 | 1.000x | 2.048x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,100.3 | 1,070.8 | 1,106.9 | 15.0 | 1.016x | 2.080x |

### `factored` / `s-079` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 107.6 | 107.2 | 114.6 | 2.9 | 0.100x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 564.4 | 492.7 | 650.0 | 52.6 | 0.523x | 5.244x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 582.8 | 536.7 | 619.4 | 29.0 | 0.540x | 5.415x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 593.3 | 570.9 | 612.5 | 14.1 | 0.550x | 5.513x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,079.5 | 1,074.6 | 1,098.1 | 10.5 | 1.000x | 10.030x |

### `factored` / `s-080` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 581.7 | 569.8 | 628.6 | 20.8 | 0.626x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 604.8 | 559.0 | 622.7 | 21.4 | 0.651x | 1.040x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 626.0 | 574.3 | 663.2 | 33.9 | 0.673x | 1.076x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 917.0 | 911.6 | 935.7 | 8.3 | 0.986x | 1.576x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 929.6 | 905.9 | 942.7 | 12.5 | 1.000x | 1.598x |

### `factored` / `s-080` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 312.3 | 306.2 | 335.3 | 10.5 | 0.097x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,756.0 | 1,728.4 | 1,842.0 | 39.1 | 0.547x | 5.624x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,771.1 | 1,713.9 | 2,167.9 | 165.0 | 0.552x | 5.672x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,782.9 | 1,726.8 | 1,866.7 | 44.9 | 0.556x | 5.710x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,207.5 | 3,173.2 | 3,564.8 | 147.0 | 1.000x | 10.272x |

### `factored` / `s-081` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 30.3 | 30.3 | 32.4 | 0.8 | 0.945x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 32.1 | 30.3 | 32.5 | 0.8 | 1.000x | 1.058x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 387.3 | 365.4 | 417.4 | 20.1 | 12.082x | 12.780x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 432.8 | 415.7 | 454.5 | 13.4 | 13.500x | 14.281x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 436.3 | 390.0 | 482.8 | 30.0 | 13.610x | 14.396x |

### `factored` / `s-081` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 31.0 | 30.4 | 33.9 | 1.3 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 41.5 | 40.3 | 51.4 | 4.2 | 1.340x | 1.340x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 434.6 | 410.8 | 467.6 | 22.7 | 14.022x | 14.022x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 440.4 | 417.8 | 471.3 | 18.6 | 14.210x | 14.210x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 445.0 | 392.8 | 491.2 | 36.1 | 14.358x | 14.358x |

### `factored` / `s-082` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 30.8 | 30.3 | 35.2 | 1.9 | 0.988x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 31.1 | 30.3 | 31.4 | 0.4 | 1.000x | 1.012x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 412.8 | 306.7 | 437.7 | 45.9 | 13.265x | 13.419x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 438.8 | 405.0 | 455.1 | 16.7 | 14.100x | 14.264x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 449.1 | 415.6 | 459.2 | 15.0 | 14.429x | 14.598x |

### `factored` / `s-082` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.7 | 30.4 | 34.3 | 1.5 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 42.1 | 40.1 | 49.8 | 3.4 | 1.369x | 1.369x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 454.5 | 450.9 | 473.3 | 8.1 | 14.780x | 14.780x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 456.9 | 412.6 | 512.6 | 32.1 | 14.860x | 14.860x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 468.2 | 430.4 | 496.4 | 27.4 | 15.227x | 15.227x |

### `factored` / `s-083` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 34.1 | 33.5 | 39.6 | 2.3 | 0.984x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 34.7 | 33.8 | 35.8 | 0.7 | 1.000x | 1.016x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 476.3 | 445.6 | 616.2 | 59.8 | 13.730x | 13.955x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 495.6 | 451.7 | 523.8 | 24.0 | 14.286x | 14.521x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 530.0 | 459.6 | 571.3 | 37.8 | 15.278x | 15.529x |

### `factored` / `s-083` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 35.2 | 34.9 | 39.9 | 1.9 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.3 | 46.1 | 48.4 | 1.0 | 1.317x | 1.317x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 3,395.1 | 3,371.3 | 3,485.3 | 41.6 | 96.544x | 96.544x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 3,402.5 | 3,328.7 | 3,482.9 | 48.9 | 96.756x | 96.756x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 3,437.5 | 3,405.4 | 3,452.8 | 19.5 | 97.751x | 97.751x |

### `factored` / `s-084` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 33.6 | 33.1 | 34.6 | 0.5 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 34.7 | 33.6 | 37.1 | 1.2 | 1.034x | 1.034x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 596.3 | 570.5 | 655.3 | 31.9 | 17.772x | 17.772x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 622.9 | 611.6 | 646.8 | 12.4 | 18.564x | 18.564x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 636.2 | 568.5 | 662.4 | 33.0 | 18.961x | 18.961x |

### `factored` / `s-084` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 34.3 | 33.9 | 39.5 | 2.1 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.4 | 44.3 | 48.7 | 1.7 | 1.296x | 1.296x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,581.2 | 1,541.0 | 1,659.0 | 42.0 | 46.147x | 46.147x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,632.7 | 1,596.8 | 1,697.4 | 35.4 | 47.647x | 47.647x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,636.8 | 1,579.9 | 1,672.1 | 32.8 | 47.768x | 47.768x |

### `factored` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 7,032,954.7 | 6,965,871.0 | 7,512,686.3 | 202,224.4 | 0.136x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 23,646,430.0 | 22,861,735.0 | 26,823,629.0 | 1,442,212.7 | 0.456x | 3.362x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 24,010,552.0 | 22,722,773.0 | 25,261,380.0 | 825,072.6 | 0.463x | 3.414x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 24,014,597.0 | 22,956,700.0 | 26,418,041.0 | 1,195,438.1 | 0.463x | 3.415x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 51,851,980.0 | 51,679,913.4 | 52,364,619.8 | 237,723.3 | 1.000x | 7.373x |

### `factored` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,812.2 | 17,783.3 | 17,813.6 | 12.0 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 17,695,592.7 | 17,644,885.3 | 17,723,881.7 | 25,980.8 | 993.453x | 993.453x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 87,151,691.0 | 87,056,790.0 | 87,870,905.0 | 296,577.9 | 4892.806x | 4892.806x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 88,138,127.0 | 87,017,010.0 | 91,290,196.0 | 1,439,973.1 | 4948.186x | 4948.186x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 88,760,543.0 | 87,217,943.0 | 92,820,847.0 | 1,915,173.9 | 4983.129x | 4983.129x |

### `factored` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,809.6 | 17,772.3 | 17,906.4 | 50.3 | 1.000x | 1.000x | 5 | 100% |

### `orig` / `s-000` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 111.2 | 110.8 | 112.9 | 0.7 | 0.201x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 111.7 | 110.8 | 120.8 | 3.7 | 0.202x | 1.005x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 244.1 | 220.6 | 275.8 | 17.7 | 0.441x | 2.196x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 548.8 | 546.7 | 553.1 | 2.1 | 0.991x | 4.936x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 553.6 | 544.8 | 556.9 | 4.4 | 1.000x | 4.979x |

### `orig` / `s-000` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 78.3 | 77.4 | 84.3 | 2.6 | 0.142x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 103.1 | 102.7 | 103.7 | 0.4 | 0.187x | 1.317x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 103.5 | 103.3 | 110.1 | 2.7 | 0.187x | 1.321x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 254.2 | 250.8 | 258.6 | 2.6 | 0.460x | 3.246x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 552.3 | 547.1 | 595.4 | 17.8 | 1.000x | 7.053x |

### `orig` / `s-001` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 143.8 | 143.5 | 153.3 | 3.8 | 0.187x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 143.9 | 143.8 | 144.8 | 0.4 | 0.187x | 1.001x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 271.7 | 251.3 | 306.7 | 19.4 | 0.353x | 1.889x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 759.8 | 757.5 | 766.5 | 3.2 | 0.986x | 5.283x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 770.4 | 753.8 | 779.7 | 9.8 | 1.000x | 5.357x |

### `orig` / `s-001` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 93.9 | 92.7 | 99.4 | 2.5 | 0.122x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 135.9 | 135.4 | 136.3 | 0.3 | 0.176x | 1.447x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 136.0 | 135.7 | 138.5 | 1.1 | 0.176x | 1.449x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 243.6 | 217.8 | 284.7 | 24.0 | 0.316x | 2.596x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 771.9 | 764.9 | 825.0 | 22.5 | 1.000x | 8.224x |

### `orig` / `s-002` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 46.2 | 46.0 | 55.8 | 3.8 | 0.097x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 46.2 | 46.2 | 46.7 | 0.2 | 0.097x | 1.000x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 241.2 | 221.1 | 266.4 | 16.5 | 0.505x | 5.219x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 477.6 | 474.7 | 487.4 | 4.5 | 1.000x | 10.333x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 484.8 | 480.6 | 499.3 | 7.2 | 1.015x | 10.489x |

### `orig` / `s-002` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 38.5 | 38.4 | 39.0 | 0.2 | 0.078x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 38.5 | 38.4 | 38.8 | 0.2 | 0.078x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 64.8 | 63.9 | 71.0 | 2.8 | 0.132x | 1.686x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 246.9 | 238.6 | 297.3 | 21.9 | 0.502x | 6.418x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 492.1 | 473.0 | 502.2 | 11.8 | 1.000x | 12.793x |

### `orig` / `s-003` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 157.5 | 157.1 | 170.6 | 5.2 | 0.206x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 157.5 | 156.6 | 166.9 | 3.9 | 0.206x | 1.000x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 247.4 | 244.9 | 301.2 | 22.1 | 0.323x | 1.571x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 766.3 | 762.8 | 835.3 | 27.9 | 1.000x | 4.866x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 773.0 | 767.5 | 785.0 | 5.8 | 1.009x | 4.908x |

### `orig` / `s-003` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 94.0 | 93.3 | 102.2 | 3.4 | 0.122x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 147.6 | 146.9 | 147.7 | 0.3 | 0.192x | 1.570x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 147.8 | 147.6 | 150.9 | 1.2 | 0.193x | 1.573x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 277.2 | 254.3 | 337.0 | 27.6 | 0.361x | 2.950x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 767.6 | 760.5 | 806.2 | 19.2 | 1.000x | 8.170x |

### `orig` / `s-004` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 222.3 | 221.8 | 224.5 | 1.0 | 0.393x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 222.4 | 221.6 | 231.5 | 3.7 | 0.393x | 1.000x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 256.1 | 228.2 | 280.4 | 17.0 | 0.452x | 1.152x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 565.6 | 557.3 | 570.6 | 4.5 | 0.999x | 2.544x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 566.2 | 561.4 | 882.0 | 125.3 | 1.000x | 2.547x |

### `orig` / `s-004` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 93.6 | 91.0 | 99.3 | 2.8 | 0.167x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 213.5 | 213.0 | 214.2 | 0.4 | 0.380x | 2.280x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 213.7 | 213.3 | 217.8 | 1.7 | 0.381x | 2.283x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 272.8 | 245.9 | 318.3 | 24.1 | 0.486x | 2.914x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 561.6 | 559.6 | 567.7 | 3.2 | 1.000x | 5.998x |

### `orig` / `s-005` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 46.1 | 45.8 | 46.6 | 0.3 | 0.097x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 46.2 | 46.1 | 55.6 | 3.8 | 0.097x | 1.001x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 253.0 | 221.8 | 279.5 | 23.4 | 0.530x | 5.484x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 477.1 | 476.2 | 540.5 | 25.2 | 1.000x | 10.341x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 479.9 | 471.5 | 484.5 | 4.4 | 1.006x | 10.403x |

### `orig` / `s-005` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 38.3 | 38.2 | 38.5 | 0.1 | 0.081x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 38.6 | 38.3 | 49.8 | 4.4 | 0.082x | 1.006x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 67.7 | 65.4 | 71.2 | 2.3 | 0.143x | 1.764x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 275.7 | 250.2 | 289.2 | 15.2 | 0.582x | 7.189x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 473.3 | 469.4 | 487.1 | 7.1 | 1.000x | 12.343x |

### `orig` / `s-006` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 104.0 | 104.0 | 115.5 | 4.5 | 0.133x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 104.3 | 104.1 | 104.5 | 0.1 | 0.134x | 1.002x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 303.6 | 282.5 | 315.6 | 10.9 | 0.389x | 2.919x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 774.3 | 772.4 | 791.8 | 7.8 | 0.991x | 7.443x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 781.0 | 770.2 | 788.2 | 7.1 | 1.000x | 7.507x |

### `orig` / `s-006` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 88.5 | 85.1 | 91.3 | 2.3 | 0.113x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 96.4 | 96.4 | 98.4 | 0.8 | 0.123x | 1.090x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 96.9 | 96.4 | 98.8 | 0.9 | 0.124x | 1.096x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 352.6 | 293.4 | 396.7 | 33.3 | 0.450x | 3.986x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 783.2 | 777.1 | 793.4 | 5.3 | 1.000x | 8.855x |

### `orig` / `s-007` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 169.9 | 169.2 | 179.1 | 3.7 | 0.274x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 169.9 | 169.5 | 174.0 | 1.7 | 0.275x | 1.000x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 283.1 | 242.7 | 288.7 | 18.4 | 0.457x | 1.667x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 618.0 | 613.2 | 623.5 | 3.4 | 0.999x | 3.639x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 618.9 | 617.2 | 643.8 | 10.1 | 1.000x | 3.644x |

### `orig` / `s-007` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 93.2 | 90.5 | 100.3 | 3.4 | 0.150x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 162.0 | 161.7 | 164.0 | 0.8 | 0.261x | 1.739x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 162.1 | 161.2 | 162.8 | 0.5 | 0.261x | 1.740x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 302.5 | 275.2 | 323.3 | 16.4 | 0.488x | 3.247x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 620.0 | 610.3 | 622.0 | 4.9 | 1.000x | 6.655x |

### `orig` / `s-008` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 130.0 | 129.8 | 143.8 | 5.5 | 0.236x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 130.2 | 129.6 | 130.6 | 0.4 | 0.236x | 1.002x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 293.5 | 267.5 | 298.2 | 12.4 | 0.533x | 2.257x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 547.6 | 541.5 | 562.4 | 8.2 | 0.994x | 4.211x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 550.8 | 541.5 | 595.0 | 19.7 | 1.000x | 4.235x |

### `orig` / `s-008` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 83.2 | 80.2 | 87.1 | 2.3 | 0.154x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 122.4 | 122.0 | 122.7 | 0.3 | 0.227x | 1.470x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 123.2 | 122.0 | 131.8 | 3.6 | 0.229x | 1.481x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 285.1 | 261.1 | 313.0 | 18.8 | 0.529x | 3.426x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 539.2 | 538.5 | 547.2 | 3.7 | 1.000x | 6.480x |

### `orig` / `s-009` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 97.0 | 96.7 | 111.8 | 6.0 | 0.181x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 97.5 | 97.3 | 98.0 | 0.3 | 0.182x | 1.005x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 288.4 | 262.1 | 296.1 | 12.4 | 0.537x | 2.973x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 537.0 | 531.7 | 541.7 | 3.3 | 1.000x | 5.534x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 537.8 | 534.5 | 542.8 | 3.3 | 1.001x | 5.542x |

### `orig` / `s-009` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 77.8 | 75.5 | 83.0 | 2.7 | 0.145x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 89.8 | 89.5 | 90.2 | 0.3 | 0.168x | 1.154x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 90.2 | 89.8 | 90.8 | 0.3 | 0.169x | 1.159x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 284.9 | 255.7 | 308.0 | 16.7 | 0.532x | 3.660x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 535.2 | 531.6 | 584.2 | 19.9 | 1.000x | 6.877x |

### `orig` / `s-010` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 97.3 | 96.9 | 107.5 | 4.2 | 0.221x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 97.7 | 97.2 | 102.7 | 2.5 | 0.222x | 1.005x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 264.9 | 258.3 | 270.5 | 4.0 | 0.601x | 2.724x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 438.2 | 436.3 | 442.0 | 2.1 | 0.995x | 4.506x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 440.5 | 436.4 | 441.5 | 2.3 | 1.000x | 4.530x |

### `orig` / `s-010` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 73.1 | 69.3 | 75.5 | 2.2 | 0.167x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 89.6 | 89.5 | 90.0 | 0.2 | 0.205x | 1.225x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 90.8 | 89.3 | 91.6 | 0.8 | 0.208x | 1.241x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 244.4 | 232.4 | 253.7 | 9.1 | 0.560x | 3.343x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 436.9 | 430.2 | 451.0 | 6.9 | 1.000x | 5.974x |

### `orig` / `s-011` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 69.5 | 69.4 | 70.1 | 0.3 | 0.200x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 69.6 | 69.3 | 81.9 | 4.9 | 0.200x | 1.001x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 308.4 | 273.8 | 328.8 | 18.1 | 0.888x | 4.438x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 343.1 | 342.4 | 357.5 | 5.8 | 0.988x | 4.938x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 347.3 | 342.6 | 351.3 | 2.8 | 1.000x | 4.999x |

### `orig` / `s-011` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 63.6 | 63.4 | 64.9 | 0.6 | 0.036x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 63.7 | 63.4 | 64.7 | 0.5 | 0.036x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 142.2 | 140.5 | 153.3 | 4.8 | 0.081x | 2.235x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 583.5 | 550.3 | 590.8 | 14.8 | 0.331x | 9.168x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,762.3 | 1,752.3 | 1,794.8 | 15.3 | 1.000x | 27.691x |

### `orig` / `s-012` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 123.6 | 123.4 | 126.9 | 1.3 | 0.180x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 123.8 | 123.3 | 134.5 | 5.0 | 0.181x | 1.001x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 306.5 | 274.5 | 356.2 | 27.4 | 0.447x | 2.479x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 681.1 | 665.0 | 699.7 | 11.1 | 0.994x | 5.509x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 685.5 | 679.9 | 697.5 | 6.2 | 1.000x | 5.545x |

### `orig` / `s-012` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 85.9 | 82.3 | 92.3 | 3.4 | 0.126x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 115.1 | 114.9 | 120.2 | 2.0 | 0.169x | 1.340x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 115.3 | 115.2 | 115.9 | 0.3 | 0.170x | 1.341x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 307.5 | 286.1 | 329.4 | 14.5 | 0.452x | 3.578x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 679.6 | 675.5 | 689.6 | 4.9 | 1.000x | 7.909x |

### `orig` / `s-013` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 123.5 | 123.4 | 134.2 | 4.3 | 0.181x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 123.6 | 123.5 | 123.7 | 0.1 | 0.181x | 1.000x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 306.7 | 268.7 | 348.1 | 25.9 | 0.449x | 2.483x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 683.3 | 680.3 | 697.9 | 7.5 | 1.000x | 5.531x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 684.0 | 676.5 | 685.1 | 3.5 | 1.001x | 5.536x |

### `orig` / `s-013` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 86.4 | 82.5 | 96.6 | 5.1 | 0.126x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 115.2 | 114.9 | 116.8 | 0.7 | 0.168x | 1.332x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 115.5 | 115.3 | 119.5 | 1.6 | 0.169x | 1.337x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 309.6 | 278.9 | 332.4 | 17.2 | 0.452x | 3.581x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 684.9 | 675.9 | 690.8 | 4.9 | 1.000x | 7.924x |

### `orig` / `s-014` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 97.2 | 97.1 | 98.0 | 0.3 | 0.181x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 97.3 | 97.0 | 113.6 | 6.5 | 0.181x | 1.001x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 293.9 | 267.8 | 298.7 | 11.3 | 0.547x | 3.025x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 536.8 | 529.1 | 541.9 | 4.2 | 1.000x | 5.525x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 539.1 | 533.9 | 552.2 | 6.1 | 1.004x | 5.549x |

### `orig` / `s-014` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 78.5 | 76.6 | 87.7 | 3.9 | 0.147x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 89.9 | 89.8 | 90.8 | 0.4 | 0.168x | 1.145x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 89.9 | 89.8 | 90.9 | 0.4 | 0.168x | 1.145x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 327.4 | 292.0 | 372.6 | 26.6 | 0.611x | 4.168x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 535.7 | 528.3 | 540.9 | 4.3 | 1.000x | 6.820x |

### `orig` / `s-015` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 117.2 | 116.9 | 118.5 | 0.6 | 0.178x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 118.5 | 117.0 | 128.2 | 5.1 | 0.180x | 1.011x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 301.6 | 285.1 | 323.9 | 14.6 | 0.459x | 2.574x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 656.6 | 646.9 | 688.3 | 14.8 | 1.000x | 5.603x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 658.5 | 651.5 | 690.0 | 14.0 | 1.003x | 5.619x |

### `orig` / `s-015` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 85.2 | 80.9 | 90.8 | 3.6 | 0.130x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 109.7 | 109.4 | 110.0 | 0.2 | 0.167x | 1.288x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 109.8 | 109.6 | 109.9 | 0.1 | 0.167x | 1.289x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 303.2 | 281.3 | 325.2 | 14.8 | 0.462x | 3.560x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 657.0 | 648.5 | 660.3 | 4.0 | 1.000x | 7.713x |

### `orig` / `s-016` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 52.9 | 52.7 | 58.9 | 2.4 | 0.286x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 53.0 | 52.4 | 54.9 | 0.9 | 0.287x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 184.6 | 183.0 | 199.7 | 6.2 | 0.999x | 3.488x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 184.8 | 183.8 | 189.9 | 2.1 | 1.000x | 3.493x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 291.5 | 271.4 | 307.1 | 11.6 | 1.577x | 5.510x |

### `orig` / `s-016` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 47.3 | 47.1 | 48.0 | 0.3 | 0.044x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 47.4 | 47.2 | 48.2 | 0.4 | 0.044x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 114.4 | 110.3 | 121.2 | 4.1 | 0.106x | 2.419x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 470.8 | 447.0 | 490.7 | 14.2 | 0.435x | 9.956x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,082.9 | 1,074.3 | 1,088.0 | 5.0 | 1.000x | 22.901x |

### `orig` / `s-017` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 123.7 | 123.3 | 124.5 | 0.4 | 0.183x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 123.7 | 123.2 | 139.4 | 6.3 | 0.183x | 1.000x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 321.5 | 292.8 | 339.6 | 17.6 | 0.475x | 2.599x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 668.4 | 665.8 | 709.9 | 16.7 | 0.987x | 5.404x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 677.0 | 669.5 | 683.3 | 4.7 | 1.000x | 5.473x |

### `orig` / `s-017` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 86.4 | 82.5 | 91.9 | 3.3 | 0.126x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 115.2 | 115.1 | 116.1 | 0.4 | 0.169x | 1.333x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 115.8 | 115.2 | 116.9 | 0.6 | 0.169x | 1.340x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 307.6 | 295.2 | 325.7 | 10.5 | 0.450x | 3.561x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 683.2 | 678.7 | 686.4 | 3.0 | 1.000x | 7.908x |

### `orig` / `s-018` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 117.5 | 117.3 | 140.9 | 9.3 | 0.179x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 117.8 | 116.9 | 123.8 | 2.6 | 0.179x | 1.002x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 312.3 | 268.1 | 331.3 | 21.9 | 0.475x | 2.658x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 649.8 | 644.5 | 658.6 | 5.2 | 0.989x | 5.529x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 657.0 | 652.9 | 667.6 | 5.3 | 1.000x | 5.590x |

### `orig` / `s-018` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 83.8 | 79.9 | 89.9 | 3.3 | 0.128x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 109.6 | 109.5 | 112.4 | 1.1 | 0.167x | 1.309x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 109.7 | 109.6 | 111.2 | 0.6 | 0.167x | 1.310x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 306.0 | 279.9 | 323.8 | 14.3 | 0.467x | 3.652x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 655.7 | 646.7 | 664.0 | 6.5 | 1.000x | 7.826x |

### `orig` / `s-019` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 56.3 | 56.2 | 57.0 | 0.3 | 0.293x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 56.4 | 56.2 | 56.7 | 0.1 | 0.294x | 1.003x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 191.9 | 191.0 | 194.4 | 1.2 | 1.000x | 3.411x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 193.1 | 191.9 | 206.7 | 5.5 | 1.006x | 3.433x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 288.9 | 241.3 | 310.6 | 24.4 | 1.505x | 5.134x |

### `orig` / `s-019` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 50.7 | 50.3 | 52.1 | 0.7 | 0.047x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 50.8 | 50.4 | 51.3 | 0.3 | 0.047x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 112.2 | 110.3 | 115.6 | 1.8 | 0.103x | 2.215x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 483.1 | 474.1 | 498.5 | 8.8 | 0.445x | 9.536x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,085.4 | 1,082.7 | 1,089.5 | 2.4 | 1.000x | 21.425x |

### `orig` / `s-020` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 136.9 | 136.5 | 138.2 | 0.6 | 0.201x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 136.9 | 136.7 | 146.5 | 3.9 | 0.201x | 1.000x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 333.3 | 318.0 | 351.2 | 11.4 | 0.489x | 2.435x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 682.0 | 679.1 | 690.7 | 4.1 | 1.000x | 4.983x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 686.0 | 677.0 | 688.9 | 4.2 | 1.006x | 5.013x |

### `orig` / `s-020` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 89.3 | 85.5 | 96.0 | 3.6 | 0.130x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 129.1 | 129.0 | 130.3 | 0.5 | 0.187x | 1.445x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 129.3 | 129.0 | 131.3 | 1.0 | 0.188x | 1.448x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 324.7 | 286.3 | 331.9 | 16.8 | 0.471x | 3.636x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 689.3 | 673.2 | 694.2 | 7.2 | 1.000x | 7.717x |

### `orig` / `s-021` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 97.1 | 96.9 | 111.9 | 5.9 | 0.137x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 97.2 | 96.4 | 107.3 | 4.1 | 0.138x | 1.001x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 294.0 | 268.5 | 307.8 | 12.9 | 0.416x | 3.029x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 703.8 | 696.4 | 723.1 | 9.3 | 0.996x | 7.250x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 706.4 | 698.1 | 707.7 | 3.7 | 1.000x | 7.277x |

### `orig` / `s-021` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 89.7 | 89.4 | 90.4 | 0.4 | 0.127x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 89.8 | 89.6 | 90.0 | 0.1 | 0.128x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 91.8 | 90.1 | 101.0 | 4.3 | 0.130x | 1.023x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 286.2 | 261.8 | 307.7 | 15.5 | 0.407x | 3.192x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 703.4 | 699.9 | 710.3 | 3.8 | 1.000x | 7.844x |

### `orig` / `s-022` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 149.9 | 149.8 | 163.8 | 5.5 | 0.334x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 150.4 | 150.0 | 155.6 | 2.1 | 0.335x | 1.003x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 286.9 | 254.5 | 296.4 | 14.4 | 0.639x | 1.914x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 448.5 | 447.1 | 450.6 | 1.3 | 0.999x | 2.992x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 448.8 | 447.0 | 452.2 | 1.9 | 1.000x | 2.994x |

### `orig` / `s-022` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 73.9 | 71.1 | 79.0 | 2.9 | 0.164x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 142.4 | 142.3 | 143.1 | 0.3 | 0.316x | 1.928x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 142.5 | 142.1 | 142.8 | 0.2 | 0.316x | 1.929x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 283.2 | 250.2 | 287.8 | 16.0 | 0.627x | 3.834x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 451.4 | 446.4 | 451.9 | 2.5 | 1.000x | 6.112x |

### `orig` / `s-023` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 124.5 | 123.5 | 132.9 | 3.6 | 0.186x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 124.9 | 123.4 | 128.6 | 1.8 | 0.187x | 1.003x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 293.2 | 267.8 | 296.2 | 10.9 | 0.439x | 2.355x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 666.8 | 665.0 | 672.8 | 3.0 | 0.998x | 5.357x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 667.9 | 662.2 | 671.5 | 3.2 | 1.000x | 5.366x |

### `orig` / `s-023` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 86.6 | 83.2 | 95.2 | 4.3 | 0.130x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 115.4 | 115.0 | 119.5 | 1.7 | 0.173x | 1.333x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 115.7 | 115.0 | 116.3 | 0.5 | 0.173x | 1.336x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 281.9 | 273.3 | 292.4 | 7.1 | 0.422x | 3.255x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 667.3 | 662.5 | 671.8 | 3.6 | 1.000x | 7.706x |

### `orig` / `s-024` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 97.4 | 96.9 | 111.4 | 5.6 | 0.136x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 97.8 | 96.8 | 106.6 | 3.6 | 0.137x | 1.004x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 292.5 | 270.0 | 294.8 | 9.2 | 0.409x | 3.002x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 712.9 | 708.3 | 718.3 | 3.6 | 0.996x | 7.317x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 715.7 | 709.0 | 742.6 | 11.7 | 1.000x | 7.346x |

### `orig` / `s-024` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 89.9 | 89.3 | 97.4 | 3.1 | 0.127x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 90.1 | 89.3 | 94.1 | 1.7 | 0.127x | 1.002x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 90.3 | 89.6 | 93.6 | 1.4 | 0.128x | 1.005x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 313.9 | 264.9 | 325.1 | 21.9 | 0.444x | 3.492x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 707.4 | 699.3 | 714.6 | 4.9 | 1.000x | 7.868x |

### `orig` / `s-025` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 123.7 | 123.3 | 124.9 | 0.6 | 0.170x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 123.8 | 123.4 | 132.9 | 3.7 | 0.170x | 1.000x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 298.1 | 276.3 | 306.6 | 10.4 | 0.410x | 2.409x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 724.4 | 720.7 | 737.0 | 6.0 | 0.997x | 5.854x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 726.7 | 724.5 | 735.3 | 4.3 | 1.000x | 5.872x |

### `orig` / `s-025` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 84.6 | 84.2 | 91.8 | 3.4 | 0.116x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 115.3 | 115.0 | 117.5 | 0.9 | 0.158x | 1.362x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 115.3 | 115.2 | 117.7 | 0.9 | 0.158x | 1.362x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 288.9 | 267.9 | 337.4 | 24.7 | 0.396x | 3.413x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 728.9 | 721.5 | 731.5 | 3.5 | 1.000x | 8.611x |

### `orig` / `s-026` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 150.3 | 149.7 | 152.2 | 0.9 | 0.334x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 150.4 | 149.5 | 155.8 | 2.3 | 0.334x | 1.000x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 282.9 | 254.2 | 287.4 | 11.9 | 0.629x | 1.882x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 447.9 | 445.6 | 455.9 | 3.7 | 0.996x | 2.979x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 449.6 | 442.4 | 452.2 | 4.1 | 1.000x | 2.991x |

### `orig` / `s-026` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 72.8 | 71.6 | 78.8 | 2.7 | 0.162x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 142.9 | 142.2 | 159.0 | 6.5 | 0.319x | 1.964x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 143.8 | 142.7 | 144.1 | 0.5 | 0.321x | 1.977x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 290.2 | 257.3 | 299.4 | 14.8 | 0.648x | 3.988x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 448.0 | 446.4 | 451.5 | 1.7 | 1.000x | 6.156x |

### `orig` / `s-027` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 150.3 | 150.1 | 153.2 | 1.2 | 0.237x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 150.3 | 149.8 | 159.5 | 3.7 | 0.237x | 1.000x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 295.7 | 272.9 | 311.4 | 12.4 | 0.467x | 1.968x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 630.6 | 626.1 | 634.9 | 3.1 | 0.996x | 4.196x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 633.4 | 627.1 | 634.9 | 2.8 | 1.000x | 4.215x |

### `orig` / `s-027` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 84.6 | 82.0 | 93.4 | 4.2 | 0.134x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 142.5 | 142.5 | 149.6 | 2.8 | 0.225x | 1.684x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 143.4 | 142.2 | 144.6 | 0.9 | 0.226x | 1.695x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 277.8 | 271.8 | 297.5 | 9.3 | 0.438x | 3.283x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 633.9 | 627.4 | 639.1 | 4.1 | 1.000x | 7.490x |

### `orig` / `s-028` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 43.7 | 43.7 | 44.2 | 0.2 | 0.146x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 44.0 | 43.7 | 48.5 | 1.8 | 0.147x | 1.005x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 287.6 | 262.7 | 295.1 | 11.0 | 0.963x | 6.577x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 297.1 | 293.5 | 299.0 | 1.9 | 0.995x | 6.795x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 298.6 | 296.4 | 310.1 | 4.9 | 1.000x | 6.829x |

### `orig` / `s-028` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 37.7 | 37.7 | 38.5 | 0.3 | 0.035x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 37.8 | 37.5 | 37.8 | 0.1 | 0.035x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 75.3 | 67.3 | 79.4 | 4.5 | 0.070x | 1.995x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 503.9 | 490.8 | 526.6 | 12.2 | 0.469x | 13.351x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,075.0 | 1,069.9 | 1,079.6 | 3.6 | 1.000x | 28.486x |

### `orig` / `s-029` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 89.5 | 89.1 | 89.5 | 0.2 | 0.298x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 89.6 | 89.2 | 94.0 | 1.8 | 0.298x | 1.001x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 283.5 | 254.2 | 294.7 | 13.9 | 0.944x | 3.168x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 295.7 | 293.5 | 306.4 | 4.7 | 0.985x | 3.304x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 300.3 | 293.7 | 302.1 | 3.0 | 1.000x | 3.356x |

### `orig` / `s-029` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 72.8 | 69.8 | 78.7 | 3.2 | 0.068x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 83.1 | 82.9 | 83.2 | 0.1 | 0.078x | 1.142x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 83.2 | 83.0 | 83.4 | 0.1 | 0.078x | 1.143x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 847.1 | 838.8 | 955.4 | 44.4 | 0.792x | 11.640x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,069.3 | 1,058.7 | 1,084.4 | 8.6 | 1.000x | 14.694x |

### `orig` / `s-030` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 43.5 | 43.4 | 43.9 | 0.2 | 0.145x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 44.0 | 43.4 | 48.1 | 1.7 | 0.147x | 1.012x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 286.8 | 257.5 | 294.0 | 12.9 | 0.956x | 6.590x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 295.0 | 294.6 | 323.5 | 12.2 | 0.984x | 6.777x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 299.9 | 294.1 | 318.8 | 8.8 | 1.000x | 6.890x |

### `orig` / `s-030` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 37.3 | 37.3 | 37.5 | 0.1 | 0.035x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 37.5 | 37.3 | 37.9 | 0.2 | 0.035x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 69.8 | 67.5 | 78.1 | 4.2 | 0.066x | 1.871x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 526.2 | 521.4 | 550.1 | 11.0 | 0.495x | 14.101x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,063.0 | 1,057.2 | 1,065.7 | 3.1 | 1.000x | 28.483x |

### `orig` / `s-031` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 59.9 | 59.6 | 64.8 | 2.0 | 0.201x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 59.9 | 59.9 | 60.0 | 0.0 | 0.201x | 1.000x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 286.4 | 256.7 | 291.3 | 12.7 | 0.962x | 4.778x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 295.9 | 291.5 | 367.2 | 28.8 | 0.994x | 4.937x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 297.7 | 293.5 | 301.3 | 2.6 | 1.000x | 4.967x |

### `orig` / `s-031` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 53.4 | 53.2 | 53.7 | 0.2 | 0.050x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 53.6 | 53.2 | 53.9 | 0.3 | 0.050x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 72.6 | 70.4 | 79.2 | 3.2 | 0.068x | 1.359x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 608.0 | 589.8 | 632.5 | 17.4 | 0.573x | 11.376x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,061.8 | 1,056.0 | 1,071.7 | 5.1 | 1.000x | 19.868x |

### `orig` / `s-032` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 50.6 | 49.9 | 54.7 | 1.7 | 0.141x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 50.7 | 50.4 | 51.1 | 0.3 | 0.141x | 1.000x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 283.1 | 258.2 | 294.1 | 12.4 | 0.786x | 5.590x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 357.4 | 352.5 | 360.9 | 3.2 | 0.993x | 7.058x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 360.0 | 354.5 | 362.2 | 2.7 | 1.000x | 7.110x |

### `orig` / `s-032` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 43.9 | 43.7 | 45.2 | 0.6 | 0.034x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 44.0 | 43.7 | 44.3 | 0.2 | 0.034x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 72.0 | 71.2 | 80.4 | 3.5 | 0.055x | 1.639x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 620.3 | 607.5 | 632.2 | 8.7 | 0.475x | 14.120x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,304.8 | 1,297.2 | 1,309.1 | 4.2 | 1.000x | 29.701x |

### `orig` / `s-033` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 50.4 | 50.0 | 51.5 | 0.5 | 0.161x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 50.6 | 49.8 | 54.3 | 1.6 | 0.161x | 1.003x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 288.5 | 255.6 | 302.2 | 16.0 | 0.919x | 5.720x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 311.7 | 308.3 | 325.9 | 6.4 | 0.993x | 6.181x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 313.8 | 312.0 | 314.9 | 1.2 | 1.000x | 6.223x |

### `orig` / `s-033` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 43.7 | 43.7 | 44.4 | 0.3 | 0.039x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 43.9 | 43.9 | 44.2 | 0.1 | 0.039x | 1.005x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 71.5 | 69.7 | 79.5 | 3.7 | 0.063x | 1.636x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 602.4 | 575.9 | 624.2 | 15.9 | 0.531x | 13.790x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,134.2 | 1,128.3 | 1,139.4 | 4.0 | 1.000x | 25.962x |

### `orig` / `s-034` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 36.8 | 36.5 | 39.9 | 1.3 | 0.064x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 36.8 | 36.7 | 37.3 | 0.2 | 0.064x | 1.000x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 285.3 | 259.0 | 295.8 | 12.9 | 0.494x | 7.747x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 575.1 | 571.0 | 585.1 | 5.1 | 0.995x | 15.619x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 577.8 | 570.3 | 590.4 | 7.0 | 1.000x | 15.692x |

### `orig` / `s-034` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 30.9 | 30.9 | 31.4 | 0.2 | 0.014x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 31.7 | 31.0 | 32.0 | 0.4 | 0.015x | 1.025x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 97.7 | 97.6 | 103.0 | 2.1 | 0.045x | 3.162x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 425.2 | 383.3 | 431.7 | 18.1 | 0.196x | 13.755x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,175.1 | 2,161.7 | 2,194.1 | 11.1 | 1.000x | 70.356x |

### `orig` / `s-035` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 50.2 | 49.9 | 50.5 | 0.2 | 0.063x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 50.4 | 50.2 | 59.0 | 3.4 | 0.063x | 1.004x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 356.4 | 322.0 | 382.4 | 21.6 | 0.445x | 7.100x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 795.0 | 786.9 | 846.5 | 21.6 | 0.992x | 15.838x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 801.4 | 792.1 | 803.8 | 4.8 | 1.000x | 15.965x |

### `orig` / `s-035` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 43.9 | 43.7 | 45.8 | 0.8 | 0.015x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 44.0 | 43.3 | 45.2 | 0.6 | 0.015x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 135.3 | 133.7 | 137.2 | 1.3 | 0.045x | 3.085x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 920.7 | 895.3 | 945.9 | 21.0 | 0.308x | 20.989x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,986.8 | 2,974.3 | 3,023.3 | 18.9 | 1.000x | 68.090x |

### `orig` / `s-036` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 53.1 | 53.0 | 53.4 | 0.2 | 0.256x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 53.1 | 52.7 | 61.0 | 3.2 | 0.256x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 206.3 | 204.8 | 211.5 | 2.3 | 0.996x | 3.888x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 207.2 | 205.3 | 211.5 | 2.3 | 1.000x | 3.904x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 286.3 | 257.3 | 291.7 | 12.3 | 1.382x | 5.396x |

### `orig` / `s-036` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 47.3 | 47.3 | 48.6 | 0.5 | 0.065x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 47.6 | 47.3 | 48.2 | 0.3 | 0.065x | 1.006x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.1 | 65.2 | 76.8 | 4.2 | 0.094x | 1.439x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 475.1 | 453.5 | 498.2 | 16.4 | 0.653x | 10.040x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 727.4 | 718.0 | 746.0 | 9.6 | 1.000x | 15.369x |

### `orig` / `s-037` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 40.1 | 39.9 | 40.7 | 0.4 | 0.118x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 40.7 | 40.4 | 48.0 | 2.9 | 0.120x | 1.017x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 280.4 | 240.7 | 300.4 | 20.5 | 0.824x | 7.000x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 340.4 | 339.4 | 340.9 | 0.6 | 1.000x | 8.497x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 340.8 | 335.8 | 345.3 | 3.4 | 1.001x | 8.507x |

### `orig` / `s-037` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 34.6 | 34.5 | 34.9 | 0.2 | 0.029x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 34.7 | 34.6 | 34.9 | 0.1 | 0.029x | 1.005x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 70.9 | 68.6 | 81.2 | 4.6 | 0.059x | 2.051x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 529.9 | 526.0 | 559.9 | 12.6 | 0.438x | 15.337x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,209.5 | 1,204.4 | 1,235.9 | 11.4 | 1.000x | 35.005x |

### `orig` / `s-038` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 53.1 | 53.0 | 55.3 | 0.9 | 0.107x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 53.3 | 52.9 | 62.1 | 3.6 | 0.107x | 1.003x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 307.6 | 275.6 | 320.7 | 15.5 | 0.620x | 5.790x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 496.4 | 483.0 | 499.2 | 6.4 | 1.000x | 9.346x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 500.1 | 489.2 | 703.4 | 82.4 | 1.007x | 9.415x |

### `orig` / `s-038` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 47.5 | 47.3 | 51.0 | 1.4 | 0.026x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 47.6 | 47.4 | 48.4 | 0.4 | 0.026x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 93.7 | 90.4 | 99.9 | 3.4 | 0.052x | 1.972x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 685.6 | 660.8 | 726.2 | 21.7 | 0.377x | 14.422x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,817.4 | 1,800.6 | 1,821.2 | 8.1 | 1.000x | 38.232x |

### `orig` / `s-039` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 110.5 | 110.4 | 121.6 | 4.4 | 0.532x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 110.9 | 110.6 | 119.6 | 3.5 | 0.534x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 204.4 | 203.6 | 213.0 | 3.5 | 0.983x | 1.850x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 207.8 | 203.5 | 209.7 | 2.5 | 1.000x | 1.881x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 291.8 | 255.0 | 298.5 | 15.8 | 1.404x | 2.640x |

### `orig` / `s-039` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 105.4 | 105.1 | 106.1 | 0.4 | 0.112x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 105.9 | 105.2 | 111.0 | 2.2 | 0.113x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 108.0 | 106.3 | 113.9 | 2.7 | 0.115x | 1.025x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 351.5 | 330.7 | 374.7 | 15.3 | 0.375x | 3.334x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 937.4 | 927.1 | 948.2 | 6.9 | 1.000x | 8.890x |

### `orig` / `s-040` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 34.1 | 34.0 | 35.0 | 0.4 | 0.955x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 35.7 | 34.3 | 38.6 | 1.8 | 1.000x | 1.047x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 46.8 | 46.4 | 46.9 | 0.2 | 1.310x | 1.371x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 46.8 | 46.7 | 47.0 | 0.1 | 1.313x | 1.374x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 244.9 | 230.2 | 263.9 | 12.2 | 6.861x | 7.182x |

### `orig` / `s-040` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 35.1 | 34.9 | 40.7 | 2.3 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 38.6 | 36.3 | 49.0 | 4.9 | 1.099x | 1.099x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 40.3 | 40.1 | 40.7 | 0.2 | 1.149x | 1.149x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 40.4 | 40.0 | 43.0 | 1.1 | 1.152x | 1.152x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 457.2 | 442.8 | 481.3 | 13.3 | 13.022x | 13.022x |

### `orig` / `s-041` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.0 | 28.9 | 31.2 | 0.9 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.3 | 29.1 | 29.4 | 0.1 | 1.010x | 1.010x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 34.3 | 33.9 | 35.1 | 0.4 | 1.184x | 1.184x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.5 | 34.2 | 39.2 | 1.9 | 1.192x | 1.192x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 261.3 | 246.8 | 263.0 | 7.3 | 9.019x | 9.019x |

### `orig` / `s-041` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 29.2 | 29.2 | 29.5 | 0.1 | 0.798x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 29.4 | 29.3 | 30.2 | 0.3 | 0.804x | 1.007x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 36.6 | 35.8 | 42.0 | 2.3 | 1.000x | 1.253x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 41.7 | 36.6 | 50.1 | 4.5 | 1.140x | 1.428x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 370.8 | 358.4 | 446.5 | 31.7 | 10.137x | 12.702x |

### `orig` / `s-042` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 17.3 | 17.3 | 17.5 | 0.1 | 0.084x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 17.4 | 17.3 | 18.9 | 0.6 | 0.084x | 1.005x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 207.5 | 204.1 | 212.0 | 2.8 | 1.000x | 11.963x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 207.6 | 205.3 | 210.0 | 1.5 | 1.001x | 11.970x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 264.2 | 240.2 | 277.2 | 13.6 | 1.273x | 15.229x |

### `orig` / `s-042` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 12.7 | 12.6 | 13.0 | 0.1 | 0.059x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 12.7 | 12.6 | 14.9 | 0.9 | 0.059x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 53.6 | 52.1 | 60.9 | 3.8 | 0.248x | 4.225x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 216.1 | 214.4 | 217.5 | 1.0 | 1.000x | 17.028x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 312.8 | 289.0 | 334.9 | 16.3 | 1.447x | 24.642x |

### `orig` / `s-043` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 130.2 | 130.1 | 130.5 | 0.2 | 0.837x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 130.2 | 130.0 | 138.9 | 3.5 | 0.838x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 151.8 | 149.0 | 153.5 | 1.6 | 0.976x | 1.166x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 155.5 | 151.7 | 158.1 | 2.3 | 1.000x | 1.194x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 264.7 | 253.3 | 270.5 | 6.2 | 1.702x | 2.033x |

### `orig` / `s-043` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 103.7 | 98.2 | 108.7 | 4.0 | 0.097x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 124.3 | 124.0 | 124.4 | 0.2 | 0.117x | 1.199x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 124.5 | 124.3 | 125.4 | 0.4 | 0.117x | 1.200x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 369.0 | 351.6 | 393.5 | 13.7 | 0.347x | 3.557x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,064.0 | 1,061.3 | 1,077.5 | 7.1 | 1.000x | 10.257x |

### `orig` / `s-044` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.2 | 29.0 | 30.9 | 0.7 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.6 | 29.1 | 33.3 | 1.5 | 1.015x | 1.015x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 111.9 | 111.1 | 112.2 | 0.4 | 3.833x | 3.833x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 112.2 | 111.4 | 120.4 | 3.4 | 3.842x | 3.842x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 256.3 | 241.4 | 285.9 | 14.6 | 8.774x | 8.774x |

### `orig` / `s-044` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 79.2 | 77.9 | 87.7 | 4.1 | 0.147x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 107.2 | 106.7 | 110.9 | 1.5 | 0.199x | 1.353x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 107.3 | 106.9 | 107.7 | 0.3 | 0.199x | 1.354x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 298.4 | 269.2 | 309.6 | 13.4 | 0.554x | 3.766x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 539.0 | 532.3 | 544.3 | 5.1 | 1.000x | 6.803x |

### `orig` / `s-045` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 49.8 | 49.7 | 50.6 | 0.3 | 0.325x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 49.8 | 49.7 | 51.2 | 0.6 | 0.325x | 1.001x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 153.2 | 151.3 | 159.9 | 3.4 | 1.000x | 3.079x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 153.8 | 149.5 | 157.4 | 2.8 | 1.003x | 3.090x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 265.5 | 252.3 | 278.9 | 9.9 | 1.733x | 5.337x |

### `orig` / `s-045` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 43.9 | 43.7 | 45.0 | 0.4 | 0.087x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 44.0 | 43.9 | 45.3 | 0.5 | 0.087x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 66.2 | 64.2 | 76.4 | 4.7 | 0.131x | 1.508x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 467.0 | 435.7 | 472.2 | 13.2 | 0.922x | 10.637x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 506.6 | 493.9 | 509.6 | 6.3 | 1.000x | 11.537x |

### `orig` / `s-046` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 36.5 | 36.3 | 36.7 | 0.1 | 0.078x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 36.6 | 36.2 | 38.9 | 1.0 | 0.078x | 1.002x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 292.4 | 257.5 | 298.7 | 14.9 | 0.622x | 8.002x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 469.8 | 467.0 | 501.2 | 12.6 | 1.000x | 12.856x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 472.6 | 465.5 | 485.3 | 7.1 | 1.006x | 12.933x |

### `orig` / `s-046` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 31.1 | 31.0 | 31.7 | 0.3 | 0.018x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 31.1 | 30.9 | 31.4 | 0.2 | 0.018x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 86.2 | 85.1 | 95.3 | 4.1 | 0.050x | 2.774x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 545.0 | 523.4 | 549.8 | 9.5 | 0.314x | 17.542x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,738.2 | 1,725.1 | 1,747.2 | 7.6 | 1.000x | 55.943x |

### `orig` / `s-047` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 39.8 | 39.7 | 40.3 | 0.2 | 0.050x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 40.6 | 39.6 | 45.9 | 2.3 | 0.051x | 1.019x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 285.4 | 256.3 | 291.7 | 12.6 | 0.361x | 7.166x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 789.4 | 786.3 | 794.1 | 2.8 | 0.998x | 19.818x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 790.8 | 777.6 | 792.6 | 5.5 | 1.000x | 19.854x |

### `orig` / `s-047` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 34.4 | 34.3 | 34.8 | 0.2 | 0.011x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 34.5 | 34.3 | 35.2 | 0.3 | 0.011x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 119.8 | 118.0 | 127.8 | 3.4 | 0.040x | 3.484x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 414.7 | 400.7 | 418.1 | 6.3 | 0.137x | 12.066x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,029.7 | 3,014.9 | 3,046.7 | 11.5 | 1.000x | 88.142x |

### `orig` / `s-048` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 22.2 | 22.1 | 22.4 | 0.1 | 0.074x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 22.3 | 22.3 | 24.2 | 0.8 | 0.075x | 1.005x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 272.5 | 236.7 | 284.6 | 16.7 | 0.914x | 12.266x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 295.6 | 294.5 | 300.2 | 2.3 | 0.991x | 13.307x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 298.2 | 295.0 | 335.8 | 15.5 | 1.000x | 13.424x |

### `orig` / `s-048` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.8 | 0.3 | 0.022x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 18.1 | 17.9 | 18.7 | 0.3 | 0.022x | 1.008x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.2 | 62.5 | 70.6 | 2.8 | 0.085x | 3.801x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 322.3 | 286.3 | 336.8 | 16.9 | 0.401x | 17.966x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 804.5 | 802.4 | 811.9 | 4.2 | 1.000x | 44.840x |

### `orig` / `s-049` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 126.6 | 126.5 | 127.1 | 0.2 | 0.870x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 127.0 | 126.4 | 135.9 | 3.6 | 0.872x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 144.4 | 143.0 | 148.5 | 1.9 | 0.992x | 1.141x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 145.6 | 144.1 | 146.6 | 1.0 | 1.000x | 1.150x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 273.4 | 254.4 | 280.0 | 8.7 | 1.878x | 2.160x |

### `orig` / `s-049` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 98.3 | 97.4 | 111.0 | 5.3 | 0.096x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 121.2 | 120.8 | 125.5 | 1.8 | 0.118x | 1.233x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 121.5 | 121.0 | 122.1 | 0.4 | 0.118x | 1.236x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 351.0 | 328.4 | 356.8 | 10.2 | 0.341x | 3.571x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,028.0 | 1,018.4 | 1,047.6 | 10.5 | 1.000x | 10.459x |

### `orig` / `s-050` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 100.6 | 100.3 | 101.2 | 0.3 | 0.332x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 102.0 | 100.7 | 110.0 | 3.5 | 0.337x | 1.014x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 288.3 | 252.3 | 293.4 | 14.9 | 0.953x | 2.866x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 302.1 | 300.2 | 303.8 | 1.3 | 0.998x | 3.003x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 302.5 | 297.7 | 305.0 | 2.5 | 1.000x | 3.008x |

### `orig` / `s-050` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 95.2 | 94.9 | 96.0 | 0.4 | 0.058x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 95.2 | 94.8 | 95.4 | 0.2 | 0.058x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 108.1 | 103.8 | 120.1 | 6.0 | 0.066x | 1.135x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 457.2 | 440.6 | 487.9 | 18.8 | 0.279x | 4.803x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,639.3 | 1,630.1 | 1,648.7 | 7.3 | 1.000x | 17.220x |

### `orig` / `s-051` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 126.6 | 126.5 | 127.0 | 0.2 | 0.880x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 127.2 | 126.5 | 135.6 | 3.4 | 0.884x | 1.005x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 143.1 | 141.6 | 150.4 | 3.2 | 0.995x | 1.131x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 143.8 | 140.3 | 146.7 | 2.1 | 1.000x | 1.136x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 271.1 | 253.9 | 279.5 | 8.8 | 1.885x | 2.141x |

### `orig` / `s-051` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 98.9 | 97.5 | 119.7 | 8.4 | 0.097x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 121.1 | 120.9 | 124.9 | 1.5 | 0.118x | 1.224x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 121.2 | 121.1 | 122.3 | 0.5 | 0.118x | 1.225x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 350.5 | 329.6 | 356.8 | 9.7 | 0.342x | 3.543x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,024.3 | 1,009.5 | 1,039.4 | 10.4 | 1.000x | 10.353x |

### `orig` / `s-052` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 37.2 | 37.1 | 37.4 | 0.1 | 0.124x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.6 | 37.4 | 40.6 | 1.2 | 0.126x | 1.009x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 287.7 | 258.6 | 297.0 | 13.2 | 0.962x | 7.729x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 297.4 | 295.3 | 310.0 | 5.4 | 0.994x | 7.989x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 299.2 | 295.8 | 313.1 | 6.1 | 1.000x | 8.036x |

### `orig` / `s-052` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 31.3 | 31.2 | 32.6 | 0.5 | 0.029x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 31.5 | 31.5 | 33.0 | 0.6 | 0.029x | 1.008x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 70.1 | 67.6 | 79.0 | 4.4 | 0.065x | 2.238x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 404.9 | 393.9 | 445.4 | 17.7 | 0.376x | 12.933x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,077.9 | 1,068.5 | 1,084.8 | 5.3 | 1.000x | 34.431x |

### `orig` / `s-053` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 28.2 | 27.8 | 28.3 | 0.2 | 0.095x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 28.4 | 28.2 | 29.9 | 0.6 | 0.096x | 1.008x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 288.2 | 255.0 | 303.5 | 16.3 | 0.976x | 10.239x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 295.2 | 294.1 | 301.4 | 2.7 | 1.000x | 10.487x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 295.9 | 294.2 | 301.1 | 2.3 | 1.002x | 10.509x |

### `orig` / `s-053` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 21.3 | 21.0 | 21.6 | 0.2 | 0.020x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 21.3 | 21.1 | 22.7 | 0.6 | 0.020x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 69.1 | 66.5 | 75.7 | 3.7 | 0.065x | 3.253x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 400.8 | 375.0 | 414.4 | 15.0 | 0.379x | 18.860x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,056.7 | 1,049.2 | 1,069.8 | 6.8 | 1.000x | 49.725x |

### `orig` / `s-054` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 28.0 | 27.9 | 28.1 | 0.1 | 0.095x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 28.2 | 28.0 | 30.4 | 0.9 | 0.095x | 1.005x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 286.8 | 255.7 | 287.5 | 12.4 | 0.968x | 10.231x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 293.9 | 291.8 | 297.7 | 2.2 | 0.992x | 10.484x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 296.3 | 294.4 | 301.1 | 2.5 | 1.000x | 10.572x |

### `orig` / `s-054` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 21.2 | 21.0 | 21.5 | 0.2 | 0.020x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 21.3 | 21.1 | 21.6 | 0.2 | 0.020x | 1.007x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 70.7 | 68.4 | 76.8 | 3.2 | 0.066x | 3.340x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 397.3 | 379.0 | 438.2 | 22.9 | 0.374x | 18.774x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,063.3 | 1,057.5 | 1,064.8 | 3.1 | 1.000x | 50.249x |

### `orig` / `s-055` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 28.1 | 27.8 | 29.7 | 0.7 | 0.095x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 28.2 | 28.0 | 30.6 | 1.0 | 0.096x | 1.007x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 283.3 | 256.5 | 286.7 | 11.3 | 0.959x | 10.101x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 294.3 | 293.2 | 299.5 | 2.3 | 0.996x | 10.491x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 295.5 | 294.3 | 301.2 | 3.0 | 1.000x | 10.536x |

### `orig` / `s-055` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 21.2 | 21.0 | 23.3 | 0.9 | 0.020x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 21.2 | 21.2 | 21.3 | 0.0 | 0.020x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 75.4 | 66.1 | 82.9 | 5.9 | 0.071x | 3.563x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 405.1 | 361.3 | 433.9 | 25.9 | 0.384x | 19.131x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,055.1 | 1,051.7 | 1,136.5 | 32.6 | 1.000x | 49.832x |

### `orig` / `s-056` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 30.9 | 30.7 | 32.4 | 0.6 | 0.103x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 31.0 | 30.8 | 32.3 | 0.6 | 0.104x | 1.002x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 283.6 | 253.3 | 286.7 | 12.3 | 0.948x | 9.166x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 294.3 | 291.9 | 299.5 | 2.5 | 0.984x | 9.511x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 299.1 | 292.3 | 303.3 | 4.2 | 1.000x | 9.666x |

### `orig` / `s-056` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 25.4 | 25.3 | 28.2 | 1.1 | 0.024x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 25.5 | 25.4 | 29.6 | 1.6 | 0.024x | 1.005x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 69.3 | 66.0 | 76.8 | 4.0 | 0.065x | 2.731x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 397.3 | 355.8 | 409.9 | 20.5 | 0.372x | 15.650x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,066.9 | 1,049.0 | 1,074.9 | 9.5 | 1.000x | 42.027x |

### `orig` / `s-057` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7,918.3 | 7,863.2 | 8,002.2 | 48.2 | 0.798x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 9,850.9 | 9,826.6 | 10,000.1 | 63.1 | 0.993x | 1.244x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 9,918.9 | 9,829.2 | 9,970.4 | 56.0 | 1.000x | 1.253x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 67,298.3 | 67,249.2 | 67,361.6 | 38.9 | 6.785x | 8.499x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 67,491.2 | 67,374.7 | 67,996.4 | 226.6 | 6.804x | 8.523x |

### `orig` / `s-058` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 6,675.3 | 6,669.3 | 6,695.3 | 9.0 | 0.092x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 26,316.1 | 26,297.5 | 26,343.4 | 15.2 | 0.361x | 3.942x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 26,352.1 | 26,306.2 | 26,422.6 | 39.2 | 0.362x | 3.948x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 72,825.0 | 72,670.3 | 74,077.2 | 552.5 | 1.000x | 10.910x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 72,883.5 | 72,697.3 | 72,998.7 | 111.2 | 1.001x | 10.918x |

### `orig` / `s-059` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 26,064.0 | 26,020.4 | 26,117.0 | 35.4 | 0.163x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33,713.1 | 33,688.7 | 33,802.2 | 42.9 | 0.211x | 1.293x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33,735.5 | 33,683.9 | 33,776.5 | 39.3 | 0.211x | 1.294x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 159,321.2 | 158,917.5 | 161,709.6 | 1,015.2 | 0.996x | 6.113x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 159,936.5 | 158,786.1 | 162,249.9 | 1,233.3 | 1.000x | 6.136x |

### `orig` / `s-060` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7,867.9 | 7,833.5 | 7,936.9 | 34.1 | 0.832x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 9,443.4 | 9,421.0 | 9,494.9 | 27.8 | 0.999x | 1.200x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 9,451.2 | 9,423.7 | 9,717.2 | 110.0 | 1.000x | 1.201x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33,480.3 | 33,462.8 | 33,575.0 | 42.0 | 3.542x | 4.255x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33,536.1 | 33,522.2 | 33,827.7 | 117.7 | 3.548x | 4.262x |

### `orig` / `s-061` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5,391.2 | 5,373.8 | 5,452.7 | 27.2 | 0.120x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13,196.0 | 13,179.0 | 13,238.8 | 20.3 | 0.295x | 2.448x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13,197.4 | 13,174.8 | 13,210.4 | 12.5 | 0.295x | 2.448x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44,693.2 | 44,589.0 | 44,988.9 | 141.6 | 0.998x | 8.290x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 44,790.5 | 44,638.6 | 45,021.3 | 141.2 | 1.000x | 8.308x |

### `orig` / `s-062` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 245.4 | 238.7 | 281.9 | 15.9 | 0.773x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 317.4 | 317.0 | 319.0 | 0.8 | 1.000x | 1.293x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 318.1 | 315.8 | 333.0 | 6.4 | 1.002x | 1.296x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 1,686.2 | 1,682.8 | 1,700.4 | 6.2 | 5.313x | 6.870x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 1,690.2 | 1,683.4 | 1,702.9 | 6.3 | 5.326x | 6.887x |

### `orig` / `s-063` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 13,122.7 | 13,112.7 | 13,128.9 | 5.8 | 0.119x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 25,279.6 | 25,276.9 | 25,357.2 | 31.2 | 0.229x | 1.926x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 25,351.7 | 25,280.8 | 25,394.7 | 42.0 | 0.229x | 1.932x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 110,470.9 | 109,344.7 | 111,522.2 | 691.8 | 1.000x | 8.418x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 110,485.5 | 110,032.6 | 115,677.4 | 2,110.9 | 1.000x | 8.419x |

### `orig` / `s-064` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 11,644.1 | 11,605.0 | 12,777.2 | 455.9 | 0.122x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 27,033.2 | 27,014.2 | 27,185.9 | 70.3 | 0.283x | 2.322x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 27,036.7 | 26,989.2 | 27,561.3 | 212.5 | 0.283x | 2.322x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 95,354.8 | 95,034.3 | 95,531.2 | 162.3 | 0.998x | 8.189x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 95,533.2 | 95,262.6 | 95,877.6 | 233.1 | 1.000x | 8.204x |

### `orig` / `s-065` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.0 | 28.9 | 30.0 | 0.4 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.3 | 29.1 | 29.6 | 0.2 | 1.009x | 1.009x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 41.3 | 41.2 | 41.4 | 0.1 | 1.423x | 1.423x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 41.6 | 41.1 | 41.7 | 0.2 | 1.434x | 1.434x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 209.5 | 204.8 | 228.4 | 9.6 | 7.222x | 7.222x |

### `orig` / `s-065` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 33.7 | 33.7 | 36.2 | 1.0 | 0.060x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 34.6 | 33.7 | 42.2 | 3.1 | 0.061x | 1.026x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 63.6 | 62.8 | 71.7 | 3.7 | 0.113x | 1.885x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 454.9 | 444.0 | 473.6 | 10.8 | 0.807x | 13.488x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 563.9 | 554.6 | 571.4 | 5.6 | 1.000x | 16.720x |

### `orig` / `s-066` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 117.2 | 117.1 | 117.3 | 0.1 | 0.178x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 118.6 | 117.4 | 135.5 | 7.1 | 0.180x | 1.012x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 275.5 | 269.2 | 316.5 | 19.6 | 0.419x | 2.351x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 657.3 | 650.8 | 663.4 | 4.3 | 1.000x | 5.609x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 660.3 | 655.4 | 666.3 | 4.4 | 1.004x | 5.634x |

### `orig` / `s-066` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 84.7 | 81.1 | 91.6 | 4.1 | 0.128x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 109.9 | 109.6 | 115.7 | 2.4 | 0.166x | 1.298x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 111.5 | 109.7 | 114.7 | 1.8 | 0.168x | 1.317x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 313.8 | 295.5 | 326.8 | 10.6 | 0.473x | 3.706x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 663.3 | 653.2 | 669.5 | 5.7 | 1.000x | 7.834x |

### `orig` / `s-067` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 110.5 | 110.5 | 110.8 | 0.1 | 0.173x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 110.8 | 110.2 | 120.0 | 3.8 | 0.173x | 1.003x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 284.0 | 275.8 | 292.6 | 5.8 | 0.444x | 2.570x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 637.3 | 631.4 | 653.7 | 8.4 | 0.997x | 5.767x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 639.1 | 634.4 | 647.0 | 4.7 | 1.000x | 5.782x |

### `orig` / `s-067` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 82.1 | 81.4 | 90.9 | 4.5 | 0.128x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 103.2 | 102.3 | 104.6 | 0.7 | 0.161x | 1.257x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 103.4 | 102.8 | 103.7 | 0.3 | 0.161x | 1.259x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 291.4 | 285.0 | 320.7 | 12.9 | 0.455x | 3.551x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 640.9 | 626.3 | 650.0 | 8.1 | 1.000x | 7.809x |

### `orig` / `s-068` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 40.2 | 39.8 | 40.4 | 0.2 | 0.097x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 40.4 | 39.8 | 49.6 | 3.7 | 0.098x | 1.007x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 261.1 | 241.1 | 273.7 | 11.0 | 0.630x | 6.499x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 412.6 | 409.4 | 430.8 | 7.7 | 0.995x | 10.272x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 414.7 | 411.7 | 421.1 | 3.1 | 1.000x | 10.324x |

### `orig` / `s-068` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 32.6 | 32.4 | 32.9 | 0.2 | 0.078x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 32.6 | 32.4 | 34.4 | 0.7 | 0.078x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 62.4 | 60.9 | 74.7 | 5.2 | 0.150x | 1.915x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 262.8 | 257.4 | 282.5 | 8.8 | 0.631x | 8.059x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 416.3 | 415.5 | 420.3 | 1.7 | 1.000x | 12.768x |

### `orig` / `s-069` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 53.2 | 52.9 | 53.6 | 0.2 | 0.255x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 54.1 | 53.5 | 54.4 | 0.4 | 0.260x | 1.018x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 207.9 | 205.8 | 217.0 | 3.9 | 0.997x | 3.910x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 208.5 | 208.0 | 215.2 | 2.7 | 1.000x | 3.921x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 283.0 | 241.7 | 299.4 | 19.2 | 1.358x | 5.324x |

### `orig` / `s-069` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 47.0 | 47.0 | 48.3 | 0.5 | 0.065x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 47.2 | 47.1 | 47.4 | 0.1 | 0.065x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 66.9 | 66.3 | 84.9 | 7.5 | 0.092x | 1.422x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 455.8 | 441.9 | 478.7 | 12.1 | 0.630x | 9.691x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 723.8 | 716.7 | 724.6 | 3.0 | 1.000x | 15.389x |

### `orig` / `s-070` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 90.7 | 90.3 | 90.8 | 0.2 | 0.167x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 91.0 | 90.6 | 100.7 | 3.9 | 0.167x | 1.004x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 287.6 | 247.3 | 292.2 | 16.4 | 0.529x | 3.171x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 542.4 | 539.8 | 564.1 | 9.2 | 0.998x | 5.981x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 543.6 | 542.6 | 545.3 | 0.9 | 1.000x | 5.994x |

### `orig` / `s-070` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 76.8 | 74.8 | 83.9 | 3.6 | 0.141x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 82.9 | 82.7 | 83.4 | 0.3 | 0.152x | 1.078x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 83.8 | 82.7 | 84.7 | 0.8 | 0.154x | 1.091x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 273.0 | 262.6 | 284.5 | 6.9 | 0.501x | 3.553x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 545.2 | 539.0 | 552.1 | 4.2 | 1.000x | 7.096x |

### `orig` / `s-071` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 202.6 | 202.4 | 203.6 | 0.4 | 0.361x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 204.5 | 202.7 | 213.3 | 4.7 | 0.365x | 1.009x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 278.7 | 244.0 | 288.8 | 16.4 | 0.497x | 1.376x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 558.3 | 555.6 | 579.7 | 8.8 | 0.996x | 2.756x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 560.5 | 558.9 | 564.5 | 1.9 | 1.000x | 2.767x |

### `orig` / `s-071` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 94.9 | 88.4 | 101.4 | 4.3 | 0.169x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 194.4 | 194.2 | 195.1 | 0.3 | 0.346x | 2.048x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 194.7 | 194.2 | 194.9 | 0.3 | 0.346x | 2.051x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 286.9 | 265.0 | 293.8 | 10.4 | 0.510x | 3.022x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 562.8 | 556.7 | 568.0 | 3.9 | 1.000x | 5.927x |

### `orig` / `s-072` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 166.0 | 165.8 | 166.9 | 0.4 | 0.139x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 166.3 | 166.0 | 174.8 | 3.4 | 0.139x | 1.002x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 386.8 | 324.0 | 394.8 | 26.0 | 0.324x | 2.330x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,192.1 | 1,181.4 | 1,213.7 | 10.7 | 0.997x | 7.183x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,195.2 | 1,173.4 | 1,213.3 | 15.1 | 1.000x | 7.202x |

### `orig` / `s-072` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 160.8 | 160.4 | 161.4 | 0.4 | 0.093x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 160.8 | 160.7 | 162.1 | 0.5 | 0.093x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 176.3 | 170.7 | 198.0 | 9.8 | 0.102x | 1.097x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 424.0 | 400.5 | 426.5 | 10.6 | 0.244x | 2.637x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,734.5 | 1,729.4 | 1,750.7 | 7.4 | 1.000x | 10.786x |

### `orig` / `s-073` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 40.2 | 40.1 | 40.5 | 0.1 | 0.135x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 40.3 | 40.2 | 44.9 | 1.9 | 0.135x | 1.002x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 285.9 | 242.5 | 291.5 | 17.9 | 0.957x | 7.112x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 298.7 | 295.8 | 304.6 | 3.2 | 1.000x | 7.430x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 299.3 | 293.8 | 318.4 | 8.8 | 1.002x | 7.444x |

### `orig` / `s-073` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 34.5 | 34.3 | 35.0 | 0.2 | 0.032x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 34.5 | 34.3 | 35.6 | 0.5 | 0.032x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 70.5 | 67.8 | 76.6 | 3.3 | 0.066x | 2.044x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 420.2 | 411.0 | 458.6 | 17.6 | 0.391x | 12.192x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,073.8 | 1,054.5 | 1,081.4 | 9.1 | 1.000x | 31.156x |

### `orig` / `s-074` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 53.3 | 53.1 | 54.9 | 0.7 | 0.180x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 53.5 | 52.9 | 58.6 | 2.1 | 0.181x | 1.004x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 285.3 | 247.8 | 291.0 | 16.0 | 0.964x | 5.357x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 296.0 | 292.9 | 301.6 | 3.0 | 1.000x | 5.558x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 296.9 | 295.0 | 417.3 | 48.3 | 1.003x | 5.575x |

### `orig` / `s-074` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 47.1 | 46.9 | 48.7 | 0.7 | 0.044x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 47.3 | 46.9 | 47.8 | 0.4 | 0.044x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 73.3 | 71.0 | 77.8 | 2.4 | 0.069x | 1.556x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 578.4 | 546.6 | 597.8 | 18.7 | 0.541x | 12.276x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,068.4 | 1,058.4 | 1,079.7 | 8.0 | 1.000x | 22.674x |

### `orig` / `s-075` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 110.5 | 110.3 | 111.0 | 0.2 | 0.175x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 111.2 | 110.6 | 119.9 | 3.6 | 0.176x | 1.006x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 292.4 | 271.6 | 297.6 | 9.0 | 0.464x | 2.646x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 630.5 | 629.3 | 638.6 | 4.1 | 1.000x | 5.706x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 636.8 | 630.7 | 767.2 | 52.4 | 1.010x | 5.763x |

### `orig` / `s-075` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 89.1 | 88.6 | 93.7 | 1.9 | 0.140x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 102.7 | 102.5 | 103.8 | 0.4 | 0.162x | 1.153x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 103.2 | 102.9 | 103.3 | 0.2 | 0.162x | 1.158x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 278.8 | 265.6 | 290.1 | 9.9 | 0.438x | 3.130x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 636.1 | 628.1 | 647.9 | 6.4 | 1.000x | 7.140x |

### `orig` / `s-076` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 110.7 | 110.5 | 111.4 | 0.3 | 0.175x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 111.2 | 110.4 | 119.6 | 3.5 | 0.176x | 1.004x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 292.4 | 270.6 | 298.9 | 10.4 | 0.462x | 2.640x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 632.8 | 629.3 | 660.1 | 11.6 | 1.000x | 5.714x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 632.8 | 625.3 | 643.9 | 6.2 | 1.000x | 5.714x |

### `orig` / `s-076` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 88.6 | 88.3 | 92.1 | 1.5 | 0.139x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 102.9 | 102.7 | 105.6 | 1.1 | 0.161x | 1.161x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 103.2 | 102.2 | 103.6 | 0.5 | 0.162x | 1.165x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 280.7 | 265.6 | 290.5 | 8.9 | 0.441x | 3.169x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 637.1 | 633.2 | 639.2 | 2.4 | 1.000x | 7.193x |

### `orig` / `s-077` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 110.6 | 110.5 | 111.2 | 0.3 | 0.158x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 110.9 | 110.5 | 119.6 | 3.5 | 0.158x | 1.003x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 298.0 | 272.1 | 300.6 | 10.6 | 0.425x | 2.693x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 698.7 | 693.3 | 739.1 | 16.6 | 0.997x | 6.315x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 700.8 | 695.5 | 712.6 | 5.8 | 1.000x | 6.333x |

### `orig` / `s-077` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 89.7 | 88.7 | 91.8 | 1.1 | 0.128x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 103.0 | 102.8 | 103.3 | 0.2 | 0.147x | 1.148x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 103.4 | 102.7 | 103.8 | 0.4 | 0.148x | 1.153x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 286.5 | 249.0 | 320.6 | 27.0 | 0.410x | 3.195x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 698.9 | 693.9 | 704.9 | 3.6 | 1.000x | 7.794x |

### `orig` / `s-078` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 110.8 | 110.4 | 111.1 | 0.2 | 0.153x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 110.9 | 110.8 | 117.2 | 2.5 | 0.153x | 1.001x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 289.1 | 268.1 | 297.4 | 10.2 | 0.400x | 2.610x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 722.4 | 712.5 | 745.2 | 10.8 | 0.998x | 6.521x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 723.6 | 718.0 | 730.5 | 4.6 | 1.000x | 6.532x |

### `orig` / `s-078` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 85.2 | 84.2 | 89.1 | 1.8 | 0.118x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 103.2 | 103.0 | 103.6 | 0.2 | 0.143x | 1.210x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 103.3 | 103.2 | 121.5 | 7.2 | 0.143x | 1.212x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 284.6 | 239.8 | 321.1 | 29.3 | 0.394x | 3.338x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 722.5 | 716.7 | 732.4 | 6.2 | 1.000x | 8.475x |

### `orig` / `s-079` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 1/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 110.6 | 110.3 | 114.9 | 1.7 | 0.153x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 111.0 | 110.3 | 111.9 | 0.5 | 0.154x | 1.003x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 283.5 | 263.9 | 309.9 | 17.0 | 0.393x | 2.562x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 721.9 | 720.9 | 741.4 | 7.8 | 1.000x | 6.525x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 723.5 | 711.7 | 751.1 | 13.2 | 1.002x | 6.539x |

### `orig` / `s-079` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 84.7 | 84.2 | 88.5 | 1.8 | 0.117x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 103.0 | 102.6 | 103.1 | 0.2 | 0.142x | 1.216x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 103.1 | 102.6 | 103.8 | 0.4 | 0.142x | 1.217x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 297.0 | 249.2 | 320.4 | 24.9 | 0.409x | 3.506x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 726.3 | 719.1 | 736.4 | 5.7 | 1.000x | 8.574x |

### `orig` / `s-080` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 50.4 | 50.0 | 54.8 | 1.8 | 0.144x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 50.5 | 49.7 | 54.9 | 1.9 | 0.144x | 1.003x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 284.1 | 254.5 | 287.4 | 12.3 | 0.811x | 5.639x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 350.2 | 348.5 | 353.4 | 1.7 | 1.000x | 6.951x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 355.5 | 349.4 | 376.3 | 9.5 | 1.015x | 7.055x |

### `orig` / `s-080` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 43.9 | 43.7 | 44.4 | 0.3 | 0.035x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 44.4 | 43.7 | 46.1 | 0.8 | 0.035x | 1.011x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 72.4 | 70.3 | 80.6 | 3.8 | 0.057x | 1.649x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 611.2 | 603.0 | 638.0 | 12.5 | 0.480x | 13.924x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,272.3 | 1,266.8 | 1,281.3 | 5.2 | 1.000x | 28.985x |

### `orig` / `s-081` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 11.9 | 11.8 | 12.3 | 0.2 | 0.408x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.1 | 11.9 | 12.1 | 0.1 | 0.412x | 1.011x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.0 | 28.9 | 29.1 | 0.1 | 0.993x | 2.435x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.2 | 29.0 | 29.5 | 0.2 | 1.000x | 2.453x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 262.5 | 250.8 | 272.2 | 7.2 | 8.979x | 22.022x |

### `orig` / `s-081` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 4.6 | 4.5 | 5.3 | 0.3 | 0.151x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 4.9 | 4.4 | 5.5 | 0.4 | 0.160x | 1.058x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.4 | 30.1 | 31.0 | 0.3 | 1.000x | 6.627x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 42.9 | 36.6 | 52.3 | 5.5 | 1.410x | 9.343x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 247.9 | 239.0 | 271.2 | 12.3 | 8.156x | 54.046x |

### `orig` / `s-082` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.0 | 12.7 | 15.4 | 1.0 | 0.436x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.5 | 12.8 | 14.8 | 0.7 | 0.452x | 1.035x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.6 | 29.4 | 30.3 | 0.4 | 0.991x | 2.271x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.9 | 29.1 | 30.3 | 0.4 | 1.000x | 2.292x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 263.1 | 251.1 | 271.3 | 6.9 | 8.809x | 20.193x |

### `orig` / `s-082` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 5.1 | 5.1 | 6.8 | 0.7 | 0.161x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 5.1 | 5.0 | 6.2 | 0.4 | 0.163x | 1.013x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 31.5 | 31.0 | 34.9 | 1.4 | 1.000x | 6.205x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 42.5 | 37.5 | 48.7 | 4.0 | 1.347x | 8.359x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 261.6 | 239.0 | 298.0 | 22.9 | 8.299x | 51.500x |

### `orig` / `s-083` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 35.1 | 34.6 | 36.6 | 0.8 | 0.960x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 36.6 | 35.7 | 38.7 | 1.1 | 1.000x | 1.041x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 138.0 | 137.6 | 138.2 | 0.2 | 3.771x | 3.927x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 138.5 | 138.2 | 139.1 | 0.4 | 3.786x | 3.943x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 272.3 | 257.7 | 282.2 | 7.8 | 7.443x | 7.751x |

### `orig` / `s-083` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 35.5 | 35.4 | 43.4 | 3.2 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.8 | 40.8 | 50.7 | 3.6 | 1.234x | 1.234x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 132.0 | 131.8 | 132.6 | 0.3 | 3.718x | 3.718x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 132.1 | 132.0 | 134.3 | 1.0 | 3.721x | 3.721x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 863.7 | 841.5 | 868.4 | 12.1 | 24.330x | 24.330x |

### `orig` / `s-084` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: 0/1 (subjects whose expected outcome is a match; record_schema.md 10.3 — ground truth lives in the sub-bench, not the record)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 30.3 | 30.1 | 31.3 | 0.4 | 0.833x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 30.4 | 30.2 | 30.5 | 0.1 | 0.835x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 34.3 | 33.6 | 36.0 | 0.8 | 0.941x | 1.129x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 36.4 | 35.1 | 38.4 | 1.4 | 1.000x | 1.200x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 260.4 | 233.4 | 264.2 | 11.5 | 7.152x | 8.582x |

### `orig` / `s-084` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 24.9 | 24.9 | 27.0 | 0.8 | 0.713x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 25.0 | 24.9 | 26.6 | 0.6 | 0.716x | 1.004x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 34.9 | 34.8 | 42.1 | 2.9 | 1.000x | 1.402x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 43.1 | 38.4 | 50.5 | 4.4 | 1.234x | 1.731x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 353.9 | 350.0 | 375.6 | 9.4 | 10.135x | 14.213x |

### `orig` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,693,007.3 | 3,619,893.5 | 3,734,169.7 | 37,747.2 | 0.128x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 6,542,380.1 | 6,533,295.3 | 6,549,917.4 | 5,888.6 | 0.227x | 1.772x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 6,546,199.3 | 6,535,898.5 | 6,599,885.0 | 23,271.6 | 0.227x | 1.773x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 12,112,463.0 | 11,459,356.0 | 13,238,110.3 | 652,907.4 | 0.420x | 3.280x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28,819,359.7 | 28,736,457.2 | 29,162,079.1 | 155,307.3 | 1.000x | 7.804x |

### `orig` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,772.8 | 17,751.1 | 17,794.1 | 14.9 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,566,034.8 | 2,533,967.4 | 2,584,589.9 | 20,303.8 | 144.380x | 144.380x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 3,428,525.6 | 3,418,886.9 | 3,463,530.5 | 15,999.0 | 192.908x | 192.908x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 3,433,874.3 | 3,419,820.9 | 3,458,171.2 | 14,923.8 | 193.209x | 193.209x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 16,968,804.0 | 16,819,943.0 | 17,133,175.0 | 99,216.8 | 954.762x | 954.762x |

### `orig` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,792.2 | 17,764.3 | 22,237.2 | 1,765.1 | 1.000x | 1.000x | 5 | 100% |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,828,833.6 | 2,821,643.6 | 2,832,572.6 | 4,020.8 | 158.993x | 158.993x | 5 | 100% |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 3,422,799.6 | 3,414,990.9 | 3,436,319.7 | 8,063.5 | 192.376x | 192.376x | 5 | 100% |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 3,424,102.3 | 3,415,649.6 | 3,511,766.2 | 35,973.8 | 192.449x | 192.449x | 5 | 100% |

## Excluded from ranking (expectation-failing cells)

| pattern | subject | regime | form | testee | n | pass-rate | gave-up | wrong | outcomes |
|---|---|---|---|---|---|---|---|---|---|
| `factored` | `s-058` | `match-compliance` | `whole-subject` | `pcrec_8da6120_auto-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-058` | `match-compliance` | `whole-subject` | `pcrec_8da6120_auto-nocaps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-058` | `match-compliance` | `whole-subject` | `pcrec_8da6120_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-059` | `match-compliance` | `whole-subject` | `pcrec_8da6120_auto-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-059` | `match-compliance` | `whole-subject` | `pcrec_8da6120_auto-nocaps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-059` | `match-compliance` | `whole-subject` | `pcrec_8da6120_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-061` | `match-compliance` | `whole-subject` | `pcrec_8da6120_auto-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-061` | `match-compliance` | `whole-subject` | `pcrec_8da6120_auto-nocaps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-061` | `match-compliance` | `whole-subject` | `pcrec_8da6120_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-063` | `match-compliance` | `whole-subject` | `pcrec_8da6120_auto-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-063` | `match-compliance` | `whole-subject` | `pcrec_8da6120_auto-nocaps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-063` | `match-compliance` | `whole-subject` | `pcrec_8da6120_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-064` | `match-compliance` | `whole-subject` | `pcrec_8da6120_auto-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-064` | `match-compliance` | `whole-subject` | `pcrec_8da6120_auto-nocaps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-064` | `match-compliance` | `whole-subject` | `pcrec_8da6120_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 5 | 0% | 0 | 0 | timed-out=5 |
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_8da6120_auto-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_8da6120_auto-nocaps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_8da6120_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `orig` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_8da6120_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |

## Compile cost (by execution-model class; never pooled across classes)

### `compiled-aot`

- `pcrec_8da6120_auto-caps-simdna`: engine=dfa, entry=plain entry, prefilter=(no stamp — pcrec I-3), rungs=-, buffers=n/s, frame=n/s
- `pcrec_8da6120_auto-nocaps-simdna`: engine=dfa, entry=plain entry, prefilter=(no stamp — pcrec I-3), rungs=-, buffers=n/s, frame=n/s
- `pcrec_8da6120_vm-caps-simdna`: engine=vm, entry=plain entry, prefilter=none, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, buffers=n/s, frame=n/s

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes | emit-c ns | gcc ns | load ns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `pcrec_8da6120_auto-caps-simdna` | 420,465,289.0 | 414,985,073.0 | 428,903,342.0 | 4,893,507.9 | 5 | 25,128 | 0.012 | compiled=5 | 1,880,342.0 | 418,531,336.0 | 110,891.0 |
| `factored` | `whole-subject` | `pcrec_8da6120_auto-caps-simdna` | 430,387,601.0 | 417,874,860.0 | 443,938,027.0 | 8,743,376.0 | 5 | 25,128 | 0.020 | compiled=5 | 1,903,072.0 | 428,382,468.0 | 199,551.0 |
| `factored` | `plain` | `pcrec_8da6120_auto-nocaps-simdna` | 427,493,516.0 | 422,008,523.0 | 434,926,485.0 | 4,492,879.1 | 5 | 25,128 | 0.011 | compiled=5 | 3,458,012.0 | 423,761,643.0 | 190,832.0 |
| `factored` | `whole-subject` | `pcrec_8da6120_auto-nocaps-simdna` | 420,974,905.0 | 413,095,565.0 | 432,864,330.0 | 7,311,852.8 | 5 | 25,128 | 0.017 | compiled=5 | 1,773,151.0 | 419,081,683.0 | 189,551.0 |
| `factored` | `plain` | `pcrec_8da6120_vm-caps-simdna` | 424,762,944.0 | 423,664,078.0 | 432,708,304.0 | 3,362,545.9 | 5 | 25,128 | 0.008 | compiled=5 | 1,716,071.0 | 422,822,902.0 | 193,901.0 |
| `factored` | `whole-subject` | `pcrec_8da6120_vm-caps-simdna` | 427,987,625.0 | 424,012,201.0 | 439,228,106.0 | 5,642,429.0 | 5 | 25,128 | 0.013 | compiled=5 | 1,699,401.0 | 426,211,414.0 | 190,301.0 |
| `orig` | `plain` | `pcrec_8da6120_auto-caps-simdna` | 118,056,825.0 | 103,621,896.0 | 120,772,314.0 | 6,366,891.3 | 5 | 29,232 | 0.054 | compiled=5 | 7,414,687.0 | 110,543,728.0 | 98,410.0 |
| `orig` | `whole-subject` | `pcrec_8da6120_auto-caps-simdna` | 117,555,053.0 | 109,696,744.0 | 130,533,016.0 | 9,212,004.5 | 5 | 33,424 | 0.078 | compiled=5 | 9,605,031.0 | 107,535,020.0 | 194,121.0 |
| `orig` | `plain` | `pcrec_8da6120_auto-nocaps-simdna` | 113,739,182.0 | 110,959,754.0 | 143,108,420.0 | 11,988,842.7 | 5 | 29,232 | 0.105 | compiled=5 | 7,620,208.0 | 106,465,166.0 | 107,390.0 |
| `orig` | `whole-subject` | `pcrec_8da6120_auto-nocaps-simdna` | 135,300,201.0 | 122,043,665.0 | 137,739,956.0 | 6,730,911.2 | 5 | 33,424 | 0.050 | compiled=5 | 19,767,436.0 | 115,433,954.0 | 101,750.0 |
| `orig` | `plain` | `pcrec_8da6120_vm-caps-simdna` | 382,875,770.0 | 372,878,556.0 | 389,967,264.0 | 6,557,411.6 | 5 | 25,088 | 0.017 | compiled=5 | 1,976,132.0 | 380,961,488.0 | 196,851.0 |
| `orig` | `whole-subject` | `pcrec_8da6120_vm-caps-simdna` | 374,587,618.0 | 362,494,710.0 | 389,369,562.0 | 9,692,150.1 | 5 | 25,088 | 0.026 | compiled=5 | 2,358,745.0 | 372,141,432.0 | 101,580.0 |

### `eager-jit`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 69,630.0 | 64,000.0 | 168,531.0 | 39,793.8 | 5 | 951 | 0.572 | compiled=5 |
| `orig` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 159,291.0 | 144,641.0 | 396,882.0 | 95,332.9 | 5 | 1,609 | 0.598 | compiled=5 |

### `interpretive`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 14,510.0 | 12,870.0 | 45,421.0 | 12,460.8 | 5 | 951 | timer-floor | compiled=5 |
| `orig` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 13,541.0 | 12,300.0 | 45,080.0 | 12,673.0 | 5 | 1,609 | timer-floor | compiled=5 |

