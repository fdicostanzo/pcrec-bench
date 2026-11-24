# pcrec-bench report

reporter: v28 (2026-10-25)

## Query

- filters: subbench=capability, version=0.4, machine=ryzen7700x, since=2026-11-01T00:00:00Z, until=2026-11-25T00:00:00Z, testee=pcrec_cb32eda28_auto-caps-simdna, testee=pcrec_d6c5e71a5_auto-caps-simdna
- record source: store/index.tsv (2 record(s) matching this query)
- records included: 2
- worst other-core busy: 47.06% (`pcrec_cb32eda28_auto-caps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `large-subject-throughput`)
    - `capability@0.4__pcrec_cb32eda28_auto-caps-simdna__ryzen7700x__20261101T133920Z` (store/records/capability@0.4/pcrec_cb32eda28_auto-caps-simdna/capability@0.4__pcrec_cb32eda28_auto-caps-simdna__ryzen7700x__20261101T133920Z.jsonl) — agreement: agree (0 of 138 groups; 10 of 6481 rows; 5 unjudged; k=1.5, 2/3; 5 trials); after: occ 10.10%
    - `capability@0.4__pcrec_d6c5e71a5_auto-caps-simdna__ryzen7700x__20261124T090806Z` (store/records/capability@0.4/pcrec_d6c5e71a5_auto-caps-simdna/capability@0.4__pcrec_d6c5e71a5_auto-caps-simdna__ryzen7700x__20261124T090806Z.jsonl) — agreement: agree (0 of 140 groups; 14 of 6575 rows; 5 unjudged; k=1.5, 2/3; 5 trials); after: occ 16.94%
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

## Null-control band (D119 bar; [B79], inbox I-93 block B / I-104)

- D119 bar (inbox I-93 block B / I-104): a cross-pin cell moved iff |Δ%| > max(IQR%, null band) -- Δ% = (after - before) / before; IQR% = the BEFORE side's Type-7 IQR of its per-trial set sums over the before median; null band = the largest |Δ%| any PROGRAM-IDENTICAL cell of the same (regime, baseline scale) stratum reached across the same pin pair (symmetric); a stratum with fewer than 10 program-identical cells has NO usable band and its verdicts say `IQR only` by name.
- baseline scale: the BEFORE (older pin) set-grain median -- `>=1us` / `100ns-1us` / `<100ns`; strata are per REGIME (I-104).
- sufficiency: a stratum needs >= 10 program-identical cells -- the band is a sample maximum, and one more null cell exceeds the maximum of n with chance 1/(n+1) (<= 9.1% at n = 10).
- identity: the records' own `engine_metadata.program_sha256` ([B88], schema v1.7) where BOTH compile rows of a cell carry it; otherwise OUR OWN census (`tools/program_identity.py`: both pins re-emitted with the pinned binaries under each config's recorded flags, `.c` + `.h` compared after dropping ONLY the generated-by line, the `.abi` integer and one-sided `#define` stamps). Which records carry the field, per side: `pcrec cb32eda28 -> d6c5e71a5`: the BEFORE (`cb32eda28`) records carry `program_sha256` (138 of 138 compiled cell(s)), the AFTER (`d6c5e71a5`) records carry `program_sha256` (140 of 140 compiled cell(s)).

### `pcrec cb32eda28 -> d6c5e71a5` (capability@0.4)

- identity from the records ([B88], schema v1.7): 135 cell(s) read `engine_metadata.program_sha256` on BOTH compile rows, 0 fell back to the census, criterion v3 (`program_sha256_v3`) on 135 cell(s), v2 (`program_sha256`) on 0; no census for this pair
- cells: 135 cross-pin set cell(s) measured on both sides; 66 program-identical (the null population)

| regime | baseline scale | n null cells | min Δ% | median Δ% | max Δ% | band (±) | status |
|---|---|---|---|---|---|---|---|
| `large-subject-throughput` | `>=1us` | 25 | -1.78% | +0.07% | +12.76% | ±12.76% | ok |
| `large-subject-throughput` | `100ns-1us` | 2 | -0.15% | +0.94% | +2.04% | n/a | insufficient (n=2 < 10) |
| `large-subject-throughput` | `<100ns` | 6 | -1.10% | -0.84% | +0.69% | n/a | insufficient (n=6 < 10) |
| `short-subject-search` | `>=1us` | 3 | -0.28% | +0.12% | +0.47% | n/a | insufficient (n=3 < 10) |
| `short-subject-search` | `100ns-1us` | 30 | -4.82% | +0.54% | +8.81% | ±8.81% | ok |
| `short-subject-search` | `<100ns` | 0 | - | - | - | n/a | empty (n=0) |

- dropped expectation triples: 2 triples, 20 rows (by name: email-nested-plus x t-evil-match-60k, email-nested-plus x t-evil-nearmiss-16k) -- no expectation could be derived for them, so their cells are not judged (per-row `no-expectation`); counted from the included records' own rows

## Ranking (per pattern x regime, SET grain: sum over the subject set; best median first)

_D119 bar in this view: |Δ%| > max(IQR%, null band), the `D119 bar` column (definition, strata and bands in the null-control section above). This view's own threshold population: 135 cross-pin cell(s): 22 improve, 3 regress, 44 within the bar, 66 null-control (program identical -- the band's own population); 6 of the verdicts are IQR-only (their stratum's band is not usable)._

### `balanced-parens-rec` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 606,924.5 | 0.0994 | 602,812.3 | 616,713.9 | 4,784.3 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 612,598.5 | 0.1004 | 606,361.3 | 635,038.9 | 9,941.5 | 1.009x | 1.009x | unchanged (within spread) | +0.93% vs bar 12.76% (band) → **within** |

#### `balanced-parens-rec` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 439,749.4 | 0.4194 |
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 444,610.1 | 0.4240 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 90,607.8 | 0.3456 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 91,615.0 | 0.3495 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 21,114.8 | 0.3222 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 21,174.2 | 0.3231 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 380.9 | 0.0062 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 381.3 | 0.0062 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 77.2 | 0.0047 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 77.7 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 77.4 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 77.6 | 0.0047 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 22.5 | 0.0055 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 22.4 | 0.0055 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 197.2 | 0.1926 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 198.1 | 0.1934 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 19,221.9 | 0.2933 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 19,414.2 | 0.2962 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 2,212.0 | 0.2700 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2,219.6 | 0.2709 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 77.5 | 0.0047 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 77.4 | 0.0047 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 22.1 | 0.0054 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 22.3 | 0.0054 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7,624.1 | 0.0073 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,568.3 | 0.0072 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,596.3 | 0.0061 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,596.6 | 0.0061 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,529.7 | 0.0072 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,549.9 | 0.0072 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,958.6 | 0.0076 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,950.0 | 0.0076 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,598.5 | 0.0072 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,662.3 | 0.0073 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 380.6 | 0.0062 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 383.2 | 0.0062 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 78.2 | 0.0048 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 77.9 | 0.0048 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 444,610.1 ns, 1,048,576 B

### `balanced-parens-rec` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 451.4 | 447.7 | 474.7 | 9.8 | 1.000x | 1.000x | unchanged (within spread) | -3.46% vs bar 8.81% (band) → **within** | 75 | 6.0 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 467.6 | 466.4 | 472.8 | 2.3 | 1.036x | 1.036x | - | - | 75 | 6.2 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `waf-concat`, 42.1 ns, 48 B; largest Δ: `floor-hit`, -1.1 ns (now 4.2 ns), 1 B

### `base10num-near-miss` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 2,406.1 | 0.0004 | 2,401.4 | 2,448.0 | 21.5 | 1.000x | 1.000x | **dominated**: `t-hyb-digits-4k` is 97.6% of this set | unchanged (within spread) | -0.93% (null control: program identical) |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 2,428.8 | 0.0004 | 2,402.9 | 2,436.5 | 12.1 | 1.009x | 1.009x | **dominated**: `t-hyb-digits-4k` is 97.7% of this set | - | - |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `base10num-near-miss` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.9 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.9 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0000 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.9 | 0.0000 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0000 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.8 | 0.0002 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0002 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 8.4 | 0.0005 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 7.6 | 0.0005 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2,349.6 | 0.5736 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 2,372.8 | 0.5793 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.9 | 0.0028 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0028 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.9 | 0.0000 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0000 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.9 | 0.0003 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0003 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.9 | 0.0002 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0002 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.9 | 0.0007 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0007 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.6 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.6 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.9 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.9 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.9 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.9 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0000 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.9 | 0.0002 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0002 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `t-hyb-digits-4k`, 2,349.6 ns, 4,096 B

### `base10num-near-miss` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 309.4 | 292.1 | 342.7 | 18.9 | 1.000x | 1.000x | - | - | 75 | 4.1 | 3.8 | 100% |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 336.7 | 316.9 | 350.6 | 11.8 | 1.088x | 1.088x | unchanged (within spread) | +8.81% (null control: program identical) | 75 | 4.5 | 3.7 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `rd-numeric-id-near-miss`, 16.3 ns, 20 B; largest Δ: `cg-number`, +1.0 ns (now 10.3 ns), 10 B

### `bracket-array-define` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 221.3 | 0.0000 | 221.0 | 222.1 | 0.4 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 223.1 | 0.0000 | 222.4 | 231.8 | 4.2 | 1.008x | 1.008x | unchanged (within spread) | +0.81% vs bar 0.33% (IQR-only) → **regress (IQR only: band n=2 < 10)** |

#### `bracket-array-define` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 11.7 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 11.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 11.6 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 11.8 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 11.7 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 11.9 | 0.0002 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 11.6 | 0.0002 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 11.7 | 0.0002 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 11.6 | 0.0007 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 11.8 | 0.0007 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 11.7 | 0.0007 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 11.7 | 0.0007 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 11.6 | 0.0028 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 11.8 | 0.0029 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 11.6 | 0.0114 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 11.8 | 0.0115 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 11.7 | 0.0002 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 11.8 | 0.0002 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 11.7 | 0.0014 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 11.8 | 0.0014 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 11.6 | 0.0007 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 11.7 | 0.0007 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 11.7 | 0.0029 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 11.8 | 0.0029 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 11.7 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 11.7 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 11.7 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 11.8 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 11.6 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 11.7 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 11.7 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 11.7 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 11.7 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 11.8 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 11.7 | 0.0002 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 11.8 | 0.0002 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 11.6 | 0.0007 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 11.8 | 0.0007 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `t-64k`, 11.9 ns, 65,536 B; largest Δ: `t-mixed-runs-4k`, +0.2 ns (now 11.8 ns), 4,096 B

### `bracket-array-define` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 869.2 | 829.9 | 873.8 | 17.8 | 1.000x | 1.000x | unchanged (within spread) | -3.29% vs bar 8.81% (band) → **within** | 75 | 11.6 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 898.8 | 856.9 | 904.4 | 21.8 | 1.034x | 1.034x | - | - | 75 | 12.0 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `rec-array-define`, 41.7 ns, 11 B; largest Δ: `cg-array-begin`, -8.2 ns (now 3.5 ns), 1 B

### `codegrammar-flat` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 376,024.9 | 0.0616 | 369,723.2 | 385,557.6 | 5,147.7 | 1.000x | 1.000x | unchanged (within spread) | -0.89% vs bar 12.76% (band) → **within** |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 379,399.5 | 0.0622 | 369,380.7 | 397,832.6 | 9,889.6 | 1.009x | 1.009x | - | - |

#### `codegrammar-flat` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 246,796.5 | 0.2354 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 252,144.9 | 0.2405 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 60,062.6 | 0.2291 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 59,280.4 | 0.2261 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 15,010.0 | 0.2290 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 14,921.8 | 0.2277 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 376.0 | 0.0061 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 374.2 | 0.0061 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.5 | 0.0047 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 77.0 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.5 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 76.4 | 0.0047 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 21.7 | 0.0053 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 22.2 | 0.0054 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 265.6 | 0.2594 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 245.4 | 0.2397 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 18,107.2 | 0.2763 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 17,809.6 | 0.2718 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2,467.5 | 0.3012 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 2,494.1 | 0.3044 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 77.4 | 0.0047 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 77.3 | 0.0047 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 21.5 | 0.0053 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 22.1 | 0.0054 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,796.2 | 0.0074 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7,563.8 | 0.0072 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,592.9 | 0.0061 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,586.3 | 0.0061 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,593.9 | 0.0072 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,522.5 | 0.0072 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,563.9 | 0.0072 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,594.1 | 0.0072 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,572.4 | 0.0072 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,627.4 | 0.0073 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 375.5 | 0.0061 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 375.7 | 0.0061 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.6 | 0.0047 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.9 | 0.0047 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 246,796.5 ns, 1,048,576 B

### `codegrammar-flat` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 410.9 | 410.3 | 415.8 | 2.1 | 1.000x | 1.000x | faster ×1.04 | -4.24% vs bar 8.81% (band) → **within** | 75 | 5.5 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 429.1 | 427.9 | 438.3 | 4.4 | 1.044x | 1.044x | - | - | 75 | 5.7 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `cg-key-colon`, 20.9 ns, 7 B; largest Δ: `cg-array-begin`, -2.7 ns (now 2.5 ns), 1 B

### `codegrammar-xflag` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 377,666.3 | 0.0619 | 369,965.1 | 383,442.4 | 4,496.0 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 380,120.0 | 0.0623 | 376,199.6 | 395,510.0 | 7,031.1 | 1.006x | 1.006x | unchanged (within spread) | +0.65% vs bar 12.76% (band) → **within** |

#### `codegrammar-xflag` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 248,218.6 | 0.2367 |
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 249,894.3 | 0.2383 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 60,463.9 | 0.2307 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 61,250.1 | 0.2337 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 15,152.9 | 0.2312 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 15,005.8 | 0.2290 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 371.9 | 0.0061 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 375.1 | 0.0061 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.9 | 0.0047 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.6 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 76.6 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.6 | 0.0047 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.8 | 0.0053 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 21.7 | 0.0053 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 249.9 | 0.2440 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 246.6 | 0.2408 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 17,855.5 | 0.2725 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 17,944.9 | 0.2738 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 2,482.0 | 0.3030 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2,541.6 | 0.3103 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 77.8 | 0.0047 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 77.3 | 0.0047 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.9 | 0.0053 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 21.5 | 0.0053 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7,507.1 | 0.0072 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,663.2 | 0.0073 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,591.1 | 0.0061 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,585.7 | 0.0061 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,621.4 | 0.0073 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,509.3 | 0.0072 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,621.4 | 0.0073 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,610.4 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,588.6 | 0.0072 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,673.0 | 0.0073 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 374.9 | 0.0061 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 376.0 | 0.0061 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.6 | 0.0047 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.6 | 0.0047 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 249,894.3 ns, 1,048,576 B

### `codegrammar-xflag` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 422.0 | 413.7 | 423.2 | 3.5 | 1.000x | 1.000x | faster ×1.02 | -1.95% vs bar 8.81% (band) → **within** | 75 | 5.6 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 430.4 | 429.5 | 438.0 | 3.2 | 1.020x | 1.020x | - | - | 75 | 5.7 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `cg-key-colon`, 21.1 ns, 7 B; largest Δ: `floor-hit`, -2.5 ns (now 2.7 ns), 1 B

### `currency-lookbehind-fixed` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 43,287.9 | 0.0071 | 43,121.9 | 43,340.6 | 92.3 | 1.000x | 1.000x | unchanged (within spread) | -0.30% (null control: program identical) |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 43,420.2 | 0.0071 | 43,229.3 | 43,445.2 | 86.4 | 1.003x | 1.003x | - | - |

#### `currency-lookbehind-fixed` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,610.0 | 0.0073 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 7,592.9 | 0.0072 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,571.1 | 0.0060 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 1,580.9 | 0.0060 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 402.6 | 0.0061 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 402.6 | 0.0061 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 376.9 | 0.0061 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 378.4 | 0.0062 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.8 | 0.0047 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 77.0 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 77.6 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 77.3 | 0.0047 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 21.6 | 0.0053 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.6 | 0.0053 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 8.9 | 0.0087 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 8.7 | 0.0085 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 403.1 | 0.0062 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 402.4 | 0.0061 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 40.5 | 0.0049 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 40.5 | 0.0049 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 77.4 | 0.0047 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 77.4 | 0.0047 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 21.9 | 0.0053 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.7 | 0.0053 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,606.8 | 0.0073 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7,896.7 | 0.0075 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,585.1 | 0.0060 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,582.0 | 0.0060 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,657.6 | 0.0073 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,583.8 | 0.0072 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,608.2 | 0.0073 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,613.3 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,602.7 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,512.3 | 0.0072 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 377.1 | 0.0061 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 377.8 | 0.0061 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.9 | 0.0047 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 77.0 | 0.0047 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `t-tail-digits-1m`, 7,657.6 ns, 1,048,522 B; largest Δ: `t-qs-1m`, -290.0 ns (now 7,606.8 ns), 1,048,501 B

### `currency-lookbehind-fixed` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 364.6 | 362.3 | 377.4 | 5.6 | 1.000x | 1.000x | unchanged (within spread) | -0.83% (null control: program identical) | 75 | 4.9 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 367.7 | 361.0 | 368.6 | 3.1 | 1.008x | 1.008x | - | - | 75 | 4.9 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `la-currency`, 18.8 ns, 10 B

### `date-nested-plus` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 426.2 | 423.1 | 431.7 | 2.8 | 1.000x | 1.000x | faster ×1.04 | -4.06% vs bar 8.81% (band) → **within** | 75 | 5.7 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 444.3 | 441.9 | 450.1 | 3.1 | 1.042x | 1.042x | - | - | 75 | 5.9 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `rd-numeric-id-near-miss`, 13.5 ns, 20 B; largest Δ: `floor-hit`, -1.0 ns (now 4.4 ns), 1 B

### `doubled-word` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 15,791,769.3 | 2.5872 | 15,671,956.3 | 16,104,921.6 | 158,605.1 | 1.000x | 1.000x | unchanged (within spread) | -1.67% vs bar 12.76% (band) → **within** |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 16,059,409.3 | 2.6311 | 15,959,174.8 | 16,139,608.0 | 67,180.6 | 1.017x | 1.017x | - | - |

#### `doubled-word` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2,694,819.3 | 2.5700 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 2,731,054.4 | 2.6045 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 664,918.4 | 2.5365 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 680,336.3 | 2.5953 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 157,141.8 | 2.3978 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 159,861.7 | 2.4393 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 95,524.7 | 1.5548 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 94,509.8 | 1.5382 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 25,341.7 | 1.5466 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 25,013.6 | 1.5266 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 34,655.6 | 2.1152 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 34,749.6 | 2.1210 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6,284.5 | 1.5343 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 6,270.6 | 1.5309 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,852.1 | 1.8087 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 1,861.5 | 1.8179 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 142,568.7 | 2.1754 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 143,348.4 | 2.1873 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 15,132.9 | 1.8473 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 15,355.7 | 1.8745 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 33,860.0 | 2.0667 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 34,751.9 | 2.1211 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,591.4 | 1.8534 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 7,503.1 | 1.8318 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2,633,085.7 | 2.5113 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 2,680,991.6 | 2.5570 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 654,292.4 | 2.4964 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 664,587.6 | 2.5357 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2,875,681.0 | 2.7426 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 2,924,096.2 | 2.7888 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2,856,136.5 | 2.7240 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 2,924,987.5 | 2.7896 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2,867,308.8 | 2.7346 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 2,929,665.7 | 2.7941 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 11,846.7 | 0.1928 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 11,780.5 | 0.1917 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,206.9 | 0.1957 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3,161.6 | 0.1930 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `t-tail-digits-1m`, 2,875,681.0 ns, 1,048,522 B; largest Δ: `t-tail-space-1m`, -68,851.0 ns (now 2,856,136.5 ns), 1,048,522 B

### `doubled-word` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 2,516.3 | 2,477.8 | 2,522.6 | 17.0 | 1.000x | 1.000x | faster ×1.03 | -3.10% vs bar 0.80% (IQR-only) → **improve (IQR only: band n=3 < 10)** | 75 | 33.6 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 2,596.9 | 2,562.1 | 2,621.7 | 20.1 | 1.032x | 1.032x | - | - | 75 | 34.6 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `sec-github-pat`, 145.6 ns, 93 B; largest Δ: `sd-empty-alt-miss`, -11.7 ns (now 94.0 ns), 60 B

### `dup-param-detect` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 528.4 | 521.0 | 534.0 | 4.8 | 1.000x | 1.000x | faster ×1.06 | -5.70% vs bar 8.81% (band) → **within** | 75 | 7.0 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 560.4 | 557.3 | 567.7 | 4.2 | 1.060x | 1.060x | - | - | 75 | 7.5 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `waf-benign`, 148.2 ns, 39 B

### `email-local-nodup` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 47,005.6 | 0.0077 | 46,990.9 | 47,038.6 | 20.6 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 47,386.5 | 0.0078 | 46,891.8 | 47,722.8 | 307.9 | 1.008x | 1.008x | unchanged (within spread) | +0.81% (null control: program identical) |

#### `email-local-nodup` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 11.6 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 15.5 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 10.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 11.6 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 13.5 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 14.0 | 0.0002 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 35,058.8 | 0.5706 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 35,232.5 | 0.5734 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 9,419.3 | 0.5749 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 9,450.6 | 0.5768 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 9.3 | 0.0006 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 9.2 | 0.0006 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 2,354.5 | 0.5748 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2,368.9 | 0.5783 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 13.3 | 0.0130 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 13.3 | 0.0130 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 13.3 | 0.0002 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 13.2 | 0.0002 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 13.3 | 0.0016 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 13.2 | 0.0016 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 11.6 | 0.0007 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 11.5 | 0.0007 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 6.4 | 0.0016 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.4 | 0.0016 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 8.7 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 8.6 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 10.9 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 10.9 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 10.4 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 10.4 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 10.4 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 10.4 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 10.4 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 10.3 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 6.5 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.4 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 6.4 | 0.0004 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.4 | 0.0004 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `t-evil-match-60k`, 35,232.5 ns, 61,440 B

### `email-local-nodup` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 806.9 | 782.6 | 813.1 | 11.5 | 1.000x | 1.000x | - | - | 75 | 10.8 | 3.8 | 100% |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 812.8 | 778.6 | 820.3 | 14.9 | 1.007x | 1.007x | unchanged (within spread) | +0.72% (null control: program identical) | 75 | 10.8 | 3.7 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `sd-empty-alt-hit`, 41.3 ns, 61 B; largest Δ: `v-email`, -1.2 ns (now 19.9 ns), 24 B

### `email-nested-plus` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 715.1 | 712.5 | 723.9 | 4.2 | 1.000x | 1.000x | - | - | 75 | 9.5 | 3.8 | 100% |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 734.1 | 725.5 | 750.7 | 9.4 | 1.027x | 1.027x | slower ×1.03 | +2.66% vs bar 8.81% (band) → **within** | 75 | 9.8 | 3.7 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `sec-github-pat`, 41.9 ns, 93 B; largest Δ: `floor-hit`, -2.1 ns (now 4.1 ns), 1 B

### `evil-alt-nested` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 49,674.8 | 0.0081 | 41,513.7 | 55,843.1 | 4,659.1 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 56,014.7 | 0.0092 | 46,334.6 | 56,201.3 | 3,892.5 | 1.128x | 1.128x | unchanged (within spread) | +12.76% (null control: program identical) |

#### `evil-alt-nested` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 7.9 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.2 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 14.7 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 14.7 | 0.0002 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 43,279.3 | 0.7044 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 46,608.9 | 0.7586 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 6,357.5 | 0.3880 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 9,248.9 | 0.5645 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0004 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.1 | 0.0004 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0015 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.1 | 0.0015 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 9.0 | 0.0087 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 8.9 | 0.0087 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 8.9 | 0.0001 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 8.9 | 0.0001 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 8.9 | 0.0011 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 9.0 | 0.0011 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 8.4 | 0.0005 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 8.3 | 0.0005 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0015 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.1 | 0.0015 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7.8 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7.8 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 10.1 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 10.1 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.1 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.1 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.1 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.0 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0004 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.2 | 0.0004 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `t-evil-match-60k`, 46,608.9 ns, 61,440 B

### `evil-alt-nested` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 650.1 | 648.6 | 750.6 | 39.7 | 1.000x | 1.000x | - | - | 75 | 8.7 | 3.8 | 100% |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 653.3 | 652.6 | 757.2 | 49.5 | 1.005x | 1.005x | unchanged (within spread) | +0.49% (null control: program identical) | 75 | 8.7 | 3.7 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `sd-empty-alt-miss`, 58.5 ns, 60 B; largest Δ: `rd-email-near-miss`, +1.3 ns (now 28.8 ns), 20 B

### `file-ext-order` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 319,243.1 | 0.0523 | 317,717.0 | 321,818.6 | 1,471.6 | 1.000x | 1.000x | unchanged (within spread) | -0.13% (null control: program identical) |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 319,667.2 | 0.0524 | 316,300.6 | 320,064.4 | 1,388.5 | 1.001x | 1.001x | - | - |

#### `file-ext-order` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 60,471.9 | 0.0577 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 59,787.8 | 0.0570 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 15,055.9 | 0.0574 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 14,866.9 | 0.0567 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,734.7 | 0.0570 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 3,682.3 | 0.0562 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 376.8 | 0.0061 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 374.0 | 0.0061 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.2 | 0.0047 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 75.6 | 0.0046 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 75.8 | 0.0046 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 75.8 | 0.0046 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 21.0 | 0.0051 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.0 | 0.0051 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 48.3 | 0.0471 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 49.0 | 0.0478 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,130.6 | 0.0478 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 3,127.4 | 0.0477 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 379.7 | 0.0463 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 379.0 | 0.0463 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 77.7 | 0.0047 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 77.4 | 0.0047 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 261.0 | 0.0637 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 259.4 | 0.0633 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 23,345.1 | 0.0223 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 23,187.9 | 0.0221 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5,587.2 | 0.0213 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 5,517.4 | 0.0211 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 68,783.3 | 0.0656 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 68,655.4 | 0.0655 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 69,172.8 | 0.0660 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 69,315.1 | 0.0661 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 69,174.1 | 0.0660 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 69,477.1 | 0.0663 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 379.1 | 0.0062 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 377.0 | 0.0061 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.4 | 0.0047 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 75.9 | 0.0046 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `t-tail-txt-1m`, 69,174.1 ns, 1,048,527 B; largest Δ: `t-1m`, +684.2 ns (now 60,471.9 ns), 1,048,576 B

### `file-ext-order` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 295.0 | 293.8 | 298.3 | 1.8 | 1.000x | 1.000x | - | - | 75 | 3.9 | 3.8 | 100% |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 298.7 | 286.5 | 311.2 | 7.9 | 1.012x | 1.012x | unchanged (within spread) | +1.24% (null control: program identical) | 75 | 4.0 | 3.7 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `sec-slack-webhook`, 6.9 ns, 81 B; largest Δ: `waf-dbnames`, +0.5 ns (now 6.2 ns), 39 B

### `float-literal-bound` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 575,459.3 | 0.0943 | 565,632.7 | 587,523.1 | 7,398.1 | 1.000x | 1.000x | faster ×6.97 | -85.66% vs bar 12.76% (band) → **improve** |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 4,012,602.8 | 0.6574 | 4,004,709.1 | 4,049,583.6 | 16,232.9 | 6.973x | 6.973x | - | - |

#### `float-literal-bound` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 150,356.9 | 0.1434 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 646,237.8 | 0.6163 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 27,437.5 | 0.1047 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 153,462.6 | 0.5854 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6,654.0 | 0.1015 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 24,095.5 | 0.3677 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 380.3 | 0.0062 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 376.3 | 0.0061 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 75.7 | 0.0046 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 75.7 | 0.0046 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.3 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 75.6 | 0.0046 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 21.0 | 0.0051 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 20.9 | 0.0051 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 73.8 | 0.0720 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 321.5 | 0.3140 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5,370.0 | 0.0819 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 26,038.5 | 0.3973 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 636.9 | 0.0777 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 3,112.5 | 0.3799 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 79.9 | 0.0049 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3,154.0 | 0.1925 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,074.9 | 0.2624 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 2,941.9 | 0.7182 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 24,744.9 | 0.0236 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 1,560,134.2 | 1.4880 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5,942.9 | 0.0227 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 374,130.4 | 1.4275 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 119,833.3 | 0.1143 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 411,550.2 | 0.3925 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 118,481.6 | 0.1130 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 406,472.5 | 0.3877 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 115,981.8 | 0.1106 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 407,086.3 | 0.3882 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 378.0 | 0.0062 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 375.0 | 0.0061 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 75.9 | 0.0046 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 75.3 | 0.0046 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `t-1m`, 150,356.9 ns, 1,048,576 B; largest Δ: `t-qs-1m`, -1,535,389.4 ns (now 24,744.9 ns), 1,048,501 B

### `float-literal-bound` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 434.0 | 433.1 | 438.9 | 2.2 | 1.000x | 1.000x | - | - | 75 | 5.8 | 3.8 | 100% |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 448.7 | 443.3 | 453.5 | 3.7 | 1.034x | 1.034x | slower ×1.03 | +3.38% vs bar 8.81% (band) → **within** | 75 | 6.0 | 3.7 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `v-ipv4`, 28.2 ns, 11 B; largest Δ: `sec-slack-webhook`, -25.4 ns (now 9.1 ns), 81 B

### `floor-byte` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 43,694.1 | 0.0072 | 43,429.3 | 44,699.4 | 499.8 | 1.000x | 1.000x | unchanged (within spread) | -0.83% (null control: program identical) |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 44,061.9 | 0.0072 | 43,028.4 | 44,155.9 | 521.4 | 1.008x | 1.008x | - | - |

#### `floor-byte` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,875.7 | 0.0075 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 7,653.8 | 0.0073 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,581.4 | 0.0060 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 1,577.8 | 0.0060 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 400.6 | 0.0061 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 399.7 | 0.0061 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 375.4 | 0.0061 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 374.5 | 0.0061 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 77.0 | 0.0047 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.8 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.4 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 76.0 | 0.0046 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 21.8 | 0.0053 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.5 | 0.0053 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7.3 | 0.0072 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 7.4 | 0.0072 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 400.3 | 0.0061 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 400.3 | 0.0061 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 39.3 | 0.0048 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 39.2 | 0.0048 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.3 | 0.0047 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 76.2 | 0.0047 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 20.4 | 0.0050 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 20.4 | 0.0050 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,856.8 | 0.0075 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7,800.3 | 0.0074 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,583.7 | 0.0060 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,583.1 | 0.0060 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,700.9 | 0.0073 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,610.3 | 0.0073 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,666.5 | 0.0073 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,766.5 | 0.0074 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,602.8 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,755.5 | 0.0074 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 375.1 | 0.0061 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 374.2 | 0.0061 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.6 | 0.0047 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.2 | 0.0047 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 7,875.7 ns, 1,048,576 B

### `floor-byte` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 275.3 | 274.8 | 300.9 | 10.3 | 1.000x | 1.000x | unchanged (within spread) | -2.28% (null control: program identical) | 75 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 281.8 | 275.1 | 294.0 | 7.5 | 1.023x | 1.023x | - | - | 75 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `floor-hit`, 5.7 ns, 1 B; largest Δ: `sd-empty-alt-hit`, -0.2 ns (now 3.8 ns), 61 B

### `hex8-bounded` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 4,588,136.5 | 0.7517 | 4,550,420.1 | 4,612,736.3 | 22,885.8 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 4,593,409.2 | 0.7526 | 4,557,320.2 | 4,617,150.1 | 19,929.7 | 1.001x | 1.001x | unchanged (within spread) | +0.11% (null control: program identical) |

#### `hex8-bounded` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 617,412.0 | 0.5888 |
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 625,202.9 | 0.5962 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 88,308.2 | 0.3369 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 89,143.2 | 0.3401 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 22,069.2 | 0.3367 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 22,191.6 | 0.3386 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 18,153.8 | 0.2955 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 18,340.3 | 0.2985 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 4,804.1 | 0.2932 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 4,866.8 | 0.2970 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 8,187.7 | 0.4997 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 8,299.4 | 0.5066 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 7,943.2 | 1.9393 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 8,047.3 | 1.9647 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 329.3 | 0.3216 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 332.6 | 0.3248 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 21,886.7 | 0.3340 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 21,983.4 | 0.3354 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 2,727.7 | 0.3330 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2,747.3 | 0.3354 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 5,078.8 | 0.3100 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5,144.6 | 0.3140 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 2,692.2 | 0.6573 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2,712.2 | 0.6622 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 1,402,691.2 | 1.3378 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,402,400.3 | 1.3375 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 333,656.1 | 1.2730 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 332,089.3 | 1.2671 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 677,558.0 | 0.6462 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 678,132.3 | 0.6468 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 672,876.4 | 0.6417 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 677,234.9 | 0.6459 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 679,146.2 | 0.6477 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 679,093.5 | 0.6477 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 14,306.8 | 0.2329 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 14,343.3 | 0.2335 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3,802.1 | 0.2320 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,818.0 | 0.2330 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `t-qs-1m`, 1,402,400.3 ns, 1,048,501 B; largest Δ: `t-1m`, +7,791.0 ns (now 625,202.9 ns), 1,048,576 B

### `hex8-bounded` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 611.8 | 597.6 | 623.7 | 9.2 | 1.000x | 1.000x | - | - | 75 | 8.2 | 3.8 | 100% |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 615.5 | 612.4 | 619.9 | 2.4 | 1.006x | 1.006x | unchanged (within spread) | +0.60% (null control: program identical) | 75 | 8.2 | 3.7 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `sd-empty-alt-hit`, 99.9 ns, 61 B; largest Δ: `sec-github-pat`, +0.9 ns (now 81.0 ns), 93 B

### `high-byte-run` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 1,158,207.5 | 0.1898 | 1,154,384.3 | 1,216,683.5 | 23,361.0 | 1.000x | 1.000x | unchanged (within spread) | -0.65% vs bar 12.76% (band) → **within** |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 1,165,766.5 | 0.1910 | 1,156,732.0 | 1,176,723.3 | 7,143.8 | 1.007x | 1.007x | - | - |

#### `high-byte-run` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 199,172.5 | 0.1899 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 198,670.2 | 0.1895 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 49,944.6 | 0.1905 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 49,539.0 | 0.1890 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 12,450.1 | 0.1900 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 12,468.7 | 0.1903 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 11,646.0 | 0.1896 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 11,637.6 | 0.1894 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,097.9 | 0.1891 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3,115.0 | 0.1901 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,104.2 | 0.1895 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3,144.0 | 0.1919 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 779.6 | 0.1903 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 795.0 | 0.1941 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 201.0 | 0.1963 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 202.3 | 0.1975 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 12,457.9 | 0.1901 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 12,580.6 | 0.1920 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,557.1 | 0.1901 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 1,571.8 | 0.1919 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,110.1 | 0.1898 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3,152.1 | 0.1924 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 780.1 | 0.1904 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 778.0 | 0.1899 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 198,688.7 | 0.1895 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 201,437.1 | 0.1921 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 49,635.6 | 0.1894 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 50,454.1 | 0.1925 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 198,903.9 | 0.1897 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 198,615.0 | 0.1894 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 198,871.1 | 0.1897 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 199,469.8 | 0.1902 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 198,942.9 | 0.1897 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 200,606.8 | 0.1913 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 11,628.3 | 0.1893 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 11,663.5 | 0.1898 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,100.1 | 0.1892 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3,110.2 | 0.1898 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `t-1m`, 199,172.5 ns, 1,048,576 B; largest Δ: `t-qs-1m`, -2,748.4 ns (now 198,688.7 ns), 1,048,501 B

### `high-byte-run` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 538.9 | 515.2 | 544.9 | 12.6 | 1.000x | 1.000x | - | - | 75 | 7.2 | 3.8 | 100% |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 553.6 | 549.8 | 569.8 | 7.0 | 1.027x | 1.027x | unchanged (within spread) | +2.73% vs bar 8.81% (band) → **within** | 75 | 7.4 | 3.7 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `sec-github-pat`, 22.1 ns, 93 B; largest Δ: `v-ipv4`, +1.5 ns (now 6.3 ns), 11 B

### `ipv4-near-miss` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 47.4 | 0.0000 | 47.3 | 47.4 | 0.0 | 1.000x | 1.000x | faster ×1.01 | -0.96% (null control: program identical) |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 47.8 | 0.0000 | 47.8 | 48.0 | 0.1 | 1.010x | 1.010x | - | - |

#### `ipv4-near-miss` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.5 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 2.5 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.5 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 2.5 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.5 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 2.6 | 0.0000 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.5 | 0.0000 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 2.5 | 0.0000 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.5 | 0.0002 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 2.5 | 0.0002 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.5 | 0.0002 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 2.5 | 0.0002 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.5 | 0.0006 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 2.5 | 0.0006 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.5 | 0.0024 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 2.5 | 0.0025 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.5 | 0.0000 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 2.5 | 0.0000 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.5 | 0.0003 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 2.5 | 0.0003 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.5 | 0.0002 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 2.5 | 0.0002 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.5 | 0.0006 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 2.5 | 0.0006 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.5 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 2.5 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.5 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 2.5 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.5 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 2.5 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.5 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 2.5 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.5 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 2.5 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.5 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 2.5 | 0.0000 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.5 | 0.0002 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 2.5 | 0.0002 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `t-64k`, 2.5 ns, 65,536 B; largest Δ: `t-tail-space-1m`, -0.0 ns (now 2.5 ns), 1,048,522 B

### `ipv4-near-miss` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 263.3 | 246.7 | 267.4 | 7.2 | 1.000x | 1.000x | - | - | 75 | 3.5 | 3.8 | 100% |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 266.0 | 263.6 | 268.2 | 1.5 | 1.010x | 1.010x | unchanged (within spread) | +1.02% (null control: program identical) | 75 | 3.5 | 3.7 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `v-ipv4`, 7.4 ns, 11 B; largest Δ: `rd-numeric-id-hit`, -0.4 ns (now 4.6 ns), 4 B

### `keyword-prefix-order` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 1,145,005.5 | 0.1876 | 1,133,601.0 | 1,155,526.9 | 8,140.3 | 1.000x | 1.000x | unchanged (within spread) | -0.60% (null control: program identical) |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 1,151,907.3 | 0.1887 | 1,146,872.8 | 1,205,164.0 | 26,521.3 | 1.006x | 1.006x | - | - |

#### `keyword-prefix-order` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 243,037.0 | 0.2318 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 241,659.6 | 0.2305 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 33,970.0 | 0.1296 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 33,606.6 | 0.1282 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 8,456.3 | 0.1290 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 8,380.3 | 0.1279 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 9,031.8 | 0.1470 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 8,973.7 | 0.1461 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2,422.0 | 0.1478 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 2,396.4 | 0.1463 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.6 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 76.8 | 0.0047 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 20.2 | 0.0049 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 22.2 | 0.0054 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 105.6 | 0.1032 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 105.2 | 0.1027 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,391.5 | 0.1128 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 7,397.8 | 0.1129 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 850.6 | 0.1038 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 847.9 | 0.1035 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2,759.9 | 0.1684 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 2,763.8 | 0.1687 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 175.4 | 0.0428 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 175.4 | 0.0428 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 83,338.0 | 0.0795 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 84,219.3 | 0.0803 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 20,620.6 | 0.0787 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 20,617.9 | 0.0787 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 247,794.0 | 0.2363 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 248,955.6 | 0.2374 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 241,506.4 | 0.2303 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 246,564.0 | 0.2352 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 243,353.8 | 0.2321 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 245,893.7 | 0.2345 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 376.8 | 0.0061 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 370.9 | 0.0060 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 75.2 | 0.0046 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 75.2 | 0.0046 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `t-tail-digits-1m`, 247,794.0 ns, 1,048,522 B; largest Δ: `t-tail-space-1m`, -5,057.5 ns (now 241,506.4 ns), 1,048,522 B

### `keyword-prefix-order` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 340.0 | 327.7 | 344.7 | 5.8 | 1.000x | 1.000x | unchanged (within spread) | -0.46% (null control: program identical) | 75 | 4.5 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 341.5 | 335.8 | 345.1 | 3.0 | 1.005x | 1.005x | - | - | 75 | 4.6 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `br-tag-mismatch`, 8.9 ns, 19 B; largest Δ: `waf-benign`, -0.2 ns (now 4.4 ns), 39 B

### `letters-bounded-tail-z` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 462.2 | 0.0001 | 461.2 | 467.9 | 2.4 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 471.6 | 0.0001 | 470.1 | 495.0 | 9.5 | 1.020x | 1.020x | unchanged (within spread) | +2.04% (null control: program identical) |

#### `letters-bounded-tail-z` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.1 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.2 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 327.3 | 0.0053 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 334.0 | 0.0054 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0004 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.2 | 0.0004 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0004 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.2 | 0.0004 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0015 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.2 | 0.0015 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 10.0 | 0.0098 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 10.3 | 0.0100 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 9.7 | 0.0001 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 9.9 | 0.0002 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 10.7 | 0.0013 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 10.9 | 0.0013 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 9.7 | 0.0006 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 9.9 | 0.0006 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 9.1 | 0.0022 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 9.3 | 0.0023 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.2 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.2 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.2 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.2 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 9.8 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 10.1 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.2 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 9.1 | 0.0006 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 9.2 | 0.0006 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `t-evil-match-60k`, 334.0 ns, 61,440 B

### `letters-bounded-tail-z` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 480.4 | 480.0 | 484.4 | 2.0 | 1.000x | 1.000x | unchanged (within spread) | -1.21% (null control: program identical) | 75 | 6.4 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 486.3 | 481.5 | 491.9 | 3.4 | 1.012x | 1.012x | - | - | 75 | 6.5 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `sd-empty-alt-miss`, 22.1 ns, 60 B; largest Δ: `rd-email-near-miss`, +0.3 ns (now 10.8 ns), 20 B

### `logparse-atomic` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 12,859.1 | 0.0021 | 12,785.6 | 12,952.1 | 58.9 | 1.000x | 1.000x | **dominated**: `t-hyb-logline-16k` is 99.1% of this set | unchanged (within spread) | -0.25% vs bar 12.76% (band) → **within** |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 12,890.8 | 0.0021 | 12,862.0 | 13,047.5 | 65.5 | 1.002x | 1.002x | **dominated**: `t-hyb-logline-16k` is 99.1% of this set | - | - |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `logparse-atomic` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.4 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 6.5 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.5 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 6.5 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.1 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.8 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 6.9 | 0.0001 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.8 | 0.0004 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 6.9 | 0.0004 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.6 | 0.0004 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 6.5 | 0.0004 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.6 | 0.0016 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 6.5 | 0.0016 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.6 | 0.0064 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 6.7 | 0.0065 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.5 | 0.0001 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 6.7 | 0.0001 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.6 | 0.0008 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 6.7 | 0.0008 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 12,741.9 | 0.7777 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 12,773.0 | 0.7796 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.5 | 0.0016 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 6.5 | 0.0016 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.8 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 6.7 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.9 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 6.9 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.4 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 6.5 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.4 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 6.5 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.5 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 6.5 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.4 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 6.5 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.4 | 0.0004 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 6.5 | 0.0004 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `t-hyb-logline-16k`, 12,741.9 ns, 16,384 B

### `logparse-atomic` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 441.9 | 428.1 | 447.9 | 6.5 | 1.000x | 1.000x | faster ×1.17 | -14.61% vs bar 8.81% (band) → **improve** | 75 | 5.9 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 517.6 | 510.0 | 520.4 | 3.8 | 1.171x | 1.171x | - | - | 75 | 6.9 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `lp-atomic-hit`, 30.4 ns, 31 B; largest Δ: `sd-dollar-nl`, -3.1 ns (now 3.6 ns), 7 B

### `logparse-atomic-removed` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 12,905.2 | 0.0021 | 12,803.9 | 12,961.7 | 60.3 | 1.000x | 1.000x | **dominated**: `t-hyb-logline-16k` is 99.1% of this set | unchanged (within spread) | -0.61% vs bar 12.76% (band) → **within** |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 12,984.4 | 0.0021 | 12,785.8 | 13,436.5 | 216.9 | 1.006x | 1.006x | **dominated**: `t-hyb-logline-16k` is 99.1% of this set | - | - |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `logparse-atomic-removed` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.5 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 6.5 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.5 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 6.8 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.1 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 5.9 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.8 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 6.9 | 0.0001 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.9 | 0.0004 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 6.8 | 0.0004 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.4 | 0.0004 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 6.4 | 0.0004 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.4 | 0.0016 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 6.4 | 0.0016 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.7 | 0.0065 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 6.6 | 0.0065 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.7 | 0.0001 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 6.6 | 0.0001 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.7 | 0.0008 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 6.6 | 0.0008 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 12,787.8 | 0.7805 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 12,866.0 | 0.7853 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.5 | 0.0016 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 6.4 | 0.0016 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.7 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 6.6 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.9 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 6.9 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.5 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 6.4 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.5 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 6.4 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.5 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 6.4 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.5 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 6.4 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.5 | 0.0004 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 6.5 | 0.0004 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `t-hyb-logline-16k`, 12,787.8 ns, 16,384 B

### `logparse-atomic-removed` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 436.1 | 416.6 | 443.0 | 9.1 | 1.000x | 1.000x | faster ×1.18 | -15.60% vs bar 8.81% (band) → **improve** | 75 | 5.8 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 516.7 | 499.8 | 547.0 | 16.5 | 1.185x | 1.185x | - | - | 75 | 6.9 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `lp-atomic-hit`, 29.7 ns, 31 B; largest Δ: `rd-evil-alt-hit`, -2.9 ns (now 3.8 ns), 4 B

### `mojibake-curly-quote` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 42,985.8 | 0.0070 | 42,864.9 | 43,162.8 | 97.7 | 1.000x | 1.000x | faster ×1.03 | -2.90% vs bar 12.76% (band) → **within** |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 44,270.2 | 0.0073 | 43,695.8 | 44,894.9 | 448.9 | 1.030x | 1.030x | - | - |

#### `mojibake-curly-quote` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,520.7 | 0.0072 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 7,877.3 | 0.0075 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,570.6 | 0.0060 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 1,580.1 | 0.0060 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 400.0 | 0.0061 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 403.2 | 0.0062 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 375.3 | 0.0061 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 377.6 | 0.0061 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.5 | 0.0047 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 77.4 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.2 | 0.0046 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 77.0 | 0.0047 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 21.3 | 0.0052 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.5 | 0.0052 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7.8 | 0.0076 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 8.0 | 0.0078 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 399.3 | 0.0061 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 402.1 | 0.0061 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 39.9 | 0.0049 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 40.1 | 0.0049 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.3 | 0.0047 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 76.7 | 0.0047 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 21.5 | 0.0052 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.7 | 0.0053 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,567.7 | 0.0072 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7,819.9 | 0.0075 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,569.9 | 0.0060 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,582.6 | 0.0060 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,580.5 | 0.0072 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,979.9 | 0.0076 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,549.7 | 0.0072 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,715.3 | 0.0074 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,607.7 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,960.3 | 0.0076 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 374.8 | 0.0061 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 377.2 | 0.0061 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.4 | 0.0047 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.8 | 0.0047 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `t-tail-txt-1m`, 7,607.7 ns, 1,048,527 B; largest Δ: `t-tail-digits-1m`, -399.4 ns (now 7,580.5 ns), 1,048,522 B

### `mojibake-curly-quote` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 307.5 | 307.3 | 324.0 | 6.4 | 1.000x | 1.000x | - | - | 75 | 4.1 | 3.8 | 100% |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 318.8 | 307.2 | 325.8 | 6.0 | 1.037x | 1.037x | unchanged (within spread) | +3.66% vs bar 8.81% (band) → **within** | 75 | 4.3 | 3.7 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `nu-mojibake`, 21.0 ns, 7 B; largest Δ: `floor-hit`, -1.8 ns (now 2.3 ns), 1 B

### `nested-comment-rec` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 42,836.5 | 0.0070 | 42,796.2 | 43,590.7 | 301.0 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 43,407.8 | 0.0071 | 43,265.0 | 43,541.4 | 92.4 | 1.013x | 1.013x | unchanged (within spread) | +1.33% vs bar 12.76% (band) → **within** |

#### `nested-comment-rec` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 7,466.3 | 0.0071 |
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,550.2 | 0.0072 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 1,572.5 | 0.0060 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,586.8 | 0.0061 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 401.5 | 0.0061 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 404.6 | 0.0062 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 376.7 | 0.0061 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 380.3 | 0.0062 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.5 | 0.0047 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 78.0 | 0.0048 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 76.5 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 77.6 | 0.0047 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.7 | 0.0053 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 22.1 | 0.0054 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 8.7 | 0.0085 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 9.2 | 0.0090 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 402.1 | 0.0061 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 405.8 | 0.0062 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 39.9 | 0.0049 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 41.1 | 0.0050 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 76.3 | 0.0047 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 77.4 | 0.0047 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.4 | 0.0052 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 22.3 | 0.0054 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7,591.9 | 0.0072 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,798.3 | 0.0074 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,571.3 | 0.0060 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,588.6 | 0.0061 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,591.0 | 0.0072 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,669.4 | 0.0073 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,539.3 | 0.0072 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,638.7 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,630.5 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,585.3 | 0.0072 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 376.9 | 0.0061 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 379.8 | 0.0062 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.3 | 0.0047 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 77.6 | 0.0047 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `t-qs-1m`, 7,798.3 ns, 1,048,501 B

### `nested-comment-rec` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 799.6 | 781.8 | 801.6 | 7.5 | 1.000x | 1.000x | faster ×1.02 | -2.11% vs bar 8.81% (band) → **within** | 75 | 10.7 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 816.9 | 813.2 | 832.0 | 6.8 | 1.022x | 1.022x | - | - | 75 | 10.9 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `rec-comment-nested`, 347.2 ns, 34 B

### `numeric-id-nested-plus` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 2,455.3 | 0.0004 | 2,440.7 | 3,030.2 | 229.4 | 1.000x | 1.000x | **dominated**: `t-hyb-digits-4k` is 95.8% of this set | unchanged (within spread) | -0.09% (null control: program identical) |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 2,457.6 | 0.0004 | 2,076.4 | 2,489.2 | 156.9 | 1.001x | 1.001x | **dominated**: `t-hyb-digits-4k` is 95.9% of this set | - | - |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `numeric-id-nested-plus` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.4 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.4 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.5 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 5.5 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.4 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0001 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.4 | 0.0003 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0003 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 9.0 | 0.0006 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 8.7 | 0.0005 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2,352.1 | 0.5742 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 2,355.9 | 0.5752 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.4 | 0.0053 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0053 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.4 | 0.0001 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0001 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.4 | 0.0007 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0007 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.4 | 0.0003 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0003 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.4 | 0.0013 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0013 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.9 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 5.8 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.3 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 6.0 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.4 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.4 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.4 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.4 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.4 | 0.0003 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0003 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `t-hyb-digits-4k`, 2,352.1 ns, 4,096 B

### `numeric-id-nested-plus` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 535.9 | 513.0 | 541.9 | 10.5 | 1.000x | 1.000x | unchanged (within spread) | -0.70% (null control: program identical) | 75 | 7.1 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 539.7 | 525.0 | 551.7 | 10.6 | 1.007x | 1.007x | - | - | 75 | 7.2 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `rd-numeric-id-near-miss`, 15.8 ns, 20 B

### `phone-list-nested-plus` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 3,263.0 | 0.0005 | 3,199.7 | 5,438.9 | 861.3 | 1.000x | 1.000x | **dominated**: `t-hyb-digits-4k` is 96.9% of this set | unchanged (within spread) | -1.78% (null control: program identical) |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 3,322.3 | 0.0005 | 3,190.8 | 3,551.7 | 133.1 | 1.018x | 1.018x | **dominated**: `t-hyb-digits-4k` is 96.9% of this set | - | - |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `phone-list-nested-plus` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.4 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.5 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.5 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 5.5 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.4 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0001 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.4 | 0.0003 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0003 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 9.7 | 0.0006 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 9.7 | 0.0006 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,160.0 | 0.7715 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 3,216.8 | 0.7853 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.4 | 0.0053 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0053 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.4 | 0.0001 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0001 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.4 | 0.0007 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0007 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.4 | 0.0003 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0003 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.4 | 0.0013 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0013 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.6 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 5.8 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.6 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 5.6 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.4 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.4 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.4 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.4 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.4 | 0.0003 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0003 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `t-hyb-digits-4k`, 3,160.0 ns, 4,096 B

### `phone-list-nested-plus` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 548.3 | 524.3 | 567.8 | 17.5 | 1.000x | 1.000x | unchanged (within spread) | -4.82% (null control: program identical) | 75 | 7.3 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 576.1 | 567.5 | 582.3 | 4.8 | 1.051x | 1.051x | - | - | 75 | 7.7 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `rd-phone-list-hit`, 19.1 ns, 7 B; largest Δ: `rd-numeric-id-near-miss`, -3.0 ns (now 15.7 ns), 20 B

### `phone-palindrome-6` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 7,258,854.7 | 1.1892 | 7,211,687.4 | 7,289,774.4 | 25,005.8 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 7,312,190.0 | 1.1980 | 7,287,969.0 | 7,326,614.6 | 13,242.8 | 1.007x | 1.007x | slower ×1.01 | +0.73% vs bar 12.76% (band) → **within** |

#### `phone-palindrome-6` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 1,031,034.3 | 0.9833 |
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,053,332.2 | 1.0045 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 252,437.5 | 0.9630 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 257,552.2 | 0.9825 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 54,961.0 | 0.8386 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 55,042.3 | 0.8399 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 11,655.5 | 0.1897 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 11,766.3 | 0.1915 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3,085.8 | 0.1883 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,140.8 | 0.1917 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 67,090.0 | 4.0948 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 68,784.9 | 4.1983 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 33,333.2 | 8.1380 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 33,586.9 | 8.1999 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 782.3 | 0.7639 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 802.3 | 0.7835 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 55,094.3 | 0.8407 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 55,366.3 | 0.8448 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 6,762.7 | 0.8255 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,077.7 | 0.8640 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3,125.5 | 0.1908 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,162.0 | 0.1930 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 10,928.6 | 2.6681 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 10,903.8 | 2.6621 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 2,338,621.4 | 2.2304 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2,341,526.4 | 2.2332 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 590,225.1 | 2.2520 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 587,064.3 | 2.2399 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 925,504.9 | 0.8827 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 928,601.8 | 0.8856 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 922,138.8 | 0.8795 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 935,487.3 | 0.8922 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 929,163.6 | 0.8862 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 944,000.0 | 0.9003 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 11,785.9 | 0.1918 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 11,750.5 | 0.1913 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3,137.4 | 0.1915 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,134.8 | 0.1913 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `t-qs-1m`, 2,341,526.4 ns, 1,048,501 B; largest Δ: `t-1m`, +22,297.8 ns (now 1,053,332.2 ns), 1,048,576 B

### `phone-palindrome-6` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 1,498.4 | 1,487.1 | 1,502.3 | 6.0 | 1.000x | 1.000x | faster ×1.07 | -6.73% vs bar 0.50% (IQR-only) → **improve (IQR only: band n=3 < 10)** | 75 | 20.0 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 1,606.5 | 1,591.7 | 1,614.4 | 7.9 | 1.072x | 1.072x | - | - | 75 | 21.4 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `sec-slack-webhook`, 166.9 ns, 81 B; largest Δ: `dt-prose-month`, -11.7 ns (now 21.5 ns), 13 B

### `pwd-strength-chain` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 447,132.5 | 0.0733 | 446,276.3 | 448,672.4 | 939.8 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 447,756.7 | 0.0734 | 445,687.6 | 454,122.3 | 2,873.0 | 1.001x | 1.001x | unchanged (within spread) | +0.14% vs bar 12.76% (band) → **within** |

#### `pwd-strength-chain` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 25.7 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 30.5 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 41.5 | 0.0002 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 41.5 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 35.3 | 0.0005 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 27.3 | 0.0004 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 233,697.6 | 3.8037 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 234,613.2 | 3.8186 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 63,042.6 | 3.8476 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 62,778.4 | 3.8315 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 56,817.6 | 3.4679 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 56,353.7 | 3.4396 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 14,148.8 | 3.4543 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 14,149.2 | 3.4544 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 19.3 | 0.0188 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 40.6 | 0.0397 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 19.2 | 0.0003 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 42.9 | 0.0007 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 19.2 | 0.0023 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 42.2 | 0.0051 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 63,239.4 | 3.8598 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 63,059.7 | 3.8489 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 15,823.2 | 3.8631 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 15,818.7 | 3.8620 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 23.5 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 18.8 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 58.4 | 0.0002 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 58.3 | 0.0002 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 21.0 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 21.2 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 21.0 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 25.7 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 21.0 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 25.4 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 7.5 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7.6 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 7.4 | 0.0005 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7.6 | 0.0005 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `t-evil-match-60k`, 234,613.2 ns, 61,440 B

### `pwd-strength-chain` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 5,953.4 | 5,914.6 | 5,963.5 | 21.0 | 1.000x | 1.000x | unchanged (within spread) | -0.94% vs bar 0.99% (IQR-only) → **within (IQR only: band n=3 < 10)** | 75 | 79.4 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 6,010.1 | 5,953.1 | 6,058.2 | 40.0 | 1.010x | 1.010x | - | - | 75 | 80.1 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `sec-github-pat`, 505.0 ns, 93 B; largest Δ: `nu-mojibake`, -3.3 ns (now 3.7 ns), 7 B

### `quoted-delim-match` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 1,409,085.1 | 0.2309 | 1,398,027.4 | 1,424,397.1 | 11,138.4 | 1.000x | 1.000x | unchanged (within spread) | -0.99% (null control: program identical) |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 1,423,227.2 | 0.2332 | 1,404,146.6 | 1,428,041.1 | 8,848.4 | 1.010x | 1.010x | - | - |

#### `quoted-delim-match` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 364,942.7 | 0.3480 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 367,302.8 | 0.3503 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 88,335.0 | 0.3370 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 88,717.8 | 0.3384 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 21,841.6 | 0.3333 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 22,160.8 | 0.3381 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 11,896.8 | 0.1936 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 12,055.9 | 0.1962 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,155.5 | 0.1926 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3,152.1 | 0.1924 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,170.5 | 0.1935 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3,160.4 | 0.1929 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 795.1 | 0.1941 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 791.9 | 0.1933 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 476.3 | 0.4651 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 484.1 | 0.4728 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 31,437.9 | 0.4797 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 31,520.1 | 0.4810 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 4,106.3 | 0.5013 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 4,097.3 | 0.5002 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,172.0 | 0.1936 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3,164.0 | 0.1931 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 782.6 | 0.1911 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 796.2 | 0.1944 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 203,609.0 | 0.1942 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 204,502.9 | 0.1950 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 51,328.3 | 0.1958 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 50,772.8 | 0.1937 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 200,019.2 | 0.1908 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 204,714.3 | 0.1952 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 202,473.0 | 0.1931 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 204,885.7 | 0.1954 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 200,862.0 | 0.1916 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 204,319.8 | 0.1949 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 11,860.8 | 0.1930 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 12,061.9 | 0.1963 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,162.8 | 0.1930 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3,159.5 | 0.1928 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `t-1m`, 364,942.7 ns, 1,048,576 B; largest Δ: `t-tail-digits-1m`, -4,695.1 ns (now 200,019.2 ns), 1,048,522 B

### `quoted-delim-match` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 940.4 | 932.1 | 945.2 | 5.0 | 1.000x | 1.000x | unchanged (within spread) | -0.41% (null control: program identical) | 75 | 12.5 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 944.2 | 939.7 | 953.1 | 4.9 | 1.004x | 1.004x | - | - | 75 | 12.6 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `waf-sleep`, 101.1 ns, 16 B; largest Δ: `sd-empty-alt-miss`, -1.0 ns (now 18.2 ns), 60 B

### `router-prefix-order` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 196,902.5 | 0.0323 | 196,471.2 | 200,882.2 | 1,651.6 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 197,835.3 | 0.0324 | 196,928.7 | 199,674.4 | 1,099.0 | 1.005x | 1.005x | unchanged (within spread) | +0.47% (null control: program identical) |

#### `router-prefix-order` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 110,869.4 | 0.1057 |
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 111,644.7 | 0.1065 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 27,209.5 | 0.1038 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 27,491.8 | 0.1049 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 6,403.1 | 0.0977 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6,476.6 | 0.0988 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 375.1 | 0.0061 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 376.5 | 0.0061 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 75.0 | 0.0046 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 75.4 | 0.0046 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 12,397.7 | 0.7567 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 12,305.0 | 0.7510 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 20.5 | 0.0050 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 20.4 | 0.0050 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 73.2 | 0.0715 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 73.8 | 0.0720 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 6,133.4 | 0.0936 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6,121.5 | 0.0934 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 741.9 | 0.0906 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 746.2 | 0.0911 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 75.4 | 0.0046 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 75.0 | 0.0046 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 119.6 | 0.0292 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 119.6 | 0.0292 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7,542.4 | 0.0072 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,579.5 | 0.0072 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,581.5 | 0.0060 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,583.2 | 0.0060 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,627.4 | 0.0073 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,455.7 | 0.0071 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,585.5 | 0.0072 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,793.6 | 0.0074 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,632.5 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,625.0 | 0.0073 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 376.7 | 0.0061 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 375.8 | 0.0061 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 75.5 | 0.0046 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 75.7 | 0.0046 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 111,644.7 ns, 1,048,576 B

### `router-prefix-order` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 298.2 | 296.3 | 302.9 | 2.7 | 1.000x | 1.000x | - | - | 75 | 4.0 | 3.8 | 100% |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 300.4 | 296.2 | 312.2 | 6.3 | 1.007x | 1.007x | unchanged (within spread) | +0.74% (null control: program identical) | 75 | 4.0 | 3.7 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `sec-slack-webhook`, 14.1 ns, 81 B

### `tag-depth3-bound` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 43,860.9 | 0.0072 | 43,463.3 | 44,176.3 | 234.0 | 1.000x | 1.000x | unchanged (within spread) | -0.41% vs bar 12.76% (band) → **within** |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 44,041.2 | 0.0072 | 43,039.1 | 44,422.4 | 461.6 | 1.004x | 1.004x | - | - |

#### `tag-depth3-bound` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,808.5 | 0.0074 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 7,650.8 | 0.0073 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,587.3 | 0.0061 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 1,582.5 | 0.0060 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 404.2 | 0.0062 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 405.0 | 0.0062 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 380.1 | 0.0062 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 379.0 | 0.0062 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 77.4 | 0.0047 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 77.4 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 77.4 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 77.4 | 0.0047 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 22.0 | 0.0054 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.8 | 0.0053 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 9.0 | 0.0088 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 8.8 | 0.0086 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 405.3 | 0.0062 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 404.4 | 0.0062 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 40.4 | 0.0049 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 40.1 | 0.0049 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 77.0 | 0.0047 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 76.9 | 0.0047 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 21.8 | 0.0053 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.6 | 0.0053 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,796.2 | 0.0074 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7,608.1 | 0.0073 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,587.8 | 0.0061 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,584.4 | 0.0060 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,868.9 | 0.0075 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,824.9 | 0.0075 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,670.1 | 0.0073 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,614.8 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,618.3 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,996.0 | 0.0076 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 379.6 | 0.0062 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 379.1 | 0.0062 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 77.1 | 0.0047 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.9 | 0.0047 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `t-tail-digits-1m`, 7,868.9 ns, 1,048,522 B; largest Δ: `t-tail-txt-1m`, -377.7 ns (now 7,618.3 ns), 1,048,527 B

### `tag-depth3-bound` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 500.5 | 496.8 | 507.9 | 3.8 | 1.000x | 1.000x | faster ×1.10 | -9.07% vs bar 8.81% (band) → **improve** | 75 | 6.7 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 550.4 | 545.6 | 560.5 | 5.3 | 1.100x | 1.100x | - | - | 75 | 7.3 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `br-tag-mismatch`, 49.0 ns, 19 B; largest Δ: `rec-parens-unbalanced`, -2.1 ns (now 3.9 ns), 5 B

### `tag-pair-match` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 42,937.5 | 0.0070 | 42,793.4 | 43,609.1 | 357.0 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 43,675.3 | 0.0072 | 43,456.4 | 44,132.9 | 228.6 | 1.017x | 1.017x | slower ×1.02 | +1.72% vs bar 12.76% (band) → **within** |

#### `tag-pair-match` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 7,496.6 | 0.0071 |
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,836.5 | 0.0075 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 1,571.7 | 0.0060 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,585.6 | 0.0060 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 404.1 | 0.0062 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 404.5 | 0.0062 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 377.0 | 0.0061 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 379.8 | 0.0062 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.2 | 0.0046 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 77.1 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 75.9 | 0.0046 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.5 | 0.0047 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.2 | 0.0052 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 21.7 | 0.0053 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 8.7 | 0.0085 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 8.8 | 0.0086 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 401.1 | 0.0061 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 404.9 | 0.0062 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 39.3 | 0.0048 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 39.6 | 0.0048 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 75.9 | 0.0046 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.5 | 0.0047 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 20.5 | 0.0050 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 20.7 | 0.0051 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7,584.8 | 0.0072 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,616.2 | 0.0073 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,580.9 | 0.0060 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,587.9 | 0.0061 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,413.3 | 0.0071 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,737.0 | 0.0074 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,574.4 | 0.0072 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,663.8 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,675.2 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,649.8 | 0.0073 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 376.7 | 0.0061 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 379.4 | 0.0062 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.1 | 0.0046 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.9 | 0.0047 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 7,836.5 ns, 1,048,576 B

### `tag-pair-match` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 507.9 | 507.5 | 511.1 | 1.4 | 1.000x | 1.000x | faster ×1.06 | -5.35% vs bar 8.81% (band) → **within** | 75 | 6.8 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 536.6 | 528.6 | 548.3 | 7.3 | 1.056x | 1.056x | - | - | 75 | 7.2 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `rec-tag-depth3`, 58.2 ns, 22 B; largest Δ: `rec-parens-unbalanced`, -2.0 ns (now 3.7 ns), 5 B

### `tail-digits-eol` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 867.5 | 0.0001 | 865.2 | 885.9 | 7.6 | 1.000x | 1.000x | **dominated**: `t-hyb-digits-4k` is 92.0% of this set | unchanged (within spread) | -0.15% (null control: program identical) |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 868.8 | 0.0001 | 849.4 | 879.0 | 10.6 | 1.002x | 1.002x | **dominated**: `t-hyb-digits-4k` is 92.0% of this set | - | - |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `tail-digits-eol` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 9.0 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 8.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 3.2 | 0.0000 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0001 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 797.8 | 0.1948 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 799.3 | 0.1952 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0030 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0030 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0004 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0004 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0008 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0008 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 3.2 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 10.8 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 10.7 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.2 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0002 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `t-hyb-digits-4k`, 797.8 ns, 4,096 B

### `tail-digits-eol` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 284.1 | 283.4 | 290.3 | 2.6 | 1.000x | 1.000x | - | - | 75 | 3.8 | 3.8 | 100% |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 287.6 | 277.2 | 291.0 | 5.1 | 1.012x | 1.012x | unchanged (within spread) | +1.23% (null control: program identical) | 75 | 3.8 | 3.7 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `v-us-zip-plus4`, 6.4 ns, 10 B; largest Δ: `rd-trim-hit`, +0.2 ns (now 3.3 ns), 4 B

### `tail-dotstar-txt` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 69.7 | 0.0000 | 69.6 | 71.0 | 0.5 | 1.000x | 1.000x | unchanged (within spread) | -0.89% (null control: program identical) |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 70.4 | 0.0000 | 70.1 | 72.3 | 0.8 | 1.009x | 1.009x | - | - |

#### `tail-dotstar-txt` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 3.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.2 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 3.4 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 3.0 | 0.0000 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 3.2 | 0.0001 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0007 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0008 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0030 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0030 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0004 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0004 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0007 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0008 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.3 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 3.3 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.3 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 3.3 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 13.9 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 13.9 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 3.2 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0002 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `t-tail-txt-1m`, 13.9 ns, 1,048,527 B; largest Δ: `t-1m`, -0.2 ns (now 3.1 ns), 1,048,576 B

### `tail-dotstar-txt` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 244.5 | 243.6 | 246.7 | 1.2 | 1.000x | 1.000x | unchanged (within spread) | -0.08% (null control: program identical) | 75 | 3.3 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 244.7 | 241.8 | 245.0 | 1.3 | 1.001x | 1.001x | - | - | 75 | 3.3 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `lp-winpath-reserved`, 9.8 ns, 24 B; largest Δ: `nu-high-byte`, +0.1 ns (now 3.1 ns), 2 B

### `tail-ext-lower-txt` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 68.2 | 0.0000 | 67.8 | 68.7 | 0.3 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 68.3 | 0.0000 | 68.2 | 70.0 | 0.7 | 1.002x | 1.002x | unchanged (within spread) | +0.20% (null control: program identical) |

#### `tail-ext-lower-txt` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 3.2 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 3.0 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 3.2 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0001 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0008 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0008 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0030 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0030 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0004 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0004 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0008 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0008 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.2 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 12.2 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 12.3 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3.2 | 0.0002 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0002 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `t-tail-txt-1m`, 12.3 ns, 1,048,527 B; largest Δ: `t-1m`, -0.1 ns (now 3.1 ns), 1,048,576 B

### `tail-ext-lower-txt` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 239.6 | 238.1 | 252.5 | 5.9 | 1.000x | 1.000x | unchanged (within spread) | -0.80% (null control: program identical) | 75 | 3.2 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 241.5 | 237.2 | 249.3 | 4.0 | 1.008x | 1.008x | - | - | 75 | 3.2 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `lp-winpath-reserved`, 8.2 ns, 24 B; largest Δ: `v-uuid-valid`, -0.2 ns (now 2.9 ns), 36 B

### `tail-space-eol` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 12,021.4 | 0.0020 | 11,984.9 | 13,685.9 | 660.3 | 1.000x | 1.000x | **dominated**: `t-trim-match-60k` is 99.3% of this set | unchanged (within spread) | -0.66% (null control: program identical) |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 12,101.1 | 0.0020 | 11,894.8 | 13,396.0 | 545.4 | 1.007x | 1.007x | **dominated**: `t-trim-match-60k` is 99.3% of this set | - | - |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `tail-space-eol` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 8.1 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 8.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 8.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 8.2 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 8.1 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 8.0 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0002 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0008 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0007 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0030 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0028 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0000 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0004 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0004 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0002 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.9 | 0.0007 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0007 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 8.2 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 8.1 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 8.1 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 8.1 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.9 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 9.2 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 9.1 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.9 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 11,936.0 | 0.1943 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 12,014.6 | 0.1955 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.9 | 0.0002 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 2.9 | 0.0002 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `t-trim-match-60k`, 11,936.0 ns, 61,440 B

### `tail-space-eol` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 225.9 | 222.2 | 232.2 | 4.1 | 1.000x | 1.000x | - | - | 75 | 3.0 | 3.8 | 100% |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 232.6 | 222.9 | 233.2 | 3.8 | 1.030x | 1.030x | unchanged (within spread) | +2.97% (null control: program identical) | 75 | 3.1 | 3.7 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `cg-key-colon`, 6.4 ns, 7 B; largest Δ: `br-tag-pair`, +0.2 ns (now 3.1 ns), 18 B

### `tail-word-eoz` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 12,948.7 | 0.0021 | 12,746.6 | 12,985.5 | 105.8 | 1.000x | 1.000x | **dominated**: `t-evil-match-60k` is 92.9% of this set | - | - |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 12,972.1 | 0.0021 | 12,852.9 | 13,003.6 | 66.4 | 1.002x | 1.002x | **dominated**: `t-evil-match-60k` is 92.9% of this set | unchanged (within spread) | +0.18% (null control: program identical) |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `tail-word-eoz` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 3.7 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.5 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 3.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.6 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 3.4 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.5 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 11,916.1 | 0.1939 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 12,051.4 | 0.1961 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3.4 | 0.0002 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.5 | 0.0002 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3.4 | 0.0002 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.5 | 0.0002 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 806.9 | 0.1970 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 803.8 | 0.1962 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 10.0 | 0.0097 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 10.0 | 0.0098 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 9.4 | 0.0001 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 9.4 | 0.0001 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 10.3 | 0.0013 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 10.4 | 0.0013 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 9.4 | 0.0006 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 9.4 | 0.0006 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 11.1 | 0.0027 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 11.1 | 0.0027 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 3.4 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.4 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 3.4 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.4 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 10.5 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 10.7 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 3.4 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.5 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 9.6 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 9.6 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 3.5 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.6 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 8.6 | 0.0005 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 8.4 | 0.0005 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `t-evil-match-60k`, 12,051.4 ns, 61,440 B

### `tail-word-eoz` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 478.5 | 477.1 | 485.5 | 3.0 | 1.000x | 1.000x | unchanged (within spread) | -1.04% (null control: program identical) | 75 | 6.4 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 483.5 | 476.2 | 489.8 | 5.3 | 1.010x | 1.010x | - | - | 75 | 6.4 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `sec-github-pat`, 23.1 ns, 93 B; largest Δ: `sd-empty-alt-hit`, -2.0 ns (now 17.2 ns), 61 B

### `trim-nested-star` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 71,713.7 | 0.0117 | 70,816.8 | 126,209.5 | 21,289.6 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 78,615.6 | 0.0129 | 68,525.3 | 90,920.4 | 7,993.2 | 1.096x | 1.096x | unchanged (within spread) | +9.62% (null control: program identical) |

#### `trim-nested-star` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 5.3 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.4 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 5.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.3 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 4.9 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 4.9 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 5.1 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.3 | 0.0001 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 5.0 | 0.0003 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.2 | 0.0003 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 5.7 | 0.0003 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.9 | 0.0004 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 5.7 | 0.0014 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.9 | 0.0015 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 5.7 | 0.0055 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.9 | 0.0058 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 5.7 | 0.0001 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.9 | 0.0001 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 5.7 | 0.0007 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.9 | 0.0007 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 5.7 | 0.0003 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.9 | 0.0004 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 6.7 | 0.0016 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.4 | 0.0016 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 5.7 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.9 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 5.7 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.9 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 5.8 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.0 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 5.7 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.9 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 5.8 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.9 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 59,465.1 | 0.9679 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 66,665.5 | 1.0850 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 11,760.2 | 0.7177 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 11,870.2 | 0.7245 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `t-trim-match-60k`, 66,665.5 ns, 61,440 B

### `trim-nested-star` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 407.0 | 403.6 | 422.2 | 6.5 | 1.000x | 1.000x | - | - | 75 | 5.4 | 3.8 | 100% |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 411.9 | 410.2 | 419.8 | 3.4 | 1.012x | 1.012x | unchanged (within spread) | +1.18% (null control: program identical) | 75 | 5.5 | 3.7 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `rd-trim-near-miss`, 31.5 ns, 20 B; largest Δ: `floor-hit`, -0.9 ns (now 5.3 ns), 1 B

### `utf8-lead-no-cont` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 2,307,278.1 | 0.3780 | 2,286,723.3 | 2,345,744.8 | 21,568.4 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 2,334,937.0 | 0.3825 | 2,294,493.3 | 2,346,048.0 | 18,664.9 | 1.012x | 1.012x | unchanged (within spread) | +1.20% (null control: program identical) |

#### `utf8-lead-no-cont` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 393,018.8 | 0.3748 |
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 400,669.1 | 0.3821 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 98,162.7 | 0.3745 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 100,290.9 | 0.3826 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 24,569.4 | 0.3749 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 25,070.1 | 0.3825 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 23,005.1 | 0.3744 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 23,506.2 | 0.3826 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 6,168.0 | 0.3764 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6,262.0 | 0.3822 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 6,138.5 | 0.3747 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6,291.3 | 0.3840 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 1,538.8 | 0.3757 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,580.7 | 0.3859 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 389.6 | 0.3804 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 398.3 | 0.3890 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 24,535.7 | 0.3744 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 25,088.8 | 0.3828 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 3,077.2 | 0.3756 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,136.6 | 0.3829 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 6,165.3 | 0.3763 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6,285.6 | 0.3836 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 1,536.3 | 0.3751 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,563.2 | 0.3816 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 393,398.1 | 0.3752 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 401,187.2 | 0.3826 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 98,125.7 | 0.3744 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 100,382.0 | 0.3830 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 395,415.1 | 0.3771 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 401,026.3 | 0.3825 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 393,574.5 | 0.3754 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 401,247.9 | 0.3827 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 394,682.0 | 0.3764 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 400,914.8 | 0.3824 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 23,562.9 | 0.3835 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 23,529.0 | 0.3830 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 6,265.7 | 0.3824 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6,278.1 | 0.3832 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `t-tail-space-1m`, 401,247.9 ns, 1,048,522 B; largest Δ: `t-qs-1m`, +7,789.1 ns (now 401,187.2 ns), 1,048,501 B

### `utf8-lead-no-cont` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 647.2 | 639.3 | 655.2 | 5.3 | 1.000x | 1.000x | - | - | 75 | 8.6 | 3.8 | 100% |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 653.0 | 642.6 | 655.6 | 4.8 | 1.009x | 1.009x | unchanged (within spread) | +0.90% (null control: program identical) | 75 | 8.7 | 3.7 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `sec-github-pat`, 37.7 ns, 93 B; largest Δ: `waf-union`, +0.8 ns (now 19.5 ns), 43 B

### `uuid-near-miss` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 50.9 | 0.0000 | 50.8 | 51.0 | 0.1 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 51.2 | 0.0000 | 51.2 | 51.3 | 0.0 | 1.007x | 1.007x | slower ×1.01 | +0.69% (null control: program identical) |

#### `uuid-near-miss` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 2.7 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 2.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.7 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 2.7 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.7 | 0.0000 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 2.7 | 0.0000 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.7 | 0.0000 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 2.7 | 0.0002 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.7 | 0.0002 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 2.7 | 0.0002 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.7 | 0.0002 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 2.7 | 0.0007 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.7 | 0.0007 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 2.7 | 0.0026 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.7 | 0.0026 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 2.7 | 0.0000 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.7 | 0.0000 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 2.7 | 0.0003 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.7 | 0.0003 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 2.7 | 0.0002 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.7 | 0.0002 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 2.7 | 0.0007 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.7 | 0.0007 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 2.7 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.7 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 2.7 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.7 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 2.7 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.7 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 2.7 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.7 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 2.7 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.7 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 2.7 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.7 | 0.0000 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 2.7 | 0.0002 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2.7 | 0.0002 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `t-64k`, 2.7 ns, 65,536 B; largest Δ: `t-evil-nearmiss-16k`, +0.0 ns (now 2.7 ns), 16,385 B

### `uuid-near-miss` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 329.8 | 323.0 | 338.6 | 5.2 | 1.000x | 1.000x | unchanged (within spread) | -0.61% (null control: program identical) | 75 | 4.4 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 331.8 | 329.7 | 338.2 | 2.9 | 1.006x | 1.006x | - | - | 75 | 4.4 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `v-uuid-valid`, 17.2 ns, 36 B; largest Δ: `dt-iso8601`, -0.7 ns (now 5.9 ns), 20 B

### `wild-codegrammar-json-array-begin` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 79,186.0 | 0.0130 | 78,117.8 | 80,418.1 | 748.6 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 79,534.6 | 0.0130 | 78,899.8 | 79,870.2 | 361.4 | 1.004x | 1.004x | unchanged (within spread) | +0.44% (null control: program identical) |

#### `wild-codegrammar-json-array-begin` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 33,888.2 | 0.0323 |
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 34,062.6 | 0.0325 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 7,822.0 | 0.0298 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,833.8 | 0.0299 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 2,025.3 | 0.0309 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2,016.3 | 0.0308 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 380.3 | 0.0062 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 380.0 | 0.0062 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 75.9 | 0.0046 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.4 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 75.8 | 0.0046 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.4 | 0.0047 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 20.9 | 0.0051 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 20.8 | 0.0051 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 12.7 | 0.0124 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 12.7 | 0.0124 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 1,666.9 | 0.0254 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,680.8 | 0.0256 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 200.7 | 0.0245 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 201.2 | 0.0246 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 76.6 | 0.0047 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 77.3 | 0.0047 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 20.4 | 0.0050 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 20.5 | 0.0050 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7,545.0 | 0.0072 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,693.4 | 0.0073 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,591.5 | 0.0061 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,596.6 | 0.0061 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,823.2 | 0.0075 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,620.5 | 0.0073 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,644.8 | 0.0073 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,616.8 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,892.6 | 0.0075 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,857.8 | 0.0075 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 379.9 | 0.0062 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 380.0 | 0.0062 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 75.8 | 0.0046 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 75.9 | 0.0046 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `t-1m`, 34,062.6 ns, 1,048,576 B; largest Δ: `t-tail-digits-1m`, -202.7 ns (now 7,620.5 ns), 1,048,522 B

### `wild-codegrammar-json-array-begin` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 290.3 | 289.7 | 293.1 | 1.3 | 1.000x | 1.000x | - | - | 75 | 3.9 | 3.8 | 100% |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 290.4 | 290.1 | 294.4 | 1.7 | 1.000x | 1.000x | unchanged (within spread) | +0.04% (null control: program identical) | 75 | 3.9 | 3.7 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `rec-array-define`, 5.7 ns, 11 B; largest Δ: `sec-slack-webhook`, -0.4 ns (now 4.0 ns), 81 B

### `wild-codegrammar-json-constant` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 6,213,936.3 | 1.0180 | 6,163,076.8 | 6,260,689.7 | 34,061.3 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 6,257,970.5 | 1.0253 | 6,194,901.0 | 6,339,237.9 | 52,402.0 | 1.007x | 1.007x | unchanged (within spread) | +0.71% vs bar 12.76% (band) → **within** |

#### `wild-codegrammar-json-constant` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 932,245.2 | 0.8891 |
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 915,133.6 | 0.8727 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 224,639.3 | 0.8569 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 215,165.8 | 0.8208 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 23,050.6 | 0.3517 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 22,370.1 | 0.3413 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 72,130.0 | 1.1740 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 69,526.0 | 1.1316 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 19,226.3 | 1.1734 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 18,524.6 | 1.1306 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3,166.4 | 0.1933 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,180.2 | 0.1941 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 791.9 | 0.1933 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 793.5 | 0.1937 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 501.3 | 0.4895 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 490.7 | 0.4792 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 29,021.5 | 0.4428 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 29,284.9 | 0.4469 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 3,426.7 | 0.4183 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,761.9 | 0.4592 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 7,363.3 | 0.4494 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,135.7 | 0.4355 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 1,585.9 | 0.3872 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,561.6 | 0.3812 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 1,248,048.7 | 1.1903 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,227,118.8 | 1.1704 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 303,160.2 | 1.1567 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 297,776.8 | 1.1362 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 1,115,973.0 | 1.0643 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,122,033.4 | 1.0701 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 1,114,120.7 | 1.0626 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,127,653.6 | 1.0755 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 1,094,434.9 | 1.0438 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,127,275.1 | 1.0751 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 22,889.1 | 0.3725 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 14,317.6 | 0.2330 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 6,136.8 | 0.3745 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,197.6 | 0.1952 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `t-qs-1m`, 1,227,118.8 ns, 1,048,501 B; largest Δ: `t-tail-txt-1m`, +32,840.2 ns (now 1,127,275.1 ns), 1,048,527 B

### `wild-codegrammar-json-constant` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 716.4 | 713.9 | 728.8 | 6.4 | 1.000x | 1.000x | faster ×1.12 | -10.77% vs bar 8.81% (band) → **improve** | 75 | 9.6 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 802.9 | 794.9 | 814.7 | 6.7 | 1.121x | 1.121x | - | - | 75 | 10.7 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `sec-github-pat`, 100.1 ns, 93 B

### `wild-codegrammar-json-number-extended` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 5,574,774.1 | 0.9133 | 5,532,783.0 | 5,596,951.5 | 23,658.9 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 5,575,153.2 | 0.9134 | 5,535,641.1 | 5,623,534.4 | 37,483.7 | 1.000x | 1.000x | unchanged (within spread) | +0.01% (null control: program identical) |

#### `wild-codegrammar-json-number-extended` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 811,734.4 | 0.7741 |
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 806,378.3 | 0.7690 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 192,693.4 | 0.7351 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 193,341.4 | 0.7375 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 35,978.1 | 0.5490 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 35,724.2 | 0.5451 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 11,734.5 | 0.1910 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 11,650.5 | 0.1896 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3,114.6 | 0.1901 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,096.6 | 0.1890 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 35,433.5 | 2.1627 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 35,652.1 | 2.1760 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 9,363.3 | 2.2860 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 9,310.2 | 2.2730 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 575.0 | 0.5615 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 574.4 | 0.5609 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 40,100.5 | 0.6119 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 40,014.8 | 0.6106 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 4,872.5 | 0.5948 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 4,841.5 | 0.5910 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3,140.3 | 0.1917 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,132.5 | 0.1912 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 5,999.7 | 1.4648 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5,992.7 | 1.4631 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 2,183,087.9 | 2.0821 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2,180,291.6 | 2.0794 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 545,261.6 | 2.0804 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 547,487.6 | 2.0889 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 565,035.8 | 0.5389 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 567,817.8 | 0.5415 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 564,816.8 | 0.5387 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 559,072.2 | 0.5332 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 567,464.4 | 0.5412 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 559,253.4 | 0.5334 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 11,675.3 | 0.1900 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 11,605.7 | 0.1889 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3,117.7 | 0.1903 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,106.3 | 0.1896 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `t-qs-1m`, 2,180,291.6 ns, 1,048,501 B; largest Δ: `t-tail-txt-1m`, -8,211.0 ns (now 559,253.4 ns), 1,048,527 B

### `wild-codegrammar-json-number-extended` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 674.1 | 671.2 | 679.1 | 3.1 | 1.000x | 1.000x | - | - | 75 | 9.0 | 3.8 | 100% |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 680.4 | 679.5 | 686.5 | 2.6 | 1.009x | 1.009x | slower ×1.01 | +0.93% (null control: program identical) | 75 | 9.1 | 3.7 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `rd-numeric-id-near-miss`, 41.2 ns, 20 B; largest Δ: `br-doubled-word`, +0.6 ns (now 7.4 ns), 15 B

### `wild-codegrammar-json-object-begin` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 43,708.4 | 0.0072 | 43,232.3 | 44,055.6 | 344.9 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 44,170.3 | 0.0072 | 43,091.4 | 44,336.5 | 484.9 | 1.011x | 1.011x | unchanged (within spread) | +1.06% (null control: program identical) |

#### `wild-codegrammar-json-object-begin` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 7,610.6 | 0.0073 |
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,737.6 | 0.0074 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 1,579.7 | 0.0060 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,581.8 | 0.0060 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 400.4 | 0.0061 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 400.2 | 0.0061 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 374.6 | 0.0061 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 375.5 | 0.0061 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.2 | 0.0047 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.2 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 75.7 | 0.0046 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 75.7 | 0.0046 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 20.8 | 0.0051 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 21.0 | 0.0051 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 11.9 | 0.0116 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 11.9 | 0.0116 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 605.3 | 0.0092 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 604.6 | 0.0092 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 78.5 | 0.0096 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 79.1 | 0.0097 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 76.5 | 0.0047 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.7 | 0.0047 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 20.5 | 0.0050 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 20.6 | 0.0050 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7,607.2 | 0.0073 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,895.2 | 0.0075 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,578.0 | 0.0060 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,583.8 | 0.0060 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,587.7 | 0.0072 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,596.6 | 0.0072 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,629.6 | 0.0073 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,814.3 | 0.0075 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,745.1 | 0.0074 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,645.8 | 0.0073 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 374.4 | 0.0061 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 375.1 | 0.0061 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 75.9 | 0.0046 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.1 | 0.0046 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `t-qs-1m`, 7,895.2 ns, 1,048,501 B

### `wild-codegrammar-json-object-begin` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 284.5 | 280.2 | 292.3 | 4.6 | 1.000x | 1.000x | - | - | 75 | 3.8 | 3.8 | 100% |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 288.2 | 278.8 | 291.6 | 4.4 | 1.013x | 1.013x | unchanged (within spread) | +1.30% (null control: program identical) | 75 | 3.8 | 3.7 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `cg-object-begin`, 5.8 ns, 1 B; largest Δ: `cg-constant`, +0.2 ns (now 3.8 ns), 4 B

### `wild-codegrammar-json-stringcontent-escape` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 43,570.4 | 0.0071 | 42,895.0 | 43,918.5 | 395.2 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 43,800.4 | 0.0072 | 43,281.6 | 43,911.3 | 260.4 | 1.005x | 1.005x | unchanged (within spread) | +0.53% vs bar 12.76% (band) → **within** |

#### `wild-codegrammar-json-stringcontent-escape` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 7,591.7 | 0.0072 |
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,866.7 | 0.0075 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 1,579.8 | 0.0060 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,585.4 | 0.0060 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 401.5 | 0.0061 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 402.0 | 0.0061 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 376.1 | 0.0061 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 374.8 | 0.0061 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.7 | 0.0047 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.9 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 76.3 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 77.0 | 0.0047 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.2 | 0.0052 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 21.5 | 0.0053 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 8.0 | 0.0079 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 8.1 | 0.0079 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 400.2 | 0.0061 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 401.8 | 0.0061 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 40.3 | 0.0049 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 40.3 | 0.0049 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 76.8 | 0.0047 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 77.4 | 0.0047 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.3 | 0.0052 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 21.3 | 0.0052 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7,577.1 | 0.0072 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,520.2 | 0.0072 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,579.5 | 0.0060 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,584.0 | 0.0060 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,653.9 | 0.0073 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,573.3 | 0.0072 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,601.7 | 0.0072 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,940.8 | 0.0076 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,575.3 | 0.0072 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,584.6 | 0.0072 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 376.6 | 0.0061 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 374.8 | 0.0061 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.6 | 0.0047 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.3 | 0.0047 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `t-tail-space-1m`, 7,940.8 ns, 1,048,522 B

### `wild-codegrammar-json-stringcontent-escape` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 345.5 | 343.3 | 346.6 | 1.2 | 1.000x | 1.000x | - | - | 75 | 4.6 | 3.8 | 100% |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 346.9 | 342.7 | 348.3 | 1.9 | 1.004x | 1.004x | unchanged (within spread) | +0.41% vs bar 8.81% (band) → **within** | 75 | 4.6 | 3.7 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `lp-winpath-reserved`, 16.5 ns, 24 B; largest Δ: `floor-hit`, -2.0 ns (now 2.3 ns), 1 B

### `wild-datetime-datefinder-alternation` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 709,273,126.6 | 116.2022 | 674,907,000.6 | 722,441,578.5 | 15,823,475.3 | 1.000x | 1.000x |

#### `wild-datetime-datefinder-alternation` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 116,217,810.8 | 110.8339 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 29,205,896.2 | 111.4117 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,409,996.4 | 113.0676 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6,668,927.0 | 108.5437 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,772,519.9 | 108.1794 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,382,800.4 | 84.3994 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,720.8 | 0.4201 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 110,375.6 | 107.7887 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6,965,810.4 | 106.2898 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 857,378.6 | 104.6605 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2,276,692.8 | 138.9583 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 383,167.2 | 93.5467 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 106,395,251.6 | 101.4737 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 26,141,773.0 | 99.7427 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 133,884,424.4 | 127.6887 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 134,472,184.8 | 128.2493 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 134,078,089.4 | 127.8728 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 23,677.1 | 0.3854 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6,266.8 | 0.3825 |

- not ranked: `pcrec_cb32eda28_auto-caps-simdna` — did-not-compile (pcrec: pattern too large: 591151 bytes of emitted code (limit 500000), which gcc cannot compile in reasonable time. A repeat's body is replicated and counts MULTIPLY through nesting -- lower a count, try --unroll=1, or raise --max-emit-code-bytes (pattern offset 0))

### `wild-datetime-datefinder-alternation` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 57,422.9 | 55,905.1 | 60,305.3 | 1,479.4 | 1.000x | 1.000x | 75 | 765.6 | 3.7 | 100% |

- not ranked: `pcrec_cb32eda28_auto-caps-simdna` — did-not-compile (pcrec: pattern too large: 591151 bytes of emitted code (limit 500000), which gcc cannot compile in reasonable time. A repeat's body is replicated and counts MULTIPLY through nesting -- lower a count, try --unroll=1, or raise --max-emit-code-bytes (pattern offset 0))

### `wild-datetime-moment-iso8601` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 41,310.1 | 0.0068 | 40,893.9 | 41,373.5 | 220.5 | 1.000x | 1.000x | faster ×2.11 | -52.55% vs bar 12.76% (band) → **improve** |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 87,055.0 | 0.0143 | 86,846.8 | 87,227.0 | 126.3 | 2.107x | 2.107x | - | - |

#### `wild-datetime-moment-iso8601` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.6 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 5.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 5.5 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.6 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.6 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 6.0 | 0.0001 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.6 | 0.0003 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 5.9 | 0.0004 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 8.7 | 0.0005 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 8.0 | 0.0005 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 8.6 | 0.0021 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 8.0 | 0.0020 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.8 | 0.0056 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 6.3 | 0.0062 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.8 | 0.0001 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 6.3 | 0.0001 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.8 | 0.0007 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 6.3 | 0.0008 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.8 | 0.0004 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 6.3 | 0.0004 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 8.2 | 0.0020 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 8.1 | 0.0020 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.7 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 6.3 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.8 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 6.2 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.8 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 6.4 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.8 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 6.4 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.8 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 6.5 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 34,867.7 | 0.5675 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 68,566.5 | 1.1160 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6,285.6 | 0.3836 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 18,352.9 | 1.1201 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `t-trim-match-60k`, 34,867.7 ns, 61,440 B

### `wild-datetime-moment-iso8601` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 444.3 | 442.5 | 464.4 | 8.5 | 1.000x | 1.000x | faster ×1.22 | -17.79% vs bar 8.81% (band) → **improve** | 75 | 5.9 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 540.4 | 512.7 | 550.0 | 12.7 | 1.216x | 1.216x | - | - | 75 | 7.2 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `dt-iso8601`, 30.8 ns, 20 B; largest Δ: `rd-trim-near-miss`, -13.0 ns (now 14.0 ns), 20 B

### `wild-logparse-base10num-grok` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 9,810,282.2 | 1.6072 | 9,753,200.7 | 9,885,401.5 | 50,243.6 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 9,824,363.2 | 1.6096 | 9,796,746.5 | 9,978,283.8 | 71,440.0 | 1.001x | 1.001x | unchanged (within spread) | +0.14% (null control: program identical) |

#### `wild-logparse-base10num-grok` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 1,535,660.7 | 1.4645 |
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,541,278.9 | 1.4699 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 368,536.0 | 1.4059 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 373,149.1 | 1.4235 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 77,211.2 | 1.1782 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 78,055.2 | 1.1910 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 16,363.1 | 0.2663 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 16,538.9 | 0.2692 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 4,192.3 | 0.2559 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 4,207.7 | 0.2568 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 72,805.8 | 4.4437 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 73,869.6 | 4.5086 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 12,807.1 | 3.1267 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 13,056.9 | 3.1877 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 1,297.2 | 1.2668 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,321.8 | 1.2908 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 92,633.6 | 1.4135 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 91,897.7 | 1.4022 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 10,677.4 | 1.3034 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 10,651.1 | 1.3002 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 4,192.0 | 0.2559 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 4,252.4 | 0.2595 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 13,485.5 | 3.2923 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 13,436.7 | 3.2804 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 3,395,484.9 | 3.2384 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,390,892.8 | 3.2340 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 857,774.2 | 3.2728 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 851,244.1 | 3.2479 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 1,116,442.5 | 1.0648 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,122,607.4 | 1.0707 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 1,108,685.6 | 1.0574 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,115,486.3 | 1.0639 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 1,109,919.3 | 1.0586 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,120,583.1 | 1.0687 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 15,635.2 | 0.2545 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 15,734.9 | 0.2561 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 4,172.5 | 0.2547 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 4,199.3 | 0.2563 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `t-qs-1m`, 3,390,892.8 ns, 1,048,501 B; largest Δ: `t-tail-txt-1m`, +10,663.8 ns (now 1,120,583.1 ns), 1,048,527 B

### `wild-logparse-base10num-grok` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 1,193.5 | 1,189.4 | 1,196.7 | 2.4 | 1.000x | 1.000x | unchanged (within spread) | -0.28% (null control: program identical) | 75 | 15.9 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 1,196.8 | 1,193.5 | 1,202.2 | 2.8 | 1.003x | 1.003x | - | - | 75 | 16.0 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `rd-numeric-id-near-miss`, 59.4 ns, 20 B; largest Δ: `sec-github-pat`, -2.1 ns (now 29.4 ns), 93 B

### `wild-logparse-base10num-noatomic` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 7,496,848.4 | 1.2282 | 7,452,504.5 | 7,592,213.6 | 51,720.5 | 1.000x | 1.000x | unchanged (within spread) | -0.28% (null control: program identical) |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 7,518,198.7 | 1.2317 | 7,443,785.2 | 7,545,831.1 | 35,124.9 | 1.003x | 1.003x | - | - |

#### `wild-logparse-base10num-noatomic` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,144,857.0 | 1.0918 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 1,140,932.5 | 1.0881 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 272,308.7 | 1.0388 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 273,552.3 | 1.0435 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 52,322.4 | 0.7984 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 51,692.6 | 0.7888 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 16,512.3 | 0.2688 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 17,696.5 | 0.2880 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 4,193.5 | 0.2559 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 4,174.0 | 0.2547 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 42,421.9 | 2.5892 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 42,818.6 | 2.6134 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 11,560.6 | 2.8224 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 11,702.7 | 2.8571 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 818.4 | 0.7992 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 821.5 | 0.8023 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 56,539.0 | 0.8627 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 57,728.3 | 0.8809 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6,815.7 | 0.8320 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 7,170.2 | 0.8753 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 4,177.7 | 0.2550 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 4,292.8 | 0.2620 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 8,179.1 | 1.9968 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 8,328.5 | 2.0333 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2,491,685.1 | 2.3764 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 2,508,401.6 | 2.3924 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 621,727.3 | 2.3722 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 631,532.5 | 2.4096 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 918,803.1 | 0.8763 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 917,759.9 | 0.8753 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 914,132.8 | 0.8718 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 917,691.8 | 0.8752 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 913,745.8 | 0.8715 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 914,236.0 | 0.8719 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 15,714.1 | 0.2558 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 15,637.1 | 0.2545 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 4,210.0 | 0.2569 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 4,175.4 | 0.2548 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `t-qs-1m`, 2,491,685.1 ns, 1,048,501 B

### `wild-logparse-base10num-noatomic` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 850.3 | 847.6 | 854.1 | 2.2 | 1.000x | 1.000x | - | - | 75 | 11.3 | 3.8 | 100% |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 851.9 | 851.3 | 853.8 | 0.9 | 1.002x | 1.002x | unchanged (within spread) | +0.19% (null control: program identical) | 75 | 11.4 | 3.7 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `rd-numeric-id-near-miss`, 52.0 ns, 20 B; largest Δ: `lp-winpath`, +0.6 ns (now 12.2 ns), 22 B

### `wild-logparse-quotedstring-grok` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 1,418,766.7 | 0.2324 | 1,396,553.0 | 1,421,346.8 | 9,377.6 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 1,419,799.9 | 0.2326 | 1,418,515.2 | 1,456,444.6 | 14,627.5 | 1.001x | 1.001x | unchanged (within spread) | +0.07% vs bar 12.76% (band) → **within** |

#### `wild-logparse-quotedstring-grok` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 354,017.1 | 0.3376 |
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 358,871.1 | 0.3422 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 87,671.2 | 0.3344 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 87,408.8 | 0.3334 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 21,552.1 | 0.3289 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 21,673.2 | 0.3307 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 13,424.4 | 0.2185 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 11,898.6 | 0.1937 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3,144.2 | 0.1919 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,177.9 | 0.1940 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3,113.6 | 0.1900 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,171.0 | 0.1935 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 787.9 | 0.1924 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 800.3 | 0.1954 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 685.3 | 0.6693 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 551.3 | 0.5384 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 33,438.8 | 0.5102 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 34,590.9 | 0.5278 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 4,547.2 | 0.5551 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 4,598.0 | 0.5613 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3,177.1 | 0.1939 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,186.1 | 0.1945 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 784.2 | 0.1914 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 807.1 | 0.1971 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 204,365.8 | 0.1949 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 205,674.7 | 0.1962 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 50,241.7 | 0.1917 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 50,847.4 | 0.1940 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 204,489.3 | 0.1950 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 206,678.9 | 0.1971 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 202,106.0 | 0.1928 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 205,962.3 | 0.1964 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 202,627.7 | 0.1932 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 204,548.5 | 0.1951 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 11,994.5 | 0.1952 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 11,886.4 | 0.1935 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3,112.0 | 0.1899 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,181.5 | 0.1942 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 358,871.1 ns, 1,048,576 B

### `wild-logparse-quotedstring-grok` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 946.0 | 935.4 | 950.0 | 5.0 | 1.000x | 1.000x | faster ×1.01 | -1.17% vs bar 8.81% (band) → **within** | 75 | 12.6 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 957.1 | 954.9 | 960.2 | 2.2 | 1.012x | 1.012x | - | - | 75 | 12.8 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `lp-quoted-escaped`, 60.6 ns, 16 B; largest Δ: `sec-github-pat`, +3.7 ns (now 29.2 ns), 93 B

### `wild-logparse-quotedstring-noatomic` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 1,302,709.8 | 0.2134 | 1,296,947.9 | 1,393,741.2 | 36,257.1 | 1.000x | 1.000x | unchanged (within spread) | -1.18% vs bar 12.76% (band) → **within** |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 1,318,229.2 | 0.2160 | 1,302,072.6 | 1,324,683.8 | 8,130.1 | 1.012x | 1.012x | - | - |

#### `wild-logparse-quotedstring-noatomic` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 289,085.8 | 0.2757 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 292,880.6 | 0.2793 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 74,954.3 | 0.2859 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 71,425.6 | 0.2725 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 17,486.3 | 0.2668 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 18,034.2 | 0.2752 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 12,755.8 | 0.2076 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 11,895.8 | 0.1936 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,094.4 | 0.1889 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3,152.0 | 0.1924 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,105.7 | 0.1896 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3,172.0 | 0.1936 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 778.2 | 0.1900 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 801.4 | 0.1957 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 353.0 | 0.3447 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 351.4 | 0.3432 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 22,670.0 | 0.3459 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 23,155.3 | 0.3533 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2,862.1 | 0.3494 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 2,890.1 | 0.3528 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,107.8 | 0.1897 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3,245.1 | 0.1981 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 789.2 | 0.1927 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 793.5 | 0.1937 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 202,745.2 | 0.1934 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 203,759.4 | 0.1943 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 50,528.6 | 0.1928 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 50,617.6 | 0.1931 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 202,784.1 | 0.1934 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 205,391.4 | 0.1959 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 202,661.3 | 0.1933 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 202,406.9 | 0.1930 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 202,773.4 | 0.1934 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 205,424.8 | 0.1959 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 11,917.6 | 0.1940 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 11,861.8 | 0.1931 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,092.4 | 0.1887 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3,150.0 | 0.1923 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 289,085.8 ns, 1,048,576 B

### `wild-logparse-quotedstring-noatomic` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 621.3 | 618.2 | 638.1 | 7.2 | 1.000x | 1.000x | faster ×1.12 | -11.03% vs bar 8.81% (band) → **improve** | 75 | 8.3 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 698.3 | 691.0 | 700.8 | 3.8 | 1.124x | 1.124x | - | - | 75 | 9.3 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `lp-quoted-escaped`, 29.4 ns, 16 B; largest Δ: `sd-empty-alt-miss`, -3.2 ns (now 16.5 ns), 60 B

### `wild-logparse-syslogbase-expanded` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 152,036.2 | 0.0249 | 151,432.1 | 152,188.3 | 261.1 | 1.000x | 1.000x | faster ×14.44 | -93.08% vs bar 12.76% (band) → **improve** |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 2,195,937.5 | 0.3598 | 2,193,073.6 | 2,214,465.5 | 7,702.6 | 14.444x | 14.444x | - | - |

#### `wild-logparse-syslogbase-expanded` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 41,154.6 | 0.0392 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 1,646,810.5 | 1.5705 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 9,998.3 | 0.0381 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 402,100.6 | 1.5339 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2,520.0 | 0.0385 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 36,608.6 | 0.5586 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 381.9 | 0.0062 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 373.4 | 0.0061 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.8 | 0.0047 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 75.5 | 0.0046 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.6 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 76.7 | 0.0047 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 22.1 | 0.0054 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.6 | 0.0053 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 386.9 | 0.3778 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 993.1 | 0.9699 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 58,160.8 | 0.8875 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 56,767.7 | 0.8662 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6,596.0 | 0.8052 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 7,028.0 | 0.8579 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 80.2 | 0.0049 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 10,747.5 | 0.6560 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 67.0 | 0.0164 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 2,588.0 | 0.6318 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,596.7 | 0.0072 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7,623.0 | 0.0073 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,596.6 | 0.0061 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,579.4 | 0.0060 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,671.5 | 0.0073 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,522.8 | 0.0072 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,635.6 | 0.0073 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,603.2 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,621.7 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,565.7 | 0.0072 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 380.5 | 0.0062 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 373.5 | 0.0061 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.3 | 0.0047 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 75.6 | 0.0046 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `t-hyb-embed-64k`, 58,160.8 ns, 65,536 B; largest Δ: `t-1m`, -1,605,655.9 ns (now 41,154.6 ns), 1,048,576 B

### `wild-logparse-syslogbase-expanded` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 568.7 | 564.2 | 578.0 | 5.1 | 1.000x | 1.000x | faster ×1.30 | -23.01% vs bar 8.81% (band) → **improve** | 75 | 7.6 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 738.7 | 732.2 | 790.2 | 21.6 | 1.299x | 1.299x | - | - | 75 | 9.8 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `lp-syslog`, 220.1 ns, 56 B; largest Δ: `sec-slack-webhook`, -50.6 ns (now 7.5 ns), 81 B

### `wild-logparse-winpath-grok` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 43,408.0 | 0.0071 | 43,056.4 | 44,182.8 | 459.2 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 43,581.6 | 0.0071 | 42,903.1 | 43,830.5 | 315.8 | 1.004x | 1.004x | unchanged (within spread) | +0.40% vs bar 12.76% (band) → **within** |

#### `wild-logparse-winpath-grok` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 7,555.8 | 0.0072 |
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,610.0 | 0.0073 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 1,572.9 | 0.0060 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,587.2 | 0.0061 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 403.2 | 0.0062 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 403.4 | 0.0062 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 378.8 | 0.0062 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 378.6 | 0.0062 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.9 | 0.0047 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 77.0 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 77.3 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 77.3 | 0.0047 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.2 | 0.0052 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 21.2 | 0.0052 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 8.8 | 0.0086 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 9.0 | 0.0088 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 403.6 | 0.0062 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 404.2 | 0.0062 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 39.7 | 0.0048 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 39.9 | 0.0049 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 77.2 | 0.0047 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 77.3 | 0.0047 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.2 | 0.0052 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 21.4 | 0.0052 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7,557.6 | 0.0072 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,841.5 | 0.0075 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,582.8 | 0.0060 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,587.7 | 0.0061 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,699.0 | 0.0073 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,650.6 | 0.0073 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,850.0 | 0.0075 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,794.0 | 0.0074 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,607.2 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,601.1 | 0.0072 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 378.1 | 0.0062 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 379.3 | 0.0062 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.5 | 0.0047 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.9 | 0.0047 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `t-qs-1m`, 7,841.5 ns, 1,048,501 B

### `wild-logparse-winpath-grok` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 459.2 | 456.4 | 463.8 | 2.6 | 1.000x | 1.000x | faster ×1.06 | -5.96% vs bar 8.81% (band) → **within** | 75 | 6.1 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 488.3 | 485.3 | 491.6 | 2.4 | 1.063x | 1.063x | - | - | 75 | 6.5 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `lp-winpath-reserved`, 40.3 ns, 24 B; largest Δ: `cg-object-begin`, -1.4 ns (now 4.0 ns), 1 B

### `wild-secrets-aws-access-key-id` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 74,141.1 | 0.0121 | 73,919.7 | 74,493.6 | 206.7 | 1.000x | 1.000x | faster ×1.17 | -14.71% vs bar 12.76% (band) → **improve** |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 86,933.2 | 0.0142 | 86,276.7 | 87,170.1 | 352.4 | 1.173x | 1.173x | - | - |

#### `wild-secrets-aws-access-key-id` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 15,001.3 | 0.0143 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 16,841.3 | 0.0161 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,461.0 | 0.0132 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 3,970.3 | 0.0151 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 857.6 | 0.0131 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 967.3 | 0.0148 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 382.7 | 0.0062 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 387.0 | 0.0063 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.6 | 0.0047 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.8 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 77.2 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 77.2 | 0.0047 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 21.3 | 0.0052 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 22.0 | 0.0054 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 59.3 | 0.0579 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 111.3 | 0.1087 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 4,518.1 | 0.0689 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 7,441.3 | 0.1135 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 726.9 | 0.0887 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 970.0 | 0.1184 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 77.6 | 0.0047 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 77.9 | 0.0048 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 21.5 | 0.0052 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 22.2 | 0.0054 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 13,266.6 | 0.0127 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 18,036.1 | 0.0172 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2,969.1 | 0.0113 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 4,209.7 | 0.0161 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 10,682.8 | 0.0102 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 11,064.1 | 0.0106 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 10,764.7 | 0.0103 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 10,949.5 | 0.0104 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 10,615.7 | 0.0101 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 11,010.2 | 0.0105 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 380.3 | 0.0062 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 381.7 | 0.0062 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.2 | 0.0046 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.9 | 0.0047 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `t-1m`, 15,001.3 ns, 1,048,576 B; largest Δ: `t-qs-1m`, -4,769.5 ns (now 13,266.6 ns), 1,048,501 B

### `wild-secrets-aws-access-key-id` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 514.1 | 507.4 | 516.1 | 3.4 | 1.000x | 1.000x | faster ×1.22 | -18.31% vs bar 8.81% (band) → **improve** | 75 | 6.9 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 629.3 | 618.6 | 634.6 | 5.3 | 1.224x | 1.224x | - | - | 75 | 8.4 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `sec-github-pat`, 145.1 ns, 93 B

### `wild-secrets-github-pat` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 352,875.2 | 0.0578 | 349,024.2 | 360,079.2 | 3,738.8 | 1.000x | 1.000x | faster ×1.03 | -3.33% vs bar 12.76% (band) → **within** |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 365,023.9 | 0.0598 | 362,943.4 | 365,487.6 | 1,068.8 | 1.034x | 1.034x | - | - |

#### `wild-secrets-github-pat` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 29,856.8 | 0.0285 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 30,191.4 | 0.0288 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,141.9 | 0.0272 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 7,193.1 | 0.0274 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,720.8 | 0.0263 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 1,736.9 | 0.0265 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 379.6 | 0.0062 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 378.5 | 0.0062 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.9 | 0.0047 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 75.8 | 0.0046 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.4 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 75.7 | 0.0046 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 21.1 | 0.0052 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.0 | 0.0051 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 375.0 | 0.3662 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 378.6 | 0.3697 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 13,210.3 | 0.2016 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 13,245.8 | 0.2021 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,669.5 | 0.2038 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 1,687.7 | 0.2060 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.4 | 0.0047 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 76.6 | 0.0047 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 83.1 | 0.0203 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 84.0 | 0.0205 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 222,498.4 | 0.2122 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 230,736.0 | 0.2201 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 53,019.6 | 0.2023 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 55,229.1 | 0.2107 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,561.7 | 0.0072 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,686.5 | 0.0073 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,652.0 | 0.0073 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,555.3 | 0.0072 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,652.1 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,544.8 | 0.0072 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 381.7 | 0.0062 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 378.8 | 0.0062 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 75.6 | 0.0046 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 75.8 | 0.0046 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `t-qs-1m`, 222,498.4 ns, 1,048,501 B

### `wild-secrets-github-pat` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 367.3 | 363.2 | 368.3 | 1.9 | 1.000x | 1.000x | faster ×1.22 | -17.86% vs bar 8.81% (band) → **improve** | 75 | 4.9 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 447.1 | 442.7 | 454.2 | 4.0 | 1.217x | 1.217x | - | - | 75 | 6.0 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `sec-github-pat`, 167.2 ns, 93 B; largest Δ: `waf-dbnames`, -3.1 ns (now 2.7 ns), 39 B

### `wild-secrets-slack-webhook-url` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 219,918.3 | 0.0360 | 218,165.9 | 220,595.0 | 1,027.2 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 253,566.9 | 0.0415 | 248,174.1 | 255,594.3 | 2,653.3 | 1.153x | 1.153x | slower ×1.15 | +15.30% vs bar 12.76% (band) → **regress** |

#### `wild-secrets-slack-webhook-url` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 117,036.7 | 0.1116 |
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 151,823.3 | 0.1448 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 28,756.9 | 0.1097 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 28,019.1 | 0.1069 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 6,772.4 | 0.1033 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6,604.4 | 0.1008 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 379.0 | 0.0062 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 378.3 | 0.0062 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.3 | 0.0047 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 75.8 | 0.0046 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 13,083.1 | 0.7985 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 12,947.6 | 0.7903 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 20.7 | 0.0050 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 20.6 | 0.0050 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 358.5 | 0.3501 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 367.2 | 0.3586 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 18,402.6 | 0.2808 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 18,358.9 | 0.2801 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 2,469.2 | 0.3014 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2,484.4 | 0.3033 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 77.7 | 0.0047 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.5 | 0.0047 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 123.4 | 0.0301 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 128.7 | 0.0314 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7,611.7 | 0.0073 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,522.6 | 0.0072 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,580.1 | 0.0060 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,586.9 | 0.0061 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,586.8 | 0.0072 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,625.9 | 0.0073 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,522.6 | 0.0072 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,619.7 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,602.5 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,669.6 | 0.0073 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 379.5 | 0.0062 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 378.8 | 0.0062 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.2 | 0.0046 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 75.5 | 0.0046 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 151,823.3 ns, 1,048,576 B

### `wild-secrets-slack-webhook-url` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 521.2 | 514.7 | 527.1 | 5.1 | 1.000x | 1.000x | faster ×1.17 | -14.59% vs bar 8.81% (band) → **improve** | 75 | 6.9 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 610.2 | 606.3 | 623.2 | 5.8 | 1.171x | 1.171x | - | - | 75 | 8.1 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `sec-slack-webhook`, 238.8 ns, 81 B; largest Δ: `rec-tag-depth3`, -5.6 ns (now 3.9 ns), 22 B

### `wild-secrets-username-password-pair` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 171,731.6 | 0.0281 | 169,392.1 | 172,337.6 | 1,076.6 | 1.000x | 1.000x | faster ×1.84 | -45.79% vs bar 12.76% (band) → **improve** |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 316,816.9 | 0.0519 | 313,604.6 | 325,438.3 | 4,140.5 | 1.845x | 1.845x | - | - |

#### `wild-secrets-username-password-pair` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,536.4 | 0.0072 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 7,612.1 | 0.0073 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,578.8 | 0.0060 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 1,583.1 | 0.0060 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 404.5 | 0.0062 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 399.7 | 0.0061 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 379.1 | 0.0062 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 377.9 | 0.0062 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.8 | 0.0047 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.9 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.9 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 76.2 | 0.0047 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 21.6 | 0.0053 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.9 | 0.0054 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 354.0 | 0.3457 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 369.7 | 0.3610 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 33,668.2 | 0.5137 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 20,259.3 | 0.3091 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,622.5 | 0.4422 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 2,250.1 | 0.2747 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 77.1 | 0.0047 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 78.1 | 0.0048 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 303.0 | 0.0740 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 294.1 | 0.0718 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 80,443.1 | 0.0767 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 228,450.2 | 0.2179 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 19,937.3 | 0.0761 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 32,032.4 | 0.1222 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,577.2 | 0.0072 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,579.1 | 0.0072 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,595.1 | 0.0072 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,595.3 | 0.0072 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,657.4 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,535.9 | 0.0072 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 378.9 | 0.0062 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 379.5 | 0.0062 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.7 | 0.0047 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.7 | 0.0047 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `t-qs-1m`, 80,443.1 ns, 1,048,501 B

### `wild-secrets-username-password-pair` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 476.3 | 473.5 | 477.9 | 1.5 | 1.000x | 1.000x | faster ×1.11 | -9.71% vs bar 8.81% (band) → **improve** | 75 | 6.4 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 527.5 | 526.2 | 530.5 | 1.7 | 1.108x | 1.108x | - | - | 75 | 7.0 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `sec-userpass`, 131.5 ns, 33 B; largest Δ: `la-float-bound`, -6.1 ns (now 4.3 ns), 13 B

### `wild-semdiv-altorder-foo-foobar-rustregex` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 504,755.3 | 0.0827 | 503,984.7 | 512,151.4 | 3,195.5 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 508,231.0 | 0.0833 | 502,999.6 | 511,254.2 | 3,305.0 | 1.007x | 1.007x | unchanged (within spread) | +0.69% (null control: program identical) |

#### `wild-semdiv-altorder-foo-foobar-rustregex` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 74,308.3 | 0.0709 |
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 74,571.9 | 0.0711 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 18,734.6 | 0.0715 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 18,817.2 | 0.0718 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 4,830.7 | 0.0737 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 4,865.8 | 0.0742 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 8,512.0 | 0.1385 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 8,537.9 | 0.1390 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 2,301.1 | 0.1404 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2,296.0 | 0.1401 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 76.0 | 0.0046 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 75.6 | 0.0046 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 20.5 | 0.0050 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 20.4 | 0.0050 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 55.4 | 0.0541 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 55.1 | 0.0538 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 3,869.9 | 0.0591 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,850.0 | 0.0587 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 533.6 | 0.0651 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 532.7 | 0.0650 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 1,508.5 | 0.0921 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,508.8 | 0.0921 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 493.3 | 0.1204 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 494.6 | 0.1208 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 108,200.2 | 0.1032 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 108,413.9 | 0.1034 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 25,387.0 | 0.0969 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 25,387.3 | 0.0969 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 86,169.0 | 0.0822 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 86,172.0 | 0.0822 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 85,147.9 | 0.0812 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 85,635.1 | 0.0817 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 85,246.4 | 0.0813 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 85,560.8 | 0.0816 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 370.0 | 0.0060 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 375.6 | 0.0061 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 75.9 | 0.0046 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 75.8 | 0.0046 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `t-qs-1m`, 108,413.9 ns, 1,048,501 B; largest Δ: `t-tail-space-1m`, +487.3 ns (now 85,635.1 ns), 1,048,522 B

### `wild-semdiv-altorder-foo-foobar-rustregex` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 290.7 | 285.4 | 305.1 | 7.5 | 1.000x | 1.000x | - | - | 75 | 3.9 | 3.8 | 100% |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 300.9 | 289.8 | 304.0 | 5.2 | 1.035x | 1.035x | unchanged (within spread) | +3.49% (null control: program identical) | 75 | 4.0 | 3.7 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `sec-slack-webhook`, 5.9 ns, 81 B; largest Δ: `nu-high-byte`, +0.2 ns (now 3.8 ns), 2 B

### `wild-semdiv-dollar-trailing-newline-pcre2` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 59.5 | 0.0000 | 59.5 | 59.7 | 0.1 | 1.000x | 1.000x | faster ×1.01 | -0.78% (null control: program identical) |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 60.0 | 0.0000 | 59.9 | 60.3 | 0.1 | 1.008x | 1.008x | - | - |

#### `wild-semdiv-dollar-trailing-newline-pcre2` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 3.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.2 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 3.3 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.2 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 3.0 | 0.0000 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 3.3 | 0.0001 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3.2 | 0.0002 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0008 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0008 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0030 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0030 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0004 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0004 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0008 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0008 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.3 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 3.3 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.3 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 3.3 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.1 | 0.0002 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3.1 | 0.0002 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `t-qs-nearmiss-256k`, 3.3 ns, 262,092 B; largest Δ: `t-1m`, -0.2 ns (now 3.1 ns), 1,048,576 B

### `wild-semdiv-dollar-trailing-newline-pcre2` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 229.3 | 228.4 | 235.8 | 3.3 | 1.000x | 1.000x | - | - | 75 | 3.1 | 3.8 | 100% |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 230.5 | 229.2 | 232.9 | 1.6 | 1.005x | 1.005x | unchanged (within spread) | +0.51% (null control: program identical) | 75 | 3.1 | 3.7 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `rec-parens-unbalanced`, 3.7 ns, 5 B; largest Δ: `sd-empty-alt-hit`, +0.0 ns (now 3.1 ns), 61 B

### `wild-semdiv-empty-alt-repeat-pcre2` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 14,970,475.9 | 2.4527 | 14,911,875.4 | 15,123,574.9 | 81,493.0 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 14,981,393.1 | 2.4544 | 14,949,803.7 | 15,012,268.1 | 21,106.4 | 1.001x | 1.001x | unchanged (within spread) | +0.07% (null control: program identical) |

#### `wild-semdiv-empty-alt-repeat-pcre2` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 2,291,338.3 | 2.1852 |
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2,306,445.3 | 2.1996 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 558,037.7 | 2.1287 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 555,564.5 | 2.1193 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 127,374.7 | 1.9436 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 128,718.9 | 1.9641 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 23,272.3 | 0.3788 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 12,330.0 | 0.2007 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3,125.4 | 0.1907 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5,361.8 | 0.3272 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 181,279.6 | 11.0644 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 181,614.3 | 11.0849 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 57,459.6 | 14.0282 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 57,070.0 | 13.9331 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 1,793.5 | 1.7515 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,781.7 | 1.7399 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 138,580.8 | 2.1146 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 135,699.3 | 2.0706 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 16,316.3 | 1.9917 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 16,249.6 | 1.9836 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 4,422.4 | 0.2699 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,212.9 | 0.1961 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 27,508.8 | 6.7160 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 27,568.4 | 6.7306 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 4,943,654.9 | 4.7150 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 4,947,113.5 | 4.7183 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,248,014.4 | 4.7617 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,250,221.6 | 4.7702 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 1,786,748.9 | 1.7041 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,775,080.3 | 1.6929 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 1,788,208.8 | 1.7055 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,772,895.2 | 1.6909 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 1,783,082.9 | 1.7006 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,778,440.7 | 1.6961 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 11,901.6 | 0.1937 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 12,087.8 | 0.1967 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3,126.6 | 0.1908 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,184.5 | 0.1944 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `t-qs-1m`, 4,947,113.5 ns, 1,048,501 B; largest Δ: `t-tail-space-1m`, -15,313.7 ns (now 1,772,895.2 ns), 1,048,522 B

### `wild-semdiv-empty-alt-repeat-pcre2` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 1,396.6 | 1,393.8 | 1,422.6 | 10.8 | 1.000x | 1.000x | - | - | 75 | 18.6 | 3.8 | 100% |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 1,398.3 | 1,393.4 | 1,435.3 | 17.9 | 1.001x | 1.001x | unchanged (within spread) | +0.12% (null control: program identical) | 75 | 18.6 | 3.7 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `sd-empty-alt-hit`, 460.4 ns, 61 B

### `wild-validator-email-owasp` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 31,216.6 | 0.0051 | 31,149.7 | 31,397.2 | 86.4 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 31,318.3 | 0.0051 | 31,179.8 | 31,413.7 | 76.3 | 1.003x | 1.003x | unchanged (within spread) | +0.33% (null control: program identical) |

#### `wild-validator-email-owasp` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 6.9 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 5.5 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.5 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 6.1 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.1 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 23,271.1 | 0.3788 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 23,364.2 | 0.3803 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 6,234.0 | 0.3805 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6,186.7 | 0.3776 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 6.0 | 0.0004 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.9 | 0.0004 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 1,556.3 | 0.3799 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,549.6 | 0.3783 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 30.3 | 0.0296 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 30.0 | 0.0293 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 29.1 | 0.0004 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 29.5 | 0.0005 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 30.3 | 0.0037 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 30.8 | 0.0038 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 8.6 | 0.0005 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 8.6 | 0.0005 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 4.0 | 0.0010 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 4.0 | 0.0010 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 8.8 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 8.4 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 7.1 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7.0 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 6.6 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.7 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 6.8 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.7 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 6.6 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6.7 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 3.9 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.9 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 4.0 | 0.0002 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 4.0 | 0.0002 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `t-evil-match-60k`, 23,364.2 ns, 61,440 B

### `wild-validator-email-owasp` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 532.5 | 519.5 | 562.5 | 16.6 | 1.000x | 1.000x | - | - | 75 | 7.1 | 3.8 | 100% |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 552.8 | 527.7 | 558.3 | 10.8 | 1.038x | 1.038x | unchanged (within spread) | +3.82% (null control: program identical) | 75 | 7.4 | 3.7 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `sec-github-pat`, 39.4 ns, 93 B; largest Δ: `lp-winpath`, +0.7 ns (now 4.9 ns), 22 B

### `wild-validator-ipv4-owasp` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 95.6 | 0.0000 | 95.6 | 96.6 | 0.4 | 1.000x | 1.000x | faster ×1.09 | -8.07% vs bar 1.49% (IQR-only) → **improve (IQR only: band n=2 < 10)** |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 104.0 | 0.0000 | 101.7 | 105.3 | 1.3 | 1.088x | 1.088x | - | - |

#### `wild-validator-ipv4-owasp` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 5.6 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 5.5 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.1 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.0 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 5.5 | 0.0001 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.0 | 0.0003 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 5.4 | 0.0003 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.0 | 0.0003 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 5.5 | 0.0003 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.0 | 0.0012 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 5.5 | 0.0013 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.0 | 0.0049 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 5.6 | 0.0055 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.0 | 0.0001 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 5.5 | 0.0001 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.0 | 0.0006 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 5.5 | 0.0007 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.0 | 0.0003 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 5.3 | 0.0003 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.0 | 0.0012 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 5.5 | 0.0013 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 5.5 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 5.3 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 5.5 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 5.3 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 5.5 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.0 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 5.6 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.0 | 0.0003 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 5.6 | 0.0003 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `t-64k`, 5.1 ns, 65,536 B; largest Δ: `t-trim-match-60k`, -0.6 ns (now 5.0 ns), 61,440 B

### `wild-validator-ipv4-owasp` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 416.0 | 414.3 | 428.1 | 6.3 | 1.000x | 1.000x | faster ×1.11 | -10.24% vs bar 8.81% (band) → **improve** | 75 | 5.5 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 463.5 | 449.2 | 472.2 | 9.3 | 1.114x | 1.114x | - | - | 75 | 6.2 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `v-ipv4`, 31.0 ns, 11 B; largest Δ: `v-us-zip`, -3.4 ns (now 4.1 ns), 5 B

### `wild-validator-us-zip-owasp` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 95.8 | 0.0000 | 95.4 | 95.9 | 0.2 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 96.2 | 0.0000 | 96.2 | 96.9 | 0.3 | 1.005x | 1.005x | unchanged (within spread) | +0.48% vs bar 0.06% (IQR-only) → **regress (IQR only: band n=6 < 10)** |

#### `wild-validator-us-zip-owasp` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 5.1 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.1 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 5.0 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.1 | 0.0001 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 5.0 | 0.0003 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.1 | 0.0003 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 5.1 | 0.0003 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.1 | 0.0003 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 5.1 | 0.0012 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.1 | 0.0012 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 5.0 | 0.0049 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.1 | 0.0050 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 5.1 | 0.0001 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.1 | 0.0001 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 5.0 | 0.0006 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.1 | 0.0006 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 5.0 | 0.0003 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.1 | 0.0003 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 5.0 | 0.0012 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.1 | 0.0012 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.1 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.1 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.1 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.1 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.1 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 5.0 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.0 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 5.0 | 0.0003 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 5.1 | 0.0003 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `t-64k`, 5.1 ns, 65,536 B; largest Δ: `t-qs-1m`, +0.1 ns (now 5.1 ns), 1,048,501 B

### `wild-validator-us-zip-owasp` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 415.8 | 412.4 | 420.2 | 2.5 | 1.000x | 1.000x | faster ×1.08 | -7.83% vs bar 8.81% (band) → **within** | 75 | 5.5 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 451.1 | 428.0 | 454.5 | 11.9 | 1.085x | 1.085x | - | - | 75 | 6.0 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `v-us-zip-plus4`, 16.2 ns, 10 B; largest Δ: `lp-num-leadzero`, -4.3 ns (now 4.0 ns), 4 B

### `wild-validator-uuid-grok` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 63,355.0 | 0.0104 | 63,144.2 | 63,549.1 | 128.9 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 63,754.5 | 0.0104 | 63,296.6 | 64,849.3 | 622.9 | 1.006x | 1.006x | unchanged (within spread) | +0.63% vs bar 12.76% (band) → **within** |

#### `wild-validator-uuid-grok` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 19,326.1 | 0.0184 |
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 19,474.3 | 0.0186 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 4,485.6 | 0.0171 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 4,492.1 | 0.0171 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 1,177.1 | 0.0180 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,188.4 | 0.0181 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 381.2 | 0.0062 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 383.0 | 0.0062 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 75.7 | 0.0046 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.5 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 4,066.9 | 0.2482 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 4,143.6 | 0.2529 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 20.4 | 0.0050 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 20.8 | 0.0051 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 8.0 | 0.0078 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7.8 | 0.0077 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 984.2 | 0.0150 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,000.8 | 0.0153 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 116.3 | 0.0142 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 119.0 | 0.0145 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 75.5 | 0.0046 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.7 | 0.0047 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 240.3 | 0.0587 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 235.5 | 0.0575 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7,543.6 | 0.0072 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,611.2 | 0.0073 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,583.1 | 0.0060 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,581.3 | 0.0060 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,467.9 | 0.0071 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,579.9 | 0.0072 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,649.7 | 0.0073 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,630.0 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,551.8 | 0.0072 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,686.0 | 0.0073 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 377.8 | 0.0061 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 379.8 | 0.0062 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.0 | 0.0046 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.1 | 0.0046 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 19,474.3 ns, 1,048,576 B

### `wild-validator-uuid-grok` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 259.3 | 258.3 | 262.0 | 1.3 | 1.000x | 1.000x | faster ×1.22 | -18.13% vs bar 8.81% (band) → **improve** | 75 | 3.5 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 316.7 | 315.4 | 320.2 | 1.7 | 1.221x | 1.221x | - | - | 75 | 4.2 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `v-uuid-badnibble`, 30.6 ns, 36 B

### `wild-waf-crs-942140-dbnames` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 9,176,841.6 | 1.5035 | 9,124,069.7 | 9,210,030.3 | 32,593.5 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 9,185,510.6 | 1.5049 | 9,042,217.4 | 9,193,521.0 | 69,423.5 | 1.001x | 1.001x | unchanged (within spread) | +0.09% vs bar 12.76% (band) → **within** |

#### `wild-waf-crs-942140-dbnames` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 1,510,700.0 | 1.4407 |
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,524,985.4 | 1.4543 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 370,707.8 | 1.4141 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 370,830.2 | 1.4146 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 34,991.9 | 0.5339 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 34,367.2 | 0.5244 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 71,322.4 | 1.1608 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 69,861.3 | 1.1371 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 18,947.7 | 1.1564 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 18,599.1 | 1.1351 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 4,687.9 | 0.2861 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6,206.2 | 0.3788 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 789.5 | 0.1928 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,544.6 | 0.3771 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 686.3 | 0.6703 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 667.5 | 0.6518 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 40,150.6 | 0.6126 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 38,881.7 | 0.5933 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 4,915.4 | 0.6000 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 4,810.3 | 0.5872 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 9,578.6 | 0.5846 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 9,287.2 | 0.5668 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 2,172.3 | 0.5304 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2,150.4 | 0.5250 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 1,852,812.3 | 1.7671 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,830,983.2 | 1.7463 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 450,744.7 | 1.7198 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 445,764.7 | 1.7008 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 1,602,679.4 | 1.5285 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,599,860.4 | 1.5258 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 1,591,051.2 | 1.5174 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,598,106.1 | 1.5242 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 1,596,262.7 | 1.5224 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,599,063.8 | 1.5251 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 14,076.9 | 0.2291 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 22,974.5 | 0.3739 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3,104.4 | 0.1895 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 6,128.2 | 0.3740 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `t-qs-1m`, 1,830,983.2 ns, 1,048,501 B

### `wild-waf-crs-942140-dbnames` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 945.8 | 937.5 | 1,202.1 | 103.4 | 1.000x | 1.000x | unchanged (within spread) | -4.58% vs bar 8.81% (band) → **within** | 75 | 12.6 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 991.2 | 986.7 | 995.0 | 2.9 | 1.048x | 1.048x | - | - | 75 | 13.2 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `sec-github-pat`, 105.5 ns, 93 B; largest Δ: `sec-slack-webhook`, -2.5 ns (now 55.8 ns), 81 B

### `wild-waf-crs-942160-sleep-benchmark` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 754,205.3 | 0.1236 | 749,826.3 | 759,030.3 | 3,409.4 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 756,743.7 | 0.1240 | 752,573.0 | 763,581.1 | 4,557.0 | 1.003x | 1.003x | unchanged (within spread) | +0.34% vs bar 12.76% (band) → **within** |

#### `wild-waf-crs-942160-sleep-benchmark` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 552,143.4 | 0.5266 |
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 557,985.1 | 0.5321 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 130,124.9 | 0.4964 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 129,476.9 | 0.4939 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 18,601.0 | 0.2838 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 17,473.5 | 0.2666 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 371.2 | 0.0060 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 371.8 | 0.0061 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 75.4 | 0.0046 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 75.4 | 0.0046 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 75.5 | 0.0046 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 75.3 | 0.0046 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.0 | 0.0051 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 20.6 | 0.0050 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 297.6 | 0.2907 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 296.9 | 0.2900 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 18,476.9 | 0.2819 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 18,269.4 | 0.2788 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 2,329.6 | 0.2844 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2,241.4 | 0.2736 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 76.6 | 0.0047 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 75.9 | 0.0046 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 20.7 | 0.0051 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 20.5 | 0.0050 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7,572.7 | 0.0072 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,613.7 | 0.0073 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,578.6 | 0.0060 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,578.4 | 0.0060 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,525.6 | 0.0072 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,631.9 | 0.0073 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,545.7 | 0.0072 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,704.1 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,644.9 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,613.4 | 0.0073 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 373.8 | 0.0061 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 374.2 | 0.0061 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 75.2 | 0.0046 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 75.3 | 0.0046 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 557,985.1 ns, 1,048,576 B

### `wild-waf-crs-942160-sleep-benchmark` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 299.6 | 296.6 | 301.0 | 1.9 | 1.000x | 1.000x | faster ×1.09 | -7.95% vs bar 8.81% (band) → **within** | 75 | 4.0 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 325.4 | 323.8 | 326.7 | 1.1 | 1.086x | 1.086x | - | - | 75 | 4.3 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `waf-sleep`, 23.1 ns, 16 B; largest Δ: `waf-concat`, -3.9 ns (now 17.5 ns), 48 B

### `wild-waf-crs-942270-union-select` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 1,440,381.6 | 0.2360 | 1,438,205.9 | 1,467,431.9 | 11,283.7 | 1.000x | 1.000x | unchanged (within spread) | -0.99% vs bar 12.76% (band) → **within** |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 1,454,740.3 | 0.2383 | 1,437,853.8 | 1,459,981.5 | 9,331.9 | 1.010x | 1.010x | - | - |

#### `wild-waf-crs-942270-union-select` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 172,647.9 | 0.1646 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 181,619.3 | 0.1732 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 31,174.5 | 0.1189 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 31,162.2 | 0.1189 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,604.7 | 0.1160 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 7,616.4 | 0.1162 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 11,652.4 | 0.1897 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 11,624.6 | 0.1892 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,077.5 | 0.1878 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3,078.9 | 0.1879 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 182.4 | 0.0111 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 185.0 | 0.0113 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 65.3 | 0.0159 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 65.8 | 0.0161 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 177.8 | 0.1736 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 177.6 | 0.1735 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 8,340.3 | 0.1273 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 8,343.7 | 0.1273 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,099.0 | 0.1342 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 1,111.3 | 0.1357 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,417.2 | 0.2086 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3,403.6 | 0.2077 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 705.1 | 0.1722 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 690.1 | 0.1685 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 319,129.7 | 0.3044 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 319,176.3 | 0.3044 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 54,099.1 | 0.2064 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 53,600.3 | 0.2045 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 276,154.4 | 0.2634 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 276,801.3 | 0.2640 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 275,268.4 | 0.2625 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 277,012.7 | 0.2642 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 274,849.6 | 0.2621 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 275,016.8 | 0.2623 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 662.1 | 0.0108 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 663.9 | 0.0108 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 182.2 | 0.0111 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 182.8 | 0.0112 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `t-qs-1m`, 319,129.7 ns, 1,048,501 B; largest Δ: `t-1m`, -8,971.5 ns (now 172,647.9 ns), 1,048,576 B

### `wild-waf-crs-942270-union-select` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 432.3 | 428.9 | 440.0 | 4.2 | 1.000x | 1.000x | unchanged (within spread) | -18.11% vs bar 15.69% (IQR) → **improve** | 75 | 5.8 | 3.7 | 100% |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 527.9 | 515.8 | 1,327.3 | 315.0 | 1.221x | 1.221x | - | - | 75 | 7.0 | 3.8 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `waf-union`, 48.5 ns, 43 B; largest Δ: `sd-keyword-short`, -5.6 ns (now 2.5 ns), 10 B

### `wild-waf-crs-942360-concat-sqli` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 18,768,960.6 | 3.0750 | 18,651,817.2 | 19,489,898.6 | 303,998.3 | 1.000x | 1.000x | unchanged (within spread) | -0.17% (null control: program identical) |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 18,800,198.3 | 3.0801 | 18,669,248.4 | 20,465,397.5 | 677,945.3 | 1.002x | 1.002x | - | - |

#### `wild-waf-crs-942360-concat-sqli` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,184,841.2 | 3.0373 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 3,176,390.3 | 3.0292 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 784,118.8 | 2.9912 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 792,486.4 | 3.0231 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 197,633.6 | 3.0156 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 197,647.6 | 3.0159 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 94,155.1 | 1.5325 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 94,107.4 | 1.5317 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 25,197.4 | 1.5378 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 25,116.5 | 1.5329 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 56,324.9 | 3.4378 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 56,463.2 | 3.4462 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,809.7 | 1.9067 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 7,820.0 | 1.9092 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2,263.8 | 2.2107 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 2,309.9 | 2.2557 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 191,102.8 | 2.9160 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 192,520.5 | 2.9376 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 22,816.0 | 2.7852 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 22,925.3 | 2.7985 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 51,387.8 | 3.1365 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 52,226.4 | 3.1876 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 9,806.2 | 2.3941 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 9,834.4 | 2.4010 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 2,929,125.8 | 2.7936 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 2,917,123.1 | 2.7822 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 734,088.1 | 2.8009 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 729,193.8 | 2.7822 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,410,090.3 | 3.2523 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 3,426,563.5 | 3.2680 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,405,807.8 | 3.2482 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 3,419,029.3 | 3.2608 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3,413,098.2 | 3.2551 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 3,418,887.8 | 3.2607 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 197,280.9 | 3.2110 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 206,796.5 | 3.3658 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 55,796.2 | 3.4053 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 58,132.5 | 3.5479 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `t-tail-txt-1m`, 3,413,098.2 ns, 1,048,527 B; largest Δ: `t-tail-digits-1m`, -16,473.2 ns (now 3,410,090.3 ns), 1,048,522 B

### `wild-waf-crs-942360-concat-sqli` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 2,757.8 | 2,726.0 | 3,453.0 | 274.8 | 1.000x | 1.000x | - | - | 75 | 36.8 | 3.8 | 100% |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 2,770.8 | 2,636.0 | 3,179.6 | 204.8 | 1.005x | 1.005x | unchanged (within spread) | +0.47% (null control: program identical) | 75 | 36.9 | 3.7 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `sec-github-pat`, 147.3 ns, 93 B; largest Δ: `sec-slack-webhook`, -8.3 ns (now 141.4 ns), 81 B

### `wild-waf-crs-942500-comment-obfuscation` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 43,643.9 | 0.0072 | 43,323.6 | 43,789.3 | 187.1 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 43,917.1 | 0.0072 | 43,552.9 | 44,250.6 | 242.4 | 1.006x | 1.006x | unchanged (within spread) | +0.63% vs bar 12.76% (band) → **within** |

#### `wild-waf-crs-942500-comment-obfuscation` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 7,798.1 | 0.0074 |
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,702.2 | 0.0073 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 1,579.2 | 0.0060 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,586.9 | 0.0061 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 400.8 | 0.0061 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 402.6 | 0.0061 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 376.1 | 0.0061 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 378.2 | 0.0062 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 76.2 | 0.0047 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.8 | 0.0047 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 75.6 | 0.0046 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.9 | 0.0047 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 21.0 | 0.0051 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 21.7 | 0.0053 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 7.5 | 0.0073 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7.9 | 0.0077 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 401.2 | 0.0061 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 402.9 | 0.0061 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 39.6 | 0.0048 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 40.0 | 0.0049 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 76.4 | 0.0047 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 77.1 | 0.0047 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 20.5 | 0.0050 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 21.1 | 0.0052 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 7,568.2 | 0.0072 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,789.5 | 0.0074 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 1,579.5 | 0.0060 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,587.3 | 0.0061 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,634.4 | 0.0073 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,903.8 | 0.0075 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 7,795.0 | 0.0074 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,672.9 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 7,637.4 | 0.0073 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 7,622.8 | 0.0073 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 376.4 | 0.0061 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 377.3 | 0.0061 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 75.8 | 0.0046 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 76.7 | 0.0047 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now (also the largest Δ): `t-tail-digits-1m`, 7,903.8 ns, 1,048,522 B

### `wild-waf-crs-942500-comment-obfuscation` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 326.0 | 324.2 | 327.8 | 1.2 | 1.000x | 1.000x | - | - | 75 | 4.3 | 3.8 | 100% |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 340.3 | 332.7 | 341.4 | 3.8 | 1.044x | 1.044x | slower ×1.04 | +4.40% vs bar 8.81% (band) → **within** | 75 | 4.5 | 3.7 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `waf-comment-obfuscation`, 38.8 ns, 18 B; largest Δ: `rec-comment-nested`, -4.5 ns (now 15.1 ns), 34 B

### `winpath-near-miss` / `large-subject-throughput` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_d6c5e71a5_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 66.1 | 0.0000 | 66.1 | 66.2 | 0.0 | 1.000x | 1.000x | faster ×1.01 | -1.10% (null control: program identical) |
| 2 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 66.9 | 0.0000 | 66.8 | 67.0 | 0.1 | 1.011x | 1.011x | - | - |

#### `winpath-near-miss` / `large-subject-throughput` per-subject (capability@0.4)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.3 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_cb32eda28_auto-caps-simdna` | 3.4 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_cb32eda28_auto-caps-simdna` | 3.4 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.3 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 3.2 | 0.0000 |
| `t-evil-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.2 | 0.0001 |
| `t-evil-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 3.4 | 0.0001 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.2 | 0.0002 |
| `t-evil-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3.3 | 0.0002 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.8 | 0.0002 |
| `t-hyb-datepath-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3.8 | 0.0002 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.8 | 0.0009 |
| `t-hyb-digits-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 3.8 | 0.0009 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.4 | 0.0033 |
| `t-hyb-embed-1k` | 1,024 | `pcrec_cb32eda28_auto-caps-simdna` | 3.4 | 0.0034 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.4 | 0.0001 |
| `t-hyb-embed-64k` | 65,536 | `pcrec_cb32eda28_auto-caps-simdna` | 3.5 | 0.0001 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.4 | 0.0004 |
| `t-hyb-embed-8k` | 8,192 | `pcrec_cb32eda28_auto-caps-simdna` | 3.4 | 0.0004 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.4 | 0.0002 |
| `t-hyb-logline-16k` | 16,384 | `pcrec_cb32eda28_auto-caps-simdna` | 3.5 | 0.0002 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.8 | 0.0009 |
| `t-mixed-runs-4k` | 4,096 | `pcrec_cb32eda28_auto-caps-simdna` | 3.8 | 0.0009 |
| `t-qs-1m` | 1,048,501 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.4 | 0.0000 |
| `t-qs-1m` | 1,048,501 | `pcrec_cb32eda28_auto-caps-simdna` | 3.5 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.4 | 0.0000 |
| `t-qs-nearmiss-256k` | 262,092 | `pcrec_cb32eda28_auto-caps-simdna` | 3.4 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.4 | 0.0000 |
| `t-tail-digits-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 3.4 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.4 | 0.0000 |
| `t-tail-space-1m` | 1,048,522 | `pcrec_cb32eda28_auto-caps-simdna` | 3.5 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.4 | 0.0000 |
| `t-tail-txt-1m` | 1,048,527 | `pcrec_cb32eda28_auto-caps-simdna` | 3.5 | 0.0000 |
| `t-trim-match-60k` | 61,440 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.8 | 0.0001 |
| `t-trim-match-60k` | 61,440 | `pcrec_cb32eda28_auto-caps-simdna` | 3.9 | 0.0001 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_d6c5e71a5_auto-caps-simdna` | 3.8 | 0.0002 |
| `t-trim-nearmiss-16k` | 16,385 | `pcrec_cb32eda28_auto-caps-simdna` | 3.9 | 0.0002 |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `t-trim-match-60k`, 3.8 ns, 61,440 B; largest Δ: `t-1m`, -0.2 ns (now 3.3 ns), 1,048,576 B

### `winpath-near-miss` / `short-subject-search` (capability@0.4) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_cb32eda28_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_cb32eda28_auto-caps-simdna` | measured | `plain` | same program | 297.4 | 295.3 | 298.9 | 1.3 | 1.000x | 1.000x | - | - | 75 | 4.0 | 3.8 | 100% |
| 2 | `pcrec_d6c5e71a5_auto-caps-simdna` | measured | `plain` | same program | 299.1 | 295.4 | 308.4 | 4.7 | 1.006x | 1.006x | unchanged (within spread) | +0.56% (null control: program identical) | 75 | 4.0 | 3.7 | 100% |

- Δ detail: `pcrec_d6c5e71a5_auto-caps-simdna` vs previous `pcrec_cb32eda28_auto-caps-simdna`: worst now: `lp-winpath`, 17.5 ns, 22 B; largest Δ: `lp-winpath-reserved`, +0.1 ns (now 9.2 ns), 24 B

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `date-nested-plus` | `large-subject-throughput` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 19 | 95% | -3:PCREC_ERR_FRAMES×1 (smallest: t-hyb-datepath-16k, 16,384 B) | 0 | `t-hyb-datepath-16k` (gave-up) |
| `date-nested-plus` | `large-subject-throughput` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 19 | 95% | -3:PCREC_ERR_FRAMES×1 (smallest: t-hyb-datepath-16k, 16,384 B) | 0 | `t-hyb-datepath-16k` (gave-up) |
| `dup-param-detect` | `large-subject-throughput` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 19 | 89% | -3:PCREC_ERR_FRAMES×2 (smallest: t-qs-nearmiss-256k, 262,092 B) | 0 | `t-qs-1m` (gave-up), `t-qs-nearmiss-256k` (gave-up) |
| `dup-param-detect` | `large-subject-throughput` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 19 | 89% | -3:PCREC_ERR_FRAMES×2 (smallest: t-qs-nearmiss-256k, 262,092 B) | 0 | `t-qs-1m` (gave-up), `t-qs-nearmiss-256k` (gave-up) |
| `email-nested-plus` | `large-subject-throughput` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 19 | 89% | 0 | 0 | `t-evil-match-60k` (no-expectation), `t-evil-nearmiss-16k` (no-expectation) |
| `email-nested-plus` | `large-subject-throughput` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 19 | 89% | 0 | 0 | `t-evil-match-60k` (no-expectation), `t-evil-nearmiss-16k` (no-expectation) |

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
- `pcrec_d6c5e71a5_auto-caps-simdna` / `balanced-parens-rec` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,071 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_d6c5e71a5_auto-caps-simdna` / `balanced-parens-rec` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,281 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_d6c5e71a5_auto-caps-simdna` / `base10num-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `base10num-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `bracket-array-define` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,402 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_d6c5e71a5_auto-caps-simdna` / `bracket-array-define` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,507 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_d6c5e71a5_auto-caps-simdna` / `codegrammar-flat` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,667 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `codegrammar-flat` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,770 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `codegrammar-xflag` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,667 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `codegrammar-xflag` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,770 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `currency-lookbehind-fixed` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=mixed offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=1, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `currency-lookbehind-fixed` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=mixed offsets=none, edge=range, edges=0 (match: 1), start=reverse-pass, folds=1, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `date-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 8,178 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `date-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 8,283 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `doubled-word` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,418 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `doubled-word` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,521 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `dup-param-detect` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,851 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `dup-param-detect` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,956 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `email-local-nodup` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 2,976 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/4 == stamped default (single tier), buffers=3/4 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `email-local-nodup` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 3,081 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/4 == stamped default (single tier), buffers=3/4 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `email-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 3,365 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `email-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 3,470 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `evil-alt-nested` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 4,599 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `evil-alt-nested` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 4,704 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `file-ext-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=cover prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `file-ext-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `float-literal-bound` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=landmark-walk prefilter=first-class-bounded table=mixed offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `float-literal-bound` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=indexed offsets=none, edge=range, edges=0 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `floor-byte` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=cover prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `floor-byte` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `hex8-bounded` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=cover prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `hex8-bounded` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=bitmap, edges=0 (match: 1), start=reverse-pass, folds=1, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `high-byte-run` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=4 (match: 2), start=reverse-pass, folds=2, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `high-byte-run` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `ipv4-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `ipv4-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `keyword-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=cover prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `keyword-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `letters-bounded-tail-z` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `letters-bounded-tail-z` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `logparse-atomic` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=1, islands=2, shape=plain (prog: 10,528 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `logparse-atomic` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=1, islands=2, shape=plain (prog: 10,633 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `logparse-atomic-removed` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=1, islands=2, shape=plain (prog: 10,118 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `logparse-atomic-removed` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=1, islands=2, shape=plain (prog: 10,223 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `mojibake-curly-quote` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `mojibake-curly-quote` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `nested-comment-rec` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 6,854 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_d6c5e71a5_auto-caps-simdna` / `nested-comment-rec` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 6,959 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_d6c5e71a5_auto-caps-simdna` / `numeric-id-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 3,052 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `numeric-id-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 3,157 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `phone-list-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 4,220 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `phone-list-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 4,325 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `phone-palindrome-6` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 4,078 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `phone-palindrome-6` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=plain (prog: 4,183 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `pwd-strength-chain` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 7,940 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `pwd-strength-chain` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 8,045 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `quoted-delim-match` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,245 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `quoted-delim-match` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,350 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `router-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=cover prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `router-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `tag-depth3-bound` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 11,207 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `tag-depth3-bound` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 11,312 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `tag-pair-match` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,848 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `tag-pair-match` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,953 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `tail-digits-eol` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `tail-digits-eol` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `tail-dotstar-txt` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `tail-dotstar-txt` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `tail-ext-lower-txt` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `tail-ext-lower-txt` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `tail-space-eol` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=bitmap, edges=2 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `tail-space-eol` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `tail-word-eoz` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `tail-word-eoz` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `trim-nested-star` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 1,844 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `trim-nested-star` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 1,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `utf8-lead-no-cont` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=cover prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `utf8-lead-no-cont` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=mixed offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `uuid-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `uuid-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-codegrammar-json-array-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=cover prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-codegrammar-json-array-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-codegrammar-json-constant` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=first-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-codegrammar-json-constant` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=0 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-codegrammar-json-number-extended` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-codegrammar-json-number-extended` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=0 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-codegrammar-json-object-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=cover prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-codegrammar-json-object-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-codegrammar-json-stringcontent-escape` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-codegrammar-json-stringcontent-escape` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-datetime-datefinder-alternation` / `plain`: engine=vm, sel=size-cap-retry (DFA fallback tripped), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 265,008 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=49/74 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-datetime-datefinder-alternation` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=mixed, edges=2 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 265,117 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=49/74 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-datetime-moment-iso8601` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 14,666 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=12/11 == stamped default (single tier), buffers=12/11 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-datetime-moment-iso8601` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 14,771 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=12/11 == stamped default (single tier), buffers=12/11 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-logparse-base10num-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=mixed, edges=2 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,873 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=3/2 == stamped default (single tier), buffers=3/2 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-logparse-base10num-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,978 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=3/2 == stamped default (single tier), buffers=3/2 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-logparse-base10num-noatomic` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=mixed offsets=none, edge=mixed, edges=2 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-logparse-base10num-noatomic` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=mixed offsets=none, edge=range, edges=0 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-logparse-quotedstring-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=first-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 17,406 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-logparse-quotedstring-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 17,511 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-logparse-quotedstring-noatomic` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=first-class-bounded table=mixed offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-logparse-quotedstring-noatomic` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=mixed offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-logparse-syslogbase-expanded` / `plain`: engine=vm, sel=size-cap-retry (DFA fallback tripped), entry=plain entry, vm_prefilter=hybrid, lang=count-collapsed (size cap retry, exact 1458783 > 1000000), dfa: scan=unanchored prefilter=first-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 296,180 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=21/32 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-logparse-syslogbase-expanded` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 296,289 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=21/32 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-logparse-winpath-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,656 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-logparse-winpath-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,762 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-secrets-aws-access-key-id` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=handoff table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, frameless=0, islands=1, shape=plain (prog: 6,307 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/3 == stamped default (single tier), buffers=2/3 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-secrets-aws-access-key-id` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=1, shape=plain (prog: 6,412 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/3 == stamped default (single tier), buffers=2/3 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-secrets-github-pat` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,6*, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, frameless=1, islands=0, shape=inline (prog: 1,864 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-secrets-github-pat` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 1,967 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-secrets-slack-webhook-url` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,6*, edge=mixed, edges=3 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=plain (prog: 8,428 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-secrets-slack-webhook-url` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=mixed, edges=3 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=plain (prog: 8,533 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-secrets-username-password-pair` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class table=mixed offsets=none, edge=mixed, edges=3 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=2, shape=plain (prog: 16,975 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-secrets-username-password-pair` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=2, shape=plain (prog: 17,080 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=cover prefilter=none table=premultiplied offsets=none, edge=range, edges=0 (match: 1), start=attempt-start, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=0 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,461 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,566 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-validator-email-owasp` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-validator-email-owasp` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-validator-ipv4-owasp` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 14,287 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-validator-ipv4-owasp` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 14,392 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-validator-us-zip-owasp` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 2,265 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=2/4 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-validator-us-zip-owasp` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, frameless=0, islands=0, shape=plain (prog: 2,368 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=2/4 (stamped default), frame=24
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-validator-uuid-grok` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,8*,13, edge=bitmap, edges=4 (match: 4), start=end-minus-width, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-validator-uuid-grok` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=bitmap, edges=4 (match: 4), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-waf-crs-942140-dbnames` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=first-class-bounded table=premultiplied offsets=none, edge=mixed, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-waf-crs-942140-dbnames` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=mixed, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-waf-crs-942270-union-select` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-waf-crs-942270-union-select` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-waf-crs-942360-concat-sqli` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-waf-crs-942360-concat-sqli` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=compound prefilter=compound table=compound offsets=compound, edge=compound, edges=0 (match: 0), start=compound, folds=-1, match=compound, compound=split, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-waf-crs-942500-comment-obfuscation` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `wild-waf-crs-942500-comment-obfuscation` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `winpath-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d6c5e71a5_auto-caps-simdna` / `winpath-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=attempt-start, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
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
| `balanced-parens-rec` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 128,239,097.0 | 127,545,942.0 | 129,023,286.0 | 527,353.8 | 5 | 37,392 | 30,866 | 29,113 | 0.004 | compiled=5 | 3,090,315.0 | 125,223,964.0 | 50,005.0 |
| `balanced-parens-rec` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 129,259,439.0 | 128,224,549.0 | 129,489,594.0 | 457,681.9 | 5 | 37,392 | 31,084 | 29,331 | 0.004 | compiled=5 | 2,949,049.0 | 126,497,384.0 | 51,647.0 |
| `base10num-near-miss` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 80,167,222.0 | 79,664,356.0 | 80,419,268.0 | 271,259.0 | 5 | 37,232 | 17,591 | 15,206 | 0.003 | compiled=5 | 1,318,795.0 | 78,756,283.0 | 51,908.0 |
| `base10num-near-miss` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 79,639,027.0 | 77,985,890.0 | 79,683,582.0 | 776,928.7 | 5 | 37,152 | 17,044 | 14,659 | 0.010 | compiled=5 | 1,341,067.0 | 78,258,996.0 | 57,718.0 |
| `base10num-near-miss` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 79,210,656.0 | 77,695,731.0 | 79,973,234.0 | 761,590.5 | 5 | 37,232 | 17,647 | 15,262 | 0.010 (max is trial 1) | compiled=5 | 1,764,336.0 | 77,269,116.0 | 52,028.0 |
| `base10num-near-miss` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 77,025,658.0 | 75,597,505.0 | 79,122,840.0 | 1,157,992.8 | 5 | 37,152 | 17,100 | 14,715 | 0.015 | compiled=5 | 1,801,285.0 | 75,312,037.0 | 41,559.0 |
| `bracket-array-define` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 139,555,588.0 | 138,148,496.0 | 143,919,934.0 | 2,065,978.2 | 5 | 37,376 | 29,322 | 29,007 | 0.015 (max is trial 1) | compiled=5 | 1,813,589.0 | 136,937,242.0 | 53,802.0 |
| `bracket-array-define` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 137,724,186.0 | 136,657,826.0 | 138,629,582.0 | 703,687.8 | 5 | 37,376 | 29,437 | 29,122 | 0.005 | compiled=5 | 2,317,749.0 | 135,228,001.0 | 53,230.0 |
| `bracket-array-define` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 131,430,724.0 | 130,325,641.0 | 132,427,824.0 | 884,174.2 | 5 | 37,376 | 29,433 | 29,118 | 0.007 | compiled=5 | 2,849,001.0 | 128,476,144.0 | 56,667.0 |
| `bracket-array-define` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 130,071,963.0 | 129,156,877.0 | 130,278,551.0 | 402,447.6 | 5 | 37,376 | 29,548 | 29,233 | 0.003 | compiled=5 | 2,844,301.0 | 127,275,400.0 | 50,415.0 |
| `codegrammar-flat` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 258,757,940.0 | 251,239,479.0 | 259,641,155.0 | 3,675,855.9 | 5 | 37,472 | 36,875 | 28,276 | 0.014 (max is trial 1) | compiled=5 | 4,457,342.0 | 253,691,711.0 | 45,476.0 |
| `codegrammar-flat` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 247,481,315.0 | 246,965,332.0 | 248,683,611.0 | 575,507.1 | 5 | 37,232 | 31,131 | 27,171 | 0.002 (max is trial 1) | compiled=5 | 2,985,718.0 | 244,547,014.0 | 43,642.0 |
| `codegrammar-flat` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 261,902,079.0 | 259,243,318.0 | 265,699,718.0 | 2,445,550.5 | 5 | 37,472 | 37,037 | 28,438 | 0.009 | compiled=5 | 5,816,054.0 | 256,855,856.0 | 53,952.0 |
| `codegrammar-flat` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 251,165,590.0 | 250,750,127.0 | 253,047,417.0 | 808,155.7 | 5 | 37,232 | 31,293 | 27,333 | 0.003 | compiled=5 | 3,514,324.0 | 247,729,944.0 | 50,896.0 |
| `codegrammar-xflag` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 249,546,978.0 | 246,484,445.0 | 251,817,849.0 | 1,969,265.1 | 5 | 37,512 | 37,153 | 28,475 | 0.008 (max is trial 1) | compiled=5 | 4,534,778.0 | 244,457,014.0 | 48,752.0 |
| `codegrammar-xflag` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 240,647,853.0 | 239,418,427.0 | 240,951,857.0 | 555,169.1 | 5 | 37,272 | 31,411 | 27,372 | 0.002 | compiled=5 | 2,288,102.0 | 237,843,507.0 | 52,319.0 |
| `codegrammar-xflag` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 256,643,277.0 | 255,668,588.0 | 257,589,480.0 | 616,680.8 | 5 | 37,512 | 37,315 | 28,637 | 0.002 | compiled=5 | 5,830,401.0 | 250,648,075.0 | 49,623.0 |
| `codegrammar-xflag` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 252,960,243.0 | 251,183,334.0 | 257,458,302.0 | 2,250,678.7 | 5 | 37,272 | 31,573 | 27,534 | 0.009 | compiled=5 | 3,858,343.0 | 248,842,461.0 | 51,427.0 |
| `currency-lookbehind-fixed` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 89,650,348.0 | 87,945,345.0 | 91,639,048.0 | 1,314,740.5 | 5 | 33,552 | 23,733 | 17,533 | 0.015 | compiled=5 | 2,182,564.0 | 87,408,072.0 | 50,445.0 |
| `currency-lookbehind-fixed` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 88,187,400.0 | 87,898,345.0 | 89,888,647.0 | 743,239.1 | 5 | 33,288 | 22,402 | 18,058 | 0.008 | compiled=5 | 2,119,255.0 | 86,367,680.0 | 53,260.0 |
| `currency-lookbehind-fixed` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 84,881,086.0 | 84,514,684.0 | 85,366,280.0 | 321,771.7 | 5 | 33,552 | 23,789 | 17,589 | 0.004 (max is trial 1) | compiled=5 | 3,250,778.0 | 81,456,730.0 | 53,621.0 |
| `currency-lookbehind-fixed` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 85,119,545.0 | 84,835,099.0 | 85,573,500.0 | 289,445.4 | 5 | 33,288 | 22,458 | 18,114 | 0.003 (max is trial 1) | compiled=5 | 2,603,879.0 | 82,563,547.0 | 50,054.0 |
| `date-nested-plus` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 146,617,900.0 | 146,228,647.0 | 147,434,119.0 | 419,663.1 | 5 | 37,536 | 36,791 | 34,765 | 0.003 | compiled=5 | 2,501,386.0 | 144,023,009.0 | 54,282.0 |
| `date-nested-plus` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 146,825,963.0 | 145,855,022.0 | 147,497,538.0 | 573,244.9 | 5 | 37,536 | 36,719 | 34,693 | 0.004 | compiled=5 | 2,624,066.0 | 144,605,787.0 | 56,006.0 |
| `date-nested-plus` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 147,417,400.0 | 146,845,019.0 | 148,098,563.0 | 493,885.0 | 5 | 37,536 | 36,902 | 34,876 | 0.003 | compiled=5 | 3,083,813.0 | 144,686,361.0 | 51,117.0 |
| `date-nested-plus` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 146,191,900.0 | 145,266,946.0 | 146,908,260.0 | 605,442.1 | 5 | 37,536 | 36,830 | 34,804 | 0.004 | compiled=5 | 3,139,739.0 | 143,407,801.0 | 53,772.0 |
| `doubled-word` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 322,346,703.0 | 316,481,017.0 | 324,106,572.0 | 2,642,157.6 | 5 | 41,096 | 26,720 | 24,790 | 0.008 | compiled=5 | 8,647,249.0 | 314,145,705.0 | 53,230.0 |
| `doubled-word` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 320,968,114.0 | 312,591,485.0 | 329,212,926.0 | 5,288,804.2 | 5 | 41,096 | 26,831 | 24,901 | 0.016 | compiled=5 | 8,624,066.0 | 311,990,813.0 | 55,194.0 |
| `doubled-word` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 326,303,459.0 | 323,681,187.0 | 334,595,040.0 | 4,463,781.6 | 5 | 41,096 | 26,882 | 24,952 | 0.014 | compiled=5 | 3,205,032.0 | 323,045,888.0 | 49,874.0 |
| `doubled-word` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 327,770,756.0 | 321,339,772.0 | 331,902,764.0 | 3,899,838.7 | 5 | 41,096 | 26,993 | 25,063 | 0.012 | compiled=5 | 9,159,616.0 | 318,938,215.0 | 44,915.0 |
| `dup-param-detect` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 144,919,459.0 | 144,225,661.0 | 145,839,323.0 | 614,818.6 | 5 | 37,432 | 32,323 | 30,339 | 0.004 | compiled=5 | 2,552,111.0 | 142,207,526.0 | 49,213.0 |
| `dup-param-detect` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 144,860,158.0 | 143,879,468.0 | 146,219,449.0 | 754,065.0 | 5 | 37,432 | 32,436 | 30,452 | 0.005 | compiled=5 | 2,711,591.0 | 141,961,494.0 | 51,007.0 |
| `dup-param-detect` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 145,318,944.0 | 144,052,697.0 | 146,181,059.0 | 694,910.0 | 5 | 37,432 | 32,485 | 30,501 | 0.005 | compiled=5 | 3,308,256.0 | 142,391,926.0 | 45,065.0 |
| `dup-param-detect` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 146,248,757.0 | 144,061,934.0 | 149,718,176.0 | 1,845,268.7 | 5 | 37,432 | 32,598 | 30,614 | 0.013 | compiled=5 | 3,188,180.0 | 143,009,901.0 | 43,732.0 |
| `email-local-nodup` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 111,829,174.0 | 109,958,559.0 | 111,935,345.0 | 743,892.9 | 5 | 33,152 | 27,960 | 25,769 | 0.007 (max is trial 1) | compiled=5 | 2,575,505.0 | 109,166,465.0 | 41,128.0 |
| `email-local-nodup` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 95,679,041.0 | 94,365,536.0 | 96,149,618.0 | 624,312.3 | 5 | 33,072 | 28,348 | 26,066 | 0.007 (max is trial 1) | compiled=5 | 1,734,399.0 | 93,584,504.0 | 51,567.0 |
| `email-local-nodup` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 108,095,957.0 | 106,992,276.0 | 108,990,633.0 | 724,621.0 | 5 | 33,152 | 28,016 | 25,825 | 0.007 | compiled=5 | 2,921,537.0 | 105,117,482.0 | 45,065.0 |
| `email-local-nodup` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 92,049,048.0 | 91,278,616.0 | 93,304,032.0 | 762,563.5 | 5 | 33,072 | 28,404 | 26,122 | 0.008 (max is trial 1) | compiled=5 | 2,024,417.0 | 89,528,315.0 | 49,172.0 |
| `email-nested-plus` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 132,171,921.0 | 131,899,157.0 | 132,813,780.0 | 387,971.0 | 5 | 37,496 | 32,089 | 30,143 | 0.003 | compiled=5 | 2,445,800.0 | 130,189,554.0 | 53,702.0 |
| `email-nested-plus` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 132,376,987.0 | 131,630,650.0 | 132,904,410.0 | 433,143.5 | 5 | 37,496 | 32,520 | 30,490 | 0.003 | compiled=5 | 2,452,693.0 | 129,825,086.0 | 54,463.0 |
| `email-nested-plus` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 133,017,925.0 | 131,867,045.0 | 133,154,784.0 | 590,014.0 | 5 | 37,496 | 32,200 | 30,254 | 0.004 | compiled=5 | 2,877,134.0 | 129,992,572.0 | 52,248.0 |
| `email-nested-plus` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 132,755,920.0 | 132,557,488.0 | 133,668,763.0 | 509,586.9 | 5 | 37,496 | 32,631 | 30,601 | 0.004 | compiled=5 | 2,919,133.0 | 130,418,075.0 | 54,964.0 |
| `evil-alt-nested` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 174,178,220.0 | 173,115,238.0 | 174,875,405.0 | 574,209.9 | 5 | 41,664 | 32,798 | 31,187 | 0.003 | compiled=5 | 2,563,803.0 | 171,496,125.0 | 52,489.0 |
| `evil-alt-nested` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 172,647,616.0 | 172,102,227.0 | 174,528,360.0 | 919,022.7 | 5 | 41,632 | 32,726 | 31,115 | 0.005 (max is trial 1) | compiled=5 | 2,599,349.0 | 169,951,223.0 | 51,067.0 |
| `evil-alt-nested` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 174,416,464.0 | 173,770,607.0 | 175,416,117.0 | 580,136.1 | 5 | 41,664 | 32,854 | 31,243 | 0.003 | compiled=5 | 3,059,637.0 | 171,356,546.0 | 43,051.0 |
| `evil-alt-nested` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 175,409,214.0 | 173,097,890.0 | 177,880,103.0 | 1,912,707.5 | 5 | 41,632 | 32,782 | 31,171 | 0.011 | compiled=5 | 3,062,363.0 | 172,195,527.0 | 49,403.0 |
| `file-ext-order` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 79,455,390.0 | 78,235,050.0 | 80,394,160.0 | 763,874.9 | 5 | 28,888 | 15,998 | 13,994 | 0.010 (max is trial 1) | compiled=5 | 2,039,975.0 | 77,243,271.0 | 56,797.0 |
| `file-ext-order` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 83,927,221.0 | 82,580,471.0 | 84,650,053.0 | 680,338.8 | 5 | 33,176 | 20,888 | 16,046 | 0.008 | compiled=5 | 2,427,216.0 | 81,443,769.0 | 54,583.0 |
| `file-ext-order` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 78,959,191.0 | 78,343,321.0 | 80,064,717.0 | 622,175.4 | 5 | 28,888 | 16,054 | 14,050 | 0.008 | compiled=5 | 3,169,384.0 | 75,748,760.0 | 49,263.0 |
| `file-ext-order` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 83,433,837.0 | 82,630,262.0 | 84,349,893.0 | 607,035.2 | 5 | 33,176 | 20,942 | 16,100 | 0.007 | compiled=5 | 3,653,918.0 | 79,690,140.0 | 45,545.0 |
| `float-literal-bound` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 90,096,679.0 | 89,251,848.0 | 91,377,193.0 | 794,269.8 | 5 | 33,648 | 24,886 | 17,710 | 0.009 | compiled=5 | 4,419,691.0 | 85,619,750.0 | 55,775.0 |
| `float-literal-bound` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 87,440,883.0 | 86,794,575.0 | 89,805,280.0 | 1,037,480.7 | 5 | 33,344 | 21,930 | 17,953 | 0.012 | compiled=5 | 2,199,526.0 | 85,184,380.0 | 45,455.0 |
| `float-literal-bound` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 97,411,386.0 | 97,230,203.0 | 97,739,494.0 | 178,468.7 | 5 | 34,120 | 32,965 | 22,081 | 0.002 | compiled=5 | 5,044,680.0 | 92,505,237.0 | 53,801.0 |
| `float-literal-bound` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 86,157,871.0 | 85,921,026.0 | 87,191,842.0 | 490,814.1 | 5 | 33,344 | 21,998 | 18,021 | 0.006 (max is trial 1) | compiled=5 | 2,790,230.0 | 83,231,055.0 | 47,941.0 |
| `floor-byte` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 76,614,608.0 | 76,078,015.0 | 77,745,999.0 | 557,535.0 | 5 | 28,888 | 15,592 | 13,923 | 0.007 | compiled=5 | 1,680,097.0 | 74,975,066.0 | 45,115.0 |
| `floor-byte` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 79,401,059.0 | 78,577,175.0 | 80,087,343.0 | 486,692.4 | 5 | 33,176 | 19,581 | 16,023 | 0.006 | compiled=5 | 1,639,721.0 | 77,786,115.0 | 50,405.0 |
| `floor-byte` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 77,855,030.0 | 76,504,785.0 | 78,354,422.0 | 672,691.1 | 5 | 28,888 | 15,648 | 13,979 | 0.009 | compiled=5 | 2,240,273.0 | 75,446,240.0 | 44,965.0 |
| `floor-byte` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 82,476,843.0 | 82,308,656.0 | 83,370,669.0 | 377,449.0 | 5 | 33,176 | 19,637 | 16,079 | 0.005 | compiled=5 | 2,562,801.0 | 79,818,221.0 | 48,471.0 |
| `hex8-bounded` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 86,441,369.0 | 86,011,840.0 | 87,457,895.0 | 592,959.8 | 5 | 33,080 | 18,901 | 15,888 | 0.007 | compiled=5 | 2,118,223.0 | 84,198,271.0 | 42,410.0 |
| `hex8-bounded` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 88,235,811.0 | 87,946,678.0 | 89,174,721.0 | 422,482.8 | 5 | 33,336 | 23,984 | 18,205 | 0.005 | compiled=5 | 2,427,306.0 | 85,832,581.0 | 44,594.0 |
| `hex8-bounded` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 85,658,431.0 | 84,831,272.0 | 88,861,669.0 | 1,409,045.6 | 5 | 33,080 | 19,056 | 16,043 | 0.016 | compiled=5 | 3,307,545.0 | 82,295,832.0 | 47,770.0 |
| `hex8-bounded` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 88,335,767.0 | 87,768,889.0 | 88,643,659.0 | 360,998.3 | 5 | 33,336 | 24,137 | 18,358 | 0.004 | compiled=5 | 3,083,453.0 | 85,130,465.0 | 46,047.0 |
| `high-byte-run` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 91,725,560.0 | 90,688,626.0 | 92,224,010.0 | 578,556.3 | 5 | 32,976 | 27,070 | 20,764 | 0.006 | compiled=5 | 2,367,593.0 | 89,197,174.0 | 48,301.0 |
| `high-byte-run` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 88,794,425.0 | 86,901,547.0 | 89,530,392.0 | 872,333.1 | 5 | 33,176 | 21,598 | 17,896 | 0.010 | compiled=5 | 2,149,101.0 | 86,692,834.0 | 44,263.0 |
| `high-byte-run` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 93,252,215.0 | 92,027,918.0 | 94,857,281.0 | 999,174.0 | 5 | 32,976 | 27,246 | 20,940 | 0.011 | compiled=5 | 3,711,797.0 | 89,627,171.0 | 46,788.0 |
| `high-byte-run` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 86,678,054.0 | 86,415,868.0 | 88,837,493.0 | 886,574.8 | 5 | 33,176 | 21,654 | 17,952 | 0.010 | compiled=5 | 2,707,684.0 | 84,118,037.0 | 49,273.0 |
| `ipv4-near-miss` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 88,524,126.0 | 88,305,242.0 | 89,399,054.0 | 384,635.1 | 5 | 42,184 | 24,556 | 19,240 | 0.004 | compiled=5 | 1,389,168.0 | 87,148,653.0 | 53,291.0 |
| `ipv4-near-miss` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 86,375,736.0 | 86,263,215.0 | 88,088,384.0 | 804,259.4 | 5 | 41,984 | 23,634 | 18,318 | 0.009 | compiled=5 | 1,496,962.0 | 84,836,344.0 | 54,734.0 |
| `ipv4-near-miss` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 86,908,728.0 | 86,333,403.0 | 87,360,329.0 | 385,783.6 | 5 | 42,184 | 24,612 | 19,296 | 0.004 | compiled=5 | 1,860,166.0 | 84,503,103.0 | 53,561.0 |
| `ipv4-near-miss` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 84,461,825.0 | 83,709,627.0 | 85,411,354.0 | 588,782.9 | 5 | 41,984 | 23,690 | 18,374 | 0.007 | compiled=5 | 1,909,219.0 | 82,432,039.0 | 48,070.0 |
| `keyword-prefix-order` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 79,996,231.0 | 78,610,168.0 | 80,433,895.0 | 762,700.6 | 5 | 28,888 | 15,948 | 14,003 | 0.010 (max is trial 1) | compiled=5 | 1,944,385.0 | 78,088,174.0 | 52,289.0 |
| `keyword-prefix-order` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 82,434,206.0 | 81,911,391.0 | 82,738,921.0 | 297,065.7 | 5 | 33,176 | 22,186 | 16,041 | 0.004 | compiled=5 | 2,183,526.0 | 79,931,137.0 | 49,964.0 |
| `keyword-prefix-order` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 79,422,335.0 | 78,405,939.0 | 80,973,439.0 | 833,686.9 | 5 | 28,888 | 16,004 | 14,059 | 0.010 | compiled=5 | 2,570,295.0 | 76,684,895.0 | 47,259.0 |
| `keyword-prefix-order` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 82,489,579.0 | 80,797,749.0 | 84,512,330.0 | 1,348,411.5 | 5 | 33,176 | 22,240 | 16,095 | 0.016 | compiled=5 | 2,681,796.0 | 79,755,514.0 | 49,794.0 |
| `letters-bounded-tail-z` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 188,477,754.0 | 186,056,141.0 | 190,037,274.0 | 1,303,262.3 | 5 | 66,160 | 137,275 | 18,930 | 0.007 | compiled=5 | 86,987,809.0 | 101,021,803.0 | 52,949.0 |
| `letters-bounded-tail-z` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 188,705,954.0 | 186,446,918.0 | 189,835,525.0 | 1,198,638.4 | 5 | 66,160 | 137,283 | 18,938 | 0.006 | compiled=5 | 86,509,338.0 | 101,891,211.0 | 50,586.0 |
| `letters-bounded-tail-z` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 191,805,193.0 | 190,045,444.0 | 192,162,637.0 | 756,387.6 | 5 | 66,160 | 137,331 | 18,986 | 0.004 | compiled=5 | 90,994,550.0 | 100,645,953.0 | 40,797.0 |
| `letters-bounded-tail-z` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 191,809,591.0 | 190,715,879.0 | 193,067,272.0 | 746,720.2 | 5 | 66,160 | 137,339 | 18,994 | 0.004 | compiled=5 | 90,520,556.0 | 101,684,420.0 | 42,049.0 |
| `logparse-atomic` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 146,528,502.0 | 145,332,047.0 | 148,651,483.0 | 1,159,001.5 | 5 | 84,408 | 59,532 | 39,599 | 0.008 | compiled=5 | 3,341,609.0 | 143,158,019.0 | 59,863.0 |
| `logparse-atomic` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 147,211,860.0 | 144,138,317.0 | 149,727,663.0 | 1,895,627.2 | 5 | 84,368 | 59,459 | 39,526 | 0.013 | compiled=5 | 3,055,530.0 | 143,922,069.0 | 61,726.0 |
| `logparse-atomic` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 145,813,407.0 | 144,459,644.0 | 150,100,106.0 | 1,918,761.4 | 5 | 84,408 | 59,738 | 39,805 | 0.013 | compiled=5 | 4,548,524.0 | 141,136,360.0 | 51,968.0 |
| `logparse-atomic` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 147,693,128.0 | 147,254,663.0 | 148,389,792.0 | 396,377.6 | 5 | 84,368 | 59,665 | 39,732 | 0.003 (max is trial 1) | compiled=5 | 4,409,722.0 | 142,926,945.0 | 64,071.0 |
| `logparse-atomic-removed` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 145,422,427.0 | 144,742,575.0 | 146,988,860.0 | 866,203.5 | 5 | 84,408 | 59,248 | 39,315 | 0.006 | compiled=5 | 3,323,044.0 | 142,410,379.0 | 56,858.0 |
| `logparse-atomic-removed` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 143,271,774.0 | 142,665,980.0 | 143,929,422.0 | 471,392.0 | 5 | 84,368 | 59,175 | 39,242 | 0.003 | compiled=5 | 3,151,370.0 | 140,223,467.0 | 49,173.0 |
| `logparse-atomic-removed` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 145,750,939.0 | 144,243,557.0 | 147,730,920.0 | 1,126,740.0 | 5 | 84,408 | 59,454 | 39,521 | 0.008 | compiled=5 | 4,371,871.0 | 141,315,708.0 | 56,747.0 |
| `logparse-atomic-removed` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 147,701,534.0 | 145,875,933.0 | 148,970,478.0 | 1,011,318.7 | 5 | 84,368 | 59,381 | 39,448 | 0.007 (max is trial 1) | compiled=5 | 4,132,489.0 | 143,517,568.0 | 60,393.0 |
| `mojibake-curly-quote` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 84,228,979.0 | 83,171,496.0 | 85,924,134.0 | 1,095,213.2 | 5 | 33,280 | 20,907 | 15,704 | 0.013 (max is trial 1) | compiled=5 | 3,199,050.0 | 80,981,197.0 | 51,307.0 |
| `mojibake-curly-quote` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 80,949,055.0 | 80,766,872.0 | 82,293,149.0 | 567,763.4 | 5 | 33,176 | 19,807 | 16,045 | 0.007 | compiled=5 | 1,965,094.0 | 78,957,272.0 | 46,077.0 |
| `mojibake-curly-quote` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 85,575,865.0 | 84,632,166.0 | 93,067,387.0 | 3,179,328.2 | 5 | 33,280 | 21,083 | 15,880 | 0.037 | compiled=5 | 4,437,174.0 | 81,132,038.0 | 53,401.0 |
| `mojibake-curly-quote` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 81,911,488.0 | 81,532,674.0 | 85,545,317.0 | 1,504,603.5 | 5 | 33,176 | 19,863 | 16,101 | 0.018 | compiled=5 | 2,653,803.0 | 79,228,750.0 | 48,642.0 |
| `negation-scope-lookbehind-var` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `negation-scope-lookbehind-var` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `nested-comment-rec` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 150,619,884.0 | 149,965,009.0 | 154,231,843.0 | 1,569,902.8 | 5 | 37,392 | 34,708 | 33,009 | 0.010 | compiled=5 | 2,883,435.0 | 147,945,312.0 | 53,130.0 |
| `nested-comment-rec` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 151,487,068.0 | 150,077,271.0 | 152,839,157.0 | 1,076,810.0 | 5 | 37,392 | 34,821 | 33,122 | 0.007 | compiled=5 | 2,763,469.0 | 148,443,471.0 | 50,154.0 |
| `nested-comment-rec` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 153,377,414.0 | 153,082,879.0 | 154,588,327.0 | 636,380.1 | 5 | 37,392 | 35,308 | 33,609 | 0.004 | compiled=5 | 3,963,932.0 | 150,105,076.0 | 50,515.0 |
| `nested-comment-rec` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 154,817,498.0 | 154,181,199.0 | 156,914,431.0 | 945,286.9 | 5 | 37,392 | 35,421 | 33,722 | 0.006 | compiled=5 | 4,058,991.0 | 150,726,958.0 | 48,281.0 |
| `numeric-id-nested-plus` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 134,789,895.0 | 131,233,901.0 | 135,257,146.0 | 1,887,440.7 | 5 | 37,416 | 31,751 | 30,069 | 0.014 | compiled=5 | 1,712,398.0 | 133,067,698.0 | 50,515.0 |
| `numeric-id-nested-plus` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 134,156,672.0 | 132,251,319.0 | 135,956,804.0 | 1,320,376.8 | 5 | 37,416 | 31,680 | 29,998 | 0.010 | compiled=5 | 1,641,154.0 | 132,313,407.0 | 43,011.0 |
| `numeric-id-nested-plus` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 134,529,866.0 | 132,250,188.0 | 140,807,319.0 | 2,856,235.9 | 5 | 37,416 | 31,807 | 30,125 | 0.021 | compiled=5 | 2,953,898.0 | 131,609,260.0 | 49,213.0 |
| `numeric-id-nested-plus` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 133,014,561.0 | 132,424,486.0 | 135,355,513.0 | 1,060,934.3 | 5 | 37,416 | 31,736 | 30,054 | 0.008 | compiled=5 | 2,917,549.0 | 130,522,321.0 | 53,231.0 |
| `phone-list-nested-plus` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 139,535,370.0 | 139,019,828.0 | 141,183,607.0 | 814,306.8 | 5 | 37,496 | 33,023 | 31,081 | 0.006 | compiled=5 | 1,695,345.0 | 137,793,758.0 | 49,573.0 |
| `phone-list-nested-plus` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 138,138,939.0 | 137,373,626.0 | 140,644,310.0 | 1,124,167.6 | 5 | 37,456 | 32,951 | 31,009 | 0.008 | compiled=5 | 1,808,940.0 | 136,224,449.0 | 44,214.0 |
| `phone-list-nested-plus` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 139,231,259.0 | 137,747,893.0 | 141,104,931.0 | 1,226,177.8 | 5 | 37,496 | 33,079 | 31,137 | 0.009 | compiled=5 | 3,109,682.0 | 135,951,386.0 | 52,179.0 |
| `phone-list-nested-plus` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 139,768,591.0 | 137,933,483.0 | 140,261,520.0 | 849,360.2 | 5 | 37,456 | 33,007 | 31,065 | 0.006 | compiled=5 | 3,069,637.0 | 136,956,370.0 | 49,884.0 |
| `phone-palindrome-6` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 213,630,909.0 | 211,061,866.0 | 214,586,008.0 | 1,275,370.1 | 5 | 36,920 | 26,386 | 24,918 | 0.006 | compiled=5 | 1,765,728.0 | 211,210,466.0 | 43,332.0 |
| `phone-palindrome-6` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 116,484,860.0 | 114,935,099.0 | 118,164,376.0 | 1,026,259.1 | 5 | 32,904 | 26,194 | 24,726 | 0.009 | compiled=5 | 2,485,966.0 | 113,960,502.0 | 51,597.0 |
| `phone-palindrome-6` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 218,682,799.0 | 215,992,397.0 | 221,047,076.0 | 1,801,787.4 | 5 | 36,920 | 26,548 | 25,080 | 0.008 | compiled=5 | 2,790,981.0 | 215,663,667.0 | 46,207.0 |
| `phone-palindrome-6` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 115,554,297.0 | 114,223,276.0 | 118,023,912.0 | 1,276,021.1 | 5 | 32,904 | 26,356 | 24,888 | 0.011 (max is trial 1) | compiled=5 | 2,189,577.0 | 113,352,967.0 | 50,095.0 |
| `pwd-strength-chain` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 130,582,735.0 | 129,933,050.0 | 132,096,247.0 | 851,652.0 | 5 | 37,472 | 34,336 | 31,695 | 0.007 | compiled=5 | 2,549,727.0 | 128,236,893.0 | 43,111.0 |
| `pwd-strength-chain` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 132,980,205.0 | 130,157,253.0 | 133,457,595.0 | 1,317,204.8 | 5 | 37,472 | 34,264 | 31,623 | 0.010 (max is trial 1) | compiled=5 | 2,700,521.0 | 130,223,578.0 | 56,106.0 |
| `pwd-strength-chain` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 128,008,574.0 | 126,924,089.0 | 129,724,918.0 | 1,022,853.7 | 5 | 37,472 | 34,447 | 31,806 | 0.008 | compiled=5 | 3,088,051.0 | 124,808,481.0 | 49,604.0 |
| `pwd-strength-chain` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 127,513,620.0 | 127,201,020.0 | 127,708,778.0 | 204,507.9 | 5 | 37,472 | 34,375 | 31,734 | 0.002 | compiled=5 | 3,051,893.0 | 124,507,022.0 | 52,168.0 |
| `quoted-delim-match` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 138,582,074.0 | 137,652,891.0 | 140,903,146.0 | 1,181,840.6 | 5 | 37,424 | 30,987 | 28,826 | 0.009 | compiled=5 | 2,544,486.0 | 135,937,368.0 | 48,902.0 |
| `quoted-delim-match` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 138,399,739.0 | 137,700,321.0 | 142,054,468.0 | 1,741,567.5 | 5 | 37,424 | 31,100 | 28,939 | 0.013 | compiled=5 | 2,536,471.0 | 135,707,464.0 | 54,322.0 |
| `quoted-delim-match` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 137,491,309.0 | 136,704,044.0 | 139,335,795.0 | 932,894.3 | 5 | 37,424 | 31,043 | 28,882 | 0.007 | compiled=5 | 2,903,013.0 | 134,535,066.0 | 53,230.0 |
| `quoted-delim-match` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 136,322,845.0 | 135,718,866.0 | 136,808,661.0 | 378,216.9 | 5 | 37,424 | 31,156 | 28,995 | 0.003 | compiled=5 | 3,090,636.0 | 133,318,272.0 | 50,566.0 |
| `router-prefix-order` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 78,707,892.0 | 78,043,529.0 | 79,354,971.0 | 491,645.1 | 5 | 28,888 | 16,138 | 14,127 | 0.006 | compiled=5 | 2,212,721.0 | 76,345,218.0 | 53,371.0 |
| `router-prefix-order` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 83,609,973.0 | 83,242,450.0 | 85,253,349.0 | 743,063.9 | 5 | 33,176 | 20,544 | 16,042 | 0.009 | compiled=5 | 2,568,432.0 | 80,681,763.0 | 48,531.0 |
| `router-prefix-order` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 80,490,149.0 | 79,062,005.0 | 81,703,306.0 | 866,068.0 | 5 | 28,888 | 16,194 | 14,183 | 0.011 | compiled=5 | 3,436,839.0 | 76,795,484.0 | 45,877.0 |
| `router-prefix-order` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 83,242,797.0 | 82,866,157.0 | 86,110,012.0 | 1,226,122.1 | 5 | 33,176 | 20,598 | 16,096 | 0.015 | compiled=5 | 4,106,531.0 | 79,677,937.0 | 49,603.0 |
| `tag-depth3-bound` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 169,430,160.0 | 168,869,273.0 | 170,231,802.0 | 496,606.4 | 5 | 37,472 | 38,732 | 36,748 | 0.003 | compiled=5 | 2,953,858.0 | 166,540,774.0 | 49,924.0 |
| `tag-depth3-bound` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 169,400,755.0 | 168,697,098.0 | 170,710,174.0 | 758,043.9 | 5 | 37,472 | 38,845 | 36,861 | 0.004 (max is trial 1) | compiled=5 | 2,981,530.0 | 166,304,178.0 | 52,579.0 |
| `tag-depth3-bound` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 170,163,246.0 | 169,813,447.0 | 170,559,603.0 | 283,025.6 | 5 | 37,472 | 38,894 | 36,910 | 0.002 | compiled=5 | 4,037,872.0 | 166,223,740.0 | 43,763.0 |
| `tag-depth3-bound` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 170,681,113.0 | 170,177,072.0 | 172,056,565.0 | 629,472.0 | 5 | 37,472 | 39,007 | 37,023 | 0.004 | compiled=5 | 3,946,449.0 | 167,316,350.0 | 54,613.0 |
| `tag-pair-match` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 130,005,847.0 | 127,495,364.0 | 131,296,370.0 | 1,239,674.8 | 5 | 33,160 | 30,680 | 28,003 | 0.010 | compiled=5 | 3,010,935.0 | 126,789,575.0 | 55,504.0 |
| `tag-pair-match` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 127,624,677.0 | 126,755,511.0 | 130,937,995.0 | 1,678,536.5 | 5 | 33,160 | 30,793 | 28,116 | 0.013 | compiled=5 | 2,252,816.0 | 125,321,577.0 | 48,361.0 |
| `tag-pair-match` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 128,161,502.0 | 126,931,232.0 | 128,963,434.0 | 695,165.7 | 5 | 33,160 | 30,842 | 28,165 | 0.005 | compiled=5 | 3,991,294.0 | 124,131,485.0 | 40,306.0 |
| `tag-pair-match` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 127,140,617.0 | 126,359,374.0 | 128,149,138.0 | 698,465.4 | 5 | 33,160 | 30,955 | 28,278 | 0.005 (max is trial 1) | compiled=5 | 3,701,748.0 | 123,389,045.0 | 51,748.0 |
| `tail-digits-eol` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 83,134,917.0 | 82,719,944.0 | 83,334,864.0 | 238,723.7 | 5 | 33,128 | 19,601 | 16,146 | 0.003 | compiled=5 | 1,867,260.0 | 81,407,951.0 | 50,235.0 |
| `tail-digits-eol` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 84,447,871.0 | 83,886,975.0 | 85,429,682.0 | 555,465.1 | 5 | 33,176 | 20,809 | 17,263 | 0.007 | compiled=5 | 1,744,899.0 | 82,606,761.0 | 54,994.0 |
| `tail-digits-eol` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 85,961,451.0 | 85,644,555.0 | 87,048,059.0 | 524,865.5 | 5 | 33,128 | 19,657 | 16,202 | 0.006 (max is trial 1) | compiled=5 | 2,580,484.0 | 83,336,734.0 | 50,495.0 |
| `tail-digits-eol` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 86,984,961.0 | 86,342,049.0 | 87,523,817.0 | 431,080.8 | 5 | 33,176 | 20,865 | 17,319 | 0.005 | compiled=5 | 2,664,663.0 | 84,331,660.0 | 51,777.0 |
| `tail-dotstar-txt` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 83,892,414.0 | 83,169,873.0 | 84,435,078.0 | 536,024.3 | 5 | 33,216 | 23,192 | 16,351 | 0.006 | compiled=5 | 2,155,252.0 | 81,660,447.0 | 41,057.0 |
| `tail-dotstar-txt` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 83,871,916.0 | 83,564,165.0 | 84,304,582.0 | 247,724.1 | 5 | 33,256 | 23,872 | 16,919 | 0.003 | compiled=5 | 2,180,701.0 | 81,619,580.0 | 49,152.0 |
| `tail-dotstar-txt` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 87,328,037.0 | 86,242,782.0 | 88,738,908.0 | 940,528.3 | 5 | 33,216 | 23,246 | 16,405 | 0.011 | compiled=5 | 3,080,036.0 | 84,410,838.0 | 48,131.0 |
| `tail-dotstar-txt` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 86,293,629.0 | 85,627,854.0 | 87,703,476.0 | 723,590.9 | 5 | 33,256 | 23,926 | 16,973 | 0.008 | compiled=5 | 3,099,192.0 | 83,152,197.0 | 42,240.0 |
| `tail-ext-lower-txt` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 83,081,577.0 | 82,180,448.0 | 83,947,668.0 | 665,705.2 | 5 | 33,128 | 20,255 | 16,169 | 0.008 | compiled=5 | 2,008,716.0 | 80,800,556.0 | 53,331.0 |
| `tail-ext-lower-txt` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 82,526,740.0 | 82,011,539.0 | 83,259,251.0 | 481,786.0 | 5 | 33,176 | 20,941 | 16,736 | 0.006 | compiled=5 | 2,129,724.0 | 80,332,184.0 | 54,392.0 |
| `tail-ext-lower-txt` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 86,892,357.0 | 85,357,854.0 | 88,096,105.0 | 872,567.2 | 5 | 33,128 | 20,316 | 16,230 | 0.010 | compiled=5 | 3,112,868.0 | 83,740,926.0 | 42,109.0 |
| `tail-ext-lower-txt` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 85,186,802.0 | 84,935,797.0 | 86,495,568.0 | 567,002.6 | 5 | 33,176 | 21,002 | 16,797 | 0.007 | compiled=5 | 2,990,517.0 | 82,172,229.0 | 44,744.0 |
| `tail-space-eol` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 88,201,938.0 | 87,927,030.0 | 88,529,966.0 | 205,513.7 | 5 | 33,256 | 25,461 | 17,499 | 0.002 | compiled=5 | 2,024,707.0 | 86,096,099.0 | 52,468.0 |
| `tail-space-eol` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 85,223,353.0 | 83,812,313.0 | 85,799,019.0 | 782,695.5 | 5 | 33,256 | 23,737 | 17,246 | 0.009 | compiled=5 | 1,829,148.0 | 83,335,715.0 | 53,371.0 |
| `tail-space-eol` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 90,810,373.0 | 89,828,181.0 | 91,511,523.0 | 556,430.2 | 5 | 33,256 | 25,517 | 17,555 | 0.006 (max is trial 1) | compiled=5 | 2,810,588.0 | 87,936,205.0 | 46,367.0 |
| `tail-space-eol` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 87,666,777.0 | 85,970,659.0 | 88,145,669.0 | 774,690.8 | 5 | 33,256 | 23,793 | 17,302 | 0.009 | compiled=5 | 2,628,144.0 | 84,949,194.0 | 44,053.0 |
| `tail-word-eoz` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 84,336,782.0 | 84,038,290.0 | 84,771,751.0 | 255,881.7 | 5 | 33,256 | 23,730 | 17,239 | 0.003 | compiled=5 | 1,852,251.0 | 82,500,611.0 | 51,307.0 |
| `tail-word-eoz` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 84,191,068.0 | 83,196,864.0 | 84,938,616.0 | 618,175.3 | 5 | 33,256 | 23,739 | 17,248 | 0.007 | compiled=5 | 1,881,326.0 | 82,255,249.0 | 53,451.0 |
| `tail-word-eoz` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 87,362,754.0 | 85,466,138.0 | 88,833,295.0 | 1,168,822.1 | 5 | 33,256 | 23,786 | 17,295 | 0.013 | compiled=5 | 2,504,030.0 | 84,655,881.0 | 51,567.0 |
| `tail-word-eoz` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 87,542,012.0 | 86,752,073.0 | 88,057,783.0 | 496,105.2 | 5 | 33,256 | 23,795 | 17,304 | 0.006 | compiled=5 | 2,538,786.0 | 84,954,594.0 | 47,059.0 |
| `trim-nested-star` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 160,170,647.0 | 159,381,238.0 | 164,800,082.0 | 2,029,928.7 | 5 | 37,568 | 30,737 | 28,895 | 0.013 | compiled=5 | 1,563,758.0 | 158,227,003.0 | 54,052.0 |
| `trim-nested-star` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 157,727,040.0 | 156,039,030.0 | 158,642,415.0 | 851,716.2 | 5 | 37,528 | 30,666 | 28,824 | 0.005 | compiled=5 | 1,844,617.0 | 155,758,429.0 | 41,729.0 |
| `trim-nested-star` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 159,968,439.0 | 156,860,040.0 | 160,498,869.0 | 1,423,983.7 | 5 | 37,568 | 30,793 | 28,951 | 0.009 | compiled=5 | 2,898,283.0 | 156,832,728.0 | 48,732.0 |
| `trim-nested-star` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 158,845,093.0 | 156,425,089.0 | 163,686,146.0 | 2,392,591.3 | 5 | 37,528 | 30,722 | 28,880 | 0.015 | compiled=5 | 3,049,148.0 | 155,440,003.0 | 47,028.0 |
| `utf8-lead-no-cont` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 78,784,296.0 | 77,956,706.0 | 79,593,031.0 | 576,587.0 | 5 | 28,896 | 16,166 | 14,372 | 0.007 | compiled=5 | 1,859,084.0 | 76,879,516.0 | 52,810.0 |
| `utf8-lead-no-cont` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 81,085,333.0 | 80,904,732.0 | 81,673,823.0 | 278,725.1 | 5 | 33,232 | 20,351 | 16,608 | 0.003 | compiled=5 | 2,027,181.0 | 79,012,516.0 | 45,536.0 |
| `utf8-lead-no-cont` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 78,590,859.0 | 77,902,890.0 | 80,269,551.0 | 805,925.9 | 5 | 28,896 | 16,222 | 14,428 | 0.010 | compiled=5 | 2,454,336.0 | 75,978,133.0 | 41,388.0 |
| `utf8-lead-no-cont` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 81,520,450.0 | 81,021,720.0 | 83,539,986.0 | 994,076.0 | 5 | 33,232 | 20,407 | 16,664 | 0.012 | compiled=5 | 2,620,880.0 | 78,844,286.0 | 42,290.0 |
| `uuid-near-miss` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 92,045,793.0 | 90,576,615.0 | 92,338,796.0 | 619,064.6 | 5 | 38,456 | 24,873 | 19,469 | 0.007 (max is trial 1) | compiled=5 | 1,495,058.0 | 90,499,659.0 | 47,760.0 |
| `uuid-near-miss` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 93,494,244.0 | 91,319,624.0 | 94,012,741.0 | 1,126,275.3 | 5 | 38,416 | 24,695 | 19,291 | 0.012 | compiled=5 | 1,457,278.0 | 91,998,344.0 | 52,719.0 |
| `uuid-near-miss` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 90,345,055.0 | 90,122,415.0 | 91,643,202.0 | 611,197.8 | 5 | 38,456 | 25,396 | 19,992 | 0.007 | compiled=5 | 2,746,227.0 | 87,871,723.0 | 55,124.0 |
| `uuid-near-miss` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 90,914,069.0 | 89,986,138.0 | 92,090,565.0 | 701,248.4 | 5 | 38,416 | 25,218 | 19,814 | 0.008 | compiled=5 | 2,503,569.0 | 88,186,396.0 | 54,252.0 |
| `wild-codegrammar-json-array-begin` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 75,190,431.0 | 74,813,471.0 | 75,978,087.0 | 433,777.2 | 5 | 28,888 | 15,592 | 13,923 | 0.006 | compiled=5 | 1,670,539.0 | 73,511,818.0 | 52,018.0 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 79,076,717.0 | 78,798,152.0 | 79,786,114.0 | 342,087.6 | 5 | 33,176 | 19,582 | 16,024 | 0.004 (max is trial 1) | compiled=5 | 1,800,323.0 | 77,334,814.0 | 53,491.0 |
| `wild-codegrammar-json-array-begin` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 76,990,641.0 | 76,677,230.0 | 78,026,504.0 | 513,858.7 | 5 | 28,888 | 15,648 | 13,979 | 0.007 | compiled=5 | 2,472,982.0 | 74,493,664.0 | 51,488.0 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 81,493,279.0 | 80,910,681.0 | 83,163,838.0 | 924,522.7 | 5 | 33,176 | 19,638 | 16,080 | 0.011 | compiled=5 | 2,387,761.0 | 79,091,422.0 | 42,650.0 |
| `wild-codegrammar-json-constant` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 84,783,665.0 | 84,494,069.0 | 85,397,592.0 | 304,852.1 | 5 | 33,592 | 29,801 | 17,540 | 0.004 | compiled=5 | 2,757,909.0 | 81,968,838.0 | 54,222.0 |
| `wild-codegrammar-json-constant` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 85,102,736.0 | 84,374,833.0 | 85,316,890.0 | 390,231.2 | 5 | 33,344 | 25,975 | 18,066 | 0.005 | compiled=5 | 2,099,527.0 | 82,928,358.0 | 54,252.0 |
| `wild-codegrammar-json-constant` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 91,016,350.0 | 90,558,837.0 | 91,405,684.0 | 285,534.8 | 5 | 33,592 | 30,009 | 17,748 | 0.003 (max is trial 1) | compiled=5 | 6,667,930.0 | 84,272,377.0 | 49,543.0 |
| `wild-codegrammar-json-constant` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 87,433,716.0 | 86,984,481.0 | 89,111,369.0 | 789,675.2 | 5 | 33,344 | 26,062 | 18,153 | 0.009 | compiled=5 | 3,131,503.0 | 84,191,806.0 | 54,132.0 |
| `wild-codegrammar-json-number-extended` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 88,411,343.0 | 87,637,304.0 | 89,243,702.0 | 527,897.8 | 5 | 33,272 | 25,946 | 17,624 | 0.006 | compiled=5 | 2,404,533.0 | 85,952,067.0 | 56,206.0 |
| `wild-codegrammar-json-number-extended` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 83,412,940.0 | 82,527,392.0 | 84,365,557.0 | 682,742.3 | 5 | 33,176 | 22,457 | 17,095 | 0.008 | compiled=5 | 1,864,515.0 | 81,438,158.0 | 53,812.0 |
| `wild-codegrammar-json-number-extended` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 92,400,089.0 | 91,319,603.0 | 93,793,276.0 | 875,481.5 | 5 | 33,272 | 26,002 | 17,680 | 0.009 (max is trial 1) | compiled=5 | 3,626,496.0 | 88,723,719.0 | 52,750.0 |
| `wild-codegrammar-json-number-extended` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 85,802,442.0 | 84,586,739.0 | 87,260,701.0 | 944,980.3 | 5 | 33,176 | 22,513 | 17,151 | 0.011 | compiled=5 | 2,792,834.0 | 83,154,821.0 | 48,000.0 |
| `wild-codegrammar-json-object-begin` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 75,161,587.0 | 74,459,454.0 | 75,658,594.0 | 462,740.5 | 5 | 28,888 | 15,594 | 13,925 | 0.006 (max is trial 1) | compiled=5 | 1,703,371.0 | 73,421,387.0 | 46,718.0 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 79,200,972.0 | 78,673,608.0 | 79,564,586.0 | 331,838.8 | 5 | 33,176 | 19,583 | 16,025 | 0.004 | compiled=5 | 1,790,425.0 | 77,241,798.0 | 51,236.0 |
| `wild-codegrammar-json-object-begin` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 77,511,153.0 | 76,836,491.0 | 79,313,950.0 | 830,031.6 | 5 | 28,888 | 15,650 | 13,981 | 0.011 | compiled=5 | 2,319,683.0 | 75,202,761.0 | 47,870.0 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 82,079,794.0 | 80,568,706.0 | 83,103,183.0 | 877,846.8 | 5 | 33,176 | 19,639 | 16,081 | 0.011 (max is trial 1) | compiled=5 | 2,612,465.0 | 79,449,807.0 | 48,481.0 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 81,631,603.0 | 80,994,983.0 | 82,199,753.0 | 439,693.8 | 5 | 33,280 | 22,059 | 15,964 | 0.005 | compiled=5 | 3,055,459.0 | 78,547,219.0 | 52,799.0 |
| `wild-codegrammar-json-stringcontent-escape` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 80,047,537.0 | 79,646,591.0 | 81,586,819.0 | 753,543.6 | 5 | 33,176 | 20,851 | 16,308 | 0.009 | compiled=5 | 1,880,435.0 | 78,116,958.0 | 54,623.0 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 85,738,601.0 | 84,412,712.0 | 88,472,124.0 | 1,439,361.5 | 5 | 33,280 | 22,235 | 16,140 | 0.017 | compiled=5 | 4,185,860.0 | 81,499,220.0 | 50,435.0 |
| `wild-codegrammar-json-stringcontent-escape` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 83,333,387.0 | 82,926,652.0 | 83,697,635.0 | 322,905.7 | 5 | 33,176 | 20,907 | 16,364 | 0.004 | compiled=5 | 2,744,865.0 | 80,604,955.0 | 40,887.0 |
| `wild-datetime-datefinder-alternation` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 235,600,479.0 | - | - |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 3,361,286,441.0 | - | - |
| `wild-datetime-datefinder-alternation` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 1,498,153,217.0 | 1,483,070,525.0 | 1,524,451,852.0 | 14,065,597.4 | 5 | 102,912 | 278,089 (warned) | 275,686 | 0.009 (max is trial 1) | compiled=5 | 148,717,600.0 | 1,349,311,703.0 | 54,362.0 |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 2,070,732,419.0 | 2,023,838,882.0 | 2,306,653,873.0 | 109,903,144.4 | 5 | 242,416 | 786,823 (warned) | 279,941 | 0.053 | compiled=5 | 576,787,184.0 | 1,493,894,419.0 | 45,867.0 |
| `wild-datetime-moment-iso8601` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 178,218,967.0 | 177,773,247.0 | 180,539,691.0 | 971,028.2 | 5 | 55,416 | 57,021 | 47,098 | 0.005 (max is trial 1) | compiled=5 | 2,964,458.0 | 175,230,744.0 | 54,282.0 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 178,087,729.0 | 176,882,459.0 | 179,501,254.0 | 972,153.7 | 5 | 55,040 | 55,460 | 45,537 | 0.005 | compiled=5 | 2,992,270.0 | 174,901,664.0 | 55,454.0 |
| `wild-datetime-moment-iso8601` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 176,452,622.0 | 174,402,077.0 | 181,848,544.0 | 2,865,750.2 | 5 | 55,456 | 56,341 | 46,187 | 0.016 | compiled=5 | 4,742,760.0 | 172,142,267.0 | 48,381.0 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 172,482,619.0 | 170,510,711.0 | 174,383,372.0 | 1,234,376.6 | 5 | 55,088 | 54,780 | 44,626 | 0.007 | compiled=5 | 4,485,535.0 | 167,718,799.0 | 57,078.0 |
| `wild-logparse-base10num-grok` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 124,205,824.0 | 123,782,867.0 | 124,396,485.0 | 204,327.6 | 5 | 33,472 | 37,124 | 29,859 | 0.002 (max is trial 1) | compiled=5 | 3,221,372.0 | 120,937,143.0 | 50,435.0 |
| `wild-logparse-base10num-grok` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 116,237,484.0 | 115,204,657.0 | 117,420,414.0 | 735,353.3 | 5 | 33,232 | 31,127 | 28,577 | 0.006 | compiled=5 | 2,745,495.0 | 113,415,615.0 | 52,809.0 |
| `wild-logparse-base10num-grok` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 128,382,027.0 | 127,502,990.0 | 130,645,603.0 | 1,202,676.8 | 5 | 33,472 | 37,180 | 29,915 | 0.009 | compiled=5 | 4,537,784.0 | 124,180,787.0 | 44,233.0 |
| `wild-logparse-base10num-grok` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 120,097,751.0 | 118,673,915.0 | 121,010,863.0 | 824,532.9 | 5 | 33,232 | 31,183 | 28,633 | 0.007 | compiled=5 | 3,678,504.0 | 116,645,363.0 | 49,082.0 |
| `wild-logparse-base10num-noatomic` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 92,077,854.0 | 91,758,864.0 | 92,538,090.0 | 251,123.9 | 5 | 33,472 | 26,859 | 18,254 | 0.003 | compiled=5 | 2,487,609.0 | 89,615,152.0 | 49,643.0 |
| `wild-logparse-base10num-noatomic` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 84,161,041.0 | 83,996,220.0 | 84,811,566.0 | 300,041.2 | 5 | 33,280 | 21,429 | 17,412 | 0.004 | compiled=5 | 1,855,638.0 | 82,252,112.0 | 57,057.0 |
| `wild-logparse-base10num-noatomic` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 95,371,059.0 | 93,924,453.0 | 97,142,148.0 | 1,072,359.0 | 5 | 33,472 | 26,915 | 18,310 | 0.011 | compiled=5 | 3,371,656.0 | 92,151,901.0 | 53,972.0 |
| `wild-logparse-base10num-noatomic` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 87,934,923.0 | 87,481,799.0 | 88,783,722.0 | 490,095.9 | 5 | 33,280 | 21,485 | 17,468 | 0.006 | compiled=5 | 2,691,213.0 | 85,248,388.0 | 51,527.0 |
| `wild-logparse-quotedstring-grok` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 200,849,505.0 | 199,828,510.0 | 201,789,306.0 | 728,926.0 | 5 | 46,408 | 66,095 | 45,434 | 0.004 | compiled=5 | 4,529,478.0 | 196,298,757.0 | 50,425.0 |
| `wild-logparse-quotedstring-grok` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 198,906,142.0 | 192,669,466.0 | 204,291,533.0 | 4,158,708.2 | 5 | 41,936 | 52,583 | 44,277 | 0.021 | compiled=5 | 4,588,889.0 | 193,903,603.0 | 54,112.0 |
| `wild-logparse-quotedstring-grok` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 211,232,745.0 | 209,694,075.0 | 214,176,183.0 | 1,464,344.5 | 5 | 46,408 | 66,257 | 45,596 | 0.007 | compiled=5 | 5,796,447.0 | 205,565,682.0 | 49,704.0 |
| `wild-logparse-quotedstring-grok` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 201,351,156.0 | 199,050,550.0 | 202,218,664.0 | 1,306,297.6 | 5 | 41,936 | 52,745 | 44,439 | 0.006 | compiled=5 | 5,556,654.0 | 196,220,015.0 | 46,218.0 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 101,961,604.0 | 100,753,768.0 | 102,076,280.0 | 505,919.2 | 5 | 37,968 | 44,989 | 18,925 | 0.005 | compiled=5 | 4,887,703.0 | 96,926,524.0 | 52,649.0 |
| `wild-logparse-quotedstring-noatomic` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 94,573,840.0 | 93,468,244.0 | 95,605,954.0 | 693,702.8 | 5 | 33,552 | 32,145 | 18,300 | 0.007 | compiled=5 | 3,734,710.0 | 90,851,112.0 | 41,047.0 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 103,068,039.0 | 102,358,702.0 | 104,514,996.0 | 748,293.4 | 5 | 37,968 | 45,165 | 19,101 | 0.007 | compiled=5 | 5,107,228.0 | 98,121,945.0 | 47,349.0 |
| `wild-logparse-quotedstring-noatomic` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 94,133,517.0 | 93,193,886.0 | 95,957,365.0 | 1,168,225.6 | 5 | 33,552 | 32,201 | 18,356 | 0.012 | compiled=5 | 4,241,957.0 | 90,234,346.0 | 44,083.0 |
| `wild-logparse-syslogbase-expanded` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 2,431,309,514.0 | 2,400,414,958.0 | 2,445,818,203.0 | 16,442,475.9 | 5 | 181,400 | 516,370 (warned) | 300,070 | 0.007 | compiled=5 | 299,245,949.0 | 2,135,331,885.0 | 52,178.0 |
| `wild-logparse-syslogbase-expanded` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 2,542,180,973.0 | 2,444,521,137.0 | 2,863,954,055.0 | 174,546,855.5 | 5 | 189,264 | 561,742 (warned) | 299,134 | 0.069 | compiled=5 | 642,271,201.0 | 1,845,807,300.0 | 47,690.0 |
| `wild-logparse-syslogbase-expanded` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 2,263,711,845.0 | 2,120,622,565.0 | 2,477,378,567.0 | 142,400,592.3 | 5 | 177,304 | 512,489 (warned) | 296,189 | 0.063 (max is trial 1) | compiled=5 | 285,846,966.0 | 1,977,812,520.0 | 40,096.0 |
| `wild-logparse-syslogbase-expanded` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 2,422,223,949.0 | 2,378,464,200.0 | 2,574,535,074.0 | 70,564,375.7 | 5 | 189,264 | 557,090 (warned) | 294,482 | 0.029 | compiled=5 | 560,026,899.0 | 1,845,104,919.0 | 50,104.0 |
| `wild-logparse-winpath-grok` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 138,591,171.0 | 136,520,757.0 | 139,043,884.0 | 929,799.2 | 5 | 37,712 | 39,372 | 30,888 | 0.007 (max is trial 1) | compiled=5 | 4,491,877.0 | 134,231,392.0 | 51,146.0 |
| `wild-logparse-winpath-grok` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 128,576,763.0 | 126,515,177.0 | 130,403,406.0 | 1,257,231.9 | 5 | 33,384 | 33,854 | 29,931 | 0.010 | compiled=5 | 3,079,335.0 | 125,484,414.0 | 53,400.0 |
| `wild-logparse-winpath-grok` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 139,868,731.0 | 139,552,745.0 | 140,624,594.0 | 378,919.4 | 5 | 37,712 | 39,534 | 31,050 | 0.003 | compiled=5 | 6,678,680.0 | 133,265,723.0 | 54,383.0 |
| `wild-logparse-winpath-grok` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 131,458,695.0 | 130,316,634.0 | 132,164,286.0 | 657,045.6 | 5 | 37,480 | 34,016 | 30,093 | 0.005 | compiled=5 | 3,615,675.0 | 127,889,648.0 | 50,936.0 |
| `wild-secrets-aws-access-key-id` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 127,312,440.0 | 126,955,688.0 | 128,229,829.0 | 424,766.4 | 5 | 33,248 | 36,965 | 29,288 | 0.003 | compiled=5 | 6,751,817.0 | 120,486,915.0 | 49,924.0 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 123,817,012.0 | 122,748,888.0 | 124,777,432.0 | 735,008.7 | 5 | 33,200 | 38,975 | 30,230 | 0.006 | compiled=5 | 4,045,506.0 | 119,608,439.0 | 48,862.0 |
| `wild-secrets-aws-access-key-id` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 140,784,957.0 | 138,808,922.0 | 143,021,613.0 | 1,384,784.9 | 5 | 33,288 | 38,469 | 31,117 | 0.010 | compiled=5 | 13,730,183.0 | 126,997,797.0 | 47,019.0 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 125,675,205.0 | 124,122,748.0 | 126,820,102.0 | 886,387.3 | 5 | 33,200 | 38,734 | 30,354 | 0.007 | compiled=5 | 5,236,170.0 | 120,196,858.0 | 52,700.0 |
| `wild-secrets-github-pat` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 247,782,141.0 | 247,346,169.0 | 251,121,136.0 | 1,392,837.0 | 5 | 41,360 | 41,877 | 27,019 | 0.006 | compiled=5 | 8,554,494.0 | 239,361,870.0 | 50,686.0 |
| `wild-secrets-github-pat` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 225,996,336.0 | 224,982,225.0 | 226,489,747.0 | 540,521.5 | 5 | 41,304 | 42,934 | 26,513 | 0.002 | compiled=5 | 4,867,225.0 | 221,183,063.0 | 54,974.0 |
| `wild-secrets-github-pat` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 260,821,843.0 | 258,437,469.0 | 263,325,883.0 | 1,792,537.3 | 5 | 41,360 | 42,328 | 27,470 | 0.007 | compiled=5 | 13,532,349.0 | 247,045,233.0 | 46,818.0 |
| `wild-secrets-github-pat` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 234,546,673.0 | 234,071,677.0 | 235,449,225.0 | 480,145.1 | 5 | 41,304 | 43,501 | 27,080 | 0.002 | compiled=5 | 6,909,915.0 | 227,837,696.0 | 41,799.0 |
| `wild-secrets-slack-webhook-url` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 153,411,306.0 | 150,087,780.0 | 157,898,253.0 | 3,015,259.1 | 5 | 58,024 | 107,666 | 36,316 | 0.020 | compiled=5 | 10,152,377.0 | 143,195,199.0 | 55,515.0 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 140,265,575.0 | 137,768,811.0 | 140,881,557.0 | 1,193,298.3 | 5 | 41,456 | 57,188 | 34,564 | 0.009 | compiled=5 | 5,136,132.0 | 134,953,774.0 | 59,632.0 |
| `wild-secrets-slack-webhook-url` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 161,350,764.0 | 161,139,876.0 | 162,026,307.0 | 326,980.6 | 5 | 58,024 | 109,379 | 38,029 | 0.002 (max is trial 1) | compiled=5 | 12,986,810.0 | 148,312,998.0 | 49,513.0 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 141,528,156.0 | 140,094,576.0 | 143,608,399.0 | 1,157,258.3 | 5 | 41,456 | 57,705 | 35,081 | 0.008 | compiled=5 | 7,880,645.0 | 133,376,804.0 | 50,264.0 |
| `wild-secrets-username-password-pair` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 296,036,239.0 | 294,900,238.0 | 297,655,933.0 | 1,116,015.4 | 5 | 214,272 | 555,019 (warned) | 47,226 | 0.004 | compiled=5 | 29,044,468.0 | 266,761,166.0 | 50,175.0 |
| `wild-secrets-username-password-pair` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 212,020,702.0 | 209,688,367.0 | 213,220,384.0 | 1,316,917.8 | 5 | 54,288 | 99,799 | 43,288 | 0.006 | compiled=5 | 18,509,159.0 | 193,683,958.0 | 53,501.0 |
| `wild-secrets-username-password-pair` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 293,766,516.0 | 291,554,616.0 | 308,248,654.0 | 6,094,879.0 | 5 | 214,320 | 556,225 (warned) | 46,958 | 0.021 (max is trial 1) | compiled=5 | 38,715,480.0 | 256,501,740.0 | 46,799.0 |
| `wild-secrets-username-password-pair` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 211,236,712.0 | 210,156,175.0 | 219,775,157.0 | 3,521,107.5 | 5 | 54,288 | 99,961 | 43,450 | 0.017 | compiled=5 | 20,778,508.0 | 191,028,178.0 | 42,480.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 82,544,784.0 | 81,762,109.0 | 84,865,840.0 | 1,046,554.2 | 5 | 32,984 | 16,834 | 15,006 | 0.013 | compiled=5 | 2,233,309.0 | 80,172,693.0 | 53,080.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 84,834,912.0 | 84,679,829.0 | 86,270,236.0 | 587,423.2 | 5 | 33,176 | 21,198 | 16,758 | 0.007 | compiled=5 | 2,326,275.0 | 82,374,593.0 | 49,964.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 82,587,651.0 | 82,175,455.0 | 84,053,155.0 | 671,154.8 | 5 | 32,984 | 16,890 | 15,062 | 0.008 | compiled=5 | 3,036,083.0 | 79,469,364.0 | 51,708.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 85,529,237.0 | 84,451,996.0 | 86,167,281.0 | 671,536.4 | 5 | 33,176 | 21,252 | 16,812 | 0.008 | compiled=5 | 3,124,400.0 | 82,135,940.0 | 50,655.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 83,194,499.0 | 82,620,216.0 | 85,844,084.0 | 1,238,491.1 | 5 | 33,128 | 19,131 | 15,346 | 0.015 | compiled=5 | 2,231,737.0 | 80,907,919.0 | 51,597.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 82,828,248.0 | 81,798,558.0 | 83,598,511.0 | 595,090.0 | 5 | 33,176 | 19,920 | 16,030 | 0.007 (max is trial 1) | compiled=5 | 1,966,026.0 | 80,815,985.0 | 46,237.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 82,571,471.0 | 81,488,961.0 | 84,353,412.0 | 921,372.6 | 5 | 33,128 | 19,185 | 15,400 | 0.011 | compiled=5 | 3,142,163.0 | 79,466,909.0 | 46,818.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 82,019,351.0 | 81,672,087.0 | 82,898,087.0 | 509,992.3 | 5 | 33,176 | 19,974 | 16,084 | 0.006 | compiled=5 | 3,229,017.0 | 79,185,940.0 | 46,167.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 137,845,354.0 | 135,072,248.0 | 140,010,656.0 | 1,606,110.5 | 5 | 37,632 | 35,239 | 30,405 | 0.012 | compiled=5 | 3,261,728.0 | 134,423,063.0 | 49,784.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 134,839,219.0 | 134,384,732.0 | 136,325,480.0 | 662,275.2 | 5 | 37,488 | 31,965 | 30,162 | 0.005 | compiled=5 | 2,945,833.0 | 131,980,219.0 | 49,884.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 137,921,890.0 | 135,477,793.0 | 141,874,902.0 | 2,078,644.3 | 5 | 37,632 | 35,295 | 30,461 | 0.015 | compiled=5 | 4,265,561.0 | 133,509,292.0 | 46,187.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 132,342,583.0 | 131,589,191.0 | 134,010,568.0 | 800,129.1 | 5 | 37,488 | 32,021 | 30,218 | 0.006 | compiled=5 | 3,560,272.0 | 128,878,432.0 | 52,680.0 |
| `wild-validator-email-owasp` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 79,145,467.0 | 78,004,666.0 | 79,840,977.0 | 676,876.2 | 5 | 37,192 | 16,843 | 14,486 | 0.009 | compiled=5 | 1,342,982.0 | 77,742,382.0 | 50,725.0 |
| `wild-validator-email-owasp` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 78,126,606.0 | 77,329,746.0 | 79,962,907.0 | 865,414.3 | 5 | 37,192 | 16,666 | 14,309 | 0.011 (max is trial 1) | compiled=5 | 1,364,041.0 | 76,714,264.0 | 49,012.0 |
| `wild-validator-email-owasp` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 77,328,128.0 | 76,318,094.0 | 78,066,750.0 | 619,176.5 | 5 | 37,192 | 16,899 | 14,542 | 0.008 | compiled=5 | 1,657,585.0 | 75,515,190.0 | 53,141.0 |
| `wild-validator-email-owasp` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 76,862,910.0 | 76,228,785.0 | 78,232,563.0 | 690,096.5 | 5 | 37,192 | 16,722 | 14,365 | 0.009 | compiled=5 | 1,792,579.0 | 75,013,374.0 | 54,693.0 |
| `wild-validator-ipv4-owasp` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 157,830,055.0 | 157,408,069.0 | 158,367,278.0 | 315,987.3 | 5 | 42,344 | 47,471 | 42,443 | 0.002 | compiled=5 | 2,860,442.0 | 155,449,608.0 | 49,753.0 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 156,909,280.0 | 155,036,098.0 | 159,150,133.0 | 1,428,216.3 | 5 | 42,144 | 46,654 | 41,626 | 0.009 | compiled=5 | 2,950,171.0 | 153,920,225.0 | 48,321.0 |
| `wild-validator-ipv4-owasp` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 155,448,550.0 | 155,089,612.0 | 155,935,125.0 | 278,657.2 | 5 | 42,344 | 47,582 | 42,554 | 0.002 | compiled=5 | 3,596,279.0 | 152,056,484.0 | 49,403.0 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 153,293,857.0 | 152,345,770.0 | 155,757,732.0 | 1,248,569.3 | 5 | 42,144 | 46,765 | 41,737 | 0.008 | compiled=5 | 3,637,487.0 | 150,162,063.0 | 54,623.0 |
| `wild-validator-us-zip-owasp` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 124,569,568.0 | 123,652,562.0 | 125,384,506.0 | 611,205.3 | 5 | 37,688 | 31,173 | 28,629 | 0.005 (max is trial 1) | compiled=5 | 1,735,341.0 | 122,718,560.0 | 52,870.0 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 122,619,484.0 | 121,815,248.0 | 124,820,121.0 | 1,099,334.6 | 5 | 37,608 | 30,913 | 28,369 | 0.009 | compiled=5 | 1,604,254.0 | 121,078,820.0 | 53,891.0 |
| `wild-validator-us-zip-owasp` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 121,890,670.0 | 120,601,281.0 | 122,985,524.0 | 788,545.7 | 5 | 37,688 | 31,322 | 28,778 | 0.006 | compiled=5 | 3,082,881.0 | 118,808,431.0 | 53,751.0 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 120,289,933.0 | 119,983,866.0 | 121,555,379.0 | 624,504.1 | 5 | 37,608 | 31,062 | 28,518 | 0.005 | compiled=5 | 3,008,591.0 | 118,070,249.0 | 52,399.0 |
| `wild-validator-uuid-grok` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 109,999,266.0 | 108,843,286.0 | 111,090,432.0 | 760,025.3 | 5 | 33,528 | 37,712 | 20,314 | 0.007 (max is trial 1) | compiled=5 | 5,471,824.0 | 104,027,318.0 | 46,858.0 |
| `wild-validator-uuid-grok` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 105,092,006.0 | 104,155,220.0 | 106,188,503.0 | 712,227.2 | 5 | 33,536 | 37,272 | 20,988 | 0.007 | compiled=5 | 4,428,247.0 | 101,010,572.0 | 51,818.0 |
| `wild-validator-uuid-grok` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 118,855,880.0 | 117,648,834.0 | 120,320,520.0 | 978,639.6 | 5 | 37,624 | 40,269 | 22,871 | 0.008 | compiled=5 | 8,704,238.0 | 110,095,797.0 | 53,120.0 |
| `wild-validator-uuid-grok` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 104,829,288.0 | 104,534,242.0 | 107,079,832.0 | 1,065,829.2 | 5 | 37,632 | 37,808 | 21,524 | 0.010 | compiled=5 | 5,297,667.0 | 100,175,516.0 | 45,125.0 |
| `wild-waf-crs-942140-dbnames` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 119,423,710.0 | 118,612,952.0 | 120,025,484.0 | 475,686.6 | 5 | 91,216 | 229,297 | 21,335 | 0.004 | compiled=5 | 9,406,220.0 | 109,867,917.0 | 52,800.0 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 111,496,599.0 | 110,182,439.0 | 111,788,207.0 | 706,108.8 | 5 | 74,488 | 170,968 | 20,725 | 0.006 | compiled=5 | 7,562,325.0 | 103,833,994.0 | 50,956.0 |
| `wild-waf-crs-942140-dbnames` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 123,743,093.0 | 122,790,957.0 | 124,500,579.0 | 647,867.5 | 5 | 91,216 | 229,473 | 21,511 | 0.005 | compiled=5 | 13,500,680.0 | 110,610,967.0 | 49,123.0 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 112,464,332.0 | 111,544,617.0 | 112,819,310.0 | 458,694.6 | 5 | 74,488 | 171,024 | 20,781 | 0.004 | compiled=5 | 11,377,276.0 | 101,351,162.0 | 49,493.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 107,295,368.0 | 105,487,150.0 | 109,590,114.0 | 1,401,688.0 | 5 | 41,968 | 59,626 | 19,226 | 0.013 | compiled=5 | 6,557,090.0 | 100,751,193.0 | 51,647.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 96,293,972.0 | 95,517,858.0 | 97,778,298.0 | 739,945.4 | 5 | 37,536 | 41,044 | 18,575 | 0.008 | compiled=5 | 3,250,096.0 | 92,866,521.0 | 51,136.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 111,761,114.0 | 110,057,653.0 | 113,948,600.0 | 1,283,588.7 | 5 | 41,968 | 59,848 | 19,448 | 0.011 | compiled=5 | 11,172,171.0 | 100,273,460.0 | 51,006.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 95,688,447.0 | 95,384,043.0 | 96,404,056.0 | 362,886.2 | 5 | 37,536 | 41,146 | 18,677 | 0.004 | compiled=5 | 4,037,601.0 | 91,734,334.0 | 49,062.0 |
| `wild-waf-crs-942270-union-select` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 108,096,229.0 | 107,593,652.0 | 110,349,234.0 | 1,101,964.0 | 5 | 37,688 | 39,661 | 18,494 | 0.010 | compiled=5 | 9,464,791.0 | 98,588,477.0 | 50,465.0 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 90,286,879.0 | 87,940,104.0 | 91,497,259.0 | 1,330,792.2 | 5 | 33,352 | 31,007 | 17,010 | 0.015 | compiled=5 | 3,100,514.0 | 87,143,764.0 | 51,217.0 |
| `wild-waf-crs-942270-union-select` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 110,669,738.0 | 109,327,048.0 | 113,080,384.0 | 1,325,038.3 | 5 | 37,688 | 39,839 | 18,672 | 0.012 | compiled=5 | 13,260,427.0 | 97,732,430.0 | 54,412.0 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 88,996,113.0 | 88,424,504.0 | 89,816,409.0 | 579,526.3 | 5 | 33,352 | 31,061 | 17,064 | 0.007 | compiled=5 | 3,857,592.0 | 84,890,594.0 | 42,801.0 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 648,693,949.0 | 600,873,939.0 | 685,895,612.0 | 30,147,172.2 | 5 | 685,928 | 395,899 (warned) | 101,419 | 0.046 (max is trial 1) | compiled=5 | 19,543,509.0 | 629,016,297.0 | 134,143.0 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 592,495,295.0 | 590,091,786.0 | 602,373,105.0 | 4,415,335.1 | 5 | 679,520 | 516,574 (warned) | 117,200 | 0.007 | compiled=5 | 17,468,077.0 | 574,684,513.0 | 137,730.0 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 697,766,376.0 | 696,217,527.0 | 747,010,113.0 | 19,746,488.3 | 5 | 685,928 | 395,955 (warned) | 101,475 | 0.028 | compiled=5 | 46,105,180.0 | 657,649,293.0 | 125,867.0 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 681,174,059.0 | 676,670,649.0 | 689,688,870.0 | 4,721,839.7 | 5 | 679,520 | 516,630 (warned) | 117,256 | 0.007 | compiled=5 | 43,933,807.0 | 643,058,068.0 | 115,858.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 85,665,156.0 | 85,176,204.0 | 87,458,757.0 | 779,290.2 | 5 | 33,280 | 22,788 | 16,876 | 0.009 | compiled=5 | 3,641,945.0 | 82,159,979.0 | 50,024.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 80,107,721.0 | 79,722,614.0 | 80,793,272.0 | 375,387.2 | 5 | 33,176 | 20,456 | 16,094 | 0.005 (max is trial 1) | compiled=5 | 2,048,100.0 | 78,021,809.0 | 53,531.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 86,701,968.0 | 86,062,574.0 | 87,858,407.0 | 671,886.8 | 5 | 33,280 | 22,311 | 16,399 | 0.008 (max is trial 1) | compiled=5 | 3,873,813.0 | 82,970,193.0 | 47,599.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 83,206,469.0 | 82,213,608.0 | 83,656,147.0 | 480,922.8 | 5 | 33,176 | 20,510 | 16,148 | 0.006 | compiled=5 | 2,987,732.0 | 79,950,561.0 | 44,013.0 |
| `winpath-near-miss` | `plain` | `pcrec_cb32eda28_auto-caps-simdna` | 78,911,165.0 | 76,620,317.0 | 80,505,710.0 | 1,286,909.6 | 5 | 37,152 | 16,232 | 14,149 | 0.016 | compiled=5 | 1,300,281.0 | 77,520,394.0 | 44,534.0 |
| `winpath-near-miss` | `whole-subject` | `pcrec_cb32eda28_auto-caps-simdna` | 78,455,046.0 | 77,899,438.0 | 78,862,374.0 | 373,766.7 | 5 | 37,112 | 16,055 | 13,972 | 0.005 (max is trial 1) | compiled=5 | 1,355,876.0 | 77,016,394.0 | 45,716.0 |
| `winpath-near-miss` | `plain` | `pcrec_d6c5e71a5_auto-caps-simdna` | 77,702,613.0 | 77,303,000.0 | 79,529,136.0 | 806,274.5 | 5 | 37,152 | 16,298 | 14,215 | 0.010 | compiled=5 | 1,611,838.0 | 76,148,694.0 | 42,389.0 |
| `winpath-near-miss` | `whole-subject` | `pcrec_d6c5e71a5_auto-caps-simdna` | 77,589,309.0 | 76,991,243.0 | 78,963,380.0 | 683,836.4 | 5 | 37,112 | 16,121 | 14,038 | 0.009 | compiled=5 | 1,760,589.0 | 75,826,377.0 | 47,719.0 |
    - emit/code bytes across abi 77: pcrec's size definition moves at the boundary -- a flat ~+106 B of counted stamp and initializer lines on a typical artifact (`RX_COMPOUND`, `RX_MEASURES`, `.measures`/`.next`/`.next_n`), and from abi 83 the find-all iterator scaffold (`_next`, the forwarder twins) is EXCLUDED from both counts with no marker in the emitted text. Read a Delta that spans the boundary against that, not as a program change; the DFA retry machine (`RX_ITER_RETRY=retry`) is NOT scaffold and counts (b142prep: +3-4 KB on narrow DFAs).

