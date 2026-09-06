# pcrec-bench report

reporter: v15 (2026-09-05)

## Query

- filters: subbench=email-specimen, version=0.2, since=2026-09-06T19:00:00Z, until=2026-09-06T19:15:00Z, testee=pcrec_d34c9131_auto-caps-simdna, testee=pcrec_d34c9131_auto-caps-simdna_noclsfold
- record source: store/index.tsv (2 record(s) matching this query)
- records included: 2
- worst other-core busy: 2.0% (`pcrec_d34c9131_auto-caps-simdna_noclsfold` / `factored` / `match-compliance`)
    - `email-specimen@0.2__pcrec_d34c9131_auto-caps-simdna__budu-ryzen1600__20260906T190251Z` (store/records/email-specimen@0.2/pcrec_d34c9131_auto-caps-simdna/email-specimen@0.2__pcrec_d34c9131_auto-caps-simdna__budu-ryzen1600__20260906T190251Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_d34c9131_auto-caps-simdna_noclsfold__budu-ryzen1600__20260906T190801Z` (store/records/email-specimen@0.2/pcrec_d34c9131_auto-caps-simdna_noclsfold/email-specimen@0.2__pcrec_d34c9131_auto-caps-simdna_noclsfold__budu-ryzen1600__20260906T190801Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
- sub-bench version(s): email-specimen@0.2
- machine(s): budu-ryzen1600
- schema version(s): 1.5
- grain: set (sum of per-subject ns/call over the whole subject set, reduced over trials; a set cell is excluded if ANY subject in it fails)
- reduction: median/min/max/stddev (population) over per-trial `elapsed_ns / iterations`; lazy-JIT compile cost is DERIVED as first-match-row-minus-steady-state (lowest `seq` timed row for the pattern, minus the median of every other timed row), one value per (pattern, testee), never pooled with another execution-model class's compile cost
- `form`: this report includes a `whole-subject` artifact beside `plain` for at least one cell (schema v1.1: a testee with no end-anchored mode compiles and times a SEPARATE artifact for match-compliance, e.g. `(?:pattern)\z`, where another testee reaches the same regime via runtime flags on its ordinary artifact) -- shown as a per-row COLUMN, not a split: both forms answer the same regime and RANK TOGETHER in one table (`form` is a key only for compile-cost rows, where a whole-subject artifact is genuinely a separate compile with its own cost); `fact` restates it as 'same program' / 'separate artifact' (R4)
- status policy (OD-B14): a ranking row whose record `status` is not `measured` is excluded from ranking by default, listed under its table as `not ranked: <testee> -- <status> (<status_detail excerpt>)`; `--include-unmeasured` ranks it instead, with `status` shown
- trial-agreement policy (schema v1.4, rule v1.4-group, X31-X33): a record's five trials must agree to within k=1.5 on every group of its rows — one slow trial of five tolerated; two, or one fast, is a disagreeing row; a group disagrees at >= 2 disagreeing rows reaching a third of it (d_min=2, c=3); a record with a disagreeing group, or with fewer than five odd trials, is `inconclusive-spread` and unranked like `inconclusive-load`; the after-run load/occupancy samples are provenance (v1.4 X13), shown under --include-provenance
- status rule: v1.4 X13 (pre-flight + trial agreement) on 2 record(s)
- tier policy (R3, schema v1.2 `tier`, absent = `pinned`): a `scratch`-tier row is excluded from ranking by default, listed as `scratch: <testee>`; `--include-scratch` ranks it instead, with a `tier` column
- duplicate-record policy (OD-B15, amended 2026-08-25): the NEWEST MEASURED record per (subbench@version, testee_id, machine) ranks by default -- a newer record that is NOT measured does not supersede a measured one of the same testee and version (listed as "newer, not measured" instead); only when no record in the group is measured does the newest record overall stand (itself unranked per the status policy above, unless --include-unmeasured). `--all-records` shows every record as its own row, its testee id suffixed `@<timestamp>`

## Ranking (per pattern x regime, SET grain: sum over the subject set; best median first)

### `factored` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 13,676,206.1 | 2.6085 | 13,658,410.5 | 13,740,603.5 | 31,219.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 13,713,507.1 | 2.6156 | 13,689,266.9 | 13,753,200.4 | 23,794.8 | 1.003x | 1.003x |

#### `factored` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 3,586,692.1 | 3.4205 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | 3,588,392.8 | 3.4222 |
| `t-b-no-at` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 1,875,347.2 | 1.7885 |
| `t-b-no-at` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | 1,875,111.5 | 1.7882 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 1,875,174.1 | 1.7883 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | 1,875,762.8 | 1.7889 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 3,192,965.9 | 3.0450 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | 3,201,787.2 | 3.0535 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 3,152,957.6 | 3.0069 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | 3,154,581.3 | 3.0084 |

### `factored` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,303.5 | 73,290.6 | 73,322.0 | 11.5 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 73,309.1 | 73,285.9 | 73,399.5 | 49.0 | 1.000x | 1.000x |

### `factored` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 3,662.4 | 3,660.4 | 3,669.2 | 3.1 | 1.000x | 1.000x | 77 | 47.6 | 17.4 | 100% |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 3,669.2 | 3,667.2 | 3,742.7 | 29.3 | 1.002x | 1.002x | 77 | 47.7 | 17.5 | 100% |

### `floor` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 711,558.5 | 0.1357 | 711,179.0 | 712,627.6 | 523.3 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 713,690.6 | 0.1361 | 711,392.5 | 714,486.3 | 1,256.0 | 1.003x | 1.003x |

#### `floor` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | 627,608.5 | 0.5985 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 628,059.0 | 0.5990 |
| `t-b-no-at` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | 17,712.9 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 17,667.6 | 0.0168 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | 17,699.6 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 17,649.3 | 0.0168 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | 30,716.9 | 0.0293 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 30,949.2 | 0.0295 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | 17,703.9 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 17,671.8 | 0.0169 |

### `floor` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 870.5 | 858.7 | 887.1 | 10.0 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 875.6 | 869.4 | 884.9 | 5.0 | 1.006x | 1.006x |

### `floor` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 1,338.1 | 1,337.9 | 1,348.7 | 4.3 | 1.000x | 1.000x | 77 | 17.4 | 100% |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 1,344.6 | 1,341.1 | 1,375.1 | 14.1 | 1.005x | 1.005x | 77 | 17.5 | 100% |

### `orig` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 13,596,186.2 | 2.5933 | 13,552,434.1 | 13,627,695.7 | 29,055.1 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 13,600,760.9 | 2.5941 | 13,561,534.8 | 13,621,913.4 | 22,663.1 | 1.000x | 1.000x |

#### `orig` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 3,578,393.8 | 3.4126 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | 3,584,760.9 | 3.4187 |
| `t-b-no-at` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 1,885,944.5 | 1.7986 |
| `t-b-no-at` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | 1,888,684.0 | 1.8012 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 1,874,971.6 | 1.7881 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | 1,875,623.9 | 1.7887 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 3,154,491.2 | 3.0084 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | 3,142,869.4 | 2.9973 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 3,095,320.2 | 2.9519 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | 3,097,970.9 | 2.9545 |

### `orig` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,208.6 | 73,199.3 | 73,292.6 | 34.9 | 1.000x | 1.000x |
| 2 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `whole-subject` | separate artifact | 73,222.4 | 73,215.1 | 73,334.9 | 45.5 | 1.000x | 1.000x |

### `orig` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | measured | `plain` | same program | 3,524.6 | 3,523.5 | 3,527.0 | 1.2 | 1.000x | 1.000x | 77 | 45.8 | 17.5 | 100% |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 3,527.0 | 3,524.4 | 3,541.1 | 5.9 | 1.001x | 1.001x | 77 | 45.8 | 17.4 | 100% |

## Compile cost (by execution-model class; never pooled across classes)

### `compiled-aot`

- `pcrec_d34c9131_auto-caps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d34c9131_auto-caps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d34c9131_auto-caps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d34c9131_auto-caps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d34c9131_auto-caps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d34c9131_auto-caps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d34c9131_auto-caps-simdna_noclsfold` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d34c9131_auto-caps-simdna_noclsfold` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d34c9131_auto-caps-simdna_noclsfold` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d34c9131_auto-caps-simdna_noclsfold` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d34c9131_auto-caps-simdna_noclsfold` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d34c9131_auto-caps-simdna_noclsfold` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
    - sel = pcrec's `RX_ENGINE_SEL`; `DFA fallback tripped` = sel not in (selected, forced), and NOTHING else -- since pcrec 263b013 ([LIM-1] / [OPT-4.1]) every fallback has its own token (`overflowed-dfa`, `overflowed-prefilter`, `collapsed-prefilter`, `declined-nullable`, `size-cap-retry`), the size-cap rescue included; at pcrec 96e44c2 that rescue stamped `sel=selected` and only its `lang=count-collapsed (size cap retry, ...)` clause says so.
    - edge = pcrec's `RX_DFA_SCAN_EDGE` ([OPT-5] STEP 1, abi 13+), how a DFA scan tests a SCAN EDGE's byte class: `range` = a contiguous run (subtract-and-compare against two immediates); `bitmap` = a non-contiguous class (a 256-byte membership read); `mixed` = one artifact whose machines took both forms; `none` = no collapsible run (an attempt/empty scan, or -fno-scan-edge).
    - edges = pcrec's `scan_edges` ([B32]): how many [OPT-5] SCAN EDGES this artifact's SEARCH-side machines carry (`rx_search`/`rx_prefilter`), the per-scan-iteration compare-count covariate `edge`'s single shape token cannot separate (I-33: the cost is one compare per edge per iteration); the `(match: M)` parenthetical, when carried, is the SAME count on the anchored `rx_match` machine, kept apart because the measured [OPT-EDGE] regression is search-band only. `0` is a real, recorded value.
    - start = pcrec's `RX_DFA_START` ([OPT-5] STEP 2, abi 16+), how the SEARCH entry recovers the match START: `pinned` = the forward machine's start state accepts unconditionally, so the match provably begins at `search_from` and THE ARTIFACT CARRIES NO REVERSE MACHINE at all (no reverse tables, accessor block or scan loop); `reverse-pass` = it carries one and walks it backwards from the match end. The two forms are ANSWER-IDENTICAL by contract -- `caps[0][0]`'s absolute offsets and the zero-length-match convention hold under both -- so this explains a row's SIZE and pass count, never its answer.
    - folds = pcrec's `RX_DFA_UNIFORM_FOLDS` ([CC-DIFF] STEP 1, abi 17+): how many of this artifact's DFA tables (two per machine it contains -- forward always, reverse unless `start=pinned`, anchored under `match=unwrapped`; so 0..6) had ALL-EQUAL cells and were NOT EMITTED, the accessor returning the constant. `table=` keeps naming the encoding that was SELECTED, so `premultiplied` beside `folds=4` is an artifact carrying NO transition table at all -- a SIZE fact, never an answer one. `0` is a real, recorded value.

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | emit bytes | code bytes | jitter | outcomes | emit-c ns | gcc ns | load ns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `pcrec_d34c9131_auto-caps-simdna` | 164,584,146.0 | 163,200,287.0 | 172,326,812.0 | 3,438,404.2 | 5 | 48,128 | 82,455 | 13,761 | 0.021 | compiled=5 | 9,866,191.0 | 154,496,783.0 | 194,071.0 |
| `factored` | `whole-subject` | `pcrec_d34c9131_auto-caps-simdna` | 183,590,851.0 | 175,932,235.0 | 194,146,927.0 | 6,021,076.8 | 5 | 48,264 | 94,666 | 15,677 | 0.033 | compiled=5 | 12,225,066.0 | 171,279,445.0 | 198,781.0 |
| `factored` | `plain` | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | 170,074,877.0 | 165,574,461.0 | 174,532,136.0 | 2,846,142.2 | 5 | 48,128 | 82,455 | 13,761 | 0.017 | compiled=5 | 9,801,310.0 | 160,084,886.0 | 187,742.0 |
| `factored` | `whole-subject` | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | 182,524,996.0 | 175,200,711.0 | 198,241,271.0 | 8,554,213.3 | 5 | 48,264 | 94,666 | 15,677 | 0.047 | compiled=5 | 22,588,480.0 | 170,146,669.0 | 206,802.0 |
| `floor` | `plain` | `pcrec_d34c9131_auto-caps-simdna` | 146,925,846.0 | 134,069,456.0 | 156,562,775.0 | 7,227,152.4 | 5 | 27,608 | 18,106 | 13,109 | 0.049 | compiled=5 | 1,805,321.0 | 144,978,534.0 | 192,931.0 |
| `floor` | `whole-subject` | `pcrec_d34c9131_auto-caps-simdna` | 158,953,769.0 | 153,090,875.0 | 161,812,987.0 | 3,417,763.5 | 5 | 27,752 | 20,449 | 15,126 | 0.022 | compiled=5 | 1,819,561.0 | 155,299,577.0 | 213,442.0 |
| `floor` | `plain` | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | 148,633,036.0 | 147,345,037.0 | 151,042,141.0 | 1,583,378.4 | 5 | 27,608 | 18,106 | 13,109 | 0.011 | compiled=5 | 1,795,791.0 | 145,452,277.0 | 114,060.0 |
| `floor` | `whole-subject` | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | 161,162,234.0 | 145,941,900.0 | 166,267,634.0 | 8,444,775.9 | 5 | 27,752 | 20,449 | 15,126 | 0.052 | compiled=5 | 1,712,380.0 | 157,287,510.0 | 188,592.0 |
| `orig` | `plain` | `pcrec_d34c9131_auto-caps-simdna` | 166,883,659.0 | 162,455,282.0 | 173,020,587.0 | 4,309,592.0 | 5 | 48,088 | 82,048 | 13,521 | 0.026 | compiled=5 | 9,496,359.0 | 154,801,744.0 | 195,231.0 |
| `orig` | `whole-subject` | `pcrec_d34c9131_auto-caps-simdna` | 178,790,732.0 | 164,688,805.0 | 180,042,050.0 | 5,996,848.9 | 5 | 48,224 | 94,259 | 15,437 | 0.034 (max is trial 1) | compiled=5 | 11,568,361.0 | 159,379,703.0 | 108,781.0 |
| `orig` | `plain` | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | 165,923,203.0 | 156,281,823.0 | 183,938,554.0 | 9,847,499.8 | 5 | 48,088 | 82,048 | 13,521 | 0.059 | compiled=5 | 9,461,649.0 | 156,327,034.0 | 192,201.0 |
| `orig` | `whole-subject` | `pcrec_d34c9131_auto-caps-simdna_noclsfold` | 180,745,944.0 | 172,905,155.0 | 187,029,724.0 | 6,048,317.3 | 5 | 48,224 | 94,259 | 15,437 | 0.033 | compiled=5 | 11,567,211.0 | 163,322,697.0 | 108,100.0 |

