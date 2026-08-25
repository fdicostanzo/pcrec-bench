# pcrec-bench report

reporter: v2 (2026-08-25)

## Query

- filters: subbench=email-specimen
- record source: store/index.tsv (11 candidate file(s))
- records included: 9
    - `email-specimen@0.1__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260825T173402Z` (store/records/email-specimen@0.1/libpcre2_10.46_interp-caps-simdna/email-specimen@0.1__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260825T173402Z.jsonl)
    - `email-specimen@0.1__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260825T174132Z` (store/records/email-specimen@0.1/libpcre2_10.46_jit-caps-simdna/email-specimen@0.1__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260825T174132Z.jsonl)
    - `email-specimen@0.1__pcrec_692c2e8_auto-caps-simdna__budu-ryzen1600__20260825T175131Z` (store/records/email-specimen@0.1/pcrec_692c2e8_auto-caps-simdna/email-specimen@0.1__pcrec_692c2e8_auto-caps-simdna__budu-ryzen1600__20260825T175131Z.jsonl)
    - `email-specimen@0.1__pcrec_692c2e8_auto-nocaps-simdna__budu-ryzen1600__20260825T175534Z` (store/records/email-specimen@0.1/pcrec_692c2e8_auto-nocaps-simdna/email-specimen@0.1__pcrec_692c2e8_auto-nocaps-simdna__budu-ryzen1600__20260825T175534Z.jsonl)
    - `email-specimen@0.1__pcrec_692c2e8_vm-caps-simdna__budu-ryzen1600__20260825T175933Z` (store/records/email-specimen@0.1/pcrec_692c2e8_vm-caps-simdna/email-specimen@0.1__pcrec_692c2e8_vm-caps-simdna__budu-ryzen1600__20260825T175933Z.jsonl)
    - `email-specimen@0.1__pcrec_692c2e8_vm-in-caps-simdna__budu-ryzen1600__20260825T180451Z` (store/records/email-specimen@0.1/pcrec_692c2e8_vm-in-caps-simdna/email-specimen@0.1__pcrec_692c2e8_vm-in-caps-simdna__budu-ryzen1600__20260825T180451Z.jsonl)
    - `email-specimen@0.1__pcrec_8da6120_auto-caps-simdna__budu-ryzen1600__20260825T065046Z` (store/records/email-specimen@0.1/pcrec_8da6120_auto-caps-simdna/email-specimen@0.1__pcrec_8da6120_auto-caps-simdna__budu-ryzen1600__20260825T065046Z.jsonl)
    - `email-specimen@0.1__pcrec_8da6120_auto-nocaps-simdna__budu-ryzen1600__20260825T063943Z` (store/records/email-specimen@0.1/pcrec_8da6120_auto-nocaps-simdna/email-specimen@0.1__pcrec_8da6120_auto-nocaps-simdna__budu-ryzen1600__20260825T063943Z.jsonl)
    - `email-specimen@0.1__pcrec_8da6120_vm-caps-simdna__budu-ryzen1600__20260825T064436Z` (store/records/email-specimen@0.1/pcrec_8da6120_vm-caps-simdna/email-specimen@0.1__pcrec_8da6120_vm-caps-simdna__budu-ryzen1600__20260825T064436Z.jsonl)
- superseded records (OD-B15: older duplicate of a (subbench@version, testee_id, machine); newest kept by default, `--all-records` shows each separately): 2
    - `email-specimen@0.1__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260825T062213Z` superseded by `email-specimen@0.1__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260825T173402Z`
    - `email-specimen@0.1__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260825T062944Z` superseded by `email-specimen@0.1__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260825T174132Z`
- sub-bench version(s): email-specimen@0.1
- machine(s): budu-ryzen1600
- schema version(s): 1.1
- grain: set (sum of per-subject ns/call over the whole subject set, reduced over trials; a set cell is excluded if ANY subject in it fails)
- reduction: median/min/max/stddev (population) over per-trial `elapsed_ns / iterations`; lazy-JIT compile cost is DERIVED as first-match-row-minus-steady-state (lowest `seq` timed row for the pattern, minus the median of every other timed row), one value per (pattern, testee), never pooled with another execution-model class's compile cost
- `form`: this report includes a `whole-subject` artifact beside `plain` for at least one cell (schema v1.1: a testee with no end-anchored mode compiles and times a SEPARATE artifact for match-compliance, e.g. `(?:pattern)\z`, where another testee reaches the same regime via runtime flags on its ordinary artifact) -- shown as a per-row COLUMN, not a split: both forms answer the same regime and RANK TOGETHER in one table (`form` is a key only for compile-cost rows, where a whole-subject artifact is genuinely a separate compile with its own cost); `fact` restates it as 'same program' / 'separate artifact' (R4)
- status policy (OD-B14): a ranking row whose record `status` is not `measured` is excluded from ranking by default, listed under its table as `not ranked: <testee> -- <status> (<status_detail excerpt>)`; `--include-unmeasured` ranks it instead, with `status` shown
- tier policy (R3, schema v1.2 `tier`, absent = `pinned`): a `scratch`-tier row is excluded from ranking by default, listed as `scratch: <testee>`; `--include-scratch` ranks it instead, with a `tier` column
- duplicate-record policy (OD-B15): only the NEWEST record per (subbench@version, testee_id, machine) by `run.timestamp` ranks by default; `--all-records` shows every record as its own row, its testee id suffixed `@<timestamp>`

