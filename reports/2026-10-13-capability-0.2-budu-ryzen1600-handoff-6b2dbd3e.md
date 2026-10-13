# pcrec-bench report

reporter: v26 (2026-10-13)

## Query

- filters: subbench=capability, version=0.2, machine=budu-ryzen1600, since=2026-10-12T00:00:00Z, testee=pcrec_b8337c33_auto-caps-simdna, testee=pcrec_00c97769_auto-caps-simdna, testee=pcrec_6b2dbd3e_auto-caps-simdna
- record source: store/index.tsv (3 record(s) matching this query)
- records included: 3
- worst other-core busy: 19.44% (`pcrec_6b2dbd3e_auto-caps-simdna` / `base10num-near-miss` / `large-subject-throughput`)
    - `capability@0.2__pcrec_00c97769_auto-caps-simdna__budu-ryzen1600__20261012T224439Z` (store/records/capability@0.2/pcrec_00c97769_auto-caps-simdna/capability@0.2__pcrec_00c97769_auto-caps-simdna__budu-ryzen1600__20261012T224439Z.jsonl) — agreement: agree (0 of 138 groups; 0 of 5932 rows; 2 unjudged; k=1.5, 2/3; 5 trials)
    - `capability@0.2__pcrec_6b2dbd3e_auto-caps-simdna__budu-ryzen1600__20261012T233655Z` (store/records/capability@0.2/pcrec_6b2dbd3e_auto-caps-simdna/capability@0.2__pcrec_6b2dbd3e_auto-caps-simdna__budu-ryzen1600__20261012T233655Z.jsonl) — agreement: agree (0 of 138 groups; 0 of 5932 rows; 2 unjudged; k=1.5, 2/3; 5 trials)
    - `capability@0.2__pcrec_b8337c33_auto-caps-simdna__budu-ryzen1600__20261012T215301Z` (store/records/capability@0.2/pcrec_b8337c33_auto-caps-simdna/capability@0.2__pcrec_b8337c33_auto-caps-simdna__budu-ryzen1600__20261012T215301Z.jsonl) — agreement: agree (0 of 138 groups; 1 of 5932 rows; 2 unjudged; k=1.5, 2/3; 5 trials)
- sub-bench version(s): capability@0.2
- machine(s): budu-ryzen1600
- schema version(s): 1.8
- grain: set (sum of per-subject ns/call over the whole subject set, reduced over trials; a set cell is excluded if ANY subject in it fails)
- reduction: median/min/max/stddev (population) over per-trial `elapsed_ns / iterations`; lazy-JIT compile cost is DERIVED as first-match-row-minus-steady-state (lowest `seq` timed row for the pattern, minus the median of every other timed row), one value per (pattern, testee), never pooled with another execution-model class's compile cost
- `form`: this report includes a `whole-subject` artifact beside `plain` for at least one cell (schema v1.1: a testee with no end-anchored mode compiles and times a SEPARATE artifact for match-compliance, e.g. `(?:pattern)\z`, where another testee reaches the same regime via runtime flags on its ordinary artifact) -- shown as a per-row COLUMN, not a split: both forms answer the same regime and RANK TOGETHER in one table (`form` is a key only for compile-cost rows, where a whole-subject artifact is genuinely a separate compile with its own cost); `fact` restates it as 'same program' / 'separate artifact' (R4)
- status policy (OD-B14): a ranking row whose record `status` is not `measured` is excluded from ranking by default, listed under its table as `not ranked: <testee> -- <status> (<status_detail excerpt>)`; `--include-unmeasured` ranks it instead, with `status` shown
- trial-agreement policy (schema v1.4, rule v1.4-group, X31-X33): a record's five trials must agree to within k=1.5 on every group of its rows — one slow trial of five tolerated; two, or one fast, is a disagreeing row; a group disagrees at >= 2 disagreeing rows reaching a third of it (d_min=2, c=3); a record with a disagreeing group, or with fewer than five odd trials, is `inconclusive-spread` and unranked like `inconclusive-load`; the after-run load/occupancy samples are provenance (v1.4 X13), shown under --include-provenance
- status rule: v1.4 X13 (pre-flight + trial agreement) on 3 record(s)
- tier policy (R3, schema v1.2 `tier`, absent = `pinned`): a `scratch`-tier row is excluded from ranking by default, listed as `scratch: <testee>`; `--include-scratch` ranks it instead, with a `tier` column
- duplicate-record policy (OD-B15, amended 2026-08-25): the NEWEST MEASURED record per (subbench@version, testee_id, machine) ranks by default -- a newer record that is NOT measured does not supersede a measured one of the same testee and version (listed as "newer, not measured" instead); only when no record in the group is measured does the newest record overall stand (itself unranked per the status policy above, unless --include-unmeasured). `--all-records` shows every record as its own row, its testee id suffixed `@<timestamp>`

## Null-control band (D119 bar; [B79], inbox I-93 block B / I-104)

- D119 bar (inbox I-93 block B / I-104): a cross-pin cell moved iff |Δ%| > max(IQR%, null band) -- Δ% = (after - before) / before; IQR% = the BEFORE side's Type-7 IQR of its per-trial set sums over the before median; null band = the largest |Δ%| any PROGRAM-IDENTICAL cell of the same (regime, baseline scale) stratum reached across the same pin pair (symmetric); a stratum with fewer than 10 program-identical cells has NO usable band and its verdicts say `IQR only` by name.
- baseline scale: the BEFORE (older pin) set-grain median -- `>=1us` / `100ns-1us` / `<100ns`; strata are per REGIME (I-104).
- sufficiency: a stratum needs >= 10 program-identical cells -- the band is a sample maximum, and one more null cell exceeds the maximum of n with chance 1/(n+1) (<= 9.1% at n = 10).
- identity: the records' own `engine_metadata.program_sha256` ([B88], schema v1.7) where BOTH compile rows of a cell carry it; otherwise OUR OWN census (`tools/program_identity.py`: both pins re-emitted with the pinned binaries under each config's recorded flags, `.c` + `.h` compared after dropping ONLY the generated-by line, the `.abi` integer and one-sided `#define` stamps). Which records carry the field, per side: `pcrec 00c97769 -> 6b2dbd3e`: the BEFORE (`00c97769`) records carry `program_sha256` (138 of 138 compiled cell(s)), the AFTER (`6b2dbd3e`) records carry `program_sha256` (138 of 138 compiled cell(s)); `pcrec b8337c33 -> 00c97769`: the BEFORE (`b8337c33`) records carry `program_sha256` (138 of 138 compiled cell(s)), the AFTER (`00c97769`) records carry `program_sha256` (138 of 138 compiled cell(s)).

### `pcrec 00c97769 -> 6b2dbd3e` (capability@0.2)

- identity from the records ([B88], schema v1.7): 137 cell(s) read `engine_metadata.program_sha256` on BOTH compile rows, 0 fell back to the census; no census for this pair
- cells: 137 cross-pin set cell(s) measured on both sides; 125 program-identical (the null population)

| regime | baseline scale | n null cells | min Δ% | median Δ% | max Δ% | band (±) | status |
|---|---|---|---|---|---|---|---|
| `large-subject-throughput` | `>=1us` | 45 | -0.61% | -0.00% | +1.47% | ±1.47% | ok |
| `large-subject-throughput` | `100ns-1us` | 13 | -1.61% | -0.05% | +0.94% | ±1.61% | ok |
| `large-subject-throughput` | `<100ns` | 4 | -0.14% | +0.04% | +1.78% | n/a | insufficient (n=4 < 10) |
| `short-subject-search` | `>=1us` | 25 | -2.21% | -0.05% | +1.06% | ±2.21% | ok |
| `short-subject-search` | `100ns-1us` | 38 | -1.02% | +0.01% | +1.08% | ±1.08% | ok |
| `short-subject-search` | `<100ns` | 0 | - | - | - | n/a | empty (n=0) |

### `pcrec b8337c33 -> 00c97769` (capability@0.2)

- identity from the records ([B88], schema v1.7): 137 cell(s) read `engine_metadata.program_sha256` on BOTH compile rows, 0 fell back to the census; no census for this pair
- cells: 137 cross-pin set cell(s) measured on both sides; 137 program-identical (the null population)

| regime | baseline scale | n null cells | min Δ% | median Δ% | max Δ% | band (±) | status |
|---|---|---|---|---|---|---|---|
| `large-subject-throughput` | `>=1us` | 51 | -3.16% | -0.02% | +0.72% | ±3.16% | ok |
| `large-subject-throughput` | `100ns-1us` | 13 | -1.75% | -0.03% | +0.47% | ±1.75% | ok |
| `large-subject-throughput` | `<100ns` | 4 | -1.46% | -0.14% | +0.29% | n/a | insufficient (n=4 < 10) |
| `short-subject-search` | `>=1us` | 30 | -0.75% | +0.03% | +2.99% | ±2.99% | ok |
| `short-subject-search` | `100ns-1us` | 39 | -0.99% | +0.03% | +1.80% | ±1.80% | ok |
| `short-subject-search` | `<100ns` | 0 | - | - | - | n/a | empty (n=0) |

## Ranking (per pattern x regime, SET grain: sum over the subject set; best median first)

_D119 bar in this view: |Δ%| > max(IQR%, null band), the `D119 bar` column (definition, strata and bands in the null-control section above). This view's own threshold population: 274 cross-pin cell(s): 5 improve, 2 regress, 5 within the bar, 262 null-control (program identical -- the band's own population); 0 of the verdicts are IQR-only (their stratum's band is not usable)._

### `balanced-parens-rec` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 1,190,324.1 | 0.2543 | 1,186,487.3 | 1,197,200.4 | 3,883.4 | 1.000x | 1.000x | unchanged (within spread) | -0.15% (null control: program identical) |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 1,191,876.4 | 0.2546 | 1,185,193.8 | 1,192,741.6 | 3,189.6 | 1.001x | 1.001x | unchanged (within spread) | +0.13% (null control: program identical) |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 1,192,145.7 | 0.2546 | 1,187,424.6 | 1,204,152.5 | 6,084.7 | 1.002x | 1.002x | - | - |

#### `balanced-parens-rec` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 869,104.5 | 0.8288 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 872,719.2 | 0.8323 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 872,611.0 | 0.8322 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 212,181.5 | 0.8094 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 211,889.8 | 0.8083 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 211,952.0 | 0.8085 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 51,973.6 | 0.7931 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 51,888.1 | 0.7917 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 52,048.9 | 0.7942 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,041.8 | 0.0170 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,037.7 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,037.9 | 0.0169 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 229.1 | 0.0140 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 228.7 | 0.0140 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 226.2 | 0.0138 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 60.8 | 0.0148 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 60.5 | 0.0148 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 60.6 | 0.0148 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,667.9 | 0.0169 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,655.5 | 0.0168 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,670.3 | 0.0169 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,665.7 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,652.6 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,621.8 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 17,660.9 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,656.6 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 17,604.5 | 0.0168 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,038.3 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,037.7 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,043.2 | 0.0170 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 229.5 | 0.0140 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 227.0 | 0.0139 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 227.0 | 0.0139 |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 869,104.5 ns, 1,048,576 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 872,719.2 ns, 1,048,576 B

### `balanced-parens-rec` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 927.2 | 924.2 | 953.9 | 11.2 | 1.000x | 1.000x | unchanged (within spread) | -0.89% (null control: program identical) | 75 | 12.4 | 9.1 | 100% |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 935.5 | 928.6 | 938.4 | 3.3 | 1.009x | 1.009x | - | - | 75 | 12.5 | 9.1 | 100% |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 937.2 | 935.4 | 945.0 | 4.4 | 1.011x | 1.011x | unchanged (within spread) | +1.08% (null control: program identical) | 75 | 12.5 | 9.1 | 100% |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `waf-concat`, 96.1 ns, 48 B; largest Δ: `rec-parens-balanced`, -0.7 ns (now 51.6 ns), 7 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `waf-concat`, 98.2 ns, 48 B

### `base10num-near-miss` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 58.6 | 0.0000 | 58.6 | 58.6 | 0.0 | 1.000x | 1.000x | faster ×1.00 | -0.40% (null control: program identical) |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 58.6 | 0.0000 | 58.6 | 58.7 | 0.1 | 1.000x | 1.000x | unchanged (within spread) | +0.04% (null control: program identical) |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 58.8 | 0.0000 | 58.7 | 59.0 | 0.1 | 1.004x | 1.004x | - | - |

#### `base10num-near-miss` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 5.3 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.3 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 5.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 5.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 5.4 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 5.4 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.3 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 5.4 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 5.3 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.3 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 5.3 | 0.0001 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 5.3 | 0.0003 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.3 | 0.0003 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 5.3 | 0.0003 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 5.3 | 0.0013 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.3 | 0.0013 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 5.3 | 0.0013 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 5.3 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.3 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 5.3 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 5.3 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.3 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 5.3 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 5.3 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.3 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 5.3 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 5.3 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.3 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 5.3 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 5.3 | 0.0003 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.3 | 0.0003 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 5.3 | 0.0003 |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `t-64k`, 5.4 ns, 65,536 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `t-256k`, 5.3 ns, 262,144 B; largest Δ: `t-64k`, -0.0 ns (now 5.3 ns), 65,536 B

### `base10num-near-miss` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 513.9 | 508.7 | 521.0 | 4.6 | 1.000x | 1.000x | - | - | 75 | 6.9 | 9.1 | 100% |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 523.2 | 516.1 | 529.8 | 5.5 | 1.018x | 1.018x | unchanged (within spread) | +1.80% (null control: program identical) | 75 | 7.0 | 9.1 | 100% |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 525.6 | 521.6 | 534.0 | 4.4 | 1.023x | 1.023x | unchanged (within spread) | +0.46% (null control: program identical) | 75 | 7.0 | 9.1 | 100% |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `rd-numeric-id-near-miss`, 36.6 ns, 20 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `rd-numeric-id-near-miss`, 36.5 ns, 20 B; largest Δ: `dt-iso8601`, -1.9 ns (now 11.1 ns), 20 B

### `bracket-array-define` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 300.0 | 0.0001 | 295.0 | 302.0 | 2.5 | 1.000x | 1.000x | faster ×1.02 | -1.75% (null control: program identical) |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 302.8 | 0.0001 | 301.7 | 305.5 | 1.3 | 1.009x | 1.009x | unchanged (within spread) | +0.94% (null control: program identical) |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 305.3 | 0.0001 | 302.5 | 305.7 | 1.3 | 1.018x | 1.018x | - | - |

#### `bracket-array-define` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 27.4 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 27.8 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 27.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 26.1 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 27.8 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 27.8 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 26.8 | 0.0004 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 27.6 | 0.0004 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 27.9 | 0.0004 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 27.8 | 0.0005 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 27.8 | 0.0005 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 27.8 | 0.0005 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 27.7 | 0.0017 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 27.7 | 0.0017 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 27.7 | 0.0017 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 27.7 | 0.0068 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 27.7 | 0.0068 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 27.7 | 0.0068 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 27.7 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 27.7 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 27.7 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 27.7 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 27.8 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 27.8 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 27.2 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 27.7 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 27.7 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 27.6 | 0.0004 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 27.7 | 0.0005 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 27.7 | 0.0005 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 27.8 | 0.0017 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 27.8 | 0.0017 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 27.7 | 0.0017 |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `t-evil-match-60k`, 27.8 ns, 61,440 B; largest Δ: `t-256k`, -1.7 ns (now 26.1 ns), 262,144 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `t-256k`, 27.8 ns, 262,144 B

### `bracket-array-define` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 1,860.1 | 1,857.2 | 1,872.8 | 5.9 | 1.000x | 1.000x | - | - | 75 | 24.8 | 9.1 | 100% |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 1,864.6 | 1,861.7 | 1,869.1 | 2.9 | 1.002x | 1.002x | unchanged (within spread) | +0.24% (null control: program identical) | 75 | 24.9 | 9.1 | 100% |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 1,865.0 | 1,861.4 | 1,872.9 | 4.3 | 1.003x | 1.003x | unchanged (within spread) | +0.02% (null control: program identical) | 75 | 24.9 | 9.1 | 100% |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `rec-array-define`, 85.6 ns, 11 B; largest Δ: `br-doubled-word`, +0.3 ns (now 24.2 ns), 15 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `rec-array-define`, 85.5 ns, 11 B; largest Δ: `sd-empty-alt-miss`, +0.3 ns (now 24.2 ns), 60 B

### `codegrammar-flat` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 661,530.8 | 0.1413 | 651,143.5 | 670,009.0 | 6,615.9 | 1.000x | 1.000x | unchanged (within spread) | -0.61% (null control: program identical) |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 665,584.0 | 0.1422 | 655,567.5 | 677,249.1 | 7,623.6 | 1.006x | 1.006x | unchanged (within spread) | -1.05% (null control: program identical) |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 672,627.8 | 0.1437 | 668,353.7 | 679,557.4 | 3,631.7 | 1.017x | 1.017x | - | - |

#### `codegrammar-flat` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 464,591.3 | 0.4431 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 467,298.0 | 0.4457 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 466,551.7 | 0.4449 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 111,276.5 | 0.4245 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 108,705.1 | 0.4147 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 125,212.7 | 0.4776 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 27,507.5 | 0.4197 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 27,158.6 | 0.4144 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 27,575.4 | 0.4208 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,039.8 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,038.0 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,038.2 | 0.0169 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 229.9 | 0.0140 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 230.3 | 0.0141 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 230.4 | 0.0141 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 61.0 | 0.0149 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 61.0 | 0.0149 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 61.0 | 0.0149 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,654.9 | 0.0168 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,647.6 | 0.0168 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,664.4 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,630.3 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,645.7 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,658.2 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,647.1 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 17,662.9 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 17,659.4 | 0.0168 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,037.3 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,038.6 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,038.9 | 0.0169 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 229.6 | 0.0140 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 227.3 | 0.0139 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 229.0 | 0.0140 |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 464,591.3 ns, 1,048,576 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `t-1m`, 467,298.0 ns, 1,048,576 B; largest Δ: `t-256k`, -16,507.5 ns (now 108,705.1 ns), 262,144 B

### `codegrammar-flat` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 911.5 | 910.1 | 913.2 | 1.0 | 1.000x | 1.000x | - | - | 75 | 12.2 | 9.1 | 100% |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 912.2 | 910.5 | 913.3 | 1.1 | 1.001x | 1.001x | unchanged (within spread) | -0.19% (null control: program identical) | 75 | 12.2 | 9.1 | 100% |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 914.0 | 913.1 | 915.9 | 1.0 | 1.003x | 1.003x | slower ×1.00 | +0.27% (null control: program identical) | 75 | 12.2 | 9.1 | 100% |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `cg-key-colon`, 41.7 ns, 7 B; largest Δ: `rec-comment-nested`, -1.2 ns (now 11.5 ns), 34 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `cg-key-colon`, 41.6 ns, 7 B; largest Δ: `rec-comment-nested`, +0.9 ns (now 12.7 ns), 34 B

### `codegrammar-xflag` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 658,351.1 | 0.1406 | 649,165.3 | 663,020.4 | 5,069.4 | 1.000x | 1.000x | unchanged (within spread) | -0.86% (null control: program identical) |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 664,054.3 | 0.1418 | 656,775.6 | 683,778.7 | 9,337.2 | 1.009x | 1.009x | - | - |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 668,021.5 | 0.1427 | 657,887.4 | 671,701.2 | 4,661.9 | 1.015x | 1.015x | unchanged (within spread) | +1.47% (null control: program identical) |

#### `codegrammar-xflag` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 465,974.7 | 0.4444 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 467,335.2 | 0.4457 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 468,023.9 | 0.4463 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 109,018.6 | 0.4159 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 113,681.6 | 0.4337 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 114,341.1 | 0.4362 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 27,510.8 | 0.4198 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 27,428.8 | 0.4185 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 27,447.3 | 0.4188 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,038.9 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,038.4 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,040.3 | 0.0169 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 230.2 | 0.0140 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 230.3 | 0.0141 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 228.7 | 0.0140 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 61.0 | 0.0149 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 61.0 | 0.0149 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 61.1 | 0.0149 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,673.2 | 0.0169 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,672.3 | 0.0169 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,675.8 | 0.0169 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,657.0 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,652.1 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,628.4 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 17,627.1 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 17,687.0 | 0.0169 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,643.2 | 0.0168 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,039.8 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,039.2 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,039.8 | 0.0169 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 229.4 | 0.0140 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 229.8 | 0.0140 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 227.1 | 0.0139 |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `t-1m`, 465,974.7 ns, 1,048,576 B; largest Δ: `t-256k`, -4,663.0 ns (now 109,018.6 ns), 262,144 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `t-1m`, 468,023.9 ns, 1,048,576 B; largest Δ: `t-256k`, +5,322.5 ns (now 114,341.1 ns), 262,144 B

### `codegrammar-xflag` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 912.0 | 911.6 | 914.9 | 1.2 | 1.000x | 1.000x | unchanged (within spread) | -0.23% (null control: program identical) | 75 | 12.2 | 9.1 | 100% |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 913.0 | 912.2 | 919.8 | 2.8 | 1.001x | 1.001x | unchanged (within spread) | +0.11% (null control: program identical) | 75 | 12.2 | 9.1 | 100% |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 914.2 | 908.1 | 915.0 | 2.5 | 1.002x | 1.002x | - | - | 75 | 12.2 | 9.1 | 100% |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `cg-key-colon`, 41.7 ns, 7 B; largest Δ: `sec-userpass`, -0.6 ns (now 29.6 ns), 33 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `cg-key-colon`, 42.0 ns, 7 B

### `currency-lookbehind-fixed` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 78,583.1 | 0.0168 | 78,539.3 | 78,647.7 | 37.9 | 1.000x | 1.000x | unchanged (within spread) | -0.13% (null control: program identical) |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 78,609.0 | 0.0168 | 78,582.2 | 78,706.9 | 43.6 | 1.000x | 1.000x | - | - |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 78,682.8 | 0.0168 | 78,605.1 | 78,728.5 | 50.8 | 1.001x | 1.001x | unchanged (within spread) | +0.09% (null control: program identical) |

#### `currency-lookbehind-fixed` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,642.5 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 17,647.5 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 17,619.1 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 4,376.1 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 4,378.8 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 4,384.8 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,109.3 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 1,111.5 | 0.0170 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 1,110.6 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,038.1 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,038.2 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,039.0 | 0.0169 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 226.6 | 0.0138 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 226.4 | 0.0138 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 225.6 | 0.0138 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 60.6 | 0.0148 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 60.6 | 0.0148 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 60.6 | 0.0148 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,628.3 | 0.0168 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,636.9 | 0.0168 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,643.5 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,628.7 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,616.1 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,647.0 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,623.3 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 17,617.0 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 17,658.6 | 0.0168 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,038.4 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,037.9 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,039.6 | 0.0169 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 224.7 | 0.0137 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 225.1 | 0.0137 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 224.7 | 0.0137 |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `t-1m`, 17,642.5 ns, 1,048,576 B; largest Δ: `t-tail-txt-1m`, -35.3 ns (now 17,623.3 ns), 1,048,527 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `t-tail-txt-1m`, 17,658.6 ns, 1,048,527 B

### `currency-lookbehind-fixed` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 802.4 | 799.3 | 816.8 | 7.8 | 1.000x | 1.000x | - | - | 75 | 10.7 | 9.1 | 100% |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 812.6 | 802.3 | 816.6 | 5.3 | 1.013x | 1.013x | unchanged (within spread) | +1.28% (null control: program identical) | 75 | 10.8 | 9.1 | 100% |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 815.2 | 813.9 | 816.1 | 0.8 | 1.016x | 1.016x | unchanged (within spread) | +0.33% (null control: program identical) | 75 | 10.9 | 9.1 | 100% |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `la-currency`, 33.4 ns, 10 B; largest Δ: `sd-empty-alt-miss`, +1.2 ns (now 11.8 ns), 60 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `la-currency`, 33.4 ns, 10 B; largest Δ: `la-negation-hit`, +0.7 ns (now 11.3 ns), 19 B

### `date-nested-plus` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 113.8 | 0.0000 | 113.8 | 122.9 | 3.6 | 1.000x | 1.000x | unchanged (within spread) | -0.07% (null control: program identical) |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 113.9 | 0.0000 | 113.8 | 113.9 | 0.0 | 1.000x | 1.000x | - | - |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 113.9 | 0.0000 | 113.8 | 113.9 | 0.0 | 1.001x | 1.001x | unchanged (within spread) | +0.03% (null control: program identical) |

#### `date-nested-plus` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.3 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 10.3 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 10.4 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.4 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 10.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 10.4 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.4 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 10.4 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 10.4 | 0.0002 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.3 | 0.0002 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 10.3 | 0.0002 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 10.4 | 0.0002 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.3 | 0.0006 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 10.3 | 0.0006 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 10.3 | 0.0006 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.3 | 0.0025 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 10.3 | 0.0025 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 10.3 | 0.0025 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.3 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 10.3 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 10.3 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.3 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 10.3 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 10.3 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.3 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 10.3 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 10.3 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.3 | 0.0002 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 10.3 | 0.0002 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 10.3 | 0.0002 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.3 | 0.0006 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 10.3 | 0.0006 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 10.3 | 0.0006 |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `t-64k`, 10.4 ns, 65,536 B; largest Δ: `t-256k`, +0.0 ns (now 10.4 ns), 262,144 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `t-64k`, 10.4 ns, 65,536 B; largest Δ: `t-1m`, +0.0 ns (now 10.4 ns), 1,048,576 B

### `date-nested-plus` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 867.8 | 866.9 | 870.3 | 1.1 | 1.000x | 1.000x | unchanged (within spread) | -0.08% (null control: program identical) | 75 | 11.6 | 9.1 | 100% |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 868.5 | 868.1 | 870.2 | 0.7 | 1.001x | 1.001x | - | - | 75 | 11.6 | 9.1 | 100% |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 868.8 | 867.5 | 869.5 | 0.8 | 1.001x | 1.001x | unchanged (within spread) | +0.11% (null control: program identical) | 75 | 11.6 | 9.1 | 100% |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `rd-numeric-id-near-miss`, 61.7 ns, 20 B; largest Δ: `br-palindrome`, -0.6 ns (now 15.7 ns), 6 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `rd-numeric-id-near-miss`, 61.7 ns, 20 B; largest Δ: `v-ipv4-oor`, +0.3 ns (now 14.3 ns), 9 B

### `doubled-word` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 29,478,431.1 | 6.2967 | 29,464,793.8 | 29,493,850.4 | 10,205.8 | 1.000x | 1.000x | faster ×1.01 | -0.51% vs bar 1.47% (band) → **within** |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 29,628,628.9 | 6.3288 | 29,593,898.0 | 29,637,617.1 | 15,928.0 | 1.005x | 1.005x | unchanged (within spread) | -0.03% (null control: program identical) |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 29,637,984.1 | 6.3308 | 29,615,318.8 | 29,645,965.9 | 10,764.1 | 1.005x | 1.005x | - | - |

#### `doubled-word` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 7,207,978.8 | 6.8741 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 7,300,211.7 | 6.9620 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 7,303,576.7 | 6.9652 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,800,125.1 | 6.8669 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 1,825,291.4 | 6.9629 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 1,826,373.6 | 6.9671 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 448,395.5 | 6.8420 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 454,819.5 | 6.9400 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 455,162.6 | 6.9452 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 190,645.2 | 3.1029 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 173,236.7 | 2.8196 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 173,214.0 | 2.8192 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 50,834.2 | 3.1025 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 46,172.4 | 2.8180 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 46,199.8 | 2.8196 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 24,379.4 | 5.9520 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 23,723.3 | 5.7918 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 24,067.2 | 5.8758 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 6,576,957.5 | 6.2726 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 6,590,907.8 | 6.2859 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 6,594,454.3 | 6.2893 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 6,579,097.9 | 6.2746 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 6,589,610.3 | 6.2847 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 6,594,764.9 | 6.2896 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 6,575,669.7 | 6.2713 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 6,586,415.2 | 6.2816 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 6,590,315.9 | 6.2853 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 21,138.0 | 0.3440 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 21,465.3 | 0.3494 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 21,455.8 | 0.3492 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5,638.5 | 0.3441 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 5,613.4 | 0.3426 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 5,646.6 | 0.3446 |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 7,207,978.8 ns, 1,048,576 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `t-1m`, 7,300,211.7 ns, 1,048,576 B; largest Δ: `t-tail-space-1m`, -5,154.7 ns (now 6,589,610.3 ns), 1,048,522 B

### `doubled-word` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 5,877.6 | 5,858.0 | 5,969.4 | 39.1 | 1.000x | 1.000x | unchanged (within spread) | -0.22% (null control: program identical) | 75 | 78.4 | 9.1 | 100% |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 5,890.5 | 5,876.4 | 5,980.3 | 38.3 | 1.002x | 1.002x | - | - | 75 | 78.5 | 9.1 | 100% |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6,267.7 | 6,236.8 | 6,272.1 | 13.4 | 1.066x | 1.066x | slower ×1.07 | +6.64% vs bar 2.21% (band) → **regress** | 75 | 83.6 | 9.1 | 100% |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `sec-slack-webhook`, 395.6 ns, 81 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `sec-slack-webhook`, 413.2 ns, 81 B; largest Δ: `waf-benign`, +42.3 ns (now 214.2 ns), 39 B

### `dup-param-detect` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 78,546.6 | 0.0168 | 78,535.5 | 78,571.7 | 12.9 | 1.000x | 1.000x | faster ×1.00 | -0.09% (null control: program identical) |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 78,604.9 | 0.0168 | 78,572.9 | 78,632.8 | 19.0 | 1.001x | 1.001x | slower ×1.00 | +0.07% vs bar 1.47% (band) → **within** |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 78,619.3 | 0.0168 | 78,558.3 | 78,632.2 | 33.2 | 1.001x | 1.001x | - | - |

#### `dup-param-detect` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 17,623.0 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,637.7 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 17,635.4 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 4,380.0 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 4,379.4 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 4,380.7 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 1,110.0 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,108.4 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 1,110.1 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,036.1 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,036.4 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,037.4 | 0.0169 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 227.1 | 0.0139 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 227.0 | 0.0139 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 226.9 | 0.0139 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 60.7 | 0.0148 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 60.5 | 0.0148 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 60.8 | 0.0148 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,615.8 | 0.0168 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,639.9 | 0.0168 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,621.0 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,607.4 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,611.0 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,621.3 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 17,630.6 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,631.2 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 17,624.5 | 0.0168 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,037.6 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,037.8 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,036.9 | 0.0169 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 226.9 | 0.0138 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 226.8 | 0.0138 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 226.7 | 0.0138 |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `t-tail-txt-1m`, 17,630.6 ns, 1,048,527 B; largest Δ: `t-tail-space-1m`, -13.9 ns (now 17,607.4 ns), 1,048,522 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `t-tail-digits-1m`, 17,639.9 ns, 1,048,522 B

### `dup-param-detect` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 1,155.4 | 1,153.2 | 1,157.2 | 1.5 | 1.000x | 1.000x | unchanged (within spread) | -0.25% (null control: program identical) | 75 | 15.4 | 9.1 | 100% |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 1,158.3 | 1,157.4 | 1,160.5 | 1.1 | 1.003x | 1.003x | - | - | 75 | 15.4 | 9.1 | 100% |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 1,178.5 | 1,177.6 | 1,180.9 | 1.1 | 1.020x | 1.020x | slower ×1.02 | +2.00% vs bar 2.21% (band) → **within** | 75 | 15.7 | 9.1 | 100% |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `waf-benign`, 357.5 ns, 39 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `waf-benign`, 370.7 ns, 39 B

### `email-local-nodup` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 69,228.2 | 0.0148 | 69,225.9 | 69,288.5 | 23.9 | 1.000x | 1.000x | unchanged (within spread) | -0.06% (null control: program identical) |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 69,234.1 | 0.0148 | 69,216.7 | 69,411.8 | 73.5 | 1.000x | 1.000x | unchanged (within spread) | +0.01% (null control: program identical) |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 69,270.9 | 0.0148 | 69,232.9 | 69,319.6 | 32.0 | 1.001x | 1.001x | - | - |

#### `email-local-nodup` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 19.6 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 20.4 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 20.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 34.3 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 34.7 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 34.8 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 18.9 | 0.0003 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 20.0 | 0.0003 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 18.1 | 0.0003 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 54,459.0 | 0.8864 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 54,454.2 | 0.8863 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 54,472.1 | 0.8866 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 14,562.8 | 0.8888 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 14,564.9 | 0.8889 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 14,565.7 | 0.8890 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 9.5 | 0.0023 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.4 | 0.0023 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 9.5 | 0.0023 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 35.7 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 35.9 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 35.9 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 36.0 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 35.9 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 35.9 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 35.9 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 36.0 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 35.9 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 9.4 | 0.0002 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.6 | 0.0002 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 9.4 | 0.0002 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 9.5 | 0.0006 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.5 | 0.0006 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 9.5 | 0.0006 |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `t-evil-match-60k`, 54,459.0 ns, 61,440 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `t-evil-match-60k`, 54,454.2 ns, 61,440 B

### `email-local-nodup` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 1,456.4 | 1,454.5 | 1,460.2 | 2.0 | 1.000x | 1.000x | - | - | 75 | 19.4 | 9.1 | 100% |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 1,459.0 | 1,457.2 | 1,462.9 | 2.1 | 1.002x | 1.002x | unchanged (within spread) | -0.03% (null control: program identical) | 75 | 19.5 | 9.1 | 100% |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 1,459.5 | 1,456.2 | 1,464.0 | 2.7 | 1.002x | 1.002x | unchanged (within spread) | +0.21% (null control: program identical) | 75 | 19.5 | 9.1 | 100% |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `rd-email-hit`, 73.9 ns, 10 B; largest Δ: `la-float-bound`, +1.2 ns (now 13.3 ns), 13 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `rd-email-hit`, 74.6 ns, 10 B; largest Δ: `sd-dollar-nl`, +1.2 ns (now 15.0 ns), 7 B

### `email-nested-plus` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 1,393.9 | 1,390.9 | 1,401.1 | 4.2 | 1.000x | 1.000x | - | - | 75 | 18.6 | 9.1 | 100% |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 1,403.8 | 1,397.9 | 1,430.3 | 11.7 | 1.007x | 1.007x | unchanged (within spread) | +0.71% (null control: program identical) | 75 | 18.7 | 9.1 | 100% |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 1,406.6 | 1,395.6 | 1,448.5 | 19.1 | 1.009x | 1.009x | unchanged (within spread) | +0.20% (null control: program identical) | 75 | 18.8 | 9.1 | 100% |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `sec-github-pat`, 75.8 ns, 93 B; largest Δ: `rd-evil-alt-hit`, +1.2 ns (now 13.6 ns), 4 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `sec-github-pat`, 76.0 ns, 93 B; largest Δ: `br-doubled-word`, +1.2 ns (now 14.8 ns), 15 B

### `evil-alt-nested` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 95,032.8 | 0.0203 | 94,813.9 | 95,818.8 | 343.4 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 95,420.5 | 0.0204 | 94,936.2 | 97,285.0 | 839.4 | 1.004x | 1.004x | unchanged (within spread) | -0.00% (null control: program identical) |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 95,422.8 | 0.0204 | 95,090.4 | 95,872.7 | 311.2 | 1.004x | 1.004x | unchanged (within spread) | +0.41% (null control: program identical) |

#### `evil-alt-nested` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 14.5 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 14.5 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 14.6 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 9.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.4 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 9.5 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 16.1 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 16.5 | 0.0003 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 17.3 | 0.0003 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 80,399.9 | 1.3086 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 80,781.6 | 1.3148 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 80,787.4 | 1.3149 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 14,536.4 | 0.8872 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 14,534.7 | 0.8871 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 14,647.9 | 0.8940 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 9.3 | 0.0023 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.3 | 0.0023 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 9.3 | 0.0023 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 9.3 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.3 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 9.3 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 9.3 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.3 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 9.3 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 9.3 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.3 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 9.3 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 9.3 | 0.0002 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.3 | 0.0002 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 9.5 | 0.0002 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 9.3 | 0.0006 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.3 | 0.0006 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 9.3 | 0.0006 |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `t-evil-match-60k`, 80,781.6 ns, 61,440 B; largest Δ: `t-evil-nearmiss-16k`, -113.1 ns (now 14,534.7 ns), 16,385 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `t-evil-match-60k`, 80,787.4 ns, 61,440 B

### `evil-alt-nested` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 1,373.9 | 1,371.2 | 1,383.7 | 4.4 | 1.000x | 1.000x | unchanged (within spread) | -0.01% (null control: program identical) | 75 | 18.3 | 9.1 | 100% |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 1,374.1 | 1,372.8 | 1,628.1 | 101.7 | 1.000x | 1.000x | - | - | 75 | 18.3 | 9.1 | 100% |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 1,374.6 | 1,372.7 | 1,379.6 | 2.5 | 1.001x | 1.001x | unchanged (within spread) | +0.05% (null control: program identical) | 75 | 18.3 | 9.1 | 100% |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `sd-empty-alt-miss`, 134.1 ns, 60 B; largest Δ: `rd-email-near-miss`, -0.4 ns (now 65.3 ns), 20 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `sd-empty-alt-miss`, 134.1 ns, 60 B; largest Δ: `cg-constant`, -0.7 ns (now 41.7 ns), 4 B

### `file-ext-order` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 795,742.1 | 0.1700 | 795,673.7 | 796,081.7 | 161.3 | 1.000x | 1.000x | faster ×1.00 | -0.09% (null control: program identical) |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 796,288.5 | 0.1701 | 796,016.0 | 796,667.1 | 226.7 | 1.001x | 1.001x | - | - |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 796,464.0 | 0.1701 | 796,206.5 | 796,897.0 | 227.2 | 1.001x | 1.001x | unchanged (within spread) | +0.02% (null control: program identical) |

#### `file-ext-order` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 202,242.5 | 0.1929 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 202,405.5 | 0.1930 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 202,367.9 | 0.1930 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 44,362.3 | 0.1692 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 44,411.9 | 0.1694 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 44,361.4 | 0.1692 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 8,616.6 | 0.1315 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 8,629.8 | 0.1317 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 8,606.6 | 0.1313 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,035.4 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,036.6 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,035.7 | 0.0169 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 226.1 | 0.0138 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 226.1 | 0.0138 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 227.0 | 0.0139 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 416.1 | 0.1016 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 417.4 | 0.1019 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 416.6 | 0.1017 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 179,243.7 | 0.1709 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 179,360.5 | 0.1711 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 179,352.1 | 0.1711 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 179,242.0 | 0.1709 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 179,310.4 | 0.1710 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 179,389.9 | 0.1711 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 179,216.8 | 0.1709 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 179,223.3 | 0.1709 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 179,411.3 | 0.1711 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,035.9 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,037.3 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,036.0 | 0.0169 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 225.7 | 0.0138 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 225.5 | 0.0138 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 226.5 | 0.0138 |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `t-1m`, 202,242.5 ns, 1,048,576 B; largest Δ: `t-tail-txt-1m`, -194.5 ns (now 179,216.8 ns), 1,048,527 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `t-1m`, 202,367.9 ns, 1,048,576 B; largest Δ: `t-tail-txt-1m`, +188.0 ns (now 179,411.3 ns), 1,048,527 B

### `file-ext-order` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 710.7 | 709.6 | 711.7 | 0.7 | 1.000x | 1.000x | - | - | 75 | 9.5 | 9.1 | 100% |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 711.4 | 709.0 | 713.3 | 1.7 | 1.001x | 1.001x | unchanged (within spread) | +0.09% (null control: program identical) | 75 | 9.5 | 9.1 | 100% |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 711.4 | 708.8 | 712.4 | 1.3 | 1.001x | 1.001x | unchanged (within spread) | +0.01% (null control: program identical) | 75 | 9.5 | 9.1 | 100% |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `sd-fileext-short`, 27.3 ns, 14 B; largest Δ: `lp-atomic-hit`, +0.1 ns (now 12.2 ns), 31 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `sd-fileext-short`, 27.3 ns, 14 B; largest Δ: `waf-dbnames`, +0.1 ns (now 13.5 ns), 39 B

### `float-literal-bound` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 4,055,728.3 | 0.8663 | 4,053,226.4 | 4,082,786.1 | 12,570.3 | 1.000x | 1.000x | unchanged (within spread) | -0.57% (null control: program identical) |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 4,078,865.0 | 0.8713 | 4,032,160.5 | 4,094,861.3 | 21,312.9 | 1.006x | 1.006x | - | - |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 4,088,261.9 | 0.8733 | 4,022,538.5 | 4,100,092.7 | 30,148.2 | 1.008x | 1.008x | unchanged (within spread) | +0.80% (null control: program identical) |

#### `float-literal-bound` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 1,320,370.8 | 1.2592 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 1,330,821.9 | 1.2692 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,329,552.0 | 1.2680 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 329,229.0 | 1.2559 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 325,811.6 | 1.2429 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 324,865.9 | 1.2393 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 80,281.3 | 1.2250 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 77,669.6 | 1.1851 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 77,689.1 | 1.1854 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,037.0 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,038.1 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,037.8 | 0.0169 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 224.1 | 0.0137 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 225.1 | 0.0137 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 222.9 | 0.0136 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 11,727.2 | 2.8631 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 11,696.7 | 2.8556 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 11,697.5 | 2.8558 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 780,748.6 | 0.7446 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 780,862.3 | 0.7447 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 780,753.6 | 0.7446 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 766,950.8 | 0.7315 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 770,679.4 | 0.7350 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 771,702.3 | 0.7360 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 769,187.0 | 0.7336 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 770,252.7 | 0.7346 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 778,918.2 | 0.7429 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,036.8 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,036.6 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,037.6 | 0.0169 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 223.6 | 0.0136 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 222.9 | 0.0136 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 223.6 | 0.0136 |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 1,320,370.8 ns, 1,048,576 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `t-1m`, 1,329,552.0 ns, 1,048,576 B; largest Δ: `t-tail-txt-1m`, +9,731.2 ns (now 778,918.2 ns), 1,048,527 B

### `float-literal-bound` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 907.3 | 903.0 | 918.8 | 5.6 | 1.000x | 1.000x | unchanged (within spread) | -1.02% (null control: program identical) | 75 | 12.1 | 9.1 | 100% |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 914.3 | 910.1 | 955.4 | 17.3 | 1.008x | 1.008x | - | - | 75 | 12.2 | 9.1 | 100% |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 916.6 | 903.4 | 921.1 | 6.2 | 1.010x | 1.010x | unchanged (within spread) | +0.26% (null control: program identical) | 75 | 12.2 | 9.1 | 100% |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `sec-slack-webhook`, 73.1 ns, 81 B; largest Δ: `lp-atomic-hit`, -3.3 ns (now 21.4 ns), 31 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `sec-slack-webhook`, 73.3 ns, 81 B; largest Δ: `lp-winpath`, +1.3 ns (now 22.1 ns), 22 B

### `floor-byte` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 78,599.9 | 0.0168 | 78,544.8 | 78,642.2 | 33.4 | 1.000x | 1.000x | unchanged (within spread) | -0.01% (null control: program identical) |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 78,605.9 | 0.0168 | 78,560.2 | 78,664.1 | 43.8 | 1.000x | 1.000x | unchanged (within spread) | -0.05% (null control: program identical) |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 78,646.3 | 0.0168 | 78,609.0 | 78,793.1 | 65.7 | 1.001x | 1.001x | - | - |

#### `floor-byte` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,632.3 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 17,656.5 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 17,639.8 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 4,376.6 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 4,382.0 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 4,383.1 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,107.4 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 1,109.7 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 1,107.8 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,034.9 | 0.0168 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,034.1 | 0.0168 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,034.4 | 0.0168 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 224.6 | 0.0137 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 225.4 | 0.0138 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 226.1 | 0.0138 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 60.2 | 0.0147 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 59.9 | 0.0146 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 60.4 | 0.0147 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,622.3 | 0.0168 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,624.4 | 0.0168 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,657.4 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,623.2 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,642.8 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,633.5 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,658.1 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 17,616.6 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 17,641.2 | 0.0168 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,035.8 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,037.1 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,037.7 | 0.0169 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 225.2 | 0.0137 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 225.3 | 0.0137 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 225.5 | 0.0138 |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `t-tail-txt-1m`, 17,658.1 ns, 1,048,527 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `t-1m`, 17,656.5 ns, 1,048,576 B; largest Δ: `t-tail-digits-1m`, -33.0 ns (now 17,624.4 ns), 1,048,522 B

### `floor-byte` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 681.0 | 678.0 | 681.9 | 1.4 | 1.000x | 1.000x | unchanged (within spread) | -0.07% (null control: program identical) | 75 | 9.1 | 100% |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 681.4 | 679.4 | 682.5 | 1.0 | 1.001x | 1.001x | - | - | 75 | 9.1 | 100% |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 681.5 | 680.5 | 683.0 | 0.8 | 1.001x | 1.001x | unchanged (within spread) | +0.07% (null control: program identical) | 75 | 9.1 | 100% |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `floor-hit`, 12.6 ns, 1 B; largest Δ: `sec-userpass`, +0.3 ns (now 9.7 ns), 33 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `floor-hit`, 12.6 ns, 1 B; largest Δ: `sd-empty-alt-miss`, +0.3 ns (now 10.0 ns), 60 B

### `hex8-bounded` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 15,109,114.5 | 3.2274 | 15,102,990.3 | 15,137,492.9 | 14,474.9 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 15,128,542.6 | 3.2315 | 15,086,049.8 | 15,159,426.4 | 27,709.9 | 1.001x | 1.001x | unchanged (within spread) | +0.13% (null control: program identical) |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 15,135,053.7 | 3.2329 | 15,075,760.8 | 15,136,359.8 | 23,531.8 | 1.002x | 1.002x | unchanged (within spread) | +0.04% (null control: program identical) |

#### `hex8-bounded` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 3,432,828.8 | 3.2738 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 3,432,605.4 | 3.2736 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 3,431,657.7 | 3.2727 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 854,946.8 | 3.2614 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 854,986.2 | 3.2615 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 854,411.3 | 3.2593 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 208,584.8 | 3.1828 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 208,601.8 | 3.1830 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 207,982.8 | 3.1736 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 114,346.9 | 1.8611 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 114,311.9 | 1.8605 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 114,235.0 | 1.8593 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 30,503.8 | 1.8617 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 30,485.3 | 1.8606 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 30,501.6 | 1.8616 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 12,111.0 | 2.9568 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 12,122.4 | 2.9596 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 12,128.9 | 2.9612 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 3,478,810.1 | 3.3178 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 3,479,336.3 | 3.3183 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 3,484,271.0 | 3.3230 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 3,479,622.2 | 3.3186 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 3,478,913.9 | 3.3179 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 3,486,177.4 | 3.3248 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 3,473,142.4 | 3.3124 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 3,470,118.4 | 3.3095 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 3,480,154.1 | 3.3191 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 21,900.2 | 0.3564 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 21,847.8 | 0.3556 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 21,842.1 | 0.3555 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 5,829.2 | 0.3558 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 5,817.5 | 0.3550 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5,816.7 | 0.3550 |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `t-tail-digits-1m`, 3,479,336.3 ns, 1,048,522 B; largest Δ: `t-tail-txt-1m`, -3,024.0 ns (now 3,470,118.4 ns), 1,048,527 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `t-tail-space-1m`, 3,486,177.4 ns, 1,048,522 B; largest Δ: `t-tail-txt-1m`, +10,035.8 ns (now 3,480,154.1 ns), 1,048,527 B

### `hex8-bounded` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 2,089.6 | 2,086.1 | 2,101.4 | 5.4 | 1.000x | 1.000x | unchanged (within spread) | -0.44% (null control: program identical) | 75 | 27.9 | 9.1 | 100% |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 2,093.3 | 2,091.2 | 2,096.9 | 2.1 | 1.002x | 1.002x | - | - | 75 | 27.9 | 9.1 | 100% |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 2,098.9 | 2,088.5 | 2,103.5 | 5.5 | 1.004x | 1.004x | unchanged (within spread) | +0.27% (null control: program identical) | 75 | 28.0 | 9.1 | 100% |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `sec-github-pat`, 167.1 ns, 93 B; largest Δ: `rec-array-define`, -1.3 ns (now 25.1 ns), 11 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `sec-github-pat`, 167.0 ns, 93 B; largest Δ: `rd-email-hit`, -1.4 ns (now 16.2 ns), 10 B

### `high-byte-run` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 1,642,865.0 | 0.3509 | 1,642,219.5 | 1,643,048.7 | 326.3 | 1.000x | 1.000x | unchanged (within spread) | -0.01% (null control: program identical) |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 1,643,066.8 | 0.3510 | 1,642,479.1 | 1,643,706.0 | 411.2 | 1.000x | 1.000x | - | - |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 1,643,361.7 | 0.3510 | 1,642,742.5 | 1,644,111.3 | 459.8 | 1.000x | 1.000x | unchanged (within spread) | +0.03% (null control: program identical) |

#### `high-byte-run` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 367,962.1 | 0.3509 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 368,040.2 | 0.3510 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 367,966.3 | 0.3509 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 91,805.8 | 0.3502 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 91,880.7 | 0.3505 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 91,905.5 | 0.3506 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 22,952.8 | 0.3502 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 23,009.7 | 0.3511 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 23,151.9 | 0.3533 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 21,464.5 | 0.3494 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 21,522.7 | 0.3503 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 21,539.2 | 0.3506 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 5,729.1 | 0.3497 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 5,752.4 | 0.3511 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5,764.1 | 0.3518 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 1,441.9 | 0.3520 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 1,452.8 | 0.3547 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,453.0 | 0.3547 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 368,040.3 | 0.3510 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 368,000.1 | 0.3510 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 368,017.9 | 0.3510 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 367,930.2 | 0.3509 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 367,987.2 | 0.3510 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 368,029.7 | 0.3510 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 367,867.9 | 0.3508 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 368,035.2 | 0.3510 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 368,024.2 | 0.3510 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 21,533.9 | 0.3505 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 21,548.9 | 0.3507 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 21,548.6 | 0.3507 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 5,740.5 | 0.3503 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 5,761.6 | 0.3516 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5,758.6 | 0.3515 |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `t-tail-digits-1m`, 368,040.3 ns, 1,048,522 B; largest Δ: `t-tail-txt-1m`, -167.3 ns (now 367,867.9 ns), 1,048,527 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `t-tail-space-1m`, 368,029.7 ns, 1,048,522 B; largest Δ: `t-64k`, +199.1 ns (now 23,151.9 ns), 65,536 B

### `high-byte-run` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 1,114.1 | 1,113.0 | 1,115.3 | 0.7 | 1.000x | 1.000x | - | - | 75 | 14.9 | 9.1 | 100% |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 1,117.4 | 1,115.5 | 1,123.5 | 2.8 | 1.003x | 1.003x | unchanged (within spread) | +0.29% (null control: program identical) | 75 | 14.9 | 9.1 | 100% |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 1,119.5 | 1,114.3 | 1,127.9 | 4.6 | 1.005x | 1.005x | unchanged (within spread) | +0.19% (null control: program identical) | 75 | 14.9 | 9.1 | 100% |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `sec-github-pat`, 52.2 ns, 93 B; largest Δ: `rec-array-define`, +0.4 ns (now 10.7 ns), 11 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `sec-github-pat`, 52.0 ns, 93 B; largest Δ: `nu-lead-with-cont`, +0.6 ns (now 11.4 ns), 2 B

### `ipv4-near-miss` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 55.3 | 0.0000 | 55.1 | 55.4 | 0.1 | 1.000x | 1.000x | unchanged (within spread) | -0.14% (null control: program identical) |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 55.3 | 0.0000 | 55.3 | 55.4 | 0.0 | 1.000x | 1.000x | - | - |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 55.4 | 0.0000 | 55.4 | 195.1 | 55.9 | 1.001x | 1.001x | unchanged (within spread) | +0.13% (null control: program identical) |

#### `ipv4-near-miss` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 5.1 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.1 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 5.1 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 5.1 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.0 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 5.0 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 5.0 | 0.0001 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.0 | 0.0003 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 5.0 | 0.0003 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 5.0 | 0.0003 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.0 | 0.0012 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 5.0 | 0.0012 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 5.0 | 0.0012 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.0 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 5.0 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 5.0 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.0 | 0.0003 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 5.0 | 0.0003 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 5.0 | 0.0003 |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `t-64k`, 5.1 ns, 65,536 B; largest Δ: `t-256k`, -0.0 ns (now 5.0 ns), 262,144 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `t-64k`, 5.1 ns, 65,536 B; largest Δ: `t-256k`, +0.0 ns (now 5.1 ns), 262,144 B

### `ipv4-near-miss` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 427.2 | 426.5 | 428.2 | 0.6 | 1.000x | 1.000x | unchanged (within spread) | -0.32% (null control: program identical) | 75 | 5.7 | 9.1 | 100% |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 428.6 | 426.5 | 429.1 | 0.9 | 1.003x | 1.003x | - | - | 75 | 5.7 | 9.1 | 100% |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 429.3 | 426.0 | 431.8 | 2.1 | 1.005x | 1.005x | unchanged (within spread) | +0.49% (null control: program identical) | 75 | 5.7 | 9.1 | 100% |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `v-ipv4`, 15.9 ns, 11 B; largest Δ: `br-palindrome`, -0.8 ns (now 8.7 ns), 6 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `v-ipv4`, 15.8 ns, 11 B; largest Δ: `br-palindrome`, -0.4 ns (now 8.3 ns), 6 B

### `keyword-prefix-order` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 2,280,204.1 | 0.4871 | 2,249,505.4 | 2,284,923.9 | 15,391.1 | 1.000x | 1.000x | unchanged (within spread) | -0.10% (null control: program identical) |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 2,280,878.2 | 0.4872 | 2,272,949.4 | 2,282,846.4 | 3,625.3 | 1.000x | 1.000x | - | - |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 2,282,530.6 | 0.4876 | 2,280,603.2 | 2,284,642.4 | 1,702.0 | 1.001x | 1.001x | unchanged (within spread) | +0.07% (null control: program identical) |

#### `keyword-prefix-order` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 537,752.3 | 0.5128 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 537,899.4 | 0.5130 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 538,071.0 | 0.5131 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 126,138.6 | 0.4812 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 128,537.8 | 0.4903 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 128,241.3 | 0.4892 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 28,612.2 | 0.4366 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 29,096.1 | 0.4440 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 29,067.2 | 0.4435 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 23,368.0 | 0.3803 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 23,357.7 | 0.3802 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 23,291.5 | 0.3791 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5,606.5 | 0.3422 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 5,617.9 | 0.3429 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 5,646.4 | 0.3446 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 311.3 | 0.0760 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 316.9 | 0.0774 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 317.5 | 0.0775 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 518,612.7 | 0.4946 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 518,320.8 | 0.4943 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 519,165.4 | 0.4951 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 518,856.0 | 0.4948 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 518,710.8 | 0.4947 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 518,832.0 | 0.4948 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 518,745.3 | 0.4947 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 517,705.7 | 0.4937 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 518,853.9 | 0.4948 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,035.8 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,038.8 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,038.8 | 0.0169 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 225.4 | 0.0138 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 225.3 | 0.0137 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 226.0 | 0.0138 |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `t-1m`, 537,752.3 ns, 1,048,576 B; largest Δ: `t-256k`, -2,102.7 ns (now 126,138.6 ns), 262,144 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `t-1m`, 538,071.0 ns, 1,048,576 B; largest Δ: `t-tail-txt-1m`, +1,148.2 ns (now 518,853.9 ns), 1,048,527 B

### `keyword-prefix-order` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 783.8 | 783.6 | 788.4 | 1.8 | 1.000x | 1.000x | unchanged (within spread) | -0.08% (null control: program identical) | 75 | 10.5 | 9.1 | 100% |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 784.5 | 784.0 | 785.6 | 0.5 | 1.001x | 1.001x | - | - | 75 | 10.5 | 9.1 | 100% |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 785.3 | 783.5 | 791.4 | 3.2 | 1.002x | 1.002x | unchanged (within spread) | +0.19% (null control: program identical) | 75 | 10.5 | 9.1 | 100% |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `br-quoted-delim`, 19.7 ns, 15 B; largest Δ: `lp-quoted-escaped`, +0.3 ns (now 12.8 ns), 16 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `br-tag-mismatch`, 19.6 ns, 19 B; largest Δ: `sd-empty-alt-miss`, +0.8 ns (now 10.6 ns), 60 B

### `letters-bounded-tail-z` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 781.9 | 0.0002 | 779.5 | 786.6 | 2.7 | 1.000x | 1.000x | unchanged (within spread) | -0.05% (null control: program identical) |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 782.0 | 0.0002 | 779.9 | 787.1 | 2.5 | 1.000x | 1.000x | - | - |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 782.3 | 0.0002 | 780.4 | 795.5 | 5.5 | 1.000x | 1.000x | unchanged (within spread) | +0.04% (null control: program identical) |

#### `letters-bounded-tail-z` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 12.8 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 12.7 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 12.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 12.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 12.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 12.7 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 12.8 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 12.8 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 12.7 | 0.0002 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 631.0 | 0.0103 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 631.8 | 0.0103 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 632.6 | 0.0103 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 13.3 | 0.0008 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 13.4 | 0.0008 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 12.9 | 0.0008 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 19.0 | 0.0046 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 19.1 | 0.0047 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 18.8 | 0.0046 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 12.8 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 12.8 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 12.9 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 12.7 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 12.7 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 12.7 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 22.2 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 22.2 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 22.6 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 12.8 | 0.0002 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 13.1 | 0.0002 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 12.8 | 0.0002 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 19.0 | 0.0012 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 18.7 | 0.0011 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 18.9 | 0.0012 |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `t-evil-match-60k`, 631.0 ns, 61,440 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `t-evil-match-60k`, 632.6 ns, 61,440 B

### `letters-bounded-tail-z` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 950.6 | 948.6 | 957.0 | 3.2 | 1.000x | 1.000x | - | - | 75 | 12.7 | 9.1 | 100% |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 954.6 | 945.5 | 957.2 | 4.0 | 1.004x | 1.004x | unchanged (within spread) | -0.27% (null control: program identical) | 75 | 12.7 | 9.1 | 100% |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 957.2 | 952.8 | 962.5 | 3.3 | 1.007x | 1.007x | slower ×1.01 | +0.69% (null control: program identical) | 75 | 12.8 | 9.1 | 100% |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `sd-empty-alt-miss`, 52.4 ns, 60 B; largest Δ: `la-float-bound`, -0.8 ns (now 14.5 ns), 13 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `sd-empty-alt-miss`, 52.3 ns, 60 B; largest Δ: `rd-evil-alt-hit`, +1.0 ns (now 14.8 ns), 4 B

### `logparse-atomic` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 120.0 | 0.0000 | 119.8 | 122.1 | 0.8 | 1.000x | 1.000x | unchanged (within spread) | -1.61% (null control: program identical) |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 121.4 | 0.0000 | 120.7 | 122.2 | 0.7 | 1.012x | 1.012x | - | - |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 122.0 | 0.0000 | 119.8 | 122.2 | 1.1 | 1.016x | 1.016x | unchanged (within spread) | +0.47% (null control: program identical) |

#### `logparse-atomic` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.7 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 10.7 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 10.6 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 10.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 10.7 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 11.6 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 11.6 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 11.6 | 0.0002 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 11.9 | 0.0002 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 12.7 | 0.0002 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 12.7 | 0.0002 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 11.5 | 0.0007 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 12.2 | 0.0007 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 12.7 | 0.0008 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.6 | 0.0026 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 10.6 | 0.0026 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 10.6 | 0.0026 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.6 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 10.6 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 10.6 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.6 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 10.6 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 10.6 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.6 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 10.6 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 10.6 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.6 | 0.0002 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 10.6 | 0.0002 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 10.6 | 0.0002 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.6 | 0.0006 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 10.7 | 0.0007 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 10.6 | 0.0006 |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `t-evil-match-60k`, 11.9 ns, 61,440 B; largest Δ: `t-evil-nearmiss-16k`, -1.2 ns (now 11.5 ns), 16,385 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `t-evil-match-60k`, 12.7 ns, 61,440 B; largest Δ: `t-evil-nearmiss-16k`, +0.4 ns (now 12.7 ns), 16,385 B

### `logparse-atomic` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 867.7 | 867.3 | 869.1 | 0.7 | 1.000x | 1.000x | unchanged (within spread) | -0.55% (null control: program identical) | 75 | 11.6 | 9.1 | 100% |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 868.2 | 867.9 | 869.8 | 0.7 | 1.001x | 1.001x | - | - | 75 | 11.6 | 9.1 | 100% |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 872.5 | 868.2 | 887.6 | 6.7 | 1.006x | 1.006x | unchanged (within spread) | +0.49% (null control: program identical) | 75 | 11.6 | 9.1 | 100% |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `lp-atomic-hit`, 63.7 ns, 31 B; largest Δ: `rd-email-near-miss`, -0.8 ns (now 11.2 ns), 20 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `lp-atomic-hit`, 64.2 ns, 31 B; largest Δ: `rd-email-near-miss`, +0.8 ns (now 12.0 ns), 20 B

### `logparse-atomic-removed` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 119.5 | 0.0000 | 119.4 | 119.8 | 0.1 | 1.000x | 1.000x | unchanged (within spread) | -0.17% (null control: program identical) |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 119.6 | 0.0000 | 119.5 | 120.3 | 0.3 | 1.001x | 1.001x | unchanged (within spread) | +0.08% (null control: program identical) |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 119.7 | 0.0000 | 119.3 | 120.0 | 0.2 | 1.002x | 1.002x | - | - |

#### `logparse-atomic-removed` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 10.6 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.6 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 10.6 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 10.6 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.6 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 10.7 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 11.6 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 11.6 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 11.6 | 0.0002 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 11.5 | 0.0002 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 11.5 | 0.0002 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 11.6 | 0.0002 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 11.5 | 0.0007 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 11.5 | 0.0007 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 11.5 | 0.0007 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 10.6 | 0.0026 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.6 | 0.0026 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 10.6 | 0.0026 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 10.6 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.6 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 10.6 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 10.6 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.6 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 10.6 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 10.6 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.6 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 10.6 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 10.6 | 0.0002 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.6 | 0.0002 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 10.6 | 0.0002 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 10.6 | 0.0006 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.6 | 0.0006 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 10.6 | 0.0006 |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `t-64k`, 11.6 ns, 65,536 B; largest Δ: `t-256k`, -0.1 ns (now 10.6 ns), 262,144 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `t-64k`, 11.6 ns, 65,536 B; largest Δ: `t-tail-digits-1m`, -0.0 ns (now 10.6 ns), 1,048,522 B

### `logparse-atomic-removed` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 843.8 | 843.2 | 852.1 | 3.3 | 1.000x | 1.000x | unchanged (within spread) | -0.78% (null control: program identical) | 75 | 11.3 | 9.1 | 100% |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 844.6 | 843.6 | 846.0 | 0.9 | 1.001x | 1.001x | - | - | 75 | 11.3 | 9.1 | 100% |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 850.5 | 843.4 | 865.2 | 7.7 | 1.008x | 1.008x | unchanged (within spread) | +0.70% (null control: program identical) | 75 | 11.3 | 9.1 | 100% |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `lp-atomic-hit`, 61.2 ns, 31 B; largest Δ: `lp-atomic-nonmatch`, -0.1 ns (now 13.0 ns), 23 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `lp-atomic-hit`, 61.1 ns, 31 B

### `mojibake-curly-quote` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 78,574.1 | 0.0168 | 78,549.1 | 78,619.9 | 26.3 | 1.000x | 1.000x | unchanged (within spread) | -0.06% (null control: program identical) |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 78,574.5 | 0.0168 | 78,514.5 | 78,585.6 | 25.5 | 1.000x | 1.000x | - | - |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 78,617.4 | 0.0168 | 78,564.7 | 78,763.8 | 73.0 | 1.001x | 1.001x | unchanged (within spread) | +0.05% (null control: program identical) |

#### `mojibake-curly-quote` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,636.9 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 17,625.2 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 17,628.1 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 4,381.0 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 4,389.0 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 4,378.8 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,108.0 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 1,107.6 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 1,106.9 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,036.5 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,035.7 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,034.9 | 0.0168 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 225.7 | 0.0138 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 225.4 | 0.0138 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 225.1 | 0.0137 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 59.3 | 0.0145 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 58.8 | 0.0144 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 59.0 | 0.0144 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,639.8 | 0.0168 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,612.4 | 0.0168 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,628.7 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,607.4 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,608.2 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,627.9 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,633.0 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 17,626.7 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 17,637.7 | 0.0168 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,035.6 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,036.6 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,036.4 | 0.0169 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 227.2 | 0.0139 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 224.7 | 0.0137 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 225.4 | 0.0138 |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `t-tail-digits-1m`, 17,639.8 ns, 1,048,522 B; largest Δ: `t-tail-space-1m`, -20.5 ns (now 17,607.4 ns), 1,048,522 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `t-tail-txt-1m`, 17,637.7 ns, 1,048,527 B; largest Δ: `t-tail-space-1m`, +19.7 ns (now 17,627.9 ns), 1,048,522 B

### `mojibake-curly-quote` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 701.7 | 701.6 | 701.9 | 0.1 | 1.000x | 1.000x | unchanged (within spread) | -0.02% (null control: program identical) | 75 | 9.4 | 9.1 | 100% |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 701.9 | 701.7 | 702.3 | 0.2 | 1.000x | 1.000x | - | - | 75 | 9.4 | 9.1 | 100% |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 701.9 | 701.6 | 702.0 | 0.1 | 1.000x | 1.000x | unchanged (within spread) | +0.03% (null control: program identical) | 75 | 9.4 | 9.1 | 100% |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `nu-mojibake`, 36.3 ns, 7 B; largest Δ: `nu-lead-no-cont`, -0.1 ns (now 8.9 ns), 2 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `nu-mojibake`, 36.4 ns, 7 B

### `nested-comment-rec` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 78,547.9 | 0.0168 | 78,515.9 | 78,572.4 | 18.0 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 78,559.1 | 0.0168 | 78,482.8 | 78,625.7 | 50.7 | 1.000x | 1.000x | unchanged (within spread) | -0.11% (null control: program identical) |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 78,648.4 | 0.0168 | 78,571.2 | 78,845.3 | 92.8 | 1.001x | 1.001x | unchanged (within spread) | +0.13% (null control: program identical) |

#### `nested-comment-rec` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 17,613.3 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,609.6 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 17,618.7 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 4,374.2 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 4,382.7 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 4,379.1 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 1,108.1 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,108.8 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 1,109.4 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,036.7 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,037.5 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,036.9 | 0.0169 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 226.7 | 0.0138 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 226.8 | 0.0138 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 227.7 | 0.0139 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 60.8 | 0.0148 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 60.8 | 0.0149 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 60.8 | 0.0148 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,655.9 | 0.0168 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,624.5 | 0.0168 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,623.1 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,600.7 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,631.0 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,683.3 | 0.0169 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 17,602.9 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,612.7 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 17,636.6 | 0.0168 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,036.5 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,036.5 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,036.9 | 0.0169 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 227.1 | 0.0139 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 227.0 | 0.0139 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 227.2 | 0.0139 |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `t-tail-space-1m`, 17,631.0 ns, 1,048,522 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `t-tail-space-1m`, 17,683.3 ns, 1,048,522 B

### `nested-comment-rec` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 1,489.2 | 1,480.1 | 1,542.8 | 23.8 | 1.000x | 1.000x | - | - | 75 | 19.9 | 9.1 | 100% |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 1,499.8 | 1,478.8 | 1,537.6 | 21.0 | 1.007x | 1.007x | unchanged (within spread) | -2.21% (null control: program identical) | 75 | 20.0 | 9.1 | 100% |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 1,533.7 | 1,493.8 | 1,560.9 | 23.1 | 1.030x | 1.030x | unchanged (within spread) | +2.99% (null control: program identical) | 75 | 20.4 | 9.1 | 100% |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `rec-comment-nested`, 637.9 ns, 34 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `rec-comment-nested`, 677.0 ns, 34 B

### `numeric-id-nested-plus` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 109.7 | 0.0000 | 109.2 | 110.2 | 0.3 | 1.000x | 1.000x | unchanged (within spread) | -0.17% (null control: program identical) |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 109.9 | 0.0000 | 109.5 | 110.1 | 0.2 | 1.002x | 1.002x | - | - |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 109.9 | 0.0000 | 109.6 | 110.4 | 0.3 | 1.002x | 1.002x | unchanged (within spread) | +0.22% (null control: program identical) |

#### `numeric-id-nested-plus` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 10.0 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 10.0 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 10.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 10.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.0 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 10.0 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 10.0 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.0 | 0.0002 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 10.0 | 0.0002 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 10.0 | 0.0002 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.0 | 0.0002 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 9.9 | 0.0006 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 10.0 | 0.0006 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.9 | 0.0006 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 10.0 | 0.0024 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 9.9 | 0.0024 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.9 | 0.0024 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 10.0 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 9.9 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.0 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 10.0 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 10.0 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.9 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 10.0 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 10.0 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.0 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 10.0 | 0.0002 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 10.0 | 0.0002 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.0 | 0.0002 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 10.0 | 0.0006 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 10.0 | 0.0006 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.0 | 0.0006 |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `t-64k`, 10.0 ns, 65,536 B; largest Δ: `t-tail-digits-1m`, +0.1 ns (now 10.0 ns), 1,048,522 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `t-64k`, 10.0 ns, 65,536 B; largest Δ: `t-tail-txt-1m`, +0.0 ns (now 10.0 ns), 1,048,527 B

### `numeric-id-nested-plus` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 876.4 | 864.2 | 879.6 | 5.6 | 1.000x | 1.000x | - | - | 75 | 11.7 | 9.1 | 100% |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 880.1 | 864.2 | 882.0 | 6.6 | 1.004x | 1.004x | unchanged (within spread) | +0.42% (null control: program identical) | 75 | 11.7 | 9.1 | 100% |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 882.2 | 878.3 | 883.8 | 2.1 | 1.007x | 1.007x | unchanged (within spread) | +0.24% (null control: program identical) | 75 | 11.8 | 9.1 | 100% |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `rd-numeric-id-near-miss`, 36.7 ns, 20 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `rd-numeric-id-near-miss`, 38.0 ns, 20 B

### `phone-list-nested-plus` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 109.1 | 0.0000 | 109.0 | 110.1 | 0.4 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 109.3 | 0.0000 | 109.1 | 110.8 | 0.6 | 1.001x | 1.001x | unchanged (within spread) | -0.07% (null control: program identical) |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 109.3 | 0.0000 | 109.1 | 109.9 | 0.3 | 1.002x | 1.002x | unchanged (within spread) | +0.19% (null control: program identical) |

#### `phone-list-nested-plus` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 9.9 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.9 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 9.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 9.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 9.9 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 10.0 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.0 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 10.0 | 0.0002 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 9.9 | 0.0002 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.9 | 0.0002 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 9.9 | 0.0002 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 9.9 | 0.0006 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.9 | 0.0006 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 9.9 | 0.0006 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 9.9 | 0.0024 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.9 | 0.0024 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 9.9 | 0.0024 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 9.9 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.9 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 9.9 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 9.9 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.9 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 9.9 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 9.9 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.9 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 9.9 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 9.9 | 0.0002 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.9 | 0.0002 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 9.9 | 0.0002 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 9.9 | 0.0006 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.9 | 0.0006 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 9.9 | 0.0006 |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `t-64k`, 10.0 ns, 65,536 B; largest Δ: `t-trim-match-60k`, -0.0 ns (now 9.9 ns), 61,440 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `t-64k`, 10.0 ns, 65,536 B

### `phone-list-nested-plus` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 895.1 | 894.8 | 899.7 | 1.9 | 1.000x | 1.000x | unchanged (within spread) | -0.08% (null control: program identical) | 75 | 11.9 | 9.1 | 100% |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 895.3 | 893.0 | 897.7 | 1.5 | 1.000x | 1.000x | unchanged (within spread) | +0.01% (null control: program identical) | 75 | 11.9 | 9.1 | 100% |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 895.9 | 893.0 | 901.2 | 2.7 | 1.001x | 1.001x | - | - | 75 | 11.9 | 9.1 | 100% |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `rd-phone-list-hit`, 44.1 ns, 7 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `rd-phone-list-hit`, 42.8 ns, 7 B

### `phone-palindrome-6` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 7,531,011.2 | 1.6086 | 7,491,365.4 | 8,019,192.1 | 200,166.1 | 1.000x | 1.000x | faster ×1.14 | -12.16% vs bar 7.72% (IQR) → **improve** |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 8,511,750.8 | 1.8181 | 8,504,084.4 | 8,518,963.8 | 5,198.2 | 1.130x | 1.130x | - | - |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 8,573,221.2 | 1.8313 | 8,489,112.8 | 9,274,656.9 | 345,674.6 | 1.138x | 1.138x | unchanged (within spread) | +0.72% (null control: program identical) |

#### `phone-palindrome-6` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 2,027,081.1 | 1.9332 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 2,177,615.2 | 2.0767 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 2,266,702.7 | 2.1617 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 488,847.6 | 1.8648 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 527,646.8 | 2.0128 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 544,806.3 | 2.0783 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 117,227.8 | 1.7888 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 127,244.3 | 1.9416 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 130,866.2 | 1.9969 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 21,000.3 | 0.3418 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 22,721.9 | 0.3698 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 22,183.6 | 0.3611 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5,599.4 | 0.3417 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 5,936.9 | 0.3623 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 5,921.3 | 0.3614 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 27,142.2 | 6.6265 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 30,670.5 | 7.4879 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 30,632.1 | 7.4785 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,612,007.2 | 1.5374 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 1,867,125.1 | 1.7807 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 1,868,990.0 | 1.7825 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,600,911.3 | 1.5268 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 1,863,117.7 | 1.7769 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 1,854,779.6 | 1.7689 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,605,351.0 | 1.5311 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 1,863,163.2 | 1.7769 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 1,847,178.5 | 1.7617 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 21,004.1 | 0.3419 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 22,177.3 | 0.3610 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 22,209.3 | 0.3615 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5,609.8 | 0.3424 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 5,923.7 | 0.3615 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 5,927.1 | 0.3617 |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `t-1m`, 2,027,081.1 ns, 1,048,576 B; largest Δ: `t-tail-digits-1m`, -256,982.8 ns (now 1,612,007.2 ns), 1,048,522 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 2,266,702.7 ns, 1,048,576 B

### `phone-palindrome-6` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 2,553.4 | 2,550.3 | 2,675.5 | 49.1 | 1.000x | 1.000x | faster ×1.13 | -11.48% vs bar 2.21% (band) → **improve** | 75 | 34.0 | 9.1 | 100% |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 2,884.6 | 2,878.6 | 2,897.7 | 7.5 | 1.130x | 1.130x | unchanged (within spread) | -0.46% (null control: program identical) | 75 | 38.5 | 9.1 | 100% |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 2,897.9 | 2,869.0 | 2,945.6 | 27.2 | 1.135x | 1.135x | - | - | 75 | 38.6 | 9.1 | 100% |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `sec-slack-webhook`, 263.7 ns, 81 B; largest Δ: `v-uuid-badnibble`, -35.4 ns (now 208.0 ns), 36 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `sec-slack-webhook`, 297.8 ns, 81 B; largest Δ: `waf-comment-obfuscation`, -17.9 ns (now 81.8 ns), 18 B

### `pwd-strength-chain` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 533,759.1 | 0.1140 | 533,382.9 | 535,693.7 | 820.8 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 533,788.3 | 0.1140 | 533,047.3 | 534,193.3 | 395.7 | 1.000x | 1.000x | unchanged (within spread) | +0.01% (null control: program identical) |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 533,790.7 | 0.1140 | 533,710.5 | 534,065.5 | 128.7 | 1.000x | 1.000x | unchanged (within spread) | +0.00% (null control: program identical) |

#### `pwd-strength-chain` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 59.1 | 0.0001 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 58.9 | 0.0001 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 58.7 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 95.8 | 0.0004 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 95.8 | 0.0004 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 96.0 | 0.0004 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 69.3 | 0.0011 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 69.4 | 0.0011 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 69.3 | 0.0011 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 399,854.0 | 6.5080 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 399,872.8 | 6.5083 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 399,887.9 | 6.5086 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 106,671.7 | 6.5103 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 106,673.5 | 6.5104 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 106,673.3 | 6.5104 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 26,716.9 | 6.5227 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 26,716.8 | 6.5227 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 26,717.3 | 6.5228 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 89.2 | 0.0001 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 90.0 | 0.0001 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 89.2 | 0.0001 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 88.9 | 0.0001 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 89.9 | 0.0001 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 89.0 | 0.0001 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 88.8 | 0.0001 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 90.1 | 0.0001 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 89.1 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 15.6 | 0.0003 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 14.9 | 0.0002 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 15.4 | 0.0003 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 15.5 | 0.0009 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 14.8 | 0.0009 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 15.6 | 0.0010 |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `t-evil-match-60k`, 399,872.8 ns, 61,440 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `t-evil-match-60k`, 399,887.9 ns, 61,440 B

### `pwd-strength-chain` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 12,094.5 | 12,085.3 | 12,168.1 | 30.7 | 1.000x | 1.000x | - | - | 75 | 161.3 | 9.1 | 100% |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 12,102.3 | 12,069.0 | 12,438.3 | 139.1 | 1.001x | 1.001x | unchanged (within spread) | -0.09% (null control: program identical) | 75 | 161.4 | 9.1 | 100% |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 12,113.7 | 12,082.8 | 12,122.2 | 16.9 | 1.002x | 1.002x | unchanged (within spread) | +0.16% (null control: program identical) | 75 | 161.5 | 9.1 | 100% |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `sec-github-pat`, 919.6 ns, 93 B; largest Δ: `waf-union`, +3.2 ns (now 584.2 ns), 43 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `sec-github-pat`, 921.2 ns, 93 B; largest Δ: `waf-dbnames`, +2.6 ns (now 460.2 ns), 39 B

### `quoted-delim-match` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 2,182,500.8 | 0.4662 | 2,182,236.9 | 2,183,534.6 | 568.6 | 1.000x | 1.000x | faster ×1.02 | -2.25% vs bar 1.47% (band) → **improve** |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 2,232,624.1 | 0.4769 | 2,229,840.1 | 2,237,025.0 | 2,435.8 | 1.023x | 1.023x | unchanged (within spread) | -0.14% (null control: program identical) |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 2,235,778.9 | 0.4776 | 2,230,529.8 | 2,241,296.2 | 3,533.7 | 1.024x | 1.024x | - | - |

#### `quoted-delim-match` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 756,964.6 | 0.7219 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 794,958.4 | 0.7581 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 798,237.2 | 0.7613 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 184,807.0 | 0.7050 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 193,918.1 | 0.7397 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 193,182.6 | 0.7369 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 46,504.5 | 0.7096 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 48,745.3 | 0.7438 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 48,764.5 | 0.7441 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 22,175.3 | 0.3609 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 22,193.2 | 0.3612 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 22,191.1 | 0.3612 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5,926.6 | 0.3617 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 5,928.2 | 0.3618 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 5,931.3 | 0.3620 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,496.4 | 0.3653 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 1,500.3 | 0.3663 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 1,499.7 | 0.3661 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 378,799.6 | 0.3613 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 378,889.4 | 0.3614 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 378,875.4 | 0.3613 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 378,841.7 | 0.3613 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 378,934.4 | 0.3614 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 378,832.5 | 0.3613 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 378,869.7 | 0.3613 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 378,922.8 | 0.3614 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 378,833.6 | 0.3613 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 22,174.2 | 0.3609 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 22,203.1 | 0.3614 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 22,199.2 | 0.3613 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5,928.3 | 0.3618 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 5,948.0 | 0.3630 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 5,932.2 | 0.3621 |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 756,964.6 ns, 1,048,576 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 794,958.4 ns, 1,048,576 B

### `quoted-delim-match` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 1,997.1 | 1,990.1 | 2,003.2 | 4.4 | 1.000x | 1.000x | faster ×1.03 | -2.59% vs bar 2.21% (band) → **improve** | 75 | 26.6 | 9.1 | 100% |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 2,050.2 | 2,046.8 | 2,064.6 | 6.6 | 1.027x | 1.027x | faster ×1.01 | -0.75% (null control: program identical) | 75 | 27.3 | 9.1 | 100% |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 2,065.8 | 2,058.1 | 2,070.0 | 4.1 | 1.034x | 1.034x | - | - | 75 | 27.5 | 9.1 | 100% |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `waf-sleep`, 239.8 ns, 16 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `waf-sleep`, 297.9 ns, 16 B; largest Δ: `v-ipv4`, -1.1 ns (now 11.9 ns), 11 B

### `router-prefix-order` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 396,243.7 | 0.0846 | 396,130.2 | 396,274.7 | 51.8 | 1.000x | 1.000x | unchanged (within spread) | -0.02% (null control: program identical) |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 396,303.0 | 0.0847 | 396,186.2 | 396,427.7 | 89.8 | 1.000x | 1.000x | - | - |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 396,330.7 | 0.0847 | 396,235.1 | 396,387.5 | 56.5 | 1.000x | 1.000x | unchanged (within spread) | +0.01% (null control: program identical) |

#### `router-prefix-order` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 261,996.9 | 0.2499 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 261,960.0 | 0.2498 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 262,046.7 | 0.2499 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 64,047.2 | 0.2443 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 64,105.4 | 0.2445 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 64,033.6 | 0.2443 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 14,578.8 | 0.2225 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 14,566.9 | 0.2223 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 14,563.9 | 0.2222 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,034.8 | 0.0168 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,035.5 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,036.2 | 0.0169 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 224.9 | 0.0137 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 226.4 | 0.0138 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 225.0 | 0.0137 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 195.2 | 0.0477 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 194.9 | 0.0476 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 193.9 | 0.0473 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,644.3 | 0.0168 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,668.8 | 0.0169 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,647.5 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,604.0 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,655.5 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,639.6 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,630.2 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 17,647.8 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 17,652.3 | 0.0168 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,036.5 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,034.9 | 0.0168 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,040.3 | 0.0169 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 225.8 | 0.0138 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 226.1 | 0.0138 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 225.8 | 0.0138 |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 261,996.9 ns, 1,048,576 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 262,046.7 ns, 1,048,576 B

### `router-prefix-order` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 692.7 | 691.5 | 693.3 | 0.6 | 1.000x | 1.000x | unchanged (within spread) | -0.04% (null control: program identical) | 75 | 9.2 | 9.1 | 100% |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 693.0 | 690.2 | 693.4 | 1.3 | 1.000x | 1.000x | unchanged (within spread) | -0.33% (null control: program identical) | 75 | 9.2 | 9.1 | 100% |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 695.3 | 694.0 | 697.8 | 1.3 | 1.004x | 1.004x | - | - | 75 | 9.3 | 9.1 | 100% |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `sec-slack-webhook`, 35.7 ns, 81 B; largest Δ: `lp-syslog`, +0.3 ns (now 9.5 ns), 56 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `sec-slack-webhook`, 35.6 ns, 81 B; largest Δ: `sd-router-short`, -0.9 ns (now 29.4 ns), 6 B

### `tag-depth3-bound` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 78,506.3 | 0.0168 | 78,487.5 | 78,582.6 | 33.1 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 78,609.9 | 0.0168 | 78,532.9 | 78,649.2 | 42.7 | 1.001x | 1.001x | unchanged (within spread) | -0.02% vs bar 1.47% (band) → **within** |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 78,623.0 | 0.0168 | 78,575.2 | 78,636.0 | 22.0 | 1.001x | 1.001x | slower ×1.00 | +0.15% (null control: program identical) |

#### `tag-depth3-bound` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 17,604.4 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,635.3 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 17,636.2 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 4,385.5 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 4,379.2 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 4,380.1 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 1,108.5 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,111.8 | 0.0170 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 1,109.6 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,038.0 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,036.6 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,036.3 | 0.0169 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 228.4 | 0.0139 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 227.3 | 0.0139 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 228.7 | 0.0140 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 61.2 | 0.0149 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 61.3 | 0.0150 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 61.4 | 0.0150 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,613.7 | 0.0168 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,608.1 | 0.0168 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,639.5 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,598.7 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,613.5 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,624.5 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 17,610.7 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,619.4 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 17,633.4 | 0.0168 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,038.3 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,036.8 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,037.3 | 0.0169 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 227.5 | 0.0139 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 227.3 | 0.0139 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 228.1 | 0.0139 |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `t-1m`, 17,635.3 ns, 1,048,576 B; largest Δ: `t-tail-digits-1m`, -31.5 ns (now 17,608.1 ns), 1,048,522 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `t-tail-digits-1m`, 17,639.5 ns, 1,048,522 B; largest Δ: `t-1m`, +31.8 ns (now 17,636.2 ns), 1,048,576 B

### `tag-depth3-bound` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 1,079.9 | 1,077.4 | 1,091.2 | 5.0 | 1.000x | 1.000x | faster ×1.07 | -6.76% vs bar 2.21% (band) → **improve** | 75 | 14.4 | 9.1 | 100% |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 1,156.5 | 1,153.3 | 1,157.8 | 1.8 | 1.071x | 1.071x | - | - | 75 | 15.4 | 9.1 | 100% |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 1,158.3 | 1,154.9 | 1,162.3 | 2.7 | 1.073x | 1.073x | unchanged (within spread) | +0.15% (null control: program identical) | 75 | 15.4 | 9.1 | 100% |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `br-tag-mismatch`, 122.9 ns, 19 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `br-tag-mismatch`, 142.8 ns, 19 B

### `tag-pair-match` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 78,574.3 | 0.0168 | 78,564.7 | 78,634.7 | 25.4 | 1.000x | 1.000x | unchanged (within spread) | -0.06% vs bar 1.47% (band) → **within** |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 78,618.3 | 0.0168 | 78,556.6 | 78,628.1 | 27.0 | 1.001x | 1.001x | unchanged (within spread) | -0.02% (null control: program identical) |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 78,637.9 | 0.0168 | 78,608.4 | 78,753.5 | 50.9 | 1.001x | 1.001x | - | - |

#### `tag-pair-match` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,652.2 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 17,618.1 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 17,668.9 | 0.0169 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 4,377.7 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 4,383.5 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 4,385.6 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,107.4 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 1,108.7 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 1,107.3 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,039.4 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,036.5 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,046.6 | 0.0170 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 226.2 | 0.0138 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 227.0 | 0.0139 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 226.8 | 0.0138 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 59.7 | 0.0146 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 60.0 | 0.0147 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 60.0 | 0.0147 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,615.0 | 0.0168 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,620.5 | 0.0168 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,619.2 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,618.6 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,629.0 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,632.6 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,625.7 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 17,642.1 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 17,620.2 | 0.0168 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,035.6 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,036.2 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,036.0 | 0.0169 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 227.0 | 0.0139 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 226.3 | 0.0138 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 226.3 | 0.0138 |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 17,652.2 ns, 1,048,576 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `t-tail-txt-1m`, 17,642.1 ns, 1,048,527 B; largest Δ: `t-1m`, -50.8 ns (now 17,618.1 ns), 1,048,576 B

### `tag-pair-match` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 1,082.7 | 1,040.1 | 1,085.8 | 17.5 | 1.000x | 1.000x | - | - | 75 | 14.4 | 9.1 | 100% |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 1,084.6 | 1,080.7 | 1,091.5 | 3.9 | 1.002x | 1.002x | unchanged (within spread) | +0.18% (null control: program identical) | 75 | 14.5 | 9.1 | 100% |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 1,153.8 | 1,149.6 | 1,167.6 | 6.2 | 1.066x | 1.066x | slower ×1.06 | +6.38% vs bar 2.21% (band) → **regress** | 75 | 15.4 | 9.1 | 100% |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `rec-tag-depth3`, 134.9 ns, 22 B; largest Δ: `sec-slack-webhook`, +2.6 ns (now 14.2 ns), 81 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `rec-tag-depth3`, 128.3 ns, 22 B

### `tail-digits-eol` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 135.7 | 0.0000 | 134.8 | 137.2 | 1.0 | 1.000x | 1.000x | unchanged (within spread) | -0.25% (null control: program identical) |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 136.1 | 0.0000 | 134.6 | 140.1 | 2.0 | 1.002x | 1.002x | unchanged (within spread) | -0.28% (null control: program identical) |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 136.4 | 0.0000 | 133.5 | 140.1 | 2.2 | 1.005x | 1.005x | - | - |

#### `tail-digits-eol` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 30.1 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 30.5 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 30.5 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 11.4 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 10.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 10.8 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.9 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 10.9 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 10.9 | 0.0002 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 8.0 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 8.0 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 8.0 | 0.0001 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 8.0 | 0.0005 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 8.0 | 0.0005 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 8.0 | 0.0005 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 8.0 | 0.0019 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 8.0 | 0.0019 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 8.0 | 0.0019 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 27.5 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 28.4 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 27.1 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 8.0 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 8.0 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 8.0 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 8.0 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 8.0 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 8.0 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 8.0 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 8.0 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 8.0 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 8.0 | 0.0005 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 8.0 | 0.0005 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 8.0 | 0.0005 |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `t-1m`, 30.1 ns, 1,048,576 B; largest Δ: `t-tail-digits-1m`, -0.9 ns (now 27.5 ns), 1,048,522 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `t-1m`, 30.5 ns, 1,048,576 B; largest Δ: `t-tail-digits-1m`, +1.4 ns (now 28.4 ns), 1,048,522 B

### `tail-digits-eol` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 712.4 | 710.4 | 898.3 | 72.7 | 1.000x | 1.000x | unchanged (within spread) | -0.09% (null control: program identical) | 75 | 9.5 | 9.1 | 100% |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 713.1 | 709.2 | 714.9 | 1.9 | 1.001x | 1.001x | unchanged (within spread) | -0.37% (null control: program identical) | 75 | 9.5 | 9.1 | 100% |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 715.8 | 712.9 | 716.1 | 1.3 | 1.005x | 1.005x | - | - | 75 | 9.5 | 9.1 | 100% |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `br-palindrome`, 16.7 ns, 6 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `br-palindrome`, 15.9 ns, 6 B; largest Δ: `cg-number`, -0.9 ns (now 13.9 ns), 10 B

### `tail-dotstar-txt` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 146.0 | 0.0000 | 144.1 | 146.8 | 1.0 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 146.1 | 0.0000 | 143.4 | 148.0 | 1.5 | 1.000x | 1.000x | unchanged (within spread) | +0.05% (null control: program identical) |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 146.1 | 0.0000 | 143.2 | 147.9 | 1.6 | 1.001x | 1.001x | unchanged (within spread) | +0.06% (null control: program identical) |

#### `tail-dotstar-txt` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 13.1 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 13.0 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 13.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 13.3 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 13.2 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 13.1 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 13.3 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 13.2 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 13.1 | 0.0002 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 9.4 | 0.0002 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 9.4 | 0.0002 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.3 | 0.0002 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 9.4 | 0.0006 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 9.3 | 0.0006 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.3 | 0.0006 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 9.4 | 0.0023 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 9.4 | 0.0023 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.3 | 0.0023 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 9.4 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 9.3 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.3 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 9.4 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 9.5 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.4 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 40.8 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 41.1 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 40.9 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 9.3 | 0.0002 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 9.4 | 0.0002 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.3 | 0.0002 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 9.4 | 0.0006 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 9.4 | 0.0006 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.3 | 0.0006 |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `t-tail-txt-1m`, 41.1 ns, 1,048,527 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `t-tail-txt-1m`, 40.9 ns, 1,048,527 B

### `tail-dotstar-txt` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 737.5 | 736.7 | 739.7 | 1.2 | 1.000x | 1.000x | - | - | 75 | 9.8 | 9.1 | 100% |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 738.4 | 735.7 | 742.9 | 2.6 | 1.001x | 1.001x | unchanged (within spread) | +0.11% (null control: program identical) | 75 | 9.8 | 9.1 | 100% |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 739.4 | 737.2 | 745.2 | 3.3 | 1.002x | 1.002x | unchanged (within spread) | +0.14% (null control: program identical) | 75 | 9.9 | 9.1 | 100% |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `lp-winpath`, 27.4 ns, 22 B; largest Δ: `lp-syslog`, +1.1 ns (now 10.4 ns), 56 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `lp-winpath-reserved`, 28.2 ns, 24 B

### `tail-ext-lower-txt` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 125.4 | 0.0000 | 124.9 | 127.2 | 0.9 | 1.000x | 1.000x | unchanged (within spread) | -1.55% (null control: program identical) |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 127.3 | 0.0000 | 125.3 | 128.9 | 1.2 | 1.016x | 1.016x | unchanged (within spread) | -0.54% (null control: program identical) |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 128.0 | 0.0000 | 125.0 | 130.3 | 2.3 | 1.021x | 1.021x | - | - |

#### `tail-ext-lower-txt` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.6 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 11.8 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 10.6 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 11.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 10.8 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.7 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 10.7 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 10.7 | 0.0002 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 8.6 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 8.6 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 8.6 | 0.0001 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 8.6 | 0.0005 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 8.6 | 0.0005 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 8.6 | 0.0005 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 8.6 | 0.0021 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 8.6 | 0.0021 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 8.6 | 0.0021 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 8.6 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 8.6 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 8.6 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 8.6 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 8.6 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 8.6 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 33.2 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 33.1 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 33.3 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 8.6 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 8.6 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 8.6 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 8.6 | 0.0005 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 8.6 | 0.0005 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 8.6 | 0.0005 |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `t-tail-txt-1m`, 33.2 ns, 1,048,527 B; largest Δ: `t-1m`, -1.2 ns (now 10.6 ns), 1,048,576 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `t-tail-txt-1m`, 33.1 ns, 1,048,527 B; largest Δ: `t-1m`, +1.2 ns (now 11.8 ns), 1,048,576 B

### `tail-ext-lower-txt` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 640.6 | 635.8 | 645.5 | 3.6 | 1.000x | 1.000x | unchanged (within spread) | -0.54% (null control: program identical) | 75 | 8.5 | 9.1 | 100% |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 643.3 | 635.9 | 645.1 | 4.0 | 1.004x | 1.004x | - | - | 75 | 8.6 | 9.1 | 100% |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 644.1 | 633.9 | 646.1 | 4.4 | 1.005x | 1.005x | unchanged (within spread) | +0.12% (null control: program identical) | 75 | 8.6 | 9.1 | 100% |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `lp-winpath`, 21.0 ns, 22 B; largest Δ: `br-palindrome`, -0.2 ns (now 8.1 ns), 6 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `lp-winpath`, 21.0 ns, 22 B; largest Δ: `rd-numeric-id-hit`, +0.1 ns (now 8.3 ns), 4 B

### `tail-space-eol` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 21,969.8 | 0.0047 | 21,968.1 | 21,975.8 | 3.2 | 1.000x | 1.000x | **dominated**: `t-trim-match-60k` is 99.2% of this set | faster ×1.00 | -0.13% (null control: program identical) |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 21,975.8 | 0.0047 | 21,970.0 | 21,984.0 | 4.6 | 1.000x | 1.000x | **dominated**: `t-trim-match-60k` is 99.2% of this set | unchanged (within spread) | +0.03% (null control: program identical) |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 21,998.6 | 0.0047 | 21,986.9 | 22,015.0 | 10.8 | 1.001x | 1.001x | **dominated**: `t-trim-match-60k` is 99.2% of this set | - | - |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `tail-space-eol` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 30.7 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 29.9 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 30.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 30.7 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 31.6 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 31.8 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 31.5 | 0.0005 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 31.8 | 0.0005 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 32.3 | 0.0005 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 9.2 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.4 | 0.0002 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 9.2 | 0.0001 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 8.7 | 0.0005 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.0 | 0.0005 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 8.6 | 0.0005 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 8.8 | 0.0021 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 8.8 | 0.0022 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 9.1 | 0.0022 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 8.8 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 8.8 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 8.8 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 28.8 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 27.7 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 27.6 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 8.8 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 8.8 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 8.8 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 21,796.3 | 0.3548 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 21,798.4 | 0.3548 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 21,825.9 | 0.3552 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 9.9 | 0.0006 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.9 | 0.0006 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 9.2 | 0.0006 |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `t-trim-match-60k`, 21,796.3 ns, 61,440 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `t-trim-match-60k`, 21,798.4 ns, 61,440 B

### `tail-space-eol` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 678.9 | 678.3 | 684.1 | 2.2 | 1.000x | 1.000x | unchanged (within spread) | -0.44% (null control: program identical) | 75 | 9.1 | 9.1 | 100% |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 679.0 | 677.4 | 679.8 | 0.9 | 1.000x | 1.000x | unchanged (within spread) | +0.02% (null control: program identical) | 75 | 9.1 | 9.1 | 100% |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 681.9 | 679.2 | 686.1 | 2.3 | 1.004x | 1.004x | - | - | 75 | 9.1 | 9.1 | 100% |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `rd-trim-hit`, 17.3 ns, 4 B; largest Δ: `br-tag-pair`, -0.3 ns (now 8.9 ns), 18 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `rd-trim-hit`, 17.1 ns, 4 B; largest Δ: `cg-key-colon`, -0.3 ns (now 13.9 ns), 7 B

### `tail-word-eoz` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 21,905.3 | 0.0047 | 21,903.6 | 21,908.3 | 1.9 | 1.000x | 1.000x | **dominated**: `t-evil-match-60k` is 99.4% of this set | faster ×1.00 | -0.06% (null control: program identical) |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 21,907.2 | 0.0047 | 21,902.5 | 21,930.4 | 10.2 | 1.000x | 1.000x | **dominated**: `t-evil-match-60k` is 99.4% of this set | unchanged (within spread) | +0.01% (null control: program identical) |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 21,918.5 | 0.0047 | 21,910.4 | 21,921.4 | 4.0 | 1.001x | 1.001x | **dominated**: `t-evil-match-60k` is 99.4% of this set | - | - |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `tail-word-eoz` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 6.7 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 6.6 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 6.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 6.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 6.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 6.6 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 6.7 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 6.6 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 6.5 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 21,773.7 | 0.3544 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 21,773.6 | 0.3544 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 21,786.0 | 0.3546 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 8.0 | 0.0005 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 7.8 | 0.0005 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 7.9 | 0.0005 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 25.1 | 0.0061 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 24.6 | 0.0060 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 25.0 | 0.0061 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 23.4 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 23.6 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 24.1 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 7.8 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 6.6 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 7.7 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 21.6 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 21.6 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 21.6 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 7.7 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 7.8 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 7.7 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 18.2 | 0.0011 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 18.0 | 0.0011 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 18.0 | 0.0011 |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `t-evil-match-60k`, 21,773.7 ns, 61,440 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `t-evil-match-60k`, 21,773.6 ns, 61,440 B; largest Δ: `t-tail-space-1m`, -1.2 ns (now 6.6 ns), 1,048,522 B

### `tail-word-eoz` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 1,010.5 | 1,003.5 | 1,039.1 | 12.4 | 1.000x | 1.000x | unchanged (within spread) | -1.10% (null control: program identical) | 75 | 13.5 | 9.1 | 100% |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 1,021.7 | 1,010.6 | 1,038.4 | 9.3 | 1.011x | 1.011x | unchanged (within spread) | -0.57% (null control: program identical) | 75 | 13.6 | 9.1 | 100% |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 1,027.5 | 1,016.5 | 1,031.3 | 5.5 | 1.017x | 1.017x | - | - | 75 | 13.7 | 9.1 | 100% |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `sec-github-pat`, 58.6 ns, 93 B; largest Δ: `lp-winpath`, -1.3 ns (now 13.6 ns), 22 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `sec-github-pat`, 58.7 ns, 93 B; largest Δ: `la-negation-miss`, +1.3 ns (now 16.3 ns), 23 B

### `trim-nested-star` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 114,791.1 | 0.0245 | 114,754.4 | 115,171.9 | 165.6 | 1.000x | 1.000x | unchanged (within spread) | -1.29% (null control: program identical) |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 115,829.5 | 0.0247 | 114,805.3 | 117,631.3 | 987.4 | 1.009x | 1.009x | unchanged (within spread) | +0.90% (null control: program identical) |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 116,294.9 | 0.0248 | 114,308.7 | 118,346.9 | 1,321.1 | 1.013x | 1.013x | - | - |

#### `trim-nested-star` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 9.6 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.6 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 9.5 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 9.5 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.5 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 9.6 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 9.6 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.5 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 9.6 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 9.5 | 0.0002 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.5 | 0.0002 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 9.5 | 0.0002 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 9.5 | 0.0006 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.5 | 0.0006 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 9.6 | 0.0006 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 11.9 | 0.0029 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 12.4 | 0.0030 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 12.7 | 0.0031 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 9.5 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.5 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 9.5 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 9.5 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.5 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 9.5 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 9.5 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.5 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 9.5 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 100,165.0 | 1.6303 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 101,203.5 | 1.6472 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 101,575.0 | 1.6532 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 14,533.7 | 0.8870 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 14,534.0 | 0.8870 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 14,631.1 | 0.8930 |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `t-trim-match-60k`, 100,165.0 ns, 61,440 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `t-trim-match-60k`, 101,203.5 ns, 61,440 B

### `trim-nested-star` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 781.0 | 780.8 | 782.8 | 0.7 | 1.000x | 1.000x | - | - | 75 | 10.4 | 9.1 | 100% |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 781.2 | 779.4 | 781.4 | 0.8 | 1.000x | 1.000x | unchanged (within spread) | -0.19% (null control: program identical) | 75 | 10.4 | 9.1 | 100% |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 782.7 | 782.2 | 786.8 | 1.7 | 1.002x | 1.002x | unchanged (within spread) | +0.22% (null control: program identical) | 75 | 10.4 | 9.1 | 100% |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `rd-trim-near-miss`, 35.7 ns, 20 B; largest Δ: `rd-evil-alt-near-miss`, -0.9 ns (now 9.8 ns), 18 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `rd-trim-near-miss`, 35.9 ns, 20 B; largest Δ: `rd-evil-alt-near-miss`, +0.9 ns (now 10.6 ns), 18 B

### `utf8-lead-no-cont` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 1,660,189.3 | 0.3546 | 1,659,906.3 | 1,660,612.5 | 266.4 | 1.000x | 1.000x | unchanged (within spread) | -0.03% (null control: program identical) |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 1,660,753.0 | 0.3547 | 1,660,077.1 | 1,662,132.2 | 669.2 | 1.000x | 1.000x | faster ×1.00 | -0.13% (null control: program identical) |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 1,662,842.2 | 0.3552 | 1,662,486.1 | 1,663,116.7 | 207.5 | 1.002x | 1.002x | - | - |

#### `utf8-lead-no-cont` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 371,760.8 | 0.3545 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 371,898.5 | 0.3547 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 372,478.4 | 0.3552 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 92,889.2 | 0.3543 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 92,965.4 | 0.3546 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 92,978.9 | 0.3547 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 23,275.4 | 0.3552 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 23,272.5 | 0.3551 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 23,347.7 | 0.3563 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 21,757.1 | 0.3541 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 21,765.4 | 0.3543 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 21,788.9 | 0.3546 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5,812.8 | 0.3548 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 5,814.3 | 0.3549 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 5,823.3 | 0.3554 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,470.2 | 0.3589 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 1,470.1 | 0.3589 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 1,471.1 | 0.3592 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 371,880.9 | 0.3547 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 371,933.5 | 0.3547 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 372,462.9 | 0.3552 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 371,815.1 | 0.3546 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 371,989.5 | 0.3548 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 372,455.9 | 0.3552 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 371,838.1 | 0.3546 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 371,961.8 | 0.3547 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 372,424.5 | 0.3552 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 21,783.3 | 0.3545 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 21,773.2 | 0.3544 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 21,800.6 | 0.3548 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5,819.2 | 0.3552 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 5,822.9 | 0.3554 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 5,826.5 | 0.3556 |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `t-tail-digits-1m`, 371,880.9 ns, 1,048,522 B; largest Δ: `t-tail-space-1m`, -174.5 ns (now 371,815.1 ns), 1,048,522 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `t-tail-space-1m`, 371,989.5 ns, 1,048,522 B; largest Δ: `t-1m`, -579.9 ns (now 371,898.5 ns), 1,048,576 B

### `utf8-lead-no-cont` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 1,245.2 | 1,240.5 | 1,247.4 | 2.6 | 1.000x | 1.000x | unchanged (within spread) | -0.13% (null control: program identical) | 75 | 16.6 | 9.1 | 100% |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 1,246.8 | 1,245.4 | 1,248.7 | 1.2 | 1.001x | 1.001x | unchanged (within spread) | -0.04% (null control: program identical) | 75 | 16.6 | 9.1 | 100% |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 1,247.3 | 1,245.5 | 1,251.3 | 2.1 | 1.002x | 1.002x | - | - | 75 | 16.6 | 9.1 | 100% |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `sec-github-pat`, 55.5 ns, 93 B; largest Δ: `floor-hit`, -0.8 ns (now 8.1 ns), 1 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `sec-github-pat`, 55.4 ns, 93 B; largest Δ: `rec-comment-nested`, +0.7 ns (now 21.5 ns), 34 B

### `uuid-near-miss` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 54.9 | 0.0000 | 54.8 | 55.1 | 0.1 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 55.0 | 0.0000 | 55.0 | 55.4 | 0.1 | 1.003x | 1.003x | unchanged (within spread) | +0.29% (null control: program identical) |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 55.1 | 0.0000 | 55.0 | 55.1 | 0.0 | 1.003x | 1.003x | unchanged (within spread) | +0.04% (null control: program identical) |

#### `uuid-near-miss` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 5.0 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 5.0 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.0 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 5.0 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 5.0 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.0 | 0.0001 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 5.0 | 0.0003 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 5.0 | 0.0003 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.0 | 0.0003 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 5.0 | 0.0012 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 5.0 | 0.0012 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.0 | 0.0012 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 5.0 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 5.0 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.0 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 5.0 | 0.0003 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 5.0 | 0.0003 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.0 | 0.0003 |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `t-64k`, 5.0 ns, 65,536 B; largest Δ: `t-evil-match-60k`, +0.0 ns (now 5.0 ns), 61,440 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `t-1m`, 5.0 ns, 1,048,576 B; largest Δ: `t-64k`, -0.0 ns (now 5.0 ns), 65,536 B

### `uuid-near-miss` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 537.0 | 535.9 | 538.4 | 0.9 | 1.000x | 1.000x | - | - | 75 | 7.2 | 9.1 | 100% |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 538.7 | 535.9 | 542.2 | 2.5 | 1.003x | 1.003x | unchanged (within spread) | -0.33% (null control: program identical) | 75 | 7.2 | 9.1 | 100% |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 540.5 | 539.6 | 554.8 | 5.8 | 1.006x | 1.006x | unchanged (within spread) | +0.64% (null control: program identical) | 75 | 7.2 | 9.1 | 100% |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `v-uuid-valid`, 34.9 ns, 36 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `v-uuid-valid`, 37.7 ns, 36 B

### `wild-codegrammar-json-array-begin` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 267,026.8 | 0.0570 | 266,836.5 | 267,813.5 | 350.2 | 1.000x | 1.000x | unchanged (within spread) | -0.06% (null control: program identical) |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 267,055.1 | 0.0570 | 266,544.5 | 268,135.9 | 530.0 | 1.000x | 1.000x | unchanged (within spread) | +0.01% (null control: program identical) |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 267,191.8 | 0.0571 | 266,957.6 | 267,574.5 | 239.1 | 1.001x | 1.001x | - | - |

#### `wild-codegrammar-json-array-begin` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 163,263.3 | 0.1557 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 163,344.7 | 0.1558 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 163,416.1 | 0.1558 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 38,795.4 | 0.1480 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 38,858.9 | 0.1482 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 38,676.1 | 0.1475 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 9,439.9 | 0.1440 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9,437.0 | 0.1440 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 9,363.1 | 0.1429 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,039.6 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,036.3 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,036.7 | 0.0169 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 224.5 | 0.0137 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 225.8 | 0.0138 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 225.9 | 0.0138 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 59.9 | 0.0146 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 60.5 | 0.0148 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 59.9 | 0.0146 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,652.0 | 0.0168 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,668.2 | 0.0169 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,688.4 | 0.0169 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,659.5 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,604.8 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,662.5 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 17,643.1 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,635.7 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 17,661.9 | 0.0168 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,038.2 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,034.2 | 0.0168 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,036.3 | 0.0169 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 225.9 | 0.0138 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 225.6 | 0.0138 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 226.0 | 0.0138 |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 163,263.3 ns, 1,048,576 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 163,344.7 ns, 1,048,576 B

### `wild-codegrammar-json-array-begin` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 687.7 | 687.4 | 691.0 | 1.6 | 1.000x | 1.000x | unchanged (within spread) | -0.83% (null control: program identical) | 75 | 9.2 | 9.1 | 100% |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 688.3 | 686.8 | 690.4 | 1.3 | 1.001x | 1.001x | unchanged (within spread) | +0.10% (null control: program identical) | 75 | 9.2 | 9.1 | 100% |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 693.4 | 691.7 | 700.2 | 3.0 | 1.008x | 1.008x | - | - | 75 | 9.2 | 9.1 | 100% |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `rec-array-define`, 14.2 ns, 11 B; largest Δ: `la-pwd-weak`, -0.3 ns (now 8.9 ns), 10 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `rec-array-define`, 13.7 ns, 11 B

### `wild-codegrammar-json-constant` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 8,601,667.4 | 1.8373 | 8,584,960.6 | 8,611,354.5 | 8,864.5 | 1.000x | 1.000x | unchanged (within spread) | -0.16% (null control: program identical) |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 8,615,497.1 | 1.8403 | 8,601,458.8 | 8,639,022.9 | 13,415.5 | 1.002x | 1.002x | unchanged (within spread) | -0.23% (null control: program identical) |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 8,634,968.2 | 1.8445 | 8,634,420.8 | 8,638,510.0 | 1,658.4 | 1.004x | 1.004x | - | - |

#### `wild-codegrammar-json-constant` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,731,580.9 | 1.6514 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 1,728,583.8 | 1.6485 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 1,738,037.2 | 1.6575 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 441,466.8 | 1.6841 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 443,516.4 | 1.6919 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 448,107.7 | 1.7094 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 110,375.4 | 1.6842 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 112,403.5 | 1.7151 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 111,897.4 | 1.7074 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 120,561.1 | 1.9623 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 120,582.6 | 1.9626 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 120,629.0 | 1.9634 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 32,139.1 | 1.9615 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 32,144.3 | 1.9618 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 32,161.3 | 1.9629 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5,887.6 | 1.4374 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 5,810.0 | 1.4185 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 5,705.9 | 1.3930 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 2,048,477.9 | 1.9537 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 2,048,277.8 | 1.9535 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 2,046,622.6 | 1.9519 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 2,042,847.8 | 1.9483 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 2,044,457.5 | 1.9498 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 2,052,636.7 | 1.9576 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 2,039,076.4 | 1.9447 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 2,054,131.3 | 1.9591 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 2,054,656.7 | 1.9596 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 21,837.9 | 0.3554 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 21,830.9 | 0.3553 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 21,837.9 | 0.3554 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5,821.3 | 0.3553 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 5,825.5 | 0.3555 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 5,830.0 | 0.3558 |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `t-tail-digits-1m`, 2,048,477.9 ns, 1,048,522 B; largest Δ: `t-tail-txt-1m`, -15,055.0 ns (now 2,039,076.4 ns), 1,048,527 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `t-tail-txt-1m`, 2,054,131.3 ns, 1,048,527 B; largest Δ: `t-1m`, -9,453.4 ns (now 1,728,583.8 ns), 1,048,576 B

### `wild-codegrammar-json-constant` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 1,617.1 | 1,613.3 | 1,622.3 | 3.5 | 1.000x | 1.000x | unchanged (within spread) | -0.21% (null control: program identical) | 75 | 21.6 | 9.1 | 100% |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 1,620.4 | 1,617.9 | 1,628.2 | 3.7 | 1.002x | 1.002x | unchanged (within spread) | -0.20% (null control: program identical) | 75 | 21.6 | 9.1 | 100% |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 1,623.7 | 1,618.4 | 1,629.4 | 3.8 | 1.004x | 1.004x | - | - | 75 | 21.6 | 9.1 | 100% |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `sec-github-pat`, 177.8 ns, 93 B; largest Δ: `br-doubled-word`, -1.7 ns (now 24.7 ns), 15 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `sec-github-pat`, 177.8 ns, 93 B; largest Δ: `br-doubled-word`, +1.9 ns (now 26.5 ns), 15 B

### `wild-codegrammar-json-number-extended` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 5,309,991.3 | 1.1342 | 5,300,116.2 | 5,316,754.2 | 6,034.8 | 1.000x | 1.000x | faster ×1.00 | -0.23% (null control: program identical) |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 5,322,491.7 | 1.1369 | 5,315,482.6 | 5,330,394.1 | 5,477.8 | 1.002x | 1.002x | - | - |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 5,325,872.0 | 1.1376 | 5,323,689.3 | 5,333,762.0 | 4,078.1 | 1.003x | 1.003x | slower ×1.00 | +0.30% (null control: program identical) |

#### `wild-codegrammar-json-number-extended` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 1,630,371.5 | 1.5548 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 1,636,596.9 | 1.5608 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,641,417.5 | 1.5654 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 399,610.5 | 1.5244 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 398,229.0 | 1.5191 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 399,363.1 | 1.5234 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 98,864.2 | 1.5085 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 101,626.2 | 1.5507 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 99,349.9 | 1.5160 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 21,459.8 | 0.3493 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 21,468.2 | 0.3494 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 21,481.1 | 0.3496 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 5,733.8 | 0.3499 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 5,737.7 | 0.3502 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5,733.2 | 0.3499 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 24,131.1 | 5.8914 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 24,203.5 | 5.9091 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 24,196.3 | 5.9073 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 1,035,942.6 | 0.9880 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 1,036,862.3 | 0.9889 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,037,302.8 | 0.9893 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 1,034,072.0 | 0.9862 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 1,035,175.9 | 0.9873 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,036,764.3 | 0.9888 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 1,034,007.9 | 0.9862 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 1,035,044.3 | 0.9871 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,034,571.9 | 0.9867 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 21,470.0 | 0.3494 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 21,492.6 | 0.3498 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 21,472.3 | 0.3495 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 5,736.7 | 0.3501 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 5,743.2 | 0.3505 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5,736.1 | 0.3501 |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 1,630,371.5 ns, 1,048,576 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 1,641,417.5 ns, 1,048,576 B

### `wild-codegrammar-json-number-extended` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 1,383.2 | 1,374.7 | 1,390.4 | 5.3 | 1.000x | 1.000x | unchanged (within spread) | -0.79% (null control: program identical) | 75 | 18.4 | 9.1 | 100% |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 1,385.3 | 1,381.7 | 1,389.3 | 2.4 | 1.002x | 1.002x | - | - | 75 | 18.5 | 9.1 | 100% |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 1,394.2 | 1,380.4 | 1,397.0 | 5.9 | 1.008x | 1.008x | unchanged (within spread) | +0.64% (null control: program identical) | 75 | 18.6 | 9.1 | 100% |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `rd-numeric-id-near-miss`, 69.3 ns, 20 B; largest Δ: `v-uuid-valid`, -1.2 ns (now 14.8 ns), 36 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `rd-numeric-id-near-miss`, 69.3 ns, 20 B; largest Δ: `sd-empty-alt-hit`, +2.7 ns (now 47.4 ns), 61 B

### `wild-codegrammar-json-object-begin` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 78,597.4 | 0.0168 | 78,572.3 | 78,652.3 | 26.4 | 1.000x | 1.000x | unchanged (within spread) | -0.01% (null control: program identical) |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 78,605.7 | 0.0168 | 78,591.3 | 78,636.7 | 17.3 | 1.000x | 1.000x | - | - |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 78,653.7 | 0.0168 | 78,571.9 | 78,713.4 | 46.9 | 1.001x | 1.001x | unchanged (within spread) | +0.07% (null control: program identical) |

#### `wild-codegrammar-json-object-begin` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 17,634.2 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 17,637.5 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,654.4 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 4,376.1 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 4,385.2 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 4,384.1 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 1,107.5 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 1,109.9 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,108.3 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,037.7 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,037.0 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,035.8 | 0.0169 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 224.0 | 0.0137 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 224.7 | 0.0137 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 224.6 | 0.0137 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 59.7 | 0.0146 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 59.7 | 0.0146 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 59.7 | 0.0146 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,651.0 | 0.0168 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,650.1 | 0.0168 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,657.9 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,623.2 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,623.5 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,611.5 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 17,633.9 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 17,616.8 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,628.1 | 0.0168 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,036.5 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,036.8 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,035.8 | 0.0169 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 224.3 | 0.0137 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 224.7 | 0.0137 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 224.5 | 0.0137 |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `t-tail-digits-1m`, 17,651.0 ns, 1,048,522 B; largest Δ: `t-tail-txt-1m`, +17.1 ns (now 17,633.9 ns), 1,048,527 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `t-tail-digits-1m`, 17,657.9 ns, 1,048,522 B; largest Δ: `t-1m`, +20.2 ns (now 17,654.4 ns), 1,048,576 B

### `wild-codegrammar-json-object-begin` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 679.8 | 678.8 | 689.3 | 3.9 | 1.000x | 1.000x | - | - | 75 | 9.1 | 9.1 | 100% |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 682.6 | 677.7 | 685.0 | 2.4 | 1.004x | 1.004x | unchanged (within spread) | +0.41% (null control: program identical) | 75 | 9.1 | 9.1 | 100% |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 686.6 | 679.0 | 710.3 | 11.1 | 1.010x | 1.010x | unchanged (within spread) | +0.59% (null control: program identical) | 75 | 9.2 | 9.1 | 100% |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `cg-object-begin`, 12.6 ns, 1 B; largest Δ: `br-quoted-delim`, +0.3 ns (now 9.2 ns), 15 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `cg-object-begin`, 12.6 ns, 1 B; largest Δ: `rec-parens-unbalanced`, +0.3 ns (now 9.1 ns), 5 B

### `wild-codegrammar-json-stringcontent-escape` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 78,609.6 | 0.0168 | 78,585.6 | 78,688.6 | 36.1 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 78,638.4 | 0.0168 | 78,590.3 | 78,689.2 | 37.0 | 1.000x | 1.000x | unchanged (within spread) | -0.13% (null control: program identical) |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 78,742.3 | 0.0168 | 78,626.8 | 78,831.8 | 70.9 | 1.002x | 1.002x | unchanged (within spread) | +0.17% (null control: program identical) |

#### `wild-codegrammar-json-stringcontent-escape` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 17,636.7 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,644.3 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 17,673.7 | 0.0169 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 4,383.8 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 4,382.4 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 4,417.7 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 1,108.9 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,108.8 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 1,108.9 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,033.9 | 0.0168 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,035.0 | 0.0168 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,034.8 | 0.0168 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 224.7 | 0.0137 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 223.5 | 0.0136 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 224.6 | 0.0137 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 59.8 | 0.0146 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 59.8 | 0.0146 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 60.2 | 0.0147 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,646.3 | 0.0168 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,685.6 | 0.0169 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,664.7 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,621.7 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,642.8 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,655.6 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 17,632.6 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,604.2 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 17,639.2 | 0.0168 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,035.6 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,033.6 | 0.0168 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,038.6 | 0.0169 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 225.0 | 0.0137 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 224.9 | 0.0137 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 225.6 | 0.0138 |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `t-tail-digits-1m`, 17,685.6 ns, 1,048,522 B; largest Δ: `t-256k`, -35.3 ns (now 4,382.4 ns), 262,144 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 17,673.7 ns, 1,048,576 B

### `wild-codegrammar-json-stringcontent-escape` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 742.9 | 741.8 | 744.0 | 0.8 | 1.000x | 1.000x | - | - | 75 | 9.9 | 9.1 | 100% |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 743.3 | 742.5 | 744.8 | 0.8 | 1.000x | 1.000x | unchanged (within spread) | +0.05% (null control: program identical) | 75 | 9.9 | 9.1 | 100% |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 743.4 | 743.3 | 743.9 | 0.2 | 1.001x | 1.001x | unchanged (within spread) | +0.02% (null control: program identical) | 75 | 9.9 | 9.1 | 100% |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `lp-winpath-reserved`, 35.3 ns, 24 B; largest Δ: `lp-winpath`, +0.2 ns (now 26.9 ns), 22 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `lp-winpath-reserved`, 35.3 ns, 24 B; largest Δ: `sd-empty-alt-hit`, -0.3 ns (now 9.5 ns), 61 B

### `wild-datetime-moment-iso8601` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 69,118.0 | 0.0148 | 69,116.9 | 69,128.5 | 5.3 | 1.000x | 1.000x | unchanged (within spread) | -0.01% (null control: program identical) |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 69,120.1 | 0.0148 | 69,116.9 | 79,758.6 | 4,255.4 | 1.000x | 1.000x | - | - |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 69,121.8 | 0.0148 | 69,119.8 | 69,167.7 | 18.3 | 1.000x | 1.000x | unchanged (within spread) | +0.00% (null control: program identical) |

#### `wild-datetime-moment-iso8601` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 11.4 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 11.4 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 11.4 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 11.5 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 11.4 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 11.5 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 11.4 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 11.4 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 11.4 | 0.0002 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 11.4 | 0.0002 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 11.5 | 0.0002 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 11.4 | 0.0002 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 11.4 | 0.0007 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 11.4 | 0.0007 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 11.4 | 0.0007 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 15.5 | 0.0038 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 14.8 | 0.0036 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 14.8 | 0.0036 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 11.4 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 11.6 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 12.1 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 11.4 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 11.4 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 11.4 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 11.4 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 11.4 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 11.4 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 54,448.6 | 0.8862 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 54,448.5 | 0.8862 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 54,452.2 | 0.8863 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 14,562.9 | 0.8888 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 14,561.8 | 0.8887 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 14,562.2 | 0.8888 |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `t-trim-match-60k`, 54,448.6 ns, 61,440 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `t-trim-match-60k`, 54,452.2 ns, 61,440 B

### `wild-datetime-moment-iso8601` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 998.1 | 945.1 | 998.7 | 21.2 | 1.000x | 1.000x | unchanged (within spread) | -0.49% (null control: program identical) | 75 | 13.3 | 9.1 | 100% |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 999.4 | 998.1 | 1,011.7 | 5.1 | 1.001x | 1.001x | - | - | 75 | 13.3 | 9.1 | 100% |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 1,002.9 | 1,001.9 | 1,019.0 | 6.4 | 1.005x | 1.005x | unchanged (within spread) | +0.36% (null control: program identical) | 75 | 13.4 | 9.1 | 100% |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `dt-iso8601`, 85.5 ns, 20 B; largest Δ: `rd-trim-near-miss`, -3.7 ns (now 62.3 ns), 20 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `dt-iso8601`, 85.5 ns, 20 B; largest Δ: `rd-trim-near-miss`, +3.6 ns (now 66.0 ns), 20 B

### `wild-logparse-base10num-grok` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 9,735,347.2 | 2.0795 | 9,715,357.8 | 9,741,848.9 | 10,680.8 | 1.000x | 1.000x | unchanged (within spread) | -0.03% (null control: program identical) |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 9,738,719.9 | 2.0802 | 9,712,647.7 | 9,752,694.1 | 14,041.8 | 1.000x | 1.000x | unchanged (within spread) | -0.09% (null control: program identical) |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 9,747,574.8 | 2.0821 | 9,733,172.9 | 9,760,381.7 | 9,215.8 | 1.001x | 1.001x | - | - |

#### `wild-logparse-base10num-grok` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 3,058,611.3 | 2.9169 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 3,057,344.1 | 2.9157 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 3,065,894.1 | 2.9239 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 755,021.5 | 2.8802 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 756,981.7 | 2.8877 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 758,487.2 | 2.8934 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 184,356.1 | 2.8131 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 183,618.9 | 2.8018 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 183,995.0 | 2.8075 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 21,777.8 | 0.3545 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 21,765.8 | 0.3543 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 21,765.5 | 0.3543 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5,822.2 | 0.3553 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 5,826.1 | 0.3556 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 5,819.4 | 0.3552 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 39,204.0 | 9.5713 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 39,254.9 | 9.5837 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 39,205.8 | 9.5717 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,878,628.6 | 1.7917 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 1,880,021.3 | 1.7930 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 1,881,399.2 | 1.7943 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,880,666.4 | 1.7936 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 1,883,571.7 | 1.7964 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 1,882,282.7 | 1.7952 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,879,498.1 | 1.7925 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 1,879,423.5 | 1.7924 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 1,881,330.9 | 1.7943 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 21,782.1 | 0.3545 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 21,772.0 | 0.3544 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 21,783.4 | 0.3545 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5,825.7 | 0.3556 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 5,834.2 | 0.3561 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 5,823.4 | 0.3554 |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `t-1m`, 3,058,611.3 ns, 1,048,576 B; largest Δ: `t-tail-space-1m`, -2,905.3 ns (now 1,880,666.4 ns), 1,048,522 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 3,057,344.1 ns, 1,048,576 B

### `wild-logparse-base10num-grok` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 2,358.6 | 2,344.1 | 2,541.1 | 75.3 | 1.000x | 1.000x | unchanged (within spread) | -0.07% (null control: program identical) | 75 | 31.4 | 9.1 | 100% |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 2,360.3 | 2,349.7 | 2,522.5 | 65.6 | 1.001x | 1.001x | unchanged (within spread) | -0.07% (null control: program identical) | 75 | 31.5 | 9.1 | 100% |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 2,362.0 | 2,359.0 | 2,516.4 | 61.2 | 1.001x | 1.001x | - | - | 75 | 31.5 | 9.1 | 100% |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `rd-numeric-id-near-miss`, 109.4 ns, 20 B; largest Δ: `sec-slack-webhook`, -1.4 ns (now 82.4 ns), 81 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `rd-numeric-id-near-miss`, 109.3 ns, 20 B; largest Δ: `sec-slack-webhook`, +1.4 ns (now 83.8 ns), 81 B

### `wild-logparse-base10num-noatomic` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 6,969,317.9 | 1.4887 | 6,962,789.7 | 6,976,012.1 | 4,897.8 | 1.000x | 1.000x | unchanged (within spread) | -0.09% (null control: program identical) |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 6,971,298.8 | 1.4891 | 6,963,237.7 | 7,016,706.4 | 19,164.1 | 1.000x | 1.000x | unchanged (within spread) | +0.03% (null control: program identical) |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 6,975,631.3 | 1.4900 | 6,969,644.3 | 6,982,027.9 | 4,620.8 | 1.001x | 1.001x | - | - |

#### `wild-logparse-base10num-noatomic` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 1,970,480.6 | 1.8792 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,971,268.6 | 1.8799 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 1,976,159.2 | 1.8846 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 479,346.5 | 1.8286 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 481,313.6 | 1.8361 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 481,305.0 | 1.8360 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 119,136.6 | 1.8179 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 118,302.9 | 1.8052 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 118,805.4 | 1.8128 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 21,756.2 | 0.3541 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 21,787.1 | 0.3546 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 21,765.2 | 0.3543 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 5,821.2 | 0.3553 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5,821.4 | 0.3553 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 5,830.8 | 0.3559 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 25,226.9 | 6.1589 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 25,211.6 | 6.1552 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 25,240.2 | 6.1622 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 1,438,683.9 | 1.3721 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,443,173.7 | 1.3764 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 1,440,503.8 | 1.3738 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 1,439,708.1 | 1.3731 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,439,458.8 | 1.3728 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 1,441,035.3 | 1.3743 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 1,438,962.1 | 1.3724 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,438,312.3 | 1.3717 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 1,439,024.1 | 1.3724 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 21,759.9 | 0.3542 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 21,796.4 | 0.3548 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 21,773.8 | 0.3544 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 5,821.4 | 0.3553 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5,829.3 | 0.3558 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 5,818.1 | 0.3551 |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 1,970,480.6 ns, 1,048,576 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `t-1m`, 1,971,268.6 ns, 1,048,576 B; largest Δ: `t-tail-digits-1m`, +4,489.9 ns (now 1,443,173.7 ns), 1,048,522 B

### `wild-logparse-base10num-noatomic` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 1,620.3 | 1,614.1 | 1,626.4 | 4.2 | 1.000x | 1.000x | - | - | 75 | 21.6 | 9.1 | 100% |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 1,622.0 | 1,620.8 | 1,634.4 | 5.1 | 1.001x | 1.001x | unchanged (within spread) | +0.10% (null control: program identical) | 75 | 21.6 | 9.1 | 100% |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 1,625.6 | 1,619.5 | 1,643.3 | 8.1 | 1.003x | 1.003x | unchanged (within spread) | +0.22% (null control: program identical) | 75 | 21.7 | 9.1 | 100% |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `rd-numeric-id-near-miss`, 82.9 ns, 20 B; largest Δ: `lp-winpath`, +1.7 ns (now 24.1 ns), 22 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `rd-numeric-id-near-miss`, 82.8 ns, 20 B; largest Δ: `lp-winpath`, +1.2 ns (now 25.4 ns), 22 B

### `wild-logparse-quotedstring-grok` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 2,063,009.7 | 0.4407 | 2,061,825.3 | 2,063,982.1 | 775.3 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 2,063,278.5 | 0.4407 | 2,063,025.2 | 2,064,532.9 | 556.6 | 1.000x | 1.000x | unchanged (within spread) | -0.10% (null control: program identical) |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 2,065,444.6 | 0.4412 | 2,060,859.3 | 2,068,058.8 | 2,341.6 | 1.001x | 1.001x | unchanged (within spread) | +0.12% (null control: program identical) |

#### `wild-logparse-quotedstring-grok` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 682,682.1 | 0.6511 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 682,938.5 | 0.6513 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 684,461.7 | 0.6528 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 165,748.4 | 0.6323 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 165,693.6 | 0.6321 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 166,083.9 | 0.6336 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 41,811.3 | 0.6380 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 42,504.0 | 0.6486 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 42,153.2 | 0.6432 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 21,784.2 | 0.3546 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 21,773.7 | 0.3544 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 21,765.9 | 0.3543 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 5,834.8 | 0.3561 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5,824.0 | 0.3554 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 5,826.7 | 0.3556 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 1,481.5 | 0.3617 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,480.3 | 0.3614 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 1,478.9 | 0.3611 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 372,001.0 | 0.3548 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 371,895.4 | 0.3547 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 372,031.7 | 0.3548 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 371,959.9 | 0.3547 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 371,900.8 | 0.3547 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 371,947.9 | 0.3547 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 371,946.0 | 0.3547 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 372,115.1 | 0.3549 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 371,904.2 | 0.3547 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 21,795.5 | 0.3547 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 21,806.4 | 0.3549 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 21,789.4 | 0.3546 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 5,833.6 | 0.3560 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5,833.0 | 0.3560 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 5,827.9 | 0.3557 |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 682,938.5 ns, 1,048,576 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 684,461.7 ns, 1,048,576 B

### `wild-logparse-quotedstring-grok` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 2,136.4 | 2,116.7 | 2,161.8 | 15.1 | 1.000x | 1.000x | - | - | 75 | 28.5 | 9.1 | 100% |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 2,137.7 | 2,109.3 | 2,168.1 | 19.3 | 1.001x | 1.001x | unchanged (within spread) | -0.17% (null control: program identical) | 75 | 28.5 | 9.1 | 100% |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 2,141.3 | 2,117.7 | 2,169.0 | 20.4 | 1.002x | 1.002x | unchanged (within spread) | +0.23% (null control: program identical) | 75 | 28.6 | 9.1 | 100% |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `lp-quoted-escaped`, 120.3 ns, 16 B; largest Δ: `lp-atomic-hit`, -3.7 ns (now 25.9 ns), 31 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `lp-quoted-escaped`, 120.9 ns, 16 B; largest Δ: `lp-atomic-hit`, +3.0 ns (now 29.6 ns), 31 B

### `wild-logparse-quotedstring-noatomic` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 1,905,018.8 | 0.4069 | 1,902,246.5 | 1,905,608.0 | 1,177.8 | 1.000x | 1.000x | unchanged (within spread) | -0.08% (null control: program identical) |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 1,906,494.6 | 0.4072 | 1,905,451.2 | 1,911,683.9 | 2,289.1 | 1.001x | 1.001x | unchanged (within spread) | +0.08% (null control: program identical) |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 1,906,620.2 | 0.4073 | 1,905,947.9 | 1,907,046.5 | 383.2 | 1.001x | 1.001x | - | - |

#### `wild-logparse-quotedstring-noatomic` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 559,653.9 | 0.5337 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 560,797.2 | 0.5348 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 560,629.7 | 0.5347 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 137,577.0 | 0.5248 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 138,351.2 | 0.5278 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 138,793.1 | 0.5295 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 34,788.2 | 0.5308 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 35,142.5 | 0.5362 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 34,949.0 | 0.5333 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 21,768.4 | 0.3543 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 21,763.5 | 0.3542 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 21,764.2 | 0.3542 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 5,822.4 | 0.3553 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5,819.4 | 0.3552 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 5,824.3 | 0.3555 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 1,474.4 | 0.3600 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,472.7 | 0.3595 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 1,475.2 | 0.3602 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 372,001.3 | 0.3548 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 372,144.7 | 0.3549 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 371,936.3 | 0.3547 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 371,796.3 | 0.3546 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 371,939.0 | 0.3547 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 371,842.9 | 0.3546 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 371,814.4 | 0.3546 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 372,016.0 | 0.3548 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 371,950.0 | 0.3547 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 21,798.9 | 0.3548 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 21,771.6 | 0.3544 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 21,771.0 | 0.3543 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 5,819.6 | 0.3552 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5,820.7 | 0.3552 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 5,822.8 | 0.3554 |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `t-1m`, 559,653.9 ns, 1,048,576 B; largest Δ: `t-256k`, -1,216.2 ns (now 137,577.0 ns), 262,144 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 560,797.2 ns, 1,048,576 B

### `wild-logparse-quotedstring-noatomic` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 1,580.1 | 1,530.0 | 1,586.0 | 21.2 | 1.000x | 1.000x | unchanged (within spread) | -0.11% (null control: program identical) | 75 | 21.1 | 9.1 | 100% |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 1,581.8 | 1,534.6 | 1,595.3 | 23.9 | 1.001x | 1.001x | - | - | 75 | 21.1 | 9.1 | 100% |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 1,588.6 | 1,535.7 | 1,594.0 | 21.4 | 1.005x | 1.005x | unchanged (within spread) | +0.54% (null control: program identical) | 75 | 21.2 | 9.1 | 100% |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `lp-quoted-escaped`, 58.0 ns, 16 B; largest Δ: `nu-mojibake`, -1.2 ns (now 13.0 ns), 7 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `lp-quoted-escaped`, 58.0 ns, 16 B; largest Δ: `sd-router-short`, +1.2 ns (now 13.9 ns), 6 B

### `wild-logparse-syslogbase-expanded` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 4,267,185.7 | 0.9115 | 4,248,720.1 | 4,268,292.2 | 7,524.5 | 1.000x | 1.000x | unchanged (within spread) | -0.06% (null control: program identical) |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 4,269,558.5 | 0.9120 | 4,251,252.0 | 4,276,193.2 | 8,535.8 | 1.001x | 1.001x | - | - |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 4,270,082.2 | 0.9121 | 4,261,158.8 | 4,275,124.4 | 5,353.6 | 1.001x | 1.001x | unchanged (within spread) | +0.07% (null control: program identical) |

#### `wild-logparse-syslogbase-expanded` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 3,217,877.4 | 3.0688 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 3,220,358.6 | 3.0712 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 3,218,713.6 | 3.0696 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 792,650.0 | 3.0237 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 794,024.2 | 3.0290 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 793,853.8 | 3.0283 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 192,415.8 | 2.9360 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 192,439.7 | 2.9364 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 192,501.2 | 2.9373 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,042.8 | 0.0170 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,041.0 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,044.6 | 0.0170 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 227.3 | 0.0139 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 228.7 | 0.0140 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 225.6 | 0.0138 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 8,160.7 | 1.9924 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 8,159.3 | 1.9920 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 8,147.4 | 1.9891 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,643.8 | 0.0168 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,642.4 | 0.0168 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,653.3 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,649.3 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,679.8 | 0.0169 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,634.8 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 17,651.1 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 17,658.8 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,670.2 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,037.8 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,035.7 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,039.3 | 0.0169 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 228.4 | 0.0139 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 228.2 | 0.0139 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 226.3 | 0.0138 |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 3,217,877.4 ns, 1,048,576 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `t-1m`, 3,218,713.6 ns, 1,048,576 B; largest Δ: `t-256k`, +1,203.7 ns (now 793,853.8 ns), 262,144 B

### `wild-logparse-syslogbase-expanded` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 1,610.6 | 1,603.7 | 1,618.9 | 5.4 | 1.000x | 1.000x | unchanged (within spread) | -0.05% (null control: program identical) | 75 | 21.5 | 9.1 | 100% |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 1,611.5 | 1,600.0 | 1,614.1 | 5.0 | 1.001x | 1.001x | unchanged (within spread) | -0.01% (null control: program identical) | 75 | 21.5 | 9.1 | 100% |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 1,611.7 | 1,600.4 | 1,628.0 | 11.0 | 1.001x | 1.001x | - | - | 75 | 21.5 | 9.1 | 100% |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `lp-syslog`, 583.4 ns, 56 B; largest Δ: `lp-atomic-hit`, +5.7 ns (now 55.9 ns), 31 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `lp-syslog`, 581.0 ns, 56 B; largest Δ: `lp-atomic-hit`, +0.7 ns (now 50.2 ns), 31 B

### `wild-logparse-winpath-grok` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 78,559.6 | 0.0168 | 78,527.4 | 78,574.0 | 15.5 | 1.000x | 1.000x | faster ×1.00 | -0.14% (null control: program identical) |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 78,561.0 | 0.0168 | 78,546.6 | 78,673.4 | 47.3 | 1.000x | 1.000x | unchanged (within spread) | +0.00% (null control: program identical) |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 78,671.5 | 0.0168 | 78,657.1 | 78,699.0 | 13.7 | 1.001x | 1.001x | - | - |

#### `wild-logparse-winpath-grok` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 17,637.0 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,629.7 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 17,685.8 | 0.0169 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 4,377.8 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 4,389.3 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 4,379.2 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 1,109.0 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,110.6 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 1,113.5 | 0.0170 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,036.7 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,037.3 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,041.5 | 0.0170 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 227.6 | 0.0139 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 227.1 | 0.0139 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 227.4 | 0.0139 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 60.9 | 0.0149 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 60.9 | 0.0149 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 61.2 | 0.0149 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,620.9 | 0.0168 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,610.5 | 0.0168 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,620.5 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,609.1 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,610.6 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,618.2 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 17,608.3 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,609.2 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 17,638.5 | 0.0168 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,037.0 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,038.2 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,037.4 | 0.0169 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 226.4 | 0.0138 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 227.4 | 0.0139 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 226.1 | 0.0138 |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 17,637.0 ns, 1,048,576 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `t-1m`, 17,629.7 ns, 1,048,576 B; largest Δ: `t-256k`, +11.5 ns (now 4,389.3 ns), 262,144 B

### `wild-logparse-winpath-grok` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 948.0 | 945.2 | 949.6 | 1.6 | 1.000x | 1.000x | unchanged (within spread) | -0.04% (null control: program identical) | 75 | 12.6 | 9.1 | 100% |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 948.4 | 945.7 | 949.1 | 1.5 | 1.000x | 1.000x | - | - | 75 | 12.6 | 9.1 | 100% |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 949.1 | 946.7 | 949.4 | 1.0 | 1.001x | 1.001x | unchanged (within spread) | +0.11% (null control: program identical) | 75 | 12.7 | 9.1 | 100% |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `lp-winpath-reserved`, 76.1 ns, 24 B; largest Δ: `lp-winpath`, +0.8 ns (now 75.7 ns), 22 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `lp-winpath-reserved`, 75.8 ns, 24 B; largest Δ: `lp-winpath`, -0.7 ns (now 75.0 ns), 22 B

### `wild-secrets-aws-access-key-id` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 158,042.2 | 0.0338 | 157,755.1 | 158,433.6 | 216.7 | 1.000x | 1.000x | unchanged (within spread) | -0.21% (null control: program identical) |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 158,379.7 | 0.0338 | 158,242.0 | 158,538.1 | 111.6 | 1.002x | 1.002x | - | - |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 158,471.1 | 0.0338 | 158,274.3 | 158,667.9 | 136.5 | 1.003x | 1.003x | unchanged (within spread) | +0.27% (null control: program identical) |

#### `wild-secrets-aws-access-key-id` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 54,950.1 | 0.0524 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 55,345.5 | 0.0528 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 55,284.9 | 0.0527 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 11,219.1 | 0.0428 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 11,214.4 | 0.0428 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 11,275.6 | 0.0430 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 2,289.8 | 0.0349 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 2,281.2 | 0.0348 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 2,267.2 | 0.0346 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,045.5 | 0.0170 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,044.5 | 0.0170 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,047.9 | 0.0171 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 228.9 | 0.0140 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 229.2 | 0.0140 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 229.3 | 0.0140 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 63.2 | 0.0154 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 63.7 | 0.0156 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 63.8 | 0.0156 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 29,018.9 | 0.0277 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 28,923.4 | 0.0276 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 29,048.0 | 0.0277 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 29,009.9 | 0.0277 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 28,954.8 | 0.0276 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 28,967.4 | 0.0276 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 28,939.3 | 0.0276 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 29,014.0 | 0.0277 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 29,008.0 | 0.0277 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,039.4 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,039.3 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,039.7 | 0.0169 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 229.6 | 0.0140 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 230.1 | 0.0140 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 229.9 | 0.0140 |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 54,950.1 ns, 1,048,576 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 55,284.9 ns, 1,048,576 B

### `wild-secrets-aws-access-key-id` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 1,363.3 | 1,361.7 | 1,364.4 | 0.9 | 1.000x | 1.000x | - | - | 75 | 18.2 | 9.1 | 100% |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 1,364.3 | 1,363.1 | 1,365.8 | 1.0 | 1.001x | 1.001x | unchanged (within spread) | -0.01% (null control: program identical) | 75 | 18.2 | 9.1 | 100% |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 1,364.4 | 1,361.7 | 1,365.7 | 1.5 | 1.001x | 1.001x | unchanged (within spread) | +0.08% (null control: program identical) | 75 | 18.2 | 9.1 | 100% |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `sec-github-pat`, 163.8 ns, 93 B; largest Δ: `lp-syslog`, +0.3 ns (now 29.1 ns), 56 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `sec-github-pat`, 163.7 ns, 93 B; largest Δ: `waf-dbnames`, +0.3 ns (now 16.2 ns), 39 B

### `wild-secrets-github-pat` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 180,218.3 | 0.0385 | 180,180.5 | 180,294.0 | 44.6 | 1.000x | 1.000x | unchanged (within spread) | -0.02% (null control: program identical) |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 180,251.3 | 0.0385 | 180,142.2 | 180,305.4 | 60.0 | 1.000x | 1.000x | - | - |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 180,427.6 | 0.0385 | 180,166.2 | 180,541.3 | 125.0 | 1.001x | 1.001x | unchanged (within spread) | +0.12% (null control: program identical) |

#### `wild-secrets-github-pat` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 102,363.5 | 0.0976 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 102,381.0 | 0.0976 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 102,466.8 | 0.0977 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 18,833.0 | 0.0718 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 18,846.1 | 0.0719 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 18,856.0 | 0.0719 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 3,446.2 | 0.0526 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 3,454.0 | 0.0527 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 3,452.2 | 0.0527 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,038.4 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,037.7 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,036.9 | 0.0169 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 224.5 | 0.0137 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 224.8 | 0.0137 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 225.1 | 0.0137 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 144.1 | 0.0352 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 144.5 | 0.0353 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 143.9 | 0.0351 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,657.3 | 0.0168 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,632.0 | 0.0168 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,636.2 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,636.8 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,631.3 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,632.5 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 17,643.5 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 17,610.3 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,649.1 | 0.0168 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,037.0 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,037.3 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,037.5 | 0.0169 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 223.4 | 0.0136 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 224.7 | 0.0137 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 223.8 | 0.0137 |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `t-1m`, 102,363.5 ns, 1,048,576 B; largest Δ: `t-tail-txt-1m`, +33.2 ns (now 17,643.5 ns), 1,048,527 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 102,466.8 ns, 1,048,576 B

### `wild-secrets-github-pat` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 838.9 | 836.8 | 840.9 | 1.4 | 1.000x | 1.000x | faster ×1.01 | -0.99% (null control: program identical) | 75 | 11.2 | 9.1 | 100% |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 847.3 | 842.6 | 849.0 | 2.2 | 1.010x | 1.010x | unchanged (within spread) | -0.07% (null control: program identical) | 75 | 11.3 | 9.1 | 100% |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 847.9 | 843.7 | 851.3 | 3.0 | 1.011x | 1.011x | - | - | 75 | 11.3 | 9.1 | 100% |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `sec-github-pat`, 288.4 ns, 93 B; largest Δ: `waf-union`, -0.6 ns (now 9.8 ns), 43 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `sec-github-pat`, 288.6 ns, 93 B; largest Δ: `sd-dollar-nl`, -0.2 ns (now 4.7 ns), 7 B

### `wild-secrets-slack-webhook-url` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 396,610.6 | 0.0847 | 396,530.8 | 396,751.2 | 72.0 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 396,636.1 | 0.0847 | 396,616.8 | 396,715.9 | 37.1 | 1.000x | 1.000x | unchanged (within spread) | +0.01% (null control: program identical) |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 396,735.2 | 0.0847 | 396,548.7 | 396,814.0 | 88.6 | 1.000x | 1.000x | unchanged (within spread) | +0.02% (null control: program identical) |

#### `wild-secrets-slack-webhook-url` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 261,774.7 | 0.2496 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 261,783.2 | 0.2497 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 261,815.1 | 0.2497 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 64,334.6 | 0.2454 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 64,362.6 | 0.2455 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 64,381.0 | 0.2456 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 14,806.3 | 0.2259 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 14,815.6 | 0.2261 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 14,811.3 | 0.2260 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,039.0 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,037.1 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,044.6 | 0.0170 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 226.5 | 0.0138 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 226.3 | 0.0138 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 226.7 | 0.0138 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 203.5 | 0.0497 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 204.4 | 0.0499 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 204.0 | 0.0498 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,638.1 | 0.0168 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,647.7 | 0.0168 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,656.2 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,658.3 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,642.0 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,642.8 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 17,619.5 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 17,650.7 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,654.7 | 0.0168 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,035.5 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,037.4 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,037.2 | 0.0169 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 226.3 | 0.0138 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 226.7 | 0.0138 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 227.9 | 0.0139 |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `t-1m`, 261,783.2 ns, 1,048,576 B; largest Δ: `t-tail-txt-1m`, +31.2 ns (now 17,650.7 ns), 1,048,527 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 261,815.1 ns, 1,048,576 B

### `wild-secrets-slack-webhook-url` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 1,140.3 | 1,137.1 | 1,143.1 | 2.1 | 1.000x | 1.000x | unchanged (within spread) | -0.32% (null control: program identical) | 75 | 15.2 | 9.1 | 100% |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 1,142.6 | 1,139.9 | 1,146.8 | 2.6 | 1.002x | 1.002x | unchanged (within spread) | +0.20% (null control: program identical) | 75 | 15.2 | 9.1 | 100% |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 1,144.0 | 1,139.9 | 1,150.3 | 3.9 | 1.003x | 1.003x | - | - | 75 | 15.3 | 9.1 | 100% |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `sec-slack-webhook`, 416.7 ns, 81 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `sec-slack-webhook`, 419.3 ns, 81 B

### `wild-secrets-username-password-pair` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 79,071.4 | 0.0169 | 79,011.2 | 79,119.3 | 38.1 | 1.000x | 1.000x | unchanged (within spread) | -0.11% (null control: program identical) |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 79,089.8 | 0.0169 | 79,026.9 | 79,143.3 | 39.6 | 1.000x | 1.000x | unchanged (within spread) | +0.02% (null control: program identical) |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 79,156.9 | 0.0169 | 79,051.3 | 79,186.7 | 48.1 | 1.001x | 1.001x | - | - |

#### `wild-secrets-username-password-pair` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 17,650.3 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,623.3 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 17,621.0 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 4,376.3 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 4,379.7 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 4,410.4 | 0.0168 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 1,109.2 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,114.1 | 0.0170 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 1,110.9 | 0.0170 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,037.2 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,037.6 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,037.6 | 0.0169 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 225.9 | 0.0138 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 225.7 | 0.0138 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 226.1 | 0.0138 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 520.0 | 0.1269 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 519.2 | 0.1268 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 524.3 | 0.1280 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,634.0 | 0.0168 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,655.6 | 0.0168 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,636.9 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,614.5 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,628.0 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,660.1 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 17,624.3 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,634.5 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 17,652.0 | 0.0168 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,034.7 | 0.0168 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,038.6 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,035.2 | 0.0168 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 226.8 | 0.0138 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 226.6 | 0.0138 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 227.3 | 0.0139 |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `t-1m`, 17,650.3 ns, 1,048,576 B; largest Δ: `t-tail-space-1m`, -45.6 ns (now 17,614.5 ns), 1,048,522 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `t-tail-digits-1m`, 17,655.6 ns, 1,048,522 B; largest Δ: `t-1m`, -27.1 ns (now 17,623.3 ns), 1,048,576 B

### `wild-secrets-username-password-pair` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 1,052.0 | 1,051.9 | 1,054.0 | 0.8 | 1.000x | 1.000x | unchanged (within spread) | -0.13% (null control: program identical) | 75 | 14.0 | 9.1 | 100% |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 1,052.2 | 1,051.4 | 1,053.2 | 0.7 | 1.000x | 1.000x | - | - | 75 | 14.0 | 9.1 | 100% |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 1,053.3 | 1,052.9 | 1,094.6 | 16.5 | 1.001x | 1.001x | unchanged (within spread) | +0.11% (null control: program identical) | 75 | 14.0 | 9.1 | 100% |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `sec-userpass`, 243.2 ns, 33 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `sec-userpass`, 244.6 ns, 33 B

### `wild-semdiv-altorder-foo-foobar-rustregex` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 1,266,274.2 | 0.2705 | 1,265,401.4 | 1,266,903.0 | 486.2 | 1.000x | 1.000x | faster ×1.00 | -0.12% (null control: program identical) |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 1,266,698.5 | 0.2706 | 1,266,022.8 | 1,268,328.9 | 771.4 | 1.000x | 1.000x | - | - |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 1,267,786.7 | 0.2708 | 1,267,067.9 | 1,268,968.0 | 694.8 | 1.001x | 1.001x | unchanged (within spread) | +0.09% (null control: program identical) |

#### `wild-semdiv-altorder-foo-foobar-rustregex` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 282,048.9 | 0.2690 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 282,213.6 | 0.2691 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 282,471.2 | 0.2694 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 58,920.3 | 0.2248 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 58,932.6 | 0.2248 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 58,952.3 | 0.2249 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 11,478.3 | 0.1751 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 11,433.1 | 0.1745 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 11,474.3 | 0.1751 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 21,539.9 | 0.3506 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 21,676.4 | 0.3528 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 21,543.8 | 0.3506 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5,313.3 | 0.3243 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 5,319.4 | 0.3246 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 5,308.4 | 0.3240 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 942.2 | 0.2300 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 934.2 | 0.2281 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 940.2 | 0.2295 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 294,981.9 | 0.2813 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 295,029.9 | 0.2814 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 295,154.9 | 0.2815 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 294,849.5 | 0.2812 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 294,905.4 | 0.2813 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 295,031.7 | 0.2814 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 294,794.5 | 0.2812 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 294,927.3 | 0.2813 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 295,189.1 | 0.2815 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,039.4 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,034.3 | 0.0168 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,039.8 | 0.0169 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 229.5 | 0.0140 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 223.5 | 0.0136 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 224.3 | 0.0137 |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `t-tail-digits-1m`, 294,981.9 ns, 1,048,522 B; largest Δ: `t-1m`, -422.3 ns (now 282,048.9 ns), 1,048,576 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `t-tail-txt-1m`, 295,189.1 ns, 1,048,527 B

### `wild-semdiv-altorder-foo-foobar-rustregex` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 659.7 | 659.5 | 660.4 | 0.3 | 1.000x | 1.000x | - | - | 75 | 8.8 | 9.1 | 100% |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 659.9 | 659.8 | 660.5 | 0.2 | 1.000x | 1.000x | unchanged (within spread) | +0.03% (null control: program identical) | 75 | 8.8 | 9.1 | 100% |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 660.0 | 659.3 | 661.8 | 0.9 | 1.000x | 1.000x | unchanged (within spread) | +0.01% (null control: program identical) | 75 | 8.8 | 9.1 | 100% |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `sec-slack-webhook`, 13.5 ns, 81 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `sec-slack-webhook`, 13.5 ns, 81 B; largest Δ: `waf-dbnames`, +0.1 ns (now 13.3 ns), 39 B

### `wild-semdiv-dollar-trailing-newline-pcre2` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 104.1 | 0.0000 | 103.5 | 104.2 | 0.3 | 1.000x | 1.000x | unchanged (within spread) | -0.45% (null control: program identical) |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 104.2 | 0.0000 | 103.8 | 104.6 | 0.3 | 1.001x | 1.001x | - | - |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 104.6 | 0.0000 | 103.7 | 106.4 | 0.9 | 1.005x | 1.005x | unchanged (within spread) | +0.35% (null control: program identical) |

#### `wild-semdiv-dollar-trailing-newline-pcre2` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 11.3 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 11.3 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 11.4 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 11.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 11.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 11.5 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 11.4 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 11.3 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 11.9 | 0.0002 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 8.7 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 8.7 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 8.8 | 0.0001 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 8.8 | 0.0005 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 8.8 | 0.0005 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 8.7 | 0.0005 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 8.8 | 0.0021 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 8.8 | 0.0021 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 8.8 | 0.0022 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 8.7 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 8.7 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 8.8 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 8.8 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 8.7 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 8.7 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 8.8 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 8.7 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 8.8 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 8.8 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 8.7 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 8.7 | 0.0005 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 8.8 | 0.0005 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 8.7 | 0.0005 |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `t-64k`, 11.4 ns, 65,536 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `t-64k`, 11.9 ns, 65,536 B

### `wild-semdiv-dollar-trailing-newline-pcre2` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 644.7 | 641.3 | 656.9 | 5.4 | 1.000x | 1.000x | unchanged (within spread) | -0.15% (null control: program identical) | 75 | 8.6 | 9.1 | 100% |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 645.7 | 641.7 | 661.9 | 7.1 | 1.002x | 1.002x | unchanged (within spread) | -0.99% (null control: program identical) | 75 | 8.6 | 9.1 | 100% |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 652.1 | 647.1 | 658.4 | 4.3 | 1.012x | 1.012x | - | - | 75 | 8.7 | 9.1 | 100% |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `rec-parens-unbalanced`, 10.7 ns, 5 B; largest Δ: `v-us-zip`, +0.2 ns (now 8.7 ns), 5 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `rec-parens-unbalanced`, 10.7 ns, 5 B; largest Δ: `br-tag-pair`, -0.2 ns (now 8.5 ns), 18 B

### `wild-semdiv-empty-alt-repeat-pcre2` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 18,734,418.3 | 4.0017 | 18,721,982.0 | 19,087,972.5 | 139,651.6 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 18,764,666.7 | 4.0082 | 18,747,196.8 | 18,826,962.3 | 28,506.6 | 1.002x | 1.002x | unchanged (within spread) | -0.25% (null control: program identical) |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 18,811,387.5 | 4.0182 | 18,730,151.4 | 18,847,241.9 | 40,991.1 | 1.004x | 1.004x | unchanged (within spread) | +0.41% (null control: program identical) |

#### `wild-semdiv-empty-alt-repeat-pcre2` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 5,337,072.9 | 5.0898 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5,337,033.6 | 5.0898 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 5,353,896.6 | 5.1059 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 1,298,030.0 | 4.9516 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,309,841.6 | 4.9966 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 1,305,320.4 | 4.9794 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 312,377.6 | 4.7665 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 312,717.5 | 4.7717 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 314,548.4 | 4.7996 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 21,461.6 | 0.3493 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 21,483.9 | 0.3497 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 21,471.5 | 0.3495 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 5,747.4 | 0.3508 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5,760.2 | 0.3516 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 5,754.1 | 0.3512 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 71,032.3 | 17.3419 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 70,887.7 | 17.3066 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 71,004.3 | 17.3350 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 3,882,266.8 | 3.7026 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 3,890,297.0 | 3.7103 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 3,898,345.7 | 3.7179 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 3,894,476.4 | 3.7143 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 3,903,300.2 | 3.7227 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 3,885,300.5 | 3.7055 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 3,896,624.1 | 3.7163 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 3,899,112.2 | 3.7187 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 3,907,184.0 | 3.7264 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 21,485.5 | 0.3497 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 21,474.4 | 0.3495 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 21,480.1 | 0.3496 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 5,755.2 | 0.3512 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5,749.1 | 0.3509 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 5,745.1 | 0.3506 |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `t-1m`, 5,337,033.6 ns, 1,048,576 B; largest Δ: `t-tail-space-1m`, +17,999.7 ns (now 3,903,300.2 ns), 1,048,522 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 5,353,896.6 ns, 1,048,576 B

### `wild-semdiv-empty-alt-repeat-pcre2` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 2,899.3 | 2,891.6 | 2,921.5 | 11.1 | 1.000x | 1.000x | unchanged (within spread) | -0.04% (null control: program identical) | 75 | 38.7 | 9.1 | 100% |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 2,900.6 | 2,877.4 | 2,913.5 | 11.8 | 1.000x | 1.000x | - | - | 75 | 38.7 | 9.1 | 100% |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 2,907.2 | 2,888.4 | 2,927.6 | 16.9 | 1.003x | 1.003x | unchanged (within spread) | +0.27% (null control: program identical) | 75 | 38.8 | 9.1 | 100% |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `sd-empty-alt-hit`, 927.7 ns, 61 B; largest Δ: `sec-slack-webhook`, +1.6 ns (now 59.8 ns), 81 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `sd-empty-alt-hit`, 936.6 ns, 61 B

### `wild-validator-email-owasp` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 46,115.4 | 0.0099 | 46,112.7 | 46,133.7 | 8.0 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 46,129.7 | 0.0099 | 46,111.6 | 46,164.2 | 19.1 | 1.000x | 1.000x | unchanged (within spread) | -0.01% (null control: program identical) |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 46,133.4 | 0.0099 | 46,129.0 | 46,135.2 | 2.2 | 1.000x | 1.000x | slower ×1.00 | +0.04% (null control: program identical) |

#### `wild-validator-email-owasp` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 13.6 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 14.7 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 15.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 11.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 11.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 11.5 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 11.4 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 11.7 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 11.5 | 0.0002 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 36,307.7 | 0.5909 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 36,309.1 | 0.5910 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 36,318.7 | 0.5911 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 9,715.3 | 0.5929 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9,716.0 | 0.5930 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 9,718.4 | 0.5931 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 6.2 | 0.0015 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 6.2 | 0.0015 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 6.2 | 0.0015 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 12.5 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 12.1 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 12.3 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 10.6 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 12.0 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 10.7 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 12.8 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 6.2 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 6.2 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 6.2 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 6.2 | 0.0004 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 6.2 | 0.0004 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 6.2 | 0.0004 |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `t-evil-match-60k`, 36,309.1 ns, 61,440 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `t-evil-match-60k`, 36,318.7 ns, 61,440 B

### `wild-validator-email-owasp` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 1,049.2 | 1,046.1 | 1,053.7 | 2.5 | 1.000x | 1.000x | - | - | 75 | 14.0 | 9.1 | 100% |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 1,049.9 | 1,047.1 | 1,051.7 | 1.5 | 1.001x | 1.001x | unchanged (within spread) | -0.08% (null control: program identical) | 75 | 14.0 | 9.1 | 100% |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 1,050.7 | 1,047.2 | 3,586.6 | 1,015.0 | 1.001x | 1.001x | unchanged (within spread) | +0.14% (null control: program identical) | 75 | 14.0 | 9.1 | 100% |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `sec-github-pat`, 72.8 ns, 93 B; largest Δ: `rd-numeric-id-hit`, +1.0 ns (now 9.7 ns), 4 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `sec-github-pat`, 73.0 ns, 93 B; largest Δ: `rd-numeric-id-hit`, -2.0 ns (now 8.7 ns), 4 B

### `wild-validator-ipv4-owasp` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 102.5 | 0.0000 | 102.4 | 102.6 | 0.1 | 1.000x | 1.000x | unchanged (within spread) | -0.05% (null control: program identical) |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 102.5 | 0.0000 | 102.5 | 102.6 | 0.0 | 1.000x | 1.000x | unchanged (within spread) | -0.03% (null control: program identical) |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 102.6 | 0.0000 | 102.4 | 102.6 | 0.1 | 1.001x | 1.001x | - | - |

#### `wild-validator-ipv4-owasp` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.3 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 9.3 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 9.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 9.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 9.3 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.3 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 9.4 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 9.4 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.3 | 0.0002 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 9.3 | 0.0002 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 9.3 | 0.0002 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.3 | 0.0006 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 9.3 | 0.0006 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 9.3 | 0.0006 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.3 | 0.0023 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 9.3 | 0.0023 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 9.3 | 0.0023 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.3 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 9.3 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 9.3 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.3 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 9.3 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 9.3 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.3 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 9.3 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 9.3 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.3 | 0.0002 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 9.3 | 0.0002 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 9.3 | 0.0002 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.3 | 0.0006 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 9.3 | 0.0006 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 9.3 | 0.0006 |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `t-64k`, 9.3 ns, 65,536 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `t-64k`, 9.4 ns, 65,536 B; largest Δ: `t-256k`, -0.0 ns (now 9.3 ns), 262,144 B

### `wild-validator-ipv4-owasp` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 822.5 | 822.1 | 822.9 | 0.3 | 1.000x | 1.000x | - | - | 75 | 11.0 | 9.1 | 100% |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 822.6 | 822.2 | 941.3 | 47.5 | 1.000x | 1.000x | unchanged (within spread) | -0.02% (null control: program identical) | 75 | 11.0 | 9.1 | 100% |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 822.7 | 822.1 | 823.4 | 0.5 | 1.000x | 1.000x | unchanged (within spread) | +0.03% (null control: program identical) | 75 | 11.0 | 9.1 | 100% |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `v-ipv4`, 82.7 ns, 11 B; largest Δ: `br-palindrome`, +0.2 ns (now 13.0 ns), 6 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `v-ipv4`, 82.7 ns, 11 B; largest Δ: `rd-date-hit`, -0.1 ns (now 11.8 ns), 5 B

### `wild-validator-us-zip-owasp` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 100.8 | 0.0000 | 100.8 | 100.9 | 0.0 | 1.000x | 1.000x | unchanged (within spread) | -0.01% (null control: program identical) |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 100.8 | 0.0000 | 100.8 | 102.1 | 0.5 | 1.000x | 1.000x | unchanged (within spread) | -0.25% (null control: program identical) |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 101.1 | 0.0000 | 101.0 | 134.3 | 13.3 | 1.003x | 1.003x | - | - |

#### `wild-validator-us-zip-owasp` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.2 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 9.2 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 9.2 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.2 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 9.2 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 9.2 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.2 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 9.2 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 9.2 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.2 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 9.2 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 9.2 | 0.0001 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.2 | 0.0006 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 9.2 | 0.0006 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 9.2 | 0.0006 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.2 | 0.0022 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 9.2 | 0.0022 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 9.2 | 0.0022 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.2 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 9.2 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 9.2 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.2 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 9.2 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 9.2 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.2 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 9.2 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 9.2 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.2 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 9.2 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 9.2 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9.1 | 0.0006 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 9.2 | 0.0006 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 9.2 | 0.0006 |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `t-64k`, 9.2 ns, 65,536 B; largest Δ: `t-evil-nearmiss-16k`, -0.0 ns (now 9.2 ns), 16,385 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `t-64k`, 9.2 ns, 65,536 B; largest Δ: `t-evil-match-60k`, -0.0 ns (now 9.2 ns), 61,440 B

### `wild-validator-us-zip-owasp` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 747.0 | 745.8 | 748.3 | 0.8 | 1.000x | 1.000x | - | - | 75 | 10.0 | 9.1 | 100% |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 747.5 | 746.5 | 749.0 | 0.9 | 1.001x | 1.001x | unchanged (within spread) | -0.04% (null control: program identical) | 75 | 10.0 | 9.1 | 100% |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 747.7 | 745.6 | 766.8 | 8.0 | 1.001x | 1.001x | unchanged (within spread) | +0.10% (null control: program identical) | 75 | 10.0 | 9.1 | 100% |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `v-us-zip-plus4`, 32.5 ns, 10 B; largest Δ: `br-palindrome`, +0.8 ns (now 15.7 ns), 6 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `v-us-zip-plus4`, 32.6 ns, 10 B; largest Δ: `rd-numeric-id-hit`, +0.6 ns (now 12.4 ns), 4 B

### `wild-validator-uuid-grok` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 139,194.4 | 0.0297 | 139,080.7 | 139,806.0 | 276.6 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 139,472.7 | 0.0298 | 139,038.1 | 139,624.6 | 209.9 | 1.002x | 1.002x | unchanged (within spread) | -0.04% (null control: program identical) |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 139,530.1 | 0.0298 | 139,091.2 | 139,625.4 | 194.7 | 1.002x | 1.002x | unchanged (within spread) | +0.24% (null control: program identical) |

#### `wild-validator-uuid-grok` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 69,135.9 | 0.0659 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 69,287.9 | 0.0661 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 69,458.5 | 0.0662 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 11,823.3 | 0.0451 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 11,999.6 | 0.0458 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 11,879.8 | 0.0453 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 2,419.6 | 0.0369 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 2,429.2 | 0.0371 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 2,406.8 | 0.0367 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,039.9 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,035.9 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,036.6 | 0.0169 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 225.4 | 0.0138 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 225.3 | 0.0137 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 225.4 | 0.0138 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 404.1 | 0.0987 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 405.2 | 0.0989 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 402.7 | 0.0983 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,649.1 | 0.0168 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,618.4 | 0.0168 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,650.4 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,669.2 | 0.0169 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,623.4 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,610.5 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 17,660.6 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,597.3 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 17,623.7 | 0.0168 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,037.4 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,038.5 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,041.1 | 0.0169 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 224.0 | 0.0137 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 224.3 | 0.0137 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 224.3 | 0.0137 |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 69,287.9 ns, 1,048,576 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 69,458.5 ns, 1,048,576 B

### `wild-validator-uuid-grok` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 646.3 | 645.7 | 648.4 | 1.0 | 1.000x | 1.000x | - | - | 75 | 8.6 | 9.1 | 100% |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 647.7 | 645.1 | 653.1 | 2.7 | 1.002x | 1.002x | unchanged (within spread) | -0.11% (null control: program identical) | 75 | 8.6 | 9.1 | 100% |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 648.4 | 646.2 | 653.0 | 2.3 | 1.003x | 1.003x | unchanged (within spread) | +0.32% (null control: program identical) | 75 | 8.6 | 9.1 | 100% |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `v-uuid-valid`, 56.1 ns, 36 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `v-uuid-valid`, 56.8 ns, 36 B

### `wild-waf-crs-942140-dbnames` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 12,487,327.8 | 2.6673 | 12,475,316.1 | 12,502,849.2 | 9,494.9 | 1.000x | 1.000x | unchanged (within spread) | -0.14% (null control: program identical) |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 12,505,181.7 | 2.6711 | 12,495,987.5 | 12,508,038.8 | 4,112.1 | 1.001x | 1.001x | unchanged (within spread) | -0.01% (null control: program identical) |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 12,505,847.0 | 2.6713 | 12,486,186.5 | 12,522,879.0 | 12,861.8 | 1.001x | 1.001x | - | - |

#### `wild-waf-crs-942140-dbnames` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 2,961,142.2 | 2.8240 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 2,962,552.0 | 2.8253 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 2,960,231.3 | 2.8231 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 739,287.1 | 2.8202 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 739,003.7 | 2.8191 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 740,810.2 | 2.8260 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 180,882.1 | 2.7600 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 181,175.9 | 2.7645 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 181,418.6 | 2.7682 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 118,862.9 | 1.9346 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 119,418.4 | 1.9437 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 120,049.1 | 1.9539 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 33,141.7 | 2.0227 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 32,594.8 | 1.9893 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 32,836.1 | 2.0040 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 7,704.7 | 1.8810 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 7,498.8 | 1.8308 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 7,467.0 | 1.8230 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 2,808,425.8 | 2.6785 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 2,811,625.2 | 2.6815 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 2,811,639.0 | 2.6815 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 2,807,403.1 | 2.6775 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 2,809,526.6 | 2.6795 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 2,807,320.7 | 2.6774 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 2,806,473.0 | 2.6766 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 2,808,768.5 | 2.6788 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 2,811,368.7 | 2.6813 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 22,225.9 | 0.3617 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 21,826.1 | 0.3552 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 21,812.4 | 0.3550 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5,819.8 | 0.3552 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 5,814.7 | 0.3549 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 5,826.0 | 0.3556 |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `t-1m`, 2,961,142.2 ns, 1,048,576 B; largest Δ: `t-tail-digits-1m`, -3,199.5 ns (now 2,808,425.8 ns), 1,048,522 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `t-1m`, 2,962,552.0 ns, 1,048,576 B; largest Δ: `t-tail-txt-1m`, -2,600.2 ns (now 2,808,768.5 ns), 1,048,527 B

### `wild-waf-crs-942140-dbnames` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 1,994.1 | 1,992.2 | 1,999.1 | 2.4 | 1.000x | 1.000x | unchanged (within spread) | -0.05% (null control: program identical) | 75 | 26.6 | 9.1 | 100% |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 1,995.2 | 1,992.3 | 2,008.2 | 5.8 | 1.001x | 1.001x | - | - | 75 | 26.6 | 9.1 | 100% |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 2,000.7 | 1,987.7 | 2,006.7 | 6.5 | 1.003x | 1.003x | unchanged (within spread) | +0.33% (null control: program identical) | 75 | 26.7 | 9.1 | 100% |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `sec-github-pat`, 192.1 ns, 93 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `sec-github-pat`, 192.2 ns, 93 B; largest Δ: `la-float-bound`, -1.2 ns (now 19.5 ns), 13 B

### `wild-waf-crs-942160-sleep-benchmark` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 1,321,382.8 | 0.2823 | 1,317,951.4 | 1,325,890.5 | 2,770.4 | 1.000x | 1.000x | unchanged (within spread) | -0.71% (null control: program identical) |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 1,323,472.7 | 0.2827 | 1,321,104.2 | 1,334,370.6 | 5,007.4 | 1.002x | 1.002x | unchanged (within spread) | +0.16% (null control: program identical) |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 1,330,793.1 | 0.2843 | 1,323,675.8 | 1,346,163.7 | 7,901.4 | 1.007x | 1.007x | - | - |

#### `wild-waf-crs-942160-sleep-benchmark` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 961,048.9 | 0.9165 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 964,795.2 | 0.9201 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 968,268.4 | 0.9234 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 240,749.2 | 0.9184 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 240,125.7 | 0.9160 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 241,006.9 | 0.9194 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 63,602.4 | 0.9705 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 63,140.7 | 0.9634 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 62,737.3 | 0.9573 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,036.9 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,039.4 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,036.6 | 0.0169 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 223.3 | 0.0136 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 222.8 | 0.0136 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 222.8 | 0.0136 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 59.2 | 0.0145 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 59.3 | 0.0145 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 59.2 | 0.0145 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,618.0 | 0.0168 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,659.7 | 0.0168 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,657.4 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,652.4 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,634.6 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,655.0 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 17,630.8 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,628.5 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 17,651.9 | 0.0168 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,034.3 | 0.0168 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,040.6 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,034.6 | 0.0168 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 226.5 | 0.0138 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 224.3 | 0.0137 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 224.8 | 0.0137 |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 961,048.9 ns, 1,048,576 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 964,795.2 ns, 1,048,576 B

### `wild-waf-crs-942160-sleep-benchmark` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 684.3 | 683.5 | 684.9 | 0.5 | 1.000x | 1.000x | - | - | 75 | 9.1 | 9.1 | 100% |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 684.9 | 683.4 | 696.0 | 4.7 | 1.001x | 1.001x | unchanged (within spread) | +0.09% (null control: program identical) | 75 | 9.1 | 9.1 | 100% |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 686.2 | 684.4 | 686.9 | 1.1 | 1.003x | 1.003x | unchanged (within spread) | +0.19% (null control: program identical) | 75 | 9.1 | 9.1 | 100% |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `waf-concat`, 44.7 ns, 48 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `waf-concat`, 45.0 ns, 48 B

### `wild-waf-crs-942270-union-select` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 1,966,373.0 | 0.4200 | 1,962,810.4 | 1,967,667.9 | 2,005.8 | 1.000x | 1.000x | unchanged (within spread) | -0.02% (null control: program identical) |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 1,966,573.9 | 0.4201 | 1,963,902.4 | 1,967,914.4 | 1,320.0 | 1.000x | 1.000x | - | - |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 1,966,668.2 | 0.4201 | 1,965,727.3 | 1,967,345.2 | 526.0 | 1.000x | 1.000x | unchanged (within spread) | +0.00% (null control: program identical) |

#### `wild-waf-crs-942270-union-select` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 365,493.0 | 0.3486 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 365,029.7 | 0.3481 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 364,966.9 | 0.3481 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 83,215.5 | 0.3174 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 83,111.5 | 0.3170 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 83,161.7 | 0.3172 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,107.3 | 0.2610 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 17,092.9 | 0.2608 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 17,049.1 | 0.2601 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 27,255.6 | 0.4436 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 27,335.8 | 0.4449 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 27,331.5 | 0.4448 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 6,739.3 | 0.4113 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 6,765.1 | 0.4129 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 6,765.5 | 0.4129 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,350.1 | 0.3296 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 1,352.9 | 0.3303 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 1,345.9 | 0.3286 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 487,783.8 | 0.4652 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 487,878.9 | 0.4653 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 487,809.9 | 0.4652 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 487,062.0 | 0.4645 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 487,819.3 | 0.4652 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 487,849.7 | 0.4653 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 487,162.5 | 0.4646 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 487,665.7 | 0.4651 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 487,731.5 | 0.4652 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 2,066.9 | 0.0336 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 2,073.0 | 0.0337 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 2,066.9 | 0.0336 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 444.1 | 0.0271 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 444.2 | 0.0271 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 444.4 | 0.0271 |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `t-tail-digits-1m`, 487,783.8 ns, 1,048,522 B; largest Δ: `t-tail-space-1m`, -787.7 ns (now 487,062.0 ns), 1,048,522 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `t-tail-space-1m`, 487,849.7 ns, 1,048,522 B; largest Δ: `t-tail-digits-1m`, -69.0 ns (now 487,809.9 ns), 1,048,522 B

### `wild-waf-crs-942270-union-select` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 994.5 | 993.0 | 996.8 | 1.3 | 1.000x | 1.000x | unchanged (within spread) | -0.07% (null control: program identical) | 75 | 13.3 | 9.1 | 100% |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 995.0 | 993.4 | 997.0 | 1.2 | 1.001x | 1.001x | - | - | 75 | 13.3 | 9.1 | 100% |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 995.1 | 994.9 | 1,001.0 | 2.3 | 1.001x | 1.001x | unchanged (within spread) | +0.01% (null control: program identical) | 75 | 13.3 | 9.1 | 100% |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `waf-union`, 85.6 ns, 43 B; largest Δ: `waf-concat`, -1.1 ns (now 39.1 ns), 48 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `waf-union`, 85.3 ns, 43 B

### `wild-waf-crs-942360-concat-sqli` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 36,610,058.7 | 7.8200 | 36,483,151.4 | 36,640,685.3 | 68,187.7 | 1.000x | 1.000x | unchanged (within spread) | -0.07% (null control: program identical) |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 36,636,535.5 | 7.8257 | 36,455,173.6 | 37,844,961.6 | 567,957.2 | 1.001x | 1.001x | unchanged (within spread) | -3.16% (null control: program identical) |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 37,830,350.9 | 8.0807 | 36,451,591.0 | 38,005,964.4 | 705,366.8 | 1.033x | 1.033x | - | - |

#### `wild-waf-crs-942360-concat-sqli` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 9,316,969.0 | 8.8854 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 9,259,104.6 | 8.8302 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 9,250,503.6 | 8.8220 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 2,320,752.1 | 8.8530 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 2,306,196.5 | 8.7974 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 2,303,857.4 | 8.7885 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 578,605.3 | 8.8288 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 575,810.1 | 8.7862 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 574,323.2 | 8.7635 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 163,360.0 | 2.6589 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 163,945.0 | 2.6684 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 163,868.3 | 2.6671 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 43,581.6 | 2.6598 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 43,593.7 | 2.6606 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 43,567.6 | 2.6590 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 25,022.6 | 6.1090 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 24,269.7 | 5.9252 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 24,766.8 | 6.0466 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 7,953,060.4 | 7.5850 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 7,952,509.2 | 7.5845 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 8,227,711.7 | 7.8470 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 7,961,264.4 | 7.5928 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 7,957,409.3 | 7.5892 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 8,208,981.2 | 7.8291 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 7,952,606.2 | 7.5846 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 7,954,769.6 | 7.5866 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 8,218,994.5 | 7.8386 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 218,713.0 | 3.5598 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 219,046.7 | 3.5652 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 218,270.6 | 3.5526 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 58,129.1 | 3.5477 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 58,114.1 | 3.5468 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 58,094.3 | 3.5456 |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 9,316,969.0 ns, 1,048,576 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `t-1m`, 9,259,104.6 ns, 1,048,576 B; largest Δ: `t-tail-digits-1m`, -275,202.5 ns (now 7,952,509.2 ns), 1,048,522 B

### `wild-waf-crs-942360-concat-sqli` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 7,390.2 | 7,373.2 | 7,449.9 | 28.3 | 1.000x | 1.000x | unchanged (within spread) | -0.32% (null control: program identical) | 75 | 98.5 | 9.1 | 100% |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 7,413.6 | 7,391.0 | 7,428.5 | 14.7 | 1.003x | 1.003x | - | - | 75 | 98.8 | 9.1 | 100% |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 7,468.3 | 7,396.8 | 7,702.0 | 110.6 | 1.011x | 1.011x | unchanged (within spread) | +1.06% (null control: program identical) | 75 | 99.6 | 9.1 | 100% |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `sec-slack-webhook`, 456.5 ns, 81 B; largest Δ: `rd-trim-near-miss`, -4.9 ns (now 134.5 ns), 20 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `sec-slack-webhook`, 460.4 ns, 81 B; largest Δ: `waf-concat`, +17.7 ns (now 336.0 ns), 48 B

### `wild-waf-crs-942500-comment-obfuscation` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 78,577.0 | 0.0168 | 78,537.8 | 78,609.8 | 27.6 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 78,643.8 | 0.0168 | 78,600.8 | 78,724.0 | 42.5 | 1.001x | 1.001x | unchanged (within spread) | -0.01% (null control: program identical) |
| 3 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 78,654.2 | 0.0168 | 78,605.1 | 78,689.5 | 28.7 | 1.001x | 1.001x | slower ×1.00 | +0.10% (null control: program identical) |

#### `wild-waf-crs-942500-comment-obfuscation` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 17,620.5 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,633.2 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 17,645.9 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 4,378.4 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 4,388.1 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 4,375.7 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 1,110.1 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,111.5 | 0.0170 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 1,108.7 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,033.0 | 0.0168 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,035.6 | 0.0169 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,033.1 | 0.0168 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 223.9 | 0.0137 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 225.0 | 0.0137 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 224.2 | 0.0137 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 58.6 | 0.0143 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 58.9 | 0.0144 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 58.9 | 0.0144 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,609.8 | 0.0168 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,653.6 | 0.0168 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,660.6 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 17,629.0 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,635.4 | 0.0168 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 17,628.6 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 17,632.1 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 17,648.3 | 0.0168 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 17,632.4 | 0.0168 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 1,034.3 | 0.0168 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,035.4 | 0.0169 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 1,034.7 | 0.0168 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 224.9 | 0.0137 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 224.8 | 0.0137 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 224.5 | 0.0137 |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `t-tail-digits-1m`, 17,653.6 ns, 1,048,522 B; largest Δ: `t-tail-txt-1m`, +15.9 ns (now 17,648.3 ns), 1,048,527 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `t-tail-digits-1m`, 17,660.6 ns, 1,048,522 B

### `wild-waf-crs-942500-comment-obfuscation` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 719.2 | 717.6 | 725.2 | 2.8 | 1.000x | 1.000x | unchanged (within spread) | -0.00% (null control: program identical) | 75 | 9.6 | 9.1 | 100% |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 719.2 | 717.0 | 727.0 | 3.7 | 1.000x | 1.000x | - | - | 75 | 9.6 | 9.1 | 100% |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 719.8 | 718.9 | 721.1 | 0.7 | 1.001x | 1.001x | unchanged (within spread) | +0.08% (null control: program identical) | 75 | 9.6 | 9.1 | 100% |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now: `waf-comment-obfuscation`, 79.0 ns, 18 B; largest Δ: `rec-comment-nested`, -0.9 ns (now 45.5 ns), 34 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `waf-comment-obfuscation`, 78.8 ns, 18 B; largest Δ: `rec-comment-nested`, +1.0 ns (now 46.4 ns), 34 B

### `winpath-near-miss` / `large-subject-throughput` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_00c97769_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 63.7 | 0.0000 | 63.3 | 66.1 | 1.0 | 1.000x | 1.000x | unchanged (within spread) | -1.46% (null control: program identical) |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 64.7 | 0.0000 | 63.3 | 78.2 | 5.7 | 1.015x | 1.015x | - | - |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 64.8 | 0.0000 | 63.3 | 66.8 | 1.2 | 1.018x | 1.018x | unchanged (within spread) | +1.78% (null control: program identical) |

#### `winpath-near-miss` / `large-subject-throughput` per-subject (capability@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_00c97769_auto-caps-simdna` | 5.9 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 5.9 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_00c97769_auto-caps-simdna` | 6.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_b8337c33_auto-caps-simdna` | 6.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_6b2dbd3e_auto-caps-simdna` | 6.0 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_00c97769_auto-caps-simdna` | 6.1 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_b8337c33_auto-caps-simdna` | 7.1 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_6b2dbd3e_auto-caps-simdna` | 6.2 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 5.9 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 5.9 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.9 | 0.0001 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 5.9 | 0.0004 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 5.9 | 0.0004 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.9 | 0.0004 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_00c97769_auto-caps-simdna` | 5.3 | 0.0013 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_b8337c33_auto-caps-simdna` | 5.3 | 0.0013 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.3 | 0.0013 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 5.9 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 5.9 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.9 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_00c97769_auto-caps-simdna` | 5.9 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_b8337c33_auto-caps-simdna` | 5.9 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.9 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_00c97769_auto-caps-simdna` | 5.9 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_b8337c33_auto-caps-simdna` | 5.9 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.9 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_00c97769_auto-caps-simdna` | 5.3 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_b8337c33_auto-caps-simdna` | 5.3 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.3 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_00c97769_auto-caps-simdna` | 5.3 | 0.0003 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_b8337c33_auto-caps-simdna` | 5.3 | 0.0003 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_6b2dbd3e_auto-caps-simdna` | 5.3 | 0.0003 |

- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `t-64k`, 6.1 ns, 65,536 B
- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `t-64k`, 6.2 ns, 65,536 B; largest Δ: `t-256k`, +0.1 ns (now 6.0 ns), 262,144 B

### `winpath-near-miss` / `short-subject-search` (capability@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 455.9 | 453.9 | 456.4 | 1.0 | 1.000x | 1.000x | unchanged (within spread) | -0.30% (null control: program identical) | 75 | 6.1 | 9.1 | 100% |
| 2 | `pcrec_00c97769_auto-caps-simdna` | measured | `plain` | same program | 457.3 | 454.6 | 461.5 | 2.5 | 1.003x | 1.003x | unchanged (within spread) | -0.11% (null control: program identical) | 75 | 6.1 | 9.1 | 100% |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 457.8 | 455.8 | 458.3 | 1.1 | 1.004x | 1.004x | - | - | 75 | 6.1 | 9.1 | 100% |

- Δ detail: `pcrec_6b2dbd3e_auto-caps-simdna` vs previous `pcrec_00c97769_auto-caps-simdna`: worst now: `lp-winpath`, 30.9 ns, 22 B; largest Δ: `lp-winpath-reserved`, -0.3 ns (now 16.0 ns), 24 B
- Δ detail: `pcrec_00c97769_auto-caps-simdna` vs previous `pcrec_b8337c33_auto-caps-simdna`: worst now (also the largest Δ): `lp-winpath`, 30.9 ns, 22 B

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `email-nested-plus` | `large-subject-throughput` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 11 | 82% | 0 | 0 | `t-evil-match-60k` (no-expectation), `t-evil-nearmiss-16k` (no-expectation) |
| `email-nested-plus` | `large-subject-throughput` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 11 | 82% | 0 | 0 | `t-evil-match-60k` (no-expectation), `t-evil-nearmiss-16k` (no-expectation) |
| `email-nested-plus` | `large-subject-throughput` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 11 | 82% | 0 | 0 | `t-evil-match-60k` (no-expectation), `t-evil-nearmiss-16k` (no-expectation) |

## Standing cross-class query (inbox I-101; Frank's own anomaly check -- a QUERY, never a ranking; every hit below is a finding on pcrec's side by definition)

_0 hits: no included YES-class config's median beats any pcrec `auto-nocaps` row's median in this report's roster._

## Compile cost (by execution-model class; never pooled across classes)

### `compiled-aot`

- `pcrec_00c97769_auto-caps-simdna` / `balanced-parens-rec` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,049 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_00c97769_auto-caps-simdna` / `balanced-parens-rec` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,259 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_00c97769_auto-caps-simdna` / `base10num-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `base10num-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `bracket-array-define` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,395 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_00c97769_auto-caps-simdna` / `bracket-array-define` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,500 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_00c97769_auto-caps-simdna` / `codegrammar-flat` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,667 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `codegrammar-flat` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,770 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `codegrammar-xflag` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,724 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `codegrammar-xflag` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,829 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `currency-lookbehind-fixed` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=mixed offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=1, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `currency-lookbehind-fixed` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=mixed offsets=none, edge=range, edges=0 (match: 1), start=reverse-pass, folds=1, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `date-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 8,112 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `date-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 8,217 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `doubled-word` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,418 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `doubled-word` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,521 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `dup-param-detect` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,829 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `dup-param-detect` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,934 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `email-local-nodup` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 2,976 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/4 == stamped default (single tier), buffers=3/4 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `email-local-nodup` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 3,081 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/4 == stamped default (single tier), buffers=3/4 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `email-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 3,343 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `email-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 3,448 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `evil-alt-nested` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 4,191 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `evil-alt-nested` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 4,296 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `file-ext-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned table=premultiplied offsets=0*,1,2,3, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `file-ext-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `float-literal-bound` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=first-class-bounded table=mixed offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `float-literal-bound` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=indexed offsets=none, edge=range, edges=0 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `floor-byte` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `floor-byte` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `hex8-bounded` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=first-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `hex8-bounded` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=bitmap, edges=0 (match: 1), start=reverse-pass, folds=1, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `high-byte-run` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=4 (match: 2), start=reverse-pass, folds=2, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `high-byte-run` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `ipv4-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `ipv4-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `keyword-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `keyword-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `letters-bounded-tail-z` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `letters-bounded-tail-z` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `logparse-atomic` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=1, islands=2, shape=plain (prog: 10,528 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `logparse-atomic` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=1, islands=2, shape=plain (prog: 10,633 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `logparse-atomic-removed` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=1, islands=2, shape=plain (prog: 10,118 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `logparse-atomic-removed` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=1, islands=2, shape=plain (prog: 10,223 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `mojibake-curly-quote` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `mojibake-curly-quote` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `nested-comment-rec` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 6,766 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_00c97769_auto-caps-simdna` / `nested-comment-rec` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 6,871 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_00c97769_auto-caps-simdna` / `numeric-id-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 3,030 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `numeric-id-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 3,135 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `phone-list-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 4,198 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `phone-list-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 4,303 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `phone-palindrome-6` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 4,078 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `phone-palindrome-6` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=plain (prog: 4,183 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `pwd-strength-chain` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 7,940 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `pwd-strength-chain` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 8,045 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `quoted-delim-match` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,223 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `quoted-delim-match` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,328 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `router-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned table=premultiplied offsets=0*,1,2,3,4, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `router-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `tag-depth3-bound` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 11,163 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `tag-depth3-bound` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 11,268 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `tag-pair-match` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,848 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `tag-pair-match` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,953 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `tail-digits-eol` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `tail-digits-eol` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `tail-dotstar-txt` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `tail-dotstar-txt` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `tail-ext-lower-txt` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `tail-ext-lower-txt` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `tail-space-eol` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `tail-space-eol` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `tail-word-eoz` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `tail-word-eoz` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `trim-nested-star` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 1,822 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `trim-nested-star` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 1,927 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `utf8-lead-no-cont` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `utf8-lead-no-cont` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=mixed offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `uuid-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `uuid-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `wild-codegrammar-json-array-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `wild-codegrammar-json-array-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `wild-codegrammar-json-constant` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=first-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `wild-codegrammar-json-constant` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=0 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `wild-codegrammar-json-number-extended` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `wild-codegrammar-json-number-extended` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `wild-codegrammar-json-object-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `wild-codegrammar-json-object-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `wild-codegrammar-json-stringcontent-escape` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `wild-codegrammar-json-stringcontent-escape` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `wild-datetime-moment-iso8601` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 15,746 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=14/11 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `wild-datetime-moment-iso8601` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 15,851 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=14/11 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `wild-logparse-base10num-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,873 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=3/2 == stamped default (single tier), buffers=3/2 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `wild-logparse-base10num-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,978 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=3/2 == stamped default (single tier), buffers=3/2 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `wild-logparse-base10num-noatomic` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=mixed offsets=none, edge=range, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `wild-logparse-base10num-noatomic` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=mixed offsets=none, edge=range, edges=0 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `wild-logparse-quotedstring-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=first-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 17,340 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `wild-logparse-quotedstring-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 17,445 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `wild-logparse-quotedstring-noatomic` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=first-class-bounded table=mixed offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `wild-logparse-quotedstring-noatomic` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=mixed offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `wild-logparse-syslogbase-expanded` / `plain`: engine=vm, sel=size-cap-retry (DFA fallback tripped), entry=plain entry, vm_prefilter=hybrid, lang=count-collapsed (size cap retry, exact 1460741 > 1000000), dfa: scan=unanchored prefilter=first-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 300,079 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=21/31 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `wild-logparse-syslogbase-expanded` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 300,188 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=21/31 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `wild-logparse-winpath-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,656 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `wild-logparse-winpath-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,762 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `wild-secrets-aws-access-key-id` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=first-memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, frameless=0, islands=1, shape=plain (prog: 5,986 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=8/3 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `wild-secrets-aws-access-key-id` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=1, shape=plain (prog: 6,091 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=8/3 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `wild-secrets-github-pat` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,6*, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, frameless=1, islands=0, shape=inline (prog: 1,864 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `wild-secrets-github-pat` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 1,967 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `wild-secrets-slack-webhook-url` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,6*, edge=mixed, edges=3 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=plain (prog: 8,487 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `wild-secrets-slack-webhook-url` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=mixed, edges=3 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=plain (prog: 8,592 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `wild-secrets-username-password-pair` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class table=mixed offsets=none, edge=range, edges=2 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=2, shape=plain (prog: 16,953 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `wild-secrets-username-password-pair` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=2, shape=plain (prog: 17,058 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned table=premultiplied offsets=0*,1,2, edge=range, edges=0 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=0 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,439 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,544 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `wild-validator-email-owasp` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `wild-validator-email-owasp` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `wild-validator-ipv4-owasp` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 14,287 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `wild-validator-ipv4-owasp` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 14,392 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `wild-validator-us-zip-owasp` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 2,243 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=2/4 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `wild-validator-us-zip-owasp` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 2,346 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=2/4 (stamped default), frame=24
- `pcrec_00c97769_auto-caps-simdna` / `wild-validator-uuid-grok` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,8*,13, edge=bitmap, edges=4 (match: 4), start=end-minus-width, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `wild-validator-uuid-grok` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=bitmap, edges=4 (match: 4), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `wild-waf-crs-942140-dbnames` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=first-class-bounded table=premultiplied offsets=none, edge=mixed, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `wild-waf-crs-942140-dbnames` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=mixed, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `wild-waf-crs-942270-union-select` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `wild-waf-crs-942270-union-select` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `wild-waf-crs-942360-concat-sqli` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `wild-waf-crs-942360-concat-sqli` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `wild-waf-crs-942500-comment-obfuscation` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `wild-waf-crs-942500-comment-obfuscation` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `winpath-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_00c97769_auto-caps-simdna` / `winpath-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `balanced-parens-rec` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,049 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_6b2dbd3e_auto-caps-simdna` / `balanced-parens-rec` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,259 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_6b2dbd3e_auto-caps-simdna` / `base10num-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `base10num-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `bracket-array-define` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,395 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_6b2dbd3e_auto-caps-simdna` / `bracket-array-define` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,500 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_6b2dbd3e_auto-caps-simdna` / `codegrammar-flat` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,667 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `codegrammar-flat` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,770 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `codegrammar-xflag` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,724 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `codegrammar-xflag` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,829 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `currency-lookbehind-fixed` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=mixed offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=1, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `currency-lookbehind-fixed` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=mixed offsets=none, edge=range, edges=0 (match: 1), start=reverse-pass, folds=1, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `date-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 8,112 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `date-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 8,217 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `doubled-word` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,418 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `doubled-word` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,521 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `dup-param-detect` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,829 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `dup-param-detect` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,934 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `email-local-nodup` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 2,976 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/4 == stamped default (single tier), buffers=3/4 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `email-local-nodup` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 3,081 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/4 == stamped default (single tier), buffers=3/4 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `email-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 3,343 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `email-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 3,448 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `evil-alt-nested` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 4,191 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `evil-alt-nested` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 4,296 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `file-ext-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned table=premultiplied offsets=0*,1,2,3, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `file-ext-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `float-literal-bound` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=first-class-bounded table=mixed offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `float-literal-bound` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=indexed offsets=none, edge=range, edges=0 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `floor-byte` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `floor-byte` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `hex8-bounded` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=first-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `hex8-bounded` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=bitmap, edges=0 (match: 1), start=reverse-pass, folds=1, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `high-byte-run` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=4 (match: 2), start=reverse-pass, folds=2, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `high-byte-run` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `ipv4-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `ipv4-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `keyword-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `keyword-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `letters-bounded-tail-z` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `letters-bounded-tail-z` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `logparse-atomic` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=1, islands=2, shape=plain (prog: 10,528 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `logparse-atomic` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=1, islands=2, shape=plain (prog: 10,633 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `logparse-atomic-removed` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=1, islands=2, shape=plain (prog: 10,118 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `logparse-atomic-removed` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=1, islands=2, shape=plain (prog: 10,223 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `mojibake-curly-quote` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `mojibake-curly-quote` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `nested-comment-rec` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 6,766 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_6b2dbd3e_auto-caps-simdna` / `nested-comment-rec` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 6,871 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_6b2dbd3e_auto-caps-simdna` / `numeric-id-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 3,030 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `numeric-id-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 3,135 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `phone-list-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 4,198 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `phone-list-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 4,303 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `phone-palindrome-6` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 4,078 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `phone-palindrome-6` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=plain (prog: 4,183 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `pwd-strength-chain` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 7,940 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `pwd-strength-chain` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 8,045 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `quoted-delim-match` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,223 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `quoted-delim-match` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,328 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `router-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned table=premultiplied offsets=0*,1,2,3,4, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `router-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `tag-depth3-bound` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 11,163 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `tag-depth3-bound` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 11,268 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `tag-pair-match` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,848 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `tag-pair-match` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,953 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `tail-digits-eol` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `tail-digits-eol` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `tail-dotstar-txt` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `tail-dotstar-txt` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `tail-ext-lower-txt` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `tail-ext-lower-txt` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `tail-space-eol` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `tail-space-eol` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `tail-word-eoz` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `tail-word-eoz` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `trim-nested-star` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 1,822 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `trim-nested-star` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 1,927 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `utf8-lead-no-cont` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `utf8-lead-no-cont` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=mixed offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `uuid-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `uuid-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-codegrammar-json-array-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-codegrammar-json-array-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-codegrammar-json-constant` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=first-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-codegrammar-json-constant` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=0 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-codegrammar-json-number-extended` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-codegrammar-json-number-extended` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-codegrammar-json-object-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-codegrammar-json-object-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-codegrammar-json-stringcontent-escape` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-codegrammar-json-stringcontent-escape` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-datetime-moment-iso8601` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 15,746 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=14/11 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-datetime-moment-iso8601` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 15,851 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=14/11 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-logparse-base10num-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,873 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=3/2 == stamped default (single tier), buffers=3/2 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-logparse-base10num-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,978 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=3/2 == stamped default (single tier), buffers=3/2 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-logparse-base10num-noatomic` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=mixed offsets=none, edge=range, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-logparse-base10num-noatomic` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=mixed offsets=none, edge=range, edges=0 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-logparse-quotedstring-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=first-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 17,340 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-logparse-quotedstring-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 17,445 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-logparse-quotedstring-noatomic` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=first-class-bounded table=mixed offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-logparse-quotedstring-noatomic` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=mixed offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-logparse-syslogbase-expanded` / `plain`: engine=vm, sel=size-cap-retry (DFA fallback tripped), entry=plain entry, vm_prefilter=hybrid, lang=count-collapsed (size cap retry, exact 1460741 > 1000000), dfa: scan=unanchored prefilter=first-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 300,079 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=21/31 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-logparse-syslogbase-expanded` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 300,188 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=21/31 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-logparse-winpath-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,656 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-logparse-winpath-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,762 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-secrets-aws-access-key-id` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=first-memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, frameless=0, islands=1, shape=plain (prog: 5,986 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=8/3 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-secrets-aws-access-key-id` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=1, shape=plain (prog: 6,091 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=8/3 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-secrets-github-pat` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,6*, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, frameless=1, islands=0, shape=inline (prog: 1,864 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-secrets-github-pat` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 1,967 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-secrets-slack-webhook-url` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,6*, edge=mixed, edges=3 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=plain (prog: 8,487 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-secrets-slack-webhook-url` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=mixed, edges=3 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=plain (prog: 8,592 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-secrets-username-password-pair` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class table=mixed offsets=none, edge=range, edges=2 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=2, shape=plain (prog: 16,953 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-secrets-username-password-pair` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=2, shape=plain (prog: 17,058 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned table=premultiplied offsets=0*,1,2, edge=range, edges=0 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=0 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,439 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,544 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-validator-email-owasp` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-validator-email-owasp` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-validator-ipv4-owasp` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 14,287 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-validator-ipv4-owasp` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 14,392 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-validator-us-zip-owasp` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 2,243 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=2/4 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-validator-us-zip-owasp` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 2,346 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=2/4 (stamped default), frame=24
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-validator-uuid-grok` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,8*,13, edge=bitmap, edges=4 (match: 4), start=end-minus-width, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-validator-uuid-grok` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=bitmap, edges=4 (match: 4), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-waf-crs-942140-dbnames` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=first-class-bounded table=premultiplied offsets=none, edge=mixed, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-waf-crs-942140-dbnames` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=mixed, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-waf-crs-942270-union-select` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-waf-crs-942270-union-select` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-waf-crs-942360-concat-sqli` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-waf-crs-942360-concat-sqli` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-waf-crs-942500-comment-obfuscation` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `wild-waf-crs-942500-comment-obfuscation` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `winpath-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `winpath-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `balanced-parens-rec` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,049 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_b8337c33_auto-caps-simdna` / `balanced-parens-rec` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,259 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_b8337c33_auto-caps-simdna` / `base10num-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `base10num-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `bracket-array-define` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,395 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_b8337c33_auto-caps-simdna` / `bracket-array-define` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,500 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_b8337c33_auto-caps-simdna` / `codegrammar-flat` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,667 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `codegrammar-flat` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,770 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `codegrammar-xflag` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,724 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `codegrammar-xflag` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,829 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `currency-lookbehind-fixed` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=mixed offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=1, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `currency-lookbehind-fixed` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=mixed offsets=none, edge=range, edges=0 (match: 1), start=reverse-pass, folds=1, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `date-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 8,112 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `date-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 8,217 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `doubled-word` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,418 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `doubled-word` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,521 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `dup-param-detect` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,829 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `dup-param-detect` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,934 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `email-local-nodup` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 2,976 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/4 == stamped default (single tier), buffers=3/4 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `email-local-nodup` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 3,081 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/4 == stamped default (single tier), buffers=3/4 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `email-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 3,343 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `email-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 3,448 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `evil-alt-nested` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 4,191 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `evil-alt-nested` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 4,296 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `file-ext-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned table=premultiplied offsets=0*,1,2,3, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `file-ext-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `float-literal-bound` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=first-class-bounded table=mixed offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `float-literal-bound` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=indexed offsets=none, edge=range, edges=0 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `floor-byte` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `floor-byte` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `hex8-bounded` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=first-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `hex8-bounded` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=bitmap, edges=0 (match: 1), start=reverse-pass, folds=1, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `high-byte-run` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=4 (match: 2), start=reverse-pass, folds=2, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `high-byte-run` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `ipv4-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `ipv4-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `keyword-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `keyword-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `letters-bounded-tail-z` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `letters-bounded-tail-z` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `logparse-atomic` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=1, islands=2, shape=plain (prog: 10,528 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `logparse-atomic` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=1, islands=2, shape=plain (prog: 10,633 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `logparse-atomic-removed` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=1, islands=2, shape=plain (prog: 10,118 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `logparse-atomic-removed` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=1, islands=2, shape=plain (prog: 10,223 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `mojibake-curly-quote` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `mojibake-curly-quote` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `nested-comment-rec` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 6,766 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_b8337c33_auto-caps-simdna` / `nested-comment-rec` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 6,871 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_b8337c33_auto-caps-simdna` / `numeric-id-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 3,030 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `numeric-id-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 3,135 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `phone-list-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 4,198 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `phone-list-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 4,303 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `phone-palindrome-6` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 4,078 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `phone-palindrome-6` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=plain (prog: 4,183 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `pwd-strength-chain` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 7,940 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `pwd-strength-chain` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 8,045 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `quoted-delim-match` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,223 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `quoted-delim-match` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,328 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `router-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned table=premultiplied offsets=0*,1,2,3,4, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `router-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `tag-depth3-bound` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 11,163 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `tag-depth3-bound` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 11,268 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `tag-pair-match` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,848 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `tag-pair-match` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,953 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `tail-digits-eol` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `tail-digits-eol` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `tail-dotstar-txt` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `tail-dotstar-txt` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `tail-ext-lower-txt` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `tail-ext-lower-txt` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `tail-space-eol` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `tail-space-eol` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `tail-word-eoz` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `tail-word-eoz` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `trim-nested-star` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 1,822 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `trim-nested-star` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 1,927 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `utf8-lead-no-cont` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `utf8-lead-no-cont` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=mixed offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `uuid-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `uuid-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `wild-codegrammar-json-array-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `wild-codegrammar-json-array-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `wild-codegrammar-json-constant` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=first-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `wild-codegrammar-json-constant` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=0 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `wild-codegrammar-json-number-extended` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `wild-codegrammar-json-number-extended` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `wild-codegrammar-json-object-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `wild-codegrammar-json-object-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `wild-codegrammar-json-stringcontent-escape` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `wild-codegrammar-json-stringcontent-escape` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `wild-datetime-moment-iso8601` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 15,746 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=14/11 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `wild-datetime-moment-iso8601` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 15,851 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=14/11 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `wild-logparse-base10num-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,873 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=3/2 == stamped default (single tier), buffers=3/2 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `wild-logparse-base10num-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,978 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=3/2 == stamped default (single tier), buffers=3/2 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `wild-logparse-base10num-noatomic` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=mixed offsets=none, edge=range, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `wild-logparse-base10num-noatomic` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=mixed offsets=none, edge=range, edges=0 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `wild-logparse-quotedstring-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=first-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 17,340 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `wild-logparse-quotedstring-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 17,445 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `wild-logparse-quotedstring-noatomic` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=first-class-bounded table=mixed offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `wild-logparse-quotedstring-noatomic` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=mixed offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `wild-logparse-syslogbase-expanded` / `plain`: engine=vm, sel=size-cap-retry (DFA fallback tripped), entry=plain entry, vm_prefilter=hybrid, lang=count-collapsed (size cap retry, exact 1460741 > 1000000), dfa: scan=unanchored prefilter=first-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 300,079 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=21/31 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `wild-logparse-syslogbase-expanded` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 300,188 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=21/31 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `wild-logparse-winpath-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,656 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `wild-logparse-winpath-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,762 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `wild-secrets-aws-access-key-id` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=first-memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, frameless=0, islands=1, shape=plain (prog: 5,986 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=8/3 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `wild-secrets-aws-access-key-id` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=1, shape=plain (prog: 6,091 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=8/3 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `wild-secrets-github-pat` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,6*, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, frameless=1, islands=0, shape=inline (prog: 1,864 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `wild-secrets-github-pat` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 1,967 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `wild-secrets-slack-webhook-url` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,6*, edge=mixed, edges=3 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=plain (prog: 8,487 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `wild-secrets-slack-webhook-url` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=mixed, edges=3 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=plain (prog: 8,592 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `wild-secrets-username-password-pair` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class table=mixed offsets=none, edge=range, edges=2 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=2, shape=plain (prog: 16,953 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `wild-secrets-username-password-pair` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=2, shape=plain (prog: 17,058 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned table=premultiplied offsets=0*,1,2, edge=range, edges=0 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=0 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,439 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,544 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `wild-validator-email-owasp` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `wild-validator-email-owasp` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `wild-validator-ipv4-owasp` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 14,287 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `wild-validator-ipv4-owasp` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 14,392 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `wild-validator-us-zip-owasp` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 2,243 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=2/4 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `wild-validator-us-zip-owasp` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 2,346 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=2/4 (stamped default), frame=24
- `pcrec_b8337c33_auto-caps-simdna` / `wild-validator-uuid-grok` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,8*,13, edge=bitmap, edges=4 (match: 4), start=end-minus-width, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `wild-validator-uuid-grok` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=bitmap, edges=4 (match: 4), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `wild-waf-crs-942140-dbnames` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=first-class-bounded table=premultiplied offsets=none, edge=mixed, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `wild-waf-crs-942140-dbnames` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=mixed, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `wild-waf-crs-942270-union-select` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `wild-waf-crs-942270-union-select` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `wild-waf-crs-942360-concat-sqli` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `wild-waf-crs-942360-concat-sqli` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `wild-waf-crs-942500-comment-obfuscation` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `wild-waf-crs-942500-comment-obfuscation` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `winpath-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `winpath-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
    - sel = pcrec's `RX_ENGINE_SEL`; `DFA fallback tripped` = sel not in (selected, forced), and NOTHING else -- since pcrec 263b013 ([LIM-1] / [OPT-4.1]) every fallback has its own token (`overflowed-dfa`, `overflowed-prefilter`, `collapsed-prefilter`, `declined-nullable`, `size-cap-retry`), the size-cap rescue included; at pcrec 96e44c2 that rescue stamped `sel=selected` and only its `lang=count-collapsed (size cap retry, ...)` clause says so.
    - K = pcrec's `RX_UNROLL_K`/`_WHY`: the VM counter rung's unroll factor and who chose it (default / option / denied / size-model / size-model-declined / cap-rescue / capacity-declined -- limits.md 8); caps = the EFFECTIVE `RX_MAX_EMIT_CODE_BYTES`/`RX_MAX_EMIT_BYTES` the artifact was built under (raise-only; 500,000/1,000,000 by default). VM artifacts only: a DFA artifact has no counter rung and stamps no code cap.
    - edge = pcrec's `RX_DFA_SCAN_EDGE` ([OPT-5] STEP 1, abi 13+), how a DFA scan tests a SCAN EDGE's byte class: `range` = a contiguous run (subtract-and-compare against two immediates); `bitmap` = a non-contiguous class (a 256-byte membership read); `mixed` = one artifact whose machines took both forms; `none` = no collapsible run (an attempt/empty scan, or -fno-scan-edge).
    - edges = pcrec's `scan_edges` ([B32]): how many [OPT-5] SCAN EDGES this artifact's SEARCH-side machines carry (`rx_search`/`rx_prefilter`), the per-scan-iteration compare-count covariate `edge`'s single shape token cannot separate (I-33: the cost is one compare per edge per iteration); the `(match: M)` parenthetical, when carried, is the SAME count on the anchored `rx_match` machine, kept apart because the measured [OPT-EDGE] regression is search-band only. `0` is a real, recorded value.
    - start = pcrec's `RX_DFA_START` ([OPT-5] STEP 2, abi 16+), how the SEARCH entry recovers the match START: `pinned` = the forward machine's start state accepts unconditionally, so the match provably begins at `search_from` and THE ARTIFACT CARRIES NO REVERSE MACHINE at all (no reverse tables, accessor block or scan loop); `reverse-pass` = it carries one and walks it backwards from the match end. The two forms are ANSWER-IDENTICAL by contract -- `caps[0][0]`'s absolute offsets and the zero-length-match convention hold under both -- so this explains a row's SIZE and pass count, never its answer.
      - start=end-minus-width: every match is one fixed byte width W, so the start is the verified end minus W; NO reverse machine (abi 74, [START-LANDING])
      - start=attempt-start: the ABSENCE value: an `attempt` loop or the empty engine asks no RECOVER and no reverse pass runs (abi 73)
    - frameless = pcrec's `RX_VM_FRAMELESS` ([OPT-VMFL], abi 16+): `1` iff this VM program emits NO push site and no linked call, so its fail label carries no pop-and-resume dispatch; `0` otherwise. VM artifacts only, hybrids included -- a DIFFERENT scope from `start=`, though the two stamps arrived at one abi. It is NOT `buffers=`'s resume-frame CAPACITY and the two can disagree: the capacity is what the artifact was SIZED for, this is what its program CONTAINS. `0` is a real, recorded value.
    - folds = pcrec's `RX_DFA_UNIFORM_FOLDS` ([CC-DIFF] STEP 1, abi 17+): how many of this artifact's DFA tables (two per machine it contains -- forward always, reverse unless `start=pinned`, anchored under `match=unwrapped`; so 0..6) had ALL-EQUAL cells and were NOT EMITTED, the accessor returning the constant. `table=` keeps naming the encoding that was SELECTED, so `premultiplied` beside `folds=4` is an artifact carrying NO transition table at all -- a SIZE fact, never an answer one. `0` is a real, recorded value.
    - islands = pcrec's `RX_VM_ALT_ISLANDS` ([ENG-ISL] STEP 1, abi 18+): how many of this VM program's flat alternations were lowered as an ALTERNATION ISLAND -- a trie dispatch over the alternatives' literal bytes -- instead of vm_alt's serial resume chain (one frame per untried branch). Selected per alternation on its LANGUAGE (a finite literal set), so a COUNT; a caseless, prefix-bearing-under-four-words or over-budget alternation is declined as a selection outcome. This is what removes the branch-ORDER effect (altwide srt-256 vs w-256) at the source; `-fno-alt-island` is the sibling that reads `0` at the same pin. `0` is a real, recorded value.
    - shape = pcrec's `RX_VM_ENTRY_SHAPE` with `RX_VM_PROGRAM_BYTES` in the parenthetical ([CC-DIFF] STEP 2, abi 22+): the entry-chain rung the emitter TOOK for the six entries -- `plain` (one body, six framed entries), `shared` (one out-of-line body behind three forwarding entries), `forward` (three bodies in the three `_in` entries, no canary anywhere), `inline` (six bodies) -- and the program size AUTO compared against VM_INLINE_CHAIN_MAX_BYTES (4,096 B) to choose it: `forward` at or below, `shared` above; `inline`/`plain` where a forward rung is illegal (the program writes its storage); a FRAMED program (`frameless=0`) is `plain` whatever the size. ANSWER-IDENTICAL across every value -- only the scaffolding above the first label moves -- so a COST and SIZE fact; the number is what makes the token checkable. `prog: N B` is the VM PROGRAM REGION with its COMMENTS INCLUDED (the raw length of the emitter's program buffer; the island trie writes a per-node comment), NOT the `code bytes` columns' quantity -- those and `--max-emit-code-bytes` count the whole .c+.h with every comment EXCLUDED -- so the program stamp can exceed the code bytes (w-256: 305,686 vs 292,043) and neither is wrong; for cap reasoning use the code bytes (pcrec I-50 1).
    - clsfolds = pcrec's `RX_VM_CLS_FOLDS` ([FORM-CHAR] STEP 1, abi 23+): how many of this VM program's class-pool entries take the ASCII-FOLD membership test -- a two-member set differing only in bit 0x20, both letters (what `(?i)` makes of a letter at parse time), tested as `(byte | 0x20) == lower` with NO 32-byte bitmap table emitted for it. Chosen per pool class, so a COUNT; a set that is not exactly two members, not a 0x20 pair, or a 0x20 pair of non-letters keeps its bitmap. A SIZE fact (one table per fold class gone, plus the test text), never an answer one: the fold compare and the bitmap read are the same predicate over the pair's two bytes. VM route only -- an `auto` row that selected the DFA prints no clause even on a `(?i)` pattern; `-fno-cls-fold` is the sibling that reads `0` at the same pin. `0` is a real, recorded value.

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | emit bytes | code bytes | jitter | outcomes | emit-c ns | gcc ns | load ns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `balanced-parens-rec` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 234,762,977.0 | 226,598,006.0 | 241,286,102.0 | 5,195,100.7 | 5 | 32,848 | 28,783 | 27,030 | 0.022 | compiled=5 | 4,647,794.0 | 232,310,075.0 | 99,930.0 |
| `balanced-parens-rec` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 237,790,853.0 | 227,712,540.0 | 244,757,619.0 | 6,112,650.0 | 5 | 32,848 | 29,001 | 27,248 | 0.026 | compiled=5 | 2,591,902.0 | 235,098,559.0 | 113,870.0 |
| `balanced-parens-rec` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 235,042,582.0 | 229,281,859.0 | 241,396,459.0 | 3,985,944.3 | 5 | 32,848 | 28,783 | 27,030 | 0.017 | compiled=5 | 2,400,074.0 | 232,392,565.0 | 106,351.0 |
| `balanced-parens-rec` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 228,131,280.0 | 220,414,958.0 | 244,689,567.0 | 8,629,132.6 | 5 | 32,848 | 29,001 | 27,248 | 0.038 | compiled=5 | 2,387,574.0 | 225,533,006.0 | 194,811.0 |
| `balanced-parens-rec` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 234,292,849.0 | 227,032,336.0 | 236,542,361.0 | 3,573,936.0 | 5 | 32,848 | 28,783 | 27,030 | 0.015 | compiled=5 | 2,340,234.0 | 231,857,394.0 | 103,301.0 |
| `balanced-parens-rec` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 235,327,614.0 | 231,599,104.0 | 236,699,693.0 | 1,750,465.5 | 5 | 32,848 | 29,001 | 27,248 | 0.007 | compiled=5 | 2,406,144.0 | 232,859,901.0 | 108,670.0 |
| `base10num-near-miss` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 160,428,821.0 | 156,477,902.0 | 167,681,490.0 | 4,197,412.3 | 5 | 28,768 | 17,485 | 15,100 | 0.026 (max is trial 1) | compiled=5 | 1,990,111.0 | 157,533,237.0 | 106,391.0 |
| `base10num-near-miss` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 151,299,495.0 | 145,484,324.0 | 169,101,137.0 | 8,232,409.7 | 5 | 28,696 | 16,938 | 14,553 | 0.054 | compiled=5 | 1,992,960.0 | 148,805,951.0 | 186,641.0 |
| `base10num-near-miss` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 160,034,372.0 | 157,053,077.0 | 172,349,464.0 | 5,553,799.5 | 5 | 28,768 | 17,485 | 15,100 | 0.035 | compiled=5 | 2,257,722.0 | 155,704,518.0 | 98,689.0 |
| `base10num-near-miss` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 158,222,652.0 | 149,804,365.0 | 163,711,845.0 | 4,859,152.2 | 5 | 28,696 | 16,938 | 14,553 | 0.031 | compiled=5 | 1,966,421.0 | 156,143,491.0 | 112,739.0 |
| `base10num-near-miss` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 166,627,112.0 | 161,946,967.0 | 173,722,693.0 | 4,566,028.0 | 5 | 28,768 | 17,485 | 15,100 | 0.027 | compiled=5 | 1,954,110.0 | 164,496,049.0 | 200,132.0 |
| `base10num-near-miss` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 155,286,987.0 | 150,716,191.0 | 164,907,061.0 | 5,209,041.1 | 5 | 28,696 | 16,938 | 14,553 | 0.034 | compiled=5 | 1,967,913.0 | 151,113,923.0 | 195,120.0 |
| `bracket-array-define` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 234,698,658.0 | 231,997,484.0 | 242,790,539.0 | 3,661,758.4 | 5 | 32,768 | 27,406 | 27,091 | 0.016 | compiled=5 | 2,462,383.0 | 231,718,031.0 | 104,520.0 |
| `bracket-array-define` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 241,027,990.0 | 227,489,950.0 | 247,472,593.0 | 7,386,743.6 | 5 | 32,768 | 27,521 | 27,206 | 0.031 | compiled=5 | 2,278,702.0 | 238,652,388.0 | 188,171.0 |
| `bracket-array-define` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 241,356,209.0 | 237,396,025.0 | 250,701,000.0 | 4,711,324.1 | 5 | 32,768 | 27,406 | 27,091 | 0.020 | compiled=5 | 2,317,403.0 | 238,927,494.0 | 98,481.0 |
| `bracket-array-define` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 233,620,423.0 | 222,914,502.0 | 240,145,141.0 | 5,540,330.5 | 5 | 32,768 | 27,521 | 27,206 | 0.024 | compiled=5 | 2,298,213.0 | 231,046,779.0 | 208,211.0 |
| `bracket-array-define` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 240,673,545.0 | 226,552,552.0 | 240,948,386.0 | 5,605,589.7 | 5 | 32,768 | 27,406 | 27,091 | 0.023 | compiled=5 | 2,254,322.0 | 238,224,181.0 | 100,200.0 |
| `bracket-array-define` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 240,708,826.0 | 237,102,765.0 | 248,770,271.0 | 4,066,589.4 | 5 | 32,768 | 27,521 | 27,206 | 0.017 | compiled=5 | 2,256,962.0 | 238,403,702.0 | 185,271.0 |
| `codegrammar-flat` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 360,905,219.0 | 355,754,764.0 | 368,123,308.0 | 4,295,551.3 | 5 | 33,104 | 36,769 | 28,170 | 0.012 | compiled=5 | 3,032,765.0 | 357,642,794.0 | 191,292.0 |
| `codegrammar-flat` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 358,402,318.0 | 346,338,192.0 | 361,967,826.0 | 5,740,999.9 | 5 | 32,872 | 31,025 | 27,065 | 0.016 | compiled=5 | 2,668,174.0 | 355,659,613.0 | 203,401.0 |
| `codegrammar-flat` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 368,507,401.0 | 361,294,342.0 | 373,506,192.0 | 4,102,530.4 | 5 | 33,104 | 36,769 | 28,170 | 0.011 | compiled=5 | 3,043,238.0 | 365,339,194.0 | 104,751.0 |
| `codegrammar-flat` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 356,094,744.0 | 351,167,975.0 | 364,115,719.0 | 4,509,585.2 | 5 | 32,872 | 31,025 | 27,065 | 0.013 (max is trial 1) | compiled=5 | 2,663,526.0 | 353,333,587.0 | 112,830.0 |
| `codegrammar-flat` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 367,560,959.0 | 364,164,941.0 | 379,379,278.0 | 5,989,986.8 | 5 | 33,104 | 36,769 | 28,170 | 0.016 (max is trial 1) | compiled=5 | 3,009,957.0 | 364,398,521.0 | 188,901.0 |
| `codegrammar-flat` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 355,131,569.0 | 349,153,806.0 | 364,993,145.0 | 5,676,667.4 | 5 | 32,872 | 31,025 | 27,065 | 0.016 | compiled=5 | 2,651,725.0 | 349,412,707.0 | 187,901.0 |
| `codegrammar-xflag` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 370,045,247.0 | 366,164,478.0 | 382,970,133.0 | 5,953,988.2 | 5 | 33,144 | 37,095 | 28,417 | 0.016 | compiled=5 | 3,072,776.0 | 366,861,281.0 | 99,860.0 |
| `codegrammar-xflag` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 358,506,409.0 | 351,688,765.0 | 359,028,492.0 | 3,482,006.9 | 5 | 32,912 | 31,355 | 27,316 | 0.010 | compiled=5 | 2,679,984.0 | 355,640,054.0 | 106,090.0 |
| `codegrammar-xflag` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 361,244,610.0 | 359,727,013.0 | 362,592,389.0 | 943,060.3 | 5 | 33,144 | 37,095 | 28,417 | 0.003 | compiled=5 | 3,065,256.0 | 357,869,132.0 | 188,671.0 |
| `codegrammar-xflag` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 358,627,816.0 | 343,848,511.0 | 361,992,446.0 | 6,446,731.2 | 5 | 32,912 | 31,355 | 27,316 | 0.018 | compiled=5 | 2,669,395.0 | 355,864,481.0 | 104,191.0 |
| `codegrammar-xflag` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 367,798,420.0 | 363,946,248.0 | 368,648,597.0 | 1,674,607.1 | 5 | 33,144 | 37,095 | 28,417 | 0.005 | compiled=5 | 3,053,137.0 | 364,641,473.0 | 103,810.0 |
| `codegrammar-xflag` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 359,496,793.0 | 356,925,019.0 | 365,760,469.0 | 3,086,834.4 | 5 | 32,912 | 31,355 | 27,316 | 0.009 | compiled=5 | 2,633,085.0 | 356,765,579.0 | 108,481.0 |
| `currency-lookbehind-fixed` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 169,173,956.0 | 164,697,103.0 | 187,482,981.0 | 8,198,341.0 | 5 | 29,192 | 23,627 | 17,427 | 0.048 (max is trial 1) | compiled=5 | 4,697,104.0 | 164,450,602.0 | 97,531.0 |
| `currency-lookbehind-fixed` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 176,324,743.0 | 165,751,310.0 | 176,647,706.0 | 4,508,011.6 | 5 | 28,928 | 22,296 | 17,952 | 0.026 | compiled=5 | 2,383,632.0 | 173,385,288.0 | 186,942.0 |
| `currency-lookbehind-fixed` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 179,289,454.0 | 168,263,530.0 | 180,982,703.0 | 4,630,315.0 | 5 | 29,192 | 23,627 | 17,427 | 0.026 (max is trial 1) | compiled=5 | 2,473,444.0 | 174,538,396.0 | 182,681.0 |
| `currency-lookbehind-fixed` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 168,278,530.0 | 162,852,090.0 | 175,484,654.0 | 4,356,287.6 | 5 | 28,928 | 22,296 | 17,952 | 0.026 | compiled=5 | 2,728,925.0 | 165,705,985.0 | 200,981.0 |
| `currency-lookbehind-fixed` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 170,450,884.0 | 168,237,322.0 | 173,589,443.0 | 1,989,978.2 | 5 | 29,192 | 23,627 | 17,427 | 0.012 (max is trial 1) | compiled=5 | 2,364,923.0 | 168,131,300.0 | 96,540.0 |
| `currency-lookbehind-fixed` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 170,212,044.0 | 165,517,567.0 | 179,590,195.0 | 5,275,047.1 | 5 | 28,928 | 22,296 | 17,952 | 0.031 | compiled=5 | 2,296,863.0 | 165,369,404.0 | 104,910.0 |
| `date-nested-plus` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 270,409,531.0 | 268,837,343.0 | 281,906,231.0 | 4,986,517.8 | 5 | 32,992 | 34,825 | 32,799 | 0.018 (max is trial 1) | compiled=5 | 2,623,423.0 | 267,594,437.0 | 200,411.0 |
| `date-nested-plus` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 270,832,433.0 | 268,189,141.0 | 285,568,211.0 | 6,250,732.0 | 5 | 32,992 | 34,753 | 32,727 | 0.023 | compiled=5 | 3,016,936.0 | 265,160,384.0 | 105,781.0 |
| `date-nested-plus` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 269,249,607.0 | 268,417,792.0 | 280,239,919.0 | 4,442,836.9 | 5 | 32,992 | 34,825 | 32,799 | 0.017 | compiled=5 | 2,678,055.0 | 266,456,570.0 | 96,660.0 |
| `date-nested-plus` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 274,069,404.0 | 269,803,390.0 | 275,526,402.0 | 2,141,775.5 | 5 | 32,992 | 34,753 | 32,727 | 0.008 | compiled=5 | 2,653,065.0 | 271,223,627.0 | 186,691.0 |
| `date-nested-plus` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 268,960,186.0 | 268,040,611.0 | 275,989,357.0 | 3,498,078.2 | 5 | 32,992 | 34,825 | 32,799 | 0.013 | compiled=5 | 2,422,584.0 | 266,457,432.0 | 107,440.0 |
| `date-nested-plus` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 273,356,962.0 | 268,484,375.0 | 275,475,803.0 | 2,766,468.3 | 5 | 32,992 | 34,753 | 32,727 | 0.010 | compiled=5 | 2,587,085.0 | 270,583,676.0 | 186,311.0 |
| `doubled-word` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 408,802,927.0 | 396,657,636.0 | 411,093,591.0 | 5,103,698.7 | 5 | 36,776 | 26,683 | 24,753 | 0.012 | compiled=5 | 2,448,163.0 | 405,995,915.0 | 109,999.0 |
| `doubled-word` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 400,108,295.0 | 389,105,388.0 | 402,520,315.0 | 4,855,061.9 | 5 | 36,776 | 26,794 | 24,864 | 0.012 | compiled=5 | 2,396,973.0 | 397,600,652.0 | 107,270.0 |
| `doubled-word` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 442,836,047.0 | 437,238,605.0 | 452,081,740.0 | 4,795,523.6 | 5 | 36,736 | 26,614 | 24,684 | 0.011 | compiled=5 | 2,330,074.0 | 440,418,343.0 | 189,721.0 |
| `doubled-word` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 439,848,849.0 | 438,867,366.0 | 442,901,577.0 | 1,468,285.4 | 5 | 36,736 | 26,725 | 24,795 | 0.003 (max is trial 1) | compiled=5 | 2,401,353.0 | 437,177,004.0 | 108,301.0 |
| `doubled-word` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 406,159,721.0 | 403,088,412.0 | 406,819,056.0 | 1,343,226.7 | 5 | 36,776 | 26,683 | 24,753 | 0.003 | compiled=5 | 2,348,243.0 | 403,706,715.0 | 104,950.0 |
| `doubled-word` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 401,875,337.0 | 392,891,365.0 | 408,495,103.0 | 5,028,783.3 | 5 | 36,776 | 26,794 | 24,864 | 0.013 (max is trial 1) | compiled=5 | 2,332,964.0 | 399,334,191.0 | 201,591.0 |
| `dup-param-detect` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 251,612,254.0 | 247,043,520.0 | 258,540,530.0 | 4,398,406.3 | 5 | 32,936 | 30,471 | 28,487 | 0.017 | compiled=5 | 2,567,073.0 | 248,821,810.0 | 189,921.0 |
| `dup-param-detect` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 257,750,465.0 | 250,948,111.0 | 258,151,989.0 | 2,764,574.4 | 5 | 32,936 | 30,584 | 28,600 | 0.011 | compiled=5 | 2,561,793.0 | 254,969,682.0 | 191,451.0 |
| `dup-param-detect` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 255,528,309.0 | 250,890,351.0 | 257,921,073.0 | 2,558,804.0 | 5 | 32,888 | 30,402 | 28,418 | 0.010 | compiled=5 | 2,550,195.0 | 252,119,839.0 | 108,751.0 |
| `dup-param-detect` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 258,344,463.0 | 250,997,912.0 | 259,462,730.0 | 3,209,762.6 | 5 | 32,888 | 30,515 | 28,531 | 0.012 | compiled=5 | 2,573,864.0 | 255,663,549.0 | 107,051.0 |
| `dup-param-detect` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 251,270,126.0 | 248,419,758.0 | 258,271,636.0 | 3,364,707.6 | 5 | 32,936 | 30,471 | 28,487 | 0.013 | compiled=5 | 2,499,234.0 | 247,678,055.0 | 102,132.0 |
| `dup-param-detect` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 258,444,726.0 | 254,225,022.0 | 258,965,567.0 | 1,760,772.2 | 5 | 32,936 | 30,584 | 28,600 | 0.007 | compiled=5 | 2,518,235.0 | 255,816,411.0 | 103,140.0 |
| `email-local-nodup` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 211,540,216.0 | 207,662,167.0 | 215,502,778.0 | 3,276,207.2 | 5 | 32,880 | 27,854 | 25,663 | 0.015 | compiled=5 | 2,368,382.0 | 208,959,542.0 | 189,051.0 |
| `email-local-nodup` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 188,143,384.0 | 186,331,684.0 | 193,984,374.0 | 3,093,048.2 | 5 | 32,808 | 28,242 | 25,960 | 0.016 | compiled=5 | 2,389,843.0 | 185,015,898.0 | 197,811.0 |
| `email-local-nodup` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 214,355,053.0 | 208,776,363.0 | 220,871,659.0 | 3,869,010.6 | 5 | 32,880 | 27,854 | 25,663 | 0.018 (max is trial 1) | compiled=5 | 2,372,764.0 | 211,813,158.0 | 192,542.0 |
| `email-local-nodup` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 186,982,277.0 | 185,972,042.0 | 191,824,423.0 | 2,274,057.6 | 5 | 32,808 | 28,242 | 25,960 | 0.012 (max is trial 1) | compiled=5 | 2,412,954.0 | 184,362,082.0 | 185,721.0 |
| `email-local-nodup` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 215,608,433.0 | 211,731,651.0 | 218,485,910.0 | 2,356,330.8 | 5 | 32,880 | 27,854 | 25,663 | 0.011 | compiled=5 | 2,389,554.0 | 213,066,488.0 | 186,911.0 |
| `email-local-nodup` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 186,761,197.0 | 180,134,820.0 | 201,359,490.0 | 7,031,792.5 | 5 | 32,808 | 28,242 | 25,960 | 0.038 | compiled=5 | 2,350,174.0 | 184,308,243.0 | 100,821.0 |
| `email-nested-plus` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 228,944,987.0 | 225,353,709.0 | 239,996,034.0 | 5,971,284.4 | 5 | 32,952 | 30,168 | 28,222 | 0.026 | compiled=5 | 2,441,833.0 | 226,317,093.0 | 189,161.0 |
| `email-nested-plus` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 240,675,018.0 | 236,202,795.0 | 246,692,569.0 | 3,558,101.7 | 5 | 32,952 | 30,599 | 28,569 | 0.015 | compiled=5 | 2,469,732.0 | 238,132,225.0 | 98,830.0 |
| `email-nested-plus` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 242,121,141.0 | 233,060,902.0 | 248,111,795.0 | 5,138,693.6 | 5 | 32,952 | 30,168 | 28,222 | 0.021 | compiled=5 | 2,452,744.0 | 236,758,561.0 | 182,921.0 |
| `email-nested-plus` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 240,120,556.0 | 222,602,710.0 | 241,152,685.0 | 7,164,744.4 | 5 | 32,952 | 30,599 | 28,569 | 0.030 | compiled=5 | 2,469,433.0 | 237,551,034.0 | 100,089.0 |
| `email-nested-plus` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 238,177,650.0 | 232,068,635.0 | 242,928,257.0 | 4,083,452.3 | 5 | 32,952 | 30,168 | 28,222 | 0.017 | compiled=5 | 2,438,914.0 | 232,941,391.0 | 101,239.0 |
| `email-nested-plus` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 238,736,594.0 | 233,071,761.0 | 250,445,261.0 | 5,716,776.7 | 5 | 32,952 | 30,599 | 28,569 | 0.024 | compiled=5 | 2,427,504.0 | 236,208,469.0 | 102,541.0 |
| `evil-alt-nested` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 242,649,788.0 | 234,750,378.0 | 247,549,334.0 | 4,754,696.7 | 5 | 32,912 | 30,605 | 28,994 | 0.020 | compiled=5 | 2,488,453.0 | 239,941,944.0 | 110,812.0 |
| `evil-alt-nested` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 240,363,246.0 | 231,083,838.0 | 246,590,489.0 | 6,016,497.5 | 5 | 32,872 | 30,533 | 28,922 | 0.025 | compiled=5 | 5,191,797.0 | 237,684,492.0 | 183,880.0 |
| `evil-alt-nested` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 247,281,411.0 | 236,323,338.0 | 248,657,080.0 | 5,424,398.5 | 5 | 32,912 | 30,605 | 28,994 | 0.022 (max is trial 1) | compiled=5 | 2,486,404.0 | 242,479,393.0 | 189,511.0 |
| `evil-alt-nested` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 241,267,587.0 | 233,340,683.0 | 247,051,370.0 | 5,322,015.9 | 5 | 32,872 | 30,533 | 28,922 | 0.022 | compiled=5 | 2,487,334.0 | 238,601,312.0 | 111,251.0 |
| `evil-alt-nested` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 243,407,699.0 | 237,489,007.0 | 244,584,116.0 | 2,636,412.5 | 5 | 32,912 | 30,605 | 28,994 | 0.011 | compiled=5 | 2,443,993.0 | 240,862,316.0 | 102,901.0 |
| `evil-alt-nested` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 235,644,337.0 | 232,710,260.0 | 250,765,895.0 | 6,727,559.6 | 5 | 32,872 | 30,533 | 28,922 | 0.029 | compiled=5 | 2,421,504.0 | 231,443,712.0 | 180,771.0 |
| `file-ext-order` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 172,373,004.0 | 166,319,002.0 | 173,318,869.0 | 2,627,840.9 | 5 | 28,912 | 22,208 | 16,085 | 0.015 | compiled=5 | 2,537,332.0 | 169,736,750.0 | 104,610.0 |
| `file-ext-order` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 168,800,964.0 | 158,262,589.0 | 169,863,741.0 | 4,928,521.3 | 5 | 28,808 | 20,782 | 15,940 | 0.029 | compiled=5 | 2,298,172.0 | 165,916,639.0 | 99,040.0 |
| `file-ext-order` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 172,925,547.0 | 169,360,289.0 | 180,221,117.0 | 4,203,995.7 | 5 | 28,912 | 22,208 | 16,085 | 0.024 | compiled=5 | 2,511,334.0 | 170,391,123.0 | 111,291.0 |
| `file-ext-order` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 169,778,068.0 | 150,682,910.0 | 177,050,230.0 | 9,406,271.3 | 5 | 28,808 | 20,782 | 15,940 | 0.055 | compiled=5 | 2,591,784.0 | 167,384,945.0 | 92,770.0 |
| `file-ext-order` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 171,710,662.0 | 163,394,914.0 | 177,847,266.0 | 5,388,865.1 | 5 | 28,912 | 22,208 | 16,085 | 0.031 | compiled=5 | 2,470,284.0 | 168,651,063.0 | 97,590.0 |
| `file-ext-order` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 167,005,195.0 | 158,390,714.0 | 169,995,512.0 | 4,234,812.8 | 5 | 28,808 | 20,782 | 15,940 | 0.025 | compiled=5 | 2,262,193.0 | 164,569,631.0 | 186,492.0 |
| `float-literal-bound` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 174,407,685.0 | 166,283,953.0 | 180,537,657.0 | 4,585,595.1 | 5 | 29,280 | 24,780 | 17,604 | 0.026 | compiled=5 | 3,232,926.0 | 169,595,089.0 | 187,161.0 |
| `float-literal-bound` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 179,412,329.0 | 168,333,862.0 | 182,159,483.0 | 4,909,157.9 | 5 | 28,976 | 21,824 | 17,847 | 0.027 | compiled=5 | 2,368,913.0 | 177,010,868.0 | 96,180.0 |
| `float-literal-bound` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 171,401,207.0 | 164,879,171.0 | 177,480,861.0 | 4,613,720.7 | 5 | 29,280 | 24,780 | 17,604 | 0.027 | compiled=5 | 2,659,815.0 | 168,854,374.0 | 105,730.0 |
| `float-literal-bound` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 182,653,623.0 | 172,069,002.0 | 184,338,873.0 | 4,415,043.7 | 5 | 28,976 | 21,824 | 17,847 | 0.024 | compiled=5 | 2,328,253.0 | 176,957,790.0 | 190,452.0 |
| `float-literal-bound` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 180,403,122.0 | 170,816,586.0 | 182,877,773.0 | 4,436,958.6 | 5 | 29,280 | 24,780 | 17,604 | 0.025 | compiled=5 | 2,516,064.0 | 177,744,946.0 | 191,042.0 |
| `float-literal-bound` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 180,606,541.0 | 175,464,603.0 | 183,882,811.0 | 2,717,690.5 | 5 | 28,976 | 21,824 | 17,847 | 0.015 | compiled=5 | 2,468,904.0 | 178,166,858.0 | 183,882.0 |
| `floor-byte` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 160,430,580.0 | 154,318,441.0 | 165,160,367.0 | 3,788,194.1 | 5 | 28,768 | 17,890 | 14,559 | 0.024 | compiled=5 | 2,153,843.0 | 157,775,107.0 | 192,571.0 |
| `floor-byte` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 164,782,104.0 | 159,149,933.0 | 168,550,345.0 | 3,221,247.1 | 5 | 28,808 | 19,475 | 15,917 | 0.020 | compiled=5 | 2,121,391.0 | 162,575,392.0 | 194,091.0 |
| `floor-byte` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 161,022,408.0 | 151,077,971.0 | 165,299,253.0 | 5,586,274.7 | 5 | 28,768 | 17,890 | 14,559 | 0.035 | compiled=5 | 2,162,862.0 | 158,720,646.0 | 118,261.0 |
| `floor-byte` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 167,704,458.0 | 156,159,611.0 | 168,814,364.0 | 5,643,668.8 | 5 | 28,808 | 19,475 | 15,917 | 0.034 | compiled=5 | 2,092,962.0 | 165,522,005.0 | 184,281.0 |
| `floor-byte` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 164,923,034.0 | 159,014,859.0 | 167,612,599.0 | 3,267,700.7 | 5 | 28,768 | 17,890 | 14,559 | 0.020 | compiled=5 | 2,189,773.0 | 160,036,325.0 | 104,671.0 |
| `floor-byte` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 164,893,412.0 | 150,311,179.0 | 171,327,157.0 | 7,542,839.8 | 5 | 28,808 | 19,475 | 15,917 | 0.046 | compiled=5 | 2,104,002.0 | 162,358,658.0 | 108,239.0 |
| `hex8-bounded` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 165,541,267.0 | 156,571,169.0 | 171,055,717.0 | 5,526,173.9 | 5 | 28,976 | 21,414 | 15,639 | 0.033 | compiled=5 | 2,538,713.0 | 162,919,974.0 | 97,610.0 |
| `hex8-bounded` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 177,591,422.0 | 172,359,914.0 | 180,823,917.0 | 3,610,530.9 | 5 | 28,968 | 23,878 | 18,099 | 0.020 | compiled=5 | 2,522,353.0 | 174,942,027.0 | 185,901.0 |
| `hex8-bounded` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 162,103,726.0 | 158,407,083.0 | 174,278,564.0 | 5,851,546.6 | 5 | 28,976 | 21,414 | 15,639 | 0.036 | compiled=5 | 2,532,604.0 | 156,635,304.0 | 113,201.0 |
| `hex8-bounded` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 179,542,065.0 | 178,950,312.0 | 187,836,492.0 | 3,376,334.1 | 5 | 28,968 | 23,878 | 18,099 | 0.019 | compiled=5 | 2,667,045.0 | 176,776,879.0 | 111,321.0 |
| `hex8-bounded` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 168,639,614.0 | 162,199,456.0 | 168,980,484.0 | 2,627,511.4 | 5 | 28,976 | 21,414 | 15,639 | 0.016 | compiled=5 | 2,502,615.0 | 165,954,979.0 | 105,241.0 |
| `hex8-bounded` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 171,634,509.0 | 163,131,453.0 | 180,227,269.0 | 6,464,054.5 | 5 | 28,968 | 23,878 | 18,099 | 0.038 | compiled=5 | 2,559,744.0 | 168,579,822.0 | 203,221.0 |
| `high-byte-run` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 186,256,086.0 | 182,829,147.0 | 194,390,976.0 | 3,912,566.2 | 5 | 28,608 | 26,964 | 20,658 | 0.021 | compiled=5 | 2,715,033.0 | 183,329,850.0 | 109,090.0 |
| `high-byte-run` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 177,268,059.0 | 170,369,983.0 | 187,299,520.0 | 5,846,664.0 | 5 | 28,808 | 21,492 | 17,790 | 0.033 | compiled=5 | 2,334,062.0 | 174,921,757.0 | 103,861.0 |
| `high-byte-run` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 187,561,900.0 | 185,184,126.0 | 191,157,892.0 | 2,165,804.4 | 5 | 28,608 | 26,964 | 20,658 | 0.012 | compiled=5 | 2,812,966.0 | 182,619,642.0 | 104,390.0 |
| `high-byte-run` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 174,959,958.0 | 163,184,592.0 | 179,685,787.0 | 5,786,812.3 | 5 | 28,808 | 21,492 | 17,790 | 0.033 | compiled=5 | 2,352,973.0 | 172,508,224.0 | 184,392.0 |
| `high-byte-run` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 186,304,103.0 | 178,429,549.0 | 188,477,158.0 | 4,395,038.4 | 5 | 28,608 | 26,964 | 20,658 | 0.024 | compiled=5 | 2,631,705.0 | 183,526,638.0 | 98,380.0 |
| `high-byte-run` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 176,645,188.0 | 166,884,033.0 | 178,828,031.0 | 4,283,571.0 | 5 | 28,808 | 21,492 | 17,790 | 0.024 | compiled=5 | 2,278,693.0 | 174,258,715.0 | 107,780.0 |
| `ipv4-near-miss` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 174,674,674.0 | 166,722,032.0 | 183,935,074.0 | 6,387,039.0 | 5 | 37,824 | 24,450 | 19,134 | 0.037 | compiled=5 | 2,261,082.0 | 172,206,842.0 | 190,501.0 |
| `ipv4-near-miss` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 178,372,524.0 | 176,514,686.0 | 179,382,369.0 | 927,589.5 | 5 | 37,616 | 23,528 | 18,212 | 0.005 | compiled=5 | 2,270,661.0 | 175,942,042.0 | 181,121.0 |
| `ipv4-near-miss` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 184,675,093.0 | 179,156,113.0 | 194,062,298.0 | 4,819,192.0 | 5 | 37,824 | 24,450 | 19,134 | 0.026 | compiled=5 | 2,248,353.0 | 182,303,820.0 | 190,901.0 |
| `ipv4-near-miss` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 178,860,481.0 | 171,082,766.0 | 182,368,092.0 | 3,908,780.7 | 5 | 37,616 | 23,528 | 18,212 | 0.022 (max is trial 1) | compiled=5 | 2,256,363.0 | 176,500,097.0 | 200,411.0 |
| `ipv4-near-miss` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 183,993,052.0 | 178,562,230.0 | 193,324,162.0 | 5,082,717.0 | 5 | 37,824 | 24,450 | 19,134 | 0.028 | compiled=5 | 2,187,253.0 | 181,697,578.0 | 188,391.0 |
| `ipv4-near-miss` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 177,296,744.0 | 171,012,997.0 | 181,730,297.0 | 4,091,678.8 | 5 | 37,616 | 23,528 | 18,212 | 0.023 | compiled=5 | 2,198,843.0 | 172,301,356.0 | 106,650.0 |
| `keyword-prefix-order` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 164,941,606.0 | 158,010,869.0 | 169,050,315.0 | 3,863,683.6 | 5 | 28,912 | 22,679 | 16,065 | 0.023 (max is trial 1) | compiled=5 | 2,502,804.0 | 161,890,060.0 | 199,270.0 |
| `keyword-prefix-order` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 159,981,927.0 | 152,890,813.0 | 173,526,690.0 | 6,773,693.6 | 5 | 28,808 | 22,080 | 15,935 | 0.042 | compiled=5 | 2,724,874.0 | 157,051,804.0 | 189,121.0 |
| `keyword-prefix-order` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 170,797,994.0 | 164,894,831.0 | 174,064,642.0 | 3,194,412.7 | 5 | 28,912 | 22,679 | 16,065 | 0.019 | compiled=5 | 2,478,094.0 | 168,128,579.0 | 186,801.0 |
| `keyword-prefix-order` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 166,302,789.0 | 159,721,081.0 | 170,471,352.0 | 3,862,128.1 | 5 | 28,808 | 22,080 | 15,935 | 0.023 (max is trial 1) | compiled=5 | 2,366,673.0 | 163,746,004.0 | 195,591.0 |
| `keyword-prefix-order` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 160,520,636.0 | 154,710,424.0 | 174,559,548.0 | 7,884,010.3 | 5 | 28,912 | 22,679 | 16,065 | 0.049 | compiled=5 | 2,432,904.0 | 157,992,922.0 | 103,171.0 |
| `keyword-prefix-order` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 167,444,097.0 | 153,970,940.0 | 169,443,018.0 | 5,985,435.8 | 5 | 28,808 | 22,080 | 15,935 | 0.036 | compiled=5 | 2,304,514.0 | 165,017,513.0 | 185,141.0 |
| `letters-bounded-tail-z` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 339,566,689.0 | 330,567,272.0 | 369,743,507.0 | 13,897,228.1 | 5 | 45,192 | 77,018 | 16,926 | 0.041 | compiled=5 | 151,524,215.0 | 182,341,265.0 | 107,171.0 |
| `letters-bounded-tail-z` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 340,087,133.0 | 325,000,925.0 | 354,105,505.0 | 9,928,875.4 | 5 | 45,192 | 77,026 | 16,934 | 0.029 | compiled=5 | 153,331,195.0 | 175,775,820.0 | 185,081.0 |
| `letters-bounded-tail-z` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 342,561,395.0 | 334,928,222.0 | 355,429,418.0 | 6,658,841.4 | 5 | 45,192 | 77,018 | 16,926 | 0.019 | compiled=5 | 151,748,786.0 | 184,893,086.0 | 186,411.0 |
| `letters-bounded-tail-z` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 338,223,839.0 | 325,249,258.0 | 342,783,437.0 | 6,403,579.6 | 5 | 45,192 | 77,026 | 16,934 | 0.019 | compiled=5 | 157,391,268.0 | 178,100,946.0 | 104,130.0 |
| `letters-bounded-tail-z` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 340,484,896.0 | 320,211,929.0 | 350,930,514.0 | 11,608,702.1 | 5 | 45,192 | 77,018 | 16,926 | 0.034 (max is trial 1) | compiled=5 | 148,389,767.0 | 182,504,243.0 | 191,701.0 |
| `letters-bounded-tail-z` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 333,417,955.0 | 320,936,742.0 | 361,071,833.0 | 15,212,896.8 | 5 | 45,192 | 77,026 | 16,934 | 0.046 | compiled=5 | 148,877,931.0 | 173,932,274.0 | 99,090.0 |
| `logparse-atomic` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 300,729,189.0 | 299,625,872.0 | 306,466,668.0 | 2,848,428.8 | 5 | 84,144 | 59,426 | 39,493 | 0.009 | compiled=5 | 8,813,656.0 | 295,758,232.0 | 119,871.0 |
| `logparse-atomic` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 303,219,601.0 | 296,384,035.0 | 305,111,801.0 | 2,986,913.2 | 5 | 84,104 | 59,353 | 39,420 | 0.010 | compiled=5 | 3,726,339.0 | 297,139,630.0 | 117,181.0 |
| `logparse-atomic` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 299,252,758.0 | 290,222,067.0 | 304,656,609.0 | 4,662,288.0 | 5 | 84,144 | 59,426 | 39,493 | 0.016 | compiled=5 | 4,132,904.0 | 295,466,536.0 | 114,601.0 |
| `logparse-atomic` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 303,374,781.0 | 299,800,440.0 | 304,029,947.0 | 1,559,925.6 | 5 | 84,104 | 59,353 | 39,420 | 0.005 | compiled=5 | 3,710,171.0 | 299,438,869.0 | 125,871.0 |
| `logparse-atomic` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 299,146,870.0 | 291,930,988.0 | 316,323,978.0 | 8,906,915.7 | 5 | 84,144 | 59,426 | 39,493 | 0.030 (max is trial 1) | compiled=5 | 3,569,520.0 | 295,487,018.0 | 121,561.0 |
| `logparse-atomic` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 303,372,913.0 | 291,415,204.0 | 303,673,435.0 | 5,336,340.9 | 5 | 84,104 | 59,353 | 39,420 | 0.018 | compiled=5 | 3,577,830.0 | 299,340,840.0 | 216,851.0 |
| `logparse-atomic-removed` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 290,571,297.0 | 290,237,173.0 | 301,092,840.0 | 4,215,548.4 | 5 | 84,144 | 59,142 | 39,209 | 0.015 | compiled=5 | 3,645,059.0 | 286,524,175.0 | 213,721.0 |
| `logparse-atomic-removed` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 304,186,267.0 | 295,701,813.0 | 316,769,902.0 | 6,960,534.8 | 5 | 84,104 | 59,069 | 39,136 | 0.023 (max is trial 1) | compiled=5 | 3,616,829.0 | 300,453,397.0 | 126,021.0 |
| `logparse-atomic-removed` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 296,067,310.0 | 291,211,823.0 | 298,046,540.0 | 2,489,059.7 | 5 | 84,144 | 59,142 | 39,209 | 0.008 | compiled=5 | 3,627,591.0 | 292,224,078.0 | 124,351.0 |
| `logparse-atomic-removed` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 302,131,205.0 | 294,708,771.0 | 303,463,981.0 | 3,377,558.9 | 5 | 84,104 | 59,069 | 39,136 | 0.011 | compiled=5 | 3,718,122.0 | 298,043,711.0 | 218,822.0 |
| `logparse-atomic-removed` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 298,753,977.0 | 283,677,640.0 | 306,453,350.0 | 8,477,926.0 | 5 | 84,144 | 59,142 | 39,209 | 0.028 | compiled=5 | 3,549,570.0 | 294,392,351.0 | 238,701.0 |
| `logparse-atomic-removed` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 299,725,832.0 | 292,996,934.0 | 302,458,278.0 | 3,622,334.8 | 5 | 84,104 | 59,069 | 39,136 | 0.012 | compiled=5 | 3,545,951.0 | 291,510,676.0 | 135,411.0 |
| `mojibake-curly-quote` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 167,656,960.0 | 162,039,619.0 | 170,153,952.0 | 3,282,766.1 | 5 | 28,912 | 20,801 | 15,598 | 0.020 | compiled=5 | 4,769,665.0 | 162,537,482.0 | 107,330.0 |
| `mojibake-curly-quote` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 159,580,467.0 | 157,151,474.0 | 173,437,448.0 | 6,066,964.7 | 5 | 28,808 | 19,701 | 15,939 | 0.038 | compiled=5 | 2,324,232.0 | 157,159,125.0 | 187,380.0 |
| `mojibake-curly-quote` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 165,340,123.0 | 160,695,347.0 | 170,965,535.0 | 3,952,036.3 | 5 | 28,912 | 20,801 | 15,598 | 0.024 | compiled=5 | 2,415,754.0 | 160,059,723.0 | 186,801.0 |
| `mojibake-curly-quote` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 159,458,970.0 | 149,206,950.0 | 167,071,861.0 | 6,122,108.2 | 5 | 28,808 | 19,701 | 15,939 | 0.038 | compiled=5 | 2,568,945.0 | 156,716,975.0 | 181,211.0 |
| `mojibake-curly-quote` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 161,726,984.0 | 159,626,151.0 | 163,284,632.0 | 1,319,278.9 | 5 | 28,912 | 20,801 | 15,598 | 0.008 | compiled=5 | 2,222,152.0 | 159,318,470.0 | 198,690.0 |
| `mojibake-curly-quote` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 161,906,234.0 | 157,233,368.0 | 169,990,802.0 | 4,464,208.2 | 5 | 28,808 | 19,701 | 15,939 | 0.028 | compiled=5 | 4,386,985.0 | 157,247,858.0 | 99,640.0 |
| `negation-scope-lookbehind-var` | `plain` | `pcrec_00c97769_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `negation-scope-lookbehind-var` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `negation-scope-lookbehind-var` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `nested-comment-rec` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 275,640,048.0 | 272,016,250.0 | 285,689,101.0 | 4,824,777.6 | 5 | 32,848 | 32,720 | 31,021 | 0.018 | compiled=5 | 2,512,363.0 | 273,021,845.0 | 194,551.0 |
| `nested-comment-rec` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 284,067,441.0 | 270,439,970.0 | 290,071,172.0 | 6,517,238.4 | 5 | 32,848 | 32,833 | 31,134 | 0.023 (max is trial 1) | compiled=5 | 2,562,093.0 | 281,419,989.0 | 107,751.0 |
| `nested-comment-rec` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 283,491,648.0 | 283,337,887.0 | 288,546,257.0 | 2,049,822.9 | 5 | 32,848 | 32,720 | 31,021 | 0.007 (max is trial 1) | compiled=5 | 2,545,514.0 | 280,764,742.0 | 190,131.0 |
| `nested-comment-rec` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 283,479,517.0 | 278,196,208.0 | 292,558,430.0 | 4,952,392.3 | 5 | 32,848 | 32,833 | 31,134 | 0.017 | compiled=5 | 2,655,345.0 | 280,820,982.0 | 104,831.0 |
| `nested-comment-rec` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 282,482,364.0 | 270,976,768.0 | 285,243,401.0 | 5,064,076.6 | 5 | 32,848 | 32,720 | 31,021 | 0.018 | compiled=5 | 2,500,654.0 | 279,875,689.0 | 108,270.0 |
| `nested-comment-rec` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 283,324,408.0 | 277,726,369.0 | 289,869,695.0 | 3,850,602.3 | 5 | 32,848 | 32,833 | 31,134 | 0.014 (max is trial 1) | compiled=5 | 2,490,194.0 | 280,624,674.0 | 194,822.0 |
| `numeric-id-nested-plus` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 236,084,703.0 | 225,594,339.0 | 245,153,681.0 | 6,470,763.9 | 5 | 32,872 | 29,830 | 28,148 | 0.027 | compiled=5 | 2,430,182.0 | 233,526,270.0 | 188,331.0 |
| `numeric-id-nested-plus` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 232,951,008.0 | 226,327,543.0 | 240,148,725.0 | 4,930,238.1 | 5 | 32,872 | 29,759 | 28,077 | 0.021 (max is trial 1) | compiled=5 | 2,583,224.0 | 230,259,473.0 | 121,751.0 |
| `numeric-id-nested-plus` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 235,728,314.0 | 230,321,354.0 | 240,150,621.0 | 3,866,903.5 | 5 | 32,872 | 29,830 | 28,148 | 0.016 | compiled=5 | 4,876,878.0 | 233,119,000.0 | 183,891.0 |
| `numeric-id-nested-plus` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 231,161,170.0 | 225,426,956.0 | 244,949,797.0 | 7,174,304.7 | 5 | 32,872 | 29,759 | 28,077 | 0.031 | compiled=5 | 2,429,955.0 | 225,414,257.0 | 204,751.0 |
| `numeric-id-nested-plus` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 234,484,180.0 | 225,346,007.0 | 242,083,564.0 | 5,733,137.7 | 5 | 32,872 | 29,830 | 28,148 | 0.024 | compiled=5 | 2,372,464.0 | 231,992,475.0 | 119,241.0 |
| `numeric-id-nested-plus` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 225,735,269.0 | 222,849,692.0 | 243,830,313.0 | 7,653,514.8 | 5 | 32,872 | 29,759 | 28,077 | 0.034 | compiled=5 | 2,391,105.0 | 223,191,825.0 | 190,541.0 |
| `phone-list-nested-plus` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 246,722,238.0 | 233,039,620.0 | 248,179,196.0 | 5,761,861.5 | 5 | 32,952 | 31,102 | 29,160 | 0.023 | compiled=5 | 2,498,313.0 | 244,064,504.0 | 101,830.0 |
| `phone-list-nested-plus` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 243,733,832.0 | 237,988,825.0 | 247,237,311.0 | 3,182,959.9 | 5 | 32,912 | 31,030 | 29,088 | 0.013 | compiled=5 | 2,917,105.0 | 238,470,785.0 | 114,411.0 |
| `phone-list-nested-plus` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 244,852,257.0 | 241,043,566.0 | 247,778,135.0 | 2,511,008.4 | 5 | 32,952 | 31,102 | 29,160 | 0.010 | compiled=5 | 2,520,525.0 | 242,120,822.0 | 111,450.0 |
| `phone-list-nested-plus` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 240,505,764.0 | 239,458,545.0 | 246,601,927.0 | 2,550,103.8 | 5 | 32,912 | 31,030 | 29,088 | 0.011 | compiled=5 | 2,713,766.0 | 237,591,405.0 | 183,362.0 |
| `phone-list-nested-plus` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 247,580,315.0 | 240,197,902.0 | 253,837,003.0 | 4,485,033.1 | 5 | 32,952 | 31,102 | 29,160 | 0.018 (max is trial 1) | compiled=5 | 2,457,594.0 | 245,016,100.0 | 192,581.0 |
| `phone-list-nested-plus` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 245,571,743.0 | 239,363,668.0 | 246,533,637.0 | 3,029,821.3 | 5 | 32,912 | 31,030 | 29,088 | 0.012 | compiled=5 | 2,486,603.0 | 242,895,418.0 | 101,990.0 |
| `phone-palindrome-6` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 315,199,293.0 | 314,448,231.0 | 320,400,790.0 | 2,173,377.1 | 5 | 32,600 | 26,349 | 24,881 | 0.007 | compiled=5 | 2,294,253.0 | 312,589,499.0 | 187,681.0 |
| `phone-palindrome-6` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 219,451,148.0 | 215,786,865.0 | 221,217,456.0 | 1,871,792.3 | 5 | 32,680 | 26,157 | 24,689 | 0.009 | compiled=5 | 2,329,573.0 | 217,016,313.0 | 107,860.0 |
| `phone-palindrome-6` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 290,726,950.0 | 282,980,917.0 | 302,592,926.0 | 6,725,293.6 | 5 | 32,552 | 26,280 | 24,812 | 0.023 (max is trial 1) | compiled=5 | 2,239,583.0 | 288,548,477.0 | 187,702.0 |
| `phone-palindrome-6` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 229,699,363.0 | 222,596,560.0 | 231,701,761.0 | 3,538,073.7 | 5 | 32,632 | 26,088 | 24,620 | 0.015 | compiled=5 | 2,277,662.0 | 224,916,575.0 | 184,601.0 |
| `phone-palindrome-6` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 321,963,830.0 | 315,348,550.0 | 331,665,866.0 | 6,048,037.4 | 5 | 32,600 | 26,349 | 24,881 | 0.019 | compiled=5 | 2,572,085.0 | 319,289,254.0 | 191,231.0 |
| `phone-palindrome-6` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 220,586,411.0 | 215,682,002.0 | 221,264,962.0 | 2,042,621.6 | 5 | 32,680 | 26,157 | 24,689 | 0.009 | compiled=5 | 2,241,421.0 | 217,706,293.0 | 107,630.0 |
| `pwd-strength-chain` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 268,418,321.0 | 263,843,778.0 | 269,325,558.0 | 1,958,068.1 | 5 | 33,104 | 34,230 | 31,589 | 0.007 | compiled=5 | 2,636,524.0 | 265,668,547.0 | 191,942.0 |
| `pwd-strength-chain` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 260,094,878.0 | 259,936,119.0 | 269,820,839.0 | 3,867,577.9 | 5 | 33,104 | 34,158 | 31,517 | 0.015 | compiled=5 | 2,637,493.0 | 257,347,804.0 | 189,161.0 |
| `pwd-strength-chain` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 267,152,546.0 | 260,302,875.0 | 267,847,427.0 | 2,987,047.9 | 5 | 33,104 | 34,230 | 31,589 | 0.011 | compiled=5 | 2,636,406.0 | 264,403,239.0 | 189,701.0 |
| `pwd-strength-chain` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 263,097,272.0 | 251,316,415.0 | 271,733,709.0 | 7,015,941.4 | 5 | 33,104 | 34,158 | 31,517 | 0.027 | compiled=5 | 2,619,315.0 | 260,218,105.0 | 190,111.0 |
| `pwd-strength-chain` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 268,565,554.0 | 263,207,024.0 | 272,609,298.0 | 2,994,599.8 | 5 | 33,104 | 34,230 | 31,589 | 0.011 | compiled=5 | 2,613,985.0 | 265,685,028.0 | 108,140.0 |
| `pwd-strength-chain` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 269,098,958.0 | 263,399,865.0 | 274,544,439.0 | 4,374,241.2 | 5 | 33,104 | 34,158 | 31,517 | 0.016 | compiled=5 | 2,710,736.0 | 266,249,081.0 | 194,581.0 |
| `quoted-delim-match` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 242,503,936.0 | 236,151,784.0 | 245,990,284.0 | 3,512,115.3 | 5 | 32,920 | 29,135 | 26,974 | 0.014 (max is trial 1) | compiled=5 | 2,542,295.0 | 239,701,273.0 | 188,310.0 |
| `quoted-delim-match` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 237,066,350.0 | 233,858,733.0 | 242,059,545.0 | 3,363,241.0 | 5 | 32,920 | 29,248 | 27,087 | 0.014 | compiled=5 | 2,403,961.0 | 234,036,493.0 | 185,791.0 |
| `quoted-delim-match` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 244,563,727.0 | 236,402,260.0 | 248,749,958.0 | 4,341,197.8 | 5 | 32,880 | 29,066 | 26,905 | 0.018 | compiled=5 | 2,384,874.0 | 242,040,691.0 | 100,160.0 |
| `quoted-delim-match` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 244,922,948.0 | 225,332,926.0 | 262,639,759.0 | 12,464,541.0 | 5 | 32,880 | 29,179 | 27,018 | 0.051 | compiled=5 | 2,395,093.0 | 242,449,234.0 | 188,482.0 |
| `quoted-delim-match` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 240,822,795.0 | 237,071,187.0 | 242,039,584.0 | 1,796,252.1 | 5 | 32,920 | 29,135 | 26,974 | 0.007 | compiled=5 | 2,375,924.0 | 238,353,161.0 | 97,910.0 |
| `quoted-delim-match` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 241,702,133.0 | 234,109,718.0 | 241,973,493.0 | 3,024,316.8 | 5 | 32,920 | 29,248 | 27,087 | 0.013 | compiled=5 | 2,343,363.0 | 239,189,407.0 | 214,091.0 |
| `router-prefix-order` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 161,711,038.0 | 156,861,683.0 | 168,240,742.0 | 3,816,280.0 | 5 | 28,912 | 22,195 | 16,215 | 0.024 (max is trial 1) | compiled=5 | 2,752,524.0 | 158,991,594.0 | 207,101.0 |
| `router-prefix-order` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 164,810,642.0 | 160,396,120.0 | 168,863,496.0 | 2,940,429.5 | 5 | 28,808 | 20,438 | 15,936 | 0.018 | compiled=5 | 2,311,641.0 | 159,739,237.0 | 107,600.0 |
| `router-prefix-order` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 168,626,682.0 | 156,948,715.0 | 172,419,166.0 | 5,672,572.8 | 5 | 28,912 | 22,195 | 16,215 | 0.034 | compiled=5 | 2,517,714.0 | 166,097,298.0 | 100,950.0 |
| `router-prefix-order` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 165,177,672.0 | 161,341,171.0 | 169,634,208.0 | 3,274,313.8 | 5 | 28,808 | 20,438 | 15,936 | 0.020 | compiled=5 | 2,277,323.0 | 162,806,409.0 | 102,140.0 |
| `router-prefix-order` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 172,015,784.0 | 165,440,726.0 | 174,996,781.0 | 3,566,034.9 | 5 | 28,912 | 22,195 | 16,215 | 0.021 | compiled=5 | 2,528,545.0 | 169,093,845.0 | 196,671.0 |
| `router-prefix-order` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 165,181,975.0 | 162,959,551.0 | 167,463,635.0 | 1,760,104.1 | 5 | 28,808 | 20,438 | 15,936 | 0.011 | compiled=5 | 2,246,993.0 | 162,718,900.0 | 101,740.0 |
| `tag-depth3-bound` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 312,593,461.0 | 310,138,396.0 | 313,367,585.0 | 1,187,796.3 | 5 | 37,072 | 36,857 | 34,873 | 0.004 | compiled=5 | 2,873,405.0 | 309,521,445.0 | 109,580.0 |
| `tag-depth3-bound` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 313,014,782.0 | 304,083,296.0 | 314,525,619.0 | 3,888,121.2 | 5 | 37,072 | 36,970 | 34,986 | 0.012 | compiled=5 | 2,858,365.0 | 309,968,126.0 | 108,349.0 |
| `tag-depth3-bound` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 323,366,575.0 | 313,621,050.0 | 330,360,015.0 | 6,094,316.0 | 5 | 37,024 | 36,788 | 34,804 | 0.019 | compiled=5 | 2,911,836.0 | 320,369,818.0 | 183,770.0 |
| `tag-depth3-bound` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 325,071,203.0 | 316,329,516.0 | 335,150,794.0 | 8,312,955.6 | 5 | 37,024 | 36,901 | 34,917 | 0.026 (max is trial 1) | compiled=5 | 2,892,356.0 | 322,061,637.0 | 187,961.0 |
| `tag-depth3-bound` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 304,852,291.0 | 303,839,165.0 | 317,041,353.0 | 5,145,197.3 | 5 | 37,072 | 36,857 | 34,873 | 0.017 | compiled=5 | 2,776,865.0 | 302,050,105.0 | 107,611.0 |
| `tag-depth3-bound` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 308,778,716.0 | 305,907,297.0 | 311,759,671.0 | 2,198,977.6 | 5 | 37,072 | 36,970 | 34,986 | 0.007 | compiled=5 | 2,843,406.0 | 303,038,091.0 | 101,131.0 |
| `tag-pair-match` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 259,063,703.0 | 251,740,214.0 | 263,106,334.0 | 3,689,492.0 | 5 | 32,936 | 30,643 | 27,966 | 0.014 | compiled=5 | 2,757,815.0 | 256,213,448.0 | 114,881.0 |
| `tag-pair-match` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 257,970,998.0 | 251,636,985.0 | 261,736,977.0 | 3,369,343.9 | 5 | 32,936 | 30,756 | 28,079 | 0.013 | compiled=5 | 2,752,305.0 | 255,118,492.0 | 107,100.0 |
| `tag-pair-match` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 257,536,708.0 | 244,158,103.0 | 259,665,432.0 | 5,633,336.6 | 5 | 32,888 | 30,574 | 27,897 | 0.022 | compiled=5 | 2,625,534.0 | 254,822,005.0 | 220,431.0 |
| `tag-pair-match` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 257,608,530.0 | 254,532,503.0 | 260,491,386.0 | 1,894,544.7 | 5 | 32,888 | 30,687 | 28,010 | 0.007 | compiled=5 | 2,613,096.0 | 254,890,755.0 | 104,680.0 |
| `tag-pair-match` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 253,871,180.0 | 241,303,848.0 | 261,976,306.0 | 7,157,681.3 | 5 | 32,936 | 30,643 | 27,966 | 0.028 | compiled=5 | 2,581,305.0 | 248,027,277.0 | 99,691.0 |
| `tag-pair-match` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 255,214,878.0 | 252,465,443.0 | 263,860,267.0 | 4,016,468.3 | 5 | 32,936 | 30,756 | 28,079 | 0.016 | compiled=5 | 5,337,301.0 | 249,688,657.0 | 187,151.0 |
| `tail-digits-eol` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 178,151,232.0 | 169,147,536.0 | 188,295,467.0 | 6,423,917.1 | 5 | 28,808 | 20,619 | 17,073 | 0.036 | compiled=5 | 2,204,803.0 | 175,843,251.0 | 184,431.0 |
| `tail-digits-eol` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 174,556,504.0 | 168,802,665.0 | 177,697,941.0 | 3,794,896.4 | 5 | 28,808 | 20,703 | 17,157 | 0.022 | compiled=5 | 2,321,742.0 | 169,571,559.0 | 97,360.0 |
| `tail-digits-eol` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 178,778,540.0 | 171,444,419.0 | 180,687,650.0 | 3,383,457.2 | 5 | 28,808 | 20,619 | 17,073 | 0.019 (max is trial 1) | compiled=5 | 2,207,561.0 | 175,799,293.0 | 180,811.0 |
| `tail-digits-eol` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 175,564,541.0 | 168,721,724.0 | 186,165,444.0 | 7,353,461.7 | 5 | 28,808 | 20,703 | 17,157 | 0.042 (max is trial 1) | compiled=5 | 2,263,913.0 | 173,231,589.0 | 187,011.0 |
| `tail-digits-eol` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 180,350,301.0 | 167,010,473.0 | 184,247,673.0 | 6,004,933.0 | 5 | 28,808 | 20,619 | 17,073 | 0.033 | compiled=5 | 2,229,943.0 | 177,972,246.0 | 113,070.0 |
| `tail-digits-eol` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 173,645,222.0 | 168,242,741.0 | 185,139,329.0 | 6,117,388.3 | 5 | 28,808 | 20,703 | 17,157 | 0.035 | compiled=5 | 2,484,574.0 | 168,829,824.0 | 182,551.0 |
| `tail-dotstar-txt` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 180,405,335.0 | 173,730,630.0 | 183,233,110.0 | 3,615,416.5 | 5 | 28,896 | 23,808 | 16,855 | 0.020 | compiled=5 | 2,430,273.0 | 177,928,082.0 | 186,681.0 |
| `tail-dotstar-txt` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 172,619,014.0 | 164,746,114.0 | 182,379,205.0 | 5,949,586.1 | 5 | 28,896 | 23,343 | 16,390 | 0.034 | compiled=5 | 2,442,372.0 | 169,873,890.0 | 98,561.0 |
| `tail-dotstar-txt` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 182,856,434.0 | 173,352,751.0 | 190,515,096.0 | 5,672,228.1 | 5 | 28,896 | 23,808 | 16,855 | 0.031 | compiled=5 | 2,437,084.0 | 180,290,679.0 | 186,361.0 |
| `tail-dotstar-txt` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 170,775,533.0 | 167,880,838.0 | 173,311,418.0 | 1,764,296.7 | 5 | 28,896 | 23,343 | 16,390 | 0.010 | compiled=5 | 2,430,134.0 | 168,150,149.0 | 105,930.0 |
| `tail-dotstar-txt` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 177,180,202.0 | 165,332,635.0 | 187,147,639.0 | 7,499,789.8 | 5 | 28,896 | 23,808 | 16,855 | 0.042 | compiled=5 | 2,527,076.0 | 171,914,202.0 | 186,991.0 |
| `tail-dotstar-txt` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 161,439,751.0 | 154,364,214.0 | 173,888,421.0 | 6,574,039.6 | 5 | 28,896 | 23,343 | 16,390 | 0.041 | compiled=5 | 2,334,584.0 | 158,953,139.0 | 188,992.0 |
| `tail-ext-lower-txt` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 174,604,046.0 | 168,090,010.0 | 179,578,821.0 | 4,096,991.1 | 5 | 28,808 | 20,607 | 16,402 | 0.023 | compiled=5 | 2,340,373.0 | 172,273,003.0 | 184,661.0 |
| `tail-ext-lower-txt` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 157,997,020.0 | 154,412,688.0 | 169,615,669.0 | 6,453,591.0 | 5 | 28,808 | 20,141 | 15,936 | 0.041 | compiled=5 | 2,292,252.0 | 155,606,207.0 | 181,141.0 |
| `tail-ext-lower-txt` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 177,107,031.0 | 170,479,682.0 | 184,397,012.0 | 4,604,557.8 | 5 | 28,808 | 20,607 | 16,402 | 0.026 | compiled=5 | 2,255,223.0 | 174,750,597.0 | 101,211.0 |
| `tail-ext-lower-txt` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 166,528,572.0 | 160,534,155.0 | 167,384,495.0 | 2,485,799.7 | 5 | 28,808 | 20,141 | 15,936 | 0.015 | compiled=5 | 2,239,782.0 | 164,084,897.0 | 199,861.0 |
| `tail-ext-lower-txt` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 170,929,077.0 | 159,845,683.0 | 176,827,991.0 | 5,919,808.6 | 5 | 28,808 | 20,607 | 16,402 | 0.035 | compiled=5 | 2,222,513.0 | 166,353,581.0 | 100,341.0 |
| `tail-ext-lower-txt` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 156,355,593.0 | 152,697,502.0 | 167,018,283.0 | 5,726,254.1 | 5 | 28,808 | 20,141 | 15,936 | 0.037 | compiled=5 | 2,238,363.0 | 153,858,359.0 | 188,352.0 |
| `tail-space-eol` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 179,907,591.0 | 176,907,027.0 | 185,098,378.0 | 2,741,635.6 | 5 | 28,848 | 22,483 | 17,465 | 0.015 | compiled=5 | 2,310,052.0 | 177,451,970.0 | 104,280.0 |
| `tail-space-eol` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 177,363,789.0 | 176,167,733.0 | 183,352,688.0 | 2,819,389.3 | 5 | 28,896 | 23,631 | 17,140 | 0.016 | compiled=5 | 2,342,992.0 | 174,848,256.0 | 187,380.0 |
| `tail-space-eol` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 184,995,525.0 | 176,222,836.0 | 186,772,615.0 | 4,662,398.3 | 5 | 28,848 | 22,483 | 17,465 | 0.025 | compiled=5 | 2,262,224.0 | 180,709,731.0 | 199,351.0 |
| `tail-space-eol` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 173,712,962.0 | 163,344,883.0 | 186,065,731.0 | 7,540,836.7 | 5 | 28,896 | 23,631 | 17,140 | 0.043 | compiled=5 | 4,952,449.0 | 168,528,702.0 | 192,301.0 |
| `tail-space-eol` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 178,039,117.0 | 176,681,949.0 | 185,671,699.0 | 3,307,157.2 | 5 | 28,848 | 22,483 | 17,465 | 0.019 | compiled=5 | 2,303,642.0 | 175,511,053.0 | 179,821.0 |
| `tail-space-eol` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 170,453,843.0 | 166,077,837.0 | 178,081,036.0 | 4,326,899.9 | 5 | 28,896 | 23,631 | 17,140 | 0.025 | compiled=5 | 2,362,524.0 | 165,957,178.0 | 98,091.0 |
| `tail-word-eoz` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 173,314,607.0 | 170,174,343.0 | 185,874,572.0 | 5,508,926.8 | 5 | 28,896 | 23,624 | 17,133 | 0.032 | compiled=5 | 2,382,562.0 | 170,860,074.0 | 188,341.0 |
| `tail-word-eoz` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 176,445,014.0 | 175,015,188.0 | 177,476,171.0 | 860,741.2 | 5 | 28,896 | 23,633 | 17,142 | 0.005 | compiled=5 | 2,389,732.0 | 173,904,991.0 | 102,931.0 |
| `tail-word-eoz` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 177,243,752.0 | 169,961,530.0 | 178,020,977.0 | 3,182,799.5 | 5 | 28,896 | 23,624 | 17,133 | 0.018 | compiled=5 | 2,393,564.0 | 174,650,247.0 | 190,611.0 |
| `tail-word-eoz` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 168,342,540.0 | 162,976,301.0 | 179,340,123.0 | 5,922,346.5 | 5 | 28,896 | 23,633 | 17,142 | 0.035 | compiled=5 | 2,391,604.0 | 165,761,726.0 | 184,910.0 |
| `tail-word-eoz` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 175,853,917.0 | 168,451,083.0 | 178,052,797.0 | 3,440,732.7 | 5 | 28,896 | 23,624 | 17,133 | 0.020 | compiled=5 | 2,372,543.0 | 171,361,918.0 | 113,421.0 |
| `tail-word-eoz` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 173,549,942.0 | 168,597,403.0 | 184,684,016.0 | 5,335,078.2 | 5 | 28,896 | 23,633 | 17,142 | 0.031 | compiled=5 | 2,385,204.0 | 170,413,595.0 | 106,760.0 |
| `trim-nested-star` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 224,492,713.0 | 216,281,180.0 | 230,149,912.0 | 5,063,253.3 | 5 | 32,912 | 28,816 | 26,974 | 0.023 (max is trial 1) | compiled=5 | 4,812,045.0 | 222,049,471.0 | 187,650.0 |
| `trim-nested-star` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 223,315,137.0 | 214,377,781.0 | 232,075,153.0 | 5,995,009.5 | 5 | 32,872 | 28,745 | 26,903 | 0.027 | compiled=5 | 2,414,243.0 | 220,859,834.0 | 188,101.0 |
| `trim-nested-star` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 223,899,387.0 | 218,595,186.0 | 224,795,523.0 | 2,353,314.5 | 5 | 32,912 | 28,816 | 26,974 | 0.011 | compiled=5 | 2,359,774.0 | 221,437,695.0 | 114,221.0 |
| `trim-nested-star` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 213,273,577.0 | 210,252,688.0 | 226,168,148.0 | 6,038,651.5 | 5 | 32,872 | 28,745 | 26,903 | 0.028 | compiled=5 | 2,521,874.0 | 210,895,194.0 | 198,791.0 |
| `trim-nested-star` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 223,232,176.0 | 219,923,597.0 | 224,604,292.0 | 1,714,253.8 | 5 | 32,912 | 28,816 | 26,974 | 0.008 | compiled=5 | 2,361,393.0 | 220,745,602.0 | 100,420.0 |
| `trim-nested-star` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 229,297,140.0 | 227,990,923.0 | 237,445,775.0 | 3,365,375.4 | 5 | 32,872 | 28,745 | 26,903 | 0.015 | compiled=5 | 2,375,974.0 | 226,719,026.0 | 180,011.0 |
| `utf8-lead-no-cont` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 161,827,349.0 | 155,943,917.0 | 166,039,392.0 | 3,499,660.1 | 5 | 28,880 | 20,346 | 15,300 | 0.022 | compiled=5 | 2,291,612.0 | 159,427,206.0 | 99,620.0 |
| `utf8-lead-no-cont` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 157,617,207.0 | 155,815,048.0 | 170,702,515.0 | 5,408,336.0 | 5 | 28,864 | 20,245 | 16,502 | 0.034 | compiled=5 | 2,214,721.0 | 155,206,164.0 | 199,371.0 |
| `utf8-lead-no-cont` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 161,132,220.0 | 158,816,598.0 | 163,637,716.0 | 1,788,877.3 | 5 | 28,880 | 20,346 | 15,300 | 0.011 | compiled=5 | 2,235,983.0 | 158,799,706.0 | 98,102.0 |
| `utf8-lead-no-cont` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 168,231,009.0 | 149,985,827.0 | 171,538,680.0 | 7,770,743.4 | 5 | 28,864 | 20,245 | 16,502 | 0.046 | compiled=5 | 2,179,972.0 | 165,830,996.0 | 220,041.0 |
| `utf8-lead-no-cont` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 165,988,467.0 | 158,548,606.0 | 170,035,452.0 | 3,823,431.1 | 5 | 28,880 | 20,346 | 15,300 | 0.023 (max is trial 1) | compiled=5 | 4,150,514.0 | 161,137,490.0 | 102,730.0 |
| `utf8-lead-no-cont` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 168,011,968.0 | 157,428,710.0 | 168,539,284.0 | 4,242,804.3 | 5 | 28,864 | 20,245 | 16,502 | 0.025 | compiled=5 | 2,103,263.0 | 165,822,877.0 | 198,951.0 |
| `uuid-near-miss` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 188,329,076.0 | 176,114,083.0 | 191,826,614.0 | 5,668,183.5 | 5 | 38,192 | 24,767 | 19,363 | 0.030 | compiled=5 | 2,344,452.0 | 186,086,354.0 | 100,311.0 |
| `uuid-near-miss` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 192,967,831.0 | 187,172,891.0 | 194,301,768.0 | 2,544,530.2 | 5 | 38,152 | 24,589 | 19,185 | 0.013 | compiled=5 | 2,190,521.0 | 190,573,298.0 | 101,921.0 |
| `uuid-near-miss` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 190,619,107.0 | 183,840,639.0 | 196,124,449.0 | 5,413,528.2 | 5 | 38,192 | 24,767 | 19,363 | 0.028 (max is trial 1) | compiled=5 | 2,179,882.0 | 188,341,904.0 | 100,301.0 |
| `uuid-near-miss` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 188,294,585.0 | 183,977,620.0 | 193,244,942.0 | 3,586,018.0 | 5 | 38,152 | 24,589 | 19,185 | 0.019 | compiled=5 | 2,189,802.0 | 183,553,947.0 | 184,771.0 |
| `uuid-near-miss` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 188,159,634.0 | 185,079,408.0 | 192,359,359.0 | 2,864,007.1 | 5 | 38,192 | 24,767 | 19,363 | 0.015 | compiled=5 | 2,147,803.0 | 184,481,354.0 | 190,441.0 |
| `uuid-near-miss` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 193,050,713.0 | 186,143,182.0 | 199,619,141.0 | 4,988,638.9 | 5 | 38,152 | 24,589 | 19,185 | 0.026 | compiled=5 | 2,138,883.0 | 190,836,750.0 | 99,741.0 |
| `wild-codegrammar-json-array-begin` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 165,054,445.0 | 152,053,579.0 | 167,980,190.0 | 5,591,806.0 | 5 | 28,768 | 17,890 | 14,559 | 0.034 (max is trial 1) | compiled=5 | 4,424,794.0 | 161,084,655.0 | 106,900.0 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 167,730,939.0 | 159,123,324.0 | 172,429,272.0 | 4,516,070.1 | 5 | 28,808 | 19,476 | 15,918 | 0.027 | compiled=5 | 2,101,631.0 | 165,409,347.0 | 188,401.0 |
| `wild-codegrammar-json-array-begin` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 155,465,578.0 | 154,228,840.0 | 170,414,894.0 | 6,299,880.0 | 5 | 28,768 | 17,890 | 14,559 | 0.041 | compiled=5 | 2,140,373.0 | 151,906,977.0 | 184,391.0 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 168,054,489.0 | 163,857,385.0 | 173,168,487.0 | 3,182,210.9 | 5 | 28,808 | 19,476 | 15,918 | 0.019 | compiled=5 | 2,110,622.0 | 165,760,656.0 | 99,761.0 |
| `wild-codegrammar-json-array-begin` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 163,244,822.0 | 157,506,281.0 | 163,859,477.0 | 2,345,203.9 | 5 | 28,768 | 17,890 | 14,559 | 0.014 | compiled=5 | 2,133,842.0 | 161,010,490.0 | 188,511.0 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 165,480,366.0 | 156,710,875.0 | 166,038,759.0 | 4,097,171.7 | 5 | 28,808 | 19,476 | 15,918 | 0.025 | compiled=5 | 2,080,962.0 | 163,172,742.0 | 113,671.0 |
| `wild-codegrammar-json-constant` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 180,077,364.0 | 176,547,576.0 | 180,726,145.0 | 1,624,839.1 | 5 | 29,232 | 29,695 | 17,434 | 0.009 (max is trial 1) | compiled=5 | 2,922,025.0 | 174,661,125.0 | 189,400.0 |
| `wild-codegrammar-json-constant` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 170,876,455.0 | 166,178,841.0 | 177,439,859.0 | 4,393,482.8 | 5 | 28,976 | 25,869 | 17,960 | 0.026 | compiled=5 | 2,741,994.0 | 168,034,080.0 | 184,271.0 |
| `wild-codegrammar-json-constant` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 166,121,377.0 | 165,013,100.0 | 180,254,519.0 | 5,937,868.8 | 5 | 29,232 | 29,695 | 17,434 | 0.036 | compiled=5 | 2,877,067.0 | 163,176,601.0 | 101,590.0 |
| `wild-codegrammar-json-constant` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 176,951,060.0 | 168,186,379.0 | 180,849,921.0 | 4,795,305.2 | 5 | 28,976 | 25,869 | 17,960 | 0.027 | compiled=5 | 2,679,176.0 | 174,135,494.0 | 187,161.0 |
| `wild-codegrammar-json-constant` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 169,495,368.0 | 168,051,940.0 | 180,476,341.0 | 4,990,878.3 | 5 | 29,232 | 29,695 | 17,434 | 0.029 | compiled=5 | 2,852,046.0 | 166,442,661.0 | 169,391.0 |
| `wild-codegrammar-json-constant` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 171,183,117.0 | 169,701,570.0 | 184,711,445.0 | 5,562,008.8 | 5 | 28,976 | 25,869 | 17,960 | 0.032 | compiled=5 | 2,624,915.0 | 168,516,424.0 | 107,011.0 |
| `wild-codegrammar-json-number-extended` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 172,497,164.0 | 167,756,898.0 | 190,199,175.0 | 8,217,141.8 | 5 | 28,904 | 24,335 | 16,013 | 0.048 (max is trial 1) | compiled=5 | 2,871,845.0 | 167,961,440.0 | 209,411.0 |
| `wild-codegrammar-json-number-extended` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 169,368,577.0 | 162,942,384.0 | 174,869,916.0 | 4,001,076.1 | 5 | 28,808 | 21,799 | 16,437 | 0.024 | compiled=5 | 2,461,753.0 | 166,673,563.0 | 188,531.0 |
| `wild-codegrammar-json-number-extended` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 169,234,126.0 | 156,014,600.0 | 177,431,522.0 | 7,156,429.8 | 5 | 28,904 | 24,335 | 16,013 | 0.042 | compiled=5 | 2,601,425.0 | 165,924,097.0 | 104,811.0 |
| `wild-codegrammar-json-number-extended` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 162,200,974.0 | 155,403,189.0 | 169,336,385.0 | 5,442,108.9 | 5 | 28,808 | 21,799 | 16,437 | 0.034 | compiled=5 | 2,838,717.0 | 156,797,555.0 | 205,562.0 |
| `wild-codegrammar-json-number-extended` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 161,311,582.0 | 153,352,497.0 | 169,541,707.0 | 5,748,694.9 | 5 | 28,904 | 24,335 | 16,013 | 0.036 | compiled=5 | 2,544,014.0 | 158,595,966.0 | 192,921.0 |
| `wild-codegrammar-json-number-extended` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 159,228,331.0 | 155,882,300.0 | 171,903,313.0 | 5,822,573.5 | 5 | 28,808 | 21,799 | 16,437 | 0.037 (max is trial 1) | compiled=5 | 2,394,134.0 | 156,750,176.0 | 203,071.0 |
| `wild-codegrammar-json-object-begin` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 163,442,638.0 | 154,674,330.0 | 172,398,564.0 | 5,645,011.7 | 5 | 28,768 | 17,892 | 14,561 | 0.035 | compiled=5 | 2,485,153.0 | 161,041,034.0 | 188,601.0 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 159,313,675.0 | 154,520,832.0 | 175,234,039.0 | 7,515,770.2 | 5 | 28,808 | 19,477 | 15,919 | 0.047 | compiled=5 | 2,115,121.0 | 156,979,633.0 | 192,141.0 |
| `wild-codegrammar-json-object-begin` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 165,629,736.0 | 155,624,159.0 | 166,470,780.0 | 4,115,128.2 | 5 | 28,768 | 17,892 | 14,561 | 0.025 (max is trial 1) | compiled=5 | 2,223,033.0 | 162,629,148.0 | 188,791.0 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 166,003,736.0 | 158,255,761.0 | 168,520,432.0 | 3,679,715.1 | 5 | 28,808 | 19,477 | 15,919 | 0.022 | compiled=5 | 2,111,162.0 | 163,809,503.0 | 188,892.0 |
| `wild-codegrammar-json-object-begin` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 163,217,972.0 | 154,057,398.0 | 165,311,264.0 | 3,948,754.8 | 5 | 28,768 | 17,892 | 14,561 | 0.024 | compiled=5 | 2,218,453.0 | 160,800,508.0 | 108,161.0 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 160,589,068.0 | 157,959,313.0 | 175,603,374.0 | 6,429,713.7 | 5 | 28,808 | 19,477 | 15,919 | 0.040 | compiled=5 | 2,082,312.0 | 157,676,170.0 | 98,910.0 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 173,183,807.0 | 161,966,620.0 | 175,964,632.0 | 4,914,990.4 | 5 | 28,912 | 21,953 | 15,858 | 0.028 | compiled=5 | 2,486,262.0 | 169,798,040.0 | 99,160.0 |
| `wild-codegrammar-json-stringcontent-escape` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 164,365,723.0 | 151,137,533.0 | 164,900,605.0 | 5,283,158.5 | 5 | 28,808 | 20,745 | 16,202 | 0.032 | compiled=5 | 2,330,092.0 | 161,749,139.0 | 103,551.0 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 167,489,295.0 | 159,875,702.0 | 172,364,032.0 | 4,560,529.2 | 5 | 28,912 | 21,953 | 15,858 | 0.027 | compiled=5 | 2,466,844.0 | 163,615,063.0 | 191,941.0 |
| `wild-codegrammar-json-stringcontent-escape` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 162,524,588.0 | 158,542,714.0 | 169,110,457.0 | 3,527,138.1 | 5 | 28,808 | 20,745 | 16,202 | 0.022 | compiled=5 | 2,328,194.0 | 158,160,493.0 | 103,231.0 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 170,515,165.0 | 160,301,865.0 | 171,478,359.0 | 4,743,039.1 | 5 | 28,912 | 21,953 | 15,858 | 0.028 | compiled=5 | 2,486,094.0 | 167,910,229.0 | 109,011.0 |
| `wild-codegrammar-json-stringcontent-escape` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 165,431,146.0 | 163,546,075.0 | 174,622,618.0 | 3,928,340.0 | 5 | 28,808 | 20,745 | 16,202 | 0.024 | compiled=5 | 2,225,993.0 | 163,012,081.0 | 193,072.0 |
| `wild-datetime-datefinder-alternation` | `plain` | `pcrec_00c97769_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 571,900,274.0 | - | - |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 9,229,142,163.0 | - | - |
| `wild-datetime-datefinder-alternation` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 572,752,238.0 | - | - |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 9,282,537,925.0 | - | - |
| `wild-datetime-datefinder-alternation` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 559,335,764.0 | - | - |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 9,225,461,672.0 | - | - |
| `wild-datetime-moment-iso8601` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 378,935,833.0 | 373,849,087.0 | 379,706,147.0 | 2,139,403.5 | 5 | 55,144 | 56,915 | 46,992 | 0.006 | compiled=5 | 3,524,768.0 | 375,308,955.0 | 108,290.0 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 367,928,386.0 | 359,333,392.0 | 376,296,561.0 | 5,773,914.0 | 5 | 54,776 | 55,354 | 45,431 | 0.016 (max is trial 1) | compiled=5 | 3,498,979.0 | 364,329,537.0 | 186,780.0 |
| `wild-datetime-moment-iso8601` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 375,560,450.0 | 371,212,977.0 | 394,614,740.0 | 8,583,301.9 | 5 | 55,144 | 56,915 | 46,992 | 0.023 | compiled=5 | 7,545,142.0 | 368,223,661.0 | 190,620.0 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 366,930,404.0 | 360,105,995.0 | 376,261,977.0 | 5,969,741.4 | 5 | 54,776 | 55,354 | 45,431 | 0.016 (max is trial 1) | compiled=5 | 3,511,420.0 | 363,337,973.0 | 107,891.0 |
| `wild-datetime-moment-iso8601` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 378,065,610.0 | 377,350,265.0 | 381,966,463.0 | 1,685,126.9 | 5 | 55,144 | 56,915 | 46,992 | 0.004 | compiled=5 | 3,403,041.0 | 374,123,757.0 | 102,949.0 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 366,468,012.0 | 364,101,941.0 | 376,282,229.0 | 4,263,725.6 | 5 | 54,776 | 55,354 | 45,431 | 0.012 | compiled=5 | 3,417,920.0 | 362,945,013.0 | 104,781.0 |
| `wild-logparse-base10num-grok` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 245,903,895.0 | 240,193,655.0 | 249,584,004.0 | 3,838,653.0 | 5 | 33,160 | 35,059 | 29,273 | 0.016 | compiled=5 | 2,967,825.0 | 239,367,101.0 | 108,792.0 |
| `wild-logparse-base10num-grok` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 236,589,256.0 | 223,548,360.0 | 240,762,507.0 | 6,346,014.6 | 5 | 32,968 | 31,021 | 28,471 | 0.027 | compiled=5 | 2,717,704.0 | 233,649,941.0 | 199,351.0 |
| `wild-logparse-base10num-grok` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 240,881,805.0 | 233,759,025.0 | 257,910,601.0 | 8,231,915.8 | 5 | 33,160 | 35,059 | 29,273 | 0.034 | compiled=5 | 2,984,758.0 | 237,768,956.0 | 170,831.0 |
| `wild-logparse-base10num-grok` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 231,229,139.0 | 229,883,452.0 | 236,742,671.0 | 3,021,452.0 | 5 | 32,968 | 31,021 | 28,471 | 0.013 | compiled=5 | 2,687,295.0 | 228,413,984.0 | 110,871.0 |
| `wild-logparse-base10num-grok` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 247,535,973.0 | 244,831,819.0 | 260,733,588.0 | 5,658,318.3 | 5 | 33,160 | 35,059 | 29,273 | 0.023 | compiled=5 | 6,292,216.0 | 240,023,621.0 | 203,761.0 |
| `wild-logparse-base10num-grok` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 230,737,228.0 | 227,050,987.0 | 249,219,694.0 | 9,943,991.4 | 5 | 32,968 | 31,021 | 28,471 | 0.043 | compiled=5 | 5,611,543.0 | 226,449,464.0 | 188,841.0 |
| `wild-logparse-base10num-noatomic` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 186,912,949.0 | 184,416,223.0 | 194,702,840.0 | 3,614,776.6 | 5 | 29,064 | 24,794 | 17,668 | 0.019 | compiled=5 | 2,617,213.0 | 184,186,385.0 | 100,130.0 |
| `wild-logparse-base10num-noatomic` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 176,888,577.0 | 168,042,212.0 | 178,609,186.0 | 4,706,920.2 | 5 | 28,912 | 21,323 | 17,306 | 0.027 | compiled=5 | 2,377,023.0 | 174,403,365.0 | 99,550.0 |
| `wild-logparse-base10num-noatomic` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 179,671,014.0 | 170,708,943.0 | 189,099,960.0 | 6,305,199.7 | 5 | 29,064 | 24,794 | 17,668 | 0.035 | compiled=5 | 2,603,445.0 | 176,967,680.0 | 102,481.0 |
| `wild-logparse-base10num-noatomic` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 171,078,697.0 | 169,113,354.0 | 178,180,006.0 | 3,382,232.3 | 5 | 28,912 | 21,323 | 17,306 | 0.020 | compiled=5 | 2,362,893.0 | 168,428,401.0 | 183,331.0 |
| `wild-logparse-base10num-noatomic` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 186,885,417.0 | 179,552,365.0 | 192,057,527.0 | 3,998,009.9 | 5 | 29,064 | 24,794 | 17,668 | 0.021 (max is trial 1) | compiled=5 | 2,585,545.0 | 184,241,632.0 | 195,000.0 |
| `wild-logparse-base10num-noatomic` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 174,504,598.0 | 167,741,507.0 | 177,025,530.0 | 3,842,929.6 | 5 | 28,912 | 21,323 | 17,306 | 0.022 | compiled=5 | 2,435,314.0 | 169,057,716.0 | 187,932.0 |
| `wild-logparse-quotedstring-grok` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 413,934,865.0 | 410,798,249.0 | 415,448,723.0 | 1,608,519.3 | 5 | 41,864 | 64,131 | 43,470 | 0.004 | compiled=5 | 5,789,330.0 | 407,978,584.0 | 99,841.0 |
| `wild-logparse-quotedstring-grok` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 398,861,587.0 | 387,230,638.0 | 420,557,030.0 | 12,573,153.0 | 5 | 37,392 | 50,619 | 42,313 | 0.032 (max is trial 1) | compiled=5 | 7,417,279.0 | 391,217,068.0 | 173,201.0 |
| `wild-logparse-quotedstring-grok` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 415,737,453.0 | 412,673,866.0 | 425,226,095.0 | 4,865,984.4 | 5 | 41,864 | 64,131 | 43,470 | 0.012 | compiled=5 | 5,744,543.0 | 410,109,590.0 | 185,591.0 |
| `wild-logparse-quotedstring-grok` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 398,234,602.0 | 389,345,800.0 | 409,227,516.0 | 6,421,507.0 | 5 | 37,392 | 50,619 | 42,313 | 0.016 | compiled=5 | 7,558,603.0 | 388,547,136.0 | 188,971.0 |
| `wild-logparse-quotedstring-grok` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 407,631,858.0 | 403,664,278.0 | 423,429,529.0 | 7,219,908.7 | 5 | 41,864 | 64,131 | 43,470 | 0.018 | compiled=5 | 5,689,782.0 | 401,752,225.0 | 206,151.0 |
| `wild-logparse-quotedstring-grok` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 394,486,484.0 | 386,965,161.0 | 396,433,884.0 | 3,923,711.5 | 5 | 37,392 | 50,619 | 42,313 | 0.010 | compiled=5 | 7,288,361.0 | 380,996,856.0 | 189,132.0 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 202,457,929.0 | 199,199,631.0 | 216,246,732.0 | 6,228,615.7 | 5 | 37,704 | 44,883 | 18,819 | 0.031 (max is trial 1) | compiled=5 | 5,103,887.0 | 195,060,550.0 | 183,101.0 |
| `wild-logparse-quotedstring-noatomic` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 194,353,037.0 | 194,068,056.0 | 195,116,941.0 | 358,973.3 | 5 | 29,184 | 32,039 | 18,194 | 0.002 (max is trial 1) | compiled=5 | 6,612,405.0 | 187,544,542.0 | 104,090.0 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 205,808,894.0 | 199,990,232.0 | 211,724,869.0 | 4,173,079.0 | 5 | 37,704 | 44,883 | 18,819 | 0.020 | compiled=5 | 5,147,640.0 | 196,464,621.0 | 104,670.0 |
| `wild-logparse-quotedstring-noatomic` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 186,304,083.0 | 177,761,045.0 | 194,194,439.0 | 5,869,134.3 | 5 | 29,184 | 32,039 | 18,194 | 0.032 | compiled=5 | 6,595,436.0 | 179,510,875.0 | 186,071.0 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 207,282,885.0 | 206,536,709.0 | 216,746,408.0 | 4,238,759.8 | 5 | 37,704 | 44,883 | 18,819 | 0.020 (max is trial 1) | compiled=5 | 5,012,438.0 | 202,193,205.0 | 196,381.0 |
| `wild-logparse-quotedstring-noatomic` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 193,409,355.0 | 188,604,589.0 | 203,458,234.0 | 4,859,324.6 | 5 | 29,184 | 32,039 | 18,194 | 0.025 (max is trial 1) | compiled=5 | 6,557,208.0 | 186,580,426.0 | 106,931.0 |
| `wild-logparse-syslogbase-expanded` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 5,628,301,750.0 | 5,603,774,042.0 | 5,644,681,965.0 | 15,026,249.5 | 5 | 176,856 | 514,447 (warned) | 298,147 | 0.003 (max is trial 1) | compiled=5 | 772,356,423.0 | 4,855,679,406.0 | 185,581.0 |
| `wild-logparse-syslogbase-expanded` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 6,767,655,966.0 | 6,733,646,788.0 | 6,819,651,886.0 | 34,268,162.4 | 5 | 188,816 | 559,819 (warned) | 297,211 | 0.005 | compiled=5 | 1,926,292,784.0 | 4,852,807,041.0 | 186,361.0 |
| `wild-logparse-syslogbase-expanded` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 5,631,979,346.0 | 5,608,704,285.0 | 5,646,765,492.0 | 12,440,116.3 | 5 | 176,856 | 514,447 (warned) | 298,147 | 0.002 (max is trial 1) | compiled=5 | 777,789,539.0 | 4,853,993,556.0 | 196,251.0 |
| `wild-logparse-syslogbase-expanded` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 6,753,802,896.0 | 6,713,274,264.0 | 6,796,952,693.0 | 26,638,576.8 | 5 | 188,816 | 559,819 (warned) | 297,211 | 0.004 | compiled=5 | 1,932,151,404.0 | 4,821,431,701.0 | 100,671.0 |
| `wild-logparse-syslogbase-expanded` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 5,638,527,241.0 | 5,634,682,770.0 | 5,661,433,810.0 | 11,486,876.7 | 5 | 176,856 | 514,447 (warned) | 298,147 | 0.002 | compiled=5 | 777,267,979.0 | 4,860,368,036.0 | 117,580.0 |
| `wild-logparse-syslogbase-expanded` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 6,767,534,970.0 | 6,745,848,147.0 | 6,784,948,350.0 | 13,391,867.3 | 5 | 188,816 | 559,819 (warned) | 297,211 | 0.002 | compiled=5 | 1,929,058,610.0 | 4,836,211,958.0 | 193,401.0 |
| `wild-logparse-winpath-grok` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 262,014,280.0 | 255,553,783.0 | 268,986,325.0 | 4,262,990.8 | 5 | 33,312 | 38,775 | 30,291 | 0.016 (max is trial 1) | compiled=5 | 3,277,067.0 | 258,636,661.0 | 112,060.0 |
| `wild-logparse-winpath-grok` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 247,443,022.0 | 244,938,429.0 | 256,521,691.0 | 4,648,610.5 | 5 | 33,072 | 33,748 | 29,825 | 0.019 | compiled=5 | 2,804,546.0 | 244,359,856.0 | 193,541.0 |
| `wild-logparse-winpath-grok` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 254,530,744.0 | 253,895,879.0 | 261,996,144.0 | 3,668,514.0 | 5 | 33,312 | 38,775 | 30,291 | 0.014 | compiled=5 | 3,104,487.0 | 251,037,553.0 | 183,981.0 |
| `wild-logparse-winpath-grok` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 247,573,314.0 | 239,440,845.0 | 256,063,621.0 | 5,982,737.2 | 5 | 33,072 | 33,748 | 29,825 | 0.024 | compiled=5 | 5,901,954.0 | 242,536,064.0 | 103,360.0 |
| `wild-logparse-winpath-grok` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 256,226,735.0 | 253,342,448.0 | 270,318,794.0 | 7,071,116.9 | 5 | 33,312 | 38,775 | 30,291 | 0.028 (max is trial 1) | compiled=5 | 3,019,667.0 | 253,121,166.0 | 107,630.0 |
| `wild-logparse-winpath-grok` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 245,986,566.0 | 245,606,462.0 | 253,425,439.0 | 3,180,944.5 | 5 | 33,072 | 33,748 | 29,825 | 0.013 | compiled=5 | 2,819,187.0 | 243,134,459.0 | 98,961.0 |
| `wild-secrets-aws-access-key-id` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 255,632,447.0 | 248,896,010.0 | 257,141,874.0 | 3,229,045.5 | 5 | 32,984 | 36,859 | 29,182 | 0.013 | compiled=5 | 3,804,390.0 | 251,623,886.0 | 121,001.0 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 252,339,829.0 | 241,730,814.0 | 253,188,373.0 | 4,526,377.9 | 5 | 32,928 | 38,869 | 30,124 | 0.018 | compiled=5 | 3,647,019.0 | 243,679,433.0 | 107,861.0 |
| `wild-secrets-aws-access-key-id` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 255,705,980.0 | 248,100,875.0 | 262,391,509.0 | 5,229,250.2 | 5 | 32,984 | 36,859 | 29,182 | 0.020 | compiled=5 | 3,792,122.0 | 246,325,626.0 | 97,720.0 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 246,026,212.0 | 236,632,161.0 | 260,924,169.0 | 8,752,065.6 | 5 | 32,928 | 38,869 | 30,124 | 0.036 | compiled=5 | 3,634,090.0 | 242,206,651.0 | 192,150.0 |
| `wild-secrets-aws-access-key-id` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 256,597,577.0 | 248,585,040.0 | 269,900,910.0 | 7,632,649.2 | 5 | 32,984 | 36,859 | 29,182 | 0.030 | compiled=5 | 3,719,551.0 | 252,664,373.0 | 103,310.0 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 253,196,757.0 | 250,854,473.0 | 261,931,178.0 | 4,229,360.4 | 5 | 32,928 | 38,869 | 30,124 | 0.017 | compiled=5 | 3,563,050.0 | 249,535,645.0 | 186,792.0 |
| `wild-secrets-github-pat` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 355,038,511.0 | 346,755,688.0 | 364,851,551.0 | 6,663,385.4 | 5 | 36,992 | 41,771 | 26,913 | 0.019 | compiled=5 | 5,481,028.0 | 348,598,107.0 | 176,161.0 |
| `wild-secrets-github-pat` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 321,034,874.0 | 318,058,708.0 | 328,715,833.0 | 3,626,727.5 | 5 | 36,944 | 42,828 | 26,407 | 0.011 | compiled=5 | 4,676,914.0 | 316,158,729.0 | 193,901.0 |
| `wild-secrets-github-pat` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 354,316,152.0 | 349,233,642.0 | 363,233,935.0 | 5,635,820.0 | 5 | 36,992 | 41,771 | 26,913 | 0.016 | compiled=5 | 5,393,230.0 | 348,799,671.0 | 189,421.0 |
| `wild-secrets-github-pat` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 321,728,095.0 | 318,933,230.0 | 329,917,791.0 | 4,649,819.6 | 5 | 36,944 | 42,828 | 26,407 | 0.014 | compiled=5 | 4,667,707.0 | 316,873,278.0 | 187,721.0 |
| `wild-secrets-github-pat` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 353,208,308.0 | 344,897,501.0 | 361,527,506.0 | 5,603,831.0 | 5 | 36,992 | 41,771 | 26,913 | 0.016 | compiled=5 | 5,362,471.0 | 347,637,866.0 | 106,961.0 |
| `wild-secrets-github-pat` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 328,329,116.0 | 320,545,382.0 | 336,047,080.0 | 6,301,364.8 | 5 | 36,944 | 42,828 | 26,407 | 0.019 | compiled=5 | 4,686,657.0 | 323,456,747.0 | 185,711.0 |
| `wild-secrets-slack-webhook-url` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 303,818,815.0 | 302,270,425.0 | 318,875,203.0 | 6,400,210.7 | 5 | 53,664 | 107,610 | 36,260 | 0.021 | compiled=5 | 9,141,627.0 | 293,028,208.0 | 111,881.0 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 284,449,195.0 | 276,050,640.0 | 286,870,017.0 | 3,770,395.9 | 5 | 37,088 | 57,132 | 34,508 | 0.013 | compiled=5 | 6,586,024.0 | 277,662,289.0 | 200,882.0 |
| `wild-secrets-slack-webhook-url` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 309,632,686.0 | 301,146,358.0 | 315,708,700.0 | 4,684,291.8 | 5 | 53,664 | 107,610 | 36,260 | 0.015 (max is trial 1) | compiled=5 | 9,246,523.0 | 298,159,042.0 | 102,771.0 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 287,559,450.0 | 281,290,025.0 | 293,568,466.0 | 4,622,005.7 | 5 | 37,088 | 57,132 | 34,508 | 0.016 (max is trial 1) | compiled=5 | 6,603,639.0 | 274,680,727.0 | 107,561.0 |
| `wild-secrets-slack-webhook-url` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 300,978,589.0 | 300,046,152.0 | 310,644,705.0 | 4,599,377.6 | 5 | 53,664 | 107,610 | 36,260 | 0.015 | compiled=5 | 9,018,051.0 | 291,738,647.0 | 110,020.0 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 283,606,151.0 | 281,759,379.0 | 291,628,186.0 | 3,571,023.8 | 5 | 37,088 | 57,132 | 34,508 | 0.013 | compiled=5 | 6,532,117.0 | 275,656,965.0 | 99,760.0 |
| `wild-secrets-username-password-pair` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 583,916,476.0 | 579,571,895.0 | 597,247,296.0 | 6,750,804.3 | 5 | 209,776 | 553,708 (warned) | 44,441 | 0.012 (max is trial 1) | compiled=5 | 60,324,834.0 | 522,349,378.0 | 181,762.0 |
| `wild-secrets-username-password-pair` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 416,826,760.0 | 408,824,980.0 | 420,337,418.0 | 4,872,441.5 | 5 | 53,840 | 97,878 | 41,367 | 0.012 | compiled=5 | 43,356,524.0 | 373,236,324.0 | 97,151.0 |
| `wild-secrets-username-password-pair` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 572,839,269.0 | 563,890,787.0 | 578,157,979.0 | 5,845,392.5 | 5 | 209,776 | 553,708 (warned) | 44,441 | 0.010 (max is trial 1) | compiled=5 | 54,276,629.0 | 512,308,973.0 | 118,831.0 |
| `wild-secrets-username-password-pair` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 417,636,623.0 | 409,800,071.0 | 427,780,501.0 | 6,700,924.8 | 5 | 53,840 | 97,878 | 41,367 | 0.016 | compiled=5 | 43,327,386.0 | 374,198,576.0 | 113,241.0 |
| `wild-secrets-username-password-pair` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 567,084,420.0 | 553,004,810.0 | 576,270,084.0 | 8,509,877.3 | 5 | 209,776 | 553,708 (warned) | 44,441 | 0.015 | compiled=5 | 53,899,328.0 | 509,674,622.0 | 181,911.0 |
| `wild-secrets-username-password-pair` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 416,838,642.0 | 415,124,712.0 | 426,691,480.0 | 4,424,190.4 | 5 | 53,840 | 97,878 | 41,367 | 0.011 | compiled=5 | 43,325,659.0 | 371,934,955.0 | 195,892.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 171,426,599.0 | 160,661,883.0 | 181,574,301.0 | 7,791,564.6 | 5 | 28,912 | 22,797 | 17,090 | 0.045 | compiled=5 | 2,498,304.0 | 168,212,032.0 | 186,691.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 167,399,406.0 | 161,224,586.0 | 175,695,271.0 | 5,347,078.1 | 5 | 28,808 | 21,092 | 16,652 | 0.032 | compiled=5 | 2,397,563.0 | 164,856,324.0 | 101,279.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 173,719,251.0 | 171,187,156.0 | 179,509,042.0 | 3,304,887.0 | 5 | 28,912 | 22,797 | 17,090 | 0.019 | compiled=5 | 2,538,084.0 | 170,994,416.0 | 98,140.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 171,122,827.0 | 169,882,629.0 | 177,321,272.0 | 2,674,225.3 | 5 | 28,808 | 21,092 | 16,652 | 0.016 (max is trial 1) | compiled=5 | 2,349,793.0 | 168,589,362.0 | 112,562.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 172,704,955.0 | 171,566,962.0 | 179,551,926.0 | 2,920,182.7 | 5 | 28,912 | 22,797 | 17,090 | 0.017 | compiled=5 | 2,851,295.0 | 168,983,395.0 | 185,162.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 172,110,004.0 | 159,146,288.0 | 175,565,802.0 | 6,664,229.0 | 5 | 28,808 | 21,092 | 16,652 | 0.039 | compiled=5 | 2,274,114.0 | 169,741,160.0 | 97,561.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 173,031,448.0 | 168,746,255.0 | 177,368,508.0 | 2,814,933.0 | 5 | 28,808 | 20,279 | 16,389 | 0.016 (max is trial 1) | compiled=5 | 2,163,112.0 | 170,670,425.0 | 101,041.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 167,576,898.0 | 166,425,464.0 | 169,645,190.0 | 1,210,321.2 | 5 | 28,808 | 19,814 | 15,924 | 0.007 (max is trial 1) | compiled=5 | 2,180,071.0 | 165,004,855.0 | 191,460.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 166,138,579.0 | 165,152,142.0 | 175,210,341.0 | 4,414,675.0 | 5 | 28,808 | 20,279 | 16,389 | 0.027 | compiled=5 | 2,173,122.0 | 163,844,164.0 | 191,011.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 168,278,070.0 | 164,838,490.0 | 169,627,388.0 | 1,589,800.5 | 5 | 28,808 | 19,814 | 15,924 | 0.009 (max is trial 1) | compiled=5 | 2,158,492.0 | 165,407,624.0 | 186,221.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 173,971,033.0 | 167,725,668.0 | 175,046,780.0 | 2,720,890.9 | 5 | 28,808 | 20,279 | 16,389 | 0.016 | compiled=5 | 2,172,423.0 | 171,610,029.0 | 107,800.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 162,724,562.0 | 157,688,882.0 | 168,360,702.0 | 4,072,230.8 | 5 | 28,808 | 19,814 | 15,924 | 0.025 | compiled=5 | 2,198,572.0 | 157,962,763.0 | 109,980.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 246,402,958.0 | 233,788,911.0 | 254,629,250.0 | 6,676,548.4 | 5 | 33,088 | 33,318 | 28,484 | 0.027 | compiled=5 | 2,721,184.0 | 242,239,165.0 | 194,011.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 225,824,530.0 | 216,594,764.0 | 238,815,199.0 | 7,401,341.3 | 5 | 32,944 | 30,044 | 28,241 | 0.033 | compiled=5 | 2,504,273.0 | 223,373,387.0 | 104,601.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 244,462,676.0 | 232,693,439.0 | 247,985,215.0 | 5,420,737.9 | 5 | 33,088 | 33,318 | 28,484 | 0.022 | compiled=5 | 5,784,703.0 | 237,883,137.0 | 201,492.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 231,871,163.0 | 217,856,474.0 | 239,874,040.0 | 7,182,925.9 | 5 | 32,944 | 30,044 | 28,241 | 0.031 | compiled=5 | 2,480,924.0 | 229,183,949.0 | 104,412.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 232,406,619.0 | 230,802,848.0 | 240,118,502.0 | 3,851,221.6 | 5 | 33,088 | 33,318 | 28,484 | 0.017 | compiled=5 | 2,657,785.0 | 229,658,802.0 | 105,721.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 231,215,941.0 | 224,188,880.0 | 232,555,148.0 | 3,312,141.5 | 5 | 32,944 | 30,044 | 28,241 | 0.014 | compiled=5 | 2,448,954.0 | 228,628,836.0 | 105,700.0 |
| `wild-validator-email-owasp` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 152,263,359.0 | 149,710,327.0 | 167,719,648.0 | 6,803,366.1 | 5 | 32,832 | 16,737 | 14,380 | 0.045 | compiled=5 | 2,098,151.0 | 150,037,398.0 | 105,781.0 |
| `wild-validator-email-owasp` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 158,456,962.0 | 152,940,463.0 | 164,031,150.0 | 4,685,114.2 | 5 | 32,832 | 16,560 | 14,203 | 0.030 | compiled=5 | 2,028,150.0 | 154,131,750.0 | 198,331.0 |
| `wild-validator-email-owasp` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 163,305,381.0 | 153,124,422.0 | 164,016,636.0 | 4,783,759.6 | 5 | 32,832 | 16,737 | 14,380 | 0.029 | compiled=5 | 1,999,611.0 | 161,127,480.0 | 188,391.0 |
| `wild-validator-email-owasp` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 158,595,406.0 | 152,358,889.0 | 166,170,368.0 | 5,036,981.3 | 5 | 32,832 | 16,560 | 14,203 | 0.032 | compiled=5 | 2,019,621.0 | 156,346,902.0 | 204,051.0 |
| `wild-validator-email-owasp` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 160,790,829.0 | 147,426,832.0 | 182,285,141.0 | 11,837,449.6 | 5 | 32,832 | 16,737 | 14,380 | 0.074 | compiled=5 | 2,235,723.0 | 158,454,485.0 | 100,621.0 |
| `wild-validator-email-owasp` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 163,733,195.0 | 153,997,870.0 | 168,636,353.0 | 5,542,598.3 | 5 | 32,832 | 16,560 | 14,203 | 0.034 | compiled=5 | 1,924,220.0 | 161,623,013.0 | 193,251.0 |
| `wild-validator-ipv4-owasp` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 336,213,444.0 | 330,136,411.0 | 341,087,688.0 | 3,522,584.9 | 5 | 42,080 | 47,365 | 42,337 | 0.010 | compiled=5 | 3,183,017.0 | 332,924,936.0 | 105,491.0 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 323,573,657.0 | 322,841,133.0 | 330,821,632.0 | 3,199,763.2 | 5 | 41,872 | 46,548 | 41,520 | 0.010 | compiled=5 | 3,175,097.0 | 320,177,419.0 | 189,140.0 |
| `wild-validator-ipv4-owasp` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 335,994,417.0 | 329,455,779.0 | 340,530,982.0 | 3,643,916.9 | 5 | 42,080 | 47,365 | 42,337 | 0.011 | compiled=5 | 3,211,098.0 | 332,664,198.0 | 119,121.0 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 330,015,584.0 | 323,373,775.0 | 341,045,257.0 | 5,744,684.7 | 5 | 41,872 | 46,548 | 41,520 | 0.017 | compiled=5 | 3,158,838.0 | 326,657,564.0 | 190,331.0 |
| `wild-validator-ipv4-owasp` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 336,072,650.0 | 329,770,134.0 | 337,503,447.0 | 2,798,744.3 | 5 | 42,080 | 47,365 | 42,337 | 0.008 | compiled=5 | 3,082,598.0 | 332,906,171.0 | 188,862.0 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 329,007,128.0 | 324,006,560.0 | 342,823,590.0 | 6,620,695.4 | 5 | 41,872 | 46,548 | 41,520 | 0.020 | compiled=5 | 3,084,858.0 | 325,992,431.0 | 191,151.0 |
| `wild-validator-us-zip-owasp` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 226,391,994.0 | 217,799,109.0 | 231,272,739.0 | 4,640,053.2 | 5 | 33,184 | 29,459 | 26,915 | 0.020 | compiled=5 | 2,460,683.0 | 223,818,121.0 | 113,191.0 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 225,692,770.0 | 214,609,221.0 | 228,857,337.0 | 5,734,401.6 | 5 | 33,104 | 29,199 | 26,655 | 0.025 | compiled=5 | 2,482,923.0 | 222,651,514.0 | 207,601.0 |
| `wild-validator-us-zip-owasp` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 222,803,462.0 | 218,886,130.0 | 225,391,776.0 | 2,448,606.8 | 5 | 33,184 | 29,459 | 26,915 | 0.011 | compiled=5 | 2,404,873.0 | 218,416,566.0 | 100,321.0 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 223,546,466.0 | 214,582,525.0 | 224,128,178.0 | 3,642,848.2 | 5 | 33,104 | 29,199 | 26,655 | 0.016 | compiled=5 | 2,417,704.0 | 220,911,780.0 | 224,721.0 |
| `wild-validator-us-zip-owasp` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 227,559,572.0 | 221,019,343.0 | 240,119,460.0 | 6,381,149.7 | 5 | 33,184 | 29,459 | 26,915 | 0.028 (max is trial 1) | compiled=5 | 2,386,465.0 | 225,067,346.0 | 118,881.0 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 223,235,004.0 | 216,793,118.0 | 224,041,720.0 | 2,711,577.0 | 5 | 33,104 | 29,199 | 26,655 | 0.012 | compiled=5 | 2,371,374.0 | 220,658,950.0 | 114,460.0 |
| `wild-validator-uuid-grok` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 233,888,542.0 | 218,875,222.0 | 236,771,688.0 | 7,763,213.4 | 5 | 33,256 | 37,606 | 20,208 | 0.033 (max is trial 1) | compiled=5 | 4,172,611.0 | 224,737,625.0 | 189,861.0 |
| `wild-validator-uuid-grok` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 213,452,746.0 | 213,298,705.0 | 220,126,561.0 | 2,607,624.7 | 5 | 33,264 | 37,166 | 20,882 | 0.012 | compiled=5 | 3,690,659.0 | 209,814,577.0 | 114,460.0 |
| `wild-validator-uuid-grok` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 225,667,265.0 | 218,960,998.0 | 227,134,766.0 | 3,657,954.3 | 5 | 33,256 | 37,606 | 20,208 | 0.016 | compiled=5 | 4,161,624.0 | 215,978,092.0 | 106,160.0 |
| `wild-validator-uuid-grok` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 220,339,967.0 | 213,586,029.0 | 220,795,068.0 | 3,189,758.5 | 5 | 33,264 | 37,166 | 20,882 | 0.014 | compiled=5 | 3,664,711.0 | 216,565,366.0 | 112,302.0 |
| `wild-validator-uuid-grok` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 220,747,741.0 | 217,245,522.0 | 227,608,320.0 | 3,383,023.6 | 5 | 33,256 | 37,606 | 20,208 | 0.015 (max is trial 1) | compiled=5 | 4,122,053.0 | 216,443,617.0 | 190,832.0 |
| `wild-validator-uuid-grok` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 214,366,535.0 | 207,026,523.0 | 215,916,673.0 | 3,138,866.6 | 5 | 33,264 | 37,166 | 20,882 | 0.015 | compiled=5 | 3,667,291.0 | 210,598,783.0 | 104,100.0 |
| `wild-waf-crs-942140-dbnames` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 248,411,149.0 | 243,287,460.0 | 252,452,398.0 | 3,039,079.5 | 5 | 90,944 | 229,191 | 21,229 | 0.012 | compiled=5 | 16,053,394.0 | 232,250,583.0 | 107,171.0 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 221,906,798.0 | 211,870,288.0 | 246,515,207.0 | 11,813,452.8 | 5 | 74,216 | 170,862 | 20,619 | 0.053 | compiled=5 | 14,522,875.0 | 207,197,423.0 | 100,111.0 |
| `wild-waf-crs-942140-dbnames` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 249,114,861.0 | 241,734,420.0 | 250,272,387.0 | 3,160,475.0 | 5 | 90,944 | 229,191 | 21,229 | 0.013 | compiled=5 | 15,979,531.0 | 232,963,310.0 | 181,881.0 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 228,926,958.0 | 226,449,203.0 | 229,904,350.0 | 1,186,561.6 | 5 | 74,216 | 170,862 | 20,619 | 0.005 | compiled=5 | 14,402,832.0 | 214,364,964.0 | 181,362.0 |
| `wild-waf-crs-942140-dbnames` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 248,760,971.0 | 231,154,762.0 | 252,660,534.0 | 7,554,523.9 | 5 | 90,944 | 229,191 | 21,229 | 0.030 (max is trial 1) | compiled=5 | 15,555,399.0 | 230,485,046.0 | 192,571.0 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 228,026,693.0 | 222,397,730.0 | 229,215,920.0 | 2,398,930.7 | 5 | 74,216 | 170,862 | 20,619 | 0.011 | compiled=5 | 14,017,890.0 | 213,921,462.0 | 105,212.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 213,733,717.0 | 213,085,695.0 | 217,871,430.0 | 1,775,993.0 | 5 | 41,696 | 59,520 | 19,120 | 0.008 | compiled=5 | 5,428,649.0 | 208,161,638.0 | 187,911.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 196,260,466.0 | 194,696,239.0 | 199,295,223.0 | 1,818,590.7 | 5 | 33,176 | 40,938 | 18,469 | 0.009 | compiled=5 | 4,594,104.0 | 191,491,242.0 | 183,411.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 212,293,551.0 | 204,792,568.0 | 214,020,931.0 | 3,291,916.9 | 5 | 41,696 | 59,520 | 19,120 | 0.016 (max is trial 1) | compiled=5 | 5,420,631.0 | 206,718,770.0 | 118,970.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 193,578,743.0 | 186,861,617.0 | 194,930,542.0 | 3,397,248.1 | 5 | 33,176 | 40,938 | 18,469 | 0.018 | compiled=5 | 4,527,615.0 | 188,860,967.0 | 186,361.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 213,584,600.0 | 205,458,185.0 | 224,847,506.0 | 7,154,332.1 | 5 | 41,696 | 59,520 | 19,120 | 0.033 (max is trial 1) | compiled=5 | 5,205,421.0 | 207,466,615.0 | 199,242.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 189,275,092.0 | 188,274,765.0 | 195,972,620.0 | 2,812,633.9 | 5 | 33,176 | 40,938 | 18,469 | 0.015 | compiled=5 | 4,596,916.0 | 184,481,364.0 | 105,441.0 |
| `wild-waf-crs-942270-union-select` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 193,335,443.0 | 183,866,943.0 | 201,149,683.0 | 6,096,719.2 | 5 | 37,416 | 39,187 | 18,020 | 0.032 | compiled=5 | 4,121,581.0 | 189,059,370.0 | 188,201.0 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 178,931,478.0 | 173,416,639.0 | 180,575,925.0 | 2,769,725.9 | 5 | 28,984 | 30,901 | 16,904 | 0.015 | compiled=5 | 3,255,927.0 | 175,592,599.0 | 183,971.0 |
| `wild-waf-crs-942270-union-select` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 192,986,963.0 | 186,493,175.0 | 200,975,676.0 | 4,607,398.8 | 5 | 37,416 | 39,187 | 18,020 | 0.024 | compiled=5 | 4,146,343.0 | 188,727,598.0 | 186,371.0 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 176,314,225.0 | 165,162,172.0 | 187,060,668.0 | 7,199,807.2 | 5 | 28,984 | 30,901 | 16,904 | 0.041 | compiled=5 | 3,268,659.0 | 169,139,685.0 | 183,131.0 |
| `wild-waf-crs-942270-union-select` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 200,865,306.0 | 191,430,323.0 | 208,140,679.0 | 5,931,134.8 | 5 | 37,416 | 39,187 | 18,020 | 0.030 | compiled=5 | 3,939,642.0 | 196,713,793.0 | 99,650.0 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 180,751,023.0 | 178,956,043.0 | 193,125,614.0 | 5,195,032.7 | 5 | 28,984 | 30,901 | 16,904 | 0.029 (max is trial 1) | compiled=5 | 3,209,019.0 | 177,361,043.0 | 196,911.0 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 1,470,240,120.0 | 1,448,438,566.0 | 1,520,587,029.0 | 24,120,364.2 | 5 | 685,664 | 395,793 (warned) | 101,313 | 0.016 (max is trial 1) | compiled=5 | 16,355,975.0 | 1,453,896,525.0 | 270,782.0 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 1,398,525,890.0 | 1,385,831,892.0 | 1,428,208,241.0 | 16,425,601.2 | 5 | 665,128 | 402,999 (warned) | 103,463 | 0.012 (max is trial 1) | compiled=5 | 17,611,902.0 | 1,380,636,125.0 | 293,911.0 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,466,519,717.0 | 1,424,492,628.0 | 1,493,690,171.0 | 23,585,850.3 | 5 | 685,664 | 395,793 (warned) | 101,313 | 0.016 | compiled=5 | 16,214,502.0 | 1,449,940,653.0 | 522,682.0 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,403,066,935.0 | 1,396,610,260.0 | 1,430,662,763.0 | 11,956,335.7 | 5 | 665,128 | 402,999 (warned) | 103,463 | 0.009 | compiled=5 | 16,836,426.0 | 1,382,857,949.0 | 299,840.0 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 1,452,928,362.0 | 1,440,971,524.0 | 1,489,440,729.0 | 18,840,566.2 | 5 | 685,664 | 395,793 (warned) | 101,313 | 0.013 (max is trial 1) | compiled=5 | 15,174,828.0 | 1,437,180,071.0 | 524,173.0 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 1,403,739,559.0 | 1,395,199,632.0 | 1,452,231,178.0 | 21,325,023.8 | 5 | 665,128 | 402,999 (warned) | 103,463 | 0.015 | compiled=5 | 16,117,943.0 | 1,387,271,615.0 | 526,994.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 172,091,332.0 | 169,492,409.0 | 182,531,496.0 | 4,777,446.4 | 5 | 28,912 | 22,682 | 16,770 | 0.028 | compiled=5 | 2,666,933.0 | 167,111,106.0 | 189,971.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 167,334,057.0 | 160,055,851.0 | 168,547,262.0 | 3,400,437.4 | 5 | 28,808 | 20,350 | 15,988 | 0.020 | compiled=5 | 2,348,312.0 | 164,793,175.0 | 188,211.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 175,601,562.0 | 161,264,301.0 | 177,570,332.0 | 6,735,345.2 | 5 | 28,912 | 22,682 | 16,770 | 0.038 | compiled=5 | 2,713,456.0 | 172,764,775.0 | 109,631.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 168,876,514.0 | 160,570,935.0 | 169,932,890.0 | 3,447,912.7 | 5 | 28,808 | 20,350 | 15,988 | 0.020 | compiled=5 | 4,946,388.0 | 164,103,997.0 | 98,340.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 174,574,396.0 | 174,192,036.0 | 184,305,172.0 | 4,359,059.7 | 5 | 28,912 | 22,682 | 16,770 | 0.025 | compiled=5 | 2,622,745.0 | 171,855,421.0 | 112,911.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 167,925,509.0 | 156,908,956.0 | 182,243,662.0 | 8,052,704.2 | 5 | 28,808 | 20,350 | 15,988 | 0.048 | compiled=5 | 2,338,743.0 | 163,430,744.0 | 181,931.0 |
| `winpath-near-miss` | `plain` | `pcrec_00c97769_auto-caps-simdna` | 164,715,193.0 | 162,805,742.0 | 167,895,711.0 | 1,790,880.5 | 5 | 28,696 | 16,126 | 14,043 | 0.011 | compiled=5 | 1,998,880.0 | 161,736,328.0 | 190,061.0 |
| `winpath-near-miss` | `whole-subject` | `pcrec_00c97769_auto-caps-simdna` | 158,755,881.0 | 155,193,864.0 | 161,956,719.0 | 2,676,784.2 | 5 | 28,656 | 15,949 | 13,866 | 0.017 | compiled=5 | 1,950,680.0 | 156,700,952.0 | 188,260.0 |
| `winpath-near-miss` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 152,696,261.0 | 149,040,740.0 | 169,114,843.0 | 7,669,933.9 | 5 | 28,696 | 16,126 | 14,043 | 0.050 | compiled=5 | 1,968,001.0 | 150,511,757.0 | 187,261.0 |
| `winpath-near-miss` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 155,591,007.0 | 150,860,951.0 | 164,951,231.0 | 5,402,896.7 | 5 | 28,656 | 15,949 | 13,866 | 0.035 | compiled=5 | 1,951,381.0 | 153,447,946.0 | 185,301.0 |
| `winpath-near-miss` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 152,326,029.0 | 148,804,949.0 | 163,882,726.0 | 5,969,062.0 | 5 | 28,696 | 16,126 | 14,043 | 0.039 | compiled=5 | 1,966,732.0 | 149,915,805.0 | 190,591.0 |
| `winpath-near-miss` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 156,982,976.0 | 141,956,782.0 | 160,157,034.0 | 6,882,286.3 | 5 | 28,656 | 15,949 | 13,866 | 0.044 | compiled=5 | 1,925,170.0 | 154,812,654.0 | 104,771.0 |

