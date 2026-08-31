# pcrec-bench report

reporter: v10 (2026-08-31)

## Query

- filters: subbench=email-specimen, until=2026-08-25T07:00:00Z
- record source: store/index.tsv (68 candidate file(s))
- records included: 5
    - `email-specimen@0.1__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260825T062213Z` (store/records/email-specimen@0.1/libpcre2_10.46_interp-caps-simdna/email-specimen@0.1__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260825T062213Z.jsonl) — agreement: n/a (v1.1)
    - `email-specimen@0.1__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260825T062944Z` (store/records/email-specimen@0.1/libpcre2_10.46_jit-caps-simdna/email-specimen@0.1__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260825T062944Z.jsonl) — agreement: n/a (v1.1)
    - `email-specimen@0.1__pcrec_8da6120_auto-caps-simdna__budu-ryzen1600__20260825T065046Z` (store/records/email-specimen@0.1/pcrec_8da6120_auto-caps-simdna/email-specimen@0.1__pcrec_8da6120_auto-caps-simdna__budu-ryzen1600__20260825T065046Z.jsonl) — agreement: n/a (v1.1)
    - `email-specimen@0.1__pcrec_8da6120_auto-nocaps-simdna__budu-ryzen1600__20260825T063943Z` (store/records/email-specimen@0.1/pcrec_8da6120_auto-nocaps-simdna/email-specimen@0.1__pcrec_8da6120_auto-nocaps-simdna__budu-ryzen1600__20260825T063943Z.jsonl) — agreement: n/a (v1.1)
    - `email-specimen@0.1__pcrec_8da6120_vm-caps-simdna__budu-ryzen1600__20260825T064436Z` (store/records/email-specimen@0.1/pcrec_8da6120_vm-caps-simdna/email-specimen@0.1__pcrec_8da6120_vm-caps-simdna__budu-ryzen1600__20260825T064436Z.jsonl) — agreement: n/a (v1.1)
- sub-bench version(s): email-specimen@0.1
- machine(s): budu-ryzen1600
- schema version(s): 1.1
- grain: set (sum of per-subject ns/call over the whole subject set, reduced over trials; a set cell is excluded if ANY subject in it fails)
- reduction: median/min/max/stddev (population) over per-trial `elapsed_ns / iterations`; lazy-JIT compile cost is DERIVED as first-match-row-minus-steady-state (lowest `seq` timed row for the pattern, minus the median of every other timed row), one value per (pattern, testee), never pooled with another execution-model class's compile cost
- `form`: this report includes a `whole-subject` artifact beside `plain` for at least one cell (schema v1.1: a testee with no end-anchored mode compiles and times a SEPARATE artifact for match-compliance, e.g. `(?:pattern)\z`, where another testee reaches the same regime via runtime flags on its ordinary artifact) -- shown as a per-row COLUMN, not a split: both forms answer the same regime and RANK TOGETHER in one table (`form` is a key only for compile-cost rows, where a whole-subject artifact is genuinely a separate compile with its own cost); `fact` restates it as 'same program' / 'separate artifact' (R4)
- status policy (OD-B14): a ranking row whose record `status` is not `measured` is excluded from ranking by default, listed under its table as `not ranked: <testee> -- <status> (<status_detail excerpt>)`; `--include-unmeasured` ranks it instead, with `status` shown
- trial-agreement policy (schema v1.4, rule v1.4-group, X31-X33): a record's five trials must agree to within k=1.5 on every group of its rows — one slow trial of five tolerated; two, or one fast, is a disagreeing row; a group disagrees at >= 2 disagreeing rows reaching a third of it (d_min=2, c=3); a record with a disagreeing group, or with fewer than five odd trials, is `inconclusive-spread` and unranked like `inconclusive-load`; the after-run load/occupancy samples are provenance (v1.4 X13), shown under --include-provenance
- status rule: v1.1-1.3 X13 (both samples quiet) on 5 record(s)
- tier policy (R3, schema v1.2 `tier`, absent = `pinned`): a `scratch`-tier row is excluded from ranking by default, listed as `scratch: <testee>`; `--include-scratch` ranks it instead, with a `tier` column
- duplicate-record policy (OD-B15, amended 2026-08-25): the NEWEST MEASURED record per (subbench@version, testee_id, machine) ranks by default -- a newer record that is NOT measured does not supersede a measured one of the same testee and version (listed as "newer, not measured" instead); only when no record in the group is measured does the newest record overall stand (itself unranked per the status policy above, unless --include-unmeasured). `--all-records` shows every record as its own row, its testee id suffixed `@<timestamp>`

