# pcrec-bench report

reporter: v8 (2026-08-30)

## Query

- filters: include-synthetic
- record source: store/index.tsv (3 candidate file(s))
- records included: 3
    - `fixture-mini@1.0__libpcre2_10.46_interp-caps-simdna__repfix-box__20260825T100500Z` (pcrecbench/tests/fixtures/store/records/fixture-mini@1.0/libpcre2_10.46_interp-caps-simdna/fixture-mini@1.0__libpcre2_10.46_interp-caps-simdna__repfix-box__20260825T100500Z.jsonl)
    - `fixture-mini@1.0__libpcre2_10.46_jit-caps-simdna__repfix-box__20260825T101000Z` (pcrecbench/tests/fixtures/store/records/fixture-mini@1.0/libpcre2_10.46_jit-caps-simdna/fixture-mini@1.0__libpcre2_10.46_jit-caps-simdna__repfix-box__20260825T101000Z.jsonl)
    - `fixture-mini@1.0__pcrec_1.0.0-gdeadbee_vm-caps-simdna__repfix-box__20260825T100000Z` (pcrecbench/tests/fixtures/store/records/fixture-mini@1.0/pcrec_1.0.0-gdeadbee_vm-caps-simdna/fixture-mini@1.0__pcrec_1.0.0-gdeadbee_vm-caps-simdna__repfix-box__20260825T100000Z.jsonl)
- sub-bench version(s): fixture-mini@1.0
- machine(s): repfix-box
- schema version(s): 1.1
- grain: set (sum of per-subject ns/call over the whole subject set, reduced over trials; a set cell is excluded if ANY subject in it fails)
- regime(s) with exactly one subject per pattern (set and subject grain render identically there): `short-subject-search`
- reduction: median/min/max/stddev (population) over per-trial `elapsed_ns / iterations`; lazy-JIT compile cost is DERIVED as first-match-row-minus-steady-state (lowest `seq` timed row for the pattern, minus the median of every other timed row), one value per (pattern, testee), never pooled with another execution-model class's compile cost
- `form`: this report includes a `whole-subject` artifact beside `plain` for at least one cell (schema v1.1: a testee with no end-anchored mode compiles and times a SEPARATE artifact for match-compliance, e.g. `(?:pattern)\z`, where another testee reaches the same regime via runtime flags on its ordinary artifact) -- shown as a per-row COLUMN, not a split: both forms answer the same regime and RANK TOGETHER in one table (`form` is a key only for compile-cost rows, where a whole-subject artifact is genuinely a separate compile with its own cost); `fact` restates it as 'same program' / 'separate artifact' (R4)
- status policy (OD-B14): a ranking row whose record `status` is not `measured` is excluded from ranking by default, listed under its table as `not ranked: <testee> -- <status> (<status_detail excerpt>)`; `--include-unmeasured` ranks it instead, with `status` shown
- tier policy (R3, schema v1.2 `tier`, absent = `pinned`): a `scratch`-tier row is excluded from ranking by default, listed as `scratch: <testee>`; `--include-scratch` ranks it instead, with a `tier` column
- duplicate-record policy (OD-B15, amended 2026-08-25): the NEWEST MEASURED record per (subbench@version, testee_id, machine) ranks by default -- a newer record that is NOT measured does not supersede a measured one of the same testee and version (listed as "newer, not measured" instead); only when no record in the group is measured does the newest record overall stand (itself unranked per the status policy above, unless --include-unmeasured). `--all-records` shows every record as its own row, its testee id suffixed `@<timestamp>`

## Ranking (per pattern x regime, SET grain: sum over the subject set; best median first)