## Ranking (per pattern x regime, SET grain: sum over the subject set; best median first)

### `factored` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 464,407.8 | 462,303.1 | 474,574.6 | 4,506.4 | 1.000x | 1.000x | 85 | 100% |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,833,523.6 | 1,825,603.4 | 1,870,065.7 | 15,610.2 | 3.948x | 3.948x | 85 | 100% |

- not ranked: `libpcre2_10.46_interp-caps-simdna` — inconclusive-load (iters for (orig, plain, match) = 36076: the median subject would need iters=98116 for 50 ms, capped to 36076 by the 20 s...)
- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `factored` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 15,364.2 | 15,306.0 | 15,389.2 | 27.8 | 1.000x | 1.000x | - | 77 | 199.5 | 100% |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 54,117.6 | 53,402.9 | 54,412.7 | 348.0 | 3.522x | 3.522x | - | 77 | 702.8 | 100% |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 69,537.5 | 68,685.3 | 69,927.0 | 413.5 | 4.526x | 4.526x | faster ×1.19 | 77 | 903.1 | 100% |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 82,438.7 | 81,501.9 | 82,820.4 | 458.8 | 5.366x | 5.366x | - | 77 | 1,070.6 | 100% |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 82,542.8 | 81,246.9 | 84,860.7 | 1,428.5 | 5.372x | 5.372x | - | 77 | 1,072.0 | 100% |
| 6 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 84,075.8 | 81,884.8 | 85,755.1 | 1,234.9 | 5.472x | 5.472x | - | 77 | 1,091.9 | 100% |

_floor: n/a (no floor pattern in this set yet -- pcrecdev1 feedback 1d/repin-2)_

- Δ detail: `pcrec_692c2e8_vm-caps-simdna` vs previous `pcrec_8da6120_vm-caps-simdna`: worst subject `s-029`, 3,345.6 ns, 28 B

- not ranked: `libpcre2_10.46_interp-caps-simdna` — inconclusive-load (iters for (orig, plain, match) = 36076: the median subject would need iters=98116 for 50 ms, capped to 36076 by the 20 s...)
- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `large-subject-throughput` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 9,124,618.5 | 9,088,777.7 | 9,377,921.3 | 108,199.9 | 1.000x | 1.000x | 3 | 100% |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 13,397,524.5 | 13,376,255.0 | 13,464,852.2 | 34,677.2 | 1.468x | 1.468x | 3 | 100% |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 13,419,710.9 | 13,378,803.9 | 13,495,708.0 | 42,286.7 | 1.471x | 1.471x | 3 | 100% |

- not ranked: `libpcre2_10.46_interp-caps-simdna` — inconclusive-load (iters for (orig, plain, match) = 36076: the median subject would need iters=98116 for 50 ms, capped to 36076 by the 20 s...)
- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 62,732.3 | 62,494.7 | 62,927.9 | 152.3 | 1.000x | 1.000x | - |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 80,227.6 | 80,062.2 | 80,517.8 | 159.4 | 1.279x | 1.279x | faster ×1.26 |
| 3 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 100,989.8 | 99,972.5 | 101,276.1 | 455.7 | 1.610x | 1.610x | - |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 234,774.0 | 234,543.1 | 234,978.3 | 179.2 | 3.742x | 3.742x | - |
| 5 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 235,230.3 | 234,913.4 | 236,508.9 | 586.4 | 3.750x | 3.750x | - |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 535,137.9 | 533,912.7 | 547,816.1 | 5,144.2 | 8.531x | 8.531x | - |

- Δ detail: `pcrec_692c2e8_vm-caps-simdna` vs previous `pcrec_8da6120_vm-caps-simdna`: worst subject `s-059`, 13,907.4 ns, 5,134 B

- not ranked: `libpcre2_10.46_interp-caps-simdna` — inconclusive-load (iters for (orig, plain, match) = 36076: the median subject would need iters=98116 for 50 ms, capped to 36076 by the 20 s...)
- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