## Ranking (per pattern x regime, SET grain: sum over the subject set; best median first)

### `factored` / `large-subject-throughput` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 51,887,584.9 | 16.4946 | 51,715,536.7 | 52,400,309.6 | 237,758.7 | 1.000x | 1.000x | **dominated**: `t-a-valid-addrs` is 99.9% of this set | 3 | 100% |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `factored` / `large-subject-throughput` per-subject (email-specimen@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 51,851,980.0 | 49.4499 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,812.2 | 0.0170 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,809.6 | 0.0170 |

### `factored` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,838,131.4 | 1,834,292.9 | 1,867,343.0 | 12,430.8 | 0.993x | 1.000x | 85 | 100% |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,851,831.7 | 1,833,210.9 | 1,882,042.5 | 16,258.5 | 1.000x | 1.007x | 85 | 100% |

### `factored` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 15,356.9 | 15,283.3 | 15,555.6 | 93.0 | 0.110x | 1.000x | 77 | 199.4 | 100% |
| 2 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 82,438.7 | 81,501.9 | 82,820.4 | 458.8 | 0.591x | 5.368x | 77 | 1,070.6 | 100% |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 82,542.8 | 81,246.9 | 84,860.7 | 1,428.5 | 0.592x | 5.375x | 77 | 1,072.0 | 100% |
| 4 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 84,075.8 | 81,884.8 | 85,755.1 | 1,234.9 | 0.603x | 5.475x | 77 | 1,091.9 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 139,473.0 | 137,977.7 | 142,462.1 | 1,654.9 | 1.000x | 9.082x | 77 | 1,811.3 | 100% |

_floor: n/a (no floor pattern in this set yet -- pcrecdev1 feedback 1d/repin-2)_

