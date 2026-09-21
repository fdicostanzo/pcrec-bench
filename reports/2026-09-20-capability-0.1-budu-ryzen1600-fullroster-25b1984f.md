# pcrec-bench report

reporter: v18 (2026-09-18)

## Query

- filters: subbench=capability, version=0.1, testee=libpcre2_10.46_interp-caps-simdna, testee=libpcre2_10.46_jit-caps-simdna, testee=libpcre2_10.46_dfa-nocaps-simdna, testee=pcrec_25b1984f_auto-caps-simdna, testee=pcrec_25b1984f_auto-nocaps-simdna, testee=pcrec_25b1984f_vm-caps-simdna, testee=pcrec_25b1984f_vm-in-caps-simdna, testee=oniguruma_6.9.10_default-caps-simdna, testee=re2_11.0.0_default-caps-simdna, testee=re2_11.0.0_longest-caps-simdna, testee=rust_1.13.1_default-caps-simdna, testee=tre_0.9.0_default-caps-simdna, testee=vectorscan_5.4.11_block-nosom-nocaps-simd
- record source: store/index.tsv (17 record(s) matching this query)
- records included: 13
- worst other-core busy: 58.96% (`pcrec_25b1984f_auto-nocaps-simdna` / `wild-waf-crs-942140-dbnames` / `large-subject-throughput`)
    - `capability@0.1__libpcre2_10.46_dfa-nocaps-simdna__budu-ryzen1600__20260917T062345Z` (store/records/capability@0.1/libpcre2_10.46_dfa-nocaps-simdna/capability@0.1__libpcre2_10.46_dfa-nocaps-simdna__budu-ryzen1600__20260917T062345Z.jsonl) — agreement: agree (0 of 116 groups; 5 of 4572 rows; 30 unjudged; k=1.5, 2/3; 5 trials)
    - `capability@0.1__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260917T005053Z` (store/records/capability@0.1/libpcre2_10.46_interp-caps-simdna/capability@0.1__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260917T005053Z.jsonl) — agreement: agree (0 of 126 groups; 52 of 4984 rows; 8 unjudged; k=1.5, 2/3; 5 trials)
    - `capability@0.1__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260917T013333Z` (store/records/capability@0.1/libpcre2_10.46_jit-caps-simdna/capability@0.1__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260917T013333Z.jsonl) — agreement: agree (0 of 128 groups; 0 of 4990 rows; 2 unjudged; k=1.5, 2/3; 5 trials)
    - `capability@0.1__oniguruma_6.9.10_default-caps-simdna__budu-ryzen1600__20260918T040233Z` (store/records/capability@0.1/oniguruma_6.9.10_default-caps-simdna/capability@0.1__oniguruma_6.9.10_default-caps-simdna__budu-ryzen1600__20260918T040233Z.jsonl) — agreement: agree (0 of 123 groups; 0 of 4831 rows; 5 unjudged; k=1.5, 2/3; 5 trials)
    - `capability@0.1__pcrec_25b1984f_auto-caps-simdna__budu-ryzen1600__20260920T223410Z` (store/records/capability@0.1/pcrec_25b1984f_auto-caps-simdna/capability@0.1__pcrec_25b1984f_auto-caps-simdna__budu-ryzen1600__20260920T223410Z.jsonl) — agreement: agree (0 of 124 groups; 4 of 4834 rows; 2 unjudged; k=1.5, 2/3; 5 trials)
    - `capability@0.1__pcrec_25b1984f_auto-nocaps-simdna__budu-ryzen1600__20260920T230714Z` (store/records/capability@0.1/pcrec_25b1984f_auto-nocaps-simdna/capability@0.1__pcrec_25b1984f_auto-nocaps-simdna__budu-ryzen1600__20260920T230714Z.jsonl) — agreement: agree (0 of 126 groups; 5 of 4912 rows; 2 unjudged; k=1.5, 2/3; 5 trials)
    - `capability@0.1__pcrec_25b1984f_vm-caps-simdna__budu-ryzen1600__20260920T233551Z` (store/records/capability@0.1/pcrec_25b1984f_vm-caps-simdna/capability@0.1__pcrec_25b1984f_vm-caps-simdna__budu-ryzen1600__20260920T233551Z.jsonl) — agreement: agree (0 of 124 groups; 5 of 4829 rows; 7 unjudged; k=1.5, 2/3; 5 trials)
    - `capability@0.1__pcrec_25b1984f_vm-in-caps-simdna__budu-ryzen1600__20260921T001807Z` (store/records/capability@0.1/pcrec_25b1984f_vm-in-caps-simdna/capability@0.1__pcrec_25b1984f_vm-in-caps-simdna__budu-ryzen1600__20260921T001807Z.jsonl) — agreement: agree (0 of 124 groups; 5 of 4829 rows; 7 unjudged; k=1.5, 2/3; 5 trials)
    - `capability@0.1__re2_11.0.0_default-caps-simdna__budu-ryzen1600__20260919T032209Z` (store/records/capability@0.1/re2_11.0.0_default-caps-simdna/capability@0.1__re2_11.0.0_default-caps-simdna__budu-ryzen1600__20260919T032209Z.jsonl) — agreement: agree (0 of 77 groups; 0 of 3037 rows; 5 unjudged; k=1.5, 2/3; 5 trials)
    - `capability@0.1__re2_11.0.0_longest-caps-simdna__budu-ryzen1600__20260918T052217Z` (store/records/capability@0.1/re2_11.0.0_longest-caps-simdna/capability@0.1__re2_11.0.0_longest-caps-simdna__budu-ryzen1600__20260918T052217Z.jsonl) — agreement: agree (0 of 77 groups; 0 of 3034 rows; 8 unjudged; k=1.5, 2/3; 5 trials)
    - `capability@0.1__rust_1.13.1_default-caps-simdna__budu-ryzen1600__20260919T213423Z` (store/records/capability@0.1/rust_1.13.1_default-caps-simdna/capability@0.1__rust_1.13.1_default-caps-simdna__budu-ryzen1600__20260919T213423Z.jsonl) — agreement: agree (0 of 82 groups; 0 of 3194 rows; 4 unjudged; k=1.5, 2/3; 5 trials)
    - `capability@0.1__tre_0.9.0_default-caps-simdna__budu-ryzen1600__20260919T033612Z` (store/records/capability@0.1/tre_0.9.0_default-caps-simdna/capability@0.1__tre_0.9.0_default-caps-simdna__budu-ryzen1600__20260919T033612Z.jsonl) — agreement: agree (0 of 79 groups; 0 of 3142 rows; 56 unjudged; k=1.5, 2/3; 5 trials)
    - `capability@0.1__vectorscan_5.4.11_block-nosom-nocaps-simd__budu-ryzen1600__20260919T035552Z` (store/records/capability@0.1/vectorscan_5.4.11_block-nosom-nocaps-simd/capability@0.1__vectorscan_5.4.11_block-nosom-nocaps-simd__budu-ryzen1600__20260919T035552Z.jsonl) — agreement: agree (0 of 80 groups; 0 of 3118 rows; 2 unjudged; k=1.5, 2/3; 5 trials)
- superseded: 4 record(s) (OD-B15; --all-records lists them)
- sub-bench version(s): capability@0.1
- machine(s): budu-ryzen1600
- schema version(s): 1.5, 1.6
- grain: set (sum of per-subject ns/call over the whole subject set, reduced over trials; a set cell is excluded if ANY subject in it fails)
- reduction: median/min/max/stddev (population) over per-trial `elapsed_ns / iterations`; lazy-JIT compile cost is DERIVED as first-match-row-minus-steady-state (lowest `seq` timed row for the pattern, minus the median of every other timed row), one value per (pattern, testee), never pooled with another execution-model class's compile cost
- `form`: this report includes a `whole-subject` artifact beside `plain` for at least one cell (schema v1.1: a testee with no end-anchored mode compiles and times a SEPARATE artifact for match-compliance, e.g. `(?:pattern)\z`, where another testee reaches the same regime via runtime flags on its ordinary artifact) -- shown as a per-row COLUMN, not a split: both forms answer the same regime and RANK TOGETHER in one table (`form` is a key only for compile-cost rows, where a whole-subject artifact is genuinely a separate compile with its own cost); `fact` restates it as 'same program' / 'separate artifact' (R4)
- status policy (OD-B14): a ranking row whose record `status` is not `measured` is excluded from ranking by default, listed under its table as `not ranked: <testee> -- <status> (<status_detail excerpt>)`; `--include-unmeasured` ranks it instead, with `status` shown
- trial-agreement policy (schema v1.4, rule v1.4-group, X31-X33): a record's five trials must agree to within k=1.5 on every group of its rows — one slow trial of five tolerated; two, or one fast, is a disagreeing row; a group disagrees at >= 2 disagreeing rows reaching a third of it (d_min=2, c=3); a record with a disagreeing group, or with fewer than five odd trials, is `inconclusive-spread` and unranked like `inconclusive-load`; the after-run load/occupancy samples are provenance (v1.4 X13), shown under --include-provenance
- status rule: v1.4 X13 (pre-flight + trial agreement) on 13 record(s)
- tier policy (R3, schema v1.2 `tier`, absent = `pinned`): a `scratch`-tier row is excluded from ranking by default, listed as `scratch: <testee>`; `--include-scratch` ranks it instead, with a `tier` column
- duplicate-record policy (OD-B15, amended 2026-08-25): the NEWEST MEASURED record per (subbench@version, testee_id, machine) ranks by default -- a newer record that is NOT measured does not supersede a measured one of the same testee and version (listed as "newer, not measured" instead); only when no record in the group is measured does the newest record overall stand (itself unranked per the status policy above, unless --include-unmeasured). `--all-records` shows every record as its own row, its testee id suffixed `@<timestamp>`

## Ranking (per pattern x regime, SET grain: sum over the subject set; best median first)

### `balanced-parens-rec` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 562,266.0 | 0.4085 | 557,095.6 | 568,518.6 | 3,824.2 | 0.194x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,903,815.8 | 2.1099 | 2,887,176.7 | 2,933,939.2 | 15,780.3 | 1.000x | 5.164x |
| 3 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 4,705,332.8 | 3.4189 | 4,688,470.7 | 4,789,755.6 | 36,667.1 | 1.620x | 8.369x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 5,478,750.8 | 3.9809 | 5,473,371.8 | 5,482,206.9 | 3,154.4 | 1.887x | 9.744x |
| 5 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 5,481,441.1 | 3.9829 | 5,476,069.6 | 5,503,772.3 | 10,593.9 | 1.888x | 9.749x |
| 6 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 5,485,431.9 | 3.9858 | 5,482,655.2 | 5,501,764.0 | 6,989.1 | 1.889x | 9.756x |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 5,493,047.8 | 3.9913 | 5,478,924.1 | 5,497,512.2 | 6,425.5 | 1.892x | 9.769x |

#### `balanced-parens-rec` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 432,269.1 | 0.4122 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 2,233,889.5 | 2.1304 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 3,624,544.2 | 3.4566 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 4,174,203.3 | 3.9808 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 4,179,305.7 | 3.9857 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 4,180,918.1 | 3.9872 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 4,187,067.3 | 3.9931 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 105,140.3 | 0.4011 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 534,267.8 | 2.0381 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 865,887.4 | 3.3031 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 1,042,661.7 | 3.9774 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,042,485.6 | 3.9768 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 1,043,194.9 | 3.9795 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 1,043,594.0 | 3.9810 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 25,209.9 | 0.3847 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 132,966.6 | 2.0289 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 214,986.9 | 3.2804 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 260,927.9 | 3.9814 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 260,670.7 | 3.9775 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 261,188.8 | 3.9854 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 261,484.6 | 3.9899 |

- not ranked: `oniguruma_6.9.10_default-caps-simdna` — did-not-compile (onig_new failed (code -116): unmatched close parenthesis)

### `balanced-parens-rec` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,959.0 | 2,846.1 | 3,284.2 | 159.3 | 0.765x | 1.000x | 75 | 39.5 | 40.4 | 100% |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,866.5 | 3,838.5 | 4,063.9 | 83.3 | 1.000x | 1.307x | 75 | 51.6 | 34.4 | 100% |
| 3 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 4,585.5 | 4,567.7 | 5,362.7 | 312.8 | 1.186x | 1.550x | 75 | 61.1 | 30.4 | 100% |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 6,494.0 | 6,319.8 | 6,642.9 | 110.9 | 1.680x | 2.195x | 75 | 86.6 | 8.9 | 100% |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 6,570.4 | 6,256.6 | 6,643.6 | 162.7 | 1.699x | 2.220x | 75 | 87.6 | 18.0 | 100% |
| 6 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 6,643.4 | 6,562.0 | 6,680.0 | 39.6 | 1.718x | 2.245x | 75 | 88.6 | 8.9 | 100% |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 6,683.4 | 6,560.4 | 6,729.4 | 57.1 | 1.729x | 2.259x | 75 | 89.1 | 17.3 | 100% |

- not ranked: `oniguruma_6.9.10_default-caps-simdna` — did-not-compile (onig_new failed (code -116): unmatched close parenthesis)

### `base10num-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 16.9 | 0.0000 | 16.9 | 16.9 | 0.0 | 0.183x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 16.9 | 0.0000 | 16.9 | 17.0 | 0.0 | 0.183x | 1.001x |
| 3 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 80.9 | 0.0001 | 80.5 | 81.2 | 0.2 | 0.874x | 4.785x |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 90.2 | 0.0001 | 87.6 | 90.7 | 1.3 | 0.974x | 5.332x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 92.6 | 0.0001 | 92.5 | 93.1 | 0.2 | 1.000x | 5.477x |
| 6 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 98.6 | 0.0001 | 96.2 | 99.6 | 1.4 | 1.065x | 5.834x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 118.9 | 0.0001 | 114.6 | 123.1 | 3.2 | 1.284x | 7.031x |
| 8 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 167.8 | 0.0001 | 167.6 | 176.0 | 3.3 | 1.812x | 9.923x |
| 9 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 284.7 | 0.0002 | 284.4 | 287.5 | 1.2 | 3.074x | 16.835x |
| 10 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 284.9 | 0.0002 | 283.3 | 287.6 | 1.8 | 3.077x | 16.850x |
| 11 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,065,662.4 | 2.9541 | 4,064,683.4 | 4,067,392.0 | 934.3 | 43901.313x | 240437.683x |
| 12 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,066,818.6 | 2.9550 | 4,065,089.2 | 4,073,718.9 | 3,331.4 | 43913.797x | 240506.055x |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 11,842,838.8 | 8.6051 | 11,797,877.3 | 11,924,289.2 | 44,904.5 | 127879.819x | 700369.190x |

#### `base10num-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 5.6 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 5.6 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 26.8 | 0.0000 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 26.9 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 31.0 | 0.0000 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 32.6 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39.8 | 0.0000 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.8 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 88.3 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 88.6 | 0.0001 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,096,556.8 | 2.9531 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,097,265.7 | 2.9538 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 8,990,462.0 | 8.5740 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 5.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 5.7 | 0.0000 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 26.9 | 0.0001 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 30.7 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 30.8 | 0.0001 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 32.5 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 38.7 | 0.0001 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.8 | 0.0002 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 88.4 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 88.8 | 0.0003 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 774,619.6 | 2.9549 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 774,810.6 | 2.9557 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 2,254,399.1 | 8.5999 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 5.6 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 5.6 | 0.0001 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 27.0 | 0.0004 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 32.3 | 0.0005 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 30.9 | 0.0005 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 32.3 | 0.0005 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 38.6 | 0.0006 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 56.1 | 0.0009 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 107.6 | 0.0016 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 108.0 | 0.0016 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 194,308.6 | 2.9649 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 194,992.4 | 2.9753 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 565,094.0 | 8.6227 |

### `base10num-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 552.0 | 538.6 | 554.5 | 5.8 | 0.122x | 1.000x | 75 | 7.4 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 555.1 | 539.8 | 560.8 | 8.4 | 0.122x | 1.005x | 75 | 7.4 | 8.9 | 100% |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,051.2 | 2,045.9 | 2,056.0 | 4.1 | 0.452x | 3.716x | 75 | 27.3 | 27.2 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,222.6 | 2,222.1 | 2,234.9 | 5.0 | 0.490x | 4.026x | 75 | 29.6 | 16.4 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,177.4 | 3,042.0 | 3,412.1 | 141.1 | 0.700x | 5.756x | 75 | 42.4 | 40.4 | 100% |
| 6 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 4,066.2 | 4,061.9 | 4,067.0 | 1.9 | 0.896x | 7.366x | 75 | 54.2 | 100.0 | 100% |
| 7 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 4,074.3 | 4,061.9 | 4,144.1 | 29.9 | 0.898x | 7.380x | 75 | 54.3 | 100.2 | 100% |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,536.7 | 4,476.0 | 4,546.8 | 29.2 | 1.000x | 8.218x | 75 | 60.5 | 34.4 | 100% |
| 9 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 4,930.6 | 4,891.8 | 5,638.0 | 290.0 | 1.087x | 8.932x | 75 | 65.7 | 30.4 | 100% |
| 10 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 5,620.4 | 5,610.9 | 5,631.8 | 6.9 | 1.239x | 10.181x | 75 | 74.9 | 17.3 | 100% |
| 11 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 5,708.1 | 5,695.9 | 5,725.4 | 10.4 | 1.258x | 10.340x | 75 | 76.1 | 18.0 | 100% |
| 12 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 7,820.8 | 7,793.4 | 8,921.5 | 439.2 | 1.724x | 14.167x | 75 | 104.3 | 58.6 | 100% |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 18,605.5 | 18,486.1 | 18,805.0 | 106.9 | 4.101x | 33.703x | 75 | 248.1 | 27.9 | 100% |

### `bracket-array-define` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 93.6 | 0.0001 | 93.5 | 94.0 | 0.2 | 0.282x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 128.3 | 0.0001 | 122.2 | 132.0 | 4.1 | 0.387x | 1.371x |
| 3 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 311.0 | 0.0002 | 310.6 | 313.0 | 0.9 | 0.938x | 3.322x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 331.4 | 0.0002 | 330.9 | 342.2 | 4.3 | 1.000x | 3.541x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,879,353.7 | 3.5454 | 4,877,747.2 | 4,900,554.2 | 8,611.1 | 14721.821x | 52122.953x |
| 6 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 4,880,173.5 | 3.5460 | 4,878,346.6 | 4,890,342.1 | 4,384.2 | 14724.295x | 52131.710x |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,880,777.6 | 3.5464 | 4,877,389.3 | 4,888,885.9 | 3,922.1 | 14726.118x | 52138.164x |
| 8 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 4,881,409.9 | 3.5469 | 4,879,862.5 | 4,883,732.9 | 1,303.4 | 14728.025x | 52144.918x |

#### `bracket-array-define` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 31.2 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 42.7 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 103.8 | 0.0001 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 110.3 | 0.0001 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,715,594.5 | 3.5435 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 3,717,265.2 | 3.5451 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,715,723.5 | 3.5436 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 3,717,710.8 | 3.5455 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 31.4 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 42.8 | 0.0002 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 103.5 | 0.0004 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 110.3 | 0.0004 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 930,167.9 | 3.5483 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 929,957.9 | 3.5475 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 930,793.4 | 3.5507 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 930,013.2 | 3.5477 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 31.2 | 0.0005 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 42.2 | 0.0006 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 104.1 | 0.0016 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 111.0 | 0.0017 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 233,735.5 | 3.5665 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 233,571.0 | 3.5640 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 233,774.1 | 3.5671 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 233,782.5 | 3.5672 |

### `bracket-array-define` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,915.5 | 2,905.9 | 2,938.8 | 11.4 | 0.330x | 1.000x | 75 | 38.9 | 58.6 | 100% |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,233.6 | 3,109.3 | 3,400.1 | 106.3 | 0.366x | 1.109x | 75 | 43.1 | 40.4 | 100% |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 6,819.6 | 6,810.3 | 6,830.2 | 6.3 | 0.773x | 2.339x | 75 | 90.9 | 18.0 | 100% |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 6,834.4 | 6,826.7 | 6,873.1 | 17.3 | 0.774x | 2.344x | 75 | 91.1 | 8.9 | 100% |
| 5 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 6,882.1 | 6,871.8 | 6,887.3 | 5.5 | 0.780x | 2.361x | 75 | 91.8 | 8.9 | 100% |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 7,078.5 | 7,074.0 | 7,190.7 | 45.5 | 0.802x | 2.428x | 75 | 94.4 | 17.3 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 8,824.7 | 8,806.4 | 8,920.4 | 41.8 | 1.000x | 3.027x | 75 | 117.7 | 34.4 | 100% |
| 8 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 8,881.9 | 8,868.2 | 9,058.8 | 70.9 | 1.006x | 3.046x | 75 | 118.4 | 30.4 | 100% |

### `codegrammar-flat` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 121,332.8 | 0.0882 | 121,232.7 | 121,541.0 | 111.9 | 0.057x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 608,610.2 | 0.4422 | 603,318.0 | 619,435.0 | 5,959.6 | 0.288x | 5.016x |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 629,144.1 | 0.4571 | 617,526.9 | 633,169.3 | 5,449.3 | 0.297x | 5.185x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 907,844.0 | 0.6596 | 900,359.0 | 923,453.5 | 8,149.8 | 0.429x | 7.482x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 2,020,828.2 | 1.4684 | 2,014,143.5 | 2,031,599.3 | 6,372.9 | 0.955x | 16.655x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,116,040.6 | 1.5375 | 2,112,873.8 | 2,117,247.5 | 1,552.2 | 1.000x | 17.440x |
| 7 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 2,237,315.8 | 1.6257 | 2,236,202.2 | 2,247,920.8 | 4,278.3 | 1.057x | 18.440x |
| 8 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,237,627.3 | 1.6259 | 2,236,494.0 | 2,241,591.7 | 1,835.7 | 1.057x | 18.442x |
| 9 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,442,428.7 | 1.7747 | 2,441,687.7 | 2,445,241.0 | 1,223.2 | 1.154x | 20.130x |
| 10 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,448,214.0 | 3.2321 | 4,440,257.2 | 4,470,154.2 | 11,238.8 | 2.102x | 36.661x |
| 11 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 9,735,646.5 | 7.0740 | 9,613,981.1 | 9,806,489.4 | 77,809.8 | 4.601x | 80.239x |
| 12 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 15,415,823.9 | 11.2013 | 14,303,071.9 | 15,973,547.6 | 684,334.2 | 7.285x | 127.054x |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 63,969,063.6 | 46.4805 | 63,711,186.4 | 65,136,253.4 | 524,881.8 | 30.231x | 527.220x |

#### `codegrammar-flat` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 92,514.9 | 0.0882 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 464,025.5 | 0.4425 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 479,852.3 | 0.4576 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 696,379.5 | 0.6641 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 1,544,697.6 | 1.4731 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 1,620,049.8 | 1.5450 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 1,697,389.9 | 1.6188 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,697,191.7 | 1.6186 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,861,370.2 | 1.7751 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,389,880.2 | 3.2328 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 7,449,226.5 | 7.1041 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 11,712,969.9 | 11.1704 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 48,591,284.2 | 46.3403 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 23,060.5 | 0.0880 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 117,356.9 | 0.4477 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 121,593.6 | 0.4638 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 166,476.6 | 0.6351 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 379,416.9 | 1.4474 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 397,465.0 | 1.5162 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 423,926.5 | 1.6172 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 424,430.5 | 1.6191 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 464,531.7 | 1.7720 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 843,764.4 | 3.2187 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 1,830,389.5 | 6.9824 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 2,958,583.6 | 11.2861 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 12,260,570.0 | 46.7704 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 5,756.0 | 0.0878 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 28,074.4 | 0.4284 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 29,501.0 | 0.4501 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 42,012.8 | 0.6411 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 96,628.2 | 1.4744 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 99,035.3 | 1.5112 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 116,024.9 | 1.7704 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 115,706.9 | 1.7655 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 116,506.5 | 1.7777 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 215,925.2 | 3.2948 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 457,626.6 | 6.9828 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 735,328.1 | 11.2202 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 3,072,513.0 | 46.8828 |

### `codegrammar-flat` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 723.9 | 722.7 | 726.1 | 1.1 | 0.265x | 1.000x | 75 | 9.7 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 931.1 | 929.6 | 932.3 | 1.0 | 0.341x | 1.286x | 75 | 12.4 | 8.9 | 100% |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 1,557.2 | 1,554.8 | 1,575.1 | 7.5 | 0.569x | 2.151x | 75 | 20.8 | 18.0 | 100% |
| 4 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 2,456.6 | 2,444.0 | 3,121.7 | 289.8 | 0.898x | 3.394x | 75 | 32.8 | 30.4 | 100% |
| 5 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,471.1 | 2,464.4 | 2,476.7 | 4.7 | 0.904x | 3.413x | 75 | 32.9 | 27.2 | 100% |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,496.1 | 2,436.4 | 2,504.6 | 24.8 | 0.913x | 3.448x | 75 | 33.3 | 16.4 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,734.4 | 2,668.6 | 2,961.0 | 111.7 | 1.000x | 3.777x | 75 | 36.5 | 34.4 | 100% |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,299.6 | 3,188.9 | 3,535.2 | 126.6 | 1.207x | 4.558x | 75 | 44.0 | 40.4 | 100% |
| 9 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 3,766.2 | 3,765.0 | 3,769.3 | 1.5 | 1.377x | 5.203x | 75 | 50.2 | 17.3 | 100% |
| 10 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,640.6 | 5,610.8 | 5,650.8 | 14.9 | 2.063x | 7.792x | 75 | 75.2 | 58.6 | 100% |
| 11 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 7,685.4 | 7,679.8 | 7,790.8 | 41.8 | 2.811x | 10.617x | 75 | 102.5 | 100.2 | 100% |
| 12 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,690.0 | 7,660.0 | 8,275.6 | 239.3 | 2.812x | 10.623x | 75 | 102.5 | 100.0 | 100% |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 23,957.2 | 23,942.3 | 24,648.5 | 278.6 | 8.761x | 33.094x | 75 | 319.4 | 27.9 | 100% |

### `codegrammar-xflag` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 121,304.1 | 0.0881 | 120,649.4 | 121,731.3 | 369.0 | 0.057x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 604,191.1 | 0.4390 | 602,630.9 | 627,321.6 | 9,481.2 | 0.285x | 4.981x |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 646,060.0 | 0.4694 | 635,576.8 | 648,800.5 | 5,284.4 | 0.305x | 5.326x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 904,180.0 | 0.6570 | 892,724.8 | 919,160.0 | 9,340.3 | 0.426x | 7.454x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 2,014,797.5 | 1.4640 | 2,006,964.3 | 2,023,457.0 | 6,181.9 | 0.950x | 16.609x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,121,186.4 | 1.5413 | 2,111,247.3 | 2,122,007.5 | 4,547.1 | 1.000x | 17.487x |
| 7 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,442,944.3 | 1.7751 | 2,441,324.0 | 2,449,735.4 | 3,087.3 | 1.152x | 20.139x |
| 8 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,414,871.2 | 3.2079 | 4,409,817.2 | 4,425,012.2 | 5,237.9 | 2.081x | 36.395x |
| 9 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 9,728,745.7 | 7.0690 | 9,629,121.1 | 9,805,223.6 | 67,491.8 | 4.586x | 80.201x |
| 10 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 14,814,920.1 | 10.7647 | 14,530,742.7 | 16,280,473.3 | 633,152.7 | 6.984x | 122.130x |

#### `codegrammar-xflag` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 92,596.0 | 0.0883 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 463,672.5 | 0.4422 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 492,498.4 | 0.4697 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 696,904.6 | 0.6646 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 1,531,427.8 | 1.4605 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 1,623,317.2 | 1.5481 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,862,007.4 | 1.7757 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,358,119.4 | 3.2026 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 7,428,697.6 | 7.0846 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 11,384,958.4 | 10.8575 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 23,042.9 | 0.0879 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 113,263.1 | 0.4321 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 122,790.6 | 0.4684 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 164,878.2 | 0.6290 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 386,455.5 | 1.4742 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 397,016.3 | 1.5145 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 464,322.9 | 1.7713 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 840,670.7 | 3.2069 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 1,835,720.2 | 7.0027 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 2,782,399.1 | 10.6140 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 5,750.1 | 0.0877 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 28,168.1 | 0.4298 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 30,454.8 | 0.4647 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 42,222.4 | 0.6443 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 97,129.4 | 1.4821 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 99,221.0 | 1.5140 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 116,614.0 | 1.7794 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 212,578.9 | 3.2437 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 464,327.9 | 7.0851 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 691,448.7 | 10.5507 |

### `codegrammar-xflag` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 724.9 | 723.3 | 727.4 | 1.4 | 0.261x | 1.000x | 75 | 9.7 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 932.2 | 931.7 | 934.5 | 1.0 | 0.336x | 1.286x | 75 | 12.4 | 8.9 | 100% |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 1,557.0 | 1,555.6 | 1,558.9 | 1.2 | 0.562x | 2.148x | 75 | 20.8 | 18.0 | 100% |
| 4 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,468.2 | 2,457.0 | 2,474.7 | 5.8 | 0.890x | 3.405x | 75 | 32.9 | 27.2 | 100% |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 2,477.9 | 2,446.8 | 3,469.5 | 446.7 | 0.894x | 3.418x | 75 | 33.0 | 30.4 | 100% |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,486.0 | 2,427.5 | 2,488.3 | 23.1 | 0.897x | 3.429x | 75 | 33.1 | 16.4 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,772.8 | 2,672.9 | 2,889.0 | 76.0 | 1.000x | 3.825x | 75 | 37.0 | 34.4 | 100% |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,154.0 | 3,149.6 | 3,191.9 | 15.7 | 1.137x | 4.351x | 75 | 42.1 | 40.4 | 100% |
| 9 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 3,769.9 | 3,767.5 | 3,780.5 | 4.6 | 1.360x | 5.200x | 75 | 50.3 | 17.3 | 100% |
| 10 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,638.2 | 5,613.3 | 5,653.6 | 15.7 | 2.033x | 7.778x | 75 | 75.2 | 58.6 | 100% |

### `currency-lookbehind-fixed` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,723,358.9 | 1.2522 | 1,722,608.4 | 1,727,284.7 | 1,688.1 | 0.152x | 1.000x |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 9,600,379.3 | 6.9757 | 9,582,038.1 | 9,607,703.2 | 8,643.7 | 0.845x | 5.571x |
| 3 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 10,819,260.4 | 7.8614 | 10,792,630.6 | 10,874,233.5 | 28,319.1 | 0.953x | 6.278x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11,113,158.8 | 8.0749 | 11,108,510.5 | 11,144,880.2 | 13,460.1 | 0.979x | 6.449x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 11,119,254.8 | 8.0794 | 11,111,549.8 | 11,140,778.7 | 10,216.3 | 0.979x | 6.452x |
| 6 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 11,179,316.8 | 8.1230 | 11,171,882.5 | 11,306,435.6 | 51,482.5 | 0.984x | 6.487x |
| 7 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 11,205,442.3 | 8.1420 | 11,169,279.6 | 11,242,453.0 | 27,159.9 | 0.987x | 6.502x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 11,356,965.2 | 8.2521 | 11,329,033.5 | 12,285,092.4 | 370,864.9 | 1.000x | 6.590x |

#### `currency-lookbehind-fixed` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 1,318,109.5 | 1.2570 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 7,351,415.6 | 7.0109 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 8,291,377.1 | 7.9073 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 8,463,985.5 | 8.0719 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 8,469,070.3 | 8.0767 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 8,517,270.1 | 8.1227 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 8,509,781.4 | 8.1156 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 8,710,549.0 | 8.3070 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 325,054.6 | 1.2400 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 1,807,749.4 | 6.8960 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 2,046,429.3 | 7.8065 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 2,116,134.4 | 8.0724 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 2,118,043.6 | 8.0797 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 2,128,465.3 | 8.1195 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 2,127,502.2 | 8.1158 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 2,132,165.0 | 8.1336 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 80,898.6 | 1.2344 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 438,464.7 | 6.6904 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 491,307.6 | 7.4968 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 532,380.5 | 8.1235 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 532,021.3 | 8.1180 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 534,601.8 | 8.1574 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 534,010.2 | 8.1483 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 514,251.2 | 7.8469 |

### `currency-lookbehind-fixed` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 4,033.4 | 4,026.7 | 4,335.2 | 149.7 | 0.253x | 1.000x | 75 | 53.8 | 40.4 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 5,149.0 | 5,141.1 | 5,168.9 | 11.4 | 0.323x | 1.277x | 75 | 68.7 | 8.9 | 100% |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 5,162.3 | 5,147.8 | 5,251.1 | 37.0 | 0.324x | 1.280x | 75 | 68.8 | 8.9 | 100% |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12,382.2 | 12,289.1 | 12,448.7 | 53.4 | 0.776x | 3.070x | 75 | 165.1 | 18.0 | 100% |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 12,634.6 | 12,626.6 | 12,719.0 | 34.8 | 0.792x | 3.132x | 75 | 168.5 | 17.3 | 100% |
| 6 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 15,324.1 | 15,262.1 | 15,399.9 | 44.0 | 0.961x | 3.799x | 75 | 204.3 | 30.4 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 15,949.0 | 15,914.0 | 15,982.4 | 25.3 | 1.000x | 3.954x | 75 | 212.7 | 34.4 | 100% |
| 8 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 17,465.4 | 17,375.1 | 18,436.9 | 400.6 | 1.095x | 4.330x | 75 | 232.9 | 58.6 | 100% |

### `date-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 16.1 | 0.0000 | 16.1 | 17.3 | 0.5 | 0.165x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 30.7 | 0.0000 | 30.5 | 91.2 | 24.2 | 0.314x | 1.902x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 82.0 | 0.0001 | 78.0 | 83.5 | 2.0 | 0.838x | 5.078x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 94.8 | 0.0001 | 93.9 | 95.0 | 0.4 | 0.969x | 5.871x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 97.8 | 0.0001 | 97.8 | 105.0 | 2.9 | 1.000x | 6.059x |
| 6 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 103.4 | 0.0001 | 102.9 | 157.6 | 22.7 | 1.058x | 6.408x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 140.5 | 0.0001 | 132.2 | 144.3 | 4.5 | 1.436x | 8.703x |
| 8 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 167.0 | 0.0001 | 166.8 | 167.2 | 0.1 | 1.708x | 10.347x |
| 9 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 286.4 | 0.0002 | 283.4 | 290.5 | 2.5 | 2.928x | 17.740x |
| 10 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 287.8 | 0.0002 | 285.8 | 291.7 | 2.1 | 2.942x | 17.828x |
| 11 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 3,869,508.7 | 2.8116 | 3,860,489.1 | 3,872,082.2 | 5,028.8 | 39561.332x | 239698.483x |
| 12 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 3,870,069.7 | 2.8120 | 3,869,392.2 | 4,033,316.0 | 65,127.7 | 39567.068x | 239733.235x |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 8,687,624.6 | 6.3125 | 8,682,949.6 | 8,722,121.4 | 15,359.7 | 88821.096x | 538158.874x |

#### `date-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 5.4 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 10.2 | 0.0000 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 25.3 | 0.0000 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 31.5 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 32.6 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 34.3 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 46.6 | 0.0000 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.6 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 88.4 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 88.5 | 0.0001 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 2,947,988.1 | 2.8114 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 2,946,459.8 | 2.8100 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 6,617,874.8 | 6.3113 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 5.4 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 10.2 | 0.0000 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 26.5 | 0.0001 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 31.6 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 32.6 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 34.3 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 46.1 | 0.0002 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.6 | 0.0002 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 89.7 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 88.2 | 0.0003 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 735,872.4 | 2.8071 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 740,627.9 | 2.8253 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 1,655,493.1 | 6.3152 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 5.3 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 10.3 | 0.0002 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 28.3 | 0.0004 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 31.4 | 0.0005 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 32.7 | 0.0005 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 34.4 | 0.0005 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 47.3 | 0.0007 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.8 | 0.0009 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 108.2 | 0.0017 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 112.2 | 0.0017 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 184,873.2 | 2.8209 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 184,700.3 | 2.8183 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 415,326.4 | 6.3374 |

### `date-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 490.9 | 490.0 | 501.3 | 4.2 | 0.113x | 1.000x | 75 | 6.5 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 869.7 | 867.6 | 873.1 | 2.0 | 0.201x | 1.772x | 75 | 11.6 | 8.9 | 100% |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,762.3 | 1,740.5 | 3,003.3 | 497.9 | 0.406x | 3.590x | 75 | 23.5 | 16.4 | 100% |
| 4 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,866.0 | 1,864.4 | 1,878.8 | 5.2 | 0.430x | 3.801x | 75 | 24.9 | 27.2 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,371.9 | 3,356.8 | 3,508.4 | 58.0 | 0.778x | 6.869x | 75 | 45.0 | 40.4 | 100% |
| 6 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 4,237.3 | 4,079.8 | 4,808.2 | 274.3 | 0.977x | 8.632x | 75 | 56.5 | 30.4 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,336.8 | 4,332.3 | 4,406.6 | 28.2 | 1.000x | 8.834x | 75 | 57.8 | 34.4 | 100% |
| 8 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,733.3 | 5,691.7 | 5,790.2 | 35.1 | 1.322x | 11.679x | 75 | 76.4 | 58.6 | 100% |
| 9 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 6,106.5 | 6,103.0 | 6,179.8 | 29.1 | 1.408x | 12.439x | 75 | 81.4 | 18.0 | 100% |
| 10 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 6,299.4 | 6,288.8 | 6,320.1 | 11.0 | 1.453x | 12.832x | 75 | 84.0 | 17.3 | 100% |
| 11 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,631.6 | 9,491.2 | 10,574.8 | 398.4 | 2.221x | 19.620x | 75 | 128.4 | 100.0 | 100% |
| 12 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 9,667.3 | 9,546.6 | 9,706.4 | 70.8 | 2.229x | 19.693x | 75 | 128.9 | 100.2 | 100% |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 13,750.6 | 13,719.8 | 13,805.6 | 31.5 | 3.171x | 28.011x | 75 | 183.3 | 27.9 | 100% |

### `doubled-word` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 13,111,656.5 | 9.5270 | 13,083,420.8 | 13,188,114.4 | 36,229.7 | 0.146x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 25,353,507.5 | 18.4221 | 25,263,706.2 | 25,446,477.9 | 71,051.7 | 0.283x | 1.934x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 25,399,861.5 | 18.4558 | 25,383,975.0 | 25,668,043.3 | 109,352.5 | 0.283x | 1.937x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 25,478,965.5 | 18.5132 | 25,397,291.5 | 25,875,991.6 | 189,014.6 | 0.284x | 1.943x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 25,812,325.3 | 18.7555 | 25,770,745.0 | 25,943,069.6 | 58,805.9 | 0.288x | 1.969x |
| 6 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 80,036,131.5 | 58.1550 | 79,688,787.0 | 80,380,958.5 | 232,715.3 | 0.893x | 6.104x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 89,645,403.0 | 65.1372 | 89,456,335.7 | 90,437,164.0 | 405,966.8 | 1.000x | 6.837x |
| 8 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 214,644,617.5 | 155.9627 | 214,203,910.0 | 215,813,103.0 | 603,659.5 | 2.394x | 16.371x |

#### `doubled-word` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 10,002,109.4 | 9.5388 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 19,347,931.2 | 18.4516 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 19,380,621.8 | 18.4828 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 19,425,139.0 | 18.5253 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 19,685,475.4 | 18.7735 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 60,903,021.0 | 58.0816 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 68,224,564.7 | 65.0640 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 163,981,124.0 | 156.3846 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 2,496,474.4 | 9.5233 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 4,839,166.9 | 18.4600 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 4,834,753.8 | 18.4431 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 4,837,180.5 | 18.4524 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 4,916,646.7 | 18.7555 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 15,257,858.0 | 58.2041 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 17,133,327.7 | 65.3585 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 40,734,300.0 | 155.3890 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 625,940.8 | 9.5511 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,204,833.3 | 18.3843 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 1,205,527.8 | 18.3949 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 1,206,494.9 | 18.4097 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 1,227,576.9 | 18.7313 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 3,851,262.2 | 58.7656 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 4,296,641.0 | 65.5615 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 10,124,105.0 | 154.4816 |

### `doubled-word` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 13,186.3 | 13,148.2 | 13,216.7 | 27.3 | 0.158x | 1.000x | 75 | 175.8 | 40.4 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 20,836.9 | 20,780.6 | 20,871.6 | 31.0 | 0.250x | 1.580x | 75 | 277.8 | 8.9 | 100% |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 20,883.1 | 20,827.0 | 20,947.9 | 42.2 | 0.251x | 1.584x | 75 | 278.4 | 8.9 | 100% |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 20,928.1 | 20,841.3 | 20,936.7 | 39.8 | 0.251x | 1.587x | 75 | 279.0 | 18.0 | 100% |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 21,012.6 | 20,937.9 | 21,047.7 | 46.0 | 0.252x | 1.594x | 75 | 280.2 | 17.3 | 100% |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 83,264.2 | 83,130.5 | 83,734.5 | 210.4 | 1.000x | 6.314x | 75 | 1,110.2 | 34.4 | 100% |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 89,010.3 | 88,938.4 | 89,450.5 | 207.9 | 1.069x | 6.750x | 75 | 1,186.8 | 58.6 | 100% |
| 8 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 211,358.9 | 210,893.3 | 211,918.7 | 327.1 | 2.538x | 16.029x | 75 | 2,818.1 | 27.9 | 100% |

### `dup-param-detect` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 23,240.8 | 0.0169 | 23,212.8 | 23,259.9 | 15.5 | 1.000x | 1.000x | spread |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,228,794.5 | 1.6195 | 2,227,479.4 | 2,233,759.4 | 2,266.2 | 95.900x | 95.900x | spread |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,301,139.6 | 2.3986 | 3,300,435.1 | 3,312,472.0 | 5,023.6 | 142.041x | 142.041x | **dominated**: `t-1m` is 99.6% of this set |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 13,395,576.0 | 9.7333 | 13,392,224.5 | 13,417,704.2 | 9,370.2 | 576.383x | 576.383x | spread |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 13,453,416.7 | 9.7754 | 13,425,654.6 | 16,153,714.4 | 1,075,709.2 | 578.871x | 578.871x | spread |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 13,458,487.0 | 9.7791 | 13,444,938.4 | 13,604,193.9 | 60,172.9 | 579.090x | 579.090x | spread |
| 7 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 13,461,104.8 | 9.7810 | 13,436,038.1 | 13,513,754.0 | 28,193.5 | 579.202x | 579.202x | spread |
| 8 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 185,048,882.0 | 134.4582 | 183,980,472.0 | 186,006,427.0 | 793,633.8 | 7962.253x | 7962.253x | spread |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `dup-param-detect` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,685.5 | 0.0169 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,696,957.5 | 1.6183 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 3,288,704.7 | 3.1364 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 10,213,465.2 | 9.7403 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 10,255,580.2 | 9.7805 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 10,263,073.9 | 9.7876 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 10,271,252.3 | 9.7954 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 140,873,785.5 | 134.3477 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 4,409.7 | 0.0168 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 424,780.4 | 1.6204 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 9,776.0 | 0.0373 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 2,552,298.6 | 9.7362 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 2,558,507.9 | 9.7599 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 2,560,412.0 | 9.7672 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 2,560,828.9 | 9.7688 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 35,411,058.5 | 135.0825 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 1,133.1 | 0.0173 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,683.3 | 1.6279 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 2,509.3 | 0.0383 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 632,048.7 | 9.6443 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 632,853.1 | 9.6566 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 629,057.0 | 9.5986 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 630,191.1 | 9.6160 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 8,764,038.0 | 133.7286 |

### `dup-param-detect` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,338.5 | 3,286.2 | 3,449.9 | 64.2 | 0.575x | 1.000x | 75 | 44.5 | 40.4 | 100% |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 5,805.1 | 5,723.5 | 5,906.3 | 62.9 | 1.000x | 1.739x | 75 | 77.4 | 34.4 | 100% |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 8,896.5 | 8,839.2 | 8,934.6 | 35.8 | 1.533x | 2.665x | 75 | 118.6 | 58.6 | 100% |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 10,836.8 | 10,820.3 | 10,876.2 | 18.8 | 1.867x | 3.246x | 75 | 144.5 | 8.9 | 100% |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 10,858.9 | 10,816.6 | 10,870.5 | 23.5 | 1.871x | 3.253x | 75 | 144.8 | 18.0 | 100% |
| 6 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 10,874.1 | 10,848.3 | 10,892.1 | 16.0 | 1.873x | 3.257x | 75 | 145.0 | 8.9 | 100% |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 10,958.1 | 10,937.4 | 10,970.7 | 12.1 | 1.888x | 3.282x | 75 | 146.1 | 17.3 | 100% |
| 8 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 196,700.5 | 195,658.9 | 197,204.7 | 623.0 | 33.884x | 58.919x | 75 | 2,622.7 | 27.9 | 100% |

### `email-local-nodup` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 258.8 | 0.0002 | 258.1 | 262.6 | 1.7 | 0.094x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 978.8 | 0.0007 | 973.3 | 984.2 | 3.8 | 0.354x | 3.782x |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 981.0 | 0.0007 | 978.9 | 990.1 | 4.1 | 0.355x | 3.790x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 1,381.0 | 0.0010 | 1,373.7 | 1,398.2 | 8.7 | 0.500x | 5.336x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,763.3 | 0.0020 | 2,747.3 | 2,792.8 | 14.8 | 1.000x | 10.677x |
| 6 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 3,885.6 | 0.0028 | 3,873.6 | 4,619.0 | 292.4 | 1.406x | 15.013x |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 3,865,398.7 | 2.8086 | 3,862,618.0 | 3,879,312.6 | 7,100.8 | 1398.854x | 14934.900x |
| 8 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 3,867,490.9 | 2.8102 | 3,863,203.5 | 3,881,125.2 | 6,458.6 | 1399.611x | 14942.983x |

#### `email-local-nodup` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 70.1 | 0.0001 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 230.4 | 0.0002 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 232.9 | 0.0002 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 388.3 | 0.0004 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 653.9 | 0.0006 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 877.4 | 0.0008 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 2,943,567.2 | 2.8072 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 2,942,808.0 | 2.8065 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 105.2 | 0.0004 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 458.1 | 0.0017 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 460.5 | 0.0018 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 555.8 | 0.0021 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 1,279.0 | 0.0049 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,873.9 | 0.0071 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 736,865.6 | 2.8109 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 736,469.4 | 2.8094 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 85.3 | 0.0013 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 289.6 | 0.0044 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 290.6 | 0.0044 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 436.3 | 0.0067 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 831.1 | 0.0127 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,137.5 | 0.0174 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 185,803.4 | 2.8351 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 184,917.2 | 2.8216 |

### `email-local-nodup` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 5,321.7 | 5,132.7 | 5,597.3 | 163.0 | 0.159x | 1.000x | 75 | 71.0 | 40.4 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 10,607.1 | 10,595.3 | 10,736.7 | 54.2 | 0.317x | 1.993x | 75 | 141.4 | 8.9 | 100% |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 10,638.3 | 10,626.2 | 10,716.6 | 32.9 | 0.318x | 1.999x | 75 | 141.8 | 8.9 | 100% |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 15,932.5 | 15,923.4 | 15,948.7 | 8.6 | 0.476x | 2.994x | 75 | 212.4 | 18.0 | 100% |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 16,135.3 | 16,066.7 | 16,178.5 | 36.2 | 0.482x | 3.032x | 75 | 215.1 | 17.3 | 100% |
| 6 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 18,596.6 | 18,446.5 | 18,750.3 | 99.5 | 0.555x | 3.494x | 75 | 248.0 | 58.6 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 33,485.1 | 33,447.6 | 33,582.3 | 53.9 | 1.000x | 6.292x | 75 | 446.5 | 34.4 | 100% |
| 8 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 42,500.9 | 42,084.8 | 43,084.4 | 344.1 | 1.269x | 7.986x | 75 | 566.7 | 30.4 | 100% |

### `email-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 32.7 | 0.0000 | 30.9 | 33.6 | 1.0 | 0.001x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 48.2 | 0.0000 | 46.5 | 50.3 | 1.2 | 0.002x | 1.476x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 107.4 | 0.0001 | 106.9 | 110.1 | 1.2 | 0.004x | 3.288x |
| 4 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 341.4 | 0.0002 | 338.4 | 350.0 | 4.0 | 0.012x | 10.456x |
| 5 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 343.5 | 0.0002 | 340.7 | 362.3 | 7.7 | 0.012x | 10.522x |
| 6 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 2,522.1 | 0.0018 | 2,494.7 | 2,535.3 | 13.7 | 0.091x | 77.244x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 13,928.0 | 0.0101 | 13,918.0 | 13,974.4 | 20.8 | 0.504x | 426.569x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 27,657.6 | 0.0201 | 27,580.1 | 27,846.8 | 114.6 | 1.000x | 847.062x |
| 9 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 31,608.8 | 0.0230 | 31,591.8 | 31,745.3 | 57.3 | 1.143x | 968.075x |
| 10 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,228,826.3 | 1.6195 | 2,227,226.6 | 2,232,639.0 | 1,937.3 | 80.586x | 68261.661x |
| 11 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,484,658.5 | 3.2586 | 4,481,185.7 | 4,507,475.5 | 9,643.1 | 162.149x | 137350.422x |
| 12 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,485,042.0 | 3.2589 | 4,480,684.8 | 4,498,328.6 | 6,190.1 | 162.163x | 137362.168x |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 21,946,697.0 | 15.9467 | 21,270,517.4 | 22,587,559.6 | 492,877.2 | 793.514x | 672155.556x |

#### `email-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 10.8 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 17.2 | 0.0000 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 37.0 | 0.0000 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 113.0 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 114.1 | 0.0001 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,133.7 | 0.0011 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 1,594.6 | 0.0015 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 16,991.2 | 0.0162 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 24,106.2 | 0.0230 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,696,697.9 | 1.6181 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,412,705.5 | 3.2546 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,412,339.7 | 3.2543 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 16,627,798.2 | 15.8575 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 10.6 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 14.9 | 0.0001 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 32.9 | 0.0001 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 102.1 | 0.0004 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 102.7 | 0.0004 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 504.3 | 0.0019 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 9,808.5 | 0.0374 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 2,120.7 | 0.0081 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 5,960.8 | 0.0227 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 424,593.3 | 1.6197 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 854,023.3 | 3.2578 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 853,374.1 | 3.2554 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 4,236,584.6 | 16.1613 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 10.1 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 15.6 | 0.0002 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 37.7 | 0.0006 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 125.1 | 0.0019 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 126.1 | 0.0019 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 889.2 | 0.0136 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 2,528.0 | 0.0386 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 8,563.5 | 0.1307 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,529.4 | 0.0233 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,555.7 | 1.6259 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 216,479.8 | 3.3032 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 217,238.4 | 3.3148 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,071,430.8 | 16.3487 |

### `email-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 975.5 | 967.1 | 977.4 | 3.7 | 0.308x | 1.000x | 75 | 13.0 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,429.6 | 1,423.7 | 1,436.5 | 4.6 | 0.451x | 1.465x | 75 | 19.1 | 8.9 | 100% |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,842.8 | 1,841.1 | 1,846.6 | 2.2 | 0.581x | 1.889x | 75 | 24.6 | 27.2 | 100% |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,079.6 | 3,036.4 | 3,207.5 | 61.1 | 0.971x | 3.157x | 75 | 41.1 | 40.4 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,172.3 | 3,162.7 | 3,292.8 | 49.6 | 1.000x | 3.252x | 75 | 42.3 | 34.4 | 100% |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 4,060.6 | 4,018.6 | 4,078.4 | 19.9 | 1.280x | 4.162x | 75 | 54.1 | 16.4 | 100% |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,069.0 | 5,055.9 | 5,084.1 | 11.9 | 1.598x | 5.196x | 75 | 67.6 | 58.6 | 100% |
| 8 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 8,805.2 | 8,711.2 | 9,628.5 | 345.8 | 2.776x | 9.026x | 75 | 117.4 | 30.4 | 100% |
| 9 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 44,042.2 | 43,672.6 | 44,380.6 | 257.6 | 13.883x | 45.146x | 75 | 587.2 | 100.0 | 100% |
| 10 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 44,529.2 | 44,338.4 | 44,617.8 | 99.0 | 14.037x | 45.645x | 75 | 593.7 | 100.2 | 100% |
| 11 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 204,644.0 | 204,232.7 | 205,863.3 | 560.9 | 64.509x | 209.774x | 75 | 2,728.6 | 27.9 | 100% |

### `evil-alt-nested` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 27.3 | 0.0000 | 26.6 | 27.9 | 0.5 | 0.001x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 87.7 | 0.0001 | 87.4 | 111.9 | 9.6 | 0.004x | 3.218x |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 169.8 | 0.0001 | 169.7 | 170.1 | 0.1 | 0.008x | 6.230x |
| 4 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 310.1 | 0.0002 | 309.6 | 355.0 | 17.9 | 0.015x | 11.379x |
| 5 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 313.2 | 0.0002 | 310.6 | 364.8 | 20.6 | 0.015x | 11.491x |
| 6 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 1,579.0 | 0.0011 | 1,573.0 | 1,591.3 | 6.2 | 0.074x | 57.929x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,948.7 | 0.0014 | 1,941.2 | 1,963.2 | 7.8 | 0.092x | 71.496x |
| 8 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 17,638.1 | 0.0128 | 17,557.2 | 17,717.4 | 53.7 | 0.829x | 647.112x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 21,266.4 | 0.0155 | 21,161.3 | 21,375.8 | 70.6 | 1.000x | 780.232x |
| 10 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,282,472.4 | 3.1117 | 4,280,424.8 | 4,294,546.0 | 5,070.7 | 201.372x | 157117.113x |
| 11 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,282,488.9 | 3.1117 | 4,278,930.8 | 4,283,985.7 | 2,083.6 | 201.373x | 157117.715x |
| 12 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 4,298,798.6 | 3.1235 | 4,285,934.0 | 5,086,619.6 | 389,881.1 | 202.140x | 157716.094x |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 10,233,238.4 | 7.4356 | 10,204,195.9 | 10,275,745.2 | 23,436.7 | 481.192x | 375441.264x |

#### `evil-alt-nested` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 10.4 | 0.0000 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 27.4 | 0.0000 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.5 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 99.4 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 100.6 | 0.0001 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 501.8 | 0.0005 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 225.0 | 0.0002 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,892.3 | 0.0018 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 2,218.3 | 0.0021 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,253,599.7 | 3.1029 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,254,100.5 | 3.1034 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 3,265,878.0 | 3.1146 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 7,798,637.2 | 7.4374 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 4.8 | 0.0000 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 27.1 | 0.0001 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.6 | 0.0002 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 88.9 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 90.5 | 0.0003 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 118.6 | 0.0005 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 49.0 | 0.0002 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 297.6 | 0.0011 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 133.7 | 0.0005 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 813,713.8 | 3.1041 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 813,507.2 | 3.1033 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 817,267.8 | 3.1176 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 1,951,998.2 | 7.4463 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 12.1 | 0.0002 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 33.2 | 0.0005 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 58.7 | 0.0009 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 122.7 | 0.0019 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 122.9 | 0.0019 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 960.4 | 0.0147 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 1,675.4 | 0.0256 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 15,439.1 | 0.2356 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 18,910.9 | 0.2886 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 215,158.9 | 3.2831 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 214,657.3 | 3.2754 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 216,567.6 | 3.3046 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 488,977.6 | 7.4612 |

### `file-ext-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 46,454.2 | 0.0338 | 46,422.0 | 46,539.6 | 41.2 | 0.038x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 76,758.0 | 0.0558 | 76,711.6 | 76,820.3 | 37.7 | 0.063x | 1.652x |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 84,722.6 | 0.0616 | 84,681.4 | 84,797.9 | 41.3 | 0.069x | 1.824x |
| 4 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 250,174.3 | 0.1818 | 249,698.6 | 250,649.2 | 300.8 | 0.205x | 5.385x |
| 5 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 250,537.7 | 0.1820 | 250,375.8 | 250,683.8 | 129.5 | 0.205x | 5.393x |
| 6 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 292,629.2 | 0.2126 | 292,441.7 | 293,655.2 | 436.3 | 0.239x | 6.299x |
| 7 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 292,750.1 | 0.2127 | 292,628.0 | 293,339.5 | 264.2 | 0.239x | 6.302x |
| 8 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 1,134,876.5 | 0.8246 | 1,133,682.1 | 1,153,975.3 | 7,620.5 | 0.928x | 24.430x |
| 9 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 1,180,777.2 | 0.8580 | 1,180,653.9 | 1,183,211.5 | 986.9 | 0.966x | 25.418x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,222,845.7 | 0.8885 | 1,217,124.1 | 1,225,350.1 | 2,917.4 | 1.000x | 26.324x |
| 11 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 3,856,595.6 | 2.8022 | 3,846,555.6 | 3,863,028.0 | 5,299.1 | 3.154x | 83.019x |
| 12 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 3,857,659.1 | 2.8030 | 3,846,513.9 | 3,865,500.2 | 6,875.3 | 3.155x | 83.042x |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 25,659,286.9 | 18.6443 | 25,645,177.6 | 25,751,021.9 | 38,923.5 | 20.983x | 552.356x |

#### `file-ext-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 35,303.8 | 0.0337 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 58,408.2 | 0.0557 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 64,532.4 | 0.0615 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 196,564.2 | 0.1875 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 196,838.5 | 0.1877 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 228,569.2 | 0.2180 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 228,693.9 | 0.2181 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 864,092.8 | 0.8241 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 897,757.5 | 0.8562 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 933,086.3 | 0.8899 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 2,937,523.4 | 2.8014 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 2,938,338.2 | 2.8022 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 19,542,557.4 | 18.6372 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 8,882.0 | 0.0339 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 14,607.1 | 0.0557 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 16,066.7 | 0.0613 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 42,522.2 | 0.1622 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 42,607.1 | 0.1625 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 52,702.5 | 0.2010 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 52,672.4 | 0.2009 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 216,457.2 | 0.8257 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 226,234.7 | 0.8630 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 232,123.8 | 0.8855 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 734,576.5 | 2.8022 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 734,500.1 | 2.8019 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 4,894,560.0 | 18.6713 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 2,282.4 | 0.0348 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 3,716.4 | 0.0567 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 4,107.3 | 0.0627 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 11,069.3 | 0.1689 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 10,930.1 | 0.1668 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 11,406.7 | 0.1741 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 11,377.2 | 0.1736 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 54,368.5 | 0.8296 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 56,901.5 | 0.8682 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 57,624.7 | 0.8793 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 183,451.0 | 2.7992 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 183,652.8 | 2.8023 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,227,590.2 | 18.7315 |

### `file-ext-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 828.8 | 816.1 | 842.6 | 8.8 | 0.203x | 1.000x | 75 | 11.1 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 852.6 | 828.1 | 865.1 | 12.7 | 0.209x | 1.029x | 75 | 11.4 | 8.9 | 100% |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,424.6 | 1,419.0 | 1,430.2 | 3.6 | 0.350x | 1.719x | 75 | 19.0 | 16.4 | 100% |
| 4 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,477.7 | 2,474.8 | 2,484.5 | 3.3 | 0.608x | 2.990x | 75 | 33.0 | 27.2 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,807.2 | 2,778.4 | 2,976.4 | 89.5 | 0.689x | 3.387x | 75 | 37.4 | 40.4 | 100% |
| 6 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,197.6 | 3,179.9 | 3,198.9 | 7.9 | 0.785x | 3.858x | 75 | 42.6 | 58.6 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,075.2 | 4,067.7 | 4,444.4 | 145.3 | 1.000x | 4.917x | 75 | 54.3 | 34.4 | 100% |
| 8 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,587.9 | 4,456.0 | 4,748.8 | 126.3 | 1.126x | 5.536x | 75 | 61.2 | 17.3 | 100% |
| 9 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,878.3 | 4,417.8 | 4,897.5 | 185.8 | 1.197x | 5.886x | 75 | 65.0 | 18.0 | 100% |
| 10 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,642.3 | 7,629.0 | 7,652.1 | 8.1 | 1.875x | 9.221x | 75 | 101.9 | 100.0 | 100% |

### `float-literal-bound` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,788,992.7 | 1.2999 | 1,786,072.2 | 1,795,353.9 | 3,353.0 | 0.118x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,789,282.2 | 1.3001 | 1,786,131.1 | 1,792,242.8 | 2,292.3 | 0.118x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,128,191.0 | 1.5464 | 2,118,594.6 | 2,136,797.6 | 5,913.3 | 0.140x | 1.190x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 13,300,527.7 | 9.6643 | 13,268,289.0 | 13,388,146.2 | 42,996.0 | 0.878x | 7.435x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 15,150,346.6 | 11.0084 | 15,124,920.9 | 15,187,452.8 | 24,785.4 | 1.000x | 8.469x |
| 6 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 18,611,391.9 | 13.5232 | 18,590,070.5 | 18,739,437.3 | 54,460.5 | 1.228x | 10.403x |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 18,864,339.9 | 13.7070 | 18,835,808.1 | 19,015,341.6 | 64,474.6 | 1.245x | 10.545x |
| 8 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 19,095,162.5 | 13.8747 | 18,977,754.6 | 19,122,895.4 | 53,001.7 | 1.260x | 10.674x |

#### `float-literal-bound` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,370,765.3 | 1.3073 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 1,367,310.1 | 1.3040 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 1,610,952.2 | 1.5363 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 10,194,825.3 | 9.7225 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 11,628,427.6 | 11.0897 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 14,263,633.7 | 13.6029 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 14,385,331.1 | 13.7189 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 14,564,744.1 | 13.8900 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 336,902.8 | 1.2852 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 337,235.0 | 1.2864 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 415,597.8 | 1.5854 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 2,505,563.0 | 9.5580 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 2,845,806.2 | 10.8559 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 3,504,517.4 | 13.3687 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 3,587,528.1 | 13.6853 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,622,356.9 | 13.8182 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 82,360.5 | 1.2567 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 82,819.5 | 1.2637 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 100,743.8 | 1.5372 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 604,153.4 | 9.2187 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 677,376.7 | 10.3359 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 839,490.2 | 12.8096 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 897,156.5 | 13.6895 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 906,380.8 | 13.8303 |

### `float-literal-bound` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 2,483.2 | 2,481.1 | 2,491.5 | 4.2 | 0.452x | 1.000x | 75 | 33.1 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 2,487.3 | 2,484.5 | 2,489.8 | 1.8 | 0.453x | 1.002x | 75 | 33.2 | 8.9 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,482.3 | 3,390.8 | 3,561.0 | 62.3 | 0.634x | 1.402x | 75 | 46.4 | 40.4 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 5,490.3 | 5,449.0 | 5,499.0 | 18.0 | 1.000x | 2.211x | 75 | 73.2 | 34.4 | 100% |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 5,858.8 | 5,825.5 | 6,555.7 | 284.1 | 1.067x | 2.359x | 75 | 78.1 | 30.4 | 100% |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 19,831.4 | 19,811.8 | 19,839.5 | 9.6 | 3.612x | 7.986x | 75 | 264.4 | 18.0 | 100% |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 20,085.3 | 20,060.8 | 20,143.0 | 30.3 | 3.658x | 8.088x | 75 | 267.8 | 17.3 | 100% |
| 8 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 20,462.7 | 20,445.9 | 20,744.0 | 111.6 | 3.727x | 8.240x | 75 | 272.8 | 58.6 | 100% |

### `floor-byte` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 23,114.5 | 0.0168 | 23,085.0 | 23,201.3 | 39.6 | 0.994x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 23,139.1 | 0.0168 | 23,107.5 | 24,561.3 | 574.4 | 0.996x | 1.001x |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 23,231.6 | 0.0169 | 23,207.7 | 23,329.0 | 44.5 | 0.999x | 1.005x |
| 4 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 23,242.8 | 0.0169 | 23,224.7 | 23,278.7 | 20.8 | 1.000x | 1.006x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 23,243.4 | 0.0169 | 23,228.8 | 25,906.0 | 1,066.4 | 1.000x | 1.006x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 23,422.6 | 0.0170 | 23,398.3 | 23,521.2 | 44.9 | 1.008x | 1.013x |
| 7 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 23,754.4 | 0.0173 | 23,746.0 | 23,848.9 | 44.5 | 1.022x | 1.028x |
| 8 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 23,801.6 | 0.0173 | 23,778.5 | 23,892.2 | 39.9 | 1.024x | 1.030x |
| 9 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 32,371.4 | 0.0235 | 32,354.8 | 32,533.6 | 66.0 | 1.393x | 1.400x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 51,954.9 | 0.0378 | 51,548.6 | 52,169.7 | 212.0 | 2.235x | 2.248x |
| 11 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 814,407.5 | 0.5918 | 814,147.2 | 814,643.8 | 180.6 | 35.038x | 35.234x |
| 12 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 815,256.0 | 0.5924 | 814,580.0 | 824,632.4 | 3,826.7 | 35.075x | 35.270x |
| 13 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,228,556.4 | 1.6193 | 2,227,650.2 | 6,262,574.3 | 1,613,659.5 | 95.879x | 96.414x |

#### `floor-byte` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 17,611.4 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 17,625.0 | 0.0168 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 17,673.0 | 0.0169 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 17,696.6 | 0.0169 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,693.4 | 0.0169 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 17,817.3 | 0.0170 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 17,809.6 | 0.0170 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 17,839.7 | 0.0170 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 24,549.8 | 0.0234 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,663.5 | 0.0378 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 620,270.3 | 0.5915 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 620,902.2 | 0.5921 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,697,229.0 | 1.6186 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 4,387.1 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 4,395.1 | 0.0168 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 4,410.8 | 0.0168 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 4,419.9 | 0.0169 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 4,409.5 | 0.0168 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 4,459.0 | 0.0170 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 4,508.8 | 0.0172 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 4,508.8 | 0.0172 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 6,143.1 | 0.0234 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 9,794.2 | 0.0374 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 155,080.4 | 0.5916 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 155,292.2 | 0.5924 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 424,555.6 | 1.6196 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 1,107.8 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,108.5 | 0.0169 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,143.7 | 0.0175 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,143.7 | 0.0175 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 1,138.2 | 0.0174 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 1,135.2 | 0.0173 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 1,441.9 | 0.0220 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 1,458.3 | 0.0223 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,673.2 | 0.0255 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 2,508.6 | 0.0383 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 39,006.7 | 0.5952 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 39,036.0 | 0.5956 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,356.4 | 1.6229 |

### `floor-byte` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 665.2 | 661.8 | 668.9 | 2.3 | 0.258x | 1.000x | 75 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 667.2 | 663.1 | 671.8 | 2.8 | 0.258x | 1.003x | 75 | 8.9 | 100% |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,228.2 | 1,226.7 | 1,230.0 | 1.1 | 0.476x | 1.846x | 75 | 16.4 | 100% |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 1,297.3 | 1,295.0 | 1,300.1 | 1.8 | 0.502x | 1.950x | 75 | 17.3 | 100% |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 1,353.4 | 1,353.0 | 1,357.3 | 1.7 | 0.524x | 2.035x | 75 | 18.0 | 100% |
| 6 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,040.9 | 2,039.2 | 2,042.2 | 1.0 | 0.790x | 3.068x | 75 | 27.2 | 100% |
| 7 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 2,093.3 | 2,089.0 | 2,157.5 | 26.5 | 0.811x | 3.147x | 75 | 27.9 | 100% |
| 8 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 2,277.3 | 2,271.3 | 2,472.5 | 80.6 | 0.882x | 3.424x | 75 | 30.4 | 100% |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,582.7 | 2,581.7 | 2,612.8 | 14.6 | 1.000x | 3.883x | 75 | 34.4 | 100% |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,031.9 | 2,822.9 | 3,197.0 | 143.2 | 1.174x | 4.558x | 75 | 40.4 | 100% |
| 11 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,397.0 | 4,389.9 | 4,412.5 | 9.0 | 1.703x | 6.610x | 75 | 58.6 | 100% |
| 12 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,498.7 | 7,496.4 | 7,543.6 | 18.5 | 2.903x | 11.273x | 75 | 100.0 | 100% |
| 13 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 7,512.5 | 7,503.6 | 7,522.3 | 6.9 | 2.909x | 11.294x | 75 | 100.2 | 100% |

### `high-byte-run` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 64,041.8 | 0.0465 | 63,989.0 | 64,175.5 | 76.5 | 0.063x | 1.000x | 3 | 100% |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 407,488.7 | 0.2961 | 407,448.7 | 408,044.4 | 224.4 | 0.400x | 6.363x | 3 | 100% |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 482,987.9 | 0.3509 | 482,583.5 | 484,623.4 | 839.3 | 0.475x | 7.542x | 3 | 100% |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 483,135.5 | 0.3511 | 482,715.7 | 483,727.8 | 409.3 | 0.475x | 7.544x | 3 | 100% |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 1,012,634.2 | 0.7358 | 1,010,832.0 | 1,015,461.7 | 1,698.9 | 0.995x | 15.812x | 3 | 100% |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,017,809.1 | 0.7395 | 1,015,898.4 | 1,019,696.4 | 1,273.6 | 1.000x | 15.893x | 3 | 100% |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,035,195.9 | 1.4788 | 2,034,726.2 | 2,041,089.2 | 2,382.7 | 2.000x | 31.779x | 3 | 100% |
| 8 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 2,035,318.6 | 1.4789 | 2,034,582.3 | 2,040,453.8 | 2,460.0 | 2.000x | 31.781x | 3 | 100% |
| 9 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 2,035,715.7 | 1.4792 | 2,034,458.8 | 2,037,253.4 | 1,027.2 | 2.000x | 31.787x | 3 | 100% |
| 10 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,237,046.8 | 1.6255 | 2,231,987.1 | 2,241,666.4 | 3,740.3 | 2.198x | 34.931x | 3 | 100% |
| 11 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 2,243,737.3 | 1.6303 | 2,242,372.1 | 2,562,583.7 | 127,765.6 | 2.204x | 35.036x | 3 | 100% |
| 12 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,444,100.7 | 1.7759 | 2,443,685.1 | 2,478,787.6 | 13,643.9 | 2.401x | 38.164x | 3 | 100% |

#### `high-byte-run` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 48,674.5 | 0.0464 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 310,296.3 | 0.2959 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 368,079.9 | 0.3510 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 368,024.7 | 0.3510 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 777,399.7 | 0.7414 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 776,432.5 | 0.7405 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,550,179.3 | 1.4784 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 1,550,113.6 | 1.4783 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 1,550,236.8 | 1.4784 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,697,697.6 | 1.6191 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 1,703,107.9 | 1.6242 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,861,517.3 | 1.7753 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 12,217.2 | 0.0466 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 77,676.8 | 0.2963 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 91,636.1 | 0.3496 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 92,062.9 | 0.3512 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 191,525.2 | 0.7306 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 193,387.6 | 0.7377 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 387,601.1 | 1.4786 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 387,763.2 | 1.4792 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 387,743.7 | 1.4791 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 423,942.2 | 1.6172 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 424,570.0 | 1.6196 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 465,521.4 | 1.7758 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 3,144.3 | 0.0480 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 19,590.5 | 0.2989 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 23,027.5 | 0.3514 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 23,058.1 | 0.3518 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 46,071.8 | 0.7030 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 47,518.4 | 0.7251 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 97,429.9 | 1.4867 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 97,403.9 | 1.4863 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 97,421.9 | 1.4865 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 116,393.1 | 1.7760 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 116,000.8 | 1.7700 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 117,203.3 | 1.7884 |

### `high-byte-run` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,105.3 | 1,103.1 | 1,109.1 | 2.1 | 0.313x | 1.000x | 75 | 14.7 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,119.7 | 1,118.5 | 1,121.8 | 1.2 | 0.317x | 1.013x | 75 | 14.9 | 8.9 | 100% |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,643.3 | 2,634.7 | 2,647.0 | 4.7 | 0.749x | 2.391x | 75 | 35.2 | 27.2 | 100% |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 2,776.3 | 2,772.2 | 3,858.4 | 432.9 | 0.787x | 2.512x | 75 | 37.0 | 17.3 | 100% |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 2,868.0 | 2,862.1 | 2,877.0 | 4.9 | 0.813x | 2.595x | 75 | 38.2 | 18.0 | 100% |
| 6 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 3,272.4 | 3,262.6 | 4,071.7 | 319.8 | 0.927x | 2.961x | 75 | 43.6 | 30.4 | 100% |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,364.8 | 3,344.3 | 3,413.9 | 24.1 | 0.953x | 3.044x | 75 | 44.9 | 40.4 | 100% |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,529.1 | 3,494.0 | 3,552.3 | 22.2 | 1.000x | 3.193x | 75 | 47.1 | 34.4 | 100% |
| 9 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,195.5 | 5,189.3 | 5,210.9 | 7.9 | 1.472x | 4.700x | 75 | 69.3 | 58.6 | 100% |
| 10 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,683.7 | 9,646.3 | 9,746.8 | 33.6 | 2.744x | 8.761x | 75 | 129.1 | 100.0 | 100% |
| 11 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 9,730.8 | 9,702.7 | 9,856.5 | 65.5 | 2.757x | 8.804x | 75 | 129.7 | 100.2 | 100% |

### `ipv4-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 18.1 | 0.0000 | 17.9 | 18.6 | 0.2 | 0.196x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.7 | 0.0000 | 18.7 | 18.9 | 0.1 | 0.203x | 1.033x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.7 | 0.0000 | 18.7 | 18.8 | 0.0 | 0.203x | 1.034x |
| 4 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 30.5 | 0.0000 | 30.3 | 32.3 | 0.7 | 0.330x | 1.681x |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 81.7 | 0.0001 | 81.3 | 120.6 | 15.2 | 0.885x | 4.508x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 92.4 | 0.0001 | 92.3 | 92.5 | 0.0 | 1.000x | 5.097x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 144.0 | 0.0001 | 142.0 | 150.7 | 3.0 | 1.559x | 7.943x |
| 8 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 286.8 | 0.0002 | 285.2 | 291.9 | 2.8 | 3.105x | 15.825x |
| 9 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 287.3 | 0.0002 | 286.4 | 291.3 | 2.1 | 3.110x | 15.851x |
| 10 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 367.4 | 0.0003 | 361.0 | 380.9 | 7.2 | 3.977x | 20.268x |
| 11 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,068,387.1 | 2.9561 | 4,065,125.1 | 4,082,953.0 | 6,349.1 | 44038.947x | 224448.525x |
| 12 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,071,939.4 | 2.9587 | 4,065,353.7 | 4,093,932.5 | 10,627.1 | 44077.400x | 224644.506x |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 15,414,828.9 | 11.2006 | 15,367,175.8 | 16,262,951.8 | 345,482.0 | 166860.434x | 850419.481x |

#### `ipv4-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 6.0 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 6.2 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 6.3 | 0.0000 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.1 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 27.5 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 30.7 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 44.4 | 0.0000 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 88.2 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 90.1 | 0.0001 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 302.7 | 0.0003 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,096,500.9 | 2.9531 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,097,300.5 | 2.9538 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 11,695,006.9 | 11.1532 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 6.2 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 6.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 6.3 | 0.0000 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.1 | 0.0000 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 27.2 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 30.8 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 48.4 | 0.0002 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 88.8 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 89.8 | 0.0003 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 32.5 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 774,779.1 | 2.9555 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 775,882.5 | 2.9598 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 2,969,110.2 | 11.3263 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 6.0 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 6.2 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 6.2 | 0.0001 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.2 | 0.0002 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 27.1 | 0.0004 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 30.8 | 0.0005 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 52.1 | 0.0008 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 108.9 | 0.0017 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 108.5 | 0.0017 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 32.4 | 0.0005 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 194,432.8 | 2.9668 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 195,416.1 | 2.9818 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 749,468.9 | 11.4360 |

### `ipv4-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 493.0 | 491.9 | 494.9 | 1.1 | 0.166x | 1.000x | 75 | 6.6 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 494.1 | 492.4 | 495.5 | 1.1 | 0.167x | 1.002x | 75 | 6.6 | 8.9 | 100% |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 951.0 | 950.1 | 953.9 | 1.3 | 0.321x | 1.929x | 75 | 12.7 | 27.2 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,435.3 | 1,433.0 | 1,993.4 | 223.3 | 0.484x | 2.911x | 75 | 19.1 | 16.4 | 100% |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 2,742.5 | 2,724.2 | 2,784.6 | 22.0 | 0.925x | 5.562x | 75 | 36.6 | 30.4 | 100% |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,964.6 | 2,940.5 | 2,993.8 | 18.0 | 1.000x | 6.013x | 75 | 39.5 | 34.4 | 100% |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,016.1 | 2,910.2 | 3,308.9 | 140.4 | 1.017x | 6.117x | 75 | 40.2 | 40.4 | 100% |
| 8 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,410.3 | 3,397.7 | 3,444.8 | 16.5 | 1.150x | 6.917x | 75 | 45.5 | 58.6 | 100% |
| 9 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 6,320.6 | 6,312.0 | 6,367.8 | 23.6 | 2.132x | 12.819x | 75 | 84.3 | 18.0 | 100% |
| 10 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 6,419.1 | 6,397.3 | 6,430.9 | 11.3 | 2.165x | 13.019x | 75 | 85.6 | 17.3 | 100% |
| 11 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 6,818.3 | 6,807.5 | 6,837.2 | 11.3 | 2.300x | 13.829x | 75 | 90.9 | 100.0 | 100% |
| 12 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 6,848.5 | 6,837.0 | 6,896.7 | 21.9 | 2.310x | 13.890x | 75 | 91.3 | 100.2 | 100% |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 30,706.0 | 30,327.9 | 30,878.0 | 228.1 | 10.358x | 62.278x | 75 | 409.4 | 27.9 | 100% |

### `keyword-prefix-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 291.4 | 0.0002 | 291.1 | 292.3 | 0.4 | 0.000x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 366,013.7 | 0.2659 | 364,991.4 | 366,809.1 | 648.4 | 0.110x | 1255.923x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 511,780.6 | 0.3719 | 502,082.3 | 518,020.7 | 5,713.5 | 0.154x | 1756.101x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 731,067.1 | 0.5312 | 730,362.0 | 733,708.2 | 1,149.1 | 0.220x | 2508.551x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 731,216.0 | 0.5313 | 730,749.8 | 731,530.0 | 273.5 | 0.220x | 2509.062x |
| 6 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,435,148.9 | 1.7694 | 2,428,039.7 | 2,489,567.4 | 25,033.8 | 0.734x | 8355.860x |
| 7 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 2,487,038.7 | 1.8071 | 2,475,028.9 | 2,506,509.1 | 10,714.5 | 0.750x | 8533.913x |
| 8 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 3,143,025.6 | 2.2838 | 3,135,065.3 | 3,164,269.1 | 11,602.0 | 0.948x | 10784.836x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,316,797.1 | 2.4100 | 3,295,097.3 | 3,389,636.2 | 33,969.5 | 1.000x | 11381.108x |
| 10 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,965,092.1 | 2.8811 | 3,957,525.3 | 3,989,063.6 | 11,202.9 | 1.195x | 13605.638x |
| 11 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,191,743.7 | 3.0458 | 4,164,474.5 | 4,203,327.0 | 14,393.4 | 1.264x | 14383.361x |
| 12 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,194,476.7 | 3.0477 | 4,177,146.3 | 4,199,943.3 | 7,790.9 | 1.265x | 14392.738x |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 29,472,540.3 | 21.4150 | 29,439,365.8 | 29,561,204.2 | 47,868.4 | 8.886x | 101130.747x |

#### `keyword-prefix-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 85.9 | 0.0001 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 280,266.4 | 0.2673 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 391,236.3 | 0.3731 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 564,384.1 | 0.5382 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 564,542.7 | 0.5384 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,858,714.8 | 1.7726 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 1,899,496.7 | 1.8115 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 2,397,249.4 | 2.2862 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 2,520,617.0 | 2.4038 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 3,023,162.4 | 2.8831 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,191,936.5 | 3.0441 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,192,846.8 | 3.0449 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 22,432,575.7 | 21.3934 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 123.7 | 0.0005 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 69,143.3 | 0.2638 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 96,555.6 | 0.3683 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 135,383.8 | 0.5164 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 135,156.0 | 0.5156 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 456,628.9 | 1.7419 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 465,675.9 | 1.7764 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 602,096.1 | 2.2968 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 633,885.2 | 2.4181 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 755,525.0 | 2.8821 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 796,914.2 | 3.0400 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 800,588.7 | 3.0540 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 5,618,181.4 | 21.4317 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 81.8 | 0.0012 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 16,727.8 | 0.2552 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 23,746.1 | 0.3623 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 31,234.8 | 0.4766 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 31,377.8 | 0.4788 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 119,284.3 | 1.8201 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 121,067.9 | 1.8473 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 151,118.0 | 2.3059 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 158,274.1 | 2.4151 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 185,727.1 | 2.8340 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 200,359.0 | 3.0572 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 200,910.6 | 3.0657 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,411,843.2 | 21.5430 |

### `keyword-prefix-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 774.2 | 772.1 | 779.5 | 2.6 | 0.193x | 1.000x | 75 | 10.3 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 774.6 | 770.5 | 779.1 | 2.8 | 0.193x | 1.001x | 75 | 10.3 | 8.9 | 100% |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,619.6 | 1,615.9 | 1,623.8 | 2.5 | 0.403x | 2.092x | 75 | 21.6 | 16.4 | 100% |
| 4 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,667.3 | 2,666.2 | 2,670.5 | 1.5 | 0.665x | 3.445x | 75 | 35.6 | 27.2 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,873.5 | 2,816.5 | 3,149.4 | 118.3 | 0.716x | 3.712x | 75 | 38.3 | 40.4 | 100% |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,014.0 | 3,958.3 | 4,104.4 | 57.3 | 1.000x | 5.185x | 75 | 53.5 | 34.4 | 100% |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,042.2 | 4,036.1 | 4,063.9 | 9.9 | 1.007x | 5.221x | 75 | 53.9 | 58.6 | 100% |
| 8 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,667.5 | 4,631.4 | 4,739.5 | 41.4 | 1.163x | 6.029x | 75 | 62.2 | 18.0 | 100% |
| 9 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,752.7 | 4,710.3 | 4,770.3 | 21.6 | 1.184x | 6.139x | 75 | 63.4 | 17.3 | 100% |
| 10 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,951.8 | 7,924.2 | 8,062.4 | 50.4 | 1.981x | 10.271x | 75 | 106.0 | 100.0 | 100% |

### `logparse-atomic` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 30.2 | 0.0000 | 30.0 | 30.2 | 0.1 | 0.115x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 31.4 | 0.0000 | 30.0 | 33.1 | 1.2 | 0.120x | 1.040x |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 97.7 | 0.0001 | 97.3 | 104.2 | 2.7 | 0.374x | 3.238x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 128.9 | 0.0001 | 125.3 | 136.9 | 3.9 | 0.493x | 4.274x |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 245.3 | 0.0002 | 243.6 | 246.1 | 0.9 | 0.938x | 8.133x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 261.4 | 0.0002 | 258.6 | 262.3 | 1.4 | 1.000x | 8.666x |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 2,847,288.6 | 2.0689 | 2,844,819.6 | 3,652,530.8 | 322,406.5 | 10891.677x | 94386.002x |
| 8 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 2,932,595.0 | 2.1308 | 2,847,142.5 | 3,649,363.7 | 376,697.2 | 11217.998x | 97213.861x |

#### `logparse-atomic` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 9.8 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 9.9 | 0.0000 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 32.6 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 42.9 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 26.9 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 31.4 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 2,167,499.5 | 2.0671 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 2,174,263.6 | 2.0735 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 9.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 11.0 | 0.0000 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 32.4 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 43.1 | 0.0002 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 27.0 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 31.4 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 542,422.8 | 2.0692 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 587,658.3 | 2.2417 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 10.4 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 10.4 | 0.0002 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 32.7 | 0.0005 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 42.5 | 0.0006 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 191.4 | 0.0029 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 198.7 | 0.0030 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 136,093.2 | 2.0766 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 149,905.3 | 2.2874 |

### `logparse-atomic` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 837.3 | 836.3 | 844.9 | 3.9 | 0.169x | 1.000x | 75 | 11.2 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 844.3 | 843.1 | 859.0 | 6.0 | 0.170x | 1.008x | 75 | 11.3 | 8.9 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,219.1 | 3,189.0 | 3,720.7 | 199.1 | 0.649x | 3.845x | 75 | 42.9 | 40.4 | 100% |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,112.5 | 4,108.9 | 4,765.0 | 261.1 | 0.829x | 4.912x | 75 | 54.8 | 18.0 | 100% |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,120.6 | 4,119.1 | 4,137.9 | 7.3 | 0.831x | 4.921x | 75 | 54.9 | 17.3 | 100% |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,959.0 | 4,930.1 | 4,986.6 | 19.2 | 1.000x | 5.923x | 75 | 66.1 | 34.4 | 100% |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,029.4 | 4,984.7 | 5,092.2 | 38.0 | 1.014x | 6.007x | 75 | 67.1 | 58.6 | 100% |
| 8 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 5,239.9 | 5,211.4 | 5,701.0 | 189.0 | 1.057x | 6.258x | 75 | 69.9 | 30.4 | 100% |

### `logparse-atomic-removed` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.7 | 0.0000 | 18.7 | 18.8 | 0.0 | 0.075x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 30.3 | 0.0000 | 30.3 | 30.9 | 0.2 | 0.121x | 1.618x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 86.5 | 0.0001 | 84.4 | 89.9 | 1.9 | 0.345x | 4.616x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 97.4 | 0.0001 | 97.1 | 104.2 | 2.7 | 0.388x | 5.200x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 128.9 | 0.0001 | 126.0 | 144.5 | 7.2 | 0.514x | 6.882x |
| 6 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 135.0 | 0.0001 | 134.7 | 136.0 | 0.5 | 0.538x | 7.202x |
| 7 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 194.1 | 0.0001 | 191.9 | 218.3 | 9.9 | 0.773x | 10.360x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 251.0 | 0.0002 | 250.2 | 256.7 | 2.4 | 1.000x | 13.397x |
| 9 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 287.0 | 0.0002 | 286.5 | 314.5 | 11.0 | 1.143x | 15.314x |
| 10 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 287.8 | 0.0002 | 285.9 | 291.5 | 2.1 | 1.146x | 15.357x |
| 11 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 3,658,937.1 | 2.6586 | 3,658,462.1 | 3,667,505.7 | 3,474.7 | 14575.011x | 195264.034x |
| 12 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 3,662,560.4 | 2.6612 | 3,659,892.5 | 3,682,800.9 | 8,584.6 | 14589.444x | 195457.394x |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 19,219,633.4 | 13.9652 | 19,129,025.2 | 19,928,501.2 | 333,094.2 | 76559.492x | 1025681.233x |

#### `logparse-atomic-removed` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 5.9 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 9.8 | 0.0000 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 26.4 | 0.0000 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 32.5 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 42.9 | 0.0000 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 44.5 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 27.2 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 31.3 | 0.0000 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 87.7 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 88.3 | 0.0001 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 2,786,684.4 | 2.6576 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 2,787,623.6 | 2.6585 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 14,649,327.5 | 13.9707 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 5.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 9.8 | 0.0000 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 28.9 | 0.0001 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 32.4 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 43.1 | 0.0002 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 44.6 | 0.0002 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 27.2 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 31.3 | 0.0001 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 89.5 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 88.8 | 0.0003 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 697,355.7 | 2.6602 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 697,024.7 | 2.6589 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 3,656,527.9 | 13.9485 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 6.8 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 10.7 | 0.0002 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 31.2 | 0.0005 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 32.6 | 0.0005 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 43.0 | 0.0007 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 45.7 | 0.0007 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 139.8 | 0.0021 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 188.4 | 0.0029 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 110.7 | 0.0017 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 112.1 | 0.0017 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 174,915.4 | 2.6690 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 175,369.5 | 2.6759 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 916,344.5 | 13.9823 |

### `logparse-atomic-removed` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 492.7 | 492.2 | 495.0 | 1.0 | 0.102x | 1.000x | 75 | 6.6 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 811.4 | 809.3 | 815.5 | 2.4 | 0.168x | 1.647x | 75 | 10.8 | 8.9 | 100% |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,150.4 | 1,145.8 | 1,164.6 | 6.4 | 0.238x | 2.335x | 75 | 15.3 | 27.2 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,562.5 | 1,551.7 | 1,568.0 | 5.3 | 0.323x | 3.171x | 75 | 20.8 | 16.4 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,218.8 | 3,116.9 | 3,272.9 | 53.0 | 0.666x | 6.533x | 75 | 42.9 | 40.4 | 100% |
| 6 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 4,582.1 | 4,533.2 | 5,174.9 | 245.7 | 0.948x | 9.300x | 75 | 61.1 | 30.4 | 100% |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,796.1 | 4,793.2 | 4,798.8 | 1.9 | 0.992x | 9.734x | 75 | 63.9 | 17.3 | 100% |
| 8 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,811.7 | 4,802.3 | 4,821.2 | 6.4 | 0.995x | 9.766x | 75 | 64.2 | 18.0 | 100% |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,833.8 | 4,814.9 | 4,875.8 | 20.5 | 1.000x | 9.811x | 75 | 64.5 | 34.4 | 100% |
| 10 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,983.4 | 4,969.5 | 5,066.7 | 36.0 | 1.031x | 10.114x | 75 | 66.4 | 58.6 | 100% |
| 11 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,889.9 | 7,859.6 | 8,447.0 | 224.8 | 1.632x | 16.014x | 75 | 105.2 | 100.0 | 100% |
| 12 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 8,028.0 | 7,948.6 | 8,153.9 | 73.3 | 1.661x | 16.294x | 75 | 107.0 | 100.2 | 100% |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 41,466.3 | 41,188.4 | 41,615.7 | 141.0 | 8.578x | 84.161x | 75 | 552.9 | 27.9 | 100% |

### `mojibake-curly-quote` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 23,119.1 | 0.0168 | 23,110.2 | 23,189.2 | 32.9 | 0.995x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 23,138.5 | 0.0168 | 23,133.7 | 23,258.4 | 48.3 | 0.996x | 1.001x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 23,237.7 | 0.0169 | 23,225.5 | 23,329.3 | 38.2 | 1.000x | 1.005x |
| 4 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 23,264.9 | 0.0169 | 23,240.8 | 23,268.0 | 11.8 | 1.001x | 1.006x |
| 5 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 23,764.4 | 0.0173 | 23,749.0 | 23,788.5 | 13.7 | 1.023x | 1.028x |
| 6 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 23,781.0 | 0.0173 | 23,730.3 | 23,982.8 | 88.2 | 1.023x | 1.029x |
| 7 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 31,604.1 | 0.0230 | 31,599.9 | 31,640.3 | 16.0 | 1.360x | 1.367x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 40,046.1 | 0.0291 | 40,002.1 | 40,176.4 | 65.6 | 1.723x | 1.732x |
| 9 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 814,022.9 | 0.5915 | 813,706.7 | 818,592.2 | 1,830.4 | 35.030x | 35.210x |
| 10 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 814,193.4 | 0.5916 | 813,993.5 | 814,559.1 | 195.3 | 35.038x | 35.217x |
| 11 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,228,965.5 | 1.6196 | 2,228,367.8 | 2,229,892.6 | 527.0 | 95.920x | 96.412x |
| 12 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 21,720,481.9 | 15.7823 | 20,799,474.3 | 22,717,032.7 | 606,971.7 | 934.710x | 939.503x |

#### `mojibake-curly-quote` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 17,620.4 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 17,641.9 | 0.0168 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,689.4 | 0.0169 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 17,706.7 | 0.0169 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 17,797.8 | 0.0170 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 17,832.4 | 0.0170 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 24,118.2 | 0.0230 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 30,515.2 | 0.0291 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 619,942.0 | 0.5912 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 620,266.1 | 0.5915 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,697,595.4 | 1.6190 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 16,468,005.4 | 15.7051 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 4,389.4 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 4,388.0 | 0.0167 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 4,413.8 | 0.0168 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 4,420.6 | 0.0169 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 4,515.3 | 0.0172 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 4,500.1 | 0.0172 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 5,968.0 | 0.0228 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 7,596.8 | 0.0290 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 155,104.2 | 0.5917 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 155,010.7 | 0.5913 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 424,823.1 | 1.6206 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 4,126,468.7 | 15.7412 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,106.0 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 1,109.3 | 0.0169 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 1,133.7 | 0.0173 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,139.7 | 0.0174 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 1,452.2 | 0.0222 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 1,447.3 | 0.0221 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,529.5 | 0.0233 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 1,968.0 | 0.0300 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 38,976.6 | 0.5947 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 38,919.3 | 0.5939 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,805.5 | 1.6297 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,109,084.1 | 16.9233 |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (pattern is not valid UTF-8 at byte 0: invalid utf-8 sequence of 1 bytes from index 0)

### `mojibake-curly-quote` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 682.6 | 681.9 | 686.1 | 1.8 | 0.242x | 1.000x | 75 | 9.1 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 683.2 | 680.6 | 691.3 | 4.5 | 0.242x | 1.001x | 75 | 9.1 | 8.9 | 100% |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 1,515.9 | 1,513.7 | 1,524.6 | 3.9 | 0.537x | 2.221x | 75 | 20.2 | 17.3 | 100% |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 1,523.2 | 1,520.7 | 1,525.5 | 1.7 | 0.539x | 2.231x | 75 | 20.3 | 18.0 | 100% |
| 5 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,044.8 | 2,036.8 | 2,052.4 | 5.6 | 0.724x | 2.995x | 75 | 27.3 | 27.2 | 100% |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,824.7 | 2,603.4 | 2,868.0 | 97.6 | 1.000x | 4.138x | 75 | 37.7 | 34.4 | 100% |
| 7 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 2,857.5 | 2,392.8 | 3,311.4 | 408.0 | 1.012x | 4.186x | 75 | 38.1 | 30.4 | 100% |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,954.5 | 2,886.8 | 3,110.9 | 96.1 | 1.046x | 4.328x | 75 | 39.4 | 40.4 | 100% |
| 9 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,421.8 | 4,415.6 | 4,517.8 | 39.0 | 1.565x | 6.478x | 75 | 59.0 | 58.6 | 100% |
| 10 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 7,528.6 | 7,518.6 | 7,541.8 | 7.6 | 2.665x | 11.029x | 75 | 100.4 | 100.2 | 100% |
| 11 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,560.5 | 7,534.7 | 7,618.2 | 30.3 | 2.677x | 11.076x | 75 | 100.8 | 100.0 | 100% |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (pattern is not valid UTF-8 at byte 0: invalid utf-8 sequence of 1 bytes from index 0)

### `negation-scope-lookbehind-var` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 51,588.5 | 0.0375 | 51,453.5 | 51,633.3 | 65.0 | 0.001x | 1.000x | 3 | 100% |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 48,746,190.7 | 35.4194 | 48,512,426.3 | 49,830,534.8 | 466,084.7 | 1.000x | 944.904x | 3 | 100% |

#### `negation-scope-lookbehind-var` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,262.0 | 0.0374 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 37,150,551.2 | 35.4295 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 9,822.3 | 0.0375 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 9,203,447.3 | 35.1084 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 2,516.1 | 0.0384 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 2,400,179.0 | 36.6238 |

### `negation-scope-lookbehind-var` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,119.1 | 2,903.3 | 3,338.9 | 168.9 | 0.340x | 1.000x | 75 | 41.6 | 40.4 | 100% |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 9,184.3 | 9,118.4 | 9,435.0 | 111.2 | 1.000x | 2.944x | 75 | 122.5 | 34.4 | 100% |

### `nested-comment-rec` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 52,006.5 | 0.0378 | 51,639.2 | 52,337.3 | 269.0 | 0.019x | 1.000x |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 1,498,679.7 | 1.0890 | 1,498,478.1 | 1,499,819.6 | 503.0 | 0.558x | 28.817x |
| 3 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 2,105,602.6 | 1.5299 | 2,087,963.4 | 2,133,077.5 | 18,485.1 | 0.784x | 40.487x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,685,331.9 | 1.9512 | 2,684,786.5 | 2,685,986.6 | 418.9 | 1.000x | 51.635x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 7,790,233.0 | 5.6605 | 7,786,402.6 | 7,822,400.5 | 13,149.8 | 2.901x | 149.793x |
| 6 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 7,807,119.1 | 5.6727 | 7,796,354.7 | 9,052,684.5 | 499,394.3 | 2.907x | 150.118x |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 7,808,133.9 | 5.6735 | 7,792,432.1 | 7,833,590.6 | 16,405.9 | 2.908x | 150.138x |
| 8 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 7,809,454.0 | 5.6744 | 7,799,061.6 | 7,831,641.1 | 12,893.3 | 2.908x | 150.163x |

#### `nested-comment-rec` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,669.7 | 0.0378 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,141,707.7 | 1.0888 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,609,287.0 | 1.5347 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 2,057,363.9 | 1.9621 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 5,934,805.8 | 5.6599 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 5,943,457.4 | 5.6681 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 5,947,320.3 | 5.6718 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 5,952,554.2 | 5.6768 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 9,835.9 | 0.0375 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 285,203.7 | 1.0880 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 402,915.4 | 1.5370 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 508,962.3 | 1.9415 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 1,484,896.9 | 5.6644 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 1,489,141.9 | 5.6806 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 1,486,476.0 | 5.6705 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,486,507.1 | 5.6706 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 2,516.2 | 0.0384 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 71,686.3 | 1.0938 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 95,215.2 | 1.4529 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 119,191.7 | 1.8187 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 371,704.1 | 5.6718 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 373,061.2 | 5.6925 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 372,012.9 | 5.6765 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 372,374.8 | 5.6820 |

### `nested-comment-rec` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,232.4 | 3,102.1 | 3,324.3 | 85.7 | 0.618x | 1.000x | 75 | 43.1 | 40.4 | 100% |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,461.8 | 4,452.7 | 4,474.4 | 7.4 | 0.853x | 1.380x | 75 | 59.5 | 58.6 | 100% |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 5,231.5 | 5,204.9 | 5,257.8 | 19.5 | 1.000x | 1.618x | 75 | 69.8 | 34.4 | 100% |
| 4 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 6,937.2 | 6,911.7 | 7,571.7 | 256.5 | 1.326x | 2.146x | 75 | 92.5 | 30.4 | 100% |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 9,287.2 | 9,268.6 | 9,306.3 | 14.6 | 1.775x | 2.873x | 75 | 123.8 | 18.0 | 100% |
| 6 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 9,306.4 | 9,298.5 | 9,361.5 | 23.6 | 1.779x | 2.879x | 75 | 124.1 | 8.9 | 100% |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 9,315.0 | 9,066.2 | 15,516.3 | 2,526.6 | 1.781x | 2.882x | 75 | 124.2 | 17.3 | 100% |
| 8 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 9,319.6 | 9,276.3 | 9,381.1 | 37.9 | 1.781x | 2.883x | 75 | 124.3 | 8.9 | 100% |

### `numeric-id-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 15.2 | 0.0000 | 15.1 | 15.4 | 0.1 | 0.161x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 27.8 | 0.0000 | 27.7 | 29.3 | 0.6 | 0.295x | 1.829x |
| 3 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 80.3 | 0.0001 | 80.2 | 91.4 | 4.4 | 0.852x | 5.284x |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 86.6 | 0.0001 | 85.6 | 103.2 | 6.8 | 0.919x | 5.696x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 94.2 | 0.0001 | 94.2 | 144.8 | 20.2 | 1.000x | 6.198x |
| 6 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 95.3 | 0.0001 | 93.7 | 101.3 | 3.2 | 1.012x | 6.271x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 124.1 | 0.0001 | 123.0 | 152.3 | 11.4 | 1.317x | 8.161x |
| 8 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 167.5 | 0.0001 | 166.8 | 169.8 | 1.1 | 1.778x | 11.022x |
| 9 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 285.1 | 0.0002 | 284.4 | 298.2 | 5.3 | 3.026x | 18.754x |
| 10 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 286.6 | 0.0002 | 285.0 | 301.2 | 5.9 | 3.043x | 18.858x |
| 11 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,066,879.1 | 2.9550 | 4,064,368.3 | 4,073,499.7 | 3,235.7 | 43170.156x | 267562.817x |
| 12 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,078,576.9 | 2.9635 | 4,064,420.0 | 4,202,404.8 | 52,508.0 | 43294.328x | 268332.423x |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 8,694,208.3 | 6.3173 | 8,684,286.3 | 8,772,257.7 | 32,602.9 | 92289.521x | 571998.037x |

#### `numeric-id-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 5.0 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 9.2 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 26.8 | 0.0000 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 27.7 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 31.3 | 0.0000 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 31.9 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 41.2 | 0.0000 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.5 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 88.9 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 88.2 | 0.0001 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,096,307.3 | 2.9529 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,096,332.9 | 2.9529 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 6,625,504.8 | 6.3186 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 5.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 9.4 | 0.0000 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 26.7 | 0.0001 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 29.1 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 31.4 | 0.0001 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 31.8 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 41.2 | 0.0002 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.6 | 0.0002 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 88.2 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 89.2 | 0.0003 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 774,603.6 | 2.9549 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 774,931.3 | 2.9561 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 1,655,366.4 | 6.3147 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 5.1 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 9.2 | 0.0001 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 26.9 | 0.0004 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 30.5 | 0.0005 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 31.5 | 0.0005 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 31.6 | 0.0005 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 41.3 | 0.0006 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.9 | 0.0009 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 107.5 | 0.0016 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 109.1 | 0.0017 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 194,406.4 | 2.9664 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 194,811.4 | 2.9726 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 415,593.9 | 6.3415 |

### `numeric-id-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | set composition | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 470.7 | 468.4 | 473.3 | 1.6 | 0.000x | 1.000x | spread | 75 | 6.3 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 834.5 | 833.3 | 852.9 | 8.2 | 0.000x | 1.773x | spread | 75 | 11.1 | 8.9 | 100% |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,963.8 | 1,959.9 | 1,965.1 | 1.8 | 0.000x | 4.172x | spread | 75 | 26.2 | 27.2 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,674.0 | 2,657.8 | 2,687.4 | 9.7 | 0.000x | 5.681x | spread | 75 | 35.7 | 16.4 | 100% |
| 5 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 9,603.5 | 9,577.6 | 9,792.7 | 79.4 | 0.000x | 20.403x | spread | 75 | 128.0 | 100.2 | 100% |
| 6 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,657.8 | 9,570.4 | 9,783.1 | 67.9 | 0.000x | 20.518x | spread | 75 | 128.8 | 100.0 | 100% |
| 7 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 13,240.3 | 13,222.2 | 13,672.8 | 173.9 | 0.000x | 28.129x | spread | 75 | 176.5 | 30.4 | 100% |
| 8 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 13,295.3 | 13,281.9 | 13,361.0 | 30.7 | 0.000x | 28.246x | spread | 75 | 177.3 | 27.9 | 100% |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,113,242.7 | 3,103,890.7 | 3,125,062.7 | 8,232.5 | 0.091x | 6614.031x | **dominated**: `rd-numeric-id-near-miss` is 99.9% of this set | 75 | 41,509.9 | 40.4 | 100% |
| 10 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 9,237,223.0 | 9,226,225.7 | 9,241,297.5 | 5,797.8 | 0.271x | 19624.324x | **dominated**: `rd-numeric-id-near-miss` is 99.9% of this set | 75 | 123,163.0 | 18.0 | 100% |
| 11 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 9,305,888.0 | 9,238,329.3 | 9,514,122.0 | 102,398.3 | 0.273x | 19770.201x | **dominated**: `rd-numeric-id-near-miss` is 99.9% of this set | 75 | 124,078.5 | 17.3 | 100% |
| 12 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 12,590,485.6 | 12,556,989.4 | 12,952,288.1 | 149,711.2 | 0.370x | 26748.273x | **dominated**: `rd-numeric-id-near-miss` is 99.9% of this set | 75 | 167,873.1 | 58.6 | 100% |
| 13 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 34,025,624.1 | 34,003,935.4 | 34,195,102.5 | 82,077.0 | 1.000x | 72286.861x | **dominated**: `rd-numeric-id-near-miss` is 100.0% of this set | 75 | 453,675.0 | 34.4 | 100% |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; `--grain subject` carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

_per-subject rows: 75 subjects — too many to enumerate here (the cap is 24); `--grain subject` renders them._

### `phone-list-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 15.2 | 0.0000 | 15.2 | 15.3 | 0.1 | 0.162x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 28.5 | 0.0000 | 28.4 | 31.0 | 1.0 | 0.303x | 1.873x |
| 3 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 81.0 | 0.0001 | 80.8 | 92.9 | 4.8 | 0.860x | 5.315x |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 86.8 | 0.0001 | 86.6 | 89.1 | 1.0 | 0.922x | 5.695x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 94.2 | 0.0001 | 94.1 | 94.2 | 0.0 | 1.000x | 6.180x |
| 6 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 94.7 | 0.0001 | 93.7 | 95.4 | 0.7 | 1.006x | 6.218x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 124.2 | 0.0001 | 120.2 | 129.1 | 2.9 | 1.319x | 8.149x |
| 8 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 167.0 | 0.0001 | 166.9 | 167.1 | 0.1 | 1.773x | 10.960x |
| 9 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 286.2 | 0.0002 | 284.3 | 289.5 | 1.9 | 3.039x | 18.780x |
| 10 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 286.4 | 0.0002 | 284.0 | 289.7 | 1.8 | 3.042x | 18.796x |
| 11 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 3,863,849.0 | 2.8075 | 3,862,204.1 | 3,866,289.0 | 1,325.1 | 41030.833x | 253566.608x |
| 12 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 3,864,688.4 | 2.8081 | 3,862,375.6 | 3,891,005.3 | 10,862.8 | 41039.747x | 253621.694x |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 8,683,755.6 | 6.3097 | 8,673,709.6 | 8,710,308.4 | 13,344.1 | 92214.195x | 569874.867x |

#### `phone-list-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 5.1 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 9.6 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 26.9 | 0.0000 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 26.6 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 31.3 | 0.0000 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 31.4 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 42.1 | 0.0000 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.5 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 89.3 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 88.2 | 0.0001 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 2,943,141.8 | 2.8068 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 2,941,782.9 | 2.8055 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 6,614,472.7 | 6.3081 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 5.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 9.5 | 0.0000 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 26.8 | 0.0001 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 29.3 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 31.4 | 0.0001 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 31.5 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 41.0 | 0.0002 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.6 | 0.0002 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 89.0 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 88.1 | 0.0003 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 736,160.1 | 2.8082 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 737,306.3 | 2.8126 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 1,653,458.6 | 6.3074 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 5.1 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 9.5 | 0.0001 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 27.1 | 0.0004 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 30.7 | 0.0005 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 31.5 | 0.0005 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 31.7 | 0.0005 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 41.0 | 0.0006 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.9 | 0.0009 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 108.2 | 0.0017 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 109.4 | 0.0017 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 184,709.6 | 2.8184 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 185,274.6 | 2.8271 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 416,018.2 | 6.3479 |

### `phone-list-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | set composition | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 480.6 | 479.9 | 482.2 | 0.8 | 0.000x | 1.000x | spread | 75 | 6.4 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 902.4 | 895.0 | 921.4 | 9.0 | 0.000x | 1.878x | spread | 75 | 12.0 | 8.9 | 100% |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,984.0 | 1,983.3 | 2,101.8 | 46.0 | 0.000x | 4.128x | spread | 75 | 26.5 | 27.2 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,969.7 | 2,965.1 | 3,034.4 | 26.7 | 0.000x | 6.179x | spread | 75 | 39.6 | 16.4 | 100% |
| 5 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 10,014.8 | 9,965.3 | 10,124.4 | 65.9 | 0.000x | 20.838x | spread | 75 | 133.5 | 100.0 | 100% |
| 6 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 10,105.3 | 10,021.8 | 10,821.2 | 302.4 | 0.000x | 21.026x | spread | 75 | 134.7 | 100.2 | 100% |
| 7 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 15,004.8 | 14,930.0 | 15,031.3 | 36.6 | 0.000x | 31.221x | spread | 75 | 200.1 | 27.9 | 100% |
| 8 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 15,202.4 | 15,145.8 | 15,902.2 | 286.2 | 0.000x | 31.632x | spread | 75 | 202.7 | 30.4 | 100% |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,895,514.6 | 3,887,027.4 | 3,903,410.1 | 5,891.8 | 0.097x | 8105.539x | **dominated**: `rd-numeric-id-near-miss` is 99.9% of this set | 75 | 51,940.2 | 40.4 | 100% |
| 10 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 9,976,242.1 | 9,959,851.9 | 10,252,541.5 | 112,186.4 | 0.250x | 20757.930x | **dominated**: `rd-numeric-id-near-miss` is 99.9% of this set | 75 | 133,016.6 | 17.3 | 100% |
| 11 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 9,984,843.3 | 9,968,537.5 | 9,988,872.6 | 7,039.2 | 0.250x | 20775.826x | **dominated**: `rd-numeric-id-near-miss` is 99.9% of this set | 75 | 133,131.2 | 18.0 | 100% |
| 12 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 16,693,186.2 | 16,645,155.7 | 17,278,804.8 | 238,231.0 | 0.418x | 34734.119x | **dominated**: `rd-numeric-id-near-miss` is 100.0% of this set | 75 | 222,575.8 | 58.6 | 100% |
| 13 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 39,975,369.4 | 39,647,313.1 | 40,435,170.8 | 273,984.8 | 1.000x | 83178.204x | **dominated**: `rd-numeric-id-near-miss` is 100.0% of this set | 75 | 533,004.9 | 34.4 | 100% |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; `--grain subject` carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

_per-subject rows: 75 subjects — too many to enumerate here (the cap is 24); `--grain subject` renders them._

### `phone-palindrome-6` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,212,527.9 | 1.6076 | 2,209,209.6 | 2,232,888.8 | 10,232.8 | 0.109x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 7,116,848.0 | 5.1712 | 6,614,522.0 | 7,446,970.7 | 295,609.9 | 0.350x | 3.217x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 7,152,601.1 | 5.1971 | 6,794,488.9 | 7,326,160.8 | 184,668.3 | 0.352x | 3.233x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 7,588,174.4 | 5.5136 | 7,535,028.1 | 7,668,152.6 | 44,808.6 | 0.373x | 3.430x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 7,609,890.0 | 5.5294 | 7,539,144.1 | 7,652,590.5 | 43,584.5 | 0.374x | 3.439x |
| 6 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 14,477,787.7 | 10.5197 | 14,410,840.5 | 16,677,678.8 | 885,794.3 | 0.712x | 6.544x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 20,329,662.6 | 14.7717 | 20,269,516.6 | 20,396,375.1 | 40,808.9 | 1.000x | 9.188x |
| 8 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 28,963,805.0 | 21.0454 | 28,720,721.8 | 29,121,590.8 | 155,206.3 | 1.425x | 13.091x |

#### `phone-palindrome-6` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 1,691,442.6 | 1.6131 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 5,564,913.6 | 5.3071 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 5,591,819.2 | 5.3328 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 5,914,560.2 | 5.6406 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 5,790,128.3 | 5.5219 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 11,103,596.2 | 10.5892 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 15,606,478.0 | 14.8835 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 22,160,921.6 | 21.1343 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 419,310.5 | 1.5995 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 1,251,513.0 | 4.7741 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 1,251,253.4 | 4.7732 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,398,779.1 | 5.3359 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 1,434,928.7 | 5.4738 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 2,720,979.9 | 10.3797 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 3,807,524.4 | 14.5246 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 5,459,734.8 | 20.8272 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 101,854.8 | 1.5542 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 311,651.4 | 4.7554 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 310,160.0 | 4.7327 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 313,853.0 | 4.7890 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 356,854.0 | 5.4452 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 658,196.4 | 10.0433 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 915,617.4 | 13.9712 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,356,522.7 | 20.6989 |

### `phone-palindrome-6` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 4,545.7 | 4,519.9 | 4,704.0 | 68.3 | 0.259x | 1.000x | 75 | 60.6 | 40.4 | 100% |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 7,212.3 | 7,130.7 | 7,791.7 | 238.1 | 0.411x | 1.587x | 75 | 96.2 | 18.0 | 100% |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 7,225.5 | 7,027.5 | 7,518.3 | 166.2 | 0.412x | 1.590x | 75 | 96.3 | 8.9 | 100% |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 7,559.1 | 7,252.5 | 7,659.0 | 147.8 | 0.431x | 1.663x | 75 | 100.8 | 8.9 | 100% |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 7,821.4 | 7,699.1 | 7,946.3 | 82.4 | 0.446x | 1.721x | 75 | 104.3 | 17.3 | 100% |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,534.3 | 17,496.5 | 17,734.1 | 85.0 | 1.000x | 3.857x | 75 | 233.8 | 34.4 | 100% |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 22,750.7 | 22,734.3 | 22,863.2 | 55.8 | 1.297x | 5.005x | 75 | 303.3 | 58.6 | 100% |
| 8 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 30,494.1 | 30,054.2 | 31,238.8 | 391.5 | 1.739x | 6.708x | 75 | 406.6 | 27.9 | 100% |

### `pwd-strength-chain` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 222.2 | 0.0002 | 221.3 | 226.8 | 2.0 | 0.043x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 225.0 | 0.0002 | 220.7 | 238.2 | 6.2 | 0.044x | 1.013x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,132.0 | 0.0008 | 1,130.0 | 1,134.7 | 1.6 | 0.219x | 5.095x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,048.4 | 0.0029 | 4,037.1 | 4,824.4 | 310.2 | 0.783x | 18.221x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 5,172.1 | 0.0038 | 5,158.0 | 5,211.6 | 20.2 | 1.000x | 23.278x |
| 6 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 12,106.1 | 0.0088 | 12,090.6 | 12,134.5 | 16.6 | 2.341x | 54.487x |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 3,675,351.7 | 2.6705 | 3,673,430.4 | 3,688,578.9 | 5,555.2 | 710.613x | 16541.996x |
| 8 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 3,678,210.4 | 2.6726 | 3,675,790.8 | 3,686,141.7 | 4,183.0 | 711.166x | 16554.862x |

#### `pwd-strength-chain` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 58.1 | 0.0001 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 57.8 | 0.0001 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 131.0 | 0.0001 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 573.5 | 0.0005 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 637.8 | 0.0006 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,280.7 | 0.0012 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 2,798,410.0 | 2.6688 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 2,801,185.2 | 2.6714 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 95.3 | 0.0004 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 95.7 | 0.0004 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 596.7 | 0.0023 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 1,841.3 | 0.0070 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 2,638.5 | 0.0101 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 5,972.6 | 0.0228 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 700,410.2 | 2.6719 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 701,616.0 | 2.6765 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 69.0 | 0.0011 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 69.1 | 0.0011 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 405.9 | 0.0062 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 1,633.7 | 0.0249 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 1,893.4 | 0.0289 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 4,865.6 | 0.0742 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 176,144.9 | 2.6878 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 176,364.0 | 2.6911 |

### `pwd-strength-chain` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 8,323.2 | 8,289.4 | 8,370.7 | 30.8 | 0.231x | 1.000x | 75 | 111.0 | 40.4 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 12,402.4 | 12,368.5 | 16,770.0 | 1,733.8 | 0.343x | 1.490x | 75 | 165.4 | 8.9 | 100% |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 12,651.4 | 12,349.8 | 12,701.5 | 151.4 | 0.350x | 1.520x | 75 | 168.7 | 8.9 | 100% |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 14,485.2 | 14,465.1 | 14,614.2 | 57.1 | 0.401x | 1.740x | 75 | 193.1 | 18.0 | 100% |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 14,705.5 | 14,688.9 | 14,762.2 | 25.7 | 0.407x | 1.767x | 75 | 196.1 | 17.3 | 100% |
| 6 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 36,028.0 | 36,023.7 | 38,607.8 | 1,014.2 | 0.998x | 4.329x | 75 | 480.4 | 58.6 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 36,107.0 | 35,957.5 | 36,313.1 | 129.7 | 1.000x | 4.338x | 75 | 481.4 | 34.4 | 100% |
| 8 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 95,501.0 | 94,995.6 | 99,228.5 | 1,574.2 | 2.645x | 11.474x | 75 | 1,273.3 | 30.4 | 100% |

### `quoted-delim-match` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 460,903.3 | 0.3349 | 458,315.3 | 467,298.6 | 2,981.1 | 0.110x | 1.000x |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,837,824.3 | 2.7886 | 3,817,923.8 | 3,870,074.1 | 18,863.8 | 0.913x | 8.327x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,205,744.4 | 3.0559 | 4,190,894.0 | 4,227,034.9 | 12,261.6 | 1.000x | 9.125x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 9,769,774.0 | 7.0988 | 9,751,456.0 | 9,859,715.6 | 38,817.9 | 2.323x | 21.197x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 10,085,258.9 | 7.3280 | 9,913,670.8 | 10,120,712.8 | 81,233.2 | 2.398x | 21.882x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 10,098,004.3 | 7.3373 | 9,965,186.9 | 10,129,201.4 | 58,369.8 | 2.401x | 21.909x |
| 7 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 10,105,662.6 | 7.3429 | 10,066,798.0 | 10,192,433.7 | 41,683.0 | 2.403x | 21.926x |

#### `quoted-delim-match` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 354,469.1 | 0.3380 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 2,936,976.8 | 2.8009 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 3,222,438.0 | 3.0732 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 7,470,637.6 | 7.1246 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 7,697,543.6 | 7.3409 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 7,716,656.4 | 7.3592 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 7,698,813.2 | 7.3422 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 84,999.4 | 0.3242 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 718,631.8 | 2.7414 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 779,383.7 | 2.9731 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,855,170.7 | 7.0769 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 1,910,123.8 | 7.2865 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 1,895,877.0 | 7.2322 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 1,926,068.2 | 7.3474 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 21,429.7 | 0.3270 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 180,419.7 | 2.7530 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 199,603.8 | 3.0457 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 450,217.2 | 6.8698 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 475,194.1 | 7.2509 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 470,250.1 | 7.1754 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 482,603.1 | 7.3639 |

### `quoted-delim-match` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,317.1 | 3,229.2 | 3,490.4 | 106.7 | 0.396x | 1.000x | 75 | 44.2 | 40.4 | 100% |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 7,095.2 | 7,081.4 | 7,134.8 | 18.7 | 0.848x | 2.139x | 75 | 94.6 | 58.6 | 100% |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 8,370.4 | 8,299.1 | 8,577.6 | 101.5 | 1.000x | 2.523x | 75 | 111.6 | 34.4 | 100% |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 11,161.3 | 11,049.3 | 11,375.0 | 111.4 | 1.333x | 3.365x | 75 | 148.8 | 8.9 | 100% |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 11,359.6 | 11,332.6 | 28,643.4 | 6,916.1 | 1.357x | 3.425x | 75 | 151.5 | 8.9 | 100% |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 11,419.3 | 11,314.3 | 11,444.1 | 50.5 | 1.364x | 3.443x | 75 | 152.3 | 18.0 | 100% |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11,510.0 | 11,463.9 | 11,743.8 | 103.2 | 1.375x | 3.470x | 75 | 153.5 | 17.3 | 100% |

### `router-prefix-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,249.4 | 0.0009 | 1,248.8 | 1,250.2 | 0.5 | 0.001x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 60,176.9 | 0.0437 | 60,140.3 | 60,326.9 | 70.0 | 0.027x | 48.164x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 91,706.5 | 0.0666 | 91,687.8 | 92,376.7 | 268.9 | 0.041x | 73.400x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 393,596.8 | 0.2860 | 393,536.7 | 398,012.7 | 1,760.1 | 0.176x | 315.027x |
| 5 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 393,775.6 | 0.2861 | 393,405.7 | 395,654.3 | 828.7 | 0.176x | 315.170x |
| 6 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 400,035.5 | 0.2907 | 399,107.4 | 403,813.4 | 1,728.4 | 0.179x | 320.180x |
| 7 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 400,418.3 | 0.2909 | 399,254.2 | 405,719.5 | 2,441.8 | 0.179x | 320.486x |
| 8 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 1,361,509.6 | 0.9893 | 1,360,131.0 | 1,366,519.3 | 2,209.7 | 0.610x | 1089.723x |
| 9 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 2,182,520.9 | 1.5858 | 2,166,544.3 | 2,186,450.1 | 7,059.5 | 0.977x | 1746.843x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,233,113.3 | 1.6226 | 2,227,974.7 | 2,235,032.1 | 2,816.5 | 1.000x | 1787.336x |
| 11 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,064,826.4 | 2.9535 | 4,055,492.8 | 4,067,653.3 | 4,536.5 | 1.820x | 3253.400x |
| 12 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,066,276.1 | 2.9546 | 4,063,349.5 | 4,079,912.9 | 6,017.5 | 1.821x | 3254.561x |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 26,327,343.3 | 19.1297 | 26,305,079.1 | 26,585,831.7 | 104,626.0 | 11.790x | 21071.844x |

#### `router-prefix-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 85.2 | 0.0001 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 46,014.7 | 0.0439 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 70,166.1 | 0.0669 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 302,133.4 | 0.2881 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 302,087.1 | 0.2881 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 304,523.3 | 0.2904 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 305,168.2 | 0.2910 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,039,087.2 | 0.9910 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,671,958.0 | 1.5945 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 1,711,559.9 | 1.6323 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,098,893.4 | 2.9553 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,100,124.9 | 2.9565 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 20,052,616.4 | 19.1237 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 632.8 | 0.0024 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 11,435.6 | 0.0436 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 17,397.9 | 0.0664 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 74,484.4 | 0.2841 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 74,540.9 | 0.2844 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 74,622.2 | 0.2847 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 74,791.7 | 0.2853 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 259,546.0 | 0.9901 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 414,660.2 | 1.5818 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 421,609.2 | 1.6083 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 773,927.8 | 2.9523 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 774,781.7 | 2.9556 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 5,019,417.1 | 19.1476 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 531.2 | 0.0081 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 2,735.2 | 0.0417 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 4,148.9 | 0.0633 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 16,950.2 | 0.2586 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 17,145.1 | 0.2616 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 20,094.7 | 0.3066 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 19,827.3 | 0.3025 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 62,428.3 | 0.9526 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 95,585.7 | 1.4585 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 98,386.7 | 1.5013 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 192,005.5 | 2.9298 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 192,636.2 | 2.9394 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,253,820.8 | 19.1318 |

### `router-prefix-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 775.5 | 769.6 | 789.6 | 7.0 | 0.209x | 1.000x | 75 | 10.3 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 786.1 | 773.4 | 803.7 | 10.0 | 0.212x | 1.014x | 75 | 10.5 | 8.9 | 100% |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,313.2 | 1,309.4 | 1,314.5 | 1.9 | 0.355x | 1.693x | 75 | 17.5 | 16.4 | 100% |
| 4 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,297.6 | 2,294.2 | 2,306.2 | 4.1 | 0.620x | 2.963x | 75 | 30.6 | 27.2 | 100% |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,808.1 | 2,801.2 | 2,840.1 | 17.2 | 0.758x | 3.621x | 75 | 37.4 | 58.6 | 100% |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,822.7 | 2,768.2 | 3,121.6 | 126.2 | 0.762x | 3.640x | 75 | 37.6 | 40.4 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,703.0 | 3,595.6 | 3,729.1 | 51.8 | 1.000x | 4.775x | 75 | 49.4 | 34.4 | 100% |
| 8 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,467.9 | 4,441.3 | 4,604.5 | 66.5 | 1.207x | 5.762x | 75 | 59.6 | 17.3 | 100% |
| 9 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,626.1 | 4,548.0 | 4,670.0 | 41.3 | 1.249x | 5.966x | 75 | 61.7 | 18.0 | 100% |
| 10 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,631.1 | 7,599.5 | 8,310.2 | 274.6 | 2.061x | 9.841x | 75 | 101.7 | 100.0 | 100% |

### `tag-depth3-bound` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 23,238.0 | 0.0169 | 23,223.2 | 23,268.6 | 17.1 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 23,252.3 | 0.0169 | 23,229.1 | 23,335.8 | 40.0 | 1.001x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 40,177.5 | 0.0292 | 40,096.1 | 40,344.8 | 91.6 | 1.729x | 1.729x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,230,556.5 | 1.6207 | 2,228,823.6 | 2,233,826.7 | 1,803.9 | 95.988x | 95.988x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,489,301.9 | 3.2620 | 4,484,756.9 | 4,500,134.3 | 6,104.1 | 193.188x | 193.188x |
| 6 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 4,512,595.0 | 3.2789 | 4,495,773.7 | 4,530,593.9 | 11,175.2 | 194.191x | 194.191x |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,513,390.3 | 3.2795 | 4,491,216.6 | 4,521,955.5 | 12,501.2 | 194.225x | 194.225x |
| 8 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 4,687,857.3 | 3.4062 | 4,681,444.2 | 4,696,744.8 | 5,004.1 | 201.733x | 201.733x |
| 9 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 34,508,904.2 | 25.0745 | 34,440,542.6 | 34,914,541.2 | 176,483.6 | 1485.022x | 1485.022x |

#### `tag-depth3-bound` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,694.1 | 0.0169 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 17,704.0 | 0.0169 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 30,532.9 | 0.0291 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,697,961.9 | 1.6193 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,413,827.5 | 3.2557 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 3,433,715.5 | 3.2746 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,412,896.0 | 3.2548 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 3,567,527.6 | 3.4023 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 26,286,922.8 | 25.0692 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 4,404.8 | 0.0168 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 4,418.7 | 0.0169 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 7,615.8 | 0.0291 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 425,020.0 | 1.6213 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 853,151.9 | 3.2545 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 856,574.0 | 3.2676 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 854,335.3 | 3.2590 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 893,868.9 | 3.4098 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 6,574,723.4 | 25.0806 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 1,133.2 | 0.0173 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,133.8 | 0.0173 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 1,964.5 | 0.0300 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,562.7 | 1.6260 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 221,905.5 | 3.3860 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 225,231.6 | 3.4368 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 226,148.5 | 3.4508 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 223,936.9 | 3.4170 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,647,258.1 | 25.1352 |

### `tag-depth3-bound` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,585.2 | 3,504.7 | 3,840.9 | 116.1 | 0.501x | 1.000x | 75 | 47.8 | 40.4 | 100% |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 6,552.2 | 6,546.6 | 6,588.6 | 15.0 | 0.916x | 1.828x | 75 | 87.4 | 58.6 | 100% |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 6,897.6 | 6,833.1 | 8,023.3 | 449.1 | 0.964x | 1.924x | 75 | 92.0 | 17.3 | 100% |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 6,976.2 | 6,931.7 | 7,079.0 | 53.7 | 0.975x | 1.946x | 75 | 93.0 | 8.9 | 100% |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 7,142.8 | 6,971.0 | 7,341.0 | 126.1 | 0.999x | 1.992x | 75 | 95.2 | 8.9 | 100% |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 7,152.0 | 7,106.6 | 7,167.1 | 21.4 | 1.000x | 1.995x | 75 | 95.4 | 34.4 | 100% |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 7,223.8 | 7,024.1 | 7,352.1 | 114.8 | 1.010x | 2.015x | 75 | 96.3 | 18.0 | 100% |
| 8 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 47,435.2 | 47,322.8 | 47,514.6 | 67.4 | 6.632x | 13.231x | 75 | 632.5 | 27.9 | 100% |

### `tag-pair-match` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 23,229.8 | 0.0169 | 23,196.0 | 23,251.0 | 19.5 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 39,993.9 | 0.0291 | 39,889.5 | 40,218.9 | 124.6 | 1.722x | 1.722x |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,229,027.8 | 1.6196 | 2,228,591.7 | 2,240,708.9 | 4,690.7 | 95.956x | 95.956x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 4,634,280.3 | 3.3673 | 4,627,646.4 | 4,643,640.7 | 6,159.4 | 199.497x | 199.497x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,653,813.3 | 3.3815 | 4,649,628.1 | 4,668,347.7 | 6,375.5 | 200.338x | 200.338x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,657,169.8 | 3.3839 | 4,646,030.3 | 4,658,462.3 | 4,906.5 | 200.483x | 200.483x |
| 7 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 4,657,312.3 | 3.3840 | 4,653,151.2 | 4,659,616.2 | 2,624.5 | 200.489x | 200.489x |
| 8 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 27,821,937.3 | 20.2157 | 27,753,897.0 | 27,866,656.7 | 42,766.3 | 1197.684x | 1197.684x |

#### `tag-pair-match` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,672.3 | 0.0169 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 30,463.7 | 0.0291 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,697,627.3 | 1.6190 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 3,531,171.5 | 3.3676 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,546,960.3 | 3.3826 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,543,370.8 | 3.3792 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 3,545,653.5 | 3.3814 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 21,149,505.7 | 20.1697 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 4,423.7 | 0.0169 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 7,568.8 | 0.0289 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 424,700.0 | 1.6201 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 881,594.4 | 3.3630 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 887,298.7 | 3.3848 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 887,885.7 | 3.3870 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 887,820.1 | 3.3868 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 5,353,807.2 | 20.4232 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 1,135.1 | 0.0173 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 1,964.8 | 0.0300 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,597.8 | 1.6266 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 222,099.9 | 3.3890 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 222,831.8 | 3.4001 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 221,754.4 | 3.3837 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 222,619.5 | 3.3969 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,337,324.6 | 20.4060 |

### `tag-pair-match` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,274.2 | 3,177.9 | 3,313.0 | 57.3 | 0.754x | 1.000x | 75 | 43.7 | 40.4 | 100% |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,343.7 | 4,283.8 | 4,474.8 | 67.5 | 1.000x | 1.327x | 75 | 57.9 | 34.4 | 100% |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,951.1 | 5,937.2 | 5,964.9 | 11.6 | 1.370x | 1.818x | 75 | 79.3 | 58.6 | 100% |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 6,023.9 | 5,972.0 | 6,055.2 | 30.0 | 1.387x | 1.840x | 75 | 80.3 | 8.9 | 100% |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 6,045.5 | 5,990.6 | 6,061.4 | 30.6 | 1.392x | 1.846x | 75 | 80.6 | 18.0 | 100% |
| 6 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 6,125.7 | 6,109.2 | 6,692.3 | 227.5 | 1.410x | 1.871x | 75 | 81.7 | 8.9 | 100% |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 6,272.5 | 6,254.1 | 6,555.6 | 114.4 | 1.444x | 1.916x | 75 | 83.6 | 17.3 | 100% |

### `trim-nested-star` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 15.2 | 0.0000 | 15.2 | 15.3 | 0.0 | 0.043x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 82.5 | 0.0001 | 82.2 | 94.6 | 4.8 | 0.232x | 5.417x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 126.8 | 0.0001 | 122.7 | 132.4 | 3.3 | 0.356x | 8.325x |
| 4 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 167.0 | 0.0001 | 166.9 | 167.0 | 0.0 | 0.469x | 10.961x |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 253.4 | 0.0002 | 243.9 | 256.5 | 5.1 | 0.712x | 16.639x |
| 6 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 286.4 | 0.0002 | 284.8 | 290.4 | 2.1 | 0.804x | 18.806x |
| 7 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 286.6 | 0.0002 | 285.7 | 289.0 | 1.1 | 0.805x | 18.813x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 356.1 | 0.0003 | 354.5 | 358.8 | 1.5 | 1.000x | 23.380x |
| 9 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 745.0 | 0.0005 | 729.6 | 752.1 | 8.6 | 2.092x | 48.907x |
| 10 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 3,255,085.8 | 2.3652 | 3,252,915.1 | 3,295,927.6 | 16,593.1 | 9140.494x | 213701.493x |
| 11 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 3,256,238.0 | 2.3660 | 3,252,293.5 | 3,280,132.2 | 10,674.1 | 9143.730x | 213777.142x |
| 12 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 3,256,381.0 | 2.3661 | 3,254,100.7 | 3,283,305.6 | 11,174.9 | 9144.132x | 213786.528x |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 11,837,748.5 | 8.6014 | 11,782,156.0 | 12,121,955.0 | 120,069.7 | 33241.175x | 777166.784x |

#### `trim-nested-star` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 5.1 | 0.0000 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 26.0 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 42.4 | 0.0000 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.6 | 0.0001 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 84.1 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 88.9 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 89.6 | 0.0001 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 118.3 | 0.0001 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 247.1 | 0.0002 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 2,478,935.5 | 2.3641 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 2,477,107.8 | 2.3624 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 2,479,174.4 | 2.3643 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 9,019,656.5 | 8.6018 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 5.1 | 0.0000 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 27.6 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 42.5 | 0.0002 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.6 | 0.0002 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 84.2 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 88.5 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 88.6 | 0.0003 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 118.9 | 0.0005 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 247.3 | 0.0009 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 620,102.5 | 2.3655 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 619,724.6 | 2.3641 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 619,996.7 | 2.3651 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 2,253,144.9 | 8.5951 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 5.1 | 0.0001 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 28.8 | 0.0004 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 41.8 | 0.0006 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.8 | 0.0009 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 84.9 | 0.0013 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 109.1 | 0.0017 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 109.0 | 0.0017 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 118.9 | 0.0018 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 249.8 | 0.0038 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 155,772.4 | 2.3769 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 155,851.7 | 2.3781 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 156,299.8 | 2.3849 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 567,622.6 | 8.6612 |

### `trim-nested-star` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | set composition | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 427.7 | 425.7 | 429.4 | 1.4 | 0.000x | 1.000x | spread | 75 | 5.7 | 8.9 | 100% |
| 2 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,862.7 | 1,861.4 | 1,865.5 | 1.6 | 0.000x | 4.355x | spread | 75 | 24.8 | 27.2 | 100% |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,993.1 | 1,966.1 | 1,997.3 | 11.2 | 0.000x | 4.660x | spread | 75 | 26.6 | 16.4 | 100% |
| 4 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,422.8 | 9,396.7 | 9,439.7 | 14.7 | 0.000x | 22.030x | spread | 75 | 125.6 | 100.0 | 100% |
| 5 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 9,468.1 | 9,446.9 | 9,519.3 | 27.8 | 0.000x | 22.136x | spread | 75 | 126.2 | 100.2 | 100% |
| 6 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 13,638.5 | 12,948.0 | 13,659.8 | 341.3 | 0.000x | 31.886x | spread | 75 | 181.8 | 30.4 | 100% |
| 7 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 19,453.6 | 19,386.4 | 19,630.7 | 89.3 | 0.001x | 45.481x | spread | 75 | 259.4 | 27.9 | 100% |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,390,462.6 | 3,381,540.0 | 3,417,180.1 | 12,931.8 | 0.100x | 7926.644x | **dominated**: `rd-trim-near-miss` is 99.9% of this set | 75 | 45,206.2 | 40.4 | 100% |
| 9 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 8,952,903.0 | 8,950,582.0 | 8,994,395.8 | 16,477.1 | 0.264x | 20931.206x | **dominated**: `rd-trim-near-miss` is 99.9% of this set | 75 | 119,372.0 | 18.0 | 100% |
| 10 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 8,971,502.8 | 8,968,103.5 | 9,021,407.6 | 20,145.0 | 0.265x | 20974.691x | **dominated**: `rd-trim-near-miss` is 99.9% of this set | 75 | 119,620.0 | 8.9 | 100% |
| 11 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 8,996,592.0 | 8,947,951.0 | 9,004,462.2 | 20,754.0 | 0.265x | 21033.348x | **dominated**: `rd-trim-near-miss` is 99.9% of this set | 75 | 119,954.6 | 17.3 | 100% |
| 12 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 12,536,685.1 | 12,517,587.1 | 12,554,973.7 | 12,607.1 | 0.370x | 29309.816x | **dominated**: `rd-trim-near-miss` is 99.9% of this set | 75 | 167,155.8 | 58.6 | 100% |
| 13 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 33,894,166.4 | 33,845,989.1 | 33,977,605.1 | 46,589.8 | 1.000x | 79241.983x | **dominated**: `rd-trim-near-miss` is 100.0% of this set | 75 | 451,922.2 | 34.4 | 100% |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; `--grain subject` carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

_per-subject rows: 75 subjects — too many to enumerate here (the cap is 24); `--grain subject` renders them._

### `utf8-lead-no-cont` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 480,493.7 | 0.3491 | 436,276.7 | 487,659.5 | 19,458.1 | 0.472x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 481,068.0 | 0.3495 | 479,371.1 | 483,073.8 | 1,173.7 | 0.473x | 1.001x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 481,115.9 | 0.3496 | 479,496.9 | 483,893.0 | 1,690.9 | 0.473x | 1.001x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,017,026.6 | 0.7390 | 1,015,014.3 | 1,020,194.6 | 1,692.2 | 1.000x | 2.117x |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 1,017,211.2 | 0.7391 | 1,016,790.2 | 1,017,792.3 | 323.3 | 1.000x | 2.117x |
| 6 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,036,374.5 | 1.4796 | 2,035,108.2 | 2,045,770.6 | 3,993.6 | 2.002x | 4.238x |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 3,662,196.2 | 2.6610 | 3,660,645.4 | 3,681,104.8 | 8,159.3 | 3.601x | 7.622x |
| 8 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 3,664,695.9 | 2.6628 | 3,662,585.6 | 3,679,577.5 | 6,649.7 | 3.603x | 7.627x |

#### `utf8-lead-no-cont` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 334,475.0 | 0.3190 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 366,748.3 | 0.3498 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 366,945.1 | 0.3499 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 776,660.9 | 0.7407 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 777,018.6 | 0.7410 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,551,224.2 | 1.4794 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 2,790,003.6 | 2.6608 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 2,791,610.6 | 2.6623 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 114,760.0 | 0.4378 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 91,677.5 | 0.3497 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 90,642.5 | 0.3458 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 194,288.9 | 0.7412 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 194,401.7 | 0.7416 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 387,805.3 | 1.4794 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 697,347.4 | 2.6602 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 698,022.2 | 2.6627 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 30,747.9 | 0.4692 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 22,589.6 | 0.3447 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 22,607.0 | 0.3450 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 46,082.2 | 0.7032 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 46,100.1 | 0.7034 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 97,542.6 | 1.4884 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 175,032.8 | 2.6708 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 175,141.9 | 2.6725 |

### `utf8-lead-no-cont` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,252.2 | 1,250.2 | 1,264.4 | 5.2 | 0.362x | 1.000x | 75 | 16.7 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,253.5 | 1,247.2 | 1,256.7 | 3.1 | 0.362x | 1.001x | 75 | 16.7 | 8.9 | 100% |
| 3 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 3,120.5 | 3,109.4 | 3,816.6 | 276.2 | 0.902x | 2.492x | 75 | 41.6 | 30.4 | 100% |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,422.4 | 3,421.4 | 3,503.3 | 31.6 | 0.989x | 2.733x | 75 | 45.6 | 40.4 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,459.6 | 3,416.1 | 3,607.6 | 65.9 | 1.000x | 2.763x | 75 | 46.1 | 34.4 | 100% |
| 6 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,932.3 | 4,926.4 | 5,678.1 | 298.7 | 1.426x | 3.939x | 75 | 65.8 | 58.6 | 100% |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,946.2 | 4,939.7 | 4,947.0 | 3.0 | 1.430x | 3.950x | 75 | 65.9 | 18.0 | 100% |
| 8 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 5,029.8 | 5,022.0 | 5,034.4 | 4.4 | 1.454x | 4.017x | 75 | 67.1 | 17.3 | 100% |

### `uuid-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 18.1 | 0.0000 | 17.9 | 18.6 | 0.3 | 0.117x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 19.9 | 0.0000 | 19.9 | 20.9 | 0.4 | 0.129x | 1.101x |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 20.0 | 0.0000 | 19.8 | 20.0 | 0.1 | 0.129x | 1.104x |
| 4 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 30.3 | 0.0000 | 30.3 | 30.5 | 0.1 | 0.196x | 1.679x |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 92.9 | 0.0001 | 92.5 | 106.5 | 5.5 | 0.600x | 5.142x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 117.3 | 0.0001 | 116.5 | 123.1 | 2.4 | 0.758x | 6.490x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 154.7 | 0.0001 | 152.1 | 170.6 | 8.1 | 1.000x | 8.563x |
| 8 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 167.8 | 0.0001 | 167.3 | 174.6 | 2.8 | 1.084x | 9.283x |
| 9 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 296.4 | 0.0002 | 295.6 | 297.6 | 0.7 | 1.916x | 16.403x |
| 10 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 300.0 | 0.0002 | 297.2 | 301.8 | 1.8 | 1.938x | 16.599x |
| 11 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 2,889,532.1 | 2.0996 | 2,439,465.5 | 3,164,340.3 | 240,997.9 | 18672.653x | 159894.990x |
| 12 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 3,229,328.4 | 2.3465 | 3,225,979.2 | 3,246,849.9 | 9,037.6 | 20868.475x | 178697.941x |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 11,818,773.0 | 8.5876 | 11,801,817.3 | 12,165,588.1 | 138,902.9 | 76374.941x | 654002.980x |

#### `uuid-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 5.9 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 5.9 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 5.9 | 0.0000 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.1 | 0.0000 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 30.9 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 37.8 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 30.7 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 27.1 | 0.0000 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 88.4 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 87.6 | 0.0001 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 2,306,999.8 | 2.2001 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 2,478,483.6 | 2.3637 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 8,996,919.4 | 8.5801 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 6.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 6.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 6.0 | 0.0000 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.1 | 0.0000 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 31.0 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 38.5 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 30.7 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 27.0 | 0.0001 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 88.5 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 88.9 | 0.0003 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 464,764.3 | 1.7729 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 620,194.8 | 2.3659 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 2,262,264.4 | 8.6299 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 5.9 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 8.0 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 8.0 | 0.0001 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.1 | 0.0002 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 30.9 | 0.0005 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 41.3 | 0.0006 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 93.3 | 0.0014 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 113.7 | 0.0017 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 119.6 | 0.0018 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 122.4 | 0.0019 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 116,870.2 | 1.7833 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 143,162.5 | 2.1845 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 568,892.3 | 8.6806 |

### `uuid-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 563.2 | 560.1 | 575.0 | 5.3 | 0.199x | 1.000x | 75 | 7.5 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 564.0 | 561.2 | 564.9 | 1.5 | 0.199x | 1.002x | 75 | 7.5 | 8.9 | 100% |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 572.9 | 572.2 | 590.3 | 7.1 | 0.202x | 1.017x | 75 | 7.6 | 27.2 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 698.2 | 696.6 | 851.3 | 59.9 | 0.247x | 1.240x | 75 | 9.3 | 16.4 | 100% |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,795.9 | 2,789.1 | 2,832.6 | 18.3 | 0.988x | 4.965x | 75 | 37.3 | 58.6 | 100% |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,809.2 | 2,800.1 | 3,197.9 | 177.0 | 0.993x | 4.988x | 75 | 37.5 | 40.4 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,830.2 | 2,769.1 | 2,834.9 | 24.7 | 1.000x | 5.026x | 75 | 37.7 | 34.4 | 100% |
| 8 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 3,168.4 | 3,147.8 | 3,974.4 | 325.5 | 1.120x | 5.626x | 75 | 42.2 | 30.4 | 100% |
| 9 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 4,219.0 | 4,206.9 | 4,232.1 | 8.9 | 1.491x | 7.492x | 75 | 56.3 | 100.2 | 100% |
| 10 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 4,225.7 | 4,211.3 | 4,488.0 | 105.1 | 1.493x | 7.504x | 75 | 56.3 | 100.0 | 100% |
| 11 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,528.7 | 4,027.0 | 4,713.4 | 249.7 | 1.600x | 8.042x | 75 | 60.4 | 18.0 | 100% |
| 12 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,631.1 | 4,551.4 | 4,951.0 | 148.6 | 1.636x | 8.224x | 75 | 61.7 | 17.3 | 100% |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 35,438.8 | 35,347.3 | 35,547.4 | 68.3 | 12.522x | 62.929x | 75 | 472.5 | 27.9 | 100% |

### `wild-codegrammar-json-array-begin` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 124.1 | 0.0001 | 123.3 | 126.4 | 1.1 | 0.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 263,663.7 | 0.1916 | 263,500.5 | 264,338.5 | 292.0 | 0.310x | 2125.449x |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 263,680.6 | 0.1916 | 263,606.9 | 264,361.0 | 284.8 | 0.310x | 2125.585x |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 306,992.6 | 0.2231 | 306,470.0 | 307,772.4 | 473.8 | 0.361x | 2474.732x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 395,185.4 | 0.2871 | 391,923.5 | 415,245.6 | 8,387.9 | 0.464x | 3185.673x |
| 6 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 700,512.6 | 0.5090 | 699,859.4 | 702,019.4 | 716.7 | 0.823x | 5646.980x |
| 7 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 770,173.9 | 0.5596 | 764,904.0 | 793,611.2 | 10,324.2 | 0.905x | 6208.535x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 851,233.8 | 0.6185 | 832,894.7 | 859,398.3 | 9,423.7 | 1.000x | 6861.975x |
| 9 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 955,351.8 | 0.6942 | 954,604.2 | 959,820.2 | 1,862.1 | 1.122x | 7701.292x |
| 10 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 956,588.1 | 0.6951 | 955,180.5 | 959,580.2 | 1,525.9 | 1.124x | 7711.259x |
| 11 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 1,642,847.0 | 1.1937 | 1,638,657.9 | 1,677,721.6 | 16,213.1 | 1.930x | 13243.337x |
| 12 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 1,678,588.5 | 1.2197 | 1,676,557.8 | 1,734,706.8 | 23,283.9 | 1.972x | 13531.456x |
| 13 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,979,405.4 | 2.8915 | 3,961,213.6 | 4,016,038.8 | 18,735.5 | 4.675x | 32078.827x |

#### `wild-codegrammar-json-array-begin` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 43.5 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 202,585.8 | 0.1932 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 202,567.3 | 0.1932 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 236,106.7 | 0.2252 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 302,608.1 | 0.2886 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 536,571.4 | 0.5117 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 594,301.4 | 0.5668 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 651,279.8 | 0.6211 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 727,752.2 | 0.6940 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 728,165.0 | 0.6944 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,249,453.9 | 1.1916 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 1,278,705.9 | 1.2195 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 3,036,809.6 | 2.8961 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 40.7 | 0.0002 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 48,624.1 | 0.1855 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 48,705.7 | 0.1858 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 56,771.8 | 0.2166 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 73,504.6 | 0.2804 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 129,736.7 | 0.4949 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 140,223.4 | 0.5349 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 158,303.6 | 0.6039 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 181,349.4 | 0.6918 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 181,148.0 | 0.6910 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 303,013.6 | 1.1559 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 309,717.8 | 1.1815 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 749,430.8 | 2.8589 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 39.6 | 0.0006 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 12,519.9 | 0.1910 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 12,514.7 | 0.1910 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 14,090.2 | 0.2150 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 19,242.1 | 0.2936 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 34,144.6 | 0.5210 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 37,005.0 | 0.5647 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 42,170.1 | 0.6435 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 46,322.5 | 0.7068 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 46,730.7 | 0.7131 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 90,208.6 | 1.3765 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 91,062.7 | 1.3895 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 192,126.6 | 2.9316 |

### `wild-codegrammar-json-array-begin` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 687.8 | 682.8 | 709.5 | 11.7 | 0.244x | 1.000x | 75 | 9.2 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 709.5 | 691.4 | 710.7 | 7.3 | 0.252x | 1.032x | 75 | 9.5 | 8.9 | 100% |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 1,284.1 | 1,276.7 | 1,285.5 | 3.3 | 0.456x | 1.867x | 75 | 17.1 | 17.3 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,330.5 | 1,329.3 | 1,332.6 | 1.3 | 0.473x | 1.935x | 75 | 17.7 | 16.4 | 100% |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 1,335.2 | 1,330.3 | 1,338.9 | 3.2 | 0.474x | 1.941x | 75 | 17.8 | 18.0 | 100% |
| 6 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,070.7 | 2,070.2 | 2,074.0 | 1.4 | 0.736x | 3.011x | 75 | 27.6 | 27.2 | 100% |
| 7 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 2,189.5 | 2,187.1 | 2,191.4 | 1.6 | 0.778x | 3.183x | 75 | 29.2 | 27.9 | 100% |
| 8 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 2,396.7 | 2,394.1 | 2,427.1 | 13.5 | 0.851x | 3.485x | 75 | 32.0 | 30.4 | 100% |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,787.1 | 2,773.0 | 3,005.0 | 86.7 | 0.990x | 4.052x | 75 | 37.2 | 40.4 | 100% |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,815.2 | 2,742.1 | 2,921.6 | 69.6 | 1.000x | 4.093x | 75 | 37.5 | 34.4 | 100% |
| 11 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,651.9 | 4,644.8 | 4,670.4 | 10.2 | 1.652x | 6.764x | 75 | 62.0 | 58.6 | 100% |
| 12 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 7,717.5 | 7,679.0 | 7,852.1 | 63.2 | 2.741x | 11.221x | 75 | 102.9 | 100.2 | 100% |
| 13 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,733.9 | 7,724.4 | 7,973.7 | 96.7 | 2.747x | 11.245x | 75 | 103.1 | 100.0 | 100% |

### `wild-codegrammar-json-constant` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 182,488.3 | 0.1326 | 182,296.3 | 182,993.6 | 295.1 | 0.026x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 280,588.6 | 0.2039 | 280,476.1 | 281,656.0 | 434.5 | 0.039x | 1.538x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,983,449.3 | 1.4412 | 1,981,109.6 | 1,983,924.2 | 1,069.8 | 0.278x | 10.869x |
| 4 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,236,308.9 | 1.6249 | 2,233,007.0 | 2,244,237.8 | 4,044.7 | 0.314x | 12.255x |
| 5 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 2,238,720.3 | 1.6267 | 2,236,559.2 | 2,240,047.1 | 1,298.8 | 0.314x | 12.268x |
| 6 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 4,198,569.5 | 3.0507 | 4,197,651.1 | 4,207,395.4 | 3,643.9 | 0.589x | 23.007x |
| 7 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 4,199,248.0 | 3.0512 | 4,196,302.6 | 4,210,714.8 | 6,592.9 | 0.589x | 23.011x |
| 8 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,720,506.2 | 3.4300 | 4,706,058.8 | 4,722,961.6 | 6,926.7 | 0.662x | 25.867x |
| 9 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,720,698.7 | 3.4301 | 4,695,448.2 | 4,751,119.5 | 17,993.4 | 0.662x | 25.869x |
| 10 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 6,207,305.8 | 4.5103 | 6,190,032.8 | 6,216,321.1 | 8,544.6 | 0.871x | 34.015x |
| 11 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 6,560,019.1 | 4.7666 | 6,529,638.9 | 6,597,222.3 | 23,928.2 | 0.920x | 35.948x |
| 12 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 7,128,347.8 | 5.1795 | 7,083,949.5 | 7,164,913.2 | 28,873.7 | 1.000x | 39.062x |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 65,630,395.8 | 47.6876 | 64,850,068.0 | 66,804,147.6 | 643,650.1 | 9.207x | 359.642x |

#### `wild-codegrammar-json-constant` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 140,280.6 | 0.1338 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 213,652.7 | 0.2038 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 1,518,907.7 | 1.4485 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,695,063.0 | 1.6165 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 1,698,688.4 | 1.6200 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 3,199,314.0 | 3.0511 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 3,197,932.4 | 3.0498 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,588,196.6 | 3.4220 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,593,440.4 | 3.4270 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 4,703,205.7 | 4.4853 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 4,983,004.7 | 4.7522 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 5,392,917.9 | 5.1431 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 49,895,688.6 | 47.5842 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 33,759.6 | 0.1288 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 53,452.0 | 0.2039 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 375,627.1 | 1.4329 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 423,967.9 | 1.6173 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 424,008.1 | 1.6175 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 800,471.3 | 3.0536 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 799,939.0 | 3.0515 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 898,571.9 | 3.4278 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 899,147.2 | 3.4300 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,198,818.0 | 4.5731 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 1,257,637.8 | 4.7975 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 1,383,127.6 | 5.2762 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 12,558,671.6 | 47.9075 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 8,359.4 | 0.1276 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 13,472.8 | 0.2056 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 88,388.9 | 1.3487 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 116,091.0 | 1.7714 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 115,557.4 | 1.7633 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 198,790.6 | 3.0333 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 198,391.8 | 3.0272 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 228,792.2 | 3.4911 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 227,204.0 | 3.4669 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 305,282.0 | 4.6582 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 319,376.6 | 4.8733 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 354,463.7 | 5.4087 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 3,111,675.4 | 47.4804 |

### `wild-codegrammar-json-constant` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 2,449.5 | 2,446.5 | 2,452.6 | 2.1 | 0.320x | 1.000x | 75 | 32.7 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 2,455.1 | 2,447.8 | 2,461.6 | 4.4 | 0.320x | 1.002x | 75 | 32.7 | 8.9 | 100% |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,988.3 | 2,983.5 | 3,000.0 | 5.8 | 0.390x | 1.220x | 75 | 39.8 | 27.2 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 3,048.9 | 3,033.9 | 3,112.7 | 28.1 | 0.398x | 1.245x | 75 | 40.7 | 16.4 | 100% |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 3,369.9 | 3,359.6 | 3,380.5 | 7.3 | 0.440x | 1.376x | 75 | 44.9 | 17.3 | 100% |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,420.2 | 3,410.5 | 3,487.9 | 28.3 | 0.446x | 1.396x | 75 | 45.6 | 40.4 | 100% |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 3,423.3 | 3,403.5 | 3,435.2 | 11.6 | 0.447x | 1.398x | 75 | 45.6 | 18.0 | 100% |
| 8 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 7,078.3 | 7,063.5 | 7,539.3 | 185.5 | 0.924x | 2.890x | 75 | 94.4 | 30.4 | 100% |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 7,664.2 | 7,636.8 | 8,474.2 | 321.2 | 1.000x | 3.129x | 75 | 102.2 | 34.4 | 100% |
| 10 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,583.1 | 9,559.0 | 9,687.4 | 47.3 | 1.250x | 3.912x | 75 | 127.8 | 100.0 | 100% |
| 11 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 9,675.3 | 9,629.7 | 9,830.8 | 72.9 | 1.262x | 3.950x | 75 | 129.0 | 100.2 | 100% |
| 12 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 13,350.6 | 13,280.3 | 13,525.0 | 91.5 | 1.742x | 5.450x | 75 | 178.0 | 58.6 | 100% |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 64,048.8 | 63,695.4 | 64,260.0 | 185.8 | 8.357x | 26.148x | 75 | 854.0 | 27.9 | 100% |

### `wild-codegrammar-json-number-extended` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 2,447,718.4 | 1.7785 | 2,431,018.5 | 2,455,745.1 | 8,711.3 | 0.130x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 2,448,298.2 | 1.7790 | 2,442,734.0 | 2,464,325.5 | 7,408.6 | 0.130x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 4,476,937.3 | 3.2530 | 4,396,172.3 | 4,564,955.5 | 53,447.5 | 0.237x | 1.829x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 9,983,143.0 | 7.2538 | 9,914,478.3 | 10,064,414.7 | 48,892.0 | 0.529x | 4.079x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 10,090,150.2 | 7.3316 | 10,057,300.8 | 10,234,243.7 | 64,242.3 | 0.535x | 4.122x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 10,611,468.2 | 7.7104 | 10,601,434.4 | 10,651,336.3 | 17,923.9 | 0.563x | 4.335x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 18,862,675.2 | 13.7058 | 18,462,520.6 | 18,996,780.5 | 226,398.0 | 1.000x | 7.706x |
| 8 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 21,848,582.0 | 15.8754 | 21,824,088.1 | 21,916,181.7 | 31,431.8 | 1.158x | 8.926x |
| 9 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 23,494,350.5 | 17.0712 | 23,280,290.1 | 23,604,505.3 | 127,658.2 | 1.246x | 9.598x |

#### `wild-codegrammar-json-number-extended` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 1,876,020.6 | 1.7891 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,880,330.5 | 1.7932 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 3,428,091.4 | 3.2693 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 7,627,744.0 | 7.2744 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 7,680,831.7 | 7.3250 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 8,118,553.5 | 7.7425 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 14,472,591.7 | 13.8021 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 16,751,286.8 | 15.9753 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 17,976,793.7 | 17.1440 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 456,201.6 | 1.7403 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 456,675.6 | 1.7421 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 842,909.3 | 3.2154 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 1,880,538.2 | 7.1737 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 1,909,189.6 | 7.2830 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 1,998,307.4 | 7.6229 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 3,536,128.7 | 13.4893 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 4,109,805.8 | 15.6777 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 4,417,126.2 | 16.8500 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 113,029.5 | 1.7247 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 112,256.5 | 1.7129 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 204,260.2 | 3.1168 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 465,663.0 | 7.1055 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 483,228.9 | 7.3735 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 490,709.4 | 7.4876 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 853,954.9 | 13.0303 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 996,303.4 | 15.2024 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 1,067,112.0 | 16.2828 |

- not ranked: `vectorscan_5.4.11_block-nosom-nocaps-simd` — did-not-compile (hs_compile failed (code -4, expression 0): Unterminated comment.)

### `wild-codegrammar-json-number-extended` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,410.3 | 1,403.3 | 1,438.6 | 12.9 | 0.142x | 1.000x | 75 | 18.8 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,417.6 | 1,407.9 | 1,424.4 | 6.1 | 0.143x | 1.005x | 75 | 18.9 | 8.9 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,666.6 | 3,661.0 | 3,700.6 | 14.7 | 0.369x | 2.600x | 75 | 48.9 | 40.4 | 100% |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 7,345.4 | 7,319.8 | 7,546.8 | 83.6 | 0.739x | 5.208x | 75 | 97.9 | 18.0 | 100% |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 7,463.4 | 7,425.8 | 7,517.0 | 33.5 | 0.751x | 5.292x | 75 | 99.5 | 17.3 | 100% |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 9,943.9 | 9,912.4 | 10,194.8 | 106.3 | 1.000x | 7.051x | 75 | 132.6 | 34.4 | 100% |
| 7 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 11,633.3 | 11,631.3 | 11,648.1 | 6.1 | 1.170x | 8.249x | 75 | 155.1 | 16.4 | 100% |
| 8 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 11,694.2 | 11,660.0 | 11,771.9 | 39.3 | 1.176x | 8.292x | 75 | 155.9 | 58.6 | 100% |
| 9 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 12,446.2 | 12,376.3 | 12,921.7 | 217.8 | 1.252x | 8.825x | 75 | 165.9 | 30.4 | 100% |

- not ranked: `vectorscan_5.4.11_block-nosom-nocaps-simd` — did-not-compile (hs_compile failed (code -4, expression 0): Unterminated comment.)

### `wild-codegrammar-json-object-begin` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 23,090.6 | 0.0168 | 23,085.8 | 23,234.2 | 56.8 | 0.994x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 23,153.6 | 0.0168 | 23,106.6 | 23,177.4 | 27.1 | 0.997x | 1.003x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 23,229.7 | 0.0169 | 23,220.0 | 23,357.2 | 50.9 | 1.000x | 1.006x |
| 4 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 23,287.6 | 0.0169 | 23,256.4 | 23,306.2 | 17.2 | 1.002x | 1.009x |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 23,288.8 | 0.0169 | 23,228.5 | 24,324.8 | 417.4 | 1.003x | 1.009x |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 23,453.4 | 0.0170 | 23,444.4 | 23,486.2 | 16.3 | 1.010x | 1.016x |
| 7 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 23,769.9 | 0.0173 | 23,747.4 | 23,804.4 | 20.6 | 1.023x | 1.029x |
| 8 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 23,779.2 | 0.0173 | 23,741.0 | 23,921.2 | 64.8 | 1.024x | 1.030x |
| 9 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 32,309.3 | 0.0235 | 32,294.8 | 32,532.0 | 91.2 | 1.391x | 1.399x |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 51,850.2 | 0.0377 | 51,685.7 | 52,279.1 | 210.6 | 2.232x | 2.246x |
| 11 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 814,037.5 | 0.5915 | 813,952.9 | 817,912.6 | 1,542.0 | 35.043x | 35.254x |
| 12 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 814,843.1 | 0.5921 | 813,996.3 | 817,840.6 | 1,455.9 | 35.078x | 35.289x |
| 13 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,229,819.3 | 1.6202 | 2,228,441.8 | 2,234,492.3 | 2,111.8 | 95.990x | 96.568x |

#### `wild-codegrammar-json-object-begin` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 17,602.2 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 17,662.3 | 0.0168 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,690.4 | 0.0169 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 17,729.1 | 0.0169 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 17,697.5 | 0.0169 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 17,863.0 | 0.0170 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 17,775.7 | 0.0170 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 17,811.9 | 0.0170 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 24,503.7 | 0.0234 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,544.8 | 0.0377 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 620,160.6 | 0.5914 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 620,562.2 | 0.5918 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,698,260.2 | 1.6196 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 4,381.3 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 4,379.9 | 0.0167 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 4,411.8 | 0.0168 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 4,422.1 | 0.0169 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 4,425.7 | 0.0169 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 4,456.2 | 0.0170 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 4,539.8 | 0.0173 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 4,517.5 | 0.0172 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 6,134.5 | 0.0234 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 9,790.9 | 0.0373 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 154,921.6 | 0.5910 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 155,125.9 | 0.5918 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 424,781.5 | 1.6204 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,107.7 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 1,110.6 | 0.0169 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 1,130.9 | 0.0173 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,137.2 | 0.0174 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,139.0 | 0.0174 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 1,132.3 | 0.0173 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 1,452.5 | 0.0222 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 1,447.6 | 0.0221 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,672.2 | 0.0255 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 2,519.5 | 0.0384 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 38,911.9 | 0.5937 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 38,960.8 | 0.5945 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,412.0 | 1.6237 |

### `wild-codegrammar-json-object-begin` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 665.9 | 661.7 | 687.3 | 9.1 | 0.245x | 1.000x | 75 | 8.9 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 687.7 | 664.4 | 689.3 | 9.5 | 0.253x | 1.033x | 75 | 9.2 | 8.9 | 100% |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,226.8 | 1,225.0 | 1,227.3 | 0.9 | 0.451x | 1.842x | 75 | 16.4 | 16.4 | 100% |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 1,298.6 | 1,296.8 | 1,299.8 | 1.2 | 0.478x | 1.950x | 75 | 17.3 | 17.3 | 100% |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 1,354.7 | 1,353.5 | 1,358.6 | 1.9 | 0.499x | 2.034x | 75 | 18.1 | 18.0 | 100% |
| 6 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,041.4 | 2,038.9 | 2,042.3 | 1.4 | 0.751x | 3.066x | 75 | 27.2 | 27.2 | 100% |
| 7 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 2,092.7 | 2,092.1 | 2,097.8 | 2.1 | 0.770x | 3.143x | 75 | 27.9 | 27.9 | 100% |
| 8 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 2,290.0 | 2,256.0 | 3,162.6 | 360.4 | 0.843x | 3.439x | 75 | 30.5 | 30.4 | 100% |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,717.4 | 2,584.1 | 2,815.8 | 91.5 | 1.000x | 4.081x | 75 | 36.2 | 34.4 | 100% |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,999.4 | 2,744.8 | 3,352.7 | 206.5 | 1.104x | 4.504x | 75 | 40.0 | 40.4 | 100% |
| 11 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,397.9 | 4,392.6 | 4,978.2 | 232.0 | 1.618x | 6.605x | 75 | 58.6 | 58.6 | 100% |
| 12 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 7,537.7 | 7,511.6 | 7,601.8 | 34.2 | 2.774x | 11.320x | 75 | 100.5 | 100.2 | 100% |
| 13 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,539.0 | 7,498.0 | 7,757.7 | 97.0 | 2.774x | 11.322x | 75 | 100.5 | 100.0 | 100% |

### `wild-codegrammar-json-stringcontent-escape` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 23,123.6 | 0.0168 | 23,099.9 | 23,167.2 | 22.5 | 0.996x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 23,131.3 | 0.0168 | 23,116.8 | 23,147.4 | 10.3 | 0.996x | 1.000x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 23,214.4 | 0.0169 | 23,191.0 | 23,344.0 | 54.7 | 1.000x | 1.004x |
| 4 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 23,343.9 | 0.0170 | 23,295.3 | 23,445.5 | 52.5 | 1.006x | 1.010x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 23,643.5 | 0.0172 | 23,519.6 | 23,660.0 | 51.8 | 1.018x | 1.022x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 40,217.6 | 0.0292 | 40,037.7 | 40,315.2 | 104.4 | 1.732x | 1.739x |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,229,854.5 | 1.6202 | 2,228,571.0 | 2,231,481.9 | 1,163.2 | 96.055x | 96.432x |
| 8 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 3,917,363.5 | 2.8464 | 3,913,971.9 | 3,956,263.8 | 16,089.6 | 168.747x | 169.409x |
| 9 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 3,917,566.2 | 2.8465 | 3,916,127.1 | 3,934,736.5 | 7,372.6 | 168.756x | 169.418x |

#### `wild-codegrammar-json-stringcontent-escape` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 17,620.7 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 17,629.9 | 0.0168 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,659.1 | 0.0168 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 17,750.7 | 0.0169 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 17,954.3 | 0.0171 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 30,730.6 | 0.0293 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,698,142.7 | 1.6195 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 2,983,210.1 | 2.8450 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 2,984,237.2 | 2.8460 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 4,384.1 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 4,382.8 | 0.0167 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 4,420.4 | 0.0169 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 4,428.3 | 0.0169 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 4,501.1 | 0.0172 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 7,530.0 | 0.0287 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 424,827.6 | 1.6206 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 745,749.7 | 2.8448 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 746,713.4 | 2.8485 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 1,107.4 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,109.0 | 0.0169 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 1,138.4 | 0.0174 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,141.0 | 0.0174 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 1,171.4 | 0.0179 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 1,978.9 | 0.0302 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,776.7 | 1.6293 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 186,942.7 | 2.8525 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 187,212.9 | 2.8566 |

- not ranked: `vectorscan_5.4.11_block-nosom-nocaps-simd` — did-not-compile (hs_compile failed (code -4, expression 0): Unterminated comment.)

### `wild-codegrammar-json-stringcontent-escape` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 741.8 | 727.4 | 757.1 | 9.5 | 0.236x | 1.000x | 75 | 9.9 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 747.1 | 730.7 | 766.6 | 12.1 | 0.237x | 1.007x | 75 | 10.0 | 8.9 | 100% |
| 3 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 2,839.0 | 2,816.0 | 2,855.6 | 12.7 | 0.902x | 3.827x | 75 | 37.9 | 30.4 | 100% |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,845.8 | 2,780.9 | 3,353.3 | 231.7 | 0.904x | 3.836x | 75 | 37.9 | 40.4 | 100% |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,946.7 | 2,899.0 | 2,959.3 | 22.0 | 0.936x | 3.972x | 75 | 39.3 | 16.4 | 100% |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,147.0 | 3,088.8 | 3,325.4 | 85.6 | 1.000x | 4.242x | 75 | 42.0 | 34.4 | 100% |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,047.9 | 5,034.5 | 5,145.9 | 43.2 | 1.604x | 6.805x | 75 | 67.3 | 58.6 | 100% |
| 8 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 5,370.7 | 5,355.1 | 5,581.0 | 85.8 | 1.707x | 7.240x | 75 | 71.6 | 17.3 | 100% |
| 9 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 5,604.3 | 5,595.2 | 5,621.7 | 8.7 | 1.781x | 7.555x | 75 | 74.7 | 18.0 | 100% |

- not ranked: `vectorscan_5.4.11_block-nosom-nocaps-simd` — did-not-compile (hs_compile failed (code -4, expression 0): Unterminated comment.)

### `wild-datetime-datefinder-alternation` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 650.7 | 0.0005 | 649.3 | 651.3 | 0.7 | 0.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 10,424,041.4 | 7.5742 | 10,411,348.2 | 10,450,138.4 | 13,505.3 | 0.002x | 16019.059x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 35,097,768.8 | 25.5024 | 34,665,106.8 | 36,664,770.8 | 689,613.0 | 0.008x | 53936.203x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 259,150,804.0 | 188.3013 | 253,743,791.0 | 264,815,748.0 | 3,655,172.5 | 0.057x | 398247.832x |
| 5 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 909,418,994.0 | 660.7920 | 907,635,774.0 | 1,039,619,183.0 | 51,272,470.0 | 0.201x | 1397542.037x |
| 6 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 946,749,306.0 | 687.9166 | 905,452,639.0 | 1,002,090,124.0 | 35,544,164.5 | 0.210x | 1454909.082x |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,137,713,544.0 | 1553.2819 | 2,120,757,817.0 | 2,480,947,384.0 | 139,483,497.6 | 0.473x | 3285113.419x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,514,881,080.0 | 3280.5532 | 4,511,883,135.0 | 4,520,715,052.0 | 3,119,805.8 | 1.000x | 6938205.758x |
| 9 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 10,046,355,001.0 | 7299.7720 | 10,033,667,338.0 | 10,084,410,115.0 | 17,585,039.0 | 2.225x | 15438652.067x |

#### `wild-datetime-datefinder-alternation` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 208.7 | 0.0002 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 7,939,932.7 | 7.5721 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 24,494,716.0 | 23.3600 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 196,725,747.5 | 187.6123 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 692,210,197.0 | 660.1431 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 716,191,416.0 | 683.0134 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,629,609,806.0 | 1554.1170 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 3,432,521,569.0 | 3273.5077 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 7,642,894,838.0 | 7288.8325 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 213.8 | 0.0008 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,984,844.9 | 7.5716 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 7,496,170.5 | 28.5956 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 49,474,310.0 | 188.7295 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 172,709,917.0 | 658.8360 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 177,913,008.0 | 678.6843 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 406,240,412.0 | 1549.6842 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 863,848,207.0 | 3295.3194 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,920,216,335.0 | 7325.0440 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 228.2 | 0.0035 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 496,707.0 | 7.5791 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 3,104,509.5 | 47.3711 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 12,268,893.0 | 187.2085 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 45,741,747.0 | 697.9637 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 51,148,487.0 | 780.4640 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 102,213,140.0 | 1559.6487 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 217,769,561.0 | 3322.8998 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 483,867,260.0 | 7383.2285 |

- not ranked: `pcrec_25b1984f_auto-caps-simdna` — did-not-compile (pcrec: pattern too large: 670159 bytes of emitted code (limit 500000), which gcc cannot compile in reasonable time. A repeat's body is replicated and counts MULTIPLY through nesting -- lower a count, try --unroll=1, or raise --max-emit-code-bytes (pattern offset 0))
- not ranked: `pcrec_25b1984f_vm-caps-simdna` — did-not-compile (pcrec: pattern too large: 665107 bytes of emitted code (limit 500000), which gcc cannot compile in reasonable time. A repeat's body is replicated and counts MULTIPLY through nesting -- lower a count, try --unroll=1, or raise --max-emit-code-bytes (pattern offset 0))
- not ranked: `pcrec_25b1984f_vm-in-caps-simdna` — did-not-compile (pcrec: pattern too large: 665107 bytes of emitted code (limit 500000), which gcc cannot compile in reasonable time. A repeat's body is replicated and counts MULTIPLY through nesting -- lower a count, try --unroll=1, or raise --max-emit-code-bytes (pattern offset 0))
- not ranked: `tre_0.9.0_default-caps-simdna` — did-not-compile (tre_regncompb failed (code 11): Invalid character range)

### `wild-datetime-datefinder-alternation` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 2,010.0 | 1,999.8 | 2,011.4 | 5.4 | 0.001x | 1.000x | 75 | 26.8 | 8.9 | 100% |
| 2 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 3,749.2 | 3,745.1 | 3,858.0 | 43.1 | 0.002x | 1.865x | 75 | 50.0 | 27.2 | 100% |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 87,853.4 | 87,550.9 | 88,123.3 | 182.6 | 0.050x | 43.708x | 75 | 1,171.4 | 16.4 | 100% |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 88,206.3 | 86,270.0 | 88,708.9 | 937.6 | 0.050x | 43.883x | 75 | 1,176.1 | 40.4 | 100% |
| 5 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 181,558.9 | 180,952.8 | 184,663.4 | 1,326.8 | 0.104x | 90.327x | 75 | 2,420.8 | 100.2 | 100% |
| 6 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 183,049.2 | 182,072.6 | 185,479.3 | 1,169.2 | 0.105x | 91.068x | 75 | 2,440.7 | 100.0 | 100% |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 765,447.8 | 763,500.9 | 769,117.1 | 1,916.0 | 0.437x | 380.815x | 75 | 10,206.0 | 58.6 | 100% |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,750,980.9 | 1,750,262.0 | 1,751,305.2 | 375.5 | 1.000x | 871.123x | 75 | 23,346.4 | 34.4 | 100% |
| 9 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 3,958,526.1 | 3,909,930.7 | 4,013,833.0 | 36,965.7 | 2.261x | 1969.390x | 75 | 52,780.3 | 30.4 | 100% |

- not ranked: `pcrec_25b1984f_auto-caps-simdna` — did-not-compile (pcrec: pattern too large: 670159 bytes of emitted code (limit 500000), which gcc cannot compile in reasonable time. A repeat's body is replicated and counts MULTIPLY through nesting -- lower a count, try --unroll=1, or raise --max-emit-code-bytes (pattern offset 0))
- not ranked: `pcrec_25b1984f_vm-caps-simdna` — did-not-compile (pcrec: pattern too large: 665107 bytes of emitted code (limit 500000), which gcc cannot compile in reasonable time. A repeat's body is replicated and counts MULTIPLY through nesting -- lower a count, try --unroll=1, or raise --max-emit-code-bytes (pattern offset 0))
- not ranked: `pcrec_25b1984f_vm-in-caps-simdna` — did-not-compile (pcrec: pattern too large: 665107 bytes of emitted code (limit 500000), which gcc cannot compile in reasonable time. A repeat's body is replicated and counts MULTIPLY through nesting -- lower a count, try --unroll=1, or raise --max-emit-code-bytes (pattern offset 0))
- not ranked: `tre_0.9.0_default-caps-simdna` — did-not-compile (tre_regncompb failed (code 11): Invalid character range)

### `wild-datetime-moment-iso8601` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 19.6 | 0.0000 | 19.6 | 20.6 | 0.4 | 0.201x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 33.0 | 0.0000 | 32.9 | 33.4 | 0.2 | 0.338x | 1.684x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 97.7 | 0.0001 | 97.6 | 110.3 | 5.0 | 1.000x | 4.982x |
| 4 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 116.6 | 0.0001 | 81.5 | 126.6 | 19.2 | 1.192x | 5.941x |
| 5 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 148.4 | 0.0001 | 147.1 | 149.1 | 0.7 | 1.518x | 7.561x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 174.9 | 0.0001 | 151.7 | 175.3 | 9.3 | 1.789x | 8.912x |
| 7 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 284.2 | 0.0002 | 283.5 | 286.2 | 0.9 | 2.908x | 14.487x |
| 8 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 287.0 | 0.0002 | 282.9 | 287.7 | 1.8 | 2.936x | 14.628x |
| 9 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 298.8 | 0.0002 | 298.3 | 306.5 | 3.1 | 3.057x | 15.231x |
| 10 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 1,006.4 | 0.0007 | 977.1 | 1,011.4 | 15.1 | 10.297x | 51.296x |
| 11 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,273,884.7 | 3.1054 | 4,269,881.1 | 4,276,420.7 | 2,891.7 | 43724.906x | 217829.355x |
| 12 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,276,122.6 | 3.1071 | 4,267,427.6 | 4,301,327.5 | 12,339.3 | 43747.801x | 217943.414x |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 15,449,886.9 | 11.2260 | 15,371,742.6 | 16,080,823.3 | 269,784.2 | 158063.425x | 787442.604x |

#### `wild-datetime-moment-iso8601` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 6.5 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 11.0 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 32.5 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 37.9 | 0.0000 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 49.2 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 55.6 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 88.5 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 88.6 | 0.0001 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 40.8 | 0.0000 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 306.0 | 0.0003 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,252,931.5 | 3.1022 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,255,697.8 | 3.1049 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 11,745,622.6 | 11.2015 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 6.5 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 11.0 | 0.0000 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 32.6 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 37.5 | 0.0001 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 49.0 | 0.0002 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 63.1 | 0.0002 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 88.9 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 89.3 | 0.0003 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 126.1 | 0.0005 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 421.2 | 0.0016 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 813,963.5 | 3.1050 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 813,596.0 | 3.1036 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 2,951,209.5 | 11.2580 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 6.5 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 11.0 | 0.0002 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 32.6 | 0.0005 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 39.0 | 0.0006 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 49.7 | 0.0008 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 56.1 | 0.0009 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 106.9 | 0.0016 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 109.0 | 0.0017 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 132.2 | 0.0020 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 278.8 | 0.0043 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 204,141.3 | 3.1149 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 204,670.0 | 3.1230 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 745,620.3 | 11.3773 |

### `wild-datetime-moment-iso8601` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 589.8 | 588.6 | 590.2 | 0.6 | 0.167x | 1.000x | 75 | 7.9 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 982.3 | 980.3 | 983.5 | 1.3 | 0.278x | 1.665x | 75 | 13.1 | 8.9 | 100% |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,618.6 | 1,617.2 | 2,044.7 | 168.0 | 0.458x | 2.744x | 75 | 21.6 | 27.2 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,043.2 | 2,041.7 | 2,059.5 | 6.7 | 0.578x | 3.464x | 75 | 27.2 | 16.4 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,263.8 | 3,056.3 | 3,433.6 | 141.8 | 0.923x | 5.533x | 75 | 43.5 | 40.4 | 100% |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,535.6 | 3,524.6 | 3,536.8 | 4.6 | 1.000x | 5.994x | 75 | 47.1 | 34.4 | 100% |
| 7 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 3,795.1 | 3,727.7 | 4,492.0 | 283.9 | 1.073x | 6.434x | 75 | 50.6 | 30.4 | 100% |
| 8 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 6,322.7 | 6,317.9 | 6,332.8 | 5.5 | 1.788x | 10.719x | 75 | 84.3 | 18.0 | 100% |
| 9 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 6,808.1 | 6,805.3 | 6,810.8 | 1.8 | 1.926x | 11.542x | 75 | 90.8 | 17.3 | 100% |
| 10 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,725.1 | 9,667.1 | 9,953.8 | 101.4 | 2.751x | 16.487x | 75 | 129.7 | 100.0 | 100% |
| 11 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 9,737.3 | 9,714.3 | 9,793.3 | 28.8 | 2.754x | 16.508x | 75 | 129.8 | 100.2 | 100% |
| 12 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 11,656.5 | 11,611.5 | 11,871.9 | 92.7 | 3.297x | 19.762x | 75 | 155.4 | 58.6 | 100% |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 42,412.1 | 42,319.1 | 42,752.5 | 152.8 | 11.996x | 71.903x | 75 | 565.5 | 27.9 | 100% |

### `wild-logparse-base10num-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 4,024,029.9 | 2.9239 | 4,021,558.8 | 4,038,594.8 | 6,978.7 | 0.203x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 4,024,234.3 | 2.9240 | 4,021,173.2 | 4,056,836.8 | 13,550.7 | 0.203x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 4,760,420.5 | 3.4590 | 4,720,910.0 | 4,886,668.8 | 68,697.2 | 0.240x | 1.183x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 19,807,034.2 | 14.3920 | 19,698,062.2 | 19,870,715.9 | 66,274.9 | 1.000x | 4.922x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 23,354,179.3 | 16.9694 | 23,267,804.2 | 23,433,823.4 | 69,188.1 | 1.179x | 5.804x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 23,708,850.1 | 17.2271 | 23,646,918.8 | 23,740,294.8 | 34,439.9 | 1.197x | 5.892x |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 27,178,784.8 | 19.7483 | 27,101,937.3 | 27,960,581.0 | 351,977.7 | 1.372x | 6.754x |
| 8 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 27,306,139.6 | 19.8409 | 27,252,933.3 | 27,426,661.2 | 74,654.1 | 1.379x | 6.786x |

#### `wild-logparse-base10num-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 3,081,535.1 | 2.9388 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 3,084,065.4 | 2.9412 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 3,648,821.5 | 3.4798 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 15,176,917.7 | 14.4738 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 17,773,957.9 | 16.9506 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 18,031,764.4 | 17.1964 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 20,814,145.0 | 19.8499 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 20,893,195.4 | 19.9253 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 759,033.2 | 2.8955 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 758,305.2 | 2.8927 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 894,895.3 | 3.4138 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 3,723,503.6 | 14.2040 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 4,448,123.2 | 16.9682 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 4,517,501.5 | 17.2329 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 5,128,784.7 | 19.5648 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 5,129,382.9 | 19.5670 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 183,717.6 | 2.8033 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 183,272.4 | 2.7965 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 217,340.4 | 3.3164 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 901,062.9 | 13.7491 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 1,120,652.6 | 17.0998 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 1,137,001.4 | 17.3493 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 1,235,855.1 | 18.8577 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,241,249.0 | 18.9400 |

### `wild-logparse-base10num-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 2,506.9 | 2,502.9 | 2,574.9 | 28.2 | 0.210x | 1.000x | 75 | 33.4 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 2,515.7 | 2,502.0 | 2,621.4 | 44.4 | 0.211x | 1.004x | 75 | 33.5 | 8.9 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 4,247.8 | 4,077.9 | 4,515.1 | 167.5 | 0.356x | 1.694x | 75 | 56.6 | 40.4 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 11,930.4 | 11,917.0 | 12,007.9 | 34.5 | 1.000x | 4.759x | 75 | 159.1 | 34.4 | 100% |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 15,893.4 | 15,772.3 | 16,188.7 | 147.3 | 1.332x | 6.340x | 75 | 211.9 | 58.6 | 100% |
| 6 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 16,435.0 | 16,285.1 | 16,519.2 | 89.5 | 1.378x | 6.556x | 75 | 219.1 | 30.4 | 100% |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 18,299.0 | 18,240.8 | 18,322.3 | 27.6 | 1.534x | 7.300x | 75 | 244.0 | 18.0 | 100% |
| 8 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 18,639.7 | 18,622.8 | 18,703.9 | 29.1 | 1.562x | 7.435x | 75 | 248.5 | 17.3 | 100% |

### `wild-logparse-base10num-noatomic` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 3,983,529.8 | 2.8945 | 3,981,657.6 | 3,996,046.9 | 5,225.8 | 0.193x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 3,983,606.8 | 2.8945 | 3,981,462.4 | 4,721,221.2 | 293,593.0 | 0.193x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 4,787,801.8 | 3.4789 | 4,715,663.1 | 4,883,608.9 | 55,695.9 | 0.232x | 1.202x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 20,669,190.5 | 15.0184 | 20,463,615.0 | 21,383,631.7 | 332,619.1 | 1.000x | 5.189x |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 22,242,282.8 | 16.1614 | 22,214,077.9 | 22,310,617.0 | 36,478.5 | 1.076x | 5.584x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 23,230,085.7 | 16.8792 | 23,155,114.4 | 23,309,899.0 | 53,835.2 | 1.124x | 5.832x |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 23,430,513.0 | 17.0248 | 23,316,424.2 | 23,735,365.7 | 140,321.1 | 1.134x | 5.882x |
| 8 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 25,776,438.6 | 18.7294 | 25,756,114.0 | 26,331,673.2 | 219,154.1 | 1.247x | 6.471x |

#### `wild-logparse-base10num-noatomic` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 3,052,186.4 | 2.9108 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 3,052,076.4 | 2.9107 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 3,665,928.1 | 3.4961 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 15,838,258.2 | 15.1045 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 17,044,377.4 | 16.2548 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 17,695,282.0 | 16.8755 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 17,853,896.9 | 17.0268 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 19,738,679.8 | 18.8243 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 749,645.6 | 2.8597 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 751,131.7 | 2.8653 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 903,839.4 | 3.4479 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 3,890,962.5 | 14.8428 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 4,187,288.9 | 15.9732 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 4,397,430.1 | 16.7749 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 4,445,519.4 | 16.9583 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 4,865,464.7 | 18.5603 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 182,407.4 | 2.7833 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 181,799.8 | 2.7740 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 221,484.2 | 3.3796 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 939,969.8 | 14.3428 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,012,041.1 | 15.4425 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 1,117,089.0 | 17.0454 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 1,131,096.7 | 17.2592 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 1,176,568.6 | 17.9530 |

### `wild-logparse-base10num-noatomic` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 2,474.9 | 2,473.0 | 2,651.2 | 72.1 | 0.203x | 1.000x | 75 | 33.0 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 2,499.1 | 2,481.1 | 2,600.1 | 49.8 | 0.205x | 1.010x | 75 | 33.3 | 8.9 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 4,146.7 | 4,078.2 | 4,580.9 | 179.4 | 0.340x | 1.676x | 75 | 55.3 | 40.4 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 12,206.1 | 12,141.1 | 12,217.6 | 29.0 | 1.000x | 4.932x | 75 | 162.7 | 34.4 | 100% |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 13,874.3 | 13,741.8 | 14,189.2 | 151.7 | 1.137x | 5.606x | 75 | 185.0 | 30.4 | 100% |
| 6 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 15,951.5 | 15,869.6 | 16,015.9 | 51.1 | 1.307x | 6.445x | 75 | 212.7 | 58.6 | 100% |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 18,043.1 | 17,826.1 | 18,193.3 | 120.3 | 1.478x | 7.290x | 75 | 240.6 | 17.3 | 100% |
| 8 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 18,188.0 | 17,930.6 | 18,341.6 | 145.4 | 1.490x | 7.349x | 75 | 242.5 | 18.0 | 100% |

### `wild-logparse-quotedstring-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,008,829.4 | 0.7330 | 1,008,125.3 | 1,011,599.9 | 1,233.3 | 0.487x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,008,866.5 | 0.7331 | 1,008,134.0 | 1,010,387.8 | 806.8 | 0.487x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,449,818.5 | 1.0535 | 1,446,924.9 | 1,454,534.3 | 2,571.3 | 0.700x | 1.437x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,071,041.1 | 1.5048 | 2,061,918.5 | 2,090,422.0 | 9,725.1 | 1.000x | 2.053x |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,461,960.6 | 2.5155 | 3,446,127.4 | 3,504,453.5 | 20,710.8 | 1.672x | 3.432x |
| 6 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 3,853,300.1 | 2.7998 | 3,841,783.2 | 4,903,298.0 | 420,748.5 | 1.861x | 3.820x |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 46,643,445.8 | 33.8915 | 46,623,642.5 | 49,862,970.2 | 1,290,466.1 | 22.522x | 46.235x |
| 8 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 46,757,543.8 | 33.9745 | 46,568,071.0 | 46,882,926.3 | 121,031.0 | 22.577x | 46.348x |

#### `wild-logparse-quotedstring-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 772,470.6 | 0.7367 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 772,438.6 | 0.7367 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 1,106,018.4 | 1.0548 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 1,585,961.1 | 1.5125 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 2,646,841.7 | 2.5242 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 2,953,625.2 | 2.8168 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 35,522,007.7 | 33.8764 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 35,557,285.2 | 33.9101 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 188,440.1 | 0.7188 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 188,458.4 | 0.7189 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 274,750.9 | 1.0481 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 387,079.3 | 1.4766 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 651,344.4 | 2.4847 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 718,614.9 | 2.7413 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 8,897,394.8 | 33.9409 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 8,902,880.7 | 33.9618 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 47,617.5 | 0.7266 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 47,698.7 | 0.7278 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 69,072.9 | 1.0540 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 98,000.6 | 1.4954 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 163,774.5 | 2.4990 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 181,060.0 | 2.7628 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 2,229,113.5 | 34.0136 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 2,233,229.3 | 34.0764 |

### `wild-logparse-quotedstring-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,962.8 | 1,960.8 | 1,964.7 | 1.3 | 0.397x | 1.000x | 75 | 26.2 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,963.2 | 1,956.9 | 1,966.6 | 3.6 | 0.398x | 1.000x | 75 | 26.2 | 8.9 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 4,185.1 | 4,093.4 | 4,418.8 | 109.0 | 0.847x | 2.132x | 75 | 55.8 | 40.4 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,938.3 | 4,890.4 | 4,940.9 | 19.2 | 1.000x | 2.516x | 75 | 65.8 | 34.4 | 100% |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 6,263.0 | 6,260.9 | 6,298.7 | 14.1 | 1.268x | 3.191x | 75 | 83.5 | 58.6 | 100% |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 48,950.1 | 48,937.7 | 49,016.7 | 33.1 | 9.912x | 24.939x | 75 | 652.7 | 18.0 | 100% |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 49,176.8 | 49,139.0 | 55,671.4 | 2,590.4 | 9.958x | 25.055x | 75 | 655.7 | 17.3 | 100% |

### `wild-logparse-quotedstring-noatomic` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 929,842.8 | 0.6756 | 928,353.9 | 937,131.7 | 3,115.0 | 0.440x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 930,343.8 | 0.6760 | 928,572.0 | 935,326.2 | 2,456.6 | 0.441x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,442,083.7 | 1.0478 | 1,441,378.5 | 1,448,881.2 | 3,525.7 | 0.683x | 1.551x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,111,987.7 | 1.5346 | 2,104,629.4 | 2,132,996.9 | 10,474.1 | 1.000x | 2.271x |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,273,987.7 | 2.3789 | 3,251,490.0 | 3,319,012.3 | 27,398.1 | 1.550x | 3.521x |
| 6 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 8,795,923.3 | 6.3912 | 8,750,426.3 | 8,851,875.6 | 32,363.8 | 4.165x | 9.460x |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 22,956,306.8 | 16.6803 | 22,882,412.9 | 23,054,076.6 | 58,170.7 | 10.870x | 24.688x |
| 8 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 23,071,812.3 | 16.7642 | 23,026,909.5 | 23,144,289.4 | 41,384.5 | 10.924x | 24.813x |

#### `wild-logparse-quotedstring-noatomic` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 711,414.1 | 0.6785 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 711,412.1 | 0.6785 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 1,099,749.4 | 1.0488 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 1,619,412.0 | 1.5444 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 2,503,123.8 | 2.3872 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 6,762,335.8 | 6.4491 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 17,485,445.8 | 16.6754 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 17,567,670.2 | 16.7538 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 174,377.0 | 0.6652 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 174,207.8 | 0.6645 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 273,600.3 | 1.0437 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 394,629.6 | 1.5054 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 616,205.0 | 2.3506 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,620,181.0 | 6.1805 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 4,362,525.5 | 16.6417 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 4,390,347.9 | 16.7478 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 44,136.7 | 0.6735 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 44,074.4 | 0.6725 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 68,700.2 | 1.0483 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 99,248.9 | 1.5144 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 154,658.9 | 2.3599 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 415,827.8 | 6.3450 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 1,107,037.9 | 16.8921 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 1,102,404.9 | 16.8214 |

### `wild-logparse-quotedstring-noatomic` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | set composition | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,855.0 | 1,817.4 | 1,863.9 | 16.5 | 0.002x | 1.000x | spread | 75 | 24.7 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,857.6 | 1,853.8 | 1,866.6 | 4.5 | 0.002x | 1.001x | spread | 75 | 24.8 | 8.9 | 100% |
| 3 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 14,952.3 | 14,723.6 | 15,350.1 | 220.4 | 0.014x | 8.060x | spread | 75 | 199.4 | 30.4 | 100% |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 104,871.2 | 104,816.5 | 104,887.4 | 26.7 | 0.100x | 56.533x | **dominated**: `waf-sleep` is 96.0% of this set | 75 | 1,398.3 | 40.4 | 100% |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 114,353.1 | 114,130.1 | 114,445.3 | 105.2 | 0.109x | 61.644x | spread | 75 | 1,524.7 | 18.0 | 100% |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 114,498.2 | 114,330.8 | 129,285.7 | 5,880.6 | 0.110x | 61.723x | spread | 75 | 1,526.6 | 17.3 | 100% |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 290,745.7 | 290,281.8 | 291,145.7 | 305.9 | 0.278x | 156.732x | **dominated**: `waf-sleep` is 98.1% of this set | 75 | 3,876.6 | 58.6 | 100% |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,045,384.5 | 1,037,774.2 | 1,107,117.1 | 25,649.9 | 1.000x | 563.536x | **dominated**: `waf-sleep` is 99.6% of this set | 75 | 13,938.5 | 34.4 | 100% |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; `--grain subject` carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

_per-subject rows: 75 subjects — too many to enumerate here (the cap is 24); `--grain subject` renders them._

### `wild-logparse-syslogbase-expanded` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 3,988,287.3 | 2.8979 | 3,986,758.3 | 3,995,596.5 | 3,127.4 | 0.054x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 3,992,451.0 | 2.9010 | 3,988,217.4 | 4,004,179.9 | 6,126.2 | 0.054x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 6,319,504.7 | 4.5918 | 6,307,496.2 | 6,328,377.8 | 7,660.1 | 0.086x | 1.585x |
| 4 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 30,190,616.4 | 21.9368 | 30,086,109.2 | 30,583,026.4 | 177,326.5 | 0.410x | 7.570x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 41,269,811.0 | 29.9870 | 41,220,910.7 | 41,411,013.4 | 65,264.6 | 0.560x | 10.348x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 41,303,234.4 | 30.0113 | 41,090,456.0 | 41,381,590.6 | 108,588.6 | 0.561x | 10.356x |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 69,561,405.2 | 50.5439 | 69,299,673.5 | 69,819,311.8 | 176,101.9 | 0.944x | 17.441x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 73,681,100.2 | 53.5374 | 73,571,742.2 | 74,819,146.2 | 469,548.0 | 1.000x | 18.474x |

#### `wild-logparse-syslogbase-expanded` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 3,037,021.6 | 2.8963 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 3,038,418.6 | 2.8977 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 4,802,529.0 | 4.5800 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 22,912,127.7 | 21.8507 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 31,490,552.4 | 30.0317 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 31,494,045.7 | 30.0351 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 52,934,450.8 | 50.4822 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 56,068,438.8 | 53.4710 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 761,065.4 | 2.9032 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 761,395.5 | 2.9045 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 1,209,442.4 | 4.6137 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 5,756,851.2 | 21.9606 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 7,825,057.4 | 29.8502 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 7,868,845.6 | 30.0173 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 13,301,012.5 | 50.7393 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 13,979,687.5 | 53.3283 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 190,126.0 | 2.9011 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 190,803.4 | 2.9114 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 305,205.9 | 4.6571 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,499,558.4 | 22.8814 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 1,952,782.6 | 29.7971 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 1,950,386.0 | 29.7605 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 3,325,942.0 | 50.7498 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 3,654,289.0 | 55.7600 |

### `wild-logparse-syslogbase-expanded` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 3,583.6 | 3,564.6 | 3,605.3 | 14.3 | 0.392x | 1.000x | 75 | 47.8 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 3,769.0 | 3,752.9 | 3,838.1 | 32.3 | 0.413x | 1.052x | 75 | 50.3 | 8.9 | 100% |
| 3 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 7,132.3 | 7,079.6 | 7,770.8 | 263.8 | 0.781x | 1.990x | 75 | 95.1 | 30.4 | 100% |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 8,929.1 | 8,853.9 | 8,995.1 | 47.0 | 0.978x | 2.492x | 75 | 119.1 | 40.4 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 9,134.2 | 9,114.4 | 9,150.9 | 13.1 | 1.000x | 2.549x | 75 | 121.8 | 34.4 | 100% |
| 6 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 23,531.8 | 23,414.9 | 29,466.6 | 2,388.1 | 2.576x | 6.566x | 75 | 313.8 | 58.6 | 100% |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 40,018.4 | 39,957.2 | 40,310.3 | 145.8 | 4.381x | 11.167x | 75 | 533.6 | 18.0 | 100% |
| 8 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 40,937.3 | 40,884.6 | 53,878.3 | 5,182.8 | 4.482x | 11.423x | 75 | 545.8 | 17.3 | 100% |

### `wild-logparse-winpath-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 23,249.3 | 0.0169 | 23,242.5 | 23,277.4 | 13.2 | 1.000x | 1.000x | spread |
| 2 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 23,338.3 | 0.0170 | 23,288.1 | 23,524.8 | 81.2 | 1.004x | 1.004x | spread |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,227,676.0 | 1.6186 | 2,226,582.6 | 2,229,305.0 | 889.6 | 95.817x | 95.817x | spread |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,947,563.9 | 2.1417 | 2,945,603.9 | 2,949,678.6 | 1,466.2 | 126.781x | 126.781x | **dominated**: `t-1m` is 99.6% of this set |
| 5 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 3,468,809.9 | 2.5205 | 3,467,171.2 | 3,504,628.6 | 14,437.9 | 149.201x | 149.201x | spread |
| 6 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 3,470,267.5 | 2.5215 | 3,466,369.0 | 3,479,444.7 | 5,517.9 | 149.263x | 149.263x | spread |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 19,295,579.4 | 14.0203 | 18,971,149.9 | 19,641,629.6 | 274,718.8 | 829.943x | 829.943x | spread |
| 8 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 20,348,075.4 | 14.7851 | 20,227,506.8 | 23,113,051.9 | 1,108,068.4 | 875.213x | 875.213x | spread |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `wild-logparse-winpath-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,695.1 | 0.0169 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 17,764.4 | 0.0169 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,697,061.3 | 1.6184 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 2,935,205.7 | 2.7992 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 2,643,693.8 | 2.5212 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 2,643,406.7 | 2.5209 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 14,951,860.8 | 14.2592 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 15,646,137.9 | 14.9213 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 4,425.1 | 0.0169 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 4,438.3 | 0.0169 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 423,987.4 | 1.6174 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 9,768.6 | 0.0373 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 659,703.2 | 2.5166 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 662,610.4 | 2.5277 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 3,520,380.6 | 13.4292 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,833,293.0 | 14.6229 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 1,139.0 | 0.0174 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,139.4 | 0.0174 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,228.4 | 1.6209 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 2,586.2 | 0.0395 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 164,883.0 | 2.5159 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 165,756.3 | 2.5292 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 871,140.9 | 13.2926 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 908,336.9 | 13.8601 |

### `wild-logparse-winpath-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 2,643.9 | 2,642.2 | 2,660.8 | 7.0 | 0.663x | 1.000x | 75 | 35.3 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 2,644.9 | 2,634.1 | 2,647.2 | 4.6 | 0.663x | 1.000x | 75 | 35.3 | 8.9 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,303.3 | 3,134.5 | 3,814.9 | 241.3 | 0.828x | 1.249x | 75 | 44.0 | 40.4 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,989.5 | 3,966.6 | 4,024.6 | 22.8 | 1.000x | 1.509x | 75 | 53.2 | 34.4 | 100% |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,334.2 | 5,319.0 | 5,343.5 | 9.4 | 1.337x | 2.018x | 75 | 71.1 | 58.6 | 100% |
| 6 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 5,810.4 | 5,739.5 | 6,445.4 | 262.6 | 1.456x | 2.198x | 75 | 77.5 | 30.4 | 100% |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 23,152.1 | 22,953.6 | 23,672.4 | 305.1 | 5.803x | 8.757x | 75 | 308.7 | 18.0 | 100% |
| 8 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 23,753.8 | 23,690.4 | 23,767.4 | 31.6 | 5.954x | 8.984x | 75 | 316.7 | 17.3 | 100% |

### `wild-secrets-aws-access-key-id` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 91,325.3 | 0.0664 | 91,282.2 | 91,632.8 | 156.5 | 0.419x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 135,249.6 | 0.0983 | 135,203.9 | 136,100.1 | 337.3 | 0.621x | 1.481x |
| 3 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 211,881.9 | 0.1540 | 207,439.4 | 212,102.6 | 2,179.1 | 0.972x | 2.320x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 217,909.0 | 0.1583 | 216,134.1 | 220,853.1 | 1,573.5 | 1.000x | 2.386x |
| 5 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 292,497.5 | 0.2125 | 292,378.8 | 293,479.4 | 401.4 | 1.342x | 3.203x |
| 6 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,170,961.4 | 1.5774 | 2,169,820.1 | 2,179,610.4 | 3,548.2 | 9.963x | 23.772x |
| 7 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,238,687.1 | 1.6267 | 2,236,183.7 | 2,248,860.0 | 4,513.5 | 10.273x | 24.513x |
| 8 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 2,243,681.0 | 1.6303 | 2,238,273.5 | 2,245,637.6 | 2,513.3 | 10.296x | 24.568x |
| 9 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 4,010,040.2 | 2.9137 | 4,008,097.6 | 4,022,793.8 | 5,262.5 | 18.402x | 43.909x |
| 10 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 4,201,042.8 | 3.0525 | 4,198,379.4 | 4,218,221.1 | 7,383.6 | 19.279x | 46.001x |
| 11 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 9,348,625.8 | 6.7928 | 9,337,276.8 | 9,560,717.4 | 85,916.9 | 42.902x | 102.366x |
| 12 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 9,371,580.2 | 6.8095 | 9,344,390.5 | 9,494,877.5 | 68,003.9 | 43.007x | 102.618x |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 173,226,369.0 | 125.8678 | 171,118,674.0 | 178,723,876.5 | 2,931,049.9 | 794.948x | 1896.806x |

#### `wild-secrets-aws-access-key-id` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 69,790.6 | 0.0666 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 104,901.4 | 0.1000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 162,635.9 | 0.1551 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 167,640.1 | 0.1599 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 223,208.2 | 0.2129 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,654,190.0 | 1.5776 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,697,341.3 | 1.6187 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 1,702,109.9 | 1.6233 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 3,053,571.2 | 2.9121 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 3,199,570.3 | 3.0513 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 7,135,811.6 | 6.8052 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 7,153,951.0 | 6.8225 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 131,533,949.5 | 125.4405 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 17,165.0 | 0.0655 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 25,024.4 | 0.0955 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 39,253.1 | 0.1497 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 39,923.0 | 0.1523 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55,294.8 | 0.2109 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 413,350.2 | 1.5768 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 425,708.1 | 1.6239 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 424,936.4 | 1.6210 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 765,917.3 | 2.9217 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 801,393.1 | 3.0571 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 1,777,411.8 | 6.7803 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 1,778,533.2 | 6.7846 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 33,634,450.0 | 128.3052 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 4,377.4 | 0.0668 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 5,385.9 | 0.0822 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 9,852.1 | 0.1503 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 10,337.5 | 0.1577 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 14,002.4 | 0.2137 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 103,737.3 | 1.5829 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 116,455.6 | 1.7770 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 116,584.6 | 1.7789 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 190,576.6 | 2.9080 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 198,254.3 | 3.0251 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 441,373.5 | 6.7348 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 444,459.7 | 6.7819 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 8,363,821.0 | 127.6218 |

### `wild-secrets-aws-access-key-id` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,105.2 | 2,103.4 | 2,110.5 | 2.5 | 0.463x | 1.000x | 75 | 28.1 | 27.2 | 100% |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,143.1 | 2,134.7 | 2,159.6 | 8.8 | 0.471x | 1.018x | 75 | 28.6 | 16.4 | 100% |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 2,468.3 | 2,467.0 | 2,470.7 | 1.2 | 0.543x | 1.173x | 75 | 32.9 | 8.9 | 100% |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 2,731.3 | 2,726.1 | 2,741.7 | 6.0 | 0.600x | 1.297x | 75 | 36.4 | 8.9 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,507.2 | 3,300.7 | 3,811.8 | 163.7 | 0.771x | 1.666x | 75 | 46.8 | 40.4 | 100% |
| 6 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 4,262.7 | 4,240.7 | 4,289.8 | 18.0 | 0.937x | 2.025x | 75 | 56.8 | 30.4 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,549.6 | 4,512.2 | 4,723.9 | 78.8 | 1.000x | 2.161x | 75 | 60.7 | 34.4 | 100% |
| 8 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 7,520.6 | 7,471.6 | 7,646.6 | 60.5 | 1.653x | 3.572x | 75 | 100.3 | 58.6 | 100% |
| 9 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 7,745.1 | 7,704.8 | 7,771.6 | 22.4 | 1.702x | 3.679x | 75 | 103.3 | 18.0 | 100% |
| 10 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 7,880.3 | 7,831.4 | 7,898.8 | 23.7 | 1.732x | 3.743x | 75 | 105.1 | 17.3 | 100% |
| 11 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,902.8 | 9,868.0 | 9,943.5 | 25.1 | 2.177x | 4.704x | 75 | 132.0 | 100.0 | 100% |
| 12 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 9,973.3 | 9,874.5 | 10,122.7 | 80.9 | 2.192x | 4.738x | 75 | 133.0 | 100.2 | 100% |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 174,869.9 | 173,420.5 | 177,029.0 | 1,329.1 | 38.436x | 83.068x | 75 | 2,331.6 | 27.9 | 100% |

### `wild-secrets-github-pat` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 46,777.4 | 0.0340 | 46,713.8 | 46,845.5 | 53.7 | 0.043x | 1.000x |
| 2 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 60,270.7 | 0.0438 | 60,264.5 | 60,280.9 | 5.6 | 0.056x | 1.288x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 98,609.1 | 0.0717 | 97,923.4 | 98,734.9 | 291.8 | 0.092x | 2.108x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 124,368.4 | 0.0904 | 124,119.9 | 124,831.0 | 237.1 | 0.115x | 2.659x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 124,479.8 | 0.0904 | 124,361.7 | 124,825.7 | 167.2 | 0.116x | 2.661x |
| 6 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 414,437.2 | 0.3011 | 414,185.1 | 414,945.7 | 275.2 | 0.385x | 8.860x |
| 7 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 1,043,729.0 | 0.7584 | 1,043,165.9 | 1,053,385.5 | 3,888.9 | 0.969x | 22.313x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,077,130.4 | 0.7827 | 1,076,043.9 | 1,081,354.1 | 1,997.5 | 1.000x | 23.027x |
| 9 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 2,240,455.1 | 1.6279 | 2,238,769.5 | 2,242,236.5 | 1,165.9 | 2.080x | 47.896x |
| 10 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,242,637.4 | 1.6295 | 2,239,616.6 | 2,246,612.1 | 2,319.0 | 2.082x | 47.943x |
| 11 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,774,557.6 | 3.4692 | 4,762,058.6 | 4,805,205.8 | 16,164.8 | 4.433x | 102.070x |
| 12 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 5,236,015.9 | 3.8045 | 5,223,715.4 | 5,289,949.2 | 23,621.5 | 4.861x | 111.935x |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 25,071,017.5 | 18.2168 | 24,963,976.9 | 25,119,971.4 | 69,434.8 | 23.276x | 535.965x |

#### `wild-secrets-github-pat` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 35,503.8 | 0.0339 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 45,842.4 | 0.0437 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 73,034.4 | 0.0697 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 102,356.3 | 0.0976 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 102,484.4 | 0.0977 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 315,240.3 | 0.3006 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 797,833.9 | 0.7609 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 822,176.7 | 0.7841 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 1,699,242.0 | 1.6205 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,699,777.5 | 1.6210 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,637,810.7 | 3.4693 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,986,523.4 | 3.8018 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 19,113,100.1 | 18.2277 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 8,964.6 | 0.0342 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 11,477.6 | 0.0438 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 20,337.2 | 0.0776 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 18,620.9 | 0.0710 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 18,572.9 | 0.0709 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 79,025.4 | 0.3015 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 196,153.9 | 0.7483 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 202,864.3 | 0.7739 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 423,936.9 | 1.6172 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 425,549.6 | 1.6233 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 910,028.0 | 3.4715 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 994,193.0 | 3.7925 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 4,767,293.4 | 18.1858 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 2,283.3 | 0.0348 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 2,955.1 | 0.0451 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 5,237.5 | 0.0799 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 3,364.8 | 0.0513 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 3,366.3 | 0.0514 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 19,967.9 | 0.3047 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 50,201.8 | 0.7660 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 51,696.2 | 0.7888 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 116,305.6 | 1.7747 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 117,200.9 | 1.7883 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 226,190.9 | 3.4514 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 249,536.4 | 3.8076 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,193,589.5 | 18.2127 |

### `wild-secrets-github-pat` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 827.4 | 826.6 | 1,019.6 | 76.7 | 0.276x | 1.000x | 75 | 11.0 | 27.2 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,371.6 | 1,367.9 | 1,372.4 | 1.7 | 0.457x | 1.658x | 75 | 18.3 | 8.9 | 100% |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,683.7 | 1,679.8 | 1,688.7 | 3.7 | 0.561x | 2.035x | 75 | 22.4 | 16.4 | 100% |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,701.6 | 1,698.2 | 1,713.2 | 5.4 | 0.567x | 2.057x | 75 | 22.7 | 8.9 | 100% |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,946.8 | 2,944.2 | 3,126.5 | 70.6 | 0.982x | 3.561x | 75 | 39.3 | 58.6 | 100% |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,999.4 | 2,915.2 | 3,155.7 | 91.4 | 1.000x | 3.625x | 75 | 40.0 | 34.4 | 100% |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,111.6 | 3,082.9 | 3,389.4 | 114.9 | 1.037x | 3.761x | 75 | 41.5 | 40.4 | 100% |
| 8 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 3,145.9 | 3,142.1 | 3,153.9 | 4.7 | 1.049x | 3.802x | 75 | 41.9 | 18.0 | 100% |
| 9 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 3,377.2 | 3,364.8 | 3,401.1 | 12.8 | 1.126x | 4.082x | 75 | 45.0 | 30.4 | 100% |
| 10 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 3,639.1 | 3,628.4 | 3,648.9 | 6.5 | 1.213x | 4.398x | 75 | 48.5 | 17.3 | 100% |
| 11 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 10,219.9 | 10,125.4 | 10,368.2 | 79.0 | 3.407x | 12.352x | 75 | 136.3 | 100.0 | 100% |
| 12 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 10,429.3 | 10,391.6 | 10,448.3 | 23.4 | 3.477x | 12.605x | 75 | 139.1 | 100.2 | 100% |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 56,743.7 | 56,665.9 | 56,839.2 | 58.3 | 18.918x | 68.579x | 75 | 756.6 | 27.9 | 100% |

### `wild-secrets-slack-webhook-url` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 51,806.5 | 0.0376 | 51,762.3 | 52,848.7 | 416.8 | 0.029x | 1.000x |
| 2 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 111,971.3 | 0.0814 | 111,773.9 | 112,352.4 | 214.6 | 0.063x | 2.161x |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 338,263.5 | 0.2458 | 338,016.6 | 338,833.8 | 278.7 | 0.190x | 6.529x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 341,200.1 | 0.2479 | 340,987.4 | 342,310.1 | 468.0 | 0.192x | 6.586x |
| 5 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 439,089.5 | 0.3190 | 438,860.0 | 445,543.4 | 2,601.3 | 0.247x | 8.476x |
| 6 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 439,307.0 | 0.3192 | 438,961.5 | 439,652.1 | 252.6 | 0.247x | 8.480x |
| 7 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 645,023.5 | 0.4687 | 644,579.6 | 647,071.6 | 882.2 | 0.363x | 12.451x |
| 8 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 1,249,951.7 | 0.9082 | 1,249,354.5 | 1,253,520.1 | 1,534.1 | 0.704x | 24.127x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,776,019.1 | 1.2905 | 1,773,741.4 | 1,780,103.0 | 2,146.9 | 1.000x | 34.282x |
| 10 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 1,846,587.7 | 1.3417 | 1,844,352.2 | 1,852,998.8 | 2,995.1 | 1.040x | 35.644x |
| 11 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,782,992.7 | 3.4754 | 4,780,447.1 | 4,788,990.9 | 3,125.8 | 2.693x | 92.324x |
| 12 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,783,516.7 | 3.4757 | 4,781,617.8 | 4,788,919.7 | 2,489.1 | 2.693x | 92.334x |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 35,182,018.8 | 25.5636 | 35,133,374.8 | 35,400,926.1 | 93,622.9 | 19.809x | 679.104x |

#### `wild-secrets-slack-webhook-url` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,445.4 | 0.0376 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 86,603.8 | 0.0826 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 259,660.2 | 0.2476 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 261,985.7 | 0.2498 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 330,778.6 | 0.3155 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 330,888.6 | 0.3156 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 493,929.8 | 0.4710 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 952,392.2 | 0.9083 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 1,351,745.3 | 1.2891 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,407,577.0 | 1.3424 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,644,082.9 | 3.4753 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,644,401.2 | 3.4756 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 26,800,021.4 | 25.5585 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 9,839.5 | 0.0375 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 20,538.4 | 0.0783 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 63,947.9 | 0.2439 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 64,634.3 | 0.2466 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 83,050.8 | 0.3168 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 83,175.2 | 0.3173 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 121,751.7 | 0.4644 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 238,027.7 | 0.9080 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 339,658.5 | 1.2957 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 352,529.8 | 1.3448 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 910,640.6 | 3.4738 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 911,381.0 | 3.4766 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 6,713,634.1 | 25.6105 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 2,562.0 | 0.0391 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 4,872.3 | 0.0743 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 14,560.5 | 0.2222 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 14,636.1 | 0.2233 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 25,376.0 | 0.3872 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 25,163.0 | 0.3840 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 29,243.6 | 0.4462 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 59,189.1 | 0.9032 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 84,027.3 | 1.2822 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 86,377.5 | 1.3180 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 228,510.7 | 3.4868 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 228,360.4 | 3.4845 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,679,405.8 | 25.6257 |

### `wild-secrets-slack-webhook-url` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 694.7 | 694.5 | 695.9 | 0.5 | 0.144x | 1.000x | 75 | 9.3 | 27.2 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 928.0 | 927.1 | 932.3 | 1.9 | 0.193x | 1.336x | 75 | 12.4 | 8.9 | 100% |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,305.9 | 1,301.3 | 1,314.3 | 4.4 | 0.271x | 1.880x | 75 | 17.4 | 8.9 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,558.7 | 2,554.5 | 2,571.5 | 6.8 | 0.531x | 3.683x | 75 | 34.1 | 16.4 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,087.0 | 3,043.5 | 3,602.5 | 212.4 | 0.641x | 4.443x | 75 | 41.2 | 40.4 | 100% |
| 6 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,356.6 | 3,349.3 | 3,396.8 | 21.5 | 0.697x | 4.832x | 75 | 44.8 | 58.6 | 100% |
| 7 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 3,956.7 | 3,922.7 | 4,960.9 | 405.6 | 0.822x | 5.695x | 75 | 52.8 | 30.4 | 100% |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,815.8 | 4,813.6 | 4,871.7 | 22.1 | 1.000x | 6.932x | 75 | 64.2 | 34.4 | 100% |
| 9 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 5,609.8 | 5,563.0 | 5,636.3 | 24.5 | 1.165x | 8.075x | 75 | 74.8 | 18.0 | 100% |
| 10 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 5,713.9 | 5,711.0 | 5,820.3 | 42.3 | 1.187x | 8.225x | 75 | 76.2 | 17.3 | 100% |
| 11 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 8,973.5 | 8,882.4 | 8,990.2 | 38.4 | 1.863x | 12.917x | 75 | 119.6 | 100.2 | 100% |
| 12 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,030.9 | 8,997.8 | 9,102.2 | 34.5 | 1.875x | 12.999x | 75 | 120.4 | 100.0 | 100% |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 74,945.8 | 74,888.0 | 75,161.5 | 105.2 | 15.563x | 107.878x | 75 | 999.3 | 27.9 | 100% |

### `wild-secrets-username-password-pair` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 23,276.3 | 0.0169 | 23,260.8 | 23,309.7 | 16.6 | 1.000x | 1.000x | spread |
| 2 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 23,326.7 | 0.0169 | 23,306.2 | 23,381.2 | 25.4 | 1.002x | 1.002x | spread |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 134,167.5 | 0.0975 | 133,810.5 | 134,646.8 | 284.4 | 5.764x | 5.764x | **dominated**: `t-1m` is 90.8% of this set |
| 4 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 475,639.5 | 0.3456 | 474,966.7 | 477,227.5 | 841.0 | 20.434x | 20.434x | spread |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 489,279.0 | 0.3555 | 488,438.4 | 490,860.7 | 818.6 | 21.020x | 21.020x | spread |
| 6 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,283,962.7 | 0.9329 | 1,282,617.7 | 1,287,631.0 | 1,717.3 | 55.162x | 55.162x | spread |
| 7 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,287,801.1 | 0.9357 | 1,286,261.5 | 1,294,299.9 | 3,090.2 | 55.327x | 55.327x | spread |
| 8 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 2,242,062.8 | 1.6291 | 2,235,212.0 | 2,251,360.1 | 5,962.2 | 96.324x | 96.324x | spread |
| 9 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,244,413.2 | 1.6308 | 2,233,465.1 | 2,368,475.8 | 51,202.5 | 96.425x | 96.425x | spread |
| 10 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,834,438.6 | 3.5127 | 4,831,155.3 | 4,839,506.2 | 2,855.6 | 207.698x | 207.698x | spread |
| 11 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 5,877,733.5 | 4.2708 | 5,873,431.7 | 5,915,609.5 | 15,642.9 | 252.520x | 252.520x | spread |
| 12 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 5,880,867.8 | 4.2731 | 5,873,235.6 | 5,891,647.4 | 6,785.4 | 252.654x | 252.654x | spread |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `wild-secrets-username-password-pair` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,692.9 | 0.0169 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 17,723.0 | 0.0169 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 121,727.6 | 0.1161 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 377,913.1 | 0.3604 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 372,494.4 | 0.3552 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 971,724.3 | 0.9267 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 974,548.9 | 0.9294 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 1,700,819.0 | 1.6220 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,700,218.2 | 1.6215 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 3,671,783.4 | 3.5017 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 4,475,857.4 | 4.2685 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 4,476,539.0 | 4.2692 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 4,425.5 | 0.0169 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 4,451.0 | 0.0170 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 9,787.9 | 0.0373 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 81,021.7 | 0.3091 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 93,594.8 | 0.3570 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 248,316.4 | 0.9473 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 251,581.9 | 0.9597 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 424,139.2 | 1.6180 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 424,587.4 | 1.6197 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 926,455.9 | 3.5341 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 1,120,941.9 | 4.2761 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 1,120,770.9 | 4.2754 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 1,160.1 | 0.0177 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,157.8 | 0.0177 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 2,616.1 | 0.0399 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 16,517.5 | 0.2520 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 22,876.4 | 0.3491 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 63,486.1 | 0.9687 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 62,913.1 | 0.9600 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 117,104.5 | 1.7869 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 116,505.2 | 1.7777 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 235,656.2 | 3.5958 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 281,635.6 | 4.2974 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 281,344.6 | 4.2930 |

- not ranked: `tre_0.9.0_default-caps-simdna` — did-not-compile (tre_regncompb failed (code 11): Invalid character range)

### `wild-secrets-username-password-pair` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,376.1 | 1,375.0 | 1,377.4 | 0.9 | 0.284x | 1.000x | 75 | 18.3 | 8.9 | 100% |
| 2 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,648.8 | 1,646.1 | 1,656.1 | 3.3 | 0.340x | 1.198x | 75 | 22.0 | 27.2 | 100% |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,863.3 | 1,860.1 | 1,884.1 | 8.9 | 0.384x | 1.354x | 75 | 24.8 | 8.9 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,478.7 | 2,475.6 | 2,555.5 | 31.3 | 0.511x | 1.801x | 75 | 33.0 | 16.4 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,330.5 | 3,136.4 | 3,792.1 | 227.4 | 0.687x | 2.420x | 75 | 44.4 | 40.4 | 100% |
| 6 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 3,835.9 | 3,811.4 | 3,860.8 | 18.2 | 0.791x | 2.788x | 75 | 51.1 | 30.4 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,847.0 | 4,842.4 | 4,879.5 | 13.6 | 1.000x | 3.522x | 75 | 64.6 | 34.4 | 100% |
| 8 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 6,350.1 | 6,345.5 | 6,523.6 | 68.6 | 1.310x | 4.615x | 75 | 84.7 | 18.0 | 100% |
| 9 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 6,522.1 | 6,499.1 | 6,568.3 | 25.0 | 1.346x | 4.740x | 75 | 87.0 | 17.3 | 100% |
| 10 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 9,033.7 | 9,020.1 | 9,165.9 | 54.3 | 1.864x | 6.565x | 75 | 120.4 | 58.6 | 100% |
| 11 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 10,351.6 | 10,345.8 | 10,484.8 | 53.4 | 2.136x | 7.522x | 75 | 138.0 | 100.2 | 100% |
| 12 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 10,401.1 | 10,251.0 | 10,837.3 | 204.3 | 2.146x | 7.558x | 75 | 138.7 | 100.0 | 100% |

- not ranked: `tre_0.9.0_default-caps-simdna` — did-not-compile (tre_regncompb failed (code 11): Invalid character range)

### `wild-semdiv-altorder-foo-foobar-rustregex` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 82,230.5 | 0.0597 | 82,015.7 | 82,304.2 | 117.6 | 0.050x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 128,335.2 | 0.0932 | 128,118.9 | 128,514.9 | 145.2 | 0.078x | 1.561x |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 153,324.4 | 0.1114 | 153,208.5 | 153,646.1 | 149.8 | 0.093x | 1.865x |
| 4 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 325,819.5 | 0.2367 | 325,598.9 | 326,135.1 | 187.8 | 0.198x | 3.962x |
| 5 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 326,198.2 | 0.2370 | 325,688.2 | 326,461.9 | 269.8 | 0.198x | 3.967x |
| 6 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 409,792.2 | 0.2978 | 408,566.1 | 410,708.5 | 703.3 | 0.249x | 4.983x |
| 7 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 410,776.5 | 0.2985 | 409,325.7 | 414,919.0 | 2,087.6 | 0.250x | 4.995x |
| 8 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 1,342,842.6 | 0.9757 | 1,341,850.0 | 1,343,793.8 | 709.0 | 0.817x | 16.330x |
| 9 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 1,586,698.5 | 1.1529 | 1,563,495.8 | 1,591,292.1 | 11,976.9 | 0.965x | 19.296x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,643,819.0 | 1.1944 | 1,634,173.4 | 1,684,813.7 | 18,345.1 | 1.000x | 19.990x |
| 11 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 3,944,041.4 | 2.8658 | 3,385,814.1 | 3,954,501.9 | 224,428.5 | 2.399x | 47.963x |
| 12 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 3,945,745.6 | 2.8670 | 3,944,684.7 | 3,948,277.4 | 1,193.4 | 2.400x | 47.984x |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 28,627,126.7 | 20.8007 | 28,540,578.1 | 29,458,641.2 | 345,586.0 | 17.415x | 348.133x |

#### `wild-semdiv-altorder-foo-foobar-rustregex` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 63,408.7 | 0.0605 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 98,269.1 | 0.0937 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 116,831.6 | 0.1114 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 256,347.8 | 0.2445 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 256,644.6 | 0.2448 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 326,087.8 | 0.3110 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 326,934.8 | 0.3118 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,021,957.1 | 0.9746 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,198,891.6 | 1.1434 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 1,246,333.5 | 1.1886 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,003,827.7 | 2.8647 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,004,543.8 | 2.8654 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 21,750,661.5 | 20.7430 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 15,087.2 | 0.0576 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 23,980.4 | 0.0915 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 29,096.1 | 0.1110 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 55,017.0 | 0.2099 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 54,923.1 | 0.2095 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 70,340.0 | 0.2683 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 70,229.1 | 0.2679 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 256,264.2 | 0.9776 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 306,458.9 | 1.1690 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 315,828.8 | 1.2048 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 751,618.3 | 2.8672 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 752,202.8 | 2.8694 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 5,456,195.5 | 20.8137 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 3,648.4 | 0.0557 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 5,955.9 | 0.0909 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 7,353.6 | 0.1122 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 14,455.2 | 0.2206 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 14,769.9 | 0.2254 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 13,417.8 | 0.2047 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 13,466.0 | 0.2055 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 64,228.4 | 0.9800 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 79,733.8 | 1.2166 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 81,656.7 | 1.2460 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 188,394.7 | 2.8747 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 189,117.4 | 2.8857 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,369,745.4 | 20.9007 |

### `wild-semdiv-altorder-foo-foobar-rustregex` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 715.3 | 709.1 | 717.2 | 2.9 | 0.233x | 1.000x | 75 | 9.5 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 716.2 | 713.8 | 718.5 | 1.6 | 0.233x | 1.001x | 75 | 9.5 | 8.9 | 100% |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,342.9 | 1,341.3 | 1,345.1 | 1.4 | 0.438x | 1.878x | 75 | 17.9 | 16.4 | 100% |
| 4 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,405.6 | 2,403.5 | 2,445.3 | 16.2 | 0.784x | 3.363x | 75 | 32.1 | 27.2 | 100% |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,986.1 | 2,980.2 | 3,139.4 | 60.7 | 0.973x | 4.175x | 75 | 39.8 | 58.6 | 100% |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,017.7 | 2,819.6 | 3,254.2 | 189.0 | 0.984x | 4.219x | 75 | 40.2 | 40.4 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,067.8 | 3,053.0 | 3,243.7 | 74.7 | 1.000x | 4.289x | 75 | 40.9 | 34.4 | 100% |
| 8 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 3,072.1 | 2,762.0 | 3,249.2 | 195.3 | 1.001x | 4.295x | 75 | 41.0 | 30.4 | 100% |
| 9 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,558.1 | 4,550.8 | 4,672.6 | 47.4 | 1.486x | 6.373x | 75 | 60.8 | 17.3 | 100% |
| 10 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,705.6 | 4,494.6 | 5,031.8 | 187.2 | 1.534x | 6.579x | 75 | 62.7 | 18.0 | 100% |
| 11 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 7,488.0 | 7,485.2 | 8,133.2 | 256.2 | 2.441x | 10.469x | 75 | 99.8 | 100.2 | 100% |
| 12 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,492.3 | 7,478.0 | 7,588.8 | 41.3 | 2.442x | 10.475x | 75 | 99.9 | 100.0 | 100% |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 30,950.7 | 30,851.5 | 31,460.2 | 223.5 | 10.089x | 43.272x | 75 | 412.7 | 27.9 | 100% |

### `wild-semdiv-dollar-trailing-newline-pcre2` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 78.3 | 0.0001 | 77.1 | 78.8 | 0.7 | 0.000x | 1.000x |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 151.3 | 0.0001 | 151.1 | 151.4 | 0.1 | 0.000x | 1.932x |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 223.8 | 0.0002 | 223.8 | 254.3 | 12.2 | 0.000x | 2.859x |
| 4 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 315.8 | 0.0002 | 312.1 | 317.3 | 1.7 | 0.000x | 4.033x |
| 5 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 316.3 | 0.0002 | 314.8 | 317.6 | 0.9 | 0.000x | 4.040x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 51,579.8 | 0.0375 | 51,399.1 | 51,870.1 | 169.2 | 0.019x | 658.821x |
| 7 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 109,703.5 | 0.0797 | 109,644.4 | 109,924.3 | 96.9 | 0.040x | 1401.225x |
| 8 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 109,772.6 | 0.0798 | 109,654.1 | 109,839.0 | 70.2 | 0.040x | 1402.107x |
| 9 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 1,671,953.4 | 1.2149 | 1,671,523.0 | 1,672,508.1 | 356.2 | 0.614x | 21355.588x |
| 10 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 1,672,015.0 | 1.2149 | 1,671,826.8 | 1,676,539.9 | 1,811.5 | 0.614x | 21356.374x |
| 11 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 2,607,795.8 | 1.8948 | 2,599,348.2 | 3,126,014.0 | 204,021.7 | 0.958x | 33308.949x |
| 12 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,722,879.4 | 1.9785 | 2,716,636.8 | 2,726,864.5 | 3,280.2 | 1.000x | 34778.893x |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 18,557,154.3 | 13.4838 | 18,341,529.1 | 18,579,317.1 | 89,780.6 | 6.815x | 237027.495x |

#### `wild-semdiv-dollar-trailing-newline-pcre2` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 25.7 | 0.0000 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 50.3 | 0.0000 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 74.0 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 99.1 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 99.3 | 0.0001 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,232.4 | 0.0374 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 89,425.3 | 0.0853 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 89,433.5 | 0.0853 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 1,273,032.0 | 1.2141 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 1,272,978.5 | 1.2140 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,981,863.9 | 1.8901 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 2,071,176.6 | 1.9752 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 14,136,239.7 | 13.4814 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 25.8 | 0.0001 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 50.4 | 0.0002 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 75.4 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 99.2 | 0.0004 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 98.6 | 0.0004 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 9,847.1 | 0.0376 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 16,778.4 | 0.0640 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 16,745.6 | 0.0639 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 318,114.2 | 1.2135 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 318,072.2 | 1.2133 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 495,539.6 | 1.8903 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 517,002.9 | 1.9722 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 3,534,583.7 | 13.4834 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 26.4 | 0.0004 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 50.4 | 0.0008 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 74.5 | 0.0011 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 118.3 | 0.0018 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 118.5 | 0.0018 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 2,511.5 | 0.0383 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 3,513.6 | 0.0536 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 3,520.8 | 0.0537 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 80,832.5 | 1.2334 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 80,791.8 | 1.2328 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 130,509.1 | 1.9914 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 135,064.2 | 2.0609 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 888,250.8 | 13.5536 |

### `wild-semdiv-dollar-trailing-newline-pcre2` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,188.7 | 1,183.9 | 1,192.4 | 2.9 | 0.316x | 1.000x | 75 | 15.8 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,189.5 | 1,185.0 | 1,193.7 | 3.5 | 0.316x | 1.001x | 75 | 15.9 | 8.9 | 100% |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,594.0 | 1,591.4 | 1,598.6 | 2.4 | 0.423x | 1.341x | 75 | 21.3 | 16.4 | 100% |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 2,004.4 | 1,995.7 | 2,011.5 | 5.6 | 0.532x | 1.686x | 75 | 26.7 | 17.3 | 100% |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 2,144.3 | 2,136.2 | 2,146.3 | 3.7 | 0.569x | 1.804x | 75 | 28.6 | 18.0 | 100% |
| 6 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,764.9 | 2,763.4 | 2,857.4 | 37.1 | 0.734x | 2.326x | 75 | 36.9 | 27.2 | 100% |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,929.9 | 2,904.7 | 3,067.8 | 60.0 | 0.778x | 2.465x | 75 | 39.1 | 40.4 | 100% |
| 8 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,474.2 | 3,455.8 | 3,477.2 | 7.8 | 0.923x | 2.923x | 75 | 46.3 | 58.6 | 100% |
| 9 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 3,546.4 | 3,531.9 | 3,602.2 | 31.5 | 0.942x | 2.983x | 75 | 47.3 | 30.4 | 100% |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,765.5 | 3,753.0 | 3,967.9 | 80.7 | 1.000x | 3.168x | 75 | 50.2 | 34.4 | 100% |
| 11 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 7,330.5 | 7,308.9 | 7,360.6 | 17.5 | 1.947x | 6.167x | 75 | 97.7 | 100.2 | 100% |
| 12 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,352.1 | 7,330.8 | 7,366.6 | 12.4 | 1.952x | 6.185x | 75 | 98.0 | 100.0 | 100% |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 12,699.1 | 12,675.2 | 12,715.8 | 13.4 | 3.372x | 10.683x | 75 | 169.3 | 27.9 | 100% |

### `wild-semdiv-empty-alt-repeat-pcre2` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 242.0 | 0.0002 | 241.3 | 242.5 | 0.4 | 0.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 3,811,980.8 | 2.7698 | 3,801,001.8 | 3,820,533.9 | 7,250.9 | 0.082x | 15754.643x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 7,017,094.1 | 5.0987 | 7,010,580.6 | 7,034,257.3 | 9,878.0 | 0.150x | 29001.146x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 10,520,381.9 | 7.6442 | 10,459,895.4 | 10,621,557.4 | 52,565.1 | 0.225x | 43479.983x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 13,150,186.6 | 9.5550 | 13,126,662.0 | 15,510,436.1 | 947,845.2 | 0.282x | 54348.776x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 25,559,972.0 | 18.5721 | 25,242,206.5 | 25,756,496.9 | 188,132.0 | 0.547x | 105637.528x |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 25,895,652.4 | 18.8160 | 25,838,549.0 | 26,041,149.2 | 74,122.5 | 0.555x | 107024.871x |
| 8 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 28,152,731.3 | 20.4560 | 28,086,400.9 | 28,703,777.5 | 257,321.0 | 0.603x | 116353.216x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 46,692,370.3 | 33.9271 | 46,170,189.3 | 47,246,026.5 | 355,737.3 | 1.000x | 192976.213x |
| 10 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 46,745,767.7 | 33.9659 | 45,643,450.0 | 46,832,126.5 | 528,821.9 | 1.001x | 193196.900x |
| 11 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 64,501,084.6 | 46.8671 | 64,309,175.6 | 65,906,957.4 | 592,380.5 | 1.381x | 266578.350x |
| 12 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 65,721,547.2 | 47.7539 | 65,413,297.6 | 66,673,090.8 | 460,939.9 | 1.408x | 271622.434x |
| 13 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 99,913,182.7 | 72.5978 | 99,339,699.3 | 101,624,659.3 | 801,474.7 | 2.140x | 412934.007x |

#### `wild-semdiv-empty-alt-repeat-pcre2` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 84.0 | 0.0001 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 2,918,880.0 | 2.7837 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 5,386,209.6 | 5.1367 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 8,048,863.1 | 7.6760 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 10,075,484.1 | 9.6087 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 19,461,327.4 | 18.5598 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 19,752,493.6 | 18.8374 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 21,566,760.1 | 20.5677 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 35,724,093.8 | 34.0692 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 35,583,869.0 | 33.9354 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 49,317,533.6 | 47.0329 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 50,273,919.2 | 47.9449 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 76,132,659.0 | 72.6058 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 78.9 | 0.0003 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 712,907.6 | 2.7195 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 1,314,657.7 | 5.0150 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 1,982,484.1 | 7.5626 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 2,478,668.1 | 9.4554 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 4,814,810.6 | 18.3670 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 4,912,147.0 | 18.7384 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 5,327,712.9 | 20.3236 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 8,795,872.0 | 33.5536 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 8,842,669.5 | 33.7321 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 12,189,440.6 | 46.4990 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 12,335,622.0 | 47.0567 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 18,924,162.3 | 72.1900 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 79.2 | 0.0012 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 174,727.2 | 2.6661 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 316,226.8 | 4.8252 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 482,588.5 | 7.3637 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 601,581.4 | 9.1794 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 1,206,651.7 | 18.4120 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 1,232,795.8 | 18.8110 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,301,005.6 | 19.8518 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 2,171,424.7 | 33.1333 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 2,208,607.0 | 33.7007 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 3,023,928.6 | 46.1415 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 3,112,006.0 | 47.4854 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 4,643,146.7 | 70.8488 |

### `wild-semdiv-empty-alt-repeat-pcre2` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,238.2 | 1,221.2 | 1,242.3 | 7.4 | 0.006x | 1.000x | 75 | 16.5 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 2,901.4 | 2,890.2 | 2,921.4 | 10.6 | 0.014x | 2.343x | 75 | 38.7 | 8.9 | 100% |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 3,900.6 | 3,895.7 | 3,909.3 | 4.7 | 0.018x | 3.150x | 75 | 52.0 | 27.2 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 13,254.6 | 13,118.4 | 13,266.3 | 61.6 | 0.062x | 10.704x | 75 | 176.7 | 16.4 | 100% |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 17,362.3 | 17,081.7 | 17,567.5 | 185.8 | 0.081x | 14.022x | 75 | 231.5 | 58.6 | 100% |
| 6 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 19,831.7 | 19,791.4 | 19,982.7 | 79.9 | 0.092x | 16.016x | 75 | 264.4 | 100.0 | 100% |
| 7 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 19,913.7 | 19,739.3 | 20,174.9 | 153.4 | 0.093x | 16.082x | 75 | 265.5 | 100.2 | 100% |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 22,433.1 | 22,339.1 | 22,578.1 | 84.8 | 0.104x | 18.117x | 75 | 299.1 | 40.4 | 100% |
| 9 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 30,646.3 | 30,613.0 | 30,716.3 | 35.7 | 0.143x | 24.750x | 75 | 408.6 | 27.9 | 100% |
| 10 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 102,021.5 | 102,002.1 | 102,124.1 | 44.0 | 0.475x | 82.393x | 75 | 1,360.3 | 17.3 | 100% |
| 11 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 104,084.1 | 104,032.3 | 104,165.9 | 48.0 | 0.484x | 84.058x | 75 | 1,387.8 | 18.0 | 100% |
| 12 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 119,950.2 | 119,601.6 | 150,820.1 | 12,375.0 | 0.558x | 96.872x | 75 | 1,599.3 | 30.4 | 100% |
| 13 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 214,887.8 | 213,786.3 | 216,740.5 | 1,171.2 | 1.000x | 173.544x | 75 | 2,865.2 | 34.4 | 100% |

### `wild-validator-email-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 39.6 | 0.0000 | 37.4 | 40.9 | 1.2 | 0.078x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 40.4 | 0.0000 | 37.7 | 41.1 | 1.2 | 0.079x | 1.019x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 107.8 | 0.0001 | 107.2 | 149.5 | 16.6 | 0.212x | 2.722x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 164.4 | 0.0001 | 162.8 | 168.3 | 2.0 | 0.324x | 4.151x |
| 5 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 202.1 | 0.0001 | 196.0 | 202.7 | 2.9 | 0.398x | 5.100x |
| 6 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 367.4 | 0.0003 | 364.0 | 392.2 | 10.5 | 0.723x | 9.274x |
| 7 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 384.4 | 0.0003 | 381.4 | 390.1 | 3.3 | 0.757x | 9.703x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 507.9 | 0.0004 | 504.5 | 518.8 | 5.2 | 1.000x | 12.820x |
| 9 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 695.3 | 0.0005 | 693.0 | 699.6 | 2.7 | 1.369x | 17.551x |
| 10 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,227,440.6 | 1.6185 | 2,226,539.7 | 2,234,098.7 | 2,758.3 | 4385.543x | 56222.461x |
| 11 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,471,929.3 | 3.2493 | 4,471,684.6 | 4,474,947.0 | 1,216.0 | 8804.651x | 112875.229x |
| 12 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,478,951.0 | 3.2544 | 4,472,372.5 | 4,485,902.9 | 4,651.8 | 8818.475x | 113052.462x |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 22,258,020.6 | 16.1729 | 21,077,869.0 | 22,376,360.2 | 501,461.0 | 43823.165x | 561811.022x |

#### `wild-validator-email-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 14.5 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 15.0 | 0.0000 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 37.3 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 60.7 | 0.0001 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 72.7 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 112.8 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 112.8 | 0.0001 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 284.0 | 0.0003 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 329.1 | 0.0003 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,696,947.3 | 1.6183 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,406,158.0 | 3.2484 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,411,463.5 | 3.2534 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 16,925,301.5 | 16.1412 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 11.6 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 12.1 | 0.0000 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 32.9 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 51.0 | 0.0002 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 60.6 | 0.0002 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 101.2 | 0.0004 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 102.7 | 0.0004 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 109.9 | 0.0004 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 171.0 | 0.0007 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 424,200.4 | 1.6182 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 851,912.9 | 3.2498 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 852,400.5 | 3.2516 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 4,258,091.4 | 16.2433 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 13.2 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 13.3 | 0.0002 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 37.4 | 0.0006 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 52.4 | 0.0008 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 68.4 | 0.0010 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 153.7 | 0.0023 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 170.1 | 0.0026 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 114.0 | 0.0017 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 194.8 | 0.0030 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,439.2 | 1.6241 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 214,017.7 | 3.2657 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 214,325.8 | 3.2704 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,070,981.8 | 16.3419 |

### `wild-validator-email-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,063.7 | 1,059.1 | 1,068.3 | 3.7 | 0.176x | 1.000x | 75 | 14.2 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,072.0 | 1,068.5 | 1,080.9 | 4.2 | 0.178x | 1.008x | 75 | 14.3 | 8.9 | 100% |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,248.6 | 2,245.6 | 2,255.5 | 3.3 | 0.373x | 2.114x | 75 | 30.0 | 27.2 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,580.2 | 2,569.8 | 2,613.6 | 17.4 | 0.428x | 2.426x | 75 | 34.4 | 16.4 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,273.1 | 3,118.7 | 3,644.4 | 190.6 | 0.543x | 3.077x | 75 | 43.6 | 40.4 | 100% |
| 6 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,227.7 | 5,218.6 | 5,288.9 | 25.3 | 0.867x | 4.915x | 75 | 69.7 | 58.6 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 6,032.0 | 6,007.6 | 6,058.8 | 18.1 | 1.000x | 5.671x | 75 | 80.4 | 34.4 | 100% |
| 8 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 6,419.4 | 6,407.0 | 6,692.5 | 111.5 | 1.064x | 6.035x | 75 | 85.6 | 17.3 | 100% |
| 9 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 6,487.2 | 6,486.0 | 6,489.6 | 1.2 | 1.075x | 6.099x | 75 | 86.5 | 18.0 | 100% |
| 10 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 7,240.1 | 7,187.1 | 7,854.1 | 253.0 | 1.200x | 6.807x | 75 | 96.5 | 30.4 | 100% |
| 11 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 8,127.5 | 8,103.7 | 8,180.7 | 25.8 | 1.347x | 7.641x | 75 | 108.4 | 100.2 | 100% |
| 12 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 8,127.6 | 8,094.8 | 8,171.0 | 24.3 | 1.347x | 7.641x | 75 | 108.4 | 100.0 | 100% |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 120,654.4 | 120,381.9 | 120,833.8 | 194.1 | 20.002x | 113.434x | 75 | 1,608.7 | 27.9 | 100% |

### `wild-validator-ipv4-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 17.9 | 0.0000 | 17.9 | 18.4 | 0.2 | 0.183x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.7 | 0.0000 | 18.7 | 18.8 | 0.0 | 0.191x | 1.043x |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 30.4 | 0.0000 | 30.3 | 35.5 | 2.1 | 0.310x | 1.693x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 32.1 | 0.0000 | 32.0 | 32.2 | 0.1 | 0.328x | 1.787x |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 82.2 | 0.0001 | 81.5 | 83.3 | 0.6 | 0.841x | 4.583x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 97.8 | 0.0001 | 97.7 | 98.3 | 0.2 | 1.000x | 5.452x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 146.3 | 0.0001 | 145.5 | 151.1 | 2.1 | 1.495x | 8.152x |
| 8 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 285.8 | 0.0002 | 285.4 | 288.2 | 1.1 | 2.921x | 15.926x |
| 9 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 287.2 | 0.0002 | 282.1 | 543.3 | 102.7 | 2.935x | 16.004x |
| 10 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 367.4 | 0.0003 | 367.0 | 389.5 | 9.6 | 3.755x | 20.475x |
| 11 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,269,041.8 | 3.1019 | 4,268,089.4 | 4,272,411.9 | 1,652.4 | 43636.983x | 237907.838x |
| 12 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,272,616.7 | 3.1045 | 4,268,675.0 | 4,314,074.2 | 17,074.9 | 43673.524x | 238107.058x |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 15,445,909.9 | 11.2231 | 15,411,565.3 | 15,503,843.6 | 33,320.8 | 157883.885x | 860779.344x |

#### `wild-validator-ipv4-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 6.0 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 6.2 | 0.0000 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.1 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 10.7 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 27.2 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 32.5 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 45.5 | 0.0000 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 88.5 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 87.5 | 0.0001 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 299.2 | 0.0003 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,250,897.7 | 3.1003 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,254,119.6 | 3.1034 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 11,736,709.9 | 11.1930 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 6.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 6.2 | 0.0000 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 10.6 | 0.0000 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 27.5 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 32.6 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 50.1 | 0.0002 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 89.3 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 91.0 | 0.0003 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 34.1 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 813,558.1 | 3.1035 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 813,629.2 | 3.1037 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 2,946,854.8 | 11.2414 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 6.0 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 6.3 | 0.0001 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.2 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 10.7 | 0.0002 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 27.6 | 0.0004 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 32.7 | 0.0005 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 52.0 | 0.0008 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 109.0 | 0.0017 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 108.2 | 0.0017 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 34.6 | 0.0005 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 204,516.5 | 3.1207 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 204,414.1 | 3.1191 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 746,044.7 | 11.3837 |

### `wild-validator-ipv4-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 497.9 | 497.3 | 500.6 | 1.3 | 0.156x | 1.000x | 75 | 6.6 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 870.4 | 870.4 | 871.4 | 0.4 | 0.272x | 1.748x | 75 | 11.6 | 8.9 | 100% |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 953.4 | 950.9 | 966.6 | 5.6 | 0.298x | 1.915x | 75 | 12.7 | 27.2 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,253.8 | 1,252.6 | 1,257.6 | 1.8 | 0.392x | 2.518x | 75 | 16.7 | 16.4 | 100% |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 2,705.8 | 2,689.0 | 3,919.9 | 488.2 | 0.847x | 5.435x | 75 | 36.1 | 30.4 | 100% |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,196.0 | 3,177.3 | 5,002.4 | 713.2 | 1.000x | 6.420x | 75 | 42.6 | 34.4 | 100% |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,318.4 | 3,213.7 | 3,852.9 | 224.3 | 1.038x | 6.665x | 75 | 44.2 | 40.4 | 100% |
| 8 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,661.5 | 3,588.6 | 3,824.5 | 85.0 | 1.146x | 7.355x | 75 | 48.8 | 58.6 | 100% |
| 9 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 6,354.2 | 6,338.1 | 6,923.9 | 228.5 | 1.988x | 12.763x | 75 | 84.7 | 18.0 | 100% |
| 10 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 6,554.1 | 6,547.5 | 6,559.6 | 4.0 | 2.051x | 13.165x | 75 | 87.4 | 17.3 | 100% |
| 11 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,344.2 | 9,301.7 | 9,386.8 | 28.4 | 2.924x | 18.769x | 75 | 124.6 | 100.0 | 100% |
| 12 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 9,420.2 | 9,330.1 | 10,128.7 | 293.5 | 2.947x | 18.922x | 75 | 125.6 | 100.2 | 100% |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 38,754.2 | 38,537.2 | 38,879.6 | 121.8 | 12.126x | 77.843x | 75 | 516.7 | 27.9 | 100% |

### `wild-validator-us-zip-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 17.8 | 0.0000 | 17.8 | 17.9 | 0.1 | 0.189x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 18.1 | 0.0000 | 17.9 | 18.3 | 0.1 | 0.192x | 1.016x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 30.2 | 0.0000 | 30.2 | 30.3 | 0.0 | 0.322x | 1.697x |
| 4 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 30.5 | 0.0000 | 30.4 | 36.7 | 2.5 | 0.325x | 1.714x |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 80.7 | 0.0001 | 79.9 | 119.8 | 16.8 | 0.858x | 4.528x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 94.1 | 0.0001 | 94.0 | 94.2 | 0.1 | 1.000x | 5.278x |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 94.8 | 0.0001 | 94.3 | 95.0 | 0.3 | 1.008x | 5.321x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 122.6 | 0.0001 | 111.7 | 127.2 | 6.4 | 1.303x | 6.879x |
| 9 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 284.9 | 0.0002 | 283.1 | 291.6 | 3.2 | 3.029x | 15.988x |
| 10 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 286.6 | 0.0002 | 283.5 | 286.9 | 1.4 | 3.047x | 16.083x |
| 11 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 3,562,498.8 | 2.5885 | 3,557,409.4 | 3,566,906.7 | 3,274.7 | 37874.670x | 199895.873x |
| 12 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 3,570,378.2 | 2.5943 | 3,565,819.5 | 3,583,110.9 | 6,022.8 | 37958.441x | 200337.998x |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 8,695,277.0 | 6.3181 | 8,692,212.8 | 8,736,184.0 | 16,684.0 | 92443.752x | 487901.919x |

#### `wild-validator-us-zip-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 6.0 | 0.0000 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 6.0 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 10.1 | 0.0000 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.2 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 26.8 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 31.3 | 0.0000 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 31.5 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 40.8 | 0.0000 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 88.1 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 87.9 | 0.0001 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 2,712,474.5 | 2.5868 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 2,717,926.4 | 2.5920 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 6,625,106.1 | 6.3182 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 5.9 | 0.0000 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 6.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 10.1 | 0.0000 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.2 | 0.0000 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 27.1 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 31.3 | 0.0001 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 31.7 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 40.5 | 0.0002 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 88.2 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 88.9 | 0.0003 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 678,224.7 | 2.5872 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 681,569.5 | 2.6000 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 1,655,985.7 | 6.3171 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 6.0 | 0.0001 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 6.0 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 10.1 | 0.0002 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.2 | 0.0002 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 26.8 | 0.0004 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 31.4 | 0.0005 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 31.7 | 0.0005 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 39.4 | 0.0006 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 108.5 | 0.0017 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 108.8 | 0.0017 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 170,810.2 | 2.6064 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 171,364.2 | 2.6148 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 415,258.1 | 6.3363 |

### `wild-validator-us-zip-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 485.0 | 484.5 | 486.2 | 0.6 | 0.153x | 1.000x | 75 | 6.5 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 808.1 | 807.5 | 809.6 | 0.9 | 0.254x | 1.666x | 75 | 10.8 | 8.9 | 100% |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 986.0 | 985.7 | 1,052.1 | 26.0 | 0.310x | 2.033x | 75 | 13.1 | 27.2 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,669.5 | 1,658.5 | 1,694.6 | 12.7 | 0.525x | 3.443x | 75 | 22.3 | 16.4 | 100% |
| 5 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,041.7 | 2,037.8 | 2,485.1 | 177.6 | 0.642x | 4.210x | 75 | 27.2 | 100.0 | 100% |
| 6 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 2,046.0 | 2,040.1 | 2,094.7 | 20.2 | 0.644x | 4.219x | 75 | 27.3 | 100.2 | 100% |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,079.4 | 2,961.1 | 3,492.1 | 216.8 | 0.969x | 6.350x | 75 | 41.1 | 40.4 | 100% |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,177.8 | 3,173.6 | 3,270.3 | 37.4 | 1.000x | 6.553x | 75 | 42.4 | 34.4 | 100% |
| 9 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 3,353.4 | 3,320.3 | 3,366.8 | 16.1 | 1.055x | 6.915x | 75 | 44.7 | 30.4 | 100% |
| 10 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,888.6 | 4,885.0 | 4,897.6 | 4.2 | 1.538x | 10.080x | 75 | 65.2 | 18.0 | 100% |
| 11 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,915.5 | 4,906.6 | 4,989.0 | 31.9 | 1.547x | 10.136x | 75 | 65.5 | 58.6 | 100% |
| 12 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 5,099.4 | 5,095.1 | 5,398.7 | 133.1 | 1.605x | 10.515x | 75 | 68.0 | 17.3 | 100% |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 13,928.4 | 13,910.8 | 14,002.7 | 32.1 | 4.383x | 28.721x | 75 | 185.7 | 27.9 | 100% |

### `wild-validator-uuid-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 82,557.9 | 0.0600 | 82,067.9 | 83,056.6 | 362.0 | 0.003x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 82,561.2 | 0.0600 | 82,216.2 | 82,703.7 | 209.2 | 0.003x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 134,578.1 | 0.0978 | 134,283.8 | 134,658.9 | 137.3 | 0.005x | 1.630x |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 210,621.0 | 0.1530 | 209,804.6 | 211,188.0 | 514.3 | 0.008x | 2.551x |
| 5 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 243,258.4 | 0.1768 | 243,026.3 | 243,534.2 | 176.8 | 0.009x | 2.947x |
| 6 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 2,235,844.8 | 1.6246 | 2,231,352.6 | 2,251,497.0 | 7,159.8 | 0.086x | 27.082x |
| 7 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,237,753.9 | 1.6260 | 2,232,636.1 | 2,244,177.6 | 3,715.4 | 0.086x | 27.105x |
| 8 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,420,629.7 | 1.7589 | 2,415,306.8 | 2,421,702.7 | 2,248.5 | 0.093x | 29.320x |
| 9 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 8,114,576.8 | 5.8961 | 8,107,786.7 | 8,127,219.0 | 6,435.8 | 0.311x | 98.290x |
| 10 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 8,129,083.2 | 5.9067 | 8,110,818.5 | 8,141,896.0 | 11,333.3 | 0.311x | 98.465x |
| 11 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 26,121,044.2 | 18.9798 | 26,088,628.6 | 26,127,729.7 | 14,582.2 | 1.000x | 316.397x |
| 12 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 28,647,224.1 | 20.8153 | 28,569,891.7 | 28,742,575.6 | 55,218.1 | 1.097x | 346.996x |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 72,093,852.0 | 52.3840 | 71,893,388.8 | 72,336,540.8 | 171,659.5 | 2.760x | 873.252x |

#### `wild-validator-uuid-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 68,513.0 | 0.0653 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 68,420.0 | 0.0653 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 102,549.8 | 0.0978 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 164,530.6 | 0.1569 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 185,633.7 | 0.1770 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 1,697,309.3 | 1.6187 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,698,742.3 | 1.6200 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,844,193.1 | 1.7588 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 6,196,361.3 | 5.9093 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 6,193,390.4 | 5.9065 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 19,930,940.9 | 19.0076 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 21,854,208.9 | 20.8418 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 54,871,984.2 | 52.3300 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 11,586.2 | 0.0442 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 11,743.9 | 0.0448 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 25,762.1 | 0.0983 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 37,196.7 | 0.1419 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 46,111.3 | 0.1759 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 423,178.7 | 1.6143 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 423,558.5 | 1.6157 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 459,146.5 | 1.7515 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 1,533,851.9 | 5.8512 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 1,538,189.9 | 5.8677 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 4,952,782.8 | 18.8934 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 5,421,512.5 | 20.6814 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 13,733,608.5 | 52.3896 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 2,475.6 | 0.0378 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 2,456.7 | 0.0375 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 6,170.6 | 0.0942 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 8,686.0 | 0.1325 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 11,415.9 | 0.1742 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 116,008.7 | 1.7702 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 115,773.2 | 1.7666 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 116,148.1 | 1.7723 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 384,385.3 | 5.8653 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 385,785.5 | 5.8866 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 1,236,205.0 | 18.8630 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,354,918.6 | 20.6744 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 3,447,786.5 | 52.6090 |

### `wild-validator-uuid-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 716.2 | 713.9 | 722.6 | 3.3 | 0.243x | 1.000x | 75 | 9.5 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 717.8 | 717.1 | 721.4 | 1.8 | 0.244x | 1.002x | 75 | 9.6 | 8.9 | 100% |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,240.7 | 1,240.2 | 1,242.9 | 1.0 | 0.421x | 1.732x | 75 | 16.5 | 16.4 | 100% |
| 4 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,623.9 | 1,622.4 | 1,628.3 | 2.1 | 0.551x | 2.268x | 75 | 21.7 | 27.2 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,893.0 | 2,869.5 | 2,971.3 | 35.6 | 0.981x | 4.040x | 75 | 38.6 | 40.4 | 100% |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,947.9 | 2,924.3 | 2,956.6 | 12.3 | 1.000x | 4.116x | 75 | 39.3 | 34.4 | 100% |
| 7 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 3,409.3 | 3,393.2 | 3,461.1 | 25.0 | 1.157x | 4.760x | 75 | 45.5 | 30.4 | 100% |
| 8 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,236.0 | 4,226.9 | 4,290.4 | 22.8 | 1.437x | 5.915x | 75 | 56.5 | 58.6 | 100% |
| 9 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 6,772.9 | 6,704.5 | 6,833.7 | 42.9 | 2.298x | 9.457x | 75 | 90.3 | 17.3 | 100% |
| 10 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 6,856.6 | 6,814.6 | 6,931.1 | 38.3 | 2.326x | 9.574x | 75 | 91.4 | 18.0 | 100% |
| 11 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 9,878.0 | 9,848.5 | 9,913.1 | 25.6 | 3.351x | 13.793x | 75 | 131.7 | 100.2 | 100% |
| 12 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,919.5 | 9,782.7 | 10,083.5 | 105.0 | 3.365x | 13.851x | 75 | 132.3 | 100.0 | 100% |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 122,037.8 | 120,842.6 | 126,332.4 | 1,992.1 | 41.398x | 170.402x | 75 | 1,627.2 | 27.9 | 100% |

### `wild-waf-crs-942140-dbnames` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 600,282.9 | 0.4362 | 600,078.2 | 600,746.5 | 223.6 | 0.020x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,241,475.2 | 1.6287 | 2,234,637.2 | 2,244,885.2 | 4,405.6 | 0.075x | 3.734x |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 2,242,907.8 | 1.6297 | 2,233,106.6 | 2,248,494.0 | 5,092.6 | 0.075x | 3.736x |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,446,068.2 | 1.7773 | 2,445,903.9 | 2,446,948.0 | 384.6 | 0.081x | 4.075x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 4,085,020.3 | 2.9682 | 4,084,502.2 | 4,127,033.3 | 19,352.1 | 0.136x | 6.805x |
| 6 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 4,099,500.9 | 2.9787 | 4,081,500.8 | 4,172,083.1 | 32,111.1 | 0.136x | 6.829x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 5,402,673.4 | 3.9256 | 5,399,299.7 | 5,466,254.6 | 31,026.6 | 0.180x | 9.000x |
| 8 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 20,895,872.0 | 15.1831 | 20,811,044.5 | 20,965,133.2 | 49,275.9 | 0.695x | 34.810x |
| 9 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 20,914,020.6 | 15.1963 | 20,867,186.5 | 23,316,368.8 | 961,851.7 | 0.695x | 34.840x |
| 10 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 23,532,100.3 | 17.0986 | 23,513,965.2 | 26,187,735.2 | 1,057,537.6 | 0.782x | 39.202x |
| 11 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30,086,298.6 | 21.8610 | 30,049,413.9 | 30,111,953.1 | 22,366.6 | 1.000x | 50.120x |
| 12 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 65,241,237.2 | 47.4049 | 65,024,447.8 | 65,398,824.0 | 130,718.7 | 2.168x | 108.684x |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 281,837,562.0 | 204.7857 | 272,627,907.0 | 286,118,153.0 | 4,960,497.9 | 9.368x | 469.508x |

#### `wild-waf-crs-942140-dbnames` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 477,896.7 | 0.4558 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,701,006.7 | 1.6222 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 1,700,838.2 | 1.6220 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,862,013.7 | 1.7758 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 3,114,801.7 | 2.9705 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 3,120,458.9 | 2.9759 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 4,116,028.1 | 3.9254 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 15,923,287.8 | 15.1856 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 15,943,314.7 | 15.2047 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 17,903,606.9 | 17.0742 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 22,873,496.7 | 21.8139 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 49,703,089.0 | 47.4006 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 215,696,548.0 | 205.7043 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 101,855.2 | 0.3885 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 425,421.6 | 1.6229 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 424,466.9 | 1.6192 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 466,148.1 | 1.7782 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 777,937.9 | 2.9676 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 778,806.3 | 2.9709 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 1,030,705.9 | 3.9318 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 3,961,577.8 | 15.1122 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,969,855.3 | 15.1438 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 4,481,656.2 | 17.0962 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 5,728,266.4 | 21.8516 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 12,403,551.6 | 47.3158 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 52,648,788.0 | 200.8392 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 20,504.8 | 0.3129 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 116,404.0 | 1.7762 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 117,046.2 | 1.7860 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 118,082.0 | 1.8018 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 192,184.1 | 2.9325 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 192,182.8 | 2.9325 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 257,015.1 | 3.9217 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 987,993.2 | 15.0756 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 988,985.9 | 15.0907 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,151,513.2 | 17.5707 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 1,471,126.6 | 22.4476 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 3,115,774.6 | 47.5429 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 13,470,716.0 | 205.5468 |

### `wild-waf-crs-942140-dbnames` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 2,707.4 | 2,697.0 | 2,871.5 | 67.0 | 0.133x | 1.000x | 75 | 36.1 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 2,713.5 | 2,704.5 | 2,718.3 | 5.2 | 0.134x | 1.002x | 75 | 36.2 | 8.9 | 100% |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 3,412.2 | 3,406.3 | 3,413.1 | 2.9 | 0.168x | 1.260x | 75 | 45.5 | 27.2 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 4,408.0 | 4,405.7 | 4,413.5 | 3.1 | 0.217x | 1.628x | 75 | 58.8 | 16.4 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 4,794.5 | 4,707.3 | 4,828.3 | 46.1 | 0.236x | 1.771x | 75 | 63.9 | 40.4 | 100% |
| 6 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,613.9 | 9,602.1 | 9,672.9 | 26.7 | 0.474x | 3.551x | 75 | 128.2 | 100.0 | 100% |
| 7 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 9,704.5 | 9,670.3 | 9,716.5 | 19.7 | 0.478x | 3.584x | 75 | 129.4 | 100.2 | 100% |
| 8 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 16,422.3 | 16,411.5 | 16,624.3 | 91.2 | 0.809x | 6.066x | 75 | 219.0 | 17.3 | 100% |
| 9 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 16,470.1 | 16,463.5 | 16,508.0 | 16.3 | 0.812x | 6.083x | 75 | 219.6 | 30.4 | 100% |
| 10 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 16,538.1 | 16,325.7 | 16,823.4 | 178.5 | 0.815x | 6.108x | 75 | 220.5 | 18.0 | 100% |
| 11 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 20,292.4 | 20,225.6 | 20,644.2 | 154.1 | 1.000x | 7.495x | 75 | 270.6 | 34.4 | 100% |
| 12 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 44,816.7 | 44,752.1 | 45,046.3 | 113.0 | 2.209x | 16.553x | 75 | 597.6 | 58.6 | 100% |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 322,509.9 | 318,340.6 | 323,735.3 | 1,968.8 | 15.893x | 119.122x | 75 | 4,300.1 | 27.9 | 100% |

### `wild-waf-crs-942160-sleep-benchmark` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 160,319.3 | 0.1165 | 160,095.4 | 160,605.1 | 165.9 | 0.024x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 388,639.4 | 0.2824 | 387,931.4 | 391,513.8 | 1,318.0 | 0.058x | 2.424x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,051,200.3 | 0.7638 | 1,050,835.9 | 1,053,165.3 | 888.4 | 0.157x | 6.557x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,269,889.4 | 0.9227 | 1,266,066.3 | 1,274,574.3 | 2,993.4 | 0.190x | 7.921x |
| 5 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,272,714.6 | 0.9248 | 1,271,672.5 | 1,276,644.2 | 1,745.0 | 0.190x | 7.939x |
| 6 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,238,967.6 | 1.6269 | 2,232,496.8 | 2,242,778.2 | 3,588.2 | 0.335x | 13.966x |
| 7 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 2,240,147.2 | 1.6277 | 2,235,744.2 | 2,248,140.7 | 4,055.5 | 0.335x | 13.973x |
| 8 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,911,042.9 | 3.5684 | 4,900,030.2 | 5,814,985.9 | 362,499.5 | 0.735x | 30.633x |
| 9 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 5,570,651.2 | 4.0477 | 5,552,794.1 | 5,706,381.4 | 58,098.5 | 0.834x | 34.747x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 6,681,609.1 | 4.8549 | 6,653,379.7 | 6,695,199.9 | 15,895.0 | 1.000x | 41.677x |
| 11 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 9,975,714.9 | 7.2484 | 9,868,647.9 | 9,995,358.3 | 45,373.5 | 1.493x | 62.224x |
| 12 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 9,984,009.0 | 7.2545 | 9,943,314.7 | 9,995,235.4 | 19,074.2 | 1.494x | 62.276x |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 60,083,206.6 | 43.6570 | 60,035,694.2 | 60,306,357.8 | 95,487.1 | 8.992x | 374.772x |

#### `wild-waf-crs-942160-sleep-benchmark` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 122,178.9 | 0.1165 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 295,961.7 | 0.2823 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 792,469.1 | 0.7558 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 963,666.6 | 0.9190 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 964,134.9 | 0.9195 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,699,488.6 | 1.6208 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 1,699,881.0 | 1.6211 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 3,729,683.1 | 3.5569 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 4,222,246.4 | 4.0266 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 5,067,071.7 | 4.8323 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 7,609,108.2 | 7.2566 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 7,609,373.0 | 7.2569 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 45,771,680.4 | 43.6513 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 30,405.1 | 0.1160 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 73,861.3 | 0.2818 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 207,111.4 | 0.7901 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 244,243.7 | 0.9317 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 244,547.4 | 0.9329 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 423,635.7 | 1.6160 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 425,758.3 | 1.6241 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 934,212.4 | 3.5637 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,060,747.7 | 4.0464 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 1,266,346.3 | 4.8307 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 1,888,244.0 | 7.2031 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 1,902,954.4 | 7.2592 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 11,441,602.0 | 43.6462 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 7,760.4 | 0.1184 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 18,531.2 | 0.2828 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 51,618.6 | 0.7876 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 64,269.1 | 0.9807 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 64,511.9 | 0.9844 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 116,321.8 | 1.7749 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 116,562.9 | 1.7786 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 246,550.1 | 3.7621 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 286,496.5 | 4.3716 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 340,268.2 | 5.1921 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 477,028.3 | 7.2789 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 476,758.4 | 7.2748 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 2,884,170.2 | 44.0089 |

### `wild-waf-crs-942160-sleep-benchmark` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,301.1 | 1,290.1 | 1,311.8 | 8.8 | 0.358x | 1.000x | 75 | 17.3 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,305.4 | 1,290.4 | 1,322.1 | 10.6 | 0.359x | 1.003x | 75 | 17.4 | 8.9 | 100% |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,424.2 | 2,416.2 | 2,427.8 | 4.6 | 0.668x | 1.863x | 75 | 32.3 | 27.2 | 100% |
| 4 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 3,182.7 | 3,170.6 | 3,186.3 | 6.3 | 0.876x | 2.446x | 75 | 42.4 | 30.4 | 100% |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 3,205.0 | 3,198.4 | 3,210.0 | 3.7 | 0.883x | 2.463x | 75 | 42.7 | 16.4 | 100% |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,420.5 | 3,410.0 | 3,585.0 | 66.9 | 0.942x | 2.629x | 75 | 45.6 | 40.4 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,631.6 | 3,577.7 | 3,706.2 | 47.2 | 1.000x | 2.791x | 75 | 48.4 | 34.4 | 100% |
| 8 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,635.8 | 9,548.8 | 9,873.0 | 115.5 | 2.653x | 7.406x | 75 | 128.5 | 100.0 | 100% |
| 9 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 9,839.2 | 9,633.0 | 9,944.0 | 116.6 | 2.709x | 7.562x | 75 | 131.2 | 100.2 | 100% |
| 10 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 11,071.1 | 11,033.7 | 11,093.3 | 20.8 | 3.049x | 8.509x | 75 | 147.6 | 18.0 | 100% |
| 11 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11,256.4 | 11,245.1 | 12,166.4 | 363.5 | 3.100x | 8.652x | 75 | 150.1 | 17.3 | 100% |
| 12 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 12,477.7 | 12,460.1 | 12,509.0 | 18.6 | 3.436x | 9.590x | 75 | 166.4 | 58.6 | 100% |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 71,092.0 | 71,064.1 | 71,195.9 | 56.8 | 19.576x | 54.641x | 75 | 947.9 | 27.9 | 100% |

### `wild-waf-crs-942270-union-select` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 60,156.2 | 0.0437 | 59,831.1 | 60,764.7 | 306.2 | 0.021x | 1.000x |
| 2 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 86,476.9 | 0.0628 | 86,305.2 | 86,557.0 | 87.2 | 0.030x | 1.438x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 280,700.7 | 0.2040 | 280,469.7 | 281,750.6 | 465.9 | 0.099x | 4.666x |
| 4 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 438,865.4 | 0.3189 | 438,743.8 | 440,523.7 | 661.7 | 0.155x | 7.295x |
| 5 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 439,297.2 | 0.3192 | 438,987.8 | 439,658.3 | 261.4 | 0.155x | 7.303x |
| 6 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 998,850.2 | 0.7258 | 996,107.3 | 1,015,194.6 | 6,873.9 | 0.352x | 16.604x |
| 7 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 999,730.7 | 0.7264 | 993,730.5 | 1,018,813.4 | 8,976.2 | 0.352x | 16.619x |
| 8 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 2,440,748.2 | 1.7735 | 2,438,170.8 | 2,637,764.5 | 78,609.1 | 0.860x | 40.574x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,836,522.1 | 2.0610 | 2,835,421.7 | 2,837,841.7 | 876.8 | 1.000x | 47.153x |
| 10 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,425,857.9 | 2.4893 | 3,423,977.2 | 3,427,078.8 | 1,119.1 | 1.208x | 56.949x |
| 11 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,312,523.7 | 3.1335 | 4,307,645.9 | 4,321,194.5 | 4,549.2 | 1.520x | 71.689x |
| 12 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,313,087.0 | 3.1339 | 4,311,661.4 | 4,336,022.5 | 9,370.5 | 1.521x | 71.698x |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 30,934,558.2 | 22.4773 | 30,890,917.0 | 30,980,398.6 | 28,546.6 | 10.906x | 514.238x |

#### `wild-waf-crs-942270-union-select` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 45,835.2 | 0.0437 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 65,906.4 | 0.0629 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 213,624.6 | 0.2037 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 330,714.0 | 0.3154 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 330,774.1 | 0.3155 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 756,299.2 | 0.7213 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 756,482.8 | 0.7214 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,854,898.8 | 1.7690 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 2,155,494.3 | 2.0556 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 2,603,920.7 | 2.4833 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,281,979.1 | 3.1299 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,283,527.5 | 3.1314 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 23,548,538.8 | 22.4576 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 11,429.6 | 0.0436 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 16,432.6 | 0.0627 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 53,419.8 | 0.2038 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 83,169.4 | 0.3173 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 83,260.4 | 0.3176 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 192,300.0 | 0.7336 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 192,461.4 | 0.7342 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 465,542.7 | 1.7759 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 542,450.0 | 2.0693 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 655,621.8 | 2.5010 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 821,222.1 | 3.1327 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 822,506.1 | 3.1376 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 5,894,987.8 | 22.4876 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 2,925.8 | 0.0446 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 4,148.6 | 0.0633 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 13,520.3 | 0.2063 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 25,110.2 | 0.3832 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 25,172.3 | 0.3841 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 49,443.2 | 0.7544 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 49,729.8 | 0.7588 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 118,749.7 | 1.8120 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 138,428.8 | 2.1123 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 166,324.6 | 2.5379 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 206,872.3 | 3.1566 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 207,139.9 | 3.1607 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,481,620.7 | 22.6077 |

### `wild-waf-crs-942270-union-select` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,148.8 | 1,145.5 | 1,154.5 | 3.1 | 0.220x | 1.000x | 75 | 15.3 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,150.5 | 1,149.0 | 1,429.7 | 111.9 | 0.220x | 1.002x | 75 | 15.3 | 8.9 | 100% |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,911.9 | 1,907.5 | 1,914.9 | 2.5 | 0.366x | 1.664x | 75 | 25.5 | 27.2 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,127.7 | 2,124.4 | 2,149.5 | 9.0 | 0.408x | 1.852x | 75 | 28.4 | 16.4 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,117.6 | 3,055.8 | 3,575.8 | 190.8 | 0.597x | 2.714x | 75 | 41.6 | 40.4 | 100% |
| 6 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 4,769.2 | 4,733.6 | 5,473.2 | 280.2 | 0.914x | 4.152x | 75 | 63.6 | 30.4 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 5,218.0 | 5,200.5 | 5,233.4 | 12.2 | 1.000x | 4.542x | 75 | 69.6 | 34.4 | 100% |
| 8 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 5,245.3 | 5,233.3 | 5,251.4 | 8.2 | 1.005x | 4.566x | 75 | 69.9 | 18.0 | 100% |
| 9 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 5,289.3 | 5,287.9 | 5,290.4 | 0.9 | 1.014x | 4.604x | 75 | 70.5 | 17.3 | 100% |
| 10 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 8,262.9 | 8,250.8 | 8,311.3 | 22.1 | 1.584x | 7.193x | 75 | 110.2 | 100.0 | 100% |
| 11 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 8,310.8 | 8,282.6 | 8,584.9 | 130.5 | 1.593x | 7.235x | 75 | 110.8 | 100.2 | 100% |
| 12 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 8,755.4 | 8,743.4 | 8,820.1 | 28.2 | 1.678x | 7.622x | 75 | 116.7 | 58.6 | 100% |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 39,238.2 | 39,190.5 | 39,256.3 | 23.6 | 7.520x | 34.157x | 75 | 523.2 | 27.9 | 100% |

### `wild-waf-crs-942360-concat-sqli` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 880,368.1 | 0.6397 | 877,335.7 | 882,480.2 | 1,938.5 | 0.003x | 1.000x |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 2,246,279.2 | 1.6322 | 2,238,966.4 | 2,249,444.7 | 3,694.4 | 0.008x | 2.552x |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,249,243.6 | 1.6343 | 2,246,083.4 | 2,255,865.2 | 3,271.8 | 0.008x | 2.555x |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,454,310.4 | 1.7833 | 2,453,185.8 | 2,464,936.9 | 4,394.6 | 0.009x | 2.788x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 12,149,169.0 | 8.8277 | 12,111,135.2 | 12,290,571.9 | 71,924.8 | 0.044x | 13.800x |
| 6 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 12,239,876.9 | 8.8936 | 12,104,333.0 | 13,070,612.2 | 359,813.5 | 0.044x | 13.903x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 17,215,396.8 | 12.5089 | 17,129,482.5 | 17,236,671.2 | 39,452.1 | 0.062x | 19.555x |
| 8 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 48,338,217.5 | 35.1230 | 48,225,425.2 | 48,667,584.7 | 151,243.1 | 0.173x | 54.907x |
| 9 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 48,353,031.2 | 35.1337 | 48,199,058.5 | 48,478,315.2 | 98,154.8 | 0.173x | 54.924x |
| 10 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 138,553,761.5 | 100.6744 | 138,270,549.0 | 153,899,022.5 | 6,138,875.5 | 0.497x | 157.382x |
| 11 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 227,773,600.5 | 165.5023 | 227,381,168.0 | 228,528,644.5 | 422,175.6 | 0.816x | 258.725x |
| 12 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 278,963,869.0 | 202.6977 | 278,287,376.0 | 279,643,673.0 | 430,615.4 | 1.000x | 316.872x |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 1,160,121,978.0 | 842.9551 | 1,154,183,359.0 | 1,166,509,339.0 | 4,250,939.9 | 4.159x | 1317.769x |

#### `wild-waf-crs-942360-concat-sqli` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 702,149.3 | 0.6696 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 1,701,537.2 | 1.6227 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,703,248.2 | 1.6243 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,865,451.3 | 1.7790 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 9,260,683.1 | 8.8317 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 9,332,702.9 | 8.9004 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 13,147,462.7 | 12.5384 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 36,887,165.5 | 35.1783 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 36,838,225.5 | 35.1317 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 105,556,164.5 | 100.6662 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 173,570,529.5 | 165.5298 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 212,573,634.0 | 202.7260 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 882,783,148.0 | 841.8876 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 149,164.9 | 0.5690 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 423,991.9 | 1.6174 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 425,660.0 | 1.6238 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 468,468.4 | 1.7871 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 2,324,202.2 | 8.8661 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 2,327,984.1 | 8.8806 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 3,260,497.4 | 12.4378 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 9,163,840.5 | 34.9573 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 9,192,720.2 | 35.0674 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 26,400,943.5 | 100.7116 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 43,361,729.5 | 165.4119 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 53,060,016.0 | 202.4079 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 221,954,228.0 | 846.6882 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 28,235.7 | 0.4308 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 120,903.2 | 1.8448 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 120,044.4 | 1.8317 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 119,788.0 | 1.8278 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 578,292.8 | 8.8240 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 579,189.9 | 8.8377 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 809,212.9 | 12.3476 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 2,287,211.5 | 34.9001 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 2,300,933.7 | 35.1095 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 6,596,653.5 | 100.6569 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 10,841,341.5 | 165.4257 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 13,330,219.0 | 203.4030 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 55,695,713.0 | 849.8491 |

### `wild-waf-crs-942360-concat-sqli` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 4,583.6 | 4,573.4 | 4,629.5 | 20.7 | 0.021x | 1.000x | 75 | 61.1 | 27.2 | 100% |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 4,812.2 | 4,807.9 | 4,854.4 | 17.1 | 0.022x | 1.050x | 75 | 64.2 | 16.4 | 100% |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 7,379.0 | 7,350.5 | 8,020.1 | 311.5 | 0.033x | 1.610x | 75 | 98.4 | 8.9 | 100% |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 7,417.1 | 7,363.7 | 7,455.2 | 31.8 | 0.033x | 1.618x | 75 | 98.9 | 8.9 | 100% |
| 5 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,587.6 | 9,552.7 | 9,857.9 | 112.0 | 0.043x | 2.092x | 75 | 127.8 | 100.0 | 100% |
| 6 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 9,625.2 | 9,613.1 | 9,639.8 | 9.1 | 0.043x | 2.100x | 75 | 128.3 | 100.2 | 100% |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 17,073.0 | 17,050.5 | 17,185.9 | 48.4 | 0.077x | 3.725x | 75 | 227.6 | 40.4 | 100% |
| 8 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 48,527.2 | 48,465.9 | 48,605.6 | 50.3 | 0.219x | 10.587x | 75 | 647.0 | 17.3 | 100% |
| 9 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 48,602.4 | 48,559.5 | 48,832.8 | 99.4 | 0.219x | 10.603x | 75 | 648.0 | 18.0 | 100% |
| 10 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 142,711.4 | 142,421.2 | 142,970.4 | 186.6 | 0.643x | 31.135x | 75 | 1,902.8 | 58.6 | 100% |
| 11 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 182,782.9 | 182,597.5 | 189,777.2 | 2,801.2 | 0.823x | 39.877x | 75 | 2,437.1 | 30.4 | 100% |
| 12 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 222,001.6 | 220,391.7 | 233,793.2 | 4,999.2 | 1.000x | 48.434x | 75 | 2,960.0 | 34.4 | 100% |

### `wild-waf-crs-942500-comment-obfuscation` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 23,121.0 | 0.0168 | 23,098.2 | 23,149.6 | 17.7 | 0.010x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 23,179.6 | 0.0168 | 23,157.2 | 23,239.3 | 27.9 | 0.010x | 1.003x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 41,251.5 | 0.0300 | 41,172.7 | 41,305.9 | 47.8 | 0.018x | 1.784x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 51,801.2 | 0.0376 | 51,769.8 | 52,147.3 | 145.0 | 0.022x | 2.240x |
| 5 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 60,189.8 | 0.0437 | 60,164.4 | 60,402.4 | 89.9 | 0.026x | 2.603x |
| 6 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 439,147.6 | 0.3191 | 438,846.7 | 440,586.2 | 637.6 | 0.187x | 18.993x |
| 7 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 440,033.2 | 0.3197 | 439,026.3 | 440,551.3 | 514.3 | 0.187x | 19.032x |
| 8 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 1,498,130.6 | 1.0886 | 1,497,611.9 | 1,500,676.9 | 1,094.7 | 0.636x | 64.795x |
| 9 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 1,949,356.0 | 1.4164 | 1,946,978.9 | 2,139,020.4 | 75,884.2 | 0.828x | 84.311x |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,354,099.0 | 1.7105 | 2,353,756.3 | 2,354,931.7 | 462.2 | 1.000x | 101.817x |
| 11 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,087,733.9 | 2.9702 | 4,084,230.2 | 4,106,608.0 | 9,414.0 | 1.736x | 176.798x |
| 12 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,090,716.3 | 2.9724 | 4,088,479.0 | 4,100,492.8 | 4,449.4 | 1.738x | 176.927x |

#### `wild-waf-crs-942500-comment-obfuscation` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 17,617.7 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 17,688.0 | 0.0169 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 31,349.4 | 0.0299 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,482.4 | 0.0377 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 45,782.7 | 0.0437 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 331,221.7 | 0.3159 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 330,973.4 | 0.3156 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,141,170.5 | 1.0883 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,491,673.6 | 1.4226 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 1,802,863.1 | 1.7193 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,115,367.6 | 2.9710 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,117,679.4 | 2.9733 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 4,387.5 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 4,379.1 | 0.0167 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 7,868.7 | 0.0300 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 9,807.9 | 0.0374 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 11,465.1 | 0.0437 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 82,981.8 | 0.3166 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 83,098.3 | 0.3170 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 285,299.8 | 1.0883 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 369,613.0 | 1.4100 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 446,632.5 | 1.7038 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 777,658.2 | 2.9665 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 778,691.4 | 2.9705 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 1,112.2 | 0.0170 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,107.2 | 0.0169 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 2,013.4 | 0.0307 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 2,512.8 | 0.0383 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 2,937.4 | 0.0448 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 24,908.9 | 0.3801 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 25,263.2 | 0.3855 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 71,488.8 | 1.0908 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 86,656.1 | 1.3223 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 104,594.7 | 1.5960 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 193,015.6 | 2.9452 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 193,542.4 | 2.9532 |

- not ranked: `tre_0.9.0_default-caps-simdna` — did-not-compile (tre_regncompb failed (code 11): Invalid character range)

### `wild-waf-crs-942500-comment-obfuscation` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 736.3 | 735.5 | 737.9 | 0.8 | 0.220x | 1.000x | 75 | 9.8 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 750.1 | 749.6 | 753.8 | 1.9 | 0.224x | 1.019x | 75 | 10.0 | 8.9 | 100% |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,355.5 | 2,351.8 | 2,361.1 | 3.7 | 0.704x | 3.199x | 75 | 31.4 | 27.2 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,422.3 | 2,362.4 | 2,505.9 | 45.9 | 0.724x | 3.290x | 75 | 32.3 | 16.4 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,811.0 | 2,805.6 | 3,107.5 | 143.4 | 0.840x | 3.818x | 75 | 37.5 | 40.4 | 100% |
| 6 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 3,237.0 | 3,212.2 | 4,395.7 | 458.3 | 0.967x | 4.397x | 75 | 43.2 | 30.4 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,347.3 | 3,337.3 | 3,365.6 | 11.8 | 1.000x | 4.546x | 75 | 44.6 | 34.4 | 100% |
| 8 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,885.2 | 3,875.5 | 3,914.5 | 13.9 | 1.161x | 5.277x | 75 | 51.8 | 58.6 | 100% |
| 9 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,761.1 | 4,666.0 | 4,859.0 | 64.0 | 1.422x | 6.467x | 75 | 63.5 | 18.0 | 100% |
| 10 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,822.2 | 4,778.1 | 4,860.0 | 30.5 | 1.441x | 6.550x | 75 | 64.3 | 17.3 | 100% |
| 11 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 8,296.2 | 8,234.9 | 8,726.7 | 197.1 | 2.478x | 11.268x | 75 | 110.6 | 100.2 | 100% |
| 12 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 8,422.8 | 8,232.6 | 8,709.3 | 178.5 | 2.516x | 11.440x | 75 | 112.3 | 100.0 | 100% |

- not ranked: `tre_0.9.0_default-caps-simdna` — did-not-compile (tre_regncompb failed (code 11): Invalid character range)

### `winpath-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 20.1 | 0.0000 | 20.0 | 20.2 | 0.1 | 0.075x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 20.2 | 0.0000 | 20.2 | 20.7 | 0.2 | 0.076x | 1.005x |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 94.2 | 0.0001 | 93.4 | 111.8 | 7.1 | 0.352x | 4.680x |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 96.0 | 0.0001 | 94.1 | 99.5 | 1.8 | 0.358x | 4.768x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 119.8 | 0.0001 | 109.8 | 123.4 | 5.2 | 0.447x | 5.949x |
| 6 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 133.2 | 0.0001 | 133.0 | 133.7 | 0.3 | 0.497x | 6.615x |
| 7 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 265.1 | 0.0002 | 264.5 | 269.7 | 1.9 | 0.989x | 13.166x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 268.0 | 0.0002 | 266.9 | 268.8 | 0.8 | 1.000x | 13.311x |
| 9 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 294.5 | 0.0002 | 292.2 | 300.8 | 2.9 | 1.099x | 14.629x |
| 10 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 300.5 | 0.0002 | 294.6 | 352.1 | 21.1 | 1.121x | 14.925x |
| 11 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,914,817.4 | 3.5712 | 4,892,943.4 | 4,921,085.2 | 11,087.3 | 18337.573x | 244099.927x |
| 12 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,925,305.2 | 3.5788 | 4,901,848.0 | 5,036,487.9 | 47,447.0 | 18376.704x | 244620.815x |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 10,186,248.8 | 7.4014 | 10,179,917.6 | 10,232,577.4 | 20,502.3 | 38005.702x | 505911.489x |

#### `winpath-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 6.8 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 6.8 | 0.0000 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 31.5 | 0.0000 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 28.2 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 41.2 | 0.0000 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 44.1 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 88.1 | 0.0001 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 89.3 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 90.8 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 93.7 | 0.0001 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,739,979.2 | 3.5667 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,750,099.6 | 3.5764 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 7,756,042.3 | 7.3967 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 6.6 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 6.8 | 0.0000 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 31.2 | 0.0001 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 32.2 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 39.4 | 0.0002 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 44.3 | 0.0002 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 87.9 | 0.0003 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 89.4 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 92.1 | 0.0004 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 94.2 | 0.0004 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 933,554.1 | 3.5612 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 935,327.0 | 3.5680 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 1,942,251.4 | 7.4091 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 6.8 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 6.7 | 0.0001 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 31.2 | 0.0005 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 35.3 | 0.0005 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 39.0 | 0.0006 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 44.8 | 0.0007 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 89.3 | 0.0014 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 89.6 | 0.0014 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 112.0 | 0.0017 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 113.5 | 0.0017 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 237,362.2 | 3.6219 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 235,054.8 | 3.5867 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 487,053.9 | 7.4319 |

### `winpath-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 499.9 | 499.0 | 520.5 | 8.2 | 0.108x | 1.000x | 75 | 6.7 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 500.7 | 500.2 | 501.6 | 0.6 | 0.108x | 1.002x | 75 | 6.7 | 8.9 | 100% |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,471.6 | 1,461.4 | 1,472.9 | 4.6 | 0.318x | 2.944x | 75 | 19.6 | 27.2 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,796.4 | 1,794.7 | 2,389.5 | 237.3 | 0.388x | 3.594x | 75 | 24.0 | 16.4 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,848.0 | 2,779.5 | 3,490.7 | 304.5 | 0.615x | 5.697x | 75 | 38.0 | 40.4 | 100% |
| 6 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,927.0 | 2,925.5 | 4,037.8 | 443.9 | 0.632x | 5.855x | 75 | 39.0 | 58.6 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,634.3 | 4,604.7 | 4,664.7 | 19.9 | 1.000x | 9.270x | 75 | 61.8 | 34.4 | 100% |
| 8 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 5,444.9 | 5,403.3 | 5,916.1 | 193.1 | 1.175x | 10.892x | 75 | 72.6 | 30.4 | 100% |
| 9 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 6,167.3 | 6,157.3 | 6,175.9 | 6.2 | 1.331x | 12.337x | 75 | 82.2 | 18.0 | 100% |
| 10 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 6,183.4 | 6,174.5 | 6,198.3 | 8.5 | 1.334x | 12.369x | 75 | 82.4 | 17.3 | 100% |
| 11 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 6,930.6 | 6,872.6 | 6,980.6 | 40.1 | 1.496x | 13.864x | 75 | 92.4 | 100.0 | 100% |
| 12 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 6,946.4 | 6,875.9 | 6,965.2 | 33.8 | 1.499x | 13.895x | 75 | 92.6 | 100.2 | 100% |
| 13 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 25,811.7 | 25,755.9 | 26,039.7 | 100.9 | 5.570x | 51.633x | 75 | 344.2 | 27.9 | 100% |

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `email-nested-plus` | `short-subject-search` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 75 | 93% | -2:PCREC_ERR_STEPS×5 (smallest: v-uuid-badnibble, 36 B) | 0 | `sd-empty-alt-hit` (gave-up), `sd-empty-alt-miss` (gave-up), `sec-github-pat` (gave-up), `v-uuid-badnibble` (gave-up), `v-uuid-valid` (gave-up) |
| `email-nested-plus` | `short-subject-search` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 75 | 93% | -2:PCREC_ERR_STEPS×5 (smallest: v-uuid-badnibble, 36 B) | 0 | `sd-empty-alt-hit` (gave-up), `sd-empty-alt-miss` (gave-up), `sec-github-pat` (gave-up), `v-uuid-badnibble` (gave-up), `v-uuid-valid` (gave-up) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 75 | 97% | 0 | 10 | `rd-evil-alt-near-miss` (wrong), `sd-empty-alt-hit` (wrong) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 75 | 97% | -47:match×2 (smallest: rd-evil-alt-near-miss, 18 B) | 0 | `rd-evil-alt-near-miss` (gave-up), `sd-empty-alt-hit` (gave-up) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 75 | 97% | -47:match×2 (smallest: rd-evil-alt-near-miss, 18 B) | 0 | `rd-evil-alt-near-miss` (gave-up), `sd-empty-alt-hit` (gave-up) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 75 | 97% | -17:retry×2 (smallest: rd-evil-alt-near-miss, 18 B) | 0 | `rd-evil-alt-near-miss` (gave-up), `sd-empty-alt-hit` (gave-up) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 75 | 97% | -2:PCREC_ERR_STEPS×2 (smallest: rd-evil-alt-near-miss, 18 B) | 0 | `rd-evil-alt-near-miss` (gave-up), `sd-empty-alt-hit` (gave-up) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 75 | 97% | 0 | 10 | `rd-evil-alt-near-miss` (wrong), `sd-empty-alt-hit` (wrong) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 75 | 97% | -2:PCREC_ERR_STEPS×2 (smallest: rd-evil-alt-near-miss, 18 B) | 0 | `rd-evil-alt-near-miss` (gave-up), `sd-empty-alt-hit` (gave-up) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 75 | 97% | -2:PCREC_ERR_STEPS×2 (smallest: rd-evil-alt-near-miss, 18 B) | 0 | `rd-evil-alt-near-miss` (gave-up), `sd-empty-alt-hit` (gave-up) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `re2_11.0.0_default-caps-simdna` | 75 | 97% | 0 | 10 | `rd-evil-alt-near-miss` (wrong), `sd-empty-alt-hit` (wrong) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `re2_11.0.0_longest-caps-simdna` | 75 | 97% | 0 | 10 | `rd-evil-alt-near-miss` (wrong), `sd-empty-alt-hit` (wrong) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `rust_1.13.1_default-caps-simdna` | 75 | 97% | 0 | 10 | `rd-evil-alt-near-miss` (wrong), `sd-empty-alt-hit` (wrong) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `tre_0.9.0_default-caps-simdna` | 75 | 97% | 0 | 10 | `rd-evil-alt-near-miss` (wrong), `sd-empty-alt-hit` (wrong) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 75 | 97% | 0 | 10 | `rd-evil-alt-near-miss` (wrong), `sd-empty-alt-hit` (wrong) |
| `file-ext-order` | `short-subject-search` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 75 | 99% | 0 | 5 | `sd-fileext-short` (wrong) |
| `file-ext-order` | `short-subject-search` | `plain` | `re2_11.0.0_longest-caps-simdna` | 75 | 99% | 0 | 5 | `sd-fileext-short` (wrong) |
| `file-ext-order` | `short-subject-search` | `plain` | `tre_0.9.0_default-caps-simdna` | 75 | 99% | 0 | 5 | `sd-fileext-short` (wrong) |
| `high-byte-run` | `large-subject-throughput` | `plain` | `tre_0.9.0_default-caps-simdna` | 3 | 0% | 0 | 15 | `t-1m` (wrong), `t-256k` (wrong), `t-64k` (wrong) |
| `high-byte-run` | `short-subject-search` | `plain` | `rust_1.13.1_default-caps-simdna` | 75 | 97% | 0 | 10 | `nu-high-byte` (wrong), `nu-lead-with-cont` (wrong) |
| `high-byte-run` | `short-subject-search` | `plain` | `tre_0.9.0_default-caps-simdna` | 75 | 48% | 0 | 195 | `br-dup-param` (wrong), `br-palindrome` (wrong), `cg-number` (wrong), `dt-iso8601` (wrong), `dt-prose-month` (wrong), `la-currency` (wrong), `la-float-bound` (wrong), `la-float-dotted` (wrong), `la-pwd-strong` (wrong), `la-pwd-weak` (wrong), `lp-num-leadzero` (wrong), `lp-num-neg-dec` (wrong), `lp-syslog` (wrong), `lp-winpath` (wrong), `lp-winpath-reserved` (wrong), `nu-high-byte` (wrong), `nu-lead-with-cont` (wrong), `rd-date-hit` (wrong), `rd-email-hit` (wrong), `rd-numeric-id-hit` (wrong), `rd-numeric-id-near-miss` (wrong), `rd-phone-list-hit` (wrong), `rec-array-define` (wrong), `rec-tag-depth3` (wrong), `sec-aws-key` (wrong), `sec-github-pat` (wrong), `sec-slack-webhook` (wrong), `v-ipv4` (wrong), `v-ipv4-oor` (wrong), `v-us-zip` (wrong), `v-us-zip-plus4` (wrong), `v-uuid-badnibble` (wrong), `v-uuid-valid` (wrong), `waf-benign` (wrong), `waf-comment-obfuscation` (wrong), `waf-concat` (wrong), `waf-dbnames` (wrong), `waf-sleep` (wrong), `waf-union` (wrong) |
| `keyword-prefix-order` | `short-subject-search` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 75 | 99% | 0 | 5 | `sd-keyword-short` (wrong) |
| `keyword-prefix-order` | `short-subject-search` | `plain` | `re2_11.0.0_longest-caps-simdna` | 75 | 99% | 0 | 5 | `sd-keyword-short` (wrong) |
| `keyword-prefix-order` | `short-subject-search` | `plain` | `tre_0.9.0_default-caps-simdna` | 75 | 99% | 0 | 5 | `sd-keyword-short` (wrong) |
| `mojibake-curly-quote` | `short-subject-search` | `plain` | `tre_0.9.0_default-caps-simdna` | 75 | 99% | 0 | 5 | `nu-mojibake` (wrong) |
| `negation-scope-lookbehind-var` | `large-subject-throughput` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 3 | 0% | -42:pattern×3 (smallest: t-64k, 65,536 B) | 0 | `t-1m` (gave-up), `t-256k` (gave-up), `t-64k` (gave-up) |
| `negation-scope-lookbehind-var` | `short-subject-search` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 75 | 80% | -42:pattern×15 (smallest: sd-fileext-short, 14 B) | 0 | `la-negation-hit` (gave-up), `la-negation-miss` (gave-up), `lp-atomic-hit` (gave-up), `lp-atomic-nonmatch` (gave-up), `lp-syslog` (gave-up), `sd-fileext-short` (gave-up), `sec-slack-webhook` (gave-up), `sec-userpass` (gave-up), `v-email` (gave-up), `v-uuid-badnibble` (gave-up), `v-uuid-valid` (gave-up), `waf-benign` (gave-up), `waf-concat` (gave-up), `waf-dbnames` (gave-up), `waf-union` (gave-up) |
| `router-prefix-order` | `short-subject-search` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 75 | 99% | 0 | 5 | `sd-router-short` (wrong) |
| `router-prefix-order` | `short-subject-search` | `plain` | `re2_11.0.0_longest-caps-simdna` | 75 | 99% | 0 | 5 | `sd-router-short` (wrong) |
| `router-prefix-order` | `short-subject-search` | `plain` | `tre_0.9.0_default-caps-simdna` | 75 | 99% | 0 | 5 | `sd-router-short` (wrong) |
| `tag-depth3-bound` | `short-subject-search` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 75 | 96% | -42:pattern×3 (smallest: br-tag-pair, 18 B) | 0 | `br-tag-mismatch` (gave-up), `br-tag-pair` (gave-up), `rec-tag-depth3` (gave-up) |
| `tag-pair-match` | `short-subject-search` | `plain` | `tre_0.9.0_default-caps-simdna` | 75 | 99% | 0 | 5 | `br-tag-pair` (wrong) |
| `wild-logparse-quotedstring-grok` | `short-subject-search` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 75 | 99% | 0 | 5 | `lp-quoted-escaped` (wrong) |
| `wild-waf-crs-942360-concat-sqli` | `short-subject-search` | `plain` | `tre_0.9.0_default-caps-simdna` | 75 | 99% | 0 | 5 | `waf-union` (wrong) |

## Compile cost (by execution-model class; never pooled across classes)

### `compiled-aot`

- `pcrec_25b1984f_auto-caps-simdna` / `balanced-parens-rec` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,049 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_25b1984f_auto-caps-simdna` / `balanced-parens-rec` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,259 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_25b1984f_auto-caps-simdna` / `base10num-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `base10num-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `bracket-array-define` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,395 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_25b1984f_auto-caps-simdna` / `bracket-array-define` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,500 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_25b1984f_auto-caps-simdna` / `codegrammar-flat` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,601 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `codegrammar-flat` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,704 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `codegrammar-xflag` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,658 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `codegrammar-xflag` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,763 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `currency-lookbehind-fixed` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,586 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/5 == stamped default (single tier), buffers=5/5 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `currency-lookbehind-fixed` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,691 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/5 == stamped default (single tier), buffers=5/5 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `date-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 8,024 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `date-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 8,129 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `doubled-word` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,982 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/6 == stamped default (single tier), buffers=3/6 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `doubled-word` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,087 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/6 == stamped default (single tier), buffers=3/6 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `dup-param-detect` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,721 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `dup-param-detect` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,826 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `email-local-nodup` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,816 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/7 == stamped default (single tier), buffers=5/7 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `email-local-nodup` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,921 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/7 == stamped default (single tier), buffers=5/7 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `email-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,299 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `email-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,404 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `evil-alt-nested` / `plain`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,147 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `evil-alt-nested` / `whole-subject`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,252 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `file-ext-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `file-ext-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `float-literal-bound` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=2 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,425 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/6 == stamped default (single tier), buffers=5/6 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `float-literal-bound` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,530 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/6 == stamped default (single tier), buffers=5/6 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `floor-byte` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `floor-byte` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `high-byte-run` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=4 (match: 2), start=reverse-pass, folds=2, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `high-byte-run` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `ipv4-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `ipv4-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `keyword-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `keyword-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `logparse-atomic` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 16,167 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `logparse-atomic` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 16,272 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `logparse-atomic-removed` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 15,757 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `logparse-atomic-removed` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 15,862 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `mojibake-curly-quote` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `mojibake-curly-quote` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `nested-comment-rec` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,432 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=46/70 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_25b1984f_auto-caps-simdna` / `nested-comment-rec` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,537 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=46/70 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_25b1984f_auto-caps-simdna` / `numeric-id-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 2,986 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `numeric-id-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,091 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `phone-list-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,110 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `phone-list-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,215 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `phone-palindrome-6` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,952 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `phone-palindrome-6` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 4,057 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `pwd-strength-chain` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 7,830 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `pwd-strength-chain` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 7,935 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `quoted-delim-match` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,139 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `quoted-delim-match` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,244 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `router-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `router-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `tag-depth3-bound` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `tag-depth3-bound` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 11,054 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `tag-pair-match` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,740 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `tag-pair-match` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,845 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `trim-nested-star` / `plain`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,800 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `trim-nested-star` / `whole-subject`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,905 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `utf8-lead-no-cont` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,206 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/3 == stamped default (single tier), buffers=2/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `utf8-lead-no-cont` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,309 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/3 == stamped default (single tier), buffers=2/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `uuid-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `uuid-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-codegrammar-json-array-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-codegrammar-json-array-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-codegrammar-json-constant` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-codegrammar-json-constant` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-codegrammar-json-number-extended` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-codegrammar-json-object-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-codegrammar-json-object-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-codegrammar-json-stringcontent-escape` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-datetime-moment-iso8601` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,575 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=14/11 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-datetime-moment-iso8601` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,680 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=14/11 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-logparse-base10num-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 5,399 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/4 == stamped default (single tier), buffers=5/4 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-logparse-base10num-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 5,507 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/4 == stamped default (single tier), buffers=5/4 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-logparse-base10num-noatomic` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,989 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/3 == stamped default (single tier), buffers=5/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-logparse-base10num-noatomic` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 5,094 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/3 == stamped default (single tier), buffers=5/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-logparse-quotedstring-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 18,844 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=60/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-logparse-quotedstring-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 18,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=60/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-logparse-quotedstring-noatomic` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,216 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-logparse-quotedstring-noatomic` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,321 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-logparse-syslogbase-expanded` / `plain`: engine=vm, sel=size-cap-retry (DFA fallback tripped), entry=plain entry, vm_prefilter=hybrid, lang=count-collapsed (size cap retry, exact 1463025 > 1000000), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 301,112 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=19/29 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-logparse-syslogbase-expanded` / `whole-subject`: engine=vm, sel=size-cap-retry (DFA fallback tripped), entry=plain entry, vm_prefilter=hybrid, lang=count-collapsed (size cap retry, exact 1484232 > 1000000), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 301,221 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=19/29 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-logparse-winpath-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,590 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-logparse-winpath-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,696 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-secrets-aws-access-key-id` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=1, shape=plain (prog: 7,403 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=8/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-secrets-aws-access-key-id` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=1, shape=plain (prog: 7,508 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=8/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-secrets-github-pat` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,6*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 3,330 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-secrets-github-pat` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,6*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 3,435 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-secrets-slack-webhook-url` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,6*, edge=mixed, edges=3 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=plain (prog: 8,624 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-secrets-slack-webhook-url` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,6*, edge=mixed, edges=3 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=plain (prog: 8,729 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-secrets-username-password-pair` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class table=mixed offsets=none, edge=range, edges=2 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=2, shape=plain (prog: 19,664 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-secrets-username-password-pair` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=mixed offsets=none, edge=range, edges=2 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=2, shape=plain (prog: 19,769 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=range, edges=0 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,439 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,544 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-validator-email-owasp` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-validator-email-owasp` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-validator-ipv4-owasp` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 14,007 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-validator-ipv4-owasp` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 14,112 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-validator-us-zip-owasp` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 2,173 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=2/4 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-validator-us-zip-owasp` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 2,276 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=2/4 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-validator-uuid-grok` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,8*,13, edge=bitmap, edges=8 (match: 4), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-validator-uuid-grok` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,8*,13, edge=bitmap, edges=8 (match: 4), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-waf-crs-942140-dbnames` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=mixed, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-waf-crs-942140-dbnames` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=mixed, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-waf-crs-942270-union-select` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-waf-crs-942270-union-select` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-waf-crs-942360-concat-sqli` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-waf-crs-942360-concat-sqli` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-waf-crs-942500-comment-obfuscation` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-waf-crs-942500-comment-obfuscation` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `winpath-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `winpath-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `balanced-parens-rec` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,049 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_25b1984f_auto-nocaps-simdna` / `balanced-parens-rec` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,259 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_25b1984f_auto-nocaps-simdna` / `base10num-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `base10num-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `bracket-array-define` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,395 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_25b1984f_auto-nocaps-simdna` / `bracket-array-define` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,500 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_25b1984f_auto-nocaps-simdna` / `codegrammar-flat` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `codegrammar-flat` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `codegrammar-xflag` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `codegrammar-xflag` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `currency-lookbehind-fixed` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,586 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/5 == stamped default (single tier), buffers=5/5 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `currency-lookbehind-fixed` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,691 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/5 == stamped default (single tier), buffers=5/5 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `date-nested-plus` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `date-nested-plus` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `doubled-word` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,982 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/6 == stamped default (single tier), buffers=3/6 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `doubled-word` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,087 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/6 == stamped default (single tier), buffers=3/6 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `dup-param-detect` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,721 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `dup-param-detect` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,826 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `email-local-nodup` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,816 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/7 == stamped default (single tier), buffers=5/7 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `email-local-nodup` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,921 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/7 == stamped default (single tier), buffers=5/7 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `email-nested-plus` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `email-nested-plus` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `evil-alt-nested` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `evil-alt-nested` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `file-ext-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `file-ext-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `float-literal-bound` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=2 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,425 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/6 == stamped default (single tier), buffers=5/6 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `float-literal-bound` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,530 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/6 == stamped default (single tier), buffers=5/6 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `floor-byte` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `floor-byte` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `high-byte-run` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=4 (match: 2), start=reverse-pass, folds=2, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `high-byte-run` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `ipv4-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `ipv4-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `keyword-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `keyword-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `logparse-atomic` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 15,914 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/2 == stamped default (single tier), buffers=1/2 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `logparse-atomic` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 16,019 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/2 == stamped default (single tier), buffers=1/2 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `logparse-atomic-removed` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `logparse-atomic-removed` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `mojibake-curly-quote` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `mojibake-curly-quote` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `nested-comment-rec` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,432 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=46/70 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_25b1984f_auto-nocaps-simdna` / `nested-comment-rec` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,537 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=46/70 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_25b1984f_auto-nocaps-simdna` / `numeric-id-nested-plus` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `numeric-id-nested-plus` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `phone-list-nested-plus` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `phone-list-nested-plus` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `phone-palindrome-6` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,952 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `phone-palindrome-6` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 4,057 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `pwd-strength-chain` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 7,830 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `pwd-strength-chain` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 7,935 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `quoted-delim-match` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,139 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `quoted-delim-match` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,244 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `router-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `router-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `tag-depth3-bound` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `tag-depth3-bound` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 11,054 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `tag-pair-match` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,740 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `tag-pair-match` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,845 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `trim-nested-star` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `trim-nested-star` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `utf8-lead-no-cont` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,206 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/3 == stamped default (single tier), buffers=2/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `utf8-lead-no-cont` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,309 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/3 == stamped default (single tier), buffers=2/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `uuid-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `uuid-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-codegrammar-json-array-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-codegrammar-json-array-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-codegrammar-json-constant` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-codegrammar-json-constant` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-codegrammar-json-number-extended` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-codegrammar-json-object-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-codegrammar-json-object-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-codegrammar-json-stringcontent-escape` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-datetime-datefinder-alternation` / `plain`: engine=dfa, sel=size-cap-retry (DFA fallback tripped), entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=2 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-datetime-moment-iso8601` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-datetime-moment-iso8601` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-logparse-base10num-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 5,399 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/4 == stamped default (single tier), buffers=5/4 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-logparse-base10num-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 5,507 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/4 == stamped default (single tier), buffers=5/4 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-logparse-base10num-noatomic` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,989 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/3 == stamped default (single tier), buffers=5/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-logparse-base10num-noatomic` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 5,094 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/3 == stamped default (single tier), buffers=5/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-logparse-quotedstring-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 18,844 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=60/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-logparse-quotedstring-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 18,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=60/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-logparse-quotedstring-noatomic` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,216 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-logparse-quotedstring-noatomic` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,321 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-logparse-syslogbase-expanded` / `plain`: engine=vm, sel=size-cap-retry (DFA fallback tripped), entry=plain entry, vm_prefilter=hybrid, lang=count-collapsed (size cap retry, exact 1419282 > 1000000), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 257,968 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=47/70 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-logparse-syslogbase-expanded` / `whole-subject`: engine=vm, sel=size-cap-retry (DFA fallback tripped), entry=plain entry, vm_prefilter=hybrid, lang=count-collapsed (size cap retry, exact 1440489 > 1000000), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 258,077 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=47/70 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-logparse-winpath-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,590 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-logparse-winpath-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,696 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-secrets-aws-access-key-id` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-secrets-aws-access-key-id` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-secrets-github-pat` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,6*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-secrets-github-pat` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,6*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-secrets-slack-webhook-url` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,6*, edge=mixed, edges=3 (match: 3), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-secrets-slack-webhook-url` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,6*, edge=mixed, edges=3 (match: 3), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-secrets-username-password-pair` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=mixed offsets=none, edge=range, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-secrets-username-password-pair` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=mixed offsets=none, edge=range, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=range, edges=0 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-validator-email-owasp` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-validator-email-owasp` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-validator-ipv4-owasp` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-validator-ipv4-owasp` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-validator-us-zip-owasp` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-validator-us-zip-owasp` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-validator-uuid-grok` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,8*,13, edge=bitmap, edges=8 (match: 4), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-validator-uuid-grok` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,8*,13, edge=bitmap, edges=8 (match: 4), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-waf-crs-942140-dbnames` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=mixed, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-waf-crs-942140-dbnames` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=mixed, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-waf-crs-942270-union-select` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-waf-crs-942270-union-select` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-waf-crs-942360-concat-sqli` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-waf-crs-942360-concat-sqli` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-waf-crs-942500-comment-obfuscation` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-waf-crs-942500-comment-obfuscation` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `winpath-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `winpath-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_vm-caps-simdna` / `balanced-parens-rec` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,049 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_25b1984f_vm-caps-simdna` / `balanced-parens-rec` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,259 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_25b1984f_vm-caps-simdna` / `base10num-near-miss` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,040 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=3/1 == stamped default (single tier), buffers=3/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `base10num-near-miss` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,145 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=3/1 == stamped default (single tier), buffers=3/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `bracket-array-define` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,395 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_25b1984f_vm-caps-simdna` / `bracket-array-define` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,500 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_25b1984f_vm-caps-simdna` / `codegrammar-flat` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,601 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `codegrammar-flat` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,704 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `codegrammar-xflag` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,658 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `codegrammar-xflag` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,763 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `currency-lookbehind-fixed` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,586 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/5 == stamped default (single tier), buffers=5/5 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `currency-lookbehind-fixed` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,691 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/5 == stamped default (single tier), buffers=5/5 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `date-nested-plus` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 8,024 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `date-nested-plus` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 8,129 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `doubled-word` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,982 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/6 == stamped default (single tier), buffers=3/6 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `doubled-word` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,087 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/6 == stamped default (single tier), buffers=3/6 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `dup-param-detect` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,721 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `dup-param-detect` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,826 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `email-local-nodup` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,816 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/7 == stamped default (single tier), buffers=5/7 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `email-local-nodup` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,921 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/7 == stamped default (single tier), buffers=5/7 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `email-nested-plus` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,299 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `email-nested-plus` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,404 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `evil-alt-nested` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,147 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `evil-alt-nested` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,252 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `file-ext-order` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,449 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=2/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `file-ext-order` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,554 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=2/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `float-literal-bound` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,425 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/6 == stamped default (single tier), buffers=5/6 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `float-literal-bound` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,530 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/6 == stamped default (single tier), buffers=5/6 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `floor-byte` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 237 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `floor-byte` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 340 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `high-byte-run` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 647 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `high-byte-run` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 750 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `ipv4-near-miss` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 13,695 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=13/5 == stamped default (single tier), buffers=13/5 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `ipv4-near-miss` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 13,800 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=13/5 == stamped default (single tier), buffers=13/5 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `keyword-prefix-order` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,930 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=2/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `keyword-prefix-order` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 2,035 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=2/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `logparse-atomic` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=2, shape=plain (prog: 16,167 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `logparse-atomic` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=2, shape=plain (prog: 16,272 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `logparse-atomic-removed` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=2, shape=plain (prog: 15,757 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `logparse-atomic-removed` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=2, shape=plain (prog: 15,862 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `mojibake-curly-quote` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 970 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `mojibake-curly-quote` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 1,073 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `nested-comment-rec` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,432 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=46/70 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_25b1984f_vm-caps-simdna` / `nested-comment-rec` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,537 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=46/70 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_25b1984f_vm-caps-simdna` / `numeric-id-nested-plus` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 2,986 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `numeric-id-nested-plus` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,091 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `phone-list-nested-plus` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,110 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `phone-list-nested-plus` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,215 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `phone-palindrome-6` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,952 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `phone-palindrome-6` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 4,057 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `pwd-strength-chain` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 7,830 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `pwd-strength-chain` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 7,935 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `quoted-delim-match` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,139 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `quoted-delim-match` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,244 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `router-prefix-order` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,291 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=2/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `router-prefix-order` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,396 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=2/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `tag-depth3-bound` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `tag-depth3-bound` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 11,054 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `tag-pair-match` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,740 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `tag-pair-match` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,845 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `trim-nested-star` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,800 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `trim-nested-star` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,905 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `utf8-lead-no-cont` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,206 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/3 == stamped default (single tier), buffers=2/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `utf8-lead-no-cont` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,309 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/3 == stamped default (single tier), buffers=2/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `uuid-near-miss` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=shared (prog: 4,685 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `uuid-near-miss` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=shared (prog: 4,790 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-codegrammar-json-array-begin` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 236 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-codegrammar-json-array-begin` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 339 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-codegrammar-json-constant` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=1, shape=forward (prog: 3,481 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-codegrammar-json-constant` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=1, shape=forward (prog: 3,586 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-codegrammar-json-number-extended` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,852 B), clsfolds=1, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/1 == stamped default (single tier), buffers=5/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-codegrammar-json-object-begin` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 237 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-codegrammar-json-object-begin` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 340 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-codegrammar-json-stringcontent-escape` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,487 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=2/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-datetime-moment-iso8601` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 15,575 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=14/11 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-datetime-moment-iso8601` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 15,680 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=14/11 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-logparse-base10num-grok` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,399 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/4 == stamped default (single tier), buffers=5/4 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-logparse-base10num-grok` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,507 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/4 == stamped default (single tier), buffers=5/4 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-logparse-base10num-noatomic` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,989 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/3 == stamped default (single tier), buffers=5/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-logparse-base10num-noatomic` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,094 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/3 == stamped default (single tier), buffers=5/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-logparse-quotedstring-grok` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 18,844 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=60/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-logparse-quotedstring-grok` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 18,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=60/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-logparse-quotedstring-noatomic` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 15,216 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-logparse-quotedstring-noatomic` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 15,321 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-logparse-syslogbase-expanded` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 301,112 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=19/29 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-logparse-syslogbase-expanded` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 301,221 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=19/29 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-logparse-winpath-grok` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,590 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-logparse-winpath-grok` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,696 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-secrets-aws-access-key-id` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=1, shape=plain (prog: 7,403 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=8/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-secrets-aws-access-key-id` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=1, shape=plain (prog: 7,508 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=8/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-secrets-github-pat` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,330 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-secrets-github-pat` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,435 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-secrets-slack-webhook-url` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=plain (prog: 8,624 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-secrets-slack-webhook-url` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=plain (prog: 8,729 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-secrets-username-password-pair` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=2, shape=plain (prog: 19,664 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-secrets-username-password-pair` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=2, shape=plain (prog: 19,769 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,290 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=2/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,395 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=2/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 728 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 831 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,439 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,544 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-validator-email-owasp` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,616 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-validator-email-owasp` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,721 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-validator-ipv4-owasp` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 14,007 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-validator-ipv4-owasp` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 14,112 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-validator-us-zip-owasp` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 2,173 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=2/4 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-validator-us-zip-owasp` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 2,276 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=2/4 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-validator-uuid-grok` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 2,549 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-validator-uuid-grok` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 2,652 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-waf-crs-942140-dbnames` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 41,952 B), clsfolds=23, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=15/2 == stamped default (single tier), buffers=15/2 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-waf-crs-942140-dbnames` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 42,059 B), clsfolds=23, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=15/2 == stamped default (single tier), buffers=15/2 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 6,899 B), clsfolds=12, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=4/3 == stamped default (single tier), buffers=4/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 7,004 B), clsfolds=12, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=4/3 == stamped default (single tier), buffers=4/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-waf-crs-942270-union-select` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,138 B), clsfolds=12, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/3 == stamped default (single tier), buffers=3/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-waf-crs-942270-union-select` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,243 B), clsfolds=12, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/3 == stamped default (single tier), buffers=3/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-waf-crs-942360-concat-sqli` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 170,600 B), clsfolds=26, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=29/3 == stamped default (single tier), buffers=29/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-waf-crs-942360-concat-sqli` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 170,707 B), clsfolds=26, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=29/3 == stamped default (single tier), buffers=29/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-waf-crs-942500-comment-obfuscation` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 2,934 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=3/2 == stamped default (single tier), buffers=3/2 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-waf-crs-942500-comment-obfuscation` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,039 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=3/2 == stamped default (single tier), buffers=3/2 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `winpath-near-miss` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 2,925 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `winpath-near-miss` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,030 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `balanced-parens-rec` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,049 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=40
- `pcrec_25b1984f_vm-in-caps-simdna` / `balanced-parens-rec` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,259 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=40
- `pcrec_25b1984f_vm-in-caps-simdna` / `base10num-near-miss` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,040 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=3/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `base10num-near-miss` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,145 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=3/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `bracket-array-define` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,395 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=40
- `pcrec_25b1984f_vm-in-caps-simdna` / `bracket-array-define` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,500 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=40
- `pcrec_25b1984f_vm-in-caps-simdna` / `codegrammar-flat` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,601 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `codegrammar-flat` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,704 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `codegrammar-xflag` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,658 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `codegrammar-xflag` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,763 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `currency-lookbehind-fixed` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,586 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/5 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `currency-lookbehind-fixed` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,691 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/5 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `date-nested-plus` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 8,024 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `date-nested-plus` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 8,129 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `doubled-word` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,982 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/6 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `doubled-word` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,087 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/6 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `dup-param-detect` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,721 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `dup-param-detect` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,826 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `email-local-nodup` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,816 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/7 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `email-local-nodup` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,921 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/7 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `email-nested-plus` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,299 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `email-nested-plus` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,404 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `evil-alt-nested` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,147 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `evil-alt-nested` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,252 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `file-ext-order` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,449 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `file-ext-order` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,554 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `float-literal-bound` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,425 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/6 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `float-literal-bound` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,530 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/6 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `floor-byte` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 237 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `floor-byte` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 340 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `high-byte-run` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 647 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `high-byte-run` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 750 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `ipv4-near-miss` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 13,695 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=13/5 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `ipv4-near-miss` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 13,800 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=13/5 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `keyword-prefix-order` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,930 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `keyword-prefix-order` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 2,035 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `logparse-atomic` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=2, shape=plain (prog: 16,167 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `logparse-atomic` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=2, shape=plain (prog: 16,272 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `logparse-atomic-removed` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=2, shape=plain (prog: 15,757 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `logparse-atomic-removed` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=2, shape=plain (prog: 15,862 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `mojibake-curly-quote` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 970 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `mojibake-curly-quote` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 1,073 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `nested-comment-rec` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,432 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=46/70 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=40
- `pcrec_25b1984f_vm-in-caps-simdna` / `nested-comment-rec` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,537 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=46/70 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=40
- `pcrec_25b1984f_vm-in-caps-simdna` / `numeric-id-nested-plus` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 2,986 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `numeric-id-nested-plus` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,091 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `phone-list-nested-plus` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,110 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `phone-list-nested-plus` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,215 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `phone-palindrome-6` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,952 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `phone-palindrome-6` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 4,057 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `pwd-strength-chain` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 7,830 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `pwd-strength-chain` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 7,935 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `quoted-delim-match` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,139 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `quoted-delim-match` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,244 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `router-prefix-order` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,291 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `router-prefix-order` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,396 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `tag-depth3-bound` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `tag-depth3-bound` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 11,054 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `tag-pair-match` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,740 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `tag-pair-match` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,845 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `trim-nested-star` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,800 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `trim-nested-star` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,905 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `utf8-lead-no-cont` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,206 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `utf8-lead-no-cont` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,309 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `uuid-near-miss` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=shared (prog: 4,685 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `uuid-near-miss` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=shared (prog: 4,790 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-codegrammar-json-array-begin` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 236 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-codegrammar-json-array-begin` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 339 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-codegrammar-json-constant` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=1, shape=forward (prog: 3,481 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-codegrammar-json-constant` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=1, shape=forward (prog: 3,586 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-codegrammar-json-number-extended` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,852 B), clsfolds=1, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-codegrammar-json-object-begin` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 237 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-codegrammar-json-object-begin` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 340 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-codegrammar-json-stringcontent-escape` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,487 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-datetime-moment-iso8601` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 15,575 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-datetime-moment-iso8601` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 15,680 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-logparse-base10num-grok` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,399 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/4 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-logparse-base10num-grok` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,507 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/4 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-logparse-base10num-noatomic` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,989 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-logparse-base10num-noatomic` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,094 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-logparse-quotedstring-grok` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 18,844 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=60/91 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-logparse-quotedstring-grok` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 18,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=60/91 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-logparse-quotedstring-noatomic` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 15,216 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-logparse-quotedstring-noatomic` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 15,321 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-logparse-syslogbase-expanded` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 301,112 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=19/29 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-logparse-syslogbase-expanded` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 301,221 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=19/29 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-logparse-winpath-grok` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,590 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-logparse-winpath-grok` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,696 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-secrets-aws-access-key-id` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=1, shape=plain (prog: 7,403 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-secrets-aws-access-key-id` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=1, shape=plain (prog: 7,508 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-secrets-github-pat` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,330 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-secrets-github-pat` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,435 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-secrets-slack-webhook-url` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=plain (prog: 8,624 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-secrets-slack-webhook-url` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=plain (prog: 8,729 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-secrets-username-password-pair` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=2, shape=plain (prog: 19,664 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-secrets-username-password-pair` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=2, shape=plain (prog: 19,769 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,290 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,395 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 728 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 831 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,439 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,544 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-validator-email-owasp` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,616 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-validator-email-owasp` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,721 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-validator-ipv4-owasp` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 14,007 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-validator-ipv4-owasp` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 14,112 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-validator-us-zip-owasp` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 2,173 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-validator-us-zip-owasp` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 2,276 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-validator-uuid-grok` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 2,549 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-validator-uuid-grok` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 2,652 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-waf-crs-942140-dbnames` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 41,952 B), clsfolds=23, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=15/2 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-waf-crs-942140-dbnames` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 42,059 B), clsfolds=23, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=15/2 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 6,899 B), clsfolds=12, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=4/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 7,004 B), clsfolds=12, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=4/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-waf-crs-942270-union-select` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,138 B), clsfolds=12, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-waf-crs-942270-union-select` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,243 B), clsfolds=12, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-waf-crs-942360-concat-sqli` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 170,600 B), clsfolds=26, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=29/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-waf-crs-942360-concat-sqli` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 170,707 B), clsfolds=26, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=29/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-waf-crs-942500-comment-obfuscation` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 2,934 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=3/2 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-waf-crs-942500-comment-obfuscation` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,039 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=3/2 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `winpath-near-miss` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 2,925 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `winpath-near-miss` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,030 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
    - sel = pcrec's `RX_ENGINE_SEL`; `DFA fallback tripped` = sel not in (selected, forced), and NOTHING else -- since pcrec 263b013 ([LIM-1] / [OPT-4.1]) every fallback has its own token (`overflowed-dfa`, `overflowed-prefilter`, `collapsed-prefilter`, `declined-nullable`, `size-cap-retry`), the size-cap rescue included; at pcrec 96e44c2 that rescue stamped `sel=selected` and only its `lang=count-collapsed (size cap retry, ...)` clause says so.
    - `prefilter declined, no cap hit` = pcrec abi 14's `declined-nullable-default` ([OPT-4.2]): the SAME ask-(b) bucket (sel is neither `selected` nor `forced`) but NOTHING overflowed -- no rung was involved, and the ordinary hybrid's own EXACT prefilter language is nullable, so the prefilter was declined. pcrec's own reading keeps it out of the five `fell back` values for that reason (match_api.md 6.3); this column keeps it in the bucket and says which reading it is, so a row is never read as a cap that was hit. Such an artifact carries `vm_prefilter=none` and NO `lang=` clause.
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
| `balanced-parens-rec` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 205,463,827.0 | 197,997,236.0 | 207,083,314.0 | 4,007,532.0 | 5 | 27,360 | 24,163 | 23,932 | 0.020 | compiled=5 | 1,527,996.0 | 202,051,243.0 | 99,411.0 |
| `balanced-parens-rec` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 205,006,324.0 | 196,987,471.0 | 209,551,794.0 | 4,800,704.9 | 5 | 27,360 | 24,381 | 24,150 | 0.023 | compiled=5 | 1,558,177.0 | 203,329,457.0 | 107,830.0 |
| `balanced-parens-rec` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 203,133,853.0 | 197,382,872.0 | 206,488,721.0 | 3,331,837.7 | 5 | 27,360 | 24,163 | 23,932 | 0.016 | compiled=5 | 1,532,848.0 | 201,671,255.0 | 106,690.0 |
| `balanced-parens-rec` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 196,869,539.0 | 187,204,888.0 | 206,094,349.0 | 6,879,124.5 | 5 | 27,360 | 24,381 | 24,150 | 0.035 | compiled=5 | 1,523,828.0 | 195,247,741.0 | 116,871.0 |
| `balanced-parens-rec` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 206,051,324.0 | 204,441,295.0 | 209,462,043.0 | 1,782,920.6 | 5 | 27,360 | 24,161 | 23,930 | 0.009 | compiled=5 | 1,546,769.0 | 204,322,514.0 | 192,151.0 |
| `balanced-parens-rec` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 207,099,270.0 | 203,013,407.0 | 215,259,736.0 | 4,037,676.0 | 5 | 27,360 | 24,379 | 24,148 | 0.019 | compiled=5 | 1,599,799.0 | 204,548,165.0 | 201,941.0 |
| `balanced-parens-rec` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 205,822,331.0 | 197,795,883.0 | 218,269,167.0 | 7,302,891.8 | 5 | 27,360 | 24,161 | 23,930 | 0.035 | compiled=5 | 2,826,167.0 | 203,203,566.0 | 117,531.0 |
| `balanced-parens-rec` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 204,826,376.0 | 198,344,607.0 | 208,915,161.0 | 4,156,579.3 | 5 | 27,360 | 24,379 | 24,148 | 0.020 | compiled=5 | 1,575,389.0 | 203,093,256.0 | 100,511.0 |
| `base10num-near-miss` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 146,589,357.0 | 136,207,965.0 | 148,569,075.0 | 4,392,601.4 | 5 | 23,376 | 15,211 | 12,826 | 0.030 | compiled=5 | 2,998,012.0 | 143,250,453.0 | 99,900.0 |
| `base10num-near-miss` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 139,877,710.0 | 137,085,469.0 | 145,130,991.0 | 2,920,416.8 | 5 | 23,296 | 14,664 | 12,279 | 0.021 | compiled=5 | 1,489,566.0 | 138,189,473.0 | 107,551.0 |
| `base10num-near-miss` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 145,924,821.0 | 143,116,036.0 | 150,489,975.0 | 2,863,368.3 | 5 | 23,376 | 15,211 | 12,826 | 0.020 | compiled=5 | 1,517,928.0 | 144,305,632.0 | 104,800.0 |
| `base10num-near-miss` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 143,319,747.0 | 131,571,015.0 | 144,791,705.0 | 5,184,634.3 | 5 | 23,296 | 14,664 | 12,279 | 0.036 | compiled=5 | 1,553,798.0 | 141,578,608.0 | 187,611.0 |
| `base10num-near-miss` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 184,747,072.0 | 178,162,972.0 | 195,792,355.0 | 6,532,630.3 | 5 | 27,200 | 21,142 | 21,142 | 0.035 (max is trial 1) | compiled=5 | 1,695,780.0 | 183,128,112.0 | 194,371.0 |
| `base10num-near-miss` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 175,553,337.0 | 168,096,476.0 | 186,678,942.0 | 6,722,691.5 | 5 | 27,200 | 21,255 | 21,255 | 0.038 | compiled=5 | 1,532,849.0 | 173,963,819.0 | 107,170.0 |
| `base10num-near-miss` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 183,504,509.0 | 176,266,786.0 | 186,088,763.0 | 3,819,491.6 | 5 | 27,200 | 21,142 | 21,142 | 0.021 | compiled=5 | 1,559,640.0 | 181,830,859.0 | 101,701.0 |
| `base10num-near-miss` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 184,674,425.0 | 177,553,084.0 | 195,673,161.0 | 6,448,082.4 | 5 | 27,200 | 21,255 | 21,255 | 0.035 | compiled=5 | 3,121,739.0 | 183,009,555.0 | 182,841.0 |
| `bracket-array-define` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 215,719,468.0 | 215,211,017.0 | 217,397,374.0 | 912,347.1 | 5 | 27,400 | 24,958 | 24,643 | 0.004 | compiled=5 | 1,579,507.0 | 213,697,530.0 | 101,670.0 |
| `bracket-array-define` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 215,479,967.0 | 206,984,002.0 | 218,605,970.0 | 4,180,238.5 | 5 | 27,400 | 25,071 | 24,756 | 0.019 (max is trial 1) | compiled=5 | 1,590,496.0 | 213,563,689.0 | 111,581.0 |
| `bracket-array-define` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 212,079,429.0 | 204,399,910.0 | 212,893,214.0 | 3,191,905.1 | 5 | 27,400 | 24,959 | 24,643 | 0.015 | compiled=5 | 1,572,668.0 | 210,406,991.0 | 108,991.0 |
| `bracket-array-define` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 213,592,528.0 | 205,791,686.0 | 214,409,052.0 | 3,207,582.0 | 5 | 27,400 | 25,072 | 24,756 | 0.015 | compiled=5 | 1,657,888.0 | 211,747,898.0 | 188,091.0 |
| `bracket-array-define` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 217,738,991.0 | 209,612,464.0 | 222,508,879.0 | 4,244,647.1 | 5 | 27,400 | 24,956 | 24,641 | 0.019 | compiled=5 | 1,570,389.0 | 216,051,892.0 | 194,831.0 |
| `bracket-array-define` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 213,937,551.0 | 208,711,319.0 | 221,002,160.0 | 4,424,946.8 | 5 | 27,400 | 25,069 | 24,754 | 0.021 | compiled=5 | 1,549,999.0 | 210,543,560.0 | 118,601.0 |
| `bracket-array-define` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 215,489,641.0 | 210,414,989.0 | 217,956,663.0 | 2,628,192.4 | 5 | 27,400 | 24,956 | 24,641 | 0.012 | compiled=5 | 1,807,561.0 | 213,583,239.0 | 101,820.0 |
| `bracket-array-define` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 215,336,529.0 | 214,623,784.0 | 218,178,977.0 | 1,417,790.0 | 5 | 27,400 | 25,069 | 24,754 | 0.007 | compiled=5 | 1,611,130.0 | 213,647,439.0 | 109,030.0 |
| `codegrammar-flat` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 347,490,695.0 | 341,432,440.0 | 349,816,404.0 | 2,826,295.3 | 5 | 31,808 | 34,144 | 25,545 | 0.008 | compiled=5 | 2,010,348.0 | 344,716,413.0 | 101,661.0 |
| `codegrammar-flat` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 354,063,182.0 | 347,198,474.0 | 356,179,871.0 | 3,866,174.6 | 5 | 31,856 | 33,865 | 26,353 | 0.011 | compiled=5 | 1,998,928.0 | 350,867,219.0 | 184,531.0 |
| `codegrammar-flat` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 173,009,903.0 | 167,162,754.0 | 177,358,637.0 | 3,818,328.2 | 5 | 27,832 | 28,185 | 15,235 | 0.022 | compiled=5 | 2,088,421.0 | 170,523,331.0 | 184,211.0 |
| `codegrammar-flat` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 169,035,971.0 | 168,061,368.0 | 170,894,283.0 | 1,048,875.6 | 5 | 27,888 | 26,435 | 15,884 | 0.006 (max is trial 1) | compiled=5 | 2,015,301.0 | 166,659,220.0 | 101,440.0 |
| `codegrammar-flat` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 310,730,136.0 | 303,969,368.0 | 321,041,154.0 | 5,477,170.6 | 5 | 27,200 | 21,230 | 20,768 | 0.018 | compiled=5 | 1,550,999.0 | 309,008,836.0 | 208,041.0 |
| `codegrammar-flat` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 309,723,520.0 | 309,325,177.0 | 316,589,629.0 | 2,768,512.5 | 5 | 27,200 | 21,341 | 20,879 | 0.009 | compiled=5 | 1,555,359.0 | 307,981,370.0 | 112,371.0 |
| `codegrammar-flat` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 310,766,200.0 | 303,393,287.0 | 313,159,555.0 | 3,539,086.3 | 5 | 27,200 | 21,230 | 20,768 | 0.011 | compiled=5 | 1,556,589.0 | 309,106,150.0 | 109,080.0 |
| `codegrammar-flat` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 317,778,382.0 | 315,939,102.0 | 317,933,212.0 | 785,481.7 | 5 | 27,200 | 21,341 | 20,879 | 0.002 | compiled=5 | 1,562,609.0 | 315,124,137.0 | 99,261.0 |
| `codegrammar-xflag` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 347,956,406.0 | 340,959,558.0 | 351,445,952.0 | 3,491,862.3 | 5 | 31,848 | 34,470 | 25,792 | 0.010 (max is trial 1) | compiled=5 | 2,041,918.0 | 345,717,317.0 | 187,671.0 |
| `codegrammar-xflag` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 357,313,215.0 | 346,990,543.0 | 364,599,025.0 | 6,282,092.9 | 5 | 31,896 | 34,193 | 26,602 | 0.018 | compiled=5 | 1,997,379.0 | 352,783,996.0 | 104,511.0 |
| `codegrammar-xflag` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 179,383,597.0 | 170,901,542.0 | 185,825,211.0 | 5,078,761.1 | 5 | 27,872 | 28,462 | 15,432 | 0.028 | compiled=5 | 4,231,762.0 | 175,376,266.0 | 212,681.0 |
| `codegrammar-xflag` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 168,262,409.0 | 161,272,692.0 | 175,837,019.0 | 5,687,662.8 | 5 | 27,928 | 26,712 | 16,081 | 0.034 (max is trial 1) | compiled=5 | 2,047,211.0 | 166,008,867.0 | 190,811.0 |
| `codegrammar-xflag` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 309,478,239.0 | 301,883,736.0 | 313,389,932.0 | 4,211,328.7 | 5 | 27,240 | 21,556 | 21,015 | 0.014 (max is trial 1) | compiled=5 | 1,781,520.0 | 307,823,839.0 | 99,080.0 |
| `codegrammar-xflag` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 316,178,976.0 | 311,171,077.0 | 317,583,554.0 | 2,222,465.6 | 5 | 27,240 | 21,669 | 21,128 | 0.007 | compiled=5 | 1,601,319.0 | 314,374,986.0 | 193,771.0 |
| `codegrammar-xflag` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 313,256,265.0 | 308,984,058.0 | 325,334,867.0 | 5,886,069.0 | 5 | 27,240 | 21,556 | 21,015 | 0.019 | compiled=5 | 1,696,780.0 | 311,428,395.0 | 105,291.0 |
| `codegrammar-xflag` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 314,220,312.0 | 312,384,720.0 | 327,733,442.0 | 5,920,335.7 | 5 | 27,240 | 21,669 | 21,128 | 0.019 | compiled=5 | 3,017,298.0 | 312,575,321.0 | 191,841.0 |
| `currency-lookbehind-fixed` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 219,159,942.0 | 217,990,648.0 | 227,495,616.0 | 3,592,721.7 | 5 | 31,824 | 31,432 | 25,801 | 0.016 | compiled=5 | 1,876,597.0 | 217,098,354.0 | 171,821.0 |
| `currency-lookbehind-fixed` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 220,916,008.0 | 216,199,681.0 | 233,311,230.0 | 6,392,716.3 | 5 | 31,920 | 33,458 | 27,209 | 0.029 | compiled=5 | 1,924,577.0 | 218,905,121.0 | 167,711.0 |
| `currency-lookbehind-fixed` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 221,322,619.0 | 219,491,750.0 | 223,188,719.0 | 1,286,240.2 | 5 | 31,824 | 31,432 | 25,801 | 0.006 | compiled=5 | 1,893,270.0 | 219,327,508.0 | 108,641.0 |
| `currency-lookbehind-fixed` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 226,122,403.0 | 219,056,197.0 | 229,838,884.0 | 3,550,914.8 | 5 | 31,920 | 33,458 | 27,209 | 0.016 | compiled=5 | 2,247,752.0 | 223,751,811.0 | 102,060.0 |
| `currency-lookbehind-fixed` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 197,122,593.0 | 186,154,900.0 | 201,577,239.0 | 6,149,342.1 | 5 | 27,288 | 21,621 | 21,390 | 0.031 (max is trial 1) | compiled=5 | 1,660,389.0 | 194,749,549.0 | 188,261.0 |
| `currency-lookbehind-fixed` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 195,494,343.0 | 188,122,371.0 | 197,073,673.0 | 3,988,571.3 | 5 | 27,288 | 21,734 | 21,503 | 0.020 | compiled=5 | 1,546,419.0 | 192,631,457.0 | 201,021.0 |
| `currency-lookbehind-fixed` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 196,422,626.0 | 189,622,225.0 | 216,334,864.0 | 8,962,613.1 | 5 | 27,288 | 21,621 | 21,390 | 0.046 (max is trial 1) | compiled=5 | 1,671,690.0 | 194,636,536.0 | 114,400.0 |
| `currency-lookbehind-fixed` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 195,848,542.0 | 195,453,710.0 | 199,167,142.0 | 1,365,145.0 | 5 | 27,288 | 21,734 | 21,503 | 0.007 | compiled=5 | 1,595,809.0 | 194,057,492.0 | 105,671.0 |
| `date-nested-plus` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 255,330,369.0 | 247,762,888.0 | 263,360,472.0 | 5,085,920.9 | 5 | 31,696 | 32,258 | 30,232 | 0.020 | compiled=5 | 3,585,315.0 | 253,439,741.0 | 189,141.0 |
| `date-nested-plus` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 254,062,874.0 | 246,185,372.0 | 258,774,104.0 | 4,353,407.4 | 5 | 31,696 | 32,186 | 30,160 | 0.017 | compiled=5 | 1,752,487.0 | 252,221,716.0 | 193,181.0 |
| `date-nested-plus` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 138,777,781.0 | 128,539,729.0 | 141,784,518.0 | 4,611,872.6 | 5 | 23,184 | 13,194 | 11,399 | 0.033 | compiled=5 | 1,490,607.0 | 135,688,596.0 | 113,740.0 |
| `date-nested-plus` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 136,282,691.0 | 128,835,600.0 | 142,193,991.0 | 4,583,462.5 | 5 | 23,184 | 13,017 | 11,222 | 0.034 | compiled=5 | 1,481,588.0 | 133,163,884.0 | 105,591.0 |
| `date-nested-plus` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 242,874,376.0 | 232,141,215.0 | 243,537,099.0 | 4,654,540.7 | 5 | 27,400 | 27,830 | 27,599 | 0.019 | compiled=5 | 1,619,919.0 | 241,149,926.0 | 105,451.0 |
| `date-nested-plus` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 243,387,419.0 | 238,663,862.0 | 244,610,085.0 | 2,206,931.9 | 5 | 27,400 | 27,943 | 27,712 | 0.009 | compiled=5 | 1,652,189.0 | 241,564,099.0 | 190,511.0 |
| `date-nested-plus` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 244,606,654.0 | 242,927,134.0 | 246,209,794.0 | 1,114,114.0 | 5 | 27,400 | 27,830 | 27,599 | 0.005 | compiled=5 | 1,636,310.0 | 242,156,390.0 | 99,620.0 |
| `date-nested-plus` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 243,189,587.0 | 237,129,970.0 | 253,225,007.0 | 5,468,436.5 | 5 | 27,400 | 27,943 | 27,712 | 0.022 | compiled=5 | 1,638,220.0 | 241,479,366.0 | 100,371.0 |
| `doubled-word` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 214,276,943.0 | 213,801,250.0 | 216,618,601.0 | 1,204,972.3 | 5 | 27,328 | 23,220 | 22,758 | 0.006 | compiled=5 | 1,549,527.0 | 212,619,575.0 | 107,841.0 |
| `doubled-word` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 212,624,036.0 | 205,105,285.0 | 214,454,233.0 | 4,184,929.8 | 5 | 27,328 | 23,333 | 22,871 | 0.020 (max is trial 1) | compiled=5 | 1,568,536.0 | 210,745,938.0 | 100,880.0 |
| `doubled-word` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 201,931,757.0 | 192,662,199.0 | 211,904,489.0 | 7,294,197.7 | 5 | 27,328 | 23,202 | 22,740 | 0.036 | compiled=5 | 1,542,718.0 | 200,205,467.0 | 211,201.0 |
| `doubled-word` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 211,244,246.0 | 202,114,168.0 | 215,089,025.0 | 4,274,289.2 | 5 | 27,328 | 23,315 | 22,853 | 0.020 | compiled=5 | 1,578,129.0 | 209,527,836.0 | 98,920.0 |
| `doubled-word` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 213,302,176.0 | 198,766,132.0 | 214,119,150.0 | 6,087,954.4 | 5 | 27,328 | 23,218 | 22,756 | 0.029 | compiled=5 | 1,560,559.0 | 211,482,205.0 | 189,151.0 |
| `doubled-word` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 212,599,242.0 | 212,230,900.0 | 215,699,380.0 | 1,352,496.9 | 5 | 27,328 | 23,331 | 22,869 | 0.006 | compiled=5 | 1,554,679.0 | 210,863,532.0 | 192,481.0 |
| `doubled-word` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 213,551,638.0 | 206,367,515.0 | 219,757,225.0 | 4,859,612.6 | 5 | 27,328 | 23,218 | 22,756 | 0.023 | compiled=5 | 1,565,019.0 | 211,889,779.0 | 99,040.0 |
| `doubled-word` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 206,005,783.0 | 204,786,656.0 | 220,487,610.0 | 6,242,525.1 | 5 | 27,328 | 23,331 | 22,869 | 0.030 | compiled=5 | 1,575,549.0 | 204,050,261.0 | 195,471.0 |
| `dup-param-detect` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 227,431,176.0 | 224,932,975.0 | 230,883,040.0 | 2,096,150.9 | 5 | 27,448 | 25,774 | 25,312 | 0.009 | compiled=5 | 1,634,527.0 | 225,725,129.0 | 113,970.0 |
| `dup-param-detect` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 222,419,676.0 | 221,550,451.0 | 231,631,124.0 | 4,233,876.7 | 5 | 27,448 | 25,887 | 25,425 | 0.019 | compiled=5 | 3,114,763.0 | 219,194,522.0 | 187,901.0 |
| `dup-param-detect` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 229,875,904.0 | 218,243,423.0 | 244,065,010.0 | 9,765,969.8 | 5 | 27,448 | 25,756 | 25,294 | 0.042 | compiled=5 | 3,238,387.0 | 226,402,465.0 | 222,771.0 |
| `dup-param-detect` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 225,208,000.0 | 224,267,494.0 | 225,927,383.0 | 530,319.9 | 5 | 27,448 | 25,869 | 25,407 | 0.002 | compiled=5 | 1,613,468.0 | 223,215,148.0 | 189,161.0 |
| `dup-param-detect` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 220,997,720.0 | 217,251,799.0 | 227,461,338.0 | 4,250,213.8 | 5 | 27,448 | 25,772 | 25,310 | 0.019 | compiled=5 | 1,626,969.0 | 219,175,360.0 | 100,010.0 |
| `dup-param-detect` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 226,664,062.0 | 221,517,733.0 | 238,772,342.0 | 6,251,351.4 | 5 | 27,448 | 25,885 | 25,423 | 0.028 | compiled=5 | 1,632,520.0 | 224,857,792.0 | 191,141.0 |
| `dup-param-detect` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 227,005,589.0 | 224,381,304.0 | 227,609,282.0 | 1,129,543.2 | 5 | 27,448 | 25,772 | 25,310 | 0.005 | compiled=5 | 1,654,120.0 | 225,178,358.0 | 190,101.0 |
| `dup-param-detect` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 228,727,249.0 | 226,763,368.0 | 236,930,158.0 | 3,605,965.7 | 5 | 27,448 | 25,885 | 25,423 | 0.016 | compiled=5 | 1,643,940.0 | 226,988,209.0 | 188,011.0 |
| `email-local-nodup` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 203,092,367.0 | 193,205,407.0 | 206,291,480.0 | 4,526,588.2 | 5 | 31,536 | 25,764 | 23,691 | 0.022 | compiled=5 | 1,642,236.0 | 200,730,317.0 | 105,580.0 |
| `email-local-nodup` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 196,098,139.0 | 189,341,111.0 | 201,609,791.0 | 4,817,190.6 | 5 | 31,536 | 26,182 | 24,038 | 0.025 | compiled=5 | 1,678,237.0 | 194,319,401.0 | 188,781.0 |
| `email-local-nodup` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 194,654,158.0 | 192,505,716.0 | 196,775,469.0 | 1,395,655.5 | 5 | 31,536 | 25,764 | 23,691 | 0.007 | compiled=5 | 1,870,399.0 | 192,960,769.0 | 108,121.0 |
| `email-local-nodup` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 197,584,763.0 | 189,864,543.0 | 200,652,469.0 | 3,780,182.0 | 5 | 31,536 | 26,182 | 24,038 | 0.019 | compiled=5 | 1,629,269.0 | 195,848,034.0 | 107,460.0 |
| `email-local-nodup` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 186,720,722.0 | 186,315,361.0 | 195,321,932.0 | 3,491,592.2 | 5 | 27,280 | 22,104 | 21,642 | 0.019 | compiled=5 | 1,602,569.0 | 184,846,602.0 | 201,741.0 |
| `email-local-nodup` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 198,315,489.0 | 188,396,633.0 | 205,094,398.0 | 5,959,898.6 | 5 | 27,240 | 22,217 | 21,755 | 0.030 | compiled=5 | 1,659,710.0 | 194,136,745.0 | 190,111.0 |
| `email-local-nodup` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 184,990,318.0 | 182,792,654.0 | 195,824,742.0 | 5,581,354.8 | 5 | 27,280 | 22,104 | 21,642 | 0.030 (max is trial 1) | compiled=5 | 1,571,750.0 | 181,831,738.0 | 187,431.0 |
| `email-local-nodup` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 194,514,685.0 | 185,361,880.0 | 196,712,068.0 | 3,969,042.6 | 5 | 27,240 | 22,217 | 21,755 | 0.020 | compiled=5 | 1,561,380.0 | 192,759,834.0 | 198,631.0 |
| `email-nested-plus` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 220,148,677.0 | 218,384,809.0 | 222,570,616.0 | 1,376,035.5 | 5 | 31,648 | 27,640 | 25,694 | 0.006 | compiled=5 | 1,753,457.0 | 217,610,475.0 | 108,050.0 |
| `email-nested-plus` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 219,486,083.0 | 213,853,481.0 | 233,872,664.0 | 6,995,164.9 | 5 | 31,648 | 28,071 | 26,041 | 0.032 | compiled=5 | 1,686,867.0 | 217,689,876.0 | 191,721.0 |
| `email-nested-plus` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 135,165,214.0 | 127,580,943.0 | 139,747,168.0 | 4,409,590.1 | 5 | 23,184 | 12,699 | 10,984 | 0.033 | compiled=5 | 1,441,487.0 | 132,111,548.0 | 200,291.0 |
| `email-nested-plus` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 127,471,293.0 | 121,724,773.0 | 136,161,450.0 | 5,335,165.9 | 5 | 23,184 | 13,025 | 11,226 | 0.042 | compiled=5 | 1,494,038.0 | 124,995,900.0 | 196,591.0 |
| `email-nested-plus` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 209,472,724.0 | 205,994,454.0 | 211,030,142.0 | 1,727,395.8 | 5 | 27,360 | 23,711 | 23,480 | 0.008 (max is trial 1) | compiled=5 | 1,631,779.0 | 207,660,584.0 | 189,201.0 |
| `email-nested-plus` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 204,345,574.0 | 202,313,001.0 | 210,879,623.0 | 3,527,060.8 | 5 | 27,360 | 23,824 | 23,593 | 0.017 (max is trial 1) | compiled=5 | 1,556,909.0 | 202,792,285.0 | 193,852.0 |
| `email-nested-plus` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 208,954,090.0 | 200,297,599.0 | 211,171,364.0 | 3,989,232.6 | 5 | 27,360 | 23,711 | 23,480 | 0.019 | compiled=5 | 1,550,710.0 | 207,217,340.0 | 191,581.0 |
| `email-nested-plus` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 206,659,768.0 | 194,099,712.0 | 210,835,643.0 | 6,156,486.5 | 5 | 27,360 | 23,824 | 23,593 | 0.030 (max is trial 1) | compiled=5 | 1,560,950.0 | 205,011,137.0 | 98,360.0 |
| `evil-alt-nested` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 213,165,138.0 | 210,619,158.0 | 216,620,944.0 | 1,936,225.1 | 5 | 27,360 | 24,177 | 24,177 | 0.009 (max is trial 1) | compiled=5 | 1,546,866.0 | 211,518,831.0 | 112,201.0 |
| `evil-alt-nested` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 215,207,346.0 | 210,873,939.0 | 220,492,818.0 | 3,529,819.2 | 5 | 27,360 | 24,290 | 24,290 | 0.016 | compiled=5 | 1,862,418.0 | 211,504,851.0 | 192,261.0 |
| `evil-alt-nested` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 128,603,360.0 | 122,204,685.0 | 141,120,635.0 | 7,367,101.6 | 5 | 23,144 | 12,686 | 11,075 | 0.057 | compiled=5 | 1,438,707.0 | 125,762,444.0 | 203,121.0 |
| `evil-alt-nested` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 129,835,625.0 | 125,177,081.0 | 139,986,428.0 | 5,192,541.1 | 5 | 23,104 | 12,509 | 10,898 | 0.040 (max is trial 1) | compiled=5 | 1,479,717.0 | 128,476,928.0 | 117,511.0 |
| `evil-alt-nested` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 206,589,128.0 | 196,450,308.0 | 215,328,899.0 | 7,616,621.8 | 5 | 27,360 | 24,158 | 24,158 | 0.037 | compiled=5 | 1,641,090.0 | 205,125,969.0 | 98,230.0 |
| `evil-alt-nested` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 205,671,471.0 | 204,528,285.0 | 211,543,666.0 | 2,594,458.1 | 5 | 27,360 | 24,271 | 24,271 | 0.013 (max is trial 1) | compiled=5 | 1,552,829.0 | 203,887,651.0 | 107,020.0 |
| `evil-alt-nested` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 212,950,964.0 | 197,525,162.0 | 215,926,333.0 | 6,609,663.5 | 5 | 27,360 | 24,158 | 24,158 | 0.031 | compiled=5 | 3,008,948.0 | 211,207,274.0 | 101,701.0 |
| `evil-alt-nested` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 210,146,259.0 | 203,519,589.0 | 219,429,924.0 | 5,786,166.4 | 5 | 27,360 | 24,271 | 24,271 | 0.028 | compiled=5 | 1,543,019.0 | 208,393,728.0 | 109,570.0 |
| `file-ext-order` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 153,953,646.0 | 140,286,702.0 | 158,343,615.0 | 6,277,707.6 | 5 | 27,608 | 19,438 | 13,315 | 0.041 | compiled=5 | 1,805,297.0 | 149,673,999.0 | 190,821.0 |
| `file-ext-order` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 155,234,772.0 | 152,250,710.0 | 163,430,356.0 | 4,680,813.4 | 5 | 27,752 | 22,398 | 15,332 | 0.030 | compiled=5 | 1,874,058.0 | 153,457,404.0 | 99,991.0 |
| `file-ext-order` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 148,780,147.0 | 147,209,347.0 | 152,939,328.0 | 1,918,570.7 | 5 | 27,608 | 19,438 | 13,315 | 0.013 | compiled=5 | 1,819,060.0 | 145,337,767.0 | 107,611.0 |
| `file-ext-order` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 162,662,728.0 | 151,453,110.0 | 171,973,557.0 | 6,539,695.7 | 5 | 27,752 | 22,398 | 15,332 | 0.040 | compiled=5 | 2,187,091.0 | 158,441,137.0 | 198,531.0 |
| `file-ext-order` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 169,351,973.0 | 161,664,869.0 | 172,539,791.0 | 4,147,124.6 | 5 | 23,104 | 19,314 | 19,314 | 0.024 | compiled=5 | 1,589,539.0 | 166,608,688.0 | 104,191.0 |
| `file-ext-order` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 170,284,258.0 | 162,114,751.0 | 173,444,226.0 | 3,824,455.0 | 5 | 23,104 | 19,427 | 19,427 | 0.022 (max is trial 1) | compiled=5 | 1,483,788.0 | 168,600,309.0 | 190,631.0 |
| `file-ext-order` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 170,589,701.0 | 156,795,100.0 | 177,795,784.0 | 7,811,706.8 | 5 | 23,104 | 19,314 | 19,314 | 0.046 | compiled=5 | 1,585,030.0 | 168,787,410.0 | 211,741.0 |
| `file-ext-order` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 171,862,868.0 | 163,119,627.0 | 173,410,178.0 | 3,792,540.4 | 5 | 23,104 | 19,427 | 19,427 | 0.022 (max is trial 1) | compiled=5 | 1,585,189.0 | 170,059,378.0 | 122,431.0 |
| `float-literal-bound` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 234,406,524.0 | 223,670,621.0 | 245,882,522.0 | 8,041,623.5 | 5 | 31,752 | 32,214 | 27,065 | 0.034 | compiled=5 | 3,783,735.0 | 232,274,105.0 | 120,811.0 |
| `float-literal-bound` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 231,634,123.0 | 231,289,082.0 | 235,869,970.0 | 1,724,733.1 | 5 | 31,848 | 33,056 | 27,598 | 0.007 (max is trial 1) | compiled=5 | 1,915,418.0 | 229,635,295.0 | 100,390.0 |
| `float-literal-bound` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 234,866,860.0 | 233,326,773.0 | 236,923,691.0 | 1,436,901.9 | 5 | 31,752 | 32,214 | 27,065 | 0.006 | compiled=5 | 1,909,120.0 | 231,664,124.0 | 99,861.0 |
| `float-literal-bound` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 232,420,586.0 | 231,967,295.0 | 233,475,553.0 | 553,381.8 | 5 | 31,848 | 33,056 | 27,598 | 0.002 (max is trial 1) | compiled=5 | 2,038,091.0 | 230,270,135.0 | 189,201.0 |
| `float-literal-bound` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 198,975,603.0 | 192,004,661.0 | 200,543,953.0 | 3,202,127.0 | 5 | 27,288 | 22,154 | 21,923 | 0.016 (max is trial 1) | compiled=5 | 1,552,120.0 | 197,216,263.0 | 185,151.0 |
| `float-literal-bound` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 200,830,653.0 | 195,833,716.0 | 202,153,911.0 | 2,361,889.6 | 5 | 27,288 | 22,267 | 22,036 | 0.012 | compiled=5 | 1,553,959.0 | 199,179,074.0 | 97,620.0 |
| `float-literal-bound` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 199,008,421.0 | 191,805,528.0 | 200,021,237.0 | 3,526,746.8 | 5 | 27,288 | 22,154 | 21,923 | 0.018 | compiled=5 | 1,581,079.0 | 197,328,291.0 | 189,981.0 |
| `float-literal-bound` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 194,877,447.0 | 193,963,051.0 | 201,994,879.0 | 2,979,294.0 | 5 | 27,288 | 22,267 | 22,036 | 0.015 (max is trial 1) | compiled=5 | 1,557,029.0 | 193,182,147.0 | 101,511.0 |
| `floor-byte` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 150,180,921.0 | 141,253,504.0 | 152,553,020.0 | 4,128,608.0 | 5 | 27,608 | 18,295 | 13,298 | 0.027 | compiled=5 | 1,673,587.0 | 148,277,413.0 | 194,350.0 |
| `floor-byte` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 160,249,632.0 | 157,238,561.0 | 164,076,338.0 | 2,384,586.1 | 5 | 27,752 | 20,638 | 15,315 | 0.015 | compiled=5 | 1,714,137.0 | 158,444,565.0 | 107,780.0 |
| `floor-byte` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 138,223,000.0 | 130,428,948.0 | 150,910,288.0 | 8,476,861.6 | 5 | 27,608 | 18,295 | 13,298 | 0.061 | compiled=5 | 1,643,519.0 | 136,404,030.0 | 93,540.0 |
| `floor-byte` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 161,011,620.0 | 150,736,206.0 | 165,224,933.0 | 4,989,736.1 | 5 | 27,752 | 20,638 | 15,315 | 0.031 (max is trial 1) | compiled=5 | 1,736,859.0 | 159,166,291.0 | 108,470.0 |
| `floor-byte` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 140,271,736.0 | 127,959,006.0 | 141,179,511.0 | 4,983,139.8 | 5 | 23,072 | 17,838 | 17,838 | 0.036 | compiled=5 | 1,472,768.0 | 138,702,487.0 | 99,901.0 |
| `floor-byte` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 142,132,048.0 | 130,430,420.0 | 145,088,884.0 | 6,294,014.3 | 5 | 23,072 | 17,949 | 17,949 | 0.044 | compiled=5 | 1,503,869.0 | 140,527,338.0 | 114,231.0 |
| `floor-byte` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 133,562,481.0 | 121,295,896.0 | 137,384,782.0 | 6,033,998.9 | 5 | 23,072 | 17,838 | 17,838 | 0.045 (max is trial 1) | compiled=5 | 1,674,270.0 | 130,608,142.0 | 192,702.0 |
| `floor-byte` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 137,689,705.0 | 133,720,670.0 | 141,213,856.0 | 2,472,718.0 | 5 | 23,072 | 17,949 | 17,949 | 0.018 (max is trial 1) | compiled=5 | 1,706,081.0 | 135,432,921.0 | 190,491.0 |
| `high-byte-run` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 168,655,696.0 | 156,782,749.0 | 171,784,070.0 | 5,392,994.7 | 5 | 23,216 | 24,544 | 18,238 | 0.032 | compiled=5 | 1,876,937.0 | 166,548,098.0 | 185,051.0 |
| `high-byte-run` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 164,196,789.0 | 161,663,917.0 | 166,513,297.0 | 1,567,552.7 | 5 | 27,744 | 23,246 | 16,119 | 0.010 | compiled=5 | 1,848,027.0 | 161,855,349.0 | 108,730.0 |
| `high-byte-run` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 166,905,481.0 | 160,564,527.0 | 171,972,518.0 | 3,633,581.0 | 5 | 23,216 | 24,544 | 18,238 | 0.022 | compiled=5 | 1,815,829.0 | 164,991,801.0 | 206,161.0 |
| `high-byte-run` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 164,446,538.0 | 159,846,234.0 | 168,838,512.0 | 2,905,024.9 | 5 | 27,744 | 23,246 | 16,119 | 0.018 | compiled=5 | 1,834,550.0 | 161,371,752.0 | 191,631.0 |
| `high-byte-run` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 161,514,959.0 | 153,159,091.0 | 171,373,296.0 | 6,714,609.9 | 5 | 23,072 | 18,383 | 18,383 | 0.042 (max is trial 1) | compiled=5 | 1,472,189.0 | 159,943,369.0 | 186,681.0 |
| `high-byte-run` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 162,942,376.0 | 161,513,218.0 | 164,446,275.0 | 1,052,575.8 | 5 | 23,072 | 18,494 | 18,494 | 0.006 (max is trial 1) | compiled=5 | 1,495,649.0 | 161,352,658.0 | 102,380.0 |
| `high-byte-run` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 162,542,543.0 | 150,352,300.0 | 168,315,627.0 | 6,885,808.7 | 5 | 23,072 | 18,383 | 18,383 | 0.042 | compiled=5 | 1,700,101.0 | 160,857,523.0 | 193,991.0 |
| `high-byte-run` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 164,086,983.0 | 157,270,652.0 | 168,141,157.0 | 3,799,739.7 | 5 | 23,072 | 18,494 | 18,494 | 0.023 (max is trial 1) | compiled=5 | 1,505,109.0 | 162,366,652.0 | 204,231.0 |
| `ipv4-near-miss` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 164,831,971.0 | 159,191,628.0 | 168,585,956.0 | 3,060,299.6 | 5 | 32,424 | 22,055 | 16,739 | 0.019 | compiled=5 | 1,710,507.0 | 162,201,540.0 | 108,730.0 |
| `ipv4-near-miss` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 161,471,867.0 | 155,173,271.0 | 167,582,404.0 | 3,945,612.8 | 5 | 32,224 | 21,133 | 15,817 | 0.024 | compiled=5 | 1,711,827.0 | 159,563,259.0 | 196,781.0 |
| `ipv4-near-miss` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 160,792,079.0 | 146,962,856.0 | 167,539,994.0 | 7,395,202.5 | 5 | 32,424 | 22,055 | 16,739 | 0.046 | compiled=5 | 1,681,549.0 | 157,359,911.0 | 105,330.0 |
| `ipv4-near-miss` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 155,431,641.0 | 153,457,500.0 | 163,219,651.0 | 3,863,099.2 | 5 | 32,224 | 21,133 | 15,817 | 0.025 | compiled=5 | 1,942,530.0 | 153,798,532.0 | 192,291.0 |
| `ipv4-near-miss` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 252,567,542.0 | 251,241,723.0 | 266,325,720.0 | 5,764,495.9 | 5 | 27,200 | 30,904 | 30,904 | 0.023 | compiled=5 | 1,716,519.0 | 250,149,517.0 | 108,440.0 |
| `ipv4-near-miss` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 256,866,616.0 | 253,145,425.0 | 260,181,895.0 | 2,259,344.4 | 5 | 27,200 | 31,017 | 31,017 | 0.009 (max is trial 1) | compiled=5 | 1,696,910.0 | 255,070,655.0 | 111,491.0 |
| `ipv4-near-miss` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 250,538,070.0 | 242,520,302.0 | 260,798,392.0 | 7,047,035.3 | 5 | 27,200 | 30,904 | 30,904 | 0.028 | compiled=5 | 1,694,100.0 | 248,635,769.0 | 206,531.0 |
| `ipv4-near-miss` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 258,539,408.0 | 255,841,571.0 | 259,862,035.0 | 1,399,769.7 | 5 | 27,200 | 31,017 | 31,017 | 0.005 | compiled=5 | 1,847,061.0 | 256,189,034.0 | 115,071.0 |
| `keyword-prefix-order` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 152,869,543.0 | 146,097,775.0 | 157,033,330.0 | 3,613,476.2 | 5 | 27,608 | 20,258 | 13,644 | 0.024 | compiled=5 | 1,895,147.0 | 149,283,728.0 | 192,151.0 |
| `keyword-prefix-order` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 163,333,745.0 | 155,023,581.0 | 167,155,650.0 | 4,236,558.0 | 5 | 27,752 | 24,563 | 15,737 | 0.026 (max is trial 1) | compiled=5 | 2,043,958.0 | 161,275,466.0 | 107,740.0 |
| `keyword-prefix-order` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 144,073,760.0 | 143,274,987.0 | 155,946,084.0 | 4,809,387.1 | 5 | 27,608 | 20,258 | 13,644 | 0.033 | compiled=5 | 1,814,280.0 | 141,831,459.0 | 189,091.0 |
| `keyword-prefix-order` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 166,305,889.0 | 164,208,528.0 | 167,334,764.0 | 1,045,381.6 | 5 | 27,752 | 24,563 | 15,737 | 0.006 | compiled=5 | 1,964,721.0 | 163,601,603.0 | 105,911.0 |
| `keyword-prefix-order` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 170,929,023.0 | 161,871,420.0 | 172,690,633.0 | 4,441,721.2 | 5 | 23,104 | 19,790 | 19,790 | 0.026 | compiled=5 | 1,499,519.0 | 167,595,833.0 | 106,090.0 |
| `keyword-prefix-order` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 172,391,680.0 | 158,828,292.0 | 174,625,894.0 | 6,285,411.0 | 5 | 23,104 | 19,903 | 19,903 | 0.036 | compiled=5 | 1,482,539.0 | 170,800,742.0 | 192,501.0 |
| `keyword-prefix-order` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 169,629,516.0 | 154,899,969.0 | 171,669,318.0 | 6,252,231.1 | 5 | 23,104 | 19,790 | 19,790 | 0.037 | compiled=5 | 1,495,169.0 | 167,974,806.0 | 98,921.0 |
| `keyword-prefix-order` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 172,112,840.0 | 170,651,822.0 | 172,832,196.0 | 748,320.0 | 5 | 23,104 | 19,903 | 19,903 | 0.004 (max is trial 1) | compiled=5 | 1,517,829.0 | 170,157,429.0 | 117,021.0 |
| `logparse-atomic` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 309,060,218.0 | 304,182,048.0 | 318,752,618.0 | 5,333,701.8 | 5 | 82,840 | 62,375 | 42,442 | 0.017 | compiled=5 | 2,627,200.0 | 306,189,306.0 | 135,680.0 |
| `logparse-atomic` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 318,276,137.0 | 303,381,115.0 | 323,999,379.0 | 7,792,198.3 | 5 | 82,800 | 62,302 | 42,369 | 0.024 | compiled=5 | 2,664,011.0 | 314,793,281.0 | 219,461.0 |
| `logparse-atomic` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 308,657,390.0 | 300,751,849.0 | 324,658,295.0 | 8,362,464.4 | 5 | 82,840 | 62,067 | 42,134 | 0.027 | compiled=5 | 3,048,916.0 | 305,374,543.0 | 233,931.0 |
| `logparse-atomic` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 304,232,556.0 | 301,356,201.0 | 313,020,002.0 | 4,473,823.5 | 5 | 82,800 | 61,994 | 42,061 | 0.015 (max is trial 1) | compiled=5 | 2,499,023.0 | 301,508,442.0 | 223,381.0 |
| `logparse-atomic` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 246,702,838.0 | 240,414,642.0 | 252,632,971.0 | 3,877,148.9 | 5 | 27,240 | 32,008 | 31,777 | 0.016 (max is trial 1) | compiled=5 | 1,793,070.0 | 244,819,407.0 | 193,541.0 |
| `logparse-atomic` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 246,918,479.0 | 244,044,313.0 | 250,825,632.0 | 2,625,568.7 | 5 | 27,240 | 32,121 | 31,890 | 0.011 | compiled=5 | 2,146,153.0 | 244,849,897.0 | 199,951.0 |
| `logparse-atomic` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 239,995,067.0 | 237,290,670.0 | 250,352,827.0 | 4,874,110.5 | 5 | 27,240 | 32,008 | 31,777 | 0.020 | compiled=5 | 1,809,780.0 | 238,269,126.0 | 181,031.0 |
| `logparse-atomic` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 249,533,473.0 | 245,211,618.0 | 262,272,820.0 | 6,208,188.4 | 5 | 27,240 | 32,121 | 31,890 | 0.025 (max is trial 1) | compiled=5 | 3,742,132.0 | 245,645,320.0 | 197,572.0 |
| `logparse-atomic-removed` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 310,536,924.0 | 305,856,064.0 | 314,509,540.0 | 2,899,788.6 | 5 | 82,840 | 62,094 | 42,161 | 0.009 | compiled=5 | 5,313,102.0 | 308,025,684.0 | 230,361.0 |
| `logparse-atomic-removed` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 317,571,373.0 | 311,958,180.0 | 321,926,001.0 | 3,456,949.8 | 5 | 82,800 | 62,021 | 42,088 | 0.011 (max is trial 1) | compiled=5 | 2,601,910.0 | 314,811,131.0 | 215,301.0 |
| `logparse-atomic-removed` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 189,204,669.0 | 180,239,682.0 | 196,001,015.0 | 5,037,555.7 | 5 | 74,496 | 39,607 | 19,905 | 0.027 | compiled=5 | 2,026,981.0 | 187,006,168.0 | 127,210.0 |
| `logparse-atomic-removed` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 200,602,920.0 | 199,367,094.0 | 215,864,500.0 | 6,115,053.3 | 5 | 74,448 | 39,429 | 19,727 | 0.030 (max is trial 1) | compiled=5 | 2,023,930.0 | 198,388,247.0 | 212,971.0 |
| `logparse-atomic-removed` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 245,184,700.0 | 244,601,596.0 | 266,951,884.0 | 8,702,040.3 | 5 | 27,240 | 31,727 | 31,496 | 0.035 | compiled=5 | 2,014,782.0 | 243,072,257.0 | 192,981.0 |
| `logparse-atomic-removed` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 238,227,049.0 | 237,124,093.0 | 252,587,631.0 | 5,855,695.1 | 5 | 27,240 | 31,840 | 31,609 | 0.025 (max is trial 1) | compiled=5 | 1,836,810.0 | 236,090,727.0 | 102,071.0 |
| `logparse-atomic-removed` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 244,881,695.0 | 237,598,223.0 | 247,119,309.0 | 4,161,615.6 | 5 | 27,240 | 31,727 | 31,496 | 0.017 (max is trial 1) | compiled=5 | 1,798,530.0 | 242,938,205.0 | 110,191.0 |
| `logparse-atomic-removed` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 244,554,425.0 | 236,462,096.0 | 245,893,372.0 | 4,014,170.4 | 5 | 27,240 | 31,840 | 31,609 | 0.016 | compiled=5 | 1,818,221.0 | 242,640,363.0 | 190,781.0 |
| `mojibake-curly-quote` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 146,936,267.0 | 138,146,532.0 | 151,280,675.0 | 5,410,501.9 | 5 | 27,608 | 18,523 | 13,320 | 0.037 | compiled=5 | 1,795,317.0 | 144,947,249.0 | 112,490.0 |
| `mojibake-curly-quote` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 160,097,262.0 | 153,409,915.0 | 163,092,234.0 | 3,323,164.9 | 5 | 27,752 | 20,942 | 15,337 | 0.021 | compiled=5 | 1,759,927.0 | 158,144,544.0 | 196,521.0 |
| `mojibake-curly-quote` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 141,730,869.0 | 140,629,143.0 | 156,801,558.0 | 6,197,558.1 | 5 | 27,608 | 18,523 | 13,320 | 0.044 | compiled=5 | 1,733,049.0 | 139,815,858.0 | 190,921.0 |
| `mojibake-curly-quote` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 158,836,218.0 | 144,439,293.0 | 160,759,808.0 | 5,973,791.4 | 5 | 27,752 | 20,942 | 15,337 | 0.038 | compiled=5 | 1,767,379.0 | 155,824,472.0 | 110,460.0 |
| `mojibake-curly-quote` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 162,213,262.0 | 155,230,273.0 | 162,863,086.0 | 2,827,880.5 | 5 | 23,072 | 19,082 | 19,082 | 0.017 | compiled=5 | 1,522,229.0 | 160,560,993.0 | 110,640.0 |
| `mojibake-curly-quote` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 166,835,728.0 | 165,016,698.0 | 167,167,120.0 | 795,704.2 | 5 | 23,072 | 19,194 | 19,194 | 0.005 | compiled=5 | 1,515,318.0 | 165,095,939.0 | 111,280.0 |
| `mojibake-curly-quote` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 164,473,805.0 | 157,137,880.0 | 170,105,208.0 | 4,227,883.3 | 5 | 23,072 | 19,082 | 19,082 | 0.026 | compiled=5 | 1,509,269.0 | 162,760,515.0 | 190,232.0 |
| `mojibake-curly-quote` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 159,477,434.0 | 151,207,776.0 | 166,359,256.0 | 5,464,778.5 | 5 | 23,072 | 19,194 | 19,194 | 0.034 (max is trial 1) | compiled=5 | 1,501,028.0 | 157,771,394.0 | 198,241.0 |
| `negation-scope-lookbehind-var` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `negation-scope-lookbehind-var` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `negation-scope-lookbehind-var` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `negation-scope-lookbehind-var` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `nested-comment-rec` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 281,456,256.0 | 274,891,968.0 | 284,726,429.0 | 3,990,459.6 | 5 | 27,360 | 29,849 | 29,618 | 0.014 (max is trial 1) | compiled=5 | 1,668,307.0 | 279,447,438.0 | 113,260.0 |
| `nested-comment-rec` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 281,411,844.0 | 276,189,574.0 | 285,186,581.0 | 3,165,794.9 | 5 | 27,360 | 29,962 | 29,731 | 0.011 (max is trial 1) | compiled=5 | 1,690,947.0 | 279,505,467.0 | 189,141.0 |
| `nested-comment-rec` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 280,026,058.0 | 278,019,878.0 | 289,711,189.0 | 4,086,382.3 | 5 | 27,360 | 29,835 | 29,604 | 0.015 | compiled=5 | 1,684,189.0 | 278,241,379.0 | 187,341.0 |
| `nested-comment-rec` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 282,067,169.0 | 274,150,189.0 | 292,374,264.0 | 5,799,035.0 | 5 | 27,360 | 29,948 | 29,717 | 0.021 | compiled=5 | 1,679,679.0 | 279,853,687.0 | 106,911.0 |
| `nested-comment-rec` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 281,534,997.0 | 275,143,952.0 | 284,956,868.0 | 3,262,972.3 | 5 | 27,360 | 29,847 | 29,616 | 0.012 (max is trial 1) | compiled=5 | 1,668,879.0 | 279,676,907.0 | 193,242.0 |
| `nested-comment-rec` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 282,705,045.0 | 277,117,542.0 | 284,922,916.0 | 3,512,528.8 | 5 | 27,360 | 29,960 | 29,729 | 0.012 (max is trial 1) | compiled=5 | 1,689,050.0 | 280,907,624.0 | 101,931.0 |
| `nested-comment-rec` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 282,532,052.0 | 273,625,648.0 | 284,926,725.0 | 4,783,381.7 | 5 | 27,360 | 29,847 | 29,616 | 0.017 | compiled=5 | 1,802,831.0 | 278,977,100.0 | 191,751.0 |
| `nested-comment-rec` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 283,328,936.0 | 274,996,796.0 | 283,714,009.0 | 3,302,943.6 | 5 | 27,360 | 29,960 | 29,729 | 0.012 | compiled=5 | 1,733,220.0 | 279,966,946.0 | 105,161.0 |
| `numeric-id-nested-plus` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 210,222,807.0 | 206,061,449.0 | 215,863,099.0 | 3,749,867.5 | 5 | 31,568 | 27,307 | 25,625 | 0.018 | compiled=5 | 3,081,123.0 | 206,845,322.0 | 205,621.0 |
| `numeric-id-nested-plus` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 214,994,474.0 | 206,427,161.0 | 220,514,947.0 | 4,638,488.3 | 5 | 31,568 | 27,236 | 25,554 | 0.022 | compiled=5 | 1,669,796.0 | 212,059,523.0 | 204,930.0 |
| `numeric-id-nested-plus` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 129,837,716.0 | 128,293,917.0 | 138,096,858.0 | 3,807,447.1 | 5 | 23,144 | 12,911 | 11,229 | 0.029 | compiled=5 | 1,521,708.0 | 128,162,067.0 | 195,341.0 |
| `numeric-id-nested-plus` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 133,590,096.0 | 125,038,670.0 | 138,899,154.0 | 5,568,638.2 | 5 | 23,144 | 12,735 | 11,053 | 0.042 | compiled=5 | 1,451,958.0 | 132,007,487.0 | 100,850.0 |
| `numeric-id-nested-plus` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 205,458,070.0 | 195,863,805.0 | 208,990,622.0 | 5,101,210.1 | 5 | 27,320 | 23,152 | 23,152 | 0.025 | compiled=5 | 1,546,039.0 | 203,566,910.0 | 101,990.0 |
| `numeric-id-nested-plus` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 203,020,816.0 | 195,170,051.0 | 210,310,719.0 | 4,901,383.4 | 5 | 27,320 | 23,266 | 23,266 | 0.024 | compiled=5 | 1,530,289.0 | 201,383,797.0 | 186,761.0 |
| `numeric-id-nested-plus` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 205,560,131.0 | 194,590,275.0 | 207,242,930.0 | 4,515,609.9 | 5 | 27,320 | 23,152 | 23,152 | 0.022 | compiled=5 | 1,598,310.0 | 202,224,801.0 | 100,970.0 |
| `numeric-id-nested-plus` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 203,606,449.0 | 196,018,093.0 | 204,956,876.0 | 3,980,201.9 | 5 | 27,320 | 23,266 | 23,266 | 0.020 | compiled=5 | 1,556,849.0 | 200,913,353.0 | 189,321.0 |
| `phone-list-nested-plus` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 227,659,307.0 | 219,385,563.0 | 228,510,850.0 | 3,377,760.1 | 5 | 31,648 | 28,535 | 26,593 | 0.015 (max is trial 1) | compiled=5 | 1,728,797.0 | 225,054,406.0 | 102,441.0 |
| `phone-list-nested-plus` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 224,844,315.0 | 219,664,253.0 | 230,274,688.0 | 4,018,633.1 | 5 | 31,608 | 28,463 | 26,521 | 0.018 (max is trial 1) | compiled=5 | 1,740,267.0 | 223,043,428.0 | 101,970.0 |
| `phone-list-nested-plus` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 137,153,124.0 | 128,725,059.0 | 140,979,713.0 | 4,424,460.7 | 5 | 23,184 | 12,945 | 11,234 | 0.032 | compiled=5 | 1,523,748.0 | 135,288,314.0 | 119,141.0 |
| `phone-list-nested-plus` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 139,415,016.0 | 132,706,961.0 | 140,791,162.0 | 3,299,456.0 | 5 | 23,144 | 12,768 | 11,057 | 0.024 | compiled=5 | 1,497,277.0 | 137,832,117.0 | 107,171.0 |
| `phone-list-nested-plus` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 214,965,965.0 | 207,300,571.0 | 218,505,785.0 | 3,684,203.9 | 5 | 27,360 | 24,351 | 24,120 | 0.017 | compiled=5 | 1,611,339.0 | 213,260,335.0 | 110,990.0 |
| `phone-list-nested-plus` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 216,351,104.0 | 208,772,729.0 | 223,293,665.0 | 4,906,583.8 | 5 | 27,360 | 24,464 | 24,233 | 0.023 | compiled=5 | 1,614,710.0 | 214,652,744.0 | 108,491.0 |
| `phone-list-nested-plus` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 214,536,034.0 | 201,411,726.0 | 227,463,432.0 | 8,773,820.4 | 5 | 27,360 | 24,351 | 24,120 | 0.041 (max is trial 1) | compiled=5 | 1,543,099.0 | 212,756,293.0 | 202,971.0 |
| `phone-list-nested-plus` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 215,404,948.0 | 211,977,719.0 | 216,405,045.0 | 1,588,476.1 | 5 | 27,360 | 24,464 | 24,233 | 0.007 | compiled=5 | 1,605,439.0 | 213,695,849.0 | 104,490.0 |
| `phone-palindrome-6` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 285,524,243.0 | 276,717,808.0 | 288,139,852.0 | 3,982,081.1 | 5 | 27,168 | 22,034 | 22,034 | 0.014 | compiled=5 | 1,514,887.0 | 283,906,496.0 | 186,450.0 |
| `phone-palindrome-6` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 289,329,718.0 | 287,201,197.0 | 294,038,536.0 | 2,407,851.6 | 5 | 27,168 | 22,147 | 22,147 | 0.008 (max is trial 1) | compiled=5 | 1,532,636.0 | 287,697,431.0 | 99,980.0 |
| `phone-palindrome-6` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 278,594,222.0 | 269,115,971.0 | 280,453,631.0 | 5,063,232.4 | 5 | 27,168 | 22,016 | 22,016 | 0.018 (max is trial 1) | compiled=5 | 1,523,608.0 | 276,861,402.0 | 186,541.0 |
| `phone-palindrome-6` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 279,972,298.0 | 273,011,331.0 | 281,263,986.0 | 3,416,541.8 | 5 | 27,168 | 22,129 | 22,129 | 0.012 (max is trial 1) | compiled=5 | 1,529,878.0 | 278,081,899.0 | 190,441.0 |
| `phone-palindrome-6` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 286,774,768.0 | 279,959,339.0 | 287,154,311.0 | 2,732,784.3 | 5 | 27,168 | 22,032 | 22,032 | 0.010 | compiled=5 | 1,519,699.0 | 283,899,501.0 | 103,370.0 |
| `phone-palindrome-6` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 283,382,637.0 | 282,005,040.0 | 297,470,770.0 | 5,985,420.1 | 5 | 27,168 | 22,145 | 22,145 | 0.021 | compiled=5 | 1,523,549.0 | 280,544,812.0 | 191,611.0 |
| `phone-palindrome-6` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 285,389,558.0 | 282,017,758.0 | 288,512,757.0 | 2,200,811.4 | 5 | 27,168 | 22,032 | 22,032 | 0.008 | compiled=5 | 1,603,300.0 | 283,759,639.0 | 189,822.0 |
| `phone-palindrome-6` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 291,718,236.0 | 287,012,738.0 | 305,003,427.0 | 6,570,650.5 | 5 | 27,168 | 22,145 | 22,145 | 0.023 (max is trial 1) | compiled=5 | 1,549,599.0 | 288,303,416.0 | 175,342.0 |
| `pwd-strength-chain` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 246,862,815.0 | 246,316,723.0 | 249,168,154.0 | 1,119,596.2 | 5 | 31,808 | 31,639 | 28,998 | 0.005 | compiled=5 | 1,747,757.0 | 244,542,825.0 | 108,230.0 |
| `pwd-strength-chain` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 247,157,606.0 | 244,955,688.0 | 248,331,241.0 | 1,116,864.9 | 5 | 31,808 | 31,567 | 28,926 | 0.005 | compiled=5 | 1,764,187.0 | 245,186,288.0 | 107,941.0 |
| `pwd-strength-chain` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 247,366,385.0 | 239,764,636.0 | 249,539,617.0 | 4,270,886.7 | 5 | 31,808 | 31,639 | 28,998 | 0.017 | compiled=5 | 1,756,479.0 | 245,510,436.0 | 191,241.0 |
| `pwd-strength-chain` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 245,368,717.0 | 234,440,107.0 | 248,338,721.0 | 5,222,688.9 | 5 | 31,808 | 31,567 | 28,926 | 0.021 (max is trial 1) | compiled=5 | 3,479,098.0 | 243,512,986.0 | 111,351.0 |
| `pwd-strength-chain` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 230,490,984.0 | 224,077,448.0 | 232,499,266.0 | 2,913,230.4 | 5 | 27,280 | 25,884 | 25,422 | 0.013 (max is trial 1) | compiled=5 | 1,644,030.0 | 228,669,224.0 | 106,630.0 |
| `pwd-strength-chain` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 230,032,712.0 | 216,479,704.0 | 239,592,107.0 | 8,237,485.9 | 5 | 27,280 | 25,997 | 25,535 | 0.036 | compiled=5 | 1,650,329.0 | 228,334,263.0 | 193,081.0 |
| `pwd-strength-chain` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 224,181,792.0 | 216,297,165.0 | 231,325,745.0 | 5,490,202.6 | 5 | 27,280 | 25,884 | 25,422 | 0.024 | compiled=5 | 1,641,660.0 | 221,468,196.0 | 113,531.0 |
| `pwd-strength-chain` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 230,310,189.0 | 222,820,864.0 | 238,144,235.0 | 5,032,762.3 | 5 | 27,280 | 25,997 | 25,535 | 0.022 (max is trial 1) | compiled=5 | 1,647,150.0 | 228,533,518.0 | 111,351.0 |
| `quoted-delim-match` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 213,519,869.0 | 203,513,859.0 | 215,048,525.0 | 4,766,375.7 | 5 | 27,488 | 24,862 | 24,169 | 0.022 | compiled=5 | 1,588,366.0 | 211,746,782.0 | 192,891.0 |
| `quoted-delim-match` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 214,168,403.0 | 205,182,356.0 | 214,411,553.0 | 3,875,865.2 | 5 | 27,488 | 24,975 | 24,282 | 0.018 | compiled=5 | 1,589,156.0 | 212,497,645.0 | 106,381.0 |
| `quoted-delim-match` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 214,419,752.0 | 204,673,211.0 | 215,512,897.0 | 4,956,764.2 | 5 | 27,488 | 24,844 | 24,151 | 0.023 | compiled=5 | 1,593,379.0 | 211,005,094.0 | 105,480.0 |
| `quoted-delim-match` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 212,801,464.0 | 212,745,953.0 | 214,401,503.0 | 647,582.4 | 5 | 27,488 | 24,957 | 24,264 | 0.003 (max is trial 1) | compiled=5 | 1,575,738.0 | 211,142,845.0 | 106,361.0 |
| `quoted-delim-match` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 206,754,938.0 | 205,319,760.0 | 220,004,924.0 | 6,036,188.3 | 5 | 27,488 | 24,860 | 24,167 | 0.029 | compiled=5 | 1,606,899.0 | 205,064,248.0 | 189,311.0 |
| `quoted-delim-match` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 215,846,990.0 | 207,139,540.0 | 219,481,611.0 | 4,774,987.9 | 5 | 27,488 | 24,973 | 24,280 | 0.022 | compiled=5 | 1,589,349.0 | 212,750,043.0 | 169,681.0 |
| `quoted-delim-match` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 216,317,914.0 | 207,177,509.0 | 217,271,251.0 | 4,478,237.4 | 5 | 27,488 | 24,860 | 24,167 | 0.021 | compiled=5 | 1,604,159.0 | 212,968,415.0 | 112,630.0 |
| `quoted-delim-match` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 215,600,561.0 | 208,229,037.0 | 216,932,659.0 | 3,075,335.3 | 5 | 27,488 | 24,973 | 24,280 | 0.014 | compiled=5 | 1,632,220.0 | 213,428,908.0 | 112,220.0 |
| `router-prefix-order` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 153,422,686.0 | 149,304,618.0 | 155,670,044.0 | 2,082,258.9 | 5 | 27,608 | 19,289 | 13,309 | 0.014 | compiled=5 | 1,830,627.0 | 151,491,327.0 | 103,011.0 |
| `router-prefix-order` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 159,877,821.0 | 151,243,555.0 | 163,115,093.0 | 4,243,794.9 | 5 | 27,752 | 21,933 | 15,326 | 0.027 | compiled=5 | 1,875,398.0 | 156,432,367.0 | 103,720.0 |
| `router-prefix-order` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 147,653,189.0 | 141,048,974.0 | 151,154,128.0 | 3,677,126.6 | 5 | 27,608 | 19,289 | 13,309 | 0.025 | compiled=5 | 1,817,539.0 | 145,730,290.0 | 108,240.0 |
| `router-prefix-order` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 161,286,851.0 | 149,180,379.0 | 162,817,149.0 | 5,853,483.6 | 5 | 27,752 | 21,933 | 15,326 | 0.036 | compiled=5 | 3,773,530.0 | 157,135,310.0 | 187,451.0 |
| `router-prefix-order` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 169,560,594.0 | 167,970,095.0 | 171,310,234.0 | 1,187,279.9 | 5 | 23,104 | 19,150 | 19,150 | 0.007 | compiled=5 | 1,511,459.0 | 167,658,514.0 | 190,951.0 |
| `router-prefix-order` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 161,564,568.0 | 158,851,083.0 | 163,116,117.0 | 1,460,664.2 | 5 | 23,104 | 19,263 | 19,263 | 0.009 | compiled=5 | 1,484,349.0 | 159,963,939.0 | 192,871.0 |
| `router-prefix-order` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 163,731,430.0 | 160,538,670.0 | 169,308,214.0 | 3,697,509.4 | 5 | 23,104 | 19,150 | 19,150 | 0.023 (max is trial 1) | compiled=5 | 1,482,608.0 | 161,957,280.0 | 99,920.0 |
| `router-prefix-order` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 167,726,474.0 | 162,787,614.0 | 169,081,863.0 | 2,259,354.7 | 5 | 23,104 | 19,263 | 19,263 | 0.013 | compiled=5 | 1,518,339.0 | 166,109,635.0 | 107,861.0 |
| `tag-depth3-bound` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 276,250,314.0 | 268,723,805.0 | 276,829,668.0 | 3,062,797.2 | 5 | 27,488 | 31,532 | 31,070 | 0.011 (max is trial 1) | compiled=5 | 1,742,017.0 | 274,148,436.0 | 101,330.0 |
| `tag-depth3-bound` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 277,563,920.0 | 276,885,997.0 | 287,283,940.0 | 4,092,658.9 | 5 | 31,584 | 31,645 | 31,183 | 0.015 | compiled=5 | 1,754,467.0 | 275,615,882.0 | 190,611.0 |
| `tag-depth3-bound` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 281,736,327.0 | 275,004,752.0 | 284,231,691.0 | 3,190,315.0 | 5 | 27,448 | 31,514 | 31,052 | 0.011 (max is trial 1) | compiled=5 | 1,793,939.0 | 279,842,968.0 | 108,460.0 |
| `tag-depth3-bound` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 275,958,967.0 | 273,782,995.0 | 285,117,847.0 | 4,154,072.1 | 5 | 27,448 | 31,627 | 31,165 | 0.015 | compiled=5 | 1,841,769.0 | 272,414,719.0 | 206,342.0 |
| `tag-depth3-bound` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 279,391,586.0 | 278,629,931.0 | 285,628,282.0 | 2,610,355.3 | 5 | 27,488 | 31,530 | 31,068 | 0.009 | compiled=5 | 1,733,730.0 | 276,898,321.0 | 188,202.0 |
| `tag-depth3-bound` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 277,162,043.0 | 269,139,306.0 | 281,939,730.0 | 4,762,773.7 | 5 | 31,584 | 31,643 | 31,181 | 0.017 | compiled=5 | 1,754,660.0 | 274,024,445.0 | 101,121.0 |
| `tag-depth3-bound` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 277,938,644.0 | 264,749,034.0 | 280,847,291.0 | 5,814,690.0 | 5 | 27,488 | 31,530 | 31,068 | 0.021 (max is trial 1) | compiled=5 | 1,734,821.0 | 275,863,782.0 | 105,101.0 |
| `tag-depth3-bound` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 276,881,596.0 | 269,253,672.0 | 277,712,792.0 | 3,213,102.3 | 5 | 31,584 | 31,643 | 31,181 | 0.012 | compiled=5 | 1,740,280.0 | 274,381,532.0 | 100,611.0 |
| `tag-pair-match` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 216,856,693.0 | 215,266,185.0 | 224,065,852.0 | 3,497,326.8 | 5 | 27,448 | 25,424 | 24,269 | 0.016 | compiled=5 | 1,657,507.0 | 215,023,115.0 | 183,021.0 |
| `tag-pair-match` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 224,187,122.0 | 217,814,526.0 | 226,957,434.0 | 3,009,918.5 | 5 | 27,448 | 25,537 | 24,382 | 0.013 (max is trial 1) | compiled=5 | 1,662,487.0 | 222,441,915.0 | 115,720.0 |
| `tag-pair-match` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 223,116,388.0 | 222,200,384.0 | 226,064,484.0 | 1,415,708.2 | 5 | 27,448 | 25,406 | 24,251 | 0.006 (max is trial 1) | compiled=5 | 1,661,909.0 | 221,270,018.0 | 115,971.0 |
| `tag-pair-match` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 223,076,117.0 | 211,070,125.0 | 224,446,745.0 | 5,307,965.2 | 5 | 27,448 | 25,519 | 24,364 | 0.024 | compiled=5 | 1,681,859.0 | 219,469,379.0 | 100,630.0 |
| `tag-pair-match` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 223,706,656.0 | 216,574,025.0 | 225,147,953.0 | 3,069,881.6 | 5 | 27,448 | 25,422 | 24,267 | 0.014 (max is trial 1) | compiled=5 | 1,647,169.0 | 221,689,234.0 | 101,150.0 |
| `tag-pair-match` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 225,556,846.0 | 217,075,406.0 | 229,324,167.0 | 4,030,472.4 | 5 | 27,448 | 25,535 | 24,380 | 0.018 (max is trial 1) | compiled=5 | 1,673,989.0 | 223,792,816.0 | 119,150.0 |
| `tag-pair-match` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 218,476,948.0 | 216,934,089.0 | 238,090,756.0 | 7,997,388.4 | 5 | 27,448 | 25,422 | 24,267 | 0.037 | compiled=5 | 1,679,780.0 | 216,577,817.0 | 192,871.0 |
| `tag-pair-match` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 225,135,677.0 | 218,895,961.0 | 229,327,473.0 | 3,377,287.6 | 5 | 27,448 | 25,535 | 24,380 | 0.015 (max is trial 1) | compiled=5 | 1,669,730.0 | 223,266,766.0 | 189,981.0 |
| `trim-nested-star` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 195,128,234.0 | 188,285,176.0 | 197,807,655.0 | 3,947,093.4 | 5 | 27,360 | 22,410 | 22,179 | 0.020 (max is trial 1) | compiled=5 | 1,513,826.0 | 193,532,458.0 | 102,400.0 |
| `trim-nested-star` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 194,915,093.0 | 187,757,604.0 | 196,060,288.0 | 3,091,398.9 | 5 | 27,360 | 22,524 | 22,293 | 0.016 (max is trial 1) | compiled=5 | 1,524,686.0 | 192,864,196.0 | 115,460.0 |
| `trim-nested-star` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 129,625,704.0 | 123,735,885.0 | 135,995,168.0 | 4,691,224.8 | 5 | 23,144 | 12,680 | 11,069 | 0.036 | compiled=5 | 1,431,567.0 | 128,273,487.0 | 110,141.0 |
| `trim-nested-star` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 129,002,022.0 | 126,366,737.0 | 137,528,536.0 | 3,860,655.7 | 5 | 23,104 | 12,504 | 10,893 | 0.030 (max is trial 1) | compiled=5 | 1,520,628.0 | 127,259,072.0 | 202,171.0 |
| `trim-nested-star` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 188,462,102.0 | 187,137,155.0 | 197,537,004.0 | 4,568,228.2 | 5 | 27,360 | 22,391 | 22,160 | 0.024 | compiled=5 | 1,530,779.0 | 186,202,360.0 | 198,961.0 |
| `trim-nested-star` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 191,423,660.0 | 186,573,562.0 | 195,384,382.0 | 3,331,932.0 | 5 | 27,360 | 22,505 | 22,274 | 0.017 | compiled=5 | 1,527,739.0 | 188,243,712.0 | 184,451.0 |
| `trim-nested-star` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 194,180,523.0 | 186,776,529.0 | 201,820,459.0 | 5,863,223.3 | 5 | 27,360 | 22,391 | 22,160 | 0.030 | compiled=5 | 1,559,889.0 | 192,521,073.0 | 115,271.0 |
| `trim-nested-star` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 188,276,497.0 | 180,397,251.0 | 196,818,629.0 | 6,125,194.8 | 5 | 27,360 | 22,505 | 22,274 | 0.033 | compiled=5 | 1,745,630.0 | 185,974,503.0 | 110,921.0 |
| `utf8-lead-no-cont` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 185,063,902.0 | 178,167,724.0 | 188,860,209.0 | 4,454,720.4 | 5 | 31,632 | 26,873 | 22,071 | 0.024 (max is trial 1) | compiled=5 | 1,763,078.0 | 183,130,665.0 | 189,460.0 |
| `utf8-lead-no-cont` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 187,591,533.0 | 177,635,782.0 | 192,169,133.0 | 5,237,563.9 | 5 | 31,728 | 28,449 | 23,433 | 0.028 | compiled=5 | 1,823,328.0 | 183,717,638.0 | 112,310.0 |
| `utf8-lead-no-cont` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 186,593,735.0 | 184,454,454.0 | 188,896,607.0 | 1,465,744.5 | 5 | 31,632 | 26,873 | 22,071 | 0.008 | compiled=5 | 1,756,549.0 | 184,736,625.0 | 100,561.0 |
| `utf8-lead-no-cont` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 192,871,039.0 | 184,284,693.0 | 193,968,184.0 | 3,517,006.2 | 5 | 31,728 | 28,449 | 23,433 | 0.018 (max is trial 1) | compiled=5 | 1,803,599.0 | 189,983,604.0 | 187,971.0 |
| `utf8-lead-no-cont` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 167,388,920.0 | 163,359,559.0 | 169,208,681.0 | 1,971,100.7 | 5 | 23,104 | 18,794 | 18,794 | 0.012 | compiled=5 | 1,474,548.0 | 164,930,138.0 | 105,150.0 |
| `utf8-lead-no-cont` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 168,510,248.0 | 166,195,274.0 | 171,328,255.0 | 1,734,282.7 | 5 | 23,104 | 18,905 | 18,905 | 0.010 | compiled=5 | 1,479,748.0 | 166,935,820.0 | 97,941.0 |
| `utf8-lead-no-cont` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 169,323,214.0 | 155,021,039.0 | 171,125,584.0 | 6,001,881.4 | 5 | 23,104 | 18,794 | 18,794 | 0.035 | compiled=5 | 1,527,859.0 | 167,737,364.0 | 99,751.0 |
| `utf8-lead-no-cont` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 165,820,762.0 | 161,322,765.0 | 171,658,328.0 | 3,651,407.0 | 5 | 23,104 | 18,905 | 18,905 | 0.022 (max is trial 1) | compiled=5 | 1,490,819.0 | 164,430,474.0 | 98,441.0 |
| `uuid-near-miss` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 171,673,490.0 | 165,300,033.0 | 176,617,599.0 | 3,729,134.9 | 5 | 36,888 | 22,372 | 16,968 | 0.022 (max is trial 1) | compiled=5 | 1,606,967.0 | 169,970,872.0 | 197,251.0 |
| `uuid-near-miss` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 175,187,033.0 | 166,909,290.0 | 183,076,475.0 | 5,115,223.1 | 5 | 36,848 | 22,194 | 16,790 | 0.029 (max is trial 1) | compiled=5 | 1,615,856.0 | 173,372,826.0 | 197,280.0 |
| `uuid-near-miss` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 174,178,270.0 | 165,320,384.0 | 179,961,220.0 | 4,733,992.6 | 5 | 36,888 | 22,372 | 16,968 | 0.027 | compiled=5 | 1,591,868.0 | 170,522,621.0 | 188,511.0 |
| `uuid-near-miss` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 176,083,321.0 | 165,129,011.0 | 185,064,167.0 | 6,414,778.1 | 5 | 36,848 | 22,194 | 16,790 | 0.036 | compiled=5 | 1,869,979.0 | 173,071,524.0 | 189,741.0 |
| `uuid-near-miss` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 195,075,972.0 | 190,577,045.0 | 202,964,696.0 | 4,307,241.3 | 5 | 23,192 | 22,985 | 22,523 | 0.022 | compiled=5 | 1,554,429.0 | 193,389,682.0 | 170,061.0 |
| `uuid-near-miss` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 193,679,453.0 | 176,898,036.0 | 196,258,289.0 | 7,051,319.3 | 5 | 23,192 | 23,098 | 22,636 | 0.036 | compiled=5 | 1,570,049.0 | 191,929,903.0 | 103,240.0 |
| `uuid-near-miss` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 194,754,096.0 | 187,533,191.0 | 198,825,249.0 | 4,394,371.6 | 5 | 23,192 | 22,985 | 22,523 | 0.023 (max is trial 1) | compiled=5 | 1,663,719.0 | 192,901,725.0 | 191,581.0 |
| `uuid-near-miss` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 194,138,923.0 | 187,748,054.0 | 196,753,768.0 | 3,000,731.6 | 5 | 23,192 | 23,098 | 22,636 | 0.015 | compiled=5 | 1,615,879.0 | 191,985,249.0 | 101,701.0 |
| `wild-codegrammar-json-array-begin` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 148,399,424.0 | 140,500,042.0 | 150,115,762.0 | 3,949,255.2 | 5 | 27,608 | 18,296 | 13,299 | 0.027 | compiled=5 | 1,657,837.0 | 146,342,106.0 | 115,660.0 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 157,021,750.0 | 152,624,202.0 | 160,244,092.0 | 2,425,389.1 | 5 | 27,752 | 20,639 | 15,316 | 0.015 | compiled=5 | 1,718,507.0 | 154,837,320.0 | 189,081.0 |
| `wild-codegrammar-json-array-begin` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 147,213,567.0 | 140,609,742.0 | 155,638,511.0 | 5,524,202.7 | 5 | 27,608 | 18,296 | 13,299 | 0.038 (max is trial 1) | compiled=5 | 1,788,369.0 | 145,446,698.0 | 100,691.0 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 159,705,303.0 | 159,133,310.0 | 167,366,163.0 | 3,307,050.5 | 5 | 27,752 | 20,639 | 15,316 | 0.021 | compiled=5 | 3,447,038.0 | 157,744,373.0 | 197,131.0 |
| `wild-codegrammar-json-array-begin` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 134,102,111.0 | 126,540,338.0 | 139,721,682.0 | 5,203,322.7 | 5 | 23,072 | 17,839 | 17,839 | 0.039 | compiled=5 | 1,452,788.0 | 132,325,441.0 | 189,391.0 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 137,648,461.0 | 128,060,647.0 | 148,170,962.0 | 6,827,213.9 | 5 | 23,072 | 17,950 | 17,950 | 0.050 | compiled=5 | 1,460,689.0 | 135,984,731.0 | 187,781.0 |
| `wild-codegrammar-json-array-begin` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 138,224,268.0 | 124,844,327.0 | 141,036,183.0 | 5,680,152.5 | 5 | 23,072 | 17,839 | 17,839 | 0.041 | compiled=5 | 1,456,469.0 | 136,576,308.0 | 108,501.0 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 136,526,918.0 | 135,557,691.0 | 150,030,117.0 | 5,435,178.6 | 5 | 23,072 | 17,950 | 17,950 | 0.040 | compiled=5 | 1,475,158.0 | 134,937,538.0 | 100,621.0 |
| `wild-codegrammar-json-constant` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 155,071,962.0 | 151,430,776.0 | 158,773,725.0 | 2,368,609.1 | 5 | 27,936 | 27,250 | 14,985 | 0.015 | compiled=5 | 2,192,759.0 | 152,780,682.0 | 101,381.0 |
| `wild-codegrammar-json-constant` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 157,669,534.0 | 156,350,608.0 | 165,293,633.0 | 4,000,829.2 | 5 | 28,080 | 30,113 | 16,960 | 0.025 | compiled=5 | 2,342,840.0 | 154,607,159.0 | 108,580.0 |
| `wild-codegrammar-json-constant` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 158,140,426.0 | 151,268,640.0 | 160,070,765.0 | 3,093,433.4 | 5 | 27,936 | 27,250 | 14,985 | 0.020 (max is trial 1) | compiled=5 | 2,184,052.0 | 154,951,148.0 | 101,600.0 |
| `wild-codegrammar-json-constant` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 166,876,491.0 | 157,649,962.0 | 167,986,177.0 | 4,815,603.2 | 5 | 28,080 | 30,113 | 16,960 | 0.029 | compiled=5 | 2,286,402.0 | 161,750,494.0 | 182,671.0 |
| `wild-codegrammar-json-constant` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 200,096,800.0 | 199,687,557.0 | 209,329,791.0 | 4,047,615.6 | 5 | 23,112 | 20,901 | 20,670 | 0.020 | compiled=5 | 1,532,179.0 | 198,438,551.0 | 110,121.0 |
| `wild-codegrammar-json-constant` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 206,959,059.0 | 198,420,421.0 | 209,556,564.0 | 3,817,645.6 | 5 | 23,112 | 21,014 | 20,783 | 0.018 | compiled=5 | 1,557,609.0 | 205,306,940.0 | 111,410.0 |
| `wild-codegrammar-json-constant` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 207,161,649.0 | 206,413,256.0 | 212,813,994.0 | 2,377,312.8 | 5 | 23,112 | 20,901 | 20,670 | 0.011 | compiled=5 | 1,540,270.0 | 205,511,950.0 | 166,611.0 |
| `wild-codegrammar-json-constant` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 206,520,156.0 | 200,143,999.0 | 210,252,588.0 | 3,427,163.5 | 5 | 23,112 | 21,014 | 20,783 | 0.017 | compiled=5 | 1,537,949.0 | 204,880,326.0 | 106,321.0 |
| `wild-codegrammar-json-number-extended` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 154,116,927.0 | 140,157,310.0 | 156,310,315.0 | 7,220,893.2 | 5 | 27,608 | 22,063 | 13,741 | 0.047 | compiled=5 | 1,979,038.0 | 151,951,468.0 | 108,771.0 |
| `wild-codegrammar-json-number-extended` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 1,118,324.0 | - | - |
| `wild-codegrammar-json-number-extended` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 150,603,766.0 | 148,398,765.0 | 153,185,198.0 | 1,892,106.7 | 5 | 27,608 | 22,063 | 13,741 | 0.013 | compiled=5 | 1,968,241.0 | 148,432,513.0 | 109,851.0 |
| `wild-codegrammar-json-number-extended` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 2,270,502.0 | - | - |
| `wild-codegrammar-json-number-extended` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 194,794,039.0 | 184,670,872.0 | 206,591,887.0 | 7,409,055.0 | 5 | 31,336 | 23,271 | 23,040 | 0.038 | compiled=5 | 1,655,380.0 | 191,467,740.0 | 108,260.0 |
| `wild-codegrammar-json-number-extended` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 2,128,252.0 | - | - |
| `wild-codegrammar-json-number-extended` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 200,858,663.0 | 199,270,183.0 | 209,087,311.0 | 4,162,891.0 | 5 | 31,336 | 23,271 | 23,040 | 0.021 | compiled=5 | 1,653,450.0 | 199,155,082.0 | 186,801.0 |
| `wild-codegrammar-json-number-extended` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 1,318,348.0 | - | - |
| `wild-codegrammar-json-object-begin` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 143,514,403.0 | 130,744,241.0 | 157,229,150.0 | 9,067,981.3 | 5 | 27,608 | 18,297 | 13,300 | 0.063 | compiled=5 | 1,689,757.0 | 139,917,949.0 | 102,060.0 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 156,384,486.0 | 144,368,527.0 | 162,242,840.0 | 6,829,010.0 | 5 | 27,752 | 20,640 | 15,317 | 0.044 (max is trial 1) | compiled=5 | 1,722,267.0 | 154,602,559.0 | 105,930.0 |
| `wild-codegrammar-json-object-begin` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 141,294,636.0 | 139,444,258.0 | 156,176,425.0 | 6,649,034.2 | 5 | 27,608 | 18,297 | 13,300 | 0.047 | compiled=5 | 1,774,320.0 | 139,417,096.0 | 101,950.0 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 160,500,326.0 | 157,029,668.0 | 161,515,242.0 | 1,768,384.7 | 5 | 27,752 | 20,640 | 15,317 | 0.011 | compiled=5 | 1,757,469.0 | 156,913,988.0 | 189,661.0 |
| `wild-codegrammar-json-object-begin` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 135,077,976.0 | 119,611,276.0 | 140,252,985.0 | 7,702,546.5 | 5 | 23,072 | 17,840 | 17,840 | 0.057 | compiled=5 | 1,446,798.0 | 133,556,297.0 | 113,490.0 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 141,411,513.0 | 136,614,305.0 | 143,737,556.0 | 2,634,833.3 | 5 | 23,072 | 17,951 | 17,951 | 0.019 | compiled=5 | 1,428,538.0 | 139,855,014.0 | 192,472.0 |
| `wild-codegrammar-json-object-begin` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 124,565,017.0 | 116,228,156.0 | 136,750,800.0 | 8,107,824.8 | 5 | 23,072 | 17,840 | 17,840 | 0.065 | compiled=5 | 2,577,595.0 | 123,048,657.0 | 97,991.0 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 127,664,534.0 | 125,849,545.0 | 130,470,141.0 | 1,658,384.8 | 5 | 23,072 | 17,951 | 17,951 | 0.013 (max is trial 1) | compiled=5 | 1,495,489.0 | 125,963,414.0 | 102,011.0 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 151,122,664.0 | 148,366,514.0 | 154,373,049.0 | 2,324,346.1 | 5 | 27,608 | 19,676 | 13,581 | 0.015 | compiled=5 | 1,834,817.0 | 149,177,927.0 | 103,770.0 |
| `wild-codegrammar-json-stringcontent-escape` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 2,322,549.0 | - | - |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 149,289,498.0 | 140,467,831.0 | 152,962,337.0 | 4,271,699.4 | 5 | 27,608 | 19,676 | 13,581 | 0.029 | compiled=5 | 1,810,289.0 | 145,504,848.0 | 100,580.0 |
| `wild-codegrammar-json-stringcontent-escape` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 2,117,511.0 | - | - |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 174,432,574.0 | 162,165,432.0 | 178,226,584.0 | 5,683,408.4 | 5 | 23,184 | 20,198 | 19,736 | 0.033 | compiled=5 | 1,550,329.0 | 172,079,229.0 | 112,541.0 |
| `wild-codegrammar-json-stringcontent-escape` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 2,431,444.0 | - | - |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 171,645,247.0 | 170,142,458.0 | 180,598,121.0 | 3,823,142.6 | 5 | 23,184 | 20,198 | 19,736 | 0.022 | compiled=5 | 1,436,939.0 | 170,081,918.0 | 194,861.0 |
| `wild-codegrammar-json-stringcontent-escape` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 2,101,863.0 | - | - |
| `wild-datetime-datefinder-alternation` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 563,818,835.0 | - | - |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 9,454,829,628.0 | - | - |
| `wild-datetime-datefinder-alternation` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 850,828,213.0 | 844,984,493.0 | 862,456,924.0 | 7,082,255.3 | 5 | 277,312 | 889,527 (warned) | 20,438 | 0.008 | compiled=5 | 567,502,697.0 | 280,342,330.0 | 192,791.0 |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 9,046,071,784.0 | - | - |
| `wild-datetime-datefinder-alternation` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 27,864,780.0 | - | - |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 39,664,088.0 | - | - |
| `wild-datetime-datefinder-alternation` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 40,617,533.0 | - | - |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 17,782,366.0 | - | - |
| `wild-datetime-moment-iso8601` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 351,865,922.0 | 348,539,248.0 | 358,011,386.0 | 3,401,043.0 | 5 | 45,648 | 54,260 | 44,337 | 0.010 | compiled=5 | 2,226,969.0 | 349,400,192.0 | 113,360.0 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 347,066,112.0 | 344,373,093.0 | 349,794,344.0 | 1,761,704.8 | 5 | 45,280 | 52,699 | 42,776 | 0.005 | compiled=5 | 2,248,669.0 | 344,612,703.0 | 119,380.0 |
| `wild-datetime-moment-iso8601` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 178,896,985.0 | 176,253,372.0 | 190,691,526.0 | 5,526,360.3 | 5 | 41,232 | 29,483 | 20,484 | 0.031 | compiled=5 | 1,813,000.0 | 176,891,084.0 | 191,211.0 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 175,599,547.0 | 165,990,917.0 | 179,859,030.0 | 4,658,303.1 | 5 | 40,864 | 27,817 | 18,818 | 0.027 | compiled=5 | 1,803,470.0 | 171,936,428.0 | 212,791.0 |
| `wild-datetime-moment-iso8601` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 299,828,583.0 | 292,027,978.0 | 300,725,779.0 | 3,799,477.6 | 5 | 27,408 | 33,723 | 32,799 | 0.013 | compiled=5 | 1,837,841.0 | 297,919,682.0 | 98,801.0 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 298,337,464.0 | 292,370,532.0 | 301,124,870.0 | 3,129,280.2 | 5 | 27,408 | 33,836 | 32,912 | 0.010 (max is trial 1) | compiled=5 | 1,835,760.0 | 296,298,253.0 | 190,551.0 |
| `wild-datetime-moment-iso8601` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 300,268,368.0 | 286,141,613.0 | 305,745,490.0 | 6,988,200.6 | 5 | 27,408 | 33,723 | 32,799 | 0.023 | compiled=5 | 1,855,711.0 | 298,290,015.0 | 108,181.0 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 300,177,237.0 | 294,423,773.0 | 301,460,725.0 | 2,492,751.4 | 5 | 27,408 | 33,836 | 32,912 | 0.008 (max is trial 1) | compiled=5 | 1,851,381.0 | 297,551,811.0 | 192,312.0 |
| `wild-logparse-base10num-grok` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 232,814,207.0 | 230,822,850.0 | 243,350,101.0 | 5,314,089.4 | 5 | 31,800 | 32,766 | 27,256 | 0.023 | compiled=5 | 1,963,928.0 | 230,194,027.0 | 191,761.0 |
| `wild-logparse-base10num-grok` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 229,917,246.0 | 228,964,712.0 | 249,305,326.0 | 7,997,129.8 | 5 | 31,888 | 33,838 | 27,903 | 0.035 (max is trial 1) | compiled=5 | 2,005,438.0 | 227,755,157.0 | 188,131.0 |
| `wild-logparse-base10num-grok` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 227,855,013.0 | 227,771,122.0 | 239,126,612.0 | 4,493,887.0 | 5 | 31,800 | 32,766 | 27,256 | 0.020 (max is trial 1) | compiled=5 | 1,940,131.0 | 225,704,921.0 | 195,581.0 |
| `wild-logparse-base10num-grok` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 239,414,785.0 | 234,649,650.0 | 241,085,064.0 | 2,277,996.2 | 5 | 31,888 | 33,838 | 27,903 | 0.010 | compiled=5 | 1,990,781.0 | 237,340,963.0 | 107,071.0 |
| `wild-logparse-base10num-grok` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 207,494,673.0 | 200,865,135.0 | 210,183,619.0 | 3,680,908.8 | 5 | 27,328 | 23,345 | 22,883 | 0.018 | compiled=5 | 1,622,260.0 | 205,665,622.0 | 100,981.0 |
| `wild-logparse-base10num-grok` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 212,672,952.0 | 204,712,987.0 | 223,019,892.0 | 5,829,233.3 | 5 | 27,328 | 23,461 | 22,999 | 0.027 (max is trial 1) | compiled=5 | 1,891,431.0 | 210,848,331.0 | 196,681.0 |
| `wild-logparse-base10num-grok` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 207,611,804.0 | 202,724,614.0 | 209,268,813.0 | 2,610,996.4 | 5 | 27,328 | 23,345 | 22,883 | 0.013 | compiled=5 | 1,645,450.0 | 205,779,612.0 | 109,801.0 |
| `wild-logparse-base10num-grok` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 211,809,808.0 | 205,155,998.0 | 217,488,242.0 | 4,953,037.6 | 5 | 27,328 | 23,461 | 22,999 | 0.023 (max is trial 1) | compiled=5 | 1,659,090.0 | 209,989,807.0 | 186,721.0 |
| `wild-logparse-base10num-noatomic` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 235,186,587.0 | 227,547,017.0 | 239,882,006.0 | 4,082,332.7 | 5 | 31,800 | 32,487 | 26,977 | 0.017 | compiled=5 | 1,984,109.0 | 233,046,919.0 | 203,140.0 |
| `wild-logparse-base10num-noatomic` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 228,508,391.0 | 222,258,544.0 | 237,478,437.0 | 5,045,931.4 | 5 | 31,888 | 33,556 | 27,621 | 0.022 | compiled=5 | 1,975,958.0 | 226,239,081.0 | 112,760.0 |
| `wild-logparse-base10num-noatomic` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 235,219,612.0 | 234,308,008.0 | 241,641,356.0 | 2,701,869.5 | 5 | 31,800 | 32,487 | 26,977 | 0.011 | compiled=5 | 1,929,170.0 | 233,174,462.0 | 106,161.0 |
| `wild-logparse-base10num-noatomic` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 231,140,240.0 | 230,039,464.0 | 235,750,034.0 | 2,431,761.0 | 5 | 31,888 | 33,556 | 27,621 | 0.011 | compiled=5 | 1,985,520.0 | 228,943,088.0 | 191,161.0 |
| `wild-logparse-base10num-noatomic` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 206,293,505.0 | 196,082,086.0 | 209,076,402.0 | 4,731,744.7 | 5 | 27,328 | 23,066 | 22,604 | 0.023 | compiled=5 | 3,183,589.0 | 203,038,367.0 | 99,340.0 |
| `wild-logparse-base10num-noatomic` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 208,360,177.0 | 201,261,516.0 | 213,145,314.0 | 3,985,733.5 | 5 | 27,328 | 23,179 | 22,717 | 0.019 | compiled=5 | 1,607,389.0 | 206,666,707.0 | 183,381.0 |
| `wild-logparse-base10num-noatomic` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 205,754,762.0 | 205,236,328.0 | 208,018,815.0 | 996,159.8 | 5 | 27,328 | 23,066 | 22,604 | 0.005 (max is trial 1) | compiled=5 | 1,611,250.0 | 204,046,031.0 | 113,651.0 |
| `wild-logparse-base10num-noatomic` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 209,414,515.0 | 201,398,675.0 | 210,785,702.0 | 3,539,129.1 | 5 | 27,328 | 23,179 | 22,717 | 0.017 | compiled=5 | 1,723,441.0 | 207,334,501.0 | 190,452.0 |
| `wild-logparse-quotedstring-grok` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 408,520,972.0 | 398,791,692.0 | 411,285,714.0 | 4,952,122.3 | 5 | 40,504 | 60,491 | 40,762 | 0.012 (max is trial 1) | compiled=5 | 5,908,064.0 | 398,442,822.0 | 189,511.0 |
| `wild-logparse-quotedstring-grok` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 409,890,939.0 | 400,414,590.0 | 412,627,780.0 | 4,922,080.5 | 5 | 40,592 | 65,134 | 42,262 | 0.012 | compiled=5 | 8,072,993.0 | 399,709,587.0 | 107,841.0 |
| `wild-logparse-quotedstring-grok` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 407,351,491.0 | 396,306,483.0 | 416,717,581.0 | 7,829,227.4 | 5 | 40,504 | 60,491 | 40,762 | 0.019 | compiled=5 | 4,958,717.0 | 395,649,989.0 | 105,311.0 |
| `wild-logparse-quotedstring-grok` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 410,059,495.0 | 395,798,019.0 | 415,802,566.0 | 7,162,126.4 | 5 | 40,592 | 65,134 | 42,262 | 0.017 | compiled=5 | 7,993,293.0 | 401,886,912.0 | 107,600.0 |
| `wild-logparse-quotedstring-grok` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 356,373,547.0 | 355,108,841.0 | 358,578,781.0 | 1,195,356.4 | 5 | 35,720 | 36,838 | 35,914 | 0.003 | compiled=5 | 1,850,061.0 | 354,039,244.0 | 100,351.0 |
| `wild-logparse-quotedstring-grok` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 356,543,109.0 | 348,994,637.0 | 366,784,458.0 | 6,144,761.3 | 5 | 35,720 | 36,951 | 36,027 | 0.017 | compiled=5 | 1,828,370.0 | 354,645,088.0 | 192,691.0 |
| `wild-logparse-quotedstring-grok` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 355,329,427.0 | 350,519,808.0 | 356,680,155.0 | 2,199,897.3 | 5 | 35,720 | 36,838 | 35,914 | 0.006 (max is trial 1) | compiled=5 | 1,885,321.0 | 353,045,283.0 | 189,712.0 |
| `wild-logparse-quotedstring-grok` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 359,443,863.0 | 349,651,044.0 | 364,457,031.0 | 4,822,685.0 | 5 | 35,720 | 36,951 | 36,027 | 0.013 (max is trial 1) | compiled=5 | 1,876,941.0 | 357,485,120.0 | 109,331.0 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 358,484,120.0 | 349,410,403.0 | 376,872,343.0 | 10,492,079.7 | 5 | 40,504 | 58,043 | 38,314 | 0.029 | compiled=5 | 5,622,183.0 | 353,475,209.0 | 186,780.0 |
| `wild-logparse-quotedstring-noatomic` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 381,239,332.0 | 373,057,708.0 | 384,808,045.0 | 4,468,929.0 | 5 | 40,592 | 62,686 | 39,814 | 0.012 (max is trial 1) | compiled=5 | 16,222,906.0 | 363,873,482.0 | 101,110.0 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 356,435,272.0 | 348,362,688.0 | 358,524,863.0 | 3,621,537.6 | 5 | 40,504 | 58,043 | 38,314 | 0.010 | compiled=5 | 4,772,355.0 | 351,504,386.0 | 106,690.0 |
| `wild-logparse-quotedstring-noatomic` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 371,722,823.0 | 366,426,785.0 | 380,887,850.0 | 5,541,412.4 | 5 | 40,592 | 62,686 | 39,814 | 0.015 (max is trial 1) | compiled=5 | 7,722,091.0 | 362,998,847.0 | 192,451.0 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 315,825,045.0 | 311,332,150.0 | 316,282,618.0 | 1,855,783.3 | 5 | 31,624 | 34,390 | 33,466 | 0.006 | compiled=5 | 1,798,310.0 | 313,841,784.0 | 200,361.0 |
| `wild-logparse-quotedstring-noatomic` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 316,837,021.0 | 314,675,548.0 | 317,675,965.0 | 1,083,881.0 | 5 | 31,624 | 34,503 | 33,579 | 0.003 | compiled=5 | 1,786,191.0 | 314,862,209.0 | 191,711.0 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 317,365,660.0 | 309,354,082.0 | 323,289,736.0 | 4,613,373.5 | 5 | 31,624 | 34,390 | 33,466 | 0.015 | compiled=5 | 1,820,341.0 | 315,350,078.0 | 108,800.0 |
| `wild-logparse-quotedstring-noatomic` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 315,964,102.0 | 307,255,490.0 | 320,218,847.0 | 5,211,474.1 | 5 | 31,624 | 34,503 | 33,579 | 0.016 | compiled=5 | 1,810,621.0 | 312,101,199.0 | 110,431.0 |
| `wild-logparse-syslogbase-expanded` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 5,457,516,316.0 | 5,428,720,299.0 | 5,470,712,080.0 | 15,048,944.3 | 5 | 175,976 | 516,731 (warned) | 298,766 | 0.003 | compiled=5 | 594,748,961.0 | 4,862,664,304.0 | 187,830.0 |
| `wild-logparse-syslogbase-expanded` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 6,459,013,692.0 | 6,432,669,375.0 | 6,490,812,793.0 | 23,838,428.0 | 5 | 180,168 | 526,348 (warned) | 300,186 | 0.004 | compiled=5 | 1,585,266,873.0 | 4,868,565,339.0 | 191,761.0 |
| `wild-logparse-syslogbase-expanded` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 4,417,258,692.0 | 4,400,143,753.0 | 4,433,934,172.0 | 12,890,359.9 | 5 | 155,456 | 472,988 (warned) | 255,019 | 0.003 (max is trial 1) | compiled=5 | 591,648,683.0 | 3,825,292,858.0 | 100,490.0 |
| `wild-logparse-syslogbase-expanded` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 5,448,230,119.0 | 5,425,852,190.0 | 5,503,305,789.0 | 25,612,137.4 | 5 | 159,648 | 482,605 (warned) | 256,439 | 0.005 | compiled=5 | 1,583,306,920.0 | 3,864,716,967.0 | 187,221.0 |
| `wild-logparse-syslogbase-expanded` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 4,776,241,608.0 | 4,769,260,398.0 | 4,789,463,943.0 | 6,963,913.2 | 5 | 105,728 | 296,609 (warned) | 293,814 | 0.001 | compiled=5 | 6,352,866.0 | 4,769,668,130.0 | 166,961.0 |
| `wild-logparse-syslogbase-expanded` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 4,783,413,247.0 | 4,770,975,787.0 | 4,794,843,215.0 | 8,993,903.2 | 5 | 105,728 | 296,726 (warned) | 293,931 | 0.002 | compiled=5 | 6,368,456.0 | 4,776,945,811.0 | 195,971.0 |
| `wild-logparse-syslogbase-expanded` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 4,781,695,015.0 | 4,744,587,513.0 | 4,792,349,580.0 | 16,528,738.1 | 5 | 105,728 | 296,609 (warned) | 293,814 | 0.003 | compiled=5 | 6,438,999.0 | 4,766,155,533.0 | 193,891.0 |
| `wild-logparse-syslogbase-expanded` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 4,776,791,156.0 | 4,759,822,465.0 | 4,787,490,909.0 | 9,907,965.9 | 5 | 105,728 | 296,726 (warned) | 293,931 | 0.002 | compiled=5 | 6,539,059.0 | 4,761,894,436.0 | 186,451.0 |
| `wild-logparse-winpath-grok` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 239,843,395.0 | 233,941,122.0 | 241,438,533.0 | 2,625,667.4 | 5 | 31,960 | 36,053 | 27,569 | 0.011 | compiled=5 | 2,052,979.0 | 237,554,727.0 | 112,881.0 |
| `wild-logparse-winpath-grok` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 250,401,568.0 | 247,748,669.0 | 253,643,092.0 | 1,886,222.9 | 5 | 32,096 | 39,397 | 29,094 | 0.008 | compiled=5 | 2,170,809.0 | 247,703,629.0 | 188,580.0 |
| `wild-logparse-winpath-grok` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 238,656,470.0 | 234,833,670.0 | 239,803,416.0 | 2,061,912.0 | 5 | 31,960 | 36,053 | 27,569 | 0.009 | compiled=5 | 2,067,681.0 | 236,188,337.0 | 100,720.0 |
| `wild-logparse-winpath-grok` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 250,002,621.0 | 244,579,851.0 | 251,305,537.0 | 2,484,215.4 | 5 | 32,096 | 39,397 | 29,094 | 0.010 | compiled=5 | 2,170,391.0 | 247,749,029.0 | 110,421.0 |
| `wild-logparse-winpath-grok` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 213,822,649.0 | 213,015,145.0 | 223,609,985.0 | 4,068,075.8 | 5 | 27,400 | 23,991 | 23,529 | 0.019 | compiled=5 | 1,611,179.0 | 211,546,965.0 | 99,651.0 |
| `wild-logparse-winpath-grok` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 210,597,181.0 | 205,771,392.0 | 215,449,889.0 | 3,794,610.3 | 5 | 27,400 | 24,105 | 23,643 | 0.018 | compiled=5 | 1,610,679.0 | 208,909,591.0 | 119,851.0 |
| `wild-logparse-winpath-grok` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 213,294,147.0 | 212,355,811.0 | 225,836,923.0 | 5,079,783.5 | 5 | 27,400 | 23,991 | 23,529 | 0.024 | compiled=5 | 1,599,809.0 | 211,245,845.0 | 188,822.0 |
| `wild-logparse-winpath-grok` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 206,292,775.0 | 204,542,374.0 | 214,598,755.0 | 4,019,661.6 | 5 | 27,400 | 24,105 | 23,643 | 0.019 | compiled=5 | 1,458,059.0 | 204,621,655.0 | 108,991.0 |
| `wild-secrets-aws-access-key-id` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 247,546,609.0 | 246,747,934.0 | 253,541,432.0 | 2,476,671.0 | 5 | 36,024 | 46,375 | 29,470 | 0.010 | compiled=5 | 3,084,402.0 | 244,290,664.0 | 190,041.0 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 250,768,681.0 | 244,782,855.0 | 252,432,288.0 | 3,017,168.8 | 5 | 36,120 | 48,792 | 30,891 | 0.012 | compiled=5 | 3,165,873.0 | 247,493,438.0 | 108,320.0 |
| `wild-secrets-aws-access-key-id` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 154,639,717.0 | 146,262,603.0 | 164,547,889.0 | 6,714,289.7 | 5 | 32,032 | 39,301 | 15,035 | 0.043 | compiled=5 | 3,432,919.0 | 146,130,822.0 | 185,231.0 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 169,012,962.0 | 158,906,259.0 | 173,913,008.0 | 5,166,298.1 | 5 | 32,176 | 42,789 | 17,010 | 0.031 (max is trial 1) | compiled=5 | 3,574,949.0 | 163,093,901.0 | 100,951.0 |
| `wild-secrets-aws-access-key-id` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 220,360,407.0 | 215,206,047.0 | 223,488,964.0 | 3,258,347.8 | 5 | 27,280 | 25,437 | 24,975 | 0.015 | compiled=5 | 3,105,338.0 | 218,465,236.0 | 191,781.0 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 221,639,645.0 | 213,958,539.0 | 224,118,177.0 | 4,310,935.3 | 5 | 27,280 | 25,550 | 25,088 | 0.019 | compiled=5 | 1,633,330.0 | 219,530,442.0 | 190,162.0 |
| `wild-secrets-aws-access-key-id` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 221,000,773.0 | 214,957,267.0 | 230,856,472.0 | 5,193,368.5 | 5 | 27,280 | 25,437 | 24,975 | 0.023 | compiled=5 | 3,154,359.0 | 219,161,362.0 | 203,351.0 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 220,791,391.0 | 219,709,055.0 | 225,300,549.0 | 2,070,507.9 | 5 | 27,280 | 25,550 | 25,088 | 0.009 | compiled=5 | 1,651,920.0 | 218,421,017.0 | 184,311.0 |
| `wild-secrets-github-pat` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 389,454,325.0 | 387,052,976.0 | 394,052,334.0 | 2,330,887.1 | 5 | 40,040 | 56,740 | 26,630 | 0.006 | compiled=5 | 4,338,658.0 | 384,153,024.0 | 203,241.0 |
| `wild-secrets-github-pat` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 390,390,209.0 | 376,449,803.0 | 401,028,933.0 | 8,651,498.9 | 5 | 40,136 | 59,994 | 28,051 | 0.022 (max is trial 1) | compiled=5 | 4,407,188.0 | 385,865,041.0 | 193,031.0 |
| `wild-secrets-github-pat` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 165,278,472.0 | 162,614,018.0 | 176,270,180.0 | 4,724,860.7 | 5 | 40,224 | 61,078 | 15,834 | 0.029 | compiled=5 | 5,401,198.0 | 159,584,312.0 | 102,570.0 |
| `wild-secrets-github-pat` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 176,688,562.0 | 175,185,936.0 | 194,794,469.0 | 8,065,606.2 | 5 | 40,368 | 65,816 | 17,809 | 0.046 (max is trial 1) | compiled=5 | 5,468,119.0 | 171,229,244.0 | 114,951.0 |
| `wild-secrets-github-pat` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 345,884,778.0 | 344,113,638.0 | 357,892,798.0 | 5,375,142.2 | 5 | 27,160 | 21,526 | 21,295 | 0.016 (max is trial 1) | compiled=5 | 1,540,489.0 | 344,305,939.0 | 190,461.0 |
| `wild-secrets-github-pat` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 346,394,281.0 | 345,308,624.0 | 362,711,035.0 | 6,519,531.7 | 5 | 27,160 | 21,639 | 21,408 | 0.019 (max is trial 1) | compiled=5 | 1,545,989.0 | 344,734,932.0 | 201,122.0 |
| `wild-secrets-github-pat` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 349,460,752.0 | 342,330,018.0 | 354,702,585.0 | 4,729,398.0 | 5 | 27,160 | 21,526 | 21,295 | 0.014 | compiled=5 | 1,558,549.0 | 347,804,682.0 | 184,781.0 |
| `wild-secrets-github-pat` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 346,160,163.0 | 337,359,189.0 | 347,598,480.0 | 4,470,277.8 | 5 | 27,160 | 21,639 | 21,408 | 0.013 | compiled=5 | 1,582,690.0 | 344,479,172.0 | 108,980.0 |
| `wild-secrets-slack-webhook-url` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 280,214,701.0 | 273,396,273.0 | 289,190,378.0 | 5,814,172.1 | 5 | 52,360 | 103,904 | 32,554 | 0.021 (max is trial 1) | compiled=5 | 7,296,769.0 | 271,565,865.0 | 104,240.0 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 282,505,010.0 | 280,682,923.0 | 290,143,041.0 | 4,115,953.5 | 5 | 52,456 | 111,143 | 33,982 | 0.015 | compiled=5 | 7,789,132.0 | 274,524,218.0 | 196,391.0 |
| `wild-secrets-slack-webhook-url` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 205,637,896.0 | 204,270,789.0 | 213,423,677.0 | 4,164,925.7 | 5 | 52,408 | 109,149 | 17,440 | 0.020 (max is trial 1) | compiled=5 | 8,255,533.0 | 195,894,324.0 | 191,481.0 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 224,493,575.0 | 206,219,910.0 | 226,725,359.0 | 7,634,064.5 | 5 | 56,640 | 117,707 | 19,304 | 0.034 | compiled=5 | 19,195,121.0 | 206,507,801.0 | 105,570.0 |
| `wild-secrets-slack-webhook-url` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 216,707,056.0 | 213,102,605.0 | 222,674,021.0 | 3,488,247.6 | 5 | 27,280 | 26,996 | 26,533 | 0.016 | compiled=5 | 3,366,410.0 | 213,026,285.0 | 106,351.0 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 218,836,398.0 | 213,464,427.0 | 234,062,524.0 | 7,458,815.3 | 5 | 27,280 | 27,109 | 26,646 | 0.034 (max is trial 1) | compiled=5 | 1,666,700.0 | 217,007,137.0 | 194,811.0 |
| `wild-secrets-slack-webhook-url` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 222,876,066.0 | 215,984,083.0 | 228,544,078.0 | 4,150,613.8 | 5 | 27,280 | 26,996 | 26,533 | 0.019 | compiled=5 | 1,681,580.0 | 219,051,562.0 | 109,570.0 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 217,722,063.0 | 205,995,863.0 | 219,561,425.0 | 4,999,985.2 | 5 | 27,280 | 27,109 | 26,646 | 0.023 | compiled=5 | 1,710,540.0 | 215,978,573.0 | 189,171.0 |
| `wild-secrets-username-password-pair` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 577,498,591.0 | 557,551,140.0 | 593,405,605.0 | 11,894,881.0 | 5 | 208,424 | 552,395 (warned) | 43,128 | 0.021 | compiled=5 | 67,222,714.0 | 502,364,385.0 | 196,541.0 |
| `wild-secrets-username-password-pair` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 591,027,576.0 | 584,754,021.0 | 592,456,203.0 | 2,718,182.4 | 5 | 212,616 | 567,185 (warned) | 44,416 | 0.005 | compiled=5 | 70,136,026.0 | 520,868,541.0 | 199,391.0 |
| `wild-secrets-username-password-pair` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 382,487,620.0 | 360,150,391.0 | 388,350,992.0 | 11,127,423.2 | 5 | 208,016 | 560,271 (warned) | 16,585 | 0.029 | compiled=5 | 68,578,212.0 | 308,254,128.0 | 181,361.0 |
| `wild-secrets-username-password-pair` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 386,674,822.0 | 376,168,985.0 | 387,379,836.0 | 5,183,291.5 | 5 | 216,344 | 576,684 (warned) | 18,313 | 0.013 | compiled=5 | 65,278,585.0 | 321,197,606.0 | 193,751.0 |
| `wild-secrets-username-password-pair` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 350,365,383.0 | 341,218,710.0 | 352,423,675.0 | 3,883,898.0 | 5 | 35,880 | 39,595 | 37,746 | 0.011 | compiled=5 | 1,955,851.0 | 346,246,580.0 | 193,421.0 |
| `wild-secrets-username-password-pair` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 348,273,532.0 | 342,016,044.0 | 350,976,938.0 | 3,013,228.4 | 5 | 35,880 | 39,708 | 37,859 | 0.009 (max is trial 1) | compiled=5 | 1,988,391.0 | 346,227,090.0 | 114,310.0 |
| `wild-secrets-username-password-pair` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 348,409,945.0 | 335,217,426.0 | 350,216,606.0 | 5,765,634.3 | 5 | 35,880 | 39,595 | 37,746 | 0.017 (max is trial 1) | compiled=5 | 1,963,411.0 | 346,074,681.0 | 112,291.0 |
| `wild-secrets-username-password-pair` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 348,751,168.0 | 344,402,631.0 | 351,028,462.0 | 2,226,696.3 | 5 | 35,880 | 39,708 | 37,859 | 0.006 | compiled=5 | 1,958,952.0 | 346,607,535.0 | 102,911.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 155,664,883.0 | 147,676,202.0 | 157,832,014.0 | 3,614,464.3 | 5 | 27,608 | 19,872 | 14,165 | 0.023 | compiled=5 | 1,768,248.0 | 153,806,616.0 | 99,430.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 162,173,990.0 | 158,866,817.0 | 163,778,796.0 | 1,828,577.2 | 5 | 27,752 | 21,932 | 15,325 | 0.011 | compiled=5 | 1,965,598.0 | 160,075,151.0 | 112,170.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 156,056,895.0 | 147,365,908.0 | 159,175,061.0 | 4,182,025.6 | 5 | 27,608 | 19,872 | 14,165 | 0.027 | compiled=5 | 1,776,769.0 | 153,261,979.0 | 186,981.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 158,178,725.0 | 157,946,753.0 | 163,263,402.0 | 2,088,048.2 | 5 | 27,752 | 21,932 | 15,325 | 0.013 (max is trial 1) | compiled=5 | 1,817,069.0 | 156,263,745.0 | 192,381.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 168,944,581.0 | 163,277,229.0 | 169,176,703.0 | 2,263,310.8 | 5 | 23,104 | 19,147 | 19,147 | 0.013 (max is trial 1) | compiled=5 | 1,528,179.0 | 167,264,051.0 | 101,911.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 171,092,173.0 | 170,496,579.0 | 178,430,865.0 | 2,989,233.4 | 5 | 23,104 | 19,260 | 19,260 | 0.017 | compiled=5 | 1,490,149.0 | 169,222,873.0 | 117,831.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 168,751,331.0 | 160,592,061.0 | 169,696,416.0 | 3,634,337.8 | 5 | 23,104 | 19,147 | 19,147 | 0.022 | compiled=5 | 1,515,429.0 | 167,207,451.0 | 98,650.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 169,679,196.0 | 162,795,975.0 | 170,507,401.0 | 2,830,964.0 | 5 | 23,104 | 19,260 | 19,260 | 0.017 (max is trial 1) | compiled=5 | 1,494,159.0 | 167,328,252.0 | 185,571.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 161,764,569.0 | 160,413,481.0 | 176,945,321.0 | 6,179,620.8 | 5 | 27,752 | 21,931 | 16,150 | 0.038 | compiled=5 | 1,777,757.0 | 160,000,582.0 | 195,331.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 160,806,025.0 | 160,448,892.0 | 168,303,625.0 | 2,999,616.4 | 5 | 27,752 | 21,503 | 15,722 | 0.019 | compiled=5 | 1,802,377.0 | 158,724,217.0 | 188,861.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 162,186,976.0 | 150,801,827.0 | 170,667,952.0 | 6,533,776.2 | 5 | 27,752 | 21,931 | 16,150 | 0.040 (max is trial 1) | compiled=5 | 1,756,089.0 | 160,238,806.0 | 192,641.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 162,136,596.0 | 161,219,242.0 | 162,966,952.0 | 556,961.0 | 5 | 27,752 | 21,503 | 15,722 | 0.003 | compiled=5 | 1,782,850.0 | 160,130,356.0 | 109,401.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 146,049,009.0 | 138,914,938.0 | 151,410,150.0 | 4,385,816.5 | 5 | 23,072 | 18,332 | 18,332 | 0.030 | compiled=5 | 1,433,048.0 | 144,520,981.0 | 106,500.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 143,984,967.0 | 141,323,403.0 | 150,165,283.0 | 3,011,946.3 | 5 | 23,072 | 18,444 | 18,444 | 0.021 | compiled=5 | 1,458,798.0 | 142,338,968.0 | 188,801.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 148,069,687.0 | 140,903,884.0 | 152,133,951.0 | 4,716,724.5 | 5 | 23,072 | 18,332 | 18,332 | 0.032 | compiled=5 | 1,465,298.0 | 146,390,477.0 | 190,351.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 146,681,927.0 | 139,762,836.0 | 151,027,224.0 | 3,888,754.3 | 5 | 23,072 | 18,444 | 18,444 | 0.027 | compiled=5 | 1,532,399.0 | 143,712,480.0 | 110,940.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 218,129,728.0 | 212,106,013.0 | 223,130,498.0 | 3,932,184.3 | 5 | 31,792 | 30,836 | 26,002 | 0.018 | compiled=5 | 1,853,348.0 | 216,169,490.0 | 100,560.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 221,713,492.0 | 215,027,666.0 | 224,088,643.0 | 3,522,135.0 | 5 | 31,880 | 32,315 | 27,251 | 0.016 | compiled=5 | 1,844,967.0 | 219,776,255.0 | 201,470.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 155,202,050.0 | 147,714,180.0 | 159,135,820.0 | 4,115,865.0 | 5 | 27,608 | 20,475 | 13,956 | 0.027 | compiled=5 | 1,757,059.0 | 151,978,222.0 | 107,410.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 162,771,440.0 | 154,434,896.0 | 165,927,946.0 | 3,903,756.4 | 5 | 27,744 | 22,624 | 15,753 | 0.024 | compiled=5 | 1,794,189.0 | 160,401,697.0 | 99,860.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 190,795,056.0 | 183,282,533.0 | 192,440,687.0 | 3,210,910.0 | 5 | 27,320 | 21,614 | 21,614 | 0.017 | compiled=5 | 1,505,149.0 | 188,581,414.0 | 107,801.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 189,893,172.0 | 181,020,682.0 | 200,802,564.0 | 6,935,529.2 | 5 | 27,320 | 21,728 | 21,728 | 0.037 | compiled=5 | 1,507,348.0 | 188,191,982.0 | 189,721.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 190,630,241.0 | 184,657,215.0 | 193,897,231.0 | 3,125,885.6 | 5 | 27,320 | 21,614 | 21,614 | 0.016 | compiled=5 | 1,554,429.0 | 188,976,371.0 | 211,031.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 192,384,612.0 | 190,954,584.0 | 195,088,128.0 | 1,361,989.5 | 5 | 27,320 | 21,728 | 21,728 | 0.007 | compiled=5 | 1,528,539.0 | 190,394,390.0 | 107,611.0 |
| `wild-validator-email-owasp` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 142,184,029.0 | 140,545,341.0 | 150,946,274.0 | 3,745,181.8 | 5 | 27,432 | 14,458 | 12,101 | 0.026 | compiled=5 | 1,900,047.0 | 139,998,539.0 | 191,781.0 |
| `wild-validator-email-owasp` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 142,160,099.0 | 127,449,789.0 | 146,469,016.0 | 8,582,250.6 | 5 | 27,432 | 14,281 | 11,924 | 0.060 | compiled=5 | 1,529,846.0 | 138,871,585.0 | 206,951.0 |
| `wild-validator-email-owasp` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 143,201,516.0 | 134,079,778.0 | 145,896,719.0 | 5,116,468.8 | 5 | 27,432 | 14,458 | 12,101 | 0.036 | compiled=5 | 1,507,168.0 | 141,648,668.0 | 111,540.0 |
| `wild-validator-email-owasp` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 139,557,307.0 | 133,377,613.0 | 145,557,438.0 | 4,613,503.7 | 5 | 27,432 | 14,281 | 11,924 | 0.033 | compiled=5 | 1,534,948.0 | 137,893,258.0 | 184,181.0 |
| `wild-validator-email-owasp` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 224,937,673.0 | 214,921,034.0 | 232,908,539.0 | 6,107,446.1 | 5 | 27,440 | 26,143 | 25,450 | 0.027 | compiled=5 | 1,423,388.0 | 223,320,514.0 | 107,480.0 |
| `wild-validator-email-owasp` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 226,057,349.0 | 221,543,364.0 | 232,138,123.0 | 3,817,342.9 | 5 | 27,440 | 26,256 | 25,563 | 0.017 | compiled=5 | 1,545,518.0 | 223,621,455.0 | 117,980.0 |
| `wild-validator-email-owasp` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 236,477,196.0 | 225,546,319.0 | 240,840,952.0 | 5,293,708.8 | 5 | 27,440 | 26,143 | 25,450 | 0.022 | compiled=5 | 1,626,789.0 | 233,104,346.0 | 108,830.0 |
| `wild-validator-email-owasp` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 232,838,785.0 | 223,798,010.0 | 237,307,261.0 | 4,594,771.6 | 5 | 27,440 | 26,256 | 25,563 | 0.020 | compiled=5 | 1,638,530.0 | 231,098,744.0 | 183,782.0 |
| `wild-validator-ipv4-owasp` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 330,067,534.0 | 308,277,725.0 | 348,217,195.0 | 14,609,530.7 | 5 | 40,776 | 44,485 | 39,457 | 0.044 | compiled=5 | 4,127,026.0 | 327,895,255.0 | 201,651.0 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 310,108,823.0 | 309,922,872.0 | 319,858,233.0 | 3,886,948.2 | 5 | 40,568 | 43,668 | 38,640 | 0.013 | compiled=5 | 2,048,669.0 | 307,847,893.0 | 195,601.0 |
| `wild-validator-ipv4-owasp` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 162,820,879.0 | 156,548,006.0 | 171,562,206.0 | 6,052,582.1 | 5 | 32,424 | 21,844 | 16,816 | 0.037 | compiled=5 | 1,641,229.0 | 156,209,384.0 | 199,641.0 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 160,832,910.0 | 153,638,131.0 | 163,127,272.0 | 3,415,492.1 | 5 | 32,224 | 20,922 | 15,894 | 0.021 | compiled=5 | 1,639,199.0 | 157,593,572.0 | 192,001.0 |
| `wild-validator-ipv4-owasp` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 278,341,559.0 | 267,026,474.0 | 279,086,304.0 | 5,267,987.2 | 5 | 27,240 | 31,561 | 31,561 | 0.019 | compiled=5 | 1,873,461.0 | 275,457,963.0 | 190,031.0 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 275,603,664.0 | 268,494,241.0 | 278,466,079.0 | 3,412,854.8 | 5 | 27,240 | 31,674 | 31,674 | 0.012 (max is trial 1) | compiled=5 | 1,720,310.0 | 273,784,223.0 | 102,970.0 |
| `wild-validator-ipv4-owasp` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 276,704,646.0 | 271,643,705.0 | 281,796,497.0 | 3,226,781.5 | 5 | 27,240 | 31,561 | 31,561 | 0.012 | compiled=5 | 1,694,800.0 | 274,887,566.0 | 111,941.0 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 275,645,520.0 | 268,289,316.0 | 275,772,771.0 | 2,881,984.7 | 5 | 27,240 | 31,674 | 31,674 | 0.010 | compiled=5 | 1,758,090.0 | 273,798,809.0 | 98,481.0 |
| `wild-validator-us-zip-owasp` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 204,581,033.0 | 195,476,595.0 | 207,486,435.0 | 4,442,290.9 | 5 | 31,888 | 26,794 | 24,250 | 0.022 | compiled=5 | 1,703,057.0 | 202,842,066.0 | 103,970.0 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 204,347,672.0 | 199,864,995.0 | 205,474,137.0 | 1,968,380.1 | 5 | 31,808 | 26,534 | 23,990 | 0.010 | compiled=5 | 1,701,637.0 | 201,542,071.0 | 99,320.0 |
| `wild-validator-us-zip-owasp` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 153,293,859.0 | 139,816,428.0 | 153,799,512.0 | 5,392,996.6 | 5 | 27,672 | 15,696 | 13,152 | 0.035 | compiled=5 | 1,515,228.0 | 151,570,690.0 | 204,611.0 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 143,483,667.0 | 130,331,018.0 | 148,474,075.0 | 6,863,947.3 | 5 | 23,496 | 15,333 | 12,789 | 0.048 | compiled=5 | 1,468,518.0 | 141,813,669.0 | 108,561.0 |
| `wild-validator-us-zip-owasp` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 184,890,743.0 | 177,231,979.0 | 187,649,088.0 | 3,811,996.8 | 5 | 27,200 | 20,258 | 20,258 | 0.021 | compiled=5 | 1,520,649.0 | 182,828,391.0 | 109,841.0 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 184,544,421.0 | 179,545,852.0 | 193,778,023.0 | 4,609,462.0 | 5 | 27,200 | 20,369 | 20,369 | 0.025 | compiled=5 | 2,968,687.0 | 182,793,621.0 | 188,731.0 |
| `wild-validator-us-zip-owasp` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 185,497,760.0 | 177,521,792.0 | 192,554,423.0 | 5,278,274.6 | 5 | 27,200 | 20,258 | 20,258 | 0.028 | compiled=5 | 1,525,819.0 | 183,748,170.0 | 194,771.0 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 184,754,777.0 | 177,464,093.0 | 186,455,667.0 | 3,790,212.3 | 5 | 27,200 | 20,369 | 20,369 | 0.021 | compiled=5 | 1,586,119.0 | 182,961,055.0 | 106,061.0 |
| `wild-validator-uuid-grok` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 244,832,497.0 | 235,066,948.0 | 251,000,153.0 | 6,123,435.6 | 5 | 36,384 | 46,458 | 21,140 | 0.025 | compiled=5 | 6,611,227.0 | 241,727,304.0 | 100,540.0 |
| `wild-validator-uuid-grok` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 252,387,167.0 | 244,486,205.0 | 257,462,818.0 | 4,294,856.5 | 5 | 36,528 | 49,319 | 22,728 | 0.017 | compiled=5 | 5,861,664.0 | 246,935,015.0 | 112,281.0 |
| `wild-validator-uuid-grok` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 242,248,500.0 | 233,781,416.0 | 244,193,829.0 | 3,844,995.8 | 5 | 36,384 | 46,458 | 21,140 | 0.016 | compiled=5 | 3,226,777.0 | 239,136,713.0 | 101,301.0 |
| `wild-validator-uuid-grok` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 249,179,077.0 | 241,365,405.0 | 252,076,370.0 | 3,691,610.9 | 5 | 36,528 | 49,319 | 22,728 | 0.015 | compiled=5 | 3,048,656.0 | 246,022,560.0 | 176,790.0 |
| `wild-validator-uuid-grok` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 252,722,353.0 | 245,718,522.0 | 256,745,117.0 | 4,345,987.8 | 5 | 27,208 | 20,758 | 20,527 | 0.017 (max is trial 1) | compiled=5 | 1,533,578.0 | 251,095,833.0 | 203,941.0 |
| `wild-validator-uuid-grok` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 254,951,884.0 | 249,124,190.0 | 256,403,923.0 | 3,261,237.1 | 5 | 27,208 | 20,869 | 20,638 | 0.013 | compiled=5 | 1,537,539.0 | 253,035,104.0 | 191,331.0 |
| `wild-validator-uuid-grok` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 253,059,695.0 | 252,596,193.0 | 255,252,258.0 | 1,123,000.0 | 5 | 27,208 | 20,758 | 20,527 | 0.004 (max is trial 1) | compiled=5 | 1,540,879.0 | 251,309,874.0 | 191,252.0 |
| `wild-validator-uuid-grok` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 255,461,078.0 | 247,623,032.0 | 257,632,553.0 | 4,379,472.1 | 5 | 27,208 | 20,869 | 20,638 | 0.017 | compiled=5 | 1,520,969.0 | 253,837,239.0 | 188,521.0 |
| `wild-waf-crs-942140-dbnames` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 226,415,382.0 | 218,740,610.0 | 232,056,846.0 | 4,411,964.8 | 5 | 85,552 | 226,458 | 18,492 | 0.019 (max is trial 1) | compiled=5 | 14,220,928.0 | 211,226,400.0 | 192,061.0 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 233,263,258.0 | 227,851,009.0 | 250,034,178.0 | 7,680,724.7 | 5 | 89,792 | 236,289 | 20,468 | 0.033 | compiled=5 | 15,889,215.0 | 217,227,274.0 | 102,781.0 |
| `wild-waf-crs-942140-dbnames` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 226,976,609.0 | 223,766,932.0 | 243,698,588.0 | 7,141,818.7 | 5 | 85,552 | 226,458 | 18,492 | 0.031 (max is trial 1) | compiled=5 | 14,220,765.0 | 211,996,709.0 | 191,321.0 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 242,071,298.0 | 230,625,397.0 | 252,822,395.0 | 7,110,573.9 | 5 | 89,792 | 236,289 | 20,468 | 0.029 | compiled=5 | 18,841,579.0 | 217,880,480.0 | 198,011.0 |
| `wild-waf-crs-942140-dbnames` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 438,749,852.0 | 434,377,716.0 | 445,779,382.0 | 4,022,028.4 | 5 | 31,376 | 59,509 | 59,046 | 0.009 | compiled=5 | 2,246,513.0 | 433,656,872.0 | 111,881.0 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 443,116,797.0 | 435,279,161.0 | 459,252,948.0 | 7,876,320.3 | 5 | 31,376 | 59,624 | 59,161 | 0.018 (max is trial 1) | compiled=5 | 2,265,163.0 | 440,748,943.0 | 99,600.0 |
| `wild-waf-crs-942140-dbnames` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 442,440,388.0 | 433,720,037.0 | 457,266,467.0 | 7,767,717.3 | 5 | 31,376 | 59,509 | 59,046 | 0.018 | compiled=5 | 2,281,843.0 | 439,558,311.0 | 193,361.0 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 443,984,408.0 | 442,034,615.0 | 455,404,497.0 | 4,958,709.4 | 5 | 31,376 | 59,624 | 59,161 | 0.011 | compiled=5 | 2,295,634.0 | 440,030,194.0 | 112,630.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 185,454,795.0 | 182,824,224.0 | 199,655,333.0 | 6,443,616.5 | 5 | 36,248 | 56,740 | 16,340 | 0.035 | compiled=5 | 4,347,768.0 | 180,906,517.0 | 201,031.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 200,009,155.0 | 199,671,303.0 | 206,916,343.0 | 2,798,931.4 | 5 | 36,392 | 60,519 | 18,131 | 0.014 (max is trial 1) | compiled=5 | 4,868,190.0 | 195,042,924.0 | 190,501.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 193,282,051.0 | 184,621,615.0 | 205,927,617.0 | 6,860,996.4 | 5 | 36,248 | 56,740 | 16,340 | 0.035 | compiled=5 | 4,640,525.0 | 188,408,305.0 | 195,401.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 205,518,746.0 | 192,353,094.0 | 208,677,392.0 | 6,196,057.4 | 5 | 36,392 | 60,519 | 18,131 | 0.030 | compiled=5 | 11,257,659.0 | 197,185,091.0 | 107,460.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 222,383,578.0 | 217,643,240.0 | 226,395,121.0 | 3,190,422.7 | 5 | 27,280 | 25,397 | 24,935 | 0.014 | compiled=5 | 1,743,310.0 | 220,614,918.0 | 189,142.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 224,213,988.0 | 215,728,250.0 | 226,541,433.0 | 3,752,151.3 | 5 | 27,280 | 25,510 | 25,048 | 0.017 | compiled=5 | 1,647,530.0 | 222,019,106.0 | 108,611.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 225,248,458.0 | 221,323,375.0 | 233,036,995.0 | 4,712,304.4 | 5 | 27,280 | 25,397 | 24,935 | 0.021 | compiled=5 | 1,845,621.0 | 221,838,838.0 | 119,571.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 224,369,993.0 | 223,421,847.0 | 226,843,818.0 | 1,187,371.4 | 5 | 27,280 | 25,510 | 25,048 | 0.005 | compiled=5 | 1,937,651.0 | 222,209,000.0 | 185,011.0 |
| `wild-waf-crs-942270-union-select` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 161,417,966.0 | 157,732,351.0 | 178,962,688.0 | 7,857,327.2 | 5 | 27,872 | 35,424 | 14,257 | 0.049 | compiled=5 | 3,106,343.0 | 155,123,421.0 | 106,961.0 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 176,098,096.0 | 169,527,380.0 | 180,816,686.0 | 3,642,275.3 | 5 | 32,112 | 38,448 | 16,269 | 0.021 (max is trial 1) | compiled=5 | 3,190,563.0 | 172,829,093.0 | 102,101.0 |
| `wild-waf-crs-942270-union-select` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 159,528,052.0 | 157,958,454.0 | 169,904,398.0 | 4,621,595.0 | 5 | 27,872 | 35,424 | 14,257 | 0.029 | compiled=5 | 2,904,326.0 | 156,582,887.0 | 101,700.0 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 171,009,113.0 | 160,018,366.0 | 180,398,403.0 | 7,237,121.6 | 5 | 32,112 | 38,448 | 16,269 | 0.042 | compiled=5 | 3,175,627.0 | 167,623,775.0 | 188,061.0 |
| `wild-waf-crs-942270-union-select` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 190,297,394.0 | 184,100,878.0 | 191,684,372.0 | 2,655,290.1 | 5 | 27,240 | 22,695 | 22,464 | 0.014 (max is trial 1) | compiled=5 | 1,556,959.0 | 188,253,782.0 | 106,380.0 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 190,264,224.0 | 183,542,216.0 | 193,271,580.0 | 3,249,163.3 | 5 | 27,240 | 22,808 | 22,577 | 0.017 (max is trial 1) | compiled=5 | 1,548,589.0 | 188,505,374.0 | 104,231.0 |
| `wild-waf-crs-942270-union-select` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 192,755,054.0 | 182,637,833.0 | 197,487,193.0 | 5,481,483.0 | 5 | 27,240 | 22,695 | 22,464 | 0.028 | compiled=5 | 1,561,609.0 | 191,004,333.0 | 173,191.0 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 191,276,395.0 | 189,271,513.0 | 194,155,282.0 | 1,661,774.9 | 5 | 27,240 | 22,808 | 22,577 | 0.009 (max is trial 1) | compiled=5 | 1,575,340.0 | 189,597,185.0 | 184,561.0 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 1,447,004,181.0 | 1,424,664,120.0 | 1,454,402,151.0 | 10,484,723.9 | 5 | 680,264 | 393,519 (warned) | 99,039 | 0.007 (max is trial 1) | compiled=5 | 11,969,219.0 | 1,433,181,825.0 | 495,842.0 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 1,379,532,285.0 | 1,371,689,154.0 | 1,434,351,309.0 | 22,936,001.9 | 5 | 659,736 | 400,725 (warned) | 101,189 | 0.017 (max is trial 1) | compiled=5 | 12,470,631.0 | 1,366,824,284.0 | 279,871.0 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 1,442,423,788.0 | 1,421,932,468.0 | 1,460,226,301.0 | 13,101,288.5 | 5 | 680,264 | 393,519 (warned) | 99,039 | 0.009 | compiled=5 | 14,331,576.0 | 1,427,545,078.0 | 277,852.0 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 1,388,269,229.0 | 1,372,056,065.0 | 1,399,357,009.0 | 10,300,023.2 | 5 | 659,736 | 400,725 (warned) | 101,189 | 0.007 (max is trial 1) | compiled=5 | 12,539,996.0 | 1,375,232,932.0 | 524,293.0 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 1,652,693,638.0 | 1,649,314,218.0 | 1,666,532,506.0 | 6,823,543.6 | 5 | 60,264 | 182,804 | 181,181 | 0.004 (max is trial 1) | compiled=5 | 4,499,196.0 | 1,648,072,881.0 | 105,291.0 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 1,665,158,299.0 | 1,657,133,573.0 | 1,676,007,732.0 | 6,732,545.8 | 5 | 60,264 | 182,919 | 181,296 | 0.004 | compiled=5 | 5,326,990.0 | 1,660,558,033.0 | 102,431.0 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 1,654,526,023.0 | 1,641,963,441.0 | 1,676,831,779.0 | 11,330,226.6 | 5 | 60,264 | 182,804 | 181,181 | 0.007 | compiled=5 | 5,377,153.0 | 1,649,644,375.0 | 109,561.0 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 1,662,390,931.0 | 1,658,752,210.0 | 1,666,053,053.0 | 2,350,287.8 | 5 | 60,264 | 182,919 | 181,296 | 0.001 | compiled=5 | 4,539,157.0 | 1,657,776,974.0 | 103,260.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 152,325,701.0 | 145,598,934.0 | 160,676,034.0 | 5,559,199.6 | 5 | 27,608 | 19,611 | 13,699 | 0.036 | compiled=5 | 1,980,478.0 | 149,879,861.0 | 191,060.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 163,851,146.0 | 152,372,350.0 | 167,394,352.0 | 5,100,990.5 | 5 | 27,752 | 22,218 | 15,788 | 0.031 | compiled=5 | 2,016,888.0 | 159,835,821.0 | 102,801.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 152,935,067.0 | 142,455,092.0 | 155,917,694.0 | 4,738,028.5 | 5 | 27,608 | 19,611 | 13,699 | 0.031 | compiled=5 | 2,299,732.0 | 150,503,274.0 | 114,171.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 164,156,966.0 | 154,617,957.0 | 165,691,524.0 | 4,102,585.7 | 5 | 27,752 | 22,218 | 15,788 | 0.025 | compiled=5 | 1,968,990.0 | 160,459,937.0 | 102,511.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 188,678,114.0 | 180,873,859.0 | 192,853,998.0 | 4,142,298.4 | 5 | 27,320 | 21,895 | 21,202 | 0.022 | compiled=5 | 1,571,679.0 | 187,014,314.0 | 106,750.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 190,117,532.0 | 183,929,177.0 | 198,205,208.0 | 4,857,299.9 | 5 | 27,320 | 22,008 | 21,315 | 0.026 | compiled=5 | 1,591,059.0 | 188,340,632.0 | 213,501.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 188,128,886.0 | 186,751,239.0 | 203,815,450.0 | 6,310,581.8 | 5 | 27,320 | 21,895 | 21,202 | 0.034 (max is trial 1) | compiled=5 | 1,576,789.0 | 186,467,446.0 | 103,010.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 190,706,772.0 | 188,349,978.0 | 192,666,454.0 | 1,834,807.0 | 5 | 27,320 | 22,008 | 21,315 | 0.010 | compiled=5 | 3,109,618.0 | 188,911,251.0 | 193,811.0 |
| `winpath-near-miss` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 138,120,293.0 | 131,663,636.0 | 146,735,777.0 | 5,572,061.5 | 5 | 27,392 | 13,845 | 11,762 | 0.040 | compiled=5 | 1,465,416.0 | 136,165,174.0 | 102,580.0 |
| `winpath-near-miss` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 142,102,979.0 | 130,844,361.0 | 146,468,986.0 | 5,286,318.8 | 5 | 23,256 | 13,668 | 11,585 | 0.037 | compiled=5 | 1,517,326.0 | 140,559,503.0 | 107,190.0 |
| `winpath-near-miss` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 140,544,022.0 | 136,280,980.0 | 149,877,832.0 | 4,737,208.6 | 5 | 27,392 | 13,845 | 11,762 | 0.034 | compiled=5 | 1,473,858.0 | 138,927,293.0 | 197,821.0 |
| `winpath-near-miss` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 137,211,015.0 | 125,326,352.0 | 143,742,830.0 | 6,035,571.8 | 5 | 23,256 | 13,668 | 11,585 | 0.044 | compiled=5 | 1,585,928.0 | 135,524,916.0 | 190,131.0 |
| `winpath-near-miss` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 200,806,954.0 | 194,365,796.0 | 201,524,898.0 | 3,255,671.6 | 5 | 27,400 | 23,634 | 23,172 | 0.016 (max is trial 1) | compiled=5 | 1,544,019.0 | 198,199,189.0 | 120,020.0 |
| `winpath-near-miss` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 195,487,563.0 | 193,601,122.0 | 201,753,340.0 | 3,561,370.7 | 5 | 27,400 | 23,747 | 23,285 | 0.018 | compiled=5 | 1,707,319.0 | 193,677,143.0 | 103,101.0 |
| `winpath-near-miss` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 199,598,376.0 | 191,200,986.0 | 205,965,414.0 | 5,868,461.1 | 5 | 27,400 | 23,634 | 23,172 | 0.029 | compiled=5 | 1,593,970.0 | 197,764,764.0 | 186,732.0 |
| `winpath-near-miss` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 200,906,543.0 | 188,288,768.0 | 203,965,930.0 | 6,105,428.1 | 5 | 27,400 | 23,747 | 23,285 | 0.030 | compiled=5 | 1,600,880.0 | 199,206,852.0 | 106,330.0 |

### `eager-jit`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `balanced-parens-rec` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 23,940.0 | 20,160.0 | 95,441.0 | 28,746.8 | 5 | 209 | 1.201 (max is trial 1) | compiled=5 |
| `balanced-parens-rec` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `balanced-parens-rec` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `balanced-parens-rec` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `balanced-parens-rec` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `base10num-near-miss` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 13,050.0 | 10,880.0 | 83,390.0 | 28,190.1 | 5 | 220 | timer-floor (max is trial 1) | compiled=5 |
| `base10num-near-miss` | `plain` | `re2_11.0.0_default-caps-simdna` | 24,310.0 | 19,370.0 | 128,541.0 | 42,092.4 | 5 | 13 | timer-floor (max is trial 1) | compiled=5 |
| `base10num-near-miss` | `plain` | `re2_11.0.0_longest-caps-simdna` | 25,250.0 | 19,031.0 | 139,081.0 | 46,269.9 | 5 | 13 | timer-floor (max is trial 1) | compiled=5 |
| `base10num-near-miss` | `plain` | `rust_1.13.1_default-caps-simdna` | 140,811.0 | 131,460.0 | 688,222.0 | 214,722.6 | 5 | - | 1.525 (max is trial 1) | compiled=5 |
| `base10num-near-miss` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 119,471.0 | 101,620.0 | 585,952.0 | 183,436.1 | 5 | - | 1.535 (max is trial 1) | compiled=5 |
| `base10num-near-miss` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 3,011,236.0 | 2,950,235.0 | 4,223,783.0 | 495,453.0 | 5 | 5,896 | 0.165 (max is trial 1) | compiled=5 |
| `base10num-near-miss` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 3,115,027.0 | 2,977,666.0 | 4,598,145.0 | 604,604.3 | 5 | 6,376 | 0.194 (max is trial 1) | compiled=5 |
| `bracket-array-define` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 24,590.0 | 17,020.0 | 97,961.0 | 30,721.3 | 5 | 240 | timer-floor (max is trial 1) | compiled=5 |
| `bracket-array-define` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `bracket-array-define` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `bracket-array-define` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `bracket-array-define` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `codegrammar-flat` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 18,410.0 | 16,670.0 | 89,860.0 | 28,558.1 | 5 | 211 | timer-floor (max is trial 1) | compiled=5 |
| `codegrammar-flat` | `plain` | `re2_11.0.0_default-caps-simdna` | 28,290.0 | 20,720.0 | 134,331.0 | 43,202.3 | 5 | 19 | 1.527 (max is trial 1) | compiled=5 |
| `codegrammar-flat` | `plain` | `re2_11.0.0_longest-caps-simdna` | 11,420.0 | 8,470.0 | 68,121.0 | 22,619.6 | 5 | 19 | timer-floor (max is trial 1) | compiled=5 |
| `codegrammar-flat` | `plain` | `rust_1.13.1_default-caps-simdna` | 192,660.0 | 178,340.0 | 1,171,524.0 | 388,211.7 | 5 | - | 2.015 (max is trial 1) | compiled=5 |
| `codegrammar-flat` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 86,081.0 | 65,380.0 | 527,902.0 | 176,294.9 | 5 | - | 2.048 (max is trial 1) | compiled=5 |
| `codegrammar-flat` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,317,627.0 | 1,264,897.0 | 2,413,513.0 | 446,399.0 | 5 | 6,088 | 0.339 (max is trial 1) | compiled=5 |
| `codegrammar-flat` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,701,830.0 | 1,614,509.0 | 2,773,775.0 | 441,302.4 | 5 | 3,672 | 0.259 (max is trial 1) | compiled=5 |
| `codegrammar-xflag` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 19,320.0 | 16,260.0 | 92,580.0 | 29,454.5 | 5 | 217 | timer-floor (max is trial 1) | compiled=5 |
| `codegrammar-xflag` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `codegrammar-xflag` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `codegrammar-xflag` | `plain` | `rust_1.13.1_default-caps-simdna` | 118,630.0 | 84,531.0 | 683,822.0 | 227,593.9 | 5 | - | 1.919 (max is trial 1) | compiled=5 |
| `codegrammar-xflag` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 247,281.0 | 181,340.0 | 1,185,623.0 | 382,322.7 | 5 | - | 1.546 (max is trial 1) | compiled=5 |
| `codegrammar-xflag` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,313,077.0 | 1,271,797.0 | 2,375,822.0 | 428,378.3 | 5 | 6,088 | 0.326 (max is trial 1) | compiled=5 |
| `codegrammar-xflag` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,684,110.0 | 1,663,789.0 | 2,879,496.0 | 477,323.8 | 5 | 3,672 | 0.283 (max is trial 1) | compiled=5 |
| `currency-lookbehind-fixed` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 16,160.0 | 13,260.0 | 92,280.0 | 30,624.9 | 5 | 186 | timer-floor (max is trial 1) | compiled=5 |
| `currency-lookbehind-fixed` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `currency-lookbehind-fixed` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `currency-lookbehind-fixed` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `currency-lookbehind-fixed` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `date-nested-plus` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 14,040.0 | 11,560.0 | 80,251.0 | 26,596.0 | 5 | 244 | timer-floor (max is trial 1) | compiled=5 |
| `date-nested-plus` | `plain` | `re2_11.0.0_default-caps-simdna` | 19,320.0 | 14,620.0 | 113,590.0 | 37,909.7 | 5 | 12 | timer-floor (max is trial 1) | compiled=5 |
| `date-nested-plus` | `plain` | `re2_11.0.0_longest-caps-simdna` | 18,861.0 | 14,570.0 | 119,600.0 | 40,228.5 | 5 | 12 | timer-floor (max is trial 1) | compiled=5 |
| `date-nested-plus` | `plain` | `rust_1.13.1_default-caps-simdna` | 22,320.0 | 19,260.0 | 250,001.0 | 90,575.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `date-nested-plus` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 26,760.0 | 22,270.0 | 232,571.0 | 82,243.1 | 5 | - | 3.073 (max is trial 1) | compiled=5 |
| `date-nested-plus` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,092,496.0 | 1,062,165.0 | 2,138,501.0 | 418,027.9 | 5 | 5,736 | 0.383 (max is trial 1) | compiled=5 |
| `date-nested-plus` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,163,306.0 | 1,130,056.0 | 2,201,942.0 | 415,022.4 | 5 | 6,024 | 0.357 (max is trial 1) | compiled=5 |
| `doubled-word` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 13,310.0 | 11,050.0 | 79,670.0 | 26,696.2 | 5 | 177 | timer-floor (max is trial 1) | compiled=5 |
| `doubled-word` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `doubled-word` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `doubled-word` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `doubled-word` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `dup-param-detect` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 48,060.0 | 39,100.0 | 199,141.0 | 60,526.2 | 5 | 192 | 1.259 (max is trial 1) | compiled=5 |
| `dup-param-detect` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `dup-param-detect` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `dup-param-detect` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `dup-param-detect` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `email-local-nodup` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 15,140.0 | 12,260.0 | 97,400.0 | 33,049.8 | 5 | 214 | timer-floor (max is trial 1) | compiled=5 |
| `email-local-nodup` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `email-local-nodup` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `email-local-nodup` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `email-local-nodup` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `email-nested-plus` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 22,260.0 | 19,410.0 | 159,721.0 | 54,857.0 | 5 | 204 | timer-floor (max is trial 1) | compiled=5 |
| `email-nested-plus` | `plain` | `re2_11.0.0_default-caps-simdna` | 22,200.0 | 16,450.0 | 120,171.0 | 39,797.9 | 5 | 13 | timer-floor (max is trial 1) | compiled=5 |
| `email-nested-plus` | `plain` | `re2_11.0.0_longest-caps-simdna` | 21,780.0 | 15,990.0 | 129,080.0 | 43,309.4 | 5 | 13 | timer-floor (max is trial 1) | compiled=5 |
| `email-nested-plus` | `plain` | `rust_1.13.1_default-caps-simdna` | 21,510.0 | 16,860.0 | 228,271.0 | 82,546.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `email-nested-plus` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 30,970.0 | 26,990.0 | 274,981.0 | 97,098.0 | 5 | - | 3.135 (max is trial 1) | compiled=5 |
| `email-nested-plus` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 562,724.0 | 533,742.0 | 1,510,198.0 | 379,578.1 | 5 | 5,784 | 0.675 (max is trial 1) | compiled=5 |
| `email-nested-plus` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 850,025.0 | 806,634.0 | 1,865,040.0 | 409,248.7 | 5 | 6,232 | 0.481 (max is trial 1) | compiled=5 |
| `evil-alt-nested` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 14,440.0 | 12,210.0 | 86,920.0 | 29,069.7 | 5 | 212 | timer-floor (max is trial 1) | compiled=5 |
| `evil-alt-nested` | `plain` | `re2_11.0.0_default-caps-simdna` | 14,430.0 | 11,300.0 | 108,280.0 | 37,351.9 | 5 | 9 | timer-floor (max is trial 1) | compiled=5 |
| `evil-alt-nested` | `plain` | `re2_11.0.0_longest-caps-simdna` | 13,930.0 | 10,670.0 | 100,461.0 | 34,470.2 | 5 | 9 | timer-floor (max is trial 1) | compiled=5 |
| `evil-alt-nested` | `plain` | `rust_1.13.1_default-caps-simdna` | 23,351.0 | 17,210.0 | 224,930.0 | 81,243.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `evil-alt-nested` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 23,880.0 | 20,030.0 | 228,321.0 | 81,842.7 | 5 | - | 3.427 (max is trial 1) | compiled=5 |
| `evil-alt-nested` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 595,423.0 | 572,213.0 | 1,555,489.0 | 381,152.2 | 5 | 5,704 | 0.640 (max is trial 1) | compiled=5 |
| `evil-alt-nested` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 749,144.0 | 685,024.0 | 1,720,819.0 | 394,948.5 | 5 | 5,992 | 0.527 (max is trial 1) | compiled=5 |
| `file-ext-order` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 25,360.0 | 20,401.0 | 149,391.0 | 49,970.6 | 5 | 184 | 1.970 (max is trial 1) | compiled=5 |
| `file-ext-order` | `plain` | `re2_11.0.0_default-caps-simdna` | 15,980.0 | 12,600.0 | 109,541.0 | 37,650.6 | 5 | 12 | timer-floor (max is trial 1) | compiled=5 |
| `file-ext-order` | `plain` | `re2_11.0.0_longest-caps-simdna` | 14,041.0 | 11,110.0 | 88,960.0 | 30,220.4 | 5 | 12 | timer-floor (max is trial 1) | compiled=5 |
| `file-ext-order` | `plain` | `rust_1.13.1_default-caps-simdna` | 10,640.0 | 7,380.0 | 228,510.0 | 87,256.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `file-ext-order` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 85,080.0 | 60,310.0 | 481,761.0 | 160,674.5 | 5 | - | 1.889 (max is trial 1) | compiled=5 |
| `file-ext-order` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 507,983.0 | 454,952.0 | 1,385,988.0 | 358,741.6 | 5 | 4,776 | 0.706 (max is trial 1) | compiled=5 |
| `file-ext-order` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 573,523.0 | 542,843.0 | 1,551,288.0 | 391,487.8 | 5 | 2,120 | 0.683 (max is trial 1) | compiled=5 |
| `float-literal-bound` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 18,070.0 | 15,250.0 | 87,301.0 | 27,830.5 | 5 | 246 | timer-floor (max is trial 1) | compiled=5 |
| `float-literal-bound` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `float-literal-bound` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `float-literal-bound` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `float-literal-bound` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `floor-byte` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 7,370.0 | 5,980.0 | 78,090.0 | 28,326.6 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `floor-byte` | `plain` | `re2_11.0.0_default-caps-simdna` | 4,791.0 | 3,890.0 | 82,310.0 | 31,039.9 | 5 | 5 | timer-floor (max is trial 1) | compiled=5 |
| `floor-byte` | `plain` | `re2_11.0.0_longest-caps-simdna` | 4,760.0 | 4,030.0 | 91,811.0 | 34,805.4 | 5 | 5 | timer-floor (max is trial 1) | compiled=5 |
| `floor-byte` | `plain` | `rust_1.13.1_default-caps-simdna` | 4,220.0 | 1,640.0 | 170,640.0 | 67,040.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `floor-byte` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 11,210.0 | 8,330.0 | 203,481.0 | 76,535.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `floor-byte` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 93,711.0 | 88,111.0 | 549,083.0 | 182,283.6 | 5 | 936 | 1.945 (max is trial 1) | compiled=5 |
| `floor-byte` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 321,662.0 | 304,682.0 | 1,172,446.0 | 339,349.0 | 5 | 1,704 | 1.055 (max is trial 1) | compiled=5 |
| `high-byte-run` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 7,820.0 | 6,410.0 | 70,170.0 | 24,949.5 | 5 | 197 | timer-floor (max is trial 1) | compiled=5 |
| `high-byte-run` | `plain` | `re2_11.0.0_default-caps-simdna` | 13,120.0 | 10,650.0 | 110,630.0 | 39,067.2 | 5 | 10 | timer-floor (max is trial 1) | compiled=5 |
| `high-byte-run` | `plain` | `re2_11.0.0_longest-caps-simdna` | 12,360.0 | 9,840.0 | 100,701.0 | 35,432.9 | 5 | 10 | timer-floor (max is trial 1) | compiled=5 |
| `high-byte-run` | `plain` | `rust_1.13.1_default-caps-simdna` | 96,760.0 | 88,580.0 | 1,031,093.0 | 367,727.8 | 5 | - | 3.800 (max is trial 1) | compiled=5 |
| `high-byte-run` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 51,470.0 | 49,150.0 | 487,061.0 | 170,450.8 | 5 | - | 3.312 (max is trial 1) | compiled=5 |
| `high-byte-run` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 595,863.0 | 526,692.0 | 1,463,748.0 | 361,108.3 | 5 | 5,784 | 0.606 (max is trial 1) | compiled=5 |
| `high-byte-run` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 502,832.0 | 485,493.0 | 1,387,567.0 | 352,381.9 | 5 | 1,832 | 0.701 (max is trial 1) | compiled=5 |
| `ipv4-near-miss` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 62,290.0 | 54,260.0 | 228,532.0 | 66,990.6 | 5 | 693 | 1.075 (max is trial 1) | compiled=5 |
| `ipv4-near-miss` | `plain` | `re2_11.0.0_default-caps-simdna` | 66,190.0 | 59,041.0 | 191,061.0 | 50,231.8 | 5 | 49 | 0.759 (max is trial 1) | compiled=5 |
| `ipv4-near-miss` | `plain` | `re2_11.0.0_longest-caps-simdna` | 67,901.0 | 59,880.0 | 218,232.0 | 60,658.9 | 5 | 49 | 0.893 (max is trial 1) | compiled=5 |
| `ipv4-near-miss` | `plain` | `rust_1.13.1_default-caps-simdna` | 590,142.0 | 471,181.0 | 1,068,383.0 | 206,287.8 | 5 | - | 0.350 (max is trial 1) | compiled=5 |
| `ipv4-near-miss` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 582,902.0 | 485,171.0 | 1,080,323.0 | 209,184.9 | 5 | - | 0.359 (max is trial 1) | compiled=5 |
| `ipv4-near-miss` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 2,032,681.0 | 2,008,021.0 | 3,119,357.0 | 433,981.6 | 5 | 3,464 | 0.214 (max is trial 1) | compiled=5 |
| `ipv4-near-miss` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 755,564.0 | 736,334.0 | 1,214,507.0 | 185,579.3 | 5 | 2,824 | 0.246 (max is trial 1) | compiled=5 |
| `keyword-prefix-order` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 15,020.0 | 12,310.0 | 151,091.0 | 54,584.1 | 5 | 186 | timer-floor (max is trial 1) | compiled=5 |
| `keyword-prefix-order` | `plain` | `re2_11.0.0_default-caps-simdna` | 21,530.0 | 13,391.0 | 108,261.0 | 37,494.5 | 5 | 15 | timer-floor (max is trial 1) | compiled=5 |
| `keyword-prefix-order` | `plain` | `re2_11.0.0_longest-caps-simdna` | 14,800.0 | 12,190.0 | 101,851.0 | 34,893.8 | 5 | 15 | timer-floor (max is trial 1) | compiled=5 |
| `keyword-prefix-order` | `plain` | `rust_1.13.1_default-caps-simdna` | 19,560.0 | 13,590.0 | 420,851.0 | 160,454.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `keyword-prefix-order` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 56,750.0 | 51,700.0 | 529,061.0 | 186,859.8 | 5 | - | 3.293 (max is trial 1) | compiled=5 |
| `keyword-prefix-order` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 543,143.0 | 508,623.0 | 1,434,127.0 | 362,359.2 | 5 | 4,840 | 0.667 (max is trial 1) | compiled=5 |
| `keyword-prefix-order` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 633,843.0 | 604,713.0 | 1,498,038.0 | 347,004.0 | 5 | 2,504 | 0.547 (max is trial 1) | compiled=5 |
| `logparse-atomic` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 30,550.0 | 25,050.0 | 109,910.0 | 32,655.9 | 5 | 376 | 1.069 (max is trial 1) | compiled=5 |
| `logparse-atomic` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `logparse-atomic` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `logparse-atomic` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `logparse-atomic` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `logparse-atomic-removed` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 29,761.0 | 23,300.0 | 102,310.0 | 29,894.1 | 5 | 376 | 1.004 (max is trial 1) | compiled=5 |
| `logparse-atomic-removed` | `plain` | `re2_11.0.0_default-caps-simdna` | 33,860.0 | 29,601.0 | 111,711.0 | 31,345.8 | 5 | 80 | 0.926 (max is trial 1) | compiled=5 |
| `logparse-atomic-removed` | `plain` | `re2_11.0.0_longest-caps-simdna` | 66,010.0 | 58,090.0 | 201,821.0 | 54,787.5 | 5 | 80 | 0.830 (max is trial 1) | compiled=5 |
| `logparse-atomic-removed` | `plain` | `rust_1.13.1_default-caps-simdna` | 147,300.0 | 129,841.0 | 595,892.0 | 178,096.7 | 5 | - | 1.209 (max is trial 1) | compiled=5 |
| `logparse-atomic-removed` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 347,762.0 | 324,651.0 | 1,352,284.0 | 397,411.1 | 5 | - | 1.143 (max is trial 1) | compiled=5 |
| `logparse-atomic-removed` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 3,952,881.0 | 3,737,390.0 | 10,969,299.0 | 3,004,810.0 | 5 | 10,168 | 0.760 (max is trial 1) | compiled=5 |
| `logparse-atomic-removed` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 3,439,378.0 | 3,421,809.0 | 4,140,323.0 | 282,624.1 | 5 | 9,496 | 0.082 (max is trial 1) | compiled=5 |
| `mojibake-curly-quote` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 12,301.0 | 9,940.0 | 70,310.0 | 23,341.5 | 5 | 197 | timer-floor (max is trial 1) | compiled=5 |
| `mojibake-curly-quote` | `plain` | `re2_11.0.0_default-caps-simdna` | 10,510.0 | 8,420.0 | 109,211.0 | 39,434.7 | 5 | 7 | timer-floor (max is trial 1) | compiled=5 |
| `mojibake-curly-quote` | `plain` | `re2_11.0.0_longest-caps-simdna` | 10,620.0 | 8,510.0 | 100,841.0 | 36,192.8 | 5 | 7 | timer-floor (max is trial 1) | compiled=5 |
| `mojibake-curly-quote` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `mojibake-curly-quote` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `mojibake-curly-quote` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 723,894.0 | 679,633.0 | 1,753,209.0 | 414,940.0 | 5 | 5,992 | 0.573 (max is trial 1) | compiled=5 |
| `mojibake-curly-quote` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,071,046.0 | 1,057,546.0 | 2,194,412.0 | 447,008.4 | 5 | 3,352 | 0.417 (max is trial 1) | compiled=5 |
| `negation-scope-lookbehind-var` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 30,080.0 | 26,050.0 | 109,620.0 | 32,029.8 | 5 | 265 | 1.065 (max is trial 1) | compiled=5 |
| `negation-scope-lookbehind-var` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `negation-scope-lookbehind-var` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `negation-scope-lookbehind-var` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `negation-scope-lookbehind-var` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `nested-comment-rec` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 38,170.0 | 33,201.0 | 123,141.0 | 34,252.6 | 5 | 247 | 0.897 (max is trial 1) | compiled=5 |
| `nested-comment-rec` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `nested-comment-rec` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `nested-comment-rec` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `nested-comment-rec` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `numeric-id-nested-plus` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 23,660.0 | 18,680.0 | 158,520.0 | 54,254.1 | 5 | 171 | timer-floor (max is trial 1) | compiled=5 |
| `numeric-id-nested-plus` | `plain` | `re2_11.0.0_default-caps-simdna` | 11,010.0 | 8,610.0 | 104,761.0 | 37,612.8 | 5 | 7 | timer-floor (max is trial 1) | compiled=5 |
| `numeric-id-nested-plus` | `plain` | `re2_11.0.0_longest-caps-simdna` | 10,890.0 | 8,190.0 | 99,711.0 | 35,703.5 | 5 | 7 | timer-floor (max is trial 1) | compiled=5 |
| `numeric-id-nested-plus` | `plain` | `rust_1.13.1_default-caps-simdna` | 82,431.0 | 67,010.0 | 526,061.0 | 176,216.0 | 5 | - | 2.138 (max is trial 1) | compiled=5 |
| `numeric-id-nested-plus` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 85,610.0 | 75,000.0 | 497,271.0 | 163,153.0 | 5 | - | 1.906 (max is trial 1) | compiled=5 |
| `numeric-id-nested-plus` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 819,034.0 | 798,775.0 | 1,780,400.0 | 384,195.0 | 5 | 5,704 | 0.469 (max is trial 1) | compiled=5 |
| `numeric-id-nested-plus` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 886,445.0 | 873,925.0 | 1,879,420.0 | 396,102.2 | 5 | 5,992 | 0.447 (max is trial 1) | compiled=5 |
| `phone-list-nested-plus` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 35,220.0 | 25,750.0 | 170,631.0 | 54,919.7 | 5 | 173 | 1.559 (max is trial 1) | compiled=5 |
| `phone-list-nested-plus` | `plain` | `re2_11.0.0_default-caps-simdna` | 18,100.0 | 13,660.0 | 111,501.0 | 37,381.7 | 5 | 11 | timer-floor (max is trial 1) | compiled=5 |
| `phone-list-nested-plus` | `plain` | `re2_11.0.0_longest-caps-simdna` | 17,700.0 | 13,260.0 | 106,140.0 | 35,403.9 | 5 | 11 | timer-floor (max is trial 1) | compiled=5 |
| `phone-list-nested-plus` | `plain` | `rust_1.13.1_default-caps-simdna` | 109,790.0 | 90,700.0 | 631,042.0 | 207,471.2 | 5 | - | 1.890 (max is trial 1) | compiled=5 |
| `phone-list-nested-plus` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 92,170.0 | 81,030.0 | 529,622.0 | 172,586.6 | 5 | - | 1.872 (max is trial 1) | compiled=5 |
| `phone-list-nested-plus` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 968,455.0 | 932,145.0 | 1,980,060.0 | 406,169.2 | 5 | 5,736 | 0.419 (max is trial 1) | compiled=5 |
| `phone-list-nested-plus` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,029,536.0 | 988,935.0 | 2,046,341.0 | 409,200.8 | 5 | 5,992 | 0.397 (max is trial 1) | compiled=5 |
| `phone-palindrome-6` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 13,101.0 | 11,200.0 | 68,610.0 | 22,297.2 | 5 | 195 | timer-floor (max is trial 1) | compiled=5 |
| `phone-palindrome-6` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `phone-palindrome-6` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `phone-palindrome-6` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `phone-palindrome-6` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `pwd-strength-chain` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 28,250.0 | 18,880.0 | 112,710.0 | 35,564.9 | 5 | 299 | timer-floor (max is trial 1) | compiled=5 |
| `pwd-strength-chain` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `pwd-strength-chain` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `pwd-strength-chain` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `pwd-strength-chain` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `quoted-delim-match` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 21,440.0 | 17,981.0 | 100,751.0 | 31,909.8 | 5 | 227 | timer-floor (max is trial 1) | compiled=5 |
| `quoted-delim-match` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `quoted-delim-match` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `quoted-delim-match` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `quoted-delim-match` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `router-prefix-order` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 12,700.0 | 10,390.0 | 72,851.0 | 24,210.8 | 5 | 184 | timer-floor (max is trial 1) | compiled=5 |
| `router-prefix-order` | `plain` | `re2_11.0.0_default-caps-simdna` | 14,960.0 | 12,321.0 | 97,500.0 | 33,138.8 | 5 | 11 | timer-floor (max is trial 1) | compiled=5 |
| `router-prefix-order` | `plain` | `re2_11.0.0_longest-caps-simdna` | 5,990.0 | 4,630.0 | 48,230.0 | 16,963.0 | 5 | 11 | timer-floor (max is trial 1) | compiled=5 |
| `router-prefix-order` | `plain` | `rust_1.13.1_default-caps-simdna` | 8,050.0 | 5,700.0 | 195,140.0 | 74,783.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `router-prefix-order` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 23,290.0 | 19,790.0 | 241,111.0 | 86,204.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `router-prefix-order` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 519,923.0 | 455,633.0 | 1,380,108.0 | 353,995.5 | 5 | 4,776 | 0.681 (max is trial 1) | compiled=5 |
| `router-prefix-order` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 555,163.0 | 534,283.0 | 1,443,578.0 | 354,765.9 | 5 | 2,120 | 0.639 (max is trial 1) | compiled=5 |
| `tag-depth3-bound` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 33,820.0 | 29,950.0 | 116,740.0 | 33,216.8 | 5 | 254 | 0.982 (max is trial 1) | compiled=5 |
| `tag-depth3-bound` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `tag-depth3-bound` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `tag-depth3-bound` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `tag-depth3-bound` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `tag-pair-match` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 21,150.0 | 17,740.0 | 81,281.0 | 24,265.4 | 5 | 261 | timer-floor (max is trial 1) | compiled=5 |
| `tag-pair-match` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `tag-pair-match` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `tag-pair-match` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `tag-pair-match` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `trim-nested-star` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 24,581.0 | 19,550.0 | 160,690.0 | 54,754.7 | 5 | 172 | timer-floor (max is trial 1) | compiled=5 |
| `trim-nested-star` | `plain` | `re2_11.0.0_default-caps-simdna` | 12,600.0 | 9,450.0 | 100,780.0 | 35,504.0 | 5 | 8 | timer-floor (max is trial 1) | compiled=5 |
| `trim-nested-star` | `plain` | `re2_11.0.0_longest-caps-simdna` | 14,120.0 | 10,450.0 | 101,491.0 | 35,291.2 | 5 | 8 | timer-floor (max is trial 1) | compiled=5 |
| `trim-nested-star` | `plain` | `rust_1.13.1_default-caps-simdna` | 51,030.0 | 42,090.0 | 468,492.0 | 165,037.2 | 5 | - | 3.234 (max is trial 1) | compiled=5 |
| `trim-nested-star` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 209,811.0 | 44,910.0 | 480,662.0 | 158,856.6 | 5 | - | 0.757 (max is trial 1) | compiled=5 |
| `trim-nested-star` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 738,664.0 | 711,424.0 | 1,702,769.0 | 388,171.2 | 5 | 5,736 | 0.526 (max is trial 1) | compiled=5 |
| `trim-nested-star` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,710,339.0 | 1,667,779.0 | 2,845,635.0 | 454,563.2 | 5 | 2,600 | 0.266 (max is trial 1) | compiled=5 |
| `utf8-lead-no-cont` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 9,270.0 | 7,690.0 | 69,811.0 | 24,221.2 | 5 | 231 | timer-floor (max is trial 1) | compiled=5 |
| `utf8-lead-no-cont` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `utf8-lead-no-cont` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `utf8-lead-no-cont` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `utf8-lead-no-cont` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `uuid-near-miss` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 33,400.0 | 30,250.0 | 175,211.0 | 56,640.6 | 5 | 425 | 1.696 (max is trial 1) | compiled=5 |
| `uuid-near-miss` | `plain` | `re2_11.0.0_default-caps-simdna` | 63,961.0 | 59,480.0 | 197,421.0 | 53,228.4 | 5 | 69 | 0.832 (max is trial 1) | compiled=5 |
| `uuid-near-miss` | `plain` | `re2_11.0.0_longest-caps-simdna` | 64,380.0 | 58,231.0 | 199,471.0 | 54,127.0 | 5 | 69 | 0.841 (max is trial 1) | compiled=5 |
| `uuid-near-miss` | `plain` | `rust_1.13.1_default-caps-simdna` | 125,351.0 | 102,370.0 | 576,502.0 | 184,029.6 | 5 | - | 1.468 (max is trial 1) | compiled=5 |
| `uuid-near-miss` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 49,400.0 | 43,570.0 | 278,650.0 | 91,957.0 | 5 | - | 1.861 (max is trial 1) | compiled=5 |
| `uuid-near-miss` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,274,837.0 | 1,242,517.0 | 2,222,272.0 | 383,276.4 | 5 | 2,216 | 0.301 (max is trial 1) | compiled=5 |
| `uuid-near-miss` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 460,543.0 | 447,722.0 | 872,405.0 | 164,967.5 | 5 | 2,088 | 0.358 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-array-begin` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 7,690.0 | 6,170.0 | 66,851.0 | 23,726.1 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-array-begin` | `plain` | `re2_11.0.0_default-caps-simdna` | 2,010.0 | 1,600.0 | 43,380.0 | 16,580.5 | 5 | 5 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-array-begin` | `plain` | `re2_11.0.0_longest-caps-simdna` | 5,370.0 | 4,440.0 | 89,071.0 | 33,535.1 | 5 | 5 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-array-begin` | `plain` | `rust_1.13.1_default-caps-simdna` | 10,280.0 | 4,310.0 | 360,371.0 | 141,188.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 11,370.0 | 8,600.0 | 205,330.0 | 77,222.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-array-begin` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 94,250.0 | 87,200.0 | 554,853.0 | 184,471.6 | 5 | 936 | 1.957 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 332,422.0 | 302,122.0 | 1,154,656.0 | 333,616.9 | 5 | 1,704 | 1.004 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-constant` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 16,040.0 | 12,870.0 | 77,390.0 | 24,615.1 | 5 | 199 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-constant` | `plain` | `re2_11.0.0_default-caps-simdna` | 23,100.0 | 18,780.0 | 116,671.0 | 37,698.7 | 5 | 19 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-constant` | `plain` | `re2_11.0.0_longest-caps-simdna` | 9,170.0 | 7,370.0 | 55,920.0 | 18,799.3 | 5 | 19 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-constant` | `plain` | `rust_1.13.1_default-caps-simdna` | 171,580.0 | 146,901.0 | 633,192.0 | 186,365.9 | 5 | - | 1.086 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-constant` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 41,760.0 | 34,130.0 | 283,641.0 | 95,965.9 | 5 | - | 2.298 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-constant` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 2,901,266.0 | 2,886,945.0 | 4,186,413.0 | 512,415.6 | 5 | 7,928 | 0.177 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-constant` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 771,784.0 | 755,235.0 | 1,708,069.0 | 372,333.9 | 5 | 2,504 | 0.482 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-number-extended` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 27,480.0 | 22,340.0 | 107,671.0 | 32,673.3 | 5 | 270 | 1.189 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-number-extended` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-codegrammar-json-number-extended` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-codegrammar-json-number-extended` | `plain` | `rust_1.13.1_default-caps-simdna` | 735,312.0 | 661,912.0 | 1,814,755.0 | 432,511.5 | 5 | - | 0.588 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-number-extended` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `wild-codegrammar-json-number-extended` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `wild-codegrammar-json-number-extended` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `wild-codegrammar-json-object-begin` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 7,980.0 | 6,450.0 | 66,771.0 | 23,617.7 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-object-begin` | `plain` | `re2_11.0.0_default-caps-simdna` | 4,920.0 | 4,120.0 | 84,061.0 | 31,638.2 | 5 | 5 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-object-begin` | `plain` | `re2_11.0.0_longest-caps-simdna` | 5,140.0 | 4,180.0 | 82,541.0 | 30,991.5 | 5 | 5 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-object-begin` | `plain` | `rust_1.13.1_default-caps-simdna` | 4,020.0 | 1,680.0 | 177,230.0 | 69,680.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 11,480.0 | 8,520.0 | 205,981.0 | 77,400.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-object-begin` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 92,541.0 | 86,381.0 | 564,413.0 | 188,703.4 | 5 | 936 | 2.039 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 313,222.0 | 300,492.0 | 1,164,837.0 | 340,346.3 | 5 | 1,704 | 1.087 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 17,740.0 | 13,860.0 | 97,390.0 | 32,115.2 | 5 | 243 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `rust_1.13.1_default-caps-simdna` | 35,930.0 | 32,180.0 | 258,970.0 | 88,445.5 | 5 | - | 2.462 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-stringcontent-escape` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `wild-codegrammar-json-stringcontent-escape` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `wild-datetime-datefinder-alternation` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 1,970,240.0 | 1,872,820.0 | 2,127,901.0 | 91,842.6 | 5 | 16,813 | 0.047 (max is trial 1) | compiled=5 |
| `wild-datetime-datefinder-alternation` | `plain` | `re2_11.0.0_default-caps-simdna` | 2,922,904.0 | 1,487,307.0 | 4,501,191.0 | 1,151,956.0 | 5 | 3,248 | 0.394 (max is trial 1) | compiled=5 |
| `wild-datetime-datefinder-alternation` | `plain` | `re2_11.0.0_longest-caps-simdna` | 2,872,367.0 | 1,377,028.0 | 4,437,856.0 | 1,175,916.5 | 5 | 3,248 | 0.409 (max is trial 1) | compiled=5 |
| `wild-datetime-datefinder-alternation` | `plain` | `rust_1.13.1_default-caps-simdna` | 10,397,271.0 | 9,794,029.0 | 16,690,550.0 | 2,548,803.5 | 5 | - | 0.245 (max is trial 1) | compiled=5 |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 10,383,311.0 | 9,743,529.0 | 23,726,090.0 | 5,357,634.1 | 5 | - | 0.516 (max is trial 1) | compiled=5 |
| `wild-datetime-datefinder-alternation` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,776,991,153.0 | 1,772,793,750.0 | 1,812,998,038.0 | 14,890,885.5 | 5 | 158,072 | 0.008 (max is trial 1) | compiled=5 |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,726,853,571.0 | 1,724,867,871.0 | 1,763,271,999.0 | 14,636,534.1 | 5 | 141,928 | 0.008 (max is trial 1) | compiled=5 |
| `wild-datetime-moment-iso8601` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 65,950.0 | 59,521.0 | 271,041.0 | 82,129.1 | 5 | 421 | 1.245 (max is trial 1) | compiled=5 |
| `wild-datetime-moment-iso8601` | `plain` | `re2_11.0.0_default-caps-simdna` | 119,571.0 | 106,681.0 | 272,261.0 | 62,382.1 | 5 | 75 | 0.522 (max is trial 1) | compiled=5 |
| `wild-datetime-moment-iso8601` | `plain` | `re2_11.0.0_longest-caps-simdna` | 146,961.0 | 115,861.0 | 283,122.0 | 61,555.3 | 5 | 75 | 0.419 (max is trial 1) | compiled=5 |
| `wild-datetime-moment-iso8601` | `plain` | `rust_1.13.1_default-caps-simdna` | 2,705,828.0 | 2,651,908.0 | 4,469,613.0 | 691,916.2 | 5 | - | 0.256 (max is trial 1) | compiled=5 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 2,532,438.0 | 2,490,967.0 | 4,210,452.0 | 657,612.0 | 5 | - | 0.260 (max is trial 1) | compiled=5 |
| `wild-datetime-moment-iso8601` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 3,001,146.0 | 2,993,956.0 | 3,645,500.0 | 258,346.2 | 5 | 4,232 | 0.086 (max is trial 1) | compiled=5 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 3,020,816.0 | 2,970,616.0 | 3,559,579.0 | 223,712.2 | 5 | 4,488 | 0.074 (max is trial 1) | compiled=5 |
| `wild-logparse-base10num-grok` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 24,250.0 | 17,620.0 | 108,151.0 | 34,609.8 | 5 | 375 | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-base10num-grok` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-base10num-grok` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-base10num-grok` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-base10num-grok` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-base10num-noatomic` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 19,100.0 | 15,770.0 | 103,661.0 | 34,008.5 | 5 | 375 | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-base10num-noatomic` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-base10num-noatomic` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-base10num-noatomic` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-base10num-noatomic` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-quotedstring-grok` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 34,450.0 | 26,670.0 | 122,381.0 | 36,615.9 | 5 | 371 | 1.063 (max is trial 1) | compiled=5 |
| `wild-logparse-quotedstring-grok` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-quotedstring-grok` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-quotedstring-grok` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-quotedstring-grok` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 33,800.0 | 25,420.0 | 115,071.0 | 33,329.1 | 5 | 371 | 0.986 (max is trial 1) | compiled=5 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-syslogbase-expanded` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 577,973.0 | 558,943.0 | 749,784.0 | 70,790.1 | 5 | 10,481 | 0.122 (max is trial 1) | compiled=5 |
| `wild-logparse-syslogbase-expanded` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-syslogbase-expanded` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-syslogbase-expanded` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-syslogbase-expanded` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-winpath-grok` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 16,360.0 | 13,470.0 | 100,580.0 | 33,886.7 | 5 | 248 | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-winpath-grok` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-winpath-grok` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-winpath-grok` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-winpath-grok` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-secrets-aws-access-key-id` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 22,540.0 | 19,240.0 | 106,451.0 | 33,774.7 | 5 | 340 | timer-floor (max is trial 1) | compiled=5 |
| `wild-secrets-aws-access-key-id` | `plain` | `re2_11.0.0_default-caps-simdna` | 31,150.0 | 25,090.0 | 90,951.0 | 24,956.6 | 5 | 68 | 0.801 (max is trial 1) | compiled=5 |
| `wild-secrets-aws-access-key-id` | `plain` | `re2_11.0.0_longest-caps-simdna` | 31,060.0 | 24,950.0 | 89,751.0 | 24,387.9 | 5 | 68 | 0.785 (max is trial 1) | compiled=5 |
| `wild-secrets-aws-access-key-id` | `plain` | `rust_1.13.1_default-caps-simdna` | 140,081.0 | 129,190.0 | 605,612.0 | 184,294.2 | 5 | - | 1.316 (max is trial 1) | compiled=5 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 51,770.0 | 46,750.0 | 269,080.0 | 86,800.4 | 5 | - | 1.677 (max is trial 1) | compiled=5 |
| `wild-secrets-aws-access-key-id` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 4,533,994.0 | 2,368,823.0 | 5,709,950.0 | 1,086,766.1 | 5 | 11,752 | 0.240 (max is trial 1) | compiled=5 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,946,271.0 | 1,731,039.0 | 3,014,116.0 | 460,918.1 | 5 | 3,464 | 0.237 (max is trial 1) | compiled=5 |
| `wild-secrets-github-pat` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 16,140.0 | 13,180.0 | 92,991.0 | 30,948.5 | 5 | 229 | timer-floor (max is trial 1) | compiled=5 |
| `wild-secrets-github-pat` | `plain` | `re2_11.0.0_default-caps-simdna` | 78,291.0 | 71,950.0 | 157,611.0 | 32,265.3 | 5 | 265 | 0.412 (max is trial 1) | compiled=5 |
| `wild-secrets-github-pat` | `plain` | `re2_11.0.0_longest-caps-simdna` | 202,871.0 | 183,211.0 | 355,603.0 | 63,505.4 | 5 | 265 | 0.313 (max is trial 1) | compiled=5 |
| `wild-secrets-github-pat` | `plain` | `rust_1.13.1_default-caps-simdna` | 229,940.0 | 193,980.0 | 687,982.0 | 186,693.9 | 5 | - | 0.812 (max is trial 1) | compiled=5 |
| `wild-secrets-github-pat` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 136,181.0 | 107,861.0 | 372,281.0 | 100,331.4 | 5 | - | 0.737 (max is trial 1) | compiled=5 |
| `wild-secrets-github-pat` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 4,077,952.0 | 1,899,340.0 | 5,524,290.0 | 1,309,038.4 | 5 | 7,224 | 0.321 (max is trial 1) | compiled=5 |
| `wild-secrets-github-pat` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 3,975,492.0 | 2,241,302.0 | 5,519,519.0 | 1,060,860.9 | 5 | 2,352 | 0.267 (max is trial 1) | compiled=5 |
| `wild-secrets-slack-webhook-url` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 29,590.0 | 27,270.0 | 109,070.0 | 31,746.1 | 5 | 353 | 1.073 (max is trial 1) | compiled=5 |
| `wild-secrets-slack-webhook-url` | `plain` | `re2_11.0.0_default-caps-simdna` | 99,410.0 | 86,101.0 | 172,411.0 | 32,161.8 | 5 | 181 | 0.324 (max is trial 1) | compiled=5 |
| `wild-secrets-slack-webhook-url` | `plain` | `re2_11.0.0_longest-caps-simdna` | 251,801.0 | 217,511.0 | 401,152.0 | 67,902.7 | 5 | 181 | 0.270 (max is trial 1) | compiled=5 |
| `wild-secrets-slack-webhook-url` | `plain` | `rust_1.13.1_default-caps-simdna` | 660,632.0 | 569,572.0 | 1,199,373.0 | 232,799.0 | 5 | - | 0.352 (max is trial 1) | compiled=5 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 409,412.0 | 334,581.0 | 868,422.0 | 196,301.2 | 5 | - | 0.479 (max is trial 1) | compiled=5 |
| `wild-secrets-slack-webhook-url` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,556,518.0 | 1,533,998.0 | 2,107,771.0 | 224,138.4 | 5 | 3,504 | 0.144 (max is trial 1) | compiled=5 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 4,101,583.0 | 2,097,941.0 | 5,316,839.0 | 1,038,276.0 | 5 | 5,048 | 0.253 (max is trial 1) | compiled=5 |
| `wild-secrets-username-password-pair` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 48,450.0 | 43,400.0 | 127,270.0 | 31,719.4 | 5 | 778 | 0.655 (max is trial 1) | compiled=5 |
| `wild-secrets-username-password-pair` | `plain` | `re2_11.0.0_default-caps-simdna` | 390,452.0 | 351,712.0 | 637,673.0 | 105,476.7 | 5 | 412 | 0.270 (max is trial 1) | compiled=5 |
| `wild-secrets-username-password-pair` | `plain` | `re2_11.0.0_longest-caps-simdna` | 373,013.0 | 352,742.0 | 605,533.0 | 94,393.8 | 5 | 412 | 0.253 (max is trial 1) | compiled=5 |
| `wild-secrets-username-password-pair` | `plain` | `rust_1.13.1_default-caps-simdna` | 507,941.0 | 456,622.0 | 1,194,223.0 | 277,353.5 | 5 | - | 0.546 (max is trial 1) | compiled=5 |
| `wild-secrets-username-password-pair` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 445,032.0 | 380,911.0 | 1,057,693.0 | 251,045.3 | 5 | - | 0.564 (max is trial 1) | compiled=5 |
| `wild-secrets-username-password-pair` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 26,746,265.0 | 26,524,793.0 | 40,582,489.0 | 5,505,525.8 | 5 | 129,576 | 0.206 (max is trial 1) | compiled=5 |
| `wild-secrets-username-password-pair` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 4,956,987.0 | 4,914,106.0 | 13,947,335.0 | 3,502,982.2 | 5 | 10,072 | 0.707 (max is trial 1) | compiled=5 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 12,550.0 | 10,160.0 | 74,621.0 | 24,956.4 | 5 | 180 | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `re2_11.0.0_default-caps-simdna` | 14,750.0 | 12,860.0 | 104,430.0 | 35,853.7 | 5 | 11 | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `re2_11.0.0_longest-caps-simdna` | 5,890.0 | 4,750.0 | 48,601.0 | 17,143.8 | 5 | 11 | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `rust_1.13.1_default-caps-simdna` | 15,120.0 | 12,080.0 | 433,781.0 | 166,549.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 57,220.0 | 51,651.0 | 475,272.0 | 165,363.4 | 5 | - | 2.890 (max is trial 1) | compiled=5 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 481,963.0 | 444,203.0 | 1,353,538.0 | 354,485.3 | 5 | 4,776 | 0.736 (max is trial 1) | compiled=5 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 535,623.0 | 512,362.0 | 1,453,707.0 | 368,342.7 | 5 | 2,120 | 0.688 (max is trial 1) | compiled=5 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 11,990.0 | 9,610.0 | 75,051.0 | 25,373.7 | 5 | 166 | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `re2_11.0.0_default-caps-simdna` | 8,370.0 | 6,650.0 | 93,550.0 | 34,134.1 | 5 | 7 | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `re2_11.0.0_longest-caps-simdna` | 4,140.0 | 3,280.0 | 52,770.0 | 19,508.7 | 5 | 7 | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `rust_1.13.1_default-caps-simdna` | 31,370.0 | 24,860.0 | 463,061.0 | 171,446.1 | 5 | - | 5.465 (max is trial 1) | compiled=5 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 40,060.0 | 27,390.0 | 467,671.0 | 172,508.3 | 5 | - | 4.306 (max is trial 1) | compiled=5 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 577,493.0 | 549,772.0 | 1,524,608.0 | 382,707.2 | 5 | 5,592 | 0.663 (max is trial 1) | compiled=5 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 356,872.0 | 326,452.0 | 1,172,966.0 | 331,263.9 | 5 | 1,832 | 0.928 (max is trial 1) | compiled=5 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 12,080.0 | 10,140.0 | 76,170.0 | 25,698.5 | 5 | 174 | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `re2_11.0.0_default-caps-simdna` | 13,950.0 | 10,661.0 | 110,390.0 | 38,796.7 | 5 | 13 | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `re2_11.0.0_longest-caps-simdna` | 14,281.0 | 10,670.0 | 121,610.0 | 43,189.5 | 5 | 13 | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `rust_1.13.1_default-caps-simdna` | 83,140.0 | 71,561.0 | 531,901.0 | 177,386.3 | 5 | - | 2.134 (max is trial 1) | compiled=5 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 102,451.0 | 83,820.0 | 635,402.0 | 211,650.2 | 5 | - | 2.066 (max is trial 1) | compiled=5 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 581,604.0 | 529,112.0 | 1,572,329.0 | 402,858.0 | 5 | 3,944 | 0.693 (max is trial 1) | compiled=5 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,116,336.0 | 1,077,986.0 | 2,153,162.0 | 415,922.6 | 5 | 6,056 | 0.373 (max is trial 1) | compiled=5 |
| `wild-validator-email-owasp` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 19,400.0 | 16,270.0 | 103,871.0 | 33,935.7 | 5 | 320 | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-email-owasp` | `plain` | `re2_11.0.0_default-caps-simdna` | 48,881.0 | 39,400.0 | 163,041.0 | 46,623.4 | 5 | 29 | 0.954 (max is trial 1) | compiled=5 |
| `wild-validator-email-owasp` | `plain` | `re2_11.0.0_longest-caps-simdna` | 18,930.0 | 15,590.0 | 80,781.0 | 24,869.2 | 5 | 29 | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-email-owasp` | `plain` | `rust_1.13.1_default-caps-simdna` | 36,150.0 | 31,730.0 | 256,800.0 | 87,985.3 | 5 | - | 2.434 (max is trial 1) | compiled=5 |
| `wild-validator-email-owasp` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 97,640.0 | 91,840.0 | 576,122.0 | 190,344.3 | 5 | - | 1.949 (max is trial 1) | compiled=5 |
| `wild-validator-email-owasp` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,132,926.0 | 1,100,746.0 | 2,199,912.0 | 426,384.2 | 5 | 6,104 | 0.376 (max is trial 1) | compiled=5 |
| `wild-validator-email-owasp` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 553,763.0 | 538,793.0 | 1,075,666.0 | 208,743.1 | 5 | 6,488 | 0.377 (max is trial 1) | compiled=5 |
| `wild-validator-ipv4-owasp` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 86,791.0 | 79,180.0 | 262,821.0 | 70,490.7 | 5 | 1,047 | 0.812 (max is trial 1) | compiled=5 |
| `wild-validator-ipv4-owasp` | `plain` | `re2_11.0.0_default-caps-simdna` | 95,910.0 | 73,360.0 | 217,581.0 | 53,531.5 | 5 | 53 | 0.558 (max is trial 1) | compiled=5 |
| `wild-validator-ipv4-owasp` | `plain` | `re2_11.0.0_longest-caps-simdna` | 95,171.0 | 74,870.0 | 212,131.0 | 50,733.7 | 5 | 53 | 0.533 (max is trial 1) | compiled=5 |
| `wild-validator-ipv4-owasp` | `plain` | `rust_1.13.1_default-caps-simdna` | 97,720.0 | 90,031.0 | 361,811.0 | 104,632.8 | 5 | - | 1.071 (max is trial 1) | compiled=5 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 85,801.0 | 77,080.0 | 308,441.0 | 90,268.5 | 5 | - | 1.052 (max is trial 1) | compiled=5 |
| `wild-validator-ipv4-owasp` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,941,141.0 | 1,890,280.0 | 2,991,426.0 | 419,073.6 | 5 | 2,984 | 0.216 (max is trial 1) | compiled=5 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 722,034.0 | 690,133.0 | 1,169,376.0 | 184,120.4 | 5 | 2,824 | 0.255 (max is trial 1) | compiled=5 |
| `wild-validator-us-zip-owasp` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 9,830.0 | 7,960.0 | 68,160.0 | 23,427.2 | 5 | 180 | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-us-zip-owasp` | `plain` | `re2_11.0.0_default-caps-simdna` | 20,940.0 | 17,870.0 | 119,841.0 | 39,402.4 | 5 | 15 | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-us-zip-owasp` | `plain` | `re2_11.0.0_longest-caps-simdna` | 30,610.0 | 17,800.0 | 121,301.0 | 38,342.3 | 5 | 15 | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-us-zip-owasp` | `plain` | `rust_1.13.1_default-caps-simdna` | 485,631.0 | 416,722.0 | 943,203.0 | 193,987.2 | 5 | - | 0.399 (max is trial 1) | compiled=5 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 494,041.0 | 320,731.0 | 952,853.0 | 229,229.7 | 5 | - | 0.464 (max is trial 1) | compiled=5 |
| `wild-validator-us-zip-owasp` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 689,674.0 | 650,993.0 | 1,609,699.0 | 367,167.5 | 5 | 2,312 | 0.532 (max is trial 1) | compiled=5 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 230,191.0 | 209,781.0 | 616,253.0 | 156,871.6 | 5 | 2,088 | 0.681 (max is trial 1) | compiled=5 |
| `wild-validator-uuid-grok` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 14,880.0 | 12,490.0 | 97,080.0 | 32,967.5 | 5 | 375 | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-uuid-grok` | `plain` | `re2_11.0.0_default-caps-simdna` | 68,951.0 | 52,610.0 | 182,441.0 | 48,604.4 | 5 | 72 | 0.705 (max is trial 1) | compiled=5 |
| `wild-validator-uuid-grok` | `plain` | `re2_11.0.0_longest-caps-simdna` | 54,460.0 | 53,260.0 | 173,661.0 | 47,036.6 | 5 | 72 | 0.864 (max is trial 1) | compiled=5 |
| `wild-validator-uuid-grok` | `plain` | `rust_1.13.1_default-caps-simdna` | 59,480.0 | 57,210.0 | 324,781.0 | 105,337.3 | 5 | - | 1.771 (max is trial 1) | compiled=5 |
| `wild-validator-uuid-grok` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 40,320.0 | 35,590.0 | 257,570.0 | 86,887.0 | 5 | - | 2.155 (max is trial 1) | compiled=5 |
| `wild-validator-uuid-grok` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 4,882,346.0 | 2,019,311.0 | 6,228,684.0 | 1,391,757.5 | 5 | 7,472 | 0.285 (max is trial 1) | compiled=5 |
| `wild-validator-uuid-grok` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,060,646.0 | 1,044,886.0 | 1,983,200.0 | 366,524.7 | 5 | 1,896 | 0.346 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942140-dbnames` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 73,570.0 | 68,960.0 | 180,851.0 | 42,863.1 | 5 | 788 | 0.583 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942140-dbnames` | `plain` | `re2_11.0.0_default-caps-simdna` | 292,202.0 | 263,341.0 | 510,042.0 | 91,487.0 | 5 | 221 | 0.313 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942140-dbnames` | `plain` | `re2_11.0.0_longest-caps-simdna` | 117,211.0 | 105,610.0 | 213,622.0 | 40,220.7 | 5 | 221 | 0.343 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942140-dbnames` | `plain` | `rust_1.13.1_default-caps-simdna` | 3,833,262.0 | 2,835,018.0 | 4,694,983.0 | 593,480.2 | 5 | - | 0.155 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 1,203,894.0 | 1,051,733.0 | 2,053,856.0 | 360,200.6 | 5 | - | 0.299 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942140-dbnames` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10,744,178.0 | 10,695,418.0 | 22,996,804.0 | 4,905,904.1 | 5 | 31,592 | 0.457 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 5,433,019.0 | 5,408,519.0 | 15,046,372.0 | 3,773,380.9 | 5 | 19,608 | 0.695 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 20,130.0 | 17,450.0 | 101,721.0 | 32,685.5 | 5 | 216 | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `re2_11.0.0_default-caps-simdna` | 52,791.0 | 45,620.0 | 178,821.0 | 50,715.6 | 5 | 35 | 0.961 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `re2_11.0.0_longest-caps-simdna` | 21,461.0 | 17,990.0 | 96,880.0 | 30,298.2 | 5 | 35 | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `rust_1.13.1_default-caps-simdna` | 604,582.0 | 556,621.0 | 1,669,345.0 | 426,955.7 | 5 | - | 0.706 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 262,091.0 | 247,491.0 | 1,250,924.0 | 390,518.8 | 5 | - | 1.490 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 2,997,886.0 | 2,953,216.0 | 4,302,553.0 | 521,059.8 | 5 | 9,144 | 0.174 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,219,777.0 | 1,202,407.0 | 1,841,440.0 | 249,483.6 | 5 | 4,904 | 0.205 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942270-union-select` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 14,090.0 | 11,700.0 | 86,911.0 | 29,289.8 | 5 | 193 | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942270-union-select` | `plain` | `re2_11.0.0_default-caps-simdna` | 13,540.0 | 10,910.0 | 69,620.0 | 22,498.5 | 5 | 23 | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942270-union-select` | `plain` | `re2_11.0.0_longest-caps-simdna` | 33,430.0 | 27,690.0 | 138,031.0 | 41,950.4 | 5 | 23 | 1.255 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942270-union-select` | `plain` | `rust_1.13.1_default-caps-simdna` | 278,330.0 | 118,880.0 | 621,462.0 | 180,963.3 | 5 | - | 0.650 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 96,951.0 | 78,850.0 | 608,641.0 | 202,006.7 | 5 | - | 2.084 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942270-union-select` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,957,031.0 | 1,849,110.0 | 3,161,057.0 | 500,712.2 | 5 | 11,160 | 0.256 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,955,150.0 | 1,898,750.0 | 3,184,487.0 | 499,313.7 | 5 | 4,936 | 0.255 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 386,192.0 | 370,512.0 | 560,423.0 | 71,007.3 | 5 | 3,459 | 0.184 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `re2_11.0.0_default-caps-simdna` | 1,130,796.0 | 1,064,665.0 | 1,449,627.0 | 140,171.9 | 5 | 859 | 0.124 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `re2_11.0.0_longest-caps-simdna` | 430,713.0 | 417,352.0 | 597,033.0 | 66,913.5 | 5 | 859 | 0.155 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `rust_1.13.1_default-caps-simdna` | 2,119,166.0 | 1,570,605.0 | 3,625,481.0 | 704,283.0 | 5 | - | 0.332 | compiled=5 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 1,351,014.0 | 1,148,633.0 | 2,135,166.0 | 394,928.2 | 5 | - | 0.292 | compiled=5 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 35,551,603.0 | 35,528,062.0 | 48,413,902.0 | 5,127,046.8 | 5 | 99,944 | 0.144 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 38,635,739.0 | 38,597,088.0 | 49,429,037.0 | 4,298,439.5 | 5 | 89,624 | 0.111 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 16,541.0 | 13,700.0 | 95,000.0 | 31,506.6 | 5 | 275 | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `re2_11.0.0_default-caps-simdna` | 18,140.0 | 15,410.0 | 78,441.0 | 24,229.8 | 5 | 20 | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `re2_11.0.0_longest-caps-simdna` | 45,130.0 | 38,440.0 | 164,191.0 | 47,947.1 | 5 | 20 | 1.062 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `rust_1.13.1_default-caps-simdna` | 171,211.0 | 164,541.0 | 1,150,723.0 | 385,886.5 | 5 | - | 2.254 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 94,700.0 | 83,860.0 | 653,522.0 | 219,977.0 | 5 | - | 2.323 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,185,897.0 | 1,128,406.0 | 2,450,234.0 | 505,179.9 | 5 | 6,136 | 0.426 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 699,214.0 | 655,134.0 | 1,335,447.0 | 257,618.8 | 5 | 3,496 | 0.368 (max is trial 1) | compiled=5 |
| `winpath-near-miss` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 13,250.0 | 10,870.0 | 88,231.0 | 30,074.8 | 5 | 275 | timer-floor (max is trial 1) | compiled=5 |
| `winpath-near-miss` | `plain` | `re2_11.0.0_default-caps-simdna` | 44,070.0 | 35,240.0 | 161,391.0 | 47,890.8 | 5 | 28 | 1.087 (max is trial 1) | compiled=5 |
| `winpath-near-miss` | `plain` | `re2_11.0.0_longest-caps-simdna` | 17,960.0 | 14,410.0 | 78,561.0 | 24,623.5 | 5 | 28 | timer-floor (max is trial 1) | compiled=5 |
| `winpath-near-miss` | `plain` | `rust_1.13.1_default-caps-simdna` | 88,270.0 | 63,660.0 | 502,212.0 | 167,280.0 | 5 | - | 1.895 (max is trial 1) | compiled=5 |
| `winpath-near-miss` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 204,781.0 | 177,370.0 | 1,230,094.0 | 408,687.0 | 5 | - | 1.996 (max is trial 1) | compiled=5 |
| `winpath-near-miss` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 2,088,531.0 | 2,043,191.0 | 3,356,148.0 | 508,088.0 | 5 | 4,152 | 0.243 (max is trial 1) | compiled=5 |
| `winpath-near-miss` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,667,289.0 | 1,643,208.0 | 2,893,086.0 | 487,965.5 | 5 | 4,184 | 0.293 (max is trial 1) | compiled=5 |

### `interpretive`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `balanced-parens-rec` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 3,660.0 | 2,840.0 | 44,281.0 | 16,305.7 | 5 | 209 | timer-floor (max is trial 1) | compiled=5 |
| `balanced-parens-rec` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 1,820.0 | 1,360.0 | 21,120.0 | 7,763.8 | 5 | 209 | timer-floor (max is trial 1) | compiled=5 |
| `balanced-parens-rec` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `balanced-parens-rec` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `balanced-parens-rec` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `base10num-near-miss` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 2,730.0 | 2,530.0 | 21,710.0 | 7,544.2 | 5 | 220 | timer-floor (max is trial 1) | compiled=5 |
| `base10num-near-miss` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 3,760.0 | 2,860.0 | 33,470.0 | 11,937.4 | 5 | 220 | timer-floor (max is trial 1) | compiled=5 |
| `base10num-near-miss` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 8,411.0 | 7,580.0 | 25,140.0 | 6,658.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `base10num-near-miss` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 20,720.0 | 18,360.0 | 49,360.0 | 11,696.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `base10num-near-miss` | `plain` | `tre_0.9.0_default-caps-simdna` | 15,390.0 | 10,650.0 | 38,150.0 | 10,117.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `base10num-near-miss` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 14,050.0 | 11,900.0 | 36,490.0 | 9,184.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `bracket-array-define` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 3,260.0 | 2,620.0 | 30,471.0 | 10,903.4 | 5 | 240 | timer-floor (max is trial 1) | compiled=5 |
| `bracket-array-define` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 3,310.0 | 2,620.0 | 27,400.0 | 9,678.7 | 5 | 240 | timer-floor (max is trial 1) | compiled=5 |
| `bracket-array-define` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 9,280.0 | 7,530.0 | 23,700.0 | 6,041.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `bracket-array-define` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 22,220.0 | 18,510.0 | 48,370.0 | 11,179.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `bracket-array-define` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `codegrammar-flat` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 1,670.0 | 1,320.0 | 19,780.0 | 7,261.1 | 5 | 211 | timer-floor (max is trial 1) | compiled=5 |
| `codegrammar-flat` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 4,040.0 | 3,180.0 | 51,540.0 | 19,040.6 | 5 | 211 | timer-floor (max is trial 1) | compiled=5 |
| `codegrammar-flat` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 11,050.0 | 9,570.0 | 22,340.0 | 5,098.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `codegrammar-flat` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 13,510.0 | 11,250.0 | 34,821.0 | 8,872.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `codegrammar-flat` | `plain` | `tre_0.9.0_default-caps-simdna` | 13,330.0 | 11,610.0 | 49,871.0 | 14,542.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `codegrammar-flat` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 14,830.0 | 13,010.0 | 42,730.0 | 11,225.5 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `codegrammar-xflag` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 2,290.0 | 1,910.0 | 21,891.0 | 7,847.7 | 5 | 217 | timer-floor (max is trial 1) | compiled=5 |
| `codegrammar-xflag` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 5,570.0 | 4,590.0 | 47,891.0 | 16,954.4 | 5 | 217 | timer-floor (max is trial 1) | compiled=5 |
| `codegrammar-xflag` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 14,580.0 | 13,090.0 | 38,370.0 | 9,507.5 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `codegrammar-xflag` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 16,250.0 | 14,050.0 | 39,350.0 | 9,475.5 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `codegrammar-xflag` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `currency-lookbehind-fixed` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 2,020.0 | 1,580.0 | 21,050.0 | 7,642.2 | 5 | 186 | timer-floor (max is trial 1) | compiled=5 |
| `currency-lookbehind-fixed` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 2,430.0 | 1,860.0 | 24,930.0 | 9,042.8 | 5 | 186 | timer-floor (max is trial 1) | compiled=5 |
| `currency-lookbehind-fixed` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 12,900.0 | 9,700.0 | 29,150.0 | 7,066.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `currency-lookbehind-fixed` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 14,970.0 | 10,980.0 | 30,850.0 | 7,216.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `currency-lookbehind-fixed` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `date-nested-plus` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 2,140.0 | 1,720.0 | 26,560.0 | 9,798.1 | 5 | 244 | timer-floor (max is trial 1) | compiled=5 |
| `date-nested-plus` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 1,720.0 | 1,370.0 | 26,750.0 | 10,025.5 | 5 | 244 | timer-floor (max is trial 1) | compiled=5 |
| `date-nested-plus` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 5,150.0 | 4,480.0 | 19,970.0 | 5,865.5 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `date-nested-plus` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 5,720.0 | 5,030.0 | 18,250.0 | 5,030.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `date-nested-plus` | `plain` | `tre_0.9.0_default-caps-simdna` | 7,660.0 | 6,080.0 | 22,090.0 | 5,955.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `date-nested-plus` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 9,050.0 | 7,350.0 | 27,210.0 | 7,437.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `doubled-word` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `doubled-word` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 1,750.0 | 1,470.0 | 27,350.0 | 10,231.0 | 5 | 177 | timer-floor (max is trial 1) | compiled=5 |
| `doubled-word` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 11,710.0 | 9,140.0 | 30,380.0 | 7,831.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `doubled-word` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 14,010.0 | 10,740.0 | 31,710.0 | 9,591.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `doubled-word` | `plain` | `tre_0.9.0_default-caps-simdna` | 14,231.0 | 12,130.0 | 40,410.0 | 10,610.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `doubled-word` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 15,590.0 | 13,420.0 | 41,630.0 | 10,685.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `dup-param-detect` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `dup-param-detect` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 2,950.0 | 2,420.0 | 28,750.0 | 10,339.9 | 5 | 192 | timer-floor (max is trial 1) | compiled=5 |
| `dup-param-detect` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 14,580.0 | 12,580.0 | 35,520.0 | 8,799.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `dup-param-detect` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 25,510.0 | 14,360.0 | 36,220.0 | 8,578.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `dup-param-detect` | `plain` | `tre_0.9.0_default-caps-simdna` | 18,130.0 | 13,680.0 | 44,040.0 | 11,215.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `dup-param-detect` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 20,721.0 | 15,340.0 | 43,550.0 | 10,277.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `email-local-nodup` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 1,950.0 | 1,580.0 | 20,590.0 | 7,451.4 | 5 | 214 | timer-floor (max is trial 1) | compiled=5 |
| `email-local-nodup` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 3,430.0 | 2,700.0 | 37,540.0 | 13,649.4 | 5 | 214 | timer-floor (max is trial 1) | compiled=5 |
| `email-local-nodup` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 5,690.0 | 4,360.0 | 24,020.0 | 7,398.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `email-local-nodup` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 11,070.0 | 9,420.0 | 29,380.0 | 7,585.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `email-local-nodup` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `email-nested-plus` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 1,920.0 | 1,560.0 | 22,310.0 | 8,166.5 | 5 | 204 | timer-floor (max is trial 1) | compiled=5 |
| `email-nested-plus` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 3,530.0 | 3,140.0 | 46,020.0 | 16,946.4 | 5 | 204 | timer-floor (max is trial 1) | compiled=5 |
| `email-nested-plus` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 4,960.0 | 3,200.0 | 13,020.0 | 3,572.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `email-nested-plus` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 6,000.0 | 3,930.0 | 14,240.0 | 3,734.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `email-nested-plus` | `plain` | `tre_0.9.0_default-caps-simdna` | 43,440.0 | 32,010.0 | 112,240.0 | 29,750.3 | 5 | - | 0.685 (max is trial 1) | compiled=5 |
| `email-nested-plus` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 37,391.0 | 32,390.0 | 97,540.0 | 24,756.0 | 5 | - | 0.662 (max is trial 1) | compiled=5 |
| `evil-alt-nested` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 1,730.0 | 1,440.0 | 26,000.0 | 9,692.9 | 5 | 212 | timer-floor (max is trial 1) | compiled=5 |
| `evil-alt-nested` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 1,540.0 | 1,180.0 | 19,860.0 | 7,344.9 | 5 | 212 | timer-floor (max is trial 1) | compiled=5 |
| `evil-alt-nested` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 3,810.0 | 2,560.0 | 9,360.0 | 2,493.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `evil-alt-nested` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 4,290.0 | 3,490.0 | 16,120.0 | 4,802.5 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `evil-alt-nested` | `plain` | `tre_0.9.0_default-caps-simdna` | 14,090.0 | 10,990.0 | 43,891.0 | 12,314.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `evil-alt-nested` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 19,990.0 | 14,670.0 | 49,440.0 | 12,829.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `file-ext-order` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 1,240.0 | 1,170.0 | 17,880.0 | 6,641.1 | 5 | 184 | timer-floor (max is trial 1) | compiled=5 |
| `file-ext-order` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 1,040.0 | 930.0 | 16,370.0 | 6,132.0 | 5 | 184 | timer-floor (max is trial 1) | compiled=5 |
| `file-ext-order` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 4,220.0 | 3,870.0 | 11,960.0 | 3,079.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `file-ext-order` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 2,790.0 | 2,440.0 | 12,510.0 | 3,905.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `file-ext-order` | `plain` | `tre_0.9.0_default-caps-simdna` | 16,530.0 | 14,590.0 | 48,920.0 | 13,018.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `file-ext-order` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 8,230.0 | 7,410.0 | 23,080.0 | 5,937.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `float-literal-bound` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 4,570.0 | 3,790.0 | 51,871.0 | 18,907.1 | 5 | 246 | timer-floor (max is trial 1) | compiled=5 |
| `float-literal-bound` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 2,560.0 | 2,100.0 | 24,400.0 | 8,733.7 | 5 | 246 | timer-floor (max is trial 1) | compiled=5 |
| `float-literal-bound` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 15,230.0 | 14,050.0 | 34,781.0 | 7,937.5 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `float-literal-bound` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 25,420.0 | 16,120.0 | 70,061.0 | 19,843.0 | 5 | - | timer-floor | compiled=5 |
| `float-literal-bound` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `floor-byte` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 970.0 | 870.0 | 37,891.0 | 14,759.9 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `floor-byte` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 450.0 | 380.0 | 20,270.0 | 7,920.5 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `floor-byte` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 750.0 | 650.0 | 5,810.0 | 2,027.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `floor-byte` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 1,230.0 | 1,070.0 | 7,600.0 | 2,547.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `floor-byte` | `plain` | `tre_0.9.0_default-caps-simdna` | 2,030.0 | 1,520.0 | 24,030.0 | 8,792.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `floor-byte` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 3,690.0 | 2,910.0 | 15,820.0 | 4,899.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `high-byte-run` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 1,090.0 | 970.0 | 23,350.0 | 8,898.0 | 5 | 197 | timer-floor (max is trial 1) | compiled=5 |
| `high-byte-run` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 890.0 | 780.0 | 19,550.0 | 7,454.1 | 5 | 197 | timer-floor (max is trial 1) | compiled=5 |
| `high-byte-run` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 1,820.0 | 1,750.0 | 9,490.0 | 3,047.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `high-byte-run` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 2,280.0 | 2,020.0 | 9,060.0 | 2,713.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `high-byte-run` | `plain` | `tre_0.9.0_default-caps-simdna` | 17,821.0 | 15,650.0 | 68,060.0 | 19,918.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `high-byte-run` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 19,970.0 | 17,960.0 | 71,120.0 | 20,272.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `ipv4-near-miss` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 10,990.0 | 9,530.0 | 63,711.0 | 21,103.7 | 5 | 693 | timer-floor (max is trial 1) | compiled=5 |
| `ipv4-near-miss` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 4,440.0 | 3,810.0 | 34,630.0 | 12,077.5 | 5 | 693 | timer-floor (max is trial 1) | compiled=5 |
| `ipv4-near-miss` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 59,200.0 | 52,951.0 | 117,041.0 | 23,797.8 | 5 | - | 0.402 (max is trial 1) | compiled=5 |
| `ipv4-near-miss` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 29,830.0 | 26,340.0 | 40,130.0 | 5,089.7 | 5 | - | 0.171 (max is trial 1) | compiled=5 |
| `ipv4-near-miss` | `plain` | `tre_0.9.0_default-caps-simdna` | 42,810.0 | 36,190.0 | 86,531.0 | 18,815.0 | 5 | - | 0.440 (max is trial 1) | compiled=5 |
| `ipv4-near-miss` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 39,740.0 | 38,660.0 | 118,270.0 | 30,896.5 | 5 | - | 0.777 (max is trial 1) | compiled=5 |
| `keyword-prefix-order` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 1,250.0 | 1,140.0 | 20,790.0 | 7,803.4 | 5 | 186 | timer-floor (max is trial 1) | compiled=5 |
| `keyword-prefix-order` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 2,500.0 | 2,250.0 | 39,140.0 | 14,630.2 | 5 | 186 | timer-floor (max is trial 1) | compiled=5 |
| `keyword-prefix-order` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 4,130.0 | 3,730.0 | 15,520.0 | 4,557.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `keyword-prefix-order` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 2,590.0 | 2,360.0 | 12,401.0 | 3,907.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `keyword-prefix-order` | `plain` | `tre_0.9.0_default-caps-simdna` | 7,320.0 | 6,600.0 | 21,540.0 | 5,683.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `keyword-prefix-order` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 8,490.0 | 7,560.0 | 22,900.0 | 5,808.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `logparse-atomic` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 6,140.0 | 5,590.0 | 23,970.0 | 7,139.8 | 5 | 376 | timer-floor (max is trial 1) | compiled=5 |
| `logparse-atomic` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 6,140.0 | 5,670.0 | 23,681.0 | 7,032.3 | 5 | 376 | timer-floor (max is trial 1) | compiled=5 |
| `logparse-atomic` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 20,790.0 | 15,030.0 | 29,410.0 | 6,007.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `logparse-atomic` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 39,610.0 | 34,890.0 | 63,840.0 | 10,716.9 | 5 | - | 0.271 (max is trial 1) | compiled=5 |
| `logparse-atomic` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `logparse-atomic-removed` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 6,140.0 | 5,620.0 | 23,130.0 | 6,815.2 | 5 | 376 | timer-floor (max is trial 1) | compiled=5 |
| `logparse-atomic-removed` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 7,700.0 | 7,130.0 | 31,090.0 | 9,353.1 | 5 | 376 | timer-floor (max is trial 1) | compiled=5 |
| `logparse-atomic-removed` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 37,950.0 | 33,670.0 | 60,680.0 | 10,033.5 | 5 | - | 0.264 (max is trial 1) | compiled=5 |
| `logparse-atomic-removed` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 34,780.0 | 32,030.0 | 63,411.0 | 11,773.1 | 5 | - | 0.339 (max is trial 1) | compiled=5 |
| `logparse-atomic-removed` | `plain` | `tre_0.9.0_default-caps-simdna` | 54,860.0 | 42,490.0 | 95,000.0 | 19,076.6 | 5 | - | 0.348 (max is trial 1) | compiled=5 |
| `logparse-atomic-removed` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 46,510.0 | 43,841.0 | 98,861.0 | 20,921.0 | 5 | - | 0.450 (max is trial 1) | compiled=5 |
| `mojibake-curly-quote` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 2,600.0 | 2,080.0 | 49,411.0 | 18,752.8 | 5 | 197 | timer-floor (max is trial 1) | compiled=5 |
| `mojibake-curly-quote` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 1,090.0 | 890.0 | 21,330.0 | 8,103.5 | 5 | 197 | timer-floor (max is trial 1) | compiled=5 |
| `mojibake-curly-quote` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 2,720.0 | 2,420.0 | 10,800.0 | 3,245.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `mojibake-curly-quote` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 2,910.0 | 2,630.0 | 8,330.0 | 2,164.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `mojibake-curly-quote` | `plain` | `tre_0.9.0_default-caps-simdna` | 17,390.0 | 7,410.0 | 26,860.0 | 7,149.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `mojibake-curly-quote` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 9,921.0 | 8,690.0 | 40,510.0 | 12,091.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `negation-scope-lookbehind-var` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 7,870.0 | 6,540.0 | 56,460.0 | 19,545.9 | 5 | 265 | timer-floor (max is trial 1) | compiled=5 |
| `negation-scope-lookbehind-var` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 3,720.0 | 3,200.0 | 26,670.0 | 9,199.0 | 5 | 265 | timer-floor (max is trial 1) | compiled=5 |
| `negation-scope-lookbehind-var` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `negation-scope-lookbehind-var` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `nested-comment-rec` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 6,830.0 | 5,430.0 | 54,961.0 | 19,332.4 | 5 | 247 | timer-floor (max is trial 1) | compiled=5 |
| `nested-comment-rec` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 3,340.0 | 2,750.0 | 28,620.0 | 10,131.0 | 5 | 247 | timer-floor (max is trial 1) | compiled=5 |
| `nested-comment-rec` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 8,220.0 | 6,840.0 | 19,010.0 | 4,568.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `nested-comment-rec` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 26,040.0 | 21,281.0 | 58,510.0 | 13,383.7 | 5 | - | 0.514 (max is trial 1) | compiled=5 |
| `nested-comment-rec` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `numeric-id-nested-plus` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 1,310.0 | 1,040.0 | 21,440.0 | 8,055.4 | 5 | 171 | timer-floor (max is trial 1) | compiled=5 |
| `numeric-id-nested-plus` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 2,670.0 | 2,230.0 | 42,180.0 | 15,792.0 | 5 | 171 | timer-floor (max is trial 1) | compiled=5 |
| `numeric-id-nested-plus` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 4,110.0 | 2,810.0 | 12,500.0 | 3,587.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `numeric-id-nested-plus` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 6,930.0 | 4,660.0 | 27,090.0 | 8,432.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `numeric-id-nested-plus` | `plain` | `tre_0.9.0_default-caps-simdna` | 13,620.0 | 11,270.0 | 48,181.0 | 13,997.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `numeric-id-nested-plus` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 18,880.0 | 12,980.0 | 48,290.0 | 12,905.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `phone-list-nested-plus` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 1,680.0 | 1,330.0 | 21,510.0 | 7,960.6 | 5 | 173 | timer-floor (max is trial 1) | compiled=5 |
| `phone-list-nested-plus` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 1,310.0 | 1,040.0 | 17,700.0 | 6,568.1 | 5 | 173 | timer-floor (max is trial 1) | compiled=5 |
| `phone-list-nested-plus` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 12,320.0 | 10,610.0 | 34,250.0 | 8,957.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `phone-list-nested-plus` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 6,280.0 | 5,550.0 | 15,410.0 | 3,777.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `phone-list-nested-plus` | `plain` | `tre_0.9.0_default-caps-simdna` | 20,550.0 | 17,390.0 | 74,420.0 | 21,727.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `phone-list-nested-plus` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 23,500.0 | 19,710.0 | 69,561.0 | 18,679.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `phone-palindrome-6` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `phone-palindrome-6` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 2,600.0 | 2,370.0 | 25,711.0 | 9,267.0 | 5 | 195 | timer-floor (max is trial 1) | compiled=5 |
| `phone-palindrome-6` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 13,100.0 | 10,640.0 | 25,160.0 | 5,302.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `phone-palindrome-6` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 14,750.0 | 11,850.0 | 29,460.0 | 6,381.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `phone-palindrome-6` | `plain` | `tre_0.9.0_default-caps-simdna` | 9,570.0 | 8,630.0 | 28,361.0 | 7,539.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `phone-palindrome-6` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 11,240.0 | 10,050.0 | 33,610.0 | 8,996.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `pwd-strength-chain` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 3,320.0 | 2,840.0 | 27,560.0 | 9,691.6 | 5 | 299 | timer-floor (max is trial 1) | compiled=5 |
| `pwd-strength-chain` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 3,400.0 | 2,800.0 | 31,810.0 | 11,391.6 | 5 | 299 | timer-floor (max is trial 1) | compiled=5 |
| `pwd-strength-chain` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 12,390.0 | 10,440.0 | 26,610.0 | 6,009.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `pwd-strength-chain` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 27,940.0 | 21,770.0 | 85,361.0 | 24,136.3 | 5 | - | 0.864 (max is trial 1) | compiled=5 |
| `pwd-strength-chain` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `quoted-delim-match` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `quoted-delim-match` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 2,920.0 | 2,230.0 | 28,830.0 | 10,428.8 | 5 | 227 | timer-floor (max is trial 1) | compiled=5 |
| `quoted-delim-match` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 10,510.0 | 8,700.0 | 30,220.0 | 9,855.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `quoted-delim-match` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 12,220.0 | 10,180.0 | 29,500.0 | 7,215.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `quoted-delim-match` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `router-prefix-order` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 1,190.0 | 1,050.0 | 20,190.0 | 7,591.2 | 5 | 184 | timer-floor (max is trial 1) | compiled=5 |
| `router-prefix-order` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 1,040.0 | 900.0 | 21,680.0 | 8,258.9 | 5 | 184 | timer-floor (max is trial 1) | compiled=5 |
| `router-prefix-order` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 2,550.0 | 2,340.0 | 15,200.0 | 5,053.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `router-prefix-order` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 2,740.0 | 2,390.0 | 12,370.0 | 3,869.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `router-prefix-order` | `plain` | `tre_0.9.0_default-caps-simdna` | 7,290.0 | 6,520.0 | 21,940.0 | 5,859.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `router-prefix-order` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 8,320.0 | 7,360.0 | 22,500.0 | 6,479.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `tag-depth3-bound` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 4,611.0 | 3,920.0 | 31,270.0 | 10,716.3 | 5 | 254 | timer-floor (max is trial 1) | compiled=5 |
| `tag-depth3-bound` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 4,360.0 | 3,770.0 | 30,250.0 | 10,347.4 | 5 | 254 | timer-floor (max is trial 1) | compiled=5 |
| `tag-depth3-bound` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 17,830.0 | 16,180.0 | 44,510.0 | 10,747.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `tag-depth3-bound` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 27,120.0 | 20,841.0 | 80,371.0 | 22,576.7 | 5 | - | 0.832 (max is trial 1) | compiled=5 |
| `tag-depth3-bound` | `plain` | `tre_0.9.0_default-caps-simdna` | 42,921.0 | 32,740.0 | 83,230.0 | 18,564.0 | 5 | - | 0.433 (max is trial 1) | compiled=5 |
| `tag-depth3-bound` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 51,100.0 | 35,121.0 | 92,951.0 | 21,065.1 | 5 | - | 0.412 (max is trial 1) | compiled=5 |
| `tag-pair-match` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `tag-pair-match` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 4,130.0 | 3,160.0 | 30,540.0 | 10,651.9 | 5 | 261 | timer-floor (max is trial 1) | compiled=5 |
| `tag-pair-match` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 22,440.0 | 20,000.0 | 43,800.0 | 8,778.4 | 5 | - | 0.391 (max is trial 1) | compiled=5 |
| `tag-pair-match` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 27,230.0 | 23,360.0 | 46,871.0 | 8,485.7 | 5 | - | 0.312 (max is trial 1) | compiled=5 |
| `tag-pair-match` | `plain` | `tre_0.9.0_default-caps-simdna` | 27,471.0 | 19,670.0 | 54,140.0 | 12,515.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `tag-pair-match` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 23,790.0 | 21,151.0 | 65,000.0 | 16,557.3 | 5 | - | 0.696 (max is trial 1) | compiled=5 |
| `trim-nested-star` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 1,390.0 | 1,140.0 | 22,240.0 | 8,342.6 | 5 | 172 | timer-floor (max is trial 1) | compiled=5 |
| `trim-nested-star` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 2,620.0 | 2,010.0 | 41,431.0 | 15,537.3 | 5 | 172 | timer-floor (max is trial 1) | compiled=5 |
| `trim-nested-star` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 8,700.0 | 6,950.0 | 21,361.0 | 5,311.5 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `trim-nested-star` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 4,870.0 | 3,530.0 | 15,040.0 | 4,235.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `trim-nested-star` | `plain` | `tre_0.9.0_default-caps-simdna` | 18,140.0 | 14,890.0 | 54,281.0 | 14,819.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `trim-nested-star` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 26,550.0 | 19,690.0 | 82,601.0 | 23,396.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `utf8-lead-no-cont` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 1,420.0 | 1,240.0 | 22,070.0 | 8,253.5 | 5 | 231 | timer-floor (max is trial 1) | compiled=5 |
| `utf8-lead-no-cont` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 1,380.0 | 1,200.0 | 30,010.0 | 11,441.2 | 5 | 231 | timer-floor (max is trial 1) | compiled=5 |
| `utf8-lead-no-cont` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 1,960.0 | 1,670.0 | 11,620.0 | 3,867.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `utf8-lead-no-cont` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 3,210.0 | 2,500.0 | 7,140.0 | 1,705.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `utf8-lead-no-cont` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `uuid-near-miss` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 7,620.0 | 7,060.0 | 49,290.0 | 16,612.0 | 5 | 425 | timer-floor (max is trial 1) | compiled=5 |
| `uuid-near-miss` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 3,090.0 | 2,850.0 | 21,801.0 | 7,468.5 | 5 | 425 | timer-floor (max is trial 1) | compiled=5 |
| `uuid-near-miss` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 25,470.0 | 20,450.0 | 41,891.0 | 7,640.4 | 5 | - | 0.300 (max is trial 1) | compiled=5 |
| `uuid-near-miss` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 10,340.0 | 8,260.0 | 31,180.0 | 8,701.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `uuid-near-miss` | `plain` | `tre_0.9.0_default-caps-simdna` | 47,050.0 | 44,750.0 | 125,130.0 | 30,773.9 | 5 | - | 0.654 (max is trial 1) | compiled=5 |
| `uuid-near-miss` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 50,190.0 | 46,441.0 | 128,931.0 | 31,291.4 | 5 | - | 0.623 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-array-begin` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 350.0 | 310.0 | 14,440.0 | 5,632.3 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-array-begin` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 940.0 | 800.0 | 38,190.0 | 14,891.9 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-array-begin` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 1,360.0 | 1,240.0 | 11,900.0 | 4,222.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 2,290.0 | 2,050.0 | 19,450.0 | 6,868.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-array-begin` | `plain` | `tre_0.9.0_default-caps-simdna` | 1,970.0 | 1,540.0 | 11,441.0 | 3,785.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 3,531.0 | 2,860.0 | 16,620.0 | 5,265.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-constant` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 1,830.0 | 1,630.0 | 21,920.0 | 8,030.8 | 5 | 199 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-constant` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 2,610.0 | 2,200.0 | 44,640.0 | 16,811.0 | 5 | 199 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-constant` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 7,390.0 | 5,810.0 | 20,750.0 | 5,487.5 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-constant` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 8,670.0 | 6,400.0 | 55,740.0 | 18,959.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-constant` | `plain` | `tre_0.9.0_default-caps-simdna` | 12,720.0 | 8,880.0 | 31,680.0 | 8,317.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-constant` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 22,760.0 | 20,050.0 | 78,881.0 | 22,414.8 | 5 | - | 0.985 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-number-extended` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 5,370.0 | 4,580.0 | 59,800.0 | 21,748.6 | 5 | 270 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-number-extended` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 7,630.0 | 6,410.0 | 47,420.0 | 15,970.1 | 5 | 270 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-number-extended` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 33,940.0 | 29,240.0 | 66,640.0 | 13,993.5 | 5 | - | 0.412 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-number-extended` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `wild-codegrammar-json-number-extended` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-codegrammar-json-object-begin` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 350.0 | 320.0 | 15,340.0 | 5,989.2 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-object-begin` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 470.0 | 420.0 | 18,960.0 | 7,389.4 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-object-begin` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 1,370.0 | 1,200.0 | 26,100.0 | 9,910.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 2,260.0 | 2,020.0 | 8,360.0 | 2,440.5 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-object-begin` | `plain` | `tre_0.9.0_default-caps-simdna` | 2,100.0 | 1,510.0 | 17,770.0 | 6,287.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 3,430.0 | 2,680.0 | 14,610.0 | 4,530.5 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 2,780.0 | 2,340.0 | 21,340.0 | 7,431.2 | 5 | 243 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 3,340.0 | 2,890.0 | 26,150.0 | 9,117.0 | 5 | 243 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 13,360.0 | 10,380.0 | 46,361.0 | 13,602.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-stringcontent-escape` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-datetime-datefinder-alternation` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 289,142.0 | 272,832.0 | 330,232.0 | 21,213.3 | 5 | 16,813 | 0.073 (max is trial 1) | compiled=5 |
| `wild-datetime-datefinder-alternation` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 282,442.0 | 275,561.0 | 336,012.0 | 22,291.8 | 5 | 16,813 | 0.079 (max is trial 1) | compiled=5 |
| `wild-datetime-datefinder-alternation` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 2,536,937.0 | 2,406,686.0 | 2,993,639.0 | 214,385.3 | 5 | - | 0.085 (max is trial 1) | compiled=5 |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 2,512,887.0 | 2,440,106.0 | 3,000,739.0 | 209,918.4 | 5 | - | 0.084 (max is trial 1) | compiled=5 |
| `wild-datetime-datefinder-alternation` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `wild-datetime-moment-iso8601` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 8,010.0 | 6,840.0 | 27,760.0 | 7,980.6 | 5 | 421 | timer-floor (max is trial 1) | compiled=5 |
| `wild-datetime-moment-iso8601` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 8,010.0 | 6,950.0 | 27,880.0 | 8,019.1 | 5 | 421 | timer-floor (max is trial 1) | compiled=5 |
| `wild-datetime-moment-iso8601` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 123,090.0 | 111,511.0 | 173,702.0 | 22,869.3 | 5 | - | 0.186 (max is trial 1) | compiled=5 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 122,390.0 | 109,851.0 | 161,761.0 | 18,882.6 | 5 | - | 0.154 (max is trial 1) | compiled=5 |
| `wild-datetime-moment-iso8601` | `plain` | `tre_0.9.0_default-caps-simdna` | 88,061.0 | 84,010.0 | 144,451.0 | 22,432.0 | 5 | - | 0.255 (max is trial 1) | compiled=5 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 89,141.0 | 86,021.0 | 145,841.0 | 22,575.2 | 5 | - | 0.253 (max is trial 1) | compiled=5 |
| `wild-logparse-base10num-grok` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 4,300.0 | 3,340.0 | 30,780.0 | 10,649.7 | 5 | 375 | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-base10num-grok` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 4,030.0 | 3,400.0 | 32,430.0 | 11,357.3 | 5 | 375 | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-base10num-grok` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 21,790.0 | 17,460.0 | 46,260.0 | 10,643.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-base10num-grok` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 23,540.0 | 18,660.0 | 46,470.0 | 10,149.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-base10num-grok` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-base10num-noatomic` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 4,350.0 | 3,500.0 | 25,781.0 | 8,620.4 | 5 | 375 | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-base10num-noatomic` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 4,300.0 | 3,430.0 | 27,570.0 | 9,371.1 | 5 | 375 | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-base10num-noatomic` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 17,170.0 | 14,440.0 | 44,231.0 | 11,213.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-base10num-noatomic` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 21,570.0 | 17,230.0 | 39,900.0 | 8,277.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-base10num-noatomic` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-quotedstring-grok` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 5,290.0 | 4,550.0 | 25,140.0 | 7,951.8 | 5 | 371 | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-quotedstring-grok` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 5,200.0 | 4,410.0 | 25,600.0 | 8,196.7 | 5 | 371 | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-quotedstring-grok` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 42,270.0 | 35,301.0 | 75,601.0 | 14,924.7 | 5 | - | 0.353 (max is trial 1) | compiled=5 |
| `wild-logparse-quotedstring-grok` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 44,911.0 | 36,840.0 | 72,381.0 | 13,000.0 | 5 | - | 0.289 (max is trial 1) | compiled=5 |
| `wild-logparse-quotedstring-grok` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 5,380.0 | 4,580.0 | 32,440.0 | 10,846.3 | 5 | 371 | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 5,230.0 | 4,510.0 | 26,790.0 | 8,618.7 | 5 | 371 | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 33,990.0 | 28,240.0 | 67,790.0 | 14,545.4 | 5 | - | 0.428 (max is trial 1) | compiled=5 |
| `wild-logparse-quotedstring-noatomic` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 35,870.0 | 30,500.0 | 66,800.0 | 13,412.1 | 5 | - | 0.374 (max is trial 1) | compiled=5 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-syslogbase-expanded` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 107,590.0 | 93,530.0 | 153,791.0 | 21,968.4 | 5 | 10,481 | 0.204 (max is trial 1) | compiled=5 |
| `wild-logparse-syslogbase-expanded` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 104,170.0 | 91,420.0 | 151,560.0 | 21,955.5 | 5 | 10,481 | 0.211 (max is trial 1) | compiled=5 |
| `wild-logparse-syslogbase-expanded` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 790,795.0 | 728,345.0 | 935,566.0 | 70,721.8 | 5 | - | 0.089 (max is trial 1) | compiled=5 |
| `wild-logparse-syslogbase-expanded` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 958,736.0 | 941,876.0 | 1,139,188.0 | 74,375.3 | 5 | - | 0.078 (max is trial 1) | compiled=5 |
| `wild-logparse-syslogbase-expanded` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-winpath-grok` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 2,490.0 | 1,990.0 | 20,280.0 | 7,141.3 | 5 | 248 | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-winpath-grok` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 2,440.0 | 1,930.0 | 20,510.0 | 7,261.2 | 5 | 248 | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-winpath-grok` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 5,790.0 | 5,330.0 | 20,140.0 | 5,667.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-winpath-grok` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 15,430.0 | 12,720.0 | 36,610.0 | 9,008.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-winpath-grok` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-secrets-aws-access-key-id` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 4,040.0 | 3,610.0 | 25,330.0 | 8,507.4 | 5 | 340 | timer-floor (max is trial 1) | compiled=5 |
| `wild-secrets-aws-access-key-id` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 4,100.0 | 3,620.0 | 21,260.0 | 6,872.6 | 5 | 340 | timer-floor (max is trial 1) | compiled=5 |
| `wild-secrets-aws-access-key-id` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 12,150.0 | 9,920.0 | 36,241.0 | 9,949.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 17,220.0 | 12,710.0 | 52,180.0 | 14,784.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-secrets-aws-access-key-id` | `plain` | `tre_0.9.0_default-caps-simdna` | 43,050.0 | 33,270.0 | 85,440.0 | 19,151.0 | 5 | - | 0.445 (max is trial 1) | compiled=5 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 43,750.0 | 34,360.0 | 90,330.0 | 20,395.3 | 5 | - | 0.466 (max is trial 1) | compiled=5 |
| `wild-secrets-github-pat` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 1,940.0 | 1,670.0 | 19,660.0 | 7,079.1 | 5 | 229 | timer-floor (max is trial 1) | compiled=5 |
| `wild-secrets-github-pat` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 4,610.0 | 3,940.0 | 46,580.0 | 16,807.6 | 5 | 229 | timer-floor (max is trial 1) | compiled=5 |
| `wild-secrets-github-pat` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 5,070.0 | 3,730.0 | 9,800.0 | 2,189.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-secrets-github-pat` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 5,870.0 | 3,770.0 | 13,731.0 | 3,571.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-secrets-github-pat` | `plain` | `tre_0.9.0_default-caps-simdna` | 128,800.0 | 112,120.0 | 362,212.0 | 95,748.7 | 5 | - | 0.743 (max is trial 1) | compiled=5 |
| `wild-secrets-github-pat` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 117,001.0 | 114,311.0 | 363,092.0 | 97,913.0 | 5 | - | 0.837 (max is trial 1) | compiled=5 |
| `wild-secrets-slack-webhook-url` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 3,830.0 | 3,600.0 | 22,200.0 | 7,329.3 | 5 | 353 | timer-floor (max is trial 1) | compiled=5 |
| `wild-secrets-slack-webhook-url` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 4,020.0 | 3,670.0 | 22,551.0 | 7,408.1 | 5 | 353 | timer-floor (max is trial 1) | compiled=5 |
| `wild-secrets-slack-webhook-url` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 28,770.0 | 25,370.0 | 42,650.0 | 6,145.9 | 5 | - | 0.214 (max is trial 1) | compiled=5 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 29,320.0 | 25,830.0 | 42,480.0 | 5,912.0 | 5 | - | 0.202 (max is trial 1) | compiled=5 |
| `wild-secrets-slack-webhook-url` | `plain` | `tre_0.9.0_default-caps-simdna` | 142,170.0 | 100,221.0 | 271,512.0 | 62,578.0 | 5 | - | 0.440 (max is trial 1) | compiled=5 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 141,631.0 | 102,710.0 | 285,351.0 | 67,204.4 | 5 | - | 0.475 (max is trial 1) | compiled=5 |
| `wild-secrets-username-password-pair` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 10,010.0 | 8,740.0 | 32,980.0 | 9,280.6 | 5 | 778 | timer-floor (max is trial 1) | compiled=5 |
| `wild-secrets-username-password-pair` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 10,130.0 | 8,930.0 | 34,900.0 | 9,993.0 | 5 | 778 | timer-floor (max is trial 1) | compiled=5 |
| `wild-secrets-username-password-pair` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 33,400.0 | 28,590.0 | 57,871.0 | 10,662.4 | 5 | - | 0.319 (max is trial 1) | compiled=5 |
| `wild-secrets-username-password-pair` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 36,800.0 | 31,160.0 | 53,711.0 | 8,246.6 | 5 | - | 0.224 (max is trial 1) | compiled=5 |
| `wild-secrets-username-password-pair` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `wild-secrets-username-password-pair` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 1,170.0 | 1,040.0 | 22,030.0 | 8,327.9 | 5 | 180 | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 1,130.0 | 1,020.0 | 16,700.0 | 6,217.5 | 5 | 180 | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 2,070.0 | 1,810.0 | 5,160.0 | 1,258.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 2,520.0 | 2,330.0 | 10,420.0 | 3,148.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `tre_0.9.0_default-caps-simdna` | 6,740.0 | 5,860.0 | 23,270.0 | 6,592.5 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 7,820.0 | 6,570.0 | 23,740.0 | 6,463.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 720.0 | 620.0 | 16,830.0 | 6,441.8 | 5 | 166 | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 610.0 | 530.0 | 15,740.0 | 6,050.7 | 5 | 166 | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 1,280.0 | 1,140.0 | 4,310.0 | 1,212.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 1,600.0 | 1,460.0 | 8,790.0 | 2,862.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `tre_0.9.0_default-caps-simdna` | 3,770.0 | 3,130.0 | 13,830.0 | 4,061.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 5,170.0 | 4,320.0 | 15,441.0 | 4,187.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 1,120.0 | 850.0 | 19,760.0 | 7,472.1 | 5 | 174 | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 1,340.0 | 1,030.0 | 32,631.0 | 12,537.1 | 5 | 174 | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 4,170.0 | 3,560.0 | 13,741.0 | 3,830.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 4,990.0 | 3,940.0 | 12,430.0 | 3,143.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `tre_0.9.0_default-caps-simdna` | 8,630.0 | 6,910.0 | 27,600.0 | 7,777.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 9,960.0 | 8,370.0 | 31,350.0 | 8,666.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-email-owasp` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 3,540.0 | 3,040.0 | 22,970.0 | 7,786.7 | 5 | 320 | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-email-owasp` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 3,490.0 | 2,960.0 | 23,960.0 | 8,207.6 | 5 | 320 | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-email-owasp` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 10,400.0 | 7,650.0 | 19,060.0 | 4,068.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-email-owasp` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 27,380.0 | 20,460.0 | 59,180.0 | 14,148.9 | 5 | - | 0.517 (max is trial 1) | compiled=5 |
| `wild-validator-email-owasp` | `plain` | `tre_0.9.0_default-caps-simdna` | 26,360.0 | 23,440.0 | 71,470.0 | 18,116.9 | 5 | - | 0.687 (max is trial 1) | compiled=5 |
| `wild-validator-email-owasp` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 34,300.0 | 27,490.0 | 72,830.0 | 16,699.4 | 5 | - | 0.487 (max is trial 1) | compiled=5 |
| `wild-validator-ipv4-owasp` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 6,510.0 | 6,240.0 | 29,860.0 | 9,293.8 | 5 | 1,047 | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-ipv4-owasp` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 6,440.0 | 6,070.0 | 29,090.0 | 8,997.6 | 5 | 1,047 | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-ipv4-owasp` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 26,281.0 | 23,320.0 | 56,830.0 | 12,660.3 | 5 | - | 0.482 (max is trial 1) | compiled=5 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 71,370.0 | 59,191.0 | 114,281.0 | 21,350.2 | 5 | - | 0.299 (max is trial 1) | compiled=5 |
| `wild-validator-ipv4-owasp` | `plain` | `tre_0.9.0_default-caps-simdna` | 42,700.0 | 36,380.0 | 85,520.0 | 18,551.5 | 5 | - | 0.434 (max is trial 1) | compiled=5 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 42,661.0 | 38,080.0 | 85,461.0 | 17,596.8 | 5 | - | 0.412 (max is trial 1) | compiled=5 |
| `wild-validator-us-zip-owasp` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 1,360.0 | 1,060.0 | 19,110.0 | 7,114.6 | 5 | 180 | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-us-zip-owasp` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 3,500.0 | 2,680.0 | 48,831.0 | 18,178.9 | 5 | 180 | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-us-zip-owasp` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 5,590.0 | 3,990.0 | 12,300.0 | 3,037.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 13,820.0 | 11,960.0 | 38,250.0 | 9,927.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-us-zip-owasp` | `plain` | `tre_0.9.0_default-caps-simdna` | 11,830.0 | 9,860.0 | 33,310.0 | 9,130.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 12,020.0 | 10,600.0 | 34,540.0 | 9,116.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-uuid-grok` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 2,260.0 | 2,060.0 | 20,960.0 | 7,459.0 | 5 | 375 | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-uuid-grok` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 2,180.0 | 2,020.0 | 23,250.0 | 8,415.4 | 5 | 375 | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-uuid-grok` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 5,310.0 | 3,660.0 | 12,361.0 | 3,168.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-uuid-grok` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 12,850.0 | 11,540.0 | 25,080.0 | 5,689.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-uuid-grok` | `plain` | `tre_0.9.0_default-caps-simdna` | 47,660.0 | 39,640.0 | 119,790.0 | 29,959.4 | 5 | - | 0.629 (max is trial 1) | compiled=5 |
| `wild-validator-uuid-grok` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 44,490.0 | 41,490.0 | 120,861.0 | 30,188.4 | 5 | - | 0.679 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942140-dbnames` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 16,350.0 | 15,360.0 | 39,960.0 | 9,510.4 | 5 | 788 | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942140-dbnames` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 16,520.0 | 15,300.0 | 40,660.0 | 9,739.2 | 5 | 788 | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942140-dbnames` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 145,391.0 | 141,191.0 | 196,671.0 | 20,797.4 | 5 | - | 0.143 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 336,712.0 | 315,563.0 | 464,203.0 | 55,035.8 | 5 | - | 0.163 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942140-dbnames` | `plain` | `tre_0.9.0_default-caps-simdna` | 276,491.0 | 229,641.0 | 495,392.0 | 97,784.6 | 5 | - | 0.354 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 289,811.0 | 228,851.0 | 498,172.0 | 98,486.8 | 5 | - | 0.340 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 2,680.0 | 2,400.0 | 21,020.0 | 7,331.6 | 5 | 216 | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 2,640.0 | 2,340.0 | 19,560.0 | 6,775.5 | 5 | 216 | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 19,550.0 | 16,620.0 | 34,750.0 | 6,673.5 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 45,530.0 | 37,740.0 | 79,250.0 | 15,970.7 | 5 | - | 0.351 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `tre_0.9.0_default-caps-simdna` | 41,410.0 | 36,820.0 | 95,550.0 | 22,179.7 | 5 | - | 0.536 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 42,410.0 | 37,690.0 | 89,060.0 | 19,123.2 | 5 | - | 0.451 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942270-union-select` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 1,480.0 | 1,310.0 | 15,860.0 | 5,753.0 | 5 | 193 | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942270-union-select` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 1,500.0 | 1,340.0 | 15,910.0 | 5,767.0 | 5 | 193 | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942270-union-select` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 11,661.0 | 9,740.0 | 21,550.0 | 4,314.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 28,001.0 | 22,970.0 | 53,390.0 | 11,170.3 | 5 | - | 0.399 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942270-union-select` | `plain` | `tre_0.9.0_default-caps-simdna` | 19,580.0 | 18,311.0 | 50,840.0 | 12,348.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 28,430.0 | 19,590.0 | 55,781.0 | 13,031.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 68,260.0 | 67,061.0 | 101,170.0 | 13,114.6 | 5 | 3,459 | 0.192 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 73,020.0 | 67,181.0 | 105,251.0 | 14,053.5 | 5 | 3,459 | 0.192 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 662,274.0 | 629,374.0 | 835,896.0 | 75,166.1 | 5 | - | 0.113 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 1,427,550.0 | 1,383,830.0 | 1,798,132.0 | 154,340.1 | 5 | - | 0.108 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `tre_0.9.0_default-caps-simdna` | 1,600,428.0 | 1,115,305.0 | 2,669,973.0 | 511,051.5 | 5 | - | 0.319 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 1,581,517.0 | 1,105,026.0 | 2,713,833.0 | 534,774.8 | 5 | - | 0.338 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 2,870.0 | 2,420.0 | 23,210.0 | 8,142.0 | 5 | 275 | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 2,830.0 | 2,310.0 | 24,250.0 | 8,603.8 | 5 | 275 | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 10,350.0 | 8,180.0 | 17,040.0 | 3,143.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 20,870.0 | 15,850.0 | 45,140.0 | 10,638.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `winpath-near-miss` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 2,470.0 | 2,100.0 | 20,550.0 | 7,240.0 | 5 | 275 | timer-floor (max is trial 1) | compiled=5 |
| `winpath-near-miss` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 2,410.0 | 2,040.0 | 21,711.0 | 7,735.0 | 5 | 275 | timer-floor (max is trial 1) | compiled=5 |
| `winpath-near-miss` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 6,380.0 | 5,090.0 | 18,980.0 | 5,152.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `winpath-near-miss` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 14,970.0 | 12,690.0 | 55,850.0 | 16,383.5 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `winpath-near-miss` | `plain` | `tre_0.9.0_default-caps-simdna` | 22,330.0 | 19,900.0 | 63,061.0 | 16,468.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `winpath-near-miss` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 23,290.0 | 20,660.0 | 72,161.0 | 19,568.6 | 5 | - | 0.840 (max is trial 1) | compiled=5 |