### `orig` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 6,123.8 | 6,111.3 | 6,274.4 | 61.5 | 1.000x | 1.000x | - | 77 | 79.5 | 100% |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 6,131.1 | 6,118.3 | 6,148.6 | 11.8 | 1.001x | 1.001x | - | 77 | 79.6 | 100% |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 6,135.3 | 6,105.5 | 6,151.9 | 16.0 | 1.002x | 1.002x | - | 77 | 79.7 | 100% |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | measured | `plain` | same program | 12,546.2 | 12,511.8 | 12,629.5 | 43.5 | 2.049x | 2.049x | - | 77 | 162.9 | 100% |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | measured | `plain` | same program | 28,996.9 | 28,809.3 | 30,001.0 | 431.1 | 4.735x | 4.735x | unchanged (within spread) | 77 | 376.6 | 100% |
| 6 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 30,090.3 | 29,227.9 | 31,144.4 | 610.3 | 4.914x | 4.914x | - | 77 | 390.8 | 100% |

_floor: n/a (no floor pattern in this set yet -- pcrecdev1 feedback 1d/repin-2)_

- Δ detail: `pcrec_692c2e8_vm-caps-simdna` vs previous `pcrec_8da6120_vm-caps-simdna`: worst subject `s-035`, 911.3 ns, 16 B

- not ranked: `libpcre2_10.46_interp-caps-simdna` — inconclusive-load (iters for (orig, plain, match) = 36076: the median subject would need iters=98116 for 50 ms, capped to 36076 by the 20 s...)
- not ranked: `pcrec_692c2e8_auto-caps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85165: the median subject would need iters=452694 for 50 ms, capped to 85165 by...)
- not ranked: `pcrec_692c2e8_auto-nocaps-simdna` — inconclusive-load (iters for (orig, whole-subject, match) = 85452: the median subject would need iters=506330 for 50 ms, capped to 85452 by...)

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `factored` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 3 | 67% | 0 | 0 | `t-c-long-atom-run` (timed-out) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_692c2e8_vm-caps-simdna` | 3 | 67% | -2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_692c2e8_vm-in-caps-simdna` | 3 | 67% | -2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_8da6120_auto-caps-simdna` | 3 | 67% | -2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_8da6120_auto-nocaps-simdna` | 3 | 67% | -2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_8da6120_vm-caps-simdna` | 3 | 67% | -2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `match-compliance` | `whole-subject` | `pcrec_692c2e8_vm-caps-simdna` | 85 | 94% | -3:PCREC_ERR_FRAMES×5 (smallest: s-061, 2,008 B) | 0 | `s-058` (gave-up), `s-059` (gave-up), `s-061` (gave-up), `s-063` (gave-up), `s-064` (gave-up) |
| `factored` | `match-compliance` | `whole-subject` | `pcrec_8da6120_auto-caps-simdna` | 85 | 94% | -3:PCREC_ERR_FRAMES×5 (smallest: s-061, 2,008 B) | 0 | `s-058` (gave-up), `s-059` (gave-up), `s-061` (gave-up), `s-063` (gave-up), `s-064` (gave-up) |
| `factored` | `match-compliance` | `whole-subject` | `pcrec_8da6120_auto-nocaps-simdna` | 85 | 94% | -3:PCREC_ERR_FRAMES×5 (smallest: s-061, 2,008 B) | 0 | `s-058` (gave-up), `s-059` (gave-up), `s-061` (gave-up), `s-063` (gave-up), `s-064` (gave-up) |
| `factored` | `match-compliance` | `whole-subject` | `pcrec_8da6120_vm-caps-simdna` | 85 | 94% | -3:PCREC_ERR_FRAMES×5 (smallest: s-061, 2,008 B) | 0 | `s-058` (gave-up), `s-059` (gave-up), `s-061` (gave-up), `s-063` (gave-up), `s-064` (gave-up) |
| `orig` | `large-subject-throughput` | `plain` | `pcrec_692c2e8_vm-caps-simdna` | 3 | 67% | -4:PCREC_ERR_WORK×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `orig` | `large-subject-throughput` | `plain` | `pcrec_692c2e8_vm-in-caps-simdna` | 3 | 67% | -4:PCREC_ERR_WORK×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `orig` | `large-subject-throughput` | `plain` | `pcrec_8da6120_vm-caps-simdna` | 3 | 67% | -4:PCREC_ERR_WORK×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |

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
| `factored` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 36,390.0 | 32,451.0 | 101,331.0 | 26,234.9 | 5 |  | compiled=5 |
| `orig` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 34,781.0 | 30,960.0 | 109,651.0 | 30,239.2 | 5 |  | compiled=5 |

