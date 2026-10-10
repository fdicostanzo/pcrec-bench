# pcrec-bench report

reporter: v25 (2026-09-26)

## Query

- filters: subbench=email-specimen, version=0.2, machine=budu-ryzen1600, testee=pcrec_a15fb77b_auto-caps-simdna, testee=pcrec_a15fb77b_auto-nocaps-simdna, testee=pcrec_7388f1c0_auto-caps-simdna, testee=pcrec_7388f1c0_auto-nocaps-simdna
- record source: store/index.tsv (4 record(s) matching this query)
- records included: 4
- worst other-core busy: 2.53% (`pcrec_a15fb77b_auto-caps-simdna` / `floor` / `large-subject-throughput`)
    - `email-specimen@0.2__pcrec_7388f1c0_auto-caps-simdna__budu-ryzen1600__20261010T212216Z` (store/records/email-specimen@0.2/pcrec_7388f1c0_auto-caps-simdna/email-specimen@0.2__pcrec_7388f1c0_auto-caps-simdna__budu-ryzen1600__20261010T212216Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_7388f1c0_auto-nocaps-simdna__budu-ryzen1600__20261010T212820Z` (store/records/email-specimen@0.2/pcrec_7388f1c0_auto-nocaps-simdna/email-specimen@0.2__pcrec_7388f1c0_auto-nocaps-simdna__budu-ryzen1600__20261010T212820Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_a15fb77b_auto-caps-simdna__budu-ryzen1600__20261010T211611Z` (store/records/email-specimen@0.2/pcrec_a15fb77b_auto-caps-simdna/email-specimen@0.2__pcrec_a15fb77b_auto-caps-simdna__budu-ryzen1600__20261010T211611Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_a15fb77b_auto-nocaps-simdna__budu-ryzen1600__20261010T213423Z` (store/records/email-specimen@0.2/pcrec_a15fb77b_auto-nocaps-simdna/email-specimen@0.2__pcrec_a15fb77b_auto-nocaps-simdna__budu-ryzen1600__20261010T213423Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
- sub-bench version(s): email-specimen@0.2
- machine(s): budu-ryzen1600
- schema version(s): 1.7
- grain: set (sum of per-subject ns/call over the whole subject set, reduced over trials; a set cell is excluded if ANY subject in it fails)
- reduction: median/min/max/stddev (population) over per-trial `elapsed_ns / iterations`; lazy-JIT compile cost is DERIVED as first-match-row-minus-steady-state (lowest `seq` timed row for the pattern, minus the median of every other timed row), one value per (pattern, testee), never pooled with another execution-model class's compile cost
- `form`: this report includes a `whole-subject` artifact beside `plain` for at least one cell (schema v1.1: a testee with no end-anchored mode compiles and times a SEPARATE artifact for match-compliance, e.g. `(?:pattern)\z`, where another testee reaches the same regime via runtime flags on its ordinary artifact) -- shown as a per-row COLUMN, not a split: both forms answer the same regime and RANK TOGETHER in one table (`form` is a key only for compile-cost rows, where a whole-subject artifact is genuinely a separate compile with its own cost); `fact` restates it as 'same program' / 'separate artifact' (R4)
- status policy (OD-B14): a ranking row whose record `status` is not `measured` is excluded from ranking by default, listed under its table as `not ranked: <testee> -- <status> (<status_detail excerpt>)`; `--include-unmeasured` ranks it instead, with `status` shown
- trial-agreement policy (schema v1.4, rule v1.4-group, X31-X33): a record's five trials must agree to within k=1.5 on every group of its rows — one slow trial of five tolerated; two, or one fast, is a disagreeing row; a group disagrees at >= 2 disagreeing rows reaching a third of it (d_min=2, c=3); a record with a disagreeing group, or with fewer than five odd trials, is `inconclusive-spread` and unranked like `inconclusive-load`; the after-run load/occupancy samples are provenance (v1.4 X13), shown under --include-provenance
- status rule: v1.4 X13 (pre-flight + trial agreement) on 4 record(s)
- tier policy (R3, schema v1.2 `tier`, absent = `pinned`): a `scratch`-tier row is excluded from ranking by default, listed as `scratch: <testee>`; `--include-scratch` ranks it instead, with a `tier` column
- duplicate-record policy (OD-B15, amended 2026-08-25): the NEWEST MEASURED record per (subbench@version, testee_id, machine) ranks by default -- a newer record that is NOT measured does not supersede a measured one of the same testee and version (listed as "newer, not measured" instead); only when no record in the group is measured does the newest record overall stand (itself unranked per the status policy above, unless --include-unmeasured). `--all-records` shows every record as its own row, its testee id suffixed `@<timestamp>`

## Null-control band (D119 bar; [B79], inbox I-93 block B / I-104)

- D119 bar (inbox I-93 block B / I-104): a cross-pin cell moved iff |Δ%| > max(IQR%, null band) -- Δ% = (after - before) / before; IQR% = the BEFORE side's Type-7 IQR of its per-trial set sums over the before median; null band = the largest |Δ%| any PROGRAM-IDENTICAL cell of the same (regime, baseline scale) stratum reached across the same pin pair (symmetric); a stratum with fewer than 10 program-identical cells has NO usable band and its verdicts say `IQR only` by name.
- baseline scale: the BEFORE (older pin) set-grain median -- `>=1us` / `100ns-1us` / `<100ns`; strata are per REGIME (I-104).
- sufficiency: a stratum needs >= 10 program-identical cells -- the band is a sample maximum, and one more null cell exceeds the maximum of n with chance 1/(n+1) (<= 9.1% at n = 10).
- identity: the records' own `engine_metadata.program_sha256` ([B88], schema v1.7) where BOTH compile rows of a cell carry it; otherwise OUR OWN census (`tools/program_identity.py`: both pins re-emitted with the pinned binaries under each config's recorded flags, `.c` + `.h` compared after dropping ONLY the generated-by line, the `.abi` integer and one-sided `#define` stamps). Which records carry the field, per side: `pcrec 7388f1c0 -> a15fb77b`: the BEFORE (`7388f1c0`) records carry `program_sha256` (6 of 6 compiled cell(s)), the AFTER (`a15fb77b`) records carry `program_sha256` (6 of 6 compiled cell(s)); `pcrec a15fb77b -> 7388f1c0`: the BEFORE (`a15fb77b`) records carry `program_sha256` (6 of 6 compiled cell(s)), the AFTER (`7388f1c0`) records carry `program_sha256` (6 of 6 compiled cell(s)).

### `pcrec 7388f1c0 -> a15fb77b` (email-specimen@0.2)

- identity from the records ([B88], schema v1.7): 9 cell(s) read `engine_metadata.program_sha256` on BOTH compile rows, 0 fell back to the census; no census for this pair
- cells: 9 cross-pin set cell(s) measured on both sides; 6 program-identical (the null population)

| regime | baseline scale | n null cells | min Δ% | median Δ% | max Δ% | band (±) | status |
|---|---|---|---|---|---|---|---|
| `large-subject-throughput` | `>=1us` | 3 | -0.07% | -0.01% | +0.05% | n/a | insufficient (n=3 < 10) |
| `large-subject-throughput` | `100ns-1us` | 0 | - | - | - | n/a | empty (n=0) |
| `large-subject-throughput` | `<100ns` | 0 | - | - | - | n/a | empty (n=0) |
| `match-compliance` | `>=1us` | 0 | - | - | - | n/a | empty (n=0) |
| `match-compliance` | `100ns-1us` | 0 | - | - | - | n/a | empty (n=0) |
| `match-compliance` | `<100ns` | 0 | - | - | - | n/a | empty (n=0) |
| `short-subject-search` | `>=1us` | 3 | +0.05% | +0.12% | +0.18% | n/a | insufficient (n=3 < 10) |
| `short-subject-search` | `100ns-1us` | 0 | - | - | - | n/a | empty (n=0) |
| `short-subject-search` | `<100ns` | 0 | - | - | - | n/a | empty (n=0) |

### `pcrec a15fb77b -> 7388f1c0` (email-specimen@0.2)

- identity from the records ([B88], schema v1.7): 9 cell(s) read `engine_metadata.program_sha256` on BOTH compile rows, 0 fell back to the census; no census for this pair
- cells: 9 cross-pin set cell(s) measured on both sides; 6 program-identical (the null population)

| regime | baseline scale | n null cells | min Δ% | median Δ% | max Δ% | band (±) | status |
|---|---|---|---|---|---|---|---|
| `large-subject-throughput` | `>=1us` | 3 | -0.21% | +0.02% | +0.02% | n/a | insufficient (n=3 < 10) |
| `large-subject-throughput` | `100ns-1us` | 0 | - | - | - | n/a | empty (n=0) |
| `large-subject-throughput` | `<100ns` | 0 | - | - | - | n/a | empty (n=0) |
| `match-compliance` | `>=1us` | 0 | - | - | - | n/a | empty (n=0) |
| `match-compliance` | `100ns-1us` | 0 | - | - | - | n/a | empty (n=0) |
| `match-compliance` | `<100ns` | 0 | - | - | - | n/a | empty (n=0) |
| `short-subject-search` | `>=1us` | 3 | -0.10% | +0.07% | +0.08% | n/a | insufficient (n=3 < 10) |
| `short-subject-search` | `100ns-1us` | 0 | - | - | - | n/a | empty (n=0) |
| `short-subject-search` | `<100ns` | 0 | - | - | - | n/a | empty (n=0) |

_[B82] (inbox I-99, Frank's ruling -- a D119 addendum): this report's roster spans BOTH capture classes, so the two views below are the HEADLINE -- "If an engine is run non-capturing on a pattern, then we can't compare that to a capturing engine run -- they are almost completely different things with different objectives." No cell in either view compares across classes; the third, MIXED table further down restates today's single-roster ranking and is never the headline._

## Ranking -- CAPTURING engines only, caps vs caps (per pattern x regime, SET grain: sum over the subject set; best median first)

_D119 bar in this view: |Δ%| > max(IQR%, null band), the `D119 bar` column (definition, strata and bands in the null-control section above). This view's own threshold population: 9 cross-pin cell(s): 1 improve, 0 regress, 2 within the bar, 6 null-control (program identical -- the band's own population); 3 of the verdicts are IQR-only (their stratum's band is not usable)._

### `factored` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | `plain` | same program | 7,021,205.1 | 1.3392 | 7,012,143.1 | 7,025,655.3 | 4,478.6 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | `plain` | same program | 7,022,515.1 | 1.3394 | 7,020,140.7 | 7,025,356.9 | 1,967.4 | 1.000x | 1.000x | unchanged (within spread) | +0.02% (null control: program identical) |

#### `factored` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_a15fb77b_auto-caps-simdna` | 3,804,411.7 | 3.6282 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 3,805,429.9 | 3.6291 |
| `t-b-no-at` | 1,048,576 | `pcrec_a15fb77b_auto-caps-simdna` | 17,715.1 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 17,682.7 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_a15fb77b_auto-caps-simdna` | 17,649.6 | 0.0168 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 17,660.3 | 0.0168 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_a15fb77b_auto-caps-simdna` | 3,163,933.4 | 3.0174 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 3,164,062.6 | 3.0175 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_a15fb77b_auto-caps-simdna` | 17,675.1 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 17,660.4 | 0.0168 |

- Δ detail: `pcrec_7388f1c0_auto-caps-simdna` vs previous `pcrec_a15fb77b_auto-caps-simdna`: worst now (also the largest Δ): `t-a-valid-addrs`, 3,805,429.9 ns, 1,048,576 B

### `factored` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,224.1 | 73,220.7 | 73,342.4 | 46.3 | 1.000x | 1.000x | unchanged (within spread) | -0.01% vs bar 0.01% (IQR-only) → **within (IQR only: band n=0 < 10)** |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,228.7 | 73,221.4 | 73,296.6 | 28.6 | 1.000x | 1.000x | - | - |

- Δ detail: `pcrec_7388f1c0_auto-caps-simdna` vs previous `pcrec_a15fb77b_auto-caps-simdna`: worst now: `s-057`, 19,063.8 ns, 10,252 B; largest Δ: `s-063`, +2.0 ns (now 4,785.2 ns), 5,135 B

### `factored` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | `plain` | same program | 3,896.3 | 3,893.7 | 4,595.2 | 279.9 | 1.000x | 1.000x | - | - | 77 | 50.6 | 17.2 | 100% |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | `plain` | same program | 3,899.1 | 3,895.1 | 3,902.8 | 2.7 | 1.001x | 1.001x | unchanged (within spread) | +0.07% (null control: program identical) | 77 | 50.6 | 17.2 | 100% |

- Δ detail: `pcrec_7388f1c0_auto-caps-simdna` vs previous `pcrec_a15fb77b_auto-caps-simdna`: worst now: `s-004`, 129.1 ns, 33 B; largest Δ: `s-001`, +0.8 ns (now 87.0 ns), 21 B

### `floor` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | `plain` | same program | 698,801.3 | 0.1333 | 698,661.3 | 698,840.6 | 65.0 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | `plain` | same program | 698,916.4 | 0.1333 | 698,543.3 | 701,266.5 | 990.6 | 1.000x | 1.000x | unchanged (within spread) | +0.02% (null control: program identical) |

#### `floor` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_a15fb77b_auto-caps-simdna` | 614,617.3 | 0.5861 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 614,572.7 | 0.5861 |
| `t-b-no-at` | 1,048,576 | `pcrec_a15fb77b_auto-caps-simdna` | 17,742.7 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 17,697.6 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_a15fb77b_auto-caps-simdna` | 17,717.6 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 17,700.8 | 0.0169 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_a15fb77b_auto-caps-simdna` | 31,025.1 | 0.0296 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 31,213.1 | 0.0298 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_a15fb77b_auto-caps-simdna` | 17,658.2 | 0.0168 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 17,671.5 | 0.0169 |

- Δ detail: `pcrec_7388f1c0_auto-caps-simdna` vs previous `pcrec_a15fb77b_auto-caps-simdna`: worst now: `t-a-valid-addrs`, 614,572.7 ns, 1,048,576 B; largest Δ: `t-d-prose-sparse-addrs`, +188.0 ns (now 31,213.1 ns), 1,048,576 B

### `floor` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 758.7 | 758.6 | 759.3 | 0.2 | 1.000x | 1.000x | unchanged (within spread) | -0.05% vs bar 0.14% (IQR-only) → **within (IQR only: band n=0 < 10)** |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 759.1 | 758.7 | 760.1 | 0.6 | 1.001x | 1.001x | - | - |

- Δ detail: `pcrec_7388f1c0_auto-caps-simdna` vs previous `pcrec_a15fb77b_auto-caps-simdna`: worst now (also the largest Δ): `s-082`, 13.0 ns, 1 B

### `floor` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | `plain` | same program | 1,325.8 | 1,324.0 | 1,327.2 | 1.1 | 1.000x | 1.000x | unchanged (within spread) | -0.10% (null control: program identical) | 77 | 17.2 | 100% |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | `plain` | same program | 1,327.1 | 1,326.4 | 1,337.6 | 4.2 | 1.001x | 1.001x | - | - | 77 | 17.2 | 100% |

- Δ detail: `pcrec_7388f1c0_auto-caps-simdna` vs previous `pcrec_a15fb77b_auto-caps-simdna`: worst now: `s-004`, 18.2 ns, 33 B; largest Δ: `s-081`, +1.2 ns (now 7.4 ns), 0 B

### `orig` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | `plain` | same program | 7,050,462.5 | 1.3448 | 7,047,494.9 | 7,057,357.8 | 4,130.9 | 1.000x | 1.000x | faster ×1.00 | -0.21% (null control: program identical) |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | `plain` | same program | 7,065,039.6 | 1.3475 | 7,062,353.0 | 7,068,371.2 | 2,146.4 | 1.002x | 1.002x | - | - |

#### `orig` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 3,781,298.9 | 3.6061 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_a15fb77b_auto-caps-simdna` | 3,781,012.1 | 3.6059 |
| `t-b-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 17,670.8 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_a15fb77b_auto-caps-simdna` | 17,681.2 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 17,702.3 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_a15fb77b_auto-caps-simdna` | 17,675.6 | 0.0169 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 3,216,105.3 | 3.0671 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_a15fb77b_auto-caps-simdna` | 3,230,027.0 | 3.0804 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 17,668.4 | 0.0168 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_a15fb77b_auto-caps-simdna` | 17,701.9 | 0.0169 |

- Δ detail: `pcrec_7388f1c0_auto-caps-simdna` vs previous `pcrec_a15fb77b_auto-caps-simdna`: worst now: `t-a-valid-addrs`, 3,781,298.9 ns, 1,048,576 B; largest Δ: `t-d-prose-sparse-addrs`, -13,921.7 ns (now 3,216,105.3 ns), 1,048,576 B

### `orig` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,125.9 | 73,125.1 | 73,224.7 | 39.3 | 1.000x | 1.000x | unchanged (within spread) | -0.00% vs bar 0.00% (IQR-only) → **improve (IQR only: band n=0 < 10)** |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,129.5 | 73,123.7 | 73,130.0 | 2.4 | 1.000x | 1.000x | - | - |

- Δ detail: `pcrec_7388f1c0_auto-caps-simdna` vs previous `pcrec_a15fb77b_auto-caps-simdna`: worst now: `s-057`, 19,064.1 ns, 10,252 B; largest Δ: `s-060`, +2.8 ns (now 19,037.9 ns), 10,240 B

### `orig` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | `plain` | same program | 3,711.6 | 3,710.7 | 3,721.4 | 4.0 | 1.000x | 1.000x | - | - | 77 | 48.2 | 17.2 | 100% |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | `plain` | same program | 3,714.6 | 3,710.5 | 3,719.4 | 3.1 | 1.001x | 1.001x | unchanged (within spread) | +0.08% (null control: program identical) | 77 | 48.2 | 17.2 | 100% |

- Δ detail: `pcrec_7388f1c0_auto-caps-simdna` vs previous `pcrec_a15fb77b_auto-caps-simdna`: worst now: `s-004`, 125.0 ns, 33 B; largest Δ: `s-047`, -0.6 ns (now 23.0 ns), 13 B

## Ranking -- NON-CAPTURING engines only, nocaps vs nocaps (per pattern x regime, SET grain: sum over the subject set; best median first)

_D119 bar in this view: |Δ%| > max(IQR%, null band), the `D119 bar` column (definition, strata and bands in the null-control section above). This view's own threshold population: 9 cross-pin cell(s): 0 improve, 0 regress, 3 within the bar, 6 null-control (program identical -- the band's own population); 3 of the verdicts are IQR-only (their stratum's band is not usable)._

### `factored` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | `plain` | same program | 7,053,687.8 | 1.3454 | 7,050,345.1 | 7,056,369.1 | 1,969.3 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | `plain` | same program | 7,057,522.5 | 1.3461 | 7,052,348.7 | 7,062,671.5 | 3,334.6 | 1.001x | 1.001x | unchanged (within spread) | +0.05% (null control: program identical) |

#### `factored` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 3,781,802.0 | 3.6066 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_a15fb77b_auto-nocaps-simdna` | 3,782,560.5 | 3.6073 |
| `t-b-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,716.3 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_a15fb77b_auto-nocaps-simdna` | 17,679.5 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,677.6 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_a15fb77b_auto-nocaps-simdna` | 17,693.1 | 0.0169 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 3,218,842.8 | 3.0697 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_a15fb77b_auto-nocaps-simdna` | 3,222,237.7 | 3.0730 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,717.4 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_a15fb77b_auto-nocaps-simdna` | 17,691.8 | 0.0169 |

- Δ detail: `pcrec_a15fb77b_auto-nocaps-simdna` vs previous `pcrec_7388f1c0_auto-nocaps-simdna`: worst now: `t-a-valid-addrs`, 3,782,560.5 ns, 1,048,576 B; largest Δ: `t-d-prose-sparse-addrs`, +3,394.9 ns (now 3,222,237.7 ns), 1,048,576 B

### `factored` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,121.8 | 73,120.3 | 76,188.0 | 1,225.5 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,126.8 | 73,121.5 | 73,134.8 | 4.7 | 1.000x | 1.000x | unchanged (within spread) | +0.01% vs bar 0.02% (IQR-only) → **within (IQR only: band n=0 < 10)** |

- Δ detail: `pcrec_a15fb77b_auto-nocaps-simdna` vs previous `pcrec_7388f1c0_auto-nocaps-simdna`: worst now: `s-057`, 19,062.9 ns, 10,252 B; largest Δ: `s-058`, -3.9 ns (now 7,459.8 ns), 4,011 B

### `factored` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | `plain` | same program | 3,710.7 | 3,706.8 | 3,714.6 | 2.9 | 1.000x | 1.000x | - | - | 77 | 48.2 | 17.2 | 100% |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | `plain` | same program | 3,715.3 | 3,714.1 | 3,719.5 | 2.0 | 1.001x | 1.001x | unchanged (within spread) | +0.12% (null control: program identical) | 77 | 48.3 | 17.2 | 100% |

- Δ detail: `pcrec_a15fb77b_auto-nocaps-simdna` vs previous `pcrec_7388f1c0_auto-nocaps-simdna`: worst now: `s-004`, 125.1 ns, 33 B; largest Δ: `s-072`, -1.1 ns (now 94.0 ns), 25 B

### `floor` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | `plain` | same program | 698,654.5 | 0.1333 | 698,527.1 | 699,677.3 | 434.4 | 1.000x | 1.000x | unchanged (within spread) | -0.07% (null control: program identical) |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | `plain` | same program | 699,134.5 | 0.1333 | 698,775.1 | 699,476.2 | 224.0 | 1.001x | 1.001x | - | - |

#### `floor` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_a15fb77b_auto-nocaps-simdna` | 614,647.8 | 0.5862 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 614,830.1 | 0.5863 |
| `t-b-no-at` | 1,048,576 | `pcrec_a15fb77b_auto-nocaps-simdna` | 17,683.2 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,672.4 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_a15fb77b_auto-nocaps-simdna` | 17,654.4 | 0.0168 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,693.9 | 0.0169 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_a15fb77b_auto-nocaps-simdna` | 31,027.5 | 0.0296 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 31,269.7 | 0.0298 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_a15fb77b_auto-nocaps-simdna` | 17,681.6 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,652.0 | 0.0168 |

- Δ detail: `pcrec_a15fb77b_auto-nocaps-simdna` vs previous `pcrec_7388f1c0_auto-nocaps-simdna`: worst now: `t-a-valid-addrs`, 614,647.8 ns, 1,048,576 B; largest Δ: `t-d-prose-sparse-addrs`, -242.3 ns (now 31,027.5 ns), 1,048,576 B

### `floor` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 759.0 | 758.7 | 759.9 | 0.4 | 1.000x | 1.000x | unchanged (within spread) | -0.02% vs bar 0.06% (IQR-only) → **within (IQR only: band n=0 < 10)** |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 759.2 | 758.6 | 759.2 | 0.3 | 1.000x | 1.000x | - | - |

- Δ detail: `pcrec_a15fb77b_auto-nocaps-simdna` vs previous `pcrec_7388f1c0_auto-nocaps-simdna`: worst now (also the largest Δ): `s-082`, 13.4 ns, 1 B

### `floor` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | `plain` | same program | 1,326.0 | 1,323.6 | 1,356.3 | 12.4 | 1.000x | 1.000x | - | - | 77 | 17.2 | 100% |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | `plain` | same program | 1,326.6 | 1,324.7 | 1,329.0 | 1.6 | 1.000x | 1.000x | unchanged (within spread) | +0.05% (null control: program identical) | 77 | 17.2 | 100% |

- Δ detail: `pcrec_a15fb77b_auto-nocaps-simdna` vs previous `pcrec_7388f1c0_auto-nocaps-simdna`: worst now: `s-004`, 18.2 ns, 33 B; largest Δ: `s-084`, -0.8 ns (now 9.2 ns), 10 B

### `orig` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | `plain` | same program | 7,057,469.6 | 1.3461 | 7,053,725.2 | 7,064,608.8 | 4,158.0 | 1.000x | 1.000x | unchanged (within spread) | -0.01% (null control: program identical) |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | `plain` | same program | 7,057,833.7 | 1.3462 | 7,053,069.6 | 7,088,174.9 | 12,795.5 | 1.000x | 1.000x | - | - |

#### `orig` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_a15fb77b_auto-nocaps-simdna` | 3,783,715.4 | 3.6084 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 3,785,158.1 | 3.6098 |
| `t-b-no-at` | 1,048,576 | `pcrec_a15fb77b_auto-nocaps-simdna` | 17,683.1 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,668.3 | 0.0168 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_a15fb77b_auto-nocaps-simdna` | 17,672.5 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,675.2 | 0.0169 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_a15fb77b_auto-nocaps-simdna` | 3,221,972.1 | 3.0727 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 3,220,264.1 | 3.0711 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_a15fb77b_auto-nocaps-simdna` | 17,687.7 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,696.1 | 0.0169 |

- Δ detail: `pcrec_a15fb77b_auto-nocaps-simdna` vs previous `pcrec_7388f1c0_auto-nocaps-simdna`: worst now: `t-a-valid-addrs`, 3,783,715.4 ns, 1,048,576 B; largest Δ: `t-d-prose-sparse-addrs`, +1,708.1 ns (now 3,221,972.1 ns), 1,048,576 B

### `orig` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,128.4 | 73,121.1 | 73,184.9 | 23.6 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,129.6 | 73,127.4 | 73,263.9 | 53.6 | 1.000x | 1.000x | unchanged (within spread) | +0.00% vs bar 0.03% (IQR-only) → **within (IQR only: band n=0 < 10)** |

- Δ detail: `pcrec_a15fb77b_auto-nocaps-simdna` vs previous `pcrec_7388f1c0_auto-nocaps-simdna`: worst now: `s-057`, 19,063.0 ns, 10,252 B; largest Δ: `s-060`, +2.7 ns (now 19,037.4 ns), 10,240 B

### `orig` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | `plain` | same program | 3,712.0 | 3,710.4 | 3,716.2 | 2.1 | 1.000x | 1.000x | - | - | 77 | 48.2 | 17.2 | 100% |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | `plain` | same program | 3,718.5 | 3,707.3 | 3,750.0 | 17.7 | 1.002x | 1.002x | unchanged (within spread) | +0.18% (null control: program identical) | 77 | 48.3 | 17.2 | 100% |

- Δ detail: `pcrec_a15fb77b_auto-nocaps-simdna` vs previous `pcrec_7388f1c0_auto-nocaps-simdna`: worst now: `s-004`, 124.8 ns, 33 B; largest Δ: `s-040`, +1.2 ns (now 8.6 ns), 15 B

## Ranking -- MIXED CLASSES, never compare across cells (per pattern x regime, SET grain: sum over the subject set; best median first)

_D119 bar in this view: |Δ%| > max(IQR%, null band), the `D119 bar` column (definition, strata and bands in the null-control section above). This view's own threshold population: 18 cross-pin cell(s): 1 improve, 0 regress, 5 within the bar, 12 null-control (program identical -- the band's own population); 6 of the verdicts are IQR-only (their stratum's band is not usable)._

### `factored` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | `plain` | same program | 7,021,205.1 | 1.3392 | 7,012,143.1 | 7,025,655.3 | 4,478.6 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | `plain` | same program | 7,022,515.1 | 1.3394 | 7,020,140.7 | 7,025,356.9 | 1,967.4 | 1.000x | 1.000x | unchanged (within spread) | +0.02% (null control: program identical) |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | `plain` | same program | 7,053,687.8 | 1.3454 | 7,050,345.1 | 7,056,369.1 | 1,969.3 | 1.005x | 1.005x | - | - |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | `plain` | same program | 7,057,522.5 | 1.3461 | 7,052,348.7 | 7,062,671.5 | 3,334.6 | 1.005x | 1.005x | unchanged (within spread) | +0.05% (null control: program identical) |

#### `factored` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_a15fb77b_auto-caps-simdna` | 3,804,411.7 | 3.6282 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 3,805,429.9 | 3.6291 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 3,781,802.0 | 3.6066 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_a15fb77b_auto-nocaps-simdna` | 3,782,560.5 | 3.6073 |
| `t-b-no-at` | 1,048,576 | `pcrec_a15fb77b_auto-caps-simdna` | 17,715.1 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 17,682.7 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,716.3 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_a15fb77b_auto-nocaps-simdna` | 17,679.5 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_a15fb77b_auto-caps-simdna` | 17,649.6 | 0.0168 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 17,660.3 | 0.0168 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,677.6 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_a15fb77b_auto-nocaps-simdna` | 17,693.1 | 0.0169 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_a15fb77b_auto-caps-simdna` | 3,163,933.4 | 3.0174 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 3,164,062.6 | 3.0175 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 3,218,842.8 | 3.0697 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_a15fb77b_auto-nocaps-simdna` | 3,222,237.7 | 3.0730 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_a15fb77b_auto-caps-simdna` | 17,675.1 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 17,660.4 | 0.0168 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,717.4 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_a15fb77b_auto-nocaps-simdna` | 17,691.8 | 0.0169 |

- Δ detail: `pcrec_7388f1c0_auto-caps-simdna` vs previous `pcrec_a15fb77b_auto-caps-simdna`: worst now (also the largest Δ): `t-a-valid-addrs`, 3,805,429.9 ns, 1,048,576 B
- Δ detail: `pcrec_a15fb77b_auto-nocaps-simdna` vs previous `pcrec_7388f1c0_auto-nocaps-simdna`: worst now: `t-a-valid-addrs`, 3,782,560.5 ns, 1,048,576 B; largest Δ: `t-d-prose-sparse-addrs`, +3,394.9 ns (now 3,222,237.7 ns), 1,048,576 B

### `factored` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,121.8 | 73,120.3 | 76,188.0 | 1,225.5 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,126.8 | 73,121.5 | 73,134.8 | 4.7 | 1.000x | 1.000x | unchanged (within spread) | +0.01% vs bar 0.02% (IQR-only) → **within (IQR only: band n=0 < 10)** |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,224.1 | 73,220.7 | 73,342.4 | 46.3 | 1.001x | 1.001x | unchanged (within spread) | -0.01% vs bar 0.01% (IQR-only) → **within (IQR only: band n=0 < 10)** |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,228.7 | 73,221.4 | 73,296.6 | 28.6 | 1.001x | 1.001x | - | - |

- Δ detail: `pcrec_a15fb77b_auto-nocaps-simdna` vs previous `pcrec_7388f1c0_auto-nocaps-simdna`: worst now: `s-057`, 19,062.9 ns, 10,252 B; largest Δ: `s-058`, -3.9 ns (now 7,459.8 ns), 4,011 B
- Δ detail: `pcrec_7388f1c0_auto-caps-simdna` vs previous `pcrec_a15fb77b_auto-caps-simdna`: worst now: `s-057`, 19,063.8 ns, 10,252 B; largest Δ: `s-063`, +2.0 ns (now 4,785.2 ns), 5,135 B

### `factored` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | `plain` | same program | 3,710.7 | 3,706.8 | 3,714.6 | 2.9 | 1.000x | 1.000x | - | - | 77 | 48.2 | 17.2 | 100% |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | `plain` | same program | 3,715.3 | 3,714.1 | 3,719.5 | 2.0 | 1.001x | 1.001x | unchanged (within spread) | +0.12% (null control: program identical) | 77 | 48.3 | 17.2 | 100% |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | `plain` | same program | 3,896.3 | 3,893.7 | 4,595.2 | 279.9 | 1.050x | 1.050x | - | - | 77 | 50.6 | 17.2 | 100% |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | `plain` | same program | 3,899.1 | 3,895.1 | 3,902.8 | 2.7 | 1.051x | 1.051x | unchanged (within spread) | +0.07% (null control: program identical) | 77 | 50.6 | 17.2 | 100% |

- Δ detail: `pcrec_a15fb77b_auto-nocaps-simdna` vs previous `pcrec_7388f1c0_auto-nocaps-simdna`: worst now: `s-004`, 125.1 ns, 33 B; largest Δ: `s-072`, -1.1 ns (now 94.0 ns), 25 B
- Δ detail: `pcrec_7388f1c0_auto-caps-simdna` vs previous `pcrec_a15fb77b_auto-caps-simdna`: worst now: `s-004`, 129.1 ns, 33 B; largest Δ: `s-001`, +0.8 ns (now 87.0 ns), 21 B

### `floor` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | `plain` | same program | 698,654.5 | 0.1333 | 698,527.1 | 699,677.3 | 434.4 | 1.000x | 1.000x | unchanged (within spread) | -0.07% (null control: program identical) |
| 2 | `pcrec_a15fb77b_auto-caps-simdna` | measured | `plain` | same program | 698,801.3 | 0.1333 | 698,661.3 | 698,840.6 | 65.0 | 1.000x | 1.000x | - | - |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | `plain` | same program | 698,916.4 | 0.1333 | 698,543.3 | 701,266.5 | 990.6 | 1.000x | 1.000x | unchanged (within spread) | +0.02% (null control: program identical) |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | `plain` | same program | 699,134.5 | 0.1333 | 698,775.1 | 699,476.2 | 224.0 | 1.001x | 1.001x | - | - |

#### `floor` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_a15fb77b_auto-nocaps-simdna` | 614,647.8 | 0.5862 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_a15fb77b_auto-caps-simdna` | 614,617.3 | 0.5861 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 614,572.7 | 0.5861 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 614,830.1 | 0.5863 |
| `t-b-no-at` | 1,048,576 | `pcrec_a15fb77b_auto-nocaps-simdna` | 17,683.2 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_a15fb77b_auto-caps-simdna` | 17,742.7 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 17,697.6 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,672.4 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_a15fb77b_auto-nocaps-simdna` | 17,654.4 | 0.0168 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_a15fb77b_auto-caps-simdna` | 17,717.6 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 17,700.8 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,693.9 | 0.0169 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_a15fb77b_auto-nocaps-simdna` | 31,027.5 | 0.0296 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_a15fb77b_auto-caps-simdna` | 31,025.1 | 0.0296 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 31,213.1 | 0.0298 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 31,269.7 | 0.0298 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_a15fb77b_auto-nocaps-simdna` | 17,681.6 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_a15fb77b_auto-caps-simdna` | 17,658.2 | 0.0168 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 17,671.5 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,652.0 | 0.0168 |

- Δ detail: `pcrec_a15fb77b_auto-nocaps-simdna` vs previous `pcrec_7388f1c0_auto-nocaps-simdna`: worst now: `t-a-valid-addrs`, 614,647.8 ns, 1,048,576 B; largest Δ: `t-d-prose-sparse-addrs`, -242.3 ns (now 31,027.5 ns), 1,048,576 B
- Δ detail: `pcrec_7388f1c0_auto-caps-simdna` vs previous `pcrec_a15fb77b_auto-caps-simdna`: worst now: `t-a-valid-addrs`, 614,572.7 ns, 1,048,576 B; largest Δ: `t-d-prose-sparse-addrs`, +188.0 ns (now 31,213.1 ns), 1,048,576 B

### `floor` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 758.7 | 758.6 | 759.3 | 0.2 | 1.000x | 1.000x | unchanged (within spread) | -0.05% vs bar 0.14% (IQR-only) → **within (IQR only: band n=0 < 10)** |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 759.0 | 758.7 | 759.9 | 0.4 | 1.000x | 1.000x | unchanged (within spread) | -0.02% vs bar 0.06% (IQR-only) → **within (IQR only: band n=0 < 10)** |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 759.1 | 758.7 | 760.1 | 0.6 | 1.001x | 1.001x | - | - |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 759.2 | 758.6 | 759.2 | 0.3 | 1.001x | 1.001x | - | - |

- Δ detail: `pcrec_7388f1c0_auto-caps-simdna` vs previous `pcrec_a15fb77b_auto-caps-simdna`: worst now (also the largest Δ): `s-082`, 13.0 ns, 1 B
- Δ detail: `pcrec_a15fb77b_auto-nocaps-simdna` vs previous `pcrec_7388f1c0_auto-nocaps-simdna`: worst now (also the largest Δ): `s-082`, 13.4 ns, 1 B

### `floor` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | `plain` | same program | 1,325.8 | 1,324.0 | 1,327.2 | 1.1 | 1.000x | 1.000x | unchanged (within spread) | -0.10% (null control: program identical) | 77 | 17.2 | 100% |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | `plain` | same program | 1,326.0 | 1,323.6 | 1,356.3 | 12.4 | 1.000x | 1.000x | - | - | 77 | 17.2 | 100% |
| 3 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | `plain` | same program | 1,326.6 | 1,324.7 | 1,329.0 | 1.6 | 1.001x | 1.001x | unchanged (within spread) | +0.05% (null control: program identical) | 77 | 17.2 | 100% |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | `plain` | same program | 1,327.1 | 1,326.4 | 1,337.6 | 4.2 | 1.001x | 1.001x | - | - | 77 | 17.2 | 100% |

- Δ detail: `pcrec_7388f1c0_auto-caps-simdna` vs previous `pcrec_a15fb77b_auto-caps-simdna`: worst now: `s-004`, 18.2 ns, 33 B; largest Δ: `s-081`, +1.2 ns (now 7.4 ns), 0 B
- Δ detail: `pcrec_a15fb77b_auto-nocaps-simdna` vs previous `pcrec_7388f1c0_auto-nocaps-simdna`: worst now: `s-004`, 18.2 ns, 33 B; largest Δ: `s-084`, -0.8 ns (now 9.2 ns), 10 B

### `orig` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | `plain` | same program | 7,050,462.5 | 1.3448 | 7,047,494.9 | 7,057,357.8 | 4,130.9 | 1.000x | 1.000x | faster ×1.00 | -0.21% (null control: program identical) |
| 2 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | `plain` | same program | 7,057,469.6 | 1.3461 | 7,053,725.2 | 7,064,608.8 | 4,158.0 | 1.001x | 1.001x | unchanged (within spread) | -0.01% (null control: program identical) |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | `plain` | same program | 7,057,833.7 | 1.3462 | 7,053,069.6 | 7,088,174.9 | 12,795.5 | 1.001x | 1.001x | - | - |
| 4 | `pcrec_a15fb77b_auto-caps-simdna` | measured | `plain` | same program | 7,065,039.6 | 1.3475 | 7,062,353.0 | 7,068,371.2 | 2,146.4 | 1.002x | 1.002x | - | - |

#### `orig` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 3,781,298.9 | 3.6061 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_a15fb77b_auto-nocaps-simdna` | 3,783,715.4 | 3.6084 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 3,785,158.1 | 3.6098 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_a15fb77b_auto-caps-simdna` | 3,781,012.1 | 3.6059 |
| `t-b-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 17,670.8 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_a15fb77b_auto-nocaps-simdna` | 17,683.1 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,668.3 | 0.0168 |
| `t-b-no-at` | 1,048,576 | `pcrec_a15fb77b_auto-caps-simdna` | 17,681.2 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 17,702.3 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_a15fb77b_auto-nocaps-simdna` | 17,672.5 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,675.2 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_a15fb77b_auto-caps-simdna` | 17,675.6 | 0.0169 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 3,216,105.3 | 3.0671 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_a15fb77b_auto-nocaps-simdna` | 3,221,972.1 | 3.0727 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 3,220,264.1 | 3.0711 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_a15fb77b_auto-caps-simdna` | 3,230,027.0 | 3.0804 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 17,668.4 | 0.0168 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_a15fb77b_auto-nocaps-simdna` | 17,687.7 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,696.1 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_a15fb77b_auto-caps-simdna` | 17,701.9 | 0.0169 |

- Δ detail: `pcrec_7388f1c0_auto-caps-simdna` vs previous `pcrec_a15fb77b_auto-caps-simdna`: worst now: `t-a-valid-addrs`, 3,781,298.9 ns, 1,048,576 B; largest Δ: `t-d-prose-sparse-addrs`, -13,921.7 ns (now 3,216,105.3 ns), 1,048,576 B
- Δ detail: `pcrec_a15fb77b_auto-nocaps-simdna` vs previous `pcrec_7388f1c0_auto-nocaps-simdna`: worst now: `t-a-valid-addrs`, 3,783,715.4 ns, 1,048,576 B; largest Δ: `t-d-prose-sparse-addrs`, +1,708.1 ns (now 3,221,972.1 ns), 1,048,576 B

### `orig` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,125.9 | 73,125.1 | 73,224.7 | 39.3 | 1.000x | 1.000x | unchanged (within spread) | -0.00% vs bar 0.00% (IQR-only) → **improve (IQR only: band n=0 < 10)** |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,128.4 | 73,121.1 | 73,184.9 | 23.6 | 1.000x | 1.000x | - | - |
| 3 | `pcrec_a15fb77b_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,129.5 | 73,123.7 | 73,130.0 | 2.4 | 1.000x | 1.000x | - | - |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,129.6 | 73,127.4 | 73,263.9 | 53.6 | 1.000x | 1.000x | unchanged (within spread) | +0.00% vs bar 0.03% (IQR-only) → **within (IQR only: band n=0 < 10)** |

- Δ detail: `pcrec_7388f1c0_auto-caps-simdna` vs previous `pcrec_a15fb77b_auto-caps-simdna`: worst now: `s-057`, 19,064.1 ns, 10,252 B; largest Δ: `s-060`, +2.8 ns (now 19,037.9 ns), 10,240 B
- Δ detail: `pcrec_a15fb77b_auto-nocaps-simdna` vs previous `pcrec_7388f1c0_auto-nocaps-simdna`: worst now: `s-057`, 19,063.0 ns, 10,252 B; largest Δ: `s-060`, +2.7 ns (now 19,037.4 ns), 10,240 B

### `orig` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a15fb77b_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a15fb77b_auto-caps-simdna` | measured | `plain` | same program | 3,711.6 | 3,710.7 | 3,721.4 | 4.0 | 1.000x | 1.000x | - | - | 77 | 48.2 | 17.2 | 100% |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | `plain` | same program | 3,712.0 | 3,710.4 | 3,716.2 | 2.1 | 1.000x | 1.000x | - | - | 77 | 48.2 | 17.2 | 100% |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | `plain` | same program | 3,714.6 | 3,710.5 | 3,719.4 | 3.1 | 1.001x | 1.001x | unchanged (within spread) | +0.08% (null control: program identical) | 77 | 48.2 | 17.2 | 100% |
| 4 | `pcrec_a15fb77b_auto-nocaps-simdna` | measured | `plain` | same program | 3,718.5 | 3,707.3 | 3,750.0 | 17.7 | 1.002x | 1.002x | unchanged (within spread) | +0.18% (null control: program identical) | 77 | 48.3 | 17.2 | 100% |

- Δ detail: `pcrec_7388f1c0_auto-caps-simdna` vs previous `pcrec_a15fb77b_auto-caps-simdna`: worst now: `s-004`, 125.0 ns, 33 B; largest Δ: `s-047`, -0.6 ns (now 23.0 ns), 13 B
- Δ detail: `pcrec_a15fb77b_auto-nocaps-simdna` vs previous `pcrec_7388f1c0_auto-nocaps-simdna`: worst now: `s-004`, 124.8 ns, 33 B; largest Δ: `s-040`, +1.2 ns (now 8.6 ns), 15 B

## Standing cross-class query (inbox I-101; Frank's own anomaly check -- a QUERY, never a ranking; every hit below is a finding on pcrec's side by definition)

**9 hit(s)** -- each is a finding on pcrec's side by definition (I-101):

| pattern | regime | pcrec auto-nocaps testee | auto-nocaps ns/call | competitor testee | competitor ns/call | ratio (competitor / auto-nocaps) | clears IQR / null band |
|---|---|---|---|---|---|---|---|
| `factored` | `large-subject-throughput` | `pcrec_7388f1c0_auto-nocaps-simdna` | 7,053,687.8 | `pcrec_7388f1c0_auto-caps-simdna` | 7,022,515.1 | 0.996x | clears IQR only: gap 0.44%; IQR 0.04% (clears); band n/a (pcrec 7388f1c0 -> a15fb77b, large-subject-throughput / >=1us: n=3 < 10) |
| `factored` | `large-subject-throughput` | `pcrec_a15fb77b_auto-nocaps-simdna` | 7,057,522.5 | `pcrec_a15fb77b_auto-caps-simdna` | 7,021,205.1 | 0.995x | clears IQR only: gap 0.51%; IQR 0.04% (clears); band n/a (pcrec 7388f1c0 -> a15fb77b, large-subject-throughput / >=1us: n=3 < 10) |
| `floor` | `large-subject-throughput` | `pcrec_7388f1c0_auto-nocaps-simdna` | 699,134.5 | `pcrec_7388f1c0_auto-caps-simdna` | 698,916.4 | 1.000x | within IQR: gap 0.03%; IQR 0.05% (within); band n/a (pcrec 7388f1c0 -> a15fb77b, large-subject-throughput / >=1us: n=3 < 10) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 759.2 | `pcrec_7388f1c0_auto-caps-simdna` | 758.7 | 0.999x | within IQR: gap 0.06%; IQR 0.06% (within); band n/a (pcrec 7388f1c0 -> a15fb77b, match-compliance / 100ns-1us: n=0 < 10) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 1,326.0 | `pcrec_7388f1c0_auto-caps-simdna` | 1,325.8 | 1.000x | within IQR: gap 0.02%; IQR 0.18% (within); band n/a (pcrec 7388f1c0 -> a15fb77b, short-subject-search / >=1us: n=3 < 10) |
| `orig` | `large-subject-throughput` | `pcrec_7388f1c0_auto-nocaps-simdna` | 7,057,833.7 | `pcrec_7388f1c0_auto-caps-simdna` | 7,050,462.5 | 0.999x | within IQR: gap 0.10%; IQR 0.12% (within); band n/a (pcrec 7388f1c0 -> a15fb77b, large-subject-throughput / >=1us: n=3 < 10) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 73,128.4 | `pcrec_7388f1c0_auto-caps-simdna` | 73,125.9 | 1.000x | within IQR: gap 0.00%; IQR 0.03% (within); band n/a (pcrec 7388f1c0 -> a15fb77b, match-compliance / >=1us: n=0 < 10) |
| `orig` | `match-compliance` | `pcrec_a15fb77b_auto-nocaps-simdna` | 73,129.6 | `pcrec_a15fb77b_auto-caps-simdna` | 73,129.5 | 1.000x | within IQR: gap 0.00%; IQR 0.01% (within); band n/a (pcrec 7388f1c0 -> a15fb77b, match-compliance / >=1us: n=0 < 10) |
| `orig` | `short-subject-search` | `pcrec_a15fb77b_auto-nocaps-simdna` | 3,718.5 | `pcrec_a15fb77b_auto-caps-simdna` | 3,711.6 | 0.998x | within IQR: gap 0.19%; IQR 0.92% (within); band n/a (pcrec 7388f1c0 -> a15fb77b, short-subject-search / >=1us: n=3 < 10) |

## Compile cost (by execution-model class; never pooled across classes)

### `compiled-aot`

- `pcrec_7388f1c0_auto-caps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_7388f1c0_auto-caps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_7388f1c0_auto-caps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_7388f1c0_auto-caps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_7388f1c0_auto-caps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_7388f1c0_auto-caps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_7388f1c0_auto-nocaps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_7388f1c0_auto-nocaps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_7388f1c0_auto-nocaps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_7388f1c0_auto-nocaps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_7388f1c0_auto-nocaps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_7388f1c0_auto-nocaps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a15fb77b_auto-caps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a15fb77b_auto-caps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a15fb77b_auto-caps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a15fb77b_auto-caps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a15fb77b_auto-caps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a15fb77b_auto-caps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a15fb77b_auto-nocaps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a15fb77b_auto-nocaps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a15fb77b_auto-nocaps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a15fb77b_auto-nocaps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a15fb77b_auto-nocaps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a15fb77b_auto-nocaps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
    - sel = pcrec's `RX_ENGINE_SEL`; `DFA fallback tripped` = sel not in (selected, forced), and NOTHING else -- since pcrec 263b013 ([LIM-1] / [OPT-4.1]) every fallback has its own token (`overflowed-dfa`, `overflowed-prefilter`, `collapsed-prefilter`, `declined-nullable`, `size-cap-retry`), the size-cap rescue included; at pcrec 96e44c2 that rescue stamped `sel=selected` and only its `lang=count-collapsed (size cap retry, ...)` clause says so.
    - edge = pcrec's `RX_DFA_SCAN_EDGE` ([OPT-5] STEP 1, abi 13+), how a DFA scan tests a SCAN EDGE's byte class: `range` = a contiguous run (subtract-and-compare against two immediates); `bitmap` = a non-contiguous class (a 256-byte membership read); `mixed` = one artifact whose machines took both forms; `none` = no collapsible run (an attempt/empty scan, or -fno-scan-edge).
    - edges = pcrec's `scan_edges` ([B32]): how many [OPT-5] SCAN EDGES this artifact's SEARCH-side machines carry (`rx_search`/`rx_prefilter`), the per-scan-iteration compare-count covariate `edge`'s single shape token cannot separate (I-33: the cost is one compare per edge per iteration); the `(match: M)` parenthetical, when carried, is the SAME count on the anchored `rx_match` machine, kept apart because the measured [OPT-EDGE] regression is search-band only. `0` is a real, recorded value.
    - start = pcrec's `RX_DFA_START` ([OPT-5] STEP 2, abi 16+), how the SEARCH entry recovers the match START: `pinned` = the forward machine's start state accepts unconditionally, so the match provably begins at `search_from` and THE ARTIFACT CARRIES NO REVERSE MACHINE at all (no reverse tables, accessor block or scan loop); `reverse-pass` = it carries one and walks it backwards from the match end. The two forms are ANSWER-IDENTICAL by contract -- `caps[0][0]`'s absolute offsets and the zero-length-match convention hold under both -- so this explains a row's SIZE and pass count, never its answer.
    - folds = pcrec's `RX_DFA_UNIFORM_FOLDS` ([CC-DIFF] STEP 1, abi 17+): how many of this artifact's DFA tables (two per machine it contains -- forward always, reverse unless `start=pinned`, anchored under `match=unwrapped`; so 0..6) had ALL-EQUAL cells and were NOT EMITTED, the accessor returning the constant. `table=` keeps naming the encoding that was SELECTED, so `premultiplied` beside `folds=4` is an artifact carrying NO transition table at all -- a SIZE fact, never an answer one. `0` is a real, recorded value.

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | emit bytes | code bytes | jitter | outcomes | emit-c ns | gcc ns | load ns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `pcrec_7388f1c0_auto-caps-simdna` | 192,593,532.0 | 183,489,073.0 | 204,394,658.0 | 7,016,613.6 | 5 | 49,472 | 85,071 | 16,377 | 0.036 | compiled=5 | 9,532,702.0 | 181,987,885.0 | 102,100.0 |
| `factored` | `whole-subject` | `pcrec_7388f1c0_auto-caps-simdna` | 182,787,890.0 | 166,014,228.0 | 189,889,510.0 | 8,638,702.5 | 5 | 37,040 | 42,326 | 16,649 | 0.047 (max is trial 1) | compiled=5 | 9,712,263.0 | 166,823,544.0 | 199,680.0 |
| `factored` | `plain` | `pcrec_7388f1c0_auto-nocaps-simdna` | 180,450,705.0 | 179,800,632.0 | 188,754,653.0 | 3,615,905.0 | 5 | 49,472 | 84,868 | 16,170 | 0.020 | compiled=5 | 9,441,531.0 | 170,746,923.0 | 177,002.0 |
| `factored` | `whole-subject` | `pcrec_7388f1c0_auto-nocaps-simdna` | 169,047,345.0 | 168,843,344.0 | 182,548,950.0 | 5,696,967.6 | 5 | 37,040 | 42,143 | 16,462 | 0.034 | compiled=5 | 9,502,823.0 | 159,449,401.0 | 106,481.0 |
| `factored` | `plain` | `pcrec_a15fb77b_auto-caps-simdna` | 192,388,932.0 | 182,509,297.0 | 200,442,183.0 | 6,907,514.1 | 5 | 49,472 | 85,071 | 16,377 | 0.036 | compiled=5 | 9,328,851.0 | 182,646,655.0 | 187,451.0 |
| `factored` | `whole-subject` | `pcrec_a15fb77b_auto-caps-simdna` | 207,644,984.0 | 195,182,265.0 | 214,034,860.0 | 6,928,437.9 | 5 | 53,712 | 97,282 | 18,293 | 0.033 | compiled=5 | 11,712,935.0 | 191,551,714.0 | 189,911.0 |
| `factored` | `plain` | `pcrec_a15fb77b_auto-nocaps-simdna` | 178,873,944.0 | 174,826,913.0 | 195,096,565.0 | 7,744,816.7 | 5 | 49,472 | 84,868 | 16,170 | 0.043 | compiled=5 | 9,459,712.0 | 169,327,823.0 | 97,770.0 |
| `factored` | `whole-subject` | `pcrec_a15fb77b_auto-nocaps-simdna` | 197,167,296.0 | 181,501,079.0 | 198,483,283.0 | 6,432,053.1 | 5 | 53,712 | 97,079 | 18,086 | 0.033 | compiled=5 | 11,491,653.0 | 179,352,667.0 | 95,560.0 |
| `floor` | `plain` | `pcrec_7388f1c0_auto-caps-simdna` | 160,470,489.0 | 159,945,835.0 | 169,664,277.0 | 4,537,888.2 | 5 | 28,912 | 20,571 | 15,574 | 0.028 | compiled=5 | 2,199,062.0 | 158,055,065.0 | 102,460.0 |
| `floor` | `whole-subject` | `pcrec_7388f1c0_auto-caps-simdna` | 161,299,053.0 | 151,975,422.0 | 172,459,064.0 | 7,199,025.6 | 5 | 28,808 | 19,474 | 15,916 | 0.045 | compiled=5 | 2,090,122.0 | 159,030,470.0 | 99,211.0 |
| `floor` | `plain` | `pcrec_7388f1c0_auto-nocaps-simdna` | 166,150,810.0 | 163,340,653.0 | 177,970,752.0 | 5,321,879.2 | 5 | 28,912 | 20,571 | 15,574 | 0.032 | compiled=5 | 2,175,522.0 | 163,778,776.0 | 201,121.0 |
| `floor` | `whole-subject` | `pcrec_7388f1c0_auto-nocaps-simdna` | 166,244,018.0 | 156,787,437.0 | 173,726,131.0 | 6,265,876.9 | 5 | 28,808 | 19,474 | 15,916 | 0.038 | compiled=5 | 1,914,900.0 | 163,949,396.0 | 99,631.0 |
| `floor` | `plain` | `pcrec_a15fb77b_auto-caps-simdna` | 163,220,121.0 | 158,983,618.0 | 169,472,102.0 | 4,072,027.2 | 5 | 28,912 | 20,571 | 15,574 | 0.025 | compiled=5 | 2,156,290.0 | 158,601,784.0 | 111,821.0 |
| `floor` | `whole-subject` | `pcrec_a15fb77b_auto-caps-simdna` | 183,307,509.0 | 174,340,722.0 | 184,584,496.0 | 3,749,259.9 | 5 | 29,056 | 23,535 | 18,212 | 0.020 | compiled=5 | 2,256,773.0 | 180,949,908.0 | 102,771.0 |
| `floor` | `plain` | `pcrec_a15fb77b_auto-nocaps-simdna` | 165,827,825.0 | 152,482,252.0 | 173,141,094.0 | 7,197,610.1 | 5 | 28,912 | 20,571 | 15,574 | 0.043 | compiled=5 | 2,187,632.0 | 163,598,593.0 | 186,921.0 |
| `floor` | `whole-subject` | `pcrec_a15fb77b_auto-nocaps-simdna` | 184,796,616.0 | 169,787,225.0 | 190,060,758.0 | 7,748,107.9 | 5 | 29,056 | 23,535 | 18,212 | 0.042 | compiled=5 | 2,271,294.0 | 181,839,772.0 | 104,691.0 |
| `orig` | `plain` | `pcrec_7388f1c0_auto-caps-simdna` | 169,077,386.0 | 166,480,440.0 | 176,582,287.0 | 4,385,119.2 | 5 | 49,440 | 84,644 | 16,117 | 0.026 | compiled=5 | 8,935,539.0 | 160,059,615.0 | 109,510.0 |
| `orig` | `whole-subject` | `pcrec_7388f1c0_auto-caps-simdna` | 175,055,258.0 | 170,624,474.0 | 185,141,853.0 | 4,809,764.9 | 5 | 32,904 | 41,919 | 16,409 | 0.027 | compiled=5 | 9,040,949.0 | 165,906,589.0 | 107,721.0 |
| `orig` | `plain` | `pcrec_7388f1c0_auto-nocaps-simdna` | 186,100,259.0 | 173,570,820.0 | 191,970,331.0 | 7,062,007.0 | 5 | 49,440 | 84,644 | 16,117 | 0.038 (max is trial 1) | compiled=5 | 10,900,751.0 | 169,805,449.0 | 186,381.0 |
| `orig` | `whole-subject` | `pcrec_7388f1c0_auto-nocaps-simdna` | 167,064,416.0 | 166,488,471.0 | 179,924,296.0 | 5,352,034.0 | 5 | 32,904 | 41,919 | 16,409 | 0.032 (max is trial 1) | compiled=5 | 8,693,699.0 | 158,271,746.0 | 193,001.0 |
| `orig` | `plain` | `pcrec_a15fb77b_auto-caps-simdna` | 180,449,624.0 | 177,287,525.0 | 190,509,198.0 | 4,849,704.8 | 5 | 49,440 | 84,644 | 16,117 | 0.027 | compiled=5 | 8,773,917.0 | 171,207,253.0 | 194,941.0 |
| `orig` | `whole-subject` | `pcrec_a15fb77b_auto-caps-simdna` | 200,726,985.0 | 196,475,203.0 | 209,402,494.0 | 4,224,669.2 | 5 | 53,672 | 96,855 | 18,033 | 0.021 | compiled=5 | 10,745,219.0 | 187,832,585.0 | 110,771.0 |
| `orig` | `plain` | `pcrec_a15fb77b_auto-nocaps-simdna` | 187,850,015.0 | 177,651,958.0 | 189,324,242.0 | 5,336,298.0 | 5 | 49,440 | 84,644 | 16,117 | 0.028 | compiled=5 | 8,931,928.0 | 178,765,315.0 | 101,621.0 |
| `orig` | `whole-subject` | `pcrec_a15fb77b_auto-nocaps-simdna` | 200,242,521.0 | 191,740,147.0 | 203,547,712.0 | 5,172,302.7 | 5 | 53,672 | 96,855 | 18,033 | 0.026 | compiled=5 | 10,803,499.0 | 181,284,258.0 | 203,682.0 |

