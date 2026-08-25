# pcrec-bench report

reporter: v2 (2026-08-25)

## Query

- filters: subbench=email-specimen
- record source: store/index.tsv (11 candidate file(s))
- records included: 9
    - `email-specimen@0.1__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260825T062213Z` (store/records/email-specimen@0.1/libpcre2_10.46_interp-caps-simdna/email-specimen@0.1__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260825T062213Z.jsonl)
    - `email-specimen@0.1__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260825T174132Z` (store/records/email-specimen@0.1/libpcre2_10.46_jit-caps-simdna/email-specimen@0.1__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260825T174132Z.jsonl)
    - `email-specimen@0.1__pcrec_692c2e8_auto-caps-simdna__budu-ryzen1600__20260825T175131Z` (store/records/email-specimen@0.1/pcrec_692c2e8_auto-caps-simdna/email-specimen@0.1__pcrec_692c2e8_auto-caps-simdna__budu-ryzen1600__20260825T175131Z.jsonl)
    - `email-specimen@0.1__pcrec_692c2e8_auto-nocaps-simdna__budu-ryzen1600__20260825T175534Z` (store/records/email-specimen@0.1/pcrec_692c2e8_auto-nocaps-simdna/email-specimen@0.1__pcrec_692c2e8_auto-nocaps-simdna__budu-ryzen1600__20260825T175534Z.jsonl)
    - `email-specimen@0.1__pcrec_692c2e8_vm-caps-simdna__budu-ryzen1600__20260825T175933Z` (store/records/email-specimen@0.1/pcrec_692c2e8_vm-caps-simdna/email-specimen@0.1__pcrec_692c2e8_vm-caps-simdna__budu-ryzen1600__20260825T175933Z.jsonl)
    - `email-specimen@0.1__pcrec_692c2e8_vm-in-caps-simdna__budu-ryzen1600__20260825T180451Z` (store/records/email-specimen@0.1/pcrec_692c2e8_vm-in-caps-simdna/email-specimen@0.1__pcrec_692c2e8_vm-in-caps-simdna__budu-ryzen1600__20260825T180451Z.jsonl)
    - `email-specimen@0.1__pcrec_8da6120_auto-caps-simdna__budu-ryzen1600__20260825T065046Z` (store/records/email-specimen@0.1/pcrec_8da6120_auto-caps-simdna/email-specimen@0.1__pcrec_8da6120_auto-caps-simdna__budu-ryzen1600__20260825T065046Z.jsonl)
    - `email-specimen@0.1__pcrec_8da6120_auto-nocaps-simdna__budu-ryzen1600__20260825T063943Z` (store/records/email-specimen@0.1/pcrec_8da6120_auto-nocaps-simdna/email-specimen@0.1__pcrec_8da6120_auto-nocaps-simdna__budu-ryzen1600__20260825T063943Z.jsonl)
    - `email-specimen@0.1__pcrec_8da6120_vm-caps-simdna__budu-ryzen1600__20260825T064436Z` (store/records/email-specimen@0.1/pcrec_8da6120_vm-caps-simdna/email-specimen@0.1__pcrec_8da6120_vm-caps-simdna__budu-ryzen1600__20260825T064436Z.jsonl)
- superseded records (OD-B15, amended: older duplicate of a (subbench@version, testee_id, machine) than the newest MEASURED record; newest-measured kept by default, `--all-records` shows each separately): 1
    - `email-specimen@0.1__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260825T062944Z` superseded by `email-specimen@0.1__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260825T174132Z`
