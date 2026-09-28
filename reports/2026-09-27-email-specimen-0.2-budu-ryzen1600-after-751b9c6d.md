# pcrec-bench report

reporter: v25 (2026-09-26)

## Query

- filters: subbench=email-specimen, version=0.2, testee=pcrec_25b1984f_auto-caps-simdna, testee=pcrec_25b1984f_auto-nocaps-simdna, testee=pcrec_25b1984f_vm-caps-simdna, testee=pcrec_25b1984f_vm-in-caps-simdna, testee=pcrec_751b9c6d_auto-caps-simdna, testee=pcrec_751b9c6d_auto-nocaps-simdna, testee=pcrec_751b9c6d_vm-caps-simdna, testee=pcrec_751b9c6d_vm-in-caps-simdna
- record source: store/index.tsv (8 record(s) matching this query)
- records included: 8
- worst other-core busy: 5.43% (`pcrec_25b1984f_auto-caps-simdna` / `orig` / `large-subject-throughput`)
    - `email-specimen@0.2__pcrec_25b1984f_auto-caps-simdna__budu-ryzen1600__20260921T065926Z` (store/records/email-specimen@0.2/pcrec_25b1984f_auto-caps-simdna/email-specimen@0.2__pcrec_25b1984f_auto-caps-simdna__budu-ryzen1600__20260921T065926Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_25b1984f_auto-nocaps-simdna__budu-ryzen1600__20260921T070439Z` (store/records/email-specimen@0.2/pcrec_25b1984f_auto-nocaps-simdna/email-specimen@0.2__pcrec_25b1984f_auto-nocaps-simdna__budu-ryzen1600__20260921T070439Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_25b1984f_vm-caps-simdna__budu-ryzen1600__20260921T070947Z` (store/records/email-specimen@0.2/pcrec_25b1984f_vm-caps-simdna/email-specimen@0.2__pcrec_25b1984f_vm-caps-simdna__budu-ryzen1600__20260921T070947Z.jsonl) — agreement: agree (0 of 8 groups; 0 of 490 rows; 11 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_25b1984f_vm-in-caps-simdna__budu-ryzen1600__20260921T071628Z` (store/records/email-specimen@0.2/pcrec_25b1984f_vm-in-caps-simdna/email-specimen@0.2__pcrec_25b1984f_vm-in-caps-simdna__budu-ryzen1600__20260921T071628Z.jsonl) — agreement: agree (0 of 8 groups; 0 of 495 rows; 6 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_751b9c6d_auto-caps-simdna__budu-ryzen1600__20260927T091338Z` (store/records/email-specimen@0.2/pcrec_751b9c6d_auto-caps-simdna/email-specimen@0.2__pcrec_751b9c6d_auto-caps-simdna__budu-ryzen1600__20260927T091338Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_751b9c6d_auto-nocaps-simdna__budu-ryzen1600__20260927T091920Z` (store/records/email-specimen@0.2/pcrec_751b9c6d_auto-nocaps-simdna/email-specimen@0.2__pcrec_751b9c6d_auto-nocaps-simdna__budu-ryzen1600__20260927T091920Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_751b9c6d_vm-caps-simdna__budu-ryzen1600__20260927T092525Z` (store/records/email-specimen@0.2/pcrec_751b9c6d_vm-caps-simdna/email-specimen@0.2__pcrec_751b9c6d_vm-caps-simdna__budu-ryzen1600__20260927T092525Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 496 rows; 5 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_751b9c6d_vm-in-caps-simdna__budu-ryzen1600__20260927T093420Z` (store/records/email-specimen@0.2/pcrec_751b9c6d_vm-in-caps-simdna/email-specimen@0.2__pcrec_751b9c6d_vm-in-caps-simdna__budu-ryzen1600__20260927T093420Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
- sub-bench version(s): email-specimen@0.2
- machine(s): budu-ryzen1600
- schema version(s): 1.6, 1.7
- grain: set (sum of per-subject ns/call over the whole subject set, reduced over trials; a set cell is excluded if ANY subject in it fails)
- reduction: median/min/max/stddev (population) over per-trial `elapsed_ns / iterations`; lazy-JIT compile cost is DERIVED as first-match-row-minus-steady-state (lowest `seq` timed row for the pattern, minus the median of every other timed row), one value per (pattern, testee), never pooled with another execution-model class's compile cost
- `form`: this report includes a `whole-subject` artifact beside `plain` for at least one cell (schema v1.1: a testee with no end-anchored mode compiles and times a SEPARATE artifact for match-compliance, e.g. `(?:pattern)\z`, where another testee reaches the same regime via runtime flags on its ordinary artifact) -- shown as a per-row COLUMN, not a split: both forms answer the same regime and RANK TOGETHER in one table (`form` is a key only for compile-cost rows, where a whole-subject artifact is genuinely a separate compile with its own cost); `fact` restates it as 'same program' / 'separate artifact' (R4)
- status policy (OD-B14): a ranking row whose record `status` is not `measured` is excluded from ranking by default, listed under its table as `not ranked: <testee> -- <status> (<status_detail excerpt>)`; `--include-unmeasured` ranks it instead, with `status` shown
- trial-agreement policy (schema v1.4, rule v1.4-group, X31-X33): a record's five trials must agree to within k=1.5 on every group of its rows — one slow trial of five tolerated; two, or one fast, is a disagreeing row; a group disagrees at >= 2 disagreeing rows reaching a third of it (d_min=2, c=3); a record with a disagreeing group, or with fewer than five odd trials, is `inconclusive-spread` and unranked like `inconclusive-load`; the after-run load/occupancy samples are provenance (v1.4 X13), shown under --include-provenance
- status rule: v1.4 X13 (pre-flight + trial agreement) on 8 record(s)
- tier policy (R3, schema v1.2 `tier`, absent = `pinned`): a `scratch`-tier row is excluded from ranking by default, listed as `scratch: <testee>`; `--include-scratch` ranks it instead, with a `tier` column
- duplicate-record policy (OD-B15, amended 2026-08-25): the NEWEST MEASURED record per (subbench@version, testee_id, machine) ranks by default -- a newer record that is NOT measured does not supersede a measured one of the same testee and version (listed as "newer, not measured" instead); only when no record in the group is measured does the newest record overall stand (itself unranked per the status policy above, unless --include-unmeasured). `--all-records` shows every record as its own row, its testee id suffixed `@<timestamp>`

## Null-control band (D119 bar; [B79], inbox I-93 block B / I-104)

- D119 bar (inbox I-93 block B / I-104): a cross-pin cell moved iff |Δ%| > max(IQR%, null band) -- Δ% = (after - before) / before; IQR% = the BEFORE side's Type-7 IQR of its per-trial set sums over the before median; null band = the largest |Δ%| any PROGRAM-IDENTICAL cell of the same (regime, baseline scale) stratum reached across the same pin pair (symmetric); a stratum with fewer than 10 program-identical cells has NO usable band and its verdicts say `IQR only` by name.
- baseline scale: the BEFORE (older pin) set-grain median -- `>=1us` / `100ns-1us` / `<100ns`; strata are per REGIME (I-104).
- sufficiency: a stratum needs >= 10 program-identical cells -- the band is a sample maximum, and one more null cell exceeds the maximum of n with chance 1/(n+1) (<= 9.1% at n = 10).
- identity: the records' own `engine_metadata.program_sha256` ([B88], schema v1.7) where BOTH compile rows of a cell carry it; otherwise OUR OWN census (`tools/program_identity.py`: both pins re-emitted with the pinned binaries under each config's recorded flags, `.c` + `.h` compared after dropping ONLY the generated-by line, the `.abi` integer and one-sided `#define` stamps). Which records carry the field, per side: `pcrec 25b1984f -> 751b9c6d`: the BEFORE (`25b1984f`) records carry NO `program_sha256` (0 of 24 compiled cell(s)), the AFTER (`751b9c6d`) records carry `program_sha256` (24 of 24 compiled cell(s)).

### `pcrec 25b1984f -> 751b9c6d` (email-specimen@0.2)

- census: `reports/identity/email-specimen@0.2/pcrec_25b1984f__751b9c6d.tsv` (sha256 `1fc2da800eb47998a75223792c793cff629a7db0848460c2b89172a93da144e5`): changed 22, identical 2 (artifact rows: every config x pattern x form)
- cells: 31 cross-pin set cell(s) measured on both sides; 4 program-identical (the null population)

| regime | baseline scale | n null cells | min Δ% | median Δ% | max Δ% | band (±) | status |
|---|---|---|---|---|---|---|---|
| `large-subject-throughput` | `>=1us` | 2 | -28.06% | -27.92% | -27.78% | n/a | insufficient (n=2 < 10) |
| `large-subject-throughput` | `100ns-1us` | 0 | - | - | - | n/a | empty (n=0) |
| `large-subject-throughput` | `<100ns` | 0 | - | - | - | n/a | empty (n=0) |
| `match-compliance` | `>=1us` | 0 | - | - | - | n/a | empty (n=0) |
| `match-compliance` | `100ns-1us` | 0 | - | - | - | n/a | empty (n=0) |
| `match-compliance` | `<100ns` | 0 | - | - | - | n/a | empty (n=0) |
| `short-subject-search` | `>=1us` | 2 | -3.69% | -3.46% | -3.22% | n/a | insufficient (n=2 < 10) |
| `short-subject-search` | `100ns-1us` | 0 | - | - | - | n/a | empty (n=0) |
| `short-subject-search` | `<100ns` | 0 | - | - | - | n/a | empty (n=0) |

_[B82] (inbox I-99, Frank's ruling -- a D119 addendum): this report's roster spans BOTH capture classes, so the two views below are the HEADLINE -- "If an engine is run non-capturing on a pattern, then we can't compare that to a capturing engine run -- they are almost completely different things with different objectives." No cell in either view compares across classes; the third, MIXED table further down restates today's single-roster ranking and is never the headline._

## Ranking -- CAPTURING engines only, caps vs caps (per pattern x regime, SET grain: sum over the subject set; best median first)

_D119 bar in this view: |Δ%| > max(IQR%, null band), the `D119 bar` column (definition, strata and bands in the null-control section above). This view's own threshold population: 22 cross-pin cell(s): 10 improve, 7 regress, 3 within the bar, 2 null-control (program identical -- the band's own population); 20 of the verdicts are IQR-only (their stratum's band is not usable)._

### `factored` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_751b9c6d_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_auto-caps-simdna` | measured | `plain` | same program | 7,018,630.0 | 1.3387 | 7,014,772.2 | 7,022,962.4 | 2,908.8 | 1.000x | 1.000x | faster ×2.03 | -50.77% vs bar 0.18% (IQR-only) → **improve (IQR only: band n=2 < 10)** | 5 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 14,255,555.6 | 2.7190 | 14,236,565.6 | 14,364,717.5 | 46,979.9 | 2.031x | 2.031x | - | - | 5 | 100% |
| 3 | `pcrec_751b9c6d_vm-caps-simdna` | measured | `plain` | same program | 111,373,789.5 | 21.2429 | 110,827,104.7 | 112,207,349.1 | 486,165.0 | 15.868x | 15.868x | now measured (was: gave-up) | - | 5 | 100% |
| 4 | `pcrec_751b9c6d_vm-in-caps-simdna` | measured | `plain` | same program | 112,681,436.2 | 21.4923 | 111,572,780.4 | 113,150,910.4 | 640,462.1 | 16.055x | 16.055x | now measured (was: gave-up) | - | 5 | 100% |

#### `factored` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 3,789,127.8 | 3.6136 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 4,143,287.4 | 3.9513 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 12,276,737.1 | 11.7080 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 12,472,845.9 | 11.8950 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 17,720.7 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 1,875,632.0 | 1.7887 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 18,037.4 | 0.0172 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 18,007.9 | 0.0172 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 17,706.7 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 1,876,063.9 | 1.7892 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 17,925.0 | 0.0171 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 17,871.4 | 0.0170 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 3,174,406.5 | 3.0273 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 3,195,106.6 | 3.0471 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 99,158,013.9 | 94.5645 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 99,749,318.3 | 95.1284 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 17,690.3 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 3,151,717.6 | 3.0057 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 17,963.3 | 0.0171 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 17,998.8 | 0.0172 |

- Δ detail: `pcrec_751b9c6d_auto-caps-simdna` vs previous `pcrec_25b1984f_auto-caps-simdna`: worst now: `t-a-valid-addrs`, 3,789,127.8 ns, 1,048,576 B; largest Δ: `t-e-prose-no-at`, -3,134,027.4 ns (now 17,690.3 ns), 1,048,576 B
- Δ detail: `pcrec_751b9c6d_vm-caps-simdna` vs previous `pcrec_25b1984f_vm-caps-simdna`: worst now: `t-d-prose-sparse-addrs`, 99,158,013.9 ns, 1,048,576 B; largest Δ: `t-e-prose-no-at`, -99,050,035.7 ns (now 17,963.3 ns), 1,048,576 B
- Δ detail: `pcrec_751b9c6d_vm-in-caps-simdna` vs previous `pcrec_25b1984f_vm-in-caps-simdna`: worst now: `t-d-prose-sparse-addrs`, 99,749,318.3 ns, 1,048,576 B; largest Δ: `t-e-prose-no-at`, -97,137,165.2 ns (now 17,998.8 ns), 1,048,576 B

### `factored` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_751b9c6d_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,245.2 | 73,241.5 | 73,251.5 | 3.3 | 1.000x | 1.000x | unchanged (within spread) | -0.11% vs bar 0.15% (IQR-only) → **within (IQR only: band n=0 < 10)** | 85 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,325.7 | 73,269.7 | 73,444.6 | 66.8 | 1.001x | 1.001x | - | - | 85 | 100% |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 457,848.2 | 455,596.2 | 489,129.2 | 12,830.0 | 6.251x | 6.251x | - | - | 85 | 100% |
| 4 | `pcrec_751b9c6d_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 460,693.1 | 454,617.7 | 461,859.2 | 3,205.5 | 6.290x | 6.290x | unchanged (within spread) | +0.62% vs bar 0.44% (IQR-only) → **regress (IQR only: band n=0 < 10)** | 85 | 100% |

- Δ detail: `pcrec_751b9c6d_auto-caps-simdna` vs previous `pcrec_25b1984f_auto-caps-simdna`: worst now (also the largest Δ): `s-057`, 19,063.4 ns, 10,252 B
- Δ detail: `pcrec_751b9c6d_vm-in-caps-simdna` vs previous `pcrec_25b1984f_vm-in-caps-simdna`: worst now: `s-060`, 193,634.7 ns, 10,240 B; largest Δ: `s-063`, +5,450.3 ns (now 100,122.9 ns), 5,135 B

### `factored` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 3,670.8 | 3,668.1 | 3,681.0 | 5.0 | 1.000x | 1.000x | - | - | 77 | 47.7 | 17.7 | 100% |
| 2 | `pcrec_751b9c6d_auto-caps-simdna` | measured | `plain` | same program | 3,940.5 | 3,935.9 | 3,944.4 | 2.9 | 1.073x | 1.073x | slower ×1.07 | +7.35% vs bar 0.21% (IQR-only) → **regress (IQR only: band n=2 < 10)** | 77 | 51.2 | 17.1 | 100% |
| 3 | `pcrec_751b9c6d_vm-in-caps-simdna` | measured | `plain` | same program | 34,899.4 | 34,419.4 | 35,025.6 | 218.4 | 9.507x | 9.507x | faster ×1.57 | -36.33% vs bar 0.29% (IQR-only) → **improve (IQR only: band n=2 < 10)** | 77 | 453.2 | 15.1 | 100% |
| 4 | `pcrec_751b9c6d_vm-caps-simdna` | measured | `plain` | same program | 35,172.7 | 34,596.0 | 35,567.8 | 343.0 | 9.582x | 9.582x | faster ×1.55 | -35.41% vs bar 1.23% (IQR-only) → **improve (IQR only: band n=2 < 10)** | 77 | 456.8 | 15.9 | 100% |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 54,452.0 | 54,248.9 | 56,967.5 | 1,019.2 | 14.834x | 14.834x | - | - | 77 | 707.2 | 13.6 | 100% |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 54,809.4 | 53,700.0 | 55,505.3 | 584.0 | 14.931x | 14.931x | - | - | 77 | 711.8 | 12.5 | 100% |

- Δ detail: `pcrec_751b9c6d_auto-caps-simdna` vs previous `pcrec_25b1984f_auto-caps-simdna`: worst now: `s-004`, 132.0 ns, 33 B; largest Δ: `s-083`, -64.7 ns (now 8.0 ns), 43 B
- Δ detail: `pcrec_751b9c6d_vm-in-caps-simdna` vs previous `pcrec_25b1984f_vm-in-caps-simdna`: worst now: `s-038`, 2,897.1 ns, 17 B; largest Δ: `s-029`, -3,247.4 ns (now 13.9 ns), 28 B
- Δ detail: `pcrec_751b9c6d_vm-caps-simdna` vs previous `pcrec_25b1984f_vm-caps-simdna`: worst now: `s-038`, 2,887.1 ns, 17 B; largest Δ: `s-029`, -3,296.7 ns (now 13.0 ns), 28 B

### `floor` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_751b9c6d_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_auto-caps-simdna` | measured | `plain` | same program | 698,825.3 | 0.1333 | 698,590.0 | 922,007.7 | 89,268.2 | 1.000x | 1.000x | spread | faster ×1.39 | -28.06% (null control: program identical) |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 971,431.9 | 0.1853 | 966,721.2 | 983,955.1 | 6,153.0 | 1.390x | 1.390x | **dominated**: `t-a-valid-addrs` is 91.1% of this set | - | - |
| 3 | `pcrec_751b9c6d_vm-in-caps-simdna` | measured | `plain` | same program | 1,685,511.1 | 0.3215 | 1,685,101.9 | 1,692,377.6 | 2,767.2 | 2.412x | 2.412x | spread | faster ×1.99 | -49.71% vs bar 0.45% (IQR-only) → **improve (IQR only: band n=2 < 10)** |
| 4 | `pcrec_751b9c6d_vm-caps-simdna` | measured | `plain` | same program | 1,692,678.3 | 0.3229 | 1,691,646.9 | 1,695,117.4 | 1,346.8 | 2.422x | 2.422x | spread | faster ×1.96 | -49.01% vs bar 0.17% (IQR-only) → **improve (IQR only: band n=2 < 10)** |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 3,319,613.0 | 0.6332 | 3,307,904.0 | 3,351,862.1 | 14,745.7 | 4.750x | 4.750x | spread | - | - |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 3,351,449.5 | 0.6392 | 3,340,220.9 | 3,389,538.2 | 17,693.1 | 4.796x | 4.796x | spread | - | - |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `floor` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 614,704.1 | 0.5862 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 881,323.3 | 0.8405 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 977,723.2 | 0.9324 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 984,134.5 | 0.9385 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 817,493.5 | 0.7796 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 855,355.9 | 0.8157 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 17,705.6 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 17,701.8 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 17,743.1 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 17,706.9 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 620,919.4 | 0.5922 |
| `t-b-no-at` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 620,441.9 | 0.5917 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 17,722.7 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 17,683.4 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 17,696.3 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 17,697.2 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 620,386.8 | 0.5916 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 620,408.6 | 0.5917 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 31,022.2 | 0.0296 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 33,341.7 | 0.0318 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 654,782.9 | 0.6244 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 655,085.0 | 0.6247 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 632,526.5 | 0.6032 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 630,340.5 | 0.6011 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 17,691.3 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 17,686.1 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 17,699.9 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 17,696.1 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 620,430.1 | 0.5917 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 620,977.6 | 0.5922 |

- Δ detail: `pcrec_751b9c6d_auto-caps-simdna` vs previous `pcrec_25b1984f_auto-caps-simdna`: worst now (also the largest Δ): `t-a-valid-addrs`, 614,704.1 ns, 1,048,576 B
- Δ detail: `pcrec_751b9c6d_vm-in-caps-simdna` vs previous `pcrec_25b1984f_vm-in-caps-simdna`: worst now: `t-a-valid-addrs`, 977,723.2 ns, 1,048,576 B; largest Δ: `t-e-prose-no-at`, -603,277.7 ns (now 17,699.9 ns), 1,048,576 B
- Δ detail: `pcrec_751b9c6d_vm-caps-simdna` vs previous `pcrec_25b1984f_vm-caps-simdna`: worst now: `t-a-valid-addrs`, 984,134.5 ns, 1,048,576 B; largest Δ: `t-b-no-at`, -603,212.6 ns (now 17,706.9 ns), 1,048,576 B

### `floor` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_25b1984f_vm-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 485.6 | 484.2 | 487.9 | 1.3 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 505.8 | 505.7 | 507.1 | 0.5 | 1.042x | 1.042x | - | - |
| 3 | `pcrec_751b9c6d_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 529.4 | 529.3 | 530.5 | 0.5 | 1.090x | 1.090x | slower ×1.05 | +4.67% vs bar 0.10% (IQR-only) → **regress (IQR only: band n=0 < 10)** |
| 4 | `pcrec_751b9c6d_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 559.2 | 557.8 | 561.2 | 1.2 | 1.152x | 1.152x | slower ×1.15 | +15.17% vs bar 0.26% (IQR-only) → **regress (IQR only: band n=0 < 10)** |
| 5 | `pcrec_751b9c6d_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 833.9 | 823.7 | 848.7 | 8.4 | 1.717x | 1.717x | faster ×1.06 | -5.47% vs bar 2.22% (IQR-only) → **improve (IQR only: band n=0 < 10)** |
| 6 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 882.2 | 858.7 | 896.2 | 13.5 | 1.817x | 1.817x | - | - |

- Δ detail: `pcrec_751b9c6d_vm-in-caps-simdna` vs previous `pcrec_25b1984f_vm-in-caps-simdna`: worst now (also the largest Δ): `s-082`, 8.6 ns, 1 B
- Δ detail: `pcrec_751b9c6d_vm-caps-simdna` vs previous `pcrec_25b1984f_vm-caps-simdna`: worst now: `s-082`, 10.1 ns, 1 B; largest Δ: `s-042`, +1.6 ns (now 7.4 ns), 5 B
- Δ detail: `pcrec_751b9c6d_auto-caps-simdna` vs previous `pcrec_25b1984f_auto-caps-simdna`: worst now: `s-082`, 13.0 ns, 1 B; largest Δ: `s-032`, -0.7 ns (now 9.7 ns), 16 B

### `floor` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: pcrec_25b1984f_vm-in-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 961.4 | 954.9 | 967.1 | 4.0 | 1.000x | 1.000x | - | - | 77 | 12.5 | 100% |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 1,043.4 | 1,039.8 | 1,045.4 | 1.8 | 1.085x | 1.085x | - | - | 77 | 13.6 | 100% |
| 3 | `pcrec_751b9c6d_vm-in-caps-simdna` | measured | `plain` | same program | 1,160.6 | 1,158.8 | 1,164.6 | 2.0 | 1.207x | 1.207x | slower ×1.21 | +20.72% vs bar 0.28% (IQR-only) → **regress (IQR only: band n=0 < 10)** | 77 | 15.1 | 100% |
| 4 | `pcrec_751b9c6d_vm-caps-simdna` | measured | `plain` | same program | 1,227.3 | 1,224.2 | 1,228.9 | 1.5 | 1.277x | 1.277x | slower ×1.18 | +17.63% vs bar 0.12% (IQR-only) → **regress (IQR only: band n=2 < 10)** | 77 | 15.9 | 100% |
| 5 | `pcrec_751b9c6d_auto-caps-simdna` | measured | `plain` | same program | 1,320.4 | 1,319.9 | 1,323.1 | 1.2 | 1.373x | 1.373x | faster ×1.03 | -3.22% (null control: program identical) | 77 | 17.1 | 100% |
| 6 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,364.3 | 1,362.9 | 1,367.5 | 1.5 | 1.419x | 1.419x | - | - | 77 | 17.7 | 100% |

- Δ detail: `pcrec_751b9c6d_vm-in-caps-simdna` vs previous `pcrec_25b1984f_vm-in-caps-simdna`: worst now: `s-004`, 26.7 ns, 33 B; largest Δ: `s-083`, -31.9 ns (now 9.5 ns), 43 B
- Δ detail: `pcrec_751b9c6d_vm-caps-simdna` vs previous `pcrec_25b1984f_vm-caps-simdna`: worst now: `s-004`, 27.5 ns, 33 B; largest Δ: `s-083`, -31.1 ns (now 10.0 ns), 43 B
- Δ detail: `pcrec_751b9c6d_auto-caps-simdna` vs previous `pcrec_25b1984f_auto-caps-simdna`: worst now: `s-004`, 18.2 ns, 33 B; largest Δ: `s-081`, -0.9 ns (now 5.0 ns), 0 B

### `orig` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_751b9c6d_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_auto-caps-simdna` | measured | `plain` | same program | 7,053,755.3 | 1.3454 | 7,048,184.0 | 7,194,846.7 | 56,986.4 | 1.000x | 1.000x | faster ×2.00 | -50.08% vs bar 0.17% (IQR-only) → **improve (IQR only: band n=2 < 10)** | 5 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 14,131,365.5 | 2.6953 | 14,105,993.7 | 14,195,054.8 | 31,617.7 | 2.003x | 2.003x | - | - | 5 | 100% |
| 3 | `pcrec_751b9c6d_vm-caps-simdna` | measured | `plain` | same program | 22,840,316.3 | 4.3564 | 22,758,079.6 | 23,117,623.4 | 122,729.8 | 3.238x | 3.238x | now measured (was: gave-up) | - | 5 | 100% |
| 4 | `pcrec_751b9c6d_vm-in-caps-simdna` | measured | `plain` | same program | 23,621,686.4 | 4.5055 | 23,337,194.8 | 23,931,857.4 | 206,785.4 | 3.349x | 3.349x | now measured (was: gave-up) | - | 5 | 100% |

#### `orig` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 3,774,303.0 | 3.5995 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 4,143,067.6 | 3.9511 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 5,236,612.5 | 4.9940 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 5,963,203.3 | 5.6870 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 17,732.3 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 1,886,626.1 | 1.7992 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 17,697.4 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 17,723.3 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 17,698.2 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 1,875,434.8 | 1.7886 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 17,681.9 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 17,726.1 | 0.0169 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 3,221,893.2 | 3.0726 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 3,132,783.4 | 2.9877 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 17,585,066.0 | 16.7704 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 17,609,664.6 | 16.7939 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 17,719.7 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 3,083,466.1 | 2.9406 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 17,693.5 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 17,716.9 | 0.0169 |

- Δ detail: `pcrec_751b9c6d_auto-caps-simdna` vs previous `pcrec_25b1984f_auto-caps-simdna`: worst now: `t-a-valid-addrs`, 3,774,303.0 ns, 1,048,576 B; largest Δ: `t-e-prose-no-at`, -3,065,746.4 ns (now 17,719.7 ns), 1,048,576 B
- Δ detail: `pcrec_751b9c6d_vm-caps-simdna` vs previous `pcrec_25b1984f_vm-caps-simdna`: worst now: `t-d-prose-sparse-addrs`, 17,585,066.0 ns, 1,048,576 B; largest Δ: `t-e-prose-no-at`, -16,526,333.0 ns (now 17,693.5 ns), 1,048,576 B
- Δ detail: `pcrec_751b9c6d_vm-in-caps-simdna` vs previous `pcrec_25b1984f_vm-in-caps-simdna`: worst now: `t-d-prose-sparse-addrs`, 17,609,664.6 ns, 1,048,576 B; largest Δ: `t-e-prose-no-at`, -16,521,403.6 ns (now 17,716.9 ns), 1,048,576 B

### `orig` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_751b9c6d_vm-in-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 61,998.6 | 61,887.2 | 62,467.7 | 212.1 | 1.000x | 1.000x | unchanged (within spread) | -0.12% vs bar 0.17% (IQR-only) → **within (IQR only: band n=0 < 10)** |
| 2 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 62,071.9 | 62,030.4 | 62,228.5 | 74.3 | 1.001x | 1.001x | - | - |
| 3 | `pcrec_751b9c6d_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 62,876.5 | 62,830.5 | 66,758.3 | 1,542.8 | 1.014x | 1.014x | unchanged (within spread) | -0.04% vs bar 0.19% (IQR-only) → **within (IQR only: band n=0 < 10)** |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 62,899.6 | 62,741.4 | 62,971.2 | 84.0 | 1.015x | 1.015x | - | - |
| 5 | `pcrec_751b9c6d_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,131.7 | 73,120.8 | 73,136.1 | 5.5 | 1.180x | 1.180x | unchanged (within spread) | -0.14% vs bar 0.10% (IQR-only) → **improve (IQR only: band n=0 < 10)** |
| 6 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,231.8 | 73,200.7 | 73,340.4 | 51.8 | 1.181x | 1.181x | - | - |

- Δ detail: `pcrec_751b9c6d_vm-in-caps-simdna` vs previous `pcrec_25b1984f_vm-in-caps-simdna`: worst now (also the largest Δ): `s-059`, 13,672.5 ns, 5,134 B
- Δ detail: `pcrec_751b9c6d_vm-caps-simdna` vs previous `pcrec_25b1984f_vm-caps-simdna`: worst now: `s-059`, 13,679.8 ns, 5,134 B; largest Δ: `s-058`, -60.2 ns (now 6,215.7 ns), 4,011 B
- Δ detail: `pcrec_751b9c6d_auto-caps-simdna` vs previous `pcrec_25b1984f_auto-caps-simdna`: worst now: `s-057`, 19,059.8 ns, 10,252 B; largest Δ: `s-060`, -31.4 ns (now 19,035.4 ns), 10,240 B

### `orig` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 3,522.1 | 3,518.8 | 3,594.9 | 29.6 | 1.000x | 1.000x | - | - | 77 | 45.7 | 17.7 | 100% |
| 2 | `pcrec_751b9c6d_auto-caps-simdna` | measured | `plain` | same program | 3,704.0 | 3,701.2 | 3,799.8 | 38.6 | 1.052x | 1.052x | slower ×1.05 | +5.16% vs bar 0.05% (IQR-only) → **regress (IQR only: band n=2 < 10)** | 77 | 48.1 | 17.1 | 100% |
| 3 | `pcrec_751b9c6d_vm-caps-simdna` | measured | `plain` | same program | 8,596.0 | 8,554.5 | 8,800.2 | 89.6 | 2.441x | 2.441x | faster ×1.48 | -32.65% vs bar 0.73% (IQR-only) → **improve (IQR only: band n=2 < 10)** | 77 | 111.6 | 15.9 | 100% |
| 4 | `pcrec_751b9c6d_vm-in-caps-simdna` | measured | `plain` | same program | 9,421.3 | 9,367.8 | 9,446.5 | 28.0 | 2.675x | 2.675x | faster ×1.36 | -26.58% vs bar 0.26% (IQR-only) → **improve (IQR only: band n=2 < 10)** | 77 | 122.4 | 15.1 | 100% |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12,764.0 | 12,666.2 | 12,851.3 | 65.7 | 3.624x | 3.624x | - | - | 77 | 165.8 | 13.6 | 100% |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 12,831.4 | 12,810.0 | 12,886.0 | 27.0 | 3.643x | 3.643x | - | - | 77 | 166.6 | 12.5 | 100% |

- Δ detail: `pcrec_751b9c6d_auto-caps-simdna` vs previous `pcrec_25b1984f_auto-caps-simdna`: worst now: `s-004`, 125.4 ns, 33 B; largest Δ: `s-083`, -65.8 ns (now 7.7 ns), 43 B
- Δ detail: `pcrec_751b9c6d_vm-caps-simdna` vs previous `pcrec_25b1984f_vm-caps-simdna`: worst now: `s-035`, 708.2 ns, 16 B; largest Δ: `s-083`, -620.9 ns (now 10.6 ns), 43 B
- Δ detail: `pcrec_751b9c6d_vm-in-caps-simdna` vs previous `pcrec_25b1984f_vm-in-caps-simdna`: worst now: `s-035`, 711.0 ns, 16 B; largest Δ: `s-083`, -619.9 ns (now 11.5 ns), 43 B

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `factored` | `large-subject-throughput` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 5 | 80% | -2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 5 | 80% | -2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `match-compliance` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 85 | 94% | -3:PCREC_ERR_FRAMES×5 (smallest: s-061, 2,008 B) | 0 | `s-058` (gave-up), `s-059` (gave-up), `s-061` (gave-up), `s-063` (gave-up), `s-064` (gave-up) |
| `factored` | `match-compliance` | `whole-subject` | `pcrec_751b9c6d_vm-caps-simdna` | 85 | 94% | -3:PCREC_ERR_FRAMES×5 (smallest: s-061, 2,008 B) | 0 | `s-058` (gave-up), `s-059` (gave-up), `s-061` (gave-up), `s-063` (gave-up), `s-064` (gave-up) |
| `orig` | `large-subject-throughput` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 5 | 80% | -4:PCREC_ERR_WORK×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `orig` | `large-subject-throughput` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 5 | 80% | -4:PCREC_ERR_WORK×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |

## Ranking -- NON-CAPTURING engines only, nocaps vs nocaps (per pattern x regime, SET grain: sum over the subject set; best median first)

_D119 bar in this view: |Δ%| > max(IQR%, null band), the `D119 bar` column (definition, strata and bands in the null-control section above). This view's own threshold population: 9 cross-pin cell(s): 5 improve, 2 regress, 0 within the bar, 2 null-control (program identical -- the band's own population); 7 of the verdicts are IQR-only (their stratum's band is not usable)._

### `factored` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_751b9c6d_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_auto-nocaps-simdna` | measured | `plain` | same program | 7,048,417.6 | 1.3444 | 7,045,136.7 | 7,053,866.5 | 2,825.0 | 1.000x | 1.000x | faster ×2.01 | -50.14% vs bar 0.04% (IQR-only) → **improve (IQR only: band n=2 < 10)** |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 14,136,501.8 | 2.6963 | 14,121,185.8 | 14,178,147.4 | 19,152.4 | 2.006x | 2.006x | - | - |

#### `factored` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 3,773,966.2 | 3.5991 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 4,140,798.8 | 3.9490 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 17,664.5 | 0.0168 |
| `t-b-no-at` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,881,351.0 | 1.7942 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 17,672.9 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,875,092.7 | 1.7882 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 3,221,634.0 | 3.0724 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 3,142,816.5 | 2.9972 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 17,679.6 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 3,098,133.9 | 2.9546 |

- Δ detail: `pcrec_751b9c6d_auto-nocaps-simdna` vs previous `pcrec_25b1984f_auto-nocaps-simdna`: worst now: `t-a-valid-addrs`, 3,773,966.2 ns, 1,048,576 B; largest Δ: `t-e-prose-no-at`, -3,080,454.3 ns (now 17,679.6 ns), 1,048,576 B

### `factored` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_751b9c6d_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,150.7 | 73,133.3 | 73,179.6 | 16.8 | 1.000x | 1.000x | faster ×1.00 | -0.14% vs bar 0.01% (IQR-only) → **improve (IQR only: band n=0 < 10)** |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,250.8 | 73,186.0 | 73,340.5 | 49.3 | 1.001x | 1.001x | - | - |

- Δ detail: `pcrec_751b9c6d_auto-nocaps-simdna` vs previous `pcrec_25b1984f_auto-nocaps-simdna`: worst now: `s-057`, 19,062.4 ns, 10,252 B; largest Δ: `s-060`, -23.7 ns (now 19,037.1 ns), 10,240 B

### `factored` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 3,525.3 | 3,518.7 | 3,564.8 | 16.9 | 1.000x | 1.000x | - | - | 77 | 45.8 | 17.8 | 100% |
| 2 | `pcrec_751b9c6d_auto-nocaps-simdna` | measured | `plain` | same program | 3,702.6 | 3,697.4 | 3,708.4 | 3.6 | 1.050x | 1.050x | slower ×1.05 | +5.03% vs bar 0.26% (IQR-only) → **regress (IQR only: band n=2 < 10)** | 77 | 48.1 | 17.1 | 100% |

- Δ detail: `pcrec_751b9c6d_auto-nocaps-simdna` vs previous `pcrec_25b1984f_auto-nocaps-simdna`: worst now: `s-004`, 125.4 ns, 33 B; largest Δ: `s-083`, -65.2 ns (now 8.5 ns), 43 B

### `floor` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_751b9c6d_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_auto-nocaps-simdna` | measured | `plain` | same program | 698,579.8 | 0.1332 | 698,448.6 | 699,266.1 | 299.9 | 1.000x | 1.000x | spread | faster ×1.38 | -27.78% (null control: program identical) |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 967,321.1 | 0.1845 | 966,348.4 | 973,089.8 | 2,487.4 | 1.385x | 1.385x | **dominated**: `t-a-valid-addrs` is 91.1% of this set | - | - |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `floor` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 614,501.1 | 0.5860 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 880,810.7 | 0.8400 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 17,664.3 | 0.0168 |
| `t-b-no-at` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 17,761.2 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 17,651.4 | 0.0168 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 17,695.8 | 0.0169 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 31,143.0 | 0.0297 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 33,253.8 | 0.0317 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 17,722.7 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 17,679.2 | 0.0169 |

- Δ detail: `pcrec_751b9c6d_auto-nocaps-simdna` vs previous `pcrec_25b1984f_auto-nocaps-simdna`: worst now (also the largest Δ): `t-a-valid-addrs`, 614,501.1 ns, 1,048,576 B

### `floor` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_751b9c6d_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 828.4 | 825.0 | 842.2 | 7.1 | 1.000x | 1.000x | faster ×1.06 | -5.29% vs bar 0.74% (IQR-only) → **improve (IQR only: band n=0 < 10)** |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 874.7 | 864.8 | 887.5 | 7.5 | 1.056x | 1.056x | - | - |

- Δ detail: `pcrec_751b9c6d_auto-nocaps-simdna` vs previous `pcrec_25b1984f_auto-nocaps-simdna`: worst now: `s-082`, 13.0 ns, 1 B; largest Δ: `s-050`, -0.7 ns (now 9.6 ns), 17 B

### `floor` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: pcrec_751b9c6d_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_auto-nocaps-simdna` | measured | `plain` | same program | 1,319.7 | 1,317.7 | 1,329.1 | 4.2 | 1.000x | 1.000x | faster ×1.04 | -3.69% (null control: program identical) | 77 | 17.1 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,370.4 | 1,367.6 | 1,374.0 | 2.2 | 1.038x | 1.038x | - | - | 77 | 17.8 | 100% |

- Δ detail: `pcrec_751b9c6d_auto-nocaps-simdna` vs previous `pcrec_25b1984f_auto-nocaps-simdna`: worst now: `s-004`, 18.1 ns, 33 B; largest Δ: `s-081`, -0.9 ns (now 5.0 ns), 0 B

### `orig` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_751b9c6d_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_auto-nocaps-simdna` | measured | `plain` | same program | 7,048,489.6 | 1.3444 | 7,040,718.7 | 7,053,433.2 | 5,019.7 | 1.000x | 1.000x | faster ×2.01 | -50.15% vs bar 0.25% (IQR-only) → **improve (IQR only: band n=2 < 10)** |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 14,138,384.1 | 2.6967 | 14,117,417.0 | 14,178,994.4 | 22,669.4 | 2.006x | 2.006x | - | - |

#### `orig` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 3,775,381.2 | 3.6005 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 4,145,504.2 | 3.9535 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 17,672.0 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,888,425.7 | 1.8009 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 17,690.8 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,874,718.0 | 1.7879 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 3,219,745.6 | 3.0706 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 3,137,025.9 | 2.9917 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 17,670.8 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 3,094,842.2 | 2.9515 |

- Δ detail: `pcrec_751b9c6d_auto-nocaps-simdna` vs previous `pcrec_25b1984f_auto-nocaps-simdna`: worst now: `t-a-valid-addrs`, 3,775,381.2 ns, 1,048,576 B; largest Δ: `t-e-prose-no-at`, -3,077,171.4 ns (now 17,670.8 ns), 1,048,576 B

### `orig` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_751b9c6d_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,137.5 | 73,127.5 | 73,141.1 | 5.0 | 1.000x | 1.000x | faster ×1.00 | -0.18% vs bar 0.14% (IQR-only) → **improve (IQR only: band n=0 < 10)** |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,267.0 | 73,211.0 | 73,343.4 | 53.1 | 1.002x | 1.002x | - | - |

- Δ detail: `pcrec_751b9c6d_auto-nocaps-simdna` vs previous `pcrec_25b1984f_auto-nocaps-simdna`: worst now: `s-057`, 19,061.8 ns, 10,252 B; largest Δ: `s-060`, -28.8 ns (now 19,036.8 ns), 10,240 B

### `orig` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 3,525.6 | 3,521.7 | 3,548.6 | 12.1 | 1.000x | 1.000x | - | - | 77 | 45.8 | 17.8 | 100% |
| 2 | `pcrec_751b9c6d_auto-nocaps-simdna` | measured | `plain` | same program | 3,703.1 | 3,701.2 | 3,705.6 | 1.6 | 1.050x | 1.050x | slower ×1.05 | +5.03% vs bar 0.70% (IQR-only) → **regress (IQR only: band n=2 < 10)** | 77 | 48.1 | 17.1 | 100% |

- Δ detail: `pcrec_751b9c6d_auto-nocaps-simdna` vs previous `pcrec_25b1984f_auto-nocaps-simdna`: worst now: `s-004`, 125.2 ns, 33 B; largest Δ: `s-083`, -64.8 ns (now 8.5 ns), 43 B

## Ranking -- MIXED CLASSES, never compare across cells (per pattern x regime, SET grain: sum over the subject set; best median first)

_D119 bar in this view: |Δ%| > max(IQR%, null band), the `D119 bar` column (definition, strata and bands in the null-control section above). This view's own threshold population: 31 cross-pin cell(s): 15 improve, 9 regress, 3 within the bar, 4 null-control (program identical -- the band's own population); 27 of the verdicts are IQR-only (their stratum's band is not usable)._

### `factored` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_751b9c6d_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_auto-caps-simdna` | measured | `plain` | same program | 7,018,630.0 | 1.3387 | 7,014,772.2 | 7,022,962.4 | 2,908.8 | 1.000x | 1.000x | faster ×2.03 | -50.77% vs bar 0.18% (IQR-only) → **improve (IQR only: band n=2 < 10)** | 5 | 100% |
| 2 | `pcrec_751b9c6d_auto-nocaps-simdna` | measured | `plain` | same program | 7,048,417.6 | 1.3444 | 7,045,136.7 | 7,053,866.5 | 2,825.0 | 1.004x | 1.004x | faster ×2.01 | -50.14% vs bar 0.04% (IQR-only) → **improve (IQR only: band n=2 < 10)** | 5 | 100% |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 14,136,501.8 | 2.6963 | 14,121,185.8 | 14,178,147.4 | 19,152.4 | 2.014x | 2.014x | - | - | 5 | 100% |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 14,255,555.6 | 2.7190 | 14,236,565.6 | 14,364,717.5 | 46,979.9 | 2.031x | 2.031x | - | - | 5 | 100% |
| 5 | `pcrec_751b9c6d_vm-caps-simdna` | measured | `plain` | same program | 111,373,789.5 | 21.2429 | 110,827,104.7 | 112,207,349.1 | 486,165.0 | 15.868x | 15.868x | now measured (was: gave-up) | - | 5 | 100% |
| 6 | `pcrec_751b9c6d_vm-in-caps-simdna` | measured | `plain` | same program | 112,681,436.2 | 21.4923 | 111,572,780.4 | 113,150,910.4 | 640,462.1 | 16.055x | 16.055x | now measured (was: gave-up) | - | 5 | 100% |

#### `factored` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 3,789,127.8 | 3.6136 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 3,773,966.2 | 3.5991 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 4,140,798.8 | 3.9490 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 4,143,287.4 | 3.9513 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 12,276,737.1 | 11.7080 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 12,472,845.9 | 11.8950 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 17,720.7 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 17,664.5 | 0.0168 |
| `t-b-no-at` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,881,351.0 | 1.7942 |
| `t-b-no-at` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 1,875,632.0 | 1.7887 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 18,037.4 | 0.0172 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 18,007.9 | 0.0172 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 17,706.7 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 17,672.9 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,875,092.7 | 1.7882 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 1,876,063.9 | 1.7892 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 17,925.0 | 0.0171 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 17,871.4 | 0.0170 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 3,174,406.5 | 3.0273 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 3,221,634.0 | 3.0724 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 3,142,816.5 | 2.9972 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 3,195,106.6 | 3.0471 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 99,158,013.9 | 94.5645 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 99,749,318.3 | 95.1284 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 17,690.3 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 17,679.6 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 3,098,133.9 | 2.9546 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 3,151,717.6 | 3.0057 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 17,963.3 | 0.0171 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 17,998.8 | 0.0172 |

- Δ detail: `pcrec_751b9c6d_auto-caps-simdna` vs previous `pcrec_25b1984f_auto-caps-simdna`: worst now: `t-a-valid-addrs`, 3,789,127.8 ns, 1,048,576 B; largest Δ: `t-e-prose-no-at`, -3,134,027.4 ns (now 17,690.3 ns), 1,048,576 B
- Δ detail: `pcrec_751b9c6d_auto-nocaps-simdna` vs previous `pcrec_25b1984f_auto-nocaps-simdna`: worst now: `t-a-valid-addrs`, 3,773,966.2 ns, 1,048,576 B; largest Δ: `t-e-prose-no-at`, -3,080,454.3 ns (now 17,679.6 ns), 1,048,576 B
- Δ detail: `pcrec_751b9c6d_vm-caps-simdna` vs previous `pcrec_25b1984f_vm-caps-simdna`: worst now: `t-d-prose-sparse-addrs`, 99,158,013.9 ns, 1,048,576 B; largest Δ: `t-e-prose-no-at`, -99,050,035.7 ns (now 17,963.3 ns), 1,048,576 B
- Δ detail: `pcrec_751b9c6d_vm-in-caps-simdna` vs previous `pcrec_25b1984f_vm-in-caps-simdna`: worst now: `t-d-prose-sparse-addrs`, 99,749,318.3 ns, 1,048,576 B; largest Δ: `t-e-prose-no-at`, -97,137,165.2 ns (now 17,998.8 ns), 1,048,576 B

### `factored` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_751b9c6d_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,150.7 | 73,133.3 | 73,179.6 | 16.8 | 1.000x | 1.000x | faster ×1.00 | -0.14% vs bar 0.01% (IQR-only) → **improve (IQR only: band n=0 < 10)** | 85 | 100% |
| 2 | `pcrec_751b9c6d_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,245.2 | 73,241.5 | 73,251.5 | 3.3 | 1.001x | 1.001x | unchanged (within spread) | -0.11% vs bar 0.15% (IQR-only) → **within (IQR only: band n=0 < 10)** | 85 | 100% |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,250.8 | 73,186.0 | 73,340.5 | 49.3 | 1.001x | 1.001x | - | - | 85 | 100% |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,325.7 | 73,269.7 | 73,444.6 | 66.8 | 1.002x | 1.002x | - | - | 85 | 100% |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 457,848.2 | 455,596.2 | 489,129.2 | 12,830.0 | 6.259x | 6.259x | - | - | 85 | 100% |
| 6 | `pcrec_751b9c6d_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 460,693.1 | 454,617.7 | 461,859.2 | 3,205.5 | 6.298x | 6.298x | unchanged (within spread) | +0.62% vs bar 0.44% (IQR-only) → **regress (IQR only: band n=0 < 10)** | 85 | 100% |

- Δ detail: `pcrec_751b9c6d_auto-nocaps-simdna` vs previous `pcrec_25b1984f_auto-nocaps-simdna`: worst now: `s-057`, 19,062.4 ns, 10,252 B; largest Δ: `s-060`, -23.7 ns (now 19,037.1 ns), 10,240 B
- Δ detail: `pcrec_751b9c6d_auto-caps-simdna` vs previous `pcrec_25b1984f_auto-caps-simdna`: worst now (also the largest Δ): `s-057`, 19,063.4 ns, 10,252 B
- Δ detail: `pcrec_751b9c6d_vm-in-caps-simdna` vs previous `pcrec_25b1984f_vm-in-caps-simdna`: worst now: `s-060`, 193,634.7 ns, 10,240 B; largest Δ: `s-063`, +5,450.3 ns (now 100,122.9 ns), 5,135 B

### `factored` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 3,525.3 | 3,518.7 | 3,564.8 | 16.9 | 1.000x | 1.000x | - | - | 77 | 45.8 | 17.8 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 3,670.8 | 3,668.1 | 3,681.0 | 5.0 | 1.041x | 1.041x | - | - | 77 | 47.7 | 17.7 | 100% |
| 3 | `pcrec_751b9c6d_auto-nocaps-simdna` | measured | `plain` | same program | 3,702.6 | 3,697.4 | 3,708.4 | 3.6 | 1.050x | 1.050x | slower ×1.05 | +5.03% vs bar 0.26% (IQR-only) → **regress (IQR only: band n=2 < 10)** | 77 | 48.1 | 17.1 | 100% |
| 4 | `pcrec_751b9c6d_auto-caps-simdna` | measured | `plain` | same program | 3,940.5 | 3,935.9 | 3,944.4 | 2.9 | 1.118x | 1.118x | slower ×1.07 | +7.35% vs bar 0.21% (IQR-only) → **regress (IQR only: band n=2 < 10)** | 77 | 51.2 | 17.1 | 100% |
| 5 | `pcrec_751b9c6d_vm-in-caps-simdna` | measured | `plain` | same program | 34,899.4 | 34,419.4 | 35,025.6 | 218.4 | 9.900x | 9.900x | faster ×1.57 | -36.33% vs bar 0.29% (IQR-only) → **improve (IQR only: band n=2 < 10)** | 77 | 453.2 | 15.1 | 100% |
| 6 | `pcrec_751b9c6d_vm-caps-simdna` | measured | `plain` | same program | 35,172.7 | 34,596.0 | 35,567.8 | 343.0 | 9.977x | 9.977x | faster ×1.55 | -35.41% vs bar 1.23% (IQR-only) → **improve (IQR only: band n=2 < 10)** | 77 | 456.8 | 15.9 | 100% |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 54,452.0 | 54,248.9 | 56,967.5 | 1,019.2 | 15.446x | 15.446x | - | - | 77 | 707.2 | 13.6 | 100% |
| 8 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 54,809.4 | 53,700.0 | 55,505.3 | 584.0 | 15.548x | 15.548x | - | - | 77 | 711.8 | 12.5 | 100% |

- Δ detail: `pcrec_751b9c6d_auto-nocaps-simdna` vs previous `pcrec_25b1984f_auto-nocaps-simdna`: worst now: `s-004`, 125.4 ns, 33 B; largest Δ: `s-083`, -65.2 ns (now 8.5 ns), 43 B
- Δ detail: `pcrec_751b9c6d_auto-caps-simdna` vs previous `pcrec_25b1984f_auto-caps-simdna`: worst now: `s-004`, 132.0 ns, 33 B; largest Δ: `s-083`, -64.7 ns (now 8.0 ns), 43 B
- Δ detail: `pcrec_751b9c6d_vm-in-caps-simdna` vs previous `pcrec_25b1984f_vm-in-caps-simdna`: worst now: `s-038`, 2,897.1 ns, 17 B; largest Δ: `s-029`, -3,247.4 ns (now 13.9 ns), 28 B
- Δ detail: `pcrec_751b9c6d_vm-caps-simdna` vs previous `pcrec_25b1984f_vm-caps-simdna`: worst now: `s-038`, 2,887.1 ns, 17 B; largest Δ: `s-029`, -3,296.7 ns (now 13.0 ns), 28 B

### `floor` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_751b9c6d_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_auto-nocaps-simdna` | measured | `plain` | same program | 698,579.8 | 0.1332 | 698,448.6 | 699,266.1 | 299.9 | 1.000x | 1.000x | spread | faster ×1.38 | -27.78% (null control: program identical) |
| 2 | `pcrec_751b9c6d_auto-caps-simdna` | measured | `plain` | same program | 698,825.3 | 0.1333 | 698,590.0 | 922,007.7 | 89,268.2 | 1.000x | 1.000x | spread | faster ×1.39 | -28.06% (null control: program identical) |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 967,321.1 | 0.1845 | 966,348.4 | 973,089.8 | 2,487.4 | 1.385x | 1.385x | **dominated**: `t-a-valid-addrs` is 91.1% of this set | - | - |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 971,431.9 | 0.1853 | 966,721.2 | 983,955.1 | 6,153.0 | 1.391x | 1.391x | **dominated**: `t-a-valid-addrs` is 91.1% of this set | - | - |
| 5 | `pcrec_751b9c6d_vm-in-caps-simdna` | measured | `plain` | same program | 1,685,511.1 | 0.3215 | 1,685,101.9 | 1,692,377.6 | 2,767.2 | 2.413x | 2.413x | spread | faster ×1.99 | -49.71% vs bar 0.45% (IQR-only) → **improve (IQR only: band n=2 < 10)** |
| 6 | `pcrec_751b9c6d_vm-caps-simdna` | measured | `plain` | same program | 1,692,678.3 | 0.3229 | 1,691,646.9 | 1,695,117.4 | 1,346.8 | 2.423x | 2.423x | spread | faster ×1.96 | -49.01% vs bar 0.17% (IQR-only) → **improve (IQR only: band n=2 < 10)** |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 3,319,613.0 | 0.6332 | 3,307,904.0 | 3,351,862.1 | 14,745.7 | 4.752x | 4.752x | spread | - | - |
| 8 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 3,351,449.5 | 0.6392 | 3,340,220.9 | 3,389,538.2 | 17,693.1 | 4.798x | 4.798x | spread | - | - |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `floor` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 614,501.1 | 0.5860 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 614,704.1 | 0.5862 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 880,810.7 | 0.8400 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 881,323.3 | 0.8405 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 977,723.2 | 0.9324 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 984,134.5 | 0.9385 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 817,493.5 | 0.7796 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 855,355.9 | 0.8157 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 17,664.3 | 0.0168 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 17,705.6 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 17,761.2 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 17,701.8 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 17,743.1 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 17,706.9 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 620,919.4 | 0.5922 |
| `t-b-no-at` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 620,441.9 | 0.5917 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 17,651.4 | 0.0168 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 17,722.7 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 17,695.8 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 17,683.4 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 17,696.3 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 17,697.2 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 620,386.8 | 0.5916 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 620,408.6 | 0.5917 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 31,143.0 | 0.0297 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 31,022.2 | 0.0296 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 33,253.8 | 0.0317 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 33,341.7 | 0.0318 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 654,782.9 | 0.6244 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 655,085.0 | 0.6247 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 632,526.5 | 0.6032 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 630,340.5 | 0.6011 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 17,722.7 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 17,691.3 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 17,679.2 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 17,686.1 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 17,699.9 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 17,696.1 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 620,430.1 | 0.5917 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 620,977.6 | 0.5922 |

- Δ detail: `pcrec_751b9c6d_auto-nocaps-simdna` vs previous `pcrec_25b1984f_auto-nocaps-simdna`: worst now (also the largest Δ): `t-a-valid-addrs`, 614,501.1 ns, 1,048,576 B
- Δ detail: `pcrec_751b9c6d_auto-caps-simdna` vs previous `pcrec_25b1984f_auto-caps-simdna`: worst now (also the largest Δ): `t-a-valid-addrs`, 614,704.1 ns, 1,048,576 B
- Δ detail: `pcrec_751b9c6d_vm-in-caps-simdna` vs previous `pcrec_25b1984f_vm-in-caps-simdna`: worst now: `t-a-valid-addrs`, 977,723.2 ns, 1,048,576 B; largest Δ: `t-e-prose-no-at`, -603,277.7 ns (now 17,699.9 ns), 1,048,576 B
- Δ detail: `pcrec_751b9c6d_vm-caps-simdna` vs previous `pcrec_25b1984f_vm-caps-simdna`: worst now: `t-a-valid-addrs`, 984,134.5 ns, 1,048,576 B; largest Δ: `t-b-no-at`, -603,212.6 ns (now 17,706.9 ns), 1,048,576 B

### `floor` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_25b1984f_vm-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 485.6 | 484.2 | 487.9 | 1.3 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 505.8 | 505.7 | 507.1 | 0.5 | 1.042x | 1.042x | - | - |
| 3 | `pcrec_751b9c6d_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 529.4 | 529.3 | 530.5 | 0.5 | 1.090x | 1.090x | slower ×1.05 | +4.67% vs bar 0.10% (IQR-only) → **regress (IQR only: band n=0 < 10)** |
| 4 | `pcrec_751b9c6d_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 559.2 | 557.8 | 561.2 | 1.2 | 1.152x | 1.152x | slower ×1.15 | +15.17% vs bar 0.26% (IQR-only) → **regress (IQR only: band n=0 < 10)** |
| 5 | `pcrec_751b9c6d_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 828.4 | 825.0 | 842.2 | 7.1 | 1.706x | 1.706x | faster ×1.06 | -5.29% vs bar 0.74% (IQR-only) → **improve (IQR only: band n=0 < 10)** |
| 6 | `pcrec_751b9c6d_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 833.9 | 823.7 | 848.7 | 8.4 | 1.717x | 1.717x | faster ×1.06 | -5.47% vs bar 2.22% (IQR-only) → **improve (IQR only: band n=0 < 10)** |
| 7 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 874.7 | 864.8 | 887.5 | 7.5 | 1.801x | 1.801x | - | - |
| 8 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 882.2 | 858.7 | 896.2 | 13.5 | 1.817x | 1.817x | - | - |

- Δ detail: `pcrec_751b9c6d_vm-in-caps-simdna` vs previous `pcrec_25b1984f_vm-in-caps-simdna`: worst now (also the largest Δ): `s-082`, 8.6 ns, 1 B
- Δ detail: `pcrec_751b9c6d_vm-caps-simdna` vs previous `pcrec_25b1984f_vm-caps-simdna`: worst now: `s-082`, 10.1 ns, 1 B; largest Δ: `s-042`, +1.6 ns (now 7.4 ns), 5 B
- Δ detail: `pcrec_751b9c6d_auto-nocaps-simdna` vs previous `pcrec_25b1984f_auto-nocaps-simdna`: worst now: `s-082`, 13.0 ns, 1 B; largest Δ: `s-050`, -0.7 ns (now 9.6 ns), 17 B
- Δ detail: `pcrec_751b9c6d_auto-caps-simdna` vs previous `pcrec_25b1984f_auto-caps-simdna`: worst now: `s-082`, 13.0 ns, 1 B; largest Δ: `s-032`, -0.7 ns (now 9.7 ns), 16 B

### `floor` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: pcrec_25b1984f_vm-in-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 961.4 | 954.9 | 967.1 | 4.0 | 1.000x | 1.000x | - | - | 77 | 12.5 | 100% |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 1,043.4 | 1,039.8 | 1,045.4 | 1.8 | 1.085x | 1.085x | - | - | 77 | 13.6 | 100% |
| 3 | `pcrec_751b9c6d_vm-in-caps-simdna` | measured | `plain` | same program | 1,160.6 | 1,158.8 | 1,164.6 | 2.0 | 1.207x | 1.207x | slower ×1.21 | +20.72% vs bar 0.28% (IQR-only) → **regress (IQR only: band n=0 < 10)** | 77 | 15.1 | 100% |
| 4 | `pcrec_751b9c6d_vm-caps-simdna` | measured | `plain` | same program | 1,227.3 | 1,224.2 | 1,228.9 | 1.5 | 1.277x | 1.277x | slower ×1.18 | +17.63% vs bar 0.12% (IQR-only) → **regress (IQR only: band n=2 < 10)** | 77 | 15.9 | 100% |
| 5 | `pcrec_751b9c6d_auto-nocaps-simdna` | measured | `plain` | same program | 1,319.7 | 1,317.7 | 1,329.1 | 4.2 | 1.373x | 1.373x | faster ×1.04 | -3.69% (null control: program identical) | 77 | 17.1 | 100% |
| 6 | `pcrec_751b9c6d_auto-caps-simdna` | measured | `plain` | same program | 1,320.4 | 1,319.9 | 1,323.1 | 1.2 | 1.373x | 1.373x | faster ×1.03 | -3.22% (null control: program identical) | 77 | 17.1 | 100% |
| 7 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,364.3 | 1,362.9 | 1,367.5 | 1.5 | 1.419x | 1.419x | - | - | 77 | 17.7 | 100% |
| 8 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,370.4 | 1,367.6 | 1,374.0 | 2.2 | 1.425x | 1.425x | - | - | 77 | 17.8 | 100% |

- Δ detail: `pcrec_751b9c6d_vm-in-caps-simdna` vs previous `pcrec_25b1984f_vm-in-caps-simdna`: worst now: `s-004`, 26.7 ns, 33 B; largest Δ: `s-083`, -31.9 ns (now 9.5 ns), 43 B
- Δ detail: `pcrec_751b9c6d_vm-caps-simdna` vs previous `pcrec_25b1984f_vm-caps-simdna`: worst now: `s-004`, 27.5 ns, 33 B; largest Δ: `s-083`, -31.1 ns (now 10.0 ns), 43 B
- Δ detail: `pcrec_751b9c6d_auto-nocaps-simdna` vs previous `pcrec_25b1984f_auto-nocaps-simdna`: worst now: `s-004`, 18.1 ns, 33 B; largest Δ: `s-081`, -0.9 ns (now 5.0 ns), 0 B
- Δ detail: `pcrec_751b9c6d_auto-caps-simdna` vs previous `pcrec_25b1984f_auto-caps-simdna`: worst now: `s-004`, 18.2 ns, 33 B; largest Δ: `s-081`, -0.9 ns (now 5.0 ns), 0 B

### `orig` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_751b9c6d_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_auto-nocaps-simdna` | measured | `plain` | same program | 7,048,489.6 | 1.3444 | 7,040,718.7 | 7,053,433.2 | 5,019.7 | 1.000x | 1.000x | faster ×2.01 | -50.15% vs bar 0.25% (IQR-only) → **improve (IQR only: band n=2 < 10)** | 5 | 100% |
| 2 | `pcrec_751b9c6d_auto-caps-simdna` | measured | `plain` | same program | 7,053,755.3 | 1.3454 | 7,048,184.0 | 7,194,846.7 | 56,986.4 | 1.001x | 1.001x | faster ×2.00 | -50.08% vs bar 0.17% (IQR-only) → **improve (IQR only: band n=2 < 10)** | 5 | 100% |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 14,131,365.5 | 2.6953 | 14,105,993.7 | 14,195,054.8 | 31,617.7 | 2.005x | 2.005x | - | - | 5 | 100% |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 14,138,384.1 | 2.6967 | 14,117,417.0 | 14,178,994.4 | 22,669.4 | 2.006x | 2.006x | - | - | 5 | 100% |
| 5 | `pcrec_751b9c6d_vm-caps-simdna` | measured | `plain` | same program | 22,840,316.3 | 4.3564 | 22,758,079.6 | 23,117,623.4 | 122,729.8 | 3.240x | 3.240x | now measured (was: gave-up) | - | 5 | 100% |
| 6 | `pcrec_751b9c6d_vm-in-caps-simdna` | measured | `plain` | same program | 23,621,686.4 | 4.5055 | 23,337,194.8 | 23,931,857.4 | 206,785.4 | 3.351x | 3.351x | now measured (was: gave-up) | - | 5 | 100% |

#### `orig` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 3,775,381.2 | 3.6005 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 3,774,303.0 | 3.5995 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 4,143,067.6 | 3.9511 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 4,145,504.2 | 3.9535 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 5,236,612.5 | 4.9940 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 5,963,203.3 | 5.6870 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 17,672.0 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 17,732.3 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 1,886,626.1 | 1.7992 |
| `t-b-no-at` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,888,425.7 | 1.8009 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 17,697.4 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 17,723.3 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 17,690.8 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 17,698.2 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 1,875,434.8 | 1.7886 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,874,718.0 | 1.7879 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 17,681.9 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 17,726.1 | 0.0169 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 3,219,745.6 | 3.0706 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 3,221,893.2 | 3.0726 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 3,132,783.4 | 2.9877 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 3,137,025.9 | 2.9917 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 17,585,066.0 | 16.7704 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 17,609,664.6 | 16.7939 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 17,670.8 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 17,719.7 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 3,083,466.1 | 2.9406 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 3,094,842.2 | 2.9515 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 17,693.5 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 17,716.9 | 0.0169 |

- Δ detail: `pcrec_751b9c6d_auto-nocaps-simdna` vs previous `pcrec_25b1984f_auto-nocaps-simdna`: worst now: `t-a-valid-addrs`, 3,775,381.2 ns, 1,048,576 B; largest Δ: `t-e-prose-no-at`, -3,077,171.4 ns (now 17,670.8 ns), 1,048,576 B
- Δ detail: `pcrec_751b9c6d_auto-caps-simdna` vs previous `pcrec_25b1984f_auto-caps-simdna`: worst now: `t-a-valid-addrs`, 3,774,303.0 ns, 1,048,576 B; largest Δ: `t-e-prose-no-at`, -3,065,746.4 ns (now 17,719.7 ns), 1,048,576 B
- Δ detail: `pcrec_751b9c6d_vm-caps-simdna` vs previous `pcrec_25b1984f_vm-caps-simdna`: worst now: `t-d-prose-sparse-addrs`, 17,585,066.0 ns, 1,048,576 B; largest Δ: `t-e-prose-no-at`, -16,526,333.0 ns (now 17,693.5 ns), 1,048,576 B
- Δ detail: `pcrec_751b9c6d_vm-in-caps-simdna` vs previous `pcrec_25b1984f_vm-in-caps-simdna`: worst now: `t-d-prose-sparse-addrs`, 17,609,664.6 ns, 1,048,576 B; largest Δ: `t-e-prose-no-at`, -16,521,403.6 ns (now 17,716.9 ns), 1,048,576 B

### `orig` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_751b9c6d_vm-in-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 61,998.6 | 61,887.2 | 62,467.7 | 212.1 | 1.000x | 1.000x | unchanged (within spread) | -0.12% vs bar 0.17% (IQR-only) → **within (IQR only: band n=0 < 10)** |
| 2 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 62,071.9 | 62,030.4 | 62,228.5 | 74.3 | 1.001x | 1.001x | - | - |
| 3 | `pcrec_751b9c6d_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 62,876.5 | 62,830.5 | 66,758.3 | 1,542.8 | 1.014x | 1.014x | unchanged (within spread) | -0.04% vs bar 0.19% (IQR-only) → **within (IQR only: band n=0 < 10)** |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 62,899.6 | 62,741.4 | 62,971.2 | 84.0 | 1.015x | 1.015x | - | - |
| 5 | `pcrec_751b9c6d_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,131.7 | 73,120.8 | 73,136.1 | 5.5 | 1.180x | 1.180x | unchanged (within spread) | -0.14% vs bar 0.10% (IQR-only) → **improve (IQR only: band n=0 < 10)** |
| 6 | `pcrec_751b9c6d_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,137.5 | 73,127.5 | 73,141.1 | 5.0 | 1.180x | 1.180x | faster ×1.00 | -0.18% vs bar 0.14% (IQR-only) → **improve (IQR only: band n=0 < 10)** |
| 7 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,231.8 | 73,200.7 | 73,340.4 | 51.8 | 1.181x | 1.181x | - | - |
| 8 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,267.0 | 73,211.0 | 73,343.4 | 53.1 | 1.182x | 1.182x | - | - |

- Δ detail: `pcrec_751b9c6d_vm-in-caps-simdna` vs previous `pcrec_25b1984f_vm-in-caps-simdna`: worst now (also the largest Δ): `s-059`, 13,672.5 ns, 5,134 B
- Δ detail: `pcrec_751b9c6d_vm-caps-simdna` vs previous `pcrec_25b1984f_vm-caps-simdna`: worst now: `s-059`, 13,679.8 ns, 5,134 B; largest Δ: `s-058`, -60.2 ns (now 6,215.7 ns), 4,011 B
- Δ detail: `pcrec_751b9c6d_auto-caps-simdna` vs previous `pcrec_25b1984f_auto-caps-simdna`: worst now: `s-057`, 19,059.8 ns, 10,252 B; largest Δ: `s-060`, -31.4 ns (now 19,035.4 ns), 10,240 B
- Δ detail: `pcrec_751b9c6d_auto-nocaps-simdna` vs previous `pcrec_25b1984f_auto-nocaps-simdna`: worst now: `s-057`, 19,061.8 ns, 10,252 B; largest Δ: `s-060`, -28.8 ns (now 19,036.8 ns), 10,240 B

### `orig` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 3,522.1 | 3,518.8 | 3,594.9 | 29.6 | 1.000x | 1.000x | - | - | 77 | 45.7 | 17.7 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 3,525.6 | 3,521.7 | 3,548.6 | 12.1 | 1.001x | 1.001x | - | - | 77 | 45.8 | 17.8 | 100% |
| 3 | `pcrec_751b9c6d_auto-nocaps-simdna` | measured | `plain` | same program | 3,703.1 | 3,701.2 | 3,705.6 | 1.6 | 1.051x | 1.051x | slower ×1.05 | +5.03% vs bar 0.70% (IQR-only) → **regress (IQR only: band n=2 < 10)** | 77 | 48.1 | 17.1 | 100% |
| 4 | `pcrec_751b9c6d_auto-caps-simdna` | measured | `plain` | same program | 3,704.0 | 3,701.2 | 3,799.8 | 38.6 | 1.052x | 1.052x | slower ×1.05 | +5.16% vs bar 0.05% (IQR-only) → **regress (IQR only: band n=2 < 10)** | 77 | 48.1 | 17.1 | 100% |
| 5 | `pcrec_751b9c6d_vm-caps-simdna` | measured | `plain` | same program | 8,596.0 | 8,554.5 | 8,800.2 | 89.6 | 2.441x | 2.441x | faster ×1.48 | -32.65% vs bar 0.73% (IQR-only) → **improve (IQR only: band n=2 < 10)** | 77 | 111.6 | 15.9 | 100% |
| 6 | `pcrec_751b9c6d_vm-in-caps-simdna` | measured | `plain` | same program | 9,421.3 | 9,367.8 | 9,446.5 | 28.0 | 2.675x | 2.675x | faster ×1.36 | -26.58% vs bar 0.26% (IQR-only) → **improve (IQR only: band n=2 < 10)** | 77 | 122.4 | 15.1 | 100% |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12,764.0 | 12,666.2 | 12,851.3 | 65.7 | 3.624x | 3.624x | - | - | 77 | 165.8 | 13.6 | 100% |
| 8 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 12,831.4 | 12,810.0 | 12,886.0 | 27.0 | 3.643x | 3.643x | - | - | 77 | 166.6 | 12.5 | 100% |

- Δ detail: `pcrec_751b9c6d_auto-nocaps-simdna` vs previous `pcrec_25b1984f_auto-nocaps-simdna`: worst now: `s-004`, 125.2 ns, 33 B; largest Δ: `s-083`, -64.8 ns (now 8.5 ns), 43 B
- Δ detail: `pcrec_751b9c6d_auto-caps-simdna` vs previous `pcrec_25b1984f_auto-caps-simdna`: worst now: `s-004`, 125.4 ns, 33 B; largest Δ: `s-083`, -65.8 ns (now 7.7 ns), 43 B
- Δ detail: `pcrec_751b9c6d_vm-caps-simdna` vs previous `pcrec_25b1984f_vm-caps-simdna`: worst now: `s-035`, 708.2 ns, 16 B; largest Δ: `s-083`, -620.9 ns (now 10.6 ns), 43 B
- Δ detail: `pcrec_751b9c6d_vm-in-caps-simdna` vs previous `pcrec_25b1984f_vm-in-caps-simdna`: worst now: `s-035`, 711.0 ns, 16 B; largest Δ: `s-083`, -619.9 ns (now 11.5 ns), 43 B

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `factored` | `large-subject-throughput` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 5 | 80% | -2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 5 | 80% | -2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `match-compliance` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 85 | 94% | -3:PCREC_ERR_FRAMES×5 (smallest: s-061, 2,008 B) | 0 | `s-058` (gave-up), `s-059` (gave-up), `s-061` (gave-up), `s-063` (gave-up), `s-064` (gave-up) |
| `factored` | `match-compliance` | `whole-subject` | `pcrec_751b9c6d_vm-caps-simdna` | 85 | 94% | -3:PCREC_ERR_FRAMES×5 (smallest: s-061, 2,008 B) | 0 | `s-058` (gave-up), `s-059` (gave-up), `s-061` (gave-up), `s-063` (gave-up), `s-064` (gave-up) |
| `orig` | `large-subject-throughput` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 5 | 80% | -4:PCREC_ERR_WORK×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `orig` | `large-subject-throughput` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 5 | 80% | -4:PCREC_ERR_WORK×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |

## Standing cross-class query (inbox I-101; Frank's own anomaly check -- a QUERY, never a ranking; every hit below is a finding on pcrec's side by definition)

**18 hit(s)** -- each is a finding on pcrec's side by definition (I-101):

| pattern | regime | pcrec auto-nocaps testee | auto-nocaps ns/call | competitor testee | competitor ns/call | ratio (competitor / auto-nocaps) | clears IQR / null band |
|---|---|---|---|---|---|---|---|
| `factored` | `large-subject-throughput` | `pcrec_751b9c6d_auto-nocaps-simdna` | 7,048,417.6 | `pcrec_751b9c6d_auto-caps-simdna` | 7,018,630.0 | 0.996x | clears IQR only: gap 0.42%; IQR 0.06% (clears); band n/a (pcrec 25b1984f -> 751b9c6d, large-subject-throughput / >=1us: n=2 < 10) |
| `floor` | `match-compliance` | `pcrec_25b1984f_auto-nocaps-simdna` | 874.7 | `pcrec_25b1984f_vm-caps-simdna` | 485.6 | 0.555x | clears IQR only: gap 44.49%; IQR 0.74% (clears); band n/a (pcrec 25b1984f -> 751b9c6d, match-compliance / 100ns-1us: n=0 < 10) |
| `floor` | `match-compliance` | `pcrec_25b1984f_auto-nocaps-simdna` | 874.7 | `pcrec_25b1984f_vm-in-caps-simdna` | 505.8 | 0.578x | clears IQR only: gap 42.18%; IQR 0.74% (clears); band n/a (pcrec 25b1984f -> 751b9c6d, match-compliance / 100ns-1us: n=0 < 10) |
| `floor` | `match-compliance` | `pcrec_751b9c6d_auto-nocaps-simdna` | 828.4 | `pcrec_751b9c6d_vm-caps-simdna` | 559.2 | 0.675x | clears IQR only: gap 32.50%; IQR 1.55% (clears); band n/a (pcrec 25b1984f -> 751b9c6d, match-compliance / 100ns-1us: n=0 < 10) |
| `floor` | `match-compliance` | `pcrec_751b9c6d_auto-nocaps-simdna` | 828.4 | `pcrec_751b9c6d_vm-in-caps-simdna` | 529.4 | 0.639x | clears IQR only: gap 36.09%; IQR 1.55% (clears); band n/a (pcrec 25b1984f -> 751b9c6d, match-compliance / 100ns-1us: n=0 < 10) |
| `floor` | `short-subject-search` | `pcrec_25b1984f_auto-nocaps-simdna` | 1,370.4 | `pcrec_25b1984f_auto-caps-simdna` | 1,364.3 | 0.996x | clears IQR only: gap 0.44%; IQR 0.22% (clears); band n/a (pcrec 25b1984f -> 751b9c6d, short-subject-search / >=1us: n=2 < 10) |
| `floor` | `short-subject-search` | `pcrec_25b1984f_auto-nocaps-simdna` | 1,370.4 | `pcrec_25b1984f_vm-caps-simdna` | 1,043.4 | 0.761x | clears IQR only: gap 23.86%; IQR 0.22% (clears); band n/a (pcrec 25b1984f -> 751b9c6d, short-subject-search / >=1us: n=2 < 10) |
| `floor` | `short-subject-search` | `pcrec_25b1984f_auto-nocaps-simdna` | 1,370.4 | `pcrec_25b1984f_vm-in-caps-simdna` | 961.4 | 0.702x | clears IQR only: gap 29.84%; IQR 0.22% (clears); band n/a (pcrec 25b1984f -> 751b9c6d, short-subject-search / >=1us: n=2 < 10) |
| `floor` | `short-subject-search` | `pcrec_751b9c6d_auto-nocaps-simdna` | 1,319.7 | `pcrec_751b9c6d_vm-caps-simdna` | 1,227.3 | 0.930x | clears IQR only: gap 7.00%; IQR 0.26% (clears); band n/a (pcrec 25b1984f -> 751b9c6d, short-subject-search / >=1us: n=2 < 10) |
| `floor` | `short-subject-search` | `pcrec_751b9c6d_auto-nocaps-simdna` | 1,319.7 | `pcrec_751b9c6d_vm-in-caps-simdna` | 1,160.6 | 0.879x | clears IQR only: gap 12.06%; IQR 0.26% (clears); band n/a (pcrec 25b1984f -> 751b9c6d, short-subject-search / >=1us: n=2 < 10) |
| `orig` | `large-subject-throughput` | `pcrec_25b1984f_auto-nocaps-simdna` | 14,138,384.1 | `pcrec_25b1984f_auto-caps-simdna` | 14,131,365.5 | 1.000x | within IQR: gap 0.05%; IQR 0.25% (within); band n/a (pcrec 25b1984f -> 751b9c6d, large-subject-throughput / >=1us: n=2 < 10) |
| `orig` | `match-compliance` | `pcrec_25b1984f_auto-nocaps-simdna` | 73,267.0 | `pcrec_25b1984f_auto-caps-simdna` | 73,231.8 | 1.000x | within IQR: gap 0.05%; IQR 0.14% (within); band n/a (pcrec 25b1984f -> 751b9c6d, match-compliance / >=1us: n=0 < 10) |
| `orig` | `match-compliance` | `pcrec_25b1984f_auto-nocaps-simdna` | 73,267.0 | `pcrec_25b1984f_vm-caps-simdna` | 62,899.6 | 0.858x | clears IQR only: gap 14.15%; IQR 0.16% (clears); band n/a (pcrec 25b1984f -> 751b9c6d, match-compliance / >=1us: n=0 < 10) |
| `orig` | `match-compliance` | `pcrec_25b1984f_auto-nocaps-simdna` | 73,267.0 | `pcrec_25b1984f_vm-in-caps-simdna` | 62,071.9 | 0.847x | clears IQR only: gap 15.28%; IQR 0.14% (clears); band n/a (pcrec 25b1984f -> 751b9c6d, match-compliance / >=1us: n=0 < 10) |
| `orig` | `match-compliance` | `pcrec_751b9c6d_auto-nocaps-simdna` | 73,137.5 | `pcrec_751b9c6d_auto-caps-simdna` | 73,131.7 | 1.000x | within IQR: gap 0.01%; IQR 0.01% (within); band n/a (pcrec 25b1984f -> 751b9c6d, match-compliance / >=1us: n=0 < 10) |
| `orig` | `match-compliance` | `pcrec_751b9c6d_auto-nocaps-simdna` | 73,137.5 | `pcrec_751b9c6d_vm-caps-simdna` | 62,876.5 | 0.860x | clears IQR only: gap 14.03%; IQR 0.23% (clears); band n/a (pcrec 25b1984f -> 751b9c6d, match-compliance / >=1us: n=0 < 10) |
| `orig` | `match-compliance` | `pcrec_751b9c6d_auto-nocaps-simdna` | 73,137.5 | `pcrec_751b9c6d_vm-in-caps-simdna` | 61,998.6 | 0.848x | clears IQR only: gap 15.23%; IQR 0.22% (clears); band n/a (pcrec 25b1984f -> 751b9c6d, match-compliance / >=1us: n=0 < 10) |
| `orig` | `short-subject-search` | `pcrec_25b1984f_auto-nocaps-simdna` | 3,525.6 | `pcrec_25b1984f_auto-caps-simdna` | 3,522.1 | 0.999x | within IQR: gap 0.10%; IQR 0.70% (within); band n/a (pcrec 25b1984f -> 751b9c6d, short-subject-search / >=1us: n=2 < 10) |

## Compile cost (by execution-model class; never pooled across classes)

### `compiled-aot`

- `pcrec_25b1984f_auto-caps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_vm-caps-simdna` / `factored` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 39,546 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `factored` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 39,654 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `floor` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 236 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `floor` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 339 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `orig` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 28,839 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `orig` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 28,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `factored` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 39,546 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `factored` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 39,654 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `floor` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 236 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `floor` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 339 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `orig` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 28,839 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `orig` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 28,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_751b9c6d_auto-caps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_751b9c6d_auto-caps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_751b9c6d_auto-caps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_751b9c6d_auto-caps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_751b9c6d_auto-caps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_751b9c6d_auto-caps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_751b9c6d_auto-nocaps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_751b9c6d_auto-nocaps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_751b9c6d_auto-nocaps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_751b9c6d_auto-nocaps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_751b9c6d_auto-nocaps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_751b9c6d_auto-nocaps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_751b9c6d_vm-caps-simdna` / `factored` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 39,546 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_751b9c6d_vm-caps-simdna` / `factored` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 39,654 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_751b9c6d_vm-caps-simdna` / `floor` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 236 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_751b9c6d_vm-caps-simdna` / `floor` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 339 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_751b9c6d_vm-caps-simdna` / `orig` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 28,839 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_751b9c6d_vm-caps-simdna` / `orig` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 28,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_751b9c6d_vm-in-caps-simdna` / `factored` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 39,546 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_751b9c6d_vm-in-caps-simdna` / `factored` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 39,654 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_751b9c6d_vm-in-caps-simdna` / `floor` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 236 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_751b9c6d_vm-in-caps-simdna` / `floor` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 339 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_751b9c6d_vm-in-caps-simdna` / `orig` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 28,839 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_751b9c6d_vm-in-caps-simdna` / `orig` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 28,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
    - sel = pcrec's `RX_ENGINE_SEL`; `DFA fallback tripped` = sel not in (selected, forced), and NOTHING else -- since pcrec 263b013 ([LIM-1] / [OPT-4.1]) every fallback has its own token (`overflowed-dfa`, `overflowed-prefilter`, `collapsed-prefilter`, `declined-nullable`, `size-cap-retry`), the size-cap rescue included; at pcrec 96e44c2 that rescue stamped `sel=selected` and only its `lang=count-collapsed (size cap retry, ...)` clause says so.
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
| `factored` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 173,526,814.0 | 164,766,687.0 | 181,490,745.0 | 6,338,789.0 | 5 | 48,128 | 82,643 | 13,949 | 0.037 (max is trial 1) | compiled=5 | 10,395,046.0 | 160,879,176.0 | 189,471.0 |
| `factored` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 186,029,821.0 | 170,466,739.0 | 206,000,837.0 | 11,357,854.9 | 5 | 48,264 | 94,854 | 15,865 | 0.061 | compiled=5 | 12,996,749.0 | 172,858,711.0 | 174,361.0 |
| `factored` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 168,681,429.0 | 156,403,863.0 | 181,503,177.0 | 8,812,007.3 | 5 | 48,128 | 82,460 | 13,762 | 0.052 (max is trial 1) | compiled=5 | 10,525,176.0 | 156,384,723.0 | 189,021.0 |
| `factored` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 181,271,647.0 | 178,884,604.0 | 182,453,363.0 | 1,282,469.9 | 5 | 48,264 | 94,671 | 15,678 | 0.007 (max is trial 1) | compiled=5 | 12,978,020.0 | 166,770,179.0 | 110,180.0 |
| `factored` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 571,637,701.0 | 557,575,008.0 | 575,374,422.0 | 6,300,976.6 | 5 | 39,936 | 58,762 | 57,208 | 0.011 | compiled=5 | 2,270,593.0 | 566,253,219.0 | 193,121.0 |
| `factored` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 566,462,271.0 | 562,968,250.0 | 594,057,801.0 | 12,339,418.7 | 5 | 39,936 | 58,878 | 57,324 | 0.022 | compiled=5 | 4,766,337.0 | 561,527,712.0 | 92,481.0 |
| `factored` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 573,406,753.0 | 560,698,170.0 | 588,568,428.0 | 9,061,480.9 | 5 | 39,936 | 58,762 | 57,208 | 0.016 | compiled=5 | 2,286,311.0 | 570,885,651.0 | 195,401.0 |
| `factored` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 573,429,854.0 | 568,076,198.0 | 577,436,234.0 | 3,411,473.3 | 5 | 39,936 | 58,878 | 57,324 | 0.006 | compiled=5 | 2,301,011.0 | 571,018,422.0 | 110,421.0 |
| `factored` | `plain` | `pcrec_751b9c6d_auto-caps-simdna` | 176,165,338.0 | 169,951,885.0 | 196,473,115.0 | 10,135,069.5 | 5 | 48,352 | 83,886 | 15,192 | 0.058 | compiled=5 | 12,853,278.0 | 161,116,428.0 | 196,921.0 |
| `factored` | `whole-subject` | `pcrec_751b9c6d_auto-caps-simdna` | 185,721,738.0 | 173,410,853.0 | 190,569,704.0 | 6,034,344.4 | 5 | 48,496 | 96,097 | 17,108 | 0.032 | compiled=5 | 13,036,999.0 | 172,772,170.0 | 123,491.0 |
| `factored` | `plain` | `pcrec_751b9c6d_auto-nocaps-simdna` | 168,937,809.0 | 163,870,263.0 | 177,438,115.0 | 4,591,805.3 | 5 | 48,352 | 83,703 | 15,005 | 0.027 | compiled=5 | 12,637,407.0 | 155,611,830.0 | 197,511.0 |
| `factored` | `whole-subject` | `pcrec_751b9c6d_auto-nocaps-simdna` | 185,504,757.0 | 168,100,154.0 | 208,858,921.0 | 14,070,465.5 | 5 | 48,496 | 95,914 | 16,921 | 0.076 (max is trial 1) | compiled=5 | 13,058,369.0 | 172,213,227.0 | 108,331.0 |
| `factored` | `plain` | `pcrec_751b9c6d_vm-caps-simdna` | 576,139,717.0 | 569,680,273.0 | 586,426,511.0 | 5,370,233.7 | 5 | 44,264 | 60,302 | 58,694 | 0.009 | compiled=5 | 2,397,543.0 | 573,555,424.0 | 127,010.0 |
| `factored` | `whole-subject` | `pcrec_751b9c6d_vm-caps-simdna` | 578,346,268.0 | 568,374,987.0 | 595,478,368.0 | 10,527,133.0 | 5 | 44,264 | 60,418 | 58,810 | 0.018 | compiled=5 | 2,480,624.0 | 575,769,775.0 | 198,041.0 |
| `factored` | `plain` | `pcrec_751b9c6d_vm-in-caps-simdna` | 584,225,110.0 | 576,541,099.0 | 590,554,034.0 | 4,707,838.2 | 5 | 44,264 | 60,302 | 58,694 | 0.008 | compiled=5 | 2,720,684.0 | 578,623,870.0 | 206,042.0 |
| `factored` | `whole-subject` | `pcrec_751b9c6d_vm-in-caps-simdna` | 587,832,999.0 | 572,366,057.0 | 592,267,772.0 | 7,146,849.0 | 5 | 44,264 | 60,418 | 58,810 | 0.012 | compiled=5 | 2,492,624.0 | 585,122,764.0 | 217,611.0 |
| `floor` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 150,392,660.0 | 141,045,572.0 | 152,132,871.0 | 3,925,733.9 | 5 | 27,608 | 18,294 | 13,297 | 0.026 | compiled=5 | 1,681,089.0 | 148,544,911.0 | 113,721.0 |
| `floor` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 159,682,441.0 | 152,028,068.0 | 176,186,068.0 | 8,194,139.2 | 5 | 27,752 | 20,637 | 15,314 | 0.051 | compiled=5 | 1,710,609.0 | 155,587,679.0 | 187,651.0 |
| `floor` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 147,937,338.0 | 140,196,106.0 | 153,161,896.0 | 4,472,283.5 | 5 | 27,608 | 18,294 | 13,297 | 0.030 | compiled=5 | 1,665,219.0 | 146,008,117.0 | 98,841.0 |
| `floor` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 159,648,271.0 | 149,105,894.0 | 164,562,937.0 | 5,277,252.6 | 5 | 27,752 | 20,637 | 15,314 | 0.033 | compiled=5 | 1,797,069.0 | 157,121,978.0 | 187,311.0 |
| `floor` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 134,754,625.0 | 125,109,458.0 | 141,177,793.0 | 6,732,611.9 | 5 | 23,072 | 17,837 | 17,837 | 0.050 | compiled=5 | 1,447,328.0 | 133,138,416.0 | 107,971.0 |
| `floor` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 137,947,814.0 | 128,667,100.0 | 144,615,432.0 | 5,824,084.4 | 5 | 23,072 | 17,948 | 17,948 | 0.042 | compiled=5 | 1,440,808.0 | 136,275,634.0 | 105,560.0 |
| `floor` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 136,660,116.0 | 131,490,790.0 | 142,668,874.0 | 4,334,978.6 | 5 | 23,072 | 17,837 | 17,837 | 0.032 | compiled=5 | 1,643,548.0 | 133,541,640.0 | 192,511.0 |
| `floor` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 133,836,271.0 | 129,480,890.0 | 139,214,469.0 | 4,000,255.9 | 5 | 23,072 | 17,948 | 17,948 | 0.030 (max is trial 1) | compiled=5 | 1,446,067.0 | 132,247,174.0 | 187,101.0 |
| `floor` | `plain` | `pcrec_751b9c6d_auto-caps-simdna` | 155,608,989.0 | 144,033,349.0 | 158,410,945.0 | 5,606,026.0 | 5 | 27,792 | 19,406 | 14,409 | 0.036 | compiled=5 | 2,043,281.0 | 153,692,710.0 | 118,701.0 |
| `floor` | `whole-subject` | `pcrec_751b9c6d_auto-caps-simdna` | 163,951,553.0 | 154,908,956.0 | 165,616,893.0 | 4,627,729.4 | 5 | 27,936 | 21,861 | 16,538 | 0.028 | compiled=5 | 1,831,690.0 | 162,031,913.0 | 118,251.0 |
| `floor` | `plain` | `pcrec_751b9c6d_auto-nocaps-simdna` | 150,936,946.0 | 143,526,446.0 | 159,092,858.0 | 5,218,235.7 | 5 | 27,792 | 19,406 | 14,409 | 0.035 | compiled=5 | 2,048,871.0 | 148,998,255.0 | 210,272.0 |
| `floor` | `whole-subject` | `pcrec_751b9c6d_auto-nocaps-simdna` | 165,490,831.0 | 155,222,089.0 | 171,165,671.0 | 5,627,958.9 | 5 | 27,936 | 21,861 | 16,538 | 0.034 (max is trial 1) | compiled=5 | 1,855,280.0 | 162,441,446.0 | 196,152.0 |
| `floor` | `plain` | `pcrec_751b9c6d_vm-caps-simdna` | 142,192,828.0 | 136,093,417.0 | 148,688,534.0 | 4,406,135.0 | 5 | 23,304 | 19,133 | 19,133 | 0.031 | compiled=5 | 1,558,598.0 | 140,525,230.0 | 107,781.0 |
| `floor` | `whole-subject` | `pcrec_751b9c6d_vm-caps-simdna` | 141,420,036.0 | 139,478,215.0 | 148,944,085.0 | 3,712,058.1 | 5 | 23,304 | 19,356 | 19,356 | 0.026 | compiled=5 | 1,576,759.0 | 138,298,569.0 | 204,191.0 |
| `floor` | `plain` | `pcrec_751b9c6d_vm-in-caps-simdna` | 147,429,877.0 | 137,109,183.0 | 149,116,775.0 | 5,452,278.7 | 5 | 23,304 | 19,133 | 19,133 | 0.037 | compiled=5 | 1,706,989.0 | 145,745,158.0 | 107,761.0 |
| `floor` | `whole-subject` | `pcrec_751b9c6d_vm-in-caps-simdna` | 141,711,338.0 | 139,209,483.0 | 152,721,425.0 | 5,374,774.0 | 5 | 23,304 | 19,356 | 19,356 | 0.038 | compiled=5 | 1,593,108.0 | 139,920,498.0 | 197,881.0 |
| `orig` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 173,309,253.0 | 165,686,853.0 | 178,341,950.0 | 4,878,175.1 | 5 | 48,088 | 82,236 | 13,709 | 0.028 | compiled=5 | 9,909,873.0 | 156,121,711.0 | 185,431.0 |
| `orig` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 183,255,716.0 | 172,385,108.0 | 186,693,395.0 | 4,956,690.6 | 5 | 48,224 | 94,447 | 15,625 | 0.027 (max is trial 1) | compiled=5 | 12,300,625.0 | 167,948,045.0 | 116,710.0 |
| `orig` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 179,676,289.0 | 159,232,408.0 | 190,602,777.0 | 12,059,362.9 | 5 | 48,088 | 82,236 | 13,709 | 0.067 (max is trial 1) | compiled=5 | 12,042,185.0 | 166,726,229.0 | 186,401.0 |
| `orig` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 180,355,242.0 | 172,212,788.0 | 196,159,277.0 | 7,844,183.0 | 5 | 48,224 | 94,447 | 15,625 | 0.043 (max is trial 1) | compiled=5 | 12,109,145.0 | 166,968,820.0 | 190,301.0 |
| `orig` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 446,696,252.0 | 442,685,129.0 | 449,710,861.0 | 2,531,966.7 | 5 | 35,760 | 47,591 | 46,204 | 0.006 (max is trial 1) | compiled=5 | 3,780,542.0 | 442,800,800.0 | 190,731.0 |
| `orig` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 439,876,962.0 | 429,616,723.0 | 446,978,854.0 | 5,741,717.6 | 5 | 35,760 | 47,709 | 46,322 | 0.013 (max is trial 1) | compiled=5 | 2,021,122.0 | 437,670,750.0 | 105,661.0 |
| `orig` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 439,646,101.0 | 432,618,487.0 | 448,206,325.0 | 5,990,601.0 | 5 | 35,760 | 47,591 | 46,204 | 0.014 | compiled=5 | 2,315,571.0 | 435,607,032.0 | 109,971.0 |
| `orig` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 438,950,479.0 | 438,450,046.0 | 441,788,012.0 | 1,181,345.0 | 5 | 35,760 | 47,709 | 46,322 | 0.003 | compiled=5 | 2,027,140.0 | 436,816,828.0 | 109,560.0 |
| `orig` | `plain` | `pcrec_751b9c6d_auto-caps-simdna` | 170,948,340.0 | 162,246,404.0 | 176,646,581.0 | 5,434,696.4 | 5 | 48,320 | 83,479 | 14,952 | 0.032 | compiled=5 | 10,201,704.0 | 157,190,908.0 | 200,461.0 |
| `orig` | `whole-subject` | `pcrec_751b9c6d_auto-caps-simdna` | 184,587,183.0 | 175,857,756.0 | 202,110,285.0 | 9,283,126.6 | 5 | 48,456 | 95,690 | 16,868 | 0.050 | compiled=5 | 12,547,796.0 | 171,134,501.0 | 200,881.0 |
| `orig` | `plain` | `pcrec_751b9c6d_auto-nocaps-simdna` | 173,343,853.0 | 164,964,798.0 | 195,040,547.0 | 10,999,416.8 | 5 | 48,320 | 83,479 | 14,952 | 0.063 (max is trial 1) | compiled=5 | 10,212,413.0 | 162,901,409.0 | 194,831.0 |
| `orig` | `whole-subject` | `pcrec_751b9c6d_auto-nocaps-simdna` | 185,316,116.0 | 183,678,096.0 | 197,207,167.0 | 5,033,881.3 | 5 | 48,456 | 95,690 | 16,868 | 0.027 (max is trial 1) | compiled=5 | 13,009,958.0 | 171,621,184.0 | 107,491.0 |
| `orig` | `plain` | `pcrec_751b9c6d_vm-caps-simdna` | 451,346,230.0 | 445,656,879.0 | 468,099,107.0 | 7,745,808.2 | 5 | 35,992 | 49,131 | 47,690 | 0.017 | compiled=5 | 2,144,891.0 | 449,001,527.0 | 116,940.0 |
| `orig` | `whole-subject` | `pcrec_751b9c6d_vm-caps-simdna` | 446,200,222.0 | 441,234,595.0 | 465,314,273.0 | 8,474,990.7 | 5 | 35,992 | 49,249 | 47,808 | 0.019 | compiled=5 | 2,121,691.0 | 443,974,881.0 | 104,941.0 |
| `orig` | `plain` | `pcrec_751b9c6d_vm-in-caps-simdna` | 440,170,060.0 | 432,054,367.0 | 452,054,323.0 | 7,025,957.5 | 5 | 35,992 | 49,131 | 47,690 | 0.016 | compiled=5 | 2,130,671.0 | 437,934,009.0 | 204,081.0 |
| `orig` | `whole-subject` | `pcrec_751b9c6d_vm-in-caps-simdna` | 439,169,464.0 | 434,068,269.0 | 460,292,136.0 | 10,513,387.1 | 5 | 35,992 | 49,249 | 47,808 | 0.024 | compiled=5 | 2,171,241.0 | 436,819,872.0 | 200,181.0 |