### `p-digits` / `match-compliance` (fixture-mini@1.0) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 20.0 | 19.0 | 21.0 | 0.8 | 0.044x | 1.000x |
| 2 | `pcrec_1.0.0-gdeadbee_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 200.0 | 150.0 | 250.0 | 40.8 | 0.440x | 10.000x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 455.0 | 440.0 | 475.0 | 14.3 | 1.000x | 22.750x |

#### `p-digits` / `match-compliance` per-subject (fixture-mini@1.0)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `s-num-1` | 3 | `libpcre2_10.46_jit-caps-simdna` | 14.0 | 4.6667 |
| `s-num-1` | 3 | `pcrec_1.0.0-gdeadbee_vm-caps-simdna` | 100.0 | 33.3333 |
| `s-num-1` | 3 | `libpcre2_10.46_interp-caps-simdna` | 305.0 | 101.6667 |
| `s-num-2` | 3 | `libpcre2_10.46_jit-caps-simdna` | 6.0 | 2.0000 |
| `s-num-2` | 3 | `pcrec_1.0.0-gdeadbee_vm-caps-simdna` | 90.0 | 30.0000 |
| `s-num-2` | 3 | `libpcre2_10.46_interp-caps-simdna` | 150.0 | 50.0000 |

### `p-digits` / `short-subject-search` (fixture-mini@1.0) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 17.5 | 17.0 | 18.0 | 0.4 | 0.043x | 1.000x | 1 | 17.5 | 100% |
| 2 | `pcrec_1.0.0-gdeadbee_vm-caps-simdna` | measured | `plain` | same program | 150.0 | 148.0 | 152.0 | 1.6 | 0.366x | 8.571x | 1 | 150.0 | 100% |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 410.0 | 405.0 | 415.0 | 4.1 | 1.000x | 23.429x | 1 | 410.0 | 100% |

_floor: n/a (no floor pattern in this set yet -- pcrecdev1 feedback 1d/repin-2)_

#### `p-digits` / `short-subject-search` per-subject (fixture-mini@1.0)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `s-num-1` | 3 | `libpcre2_10.46_jit-caps-simdna` | 17.5 | 5.8333 |
| `s-num-1` | 3 | `pcrec_1.0.0-gdeadbee_vm-caps-simdna` | 150.0 | 50.0000 |
| `s-num-1` | 3 | `libpcre2_10.46_interp-caps-simdna` | 410.0 | 136.6667 |

### `p-word` / `match-compliance` (fixture-mini@1.0) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1.0.0-gdeadbee_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 96.0 | 95.0 | 97.0 | 0.8 | 1.000x | 1.000x | 1 | 100% |

#### `p-word` / `match-compliance` per-subject (fixture-mini@1.0)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `s-word-1` | 3 | `pcrec_1.0.0-gdeadbee_vm-caps-simdna` | 96.0 | 32.0000 |

### `p-word` / `short-subject-search` (fixture-mini@1.0) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1.0.0-gdeadbee_vm-caps-simdna` | measured | `plain` | same program | 800.0 | 790.0 | 820.0 | 12.5 | 0.444x | 1.000x | 1 | 800.0 | 100% |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,800.0 | 1,790.0 | 1,820.0 | 12.5 | 1.000x | 2.250x | 1 | 1,800.0 | 100% |

_floor: n/a (no floor pattern in this set yet -- pcrecdev1 feedback 1d/repin-2)_

#### `p-word` / `short-subject-search` per-subject (fixture-mini@1.0)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `s-mix-set` | 40 | `pcrec_1.0.0-gdeadbee_vm-caps-simdna` | 800.0 | 20.0000 |
| `s-mix-set` | 40 | `libpcre2_10.46_interp-caps-simdna` | 1,800.0 | 45.0000 |

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `p-word` | `match-compliance` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 2 | 0% | pcre2: PCRE2_ERROR_MATCHLIMIT (match limit exceeded) -- FIXTURE×1 (smallest: s-give-up-1, 3 B) | 3 | `s-give-up-1` (gave-up), `s-word-1` (wrong) |

## Compile cost (by execution-model class; never pooled across classes)

### `compiled-aot`

- `pcrec_1.0.0-gdeadbee_vm-caps-simdna`: engine=vm, entry=plain entry, vm_prefilter=-, dfa: n/s (no abi pair: cannot say which absence this is), rungs=-, fast tier=n/s (no abi pair), buffers=n/s, frame=n/s
    - (identical on all 4 (pattern, form) cells of this testee)

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes | emit-c ns | gcc ns | load ns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `p-digits` | `plain` | `pcrec_1.0.0-gdeadbee_vm-caps-simdna` | 22,020,000.0 | 21,831,000.0 | 22,314,500.0 | 198,948.2 | 3 | 40,960 | 0.009 | compiled=3 | 120,000.0 | 21,000,000.0 | 900,000.0 |
| `p-digits` | `whole-subject` | `pcrec_1.0.0-gdeadbee_vm-caps-simdna` | 26,090,000.0 | 25,894,000.0 | 26,389,000.0 | 203,536.0 | 3 | 41,472 | 0.008 | compiled=3 | 140,000.0 | 25,000,000.0 | 950,000.0 |
| `p-word` | `plain` | `pcrec_1.0.0-gdeadbee_vm-caps-simdna` | 21,617,500.0 | 21,523,000.0 | 21,720,500.0 | 80,653.9 | 3 | 40,960 | 0.004 | compiled=3 | 118,000.0 | 20,600,000.0 | 902,000.0 |
| `p-word` | `whole-subject` | `pcrec_1.0.0-gdeadbee_vm-caps-simdna` | 25,679,500.0 | 25,578,000.0 | 25,783,500.0 | 83,897.1 | 3 | 41,472 | 0.003 | compiled=3 | 138,000.0 | 24,600,000.0 | 942,000.0 |

### `eager-jit`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `p-digits` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 4,900,000.0 | 4,870,000.0 | 4,950,000.0 | 32,998.3 | 3 | - | 0.007 | compiled=3 |
| `p-word` | `plain` | `libpcre2_10.46_jit-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |

### `interpretive`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `p-digits` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 5,100,000.0 | 4,900,000.0 | 5,300,000.0 | 163,299.3 | 3 | - | 0.032 | compiled=3 |
| `p-word` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 5,100,000.0 | 4,900,000.0 | 5,300,000.0 | 163,299.3 | 3 | - | 0.032 | compiled=3 |