### `orig` / `large-subject-throughput` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 9,080,736.7 | 2.8867 | 9,007,571.8 | 9,110,169.7 | 36,680.6 | 0.315x | 1.000x | spread | 3 | 100% |
| 2 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 13,397,524.5 | 4.2590 | 13,376,255.0 | 13,464,852.2 | 34,677.2 | 0.464x | 1.475x | spread | 3 | 100% |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 13,419,710.9 | 4.2660 | 13,378,803.9 | 13,495,708.0 | 42,286.7 | 0.465x | 1.478x | spread | 3 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 28,855,145.7 | 9.1728 | 28,771,996.2 | 29,202,089.1 | 156,956.7 | 1.000x | 3.178x | **dominated**: `t-a-valid-addrs` is 99.9% of this set | 3 | 100% |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `orig` / `large-subject-throughput` per-subject (email-specimen@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 3,693,007.3 | 3.5219 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_8da6120_auto-caps-simdna` | 6,546,199.3 | 6.2429 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_8da6120_auto-nocaps-simdna` | 6,542,380.1 | 6.2393 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 28,819,359.7 | 27.4843 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 2,566,034.8 | 2.4472 |
| `t-b-no-at` | 1,048,576 | `pcrec_8da6120_auto-caps-simdna` | 3,428,525.6 | 3.2697 |
| `t-b-no-at` | 1,048,576 | `pcrec_8da6120_auto-nocaps-simdna` | 3,433,874.3 | 3.2748 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,772.8 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 2,828,833.6 | 2.6978 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_8da6120_auto-caps-simdna` | 3,422,799.6 | 3.2642 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_8da6120_auto-nocaps-simdna` | 3,424,102.3 | 3.2655 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,792.2 | 0.0170 |

### `orig` / `match-compliance` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 100,989.8 | 99,972.5 | 101,276.1 | 455.7 | 0.188x | 1.000x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 234,774.0 | 234,543.1 | 234,978.3 | 179.2 | 0.437x | 2.325x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 235,230.3 | 234,913.4 | 236,508.9 | 586.4 | 0.438x | 2.329x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 536,225.9 | 535,003.5 | 538,779.0 | 1,231.3 | 0.998x | 5.310x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 537,486.9 | 535,808.3 | 545,853.0 | 3,695.2 | 1.000x | 5.322x |

### `orig` / `short-subject-search` (email-specimen@0.1) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | measured | `plain` | same program | 6,131.1 | 6,118.3 | 6,148.6 | 11.8 | 0.093x | 1.000x | 77 | 79.6 | 100% |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | measured | `plain` | same program | 6,135.3 | 6,105.5 | 6,151.9 | 16.0 | 0.093x | 1.001x | 77 | 79.7 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 6,276.7 | 6,174.2 | 6,828.3 | 242.4 | 0.096x | 1.024x | 77 | 81.5 | 100% |
| 4 | `pcrec_8da6120_vm-caps-simdna` | measured | `plain` | same program | 30,090.3 | 29,227.9 | 31,144.4 | 610.3 | 0.458x | 4.908x | 77 | 390.8 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 65,681.7 | 65,504.1 | 66,190.9 | 292.3 | 1.000x | 10.713x | 77 | 853.0 | 100% |

_floor: n/a (no floor pattern in this set yet -- pcrecdev1 feedback 1d/repin-2)_

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `factored` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 3 | 67% | 0 | 0 | `t-c-long-atom-run` (timed-out) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_8da6120_auto-caps-simdna` | 3 | 67% | -2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_8da6120_auto-nocaps-simdna` | 3 | 67% | -2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_8da6120_vm-caps-simdna` | 3 | 67% | -2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `match-compliance` | `whole-subject` | `pcrec_8da6120_auto-caps-simdna` | 85 | 94% | -3:PCREC_ERR_FRAMES×5 (smallest: s-061, 2,008 B) | 0 | `s-058` (gave-up), `s-059` (gave-up), `s-061` (gave-up), `s-063` (gave-up), `s-064` (gave-up) |
| `factored` | `match-compliance` | `whole-subject` | `pcrec_8da6120_auto-nocaps-simdna` | 85 | 94% | -3:PCREC_ERR_FRAMES×5 (smallest: s-061, 2,008 B) | 0 | `s-058` (gave-up), `s-059` (gave-up), `s-061` (gave-up), `s-063` (gave-up), `s-064` (gave-up) |
| `factored` | `match-compliance` | `whole-subject` | `pcrec_8da6120_vm-caps-simdna` | 85 | 94% | -3:PCREC_ERR_FRAMES×5 (smallest: s-061, 2,008 B) | 0 | `s-058` (gave-up), `s-059` (gave-up), `s-061` (gave-up), `s-063` (gave-up), `s-064` (gave-up) |
| `orig` | `large-subject-throughput` | `plain` | `pcrec_8da6120_vm-caps-simdna` | 3 | 67% | -4:PCREC_ERR_WORK×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |

## Compile cost (by execution-model class; never pooled across classes)

### `compiled-aot`

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
| `factored` | `plain` | `pcrec_8da6120_auto-caps-simdna` | 420,465,289.0 | 414,985,073.0 | 428,903,342.0 | 4,893,507.9 | 5 | 25,128 | 0.012 (max is trial 1) | compiled=5 | 1,880,342.0 | 418,531,336.0 | 110,891.0 |
| `factored` | `whole-subject` | `pcrec_8da6120_auto-caps-simdna` | 430,387,601.0 | 417,874,860.0 | 443,938,027.0 | 8,743,376.0 | 5 | 25,128 | 0.020 | compiled=5 | 1,903,072.0 | 428,382,468.0 | 199,551.0 |
| `factored` | `plain` | `pcrec_8da6120_auto-nocaps-simdna` | 427,493,516.0 | 422,008,523.0 | 434,926,485.0 | 4,492,879.1 | 5 | 25,128 | 0.011 | compiled=5 | 3,458,012.0 | 423,761,643.0 | 190,832.0 |
| `factored` | `whole-subject` | `pcrec_8da6120_auto-nocaps-simdna` | 420,974,905.0 | 413,095,565.0 | 432,864,330.0 | 7,311,852.8 | 5 | 25,128 | 0.017 | compiled=5 | 1,773,151.0 | 419,081,683.0 | 189,551.0 |
| `factored` | `plain` | `pcrec_8da6120_vm-caps-simdna` | 424,762,944.0 | 423,664,078.0 | 432,708,304.0 | 3,362,545.9 | 5 | 25,128 | 0.008 | compiled=5 | 1,716,071.0 | 422,822,902.0 | 193,901.0 |
| `factored` | `whole-subject` | `pcrec_8da6120_vm-caps-simdna` | 427,987,625.0 | 424,012,201.0 | 439,228,106.0 | 5,642,429.0 | 5 | 25,128 | 0.013 | compiled=5 | 1,699,401.0 | 426,211,414.0 | 190,301.0 |
| `orig` | `plain` | `pcrec_8da6120_auto-caps-simdna` | 118,056,825.0 | 103,621,896.0 | 120,772,314.0 | 6,366,891.3 | 5 | 29,232 | 0.054 | compiled=5 | 7,414,687.0 | 110,543,728.0 | 98,410.0 |
| `orig` | `whole-subject` | `pcrec_8da6120_auto-caps-simdna` | 117,555,053.0 | 109,696,744.0 | 130,533,016.0 | 9,212,004.5 | 5 | 33,424 | 0.078 | compiled=5 | 9,605,031.0 | 107,535,020.0 | 194,121.0 |
| `orig` | `plain` | `pcrec_8da6120_auto-nocaps-simdna` | 113,739,182.0 | 110,959,754.0 | 143,108,420.0 | 11,988,842.7 | 5 | 29,232 | 0.105 | compiled=5 | 7,620,208.0 | 106,465,166.0 | 107,390.0 |
| `orig` | `whole-subject` | `pcrec_8da6120_auto-nocaps-simdna` | 135,300,201.0 | 122,043,665.0 | 137,739,956.0 | 6,730,911.2 | 5 | 33,424 | 0.050 (max is trial 1) | compiled=5 | 19,767,436.0 | 115,433,954.0 | 101,750.0 |
| `orig` | `plain` | `pcrec_8da6120_vm-caps-simdna` | 382,875,770.0 | 372,878,556.0 | 389,967,264.0 | 6,557,411.6 | 5 | 25,088 | 0.017 | compiled=5 | 1,976,132.0 | 380,961,488.0 | 196,851.0 |
| `orig` | `whole-subject` | `pcrec_8da6120_vm-caps-simdna` | 374,587,618.0 | 362,494,710.0 | 389,369,562.0 | 9,692,150.1 | 5 | 25,088 | 0.026 | compiled=5 | 2,358,745.0 | 372,141,432.0 | 101,580.0 |

### `eager-jit`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 69,630.0 | 64,000.0 | 168,531.0 | 39,793.8 | 5 | 951 | 0.572 (max is trial 1) | compiled=5 |
| `orig` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 159,291.0 | 144,641.0 | 396,882.0 | 95,332.9 | 5 | 1,609 | 0.598 (max is trial 1) | compiled=5 |

### `interpretive`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 14,510.0 | 12,870.0 | 45,421.0 | 12,460.8 | 5 | 951 | timer-floor (max is trial 1) | compiled=5 |
| `orig` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 13,541.0 | 12,300.0 | 45,080.0 | 12,673.0 | 5 | 1,609 | timer-floor (max is trial 1) | compiled=5 |