- newer, not measured (OD-B15 amendment, 2026-08-25: a record newer than the kept one but NOT `measured` does not supersede it -- a non-measured record is not evidence against a measured one of the same testee and version; it stands only if the group has no measured record at all): 1
    - newer, not measured: `email-specimen@0.1__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260825T173402Z` (inconclusive-load) -- kept `email-specimen@0.1__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260825T062213Z`
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

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 148.9 | 147.4 | 149.6 | 0.9 | 0.171x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 320.6 | 307.5 | 329.7 | 9.4 | 0.368x | 2.153x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 466.9 | 421.0 | 495.7 | 25.2 | 0.537x | 3.137x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 490.2 | 483.1 | 536.9 | 20.1 | 0.563x | 3.293x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 500.9 | 494.5 | 502.4 | 3.0 | 0.576x | 3.365x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 862.1 | 861.7 | 879.0 | 7.5 | 0.991x | 5.792x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 870.0 | 862.1 | 878.4 | 6.0 | 1.000x | 5.844x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-000` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 153.1 | 152.2 | 153.3 | 0.4 | 0.178x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 155.0 | 154.3 | 156.5 | 0.8 | 0.180x | 1.012x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 330.5 | 321.2 | 338.9 | 6.4 | 0.384x | 2.159x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 430.7 | 416.6 | 504.6 | 31.6 | 0.500x | 2.814x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 464.5 | 445.4 | 495.6 | 17.8 | 0.539x | 3.034x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 467.6 | 450.4 | 488.3 | 13.3 | 0.543x | 3.055x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 861.1 | 856.8 | 878.9 | 8.1 | 1.000x | 5.625x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-001` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 203.5 | 201.8 | 207.1 | 1.8 | 0.165x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 379.2 | 369.0 | 402.7 | 13.0 | 0.308x | 1.863x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 506.6 | 493.4 | 538.1 | 15.3 | 0.412x | 2.489x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 584.4 | 572.0 | 619.1 | 16.2 | 0.475x | 2.872x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 600.3 | 562.6 | 692.0 | 46.5 | 0.488x | 2.950x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,218.9 | 1,212.4 | 1,234.3 | 9.2 | 0.991x | 5.989x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,230.3 | 1,222.3 | 1,234.8 | 4.8 | 1.000x | 6.045x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-001` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 175.6 | 175.4 | 176.3 | 0.4 | 0.143x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 208.4 | 208.0 | 210.5 | 1.1 | 0.170x | 1.187x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 392.5 | 374.8 | 402.2 | 10.5 | 0.319x | 2.236x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 520.6 | 492.6 | 536.5 | 19.3 | 0.424x | 2.965x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 551.7 | 511.9 | 579.7 | 29.3 | 0.449x | 3.142x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 563.7 | 533.3 | 597.8 | 26.8 | 0.459x | 3.211x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,228.7 | 1,220.2 | 1,256.0 | 13.4 | 1.000x | 6.998x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-002` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 103.0 | 102.8 | 103.7 | 0.3 | 0.136x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 279.0 | 274.8 | 302.6 | 12.1 | 0.368x | 2.710x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 430.1 | 380.9 | 443.6 | 22.1 | 0.567x | 4.178x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 431.3 | 408.0 | 454.4 | 17.8 | 0.569x | 4.189x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 452.3 | 402.1 | 485.4 | 31.1 | 0.597x | 4.394x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 750.8 | 744.0 | 756.2 | 4.4 | 0.990x | 7.293x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 758.3 | 746.0 | 768.9 | 7.9 | 1.000x | 7.365x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-002` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 106.5 | 106.4 | 109.6 | 1.3 | 0.140x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 121.0 | 119.9 | 122.8 | 1.1 | 0.159x | 1.136x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 269.7 | 264.1 | 292.4 | 10.0 | 0.355x | 2.532x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 350.0 | 299.7 | 478.7 | 64.0 | 0.461x | 3.286x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 375.7 | 371.4 | 488.0 | 48.1 | 0.495x | 3.527x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 390.2 | 355.6 | 453.4 | 33.1 | 0.514x | 3.663x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 759.6 | 744.8 | 776.2 | 10.1 | 1.000x | 7.131x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-003` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 215.8 | 214.2 | 219.0 | 1.6 | 0.163x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 428.8 | 379.5 | 445.9 | 23.3 | 0.324x | 1.987x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 590.8 | 545.4 | 621.1 | 27.6 | 0.446x | 2.738x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 652.5 | 596.4 | 727.2 | 43.3 | 0.493x | 3.024x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 660.6 | 595.4 | 709.3 | 47.2 | 0.499x | 3.062x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,323.4 | 1,322.1 | 1,348.5 | 10.0 | 1.000x | 6.134x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,324.6 | 1,315.1 | 1,340.3 | 9.8 | 1.001x | 6.139x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-003` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 185.1 | 184.7 | 185.6 | 0.3 | 0.138x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 219.0 | 218.6 | 223.6 | 1.9 | 0.163x | 1.183x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 411.6 | 381.9 | 425.4 | 14.3 | 0.306x | 2.224x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 566.9 | 558.6 | 680.0 | 46.1 | 0.422x | 3.063x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 581.7 | 557.8 | 636.4 | 27.8 | 0.433x | 3.143x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 626.4 | 601.0 | 665.6 | 22.0 | 0.466x | 3.384x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,344.9 | 1,332.0 | 1,440.4 | 41.0 | 1.000x | 7.266x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-004` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 167.3 | 167.1 | 168.1 | 0.4 | 0.190x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 375.5 | 369.8 | 378.2 | 2.7 | 0.426x | 2.245x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 529.9 | 476.0 | 572.3 | 34.4 | 0.601x | 3.168x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 572.3 | 517.2 | 584.7 | 27.5 | 0.650x | 3.421x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 611.8 | 531.7 | 657.6 | 46.0 | 0.695x | 3.657x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 881.0 | 875.5 | 898.3 | 9.3 | 1.000x | 5.266x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 887.0 | 870.4 | 892.6 | 9.9 | 1.007x | 5.302x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-004` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 167.3 | 166.6 | 175.7 | 3.4 | 0.190x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 171.9 | 171.3 | 172.2 | 0.4 | 0.195x | 1.028x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 365.7 | 346.7 | 371.5 | 11.0 | 0.414x | 2.186x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 508.5 | 458.7 | 540.8 | 31.9 | 0.576x | 3.040x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 511.9 | 467.4 | 559.7 | 31.3 | 0.580x | 3.059x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 544.3 | 524.8 | 550.2 | 10.3 | 0.617x | 3.253x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 882.5 | 861.9 | 899.0 | 13.6 | 1.000x | 5.275x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-005` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 102.8 | 102.7 | 103.1 | 0.1 | 0.137x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 299.0 | 270.4 | 325.7 | 17.7 | 0.399x | 2.909x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 429.2 | 380.7 | 544.8 | 55.3 | 0.572x | 4.175x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 451.3 | 416.5 | 483.3 | 24.7 | 0.602x | 4.391x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 453.9 | 404.4 | 469.4 | 22.6 | 0.605x | 4.415x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 749.7 | 740.7 | 756.1 | 5.4 | 0.999x | 7.294x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 750.3 | 743.5 | 756.6 | 4.9 | 1.000x | 7.299x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-005` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 106.7 | 106.3 | 107.1 | 0.3 | 0.140x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 121.5 | 120.0 | 123.5 | 1.2 | 0.160x | 1.138x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 298.4 | 283.9 | 327.3 | 14.3 | 0.392x | 2.795x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 384.6 | 316.6 | 486.6 | 54.4 | 0.506x | 3.603x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 398.4 | 358.1 | 585.4 | 82.4 | 0.524x | 3.732x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 413.5 | 346.1 | 452.2 | 36.5 | 0.544x | 3.874x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 760.3 | 742.3 | 775.1 | 13.2 | 1.000x | 7.122x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-006` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 221.4 | 220.5 | 250.1 | 11.4 | 0.164x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 442.7 | 424.2 | 443.0 | 7.2 | 0.328x | 1.999x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 610.4 | 599.5 | 768.3 | 64.3 | 0.453x | 2.756x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 643.7 | 620.7 | 699.9 | 29.3 | 0.478x | 2.907x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 681.0 | 603.5 | 692.3 | 32.1 | 0.505x | 3.075x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,347.9 | 1,335.0 | 1,367.6 | 10.7 | 1.000x | 6.087x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,356.0 | 1,350.4 | 1,453.0 | 39.1 | 1.006x | 6.123x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-006` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 165.5 | 164.5 | 173.6 | 3.3 | 0.123x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 227.7 | 226.7 | 229.3 | 1.0 | 0.169x | 1.376x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 440.5 | 410.8 | 444.6 | 12.6 | 0.327x | 2.662x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 603.5 | 597.0 | 676.6 | 36.1 | 0.449x | 3.646x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 618.0 | 585.7 | 699.6 | 37.9 | 0.459x | 3.734x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 671.0 | 665.0 | 695.0 | 12.3 | 0.499x | 4.055x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,345.0 | 1,332.7 | 1,372.3 | 13.4 | 1.000x | 8.128x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-007` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 168.0 | 167.8 | 168.4 | 0.2 | 0.173x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 387.9 | 332.0 | 398.3 | 23.9 | 0.399x | 2.310x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 517.4 | 491.2 | 596.9 | 36.0 | 0.533x | 3.080x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 582.5 | 531.6 | 641.0 | 35.6 | 0.600x | 3.468x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 609.1 | 544.9 | 655.3 | 42.1 | 0.627x | 3.626x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 971.2 | 952.5 | 978.3 | 8.9 | 1.000x | 5.782x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 971.5 | 968.3 | 1,010.9 | 16.1 | 1.000x | 5.784x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-007` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 172.8 | 172.3 | 175.4 | 1.1 | 0.175x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 173.5 | 172.5 | 190.9 | 7.1 | 0.176x | 1.004x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 383.4 | 370.8 | 388.9 | 6.5 | 0.388x | 2.219x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 512.1 | 492.5 | 573.0 | 30.3 | 0.519x | 2.964x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 567.2 | 546.3 | 586.4 | 14.4 | 0.574x | 3.282x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 576.3 | 496.7 | 595.9 | 41.2 | 0.584x | 3.335x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 987.5 | 985.4 | 997.8 | 4.5 | 1.000x | 5.715x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-008` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 149.7 | 148.5 | 150.0 | 0.6 | 0.173x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 354.2 | 310.7 | 375.8 | 22.9 | 0.409x | 2.365x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 512.8 | 495.3 | 524.7 | 11.8 | 0.592x | 3.425x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 570.0 | 494.9 | 615.3 | 40.3 | 0.658x | 3.807x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 602.6 | 525.3 | 629.6 | 35.5 | 0.696x | 4.025x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 865.7 | 860.7 | 872.0 | 4.3 | 1.000x | 5.782x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 866.9 | 853.5 | 870.6 | 6.5 | 1.001x | 5.790x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-008` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 154.6 | 153.9 | 154.9 | 0.3 | 0.177x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 158.6 | 158.1 | 159.7 | 0.5 | 0.182x | 1.025x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 368.2 | 357.5 | 382.3 | 8.3 | 0.422x | 2.381x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 486.7 | 461.1 | 548.0 | 29.5 | 0.558x | 3.147x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 499.0 | 440.8 | 545.0 | 39.9 | 0.572x | 3.227x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 531.7 | 460.3 | 603.6 | 50.1 | 0.609x | 3.438x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 872.8 | 860.3 | 896.9 | 11.9 | 1.000x | 5.644x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-009` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 146.1 | 145.3 | 153.7 | 3.1 | 0.170x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 352.7 | 320.6 | 370.9 | 16.9 | 0.410x | 2.414x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 484.3 | 472.8 | 535.7 | 27.8 | 0.563x | 3.315x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 557.6 | 496.0 | 607.5 | 38.4 | 0.648x | 3.816x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 582.2 | 541.5 | 597.9 | 21.1 | 0.676x | 3.985x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 860.5 | 857.3 | 870.4 | 4.8 | 1.000x | 5.890x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 860.7 | 847.6 | 873.4 | 9.8 | 1.000x | 5.891x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-009` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 148.4 | 147.5 | 151.1 | 1.3 | 0.168x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 150.4 | 150.2 | 152.1 | 0.7 | 0.171x | 1.013x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 362.6 | 353.5 | 374.8 | 7.5 | 0.411x | 2.443x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 469.9 | 421.4 | 507.0 | 32.2 | 0.533x | 3.167x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 472.8 | 462.0 | 541.1 | 29.7 | 0.536x | 3.186x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 529.4 | 501.8 | 566.8 | 22.6 | 0.600x | 3.567x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 881.8 | 853.9 | 886.0 | 11.7 | 1.000x | 5.942x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-010` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 100.6 | 100.3 | 107.6 | 2.8 | 0.142x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 314.1 | 291.6 | 318.1 | 9.8 | 0.442x | 3.124x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 446.3 | 387.6 | 452.9 | 23.9 | 0.628x | 4.437x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 460.8 | 410.4 | 488.6 | 26.1 | 0.649x | 4.582x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 465.9 | 444.5 | 501.5 | 20.7 | 0.656x | 4.633x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 710.1 | 705.8 | 715.9 | 3.5 | 1.000x | 7.060x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 712.6 | 704.3 | 723.8 | 7.1 | 1.004x | 7.085x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-010` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 106.4 | 106.3 | 106.7 | 0.1 | 0.146x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 121.0 | 120.4 | 121.7 | 0.5 | 0.166x | 1.137x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 296.5 | 252.0 | 332.4 | 26.5 | 0.406x | 2.787x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 388.8 | 361.6 | 476.7 | 40.5 | 0.533x | 3.655x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 417.0 | 340.2 | 472.0 | 44.3 | 0.572x | 3.919x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 428.2 | 406.4 | 516.4 | 38.8 | 0.587x | 4.025x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 729.5 | 712.7 | 731.7 | 8.8 | 1.000x | 6.857x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-011` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 224.5 | 218.0 | 225.8 | 2.7 | 0.362x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 431.8 | 408.2 | 435.5 | 10.3 | 0.697x | 1.923x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 531.0 | 469.5 | 594.4 | 44.2 | 0.857x | 2.365x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 555.3 | 516.0 | 609.9 | 29.9 | 0.896x | 2.473x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 568.9 | 535.2 | 597.2 | 22.3 | 0.918x | 2.534x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 619.8 | 617.9 | 642.2 | 10.1 | 1.000x | 2.761x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 624.8 | 611.2 | 641.4 | 11.2 | 1.008x | 2.783x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-011` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 443.5 | 438.3 | 459.2 | 7.2 | 0.093x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 2,031.7 | 2,008.1 | 2,256.0 | 92.0 | 0.428x | 4.581x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 2,223.9 | 2,184.4 | 2,277.3 | 31.4 | 0.469x | 5.014x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 2,346.9 | 2,332.0 | 2,382.0 | 17.9 | 0.495x | 5.292x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 2,380.1 | 2,342.9 | 2,515.8 | 60.6 | 0.502x | 5.366x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 2,383.6 | 2,352.9 | 2,427.3 | 26.6 | 0.502x | 5.374x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,745.1 | 4,703.2 | 4,804.0 | 33.5 | 1.000x | 10.699x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-012` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 204.2 | 203.6 | 205.7 | 0.7 | 0.184x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 421.3 | 394.7 | 436.5 | 13.8 | 0.379x | 2.063x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 580.5 | 563.8 | 604.2 | 13.2 | 0.523x | 2.843x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 640.8 | 603.9 | 662.7 | 22.2 | 0.577x | 3.138x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 650.6 | 601.5 | 696.0 | 30.1 | 0.586x | 3.186x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,089.5 | 1,074.0 | 1,117.1 | 14.0 | 0.981x | 5.335x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,110.4 | 1,092.4 | 1,119.9 | 10.3 | 1.000x | 5.438x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-012` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 173.8 | 172.1 | 175.0 | 1.2 | 0.157x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 208.9 | 208.8 | 210.1 | 0.5 | 0.188x | 1.202x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 425.9 | 405.3 | 471.0 | 22.7 | 0.384x | 2.451x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 612.3 | 519.2 | 639.6 | 42.7 | 0.552x | 3.524x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 615.4 | 573.0 | 630.7 | 19.7 | 0.555x | 3.542x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 629.0 | 607.1 | 659.4 | 20.2 | 0.567x | 3.620x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,109.6 | 1,095.7 | 1,128.6 | 10.8 | 1.000x | 6.386x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-013` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 204.2 | 203.2 | 206.9 | 1.7 | 0.184x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 422.4 | 410.8 | 451.5 | 14.0 | 0.381x | 2.068x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 602.2 | 554.6 | 609.6 | 20.3 | 0.544x | 2.948x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 619.7 | 594.1 | 649.6 | 20.0 | 0.559x | 3.034x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 647.5 | 605.1 | 716.7 | 37.1 | 0.584x | 3.170x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,095.3 | 1,091.0 | 1,129.2 | 14.0 | 0.989x | 5.363x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,107.9 | 1,075.2 | 1,129.3 | 17.3 | 1.000x | 5.425x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-013` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 173.8 | 170.4 | 176.1 | 2.1 | 0.156x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 209.3 | 208.7 | 212.1 | 1.2 | 0.188x | 1.204x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 429.8 | 412.8 | 465.6 | 17.4 | 0.386x | 2.472x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 604.9 | 430.6 | 636.1 | 73.8 | 0.544x | 3.480x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 610.4 | 569.7 | 661.0 | 32.1 | 0.549x | 3.511x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 622.1 | 602.8 | 651.4 | 16.2 | 0.559x | 3.578x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,112.3 | 1,092.6 | 1,124.6 | 10.9 | 1.000x | 6.398x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-014` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 159.5 | 158.1 | 163.6 | 2.0 | 0.181x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 377.4 | 376.8 | 394.5 | 7.4 | 0.428x | 2.366x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 595.0 | 591.5 | 625.5 | 12.9 | 0.675x | 3.731x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 597.9 | 544.4 | 703.5 | 56.9 | 0.679x | 3.749x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 608.4 | 574.9 | 634.0 | 21.6 | 0.691x | 3.815x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 874.9 | 857.1 | 911.0 | 19.4 | 0.993x | 5.486x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 881.0 | 864.7 | 906.7 | 14.4 | 1.000x | 5.524x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-014` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 155.5 | 153.6 | 156.4 | 0.9 | 0.176x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 169.2 | 168.5 | 169.4 | 0.3 | 0.192x | 1.088x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 383.1 | 368.1 | 397.5 | 12.5 | 0.434x | 2.463x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 517.3 | 497.5 | 575.7 | 27.6 | 0.587x | 3.326x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 523.7 | 502.5 | 563.8 | 20.4 | 0.594x | 3.367x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 547.2 | 531.0 | 629.9 | 35.6 | 0.620x | 3.518x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 881.9 | 875.7 | 894.3 | 6.6 | 1.000x | 5.670x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-015` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 201.7 | 201.3 | 202.4 | 0.5 | 0.188x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 426.5 | 399.5 | 436.7 | 12.5 | 0.397x | 2.114x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 623.6 | 592.9 | 715.3 | 45.2 | 0.580x | 3.092x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 629.7 | 586.1 | 643.4 | 20.6 | 0.586x | 3.122x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 639.8 | 577.5 | 700.2 | 42.0 | 0.596x | 3.172x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,060.1 | 1,055.8 | 1,113.6 | 21.8 | 0.987x | 5.256x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,074.3 | 1,051.5 | 1,086.3 | 13.1 | 1.000x | 5.326x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-015` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 174.3 | 173.1 | 178.4 | 2.2 | 0.164x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 208.0 | 207.9 | 208.8 | 0.4 | 0.196x | 1.193x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 430.2 | 410.6 | 438.8 | 10.2 | 0.405x | 2.468x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 601.7 | 596.6 | 639.3 | 18.7 | 0.566x | 3.452x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 609.7 | 509.9 | 644.2 | 47.3 | 0.574x | 3.498x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 641.3 | 613.6 | 661.5 | 17.4 | 0.604x | 3.679x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,062.4 | 1,052.5 | 1,070.7 | 6.0 | 1.000x | 6.095x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-016` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 107.9 | 107.4 | 110.4 | 1.1 | 0.295x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 333.0 | 316.8 | 350.3 | 11.3 | 0.910x | 3.085x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 363.7 | 361.9 | 383.4 | 8.1 | 0.994x | 3.370x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 365.9 | 358.0 | 377.3 | 7.6 | 1.000x | 3.390x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 450.0 | 420.2 | 506.3 | 29.4 | 1.230x | 4.169x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 467.6 | 453.0 | 511.3 | 22.5 | 1.278x | 4.333x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 479.7 | 424.5 | 532.7 | 39.7 | 1.311x | 4.445x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-016` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 259.5 | 259.0 | 266.3 | 2.7 | 0.107x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 1,440.2 | 1,414.0 | 1,513.6 | 35.2 | 0.594x | 5.549x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,671.5 | 1,643.5 | 1,736.4 | 32.8 | 0.690x | 6.440x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,806.7 | 1,778.3 | 1,866.6 | 30.2 | 0.745x | 6.961x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,813.5 | 1,752.2 | 1,835.7 | 34.2 | 0.748x | 6.988x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,829.7 | 1,768.5 | 1,867.0 | 34.1 | 0.755x | 7.050x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,424.0 | 2,393.9 | 2,460.6 | 23.7 | 1.000x | 9.340x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-017` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 205.1 | 203.5 | 206.5 | 1.2 | 0.185x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 428.6 | 419.3 | 447.7 | 9.7 | 0.387x | 2.089x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 597.0 | 548.2 | 657.6 | 39.2 | 0.540x | 2.911x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 615.4 | 566.5 | 726.4 | 62.4 | 0.556x | 3.000x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 648.3 | 610.7 | 698.3 | 31.9 | 0.586x | 3.161x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,090.1 | 1,084.8 | 1,105.0 | 8.4 | 0.985x | 5.314x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,106.1 | 1,091.0 | 1,127.2 | 12.5 | 1.000x | 5.393x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-017` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 170.7 | 170.5 | 184.1 | 5.2 | 0.155x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 209.3 | 208.9 | 214.5 | 2.2 | 0.190x | 1.226x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 414.0 | 402.2 | 425.9 | 8.7 | 0.377x | 2.425x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 576.3 | 545.8 | 654.8 | 41.2 | 0.524x | 3.375x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 614.3 | 592.7 | 638.0 | 16.3 | 0.559x | 3.598x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 643.5 | 590.7 | 700.1 | 36.5 | 0.585x | 3.769x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,099.2 | 1,093.9 | 1,116.2 | 10.0 | 1.000x | 6.438x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-018` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 201.8 | 200.8 | 202.6 | 0.7 | 0.189x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 432.5 | 415.5 | 436.0 | 7.4 | 0.406x | 2.143x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 618.1 | 592.2 | 657.7 | 27.5 | 0.580x | 3.062x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 620.8 | 587.8 | 708.5 | 41.0 | 0.583x | 3.076x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 651.0 | 622.5 | 698.6 | 25.1 | 0.611x | 3.225x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,058.1 | 1,048.7 | 1,077.5 | 10.2 | 0.993x | 5.242x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,065.8 | 1,060.7 | 1,103.3 | 15.5 | 1.000x | 5.280x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-018` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 173.4 | 172.6 | 177.6 | 1.8 | 0.164x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 208.2 | 207.9 | 208.9 | 0.4 | 0.197x | 1.201x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 416.4 | 403.8 | 432.7 | 9.9 | 0.394x | 2.402x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 588.0 | 558.4 | 608.3 | 18.4 | 0.557x | 3.391x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 623.8 | 609.8 | 660.7 | 18.9 | 0.591x | 3.598x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 638.6 | 610.8 | 662.3 | 17.7 | 0.605x | 3.683x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,056.2 | 1,050.8 | 1,073.5 | 8.4 | 1.000x | 6.092x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-019` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 109.4 | 109.0 | 111.5 | 0.9 | 0.280x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 336.1 | 315.7 | 355.8 | 13.6 | 0.859x | 3.071x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 386.5 | 382.4 | 398.6 | 5.6 | 0.987x | 3.532x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 391.5 | 389.0 | 392.4 | 1.2 | 1.000x | 3.578x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 481.4 | 472.2 | 528.3 | 20.0 | 1.230x | 4.399x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 490.3 | 475.9 | 497.3 | 8.7 | 1.252x | 4.480x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 506.0 | 462.8 | 519.1 | 21.4 | 1.292x | 4.624x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-019` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 265.6 | 264.2 | 268.1 | 1.5 | 0.104x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 1,450.3 | 1,410.7 | 1,532.1 | 41.0 | 0.566x | 5.460x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,641.1 | 1,553.6 | 1,748.0 | 62.4 | 0.640x | 6.178x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,834.6 | 1,767.6 | 1,853.1 | 30.6 | 0.716x | 6.906x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,856.0 | 1,805.3 | 1,875.9 | 25.1 | 0.724x | 6.987x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,865.9 | 1,816.2 | 1,885.9 | 27.0 | 0.728x | 7.024x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,563.0 | 2,544.4 | 2,622.8 | 26.6 | 1.000x | 9.649x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-020` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 224.2 | 223.3 | 235.1 | 4.4 | 0.200x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 452.2 | 438.9 | 466.1 | 8.6 | 0.403x | 2.017x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 619.6 | 606.8 | 763.4 | 58.8 | 0.553x | 2.764x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 665.6 | 612.3 | 700.1 | 31.2 | 0.594x | 2.969x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 669.1 | 631.5 | 675.1 | 16.6 | 0.597x | 2.985x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,109.3 | 1,099.7 | 1,148.2 | 17.0 | 0.990x | 4.948x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,121.0 | 1,107.4 | 1,173.1 | 23.1 | 1.000x | 5.001x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-020` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 175.2 | 174.7 | 179.2 | 1.7 | 0.157x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 214.2 | 213.6 | 223.5 | 3.8 | 0.191x | 1.223x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 419.1 | 410.0 | 424.4 | 5.2 | 0.375x | 2.392x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 623.3 | 562.9 | 634.5 | 26.2 | 0.557x | 3.558x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 650.8 | 638.1 | 670.9 | 10.6 | 0.582x | 3.715x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 654.1 | 599.2 | 682.5 | 27.6 | 0.585x | 3.734x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,119.1 | 1,109.6 | 1,165.7 | 20.5 | 1.000x | 6.388x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-021` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 169.9 | 169.3 | 173.8 | 1.7 | 0.149x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 387.5 | 337.2 | 400.6 | 22.8 | 0.339x | 2.281x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 573.8 | 555.6 | 624.5 | 23.4 | 0.502x | 3.378x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 587.3 | 502.4 | 627.7 | 41.2 | 0.513x | 3.457x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 589.7 | 587.4 | 643.0 | 21.4 | 0.516x | 3.472x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,143.8 | 1,132.6 | 1,167.0 | 12.4 | 1.000x | 6.733x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,145.5 | 1,137.8 | 1,167.5 | 10.5 | 1.002x | 6.744x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-021` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 110.8 | 110.0 | 112.5 | 0.9 | 0.097x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 171.9 | 171.5 | 172.4 | 0.3 | 0.150x | 1.552x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 378.7 | 356.0 | 421.3 | 21.7 | 0.330x | 3.418x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 579.0 | 549.3 | 615.6 | 24.9 | 0.505x | 5.227x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 590.9 | 574.4 | 612.8 | 14.8 | 0.515x | 5.334x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 603.5 | 560.5 | 682.1 | 44.6 | 0.526x | 5.448x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,147.2 | 1,143.8 | 1,196.9 | 22.1 | 1.000x | 10.356x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-022` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 138.8 | 137.3 | 154.1 | 6.2 | 0.204x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 333.5 | 295.2 | 368.3 | 24.5 | 0.491x | 2.402x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 537.8 | 458.9 | 584.8 | 45.2 | 0.792x | 3.875x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 564.8 | 520.9 | 693.4 | 58.5 | 0.832x | 4.069x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 572.4 | 525.2 | 628.4 | 32.9 | 0.843x | 4.124x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 679.0 | 677.5 | 692.7 | 5.7 | 1.000x | 4.892x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 680.8 | 677.8 | 691.2 | 4.7 | 1.003x | 4.905x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-022` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 99.4 | 98.3 | 99.6 | 0.6 | 0.144x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 141.4 | 141.1 | 141.8 | 0.2 | 0.205x | 1.422x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 355.9 | 324.9 | 366.3 | 15.2 | 0.516x | 3.581x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 530.8 | 480.7 | 583.3 | 34.9 | 0.770x | 5.339x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 538.2 | 516.9 | 640.6 | 43.6 | 0.781x | 5.415x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 548.8 | 493.2 | 585.9 | 32.8 | 0.796x | 5.521x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 689.3 | 678.3 | 708.9 | 10.9 | 1.000x | 6.935x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-023` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 170.6 | 170.0 | 172.0 | 0.7 | 0.151x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 390.9 | 344.7 | 402.3 | 20.3 | 0.345x | 2.291x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 552.4 | 443.6 | 577.8 | 47.0 | 0.487x | 3.237x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 555.0 | 467.7 | 571.8 | 37.9 | 0.490x | 3.252x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 558.7 | 550.1 | 630.6 | 31.3 | 0.493x | 3.274x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,123.6 | 1,121.4 | 1,134.1 | 5.0 | 0.991x | 6.585x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,133.3 | 1,124.5 | 1,173.3 | 17.3 | 1.000x | 6.642x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-023` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 106.9 | 106.5 | 107.4 | 0.3 | 0.094x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 172.7 | 172.4 | 172.9 | 0.2 | 0.152x | 1.615x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 380.0 | 356.2 | 422.4 | 21.7 | 0.334x | 3.554x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 570.7 | 560.1 | 621.0 | 22.0 | 0.501x | 5.337x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 576.8 | 558.3 | 691.1 | 51.8 | 0.506x | 5.394x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 589.0 | 541.4 | 613.1 | 24.1 | 0.517x | 5.508x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,138.9 | 1,121.7 | 1,201.5 | 29.3 | 1.000x | 10.651x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-024` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 173.4 | 173.4 | 173.5 | 0.1 | 0.151x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 393.4 | 377.5 | 401.0 | 8.4 | 0.344x | 2.269x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 512.9 | 466.1 | 545.4 | 28.4 | 0.448x | 2.957x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 546.5 | 512.8 | 605.9 | 36.6 | 0.477x | 3.152x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 560.5 | 504.1 | 594.4 | 29.7 | 0.489x | 3.232x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,145.3 | 1,138.9 | 1,156.9 | 5.9 | 1.000x | 6.605x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,154.8 | 1,150.8 | 1,162.0 | 4.0 | 1.008x | 6.659x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-024` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 109.9 | 108.6 | 111.9 | 1.2 | 0.094x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 176.0 | 175.7 | 176.5 | 0.3 | 0.150x | 1.603x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 381.7 | 360.1 | 387.5 | 9.7 | 0.325x | 3.475x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 590.9 | 518.2 | 645.9 | 41.9 | 0.503x | 5.379x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 591.3 | 513.3 | 631.4 | 48.7 | 0.504x | 5.383x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 612.6 | 565.1 | 690.5 | 46.0 | 0.522x | 5.576x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,173.8 | 1,150.1 | 1,181.1 | 12.5 | 1.000x | 10.685x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-025` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 175.9 | 175.6 | 176.1 | 0.2 | 0.155x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 418.7 | 388.7 | 429.4 | 15.5 | 0.370x | 2.381x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 486.9 | 432.4 | 528.0 | 35.4 | 0.430x | 2.769x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 526.1 | 455.2 | 655.5 | 65.1 | 0.464x | 2.991x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 529.2 | 486.7 | 539.9 | 21.3 | 0.467x | 3.009x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,132.9 | 1,126.8 | 1,154.0 | 9.2 | 1.000x | 6.442x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,137.9 | 1,123.3 | 1,141.9 | 6.7 | 1.004x | 6.470x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-025` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 107.1 | 106.3 | 107.5 | 0.4 | 0.094x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 178.4 | 178.0 | 180.2 | 0.8 | 0.156x | 1.665x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 390.7 | 370.1 | 412.0 | 13.3 | 0.341x | 3.647x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 562.2 | 499.5 | 618.4 | 42.4 | 0.491x | 5.248x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 581.4 | 524.1 | 658.0 | 48.5 | 0.508x | 5.428x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 585.1 | 561.8 | 643.9 | 32.6 | 0.511x | 5.463x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,145.5 | 1,128.7 | 1,177.2 | 17.5 | 1.000x | 10.694x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-026` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 138.6 | 137.6 | 141.0 | 1.3 | 0.205x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 354.9 | 297.0 | 387.5 | 29.8 | 0.524x | 2.560x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 509.5 | 453.8 | 571.6 | 40.5 | 0.753x | 3.676x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 535.4 | 448.0 | 648.9 | 67.3 | 0.791x | 3.864x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 546.9 | 527.9 | 624.2 | 33.8 | 0.808x | 3.946x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 676.6 | 673.6 | 688.8 | 5.5 | 1.000x | 4.882x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 679.6 | 674.3 | 684.4 | 3.5 | 1.005x | 4.904x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-026` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 98.5 | 98.3 | 99.1 | 0.3 | 0.143x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 141.8 | 141.1 | 142.1 | 0.3 | 0.206x | 1.439x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 357.5 | 299.8 | 403.2 | 35.3 | 0.520x | 3.629x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 530.1 | 509.0 | 601.9 | 34.5 | 0.771x | 5.381x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 552.1 | 525.9 | 582.3 | 18.9 | 0.803x | 5.604x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 562.1 | 522.0 | 615.9 | 35.9 | 0.818x | 5.706x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 687.4 | 675.9 | 694.0 | 6.6 | 1.000x | 6.978x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-027` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 171.5 | 170.9 | 175.8 | 1.8 | 0.160x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 410.1 | 384.3 | 428.0 | 16.3 | 0.382x | 2.391x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 504.7 | 477.0 | 568.0 | 30.5 | 0.470x | 2.943x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 527.4 | 484.3 | 556.5 | 26.6 | 0.491x | 3.075x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 538.0 | 515.0 | 628.3 | 39.8 | 0.501x | 3.137x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,073.3 | 1,066.4 | 1,076.8 | 4.4 | 0.999x | 6.258x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,074.2 | 1,056.1 | 1,089.9 | 12.7 | 1.000x | 6.263x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-027` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 104.8 | 104.0 | 105.3 | 0.5 | 0.096x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 173.4 | 172.9 | 173.6 | 0.2 | 0.159x | 1.654x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 385.5 | 377.2 | 405.5 | 9.4 | 0.354x | 3.678x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 560.5 | 520.8 | 609.5 | 30.4 | 0.514x | 5.348x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 564.4 | 548.6 | 590.6 | 17.5 | 0.518x | 5.385x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 609.1 | 551.0 | 681.8 | 45.6 | 0.559x | 5.811x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,090.2 | 1,070.2 | 1,106.4 | 11.7 | 1.000x | 10.401x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-028` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 187.9 | 185.9 | 189.9 | 1.4 | 0.242x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 430.1 | 412.8 | 448.3 | 11.6 | 0.554x | 2.289x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 554.4 | 542.5 | 581.7 | 15.3 | 0.714x | 2.951x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 555.1 | 534.4 | 604.5 | 23.8 | 0.715x | 2.955x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 572.6 | 555.8 | 622.2 | 22.7 | 0.737x | 3.048x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 776.9 | 772.5 | 816.0 | 16.1 | 1.000x | 4.136x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 780.1 | 775.1 | 797.4 | 8.0 | 1.004x | 4.153x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-028` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 221.3 | 211.0 | 229.5 | 5.9 | 0.082x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 934.3 | 902.9 | 1,079.8 | 62.5 | 0.347x | 4.222x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,103.3 | 1,076.8 | 1,138.0 | 20.0 | 0.409x | 4.986x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,419.9 | 1,409.4 | 1,436.4 | 10.9 | 0.527x | 6.417x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,427.2 | 1,379.3 | 1,448.9 | 23.6 | 0.530x | 6.450x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,429.5 | 1,392.0 | 1,528.8 | 45.9 | 0.530x | 6.460x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,695.2 | 2,680.2 | 2,824.8 | 54.3 | 1.000x | 12.180x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-029` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 189.4 | 183.2 | 190.8 | 2.9 | 0.242x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 428.7 | 419.7 | 438.6 | 7.5 | 0.549x | 2.264x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 553.4 | 540.8 | 592.4 | 20.1 | 0.708x | 2.922x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 553.9 | 531.4 | 563.7 | 13.2 | 0.709x | 2.925x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 564.8 | 555.1 | 613.9 | 20.9 | 0.723x | 2.982x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 779.1 | 763.3 | 805.4 | 13.9 | 0.997x | 4.114x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 781.1 | 774.9 | 789.3 | 5.1 | 1.000x | 4.125x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-029` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 235.1 | 232.2 | 237.8 | 2.1 | 0.087x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,707.1 | 2,668.0 | 2,794.6 | 49.4 | 1.000x | 11.513x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 3,330.5 | 3,291.4 | 3,432.4 | 57.7 | 1.230x | 14.165x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 3,345.6 | 3,284.5 | 3,384.5 | 32.4 | 1.236x | 14.229x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 4,412.9 | 4,402.6 | 4,447.4 | 15.7 | 1.630x | 18.768x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 4,423.8 | 4,355.4 | 4,445.3 | 33.3 | 1.634x | 18.815x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 4,456.4 | 4,346.2 | 4,548.4 | 71.4 | 1.646x | 18.953x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-030` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 186.9 | 186.4 | 188.5 | 0.8 | 0.239x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 426.7 | 416.0 | 429.9 | 5.0 | 0.545x | 2.284x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 557.0 | 531.4 | 570.4 | 15.1 | 0.712x | 2.981x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 568.4 | 554.5 | 589.5 | 14.4 | 0.726x | 3.042x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 574.6 | 550.8 | 616.8 | 26.0 | 0.734x | 3.075x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 782.7 | 772.1 | 801.7 | 10.0 | 1.000x | 4.189x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 783.3 | 772.3 | 804.2 | 11.7 | 1.001x | 4.192x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-030` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 218.9 | 216.5 | 222.5 | 2.1 | 0.081x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 872.6 | 842.3 | 902.4 | 20.0 | 0.322x | 3.987x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,047.5 | 962.9 | 1,095.6 | 45.5 | 0.386x | 4.786x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,447.1 | 1,409.9 | 1,531.8 | 41.7 | 0.533x | 6.612x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,450.7 | 1,440.5 | 1,503.3 | 23.9 | 0.535x | 6.629x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,488.1 | 1,340.5 | 1,520.2 | 64.8 | 0.548x | 6.799x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,713.4 | 2,677.4 | 2,785.1 | 44.1 | 1.000x | 12.398x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-031` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 189.6 | 187.0 | 190.6 | 1.3 | 0.242x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 423.7 | 411.5 | 433.4 | 8.0 | 0.542x | 2.235x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 554.7 | 546.4 | 563.4 | 6.2 | 0.709x | 2.926x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 567.0 | 553.3 | 617.6 | 25.9 | 0.725x | 2.991x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 577.4 | 553.8 | 584.0 | 11.1 | 0.738x | 3.046x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 780.1 | 771.7 | 803.7 | 11.6 | 0.997x | 4.115x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 782.2 | 774.7 | 800.8 | 9.8 | 1.000x | 4.126x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-031` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 230.7 | 229.7 | 235.2 | 2.1 | 0.086x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 1,410.3 | 1,381.0 | 1,550.0 | 60.5 | 0.527x | 6.112x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,558.2 | 1,539.8 | 1,605.6 | 22.2 | 0.583x | 6.753x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 2,029.2 | 1,989.0 | 2,113.6 | 44.2 | 0.759x | 8.794x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 2,051.3 | 1,992.1 | 2,109.4 | 38.1 | 0.767x | 8.890x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 2,079.6 | 1,997.4 | 2,176.5 | 58.9 | 0.778x | 9.012x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,673.9 | 2,666.6 | 2,807.1 | 55.0 | 1.000x | 11.588x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-032` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 303.9 | 266.3 | 321.7 | 19.6 | 0.328x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 527.3 | 490.7 | 560.8 | 23.1 | 0.570x | 1.735x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 594.5 | 564.5 | 639.2 | 24.7 | 0.642x | 1.957x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 610.8 | 597.9 | 615.1 | 7.2 | 0.660x | 2.010x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 634.0 | 591.0 | 647.5 | 20.4 | 0.685x | 2.086x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 925.8 | 915.9 | 953.5 | 12.7 | 1.000x | 3.047x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 934.3 | 923.0 | 964.9 | 14.3 | 1.009x | 3.075x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-032` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 323.4 | 314.0 | 325.4 | 4.7 | 0.098x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 1,742.4 | 1,735.8 | 1,750.6 | 5.0 | 0.531x | 5.387x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,746.4 | 1,722.4 | 1,856.2 | 52.7 | 0.532x | 5.400x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,771.6 | 1,739.3 | 1,793.5 | 20.2 | 0.539x | 5.477x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,786.6 | 1,707.7 | 1,827.8 | 45.8 | 0.544x | 5.524x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,930.6 | 1,920.3 | 1,943.1 | 8.0 | 0.588x | 5.969x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,284.0 | 3,255.3 | 3,414.3 | 59.2 | 1.000x | 10.153x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-033` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 268.8 | 255.5 | 298.7 | 15.9 | 0.309x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 513.0 | 507.4 | 551.9 | 16.7 | 0.590x | 1.909x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 600.9 | 574.8 | 621.8 | 17.5 | 0.691x | 2.235x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 610.4 | 577.4 | 638.2 | 20.1 | 0.702x | 2.271x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 611.1 | 590.1 | 637.0 | 16.7 | 0.703x | 2.273x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 869.7 | 868.0 | 913.9 | 17.7 | 1.000x | 3.235x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 872.9 | 872.4 | 896.1 | 9.1 | 1.004x | 3.247x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-033` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 326.2 | 316.7 | 335.9 | 7.4 | 0.107x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 1,726.9 | 1,719.7 | 1,740.3 | 7.3 | 0.566x | 5.294x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,756.7 | 1,714.1 | 1,781.6 | 25.9 | 0.576x | 5.385x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,767.7 | 1,715.8 | 1,805.5 | 31.6 | 0.580x | 5.419x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,780.4 | 1,716.8 | 1,802.8 | 35.0 | 0.584x | 5.458x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,924.4 | 1,898.8 | 1,977.8 | 26.4 | 0.631x | 5.900x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,048.6 | 3,027.0 | 3,186.7 | 69.7 | 1.000x | 9.346x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-034` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 153.4 | 152.1 | 153.7 | 0.6 | 0.123x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 375.4 | 348.9 | 380.0 | 11.4 | 0.300x | 2.446x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 520.4 | 488.8 | 579.5 | 29.7 | 0.416x | 3.392x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 535.8 | 504.5 | 568.8 | 22.2 | 0.428x | 3.492x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 536.8 | 500.6 | 557.1 | 20.5 | 0.429x | 3.498x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,250.8 | 1,242.9 | 1,286.5 | 15.2 | 1.000x | 8.152x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,253.4 | 1,245.3 | 1,290.0 | 15.6 | 1.002x | 8.168x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-034` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 385.8 | 383.4 | 390.1 | 2.2 | 0.082x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 682.7 | 664.0 | 728.8 | 24.9 | 0.145x | 1.770x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 860.2 | 810.2 | 901.9 | 31.9 | 0.183x | 2.230x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,034.4 | 1,006.6 | 1,133.9 | 47.1 | 0.220x | 2.681x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,045.1 | 998.1 | 1,076.8 | 29.7 | 0.222x | 2.709x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,065.5 | 1,032.4 | 1,091.0 | 20.1 | 0.226x | 2.762x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,704.2 | 4,611.0 | 4,784.4 | 64.8 | 1.000x | 12.194x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-035` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 387.6 | 385.4 | 391.0 | 2.0 | 0.247x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 708.9 | 703.6 | 712.0 | 2.8 | 0.451x | 1.829x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 731.3 | 707.9 | 793.0 | 29.1 | 0.465x | 1.887x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 752.5 | 739.4 | 831.3 | 33.6 | 0.479x | 1.942x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 767.8 | 698.3 | 793.0 | 31.8 | 0.489x | 1.981x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,571.2 | 1,569.0 | 1,604.5 | 13.4 | 1.000x | 4.054x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,586.1 | 1,579.9 | 1,618.9 | 14.0 | 1.009x | 4.092x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-035` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 486.7 | 472.9 | 523.3 | 17.4 | 0.082x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 1,776.0 | 1,763.2 | 1,791.0 | 8.8 | 0.300x | 3.649x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,966.7 | 1,949.6 | 2,006.1 | 21.2 | 0.333x | 4.041x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 2,285.0 | 2,243.8 | 2,352.5 | 36.6 | 0.386x | 4.695x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 2,289.2 | 2,218.5 | 2,367.3 | 58.8 | 0.387x | 4.704x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 2,291.2 | 2,217.7 | 2,301.8 | 31.6 | 0.387x | 4.708x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 5,913.8 | 5,883.7 | 6,023.9 | 57.7 | 1.000x | 12.151x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-036` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 153.3 | 152.0 | 156.2 | 1.5 | 0.244x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 377.2 | 363.4 | 383.3 | 6.8 | 0.599x | 2.461x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 545.2 | 524.6 | 568.4 | 16.6 | 0.866x | 3.557x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 549.7 | 535.4 | 561.7 | 9.8 | 0.873x | 3.586x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 564.2 | 538.7 | 618.5 | 26.6 | 0.896x | 3.681x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 629.3 | 623.2 | 643.5 | 6.9 | 1.000x | 4.106x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 632.1 | 624.7 | 652.4 | 9.5 | 1.004x | 4.124x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-036` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 195.0 | 194.4 | 195.4 | 0.4 | 0.093x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 1,506.0 | 1,491.2 | 1,601.6 | 39.5 | 0.721x | 7.723x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,682.0 | 1,621.0 | 1,767.1 | 47.5 | 0.806x | 8.625x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,964.5 | 1,947.4 | 2,031.3 | 29.0 | 0.941x | 10.074x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,970.7 | 1,967.2 | 2,012.3 | 19.0 | 0.944x | 10.105x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,983.5 | 1,906.7 | 2,002.5 | 35.9 | 0.950x | 10.171x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,088.1 | 2,062.7 | 2,171.6 | 41.1 | 1.000x | 10.708x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-037` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 214.9 | 213.6 | 216.1 | 0.9 | 0.252x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 438.4 | 431.9 | 455.9 | 8.4 | 0.514x | 2.040x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 585.7 | 569.5 | 630.3 | 21.3 | 0.687x | 2.726x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 589.5 | 571.7 | 640.2 | 26.9 | 0.691x | 2.743x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 608.1 | 526.8 | 642.4 | 39.7 | 0.713x | 2.830x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 840.7 | 836.3 | 850.2 | 4.8 | 0.986x | 3.912x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 852.5 | 844.8 | 859.4 | 4.9 | 1.000x | 3.967x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-037` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 287.0 | 285.8 | 289.5 | 1.3 | 0.098x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 1,226.7 | 1,155.4 | 1,242.3 | 31.9 | 0.417x | 4.274x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,503.4 | 1,446.5 | 1,570.2 | 40.8 | 0.511x | 5.238x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,510.7 | 1,461.9 | 1,558.1 | 32.8 | 0.514x | 5.263x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,514.4 | 1,433.5 | 1,521.9 | 37.0 | 0.515x | 5.276x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,524.5 | 1,483.7 | 1,532.7 | 17.9 | 0.518x | 5.311x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,940.2 | 2,913.6 | 3,070.2 | 55.4 | 1.000x | 10.243x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-038` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 473.1 | 354.4 | 493.9 | 50.8 | 0.469x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 645.7 | 614.6 | 665.0 | 17.4 | 0.640x | 1.365x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 676.8 | 623.7 | 687.6 | 25.1 | 0.671x | 1.431x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 697.9 | 637.7 | 727.9 | 34.3 | 0.691x | 1.475x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 698.6 | 692.3 | 732.6 | 14.8 | 0.692x | 1.477x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 999.8 | 995.7 | 1,043.2 | 17.8 | 0.990x | 2.113x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,009.4 | 995.2 | 1,056.9 | 22.5 | 1.000x | 2.134x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-038` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 569.9 | 565.0 | 572.4 | 2.6 | 0.159x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 2,453.6 | 2,449.3 | 2,520.2 | 32.4 | 0.683x | 4.305x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 2,501.9 | 2,481.9 | 2,548.1 | 24.7 | 0.696x | 4.390x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 2,507.4 | 2,486.5 | 2,517.1 | 11.1 | 0.698x | 4.400x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 2,869.1 | 2,862.9 | 2,924.6 | 22.7 | 0.798x | 5.034x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 3,089.5 | 3,049.7 | 3,169.4 | 41.6 | 0.860x | 5.421x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,593.5 | 3,585.7 | 4,022.8 | 169.0 | 1.000x | 6.306x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-039` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 108.0 | 107.3 | 110.1 | 1.0 | 0.284x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 325.8 | 311.8 | 340.1 | 10.8 | 0.857x | 3.017x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 380.0 | 378.6 | 395.1 | 6.3 | 1.000x | 3.519x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 381.9 | 374.9 | 401.3 | 9.5 | 1.005x | 3.537x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 473.6 | 436.1 | 493.7 | 19.2 | 1.246x | 4.386x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 480.7 | 444.8 | 524.4 | 31.9 | 1.265x | 4.451x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 500.0 | 436.8 | 515.3 | 28.6 | 1.316x | 4.630x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-039` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 211.8 | 211.1 | 214.0 | 1.0 | 0.135x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 305.2 | 299.9 | 346.0 | 17.1 | 0.194x | 1.441x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 496.5 | 486.9 | 500.7 | 4.9 | 0.316x | 2.344x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 698.7 | 671.1 | 719.9 | 16.6 | 0.444x | 3.298x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 706.4 | 656.3 | 759.8 | 36.0 | 0.449x | 3.335x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 748.1 | 672.6 | 775.8 | 35.7 | 0.476x | 3.531x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,572.3 | 1,551.9 | 1,637.2 | 30.7 | 1.000x | 7.422x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-040` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 33.3 | 33.1 | 35.3 | 0.8 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 34.6 | 34.1 | 35.3 | 0.5 | 1.040x | 1.040x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 262.8 | 258.8 | 273.7 | 5.0 | 7.894x | 7.894x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 482.7 | 480.2 | 484.0 | 1.4 | 14.500x | 14.500x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 644.3 | 623.7 | 682.0 | 22.5 | 19.357x | 19.357x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 668.5 | 645.5 | 690.6 | 17.5 | 20.082x | 20.082x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 707.1 | 638.4 | 724.9 | 37.0 | 21.243x | 21.243x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-040` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 35.2 | 34.7 | 52.3 | 6.7 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.3 | 44.3 | 44.6 | 0.1 | 1.260x | 1.260x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 1,827.1 | 1,752.0 | 1,865.2 | 39.7 | 51.923x | 51.923x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,965.6 | 1,848.9 | 2,066.3 | 87.9 | 55.860x | 55.860x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 2,193.6 | 2,189.2 | 2,204.8 | 5.9 | 62.341x | 62.341x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 2,214.4 | 2,211.8 | 2,245.4 | 13.1 | 62.930x | 62.930x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 2,224.4 | 2,124.1 | 2,352.7 | 89.9 | 63.215x | 63.215x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-041` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 54.8 | 54.5 | 54.9 | 0.2 | 0.337x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 162.7 | 161.9 | 165.8 | 1.4 | 1.000x | 2.968x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 164.3 | 160.1 | 164.9 | 1.7 | 1.010x | 2.997x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 277.7 | 270.0 | 293.1 | 8.0 | 1.707x | 5.066x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 418.1 | 401.8 | 456.7 | 21.1 | 2.569x | 7.627x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 428.8 | 422.0 | 455.5 | 13.9 | 2.635x | 7.822x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 429.6 | 409.5 | 451.9 | 14.6 | 2.639x | 7.835x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-041` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 54.8 | 54.7 | 64.6 | 3.9 | 0.285x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 192.0 | 178.7 | 197.2 | 7.0 | 1.000x | 3.503x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 949.6 | 924.5 | 1,024.5 | 38.4 | 4.945x | 17.326x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,183.8 | 1,079.5 | 1,246.3 | 64.5 | 6.165x | 21.599x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,342.9 | 1,289.5 | 1,407.5 | 40.5 | 6.993x | 24.500x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,359.6 | 1,344.5 | 1,379.8 | 12.6 | 7.080x | 24.805x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,371.7 | 1,359.5 | 1,408.8 | 16.9 | 7.144x | 25.027x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-042` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 82.9 | 79.7 | 103.2 | 10.6 | 0.136x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 291.5 | 283.9 | 320.4 | 13.3 | 0.479x | 3.519x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 504.3 | 485.4 | 581.2 | 35.2 | 0.829x | 6.087x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 517.4 | 415.0 | 536.9 | 46.7 | 0.851x | 6.245x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 530.1 | 471.9 | 549.7 | 27.1 | 0.871x | 6.398x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 608.3 | 602.7 | 624.2 | 7.2 | 1.000x | 7.342x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 612.4 | 610.0 | 623.7 | 4.8 | 1.007x | 7.391x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-042` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 84.0 | 83.6 | 129.7 | 18.3 | 0.133x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 176.5 | 174.1 | 180.6 | 2.1 | 0.279x | 2.100x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 370.1 | 369.0 | 383.3 | 5.5 | 0.586x | 4.406x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 632.1 | 617.9 | 1,078.8 | 179.5 | 1.000x | 7.524x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 712.9 | 705.4 | 802.1 | 35.9 | 1.128x | 8.485x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 737.3 | 704.8 | 742.0 | 15.3 | 1.166x | 8.776x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 740.5 | 695.8 | 772.1 | 25.4 | 1.171x | 8.814x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-043` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 151.6 | 150.7 | 153.4 | 0.9 | 0.263x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 379.8 | 369.3 | 417.5 | 17.5 | 0.659x | 2.505x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 522.2 | 506.5 | 566.0 | 20.3 | 0.906x | 3.445x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 562.0 | 503.7 | 574.5 | 25.7 | 0.976x | 3.708x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 571.1 | 463.8 | 584.6 | 49.9 | 0.991x | 3.768x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 576.1 | 569.9 | 600.1 | 11.8 | 1.000x | 3.801x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 576.3 | 571.5 | 584.8 | 4.6 | 1.000x | 3.802x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-043` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 290.1 | 289.6 | 292.5 | 1.1 | 0.102x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 722.6 | 668.4 | 751.2 | 29.4 | 0.255x | 2.491x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 955.0 | 924.2 | 988.0 | 20.8 | 0.336x | 3.292x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 998.8 | 945.8 | 1,026.1 | 28.5 | 0.352x | 3.444x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,001.7 | 980.7 | 1,040.1 | 22.7 | 0.353x | 3.453x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,012.3 | 969.5 | 1,046.1 | 27.2 | 0.357x | 3.490x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,838.6 | 2,800.5 | 2,875.0 | 28.7 | 1.000x | 9.786x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-044` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 54.6 | 54.5 | 55.3 | 0.3 | 0.334x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 161.9 | 158.6 | 163.4 | 1.7 | 0.989x | 2.963x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 163.7 | 161.3 | 165.8 | 1.9 | 1.000x | 2.996x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 287.0 | 280.3 | 306.7 | 9.8 | 1.753x | 5.251x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 419.6 | 389.7 | 467.6 | 26.1 | 2.562x | 7.678x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 424.5 | 371.3 | 432.2 | 22.1 | 2.593x | 7.768x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 428.1 | 392.2 | 459.5 | 22.8 | 2.614x | 7.833x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-044` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 160.1 | 159.0 | 160.8 | 0.7 | 0.157x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 172.2 | 171.8 | 173.8 | 0.7 | 0.169x | 1.076x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 385.4 | 366.2 | 398.8 | 12.2 | 0.378x | 2.407x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 533.0 | 472.7 | 583.9 | 37.9 | 0.523x | 3.329x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 549.5 | 501.4 | 566.0 | 23.0 | 0.540x | 3.432x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 568.6 | 535.4 | 640.6 | 38.5 | 0.558x | 3.551x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,018.5 | 1,012.3 | 1,038.0 | 8.8 | 1.000x | 6.361x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-045` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 150.9 | 149.8 | 152.1 | 0.9 | 0.260x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 368.1 | 363.8 | 418.1 | 20.3 | 0.635x | 2.439x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 530.6 | 460.8 | 573.5 | 40.4 | 0.915x | 3.515x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 542.5 | 521.8 | 601.5 | 27.0 | 0.936x | 3.594x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 565.8 | 537.6 | 607.1 | 23.8 | 0.976x | 3.749x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 575.6 | 573.6 | 602.9 | 11.5 | 0.993x | 3.813x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 579.8 | 569.5 | 653.3 | 30.8 | 1.000x | 3.841x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-045` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 197.5 | 196.0 | 199.8 | 1.4 | 0.096x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 1,405.0 | 1,296.7 | 1,600.0 | 104.9 | 0.680x | 7.114x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,596.6 | 1,501.8 | 1,783.2 | 108.5 | 0.773x | 8.085x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,804.6 | 1,790.8 | 1,828.1 | 13.0 | 0.873x | 9.138x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,819.9 | 1,796.6 | 1,844.0 | 15.9 | 0.881x | 9.216x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,823.7 | 1,798.6 | 1,844.7 | 16.1 | 0.883x | 9.235x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,066.4 | 1,985.6 | 2,259.9 | 99.9 | 1.000x | 10.464x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-046` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 378.2 | 354.2 | 414.8 | 21.3 | 0.377x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 597.5 | 585.8 | 633.8 | 17.3 | 0.596x | 1.580x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 666.3 | 641.0 | 687.0 | 15.1 | 0.664x | 1.762x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 671.0 | 637.4 | 705.9 | 27.3 | 0.669x | 1.774x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 688.3 | 638.3 | 707.5 | 27.9 | 0.686x | 1.820x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 998.1 | 993.4 | 1,018.2 | 9.9 | 0.995x | 2.639x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,002.9 | 991.0 | 1,009.0 | 6.9 | 1.000x | 2.652x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-046` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 538.3 | 535.8 | 543.2 | 2.5 | 0.150x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 1,731.2 | 1,717.7 | 1,776.5 | 21.3 | 0.484x | 3.216x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,908.3 | 1,889.9 | 1,944.9 | 19.2 | 0.534x | 3.545x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,967.0 | 1,883.7 | 2,010.0 | 45.3 | 0.550x | 3.654x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,969.6 | 1,960.7 | 1,982.3 | 8.0 | 0.551x | 3.659x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,971.3 | 1,927.4 | 1,996.9 | 29.1 | 0.551x | 3.662x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,576.8 | 3,497.5 | 3,605.1 | 37.9 | 1.000x | 6.645x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-047` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 152.6 | 151.7 | 154.6 | 1.0 | 0.094x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 387.1 | 380.6 | 389.5 | 3.1 | 0.239x | 2.536x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 524.4 | 493.6 | 564.7 | 24.8 | 0.324x | 3.437x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 527.0 | 499.6 | 570.7 | 29.9 | 0.325x | 3.454x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 562.0 | 518.5 | 587.1 | 23.9 | 0.347x | 3.683x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,620.4 | 1,606.5 | 1,655.1 | 16.5 | 1.000x | 10.619x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,627.9 | 1,598.9 | 1,660.0 | 20.1 | 1.005x | 10.668x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-047` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 474.0 | 464.6 | 485.2 | 6.8 | 0.078x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 716.3 | 715.3 | 795.3 | 33.6 | 0.118x | 1.511x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 981.5 | 929.3 | 1,039.0 | 40.0 | 0.161x | 2.071x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,127.6 | 1,077.0 | 1,158.3 | 27.4 | 0.185x | 2.379x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,130.6 | 1,122.5 | 1,163.5 | 15.6 | 0.186x | 2.385x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,133.5 | 1,108.0 | 1,196.4 | 31.0 | 0.186x | 2.391x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 6,090.9 | 6,019.8 | 6,203.6 | 67.0 | 1.000x | 12.850x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-048` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 110.0 | 109.7 | 111.4 | 0.6 | 0.142x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 345.5 | 342.6 | 347.4 | 2.0 | 0.445x | 3.141x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 494.5 | 427.4 | 527.2 | 34.1 | 0.637x | 4.496x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 528.8 | 495.9 | 559.5 | 23.3 | 0.681x | 4.807x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 529.7 | 480.2 | 550.1 | 23.9 | 0.682x | 4.815x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 776.3 | 774.3 | 801.9 | 10.5 | 1.000x | 7.057x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 779.6 | 773.4 | 806.5 | 12.1 | 1.004x | 7.087x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-048` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 187.1 | 178.9 | 188.6 | 3.7 | 0.092x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 312.3 | 310.8 | 325.1 | 5.3 | 0.153x | 1.669x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 555.3 | 528.5 | 599.0 | 24.8 | 0.272x | 2.968x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 751.4 | 750.3 | 777.4 | 11.8 | 0.368x | 4.016x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 773.0 | 744.6 | 847.8 | 35.4 | 0.379x | 4.131x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 791.9 | 753.2 | 810.8 | 19.4 | 0.388x | 4.232x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,042.0 | 2,025.7 | 2,116.1 | 33.8 | 1.000x | 10.912x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-049` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 134.8 | 132.9 | 137.0 | 1.3 | 0.248x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 368.1 | 348.5 | 375.8 | 9.5 | 0.676x | 2.730x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 516.9 | 464.7 | 539.4 | 25.4 | 0.950x | 3.834x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 528.4 | 494.5 | 632.1 | 56.5 | 0.971x | 3.919x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 544.2 | 542.6 | 550.9 | 3.4 | 1.000x | 4.036x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 546.7 | 545.1 | 554.8 | 3.6 | 1.005x | 4.055x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 559.4 | 541.4 | 584.5 | 15.4 | 1.028x | 4.150x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-049` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 271.9 | 271.5 | 275.0 | 1.3 | 0.105x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 591.0 | 587.3 | 608.8 | 7.8 | 0.228x | 2.174x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 802.6 | 787.6 | 836.3 | 16.7 | 0.310x | 2.952x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 836.5 | 794.4 | 867.2 | 25.7 | 0.323x | 3.076x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 872.4 | 839.7 | 932.8 | 31.6 | 0.337x | 3.208x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 896.6 | 837.1 | 901.7 | 26.0 | 0.346x | 3.297x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,588.8 | 2,546.1 | 2,632.3 | 29.1 | 1.000x | 9.521x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-050` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 247.5 | 232.8 | 262.6 | 10.1 | 0.324x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 483.7 | 473.0 | 529.5 | 20.9 | 0.633x | 1.955x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 546.5 | 510.6 | 619.4 | 41.9 | 0.716x | 2.208x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 572.6 | 526.5 | 591.2 | 24.1 | 0.750x | 2.314x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 601.6 | 551.0 | 655.7 | 39.6 | 0.788x | 2.431x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 763.7 | 760.6 | 801.8 | 15.7 | 1.000x | 3.086x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 769.2 | 758.2 | 774.7 | 6.9 | 1.007x | 3.109x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-050` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 381.8 | 374.9 | 388.6 | 4.3 | 0.107x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 1,035.9 | 1,023.5 | 1,043.6 | 7.7 | 0.289x | 2.713x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,164.0 | 1,076.4 | 1,177.1 | 41.3 | 0.325x | 3.048x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,194.0 | 1,146.4 | 1,201.8 | 23.6 | 0.333x | 3.127x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,199.4 | 1,084.9 | 1,229.9 | 49.7 | 0.335x | 3.141x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,203.9 | 1,186.7 | 1,246.7 | 21.5 | 0.336x | 3.153x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,581.4 | 3,492.4 | 3,625.9 | 51.9 | 1.000x | 9.380x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-051` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 133.0 | 131.1 | 135.2 | 1.3 | 0.242x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 365.7 | 362.1 | 383.5 | 7.6 | 0.667x | 2.749x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 504.6 | 478.3 | 556.9 | 31.1 | 0.920x | 3.793x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 547.4 | 518.0 | 575.6 | 21.9 | 0.998x | 4.115x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 548.6 | 540.1 | 550.2 | 3.7 | 1.000x | 4.124x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 548.8 | 544.4 | 605.7 | 23.3 | 1.000x | 4.126x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 558.9 | 482.5 | 613.8 | 44.5 | 1.019x | 4.202x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-051` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 273.2 | 272.7 | 275.1 | 0.8 | 0.106x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 593.9 | 549.8 | 602.7 | 21.1 | 0.230x | 2.174x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 814.2 | 802.1 | 820.9 | 6.6 | 0.315x | 2.980x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 825.8 | 751.8 | 855.8 | 35.1 | 0.319x | 3.023x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 883.0 | 822.9 | 888.7 | 24.9 | 0.342x | 3.232x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 886.3 | 843.0 | 892.6 | 18.8 | 0.343x | 3.244x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,585.0 | 2,554.3 | 2,639.2 | 32.8 | 1.000x | 9.463x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-052` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 153.0 | 151.3 | 154.4 | 1.2 | 0.196x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 384.9 | 376.8 | 397.6 | 7.3 | 0.494x | 2.516x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 521.4 | 495.6 | 536.5 | 18.0 | 0.670x | 3.408x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 526.5 | 505.2 | 577.8 | 28.3 | 0.676x | 3.441x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 532.4 | 482.6 | 552.4 | 23.7 | 0.684x | 3.480x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 778.7 | 772.5 | 808.0 | 15.4 | 1.000x | 5.090x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 780.8 | 771.8 | 792.0 | 7.3 | 1.003x | 5.104x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-052` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 218.8 | 214.2 | 221.2 | 2.7 | 0.081x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 666.9 | 613.8 | 722.7 | 40.8 | 0.247x | 3.048x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 843.2 | 820.2 | 941.9 | 48.7 | 0.312x | 3.854x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,037.6 | 980.6 | 1,059.1 | 28.7 | 0.385x | 4.742x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,054.8 | 1,036.4 | 1,095.0 | 20.1 | 0.391x | 4.821x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,069.2 | 1,015.0 | 1,077.0 | 23.1 | 0.396x | 4.887x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,698.5 | 2,654.8 | 2,807.6 | 56.9 | 1.000x | 12.333x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-053` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 153.4 | 151.7 | 156.3 | 1.5 | 0.198x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 380.2 | 377.6 | 393.2 | 5.7 | 0.492x | 2.479x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 521.8 | 479.2 | 530.7 | 18.7 | 0.675x | 3.402x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 538.6 | 507.1 | 556.7 | 20.0 | 0.697x | 3.511x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 544.6 | 519.3 | 564.2 | 18.0 | 0.704x | 3.551x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 773.2 | 769.7 | 799.0 | 10.7 | 1.000x | 5.041x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 774.4 | 773.8 | 782.4 | 3.2 | 1.002x | 5.049x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-053` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 218.9 | 215.6 | 221.0 | 1.9 | 0.081x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 626.1 | 559.4 | 645.1 | 30.2 | 0.233x | 2.860x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 866.7 | 807.3 | 885.9 | 35.6 | 0.322x | 3.959x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 963.8 | 949.9 | 1,000.8 | 17.5 | 0.359x | 4.403x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 987.0 | 925.0 | 1,004.0 | 28.9 | 0.367x | 4.509x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,026.6 | 951.7 | 1,145.8 | 72.1 | 0.382x | 4.689x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,687.5 | 2,667.5 | 2,804.0 | 50.3 | 1.000x | 12.276x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-054` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 153.0 | 151.9 | 154.7 | 1.0 | 0.198x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 384.5 | 366.1 | 417.1 | 16.6 | 0.497x | 2.513x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 517.0 | 492.4 | 517.5 | 10.2 | 0.669x | 3.378x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 542.4 | 497.5 | 574.1 | 30.9 | 0.702x | 3.545x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 550.3 | 522.8 | 567.2 | 14.4 | 0.712x | 3.596x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 772.9 | 770.6 | 794.4 | 9.2 | 1.000x | 5.051x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 782.3 | 774.0 | 900.7 | 49.1 | 1.012x | 5.113x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-054` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 217.7 | 216.4 | 221.0 | 1.8 | 0.080x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 618.0 | 539.0 | 634.2 | 37.7 | 0.228x | 2.839x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 830.2 | 777.7 | 898.4 | 40.1 | 0.307x | 3.813x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 956.6 | 939.0 | 975.3 | 12.8 | 0.353x | 4.394x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 993.6 | 939.4 | 1,021.4 | 27.6 | 0.367x | 4.564x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 999.8 | 915.6 | 1,021.5 | 38.8 | 0.369x | 4.592x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,706.8 | 2,658.3 | 2,807.3 | 53.0 | 1.000x | 12.433x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-055` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 153.0 | 151.6 | 154.0 | 0.9 | 0.197x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 389.6 | 372.6 | 403.8 | 10.6 | 0.502x | 2.547x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 514.4 | 459.1 | 541.2 | 27.7 | 0.662x | 3.362x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 532.3 | 499.1 | 568.8 | 22.3 | 0.686x | 3.480x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 546.2 | 510.3 | 582.1 | 26.8 | 0.703x | 3.570x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 776.5 | 774.0 | 792.4 | 6.6 | 1.000x | 5.076x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 782.2 | 771.0 | 790.7 | 6.5 | 1.007x | 5.113x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-055` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 219.4 | 218.1 | 223.5 | 2.0 | 0.082x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 634.7 | 620.1 | 650.7 | 11.0 | 0.236x | 2.893x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 849.2 | 838.2 | 934.0 | 34.9 | 0.316x | 3.871x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 980.4 | 924.3 | 1,062.0 | 45.1 | 0.365x | 4.469x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 981.3 | 957.7 | 1,016.7 | 19.8 | 0.365x | 4.473x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 994.7 | 950.2 | 1,014.5 | 23.6 | 0.370x | 4.534x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,687.5 | 2,665.8 | 2,783.2 | 45.8 | 1.000x | 12.251x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-056` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 153.1 | 151.6 | 153.7 | 0.7 | 0.197x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 385.0 | 357.9 | 389.0 | 11.2 | 0.496x | 2.514x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 523.5 | 511.5 | 552.9 | 15.6 | 0.675x | 3.418x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 523.7 | 490.4 | 559.6 | 23.3 | 0.675x | 3.420x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 552.5 | 525.7 | 559.0 | 11.6 | 0.712x | 3.607x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 775.7 | 772.4 | 786.9 | 5.2 | 1.000x | 5.065x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 780.1 | 768.5 | 814.3 | 15.8 | 1.006x | 5.094x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-056` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 219.2 | 212.0 | 219.9 | 2.9 | 0.082x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 631.8 | 592.5 | 680.3 | 31.1 | 0.237x | 2.883x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 871.3 | 790.0 | 885.4 | 35.4 | 0.326x | 3.975x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 963.0 | 955.7 | 1,035.0 | 29.8 | 0.361x | 4.394x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 979.1 | 965.2 | 1,013.2 | 17.5 | 0.367x | 4.467x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 994.4 | 971.7 | 1,031.0 | 21.8 | 0.373x | 4.537x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,669.1 | 2,660.0 | 2,799.8 | 54.7 | 1.000x | 12.178x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-057` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 7,760.7 | 7,745.9 | 7,830.2 | 31.7 | 0.763x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7,956.4 | 7,935.7 | 8,054.4 | 43.8 | 0.782x | 1.025x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 8,184.1 | 8,180.3 | 8,248.8 | 28.3 | 0.805x | 1.055x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 8,202.1 | 8,134.9 | 8,275.5 | 44.9 | 0.806x | 1.057x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 8,249.6 | 8,134.0 | 8,379.3 | 89.4 | 0.811x | 1.063x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 10,171.8 | 10,133.1 | 10,563.1 | 161.2 | 1.000x | 1.311x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 10,267.2 | 10,140.6 | 10,337.4 | 77.2 | 1.009x | 1.323x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-058` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 29,394.6 | 29,113.7 | 29,479.6 | 143.2 | 0.161x | 1.000x | 5 | 100% |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 182,311.8 | 181,881.6 | 188,510.3 | 2,531.1 | 1.000x | 6.202x | 5 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 182,464.9 | 180,436.3 | 184,232.2 | 1,367.9 | 1.001x | 6.207x | 5 | 100% |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-059` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 72,651.8 | 71,878.3 | 73,309.0 | 508.4 | 0.249x | 1.000x | 5 | 100% |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 291,546.0 | 290,559.2 | 295,500.6 | 1,854.9 | 0.997x | 4.013x | 5 | 100% |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 292,306.7 | 291,197.0 | 294,026.7 | 1,097.3 | 1.000x | 4.023x | 5 | 100% |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-060` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 194,929.3 | 194,669.2 | 195,582.5 | 342.7 | 0.225x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 195,025.4 | 194,449.5 | 206,100.3 | 4,460.5 | 0.225x | 1.000x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 199,473.7 | 198,611.8 | 199,797.7 | 414.8 | 0.230x | 1.023x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 199,566.3 | 198,383.9 | 203,457.6 | 1,727.6 | 0.230x | 1.024x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 200,221.4 | 199,199.0 | 201,995.0 | 1,009.4 | 0.231x | 1.027x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 849,449.9 | 845,906.9 | 876,087.2 | 11,038.7 | 0.980x | 4.358x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 866,970.7 | 848,569.5 | 887,969.5 | 13,530.6 | 1.000x | 4.448x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-061` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 10,994.4 | 10,961.8 | 11,270.8 | 117.0 | 0.149x | 1.000x | 5 | 100% |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 72,983.8 | 72,564.0 | 74,111.1 | 563.9 | 0.990x | 6.638x | 5 | 100% |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 73,745.5 | 72,822.0 | 75,219.3 | 841.4 | 1.000x | 6.708x | 5 | 100% |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-062` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 315.4 | 298.4 | 324.5 | 10.6 | 0.346x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 482.2 | 471.4 | 518.2 | 16.4 | 0.528x | 1.529x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 510.9 | 497.2 | 544.4 | 16.3 | 0.560x | 1.620x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 516.0 | 495.3 | 549.3 | 17.3 | 0.565x | 1.636x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 525.2 | 492.2 | 559.7 | 28.9 | 0.575x | 1.665x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 874.6 | 872.7 | 889.5 | 6.3 | 0.958x | 2.773x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 912.8 | 869.8 | 917.0 | 17.3 | 1.000x | 2.894x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-063` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 101,057.8 | 99,678.4 | 101,371.7 | 596.2 | 0.474x | 1.000x | 5 | 100% |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 212,552.9 | 211,742.0 | 214,033.1 | 962.1 | 0.997x | 2.103x | 5 | 100% |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 213,286.2 | 211,072.4 | 215,032.2 | 1,389.9 | 1.000x | 2.111x | 5 | 100% |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-064` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 33,003.8 | 32,878.4 | 33,105.0 | 84.6 | 0.220x | 1.000x | 5 | 100% |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 150,177.3 | 148,436.4 | 150,779.1 | 796.2 | 0.999x | 4.550x | 5 | 100% |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 150,255.4 | 149,104.6 | 150,677.2 | 581.5 | 1.000x | 4.553x | 5 | 100% |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-065` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 55.1 | 54.9 | 55.3 | 0.1 | 0.327x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 165.7 | 159.4 | 170.9 | 4.1 | 0.983x | 3.005x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 168.5 | 162.7 | 172.5 | 3.2 | 1.000x | 3.055x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 245.8 | 222.1 | 275.8 | 17.3 | 1.458x | 4.456x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 353.9 | 264.6 | 395.1 | 43.8 | 2.100x | 6.417x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 365.8 | 316.0 | 395.3 | 29.1 | 2.171x | 6.633x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 391.5 | 302.8 | 447.7 | 47.2 | 2.324x | 7.100x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-065` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 141.6 | 140.5 | 142.3 | 0.7 | 0.086x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 1,148.4 | 1,084.9 | 1,216.1 | 48.8 | 0.701x | 8.111x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,396.9 | 1,372.0 | 1,473.7 | 34.5 | 0.853x | 9.866x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,406.4 | 1,316.2 | 1,441.6 | 44.1 | 0.859x | 9.933x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,437.8 | 1,395.7 | 1,498.3 | 33.2 | 0.878x | 10.155x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,438.1 | 1,373.1 | 1,475.3 | 37.9 | 0.878x | 10.157x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,637.1 | 1,632.4 | 1,683.4 | 19.6 | 1.000x | 11.563x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-066` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 203.5 | 203.1 | 205.1 | 0.8 | 0.190x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 399.4 | 370.0 | 429.1 | 23.1 | 0.373x | 1.962x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 540.4 | 533.0 | 593.1 | 22.4 | 0.505x | 2.655x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 552.5 | 541.8 | 651.9 | 41.2 | 0.516x | 2.714x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 586.4 | 543.1 | 617.0 | 24.6 | 0.548x | 2.881x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,070.9 | 1,059.7 | 1,091.1 | 10.5 | 1.000x | 5.261x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,073.1 | 1,060.9 | 1,079.6 | 6.8 | 1.002x | 5.272x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-066` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 173.4 | 172.8 | 176.2 | 1.2 | 0.161x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 208.7 | 208.1 | 209.5 | 0.5 | 0.194x | 1.204x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 424.2 | 409.7 | 431.0 | 7.4 | 0.394x | 2.447x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 618.3 | 596.3 | 639.4 | 14.4 | 0.574x | 3.566x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 623.1 | 593.0 | 634.7 | 14.6 | 0.579x | 3.594x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 638.0 | 592.8 | 658.0 | 27.1 | 0.593x | 3.680x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,076.5 | 1,057.3 | 1,083.2 | 9.7 | 1.000x | 6.209x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-067` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 165.7 | 165.4 | 169.7 | 1.6 | 0.164x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 361.7 | 333.8 | 385.0 | 16.7 | 0.357x | 2.182x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 540.3 | 509.9 | 592.2 | 28.1 | 0.534x | 3.261x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 545.8 | 511.7 | 562.7 | 16.9 | 0.539x | 3.294x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 551.9 | 528.7 | 627.2 | 33.5 | 0.545x | 3.330x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,010.0 | 996.8 | 1,219.4 | 86.2 | 0.998x | 6.095x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,012.5 | 1,004.3 | 1,023.5 | 6.1 | 1.000x | 6.110x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-067` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 160.4 | 159.5 | 161.3 | 0.6 | 0.158x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 176.3 | 175.7 | 178.5 | 1.0 | 0.174x | 1.099x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 392.3 | 378.6 | 425.9 | 15.9 | 0.387x | 2.446x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 542.0 | 539.2 | 549.2 | 3.7 | 0.535x | 3.379x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 542.0 | 519.4 | 559.0 | 12.7 | 0.535x | 3.379x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 579.4 | 542.7 | 595.0 | 18.3 | 0.572x | 3.612x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,012.8 | 1,001.9 | 1,047.7 | 15.7 | 1.000x | 6.314x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-068` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 84.7 | 84.0 | 85.9 | 0.7 | 0.122x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 278.1 | 243.7 | 293.8 | 20.7 | 0.401x | 3.282x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 401.1 | 377.4 | 435.4 | 19.6 | 0.578x | 4.733x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 423.2 | 415.2 | 507.5 | 37.9 | 0.610x | 4.995x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 449.3 | 366.1 | 472.1 | 41.8 | 0.647x | 5.303x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 687.2 | 685.7 | 691.6 | 2.1 | 0.990x | 8.110x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 694.1 | 688.6 | 707.8 | 6.5 | 1.000x | 8.192x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-068` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 84.5 | 84.3 | 84.7 | 0.1 | 0.122x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 104.9 | 103.9 | 105.2 | 0.5 | 0.151x | 1.241x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 289.1 | 282.1 | 302.3 | 7.2 | 0.417x | 3.422x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 419.2 | 375.9 | 580.3 | 71.5 | 0.605x | 4.963x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 425.0 | 329.7 | 460.3 | 51.4 | 0.613x | 5.031x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 450.7 | 434.1 | 477.5 | 14.2 | 0.650x | 5.337x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 693.1 | 681.8 | 720.6 | 14.6 | 1.000x | 8.206x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-069` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 152.6 | 152.2 | 155.0 | 1.1 | 0.234x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 361.3 | 328.0 | 369.1 | 16.1 | 0.553x | 2.367x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 504.4 | 491.5 | 518.9 | 10.0 | 0.772x | 3.305x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 511.4 | 429.4 | 534.4 | 39.5 | 0.783x | 3.351x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 533.2 | 493.2 | 540.6 | 18.8 | 0.816x | 3.494x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 640.4 | 632.7 | 655.4 | 7.6 | 0.981x | 4.196x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 653.1 | 631.6 | 660.0 | 9.9 | 1.000x | 4.279x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-069` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 203.3 | 202.4 | 203.5 | 0.4 | 0.090x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 1,460.0 | 1,348.8 | 1,512.5 | 66.8 | 0.645x | 7.183x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,626.2 | 1,589.7 | 1,695.0 | 34.6 | 0.719x | 8.001x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,817.7 | 1,757.4 | 1,839.1 | 27.5 | 0.803x | 8.943x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,819.6 | 1,773.2 | 1,847.9 | 24.2 | 0.804x | 8.952x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,820.6 | 1,804.2 | 1,848.9 | 16.4 | 0.805x | 8.957x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,262.7 | 2,236.7 | 2,316.2 | 31.6 | 1.000x | 11.132x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-070` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 144.2 | 143.8 | 148.9 | 1.9 | 0.166x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 372.9 | 323.4 | 384.1 | 21.7 | 0.429x | 2.587x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 525.4 | 516.7 | 544.9 | 11.9 | 0.604x | 3.645x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 565.7 | 497.5 | 598.6 | 38.4 | 0.650x | 3.924x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 568.6 | 514.9 | 679.0 | 53.7 | 0.654x | 3.944x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 856.2 | 848.0 | 869.0 | 7.2 | 0.984x | 5.939x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 869.9 | 857.4 | 922.0 | 23.1 | 1.000x | 6.034x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-070` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 148.4 | 148.1 | 149.6 | 0.7 | 0.170x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 149.5 | 149.1 | 149.7 | 0.2 | 0.172x | 1.008x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 355.8 | 350.6 | 372.7 | 8.1 | 0.409x | 2.398x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 506.7 | 432.6 | 563.6 | 42.9 | 0.582x | 3.416x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 512.7 | 478.9 | 567.1 | 29.8 | 0.589x | 3.456x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 514.3 | 470.9 | 527.5 | 23.7 | 0.591x | 3.467x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 870.6 | 849.8 | 886.1 | 12.4 | 1.000x | 5.868x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-071` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 159.8 | 159.3 | 160.1 | 0.3 | 0.180x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 379.2 | 344.5 | 404.5 | 19.1 | 0.427x | 2.374x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 552.9 | 481.5 | 567.5 | 31.3 | 0.623x | 3.461x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 588.7 | 496.5 | 621.3 | 46.4 | 0.663x | 3.685x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 611.8 | 552.8 | 650.3 | 32.0 | 0.689x | 3.829x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 886.1 | 865.4 | 888.0 | 8.4 | 0.998x | 5.546x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 888.2 | 865.0 | 900.3 | 12.0 | 1.000x | 5.559x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-071` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 164.3 | 163.9 | 164.6 | 0.2 | 0.187x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 164.6 | 164.1 | 175.3 | 4.3 | 0.187x | 1.002x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 379.6 | 370.2 | 392.5 | 8.8 | 0.431x | 2.311x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 488.5 | 462.7 | 514.9 | 16.6 | 0.555x | 2.973x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 525.8 | 460.2 | 544.4 | 31.0 | 0.597x | 3.200x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 526.6 | 473.0 | 570.9 | 37.7 | 0.598x | 3.206x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 880.1 | 868.9 | 900.2 | 10.9 | 1.000x | 5.357x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-072` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 739.7 | 729.6 | 744.7 | 5.2 | 0.326x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 949.5 | 933.9 | 958.6 | 8.9 | 0.419x | 1.284x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 962.9 | 934.7 | 987.9 | 22.4 | 0.425x | 1.302x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 974.6 | 926.1 | 1,119.7 | 67.3 | 0.430x | 1.318x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 987.3 | 944.4 | 1,014.1 | 23.3 | 0.436x | 1.335x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,245.8 | 2,228.1 | 2,270.6 | 16.1 | 0.991x | 3.036x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,265.7 | 2,231.0 | 2,300.4 | 24.4 | 1.000x | 3.063x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-072` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 407.6 | 406.2 | 409.9 | 1.2 | 0.130x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 912.1 | 862.8 | 919.3 | 20.6 | 0.291x | 2.238x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,123.3 | 1,103.8 | 1,135.1 | 10.7 | 0.358x | 2.756x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,176.2 | 1,140.1 | 1,215.7 | 24.1 | 0.375x | 2.885x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,201.6 | 1,178.0 | 1,249.2 | 23.2 | 0.383x | 2.948x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,205.6 | 1,185.0 | 1,263.4 | 27.0 | 0.385x | 2.958x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,133.7 | 3,110.0 | 3,181.5 | 24.8 | 1.000x | 7.688x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-073` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 153.2 | 150.3 | 155.1 | 1.9 | 0.191x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 382.0 | 373.1 | 393.2 | 7.9 | 0.475x | 2.494x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 499.6 | 456.5 | 538.5 | 30.1 | 0.622x | 3.262x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 514.7 | 465.9 | 565.8 | 33.4 | 0.640x | 3.360x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 543.9 | 497.0 | 576.1 | 25.7 | 0.677x | 3.551x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 795.6 | 769.1 | 983.4 | 79.5 | 0.990x | 5.194x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 803.6 | 770.5 | 825.5 | 17.9 | 1.000x | 5.247x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-073` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 218.2 | 215.9 | 222.6 | 2.3 | 0.080x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 914.3 | 802.0 | 948.9 | 54.9 | 0.337x | 4.189x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,069.3 | 941.4 | 1,127.9 | 77.4 | 0.394x | 4.899x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,396.4 | 1,376.5 | 1,415.7 | 12.6 | 0.515x | 6.398x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,418.5 | 1,384.2 | 1,434.9 | 17.7 | 0.523x | 6.500x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,423.8 | 1,407.5 | 1,448.9 | 14.3 | 0.525x | 6.524x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,711.3 | 2,673.2 | 3,291.5 | 233.1 | 1.000x | 12.423x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-074` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 199.9 | 184.6 | 205.6 | 7.1 | 0.248x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 425.8 | 410.0 | 443.4 | 11.7 | 0.528x | 2.130x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 526.9 | 505.2 | 569.0 | 20.9 | 0.654x | 2.636x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 551.7 | 490.5 | 582.4 | 32.2 | 0.684x | 2.760x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 558.8 | 539.2 | 601.2 | 24.0 | 0.693x | 2.795x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 782.3 | 767.8 | 801.2 | 14.2 | 0.970x | 3.913x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 806.1 | 768.6 | 807.5 | 14.9 | 1.000x | 4.032x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-074` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 230.1 | 228.8 | 238.6 | 3.6 | 0.086x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 1,185.1 | 1,108.3 | 1,267.1 | 52.0 | 0.441x | 5.151x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,299.3 | 1,270.4 | 1,381.2 | 43.7 | 0.483x | 5.647x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,781.8 | 1,732.5 | 1,794.4 | 23.3 | 0.663x | 7.744x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,782.2 | 1,685.6 | 1,823.5 | 48.2 | 0.663x | 7.746x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,790.7 | 1,739.1 | 1,812.7 | 26.5 | 0.666x | 7.783x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,688.9 | 2,675.5 | 2,804.9 | 51.4 | 1.000x | 11.687x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-075` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 176.0 | 175.9 | 180.0 | 1.7 | 0.170x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 381.1 | 360.8 | 413.1 | 20.6 | 0.369x | 2.165x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 509.1 | 491.3 | 519.3 | 11.1 | 0.493x | 2.892x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 521.6 | 509.9 | 561.4 | 17.6 | 0.505x | 2.964x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 607.9 | 563.0 | 617.8 | 19.9 | 0.588x | 3.453x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,033.7 | 1,028.0 | 1,067.8 | 16.5 | 1.000x | 5.872x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,034.4 | 1,026.1 | 1,045.5 | 6.2 | 1.001x | 5.877x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-075` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 108.0 | 106.6 | 111.1 | 1.7 | 0.103x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 177.2 | 177.0 | 179.8 | 1.1 | 0.170x | 1.640x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 385.3 | 362.7 | 394.7 | 10.7 | 0.369x | 3.566x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 553.5 | 466.5 | 619.4 | 49.2 | 0.530x | 5.123x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 579.0 | 545.5 | 701.5 | 54.8 | 0.554x | 5.359x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 619.7 | 601.6 | 626.1 | 9.8 | 0.593x | 5.735x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,044.4 | 1,024.2 | 1,084.3 | 23.0 | 1.000x | 9.666x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-076` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 176.2 | 176.0 | 187.5 | 4.5 | 0.169x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 391.7 | 357.6 | 425.2 | 26.9 | 0.376x | 2.222x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 510.7 | 491.5 | 519.1 | 11.5 | 0.490x | 2.897x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 516.7 | 502.2 | 561.6 | 21.0 | 0.496x | 2.932x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 607.5 | 559.6 | 629.2 | 24.4 | 0.583x | 3.447x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,031.3 | 1,027.6 | 1,050.5 | 9.5 | 0.990x | 5.851x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,041.3 | 1,024.5 | 1,078.0 | 18.5 | 1.000x | 5.908x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-076` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 106.7 | 106.6 | 110.2 | 1.4 | 0.103x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 177.4 | 177.1 | 179.5 | 0.9 | 0.172x | 1.662x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 386.3 | 374.9 | 400.5 | 9.8 | 0.374x | 3.619x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 535.0 | 522.5 | 634.4 | 40.9 | 0.518x | 5.012x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 598.3 | 542.1 | 627.2 | 35.0 | 0.579x | 5.605x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 601.4 | 569.4 | 643.6 | 24.6 | 0.583x | 5.634x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,032.4 | 1,021.1 | 1,068.6 | 16.6 | 1.000x | 9.672x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-077` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 170.2 | 169.5 | 174.6 | 1.9 | 0.147x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 380.8 | 364.9 | 418.5 | 18.9 | 0.329x | 2.237x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 501.3 | 460.0 | 513.3 | 19.5 | 0.433x | 2.945x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 513.0 | 489.1 | 536.4 | 16.6 | 0.443x | 3.013x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 565.6 | 534.6 | 592.0 | 19.9 | 0.488x | 3.322x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,136.9 | 1,133.8 | 1,162.6 | 10.6 | 0.981x | 6.679x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,158.8 | 1,127.8 | 1,165.4 | 14.7 | 1.000x | 6.807x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-077` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 108.1 | 107.5 | 109.3 | 0.6 | 0.096x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 172.5 | 172.4 | 172.7 | 0.1 | 0.153x | 1.596x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 374.6 | 350.8 | 412.7 | 24.3 | 0.332x | 3.466x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 576.2 | 535.9 | 597.6 | 23.6 | 0.510x | 5.331x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 593.0 | 514.6 | 686.8 | 58.2 | 0.525x | 5.487x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 605.3 | 548.6 | 611.3 | 23.5 | 0.536x | 5.600x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,129.4 | 1,123.6 | 1,160.7 | 15.2 | 1.000x | 10.449x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-078` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 160.1 | 159.9 | 165.0 | 2.0 | 0.147x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 374.9 | 334.9 | 420.4 | 31.9 | 0.345x | 2.342x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 543.2 | 511.1 | 572.1 | 22.5 | 0.500x | 3.392x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 558.2 | 528.3 | 563.0 | 13.4 | 0.514x | 3.486x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 579.3 | 550.0 | 601.1 | 17.8 | 0.534x | 3.618x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,081.6 | 1,070.9 | 1,098.0 | 9.6 | 0.996x | 6.755x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,085.5 | 1,073.4 | 1,102.7 | 10.5 | 1.000x | 6.780x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-078` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 107.4 | 107.3 | 109.8 | 1.0 | 0.100x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 163.1 | 162.8 | 164.4 | 0.6 | 0.152x | 1.519x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 365.5 | 346.9 | 432.1 | 31.1 | 0.340x | 3.404x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 563.9 | 500.6 | 661.2 | 57.8 | 0.525x | 5.251x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 572.8 | 545.5 | 594.7 | 16.0 | 0.533x | 5.334x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 589.9 | 562.7 | 598.4 | 15.5 | 0.549x | 5.494x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,074.9 | 1,069.4 | 1,100.7 | 12.8 | 1.000x | 10.011x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-079` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 160.5 | 160.0 | 169.2 | 3.6 | 0.148x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 380.2 | 329.8 | 401.0 | 25.2 | 0.351x | 2.369x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 528.9 | 504.6 | 569.7 | 22.2 | 0.488x | 3.296x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 557.9 | 549.7 | 578.3 | 10.9 | 0.515x | 3.476x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 584.7 | 564.4 | 589.4 | 9.8 | 0.540x | 3.643x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,075.1 | 1,070.8 | 1,101.9 | 11.4 | 0.993x | 6.699x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,083.2 | 1,074.7 | 1,099.1 | 9.9 | 1.000x | 6.750x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-079` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 107.4 | 107.1 | 108.9 | 0.7 | 0.100x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 163.5 | 162.9 | 163.8 | 0.4 | 0.151x | 1.522x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 370.1 | 341.4 | 436.2 | 33.3 | 0.343x | 3.445x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 564.4 | 492.7 | 650.0 | 52.6 | 0.523x | 5.254x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 582.8 | 536.7 | 619.4 | 29.0 | 0.540x | 5.425x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 593.3 | 570.9 | 612.5 | 14.1 | 0.550x | 5.523x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,079.5 | 1,074.6 | 1,098.1 | 10.5 | 1.000x | 10.049x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-080` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 279.1 | 261.0 | 306.7 | 16.4 | 0.300x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 534.0 | 520.3 | 552.8 | 12.5 | 0.574x | 1.913x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 581.7 | 569.8 | 628.6 | 20.8 | 0.626x | 2.084x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 604.8 | 559.0 | 622.7 | 21.4 | 0.651x | 2.167x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 626.0 | 574.3 | 663.2 | 33.9 | 0.673x | 2.243x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 925.4 | 902.3 | 947.6 | 17.0 | 0.995x | 3.316x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 929.6 | 905.9 | 942.7 | 12.5 | 1.000x | 3.331x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-080` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 321.0 | 307.5 | 325.1 | 6.2 | 0.100x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 1,745.3 | 1,732.9 | 1,788.3 | 19.6 | 0.544x | 5.437x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,756.0 | 1,728.4 | 1,842.0 | 39.1 | 0.547x | 5.470x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,771.1 | 1,713.9 | 2,167.9 | 165.0 | 0.552x | 5.517x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,782.9 | 1,726.8 | 1,866.7 | 44.9 | 0.556x | 5.554x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 1,939.2 | 1,936.5 | 1,958.0 | 9.3 | 0.605x | 6.041x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,207.5 | 3,173.2 | 3,564.8 | 147.0 | 1.000x | 9.992x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-081` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 30.8 | 30.3 | 33.6 | 1.2 | 0.960x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 32.1 | 30.3 | 32.5 | 0.8 | 1.000x | 1.042x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 51.4 | 51.1 | 52.4 | 0.5 | 1.605x | 1.672x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 290.7 | 258.9 | 292.4 | 13.1 | 9.068x | 9.446x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 387.3 | 365.4 | 417.4 | 20.1 | 12.082x | 12.585x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 432.8 | 415.7 | 454.5 | 13.4 | 13.500x | 14.063x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 436.3 | 390.0 | 482.8 | 30.0 | 13.610x | 14.177x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-081` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 31.0 | 30.4 | 33.9 | 1.3 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 40.9 | 40.1 | 44.0 | 1.4 | 1.320x | 1.320x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 50.2 | 49.9 | 50.5 | 0.2 | 1.621x | 1.621x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 270.0 | 263.9 | 291.2 | 9.7 | 8.711x | 8.711x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 434.6 | 410.8 | 467.6 | 22.7 | 14.022x | 14.022x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 440.4 | 417.8 | 471.3 | 18.6 | 14.210x | 14.210x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 445.0 | 392.8 | 491.2 | 36.1 | 14.358x | 14.358x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-082` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 30.7 | 30.3 | 32.3 | 0.8 | 0.985x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 31.1 | 30.3 | 31.4 | 0.4 | 1.000x | 1.015x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 51.3 | 51.2 | 52.8 | 0.6 | 1.647x | 1.672x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 284.2 | 266.3 | 306.3 | 13.1 | 9.132x | 9.269x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 412.8 | 306.7 | 437.7 | 45.9 | 13.265x | 13.463x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 438.8 | 405.0 | 455.1 | 16.7 | 14.100x | 14.311x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 449.1 | 415.6 | 459.2 | 15.0 | 14.429x | 14.645x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-082` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.7 | 30.4 | 34.3 | 1.5 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 40.4 | 40.2 | 43.9 | 1.4 | 1.315x | 1.315x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 67.8 | 67.5 | 69.3 | 0.8 | 2.206x | 2.206x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 286.9 | 278.9 | 305.7 | 9.6 | 9.329x | 9.329x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 454.5 | 450.9 | 473.3 | 8.1 | 14.780x | 14.780x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 456.9 | 412.6 | 512.6 | 32.1 | 14.860x | 14.860x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 468.2 | 430.4 | 496.4 | 27.4 | 15.227x | 15.227x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-083` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 34.4 | 33.5 | 35.4 | 0.8 | 0.990x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 34.7 | 33.8 | 35.8 | 0.7 | 1.000x | 1.010x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 115.4 | 113.3 | 116.1 | 0.9 | 3.326x | 3.359x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 340.2 | 334.1 | 350.5 | 5.7 | 9.806x | 9.903x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 476.3 | 445.6 | 616.2 | 59.8 | 13.730x | 13.866x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 495.6 | 451.7 | 523.8 | 24.0 | 14.286x | 14.428x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 530.0 | 459.6 | 571.3 | 37.8 | 15.278x | 15.430x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-083` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 35.2 | 34.9 | 39.9 | 1.9 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 46.4 | 46.2 | 46.6 | 0.2 | 1.319x | 1.319x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 2,889.6 | 2,868.4 | 3,035.0 | 62.0 | 82.170x | 82.170x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 3,129.7 | 3,018.7 | 3,181.6 | 57.1 | 88.997x | 88.997x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 3,395.1 | 3,371.3 | 3,485.3 | 41.6 | 96.544x | 96.544x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 3,402.5 | 3,328.7 | 3,482.9 | 48.9 | 96.756x | 96.756x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 3,437.5 | 3,405.4 | 3,452.8 | 19.5 | 97.751x | 97.751x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-084` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 33.6 | 33.1 | 34.6 | 0.5 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 34.7 | 34.3 | 35.5 | 0.4 | 1.034x | 1.034x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 169.6 | 164.6 | 175.9 | 3.8 | 5.055x | 5.055x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 392.6 | 389.3 | 402.1 | 5.0 | 11.701x | 11.701x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 596.3 | 570.5 | 655.3 | 31.9 | 17.772x | 17.772x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 622.9 | 611.6 | 646.8 | 12.4 | 18.564x | 18.564x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 636.2 | 568.5 | 662.4 | 33.0 | 18.961x | 18.961x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `s-084` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 34.3 | 33.9 | 39.5 | 2.1 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44.4 | 44.3 | 45.4 | 0.4 | 1.297x | 1.297x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 811.1 | 763.1 | 839.1 | 25.9 | 23.670x | 23.670x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 998.5 | 971.7 | 1,048.5 | 25.3 | 29.140x | 29.140x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 1,581.2 | 1,541.0 | 1,659.0 | 42.0 | 46.147x | 46.147x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 1,632.7 | 1,596.8 | 1,697.4 | 35.4 | 47.647x | 47.647x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 1,636.8 | 1,579.9 | 1,672.1 | 32.8 | 47.768x | 47.768x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 7,045,186.7 | 6,964,179.7 | 7,172,586.3 | 77,777.1 | 0.136x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 10,975,556.0 | 10,898,005.0 | 11,025,015.0 | 46,442.2 | 0.212x | 1.558x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 18,612,288.0 | 17,644,272.0 | 19,618,594.0 | 627,811.6 | 0.359x | 2.642x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 23,646,430.0 | 22,861,735.0 | 26,823,629.0 | 1,442,212.7 | 0.456x | 3.356x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 24,010,552.0 | 22,722,773.0 | 25,261,380.0 | 825,072.6 | 0.463x | 3.408x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 24,014,597.0 | 22,956,700.0 | 26,418,041.0 | 1,195,438.1 | 0.463x | 3.409x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 51,851,980.0 | 51,679,913.4 | 52,364,619.8 | 237,723.3 | 1.000x | 7.360x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,812.2 | 17,783.3 | 17,813.6 | 12.0 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 17,718,011.3 | 17,676,191.0 | 17,781,863.7 | 38,931.5 | 994.712x | 994.712x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 84,138,418.0 | 83,753,954.0 | 84,516,340.0 | 281,935.0 | 4723.637x | 4723.637x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 87,151,691.0 | 87,056,790.0 | 87,870,905.0 | 296,577.9 | 4892.806x | 4892.806x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 88,138,127.0 | 87,017,010.0 | 91,290,196.0 | 1,439,973.1 | 4948.186x | 4948.186x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 88,760,543.0 | 87,217,943.0 | 92,820,847.0 | 1,915,173.9 | 4983.129x | 4983.129x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 89,148,076.0 | 82,492,434.0 | 90,456,955.0 | 3,365,895.9 | 5004.886x | 5004.886x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,809.6 | 17,772.3 | 17,906.4 | 50.3 | 1.000x | 1.000x | 5 | 100% |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-000` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 47.2 | 46.6 | 48.7 | 0.8 | 0.085x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 111.2 | 110.8 | 112.9 | 0.7 | 0.201x | 2.356x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 111.7 | 110.8 | 120.8 | 3.7 | 0.202x | 2.368x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 236.1 | 223.8 | 252.6 | 10.6 | 0.427x | 5.005x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 244.1 | 220.6 | 275.8 | 17.7 | 0.441x | 5.174x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 552.3 | 541.5 | 588.1 | 17.0 | 0.998x | 11.705x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 553.6 | 544.8 | 556.9 | 4.4 | 1.000x | 11.733x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-000` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 54.4 | 54.1 | 55.2 | 0.4 | 0.098x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 77.4 | 76.8 | 78.4 | 0.7 | 0.140x | 1.424x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 103.1 | 102.7 | 103.7 | 0.4 | 0.187x | 1.897x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 103.5 | 103.3 | 110.1 | 2.7 | 0.187x | 1.903x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 230.2 | 223.7 | 244.6 | 7.4 | 0.417x | 4.235x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 254.2 | 250.8 | 258.6 | 2.6 | 0.460x | 4.675x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 552.3 | 547.1 | 595.4 | 17.8 | 1.000x | 10.158x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-001` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 97.3 | 97.2 | 105.6 | 3.3 | 0.126x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 143.8 | 143.5 | 153.3 | 3.8 | 0.187x | 1.478x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 143.9 | 143.8 | 144.8 | 0.4 | 0.187x | 1.479x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 271.7 | 251.3 | 306.7 | 19.4 | 0.353x | 2.791x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 281.3 | 260.5 | 307.1 | 15.4 | 0.365x | 2.890x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 770.4 | 753.8 | 779.7 | 9.8 | 1.000x | 7.915x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 772.7 | 759.0 | 810.7 | 18.0 | 1.003x | 7.939x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-001` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 92.4 | 92.3 | 92.5 | 0.1 | 0.120x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 92.9 | 92.2 | 93.4 | 0.5 | 0.120x | 1.005x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 135.9 | 135.4 | 136.3 | 0.3 | 0.176x | 1.470x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 136.0 | 135.7 | 138.5 | 1.1 | 0.176x | 1.471x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 243.6 | 217.8 | 284.7 | 24.0 | 0.316x | 2.636x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 265.5 | 237.4 | 280.0 | 14.8 | 0.344x | 2.872x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 771.9 | 764.9 | 825.0 | 22.5 | 1.000x | 8.353x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-002` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 33.4 | 33.1 | 35.0 | 0.7 | 0.070x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 46.2 | 46.0 | 55.8 | 3.8 | 0.097x | 1.384x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 46.2 | 46.2 | 46.7 | 0.2 | 0.097x | 1.384x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 235.6 | 220.9 | 251.2 | 11.4 | 0.493x | 7.056x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 241.2 | 221.1 | 266.4 | 16.5 | 0.505x | 7.222x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 477.6 | 474.7 | 487.4 | 4.5 | 1.000x | 14.299x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 482.1 | 475.8 | 503.8 | 10.2 | 1.010x | 14.437x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-002` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 38.5 | 38.4 | 39.0 | 0.2 | 0.078x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 38.5 | 38.4 | 38.8 | 0.2 | 0.078x | 1.002x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 38.6 | 38.4 | 38.6 | 0.1 | 0.078x | 1.003x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 63.9 | 61.4 | 64.7 | 1.2 | 0.130x | 1.662x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 228.4 | 206.3 | 259.3 | 16.9 | 0.464x | 5.939x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 246.9 | 238.6 | 297.3 | 21.9 | 0.502x | 6.418x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 492.1 | 473.0 | 502.2 | 11.8 | 1.000x | 12.793x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-003` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 60.9 | 60.1 | 76.4 | 6.2 | 0.080x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 157.5 | 157.1 | 170.6 | 5.2 | 0.206x | 2.584x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 157.5 | 156.6 | 166.9 | 3.9 | 0.206x | 2.585x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 247.4 | 244.9 | 301.2 | 22.1 | 0.323x | 4.059x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 258.5 | 251.3 | 276.4 | 10.0 | 0.337x | 4.242x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 766.3 | 762.8 | 835.3 | 27.9 | 1.000x | 12.575x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 768.2 | 761.8 | 796.8 | 12.6 | 1.002x | 12.605x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-003` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 67.9 | 67.1 | 68.5 | 0.5 | 0.089x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 92.4 | 90.6 | 97.6 | 2.5 | 0.120x | 1.360x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 147.6 | 146.9 | 147.7 | 0.3 | 0.192x | 2.172x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 147.8 | 147.6 | 150.9 | 1.2 | 0.193x | 2.176x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 255.5 | 236.4 | 295.6 | 21.3 | 0.333x | 3.761x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 277.2 | 254.3 | 337.0 | 27.6 | 0.361x | 4.080x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 767.6 | 760.5 | 806.2 | 19.2 | 1.000x | 11.299x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-004` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 61.8 | 60.7 | 76.6 | 6.1 | 0.109x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 222.3 | 221.8 | 224.5 | 1.0 | 0.393x | 3.597x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 222.4 | 221.6 | 231.5 | 3.7 | 0.393x | 3.598x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 256.1 | 228.2 | 280.4 | 17.0 | 0.452x | 4.144x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 261.4 | 252.2 | 274.1 | 8.8 | 0.462x | 4.230x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 560.9 | 557.0 | 585.3 | 10.1 | 0.991x | 9.075x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 566.2 | 561.4 | 882.0 | 125.3 | 1.000x | 9.162x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-004` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 68.1 | 67.2 | 69.1 | 0.6 | 0.121x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 92.8 | 91.4 | 96.3 | 1.6 | 0.165x | 1.362x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 213.5 | 213.0 | 214.2 | 0.4 | 0.380x | 3.133x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 213.7 | 213.3 | 217.8 | 1.7 | 0.381x | 3.137x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 272.8 | 245.9 | 318.3 | 24.1 | 0.486x | 4.004x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 276.1 | 232.0 | 295.0 | 22.4 | 0.492x | 4.053x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 561.6 | 559.6 | 567.7 | 3.2 | 1.000x | 8.243x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-005` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 33.5 | 33.3 | 33.9 | 0.2 | 0.070x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 46.1 | 45.8 | 46.6 | 0.3 | 0.097x | 1.378x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 46.2 | 46.1 | 55.6 | 3.8 | 0.097x | 1.379x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 242.7 | 232.2 | 250.0 | 6.5 | 0.509x | 7.250x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 253.0 | 221.8 | 279.5 | 23.4 | 0.530x | 7.558x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 477.1 | 476.2 | 540.5 | 25.2 | 1.000x | 14.252x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 479.1 | 474.5 | 503.3 | 10.4 | 1.004x | 14.314x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-005` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 38.3 | 38.2 | 38.5 | 0.1 | 0.081x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 38.6 | 38.3 | 49.8 | 4.4 | 0.082x | 1.006x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 38.7 | 38.5 | 38.8 | 0.1 | 0.082x | 1.009x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 64.2 | 63.0 | 64.8 | 0.6 | 0.136x | 1.675x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 263.8 | 211.1 | 282.8 | 27.5 | 0.557x | 6.879x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 275.7 | 250.2 | 289.2 | 15.2 | 0.582x | 7.189x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 473.3 | 469.4 | 487.1 | 7.1 | 1.000x | 12.343x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-006` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 104.0 | 104.0 | 115.5 | 4.5 | 0.133x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 104.3 | 104.1 | 104.5 | 0.1 | 0.134x | 1.002x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 121.5 | 121.1 | 122.5 | 0.4 | 0.156x | 1.168x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 303.6 | 282.5 | 315.6 | 10.9 | 0.389x | 2.919x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 314.0 | 300.3 | 316.2 | 5.7 | 0.402x | 3.018x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 781.0 | 770.2 | 788.2 | 7.1 | 1.000x | 7.507x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 781.2 | 776.3 | 829.0 | 20.0 | 1.000x | 7.509x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-006` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 84.2 | 83.7 | 85.2 | 0.6 | 0.108x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 96.4 | 96.4 | 98.4 | 0.8 | 0.123x | 1.145x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 96.9 | 96.4 | 98.8 | 0.9 | 0.124x | 1.151x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 133.1 | 131.7 | 133.2 | 0.6 | 0.170x | 1.581x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 335.9 | 296.4 | 364.4 | 23.7 | 0.429x | 3.989x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 352.6 | 293.4 | 396.7 | 33.3 | 0.450x | 4.188x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 783.2 | 777.1 | 793.4 | 5.3 | 1.000x | 9.302x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-007` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 55.6 | 55.4 | 59.7 | 1.6 | 0.090x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 169.9 | 169.2 | 179.1 | 3.7 | 0.274x | 3.056x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 169.9 | 169.5 | 174.0 | 1.7 | 0.275x | 3.057x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 261.1 | 258.3 | 270.6 | 4.6 | 0.422x | 4.698x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 283.1 | 242.7 | 288.7 | 18.4 | 0.457x | 5.093x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 618.6 | 613.0 | 641.3 | 9.9 | 1.000x | 11.129x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 618.9 | 617.2 | 643.8 | 10.1 | 1.000x | 11.134x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-007` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 65.0 | 63.7 | 65.8 | 0.7 | 0.105x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 91.2 | 89.7 | 95.0 | 1.9 | 0.147x | 1.402x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 162.0 | 161.7 | 164.0 | 0.8 | 0.261x | 2.492x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 162.1 | 161.2 | 162.8 | 0.5 | 0.261x | 2.493x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 279.9 | 234.4 | 291.7 | 19.8 | 0.451x | 4.304x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 302.5 | 275.2 | 323.3 | 16.4 | 0.488x | 4.653x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 620.0 | 610.3 | 622.0 | 4.9 | 1.000x | 9.535x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-008` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 49.5 | 48.9 | 53.7 | 1.8 | 0.090x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 130.0 | 129.8 | 143.8 | 5.5 | 0.236x | 2.629x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 130.2 | 129.6 | 130.6 | 0.4 | 0.236x | 2.633x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 262.0 | 260.4 | 268.0 | 2.8 | 0.476x | 5.297x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 293.5 | 267.5 | 298.2 | 12.4 | 0.533x | 5.935x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 538.0 | 534.1 | 566.6 | 11.7 | 0.977x | 10.879x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 550.8 | 541.5 | 595.0 | 19.7 | 1.000x | 11.137x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-008` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 56.4 | 56.1 | 57.2 | 0.4 | 0.105x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 79.6 | 78.7 | 80.6 | 0.6 | 0.148x | 1.411x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 122.4 | 122.0 | 122.7 | 0.3 | 0.227x | 2.168x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 123.2 | 122.0 | 131.8 | 3.6 | 0.229x | 2.183x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 282.0 | 230.1 | 290.5 | 21.6 | 0.523x | 4.997x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 285.1 | 261.1 | 313.0 | 18.8 | 0.529x | 5.051x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 539.2 | 538.5 | 547.2 | 3.7 | 1.000x | 9.554x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-009` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 45.5 | 45.2 | 61.0 | 6.1 | 0.085x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 97.0 | 96.7 | 111.8 | 6.0 | 0.181x | 2.135x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 97.5 | 97.3 | 98.0 | 0.3 | 0.182x | 2.145x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 258.5 | 255.3 | 259.8 | 1.6 | 0.481x | 5.686x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 288.4 | 262.1 | 296.1 | 12.4 | 0.537x | 6.346x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 537.0 | 531.7 | 541.7 | 3.3 | 1.000x | 11.813x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 543.5 | 533.2 | 567.6 | 14.4 | 1.012x | 11.957x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-009` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 52.6 | 51.8 | 52.9 | 0.4 | 0.098x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 75.0 | 72.4 | 79.1 | 2.2 | 0.140x | 1.426x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 89.8 | 89.5 | 90.2 | 0.3 | 0.168x | 1.708x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 90.2 | 89.8 | 90.8 | 0.3 | 0.169x | 1.715x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 277.0 | 228.1 | 282.1 | 20.2 | 0.518x | 5.269x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 284.9 | 255.7 | 308.0 | 16.7 | 0.532x | 5.418x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 535.2 | 531.6 | 584.2 | 19.9 | 1.000x | 10.180x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-010` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 32.9 | 32.4 | 34.3 | 0.7 | 0.075x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 97.3 | 96.9 | 107.5 | 4.2 | 0.221x | 2.955x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 97.7 | 97.2 | 102.7 | 2.5 | 0.222x | 2.969x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 247.6 | 240.4 | 252.1 | 4.3 | 0.562x | 7.523x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 264.9 | 258.3 | 270.5 | 4.0 | 0.601x | 8.050x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 439.5 | 433.5 | 454.6 | 7.0 | 0.998x | 13.354x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 440.5 | 436.4 | 441.5 | 2.3 | 1.000x | 13.386x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-010` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 37.7 | 37.2 | 38.0 | 0.3 | 0.086x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 69.2 | 68.2 | 71.5 | 1.1 | 0.158x | 1.833x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 89.6 | 89.5 | 90.0 | 0.2 | 0.205x | 2.372x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 90.8 | 89.3 | 91.6 | 0.8 | 0.208x | 2.404x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 244.4 | 232.4 | 253.7 | 9.1 | 0.560x | 6.476x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 254.4 | 213.4 | 266.8 | 18.7 | 0.582x | 6.739x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 436.9 | 430.2 | 451.0 | 6.9 | 1.000x | 11.573x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-011` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 33.8 | 33.6 | 35.6 | 0.7 | 0.097x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 69.5 | 69.4 | 70.1 | 0.3 | 0.200x | 2.057x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 69.6 | 69.3 | 81.9 | 4.9 | 0.200x | 2.059x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 255.3 | 254.0 | 262.3 | 3.0 | 0.735x | 7.556x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 308.4 | 273.8 | 328.8 | 18.1 | 0.888x | 9.128x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 340.5 | 338.4 | 358.9 | 7.4 | 0.980x | 10.080x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 347.3 | 342.6 | 351.3 | 2.8 | 1.000x | 10.281x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-011` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 63.6 | 63.4 | 64.9 | 0.6 | 0.036x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 63.7 | 63.4 | 64.7 | 0.5 | 0.036x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 140.2 | 138.7 | 150.5 | 4.3 | 0.080x | 2.203x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 317.0 | 315.4 | 320.7 | 2.2 | 0.180x | 4.981x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 536.4 | 493.8 | 547.9 | 19.2 | 0.304x | 8.429x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 583.5 | 550.3 | 590.8 | 14.8 | 0.331x | 9.168x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,762.3 | 1,752.3 | 1,794.8 | 15.3 | 1.000x | 27.691x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-012` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 80.3 | 80.1 | 81.0 | 0.3 | 0.117x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 123.6 | 123.4 | 126.9 | 1.3 | 0.180x | 1.539x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 123.8 | 123.3 | 134.5 | 5.0 | 0.181x | 1.541x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 279.3 | 274.8 | 283.3 | 3.1 | 0.407x | 3.477x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 306.5 | 274.5 | 356.2 | 27.4 | 0.447x | 3.815x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 676.7 | 671.9 | 697.8 | 9.3 | 0.987x | 8.425x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 685.5 | 679.9 | 697.5 | 6.2 | 1.000x | 8.534x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-012` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 82.2 | 81.1 | 84.0 | 1.0 | 0.121x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 82.6 | 82.1 | 85.1 | 1.1 | 0.122x | 1.005x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 115.1 | 114.9 | 120.2 | 2.0 | 0.169x | 1.401x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 115.3 | 115.2 | 115.9 | 0.3 | 0.170x | 1.403x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 296.0 | 270.1 | 333.2 | 20.4 | 0.436x | 3.603x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 307.5 | 286.1 | 329.4 | 14.5 | 0.452x | 3.742x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 679.6 | 675.5 | 689.6 | 4.9 | 1.000x | 8.272x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-013` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 80.5 | 80.4 | 80.7 | 0.1 | 0.118x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 123.5 | 123.4 | 134.2 | 4.3 | 0.181x | 1.534x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 123.6 | 123.5 | 123.7 | 0.1 | 0.181x | 1.535x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 278.5 | 274.2 | 284.6 | 3.5 | 0.408x | 3.458x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 306.7 | 268.7 | 348.1 | 25.9 | 0.449x | 3.809x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 680.8 | 678.4 | 699.7 | 7.8 | 0.996x | 8.454x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 683.3 | 680.3 | 697.9 | 7.5 | 1.000x | 8.486x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-013` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 81.7 | 80.9 | 85.1 | 1.5 | 0.119x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 82.2 | 82.0 | 82.5 | 0.2 | 0.120x | 1.006x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 115.2 | 114.9 | 116.8 | 0.7 | 0.168x | 1.410x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 115.5 | 115.3 | 119.5 | 1.6 | 0.169x | 1.414x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 299.2 | 291.3 | 312.3 | 6.9 | 0.437x | 3.662x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 309.6 | 278.9 | 332.4 | 17.2 | 0.452x | 3.789x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 684.9 | 675.9 | 690.8 | 4.9 | 1.000x | 8.384x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-014` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 50.2 | 50.1 | 50.5 | 0.1 | 0.094x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 97.2 | 97.1 | 98.0 | 0.3 | 0.181x | 1.934x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 97.3 | 97.0 | 113.6 | 6.5 | 0.181x | 1.937x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 265.8 | 262.8 | 275.2 | 4.4 | 0.495x | 5.293x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 293.9 | 267.8 | 298.7 | 11.3 | 0.547x | 5.851x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 536.8 | 529.1 | 541.9 | 4.2 | 1.000x | 10.689x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 538.2 | 535.4 | 550.2 | 5.3 | 1.003x | 10.717x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-014` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 66.3 | 66.1 | 67.3 | 0.4 | 0.124x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 75.9 | 75.0 | 79.3 | 1.6 | 0.142x | 1.145x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 89.9 | 89.8 | 90.8 | 0.4 | 0.168x | 1.356x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 89.9 | 89.8 | 90.9 | 0.4 | 0.168x | 1.357x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 287.4 | 282.0 | 290.4 | 2.8 | 0.537x | 4.335x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 327.4 | 292.0 | 372.6 | 26.6 | 0.611x | 4.938x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 535.7 | 528.3 | 540.9 | 4.3 | 1.000x | 8.079x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-015` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 74.7 | 74.6 | 75.8 | 0.5 | 0.114x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 117.2 | 116.9 | 118.5 | 0.6 | 0.178x | 1.569x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 118.5 | 117.0 | 128.2 | 5.1 | 0.180x | 1.587x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 276.0 | 275.5 | 294.5 | 7.3 | 0.420x | 3.695x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 301.6 | 285.1 | 323.9 | 14.6 | 0.459x | 4.038x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 655.5 | 654.9 | 667.7 | 5.9 | 0.998x | 8.776x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 656.6 | 646.9 | 688.3 | 14.8 | 1.000x | 8.792x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-015` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 80.2 | 79.3 | 82.9 | 1.3 | 0.122x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 80.3 | 80.2 | 80.6 | 0.2 | 0.122x | 1.001x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 109.7 | 109.4 | 110.0 | 0.2 | 0.167x | 1.368x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 109.8 | 109.6 | 109.9 | 0.1 | 0.167x | 1.369x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 293.9 | 288.9 | 305.8 | 6.0 | 0.447x | 3.665x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 303.2 | 281.3 | 325.2 | 14.8 | 0.462x | 3.780x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 657.0 | 648.5 | 660.3 | 4.0 | 1.000x | 8.191x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-016` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.0 | 25.8 | 27.4 | 0.6 | 0.141x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 52.9 | 52.7 | 58.9 | 2.4 | 0.286x | 2.037x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 53.0 | 52.4 | 54.9 | 0.9 | 0.287x | 2.043x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 184.8 | 183.8 | 189.9 | 2.1 | 1.000x | 7.116x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 185.9 | 184.9 | 194.6 | 3.7 | 1.006x | 7.156x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 248.5 | 246.9 | 255.3 | 3.1 | 1.344x | 9.567x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 291.5 | 271.4 | 307.1 | 11.6 | 1.577x | 11.225x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-016` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 47.3 | 47.1 | 48.0 | 0.3 | 0.044x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 47.4 | 47.2 | 48.2 | 0.4 | 0.044x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 108.7 | 106.6 | 109.4 | 1.0 | 0.100x | 2.299x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 226.9 | 226.3 | 229.9 | 1.3 | 0.210x | 4.799x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 446.4 | 431.5 | 453.3 | 7.2 | 0.412x | 9.439x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 470.8 | 447.0 | 490.7 | 14.2 | 0.435x | 9.956x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,082.9 | 1,074.3 | 1,088.0 | 5.0 | 1.000x | 22.901x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-017` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 80.6 | 80.2 | 80.7 | 0.2 | 0.119x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 123.7 | 123.3 | 124.5 | 0.4 | 0.183x | 1.535x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 123.7 | 123.2 | 139.4 | 6.3 | 0.183x | 1.535x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 284.3 | 279.1 | 285.5 | 2.3 | 0.420x | 3.528x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 321.5 | 292.8 | 339.6 | 17.6 | 0.475x | 3.990x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 674.6 | 669.8 | 688.8 | 7.0 | 0.996x | 8.371x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 677.0 | 669.5 | 683.3 | 4.7 | 1.000x | 8.401x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-017` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 82.1 | 82.0 | 82.8 | 0.3 | 0.120x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 82.3 | 81.3 | 85.1 | 1.3 | 0.120x | 1.001x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 115.2 | 115.1 | 116.1 | 0.4 | 0.169x | 1.402x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 115.8 | 115.2 | 116.9 | 0.6 | 0.169x | 1.409x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 305.8 | 286.8 | 319.2 | 11.4 | 0.448x | 3.723x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 307.6 | 295.2 | 325.7 | 10.5 | 0.450x | 3.745x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 683.2 | 678.7 | 686.4 | 3.0 | 1.000x | 8.317x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-018` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 74.4 | 74.3 | 74.8 | 0.2 | 0.113x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 117.5 | 117.3 | 140.9 | 9.3 | 0.179x | 1.579x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 117.8 | 116.9 | 123.8 | 2.6 | 0.179x | 1.583x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 281.2 | 280.4 | 283.8 | 1.2 | 0.428x | 3.778x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 312.3 | 268.1 | 331.3 | 21.9 | 0.475x | 4.196x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 655.3 | 651.3 | 665.3 | 4.9 | 0.997x | 8.805x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 657.0 | 652.9 | 667.6 | 5.3 | 1.000x | 8.827x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-018` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 80.0 | 79.0 | 83.6 | 1.6 | 0.122x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 80.6 | 80.3 | 80.9 | 0.2 | 0.123x | 1.008x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 109.6 | 109.5 | 112.4 | 1.1 | 0.167x | 1.371x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 109.7 | 109.6 | 111.2 | 0.6 | 0.167x | 1.373x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 291.5 | 287.3 | 301.9 | 5.9 | 0.445x | 3.646x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 306.0 | 279.9 | 323.8 | 14.3 | 0.467x | 3.827x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 655.7 | 646.7 | 664.0 | 6.5 | 1.000x | 8.202x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-019` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.6 | 26.5 | 27.4 | 0.4 | 0.139x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 56.3 | 56.2 | 57.0 | 0.3 | 0.293x | 2.116x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 56.4 | 56.2 | 56.7 | 0.1 | 0.294x | 2.122x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 191.9 | 191.0 | 194.4 | 1.2 | 1.000x | 7.218x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 193.2 | 190.1 | 196.9 | 2.4 | 1.007x | 7.267x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 253.8 | 244.3 | 254.3 | 4.1 | 1.323x | 9.548x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 288.9 | 241.3 | 310.6 | 24.4 | 1.505x | 10.865x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-019` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 50.7 | 50.3 | 52.1 | 0.7 | 0.047x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 50.8 | 50.4 | 51.3 | 0.3 | 0.047x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 110.2 | 109.1 | 110.9 | 0.7 | 0.102x | 2.175x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 236.6 | 235.3 | 238.6 | 1.2 | 0.218x | 4.670x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 451.8 | 444.5 | 466.9 | 7.7 | 0.416x | 8.918x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 483.1 | 474.1 | 498.5 | 8.8 | 0.445x | 9.536x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,085.4 | 1,082.7 | 1,089.5 | 2.4 | 1.000x | 21.425x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-020` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 87.6 | 87.3 | 87.9 | 0.2 | 0.128x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 136.9 | 136.5 | 138.2 | 0.6 | 0.201x | 1.563x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 136.9 | 136.7 | 146.5 | 3.9 | 0.201x | 1.563x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 287.6 | 286.3 | 290.7 | 1.7 | 0.422x | 3.284x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 333.3 | 318.0 | 351.2 | 11.4 | 0.489x | 3.806x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 682.0 | 679.1 | 690.7 | 4.1 | 1.000x | 7.789x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 683.0 | 681.6 | 698.1 | 6.2 | 1.002x | 7.800x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-020` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 84.6 | 84.0 | 88.3 | 1.8 | 0.123x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 93.5 | 93.2 | 95.1 | 0.7 | 0.136x | 1.105x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 129.1 | 129.0 | 130.3 | 0.5 | 0.187x | 1.525x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 129.3 | 129.0 | 131.3 | 1.0 | 0.188x | 1.528x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 303.1 | 290.1 | 310.5 | 7.2 | 0.440x | 3.581x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 324.7 | 286.3 | 331.9 | 16.8 | 0.471x | 3.837x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 689.3 | 673.2 | 694.2 | 7.2 | 1.000x | 8.145x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-021` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 85.7 | 85.6 | 87.1 | 0.6 | 0.121x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 97.1 | 96.9 | 111.9 | 5.9 | 0.137x | 1.133x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 97.2 | 96.4 | 107.3 | 4.1 | 0.138x | 1.134x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 274.1 | 262.1 | 283.1 | 6.8 | 0.388x | 3.198x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 294.0 | 268.5 | 307.8 | 12.9 | 0.416x | 3.431x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 706.2 | 700.8 | 734.3 | 12.4 | 1.000x | 8.241x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 706.4 | 698.1 | 707.7 | 3.7 | 1.000x | 8.243x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-021` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 62.8 | 62.2 | 64.1 | 0.7 | 0.089x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 89.7 | 89.4 | 90.4 | 0.4 | 0.127x | 1.428x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 89.8 | 89.6 | 90.0 | 0.1 | 0.128x | 1.430x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 90.1 | 90.0 | 91.5 | 0.6 | 0.128x | 1.434x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 279.4 | 275.7 | 288.5 | 4.5 | 0.397x | 4.449x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 286.2 | 261.8 | 307.7 | 15.5 | 0.407x | 4.557x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 703.4 | 699.9 | 710.3 | 3.8 | 1.000x | 11.198x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-022` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 37.8 | 37.6 | 39.7 | 0.8 | 0.084x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 149.9 | 149.8 | 163.8 | 5.5 | 0.334x | 3.967x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 150.4 | 150.0 | 155.6 | 2.1 | 0.335x | 3.980x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 250.3 | 242.6 | 260.3 | 6.2 | 0.558x | 6.624x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 286.9 | 254.5 | 296.4 | 14.4 | 0.639x | 7.592x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 446.4 | 444.3 | 466.4 | 8.2 | 0.995x | 11.815x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 448.8 | 447.0 | 452.2 | 1.9 | 1.000x | 11.876x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-022` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 42.0 | 41.4 | 42.2 | 0.3 | 0.093x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 70.7 | 70.4 | 72.0 | 0.7 | 0.157x | 1.685x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 142.4 | 142.3 | 143.1 | 0.3 | 0.316x | 3.394x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 142.5 | 142.1 | 142.8 | 0.2 | 0.316x | 3.395x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 263.2 | 256.0 | 274.4 | 6.8 | 0.583x | 6.273x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 283.2 | 250.2 | 287.8 | 16.0 | 0.627x | 6.749x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 451.4 | 446.4 | 451.9 | 2.5 | 1.000x | 10.758x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-023` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 86.6 | 86.2 | 90.1 | 1.5 | 0.130x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 124.5 | 123.5 | 132.9 | 3.6 | 0.186x | 1.437x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 124.9 | 123.4 | 128.6 | 1.8 | 0.187x | 1.442x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 281.4 | 268.3 | 288.5 | 6.7 | 0.421x | 3.249x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 293.2 | 267.8 | 296.2 | 10.9 | 0.439x | 3.385x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 667.9 | 662.2 | 671.5 | 3.2 | 1.000x | 7.712x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 672.8 | 663.2 | 684.1 | 7.1 | 1.007x | 7.768x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-023` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 64.6 | 62.5 | 70.0 | 2.8 | 0.097x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 83.1 | 82.9 | 88.4 | 2.1 | 0.125x | 1.286x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 115.4 | 115.0 | 119.5 | 1.7 | 0.173x | 1.787x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 115.7 | 115.0 | 116.3 | 0.5 | 0.173x | 1.791x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 281.9 | 273.3 | 292.4 | 7.1 | 0.422x | 4.362x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 304.3 | 287.9 | 310.1 | 8.2 | 0.456x | 4.709x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 667.3 | 662.5 | 671.8 | 3.6 | 1.000x | 10.328x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-024` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 90.6 | 87.7 | 91.2 | 1.5 | 0.127x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 97.4 | 96.9 | 111.4 | 5.6 | 0.136x | 1.075x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 97.8 | 96.8 | 106.6 | 3.6 | 0.137x | 1.080x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 278.9 | 262.3 | 289.4 | 9.3 | 0.390x | 3.078x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 292.5 | 270.0 | 294.8 | 9.2 | 0.409x | 3.228x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 711.8 | 706.3 | 724.7 | 7.7 | 0.995x | 7.857x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 715.7 | 709.0 | 742.6 | 11.7 | 1.000x | 7.899x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-024` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 87.5 | 87.5 | 90.8 | 1.3 | 0.124x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 89.0 | 88.9 | 89.7 | 0.3 | 0.126x | 1.017x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 90.1 | 89.3 | 94.1 | 1.7 | 0.127x | 1.029x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 90.3 | 89.6 | 93.6 | 1.4 | 0.128x | 1.032x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 306.6 | 295.5 | 323.1 | 10.0 | 0.433x | 3.502x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 313.9 | 264.9 | 325.1 | 21.9 | 0.444x | 3.586x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 707.4 | 699.3 | 714.6 | 4.9 | 1.000x | 8.081x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-025` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 88.4 | 88.2 | 88.6 | 0.1 | 0.122x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 123.7 | 123.3 | 124.9 | 0.6 | 0.170x | 1.400x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 123.8 | 123.4 | 132.9 | 3.7 | 0.170x | 1.400x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 284.0 | 270.3 | 285.5 | 6.0 | 0.391x | 3.213x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 298.1 | 276.3 | 306.6 | 10.4 | 0.410x | 3.373x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 726.7 | 724.5 | 735.3 | 4.3 | 1.000x | 8.222x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 730.0 | 720.4 | 747.6 | 10.6 | 1.005x | 8.260x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-025` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 84.0 | 83.9 | 84.9 | 0.4 | 0.115x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 89.1 | 84.6 | 89.3 | 1.8 | 0.122x | 1.060x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 115.3 | 115.0 | 117.5 | 0.9 | 0.158x | 1.373x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 115.3 | 115.2 | 117.7 | 0.9 | 0.158x | 1.373x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 288.9 | 267.9 | 337.4 | 24.7 | 0.396x | 3.440x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 296.2 | 293.8 | 320.4 | 10.5 | 0.406x | 3.527x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 728.9 | 721.5 | 731.5 | 3.5 | 1.000x | 8.679x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-026` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 38.1 | 37.6 | 38.2 | 0.2 | 0.085x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 150.3 | 149.7 | 152.2 | 0.9 | 0.334x | 3.951x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 150.4 | 149.5 | 155.8 | 2.3 | 0.334x | 3.952x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 253.7 | 236.2 | 259.7 | 8.3 | 0.564x | 6.667x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 282.9 | 254.2 | 287.4 | 11.9 | 0.629x | 7.434x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 449.6 | 442.4 | 452.2 | 4.1 | 1.000x | 11.815x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 453.8 | 448.4 | 461.3 | 4.4 | 1.009x | 11.924x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-026` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 41.7 | 40.7 | 41.9 | 0.4 | 0.093x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 70.3 | 70.3 | 71.7 | 0.6 | 0.157x | 1.685x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 142.9 | 142.2 | 159.0 | 6.5 | 0.319x | 3.424x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 143.8 | 142.7 | 144.1 | 0.5 | 0.321x | 3.447x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 272.3 | 253.4 | 279.8 | 10.0 | 0.608x | 6.525x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 290.2 | 257.3 | 299.4 | 14.8 | 0.648x | 6.954x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 448.0 | 446.4 | 451.5 | 1.7 | 1.000x | 10.735x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-027` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 86.7 | 86.5 | 96.9 | 4.1 | 0.137x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 150.3 | 150.1 | 153.2 | 1.2 | 0.237x | 1.734x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 150.3 | 149.8 | 159.5 | 3.7 | 0.237x | 1.734x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 273.5 | 267.8 | 292.8 | 8.7 | 0.432x | 3.156x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 295.7 | 272.9 | 311.4 | 12.4 | 0.467x | 3.411x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 633.4 | 627.1 | 634.9 | 2.8 | 1.000x | 7.307x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 634.3 | 630.1 | 648.7 | 6.4 | 1.001x | 7.318x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-027` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 62.9 | 62.8 | 63.2 | 0.1 | 0.099x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 81.5 | 81.4 | 82.0 | 0.2 | 0.129x | 1.294x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 142.5 | 142.5 | 149.6 | 2.8 | 0.225x | 2.265x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 143.4 | 142.2 | 144.6 | 0.9 | 0.226x | 2.279x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 277.8 | 271.8 | 297.5 | 9.3 | 0.438x | 4.414x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 283.6 | 272.4 | 305.9 | 12.1 | 0.447x | 4.505x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 633.9 | 627.4 | 639.1 | 4.1 | 1.000x | 10.072x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-028` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 34.8 | 34.8 | 35.5 | 0.3 | 0.116x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 43.7 | 43.7 | 44.2 | 0.2 | 0.146x | 1.257x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 44.0 | 43.7 | 48.5 | 1.8 | 0.147x | 1.264x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 250.1 | 247.6 | 254.3 | 2.2 | 0.838x | 7.192x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 287.6 | 262.7 | 295.1 | 11.0 | 0.963x | 8.268x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 298.0 | 289.7 | 309.9 | 6.5 | 0.998x | 8.568x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 298.6 | 296.4 | 310.1 | 4.9 | 1.000x | 8.584x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-028` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 37.7 | 37.7 | 38.5 | 0.3 | 0.035x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 37.8 | 37.5 | 37.8 | 0.1 | 0.035x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.0 | 67.5 | 68.8 | 0.5 | 0.063x | 1.801x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 255.6 | 253.2 | 257.8 | 1.7 | 0.238x | 6.774x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 483.4 | 457.8 | 508.2 | 16.1 | 0.450x | 12.809x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 503.9 | 490.8 | 526.6 | 12.2 | 0.469x | 13.351x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,075.0 | 1,069.9 | 1,079.6 | 3.6 | 1.000x | 28.486x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-029` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 35.0 | 35.0 | 35.1 | 0.1 | 0.117x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 89.5 | 89.1 | 89.5 | 0.2 | 0.298x | 2.555x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 89.6 | 89.2 | 94.0 | 1.8 | 0.298x | 2.557x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 252.3 | 246.0 | 253.2 | 2.7 | 0.840x | 7.205x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 283.5 | 254.2 | 294.7 | 13.9 | 0.944x | 8.095x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 298.3 | 289.8 | 309.8 | 7.2 | 0.993x | 8.517x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 300.3 | 293.7 | 302.1 | 3.0 | 1.000x | 8.575x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-029` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 69.9 | 69.3 | 71.1 | 0.7 | 0.065x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 83.1 | 82.9 | 83.2 | 0.1 | 0.078x | 1.189x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 83.2 | 83.0 | 83.4 | 0.1 | 0.078x | 1.191x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 534.0 | 530.3 | 548.8 | 7.0 | 0.499x | 7.642x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 760.1 | 724.7 | 767.9 | 15.3 | 0.711x | 10.878x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 847.1 | 838.8 | 955.4 | 44.4 | 0.792x | 12.123x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,069.3 | 1,058.7 | 1,084.4 | 8.6 | 1.000x | 15.303x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-030` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 34.8 | 34.6 | 35.1 | 0.2 | 0.116x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 43.5 | 43.4 | 43.9 | 0.2 | 0.145x | 1.251x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 44.0 | 43.4 | 48.1 | 1.7 | 0.147x | 1.266x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 250.6 | 245.5 | 257.7 | 4.2 | 0.836x | 7.203x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 286.8 | 257.5 | 294.0 | 12.9 | 0.956x | 8.243x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 295.9 | 291.8 | 311.8 | 7.3 | 0.987x | 8.505x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 299.9 | 294.1 | 318.8 | 8.8 | 1.000x | 8.618x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-030` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 37.3 | 37.3 | 37.5 | 0.1 | 0.035x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 37.5 | 37.3 | 37.9 | 0.2 | 0.035x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 67.6 | 67.4 | 69.1 | 0.6 | 0.064x | 1.812x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 263.6 | 255.6 | 269.9 | 5.4 | 0.248x | 7.063x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 475.0 | 458.7 | 491.9 | 11.3 | 0.447x | 12.728x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 526.2 | 521.4 | 550.1 | 11.0 | 0.495x | 14.101x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,063.0 | 1,057.2 | 1,065.7 | 3.1 | 1.000x | 28.483x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-031` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 35.0 | 34.8 | 35.1 | 0.1 | 0.117x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 59.9 | 59.6 | 64.8 | 2.0 | 0.201x | 1.714x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 59.9 | 59.9 | 60.0 | 0.0 | 0.201x | 1.714x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 251.7 | 243.7 | 257.7 | 4.9 | 0.845x | 7.197x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 286.4 | 256.7 | 291.3 | 12.7 | 0.962x | 8.189x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 296.6 | 290.7 | 321.9 | 11.4 | 0.996x | 8.481x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 297.7 | 293.5 | 301.3 | 2.6 | 1.000x | 8.513x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-031` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 53.4 | 53.2 | 53.7 | 0.2 | 0.050x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 53.6 | 53.2 | 53.9 | 0.3 | 0.050x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 69.9 | 69.0 | 70.1 | 0.4 | 0.066x | 1.307x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 328.7 | 327.7 | 329.9 | 0.8 | 0.310x | 6.151x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 550.3 | 531.3 | 571.4 | 14.6 | 0.518x | 10.298x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 608.0 | 589.8 | 632.5 | 17.4 | 0.573x | 11.376x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,061.8 | 1,056.0 | 1,071.7 | 5.1 | 1.000x | 19.868x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-032` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 48.7 | 47.0 | 51.5 | 1.8 | 0.135x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 50.6 | 49.9 | 54.7 | 1.7 | 0.141x | 1.039x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 50.7 | 50.4 | 51.1 | 0.3 | 0.141x | 1.040x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 263.2 | 259.9 | 270.9 | 4.3 | 0.731x | 5.401x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 283.1 | 258.2 | 294.1 | 12.4 | 0.786x | 5.809x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 356.0 | 353.6 | 395.8 | 16.0 | 0.989x | 7.304x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 360.0 | 354.5 | 362.2 | 2.7 | 1.000x | 7.387x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-032` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 43.9 | 43.7 | 45.2 | 0.6 | 0.034x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 44.0 | 43.7 | 44.3 | 0.2 | 0.034x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 71.9 | 70.8 | 73.0 | 0.9 | 0.055x | 1.637x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 387.9 | 380.5 | 394.2 | 4.8 | 0.297x | 8.830x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 612.3 | 586.6 | 617.3 | 11.4 | 0.469x | 13.939x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 620.3 | 607.5 | 632.2 | 8.7 | 0.475x | 14.120x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,304.8 | 1,297.2 | 1,309.1 | 4.2 | 1.000x | 29.701x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-033` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 44.0 | 43.7 | 48.4 | 1.8 | 0.140x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 50.4 | 50.0 | 51.5 | 0.5 | 0.161x | 1.146x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 50.6 | 49.8 | 54.3 | 1.6 | 0.161x | 1.149x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 261.2 | 251.1 | 268.8 | 6.1 | 0.832x | 5.934x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 288.5 | 255.6 | 302.2 | 16.0 | 0.919x | 6.554x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 313.3 | 309.2 | 354.4 | 17.0 | 0.998x | 7.118x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 313.8 | 312.0 | 314.9 | 1.2 | 1.000x | 7.131x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-033` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 43.7 | 43.7 | 44.4 | 0.3 | 0.039x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 43.9 | 43.9 | 44.2 | 0.1 | 0.039x | 1.005x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 69.9 | 69.5 | 71.9 | 0.9 | 0.062x | 1.601x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 363.2 | 359.8 | 364.3 | 1.7 | 0.320x | 8.314x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 584.1 | 559.1 | 595.3 | 13.7 | 0.515x | 13.370x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 602.4 | 575.9 | 624.2 | 15.9 | 0.531x | 13.790x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,134.2 | 1,128.3 | 1,139.4 | 4.0 | 1.000x | 25.962x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-034` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 26.0 | 26.6 | 0.2 | 0.045x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 36.8 | 36.5 | 39.9 | 1.3 | 0.064x | 1.410x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 36.8 | 36.7 | 37.3 | 0.2 | 0.064x | 1.411x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 246.8 | 237.7 | 251.2 | 5.1 | 0.427x | 9.452x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 285.3 | 259.0 | 295.8 | 12.9 | 0.494x | 10.926x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 577.2 | 575.7 | 618.7 | 16.8 | 0.999x | 22.105x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 577.8 | 570.3 | 590.4 | 7.0 | 1.000x | 22.130x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-034` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 30.9 | 30.9 | 31.4 | 0.2 | 0.014x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 31.7 | 31.0 | 32.0 | 0.4 | 0.015x | 1.025x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 97.5 | 97.2 | 98.8 | 0.6 | 0.045x | 3.153x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 177.2 | 173.5 | 182.1 | 2.9 | 0.081x | 5.731x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 401.6 | 381.9 | 416.5 | 11.6 | 0.185x | 12.992x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 425.2 | 383.3 | 431.7 | 18.1 | 0.196x | 13.755x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,175.1 | 2,161.7 | 2,194.1 | 11.1 | 1.000x | 70.356x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-035` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 50.2 | 49.9 | 50.5 | 0.2 | 0.063x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 50.4 | 50.2 | 59.0 | 3.4 | 0.063x | 1.004x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 116.5 | 116.3 | 117.0 | 0.3 | 0.145x | 2.320x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 318.9 | 317.5 | 339.0 | 8.7 | 0.398x | 6.354x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 356.4 | 322.0 | 382.4 | 21.6 | 0.445x | 7.100x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 794.0 | 783.9 | 841.6 | 20.5 | 0.991x | 15.819x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 801.4 | 792.1 | 803.8 | 4.8 | 1.000x | 15.965x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-035` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 43.9 | 43.7 | 45.8 | 0.8 | 0.015x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 44.0 | 43.3 | 45.2 | 0.6 | 0.015x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 133.2 | 131.3 | 133.6 | 0.9 | 0.045x | 3.036x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 700.3 | 697.1 | 702.0 | 1.6 | 0.234x | 15.966x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 911.3 | 895.7 | 921.0 | 8.8 | 0.305x | 20.775x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 920.7 | 895.3 | 945.9 | 21.0 | 0.308x | 20.989x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,986.8 | 2,974.3 | 3,023.3 | 18.9 | 1.000x | 68.090x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-036` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 26.0 | 26.7 | 0.3 | 0.126x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 53.1 | 53.0 | 53.4 | 0.2 | 0.256x | 2.031x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 53.1 | 52.7 | 61.0 | 3.2 | 0.256x | 2.031x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 205.8 | 203.1 | 221.7 | 6.9 | 0.993x | 7.876x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 207.2 | 205.3 | 211.5 | 2.3 | 1.000x | 7.929x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 248.7 | 235.1 | 256.0 | 7.8 | 1.200x | 9.517x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 286.3 | 257.3 | 291.7 | 12.3 | 1.382x | 10.957x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-036` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 47.3 | 47.3 | 48.6 | 0.5 | 0.065x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 47.6 | 47.3 | 48.2 | 0.3 | 0.065x | 1.006x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 65.8 | 64.2 | 68.7 | 1.6 | 0.090x | 1.391x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 239.5 | 237.8 | 240.8 | 1.0 | 0.329x | 5.060x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 444.2 | 439.9 | 469.2 | 11.2 | 0.611x | 9.385x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 475.1 | 453.5 | 498.2 | 16.4 | 0.653x | 10.040x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 727.4 | 718.0 | 746.0 | 9.6 | 1.000x | 15.369x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-037` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 39.7 | 39.6 | 41.0 | 0.5 | 0.117x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 40.1 | 39.9 | 40.7 | 0.4 | 0.118x | 1.008x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 40.7 | 40.4 | 48.0 | 2.9 | 0.120x | 1.025x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 254.6 | 249.2 | 271.7 | 8.7 | 0.748x | 6.407x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 280.4 | 240.7 | 300.4 | 20.5 | 0.824x | 7.057x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 334.9 | 334.3 | 364.7 | 11.8 | 0.984x | 8.428x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 340.4 | 339.4 | 340.9 | 0.6 | 1.000x | 8.566x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-037` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 34.6 | 34.5 | 34.9 | 0.2 | 0.029x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 34.7 | 34.6 | 34.9 | 0.1 | 0.029x | 1.005x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.3 | 67.3 | 72.4 | 1.9 | 0.056x | 1.978x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 294.0 | 293.2 | 298.6 | 2.0 | 0.243x | 8.510x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 502.1 | 501.0 | 531.2 | 11.4 | 0.415x | 14.532x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 529.9 | 526.0 | 559.9 | 12.6 | 0.438x | 15.337x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,209.5 | 1,204.4 | 1,235.9 | 11.4 | 1.000x | 35.005x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-038` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 53.1 | 53.0 | 55.3 | 0.9 | 0.107x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 53.3 | 52.9 | 62.1 | 3.6 | 0.107x | 1.003x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 74.2 | 73.8 | 74.4 | 0.2 | 0.150x | 1.398x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 297.1 | 288.1 | 301.4 | 5.1 | 0.598x | 5.594x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 307.6 | 275.6 | 320.7 | 15.5 | 0.620x | 5.790x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 491.1 | 482.2 | 525.3 | 15.0 | 0.989x | 9.246x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 496.4 | 483.0 | 499.2 | 6.4 | 1.000x | 9.346x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-038` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 47.5 | 47.3 | 51.0 | 1.4 | 0.026x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 47.6 | 47.4 | 48.4 | 0.4 | 0.026x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 95.2 | 91.4 | 96.0 | 1.8 | 0.052x | 2.004x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 590.4 | 575.6 | 602.1 | 8.9 | 0.325x | 12.421x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 685.6 | 660.8 | 726.2 | 21.7 | 0.377x | 14.422x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 814.1 | 787.5 | 828.0 | 14.2 | 0.448x | 17.125x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,817.4 | 1,800.6 | 1,821.2 | 8.1 | 1.000x | 38.232x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-039` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 26.0 | 28.1 | 0.8 | 0.126x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 110.5 | 110.4 | 121.6 | 4.4 | 0.532x | 4.234x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 110.9 | 110.6 | 119.6 | 3.5 | 0.534x | 4.250x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 205.2 | 198.5 | 211.2 | 4.5 | 0.987x | 7.861x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 207.8 | 203.5 | 209.7 | 2.5 | 1.000x | 7.963x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 253.8 | 247.8 | 271.2 | 8.0 | 1.221x | 9.724x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 291.8 | 255.0 | 298.5 | 15.8 | 1.404x | 11.178x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-039` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 105.4 | 105.1 | 106.1 | 0.4 | 0.112x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 105.7 | 104.9 | 109.5 | 1.6 | 0.113x | 1.003x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 105.9 | 105.2 | 111.0 | 2.2 | 0.113x | 1.004x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 109.3 | 105.5 | 110.1 | 1.7 | 0.117x | 1.037x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 334.7 | 325.4 | 350.9 | 10.0 | 0.357x | 3.174x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 351.5 | 330.7 | 374.7 | 15.3 | 0.375x | 3.334x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 937.4 | 927.1 | 948.2 | 6.9 | 1.000x | 8.890x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-040` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 25.2 | 25.2 | 25.3 | 0.0 | 0.707x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 34.3 | 33.7 | 40.9 | 2.8 | 0.961x | 1.359x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 35.7 | 34.3 | 38.6 | 1.8 | 1.000x | 1.414x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 46.8 | 46.4 | 46.9 | 0.2 | 1.310x | 1.852x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 46.8 | 46.7 | 47.0 | 0.1 | 1.313x | 1.856x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 241.6 | 228.7 | 254.6 | 10.4 | 6.769x | 9.572x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 244.9 | 230.2 | 263.9 | 12.2 | 6.861x | 9.703x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-040` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 35.1 | 34.9 | 40.7 | 2.3 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 39.3 | 36.7 | 41.6 | 1.6 | 1.119x | 1.119x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 40.3 | 40.1 | 40.7 | 0.2 | 1.149x | 1.149x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 40.4 | 40.0 | 43.0 | 1.1 | 1.152x | 1.152x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 200.5 | 199.3 | 200.8 | 0.5 | 5.710x | 5.710x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 411.8 | 409.0 | 438.4 | 11.2 | 11.729x | 11.729x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 457.2 | 442.8 | 481.3 | 13.3 | 13.022x | 13.022x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-041` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 16.5 | 16.3 | 18.7 | 0.9 | 0.569x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.0 | 28.9 | 31.2 | 0.9 | 1.000x | 1.758x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.3 | 29.2 | 29.7 | 0.2 | 1.011x | 1.777x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 34.3 | 33.9 | 35.1 | 0.4 | 1.184x | 2.081x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 34.5 | 34.2 | 39.2 | 1.9 | 1.192x | 2.095x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 253.3 | 237.1 | 269.9 | 11.1 | 8.744x | 15.368x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 261.3 | 246.8 | 263.0 | 7.3 | 9.019x | 15.852x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-041` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 29.2 | 29.2 | 29.5 | 0.1 | 0.798x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 29.4 | 29.3 | 30.2 | 0.3 | 0.804x | 1.007x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 36.6 | 35.8 | 42.0 | 2.3 | 1.000x | 1.253x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 40.3 | 37.2 | 43.0 | 1.8 | 1.101x | 1.380x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 144.1 | 143.2 | 144.9 | 0.6 | 3.940x | 4.936x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 357.9 | 344.4 | 373.4 | 9.6 | 9.785x | 12.260x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 370.8 | 358.4 | 446.5 | 31.7 | 10.137x | 12.702x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-042` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 17.3 | 17.3 | 17.5 | 0.1 | 0.084x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 17.4 | 17.3 | 18.9 | 0.6 | 0.084x | 1.005x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 18.7 | 18.7 | 19.2 | 0.2 | 0.090x | 1.079x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 207.4 | 206.8 | 213.5 | 2.5 | 0.999x | 11.955x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 207.5 | 204.1 | 212.0 | 2.8 | 1.000x | 11.963x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 249.2 | 215.6 | 268.9 | 17.5 | 1.201x | 14.363x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 264.2 | 240.2 | 277.2 | 13.6 | 1.273x | 15.229x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-042` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 12.7 | 12.6 | 13.0 | 0.1 | 0.059x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 12.7 | 12.6 | 14.9 | 0.9 | 0.059x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 52.8 | 51.9 | 54.9 | 1.2 | 0.245x | 4.164x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 64.3 | 63.6 | 64.7 | 0.4 | 0.297x | 5.065x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 216.1 | 214.4 | 217.5 | 1.0 | 1.000x | 17.028x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 279.6 | 273.8 | 291.2 | 7.6 | 1.294x | 22.032x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 312.8 | 289.0 | 334.9 | 16.3 | 1.447x | 24.642x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-043` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 23.5 | 23.4 | 24.7 | 0.6 | 0.151x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 130.2 | 130.1 | 130.5 | 0.2 | 0.837x | 5.530x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 130.2 | 130.0 | 138.9 | 3.5 | 0.838x | 5.532x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 153.0 | 152.3 | 162.1 | 3.7 | 0.984x | 6.498x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 155.5 | 151.7 | 158.1 | 2.3 | 1.000x | 6.604x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 238.7 | 235.8 | 250.7 | 5.5 | 1.535x | 10.139x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 264.7 | 253.3 | 270.5 | 6.2 | 1.702x | 11.243x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-043` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 101.9 | 98.9 | 103.8 | 1.7 | 0.096x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 124.3 | 124.0 | 124.4 | 0.2 | 0.117x | 1.220x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 124.5 | 124.3 | 125.4 | 0.4 | 0.117x | 1.222x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 150.7 | 147.5 | 151.6 | 1.7 | 0.142x | 1.479x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 369.0 | 351.6 | 393.5 | 13.7 | 0.347x | 3.621x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 369.9 | 352.9 | 378.6 | 9.2 | 0.348x | 3.630x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,064.0 | 1,061.3 | 1,077.5 | 7.1 | 1.000x | 10.441x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-044` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 16.4 | 16.3 | 18.4 | 0.8 | 0.561x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.2 | 29.0 | 30.9 | 0.7 | 1.000x | 1.783x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.5 | 29.2 | 29.7 | 0.2 | 1.009x | 1.800x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 111.9 | 111.1 | 112.2 | 0.4 | 3.833x | 6.833x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 112.2 | 111.4 | 120.4 | 3.4 | 3.842x | 6.848x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 255.2 | 226.4 | 265.4 | 13.5 | 8.737x | 15.576x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 256.3 | 241.4 | 285.9 | 14.6 | 8.774x | 15.641x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-044` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 73.0 | 71.6 | 75.9 | 1.5 | 0.135x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 79.3 | 77.4 | 83.3 | 2.1 | 0.147x | 1.086x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 107.2 | 106.7 | 110.9 | 1.5 | 0.199x | 1.469x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 107.3 | 106.9 | 107.7 | 0.3 | 0.199x | 1.470x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 286.0 | 283.1 | 310.0 | 9.8 | 0.531x | 3.920x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 298.4 | 269.2 | 309.6 | 13.4 | 0.554x | 4.090x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 539.0 | 532.3 | 544.3 | 5.1 | 1.000x | 7.388x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-045` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 23.5 | 23.3 | 25.0 | 0.6 | 0.154x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 49.8 | 49.7 | 50.6 | 0.3 | 0.325x | 2.113x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 49.8 | 49.7 | 51.2 | 0.6 | 0.325x | 2.115x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 151.7 | 151.5 | 159.9 | 3.3 | 0.990x | 6.444x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 153.2 | 151.3 | 159.9 | 3.4 | 1.000x | 6.507x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 242.1 | 232.1 | 249.7 | 6.0 | 1.580x | 10.284x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 265.5 | 252.3 | 278.9 | 9.9 | 1.733x | 11.277x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-045` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 43.9 | 43.7 | 45.0 | 0.4 | 0.087x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 44.0 | 43.9 | 45.3 | 0.5 | 0.087x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 65.1 | 62.7 | 65.5 | 1.3 | 0.129x | 1.483x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 225.5 | 224.9 | 226.9 | 0.8 | 0.445x | 5.136x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 424.9 | 420.4 | 448.7 | 10.4 | 0.839x | 9.677x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 467.0 | 435.7 | 472.2 | 13.2 | 0.922x | 10.637x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 506.6 | 493.9 | 509.6 | 6.3 | 1.000x | 11.537x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-046` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 36.5 | 36.3 | 36.7 | 0.1 | 0.078x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 36.6 | 36.2 | 38.9 | 1.0 | 0.078x | 1.002x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 52.2 | 51.9 | 52.5 | 0.2 | 0.111x | 1.427x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 270.8 | 258.1 | 280.6 | 8.0 | 0.576x | 7.411x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 292.4 | 257.5 | 298.7 | 14.9 | 0.622x | 8.002x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 469.8 | 467.0 | 501.2 | 12.6 | 1.000x | 12.856x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 471.8 | 462.6 | 489.5 | 9.2 | 1.004x | 12.912x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-046` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 31.1 | 31.0 | 31.7 | 0.3 | 0.018x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 31.1 | 30.9 | 31.4 | 0.2 | 0.018x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 88.5 | 84.8 | 91.6 | 2.6 | 0.051x | 2.848x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 348.1 | 347.1 | 349.7 | 0.8 | 0.200x | 11.204x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 545.0 | 523.4 | 549.8 | 9.5 | 0.314x | 17.542x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 570.1 | 543.7 | 582.1 | 13.6 | 0.328x | 18.348x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,738.2 | 1,725.1 | 1,747.2 | 7.6 | 1.000x | 55.943x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-047` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.0 | 26.0 | 26.2 | 0.1 | 0.033x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 39.8 | 39.7 | 40.3 | 0.2 | 0.050x | 1.530x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 40.6 | 39.6 | 45.9 | 2.3 | 0.051x | 1.559x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 242.6 | 233.3 | 258.5 | 8.5 | 0.307x | 9.318x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 285.4 | 256.3 | 291.7 | 12.6 | 0.361x | 10.963x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 785.1 | 779.1 | 841.1 | 22.8 | 0.993x | 30.158x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 790.8 | 777.6 | 792.6 | 5.5 | 1.000x | 30.376x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-047` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 34.4 | 34.3 | 34.8 | 0.2 | 0.011x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 34.5 | 34.3 | 35.2 | 0.3 | 0.011x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 120.4 | 118.3 | 120.6 | 0.9 | 0.040x | 3.503x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 185.1 | 183.0 | 187.5 | 1.5 | 0.061x | 5.385x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 411.5 | 385.9 | 414.6 | 12.5 | 0.136x | 11.973x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 414.7 | 400.7 | 418.1 | 6.3 | 0.137x | 12.066x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,029.7 | 3,014.9 | 3,046.7 | 11.5 | 1.000x | 88.142x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-048` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 18.8 | 18.6 | 18.9 | 0.1 | 0.063x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 22.2 | 22.1 | 22.4 | 0.1 | 0.074x | 1.180x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 22.3 | 22.3 | 24.2 | 0.8 | 0.075x | 1.186x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 244.1 | 222.3 | 259.1 | 13.3 | 0.819x | 12.967x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 272.5 | 236.7 | 284.6 | 16.7 | 0.914x | 14.471x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 296.1 | 292.6 | 313.6 | 7.5 | 0.993x | 15.726x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 298.2 | 295.0 | 335.8 | 15.5 | 1.000x | 15.837x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-048` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 17.9 | 17.8 | 18.8 | 0.3 | 0.022x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 18.1 | 17.9 | 18.7 | 0.3 | 0.022x | 1.008x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 62.2 | 60.5 | 64.0 | 1.3 | 0.077x | 3.469x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 90.3 | 89.4 | 94.2 | 1.6 | 0.112x | 5.036x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 321.2 | 257.1 | 343.9 | 30.7 | 0.399x | 17.905x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 322.3 | 286.3 | 336.8 | 16.9 | 0.401x | 17.966x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 804.5 | 802.4 | 811.9 | 4.2 | 1.000x | 44.840x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-049` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 22.3 | 22.1 | 22.5 | 0.1 | 0.153x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 126.6 | 126.5 | 127.1 | 0.2 | 0.870x | 5.682x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 127.0 | 126.4 | 135.9 | 3.6 | 0.872x | 5.699x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 143.0 | 141.2 | 161.5 | 7.5 | 0.983x | 6.420x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 145.6 | 144.1 | 146.6 | 1.0 | 1.000x | 6.533x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 242.4 | 231.9 | 255.3 | 8.6 | 1.666x | 10.881x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 273.4 | 254.4 | 280.0 | 8.7 | 1.878x | 12.272x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-049` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 98.8 | 97.1 | 104.2 | 2.5 | 0.096x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 121.2 | 120.8 | 125.5 | 1.8 | 0.118x | 1.227x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 121.5 | 121.0 | 122.1 | 0.4 | 0.118x | 1.230x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 129.5 | 128.1 | 148.4 | 7.7 | 0.126x | 1.311x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 351.0 | 328.4 | 356.8 | 10.2 | 0.341x | 3.554x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 353.7 | 334.7 | 359.6 | 11.2 | 0.344x | 3.581x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,028.0 | 1,018.4 | 1,047.6 | 10.5 | 1.000x | 10.408x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-050` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 41.8 | 40.3 | 43.0 | 1.0 | 0.138x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 100.6 | 100.3 | 101.2 | 0.3 | 0.332x | 2.409x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 102.0 | 100.7 | 110.0 | 3.5 | 0.337x | 2.443x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 257.1 | 248.6 | 270.2 | 7.1 | 0.850x | 6.158x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 288.3 | 252.3 | 293.4 | 14.9 | 0.953x | 6.905x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 300.7 | 297.8 | 325.1 | 10.2 | 0.994x | 7.201x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 302.5 | 297.7 | 305.0 | 2.5 | 1.000x | 7.245x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-050` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 95.2 | 94.9 | 96.0 | 0.4 | 0.058x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 95.2 | 94.8 | 95.4 | 0.2 | 0.058x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 105.1 | 103.5 | 109.3 | 2.0 | 0.064x | 1.104x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 304.1 | 302.4 | 305.6 | 1.1 | 0.185x | 3.194x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 457.2 | 440.6 | 487.9 | 18.8 | 0.279x | 4.803x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 506.4 | 495.2 | 517.4 | 7.3 | 0.309x | 5.319x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,639.3 | 1,630.1 | 1,648.7 | 7.3 | 1.000x | 17.220x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-051` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 22.3 | 22.2 | 23.7 | 0.6 | 0.155x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 126.6 | 126.5 | 127.0 | 0.2 | 0.880x | 5.675x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 127.2 | 126.5 | 135.6 | 3.4 | 0.884x | 5.701x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 143.1 | 140.8 | 158.9 | 6.7 | 0.995x | 6.412x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 143.8 | 140.3 | 146.7 | 2.1 | 1.000x | 6.446x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 239.5 | 232.4 | 254.4 | 8.1 | 1.665x | 10.735x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 271.1 | 253.9 | 279.5 | 8.8 | 1.885x | 12.150x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-051` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 98.6 | 97.7 | 103.1 | 2.0 | 0.096x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 121.1 | 120.9 | 124.9 | 1.5 | 0.118x | 1.229x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 121.2 | 121.1 | 122.3 | 0.5 | 0.118x | 1.229x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 128.3 | 127.9 | 129.5 | 0.6 | 0.125x | 1.302x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 343.1 | 336.8 | 355.8 | 7.3 | 0.335x | 3.481x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 350.5 | 329.6 | 356.8 | 9.7 | 0.342x | 3.556x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,024.3 | 1,009.5 | 1,039.4 | 10.4 | 1.000x | 10.391x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-052` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 26.0 | 27.1 | 0.4 | 0.087x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 37.2 | 37.1 | 37.4 | 0.1 | 0.124x | 1.423x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 37.6 | 37.4 | 40.6 | 1.2 | 0.126x | 1.436x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 243.8 | 233.8 | 250.5 | 6.2 | 0.815x | 9.318x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 287.7 | 258.6 | 297.0 | 13.2 | 0.962x | 10.999x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 294.1 | 291.7 | 313.1 | 7.9 | 0.983x | 11.241x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 299.2 | 295.8 | 313.1 | 6.1 | 1.000x | 11.436x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-052` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 31.3 | 31.2 | 32.6 | 0.5 | 0.029x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 31.5 | 31.5 | 33.0 | 0.6 | 0.029x | 1.008x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.7 | 67.3 | 71.5 | 1.7 | 0.064x | 2.196x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 176.7 | 174.0 | 178.3 | 1.6 | 0.164x | 5.644x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 404.9 | 393.9 | 445.4 | 17.7 | 0.376x | 12.933x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 406.3 | 383.3 | 410.5 | 11.4 | 0.377x | 12.978x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,077.9 | 1,068.5 | 1,084.8 | 5.3 | 1.000x | 34.431x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-053` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 26.1 | 27.2 | 0.4 | 0.089x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 28.2 | 27.8 | 28.3 | 0.2 | 0.095x | 1.074x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 28.4 | 28.2 | 29.9 | 0.6 | 0.096x | 1.082x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 245.3 | 234.8 | 251.4 | 6.2 | 0.831x | 9.355x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 288.2 | 255.0 | 303.5 | 16.3 | 0.976x | 10.993x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 294.7 | 292.4 | 312.2 | 7.5 | 0.998x | 11.240x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 295.2 | 294.1 | 301.4 | 2.7 | 1.000x | 11.260x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-053` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 21.3 | 21.0 | 21.6 | 0.2 | 0.020x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 21.3 | 21.1 | 22.7 | 0.6 | 0.020x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.4 | 65.8 | 69.6 | 1.5 | 0.065x | 3.218x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 166.8 | 164.9 | 169.1 | 1.5 | 0.158x | 7.847x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 394.7 | 389.4 | 404.9 | 5.1 | 0.374x | 18.572x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 400.8 | 375.0 | 414.4 | 15.0 | 0.379x | 18.860x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,056.7 | 1,049.2 | 1,069.8 | 6.8 | 1.000x | 49.725x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-054` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 26.0 | 26.5 | 0.2 | 0.088x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 28.0 | 27.9 | 28.1 | 0.1 | 0.095x | 1.076x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 28.2 | 28.0 | 30.4 | 0.9 | 0.095x | 1.081x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 247.3 | 233.7 | 253.9 | 7.2 | 0.835x | 9.494x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 286.8 | 255.7 | 287.5 | 12.4 | 0.968x | 11.009x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 295.2 | 292.8 | 313.9 | 7.9 | 0.996x | 11.332x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 296.3 | 294.4 | 301.1 | 2.5 | 1.000x | 11.376x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-054` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 21.2 | 21.0 | 21.5 | 0.2 | 0.020x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 21.3 | 21.1 | 21.6 | 0.2 | 0.020x | 1.007x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 66.8 | 64.9 | 69.7 | 1.8 | 0.063x | 3.158x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 170.3 | 165.5 | 170.5 | 2.0 | 0.160x | 8.048x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 393.8 | 377.9 | 405.3 | 9.4 | 0.370x | 18.611x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 397.3 | 379.0 | 438.2 | 22.9 | 0.374x | 18.774x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,063.3 | 1,057.5 | 1,064.8 | 3.1 | 1.000x | 50.249x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-055` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 26.1 | 26.6 | 0.2 | 0.089x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 28.1 | 27.8 | 29.7 | 0.7 | 0.095x | 1.071x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 28.2 | 28.0 | 30.6 | 1.0 | 0.096x | 1.078x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 249.5 | 234.4 | 254.8 | 7.6 | 0.844x | 9.524x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 283.3 | 256.5 | 286.7 | 11.3 | 0.959x | 10.818x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 294.5 | 293.4 | 312.7 | 7.3 | 0.997x | 11.245x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 295.5 | 294.3 | 301.2 | 3.0 | 1.000x | 11.284x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-055` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 21.2 | 21.0 | 23.3 | 0.9 | 0.020x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 21.2 | 21.2 | 21.3 | 0.0 | 0.020x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 67.1 | 65.3 | 69.3 | 1.5 | 0.064x | 3.169x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 168.9 | 165.6 | 170.5 | 1.7 | 0.160x | 7.977x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 398.3 | 385.5 | 412.1 | 9.5 | 0.377x | 18.811x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 405.1 | 361.3 | 433.9 | 25.9 | 0.384x | 19.131x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,055.1 | 1,051.7 | 1,136.5 | 32.6 | 1.000x | 49.832x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-056` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.2 | 26.0 | 27.7 | 0.6 | 0.088x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 30.9 | 30.7 | 32.4 | 0.6 | 0.103x | 1.181x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 31.0 | 30.8 | 32.3 | 0.6 | 0.104x | 1.183x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 251.2 | 237.2 | 258.0 | 8.5 | 0.840x | 9.589x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 283.6 | 253.3 | 286.7 | 12.3 | 0.948x | 10.827x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 294.5 | 293.6 | 310.9 | 6.6 | 0.985x | 11.242x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 299.1 | 292.3 | 303.3 | 4.2 | 1.000x | 11.418x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-056` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 25.4 | 25.3 | 28.2 | 1.1 | 0.024x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 25.5 | 25.4 | 29.6 | 1.6 | 0.024x | 1.005x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 67.2 | 65.1 | 69.8 | 1.7 | 0.063x | 2.648x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 158.4 | 156.7 | 165.1 | 3.0 | 0.148x | 6.238x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 386.8 | 379.2 | 398.3 | 6.5 | 0.363x | 15.237x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 397.3 | 355.8 | 409.9 | 20.5 | 0.372x | 15.650x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,066.9 | 1,049.0 | 1,074.9 | 9.5 | 1.000x | 42.027x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-057` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 7,695.9 | 7,688.4 | 7,744.5 | 20.4 | 0.776x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7,871.4 | 7,859.3 | 7,894.1 | 13.3 | 0.794x | 1.023x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7,918.3 | 7,863.2 | 8,002.2 | 48.2 | 0.798x | 1.029x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 9,859.2 | 9,827.4 | 9,878.4 | 16.9 | 0.994x | 1.281x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 9,918.9 | 9,829.2 | 9,970.4 | 56.0 | 1.000x | 1.289x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 67,298.3 | 67,249.2 | 67,361.6 | 38.9 | 6.785x | 8.745x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 67,491.2 | 67,374.7 | 67,996.4 | 226.6 | 6.804x | 8.770x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-058` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 5,971.4 | 5,913.7 | 6,151.8 | 86.0 | 0.082x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 6,145.7 | 6,081.6 | 6,201.2 | 44.7 | 0.084x | 1.029x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 6,675.3 | 6,669.3 | 6,695.3 | 9.0 | 0.092x | 1.118x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 26,316.1 | 26,297.5 | 26,343.4 | 15.2 | 0.361x | 4.407x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 26,352.1 | 26,306.2 | 26,422.6 | 39.2 | 0.362x | 4.413x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 72,825.0 | 72,670.3 | 74,077.2 | 552.5 | 1.000x | 12.196x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 72,970.1 | 72,674.5 | 78,811.0 | 2,379.3 | 1.002x | 12.220x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-059` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 13,749.4 | 13,740.5 | 13,818.2 | 29.1 | 0.086x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 13,907.4 | 13,872.5 | 14,000.9 | 44.2 | 0.087x | 1.011x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 26,064.0 | 26,020.4 | 26,117.0 | 35.4 | 0.163x | 1.896x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33,713.1 | 33,688.7 | 33,802.2 | 42.9 | 0.211x | 2.452x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33,735.5 | 33,683.9 | 33,776.5 | 39.3 | 0.211x | 2.454x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 159,044.0 | 158,732.5 | 161,263.0 | 966.9 | 0.994x | 11.567x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 159,936.5 | 158,786.1 | 162,249.9 | 1,233.3 | 1.000x | 11.632x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-060` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 7,664.6 | 7,656.8 | 7,691.1 | 11.9 | 0.811x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7,818.9 | 7,785.7 | 7,841.9 | 20.4 | 0.827x | 1.020x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7,867.9 | 7,833.5 | 7,936.9 | 34.1 | 0.832x | 1.027x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 9,438.7 | 9,419.2 | 9,538.3 | 47.0 | 0.999x | 1.231x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 9,451.2 | 9,423.7 | 9,717.2 | 110.0 | 1.000x | 1.233x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 33,480.3 | 33,462.8 | 33,575.0 | 42.0 | 3.542x | 4.368x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 33,536.1 | 33,522.2 | 33,827.7 | 117.7 | 3.548x | 4.375x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-061` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 5,391.2 | 5,373.8 | 5,452.7 | 27.2 | 0.120x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6,158.0 | 6,137.2 | 6,577.2 | 189.1 | 0.137x | 1.142x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 6,305.0 | 6,296.9 | 6,414.4 | 44.7 | 0.141x | 1.169x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13,196.0 | 13,179.0 | 13,238.8 | 20.3 | 0.295x | 2.448x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13,197.4 | 13,174.8 | 13,210.4 | 12.5 | 0.295x | 2.448x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 44,625.9 | 44,550.6 | 45,315.0 | 301.9 | 0.996x | 8.277x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 44,790.5 | 44,638.6 | 45,021.3 | 141.2 | 1.000x | 8.308x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-062` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 43.7 | 43.7 | 44.6 | 0.3 | 0.138x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 224.8 | 206.7 | 269.3 | 24.6 | 0.708x | 5.141x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 245.4 | 238.7 | 281.9 | 15.9 | 0.773x | 5.612x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 317.4 | 317.0 | 319.0 | 0.8 | 1.000x | 7.256x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 321.7 | 318.6 | 333.2 | 5.5 | 1.014x | 7.356x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 1,686.2 | 1,682.8 | 1,700.4 | 6.2 | 5.313x | 38.554x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 1,690.2 | 1,683.4 | 1,702.9 | 6.3 | 5.326x | 38.646x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-063` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 6,877.5 | 6,857.1 | 6,937.4 | 29.1 | 0.062x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 7,041.6 | 7,024.9 | 7,114.8 | 32.0 | 0.064x | 1.024x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 13,122.7 | 13,112.7 | 13,128.9 | 5.8 | 0.119x | 1.908x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 25,279.6 | 25,276.9 | 25,357.2 | 31.2 | 0.229x | 3.676x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 25,351.7 | 25,280.8 | 25,394.7 | 42.0 | 0.229x | 3.686x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 110,103.9 | 109,391.1 | 111,391.7 | 701.5 | 0.997x | 16.009x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 110,485.5 | 110,032.6 | 115,677.4 | 2,110.9 | 1.000x | 16.065x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-064` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 10,640.7 | 10,624.5 | 10,649.9 | 10.8 | 0.111x | 1.000x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 10,799.0 | 10,772.3 | 10,869.6 | 34.6 | 0.113x | 1.015x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 11,644.1 | 11,605.0 | 12,777.2 | 455.9 | 0.122x | 1.094x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 27,033.2 | 27,014.2 | 27,185.9 | 70.3 | 0.283x | 2.541x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 27,036.7 | 26,989.2 | 27,561.3 | 212.5 | 0.283x | 2.541x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 95,112.6 | 94,870.7 | 97,338.8 | 917.3 | 0.996x | 8.939x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 95,533.2 | 95,262.6 | 95,877.6 | 233.1 | 1.000x | 8.978x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-065` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 16.4 | 16.3 | 19.5 | 1.3 | 0.564x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.0 | 28.9 | 30.0 | 0.4 | 1.000x | 1.773x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.4 | 29.3 | 29.6 | 0.1 | 1.014x | 1.797x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 41.3 | 41.2 | 41.4 | 0.1 | 1.423x | 2.523x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 41.6 | 41.1 | 41.7 | 0.2 | 1.434x | 2.543x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 209.5 | 204.8 | 228.4 | 9.6 | 7.222x | 12.807x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 226.1 | 178.6 | 244.2 | 23.5 | 7.793x | 13.817x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-065` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 33.7 | 33.7 | 36.2 | 1.0 | 0.060x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 34.6 | 33.7 | 42.2 | 3.1 | 0.061x | 1.026x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 63.3 | 61.0 | 65.8 | 1.6 | 0.112x | 1.877x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 230.0 | 228.5 | 233.7 | 1.7 | 0.408x | 6.820x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 454.9 | 444.0 | 473.6 | 10.8 | 0.807x | 13.488x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 460.4 | 434.4 | 469.0 | 13.9 | 0.816x | 13.652x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 563.9 | 554.6 | 571.4 | 5.6 | 1.000x | 16.720x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-066` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 74.6 | 74.6 | 74.8 | 0.1 | 0.114x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 117.2 | 117.1 | 117.3 | 0.1 | 0.178x | 1.570x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 118.6 | 117.4 | 135.5 | 7.1 | 0.180x | 1.589x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 271.1 | 250.8 | 281.1 | 10.8 | 0.412x | 3.632x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 275.5 | 269.2 | 316.5 | 19.6 | 0.419x | 3.691x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 657.3 | 650.8 | 663.4 | 4.3 | 1.000x | 8.808x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 660.0 | 651.3 | 666.3 | 5.1 | 1.004x | 8.843x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-066` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 80.4 | 80.3 | 80.8 | 0.2 | 0.121x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 82.2 | 81.3 | 84.9 | 1.3 | 0.124x | 1.021x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 109.9 | 109.6 | 115.7 | 2.4 | 0.166x | 1.366x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 111.5 | 109.7 | 114.7 | 1.8 | 0.168x | 1.386x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 295.4 | 286.8 | 298.9 | 4.8 | 0.445x | 3.672x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 313.8 | 295.5 | 326.8 | 10.6 | 0.473x | 3.901x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 663.3 | 653.2 | 669.5 | 5.7 | 1.000x | 8.245x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-067` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 77.7 | 77.7 | 79.6 | 0.8 | 0.122x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 110.5 | 110.5 | 110.8 | 0.1 | 0.173x | 1.423x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 110.8 | 110.2 | 120.0 | 3.8 | 0.173x | 1.427x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 279.4 | 271.6 | 296.7 | 9.2 | 0.437x | 3.597x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 284.0 | 275.8 | 292.6 | 5.8 | 0.444x | 3.656x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 639.1 | 634.4 | 647.0 | 4.7 | 1.000x | 8.226x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 648.4 | 635.2 | 656.9 | 7.1 | 1.015x | 8.346x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-067` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 81.7 | 80.9 | 86.1 | 1.9 | 0.127x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 90.0 | 89.8 | 90.1 | 0.1 | 0.140x | 1.102x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 103.2 | 102.3 | 104.6 | 0.7 | 0.161x | 1.264x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 103.4 | 102.8 | 103.7 | 0.3 | 0.161x | 1.266x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 286.9 | 254.3 | 299.4 | 15.3 | 0.448x | 3.513x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 291.4 | 285.0 | 320.7 | 12.9 | 0.455x | 3.569x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 640.9 | 626.3 | 650.0 | 8.1 | 1.000x | 7.849x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-068` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 20.8 | 20.6 | 21.0 | 0.1 | 0.050x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 40.2 | 39.8 | 40.4 | 0.2 | 0.097x | 1.934x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 40.4 | 39.8 | 49.6 | 3.7 | 0.098x | 1.947x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 258.6 | 221.8 | 261.8 | 14.8 | 0.623x | 12.451x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 261.1 | 241.1 | 273.7 | 11.0 | 0.630x | 12.572x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 414.7 | 411.7 | 421.1 | 3.1 | 1.000x | 19.971x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 416.2 | 408.8 | 425.0 | 5.4 | 1.004x | 20.043x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-068` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 26.2 | 25.5 | 27.1 | 0.5 | 0.063x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 32.6 | 32.4 | 32.9 | 0.2 | 0.078x | 1.246x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 32.6 | 32.4 | 34.4 | 0.7 | 0.078x | 1.247x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 58.9 | 54.1 | 64.9 | 3.8 | 0.142x | 2.252x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 262.8 | 257.4 | 282.5 | 8.8 | 0.631x | 10.041x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 264.5 | 248.6 | 271.5 | 7.7 | 0.635x | 10.106x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 416.3 | 415.5 | 420.3 | 1.7 | 1.000x | 15.908x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-069` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 26.0 | 27.2 | 0.4 | 0.125x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 53.2 | 52.9 | 53.6 | 0.2 | 0.255x | 2.034x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 54.1 | 53.5 | 54.4 | 0.4 | 0.260x | 2.071x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 206.2 | 206.0 | 223.2 | 6.6 | 0.989x | 7.889x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 208.5 | 208.0 | 215.2 | 2.7 | 1.000x | 7.976x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 244.5 | 224.4 | 261.5 | 12.1 | 1.173x | 9.356x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 283.0 | 241.7 | 299.4 | 19.2 | 1.358x | 10.830x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-069` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 47.0 | 47.0 | 48.3 | 0.5 | 0.065x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 47.2 | 47.1 | 47.4 | 0.1 | 0.065x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 66.2 | 65.4 | 68.6 | 1.3 | 0.091x | 1.408x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 236.5 | 235.7 | 241.4 | 2.1 | 0.327x | 5.028x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 455.5 | 442.6 | 469.0 | 9.7 | 0.629x | 9.685x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 455.8 | 441.9 | 478.7 | 12.1 | 0.630x | 9.691x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 723.8 | 716.7 | 724.6 | 3.0 | 1.000x | 15.389x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-070` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 44.7 | 44.2 | 46.1 | 0.7 | 0.082x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 90.7 | 90.3 | 90.8 | 0.2 | 0.167x | 2.030x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 91.0 | 90.6 | 100.7 | 3.9 | 0.167x | 2.037x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 262.9 | 251.6 | 292.8 | 14.5 | 0.484x | 5.883x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 287.6 | 247.3 | 292.2 | 16.4 | 0.529x | 6.436x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 542.3 | 536.1 | 578.9 | 15.9 | 0.998x | 12.136x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 543.6 | 542.6 | 545.3 | 0.9 | 1.000x | 12.164x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-070` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 51.3 | 51.0 | 52.1 | 0.4 | 0.094x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 75.1 | 74.0 | 79.1 | 1.9 | 0.138x | 1.462x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 82.9 | 82.7 | 83.4 | 0.3 | 0.152x | 1.614x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 83.8 | 82.7 | 84.7 | 0.8 | 0.154x | 1.633x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 273.0 | 262.6 | 284.5 | 6.9 | 0.501x | 5.317x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 282.8 | 268.4 | 289.3 | 7.8 | 0.519x | 5.509x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 545.2 | 539.0 | 552.1 | 4.2 | 1.000x | 10.618x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-071` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 58.4 | 57.8 | 60.6 | 1.0 | 0.104x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 202.6 | 202.4 | 203.6 | 0.4 | 0.361x | 3.469x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 204.5 | 202.7 | 213.3 | 4.7 | 0.365x | 3.502x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 271.8 | 269.9 | 276.6 | 2.4 | 0.485x | 4.654x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 278.7 | 244.0 | 288.8 | 16.4 | 0.497x | 4.773x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 560.5 | 558.9 | 564.5 | 1.9 | 1.000x | 9.600x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 561.8 | 557.3 | 580.0 | 7.8 | 1.002x | 9.622x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-071` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 65.4 | 65.2 | 67.6 | 0.9 | 0.116x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 89.7 | 89.1 | 94.9 | 2.2 | 0.159x | 1.371x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 194.4 | 194.2 | 195.1 | 0.3 | 0.346x | 2.973x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 194.7 | 194.2 | 194.9 | 0.3 | 0.346x | 2.977x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 281.7 | 272.8 | 295.4 | 7.4 | 0.501x | 4.307x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 286.9 | 265.0 | 293.8 | 10.4 | 0.510x | 4.387x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 562.8 | 556.7 | 568.0 | 3.9 | 1.000x | 8.604x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-072` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 67.1 | 66.9 | 68.0 | 0.4 | 0.056x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 166.0 | 165.8 | 166.9 | 0.4 | 0.139x | 2.474x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 166.3 | 166.0 | 174.8 | 3.4 | 0.139x | 2.479x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 300.0 | 285.2 | 306.2 | 7.4 | 0.251x | 4.472x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 386.8 | 324.0 | 394.8 | 26.0 | 0.324x | 5.766x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,194.3 | 1,183.1 | 1,241.6 | 21.1 | 0.999x | 17.804x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,195.2 | 1,173.4 | 1,213.3 | 15.1 | 1.000x | 17.817x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-072` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 153.6 | 153.1 | 154.8 | 0.6 | 0.089x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 160.8 | 160.4 | 161.4 | 0.4 | 0.093x | 1.047x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 160.8 | 160.7 | 162.1 | 0.5 | 0.093x | 1.047x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 171.4 | 168.1 | 186.7 | 6.6 | 0.099x | 1.116x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 368.4 | 350.2 | 380.0 | 11.0 | 0.212x | 2.398x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 424.0 | 400.5 | 426.5 | 10.6 | 0.244x | 2.760x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,734.5 | 1,729.4 | 1,750.7 | 7.4 | 1.000x | 11.289x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-073` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 26.1 | 26.0 | 26.9 | 0.3 | 0.087x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 40.2 | 40.1 | 40.5 | 0.1 | 0.135x | 1.540x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 40.3 | 40.2 | 44.9 | 1.9 | 0.135x | 1.543x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 246.7 | 231.9 | 248.2 | 6.1 | 0.826x | 9.452x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 285.9 | 242.5 | 291.5 | 17.9 | 0.957x | 10.953x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 298.5 | 292.3 | 312.5 | 6.7 | 0.999x | 11.434x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 298.7 | 295.8 | 304.6 | 3.2 | 1.000x | 11.444x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-073` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 34.5 | 34.3 | 35.0 | 0.2 | 0.032x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 34.5 | 34.3 | 35.6 | 0.5 | 0.032x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 68.5 | 67.4 | 71.9 | 1.6 | 0.064x | 1.988x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 190.0 | 188.8 | 190.7 | 0.6 | 0.177x | 5.512x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 406.4 | 385.4 | 426.1 | 13.6 | 0.378x | 11.793x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 420.2 | 411.0 | 458.6 | 17.6 | 0.391x | 12.192x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,073.8 | 1,054.5 | 1,081.4 | 9.1 | 1.000x | 31.156x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-074` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 35.1 | 35.0 | 35.1 | 0.0 | 0.118x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 53.3 | 53.1 | 54.9 | 0.7 | 0.180x | 1.519x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 53.5 | 52.9 | 58.6 | 2.1 | 0.181x | 1.525x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 253.0 | 236.4 | 253.9 | 6.7 | 0.855x | 7.217x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 285.3 | 247.8 | 291.0 | 16.0 | 0.964x | 8.137x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 295.4 | 295.0 | 312.7 | 6.9 | 0.998x | 8.426x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 296.0 | 292.9 | 301.6 | 3.0 | 1.000x | 8.443x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-074` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 47.1 | 46.9 | 48.7 | 0.7 | 0.044x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 47.3 | 46.9 | 47.8 | 0.4 | 0.044x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 70.1 | 69.5 | 72.1 | 1.0 | 0.066x | 1.488x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 303.6 | 301.5 | 304.6 | 1.2 | 0.284x | 6.443x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 531.2 | 504.6 | 550.2 | 16.9 | 0.497x | 11.273x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 578.4 | 546.6 | 597.8 | 18.7 | 0.541x | 12.276x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,068.4 | 1,058.4 | 1,079.7 | 8.0 | 1.000x | 22.674x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-075` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 88.4 | 88.3 | 90.1 | 0.7 | 0.140x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 110.5 | 110.3 | 111.0 | 0.2 | 0.175x | 1.250x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 111.2 | 110.6 | 119.9 | 3.6 | 0.176x | 1.257x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 280.6 | 270.4 | 286.7 | 6.1 | 0.445x | 3.174x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 292.4 | 271.6 | 297.6 | 9.0 | 0.464x | 3.306x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 630.5 | 629.3 | 638.6 | 4.1 | 1.000x | 7.130x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 641.3 | 633.6 | 662.4 | 10.1 | 1.017x | 7.253x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-075` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 69.2 | 68.9 | 69.6 | 0.2 | 0.109x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 87.5 | 87.2 | 87.9 | 0.3 | 0.137x | 1.264x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 102.7 | 102.5 | 103.8 | 0.4 | 0.162x | 1.486x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 103.2 | 102.9 | 103.3 | 0.2 | 0.162x | 1.492x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 278.8 | 265.6 | 290.1 | 9.9 | 0.438x | 4.032x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 292.0 | 281.4 | 303.0 | 7.7 | 0.459x | 4.222x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 636.1 | 628.1 | 647.9 | 6.4 | 1.000x | 9.198x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-076` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 88.6 | 88.2 | 89.2 | 0.4 | 0.140x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 110.7 | 110.5 | 111.4 | 0.3 | 0.175x | 1.249x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 111.2 | 110.4 | 119.6 | 3.5 | 0.176x | 1.255x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 277.5 | 267.7 | 282.2 | 5.0 | 0.439x | 3.131x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 292.4 | 270.6 | 298.9 | 10.4 | 0.462x | 3.299x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 632.8 | 625.3 | 643.9 | 6.2 | 1.000x | 7.139x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 636.7 | 628.2 | 652.6 | 8.4 | 1.006x | 7.183x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-076` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 69.2 | 69.1 | 69.3 | 0.1 | 0.109x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 87.8 | 87.3 | 88.0 | 0.3 | 0.138x | 1.269x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 102.9 | 102.7 | 105.6 | 1.1 | 0.161x | 1.487x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 103.2 | 102.2 | 103.6 | 0.5 | 0.162x | 1.491x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 280.7 | 265.6 | 290.5 | 8.9 | 0.441x | 4.057x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 293.8 | 277.7 | 303.6 | 9.1 | 0.461x | 4.246x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 637.1 | 633.2 | 639.2 | 2.4 | 1.000x | 9.208x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-077` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 87.3 | 86.5 | 88.4 | 0.6 | 0.125x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 110.6 | 110.5 | 111.2 | 0.3 | 0.158x | 1.267x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 110.9 | 110.5 | 119.6 | 3.5 | 0.158x | 1.270x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 275.0 | 269.5 | 287.8 | 6.4 | 0.392x | 3.148x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 298.0 | 272.1 | 300.6 | 10.6 | 0.425x | 3.412x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 700.8 | 695.5 | 712.6 | 5.8 | 1.000x | 8.023x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 716.3 | 698.5 | 854.4 | 57.4 | 1.022x | 8.202x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-077` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 62.8 | 62.3 | 69.7 | 2.8 | 0.090x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 88.7 | 88.3 | 89.1 | 0.3 | 0.127x | 1.411x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 103.0 | 102.8 | 103.3 | 0.2 | 0.147x | 1.639x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 103.4 | 102.7 | 103.8 | 0.4 | 0.148x | 1.645x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 286.5 | 249.0 | 320.6 | 27.0 | 0.410x | 4.559x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 291.4 | 273.9 | 310.4 | 12.3 | 0.417x | 4.637x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 698.9 | 693.9 | 704.9 | 3.6 | 1.000x | 11.123x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-078` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 74.0 | 73.8 | 74.1 | 0.1 | 0.102x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 110.8 | 110.4 | 111.1 | 0.2 | 0.153x | 1.497x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 110.9 | 110.8 | 117.2 | 2.5 | 0.153x | 1.498x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 271.0 | 267.3 | 273.5 | 2.4 | 0.375x | 3.662x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 289.1 | 268.1 | 297.4 | 10.2 | 0.400x | 3.906x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 723.6 | 718.0 | 730.5 | 4.6 | 1.000x | 9.776x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 724.8 | 720.4 | 768.0 | 17.5 | 1.002x | 9.793x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-078` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 64.7 | 60.0 | 72.1 | 4.2 | 0.090x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 83.7 | 83.1 | 85.5 | 0.9 | 0.116x | 1.294x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 103.2 | 103.0 | 103.6 | 0.2 | 0.143x | 1.594x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 103.3 | 103.2 | 121.5 | 7.2 | 0.143x | 1.597x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 277.5 | 263.8 | 296.3 | 11.2 | 0.384x | 4.289x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 284.6 | 239.8 | 321.1 | 29.3 | 0.394x | 4.399x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 722.5 | 716.7 | 732.4 | 6.2 | 1.000x | 11.166x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-079` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 73.9 | 73.8 | 74.0 | 0.1 | 0.102x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 110.6 | 110.3 | 114.9 | 1.7 | 0.153x | 1.496x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 111.0 | 110.3 | 111.9 | 0.5 | 0.154x | 1.501x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 270.8 | 267.2 | 281.1 | 4.8 | 0.375x | 3.662x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 283.5 | 263.9 | 309.9 | 17.0 | 0.393x | 3.834x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 721.9 | 720.9 | 741.4 | 7.8 | 1.000x | 9.764x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 722.8 | 721.8 | 764.6 | 16.4 | 1.001x | 9.776x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-079` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 64.9 | 62.1 | 67.9 | 2.2 | 0.089x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 83.3 | 83.1 | 84.5 | 0.6 | 0.115x | 1.284x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 103.0 | 102.6 | 103.1 | 0.2 | 0.142x | 1.588x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 103.1 | 102.6 | 103.8 | 0.4 | 0.142x | 1.590x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 285.7 | 268.5 | 306.5 | 13.4 | 0.393x | 4.404x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 297.0 | 249.2 | 320.4 | 24.9 | 0.409x | 4.578x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 726.3 | 719.1 | 736.4 | 5.7 | 1.000x | 11.196x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-080` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 46.8 | 46.6 | 47.5 | 0.3 | 0.134x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 50.4 | 50.0 | 54.8 | 1.8 | 0.144x | 1.076x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 50.5 | 49.7 | 54.9 | 1.9 | 0.144x | 1.080x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 265.9 | 261.8 | 273.7 | 4.2 | 0.759x | 5.681x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 284.1 | 254.5 | 287.4 | 12.3 | 0.811x | 6.070x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 350.2 | 348.5 | 353.4 | 1.7 | 1.000x | 7.483x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 355.5 | 347.6 | 388.0 | 14.5 | 1.015x | 7.595x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-080` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 43.9 | 43.7 | 44.4 | 0.3 | 0.035x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 44.4 | 43.7 | 46.1 | 0.8 | 0.035x | 1.011x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 70.8 | 70.3 | 74.0 | 1.4 | 0.056x | 1.613x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 378.5 | 377.2 | 379.4 | 0.8 | 0.297x | 8.623x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 598.9 | 590.0 | 600.5 | 3.9 | 0.471x | 13.644x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 611.2 | 603.0 | 638.0 | 12.5 | 0.480x | 13.924x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,272.3 | 1,266.8 | 1,281.3 | 5.2 | 1.000x | 28.985x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-081` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 11.9 | 11.8 | 12.3 | 0.2 | 0.408x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 12.1 | 11.9 | 12.1 | 0.1 | 0.412x | 1.011x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 15.6 | 15.5 | 16.8 | 0.5 | 0.533x | 1.307x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.2 | 29.0 | 29.5 | 0.2 | 1.000x | 2.453x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.3 | 28.9 | 34.2 | 2.1 | 1.001x | 2.455x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 247.4 | 224.7 | 268.2 | 13.8 | 8.463x | 20.757x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 262.5 | 250.8 | 272.2 | 7.2 | 8.979x | 22.022x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-081` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 4.6 | 4.5 | 5.3 | 0.3 | 0.151x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 4.9 | 4.4 | 5.5 | 0.4 | 0.160x | 1.058x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 17.2 | 17.1 | 18.9 | 0.7 | 0.565x | 3.743x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30.4 | 30.1 | 31.0 | 0.3 | 1.000x | 6.627x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 37.4 | 37.1 | 38.0 | 0.3 | 1.231x | 8.157x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 209.2 | 204.4 | 235.5 | 11.5 | 6.881x | 45.600x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 247.9 | 239.0 | 271.2 | 12.3 | 8.156x | 54.046x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-082` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 13.0 | 12.7 | 15.4 | 1.0 | 0.436x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 13.5 | 12.8 | 14.8 | 0.7 | 0.452x | 1.035x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 16.4 | 16.3 | 18.7 | 0.9 | 0.550x | 1.260x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 29.5 | 29.3 | 31.5 | 0.9 | 0.989x | 2.266x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 29.9 | 29.1 | 30.3 | 0.4 | 1.000x | 2.292x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 248.7 | 229.0 | 268.5 | 12.5 | 8.328x | 19.089x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 263.1 | 251.1 | 271.3 | 6.9 | 8.809x | 20.193x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-082` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 5.1 | 5.1 | 6.8 | 0.7 | 0.161x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 5.1 | 5.0 | 6.2 | 0.4 | 0.163x | 1.013x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 24.0 | 23.9 | 26.9 | 1.1 | 0.762x | 4.729x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 31.5 | 31.0 | 34.9 | 1.4 | 1.000x | 6.205x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 40.1 | 38.8 | 40.6 | 0.6 | 1.271x | 7.886x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 245.4 | 217.0 | 261.2 | 16.5 | 7.785x | 48.305x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 261.6 | 239.0 | 298.0 | 22.9 | 8.299x | 51.500x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-083` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 21.6 | 21.5 | 22.6 | 0.4 | 0.589x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 36.6 | 35.7 | 38.7 | 1.1 | 1.000x | 1.697x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 36.9 | 35.0 | 38.1 | 1.2 | 1.008x | 1.711x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 138.0 | 137.6 | 138.2 | 0.2 | 3.771x | 6.400x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 138.5 | 138.2 | 139.1 | 0.4 | 3.786x | 6.427x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 244.7 | 240.3 | 248.0 | 2.5 | 6.689x | 11.354x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 272.3 | 257.7 | 282.2 | 7.8 | 7.443x | 12.634x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-083` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 35.5 | 35.4 | 43.4 | 3.2 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 40.3 | 39.9 | 44.7 | 1.8 | 1.135x | 1.135x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 132.0 | 131.8 | 132.6 | 0.3 | 3.718x | 3.718x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 132.1 | 132.0 | 134.3 | 1.0 | 3.721x | 3.721x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 616.6 | 613.7 | 630.9 | 6.1 | 17.369x | 17.369x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 839.0 | 809.0 | 845.9 | 13.6 | 23.634x | 23.634x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 863.7 | 841.5 | 868.4 | 12.1 | 24.330x | 24.330x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-084` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 23.1 | 22.9 | 24.4 | 0.6 | 0.634x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 30.3 | 30.1 | 31.3 | 0.4 | 0.833x | 1.315x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 30.4 | 30.2 | 30.5 | 0.1 | 0.835x | 1.318x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 35.4 | 34.0 | 37.1 | 1.0 | 0.973x | 1.535x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 36.4 | 35.1 | 38.4 | 1.4 | 1.000x | 1.578x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 237.2 | 225.7 | 246.4 | 6.7 | 6.515x | 10.283x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 260.4 | 233.4 | 264.2 | 11.5 | 7.152x | 11.289x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `s-084` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 24.9 | 24.9 | 27.0 | 0.8 | 0.713x | 1.000x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 25.0 | 24.9 | 26.6 | 0.6 | 0.716x | 1.004x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 34.9 | 34.8 | 42.1 | 2.9 | 1.000x | 1.402x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 39.5 | 39.1 | 40.7 | 0.5 | 1.132x | 1.588x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 125.0 | 124.2 | 126.9 | 0.9 | 3.580x | 5.021x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 328.6 | 325.1 | 353.0 | 10.5 | 9.410x | 13.197x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 353.9 | 350.0 | 375.6 | 9.4 | 10.135x | 14.213x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,716,942.6 | 3,676,996.1 | 3,962,741.4 | 105,028.8 | 0.129x | 1.000x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 5,514,810.0 | 5,497,894.8 | 5,886,715.0 | 151,500.9 | 0.191x | 1.484x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 6,542,380.1 | 6,533,295.3 | 6,549,917.4 | 5,888.6 | 0.227x | 1.760x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 6,546,199.3 | 6,535,898.5 | 6,599,885.0 | 23,271.6 | 0.227x | 1.761x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 12,112,463.0 | 11,459,356.0 | 13,238,110.3 | 652,907.4 | 0.420x | 3.259x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 12,594,527.0 | 11,540,583.2 | 12,999,718.2 | 513,274.6 | 0.437x | 3.388x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28,819,359.7 | 28,736,457.2 | 29,162,079.1 | 155,307.3 | 1.000x | 7.754x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,772.8 | 17,751.1 | 17,794.1 | 14.9 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,570,591.8 | 2,567,361.8 | 2,586,428.6 | 7,774.1 | 144.636x | 144.636x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 3,428,525.6 | 3,418,886.9 | 3,463,530.5 | 15,999.0 | 192.908x | 192.908x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 3,433,874.3 | 3,419,820.9 | 3,458,171.2 | 14,923.8 | 193.209x | 193.209x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 16,029,994.2 | 15,803,482.8 | 16,746,954.0 | 323,159.8 | 901.939x | 901.939x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 16,153,819.5 | 15,986,018.8 | 16,494,018.2 | 181,111.1 | 908.906x | 908.906x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 16,968,804.0 | 16,819,943.0 | 17,133,175.0 | 99,216.8 | 954.762x | 954.762x |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,792.2 | 17,764.3 | 22,237.2 | 1,765.1 | 1.000x | 1.000x | 5 | 100% |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,830,238.0 | 2,828,751.3 | 2,842,780.3 | 5,188.6 | 159.072x | 159.072x | 5 | 100% |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 3,422,799.6 | 3,414,990.9 | 3,436,319.7 | 8,063.5 | 192.376x | 192.376x | 5 | 100% |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 3,424,102.3 | 3,415,649.6 | 3,511,766.2 | 35,973.8 | 192.449x | 192.449x | 5 | 100% |

- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

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

| pattern | form | testee | median total_ns | min | max | stddev | n costed | jitter | outcomes | engine | entry | prefilter | vm_rungs | buffer_frames | buffer_trail | resume_frame_size | emit-c ns | gcc ns | load ns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `pcrec_692c2e8_auto-caps-simdna` | 137,870,986.0 | 131,535,054.0 | 141,303,679.0 | 3,360,140.2 | 5 |  | compiled=5 | dfa | plain entry | (no stamp — pcrec I-3) | - | - | - | 0 | 7,879,962.0 | 129,878,084.0 | 187,322.0 |
| `factored` | `whole-subject` | `pcrec_692c2e8_auto-caps-simdna` | 151,352,487.0 | 146,828,416.0 | 172,195,634.0 | 9,583,670.9 | 5 |  | compiled=5 | dfa | plain entry | (no stamp — pcrec I-3) | - | - | - | 0 | 20,639,297.0 | 136,587,108.0 | 100,681.0 |
| `factored` | `plain` | `pcrec_692c2e8_auto-nocaps-simdna` | 135,825,530.0 | 123,966,752.0 | 150,180,853.0 | 8,917,589.7 | 5 |  | compiled=5 | dfa | plain entry | (no stamp — pcrec I-3) | - | - | - | 0 | 7,829,735.0 | 127,847,695.0 | 199,751.0 |
| `factored` | `whole-subject` | `pcrec_692c2e8_auto-nocaps-simdna` | 141,989,216.0 | 125,149,031.0 | 147,678,719.0 | 8,307,974.1 | 5 |  | compiled=5 | dfa | plain entry | (no stamp — pcrec I-3) | - | - | - | 0 | 10,456,650.0 | 128,978,521.0 | 108,621.0 |
| `factored` | `plain` | `pcrec_692c2e8_vm-caps-simdna` | 535,765,380.0 | 526,468,518.0 | 537,513,576.0 | 4,046,565.0 | 5 |  | compiled=5 | vm | plain entry | none | PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED | - | - | 24 | 2,136,698.0 | 532,659,209.0 | 99,420.0 |
| `factored` | `whole-subject` | `pcrec_692c2e8_vm-caps-simdna` | 538,961,373.0 | 537,787,867.0 | 542,941,905.0 | 1,841,075.2 | 5 |  | compiled=5 | vm | plain entry | none | PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED | - | - | 24 | 2,024,237.0 | 536,246,952.0 | 108,041.0 |
| `factored` | `plain` | `pcrec_692c2e8_vm-in-caps-simdna` | 533,212,035.0 | 528,952,948.0 | 535,271,359.0 | 2,613,095.7 | 5 |  | compiled=5 | vm | _in | none | PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED | 32768 | 131072 | 24 | 2,036,853.0 | 529,840,444.0 | 108,041.0 |
| `factored` | `whole-subject` | `pcrec_692c2e8_vm-in-caps-simdna` | 542,331,633.0 | 530,896,401.0 | 545,425,863.0 | 5,487,425.3 | 5 |  | compiled=5 | vm | _in | none | PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED | 32768 | 131072 | 24 | 2,076,533.0 | 539,578,846.0 | 115,011.0 |
| `factored` | `plain` | `pcrec_8da6120_auto-caps-simdna` | 420,465,289.0 | 414,985,073.0 | 428,903,342.0 | 4,893,507.9 | 5 |  | compiled=5 | vm | plain entry | none | PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED | - | - | - | 1,880,342.0 | 418,531,336.0 | 110,891.0 |
| `factored` | `whole-subject` | `pcrec_8da6120_auto-caps-simdna` | 430,387,601.0 | 417,874,860.0 | 443,938,027.0 | 8,743,376.0 | 5 |  | compiled=5 | vm | plain entry | none | PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED | - | - | - | 1,903,072.0 | 428,382,468.0 | 199,551.0 |
| `factored` | `plain` | `pcrec_8da6120_auto-nocaps-simdna` | 427,493,516.0 | 422,008,523.0 | 434,926,485.0 | 4,492,879.1 | 5 |  | compiled=5 | vm | plain entry | none | PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED | - | - | - | 3,458,012.0 | 423,761,643.0 | 190,832.0 |
| `factored` | `whole-subject` | `pcrec_8da6120_auto-nocaps-simdna` | 420,974,905.0 | 413,095,565.0 | 432,864,330.0 | 7,311,852.8 | 5 |  | compiled=5 | vm | plain entry | none | PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED | - | - | - | 1,773,151.0 | 419,081,683.0 | 189,551.0 |
| `factored` | `plain` | `pcrec_8da6120_vm-caps-simdna` | 424,762,944.0 | 423,664,078.0 | 432,708,304.0 | 3,362,545.9 | 5 |  | compiled=5 | vm | plain entry | none | PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED | - | - | - | 1,716,071.0 | 422,822,902.0 | 193,901.0 |
| `factored` | `whole-subject` | `pcrec_8da6120_vm-caps-simdna` | 427,987,625.0 | 424,012,201.0 | 439,228,106.0 | 5,642,429.0 | 5 |  | compiled=5 | vm | plain entry | none | PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED | - | - | - | 1,699,401.0 | 426,211,414.0 | 190,301.0 |
| `orig` | `plain` | `pcrec_692c2e8_auto-caps-simdna` | 138,059,729.0 | 124,894,261.0 | 149,332,363.0 | 8,629,100.3 | 5 |  | compiled=5 | dfa | plain entry | (no stamp — pcrec I-3) | - | - | - | 0 | 7,446,200.0 | 130,525,339.0 | 196,291.0 |
| `orig` | `whole-subject` | `pcrec_692c2e8_auto-caps-simdna` | 140,676,166.0 | 139,723,758.0 | 158,223,452.0 | 7,360,641.1 | 5 |  | compiled=5 | dfa | plain entry | (no stamp — pcrec I-3) | - | - | - | 0 | 9,551,293.0 | 130,252,656.0 | 99,850.0 |
| `orig` | `plain` | `pcrec_692c2e8_auto-nocaps-simdna` | 133,689,958.0 | 120,601,984.0 | 142,934,562.0 | 8,297,236.7 | 5 |  | compiled=5 | dfa | plain entry | (no stamp — pcrec I-3) | - | - | - | 0 | 7,566,984.0 | 118,019,499.0 | 206,471.0 |
| `orig` | `whole-subject` | `pcrec_692c2e8_auto-nocaps-simdna` | 160,936,575.0 | 140,161,606.0 | 164,819,689.0 | 10,686,048.7 | 5 |  | compiled=5 | dfa | plain entry | (no stamp — pcrec I-3) | - | - | - | 0 | 20,150,875.0 | 141,206,022.0 | 196,861.0 |
| `orig` | `plain` | `pcrec_692c2e8_vm-caps-simdna` | 406,687,295.0 | 398,252,896.0 | 413,024,068.0 | 5,798,706.7 | 5 |  | compiled=5 | vm | plain entry | none | PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED | - | - | 24 | 1,943,277.0 | 401,723,407.0 | 195,001.0 |
| `orig` | `whole-subject` | `pcrec_692c2e8_vm-caps-simdna` | 404,607,847.0 | 391,192,410.0 | 416,889,170.0 | 8,332,820.0 | 5 |  | compiled=5 | vm | plain entry | none | PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED | - | - | 24 | 1,846,257.0 | 402,667,491.0 | 102,910.0 |
| `orig` | `plain` | `pcrec_692c2e8_vm-in-caps-simdna` | 406,593,912.0 | 392,519,313.0 | 419,969,716.0 | 9,292,650.8 | 5 |  | compiled=5 | vm | _in | none | PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED | 32768 | 131072 | 24 | 1,944,632.0 | 404,648,530.0 | 100,580.0 |
| `orig` | `whole-subject` | `pcrec_692c2e8_vm-in-caps-simdna` | 401,511,589.0 | 398,264,420.0 | 408,501,273.0 | 3,919,558.6 | 5 |  | compiled=5 | vm | _in | none | PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED | 32768 | 131072 | 24 | 2,046,133.0 | 399,354,875.0 | 110,581.0 |
| `orig` | `plain` | `pcrec_8da6120_auto-caps-simdna` | 118,056,825.0 | 103,621,896.0 | 120,772,314.0 | 6,366,891.3 | 5 |  | compiled=5 | dfa | plain entry | (no stamp — pcrec I-3) | - | - | - | - | 7,414,687.0 | 110,543,728.0 | 98,410.0 |
| `orig` | `whole-subject` | `pcrec_8da6120_auto-caps-simdna` | 117,555,053.0 | 109,696,744.0 | 130,533,016.0 | 9,212,004.5 | 5 |  | compiled=5 | dfa | plain entry | (no stamp — pcrec I-3) | - | - | - | - | 9,605,031.0 | 107,535,020.0 | 194,121.0 |
| `orig` | `plain` | `pcrec_8da6120_auto-nocaps-simdna` | 113,739,182.0 | 110,959,754.0 | 143,108,420.0 | 11,988,842.7 | 5 |  | compiled=5 | dfa | plain entry | (no stamp — pcrec I-3) | - | - | - | - | 7,620,208.0 | 106,465,166.0 | 107,390.0 |
| `orig` | `whole-subject` | `pcrec_8da6120_auto-nocaps-simdna` | 135,300,201.0 | 122,043,665.0 | 137,739,956.0 | 6,730,911.2 | 5 |  | compiled=5 | dfa | plain entry | (no stamp — pcrec I-3) | - | - | - | - | 19,767,436.0 | 115,433,954.0 | 101,750.0 |
| `orig` | `plain` | `pcrec_8da6120_vm-caps-simdna` | 382,875,770.0 | 372,878,556.0 | 389,967,264.0 | 6,557,411.6 | 5 |  | compiled=5 | vm | plain entry | none | PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED | - | - | - | 1,976,132.0 | 380,961,488.0 | 196,851.0 |
| `orig` | `whole-subject` | `pcrec_8da6120_vm-caps-simdna` | 374,587,618.0 | 362,494,710.0 | 389,369,562.0 | 9,692,150.1 | 5 |  | compiled=5 | vm | plain entry | none | PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED | - | - | - | 2,358,745.0 | 372,141,432.0 | 101,580.0 |

### `eager-jit`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 68,951.0 | 62,961.0 | 164,202.0 | 38,343.6 | 5 |  | compiled=5 |
| `orig` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 148,341.0 | 133,921.0 | 384,633.0 | 95,697.6 | 5 |  | compiled=5 |

### `interpretive`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 14,510.0 | 12,870.0 | 45,421.0 | 12,460.8 | 5 |  | compiled=5 |
| `orig` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 13,541.0 | 12,300.0 | 45,080.0 | 12,673.0 | 5 |  | compiled=5 |

