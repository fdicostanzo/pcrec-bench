# pcrec-bench report

reporter: v28 (2026-10-25)

## Query

- filters: subbench=capability, version=0.4, machine=ryzen7700x, since=2026-11-01T00:00:00Z, until=2026-11-03T00:00:00Z, testee=pcrec_cb32eda28_auto-caps-simdna, testee=pcrec_cb32eda28_auto-caps-simdna_noedge
- record source: store/index.tsv (2 record(s) matching this query)
- records included: 2
- worst other-core busy: 47.06% (`pcrec_cb32eda28_auto-caps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `large-subject-throughput`)
    - `capability@0.4__pcrec_cb32eda28_auto-caps-simdna__ryzen7700x__20261101T133920Z` (store/records/capability@0.4/pcrec_cb32eda28_auto-caps-simdna/capability@0.4__pcrec_cb32eda28_auto-caps-simdna__ryzen7700x__20261101T133920Z.jsonl) — agreement: agree (0 of 138 groups; 10 of 6481 rows; 5 unjudged; k=1.5, 2/3; 5 trials); after: occ 10.10%
    - `capability@0.4__pcrec_cb32eda28_auto-caps-simdna_noedge__ryzen7700x__20261102T150243Z` (store/records/capability@0.4/pcrec_cb32eda28_auto-caps-simdna_noedge/capability@0.4__pcrec_cb32eda28_auto-caps-simdna_noedge__ryzen7700x__20261102T150243Z.jsonl) — agreement: agree (0 of 138 groups; 2 of 6481 rows; 5 unjudged; k=1.5, 2/3; 5 trials); after: load1 2.20
- sub-bench version(s): capability@0.4
- machine(s): ryzen7700x
- schema version(s): 1.11
- grain: set (sum of per-subject ns/call over the whole subject set, reduced over trials; a set cell is excluded if ANY subject in it fails)
- reduction: median/min/max/stddev (population) over per-trial `elapsed_ns / iterations`; lazy-JIT compile cost is DERIVED as first-match-row-minus-steady-state (lowest `seq` timed row for the pattern, minus the median of every other timed row), one value per (pattern, testee), never pooled with another execution-model class's compile cost
- `form`: this report includes a `whole-subject` artifact beside `plain` for at least one cell (schema v1.1: a testee with no end-anchored mode compiles and times a SEPARATE artifact for match-compliance, e.g. `(?:pattern)\z`, where another testee reaches the same regime via runtime flags on its ordinary artifact) -- shown as a per-row COLUMN, not a split: both forms answer the same regime and RANK TOGETHER in one table (`form` is a key only for compile-cost rows, where a whole-subject artifact is genuinely a separate compile with its own cost); `fact` restates it as 'same program' / 'separate artifact' (R4)
- status policy (OD-B14): a ranking row whose record `status` is not `measured` is excluded from ranking by default, listed under its table as `not ranked: <testee> -- <status> (<status_detail excerpt>)`; `--include-unmeasured` ranks it instead, with `status` shown
- trial-agreement policy (schema v1.4, rule v1.11-group, X31-X33): a record's five trials must agree to within k=1.5 on every group of its rows — one slow trial of five tolerated; two, or one fast, is a disagreeing row; a group disagrees at >= 2 disagreeing rows reaching a third of it (d_min=2, c=3); a record with a disagreeing group, or with fewer than five odd trials, is `inconclusive-spread` and unranked like `inconclusive-load`; the after-run load/occupancy samples are provenance (v1.4 X13), shown under --include-provenance
- status rule: v1.4 X13 (pre-flight + trial agreement) on 2 record(s)
- tier policy (R3, schema v1.2 `tier`, absent = `pinned`): a `scratch`-tier row is excluded from ranking by default, listed as `scratch: <testee>`; `--include-scratch` ranks it instead, with a `tier` column
- duplicate-record policy (OD-B15, amended 2026-08-25): the NEWEST MEASURED record per (subbench@version, testee_id, machine) ranks by default -- a newer record that is NOT measured does not supersede a measured one of the same testee and version (listed as "newer, not measured" instead); only when no record in the group is measured does the newest record overall stand (itself unranked per the status policy above, unless --include-unmeasured). `--all-records` shows every record as its own row, its testee id suffixed `@<timestamp>`

- dropped expectation triples: 2 triples, 20 rows (by name: email-nested-plus x t-evil-match-60k, email-nested-plus x t-evil-nearmiss-16k) -- no expectation could be derived for them, so their cells are not judged (per-row `no-expectation`); counted from the included records' own rows

## Ranking (per pattern x regime, SET grain: sum over the subject set; best median first)

### `balanced-parens-rec` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 606,924.5 | 0.0994 | 602,812.3 | 616,713.9 | 4,784.3 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 607,714.6 | 0.0996 | 600,756.8 | 610,237.5 | 3,450.8 | 1.001x | 1.001x |

#### `balanced-parens-rec` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 439,749.4 | 0.4194 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 440,342.6 | 0.4199 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 90,607.8 | 0.3456 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 90,575.9 | 0.3455 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 21,114.8 | 0.3222 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 20,813.6 | 0.3176 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 380.9 | 0.0062 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 378.4 | 0.0062 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 77.2 | 0.0047 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 77.4 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 77.4 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 77.1 | 0.0047 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 22.5 | 0.0055 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 21.7 | 0.0053 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 197.2 | 0.1926 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 195.6 | 0.1910 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 19,221.9 | 0.2933 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 19,115.2 | 0.2917 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 2,212.0 | 0.2700 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2,181.0 | 0.2662 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 77.5 | 0.0047 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 78.4 | 0.0048 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 22.1 | 0.0054 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 22.0 | 0.0054 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7,624.1 | 0.0073 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,552.5 | 0.0072 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,596.3 | 0.0061 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,579.2 | 0.0060 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,529.7 | 0.0072 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,619.3 | 0.0073 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,958.6 | 0.0076 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,612.7 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,598.5 | 0.0072 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,533.6 | 0.0072 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 380.6 | 0.0062 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 378.8 | 0.0062 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 78.2 | 0.0048 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.6 | 0.0047 |

### `balanced-parens-rec` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 431.8 | 430.6 | 453.4 | 8.6 | 1.000x | 1.000x | 75 | 5.8 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 467.6 | 466.4 | 472.8 | 2.3 | 1.083x | 1.083x | 75 | 6.2 | 3.8 | 100% |

### `base10num-near-miss` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 2,428.8 | 0.0004 | 2,402.9 | 2,436.5 | 12.1 | 1.000x | 1.000x | **dominated**: `t-hyb-digits-4k` is 97.7% of this set |
| 2 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 2,430.5 | 0.0004 | 2,410.8 | 2,436.0 | 11.1 | 1.001x | 1.001x | **dominated**: `t-hyb-digits-4k` is 97.8% of this set |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `base10num-near-miss` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.8 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.8 | 0.0000 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0000 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.7 | 0.0000 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0002 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.7 | 0.0002 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 7.6 | 0.0005 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.3 | 0.0004 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 2,372.8 | 0.5793 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2,377.3 | 0.5804 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0028 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.7 | 0.0026 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0000 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.7 | 0.0000 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0003 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.7 | 0.0003 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0002 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.7 | 0.0002 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0007 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.7 | 0.0007 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.0 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.7 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.7 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.7 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.7 | 0.0000 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0002 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.7 | 0.0002 |

### `base10num-near-miss` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 289.8 | 286.2 | 295.5 | 3.5 | 1.000x | 1.000x | 75 | 3.9 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 309.4 | 292.1 | 342.7 | 18.9 | 1.068x | 1.068x | 75 | 4.1 | 3.8 | 100% |

### `bracket-array-define` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 219.0 | 0.0000 | 218.4 | 224.9 | 3.0 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 221.3 | 0.0000 | 221.0 | 222.1 | 0.4 | 1.011x | 1.011x |

#### `bracket-array-define` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 11.6 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 11.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 11.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 11.6 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 12.0 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 11.7 | 0.0002 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 11.5 | 0.0002 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 11.6 | 0.0002 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 11.6 | 0.0007 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 11.6 | 0.0007 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 11.5 | 0.0007 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 11.7 | 0.0007 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 11.5 | 0.0028 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 11.6 | 0.0028 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 11.6 | 0.0113 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 11.6 | 0.0114 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 11.5 | 0.0002 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 11.7 | 0.0002 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 11.5 | 0.0014 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 11.7 | 0.0014 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 11.6 | 0.0007 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 11.6 | 0.0007 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 11.5 | 0.0028 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 11.7 | 0.0029 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 11.5 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 11.7 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 11.5 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 11.7 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 11.5 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 11.6 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 11.5 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 11.7 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 11.6 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 11.7 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 11.4 | 0.0002 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 11.7 | 0.0002 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 11.7 | 0.0007 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 11.6 | 0.0007 |

### `bracket-array-define` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 876.1 | 869.2 | 1,106.5 | 93.3 | 1.000x | 1.000x | 75 | 11.7 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 898.8 | 856.9 | 904.4 | 21.8 | 1.026x | 1.026x | 75 | 12.0 | 3.8 | 100% |

### `codegrammar-flat` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 371,529.2 | 0.0609 | 363,558.4 | 377,818.1 | 5,189.9 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 379,399.5 | 0.0622 | 369,380.7 | 397,832.6 | 9,889.6 | 1.021x | 1.021x |

#### `codegrammar-flat` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 240,723.3 | 0.2296 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 252,144.9 | 0.2405 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 58,809.2 | 0.2243 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 59,280.4 | 0.2261 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 14,675.3 | 0.2239 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 14,921.8 | 0.2277 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 371.1 | 0.0060 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 374.2 | 0.0061 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 75.9 | 0.0046 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 77.0 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 75.8 | 0.0046 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 76.4 | 0.0047 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 21.8 | 0.0053 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 22.2 | 0.0054 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 272.3 | 0.2659 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 245.4 | 0.2397 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 19,439.8 | 0.2966 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 17,809.6 | 0.2718 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2,857.5 | 0.3488 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 2,494.1 | 0.3044 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 77.8 | 0.0047 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 77.3 | 0.0047 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 21.5 | 0.0053 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 22.1 | 0.0054 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,806.2 | 0.0074 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7,563.8 | 0.0072 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,573.2 | 0.0060 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,586.3 | 0.0061 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,545.2 | 0.0072 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,522.5 | 0.0072 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,870.9 | 0.0075 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,594.1 | 0.0072 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,798.4 | 0.0074 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,627.4 | 0.0073 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 372.9 | 0.0061 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 375.7 | 0.0061 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 75.6 | 0.0046 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.9 | 0.0047 |

### `codegrammar-flat` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 421.1 | 420.6 | 427.7 | 2.8 | 1.000x | 1.000x | 75 | 5.6 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 429.1 | 427.9 | 438.3 | 4.4 | 1.019x | 1.019x | 75 | 5.7 | 3.8 | 100% |

### `codegrammar-xflag` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 368,561.3 | 0.0604 | 361,938.0 | 372,510.2 | 3,886.0 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 377,666.3 | 0.0619 | 369,965.1 | 383,442.4 | 4,496.0 | 1.025x | 1.025x |

#### `codegrammar-xflag` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 239,334.5 | 0.2282 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 248,218.6 | 0.2367 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 57,857.2 | 0.2207 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 60,463.9 | 0.2307 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 14,301.0 | 0.2182 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 15,152.9 | 0.2312 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 372.4 | 0.0061 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 371.9 | 0.0061 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.2 | 0.0046 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.9 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.3 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 76.6 | 0.0047 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 21.1 | 0.0051 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.8 | 0.0053 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 269.3 | 0.2630 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 249.9 | 0.2440 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 18,828.8 | 0.2873 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 17,855.5 | 0.2725 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2,764.9 | 0.3375 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 2,482.0 | 0.3030 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 77.6 | 0.0047 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 77.8 | 0.0047 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 21.7 | 0.0053 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.9 | 0.0053 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,648.9 | 0.0073 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7,507.1 | 0.0072 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,571.9 | 0.0060 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,591.1 | 0.0061 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,626.9 | 0.0073 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,621.4 | 0.0073 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,616.1 | 0.0073 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,621.4 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,655.4 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,588.6 | 0.0072 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 375.3 | 0.0061 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 374.9 | 0.0061 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.1 | 0.0046 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.6 | 0.0047 |

### `codegrammar-xflag` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 421.1 | 419.4 | 426.3 | 2.9 | 1.000x | 1.000x | 75 | 5.6 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 430.4 | 429.5 | 438.0 | 3.2 | 1.022x | 1.022x | 75 | 5.7 | 3.8 | 100% |

### `currency-lookbehind-fixed` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 42,777.3 | 0.0070 | 42,761.0 | 42,977.0 | 80.6 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 43,420.2 | 0.0071 | 43,229.3 | 43,445.2 | 86.4 | 1.015x | 1.015x |

#### `currency-lookbehind-fixed` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,573.9 | 0.0072 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 7,592.9 | 0.0072 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,572.0 | 0.0060 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 1,580.9 | 0.0060 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 400.3 | 0.0061 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 402.6 | 0.0061 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 375.9 | 0.0061 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 378.4 | 0.0062 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.5 | 0.0047 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 77.0 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.3 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 77.3 | 0.0047 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 21.9 | 0.0054 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.6 | 0.0053 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 8.8 | 0.0086 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 8.7 | 0.0085 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 400.1 | 0.0061 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 402.4 | 0.0061 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 39.9 | 0.0049 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 40.5 | 0.0049 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.8 | 0.0047 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 77.4 | 0.0047 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 21.6 | 0.0053 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.7 | 0.0053 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,544.9 | 0.0072 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7,896.7 | 0.0075 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,571.1 | 0.0060 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,582.0 | 0.0060 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,620.4 | 0.0073 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,583.8 | 0.0072 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,451.8 | 0.0071 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,613.3 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,506.6 | 0.0072 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,512.3 | 0.0072 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 375.5 | 0.0061 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 377.8 | 0.0061 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.5 | 0.0047 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 77.0 | 0.0047 |

### `currency-lookbehind-fixed` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 366.8 | 364.0 | 374.1 | 4.3 | 1.000x | 1.000x | 75 | 4.9 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 367.7 | 361.0 | 368.6 | 3.1 | 1.002x | 1.002x | 75 | 4.9 | 3.8 | 100% |

### `date-nested-plus` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 443.3 | 441.5 | 451.1 | 4.0 | 1.000x | 1.000x | 75 | 5.9 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 444.3 | 441.9 | 450.1 | 3.1 | 1.002x | 1.002x | 75 | 5.9 | 3.8 | 100% |

### `doubled-word` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 16,059,409.3 | 2.6311 | 15,959,174.8 | 16,139,608.0 | 67,180.6 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 16,157,967.8 | 2.6472 | 15,971,865.7 | 16,283,463.7 | 119,045.3 | 1.006x | 1.006x |

#### `doubled-word` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 2,731,054.4 | 2.6045 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2,710,705.6 | 2.5851 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 680,336.3 | 2.5953 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 673,981.0 | 2.5710 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 159,861.7 | 2.4393 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 158,188.5 | 2.4138 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 94,509.8 | 1.5382 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 94,079.3 | 1.5312 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 25,013.6 | 1.5266 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 24,914.4 | 1.5206 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 34,749.6 | 2.1210 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 34,522.5 | 2.1071 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 6,270.6 | 1.5309 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6,292.5 | 1.5363 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 1,861.5 | 1.8179 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,873.8 | 1.8299 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 143,348.4 | 2.1873 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 142,407.4 | 2.1730 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 15,355.7 | 1.8745 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 15,300.8 | 1.8678 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 34,751.9 | 2.1211 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 34,512.4 | 2.1065 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 7,503.1 | 1.8318 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,521.4 | 1.8363 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 2,680,991.6 | 2.5570 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2,653,309.9 | 2.5306 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 664,587.6 | 2.5357 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 661,417.7 | 2.5236 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 2,924,096.2 | 2.7888 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2,915,221.6 | 2.7803 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 2,924,987.5 | 2.7896 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2,917,756.3 | 2.7827 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 2,929,665.7 | 2.7941 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2,915,128.0 | 2.7802 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 11,780.5 | 0.1917 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 11,927.4 | 0.1941 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3,161.6 | 0.1930 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,107.4 | 0.1896 |

### `doubled-word` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 2,533.9 | 2,527.1 | 2,601.0 | 28.7 | 1.000x | 1.000x | 75 | 33.8 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 2,596.9 | 2,562.1 | 2,621.7 | 20.1 | 1.025x | 1.025x | 75 | 34.6 | 3.8 | 100% |

### `dup-param-detect` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 535.8 | 528.8 | 545.6 | 5.7 | 1.000x | 1.000x | 75 | 7.1 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 560.4 | 557.3 | 567.7 | 4.2 | 1.046x | 1.046x | 75 | 7.5 | 3.8 | 100% |

### `email-local-nodup` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 47,005.6 | 0.0077 | 46,990.9 | 47,038.6 | 20.6 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 47,094.2 | 0.0077 | 47,049.7 | 47,322.6 | 104.8 | 1.002x | 1.002x |

#### `email-local-nodup` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 11.6 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 11.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 10.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 9.8 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 13.5 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 10.8 | 0.0002 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 35,058.8 | 0.5706 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 35,256.7 | 0.5738 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 9,419.3 | 0.5749 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 9,379.9 | 0.5725 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 9.3 | 0.0006 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 8.5 | 0.0005 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 2,354.5 | 0.5748 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2,335.7 | 0.5702 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 13.3 | 0.0130 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 17.2 | 0.0168 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 13.3 | 0.0002 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 17.0 | 0.0003 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 13.3 | 0.0016 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 17.2 | 0.0021 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 11.6 | 0.0007 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 10.8 | 0.0007 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 6.4 | 0.0016 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.2 | 0.0015 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 8.7 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7.8 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 10.9 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 10.1 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 10.4 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 9.7 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 10.4 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 9.7 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 10.4 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 9.6 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 6.5 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.1 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 6.4 | 0.0004 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.1 | 0.0004 |

### `email-local-nodup` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 771.4 | 764.7 | 801.2 | 13.1 | 1.000x | 1.000x | 75 | 10.3 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 806.9 | 782.6 | 813.1 | 11.5 | 1.046x | 1.046x | 75 | 10.8 | 3.8 | 100% |

### `email-nested-plus` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 702.6 | 700.1 | 713.1 | 4.8 | 1.000x | 1.000x | 75 | 9.4 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 715.1 | 712.5 | 723.9 | 4.2 | 1.018x | 1.018x | 75 | 9.5 | 3.8 | 100% |

### `evil-alt-nested` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 49,674.8 | 0.0081 | 41,513.7 | 55,843.1 | 4,659.1 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 54,415.1 | 0.0089 | 50,232.9 | 55,526.3 | 1,911.7 | 1.095x | 1.095x |

#### `evil-alt-nested` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 7.9 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.1 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 14.7 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 14.5 | 0.0002 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 43,279.3 | 0.7044 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 46,606.0 | 0.7586 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 6,357.5 | 0.3880 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 8,273.0 | 0.5049 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0004 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.9 | 0.0004 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0015 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.9 | 0.0014 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 9.0 | 0.0087 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7.8 | 0.0076 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 8.9 | 0.0001 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7.8 | 0.0001 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 8.9 | 0.0011 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7.8 | 0.0010 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 8.4 | 0.0005 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7.4 | 0.0005 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0015 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.9 | 0.0014 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7.8 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7.1 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 10.1 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 8.6 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.9 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.9 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.9 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.9 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0004 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.9 | 0.0004 |

### `evil-alt-nested` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 647.6 | 644.6 | 654.6 | 4.4 | 1.000x | 1.000x | 75 | 8.6 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 650.1 | 648.6 | 750.6 | 39.7 | 1.004x | 1.004x | 75 | 8.7 | 3.8 | 100% |

### `file-ext-order` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 319,667.2 | 0.0524 | 316,300.6 | 320,064.4 | 1,388.5 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 321,173.5 | 0.0526 | 317,528.7 | 322,100.7 | 1,919.4 | 1.005x | 1.005x |

#### `file-ext-order` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 59,787.8 | 0.0570 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 60,130.0 | 0.0573 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 14,866.9 | 0.0567 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 14,887.5 | 0.0568 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 3,682.3 | 0.0562 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,688.5 | 0.0563 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 374.0 | 0.0061 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 376.0 | 0.0061 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 75.6 | 0.0046 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.2 | 0.0046 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 75.8 | 0.0046 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.2 | 0.0046 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.0 | 0.0051 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 21.0 | 0.0051 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 49.0 | 0.0478 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 47.9 | 0.0468 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 3,127.4 | 0.0477 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,144.2 | 0.0480 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 379.0 | 0.0463 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 375.9 | 0.0459 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 77.4 | 0.0047 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 77.6 | 0.0047 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 259.4 | 0.0633 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 258.9 | 0.0632 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 23,187.9 | 0.0221 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 23,364.6 | 0.0223 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 5,517.4 | 0.0211 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5,561.1 | 0.0212 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 68,655.4 | 0.0655 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 68,859.2 | 0.0657 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 69,315.1 | 0.0661 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 69,778.4 | 0.0665 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 69,477.1 | 0.0663 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 69,493.8 | 0.0663 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 377.0 | 0.0061 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 377.4 | 0.0061 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 75.9 | 0.0046 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 75.8 | 0.0046 |

### `file-ext-order` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 271.2 | 271.0 | 274.0 | 1.2 | 1.000x | 1.000x | 75 | 3.6 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 295.0 | 293.8 | 298.3 | 1.8 | 1.088x | 1.088x | 75 | 3.9 | 3.8 | 100% |

### `float-literal-bound` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 3,937,440.5 | 0.6451 | 3,925,892.3 | 3,977,122.5 | 18,312.9 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 4,012,602.8 | 0.6574 | 4,004,709.1 | 4,049,583.6 | 16,232.9 | 1.019x | 1.019x |

#### `float-literal-bound` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 648,206.0 | 0.6182 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 646,237.8 | 0.6163 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 147,941.0 | 0.5644 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 153,462.6 | 0.5854 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 25,485.6 | 0.3889 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 24,095.5 | 0.3677 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 373.1 | 0.0061 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 376.3 | 0.0061 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 75.3 | 0.0046 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 75.7 | 0.0046 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.5 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 75.6 | 0.0046 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 20.4 | 0.0050 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 20.9 | 0.0051 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 320.6 | 0.3131 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 321.5 | 0.3140 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 24,802.0 | 0.3784 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 26,038.5 | 0.3973 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2,789.0 | 0.3405 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 3,112.5 | 0.3799 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,188.3 | 0.1946 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3,154.0 | 0.1925 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2,939.9 | 0.7177 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 2,941.9 | 0.7182 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,523,698.7 | 1.4532 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 1,560,134.2 | 1.4880 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 363,384.9 | 1.3865 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 374,130.4 | 1.4275 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 391,096.8 | 0.3730 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 411,550.2 | 0.3925 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 395,309.6 | 0.3770 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 406,472.5 | 0.3877 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 393,825.5 | 0.3756 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 407,086.3 | 0.3882 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 374.1 | 0.0061 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 375.0 | 0.0061 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 74.7 | 0.0046 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 75.3 | 0.0046 |

### `float-literal-bound` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 404.0 | 402.0 | 413.0 | 3.8 | 1.000x | 1.000x | 75 | 5.4 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 434.0 | 433.1 | 438.9 | 2.2 | 1.074x | 1.074x | 75 | 5.8 | 3.8 | 100% |

### `floor-byte` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 43,557.6 | 0.0071 | 42,925.8 | 44,270.9 | 472.2 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 44,061.9 | 0.0072 | 43,028.4 | 44,155.9 | 521.4 | 1.012x | 1.012x |

#### `floor-byte` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,633.0 | 0.0073 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 7,653.8 | 0.0073 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,579.3 | 0.0060 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 1,577.8 | 0.0060 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 399.5 | 0.0061 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 399.7 | 0.0061 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 376.0 | 0.0061 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 374.5 | 0.0061 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.5 | 0.0047 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.8 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 77.3 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 76.0 | 0.0046 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 21.5 | 0.0053 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.5 | 0.0053 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.9 | 0.0068 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 7.4 | 0.0072 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 401.7 | 0.0061 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 400.3 | 0.0061 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 39.2 | 0.0048 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 39.2 | 0.0048 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.3 | 0.0047 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 76.2 | 0.0047 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 20.7 | 0.0051 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 20.4 | 0.0050 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,711.8 | 0.0074 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7,800.3 | 0.0074 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,585.9 | 0.0061 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,583.1 | 0.0060 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,689.3 | 0.0073 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,610.3 | 0.0073 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,605.2 | 0.0073 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,766.5 | 0.0074 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,583.5 | 0.0072 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,755.5 | 0.0074 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 375.8 | 0.0061 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 374.2 | 0.0061 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.4 | 0.0047 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.2 | 0.0047 |

### `floor-byte` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 251.3 | 250.0 | 260.1 | 3.9 | 1.000x | 1.000x | 75 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 281.8 | 275.1 | 294.0 | 7.5 | 1.121x | 1.121x | 75 | 3.8 | 100% |

### `hex8-bounded` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 4,580,631.5 | 0.7505 | 4,565,875.5 | 4,592,814.7 | 9,962.7 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 4,588,136.5 | 0.7517 | 4,550,420.1 | 4,612,736.3 | 22,885.8 | 1.002x | 1.002x |

#### `hex8-bounded` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 625,280.2 | 0.5963 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 617,412.0 | 0.5888 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 88,975.1 | 0.3394 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 88,308.2 | 0.3369 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 22,122.0 | 0.3376 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 22,069.2 | 0.3367 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 18,307.6 | 0.2980 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 18,153.8 | 0.2955 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 4,845.6 | 0.2957 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 4,804.1 | 0.2932 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 8,303.9 | 0.5068 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 8,187.7 | 0.4997 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 8,029.8 | 1.9604 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 7,943.2 | 1.9393 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 332.2 | 0.3244 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 329.3 | 0.3216 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 21,973.4 | 0.3353 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 21,886.7 | 0.3340 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2,755.4 | 0.3363 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 2,727.7 | 0.3330 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5,128.5 | 0.3130 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 5,078.8 | 0.3100 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2,668.3 | 0.6514 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 2,692.2 | 0.6573 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,407,564.3 | 1.3425 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 1,402,691.2 | 1.3378 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 332,578.7 | 1.2689 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 333,656.1 | 1.2730 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 672,037.4 | 0.6409 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 677,558.0 | 0.6462 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 675,551.4 | 0.6443 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 672,876.4 | 0.6417 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 674,774.5 | 0.6435 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 679,146.2 | 0.6477 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 14,266.2 | 0.2322 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 14,306.8 | 0.2329 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,798.8 | 0.2318 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3,802.1 | 0.2320 |

### `hex8-bounded` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 590.9 | 588.9 | 592.2 | 1.1 | 1.000x | 1.000x | 75 | 7.9 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 611.8 | 597.6 | 623.7 | 9.2 | 1.035x | 1.035x | 75 | 8.2 | 3.8 | 100% |

### `high-byte-run` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 1,165,766.5 | 0.1910 | 1,156,732.0 | 1,176,723.3 | 7,143.8 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 1,177,215.6 | 0.1929 | 1,173,244.9 | 1,215,206.2 | 15,724.6 | 1.010x | 1.010x |

#### `high-byte-run` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 198,670.2 | 0.1895 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 202,252.2 | 0.1929 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 49,539.0 | 0.1890 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 50,364.6 | 0.1921 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 12,468.7 | 0.1903 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 12,632.1 | 0.1928 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 11,637.6 | 0.1894 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 11,808.8 | 0.1922 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3,115.0 | 0.1901 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,086.5 | 0.1884 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3,144.0 | 0.1919 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,097.1 | 0.1890 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 795.0 | 0.1941 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 778.1 | 0.1900 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 202.3 | 0.1975 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 198.7 | 0.1940 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 12,580.6 | 0.1920 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 12,618.0 | 0.1925 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 1,571.8 | 0.1919 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,543.9 | 0.1885 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3,152.1 | 0.1924 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,103.8 | 0.1894 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 778.0 | 0.1899 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 777.4 | 0.1898 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 201,437.1 | 0.1921 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 202,450.1 | 0.1931 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 50,454.1 | 0.1925 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 50,292.3 | 0.1919 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 198,615.0 | 0.1894 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 201,838.2 | 0.1925 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 199,469.8 | 0.1902 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 201,956.3 | 0.1926 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 200,606.8 | 0.1913 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 202,051.5 | 0.1927 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 11,663.5 | 0.1898 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 11,859.0 | 0.1930 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3,110.2 | 0.1898 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,102.2 | 0.1893 |

### `high-byte-run` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 474.7 | 471.3 | 482.7 | 4.3 | 1.000x | 1.000x | 75 | 6.3 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 538.9 | 515.2 | 544.9 | 12.6 | 1.135x | 1.135x | 75 | 7.2 | 3.8 | 100% |

### `ipv4-near-miss` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 47.4 | 0.0000 | 47.3 | 47.8 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 47.8 | 0.0000 | 47.8 | 48.0 | 0.1 | 1.009x | 1.009x |

#### `ipv4-near-miss` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.5 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 2.5 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.5 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 2.5 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.6 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 2.6 | 0.0000 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.5 | 0.0000 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 2.5 | 0.0000 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.5 | 0.0002 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 2.5 | 0.0002 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.5 | 0.0002 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 2.5 | 0.0002 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.5 | 0.0006 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 2.5 | 0.0006 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.5 | 0.0024 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 2.5 | 0.0025 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.5 | 0.0000 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 2.5 | 0.0000 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.5 | 0.0003 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 2.5 | 0.0003 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.5 | 0.0002 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 2.5 | 0.0002 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.5 | 0.0006 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 2.5 | 0.0006 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.5 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 2.5 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.5 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 2.5 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.5 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 2.5 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.5 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 2.5 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.5 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 2.5 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.5 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 2.5 | 0.0000 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.5 | 0.0002 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 2.5 | 0.0002 |

### `ipv4-near-miss` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 250.8 | 249.9 | 253.6 | 1.3 | 1.000x | 1.000x | 75 | 3.3 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 263.3 | 246.7 | 267.4 | 7.2 | 1.050x | 1.050x | 75 | 3.5 | 3.8 | 100% |

### `keyword-prefix-order` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 1,119,913.2 | 0.1835 | 1,111,447.3 | 1,147,405.5 | 13,983.7 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 1,151,907.3 | 0.1887 | 1,146,872.8 | 1,205,164.0 | 26,521.3 | 1.029x | 1.029x |

#### `keyword-prefix-order` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 228,900.8 | 0.2183 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 241,659.6 | 0.2305 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 33,905.0 | 0.1293 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 33,606.6 | 0.1282 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 8,429.3 | 0.1286 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 8,380.3 | 0.1279 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 8,979.7 | 0.1462 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 8,973.7 | 0.1461 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2,405.3 | 0.1468 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 2,396.4 | 0.1463 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.4 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 76.8 | 0.0047 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 21.8 | 0.0053 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 22.2 | 0.0054 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 107.0 | 0.1044 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 105.2 | 0.1027 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,435.9 | 0.1135 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 7,397.8 | 0.1129 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 854.7 | 0.1043 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 847.9 | 0.1035 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2,758.7 | 0.1684 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 2,763.8 | 0.1687 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 180.1 | 0.0440 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 175.4 | 0.0428 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 86,687.6 | 0.0827 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 84,219.3 | 0.0803 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 20,627.1 | 0.0787 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 20,617.9 | 0.0787 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 236,115.5 | 0.2252 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 248,955.6 | 0.2374 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 250,925.1 | 0.2393 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 246,564.0 | 0.2352 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 233,712.9 | 0.2229 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 245,893.7 | 0.2345 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 370.6 | 0.0060 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 370.9 | 0.0060 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 74.9 | 0.0046 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 75.2 | 0.0046 |

### `keyword-prefix-order` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 312.1 | 308.9 | 337.5 | 10.8 | 1.000x | 1.000x | 75 | 4.2 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 341.5 | 335.8 | 345.1 | 3.0 | 1.094x | 1.094x | 75 | 4.6 | 3.8 | 100% |

### `letters-bounded-tail-z` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 462.2 | 0.0001 | 461.2 | 467.9 | 2.4 | 1.000x | 1.000x | spread |
| 2 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 1,300.3 | 0.0002 | 1,289.8 | 1,305.0 | 6.1 | 2.814x | 2.814x | **dominated**: `t-evil-match-60k` is 90.1% of this set |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `letters-bounded-tail-z` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.0 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.0 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 327.3 | 0.0053 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,171.5 | 0.0191 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0004 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.9 | 0.0004 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0004 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.0 | 0.0004 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0015 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.9 | 0.0015 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 10.0 | 0.0098 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 9.6 | 0.0093 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 9.7 | 0.0001 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 8.6 | 0.0001 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 10.7 | 0.0013 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 10.9 | 0.0013 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 9.7 | 0.0006 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 8.6 | 0.0005 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 9.1 | 0.0022 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 8.1 | 0.0020 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.9 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.9 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.0 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.0 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 9.8 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 9.1 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.0 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 9.1 | 0.0006 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 8.2 | 0.0005 |

### `letters-bounded-tail-z` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 486.3 | 481.5 | 491.9 | 3.4 | 1.000x | 1.000x | 75 | 6.5 | 3.8 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 581.7 | 576.9 | 583.8 | 2.3 | 1.196x | 1.196x | 75 | 7.8 | 3.4 | 100% |

### `logparse-atomic` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 12,865.9 | 0.0021 | 12,821.8 | 13,033.6 | 83.0 | 1.000x | 1.000x | **dominated**: `t-hyb-logline-16k` is 99.1% of this set |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 12,890.8 | 0.0021 | 12,862.0 | 13,047.5 | 65.5 | 1.002x | 1.002x | **dominated**: `t-hyb-logline-16k` is 99.1% of this set |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `logparse-atomic` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.4 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 6.5 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 6.5 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.9 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.2 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 6.9 | 0.0001 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.2 | 0.0004 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 6.9 | 0.0004 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.3 | 0.0004 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 6.5 | 0.0004 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.3 | 0.0015 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 6.5 | 0.0016 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.3 | 0.0062 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 6.7 | 0.0065 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.3 | 0.0001 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 6.7 | 0.0001 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.3 | 0.0008 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 6.7 | 0.0008 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 12,751.8 | 0.7783 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 12,773.0 | 0.7796 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.2 | 0.0015 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 6.5 | 0.0016 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.5 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 6.7 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.8 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 6.9 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.1 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 6.5 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.1 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 6.5 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.1 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 6.5 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.2 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 6.5 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.1 | 0.0004 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 6.5 | 0.0004 |

### `logparse-atomic` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 496.1 | 493.3 | 499.7 | 2.3 | 1.000x | 1.000x | 75 | 6.6 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 517.6 | 510.0 | 520.4 | 3.8 | 1.043x | 1.043x | 75 | 6.9 | 3.8 | 100% |

### `logparse-atomic-removed` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 12,936.1 | 0.0021 | 12,905.7 | 12,944.4 | 16.9 | 1.000x | 1.000x | **dominated**: `t-hyb-logline-16k` is 99.1% of this set |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 12,984.4 | 0.0021 | 12,785.8 | 13,436.5 | 216.9 | 1.004x | 1.004x | **dominated**: `t-hyb-logline-16k` is 99.1% of this set |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `logparse-atomic-removed` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.3 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 6.5 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 6.8 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.1 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 5.9 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.1 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 6.9 | 0.0001 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.0 | 0.0004 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 6.8 | 0.0004 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.4 | 0.0004 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 6.4 | 0.0004 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.3 | 0.0015 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 6.4 | 0.0016 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.3 | 0.0061 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 6.6 | 0.0065 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.4 | 0.0001 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 6.6 | 0.0001 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.3 | 0.0008 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 6.6 | 0.0008 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 12,823.7 | 0.7827 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 12,866.0 | 0.7853 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.3 | 0.0015 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 6.4 | 0.0016 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.5 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 6.6 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.6 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 6.9 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.2 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 6.4 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.1 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 6.4 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.1 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 6.4 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.2 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 6.4 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.2 | 0.0004 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 6.5 | 0.0004 |

### `logparse-atomic-removed` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 492.8 | 489.4 | 510.8 | 7.9 | 1.000x | 1.000x | 75 | 6.6 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 516.7 | 499.8 | 547.0 | 16.5 | 1.049x | 1.049x | 75 | 6.9 | 3.8 | 100% |

### `mojibake-curly-quote` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 42,793.7 | 0.0070 | 42,741.4 | 43,053.4 | 112.4 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 44,270.2 | 0.0073 | 43,695.8 | 44,894.9 | 448.9 | 1.035x | 1.035x |

#### `mojibake-curly-quote` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,598.9 | 0.0072 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 7,877.3 | 0.0075 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,570.9 | 0.0060 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 1,580.1 | 0.0060 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 399.9 | 0.0061 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 403.2 | 0.0062 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 375.3 | 0.0061 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 377.6 | 0.0061 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.3 | 0.0047 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 77.4 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.5 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 77.0 | 0.0047 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 21.1 | 0.0051 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.5 | 0.0052 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 8.0 | 0.0078 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 8.0 | 0.0078 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 399.7 | 0.0061 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 402.1 | 0.0061 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 39.6 | 0.0048 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 40.1 | 0.0049 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.3 | 0.0047 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 76.7 | 0.0047 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 21.2 | 0.0052 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.7 | 0.0053 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,619.0 | 0.0073 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7,819.9 | 0.0075 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,570.1 | 0.0060 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,582.6 | 0.0060 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,480.1 | 0.0071 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,979.9 | 0.0076 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,523.1 | 0.0072 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,715.3 | 0.0074 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,549.7 | 0.0072 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,960.3 | 0.0076 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 375.0 | 0.0061 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 377.2 | 0.0061 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.0 | 0.0046 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.8 | 0.0047 |

### `mojibake-curly-quote` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 301.4 | 298.8 | 308.2 | 3.4 | 1.000x | 1.000x | 75 | 4.0 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 307.5 | 307.3 | 324.0 | 6.4 | 1.020x | 1.020x | 75 | 4.1 | 3.8 | 100% |

### `nested-comment-rec` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 42,836.5 | 0.0070 | 42,796.2 | 43,590.7 | 301.0 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 43,215.7 | 0.0071 | 42,903.4 | 43,322.1 | 153.5 | 1.009x | 1.009x |

#### `nested-comment-rec` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 7,466.3 | 0.0071 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,801.2 | 0.0074 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 1,572.5 | 0.0060 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,573.8 | 0.0060 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 401.5 | 0.0061 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 401.6 | 0.0061 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 376.7 | 0.0061 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 377.4 | 0.0061 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.5 | 0.0047 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.3 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 76.5 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.5 | 0.0047 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.7 | 0.0053 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 21.1 | 0.0052 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 8.7 | 0.0085 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 9.0 | 0.0087 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 402.1 | 0.0061 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 401.9 | 0.0061 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 39.9 | 0.0049 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 39.6 | 0.0048 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 76.3 | 0.0047 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.6 | 0.0047 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.4 | 0.0052 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 21.4 | 0.0052 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7,591.9 | 0.0072 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,554.5 | 0.0072 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,571.3 | 0.0060 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,573.7 | 0.0060 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,591.0 | 0.0072 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,632.6 | 0.0073 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,539.3 | 0.0072 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,463.9 | 0.0071 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,630.5 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,567.8 | 0.0072 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 376.9 | 0.0061 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 376.9 | 0.0061 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.3 | 0.0047 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.1 | 0.0046 |

### `nested-comment-rec` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 795.8 | 770.0 | 811.7 | 14.9 | 1.000x | 1.000x | 75 | 10.6 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 816.9 | 813.2 | 832.0 | 6.8 | 1.027x | 1.027x | 75 | 10.9 | 3.8 | 100% |

### `numeric-id-nested-plus` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 2,354.7 | 0.0004 | 2,236.9 | 2,437.8 | 71.5 | 1.000x | 1.000x | **dominated**: `t-hyb-digits-4k` is 95.8% of this set |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 2,457.6 | 0.0004 | 2,076.4 | 2,489.2 | 156.9 | 1.044x | 1.044x | **dominated**: `t-hyb-digits-4k` is 95.9% of this set |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `numeric-id-nested-plus` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.4 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.4 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.5 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 5.5 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.3 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0001 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.2 | 0.0003 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0003 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 8.5 | 0.0005 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 8.7 | 0.0005 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2,257.1 | 0.5511 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 2,355.9 | 0.5752 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.2 | 0.0051 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0053 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.2 | 0.0001 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0001 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.2 | 0.0006 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0007 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.2 | 0.0003 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0003 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.3 | 0.0013 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0013 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.9 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 5.8 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.8 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 6.0 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.2 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.2 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.2 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.2 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.2 | 0.0003 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0003 |

### `numeric-id-nested-plus` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 498.8 | 491.2 | 521.8 | 11.3 | 1.000x | 1.000x | 75 | 6.7 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 539.7 | 525.0 | 551.7 | 10.6 | 1.082x | 1.082x | 75 | 7.2 | 3.8 | 100% |

### `phone-list-nested-plus` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 3,246.8 | 0.0005 | 3,226.6 | 4,993.2 | 696.8 | 1.000x | 1.000x | **dominated**: `t-hyb-digits-4k` is 96.9% of this set |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 3,322.3 | 0.0005 | 3,190.8 | 3,551.7 | 133.1 | 1.023x | 1.023x | **dominated**: `t-hyb-digits-4k` is 96.9% of this set |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `phone-list-nested-plus` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.4 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.5 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.5 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 5.5 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.4 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0001 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.3 | 0.0003 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0003 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 9.4 | 0.0006 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 9.7 | 0.0006 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,147.0 | 0.7683 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 3,216.8 | 0.7853 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.2 | 0.0051 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0053 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.3 | 0.0001 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0001 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.2 | 0.0006 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0007 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.2 | 0.0003 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0003 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.4 | 0.0013 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0013 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.6 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 5.8 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.7 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 5.6 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.3 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.2 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.2 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.4 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.4 | 0.0003 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0003 |

### `phone-list-nested-plus` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 486.6 | 483.8 | 522.0 | 14.3 | 1.000x | 1.000x | 75 | 6.5 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 576.1 | 567.5 | 582.3 | 4.8 | 1.184x | 1.184x | 75 | 7.7 | 3.8 | 100% |

### `phone-palindrome-6` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 7,252,070.4 | 1.1881 | 7,200,418.5 | 7,359,874.4 | 55,806.7 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 7,258,854.7 | 1.1892 | 7,211,687.4 | 7,289,774.4 | 25,005.8 | 1.001x | 1.001x |

#### `phone-palindrome-6` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,029,556.9 | 0.9819 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 1,031,034.3 | 0.9833 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 251,974.3 | 0.9612 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 252,437.5 | 0.9630 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 55,105.0 | 0.8408 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 54,961.0 | 0.8386 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 11,744.3 | 0.1912 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 11,655.5 | 0.1897 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,105.3 | 0.1895 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3,085.8 | 0.1883 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 67,939.8 | 4.1467 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 67,090.0 | 4.0948 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 33,362.9 | 8.1452 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 33,333.2 | 8.1380 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 776.1 | 0.7579 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 782.3 | 0.7639 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 55,585.7 | 0.8482 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 55,094.3 | 0.8407 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6,728.8 | 0.8214 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 6,762.7 | 0.8255 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,154.1 | 0.1925 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3,125.5 | 0.1908 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 10,897.1 | 2.6604 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 10,928.6 | 2.6681 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2,331,388.7 | 2.2235 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 2,338,621.4 | 2.2304 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 585,176.7 | 2.2327 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 590,225.1 | 2.2520 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 929,384.3 | 0.8864 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 925,504.9 | 0.8827 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 923,698.2 | 0.8810 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 922,138.8 | 0.8795 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 927,841.6 | 0.8849 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 929,163.6 | 0.8862 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 11,665.4 | 0.1899 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 11,785.9 | 0.1918 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,090.6 | 0.1886 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3,137.4 | 0.1915 |

### `phone-palindrome-6` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 1,593.8 | 1,584.3 | 1,601.6 | 6.5 | 1.000x | 1.000x | 75 | 21.3 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 1,606.5 | 1,591.7 | 1,614.4 | 7.9 | 1.008x | 1.008x | 75 | 21.4 | 3.8 | 100% |

### `pwd-strength-chain` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 447,132.5 | 0.0733 | 446,276.3 | 448,672.4 | 939.8 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 448,153.2 | 0.0734 | 447,226.6 | 454,469.5 | 2,604.7 | 1.002x | 1.002x |

#### `pwd-strength-chain` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 25.7 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 29.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 41.5 | 0.0002 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 41.5 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 35.3 | 0.0005 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 36.3 | 0.0006 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 233,697.6 | 3.8037 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 234,934.0 | 3.8238 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 63,042.6 | 3.8476 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 63,635.3 | 3.8838 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 56,817.6 | 3.4679 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 56,064.9 | 3.4219 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 14,148.8 | 3.4543 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 14,026.0 | 3.4243 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 19.3 | 0.0188 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 43.4 | 0.0424 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 19.2 | 0.0003 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 41.4 | 0.0006 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 19.2 | 0.0023 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 42.8 | 0.0052 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 63,239.4 | 3.8598 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 62,658.2 | 3.8244 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 15,823.2 | 3.8631 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 15,846.6 | 3.8688 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 23.5 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 18.5 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 58.4 | 0.0002 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 57.1 | 0.0002 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 21.0 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 22.0 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 21.0 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 25.6 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 21.0 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 25.1 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 7.5 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7.3 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 7.4 | 0.0005 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7.3 | 0.0004 |

### `pwd-strength-chain` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 5,988.8 | 5,944.1 | 6,021.0 | 32.3 | 1.000x | 1.000x | 75 | 79.9 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 6,010.1 | 5,953.1 | 6,058.2 | 40.0 | 1.004x | 1.004x | 75 | 80.1 | 3.8 | 100% |

### `quoted-delim-match` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 1,405,036.0 | 0.2302 | 1,399,277.4 | 1,442,382.0 | 15,989.8 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 1,423,227.2 | 0.2332 | 1,404,146.6 | 1,428,041.1 | 8,848.4 | 1.013x | 1.013x |

#### `quoted-delim-match` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 363,132.9 | 0.3463 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 367,302.8 | 0.3503 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 87,510.5 | 0.3338 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 88,717.8 | 0.3384 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 21,751.0 | 0.3319 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 22,160.8 | 0.3381 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 11,966.6 | 0.1948 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 12,055.9 | 0.1962 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,119.1 | 0.1904 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3,152.1 | 0.1924 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,122.2 | 0.1906 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3,160.4 | 0.1929 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 805.0 | 0.1965 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 791.9 | 0.1933 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 472.7 | 0.4616 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 484.1 | 0.4728 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 31,976.5 | 0.4879 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 31,520.1 | 0.4810 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 4,059.4 | 0.4955 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 4,097.3 | 0.5002 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,152.4 | 0.1924 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3,164.0 | 0.1931 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 789.4 | 0.1927 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 796.2 | 0.1944 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 200,879.4 | 0.1916 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 204,502.9 | 0.1950 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 50,326.7 | 0.1920 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 50,772.8 | 0.1937 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 204,895.7 | 0.1954 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 204,714.3 | 0.1952 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 200,118.6 | 0.1909 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 204,885.7 | 0.1954 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 201,841.8 | 0.1925 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 204,319.8 | 0.1949 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 11,835.2 | 0.1926 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 12,061.9 | 0.1963 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,145.1 | 0.1919 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3,159.5 | 0.1928 |

### `quoted-delim-match` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 918.9 | 909.8 | 1,036.1 | 47.3 | 1.000x | 1.000x | 75 | 12.3 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 944.2 | 939.7 | 953.1 | 4.9 | 1.028x | 1.028x | 75 | 12.6 | 3.8 | 100% |

### `router-prefix-order` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 196,902.5 | 0.0323 | 196,471.2 | 200,882.2 | 1,651.6 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 197,752.6 | 0.0324 | 197,058.8 | 201,115.6 | 1,498.8 | 1.004x | 1.004x |

#### `router-prefix-order` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 110,869.4 | 0.1057 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 111,380.5 | 0.1062 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 27,209.5 | 0.1038 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 27,268.0 | 0.1040 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 6,403.1 | 0.0977 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6,415.7 | 0.0979 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 375.1 | 0.0061 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 374.1 | 0.0061 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 75.0 | 0.0046 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 75.9 | 0.0046 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 12,397.7 | 0.7567 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 12,336.7 | 0.7530 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 20.5 | 0.0050 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 20.0 | 0.0049 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 73.2 | 0.0715 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 73.1 | 0.0714 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 6,133.4 | 0.0936 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6,121.1 | 0.0934 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 741.9 | 0.0906 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 741.6 | 0.0905 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 75.4 | 0.0046 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 75.1 | 0.0046 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 119.6 | 0.0292 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 117.7 | 0.0287 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7,542.4 | 0.0072 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,648.6 | 0.0073 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,581.5 | 0.0060 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,569.1 | 0.0060 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,627.4 | 0.0073 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,608.0 | 0.0073 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,585.5 | 0.0072 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,595.0 | 0.0072 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,632.5 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,566.7 | 0.0072 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 376.7 | 0.0061 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 371.0 | 0.0060 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 75.5 | 0.0046 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 75.8 | 0.0046 |

### `router-prefix-order` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 278.4 | 274.7 | 293.1 | 7.4 | 1.000x | 1.000x | 75 | 3.7 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 298.2 | 296.3 | 302.9 | 2.7 | 1.071x | 1.071x | 75 | 4.0 | 3.8 | 100% |

### `tag-depth3-bound` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 43,735.2 | 0.0072 | 43,205.0 | 44,558.3 | 466.5 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 44,041.2 | 0.0072 | 43,039.1 | 44,422.4 | 461.6 | 1.007x | 1.007x |

#### `tag-depth3-bound` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,844.0 | 0.0075 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 7,650.8 | 0.0073 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,594.0 | 0.0061 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 1,582.5 | 0.0060 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 405.2 | 0.0062 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 405.0 | 0.0062 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 381.3 | 0.0062 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 379.0 | 0.0062 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 77.5 | 0.0047 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 77.4 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 77.2 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 77.4 | 0.0047 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 21.9 | 0.0053 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.8 | 0.0053 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 8.9 | 0.0087 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 8.8 | 0.0086 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 405.5 | 0.0062 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 404.4 | 0.0062 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 40.2 | 0.0049 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 40.1 | 0.0049 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 77.0 | 0.0047 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 76.9 | 0.0047 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 22.0 | 0.0054 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.6 | 0.0053 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,611.3 | 0.0073 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7,608.1 | 0.0073 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,591.1 | 0.0061 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,584.4 | 0.0060 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,697.2 | 0.0073 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,824.9 | 0.0075 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,691.3 | 0.0073 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,614.8 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,686.7 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,996.0 | 0.0076 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 381.4 | 0.0062 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 379.1 | 0.0062 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 77.8 | 0.0047 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.9 | 0.0047 |

### `tag-depth3-bound` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 529.9 | 527.4 | 542.1 | 5.9 | 1.000x | 1.000x | 75 | 7.1 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 550.4 | 545.6 | 560.5 | 5.3 | 1.039x | 1.039x | 75 | 7.3 | 3.8 | 100% |

### `tag-pair-match` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 42,937.5 | 0.0070 | 42,793.4 | 43,609.1 | 357.0 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 43,835.4 | 0.0072 | 42,760.6 | 43,883.3 | 485.4 | 1.021x | 1.021x |

#### `tag-pair-match` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 7,496.6 | 0.0071 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,551.4 | 0.0072 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 1,571.7 | 0.0060 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,585.3 | 0.0060 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 404.1 | 0.0062 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 403.8 | 0.0062 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 377.0 | 0.0061 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 380.2 | 0.0062 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.2 | 0.0046 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.9 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 75.9 | 0.0046 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.8 | 0.0047 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.2 | 0.0052 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 21.5 | 0.0053 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 8.7 | 0.0085 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 8.5 | 0.0083 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 401.1 | 0.0061 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 406.1 | 0.0062 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 39.3 | 0.0048 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 39.6 | 0.0048 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 75.9 | 0.0046 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.5 | 0.0047 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 20.5 | 0.0050 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 21.1 | 0.0052 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7,584.8 | 0.0072 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,618.4 | 0.0073 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,580.9 | 0.0060 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,588.1 | 0.0061 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,413.3 | 0.0071 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,654.9 | 0.0073 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,574.4 | 0.0072 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,634.6 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,675.2 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,602.1 | 0.0073 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 376.7 | 0.0061 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 380.0 | 0.0062 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.1 | 0.0046 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.9 | 0.0047 |

### `tag-pair-match` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 496.7 | 493.3 | 511.1 | 6.4 | 1.000x | 1.000x | 75 | 6.6 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 536.6 | 528.6 | 548.3 | 7.3 | 1.080x | 1.080x | 75 | 7.2 | 3.8 | 100% |

### `tail-digits-eol` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 868.8 | 0.0001 | 849.4 | 879.0 | 10.6 | 1.000x | 1.000x | **dominated**: `t-hyb-digits-4k` is 92.0% of this set |
| 2 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 4,670.1 | 0.0008 | 4,632.1 | 4,687.5 | 20.1 | 5.375x | 5.375x | **dominated**: `t-hyb-digits-4k` is 98.5% of this set |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `tail-digits-eol` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 8.8 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 8.6 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.4 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 3.2 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.0 | 0.0000 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0001 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.2 | 0.0002 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0002 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 799.3 | 0.1952 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 4,601.4 | 1.1234 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0030 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0030 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0000 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0004 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0004 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0002 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0008 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0008 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.2 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 3.2 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.3 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 10.7 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 10.1 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0002 |

### `tail-digits-eol` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 281.7 | 280.2 | 282.9 | 0.9 | 1.000x | 1.000x | 75 | 3.8 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 284.1 | 283.4 | 290.3 | 2.6 | 1.009x | 1.009x | 75 | 3.8 | 3.8 | 100% |

### `tail-dotstar-txt` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 70.4 | 0.0000 | 70.1 | 72.3 | 0.8 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 76.8 | 0.0000 | 76.4 | 77.1 | 0.2 | 1.091x | 1.091x |

#### `tail-dotstar-txt` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 3.3 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.6 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 3.4 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.7 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 3.0 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.4 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 3.2 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.5 | 0.0001 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.4 | 0.0002 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.4 | 0.0002 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0008 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.4 | 0.0008 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0030 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.4 | 0.0034 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.5 | 0.0001 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0004 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.5 | 0.0004 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.4 | 0.0002 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0008 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.4 | 0.0008 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 3.3 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.6 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 3.3 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.6 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.4 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.4 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 13.9 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 13.8 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 3.2 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.5 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.5 | 0.0002 |

### `tail-dotstar-txt` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 244.7 | 241.8 | 245.0 | 1.3 | 1.000x | 1.000x | 75 | 3.3 | 3.8 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 271.6 | 270.3 | 274.0 | 1.5 | 1.110x | 1.110x | 75 | 3.6 | 3.4 | 100% |

### `tail-ext-lower-txt` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 67.1 | 0.0000 | 66.6 | 68.5 | 0.7 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 68.2 | 0.0000 | 67.8 | 68.7 | 0.3 | 1.017x | 1.017x |

#### `tail-ext-lower-txt` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 3.2 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 3.0 | 0.0000 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.0 | 0.0000 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 3.2 | 0.0001 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0002 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0002 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0007 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0008 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.2 | 0.0031 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0030 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0000 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0004 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0004 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0002 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0007 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0008 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.2 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.2 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 11.0 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 12.2 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.0 | 0.0002 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3.2 | 0.0002 |

### `tail-ext-lower-txt` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 241.2 | 239.5 | 242.1 | 0.8 | 1.000x | 1.000x | 75 | 3.2 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 241.5 | 237.2 | 249.3 | 4.0 | 1.001x | 1.001x | 75 | 3.2 | 3.8 | 100% |

### `tail-space-eol` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 12,101.1 | 0.0020 | 11,894.8 | 13,396.0 | 545.4 | 1.000x | 1.000x | **dominated**: `t-trim-match-60k` is 99.3% of this set |
| 2 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 73,202.6 | 0.0120 | 73,120.0 | 73,325.7 | 73.4 | 6.049x | 6.049x | **dominated**: `t-trim-match-60k` is 99.9% of this set |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `tail-space-eol` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 8.1 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 8.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 8.2 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 8.0 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 8.0 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7.5 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.9 | 0.0000 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.0 | 0.0002 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0002 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.8 | 0.0002 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0007 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.9 | 0.0007 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0028 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.9 | 0.0028 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0000 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.9 | 0.0000 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0004 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.9 | 0.0004 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0002 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.9 | 0.0002 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0007 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.8 | 0.0007 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 8.1 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7.7 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 8.1 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7.5 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.9 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 9.1 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 8.4 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.9 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 12,014.6 | 0.1955 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 73,121.4 | 1.1901 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0002 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.8 | 0.0002 |

### `tail-space-eol` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 210.0 | 209.8 | 211.2 | 0.5 | 1.000x | 1.000x | 75 | 2.8 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 225.9 | 222.2 | 232.2 | 4.1 | 1.076x | 1.076x | 75 | 3.0 | 3.8 | 100% |

### `tail-word-eoz` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 12,948.7 | 0.0021 | 12,746.6 | 12,985.5 | 105.8 | 1.000x | 1.000x | **dominated**: `t-evil-match-60k` is 92.9% of this set |
| 2 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 73,685.1 | 0.0121 | 73,657.3 | 73,728.2 | 29.3 | 5.691x | 5.691x | **dominated**: `t-evil-match-60k` is 93.6% of this set |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `tail-word-eoz` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 3.7 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 3.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.0 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 3.4 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.8 | 0.0000 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 11,916.1 | 0.1939 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 68,980.3 | 1.1227 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3.4 | 0.0002 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.0 | 0.0002 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3.4 | 0.0002 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0002 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 806.9 | 0.1970 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 4,621.0 | 1.1282 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 10.0 | 0.0097 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 9.5 | 0.0093 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 9.4 | 0.0001 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 8.5 | 0.0001 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 10.3 | 0.0013 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 10.2 | 0.0012 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 9.4 | 0.0006 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 8.5 | 0.0005 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 11.1 | 0.0027 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 13.0 | 0.0032 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 3.4 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.0 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 3.4 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.0 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 10.5 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 10.8 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 3.4 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 9.6 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 8.7 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 3.5 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.0 | 0.0000 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 8.6 | 0.0005 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 8.4 | 0.0005 |

### `tail-word-eoz` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 483.5 | 476.2 | 489.8 | 5.3 | 1.000x | 1.000x | 75 | 6.4 | 3.8 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 694.3 | 691.4 | 700.8 | 3.3 | 1.436x | 1.436x | 75 | 9.3 | 3.4 | 100% |

### `trim-nested-star` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 69,489.0 | 0.0114 | 69,075.9 | 113,465.8 | 17,147.1 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 71,713.7 | 0.0117 | 70,816.8 | 126,209.5 | 21,289.6 | 1.032x | 1.032x |

#### `trim-nested-star` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.4 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 5.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 5.1 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 4.8 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 4.9 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.3 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 5.1 | 0.0001 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.1 | 0.0003 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 5.0 | 0.0003 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.9 | 0.0004 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 5.7 | 0.0003 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.8 | 0.0014 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 5.7 | 0.0014 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.9 | 0.0058 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 5.7 | 0.0055 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.7 | 0.0001 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 5.7 | 0.0001 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.9 | 0.0007 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 5.7 | 0.0007 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.8 | 0.0004 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 5.7 | 0.0003 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.9 | 0.0014 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 6.7 | 0.0016 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.8 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 5.7 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.8 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 5.7 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.7 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 5.8 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.9 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 5.7 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.8 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 5.8 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 59,373.5 | 0.9664 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 59,465.1 | 0.9679 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 9,760.5 | 0.5957 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 11,760.2 | 0.7177 |

### `trim-nested-star` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 401.7 | 399.5 | 419.3 | 7.4 | 1.000x | 1.000x | 75 | 5.4 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 407.0 | 403.6 | 422.2 | 6.5 | 1.013x | 1.013x | 75 | 5.4 | 3.8 | 100% |

### `utf8-lead-no-cont` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 2,307,278.1 | 0.3780 | 2,286,723.3 | 2,345,744.8 | 21,568.4 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 2,309,525.6 | 0.3784 | 2,292,702.3 | 2,362,351.3 | 28,335.9 | 1.001x | 1.001x |

#### `utf8-lead-no-cont` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 393,018.8 | 0.3748 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 398,356.6 | 0.3799 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 98,162.7 | 0.3745 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 99,645.0 | 0.3801 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 24,569.4 | 0.3749 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 24,892.3 | 0.3798 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 23,005.1 | 0.3744 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 23,281.0 | 0.3789 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 6,168.0 | 0.3764 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6,167.4 | 0.3764 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 6,138.5 | 0.3747 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6,153.6 | 0.3756 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 1,538.8 | 0.3757 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,553.0 | 0.3791 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 389.6 | 0.3804 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 389.3 | 0.3802 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 24,535.7 | 0.3744 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 24,740.2 | 0.3775 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 3,077.2 | 0.3756 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,088.8 | 0.3771 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 6,165.3 | 0.3763 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6,262.4 | 0.3822 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 1,536.3 | 0.3751 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,552.2 | 0.3790 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 393,398.1 | 0.3752 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 393,563.7 | 0.3754 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 98,125.7 | 0.3744 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 98,334.7 | 0.3752 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 395,415.1 | 0.3771 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 395,423.0 | 0.3771 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 393,574.5 | 0.3754 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 400,101.7 | 0.3816 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 394,682.0 | 0.3764 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 395,937.6 | 0.3776 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 23,562.9 | 0.3835 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 23,125.7 | 0.3764 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 6,265.7 | 0.3824 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6,257.7 | 0.3819 |

### `utf8-lead-no-cont` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 647.2 | 639.3 | 655.2 | 5.3 | 1.000x | 1.000x | 75 | 8.6 | 3.8 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 651.7 | 638.7 | 656.7 | 6.4 | 1.007x | 1.007x | 75 | 8.7 | 3.4 | 100% |

### `uuid-near-miss` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 48.0 | 0.0000 | 47.8 | 49.4 | 0.6 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 50.9 | 0.0000 | 50.8 | 51.0 | 0.1 | 1.060x | 1.060x |

#### `uuid-near-miss` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.7 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 2.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 2.7 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.7 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 2.7 | 0.0000 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.6 | 0.0000 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 2.7 | 0.0000 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.5 | 0.0002 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 2.7 | 0.0002 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.5 | 0.0002 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 2.7 | 0.0002 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.5 | 0.0006 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 2.7 | 0.0007 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.5 | 0.0024 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 2.7 | 0.0026 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.5 | 0.0000 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 2.7 | 0.0000 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.5 | 0.0003 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 2.7 | 0.0003 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.5 | 0.0002 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 2.7 | 0.0002 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.5 | 0.0006 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 2.7 | 0.0007 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.5 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 2.7 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.5 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 2.7 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.5 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 2.7 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.5 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 2.7 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.5 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 2.7 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.5 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 2.7 | 0.0000 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2.5 | 0.0002 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 2.7 | 0.0002 |

### `uuid-near-miss` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 311.4 | 309.0 | 334.3 | 9.6 | 1.000x | 1.000x | 75 | 4.2 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 331.8 | 329.7 | 338.2 | 2.9 | 1.066x | 1.066x | 75 | 4.4 | 3.8 | 100% |

### `wild-codegrammar-json-array-begin` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 77,539.7 | 0.0127 | 76,984.6 | 77,936.5 | 345.5 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 79,186.0 | 0.0130 | 78,117.8 | 80,418.1 | 748.6 | 1.021x | 1.021x |

#### `wild-codegrammar-json-array-begin` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 33,031.9 | 0.0315 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 33,888.2 | 0.0323 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,630.4 | 0.0291 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 7,822.0 | 0.0298 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,999.7 | 0.0305 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 2,025.3 | 0.0309 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 377.7 | 0.0061 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 380.3 | 0.0062 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 75.4 | 0.0046 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 75.9 | 0.0046 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.3 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 75.8 | 0.0046 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 20.5 | 0.0050 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 20.9 | 0.0051 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 12.1 | 0.0118 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 12.7 | 0.0124 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,551.0 | 0.0237 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 1,666.9 | 0.0254 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 186.1 | 0.0227 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 200.7 | 0.0245 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.8 | 0.0047 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 76.6 | 0.0047 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 21.4 | 0.0052 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 20.4 | 0.0050 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,556.5 | 0.0072 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7,545.0 | 0.0072 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,568.6 | 0.0060 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,591.5 | 0.0061 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,565.6 | 0.0072 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,823.2 | 0.0075 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,579.5 | 0.0072 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,644.8 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,553.1 | 0.0072 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,892.6 | 0.0075 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 373.6 | 0.0061 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 379.9 | 0.0062 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.2 | 0.0046 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 75.8 | 0.0046 |

### `wild-codegrammar-json-array-begin` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 255.9 | 254.7 | 266.2 | 4.5 | 1.000x | 1.000x | 75 | 3.4 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 290.3 | 289.7 | 293.1 | 1.3 | 1.135x | 1.135x | 75 | 3.9 | 3.8 | 100% |

### `wild-codegrammar-json-constant` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 6,120,657.5 | 1.0028 | 6,098,506.4 | 6,273,994.3 | 77,843.7 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 6,213,936.3 | 1.0180 | 6,163,076.8 | 6,260,689.7 | 34,061.3 | 1.015x | 1.015x |

#### `wild-codegrammar-json-constant` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 914,886.0 | 0.8725 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 932,245.2 | 0.8891 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 215,737.3 | 0.8230 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 224,639.3 | 0.8569 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 23,203.4 | 0.3541 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 23,050.6 | 0.3517 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 71,613.8 | 1.1656 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 72,130.0 | 1.1740 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 19,077.7 | 1.1643 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 19,226.3 | 1.1734 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,164.1 | 0.1931 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3,166.4 | 0.1933 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 787.4 | 0.1922 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 791.9 | 0.1933 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 505.4 | 0.4935 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 501.3 | 0.4895 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 28,215.6 | 0.4305 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 29,021.5 | 0.4428 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,371.9 | 0.4116 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 3,426.7 | 0.4183 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,162.0 | 0.4371 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 7,363.3 | 0.4494 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,578.1 | 0.3853 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 1,585.9 | 0.3872 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,227,044.5 | 1.1703 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 1,248,048.7 | 1.1903 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 288,359.4 | 1.1002 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 303,160.2 | 1.1567 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,103,570.3 | 1.0525 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 1,115,973.0 | 1.0643 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,096,198.0 | 1.0455 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 1,114,120.7 | 1.0626 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,095,922.4 | 1.0452 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 1,094,434.9 | 1.0438 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 13,831.7 | 0.2251 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 22,889.1 | 0.3725 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,129.7 | 0.1910 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 6,136.8 | 0.3745 |

### `wild-codegrammar-json-constant` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 790.2 | 781.2 | 792.6 | 4.2 | 1.000x | 1.000x | 75 | 10.5 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 802.9 | 794.9 | 814.7 | 6.7 | 1.016x | 1.016x | 75 | 10.7 | 3.8 | 100% |

### `wild-codegrammar-json-number-extended` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 5,374,756.8 | 0.8806 | 5,335,866.2 | 5,456,500.8 | 41,172.3 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 5,574,774.1 | 0.9133 | 5,532,783.0 | 5,596,951.5 | 23,658.9 | 1.037x | 1.037x |

#### `wild-codegrammar-json-number-extended` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 810,763.6 | 0.7732 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 811,734.4 | 0.7741 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 190,574.7 | 0.7270 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 192,693.4 | 0.7351 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 35,780.5 | 0.5460 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 35,978.1 | 0.5490 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 12,058.8 | 0.1963 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 11,734.5 | 0.1910 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,153.8 | 0.1925 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3,114.6 | 0.1901 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 33,730.8 | 2.0588 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 35,433.5 | 2.1627 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 9,283.2 | 2.2664 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 9,363.3 | 2.2860 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 548.3 | 0.5355 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 575.0 | 0.5615 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 39,348.7 | 0.6004 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 40,100.5 | 0.6119 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 4,675.3 | 0.5707 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 4,872.5 | 0.5948 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,123.6 | 0.1906 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3,140.3 | 0.1917 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5,811.5 | 1.4188 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 5,999.7 | 1.4648 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2,058,410.1 | 1.9632 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 2,183,087.9 | 2.0821 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 510,407.2 | 1.9474 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 545,261.6 | 2.0804 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 544,966.3 | 0.5197 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 565,035.8 | 0.5389 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 551,060.8 | 0.5256 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 564,816.8 | 0.5387 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 542,029.4 | 0.5169 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 567,464.4 | 0.5412 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 12,020.1 | 0.1956 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 11,675.3 | 0.1900 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,141.3 | 0.1917 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3,117.7 | 0.1903 |

### `wild-codegrammar-json-number-extended` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 636.1 | 628.7 | 649.3 | 6.8 | 1.000x | 1.000x | 75 | 8.5 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 674.1 | 671.2 | 679.1 | 3.1 | 1.060x | 1.060x | 75 | 9.0 | 3.8 | 100% |

### `wild-codegrammar-json-object-begin` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 43,412.9 | 0.0071 | 43,337.8 | 43,892.1 | 245.4 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 43,708.4 | 0.0072 | 43,232.3 | 44,055.6 | 344.9 | 1.007x | 1.007x |

#### `wild-codegrammar-json-object-begin` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,673.5 | 0.0073 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 7,610.6 | 0.0073 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,572.9 | 0.0060 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 1,579.7 | 0.0060 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 399.7 | 0.0061 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 400.4 | 0.0061 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 373.0 | 0.0061 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 374.6 | 0.0061 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 75.6 | 0.0046 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.2 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 75.5 | 0.0046 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 75.7 | 0.0046 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 20.4 | 0.0050 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 20.8 | 0.0051 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 11.9 | 0.0116 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 11.9 | 0.0116 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 605.8 | 0.0092 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 605.3 | 0.0092 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 79.0 | 0.0096 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 78.5 | 0.0096 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.7 | 0.0047 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 76.5 | 0.0047 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 21.4 | 0.0052 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 20.5 | 0.0050 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,609.8 | 0.0073 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7,607.2 | 0.0073 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,570.3 | 0.0060 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,578.0 | 0.0060 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,571.8 | 0.0072 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,587.7 | 0.0072 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,631.9 | 0.0073 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,629.6 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,612.1 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,745.1 | 0.0074 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 373.9 | 0.0061 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 374.4 | 0.0061 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.2 | 0.0047 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 75.9 | 0.0046 |

### `wild-codegrammar-json-object-begin` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 259.5 | 251.2 | 276.9 | 8.7 | 1.000x | 1.000x | 75 | 3.5 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 284.5 | 280.2 | 292.3 | 4.6 | 1.097x | 1.097x | 75 | 3.8 | 3.8 | 100% |

### `wild-codegrammar-json-stringcontent-escape` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 43,570.4 | 0.0071 | 42,895.0 | 43,918.5 | 395.2 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 43,806.3 | 0.0072 | 43,116.8 | 44,561.5 | 541.4 | 1.005x | 1.005x |

#### `wild-codegrammar-json-stringcontent-escape` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 7,591.7 | 0.0072 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,578.1 | 0.0072 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 1,579.8 | 0.0060 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,573.0 | 0.0060 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 401.5 | 0.0061 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 400.4 | 0.0061 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 376.1 | 0.0061 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 375.5 | 0.0061 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.7 | 0.0047 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.4 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 76.3 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.1 | 0.0046 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.2 | 0.0052 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 21.3 | 0.0052 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 8.0 | 0.0079 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 8.1 | 0.0079 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 400.2 | 0.0061 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 399.7 | 0.0061 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 40.3 | 0.0049 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 39.4 | 0.0048 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 76.8 | 0.0047 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.3 | 0.0047 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.3 | 0.0052 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 21.7 | 0.0053 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7,577.1 | 0.0072 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,615.8 | 0.0073 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,579.5 | 0.0060 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,572.0 | 0.0060 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,653.9 | 0.0073 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,684.6 | 0.0073 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,601.7 | 0.0072 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,669.1 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,575.3 | 0.0072 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,981.2 | 0.0076 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 376.6 | 0.0061 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 374.7 | 0.0061 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.6 | 0.0047 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.5 | 0.0047 |

### `wild-codegrammar-json-stringcontent-escape` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 313.7 | 313.6 | 322.9 | 4.4 | 1.000x | 1.000x | 75 | 4.2 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 345.5 | 343.3 | 346.6 | 1.2 | 1.101x | 1.101x | 75 | 4.6 | 3.8 | 100% |

### `wild-datetime-moment-iso8601` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 87,055.0 | 0.0143 | 86,846.8 | 87,227.0 | 126.3 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 87,298.7 | 0.0143 | 86,810.7 | 87,444.8 | 223.9 | 1.003x | 1.003x |

#### `wild-datetime-moment-iso8601` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 5.8 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 5.5 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.5 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.5 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 6.0 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.0 | 0.0001 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 5.9 | 0.0004 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.9 | 0.0004 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 8.0 | 0.0005 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7.9 | 0.0005 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 8.0 | 0.0020 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7.8 | 0.0019 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 6.3 | 0.0062 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.7 | 0.0055 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 6.3 | 0.0001 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.6 | 0.0001 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 6.3 | 0.0008 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.6 | 0.0007 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 6.3 | 0.0004 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.8 | 0.0004 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 8.1 | 0.0020 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7.9 | 0.0019 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 6.3 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.6 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 6.2 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.5 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 6.4 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.6 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 6.4 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.1 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 6.5 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.8 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 68,566.5 | 1.1160 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 68,856.4 | 1.1207 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 18,352.9 | 1.1201 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 18,280.0 | 1.1157 |

### `wild-datetime-moment-iso8601` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 501.0 | 494.0 | 516.7 | 8.7 | 1.000x | 1.000x | 75 | 6.7 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 540.4 | 512.7 | 550.0 | 12.7 | 1.079x | 1.079x | 75 | 7.2 | 3.8 | 100% |

### `wild-logparse-base10num-grok` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 8,589,732.2 | 1.4073 | 8,560,376.6 | 8,605,029.7 | 15,336.5 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 9,810,282.2 | 1.6072 | 9,753,200.7 | 9,885,401.5 | 50,243.6 | 1.142x | 1.142x |

#### `wild-logparse-base10num-grok` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,310,393.5 | 1.2497 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 1,535,660.7 | 1.4645 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 315,506.5 | 1.2036 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 368,536.0 | 1.4059 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 64,624.3 | 0.9861 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 77,211.2 | 1.1782 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 11,917.6 | 0.1940 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 16,363.1 | 0.2663 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,154.6 | 0.1925 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 4,192.3 | 0.2559 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 61,249.4 | 3.7384 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 72,805.8 | 4.4437 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 10,396.0 | 2.5381 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 12,807.1 | 3.1267 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,086.2 | 1.0608 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 1,297.2 | 1.2668 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 77,123.3 | 1.1768 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 92,633.6 | 1.4135 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 8,981.7 | 1.0964 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 10,677.4 | 1.3034 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,178.7 | 0.1940 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 4,192.0 | 0.2559 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 10,954.3 | 2.6744 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 13,485.5 | 3.2923 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,121,655.0 | 2.9773 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 3,395,484.9 | 3.2384 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 783,050.5 | 2.9877 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 857,774.2 | 3.2728 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 926,238.5 | 0.8834 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 1,116,442.5 | 1.0648 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 935,317.3 | 0.8920 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 1,108,685.6 | 1.0574 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 933,486.3 | 0.8903 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 1,109,919.3 | 1.0586 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 11,725.9 | 0.1909 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 15,635.2 | 0.2545 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,128.2 | 0.1909 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 4,172.5 | 0.2547 |

### `wild-logparse-base10num-grok` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 1,001.1 | 995.9 | 1,010.8 | 5.5 | 1.000x | 1.000x | 75 | 13.3 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 1,196.8 | 1,193.5 | 1,202.2 | 2.8 | 1.195x | 1.195x | 75 | 16.0 | 3.8 | 100% |

### `wild-logparse-base10num-noatomic` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 6,186,487.7 | 1.0135 | 6,180,041.3 | 6,228,911.4 | 18,515.1 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 7,518,198.7 | 1.2317 | 7,443,785.2 | 7,545,831.1 | 35,124.9 | 1.215x | 1.215x |

#### `wild-logparse-base10num-noatomic` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 878,366.6 | 0.8377 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 1,140,932.5 | 1.0881 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 212,925.8 | 0.8122 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 273,552.3 | 1.0435 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 37,847.5 | 0.5775 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 51,692.6 | 0.7888 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 12,196.2 | 0.1985 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 17,696.5 | 0.2880 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,175.3 | 0.1938 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 4,174.0 | 0.2547 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 30,368.8 | 1.8536 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 42,818.6 | 2.6134 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 9,367.2 | 2.2869 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 11,702.7 | 2.8571 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 646.8 | 0.6316 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 821.5 | 0.8023 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 44,324.1 | 0.6763 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 57,728.3 | 0.8809 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5,374.3 | 0.6560 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 7,170.2 | 0.8753 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 4,006.9 | 0.2446 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 4,292.8 | 0.2620 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5,875.9 | 1.4346 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 8,328.5 | 2.0333 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2,240,890.5 | 2.1372 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 2,508,401.6 | 2.3924 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 554,772.3 | 2.1167 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 631,532.5 | 2.4096 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 718,807.1 | 0.6855 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 917,759.9 | 0.8753 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 716,461.0 | 0.6833 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 917,691.8 | 0.8752 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 721,029.8 | 0.6877 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 914,236.0 | 0.8719 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 12,055.3 | 0.1962 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 15,637.1 | 0.2545 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,154.3 | 0.1925 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 4,175.4 | 0.2548 |

### `wild-logparse-base10num-noatomic` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 668.6 | 665.2 | 672.5 | 2.4 | 1.000x | 1.000x | 75 | 8.9 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 850.3 | 847.6 | 854.1 | 2.2 | 1.272x | 1.272x | 75 | 11.3 | 3.8 | 100% |

### `wild-logparse-quotedstring-grok` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 1,411,081.4 | 0.2312 | 1,403,438.9 | 1,420,470.7 | 6,820.1 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 1,418,766.7 | 0.2324 | 1,396,553.0 | 1,421,346.8 | 9,377.6 | 1.005x | 1.005x |

#### `wild-logparse-quotedstring-grok` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 358,529.8 | 0.3419 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 354,017.1 | 0.3376 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 87,275.9 | 0.3329 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 87,671.2 | 0.3344 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 21,632.6 | 0.3301 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 21,552.1 | 0.3289 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 12,081.2 | 0.1966 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 13,424.4 | 0.2185 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,160.0 | 0.1929 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3,144.2 | 0.1919 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,135.9 | 0.1914 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3,113.6 | 0.1900 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 788.7 | 0.1925 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 787.9 | 0.1924 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 540.1 | 0.5274 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 685.3 | 0.6693 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 35,222.2 | 0.5374 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 33,438.8 | 0.5102 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 4,762.4 | 0.5813 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 4,547.2 | 0.5551 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,178.2 | 0.1940 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3,177.1 | 0.1939 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 795.0 | 0.1941 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 784.2 | 0.1914 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 204,375.4 | 0.1949 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 204,365.8 | 0.1949 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 50,963.7 | 0.1944 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 50,241.7 | 0.1917 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 204,548.8 | 0.1951 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 204,489.3 | 0.1950 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 202,542.1 | 0.1932 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 202,106.0 | 0.1928 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 204,418.3 | 0.1950 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 202,627.7 | 0.1932 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 12,096.1 | 0.1969 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 11,994.5 | 0.1952 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,161.8 | 0.1930 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3,112.0 | 0.1899 |

### `wild-logparse-quotedstring-grok` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 909.8 | 907.7 | 910.3 | 0.9 | 1.000x | 1.000x | 75 | 12.1 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 957.1 | 954.9 | 960.2 | 2.2 | 1.052x | 1.052x | 75 | 12.8 | 3.8 | 100% |

### `wild-logparse-quotedstring-noatomic` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 1,315,190.6 | 0.2155 | 1,297,298.4 | 1,324,382.7 | 11,863.4 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 1,318,229.2 | 0.2160 | 1,302,072.6 | 1,324,683.8 | 8,130.1 | 1.002x | 1.002x |

#### `wild-logparse-quotedstring-noatomic` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 290,423.2 | 0.2770 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 292,880.6 | 0.2793 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 70,725.1 | 0.2698 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 71,425.6 | 0.2725 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 17,466.0 | 0.2665 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 18,034.2 | 0.2752 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 11,860.9 | 0.1930 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 11,895.8 | 0.1936 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,163.4 | 0.1931 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3,152.0 | 0.1924 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,163.6 | 0.1931 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3,172.0 | 0.1936 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 795.8 | 0.1943 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 801.4 | 0.1957 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 354.1 | 0.3458 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 351.4 | 0.3432 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 23,291.4 | 0.3554 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 23,155.3 | 0.3533 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2,912.9 | 0.3556 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 2,890.1 | 0.3528 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,175.0 | 0.1938 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3,245.1 | 0.1981 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 796.6 | 0.1945 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 793.5 | 0.1937 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 204,847.3 | 0.1954 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 203,759.4 | 0.1943 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 50,295.6 | 0.1919 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 50,617.6 | 0.1931 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 204,664.1 | 0.1952 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 205,391.4 | 0.1959 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 204,424.5 | 0.1950 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 202,406.9 | 0.1930 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 204,098.2 | 0.1947 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 205,424.8 | 0.1959 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 11,837.9 | 0.1927 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 11,861.8 | 0.1931 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,160.0 | 0.1929 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3,150.0 | 0.1923 |

### `wild-logparse-quotedstring-noatomic` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 661.1 | 658.0 | 665.2 | 3.1 | 1.000x | 1.000x | 75 | 8.8 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 698.3 | 691.0 | 700.8 | 3.8 | 1.056x | 1.056x | 75 | 9.3 | 3.8 | 100% |

### `wild-logparse-syslogbase-expanded` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 2,195,937.5 | 0.3598 | 2,193,073.6 | 2,214,465.5 | 7,702.6 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 2,196,542.0 | 0.3599 | 2,182,113.4 | 2,226,505.5 | 19,204.2 | 1.000x | 1.000x |

#### `wild-logparse-syslogbase-expanded` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 1,646,810.5 | 1.5705 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,647,863.8 | 1.5715 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 402,100.6 | 1.5339 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 402,278.9 | 1.5346 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 36,608.6 | 0.5586 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 37,273.9 | 0.5688 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 373.4 | 0.0061 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 373.9 | 0.0061 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 75.5 | 0.0046 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 75.3 | 0.0046 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 76.7 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.8 | 0.0047 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.6 | 0.0053 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 21.2 | 0.0052 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 993.1 | 0.9699 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 988.6 | 0.9655 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 56,767.7 | 0.8662 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 56,454.2 | 0.8614 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 7,028.0 | 0.8579 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,022.2 | 0.8572 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 10,747.5 | 0.6560 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 10,736.9 | 0.6553 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 2,588.0 | 0.6318 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2,595.4 | 0.6337 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7,623.0 | 0.0073 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,590.3 | 0.0072 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,579.4 | 0.0060 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,578.1 | 0.0060 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,522.8 | 0.0072 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,557.7 | 0.0072 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,603.2 | 0.0073 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,610.6 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,565.7 | 0.0072 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,648.1 | 0.0073 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 373.5 | 0.0061 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 373.6 | 0.0061 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 75.6 | 0.0046 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.6 | 0.0047 |

### `wild-logparse-syslogbase-expanded` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 703.7 | 698.5 | 726.8 | 10.0 | 1.000x | 1.000x | 75 | 9.4 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 738.7 | 732.2 | 790.2 | 21.6 | 1.050x | 1.050x | 75 | 9.8 | 3.8 | 100% |

### `wild-logparse-winpath-grok` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 43,408.0 | 0.0071 | 43,056.4 | 44,182.8 | 459.2 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 43,925.4 | 0.0072 | 43,330.0 | 44,097.1 | 292.7 | 1.012x | 1.012x |

#### `wild-logparse-winpath-grok` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 7,555.8 | 0.0072 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,625.9 | 0.0073 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 1,572.9 | 0.0060 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,574.6 | 0.0060 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 403.2 | 0.0062 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 403.2 | 0.0062 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 378.8 | 0.0062 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 376.4 | 0.0061 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.9 | 0.0047 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.8 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 77.3 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.2 | 0.0047 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.2 | 0.0052 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 21.5 | 0.0052 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 8.8 | 0.0086 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 8.7 | 0.0085 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 403.6 | 0.0062 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 401.7 | 0.0061 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 39.7 | 0.0048 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 40.1 | 0.0049 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 77.2 | 0.0047 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.6 | 0.0047 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.2 | 0.0052 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 21.2 | 0.0052 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7,557.6 | 0.0072 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,781.0 | 0.0074 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,582.8 | 0.0060 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,572.7 | 0.0060 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,699.0 | 0.0073 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,629.8 | 0.0073 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,850.0 | 0.0075 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,845.3 | 0.0075 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,607.2 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,853.1 | 0.0075 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 378.1 | 0.0062 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 376.2 | 0.0061 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.5 | 0.0047 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.2 | 0.0047 |

### `wild-logparse-winpath-grok` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 447.7 | 445.3 | 454.4 | 3.3 | 1.000x | 1.000x | 75 | 6.0 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 488.3 | 485.3 | 491.6 | 2.4 | 1.091x | 1.091x | 75 | 6.5 | 3.8 | 100% |

### `wild-secrets-aws-access-key-id` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 86,897.8 | 0.0142 | 86,348.5 | 89,403.9 | 1,129.2 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 86,933.2 | 0.0142 | 86,276.7 | 87,170.1 | 352.4 | 1.000x | 1.000x |

#### `wild-secrets-aws-access-key-id` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 17,071.1 | 0.0163 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 16,841.3 | 0.0161 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,939.8 | 0.0150 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 3,970.3 | 0.0151 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 968.6 | 0.0148 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 967.3 | 0.0148 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 383.4 | 0.0062 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 387.0 | 0.0063 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 77.1 | 0.0047 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.8 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.2 | 0.0046 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 77.2 | 0.0047 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 22.2 | 0.0054 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 22.0 | 0.0054 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 111.2 | 0.1086 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 111.3 | 0.1087 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,402.2 | 0.1129 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 7,441.3 | 0.1135 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 966.2 | 0.1179 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 970.0 | 0.1184 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 78.2 | 0.0048 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 77.9 | 0.0048 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 22.3 | 0.0054 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 22.2 | 0.0054 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 17,968.2 | 0.0171 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 18,036.1 | 0.0172 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 4,239.3 | 0.0162 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 4,209.7 | 0.0161 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 10,926.4 | 0.0104 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 11,064.1 | 0.0106 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 11,288.7 | 0.0108 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 10,949.5 | 0.0104 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 10,950.5 | 0.0104 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 11,010.2 | 0.0105 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 379.7 | 0.0062 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 381.7 | 0.0062 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.9 | 0.0047 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.9 | 0.0047 |

### `wild-secrets-aws-access-key-id` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 590.6 | 587.7 | 608.8 | 7.8 | 1.000x | 1.000x | 75 | 7.9 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 629.3 | 618.6 | 634.6 | 5.3 | 1.066x | 1.066x | 75 | 8.4 | 3.8 | 100% |

### `wild-secrets-github-pat` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 363,914.4 | 0.0596 | 361,189.6 | 367,104.8 | 2,220.2 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 365,023.9 | 0.0598 | 362,943.4 | 365,487.6 | 1,068.8 | 1.003x | 1.003x |

#### `wild-secrets-github-pat` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 30,421.3 | 0.0290 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 30,191.4 | 0.0288 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,162.5 | 0.0273 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 7,193.1 | 0.0274 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,724.4 | 0.0263 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 1,736.9 | 0.0265 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 379.2 | 0.0062 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 378.5 | 0.0062 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 75.8 | 0.0046 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 75.8 | 0.0046 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 75.0 | 0.0046 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 75.7 | 0.0046 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 20.3 | 0.0049 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.0 | 0.0051 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 377.1 | 0.3683 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 378.6 | 0.3697 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 13,100.1 | 0.1999 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 13,245.8 | 0.2021 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,668.5 | 0.2037 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 1,687.7 | 0.2060 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.7 | 0.0047 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 76.6 | 0.0047 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 79.2 | 0.0193 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 84.0 | 0.0205 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 228,925.7 | 0.2183 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 230,736.0 | 0.2201 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 55,054.7 | 0.2101 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 55,229.1 | 0.2107 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,578.8 | 0.0072 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,686.5 | 0.0073 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,573.2 | 0.0072 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,555.3 | 0.0072 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,845.2 | 0.0075 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,544.8 | 0.0072 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 377.2 | 0.0061 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 378.8 | 0.0062 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.0 | 0.0046 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 75.8 | 0.0046 |

### `wild-secrets-github-pat` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 429.2 | 426.9 | 442.4 | 5.8 | 1.000x | 1.000x | 75 | 5.7 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 447.1 | 442.7 | 454.2 | 4.0 | 1.042x | 1.042x | 75 | 6.0 | 3.8 | 100% |

### `wild-secrets-slack-webhook-url` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 219,918.3 | 0.0360 | 218,165.9 | 220,595.0 | 1,027.2 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 220,890.4 | 0.0362 | 220,150.6 | 224,090.1 | 1,434.3 | 1.004x | 1.004x |

#### `wild-secrets-slack-webhook-url` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 117,036.7 | 0.1116 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 117,470.1 | 0.1120 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 28,756.9 | 0.1097 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 28,898.4 | 0.1102 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 6,772.4 | 0.1033 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6,818.8 | 0.1040 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 379.0 | 0.0062 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 375.9 | 0.0061 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.3 | 0.0047 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.2 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 13,083.1 | 0.7985 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 13,115.1 | 0.8005 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 20.7 | 0.0050 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 21.2 | 0.0052 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 358.5 | 0.3501 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 374.6 | 0.3658 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 18,402.6 | 0.2808 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 18,864.2 | 0.2878 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 2,469.2 | 0.3014 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2,549.1 | 0.3112 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 77.7 | 0.0047 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 77.4 | 0.0047 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 123.4 | 0.0301 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 123.8 | 0.0302 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7,611.7 | 0.0073 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,556.0 | 0.0072 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,580.1 | 0.0060 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,577.2 | 0.0060 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,586.8 | 0.0072 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,598.2 | 0.0072 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,522.6 | 0.0072 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,615.6 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,602.5 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,603.8 | 0.0073 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 379.5 | 0.0062 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 379.9 | 0.0062 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.2 | 0.0046 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 75.6 | 0.0046 |

### `wild-secrets-slack-webhook-url` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 610.2 | 606.3 | 623.2 | 5.8 | 1.000x | 1.000x | 75 | 8.1 | 3.8 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 612.1 | 605.2 | 645.9 | 14.6 | 1.003x | 1.003x | 75 | 8.2 | 3.4 | 100% |

### `wild-secrets-username-password-pair` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 316,816.9 | 0.0519 | 313,604.6 | 325,438.3 | 4,140.5 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 331,320.9 | 0.0543 | 327,265.1 | 336,099.5 | 3,752.8 | 1.046x | 1.046x |

#### `wild-secrets-username-password-pair` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 7,612.1 | 0.0073 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,588.5 | 0.0072 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 1,583.1 | 0.0060 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,584.2 | 0.0060 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 399.7 | 0.0061 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 398.5 | 0.0061 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 377.9 | 0.0062 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 377.2 | 0.0061 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.9 | 0.0047 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.3 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 76.2 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.5 | 0.0047 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.9 | 0.0054 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 21.0 | 0.0051 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 369.7 | 0.3610 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 374.1 | 0.3654 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 20,259.3 | 0.3091 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 20,232.5 | 0.3087 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 2,250.1 | 0.2747 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2,254.3 | 0.2752 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 78.1 | 0.0048 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.1 | 0.0046 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 294.1 | 0.0718 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 288.6 | 0.0704 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 228,450.2 | 0.2179 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 242,441.6 | 0.2312 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 32,032.4 | 0.1222 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 32,207.8 | 0.1229 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,579.1 | 0.0072 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,549.5 | 0.0072 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,595.3 | 0.0072 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,643.7 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,535.9 | 0.0072 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,632.4 | 0.0073 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 379.5 | 0.0062 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 378.9 | 0.0062 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.7 | 0.0047 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.2 | 0.0046 |

### `wild-secrets-username-password-pair` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 507.7 | 505.8 | 514.7 | 3.4 | 1.000x | 1.000x | 75 | 6.8 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 527.5 | 526.2 | 530.5 | 1.7 | 1.039x | 1.039x | 75 | 7.0 | 3.8 | 100% |

### `wild-semdiv-altorder-foo-foobar-rustregex` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 504,755.3 | 0.0827 | 503,984.7 | 512,151.4 | 3,195.5 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 528,246.6 | 0.0865 | 527,900.5 | 535,977.2 | 3,094.7 | 1.047x | 1.047x |

#### `wild-semdiv-altorder-foo-foobar-rustregex` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 74,308.3 | 0.0709 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 74,894.0 | 0.0714 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 18,734.6 | 0.0715 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 18,610.4 | 0.0710 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 4,830.7 | 0.0737 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 4,804.5 | 0.0733 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 8,512.0 | 0.1385 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 8,425.3 | 0.1371 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 2,301.1 | 0.1404 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2,266.8 | 0.1383 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 76.0 | 0.0046 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 74.9 | 0.0046 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 20.5 | 0.0050 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 20.2 | 0.0049 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 55.4 | 0.0541 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 53.8 | 0.0525 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 3,869.9 | 0.0591 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,813.7 | 0.0582 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 533.6 | 0.0651 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 526.2 | 0.0642 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 1,508.5 | 0.0921 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,504.7 | 0.0918 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 493.3 | 0.1204 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 498.6 | 0.1217 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 108,200.2 | 0.1032 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 130,494.6 | 0.1245 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 25,387.0 | 0.0969 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 25,273.0 | 0.0964 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 86,169.0 | 0.0822 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 85,915.4 | 0.0819 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 85,147.9 | 0.0812 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 85,311.0 | 0.0814 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 85,246.4 | 0.0813 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 85,470.4 | 0.0815 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 370.0 | 0.0060 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 369.7 | 0.0060 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 75.9 | 0.0046 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 75.1 | 0.0046 |

### `wild-semdiv-altorder-foo-foobar-rustregex` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 264.5 | 262.5 | 268.0 | 2.2 | 1.000x | 1.000x | 75 | 3.5 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 290.7 | 285.4 | 305.1 | 7.5 | 1.099x | 1.099x | 75 | 3.9 | 3.8 | 100% |

### `wild-semdiv-dollar-trailing-newline-pcre2` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 59.8 | 0.0000 | 59.3 | 60.1 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 60.0 | 0.0000 | 59.9 | 60.3 | 0.1 | 1.003x | 1.003x |

#### `wild-semdiv-dollar-trailing-newline-pcre2` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.2 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 3.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 3.3 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 3.0 | 0.0000 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 3.3 | 0.0001 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0002 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3.2 | 0.0002 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0002 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0008 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0008 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0030 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0030 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0000 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0004 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0004 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0002 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0008 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0008 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.3 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 3.3 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.3 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 3.3 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.2 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.1 | 0.0002 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0002 |

### `wild-semdiv-dollar-trailing-newline-pcre2` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 229.3 | 228.4 | 235.8 | 3.3 | 1.000x | 1.000x | 75 | 3.1 | 3.8 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 230.6 | 229.8 | 235.0 | 1.9 | 1.006x | 1.006x | 75 | 3.1 | 3.4 | 100% |

### `wild-semdiv-empty-alt-repeat-pcre2` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 14,970,475.9 | 2.4527 | 14,911,875.4 | 15,123,574.9 | 81,493.0 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 15,156,825.7 | 2.4832 | 14,993,945.1 | 15,706,240.9 | 253,160.5 | 1.012x | 1.012x |

#### `wild-semdiv-empty-alt-repeat-pcre2` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 2,291,338.3 | 2.1852 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2,293,447.7 | 2.1872 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 558,037.7 | 2.1287 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 564,095.0 | 2.1519 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 127,374.7 | 1.9436 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 130,823.9 | 1.9962 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 23,272.3 | 0.3788 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 12,691.1 | 0.2066 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3,125.4 | 0.1907 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,118.5 | 0.1903 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 181,279.6 | 11.0644 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 184,872.3 | 11.2837 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 57,459.6 | 14.0282 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 60,440.4 | 14.7560 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 1,793.5 | 1.7515 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,794.6 | 1.7525 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 138,580.8 | 2.1146 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 139,194.2 | 2.1239 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 16,316.3 | 1.9917 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 16,418.4 | 2.0042 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 4,422.4 | 0.2699 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,177.1 | 0.1939 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 27,508.8 | 6.7160 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 28,114.2 | 6.8638 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 4,943,654.9 | 4.7150 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5,022,277.8 | 4.7900 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,248,014.4 | 4.7617 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,264,280.7 | 4.8238 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 1,786,748.9 | 1.7041 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,805,595.5 | 1.7220 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 1,788,208.8 | 1.7055 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,790,271.4 | 1.7074 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 1,783,082.9 | 1.7006 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,796,781.0 | 1.7136 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 11,901.6 | 0.1937 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 11,963.7 | 0.1947 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3,126.6 | 0.1908 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,116.2 | 0.1902 |

### `wild-semdiv-empty-alt-repeat-pcre2` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 1,396.6 | 1,393.8 | 1,422.6 | 10.8 | 1.000x | 1.000x | 75 | 18.6 | 3.8 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 1,546.0 | 1,478.3 | 1,570.9 | 37.7 | 1.107x | 1.107x | 75 | 20.6 | 3.4 | 100% |

### `wild-validator-email-owasp` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 31,216.0 | 0.0051 | 31,198.8 | 31,268.5 | 24.5 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 31,216.6 | 0.0051 | 31,149.7 | 31,397.2 | 86.4 | 1.000x | 1.000x |

#### `wild-validator-email-owasp` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.9 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 6.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.6 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 5.5 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.1 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 23,293.1 | 0.3791 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 23,271.1 | 0.3788 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6,238.5 | 0.3807 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 6,234.0 | 0.3805 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.3 | 0.0003 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 6.0 | 0.0004 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,567.5 | 0.3827 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 1,556.3 | 0.3799 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 29.0 | 0.0283 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 30.3 | 0.0296 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 29.8 | 0.0005 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 29.1 | 0.0004 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 29.1 | 0.0036 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 30.3 | 0.0037 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7.8 | 0.0005 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 8.6 | 0.0005 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.8 | 0.0009 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 4.0 | 0.0010 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 8.2 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 8.8 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.3 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 7.1 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.5 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 6.6 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.5 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 6.8 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 6.5 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 6.6 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.8 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 3.9 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.8 | 0.0002 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 4.0 | 0.0002 |

### `wild-validator-email-owasp` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 511.1 | 509.6 | 523.0 | 4.9 | 1.000x | 1.000x | 75 | 6.8 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 532.5 | 519.5 | 562.5 | 16.6 | 1.042x | 1.042x | 75 | 7.1 | 3.8 | 100% |

### `wild-validator-ipv4-owasp` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 104.0 | 0.0000 | 101.7 | 105.3 | 1.3 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 108.1 | 0.0000 | 105.8 | 109.3 | 1.3 | 1.039x | 1.039x |

#### `wild-validator-ipv4-owasp` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 5.6 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.2 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 5.5 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.2 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.4 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 5.5 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.6 | 0.0001 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0003 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.5 | 0.0003 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 5.5 | 0.0003 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.8 | 0.0004 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 5.5 | 0.0013 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.8 | 0.0014 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 5.6 | 0.0055 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.8 | 0.0057 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 5.5 | 0.0001 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.8 | 0.0001 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 5.5 | 0.0007 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.8 | 0.0007 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 5.3 | 0.0003 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.8 | 0.0004 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 5.5 | 0.0013 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.8 | 0.0014 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 5.5 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.8 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 5.3 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.8 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 5.5 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.8 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 5.3 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.8 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 5.5 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.8 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 5.6 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.8 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 5.6 | 0.0003 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.8 | 0.0004 |

### `wild-validator-ipv4-owasp` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 449.2 | 430.7 | 451.9 | 9.6 | 1.000x | 1.000x | 75 | 6.0 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 463.5 | 449.2 | 472.2 | 9.3 | 1.032x | 1.032x | 75 | 6.2 | 3.8 | 100% |

### `wild-validator-us-zip-owasp` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 93.4 | 0.0000 | 93.1 | 93.9 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 95.8 | 0.0000 | 95.4 | 95.9 | 0.2 | 1.025x | 1.025x |

#### `wild-validator-us-zip-owasp` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 4.8 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5.1 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 5.1 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 4.9 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 5.0 | 0.0001 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 4.9 | 0.0003 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 5.0 | 0.0003 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 4.9 | 0.0003 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 5.1 | 0.0003 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 4.9 | 0.0012 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 5.1 | 0.0012 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 4.9 | 0.0048 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 5.0 | 0.0049 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 4.9 | 0.0001 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 5.1 | 0.0001 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 4.9 | 0.0006 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 5.0 | 0.0006 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 4.9 | 0.0003 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 5.0 | 0.0003 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 4.9 | 0.0012 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 5.0 | 0.0012 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 4.9 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 4.9 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 4.9 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 4.9 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 4.9 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 4.9 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 5.0 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 4.9 | 0.0003 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 5.0 | 0.0003 |

### `wild-validator-us-zip-owasp` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 413.5 | 412.0 | 431.8 | 9.2 | 1.000x | 1.000x | 75 | 5.5 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 451.1 | 428.0 | 454.5 | 11.9 | 1.091x | 1.091x | 75 | 6.0 | 3.8 | 100% |

### `wild-validator-uuid-grok` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 63,355.0 | 0.0104 | 63,144.2 | 63,549.1 | 128.9 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 64,046.6 | 0.0105 | 63,474.8 | 64,687.1 | 462.6 | 1.011x | 1.011x |

#### `wild-validator-uuid-grok` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 19,326.1 | 0.0184 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 19,414.4 | 0.0185 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 4,485.6 | 0.0171 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 4,576.9 | 0.0175 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 1,177.1 | 0.0180 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,197.9 | 0.0183 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 381.2 | 0.0062 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 384.3 | 0.0063 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 75.7 | 0.0046 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 75.6 | 0.0046 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 4,066.9 | 0.2482 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 4,250.5 | 0.2594 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 20.4 | 0.0050 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 20.6 | 0.0050 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 8.0 | 0.0078 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7.6 | 0.0074 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 984.2 | 0.0150 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 999.8 | 0.0153 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 116.3 | 0.0142 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 117.2 | 0.0143 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 75.5 | 0.0046 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 75.6 | 0.0046 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 240.3 | 0.0587 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 245.4 | 0.0599 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7,543.6 | 0.0072 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,611.9 | 0.0073 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,583.1 | 0.0060 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,580.3 | 0.0060 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,467.9 | 0.0071 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,607.0 | 0.0073 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,649.7 | 0.0073 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,619.7 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,551.8 | 0.0072 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,675.2 | 0.0073 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 377.8 | 0.0061 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 377.2 | 0.0061 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.0 | 0.0046 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 75.8 | 0.0046 |

### `wild-validator-uuid-grok` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 307.2 | 303.7 | 309.4 | 2.0 | 1.000x | 1.000x | 75 | 4.1 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 316.7 | 315.4 | 320.2 | 1.7 | 1.031x | 1.031x | 75 | 4.2 | 3.8 | 100% |

### `wild-waf-crs-942140-dbnames` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 9,157,111.5 | 1.5002 | 9,094,553.5 | 9,282,668.0 | 66,873.3 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 9,176,841.6 | 1.5035 | 9,124,069.7 | 9,210,030.3 | 32,593.5 | 1.002x | 1.002x |

#### `wild-waf-crs-942140-dbnames` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,513,411.1 | 1.4433 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 1,510,700.0 | 1.4407 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 367,966.5 | 1.4037 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 370,707.8 | 1.4141 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 35,704.7 | 0.5448 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 34,991.9 | 0.5339 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 71,617.3 | 1.1656 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 71,322.4 | 1.1608 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 19,386.1 | 1.1832 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 18,947.7 | 1.1564 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,179.4 | 0.1941 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 4,687.9 | 0.2861 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 785.8 | 0.1918 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 789.5 | 0.1928 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 686.3 | 0.6703 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 686.3 | 0.6703 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 40,014.0 | 0.6106 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 40,150.6 | 0.6126 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 5,015.1 | 0.6122 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 4,915.4 | 0.6000 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 9,594.6 | 0.5856 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 9,578.6 | 0.5846 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2,280.1 | 0.5567 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 2,172.3 | 0.5304 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,862,019.4 | 1.7759 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 1,852,812.3 | 1.7671 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 455,459.6 | 1.7378 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 450,744.7 | 1.7198 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,590,718.1 | 1.5171 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 1,602,679.4 | 1.5285 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,607,833.9 | 1.5334 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 1,591,051.2 | 1.5174 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,584,867.2 | 1.5115 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 1,596,262.7 | 1.5224 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 12,782.0 | 0.2080 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 14,076.9 | 0.2291 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,118.9 | 0.1903 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3,104.4 | 0.1895 |

### `wild-waf-crs-942140-dbnames` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 957.7 | 955.3 | 971.4 | 7.1 | 1.000x | 1.000x | 75 | 12.8 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 991.2 | 986.7 | 995.0 | 2.9 | 1.035x | 1.035x | 75 | 13.2 | 3.8 | 100% |

### `wild-waf-crs-942160-sleep-benchmark` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 751,444.9 | 0.1231 | 748,043.0 | 766,373.2 | 8,041.9 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 754,205.3 | 0.1236 | 749,826.3 | 759,030.3 | 3,409.4 | 1.004x | 1.004x |

#### `wild-waf-crs-942160-sleep-benchmark` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 550,544.9 | 0.5250 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 552,143.4 | 0.5266 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 129,901.7 | 0.4955 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 130,124.9 | 0.4964 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 18,346.2 | 0.2799 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 18,601.0 | 0.2838 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 369.3 | 0.0060 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 371.2 | 0.0060 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 74.8 | 0.0046 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 75.4 | 0.0046 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.3 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 75.5 | 0.0046 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 20.6 | 0.0050 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.0 | 0.0051 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 292.7 | 0.2858 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 297.6 | 0.2907 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 18,100.7 | 0.2762 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 18,476.9 | 0.2819 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2,229.8 | 0.2722 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 2,329.6 | 0.2844 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.7 | 0.0047 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 76.6 | 0.0047 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 20.4 | 0.0050 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 20.7 | 0.0051 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,676.4 | 0.0073 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7,572.7 | 0.0072 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,572.7 | 0.0060 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,578.6 | 0.0060 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,647.0 | 0.0073 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,525.6 | 0.0072 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,592.2 | 0.0072 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,545.7 | 0.0072 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,629.8 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,644.9 | 0.0073 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 372.7 | 0.0061 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 373.8 | 0.0061 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 74.9 | 0.0046 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 75.2 | 0.0046 |

### `wild-waf-crs-942160-sleep-benchmark` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 310.1 | 305.9 | 319.8 | 4.6 | 1.000x | 1.000x | 75 | 4.1 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 325.4 | 323.8 | 326.7 | 1.1 | 1.050x | 1.050x | 75 | 4.3 | 3.8 | 100% |

### `wild-waf-crs-942270-union-select` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 1,421,956.0 | 0.2330 | 1,406,716.5 | 1,448,357.1 | 14,514.1 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 1,454,740.3 | 0.2383 | 1,437,853.8 | 1,459,981.5 | 9,331.9 | 1.023x | 1.023x |

#### `wild-waf-crs-942270-union-select` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 172,441.9 | 0.1645 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 181,619.3 | 0.1732 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 30,924.1 | 0.1180 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 31,162.2 | 0.1189 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,571.1 | 0.1155 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 7,616.4 | 0.1162 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 11,508.8 | 0.1873 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 11,624.6 | 0.1892 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,047.6 | 0.1860 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3,078.9 | 0.1879 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 185.1 | 0.0113 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 185.0 | 0.0113 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 65.4 | 0.0160 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 65.8 | 0.0161 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 177.6 | 0.1735 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 177.6 | 0.1735 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 8,235.2 | 0.1257 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 8,343.7 | 0.1273 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,103.5 | 0.1347 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 1,111.3 | 0.1357 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,348.3 | 0.2044 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3,403.6 | 0.2077 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 687.1 | 0.1677 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 690.1 | 0.1685 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 317,520.7 | 0.3028 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 319,176.3 | 0.3044 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 53,381.2 | 0.2037 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 53,600.3 | 0.2045 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 270,976.8 | 0.2584 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 276,801.3 | 0.2640 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 268,025.6 | 0.2556 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 277,012.7 | 0.2642 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 269,367.9 | 0.2569 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 275,016.8 | 0.2623 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 658.3 | 0.0107 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 663.9 | 0.0108 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 183.4 | 0.0112 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 182.8 | 0.0112 |

### `wild-waf-crs-942270-union-select` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 509.9 | 505.1 | 519.2 | 4.7 | 1.000x | 1.000x | 75 | 6.8 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 527.9 | 515.8 | 1,327.3 | 315.0 | 1.035x | 1.035x | 75 | 7.0 | 3.8 | 100% |

### `wild-waf-crs-942360-concat-sqli` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 18,800,198.3 | 3.0801 | 18,669,248.4 | 20,465,397.5 | 677,945.3 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 18,847,640.3 | 3.0879 | 18,669,737.0 | 19,288,393.8 | 236,021.6 | 1.003x | 1.003x |

#### `wild-waf-crs-942360-concat-sqli` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 3,176,390.3 | 3.0292 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,262,872.4 | 3.1117 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 792,486.4 | 3.0231 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 792,346.1 | 3.0226 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 197,647.6 | 3.0159 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 195,431.1 | 2.9820 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 94,107.4 | 1.5317 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 94,424.3 | 1.5369 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 25,116.5 | 1.5329 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 25,100.8 | 1.5319 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 56,463.2 | 3.4462 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 56,234.8 | 3.4323 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 7,820.0 | 1.9092 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,742.2 | 1.8902 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 2,309.9 | 2.2557 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2,270.8 | 2.2176 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 192,520.5 | 2.9376 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 200,082.4 | 3.0530 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 22,925.3 | 2.7985 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 22,504.4 | 2.7471 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 52,226.4 | 3.1876 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 55,765.1 | 3.4036 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 9,834.4 | 2.4010 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 10,675.1 | 2.6062 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 2,917,123.1 | 2.7822 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2,907,580.1 | 2.7731 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 729,193.8 | 2.7822 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 719,918.3 | 2.7468 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 3,426,563.5 | 3.2680 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,388,421.0 | 3.2316 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 3,419,029.3 | 3.2608 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,327,221.6 | 3.1732 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 3,418,887.8 | 3.2607 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3,578,912.8 | 3.4133 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 206,796.5 | 3.3658 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 190,175.5 | 3.0953 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 58,132.5 | 3.5479 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 54,607.0 | 3.3327 |

### `wild-waf-crs-942360-concat-sqli` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 2,707.4 | 2,636.1 | 2,894.5 | 87.3 | 1.000x | 1.000x | 75 | 36.1 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 2,757.8 | 2,726.0 | 3,453.0 | 274.8 | 1.019x | 1.019x | 75 | 36.8 | 3.8 | 100% |

### `wild-waf-crs-942500-comment-obfuscation` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 43,277.9 | 0.0071 | 42,981.0 | 44,594.9 | 652.8 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 43,643.9 | 0.0072 | 43,323.6 | 43,789.3 | 187.1 | 1.008x | 1.008x |

#### `wild-waf-crs-942500-comment-obfuscation` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,628.2 | 0.0073 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 7,798.1 | 0.0074 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,578.9 | 0.0060 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 1,579.2 | 0.0060 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 401.1 | 0.0061 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 400.8 | 0.0061 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 374.7 | 0.0061 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 376.1 | 0.0061 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 75.8 | 0.0046 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.2 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 75.9 | 0.0046 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 75.6 | 0.0046 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 20.4 | 0.0050 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.0 | 0.0051 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7.6 | 0.0074 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 7.5 | 0.0073 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 399.8 | 0.0061 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 401.2 | 0.0061 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 39.3 | 0.0048 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 39.6 | 0.0048 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.1 | 0.0046 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 76.4 | 0.0047 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 21.0 | 0.0051 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 20.5 | 0.0050 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,730.1 | 0.0074 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7,568.2 | 0.0072 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 1,572.7 | 0.0060 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,579.5 | 0.0060 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,682.8 | 0.0073 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,634.4 | 0.0073 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,532.6 | 0.0072 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,795.0 | 0.0074 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 7,665.2 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,637.4 | 0.0073 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 375.3 | 0.0061 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 376.4 | 0.0061 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 76.2 | 0.0047 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 75.8 | 0.0046 |

### `wild-waf-crs-942500-comment-obfuscation` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 315.2 | 314.6 | 324.0 | 3.5 | 1.000x | 1.000x | 75 | 4.2 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 326.0 | 324.2 | 327.8 | 1.2 | 1.034x | 1.034x | 75 | 4.3 | 3.8 | 100% |

### `winpath-near-miss` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 64.3 | 0.0000 | 62.8 | 65.0 | 0.8 | 1.000x | 1.000x |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 66.9 | 0.0000 | 66.8 | 67.0 | 0.1 | 1.039x | 1.039x |

#### `winpath-near-miss` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.3 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 3.4 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 3.4 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.3 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 3.2 | 0.0000 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.2 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 3.4 | 0.0001 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.2 | 0.0002 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3.3 | 0.0002 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.6 | 0.0002 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3.8 | 0.0002 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.6 | 0.0009 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 3.8 | 0.0009 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.3 | 0.0032 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 3.4 | 0.0034 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.2 | 0.0000 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 3.5 | 0.0001 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.3 | 0.0004 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 3.4 | 0.0004 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.2 | 0.0002 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3.5 | 0.0002 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.6 | 0.0009 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 3.8 | 0.0009 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.3 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 3.5 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.2 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 3.4 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.4 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 3.4 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.3 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 3.5 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.3 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 3.5 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.8 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 3.9 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 3.6 | 0.0002 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3.9 | 0.0002 |

### `winpath-near-miss` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna_noedge (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna_noedge` | measured | `plain` | same program | 283.8 | 281.8 | 286.7 | 1.9 | 1.000x | 1.000x | 75 | 3.8 | 3.4 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 297.4 | 295.3 | 298.9 | 1.3 | 1.048x | 1.048x | 75 | 4.0 | 3.8 | 100% |

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `date-nested-plus` | `large-subject-throughput` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 19 | 95% | -3:PCREC_ERR_FRAMES×1 (smallest: t-hyb-datepath-16k, 16,384 B) | 0 | `t-hyb-datepath-16k` (gave-up) |
| `date-nested-plus` | `large-subject-throughput` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 19 | 95% | -3:PCREC_ERR_FRAMES×1 (smallest: t-hyb-datepath-16k, 16,384 B) | 0 | `t-hyb-datepath-16k` (gave-up) |
| `dup-param-detect` | `large-subject-throughput` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 19 | 89% | -3:PCREC_ERR_FRAMES×2 (smallest: t-qs-nearmiss-256k, 262,092 B) | 0 | `t-qs-1m` (gave-up), `t-qs-nearmiss-256k` (gave-up) |
| `dup-param-detect` | `large-subject-throughput` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 19 | 89% | -3:PCREC_ERR_FRAMES×2 (smallest: t-qs-nearmiss-256k, 262,092 B) | 0 | `t-qs-1m` (gave-up), `t-qs-nearmiss-256k` (gave-up) |
| `email-nested-plus` | `large-subject-throughput` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 19 | 89% | 0 | 0 | `t-evil-match-60k` (no-expectation), `t-evil-nearmiss-16k` (no-expectation) |
| `email-nested-plus` | `large-subject-throughput` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 19 | 89% | 0 | 0 | `t-evil-match-60k` (no-expectation), `t-evil-nearmiss-16k` (no-expectation) |

## Standing cross-class query (inbox I-101; Frank's own anomaly check -- a QUERY, never a ranking; every hit below is a finding on pcrec's side by definition)

_0 hits: no included YES-class config's median beats any pcrec `auto-nocaps` row's median in this report's roster._

## Compile cost (by execution-model class; never pooled across classes)

### `compiled-aot`

- `pcrec_cb32eda28_auto-caps-simdna` / `balanced-parens-rec` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,071 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_cb32eda28_auto-caps-simdna` / `balanced-parens-rec` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,281 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_cb32eda28_auto-caps-simdna` / `base10num-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `base10num-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `bracket-array-define` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,402 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_cb32eda28_auto-caps-simdna` / `bracket-array-define` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,507 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_cb32eda28_auto-caps-simdna` / `codegrammar-flat` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,667 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `codegrammar-flat` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,770 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `codegrammar-xflag` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,667 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `codegrammar-xflag` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,770 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `currency-lookbehind-fixed` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=mixed offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=1, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `currency-lookbehind-fixed` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=mixed offsets=none, edge=range, edges=0 (match: 1), start=reverse-pass, folds=1, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `date-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 8,178 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `date-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 8,283 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `doubled-word` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,418 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `doubled-word` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,521 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `dup-param-detect` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,851 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `dup-param-detect` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,956 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `email-local-nodup` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 2,976 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/4 == stamped default (single tier), buffers=3/4 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `email-local-nodup` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 3,081 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/4 == stamped default (single tier), buffers=3/4 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `email-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 3,365 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `email-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 3,470 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `evil-alt-nested` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 4,599 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `evil-alt-nested` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 4,704 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `file-ext-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=cover prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `file-ext-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `float-literal-bound` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=first-class-bounded table=mixed offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `float-literal-bound` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=indexed offsets=none, edge=range, edges=0 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `floor-byte` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=cover prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `floor-byte` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `hex8-bounded` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=cover prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `hex8-bounded` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=bitmap, edges=0 (match: 1), start=reverse-pass, folds=1, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `high-byte-run` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=4 (match: 2), start=reverse-pass, folds=2, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `high-byte-run` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `ipv4-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `ipv4-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `keyword-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=cover prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `keyword-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `letters-bounded-tail-z` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `letters-bounded-tail-z` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `logparse-atomic` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=1, islands=2, shape=plain (prog: 10,528 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `logparse-atomic` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=1, islands=2, shape=plain (prog: 10,633 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `logparse-atomic-removed` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=1, islands=2, shape=plain (prog: 10,118 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `logparse-atomic-removed` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=1, islands=2, shape=plain (prog: 10,223 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `mojibake-curly-quote` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `mojibake-curly-quote` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `nested-comment-rec` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 6,854 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_cb32eda28_auto-caps-simdna` / `nested-comment-rec` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 6,959 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_cb32eda28_auto-caps-simdna` / `numeric-id-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 3,052 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `numeric-id-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 3,157 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `phone-list-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 4,220 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `phone-list-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 4,325 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `phone-palindrome-6` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 4,078 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `phone-palindrome-6` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=plain (prog: 4,183 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `pwd-strength-chain` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 7,940 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `pwd-strength-chain` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 8,045 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `quoted-delim-match` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,245 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `quoted-delim-match` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,350 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `router-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=cover prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `router-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `tag-depth3-bound` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 11,207 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `tag-depth3-bound` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 11,312 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `tag-pair-match` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,848 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `tag-pair-match` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,953 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `tail-digits-eol` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `tail-digits-eol` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `tail-dotstar-txt` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `tail-dotstar-txt` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `tail-ext-lower-txt` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `tail-ext-lower-txt` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `tail-space-eol` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=bitmap, edges=2 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `tail-space-eol` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `tail-word-eoz` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `tail-word-eoz` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `trim-nested-star` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 1,844 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `trim-nested-star` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 1,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `utf8-lead-no-cont` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=cover prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `utf8-lead-no-cont` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=mixed offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `uuid-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `uuid-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-codegrammar-json-array-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=cover prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-codegrammar-json-array-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-codegrammar-json-constant` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=first-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-codegrammar-json-constant` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=0 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-codegrammar-json-number-extended` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-codegrammar-json-number-extended` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=0 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-codegrammar-json-object-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=cover prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-codegrammar-json-object-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-codegrammar-json-stringcontent-escape` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-codegrammar-json-stringcontent-escape` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-datetime-moment-iso8601` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 15,746 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=14/11 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-datetime-moment-iso8601` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 15,851 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=14/11 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-logparse-base10num-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=mixed, edges=2 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,873 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=3/2 == stamped default (single tier), buffers=3/2 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-logparse-base10num-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,978 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=3/2 == stamped default (single tier), buffers=3/2 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-logparse-base10num-noatomic` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=mixed offsets=none, edge=mixed, edges=2 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-logparse-base10num-noatomic` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=mixed offsets=none, edge=range, edges=0 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-logparse-quotedstring-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=first-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 17,406 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-logparse-quotedstring-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 17,511 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-logparse-quotedstring-noatomic` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=first-class-bounded table=mixed offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-logparse-quotedstring-noatomic` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=mixed offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-logparse-syslogbase-expanded` / `plain`: engine=vm, sel=size-cap-retry (DFA fallback tripped), entry=plain entry, vm_prefilter=hybrid, lang=count-collapsed (size cap retry, exact 1462664 > 1000000), dfa: scan=unanchored prefilter=first-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 300,101 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=21/31 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-logparse-syslogbase-expanded` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 300,210 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=21/31 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-logparse-winpath-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,656 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-logparse-winpath-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,762 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-secrets-aws-access-key-id` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=first-memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, frameless=0, islands=1, shape=plain (prog: 5,986 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=8/3 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-secrets-aws-access-key-id` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=1, shape=plain (prog: 6,091 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=8/3 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-secrets-github-pat` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,6*, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, frameless=1, islands=0, shape=inline (prog: 1,864 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-secrets-github-pat` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 1,967 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-secrets-slack-webhook-url` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,6*, edge=mixed, edges=3 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=plain (prog: 8,428 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-secrets-slack-webhook-url` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=mixed, edges=3 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=plain (prog: 8,533 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-secrets-username-password-pair` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=handoff table=mixed offsets=none, edge=mixed, edges=3 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=2, shape=plain (prog: 16,975 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-secrets-username-password-pair` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=2, shape=plain (prog: 17,080 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=cover prefilter=none table=premultiplied offsets=none, edge=range, edges=0 (match: 1), start=attempt-start, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=0 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,461 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,566 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-validator-email-owasp` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-validator-email-owasp` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-validator-ipv4-owasp` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 14,287 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-validator-ipv4-owasp` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 14,392 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-validator-us-zip-owasp` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 2,265 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=2/4 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-validator-us-zip-owasp` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 2,368 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=2/4 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-validator-uuid-grok` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,8*,13, edge=bitmap, edges=4 (match: 4), start=end-minus-width, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-validator-uuid-grok` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=bitmap, edges=4 (match: 4), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-waf-crs-942140-dbnames` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=first-class-bounded table=premultiplied offsets=none, edge=mixed, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-waf-crs-942140-dbnames` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=mixed, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-waf-crs-942270-union-select` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-waf-crs-942270-union-select` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-waf-crs-942360-concat-sqli` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-waf-crs-942360-concat-sqli` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=compound prefilter=compound table=compound offsets=compound, edge=compound, edges=0 (match: 0), start=compound, folds=-1, match=compound, compound=split, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-waf-crs-942500-comment-obfuscation` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `wild-waf-crs-942500-comment-obfuscation` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `winpath-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna` / `winpath-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `balanced-parens-rec` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,071 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `balanced-parens-rec` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,281 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `base10num-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `base10num-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `bracket-array-define` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,402 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `bracket-array-define` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,507 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `codegrammar-flat` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,667 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `codegrammar-flat` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,770 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `codegrammar-xflag` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,667 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `codegrammar-xflag` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,770 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `currency-lookbehind-fixed` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=mixed offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=1, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `currency-lookbehind-fixed` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=mixed offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=1, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `date-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 8,178 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `date-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 8,283 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `doubled-word` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,418 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `doubled-word` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,521 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `dup-param-detect` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,851 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `dup-param-detect` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,956 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `email-local-nodup` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 2,976 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/4 == stamped default (single tier), buffers=3/4 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `email-local-nodup` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 3,081 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/4 == stamped default (single tier), buffers=3/4 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `email-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 3,365 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `email-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 3,470 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `evil-alt-nested` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 4,599 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `evil-alt-nested` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 4,704 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `file-ext-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=cover prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `file-ext-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `float-literal-bound` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=first-class-bounded table=mixed offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `float-literal-bound` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=indexed offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `floor-byte` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=cover prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `floor-byte` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `hex8-bounded` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=cover prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `hex8-bounded` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `high-byte-run` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `high-byte-run` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `ipv4-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `ipv4-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `keyword-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=cover prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `keyword-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `letters-bounded-tail-z` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `letters-bounded-tail-z` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `logparse-atomic` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=1, islands=2, shape=plain (prog: 10,528 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `logparse-atomic` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=1, islands=2, shape=plain (prog: 10,633 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `logparse-atomic-removed` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=1, islands=2, shape=plain (prog: 10,118 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `logparse-atomic-removed` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=1, islands=2, shape=plain (prog: 10,223 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `mojibake-curly-quote` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `mojibake-curly-quote` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `nested-comment-rec` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 6,854 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `nested-comment-rec` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 6,959 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `numeric-id-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 3,052 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `numeric-id-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 3,157 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `phone-list-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 4,220 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `phone-list-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 4,325 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `phone-palindrome-6` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 4,078 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `phone-palindrome-6` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=plain (prog: 4,183 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `pwd-strength-chain` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 7,940 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `pwd-strength-chain` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 8,045 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `quoted-delim-match` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,245 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `quoted-delim-match` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,350 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `router-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=cover prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `router-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `tag-depth3-bound` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 11,207 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `tag-depth3-bound` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 11,312 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `tag-pair-match` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,848 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `tag-pair-match` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,953 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `tail-digits-eol` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `tail-digits-eol` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `tail-dotstar-txt` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `tail-dotstar-txt` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `tail-ext-lower-txt` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `tail-ext-lower-txt` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `tail-space-eol` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `tail-space-eol` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `tail-word-eoz` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `tail-word-eoz` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `trim-nested-star` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 1,844 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `trim-nested-star` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 1,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `utf8-lead-no-cont` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=cover prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `utf8-lead-no-cont` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=mixed offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `uuid-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `uuid-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-codegrammar-json-array-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=cover prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-codegrammar-json-array-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-codegrammar-json-constant` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=first-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-codegrammar-json-constant` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-codegrammar-json-number-extended` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-codegrammar-json-number-extended` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-codegrammar-json-object-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=cover prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-codegrammar-json-object-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-codegrammar-json-stringcontent-escape` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-codegrammar-json-stringcontent-escape` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-datetime-moment-iso8601` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 15,746 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=14/11 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-datetime-moment-iso8601` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 15,851 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=14/11 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-logparse-base10num-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,873 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=3/2 == stamped default (single tier), buffers=3/2 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-logparse-base10num-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,978 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=3/2 == stamped default (single tier), buffers=3/2 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-logparse-base10num-noatomic` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=mixed offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-logparse-base10num-noatomic` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=mixed offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-logparse-quotedstring-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=first-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 17,406 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-logparse-quotedstring-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 17,511 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-logparse-quotedstring-noatomic` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=first-class-bounded table=mixed offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-logparse-quotedstring-noatomic` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=mixed offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-logparse-syslogbase-expanded` / `plain`: engine=vm, sel=size-cap-retry (DFA fallback tripped), entry=plain entry, vm_prefilter=hybrid, lang=count-collapsed (size cap retry, exact 1462664 > 1000000), dfa: scan=unanchored prefilter=first-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 300,101 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=21/31 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-logparse-syslogbase-expanded` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 300,210 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=21/31 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-logparse-winpath-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,656 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-logparse-winpath-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,762 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-secrets-aws-access-key-id` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=first-memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, frameless=0, islands=1, shape=plain (prog: 5,986 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=8/3 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-secrets-aws-access-key-id` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=1, shape=plain (prog: 6,091 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=8/3 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-secrets-github-pat` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,6*, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, frameless=1, islands=0, shape=inline (prog: 1,864 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-secrets-github-pat` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 1,967 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-secrets-slack-webhook-url` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,6*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=plain (prog: 8,428 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-secrets-slack-webhook-url` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=plain (prog: 8,533 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-secrets-username-password-pair` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=handoff table=mixed offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=2, shape=plain (prog: 16,975 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-secrets-username-password-pair` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=2, shape=plain (prog: 17,080 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-semdiv-altorder-foo-foobar-rustregex` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=cover prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-semdiv-altorder-foo-foobar-rustregex` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-semdiv-dollar-trailing-newline-pcre2` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-semdiv-dollar-trailing-newline-pcre2` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-semdiv-empty-alt-repeat-pcre2` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,461 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-semdiv-empty-alt-repeat-pcre2` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,566 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-validator-email-owasp` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-validator-email-owasp` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-validator-ipv4-owasp` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 14,287 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-validator-ipv4-owasp` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 14,392 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-validator-us-zip-owasp` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 2,265 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=2/4 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-validator-us-zip-owasp` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 2,368 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=2/4 (stamped default), frame=24
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-validator-uuid-grok` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,8*,13, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-validator-uuid-grok` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-waf-crs-942140-dbnames` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=first-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-waf-crs-942140-dbnames` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-waf-crs-942160-sleep-benchmark` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-waf-crs-942160-sleep-benchmark` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-waf-crs-942270-union-select` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-waf-crs-942270-union-select` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-waf-crs-942360-concat-sqli` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-waf-crs-942360-concat-sqli` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=compound prefilter=compound table=compound offsets=compound, edge=compound, edges=0 (match: 0), start=compound, folds=-1, match=compound, compound=split, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-waf-crs-942500-comment-obfuscation` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `wild-waf-crs-942500-comment-obfuscation` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `winpath-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_cb32eda28_auto-caps-simdna_noedge` / `winpath-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
    - sel = pcrec's `RX_ENGINE_SEL`; `DFA fallback tripped` = sel not in (selected, forced), and NOTHING else -- since pcrec 263b013 ([LIM-1] / [OPT-4.1]) every fallback has its own token (`overflowed-dfa`, `overflowed-prefilter`, `collapsed-prefilter`, `declined-nullable`, `size-cap-retry`), the size-cap rescue included; at pcrec 96e44c2 that rescue stamped `sel=selected` and only its `lang=count-collapsed (size cap retry, ...)` clause says so.
    - K = pcrec's `RX_UNROLL_K`/`_WHY`: the VM counter rung's unroll factor and who chose it (default / option / denied / size-model / size-model-declined / cap-rescue / capacity-declined -- limits.md 8); caps = the EFFECTIVE `RX_MAX_EMIT_CODE_BYTES`/`RX_MAX_EMIT_BYTES` the artifact was built under (raise-only; 500,000/1,000,000 by default). VM artifacts only: a DFA artifact has no counter rung and stamps no code cap.
    - edge = pcrec's `RX_DFA_SCAN_EDGE` ([OPT-5] STEP 1, abi 13+), how a DFA scan tests a SCAN EDGE's byte class: `range` = a contiguous run (subtract-and-compare against two immediates); `bitmap` = a non-contiguous class (a 256-byte membership read); `mixed` = one artifact whose machines took both forms; `none` = no collapsible run (an attempt/empty scan, or -fno-scan-edge).
    - edges = pcrec's `scan_edges` ([B32]): how many [OPT-5] SCAN EDGES this artifact's SEARCH-side machines carry (`rx_search`/`rx_prefilter`), the per-scan-iteration compare-count covariate `edge`'s single shape token cannot separate (I-33: the cost is one compare per edge per iteration); the `(match: M)` parenthetical, when carried, is the SAME count on the anchored `rx_match` machine, kept apart because the measured [OPT-EDGE] regression is search-band only. `0` is a real, recorded value.
    - start = pcrec's `RX_DFA_START` ([OPT-5] STEP 2, abi 16+), how the SEARCH entry recovers the match START: `pinned` = the forward machine's start state accepts unconditionally, so the match provably begins at `search_from` and THE ARTIFACT CARRIES NO REVERSE MACHINE at all (no reverse tables, accessor block or scan loop); `reverse-pass` = it carries one and walks it backwards from the match end. The two forms are ANSWER-IDENTICAL by contract -- `caps[0][0]`'s absolute offsets and the zero-length-match convention hold under both -- so this explains a row's SIZE and pass count, never its answer.
      - start=end-minus-width: every match is one fixed byte width W, so the start is the verified end minus W; NO reverse machine (abi 74, [START-LANDING])
      - start=attempt-start: the ABSENCE value: an `attempt` loop or the empty engine asks no RECOVER and no reverse pass runs (abi 73)
      - prefilter=handoff: the forward scan RE-ENTERS the pre-check handoff at each restart: it re-finds the one-byte or run landmark and moves to hit - K (K = `REQ_HANDOFF`) when that is ahead (abi 75, [REQ-HANDOFF-L1]); removed by `-fno-req-handoff`, which also removes the K82 entry handoff
    - frameless = pcrec's `RX_VM_FRAMELESS` ([OPT-VMFL], abi 16+): `1` iff this VM program emits NO push site and no linked call, so its fail label carries no pop-and-resume dispatch; `0` otherwise. VM artifacts only, hybrids included -- a DIFFERENT scope from `start=`, though the two stamps arrived at one abi. It is NOT `buffers=`'s resume-frame CAPACITY and the two can disagree: the capacity is what the artifact was SIZED for, this is what its program CONTAINS. `0` is a real, recorded value.
    - folds = pcrec's `RX_DFA_UNIFORM_FOLDS` ([CC-DIFF] STEP 1, abi 17+): how many of this artifact's DFA tables (two per machine it contains -- forward always, reverse unless `start=pinned`, anchored under `match=unwrapped`; so 0..6) had ALL-EQUAL cells and were NOT EMITTED, the accessor returning the constant. `table=` keeps naming the encoding that was SELECTED, so `premultiplied` beside `folds=4` is an artifact carrying NO transition table at all -- a SIZE fact, never an answer one. `0` is a real, recorded value.
    - islands = pcrec's `RX_VM_ALT_ISLANDS` ([ENG-ISL] STEP 1, abi 18+): how many of this VM program's flat alternations were lowered as an ALTERNATION ISLAND -- a trie dispatch over the alternatives' literal bytes -- instead of vm_alt's serial resume chain (one frame per untried branch). Selected per alternation on its LANGUAGE (a finite literal set), so a COUNT; a caseless, prefix-bearing-under-four-words or over-budget alternation is declined as a selection outcome. This is what removes the branch-ORDER effect (altwide srt-256 vs w-256) at the source; `-fno-alt-island` is the sibling that reads `0` at the same pin. `0` is a real, recorded value.
    - shape = pcrec's `RX_VM_ENTRY_SHAPE` with `RX_VM_PROGRAM_BYTES` in the parenthetical ([CC-DIFF] STEP 2, abi 22+): the entry-chain rung the emitter TOOK for the six entries -- `plain` (one body, six framed entries), `shared` (one out-of-line body behind three forwarding entries), `forward` (three bodies in the three `_in` entries, no canary anywhere), `inline` (six bodies) -- and the program size AUTO compared against VM_INLINE_CHAIN_MAX_BYTES (4,096 B) to choose it: `forward` at or below, `shared` above; `inline`/`plain` where a forward rung is illegal (the program writes its storage); a FRAMED program (`frameless=0`) is `plain` whatever the size. ANSWER-IDENTICAL across every value -- only the scaffolding above the first label moves -- so a COST and SIZE fact; the number is what makes the token checkable. `prog: N B` is the VM PROGRAM REGION with its COMMENTS INCLUDED (the raw length of the emitter's program buffer; the island trie writes a per-node comment), NOT the `code bytes` columns' quantity -- those and `--max-emit-code-bytes` count the whole .c+.h with every comment EXCLUDED -- so the program stamp can exceed the code bytes (w-256: 305,686 vs 292,043) and neither is wrong; for cap reasoning use the code bytes (pcrec I-50 1).
    - clsfolds = pcrec's `RX_VM_CLS_FOLDS` ([FORM-CHAR] STEP 1, abi 23+): how many of this VM program's class-pool entries take the ASCII-FOLD membership test -- a two-member set differing only in bit 0x20, both letters (what `(?i)` makes of a letter at parse time), tested as `(byte | 0x20) == lower` with NO 32-byte bitmap table emitted for it. Chosen per pool class, so a COUNT; a set that is not exactly two members, not a 0x20 pair, or a 0x20 pair of non-letters keeps its bitmap. A SIZE fact (one table per fold class gone, plus the test text), never an answer one: the fold compare and the bitmap read are the same predicate over the pair's two bytes. VM route only -- an `auto` row that selected the DFA prints no clause even on a `(?i)` pattern; `-fno-cls-fold` is the sibling that reads `0` at the same pin. `0` is a real, recorded value.
    - compound = pcrec's `RX_COMPOUND` ([COMPOUND] B4, abi 77+): this artifact is a COMPOUND -- a pin-only pattern split into a controller and two bounded parts (compound.md), the value the compound row's name (`split`). `forced-off` is pcrec's harness-only lever, never set by this bench. Stamped on every artifact at abi 77+ with `none` the plain case; the clause prints only for a compound. A ROUTE and SIZE fact (+113,575 B on the one corpus pattern, b142prep), answer-identical by construction; the `drop-compound` size-cap fallback is the only off-ramp (no CLI deny flag).

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | emit bytes | code bytes | jitter | outcomes | emit-c ns | gcc ns | load ns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `balanced-parens-rec` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 131,443,527.0 | 130,355,144.0 | 134,264,205.0 | 1,327,996.0 | 5 | 37,392 | 30,704 | 28,951 | 0.010 | compiled=5 | 2,537,904.0 | 128,882,679.0 | 53,782.0 |
| `balanced-parens-rec` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 132,627,750.0 | 131,944,130.0 | 133,255,001.0 | 425,865.2 | 5 | 37,392 | 30,922 | 29,169 | 0.003 | compiled=5 | 2,751,987.0 | 129,879,449.0 | 47,690.0 |
| `balanced-parens-rec` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 132,119,831.0 | 131,006,383.0 | 133,337,845.0 | 874,143.9 | 5 | 37,392 | 30,704 | 28,951 | 0.007 | compiled=5 | 1,643,707.0 | 130,251,410.0 | 45,947.0 |
| `balanced-parens-rec` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 132,739,779.0 | 130,507,903.0 | 133,343,827.0 | 1,172,630.1 | 5 | 37,392 | 30,922 | 29,169 | 0.009 (max is trial 1) | compiled=5 | 1,786,998.0 | 130,835,100.0 | 49,994.0 |
| `base10num-near-miss` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 80,167,222.0 | 79,664,356.0 | 80,419,268.0 | 271,259.0 | 5 | 37,232 | 17,591 | 15,206 | 0.003 | compiled=5 | 1,318,795.0 | 78,756,283.0 | 51,908.0 |
| `base10num-near-miss` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 79,639,027.0 | 77,985,890.0 | 79,683,582.0 | 776,928.7 | 5 | 37,152 | 17,044 | 14,659 | 0.010 | compiled=5 | 1,341,067.0 | 78,258,996.0 | 57,718.0 |
| `base10num-near-miss` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 80,578,976.0 | 79,781,902.0 | 81,354,366.0 | 545,303.7 | 5 | 37,232 | 17,591 | 15,206 | 0.007 | compiled=5 | 1,291,964.0 | 79,202,031.0 | 50,735.0 |
| `base10num-near-miss` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 78,412,123.0 | 77,800,619.0 | 79,391,498.0 | 622,780.1 | 5 | 37,152 | 17,044 | 14,659 | 0.008 | compiled=5 | 1,240,488.0 | 77,229,704.0 | 44,303.0 |
| `bracket-array-define` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 139,555,588.0 | 138,148,496.0 | 143,919,934.0 | 2,065,978.2 | 5 | 37,376 | 29,322 | 29,007 | 0.015 (max is trial 1) | compiled=5 | 1,813,589.0 | 136,937,242.0 | 53,802.0 |
| `bracket-array-define` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 137,724,186.0 | 136,657,826.0 | 138,629,582.0 | 703,687.8 | 5 | 37,376 | 29,437 | 29,122 | 0.005 | compiled=5 | 2,317,749.0 | 135,228,001.0 | 53,230.0 |
| `bracket-array-define` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 139,708,371.0 | 138,854,542.0 | 142,733,390.0 | 1,441,116.0 | 5 | 37,376 | 29,322 | 29,007 | 0.010 | compiled=5 | 1,621,175.0 | 138,022,694.0 | 53,591.0 |
| `bracket-array-define` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 138,982,602.0 | 138,772,066.0 | 141,567,645.0 | 1,148,067.0 | 5 | 37,376 | 29,437 | 29,122 | 0.008 | compiled=5 | 1,643,607.0 | 137,587,424.0 | 49,463.0 |
| `codegrammar-flat` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 258,757,940.0 | 251,239,479.0 | 259,641,155.0 | 3,675,855.9 | 5 | 37,472 | 36,875 | 28,276 | 0.014 (max is trial 1) | compiled=5 | 4,457,342.0 | 253,691,711.0 | 45,476.0 |
| `codegrammar-flat` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 247,481,315.0 | 246,965,332.0 | 248,683,611.0 | 575,507.1 | 5 | 37,232 | 31,131 | 27,171 | 0.002 (max is trial 1) | compiled=5 | 2,985,718.0 | 244,547,014.0 | 43,642.0 |
| `codegrammar-flat` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 251,468,264.0 | 248,525,229.0 | 254,346,449.0 | 1,924,952.9 | 5 | 37,432 | 34,664 | 27,537 | 0.008 | compiled=5 | 3,735,870.0 | 247,360,163.0 | 52,850.0 |
| `codegrammar-flat` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 249,540,121.0 | 246,789,608.0 | 252,617,651.0 | 2,165,128.7 | 5 | 37,232 | 31,131 | 27,171 | 0.009 (max is trial 1) | compiled=5 | 2,266,371.0 | 247,339,074.0 | 47,630.0 |
| `codegrammar-xflag` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 249,546,978.0 | 246,484,445.0 | 251,817,849.0 | 1,969,265.1 | 5 | 37,512 | 37,153 | 28,475 | 0.008 (max is trial 1) | compiled=5 | 4,534,778.0 | 244,457,014.0 | 48,752.0 |
| `codegrammar-xflag` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 240,647,853.0 | 239,418,427.0 | 240,951,857.0 | 555,169.1 | 5 | 37,272 | 31,411 | 27,372 | 0.002 | compiled=5 | 2,288,102.0 | 237,843,507.0 | 52,319.0 |
| `codegrammar-xflag` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 247,276,496.0 | 246,890,568.0 | 248,432,263.0 | 700,018.5 | 5 | 37,464 | 34,942 | 27,736 | 0.003 (max is trial 1) | compiled=5 | 3,856,988.0 | 243,739,330.0 | 54,713.0 |
| `codegrammar-xflag` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 243,496,793.0 | 240,835,858.0 | 249,525,775.0 | 3,031,974.4 | 5 | 37,272 | 31,411 | 27,372 | 0.012 (max is trial 1) | compiled=5 | 2,130,886.0 | 241,503,767.0 | 47,270.0 |
| `currency-lookbehind-fixed` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 89,650,348.0 | 87,945,345.0 | 91,639,048.0 | 1,314,740.5 | 5 | 33,552 | 23,733 | 17,533 | 0.015 | compiled=5 | 2,182,564.0 | 87,408,072.0 | 50,445.0 |
| `currency-lookbehind-fixed` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 88,187,400.0 | 87,898,345.0 | 89,888,647.0 | 743,239.1 | 5 | 33,288 | 22,402 | 18,058 | 0.008 | compiled=5 | 2,119,255.0 | 86,367,680.0 | 53,260.0 |
| `currency-lookbehind-fixed` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 84,579,123.0 | 82,909,576.0 | 85,320,862.0 | 822,167.6 | 5 | 33,552 | 23,733 | 17,533 | 0.010 | compiled=5 | 2,026,649.0 | 82,264,502.0 | 53,210.0 |
| `currency-lookbehind-fixed` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 80,624,361.0 | 80,369,059.0 | 81,573,840.0 | 423,133.6 | 5 | 33,288 | 21,708 | 17,308 | 0.005 | compiled=5 | 1,748,755.0 | 78,993,318.0 | 42,109.0 |
| `date-nested-plus` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 146,617,900.0 | 146,228,647.0 | 147,434,119.0 | 419,663.1 | 5 | 37,536 | 36,791 | 34,765 | 0.003 | compiled=5 | 2,501,386.0 | 144,023,009.0 | 54,282.0 |
| `date-nested-plus` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 146,825,963.0 | 145,855,022.0 | 147,497,538.0 | 573,244.9 | 5 | 37,536 | 36,719 | 34,693 | 0.004 | compiled=5 | 2,624,066.0 | 144,605,787.0 | 56,006.0 |
| `date-nested-plus` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 147,063,731.0 | 146,162,554.0 | 147,994,075.0 | 658,919.0 | 5 | 37,536 | 36,791 | 34,765 | 0.004 | compiled=5 | 1,673,563.0 | 145,490,737.0 | 44,564.0 |
| `date-nested-plus` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 146,332,303.0 | 145,649,266.0 | 146,644,913.0 | 369,023.0 | 5 | 37,536 | 36,719 | 34,693 | 0.003 | compiled=5 | 1,681,819.0 | 144,542,040.0 | 53,451.0 |
| `doubled-word` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 322,346,703.0 | 316,481,017.0 | 324,106,572.0 | 2,642,157.6 | 5 | 41,096 | 26,720 | 24,790 | 0.008 | compiled=5 | 8,647,249.0 | 314,145,705.0 | 53,230.0 |
| `doubled-word` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 320,968,114.0 | 312,591,485.0 | 329,212,926.0 | 5,288,804.2 | 5 | 41,096 | 26,831 | 24,901 | 0.016 | compiled=5 | 8,624,066.0 | 311,990,813.0 | 55,194.0 |
| `doubled-word` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 316,400,755.0 | 315,311,292.0 | 317,855,045.0 | 833,714.2 | 5 | 41,096 | 26,720 | 24,790 | 0.003 | compiled=5 | 1,516,849.0 | 314,869,860.0 | 50,775.0 |
| `doubled-word` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 321,880,472.0 | 318,889,326.0 | 324,408,877.0 | 2,142,856.0 | 5 | 41,096 | 26,831 | 24,901 | 0.007 | compiled=5 | 1,619,842.0 | 320,180,859.0 | 52,950.0 |
| `dup-param-detect` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 144,919,459.0 | 144,225,661.0 | 145,839,323.0 | 614,818.6 | 5 | 37,432 | 32,323 | 30,339 | 0.004 | compiled=5 | 2,552,111.0 | 142,207,526.0 | 49,213.0 |
| `dup-param-detect` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 144,860,158.0 | 143,879,468.0 | 146,219,449.0 | 754,065.0 | 5 | 37,432 | 32,436 | 30,452 | 0.005 | compiled=5 | 2,711,591.0 | 141,961,494.0 | 51,007.0 |
| `dup-param-detect` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 144,147,256.0 | 143,246,388.0 | 146,763,514.0 | 1,221,911.8 | 5 | 37,432 | 32,323 | 30,339 | 0.008 (max is trial 1) | compiled=5 | 1,862,269.0 | 142,275,368.0 | 45,235.0 |
| `dup-param-detect` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 145,156,908.0 | 144,235,242.0 | 146,177,711.0 | 624,051.8 | 5 | 37,432 | 32,436 | 30,452 | 0.004 | compiled=5 | 1,875,003.0 | 143,232,301.0 | 51,326.0 |
| `email-local-nodup` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 111,829,174.0 | 109,958,559.0 | 111,935,345.0 | 743,892.9 | 5 | 33,152 | 27,960 | 25,769 | 0.007 (max is trial 1) | compiled=5 | 2,575,505.0 | 109,166,465.0 | 41,128.0 |
| `email-local-nodup` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 95,679,041.0 | 94,365,536.0 | 96,149,618.0 | 624,312.3 | 5 | 33,072 | 28,348 | 26,066 | 0.007 (max is trial 1) | compiled=5 | 1,734,399.0 | 93,584,504.0 | 51,567.0 |
| `email-local-nodup` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 106,974,396.0 | 106,012,773.0 | 109,856,778.0 | 1,401,576.7 | 5 | 33,152 | 27,960 | 25,769 | 0.013 | compiled=5 | 1,482,654.0 | 105,430,988.0 | 52,048.0 |
| `email-local-nodup` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 93,901,201.0 | 93,371,903.0 | 94,383,799.0 | 385,033.8 | 5 | 33,072 | 28,348 | 26,066 | 0.004 | compiled=5 | 1,658,275.0 | 92,184,886.0 | 52,078.0 |
| `email-nested-plus` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 132,171,921.0 | 131,899,157.0 | 132,813,780.0 | 387,971.0 | 5 | 37,496 | 32,089 | 30,143 | 0.003 | compiled=5 | 2,445,800.0 | 130,189,554.0 | 53,702.0 |
| `email-nested-plus` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 132,376,987.0 | 131,630,650.0 | 132,904,410.0 | 433,143.5 | 5 | 37,496 | 32,520 | 30,490 | 0.003 | compiled=5 | 2,452,693.0 | 129,825,086.0 | 54,463.0 |
| `email-nested-plus` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 132,382,056.0 | 131,599,862.0 | 133,524,379.0 | 643,927.4 | 5 | 37,496 | 32,089 | 30,143 | 0.005 | compiled=5 | 1,523,121.0 | 130,879,484.0 | 57,609.0 |
| `email-nested-plus` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 133,282,892.0 | 132,308,637.0 | 141,337,461.0 | 3,404,281.1 | 5 | 37,496 | 32,520 | 30,490 | 0.026 | compiled=5 | 1,692,138.0 | 131,650,637.0 | 53,702.0 |
| `evil-alt-nested` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 174,178,220.0 | 173,115,238.0 | 174,875,405.0 | 574,209.9 | 5 | 41,664 | 32,798 | 31,187 | 0.003 | compiled=5 | 2,563,803.0 | 171,496,125.0 | 52,489.0 |
| `evil-alt-nested` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 172,647,616.0 | 172,102,227.0 | 174,528,360.0 | 919,022.7 | 5 | 41,632 | 32,726 | 31,115 | 0.005 (max is trial 1) | compiled=5 | 2,599,349.0 | 169,951,223.0 | 51,067.0 |
| `evil-alt-nested` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 174,012,043.0 | 173,469,662.0 | 174,468,954.0 | 333,055.0 | 5 | 41,664 | 32,798 | 31,187 | 0.002 | compiled=5 | 1,657,143.0 | 172,339,432.0 | 55,384.0 |
| `evil-alt-nested` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 177,663,236.0 | 173,407,955.0 | 180,451,028.0 | 2,704,769.3 | 5 | 41,632 | 32,726 | 31,115 | 0.015 | compiled=5 | 1,626,836.0 | 175,926,472.0 | 52,800.0 |
| `file-ext-order` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 79,455,390.0 | 78,235,050.0 | 80,394,160.0 | 763,874.9 | 5 | 28,888 | 15,998 | 13,994 | 0.010 (max is trial 1) | compiled=5 | 2,039,975.0 | 77,243,271.0 | 56,797.0 |
| `file-ext-order` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 83,927,221.0 | 82,580,471.0 | 84,650,053.0 | 680,338.8 | 5 | 33,176 | 20,888 | 16,046 | 0.008 | compiled=5 | 2,427,216.0 | 81,443,769.0 | 54,583.0 |
| `file-ext-order` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 78,945,278.0 | 78,443,621.0 | 80,437,649.0 | 739,390.0 | 5 | 28,888 | 15,998 | 13,994 | 0.009 | compiled=5 | 2,136,726.0 | 76,697,562.0 | 44,143.0 |
| `file-ext-order` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 82,026,132.0 | 81,074,899.0 | 83,558,600.0 | 879,185.9 | 5 | 33,176 | 20,888 | 16,046 | 0.011 | compiled=5 | 2,464,765.0 | 79,504,881.0 | 49,583.0 |
| `float-literal-bound` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 90,096,679.0 | 89,251,848.0 | 91,377,193.0 | 794,269.8 | 5 | 33,648 | 24,886 | 17,710 | 0.009 | compiled=5 | 4,419,691.0 | 85,619,750.0 | 55,775.0 |
| `float-literal-bound` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 87,440,883.0 | 86,794,575.0 | 89,805,280.0 | 1,037,480.7 | 5 | 33,344 | 21,930 | 17,953 | 0.012 | compiled=5 | 2,199,526.0 | 85,184,380.0 | 45,455.0 |
| `float-literal-bound` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 90,126,536.0 | 88,963,345.0 | 90,780,700.0 | 635,118.9 | 5 | 33,648 | 24,886 | 17,710 | 0.007 | compiled=5 | 4,046,555.0 | 85,849,647.0 | 53,370.0 |
| `float-literal-bound` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 83,890,135.0 | 83,498,647.0 | 84,018,887.0 | 182,220.0 | 5 | 33,344 | 21,380 | 17,403 | 0.002 | compiled=5 | 1,940,497.0 | 81,995,255.0 | 49,644.0 |
| `floor-byte` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 76,614,608.0 | 76,078,015.0 | 77,745,999.0 | 557,535.0 | 5 | 28,888 | 15,592 | 13,923 | 0.007 | compiled=5 | 1,680,097.0 | 74,975,066.0 | 45,115.0 |
| `floor-byte` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 79,401,059.0 | 78,577,175.0 | 80,087,343.0 | 486,692.4 | 5 | 33,176 | 19,581 | 16,023 | 0.006 | compiled=5 | 1,639,721.0 | 77,786,115.0 | 50,405.0 |
| `floor-byte` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 78,376,726.0 | 76,754,127.0 | 79,005,290.0 | 809,989.3 | 5 | 28,888 | 15,592 | 13,923 | 0.010 (max is trial 1) | compiled=5 | 1,589,685.0 | 76,638,180.0 | 50,976.0 |
| `floor-byte` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 82,462,035.0 | 81,178,746.0 | 82,936,328.0 | 643,063.8 | 5 | 33,176 | 19,581 | 16,023 | 0.008 (max is trial 1) | compiled=5 | 1,706,005.0 | 80,604,674.0 | 56,366.0 |
| `hex8-bounded` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 86,441,369.0 | 86,011,840.0 | 87,457,895.0 | 592,959.8 | 5 | 33,080 | 18,901 | 15,888 | 0.007 | compiled=5 | 2,118,223.0 | 84,198,271.0 | 42,410.0 |
| `hex8-bounded` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 88,235,811.0 | 87,946,678.0 | 89,174,721.0 | 422,482.8 | 5 | 33,336 | 23,984 | 18,205 | 0.005 | compiled=5 | 2,427,306.0 | 85,832,581.0 | 44,594.0 |
| `hex8-bounded` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 85,599,096.0 | 85,401,253.0 | 85,897,687.0 | 163,814.4 | 5 | 33,080 | 18,901 | 15,888 | 0.002 | compiled=5 | 2,118,442.0 | 83,437,813.0 | 54,603.0 |
| `hex8-bounded` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 86,032,683.0 | 84,850,635.0 | 86,745,447.0 | 721,850.8 | 5 | 33,344 | 22,144 | 17,330 | 0.008 | compiled=5 | 2,157,636.0 | 83,849,249.0 | 45,235.0 |
| `high-byte-run` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 91,725,560.0 | 90,688,626.0 | 92,224,010.0 | 578,556.3 | 5 | 32,976 | 27,070 | 20,764 | 0.006 | compiled=5 | 2,367,593.0 | 89,197,174.0 | 48,301.0 |
| `high-byte-run` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 88,794,425.0 | 86,901,547.0 | 89,530,392.0 | 872,333.1 | 5 | 33,176 | 21,598 | 17,896 | 0.010 | compiled=5 | 2,149,101.0 | 86,692,834.0 | 44,263.0 |
| `high-byte-run` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 82,664,075.0 | 81,129,091.0 | 83,343,546.0 | 781,833.4 | 5 | 33,272 | 22,232 | 15,615 | 0.009 | compiled=5 | 2,179,036.0 | 80,529,102.0 | 55,815.0 |
| `high-byte-run` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 82,844,545.0 | 81,375,857.0 | 85,390,282.0 | 1,458,812.0 | 5 | 33,176 | 19,781 | 16,037 | 0.018 | compiled=5 | 1,857,721.0 | 80,199,360.0 | 51,817.0 |
| `ipv4-near-miss` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 88,524,126.0 | 88,305,242.0 | 89,399,054.0 | 384,635.1 | 5 | 42,184 | 24,556 | 19,240 | 0.004 | compiled=5 | 1,389,168.0 | 87,148,653.0 | 53,291.0 |
| `ipv4-near-miss` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 86,375,736.0 | 86,263,215.0 | 88,088,384.0 | 804,259.4 | 5 | 41,984 | 23,634 | 18,318 | 0.009 | compiled=5 | 1,496,962.0 | 84,836,344.0 | 54,734.0 |
| `ipv4-near-miss` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 90,613,534.0 | 89,201,724.0 | 91,207,685.0 | 693,518.2 | 5 | 42,184 | 24,556 | 19,240 | 0.008 | compiled=5 | 1,409,757.0 | 89,058,514.0 | 51,116.0 |
| `ipv4-near-miss` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 88,386,428.0 | 86,516,233.0 | 89,734,679.0 | 1,256,925.4 | 5 | 41,984 | 23,634 | 18,318 | 0.014 (max is trial 1) | compiled=5 | 1,446,025.0 | 86,851,446.0 | 49,092.0 |
| `keyword-prefix-order` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 79,996,231.0 | 78,610,168.0 | 80,433,895.0 | 762,700.6 | 5 | 28,888 | 15,948 | 14,003 | 0.010 (max is trial 1) | compiled=5 | 1,944,385.0 | 78,088,174.0 | 52,289.0 |
| `keyword-prefix-order` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 82,434,206.0 | 81,911,391.0 | 82,738,921.0 | 297,065.7 | 5 | 33,176 | 22,186 | 16,041 | 0.004 | compiled=5 | 2,183,526.0 | 79,931,137.0 | 49,964.0 |
| `keyword-prefix-order` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 79,366,530.0 | 78,498,305.0 | 80,036,572.0 | 528,519.3 | 5 | 28,888 | 15,948 | 14,003 | 0.007 | compiled=5 | 1,923,525.0 | 77,641,460.0 | 44,444.0 |
| `keyword-prefix-order` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 81,639,624.0 | 80,692,669.0 | 84,232,199.0 | 1,239,574.8 | 5 | 33,176 | 22,186 | 16,041 | 0.015 | compiled=5 | 2,048,571.0 | 79,391,137.0 | 54,663.0 |
| `letters-bounded-tail-z` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 188,477,754.0 | 186,056,141.0 | 190,037,274.0 | 1,303,262.3 | 5 | 66,160 | 137,275 | 18,930 | 0.007 | compiled=5 | 86,987,809.0 | 101,021,803.0 | 52,949.0 |
| `letters-bounded-tail-z` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 188,705,954.0 | 186,446,918.0 | 189,835,525.0 | 1,198,638.4 | 5 | 66,160 | 137,283 | 18,938 | 0.006 | compiled=5 | 86,509,338.0 | 101,891,211.0 | 50,586.0 |
| `letters-bounded-tail-z` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 185,485,094.0 | 183,779,861.0 | 189,531,540.0 | 2,010,112.6 | 5 | 74,352 | 164,869 | 17,930 | 0.011 | compiled=5 | 86,063,039.0 | 99,187,512.0 | 48,572.0 |
| `letters-bounded-tail-z` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 186,077,761.0 | 183,789,458.0 | 190,119,127.0 | 2,040,866.7 | 5 | 74,352 | 164,877 | 17,938 | 0.011 | compiled=5 | 86,828,823.0 | 99,390,565.0 | 45,606.0 |
| `logparse-atomic` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 146,528,502.0 | 145,332,047.0 | 148,651,483.0 | 1,159,001.5 | 5 | 84,408 | 59,532 | 39,599 | 0.008 | compiled=5 | 3,341,609.0 | 143,158,019.0 | 59,863.0 |
| `logparse-atomic` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 147,211,860.0 | 144,138,317.0 | 149,727,663.0 | 1,895,627.2 | 5 | 84,368 | 59,459 | 39,526 | 0.013 | compiled=5 | 3,055,530.0 | 143,922,069.0 | 61,726.0 |
| `logparse-atomic` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 145,671,257.0 | 144,092,974.0 | 147,357,405.0 | 1,062,780.6 | 5 | 84,408 | 59,532 | 39,599 | 0.007 | compiled=5 | 2,298,391.0 | 143,507,711.0 | 61,375.0 |
| `logparse-atomic` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 144,244,069.0 | 141,591,089.0 | 146,293,210.0 | 1,555,457.0 | 5 | 84,368 | 59,459 | 39,526 | 0.011 (max is trial 1) | compiled=5 | 2,280,607.0 | 141,647,535.0 | 59,973.0 |
| `logparse-atomic-removed` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 145,422,427.0 | 144,742,575.0 | 146,988,860.0 | 866,203.5 | 5 | 84,408 | 59,248 | 39,315 | 0.006 | compiled=5 | 3,323,044.0 | 142,410,379.0 | 56,858.0 |
| `logparse-atomic-removed` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 143,271,774.0 | 142,665,980.0 | 143,929,422.0 | 471,392.0 | 5 | 84,368 | 59,175 | 39,242 | 0.003 | compiled=5 | 3,151,370.0 | 140,223,467.0 | 49,173.0 |
| `logparse-atomic-removed` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 140,200,478.0 | 139,705,906.0 | 140,827,429.0 | 386,175.6 | 5 | 84,408 | 59,248 | 39,315 | 0.003 | compiled=5 | 2,255,591.0 | 138,048,773.0 | 63,980.0 |
| `logparse-atomic-removed` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 141,873,161.0 | 140,813,524.0 | 142,488,269.0 | 607,903.2 | 5 | 84,368 | 59,175 | 39,242 | 0.004 | compiled=5 | 2,236,394.0 | 139,579,038.0 | 57,729.0 |
| `mojibake-curly-quote` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 84,228,979.0 | 83,171,496.0 | 85,924,134.0 | 1,095,213.2 | 5 | 33,280 | 20,907 | 15,704 | 0.013 (max is trial 1) | compiled=5 | 3,199,050.0 | 80,981,197.0 | 51,307.0 |
| `mojibake-curly-quote` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 80,949,055.0 | 80,766,872.0 | 82,293,149.0 | 567,763.4 | 5 | 33,176 | 19,807 | 16,045 | 0.007 | compiled=5 | 1,965,094.0 | 78,957,272.0 | 46,077.0 |
| `mojibake-curly-quote` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 84,511,657.0 | 84,153,681.0 | 87,174,264.0 | 1,113,476.4 | 5 | 33,280 | 20,907 | 15,704 | 0.013 | compiled=5 | 3,138,234.0 | 81,469,985.0 | 45,897.0 |
| `mojibake-curly-quote` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 81,204,063.0 | 80,426,288.0 | 81,490,443.0 | 378,989.4 | 5 | 33,176 | 19,807 | 16,045 | 0.005 | compiled=5 | 1,857,991.0 | 79,406,876.0 | 53,170.0 |
| `negation-scope-lookbehind-var` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `negation-scope-lookbehind-var` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `nested-comment-rec` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 150,619,884.0 | 149,965,009.0 | 154,231,843.0 | 1,569,902.8 | 5 | 37,392 | 34,708 | 33,009 | 0.010 | compiled=5 | 2,883,435.0 | 147,945,312.0 | 53,130.0 |
| `nested-comment-rec` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 151,487,068.0 | 150,077,271.0 | 152,839,157.0 | 1,076,810.0 | 5 | 37,392 | 34,821 | 33,122 | 0.007 | compiled=5 | 2,763,469.0 | 148,443,471.0 | 50,154.0 |
| `nested-comment-rec` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 153,031,518.0 | 151,127,951.0 | 154,412,370.0 | 1,269,067.9 | 5 | 37,392 | 34,708 | 33,009 | 0.008 (max is trial 1) | compiled=5 | 2,038,281.0 | 150,869,192.0 | 52,288.0 |
| `nested-comment-rec` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 151,630,136.0 | 151,035,736.0 | 160,965,169.0 | 3,725,007.5 | 5 | 37,392 | 34,821 | 33,122 | 0.025 | compiled=5 | 1,938,402.0 | 149,706,021.0 | 50,084.0 |
| `numeric-id-nested-plus` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 134,789,895.0 | 131,233,901.0 | 135,257,146.0 | 1,887,440.7 | 5 | 37,416 | 31,751 | 30,069 | 0.014 | compiled=5 | 1,712,398.0 | 133,067,698.0 | 50,515.0 |
| `numeric-id-nested-plus` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 134,156,672.0 | 132,251,319.0 | 135,956,804.0 | 1,320,376.8 | 5 | 37,416 | 31,680 | 29,998 | 0.010 | compiled=5 | 1,641,154.0 | 132,313,407.0 | 43,011.0 |
| `numeric-id-nested-plus` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 134,344,564.0 | 132,831,470.0 | 135,250,431.0 | 936,691.5 | 5 | 37,416 | 31,751 | 30,069 | 0.007 | compiled=5 | 1,480,720.0 | 132,575,189.0 | 50,285.0 |
| `numeric-id-nested-plus` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 133,506,092.0 | 132,150,618.0 | 134,295,281.0 | 736,368.5 | 5 | 37,416 | 31,680 | 29,998 | 0.006 | compiled=5 | 1,658,145.0 | 131,899,977.0 | 54,122.0 |
| `phone-list-nested-plus` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 139,535,370.0 | 139,019,828.0 | 141,183,607.0 | 814,306.8 | 5 | 37,496 | 33,023 | 31,081 | 0.006 | compiled=5 | 1,695,345.0 | 137,793,758.0 | 49,573.0 |
| `phone-list-nested-plus` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 138,138,939.0 | 137,373,626.0 | 140,644,310.0 | 1,124,167.6 | 5 | 37,456 | 32,951 | 31,009 | 0.008 | compiled=5 | 1,808,940.0 | 136,224,449.0 | 44,214.0 |
| `phone-list-nested-plus` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 141,533,201.0 | 137,888,762.0 | 142,008,455.0 | 1,506,830.2 | 5 | 37,496 | 33,023 | 31,081 | 0.011 | compiled=5 | 1,727,515.0 | 139,653,127.0 | 53,701.0 |
| `phone-list-nested-plus` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 138,148,081.0 | 137,182,560.0 | 139,157,494.0 | 645,872.7 | 5 | 37,456 | 32,951 | 31,009 | 0.005 | compiled=5 | 1,772,410.0 | 136,293,907.0 | 50,284.0 |
| `phone-palindrome-6` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 213,630,909.0 | 211,061,866.0 | 214,586,008.0 | 1,275,370.1 | 5 | 36,920 | 26,386 | 24,918 | 0.006 | compiled=5 | 1,765,728.0 | 211,210,466.0 | 43,332.0 |
| `phone-palindrome-6` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 116,484,860.0 | 114,935,099.0 | 118,164,376.0 | 1,026,259.1 | 5 | 32,904 | 26,194 | 24,726 | 0.009 | compiled=5 | 2,485,966.0 | 113,960,502.0 | 51,597.0 |
| `phone-palindrome-6` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 215,420,495.0 | 213,677,421.0 | 220,642,005.0 | 2,447,541.8 | 5 | 36,920 | 26,386 | 24,918 | 0.011 | compiled=5 | 1,604,224.0 | 214,014,376.0 | 51,778.0 |
| `phone-palindrome-6` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 117,556,968.0 | 115,234,472.0 | 117,963,603.0 | 1,061,986.7 | 5 | 32,904 | 26,194 | 24,726 | 0.009 (max is trial 1) | compiled=5 | 1,412,922.0 | 115,961,532.0 | 51,477.0 |
| `pwd-strength-chain` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 130,582,735.0 | 129,933,050.0 | 132,096,247.0 | 851,652.0 | 5 | 37,472 | 34,336 | 31,695 | 0.007 | compiled=5 | 2,549,727.0 | 128,236,893.0 | 43,111.0 |
| `pwd-strength-chain` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 132,980,205.0 | 130,157,253.0 | 133,457,595.0 | 1,317,204.8 | 5 | 37,472 | 34,264 | 31,623 | 0.010 (max is trial 1) | compiled=5 | 2,700,521.0 | 130,223,578.0 | 56,106.0 |
| `pwd-strength-chain` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 131,864,300.0 | 129,847,218.0 | 132,061,160.0 | 932,815.8 | 5 | 37,472 | 34,336 | 31,695 | 0.007 | compiled=5 | 1,803,158.0 | 130,198,710.0 | 48,902.0 |
| `pwd-strength-chain` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 130,706,618.0 | 130,530,316.0 | 133,051,357.0 | 1,098,891.8 | 5 | 37,472 | 34,264 | 31,623 | 0.008 (max is trial 1) | compiled=5 | 1,735,370.0 | 128,975,034.0 | 50,125.0 |
| `quoted-delim-match` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 138,582,074.0 | 137,652,891.0 | 140,903,146.0 | 1,181,840.6 | 5 | 37,424 | 30,987 | 28,826 | 0.009 | compiled=5 | 2,544,486.0 | 135,937,368.0 | 48,902.0 |
| `quoted-delim-match` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 138,399,739.0 | 137,700,321.0 | 142,054,468.0 | 1,741,567.5 | 5 | 37,424 | 31,100 | 28,939 | 0.013 | compiled=5 | 2,536,471.0 | 135,707,464.0 | 54,322.0 |
| `quoted-delim-match` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 138,401,388.0 | 136,650,498.0 | 140,370,959.0 | 1,246,910.0 | 5 | 37,424 | 30,987 | 28,826 | 0.009 (max is trial 1) | compiled=5 | 1,733,807.0 | 136,529,751.0 | 53,340.0 |
| `quoted-delim-match` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 140,005,471.0 | 138,400,366.0 | 143,310,559.0 | 1,936,889.5 | 5 | 37,424 | 31,100 | 28,939 | 0.014 | compiled=5 | 1,824,689.0 | 137,122,027.0 | 44,594.0 |
| `router-prefix-order` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 78,707,892.0 | 78,043,529.0 | 79,354,971.0 | 491,645.1 | 5 | 28,888 | 16,138 | 14,127 | 0.006 | compiled=5 | 2,212,721.0 | 76,345,218.0 | 53,371.0 |
| `router-prefix-order` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 83,609,973.0 | 83,242,450.0 | 85,253,349.0 | 743,063.9 | 5 | 33,176 | 20,544 | 16,042 | 0.009 | compiled=5 | 2,568,432.0 | 80,681,763.0 | 48,531.0 |
| `router-prefix-order` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 78,795,896.0 | 77,604,789.0 | 79,080,392.0 | 527,557.7 | 5 | 28,888 | 16,138 | 14,127 | 0.007 (max is trial 1) | compiled=5 | 2,190,328.0 | 76,512,963.0 | 53,480.0 |
| `router-prefix-order` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 80,123,728.0 | 79,787,184.0 | 80,303,326.0 | 212,971.9 | 5 | 33,176 | 20,544 | 16,042 | 0.003 | compiled=5 | 2,338,126.0 | 77,508,810.0 | 49,423.0 |
| `tag-depth3-bound` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 169,430,160.0 | 168,869,273.0 | 170,231,802.0 | 496,606.4 | 5 | 37,472 | 38,732 | 36,748 | 0.003 | compiled=5 | 2,953,858.0 | 166,540,774.0 | 49,924.0 |
| `tag-depth3-bound` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 169,400,755.0 | 168,697,098.0 | 170,710,174.0 | 758,043.9 | 5 | 37,472 | 38,845 | 36,861 | 0.004 (max is trial 1) | compiled=5 | 2,981,530.0 | 166,304,178.0 | 52,579.0 |
| `tag-depth3-bound` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 169,559,343.0 | 168,263,160.0 | 171,416,123.0 | 1,116,167.0 | 5 | 37,472 | 38,732 | 36,748 | 0.007 | compiled=5 | 2,201,609.0 | 167,202,101.0 | 55,595.0 |
| `tag-depth3-bound` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 169,542,090.0 | 168,795,132.0 | 169,807,882.0 | 384,599.0 | 5 | 37,472 | 38,845 | 36,861 | 0.002 | compiled=5 | 2,090,369.0 | 167,509,821.0 | 55,485.0 |
| `tag-pair-match` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 130,005,847.0 | 127,495,364.0 | 131,296,370.0 | 1,239,674.8 | 5 | 33,160 | 30,680 | 28,003 | 0.010 | compiled=5 | 3,010,935.0 | 126,789,575.0 | 55,504.0 |
| `tag-pair-match` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 127,624,677.0 | 126,755,511.0 | 130,937,995.0 | 1,678,536.5 | 5 | 33,160 | 30,793 | 28,116 | 0.013 | compiled=5 | 2,252,816.0 | 125,321,577.0 | 48,361.0 |
| `tag-pair-match` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 127,484,726.0 | 126,813,942.0 | 128,797,420.0 | 688,901.5 | 5 | 33,160 | 30,680 | 28,003 | 0.005 | compiled=5 | 2,145,222.0 | 125,292,805.0 | 48,461.0 |
| `tag-pair-match` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 125,637,385.0 | 125,373,648.0 | 128,934,077.0 | 1,410,813.0 | 5 | 33,160 | 30,793 | 28,116 | 0.011 | compiled=5 | 1,952,600.0 | 123,571,933.0 | 53,040.0 |
| `tail-digits-eol` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 83,134,917.0 | 82,719,944.0 | 83,334,864.0 | 238,723.7 | 5 | 33,128 | 19,601 | 16,146 | 0.003 | compiled=5 | 1,867,260.0 | 81,407,951.0 | 50,235.0 |
| `tail-digits-eol` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 84,447,871.0 | 83,886,975.0 | 85,429,682.0 | 555,465.1 | 5 | 33,176 | 20,809 | 17,263 | 0.007 | compiled=5 | 1,744,899.0 | 82,606,761.0 | 54,994.0 |
| `tail-digits-eol` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 79,693,697.0 | 79,600,412.0 | 80,088,241.0 | 206,408.5 | 5 | 33,128 | 18,795 | 15,340 | 0.003 | compiled=5 | 1,557,114.0 | 78,155,869.0 | 50,796.0 |
| `tail-digits-eol` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 79,164,289.0 | 78,519,484.0 | 80,119,410.0 | 556,151.6 | 5 | 33,176 | 19,570 | 16,024 | 0.007 | compiled=5 | 1,599,915.0 | 77,506,265.0 | 44,764.0 |
| `tail-dotstar-txt` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 83,892,414.0 | 83,169,873.0 | 84,435,078.0 | 536,024.3 | 5 | 33,216 | 23,192 | 16,351 | 0.006 | compiled=5 | 2,155,252.0 | 81,660,447.0 | 41,057.0 |
| `tail-dotstar-txt` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 83,871,916.0 | 83,564,165.0 | 84,304,582.0 | 247,724.1 | 5 | 33,256 | 23,872 | 16,919 | 0.003 | compiled=5 | 2,180,701.0 | 81,619,580.0 | 49,152.0 |
| `tail-dotstar-txt` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 82,345,605.0 | 81,354,356.0 | 82,523,561.0 | 438,721.2 | 5 | 33,216 | 22,669 | 15,828 | 0.005 | compiled=5 | 1,911,792.0 | 80,221,381.0 | 53,581.0 |
| `tail-dotstar-txt` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 83,497,776.0 | 82,448,178.0 | 84,882,296.0 | 808,450.3 | 5 | 33,256 | 23,449 | 16,496 | 0.010 | compiled=5 | 1,895,663.0 | 81,514,488.0 | 40,336.0 |
| `tail-ext-lower-txt` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 83,081,577.0 | 82,180,448.0 | 83,947,668.0 | 665,705.2 | 5 | 33,128 | 20,255 | 16,169 | 0.008 | compiled=5 | 2,008,716.0 | 80,800,556.0 | 53,331.0 |
| `tail-ext-lower-txt` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 82,526,740.0 | 82,011,539.0 | 83,259,251.0 | 481,786.0 | 5 | 33,176 | 20,941 | 16,736 | 0.006 | compiled=5 | 2,129,724.0 | 80,332,184.0 | 54,392.0 |
| `tail-ext-lower-txt` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 80,212,114.0 | 79,730,105.0 | 81,651,966.0 | 670,603.6 | 5 | 33,128 | 19,445 | 15,359 | 0.008 | compiled=5 | 1,852,410.0 | 78,322,763.0 | 50,034.0 |
| `tail-ext-lower-txt` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 79,460,186.0 | 79,144,874.0 | 80,142,884.0 | 363,481.5 | 5 | 33,176 | 20,247 | 16,042 | 0.005 (max is trial 1) | compiled=5 | 1,849,706.0 | 77,596,776.0 | 49,914.0 |
| `tail-space-eol` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 88,201,938.0 | 87,927,030.0 | 88,529,966.0 | 205,513.7 | 5 | 33,256 | 25,461 | 17,499 | 0.002 | compiled=5 | 2,024,707.0 | 86,096,099.0 | 52,468.0 |
| `tail-space-eol` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 85,223,353.0 | 83,812,313.0 | 85,799,019.0 | 782,695.5 | 5 | 33,256 | 23,737 | 17,246 | 0.009 | compiled=5 | 1,829,148.0 | 83,335,715.0 | 53,371.0 |
| `tail-space-eol` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 79,583,940.0 | 78,890,324.0 | 80,340,285.0 | 547,412.1 | 5 | 33,128 | 19,116 | 15,571 | 0.007 | compiled=5 | 1,601,698.0 | 77,905,307.0 | 53,491.0 |
| `tail-space-eol` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 79,553,813.0 | 78,660,600.0 | 79,825,757.0 | 420,171.2 | 5 | 33,176 | 19,570 | 16,024 | 0.005 (max is trial 1) | compiled=5 | 1,502,602.0 | 78,037,135.0 | 54,082.0 |
| `tail-word-eoz` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 84,336,782.0 | 84,038,290.0 | 84,771,751.0 | 255,881.7 | 5 | 33,256 | 23,730 | 17,239 | 0.003 | compiled=5 | 1,852,251.0 | 82,500,611.0 | 51,307.0 |
| `tail-word-eoz` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 84,191,068.0 | 83,196,864.0 | 84,938,616.0 | 618,175.3 | 5 | 33,256 | 23,739 | 17,248 | 0.007 | compiled=5 | 1,881,326.0 | 82,255,249.0 | 53,451.0 |
| `tail-word-eoz` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 79,244,962.0 | 78,982,478.0 | 80,155,748.0 | 425,973.6 | 5 | 33,176 | 19,563 | 16,017 | 0.005 | compiled=5 | 1,615,454.0 | 77,581,798.0 | 47,710.0 |
| `tail-word-eoz` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 79,336,503.0 | 78,666,311.0 | 80,103,089.0 | 475,281.1 | 5 | 33,176 | 19,572 | 16,026 | 0.006 | compiled=5 | 1,517,519.0 | 77,766,846.0 | 49,904.0 |
| `trim-nested-star` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 160,170,647.0 | 159,381,238.0 | 164,800,082.0 | 2,029,928.7 | 5 | 37,568 | 30,737 | 28,895 | 0.013 | compiled=5 | 1,563,758.0 | 158,227,003.0 | 54,052.0 |
| `trim-nested-star` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 157,727,040.0 | 156,039,030.0 | 158,642,415.0 | 851,716.2 | 5 | 37,528 | 30,666 | 28,824 | 0.005 | compiled=5 | 1,844,617.0 | 155,758,429.0 | 41,729.0 |
| `trim-nested-star` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 159,384,349.0 | 157,825,611.0 | 160,855,020.0 | 972,762.7 | 5 | 37,568 | 30,737 | 28,895 | 0.006 (max is trial 1) | compiled=5 | 1,675,778.0 | 157,648,778.0 | 52,619.0 |
| `trim-nested-star` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 158,683,098.0 | 156,879,788.0 | 159,406,651.0 | 995,664.6 | 5 | 37,528 | 30,666 | 28,824 | 0.006 | compiled=5 | 1,758,985.0 | 156,847,118.0 | 51,867.0 |
| `utf8-lead-no-cont` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 78,784,296.0 | 77,956,706.0 | 79,593,031.0 | 576,587.0 | 5 | 28,896 | 16,166 | 14,372 | 0.007 | compiled=5 | 1,859,084.0 | 76,879,516.0 | 52,810.0 |
| `utf8-lead-no-cont` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 81,085,333.0 | 80,904,732.0 | 81,673,823.0 | 278,725.1 | 5 | 33,232 | 20,351 | 16,608 | 0.003 | compiled=5 | 2,027,181.0 | 79,012,516.0 | 45,536.0 |
| `utf8-lead-no-cont` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 78,353,813.0 | 77,938,260.0 | 80,541,295.0 | 959,848.4 | 5 | 28,896 | 16,166 | 14,372 | 0.012 | compiled=5 | 1,732,504.0 | 76,538,612.0 | 48,251.0 |
| `utf8-lead-no-cont` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 81,991,939.0 | 81,805,928.0 | 82,136,510.0 | 123,500.2 | 5 | 33,232 | 20,351 | 16,608 | 0.002 | compiled=5 | 1,708,329.0 | 80,286,073.0 | 50,184.0 |
| `uuid-near-miss` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 92,045,793.0 | 90,576,615.0 | 92,338,796.0 | 619,064.6 | 5 | 38,456 | 24,873 | 19,469 | 0.007 (max is trial 1) | compiled=5 | 1,495,058.0 | 90,499,659.0 | 47,760.0 |
| `uuid-near-miss` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 93,494,244.0 | 91,319,624.0 | 94,012,741.0 | 1,126,275.3 | 5 | 38,416 | 24,695 | 19,291 | 0.012 | compiled=5 | 1,457,278.0 | 91,998,344.0 | 52,719.0 |
| `uuid-near-miss` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 92,982,680.0 | 90,717,963.0 | 94,094,675.0 | 1,195,530.9 | 5 | 38,456 | 24,873 | 19,469 | 0.013 | compiled=5 | 1,453,679.0 | 91,526,415.0 | 51,498.0 |
| `uuid-near-miss` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 93,207,664.0 | 91,599,453.0 | 93,612,407.0 | 710,751.8 | 5 | 38,416 | 24,695 | 19,291 | 0.008 | compiled=5 | 1,201,034.0 | 91,792,657.0 | 52,128.0 |
| `wild-codegrammar-json-array-begin` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 75,190,431.0 | 74,813,471.0 | 75,978,087.0 | 433,777.2 | 5 | 28,888 | 15,592 | 13,923 | 0.006 | compiled=5 | 1,670,539.0 | 73,511,818.0 | 52,018.0 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 79,076,717.0 | 78,798,152.0 | 79,786,114.0 | 342,087.6 | 5 | 33,176 | 19,582 | 16,024 | 0.004 (max is trial 1) | compiled=5 | 1,800,323.0 | 77,334,814.0 | 53,491.0 |
| `wild-codegrammar-json-array-begin` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 75,362,605.0 | 74,740,011.0 | 75,732,392.0 | 370,077.7 | 5 | 28,888 | 15,592 | 13,923 | 0.005 | compiled=5 | 1,461,174.0 | 73,935,276.0 | 54,122.0 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 78,964,673.0 | 78,186,327.0 | 80,634,941.0 | 828,261.8 | 5 | 33,176 | 19,582 | 16,024 | 0.010 (max is trial 1) | compiled=5 | 1,514,043.0 | 77,394,885.0 | 52,649.0 |
| `wild-codegrammar-json-constant` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 84,783,665.0 | 84,494,069.0 | 85,397,592.0 | 304,852.1 | 5 | 33,592 | 29,801 | 17,540 | 0.004 | compiled=5 | 2,757,909.0 | 81,968,838.0 | 54,222.0 |
| `wild-codegrammar-json-constant` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 85,102,736.0 | 84,374,833.0 | 85,316,890.0 | 390,231.2 | 5 | 33,344 | 25,975 | 18,066 | 0.005 | compiled=5 | 2,099,527.0 | 82,928,358.0 | 54,252.0 |
| `wild-codegrammar-json-constant` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 85,358,672.0 | 84,765,956.0 | 86,704,398.0 | 697,832.3 | 5 | 33,592 | 29,801 | 17,540 | 0.008 | compiled=5 | 2,613,645.0 | 82,438,820.0 | 54,923.0 |
| `wild-codegrammar-json-constant` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 82,172,128.0 | 81,786,801.0 | 83,049,872.0 | 436,749.2 | 5 | 33,344 | 25,398 | 17,342 | 0.005 | compiled=5 | 1,970,924.0 | 80,196,455.0 | 51,146.0 |
| `wild-codegrammar-json-number-extended` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 88,411,343.0 | 87,637,304.0 | 89,243,702.0 | 527,897.8 | 5 | 33,272 | 25,946 | 17,624 | 0.006 | compiled=5 | 2,404,533.0 | 85,952,067.0 | 56,206.0 |
| `wild-codegrammar-json-number-extended` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 83,412,940.0 | 82,527,392.0 | 84,365,557.0 | 682,742.3 | 5 | 33,176 | 22,457 | 17,095 | 0.008 | compiled=5 | 1,864,515.0 | 81,438,158.0 | 53,812.0 |
| `wild-codegrammar-json-number-extended` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 81,707,492.0 | 80,678,423.0 | 81,879,627.0 | 464,612.2 | 5 | 33,272 | 24,441 | 16,119 | 0.006 | compiled=5 | 2,117,931.0 | 79,539,086.0 | 50,475.0 |
| `wild-codegrammar-json-number-extended` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 80,065,519.0 | 79,587,479.0 | 81,162,115.0 | 603,121.9 | 5 | 33,176 | 21,905 | 16,543 | 0.008 (max is trial 1) | compiled=5 | 1,756,571.0 | 78,370,915.0 | 45,034.0 |
| `wild-codegrammar-json-object-begin` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 75,161,587.0 | 74,459,454.0 | 75,658,594.0 | 462,740.5 | 5 | 28,888 | 15,594 | 13,925 | 0.006 (max is trial 1) | compiled=5 | 1,703,371.0 | 73,421,387.0 | 46,718.0 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 79,200,972.0 | 78,673,608.0 | 79,564,586.0 | 331,838.8 | 5 | 33,176 | 19,583 | 16,025 | 0.004 | compiled=5 | 1,790,425.0 | 77,241,798.0 | 51,236.0 |
| `wild-codegrammar-json-object-begin` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 75,962,805.0 | 75,309,706.0 | 76,165,699.0 | 295,458.0 | 5 | 28,888 | 15,594 | 13,925 | 0.004 (max is trial 1) | compiled=5 | 1,454,741.0 | 74,475,224.0 | 50,154.0 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 79,495,333.0 | 78,545,885.0 | 79,797,133.0 | 439,316.2 | 5 | 33,176 | 19,583 | 16,025 | 0.006 (max is trial 1) | compiled=5 | 1,529,151.0 | 77,920,737.0 | 45,646.0 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 81,631,603.0 | 80,994,983.0 | 82,199,753.0 | 439,693.8 | 5 | 33,280 | 22,059 | 15,964 | 0.005 | compiled=5 | 3,055,459.0 | 78,547,219.0 | 52,799.0 |
| `wild-codegrammar-json-stringcontent-escape` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 80,047,537.0 | 79,646,591.0 | 81,586,819.0 | 753,543.6 | 5 | 33,176 | 20,851 | 16,308 | 0.009 | compiled=5 | 1,880,435.0 | 78,116,958.0 | 54,623.0 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 81,396,406.0 | 80,752,393.0 | 81,717,861.0 | 345,575.0 | 5 | 33,280 | 22,059 | 15,964 | 0.004 (max is trial 1) | compiled=5 | 2,756,584.0 | 78,365,605.0 | 52,619.0 |
| `wild-codegrammar-json-stringcontent-escape` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 79,840,124.0 | 79,530,270.0 | 80,502,040.0 | 345,720.0 | 5 | 33,176 | 20,851 | 16,308 | 0.004 | compiled=5 | 1,813,608.0 | 77,986,961.0 | 49,894.0 |
| `wild-datetime-datefinder-alternation` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 235,600,479.0 | - | - |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 3,361,286,441.0 | - | - |
| `wild-datetime-datefinder-alternation` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 236,115,844.0 | - | - |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 3,046,296,948.0 | - | - |
| `wild-datetime-moment-iso8601` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 178,218,967.0 | 177,773,247.0 | 180,539,691.0 | 971,028.2 | 5 | 55,416 | 57,021 | 47,098 | 0.005 (max is trial 1) | compiled=5 | 2,964,458.0 | 175,230,744.0 | 54,282.0 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 178,087,729.0 | 176,882,459.0 | 179,501,254.0 | 972,153.7 | 5 | 55,040 | 55,460 | 45,537 | 0.005 | compiled=5 | 2,992,270.0 | 174,901,664.0 | 55,454.0 |
| `wild-datetime-moment-iso8601` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 181,345,442.0 | 178,590,542.0 | 186,001,306.0 | 2,394,733.8 | 5 | 55,416 | 57,021 | 47,098 | 0.013 | compiled=5 | 2,195,748.0 | 179,052,583.0 | 58,220.0 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 176,244,019.0 | 175,233,807.0 | 176,463,984.0 | 446,994.4 | 5 | 55,040 | 55,460 | 45,537 | 0.003 (max is trial 1) | compiled=5 | 2,015,358.0 | 174,070,043.0 | 61,085.0 |
| `wild-logparse-base10num-grok` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 124,205,824.0 | 123,782,867.0 | 124,396,485.0 | 204,327.6 | 5 | 33,472 | 37,124 | 29,859 | 0.002 (max is trial 1) | compiled=5 | 3,221,372.0 | 120,937,143.0 | 50,435.0 |
| `wild-logparse-base10num-grok` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 116,237,484.0 | 115,204,657.0 | 117,420,414.0 | 735,353.3 | 5 | 33,232 | 31,127 | 28,577 | 0.006 | compiled=5 | 2,745,495.0 | 113,415,615.0 | 52,809.0 |
| `wild-logparse-base10num-grok` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 118,734,536.0 | 117,870,858.0 | 119,374,804.0 | 507,356.3 | 5 | 33,424 | 34,527 | 28,741 | 0.004 | compiled=5 | 2,488,339.0 | 116,143,564.0 | 48,993.0 |
| `wild-logparse-base10num-grok` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 115,552,031.0 | 115,456,240.0 | 116,839,566.0 | 589,832.6 | 5 | 33,232 | 31,127 | 28,577 | 0.005 | compiled=5 | 1,860,786.0 | 113,716,020.0 | 50,486.0 |
| `wild-logparse-base10num-noatomic` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 92,077,854.0 | 91,758,864.0 | 92,538,090.0 | 251,123.9 | 5 | 33,472 | 26,859 | 18,254 | 0.003 | compiled=5 | 2,487,609.0 | 89,615,152.0 | 49,643.0 |
| `wild-logparse-base10num-noatomic` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 84,161,041.0 | 83,996,220.0 | 84,811,566.0 | 300,041.2 | 5 | 33,280 | 21,429 | 17,412 | 0.004 | compiled=5 | 1,855,638.0 | 82,252,112.0 | 57,057.0 |
| `wild-logparse-base10num-noatomic` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 84,346,635.0 | 82,061,328.0 | 87,058,305.0 | 1,723,793.1 | 5 | 33,432 | 23,620 | 16,494 | 0.020 | compiled=5 | 2,268,865.0 | 82,024,109.0 | 53,661.0 |
| `wild-logparse-base10num-noatomic` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 83,080,921.0 | 82,555,361.0 | 83,459,705.0 | 344,106.4 | 5 | 33,280 | 20,879 | 16,862 | 0.004 | compiled=5 | 1,841,851.0 | 81,185,318.0 | 51,477.0 |
| `wild-logparse-quotedstring-grok` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 200,849,505.0 | 199,828,510.0 | 201,789,306.0 | 728,926.0 | 5 | 46,408 | 66,095 | 45,434 | 0.004 | compiled=5 | 4,529,478.0 | 196,298,757.0 | 50,425.0 |
| `wild-logparse-quotedstring-grok` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 198,906,142.0 | 192,669,466.0 | 204,291,533.0 | 4,158,708.2 | 5 | 41,936 | 52,583 | 44,277 | 0.021 | compiled=5 | 4,588,889.0 | 193,903,603.0 | 54,112.0 |
| `wild-logparse-quotedstring-grok` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 207,486,585.0 | 204,775,645.0 | 208,469,606.0 | 1,401,173.8 | 5 | 46,408 | 66,095 | 45,434 | 0.007 (max is trial 1) | compiled=5 | 3,792,627.0 | 203,326,705.0 | 52,018.0 |
| `wild-logparse-quotedstring-grok` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 199,252,087.0 | 198,216,205.0 | 200,183,192.0 | 690,904.4 | 5 | 41,936 | 52,583 | 44,277 | 0.003 | compiled=5 | 3,638,517.0 | 195,601,428.0 | 46,377.0 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 101,961,604.0 | 100,753,768.0 | 102,076,280.0 | 505,919.2 | 5 | 37,968 | 44,989 | 18,925 | 0.005 | compiled=5 | 4,887,703.0 | 96,926,524.0 | 52,649.0 |
| `wild-logparse-quotedstring-noatomic` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 94,573,840.0 | 93,468,244.0 | 95,605,954.0 | 693,702.8 | 5 | 33,552 | 32,145 | 18,300 | 0.007 | compiled=5 | 3,734,710.0 | 90,851,112.0 | 41,047.0 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 99,011,090.0 | 97,957,745.0 | 100,658,966.0 | 898,336.3 | 5 | 37,968 | 44,989 | 18,925 | 0.009 (max is trial 1) | compiled=5 | 3,910,740.0 | 95,270,681.0 | 50,676.0 |
| `wild-logparse-quotedstring-noatomic` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 93,596,976.0 | 92,661,084.0 | 95,323,592.0 | 898,081.3 | 5 | 33,552 | 32,145 | 18,300 | 0.010 | compiled=5 | 3,280,802.0 | 90,273,875.0 | 52,579.0 |
| `wild-logparse-syslogbase-expanded` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 2,431,309,514.0 | 2,400,414,958.0 | 2,445,818,203.0 | 16,442,475.9 | 5 | 181,400 | 516,370 (warned) | 300,070 | 0.007 | compiled=5 | 299,245,949.0 | 2,135,331,885.0 | 52,178.0 |
| `wild-logparse-syslogbase-expanded` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 2,542,180,973.0 | 2,444,521,137.0 | 2,863,954,055.0 | 174,546,855.5 | 5 | 189,264 | 561,742 (warned) | 299,134 | 0.069 | compiled=5 | 642,271,201.0 | 1,845,807,300.0 | 47,690.0 |
| `wild-logparse-syslogbase-expanded` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2,449,980,481.0 | 2,223,273,808.0 | 2,556,732,348.0 | 110,673,758.0 | 5 | 181,400 | 516,370 (warned) | 300,070 | 0.045 | compiled=5 | 297,913,879.0 | 2,151,416,768.0 | 49,814.0 |
| `wild-logparse-syslogbase-expanded` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 2,697,089,611.0 | 2,470,716,086.0 | 2,771,937,578.0 | 124,016,837.0 | 5 | 189,264 | 561,742 (warned) | 299,134 | 0.046 | compiled=5 | 612,912,983.0 | 2,091,281,386.0 | 50,044.0 |
| `wild-logparse-winpath-grok` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 138,591,171.0 | 136,520,757.0 | 139,043,884.0 | 929,799.2 | 5 | 37,712 | 39,372 | 30,888 | 0.007 (max is trial 1) | compiled=5 | 4,491,877.0 | 134,231,392.0 | 51,146.0 |
| `wild-logparse-winpath-grok` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 128,576,763.0 | 126,515,177.0 | 130,403,406.0 | 1,257,231.9 | 5 | 33,384 | 33,854 | 29,931 | 0.010 | compiled=5 | 3,079,335.0 | 125,484,414.0 | 53,400.0 |
| `wild-logparse-winpath-grok` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 133,449,456.0 | 133,140,174.0 | 133,955,750.0 | 290,102.1 | 5 | 37,712 | 38,881 | 30,397 | 0.002 | compiled=5 | 3,962,567.0 | 129,340,975.0 | 54,213.0 |
| `wild-logparse-winpath-grok` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 128,365,707.0 | 126,582,857.0 | 131,089,428.0 | 1,516,935.2 | 5 | 33,384 | 33,854 | 29,931 | 0.012 | compiled=5 | 2,055,453.0 | 126,200,597.0 | 43,401.0 |
| `wild-secrets-aws-access-key-id` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 127,312,440.0 | 126,955,688.0 | 128,229,829.0 | 424,766.4 | 5 | 33,248 | 36,965 | 29,288 | 0.003 | compiled=5 | 6,751,817.0 | 120,486,915.0 | 49,924.0 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 123,817,012.0 | 122,748,888.0 | 124,777,432.0 | 735,008.7 | 5 | 33,200 | 38,975 | 30,230 | 0.006 | compiled=5 | 4,045,506.0 | 119,608,439.0 | 48,862.0 |
| `wild-secrets-aws-access-key-id` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 126,946,031.0 | 125,860,986.0 | 127,702,756.0 | 683,741.0 | 5 | 33,248 | 36,965 | 29,288 | 0.005 | compiled=5 | 5,727,994.0 | 121,136,914.0 | 52,739.0 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 123,553,468.0 | 121,970,967.0 | 124,693,958.0 | 955,773.6 | 5 | 33,200 | 38,975 | 30,230 | 0.008 | compiled=5 | 3,098,839.0 | 120,225,466.0 | 42,911.0 |
| `wild-secrets-github-pat` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 247,782,141.0 | 247,346,169.0 | 251,121,136.0 | 1,392,837.0 | 5 | 41,360 | 41,877 | 27,019 | 0.006 | compiled=5 | 8,554,494.0 | 239,361,870.0 | 50,686.0 |
| `wild-secrets-github-pat` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 225,996,336.0 | 224,982,225.0 | 226,489,747.0 | 540,521.5 | 5 | 41,304 | 42,934 | 26,513 | 0.002 | compiled=5 | 4,867,225.0 | 221,183,063.0 | 54,974.0 |
| `wild-secrets-github-pat` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 249,215,370.0 | 248,387,150.0 | 255,886,361.0 | 2,899,379.6 | 5 | 41,360 | 41,877 | 27,019 | 0.012 | compiled=5 | 7,853,039.0 | 241,309,040.0 | 53,291.0 |
| `wild-secrets-github-pat` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 232,379,504.0 | 230,677,757.0 | 234,083,824.0 | 1,283,731.1 | 5 | 41,304 | 42,934 | 26,513 | 0.006 (max is trial 1) | compiled=5 | 3,790,152.0 | 228,547,082.0 | 42,000.0 |
| `wild-secrets-slack-webhook-url` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 153,411,306.0 | 150,087,780.0 | 157,898,253.0 | 3,015,259.1 | 5 | 58,024 | 107,666 | 36,316 | 0.020 | compiled=5 | 10,152,377.0 | 143,195,199.0 | 55,515.0 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 140,265,575.0 | 137,768,811.0 | 140,881,557.0 | 1,193,298.3 | 5 | 41,456 | 57,188 | 34,564 | 0.009 | compiled=5 | 5,136,132.0 | 134,953,774.0 | 59,632.0 |
| `wild-secrets-slack-webhook-url` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 147,741,607.0 | 145,862,648.0 | 148,453,070.0 | 974,494.7 | 5 | 53,840 | 103,347 | 34,285 | 0.007 | compiled=5 | 9,103,404.0 | 138,594,852.0 | 45,666.0 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 132,762,913.0 | 132,113,099.0 | 135,364,305.0 | 1,177,431.8 | 5 | 37,272 | 53,008 | 32,651 | 0.009 | compiled=5 | 4,616,440.0 | 127,786,295.0 | 48,462.0 |
| `wild-secrets-username-password-pair` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 296,036,239.0 | 294,900,238.0 | 297,655,933.0 | 1,116,015.4 | 5 | 214,272 | 555,019 (warned) | 47,226 | 0.004 | compiled=5 | 29,044,468.0 | 266,761,166.0 | 50,175.0 |
| `wild-secrets-username-password-pair` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 212,020,702.0 | 209,688,367.0 | 213,220,384.0 | 1,316,917.8 | 5 | 54,288 | 99,799 | 43,288 | 0.006 | compiled=5 | 18,509,159.0 | 193,683,958.0 | 53,501.0 |
| `wild-secrets-username-password-pair` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 293,072,025.0 | 291,778,157.0 | 294,556,071.0 | 1,153,746.4 | 5 | 214,272 | 553,907 (warned) | 45,812 | 0.004 | compiled=5 | 28,290,131.0 | 264,905,917.0 | 45,927.0 |
| `wild-secrets-username-password-pair` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 213,504,035.0 | 211,524,854.0 | 224,424,483.0 | 4,796,737.3 | 5 | 54,288 | 99,799 | 43,288 | 0.022 (max is trial 1) | compiled=5 | 17,775,216.0 | 195,727,896.0 | 53,932.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 82,544,784.0 | 81,762,109.0 | 84,865,840.0 | 1,046,554.2 | 5 | 32,984 | 16,834 | 15,006 | 0.013 | compiled=5 | 2,233,309.0 | 80,172,693.0 | 53,080.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 84,834,912.0 | 84,679,829.0 | 86,270,236.0 | 587,423.2 | 5 | 33,176 | 21,198 | 16,758 | 0.007 | compiled=5 | 2,326,275.0 | 82,374,593.0 | 49,964.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 77,306,959.0 | 76,931,102.0 | 77,880,590.0 | 313,995.3 | 5 | 28,888 | 16,000 | 14,119 | 0.004 (max is trial 1) | compiled=5 | 1,784,893.0 | 75,449,640.0 | 53,140.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 80,644,969.0 | 79,937,766.0 | 81,515,250.0 | 660,479.8 | 5 | 33,176 | 20,539 | 16,037 | 0.008 | compiled=5 | 2,036,197.0 | 78,334,365.0 | 52,780.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 83,194,499.0 | 82,620,216.0 | 85,844,084.0 | 1,238,491.1 | 5 | 33,128 | 19,131 | 15,346 | 0.015 | compiled=5 | 2,231,737.0 | 80,907,919.0 | 51,597.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 82,828,248.0 | 81,798,558.0 | 83,598,511.0 | 595,090.0 | 5 | 33,176 | 19,920 | 16,030 | 0.007 (max is trial 1) | compiled=5 | 1,966,026.0 | 80,815,985.0 | 46,237.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 80,359,984.0 | 79,973,133.0 | 81,972,012.0 | 725,021.7 | 5 | 33,128 | 19,131 | 15,346 | 0.009 | compiled=5 | 2,110,107.0 | 78,262,892.0 | 53,631.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 81,443,866.0 | 80,448,148.0 | 82,533,779.0 | 740,707.0 | 5 | 33,176 | 19,920 | 16,030 | 0.009 | compiled=5 | 2,057,187.0 | 79,261,564.0 | 52,680.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 137,845,354.0 | 135,072,248.0 | 140,010,656.0 | 1,606,110.5 | 5 | 37,632 | 35,239 | 30,405 | 0.012 | compiled=5 | 3,261,728.0 | 134,423,063.0 | 49,784.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 134,839,219.0 | 134,384,732.0 | 136,325,480.0 | 662,275.2 | 5 | 37,488 | 31,965 | 30,162 | 0.005 | compiled=5 | 2,945,833.0 | 131,980,219.0 | 49,884.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 132,379,201.0 | 132,262,531.0 | 132,576,723.0 | 118,193.7 | 5 | 37,632 | 34,465 | 29,631 | 0.001 | compiled=5 | 2,137,198.0 | 130,146,032.0 | 48,692.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 129,690,613.0 | 128,777,161.0 | 130,341,929.0 | 513,266.4 | 5 | 37,488 | 31,309 | 29,506 | 0.004 | compiled=5 | 1,874,121.0 | 127,779,962.0 | 49,273.0 |
| `wild-validator-email-owasp` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 79,145,467.0 | 78,004,666.0 | 79,840,977.0 | 676,876.2 | 5 | 37,192 | 16,843 | 14,486 | 0.009 | compiled=5 | 1,342,982.0 | 77,742,382.0 | 50,725.0 |
| `wild-validator-email-owasp` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 78,126,606.0 | 77,329,746.0 | 79,962,907.0 | 865,414.3 | 5 | 37,192 | 16,666 | 14,309 | 0.011 (max is trial 1) | compiled=5 | 1,364,041.0 | 76,714,264.0 | 49,012.0 |
| `wild-validator-email-owasp` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 79,336,054.0 | 78,755,990.0 | 81,963,344.0 | 1,172,237.7 | 5 | 37,192 | 16,843 | 14,486 | 0.015 | compiled=5 | 1,287,907.0 | 78,217,115.0 | 54,262.0 |
| `wild-validator-email-owasp` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 77,913,143.0 | 77,728,623.0 | 79,521,543.0 | 791,491.3 | 5 | 37,192 | 16,666 | 14,309 | 0.010 | compiled=5 | 1,142,272.0 | 76,779,015.0 | 52,710.0 |
| `wild-validator-ipv4-owasp` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 157,830,055.0 | 157,408,069.0 | 158,367,278.0 | 315,987.3 | 5 | 42,344 | 47,471 | 42,443 | 0.002 | compiled=5 | 2,860,442.0 | 155,449,608.0 | 49,753.0 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 156,909,280.0 | 155,036,098.0 | 159,150,133.0 | 1,428,216.3 | 5 | 42,144 | 46,654 | 41,626 | 0.009 | compiled=5 | 2,950,171.0 | 153,920,225.0 | 48,321.0 |
| `wild-validator-ipv4-owasp` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 158,987,381.0 | 155,268,172.0 | 159,284,612.0 | 1,608,606.5 | 5 | 42,344 | 47,471 | 42,443 | 0.010 (max is trial 1) | compiled=5 | 1,912,083.0 | 156,816,680.0 | 43,862.0 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 153,186,570.0 | 151,478,352.0 | 154,045,088.0 | 954,628.6 | 5 | 42,144 | 46,654 | 41,626 | 0.006 (max is trial 1) | compiled=5 | 1,916,171.0 | 151,147,097.0 | 52,369.0 |
| `wild-validator-us-zip-owasp` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 124,569,568.0 | 123,652,562.0 | 125,384,506.0 | 611,205.3 | 5 | 37,688 | 31,173 | 28,629 | 0.005 (max is trial 1) | compiled=5 | 1,735,341.0 | 122,718,560.0 | 52,870.0 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 122,619,484.0 | 121,815,248.0 | 124,820,121.0 | 1,099,334.6 | 5 | 37,608 | 30,913 | 28,369 | 0.009 | compiled=5 | 1,604,254.0 | 121,078,820.0 | 53,891.0 |
| `wild-validator-us-zip-owasp` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 123,769,657.0 | 122,849,320.0 | 126,252,374.0 | 1,353,598.3 | 5 | 37,688 | 31,173 | 28,629 | 0.011 | compiled=5 | 1,515,776.0 | 122,252,587.0 | 49,743.0 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 123,863,001.0 | 122,560,466.0 | 124,916,136.0 | 942,348.5 | 5 | 37,608 | 30,913 | 28,369 | 0.008 | compiled=5 | 1,631,595.0 | 122,143,200.0 | 54,002.0 |
| `wild-validator-uuid-grok` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 109,999,266.0 | 108,843,286.0 | 111,090,432.0 | 760,025.3 | 5 | 33,528 | 37,712 | 20,314 | 0.007 (max is trial 1) | compiled=5 | 5,471,824.0 | 104,027,318.0 | 46,858.0 |
| `wild-validator-uuid-grok` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 105,092,006.0 | 104,155,220.0 | 106,188,503.0 | 712,227.2 | 5 | 33,536 | 37,272 | 20,988 | 0.007 | compiled=5 | 4,428,247.0 | 101,010,572.0 | 51,818.0 |
| `wild-validator-uuid-grok` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 86,813,995.0 | 86,486,078.0 | 87,296,254.0 | 303,731.0 | 5 | 33,168 | 21,978 | 15,326 | 0.003 (max is trial 1) | compiled=5 | 4,803,482.0 | 81,884,806.0 | 53,421.0 |
| `wild-validator-uuid-grok` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 83,532,302.0 | 82,259,624.0 | 85,087,842.0 | 900,486.2 | 5 | 33,176 | 22,345 | 16,075 | 0.011 | compiled=5 | 3,078,421.0 | 80,429,234.0 | 43,211.0 |
| `wild-waf-crs-942140-dbnames` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 119,423,710.0 | 118,612,952.0 | 120,025,484.0 | 475,686.6 | 5 | 91,216 | 229,297 | 21,335 | 0.004 | compiled=5 | 9,406,220.0 | 109,867,917.0 | 52,800.0 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 111,496,599.0 | 110,182,439.0 | 111,788,207.0 | 706,108.8 | 5 | 74,488 | 170,968 | 20,725 | 0.006 | compiled=5 | 7,562,325.0 | 103,833,994.0 | 50,956.0 |
| `wild-waf-crs-942140-dbnames` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 108,214,201.0 | 108,146,895.0 | 109,408,293.0 | 503,280.4 | 5 | 91,120 | 225,451 | 18,746 | 0.005 | compiled=5 | 8,551,585.0 | 99,626,319.0 | 47,920.0 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 98,985,482.0 | 98,152,832.0 | 100,802,245.0 | 1,041,382.4 | 5 | 74,392 | 167,104 | 18,138 | 0.011 | compiled=5 | 6,918,428.0 | 92,139,281.0 | 54,403.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 107,295,368.0 | 105,487,150.0 | 109,590,114.0 | 1,401,688.0 | 5 | 41,968 | 59,626 | 19,226 | 0.013 | compiled=5 | 6,557,090.0 | 100,751,193.0 | 51,647.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 96,293,972.0 | 95,517,858.0 | 97,778,298.0 | 739,945.4 | 5 | 37,536 | 41,044 | 18,575 | 0.008 | compiled=5 | 3,250,096.0 | 92,866,521.0 | 51,136.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 96,936,971.0 | 96,672,743.0 | 99,416,475.0 | 1,043,659.5 | 5 | 41,872 | 55,274 | 17,437 | 0.011 | compiled=5 | 5,656,329.0 | 91,388,084.0 | 52,960.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 90,070,682.0 | 87,365,725.0 | 91,072,401.0 | 1,345,674.1 | 5 | 37,448 | 36,937 | 17,017 | 0.015 | compiled=5 | 2,611,972.0 | 87,542,027.0 | 51,067.0 |
| `wild-waf-crs-942270-union-select` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 108,096,229.0 | 107,593,652.0 | 110,349,234.0 | 1,101,964.0 | 5 | 37,688 | 39,661 | 18,494 | 0.010 | compiled=5 | 9,464,791.0 | 98,588,477.0 | 50,465.0 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 90,286,879.0 | 87,940,104.0 | 91,497,259.0 | 1,330,792.2 | 5 | 33,352 | 31,007 | 17,010 | 0.015 | compiled=5 | 3,100,514.0 | 87,143,764.0 | 51,217.0 |
| `wild-waf-crs-942270-union-select` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 107,021,094.0 | 104,874,027.0 | 108,400,393.0 | 1,141,037.5 | 5 | 37,688 | 39,661 | 18,494 | 0.011 | compiled=5 | 8,969,813.0 | 97,504,661.0 | 42,109.0 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 88,134,133.0 | 87,927,152.0 | 88,723,854.0 | 273,832.7 | 5 | 33,352 | 31,007 | 17,010 | 0.003 (max is trial 1) | compiled=5 | 2,810,556.0 | 85,204,742.0 | 50,665.0 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 648,693,949.0 | 600,873,939.0 | 685,895,612.0 | 30,147,172.2 | 5 | 685,928 | 395,899 (warned) | 101,419 | 0.046 (max is trial 1) | compiled=5 | 19,543,509.0 | 629,016,297.0 | 134,143.0 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 592,495,295.0 | 590,091,786.0 | 602,373,105.0 | 4,415,335.1 | 5 | 679,520 | 516,574 (warned) | 117,200 | 0.007 | compiled=5 | 17,468,077.0 | 574,684,513.0 | 137,730.0 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 660,814,089.0 | 637,842,190.0 | 675,771,916.0 | 14,904,655.2 | 5 | 685,928 | 395,899 (warned) | 101,419 | 0.023 | compiled=5 | 19,632,977.0 | 641,032,522.0 | 138,480.0 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 592,443,189.0 | 590,184,152.0 | 597,746,481.0 | 2,735,405.9 | 5 | 679,520 | 516,574 (warned) | 117,200 | 0.005 | compiled=5 | 17,144,457.0 | 574,632,947.0 | 144,483.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 85,665,156.0 | 85,176,204.0 | 87,458,757.0 | 779,290.2 | 5 | 33,280 | 22,788 | 16,876 | 0.009 | compiled=5 | 3,641,945.0 | 82,159,979.0 | 50,024.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 80,107,721.0 | 79,722,614.0 | 80,793,272.0 | 375,387.2 | 5 | 33,176 | 20,456 | 16,094 | 0.005 (max is trial 1) | compiled=5 | 2,048,100.0 | 78,021,809.0 | 53,531.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 85,819,881.0 | 85,372,961.0 | 86,093,878.0 | 238,605.9 | 5 | 33,280 | 22,788 | 16,876 | 0.003 | compiled=5 | 3,390,389.0 | 82,236,228.0 | 47,530.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 79,982,962.0 | 79,622,734.0 | 80,560,079.0 | 385,538.9 | 5 | 33,176 | 20,456 | 16,094 | 0.005 (max is trial 1) | compiled=5 | 1,884,401.0 | 77,958,277.0 | 49,774.0 |
| `winpath-near-miss` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 78,911,165.0 | 76,620,317.0 | 80,505,710.0 | 1,286,909.6 | 5 | 37,152 | 16,232 | 14,149 | 0.016 | compiled=5 | 1,300,281.0 | 77,520,394.0 | 44,534.0 |
| `winpath-near-miss` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 78,455,046.0 | 77,899,438.0 | 78,862,374.0 | 373,766.7 | 5 | 37,112 | 16,055 | 13,972 | 0.005 (max is trial 1) | compiled=5 | 1,355,876.0 | 77,016,394.0 | 45,716.0 |
| `winpath-near-miss` | `plain` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 78,321,522.0 | 77,125,006.0 | 79,060,775.0 | 640,879.8 | 5 | 37,152 | 16,232 | 14,149 | 0.008 | compiled=5 | 1,315,549.0 | 77,002,036.0 | 43,281.0 |
| `winpath-near-miss` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna_noedge` | 77,403,881.0 | 76,627,438.0 | 78,334,255.0 | 593,260.1 | 5 | 37,112 | 16,055 | 13,972 | 0.008 | compiled=5 | 1,285,422.0 | 76,075,068.0 | 50,996.0 |
    - emit/code bytes across abi 77: pcrec's size definition moves at the boundary -- a flat ~+106 B of counted stamp and initializer lines on a typical artifact (`RX_COMPOUND`, `RX_MEASURES`, `.measures`/`.next`/`.next_n`), and from abi 83 the find-all iterator scaffold (`_next`, the forwarder twins) is EXCLUDED from both counts with no marker in the emitted text. Read a Delta that spans the boundary against that, not as a program change; the DFA retry machine (`RX_ITER_RETRY=retry`) is NOT scaffold and counts (b142prep: +3-4 KB on narrow DFAs).

