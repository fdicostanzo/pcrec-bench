# pcrec-bench report

reporter: v25 (2026-09-26)

## Query

- filters: subbench=email-specimen, version=0.2, machine=budu-ryzen1600, since=2026-10-11T00:00:00Z, testee=pcrec_7388f1c0_auto-caps-simdna, testee=pcrec_7388f1c0_auto-nocaps-simdna, testee=pcrec_b8337c33_auto-caps-simdna, testee=pcrec_b8337c33_auto-nocaps-simdna
- record source: store/index.tsv (4 record(s) matching this query)
- records included: 4
- worst other-core busy: 23.68% (`pcrec_7388f1c0_auto-caps-simdna` / `floor` / `large-subject-throughput`)
    - `email-specimen@0.2__pcrec_7388f1c0_auto-caps-simdna__budu-ryzen1600__20261011T054009Z` (store/records/email-specimen@0.2/pcrec_7388f1c0_auto-caps-simdna/email-specimen@0.2__pcrec_7388f1c0_auto-caps-simdna__budu-ryzen1600__20261011T054009Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials); after: occ 20.85%
    - `email-specimen@0.2__pcrec_7388f1c0_auto-nocaps-simdna__budu-ryzen1600__20261011T055746Z` (store/records/email-specimen@0.2/pcrec_7388f1c0_auto-nocaps-simdna/email-specimen@0.2__pcrec_7388f1c0_auto-nocaps-simdna__budu-ryzen1600__20261011T055746Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_b8337c33_auto-caps-simdna__budu-ryzen1600__20261011T054614Z` (store/records/email-specimen@0.2/pcrec_b8337c33_auto-caps-simdna/email-specimen@0.2__pcrec_b8337c33_auto-caps-simdna__budu-ryzen1600__20261011T054614Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_b8337c33_auto-nocaps-simdna__budu-ryzen1600__20261011T055209Z` (store/records/email-specimen@0.2/pcrec_b8337c33_auto-nocaps-simdna/email-specimen@0.2__pcrec_b8337c33_auto-nocaps-simdna__budu-ryzen1600__20261011T055209Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
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
- identity: the records' own `engine_metadata.program_sha256` ([B88], schema v1.7) where BOTH compile rows of a cell carry it; otherwise OUR OWN census (`tools/program_identity.py`: both pins re-emitted with the pinned binaries under each config's recorded flags, `.c` + `.h` compared after dropping ONLY the generated-by line, the `.abi` integer and one-sided `#define` stamps). Which records carry the field, per side: `pcrec 7388f1c0 -> b8337c33`: the BEFORE (`7388f1c0`) records carry `program_sha256` (12 of 12 compiled cell(s)), the AFTER (`b8337c33`) records carry `program_sha256` (12 of 12 compiled cell(s)).

### `pcrec 7388f1c0 -> b8337c33` (email-specimen@0.2)

- identity from the records ([B88], schema v1.7): 18 cell(s) read `engine_metadata.program_sha256` on BOTH compile rows, 0 fell back to the census; no census for this pair
- cells: 18 cross-pin set cell(s) measured on both sides; 14 program-identical (the null population)

| regime | baseline scale | n null cells | min Δ% | median Δ% | max Δ% | band (±) | status |
|---|---|---|---|---|---|---|---|
| `large-subject-throughput` | `>=1us` | 4 | -0.09% | +0.01% | +0.09% | n/a | insufficient (n=4 < 10) |
| `large-subject-throughput` | `100ns-1us` | 0 | - | - | - | n/a | empty (n=0) |
| `large-subject-throughput` | `<100ns` | 0 | - | - | - | n/a | empty (n=0) |
| `match-compliance` | `>=1us` | 4 | -0.00% | +0.02% | +0.05% | n/a | insufficient (n=4 < 10) |
| `match-compliance` | `100ns-1us` | 2 | +0.04% | +0.06% | +0.08% | n/a | insufficient (n=2 < 10) |
| `match-compliance` | `<100ns` | 0 | - | - | - | n/a | empty (n=0) |
| `short-subject-search` | `>=1us` | 4 | -0.00% | +0.04% | +0.21% | n/a | insufficient (n=4 < 10) |
| `short-subject-search` | `100ns-1us` | 0 | - | - | - | n/a | empty (n=0) |
| `short-subject-search` | `<100ns` | 0 | - | - | - | n/a | empty (n=0) |

_[B82] (inbox I-99, Frank's ruling -- a D119 addendum): this report's roster spans BOTH capture classes, so the two views below are the HEADLINE -- "If an engine is run non-capturing on a pattern, then we can't compare that to a capturing engine run -- they are almost completely different things with different objectives." No cell in either view compares across classes; the third, MIXED table further down restates today's single-roster ranking and is never the headline._

## Ranking -- CAPTURING engines only, caps vs caps (per pattern x regime, SET grain: sum over the subject set; best median first)

_D119 bar in this view: |Δ%| > max(IQR%, null band), the `D119 bar` column (definition, strata and bands in the null-control section above). This view's own threshold population: 9 cross-pin cell(s): 2 improve, 0 regress, 0 within the bar, 7 null-control (program identical -- the band's own population); 2 of the verdicts are IQR-only (their stratum's band is not usable)._

### `factored` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | `plain` | same program | 7,020,269.0 | 1.3390 | 7,015,479.6 | 7,028,927.5 | 4,629.1 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 7,023,275.0 | 1.3396 | 7,021,446.1 | 7,026,596.2 | 1,860.0 | 1.000x | 1.000x | unchanged (within spread) | +0.04% (null control: program identical) |

#### `factored` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 3,805,462.8 | 3.6292 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 3,807,136.4 | 3.6308 |
| `t-b-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 17,678.9 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 17,677.9 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 17,689.5 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 17,703.1 | 0.0169 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 3,162,541.5 | 3.0160 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 3,162,106.4 | 3.0156 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 17,689.1 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 17,683.5 | 0.0169 |

- Δ detail: `pcrec_b8337c33_auto-caps-simdna` vs previous `pcrec_7388f1c0_auto-caps-simdna`: worst now (also the largest Δ): `t-a-valid-addrs`, 3,807,136.4 ns, 1,048,576 B

### `factored` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,228.5 | 73,223.7 | 73,239.2 | 5.4 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,257.1 | 73,247.6 | 73,260.8 | 4.7 | 1.000x | 1.000x | slower ×1.00 | +0.04% (null control: program identical) |

- Δ detail: `pcrec_b8337c33_auto-caps-simdna` vs previous `pcrec_7388f1c0_auto-caps-simdna`: worst now: `s-057`, 19,071.1 ns, 10,252 B; largest Δ: `s-060`, +8.9 ns (now 19,045.2 ns), 10,240 B

### `factored` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | `plain` | same program | 3,896.4 | 3,895.4 | 3,900.9 | 2.5 | 1.000x | 1.000x | - | - | 77 | 50.6 | 17.2 | 100% |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 3,899.7 | 3,897.3 | 3,902.3 | 1.7 | 1.001x | 1.001x | unchanged (within spread) | +0.09% (null control: program identical) | 77 | 50.6 | 12.8 | 100% |

- Δ detail: `pcrec_b8337c33_auto-caps-simdna` vs previous `pcrec_7388f1c0_auto-caps-simdna`: worst now: `s-004`, 129.0 ns, 33 B; largest Δ: `s-081`, +1.1 ns (now 5.0 ns), 0 B

### `floor` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 659,860.4 | 0.1259 | 659,768.9 | 660,219.0 | 191.5 | 1.000x | 1.000x | faster ×1.06 | -5.59% vs bar 0.30% (IQR-only) → **improve (IQR only: band n=4 < 10)** |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | `plain` | same program | 698,908.1 | 0.1333 | 698,528.6 | 713,705.5 | 5,822.2 | 1.059x | 1.059x | - | - |

#### `floor` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 576,391.5 | 0.5497 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 614,889.3 | 0.5864 |
| `t-b-no-at` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 17,728.5 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 17,669.3 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 17,710.2 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 17,713.4 | 0.0169 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 30,309.3 | 0.0289 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 30,963.8 | 0.0295 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 17,700.6 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 17,689.1 | 0.0169 |

- Δ detail: `pcrec_b8337c33_auto-caps-simdna` vs previous `pcrec_7388f1c0_auto-caps-simdna`: worst now (also the largest Δ): `t-a-valid-addrs`, 576,391.5 ns, 1,048,576 B

### `floor` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 759.2 | 758.5 | 761.4 | 1.1 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 759.8 | 759.0 | 762.1 | 1.3 | 1.001x | 1.001x | unchanged (within spread) | +0.08% (null control: program identical) |

- Δ detail: `pcrec_b8337c33_auto-caps-simdna` vs previous `pcrec_7388f1c0_auto-caps-simdna`: worst now: `s-082`, 13.1 ns, 1 B; largest Δ: `s-081`, +0.1 ns (now 10.2 ns), 0 B

### `floor` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 986.1 | 984.9 | 988.0 | 1.1 | 1.000x | 1.000x | faster ×1.34 | -25.61% vs bar 0.11% (IQR-only) → **improve (IQR only: band n=4 < 10)** | 77 | 12.8 | 100% |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | `plain` | same program | 1,325.6 | 1,324.6 | 1,328.4 | 1.3 | 1.344x | 1.344x | - | - | 77 | 17.2 | 100% |

- Δ detail: `pcrec_b8337c33_auto-caps-simdna` vs previous `pcrec_7388f1c0_auto-caps-simdna`: worst now: `s-004`, 13.5 ns, 33 B; largest Δ: `s-042`, -4.9 ns (now 12.6 ns), 5 B

### `orig` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | `plain` | same program | 7,053,695.9 | 1.3454 | 7,046,971.8 | 7,061,389.3 | 4,682.7 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 7,059,721.9 | 1.3465 | 7,053,019.5 | 7,079,510.2 | 9,117.6 | 1.001x | 1.001x | unchanged (within spread) | +0.09% (null control: program identical) |

#### `orig` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 3,781,204.7 | 3.6060 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 3,782,965.9 | 3.6077 |
| `t-b-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 17,685.7 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 17,715.8 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 17,682.7 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 17,680.9 | 0.0169 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 3,218,037.1 | 3.0690 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 3,224,086.7 | 3.0747 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 17,689.6 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 17,704.7 | 0.0169 |

- Δ detail: `pcrec_b8337c33_auto-caps-simdna` vs previous `pcrec_7388f1c0_auto-caps-simdna`: worst now: `t-a-valid-addrs`, 3,782,965.9 ns, 1,048,576 B; largest Δ: `t-d-prose-sparse-addrs`, +6,049.6 ns (now 3,224,086.7 ns), 1,048,576 B

### `orig` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,126.2 | 73,125.1 | 73,161.0 | 13.7 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,165.0 | 73,135.6 | 73,256.5 | 42.5 | 1.001x | 1.001x | unchanged (within spread) | +0.05% (null control: program identical) |

- Δ detail: `pcrec_b8337c33_auto-caps-simdna` vs previous `pcrec_7388f1c0_auto-caps-simdna`: worst now (also the largest Δ): `s-057`, 19,067.5 ns, 10,252 B

### `orig` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | `plain` | same program | 3,710.3 | 3,707.6 | 3,723.2 | 5.6 | 1.000x | 1.000x | - | - | 77 | 48.2 | 17.2 | 100% |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 3,718.2 | 3,714.5 | 3,718.9 | 1.6 | 1.002x | 1.002x | unchanged (within spread) | +0.21% (null control: program identical) | 77 | 48.3 | 12.8 | 100% |

- Δ detail: `pcrec_b8337c33_auto-caps-simdna` vs previous `pcrec_7388f1c0_auto-caps-simdna`: worst now: `s-004`, 125.1 ns, 33 B; largest Δ: `s-040`, +1.1 ns (now 8.7 ns), 15 B

## Ranking -- NON-CAPTURING engines only, nocaps vs nocaps (per pattern x regime, SET grain: sum over the subject set; best median first)

_D119 bar in this view: |Δ%| > max(IQR%, null band), the `D119 bar` column (definition, strata and bands in the null-control section above). This view's own threshold population: 9 cross-pin cell(s): 2 improve, 0 regress, 0 within the bar, 7 null-control (program identical -- the band's own population); 2 of the verdicts are IQR-only (their stratum's band is not usable)._

### `factored` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | `plain` | same program | 7,058,665.0 | 1.3463 | 7,054,442.3 | 7,060,286.6 | 2,387.7 | 1.000x | 1.000x | unchanged (within spread) | -0.09% (null control: program identical) |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | `plain` | same program | 7,064,912.5 | 1.3475 | 7,055,808.0 | 7,067,316.3 | 4,576.8 | 1.001x | 1.001x | - | - |

#### `factored` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_b8337c33_auto-nocaps-simdna` | 3,783,423.4 | 3.6082 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 3,784,653.7 | 3.6093 |
| `t-b-no-at` | 1,048,576 | `pcrec_b8337c33_auto-nocaps-simdna` | 17,720.0 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,745.9 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_b8337c33_auto-nocaps-simdna` | 17,722.6 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,698.6 | 0.0169 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_b8337c33_auto-nocaps-simdna` | 3,219,462.6 | 3.0703 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 3,221,767.3 | 3.0725 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_b8337c33_auto-nocaps-simdna` | 17,732.0 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,716.3 | 0.0169 |

- Δ detail: `pcrec_b8337c33_auto-nocaps-simdna` vs previous `pcrec_7388f1c0_auto-nocaps-simdna`: worst now: `t-a-valid-addrs`, 3,783,423.4 ns, 1,048,576 B; largest Δ: `t-d-prose-sparse-addrs`, -2,304.8 ns (now 3,219,462.6 ns), 1,048,576 B

### `factored` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,164.9 | 73,152.1 | 73,179.5 | 8.7 | 1.000x | 1.000x | unchanged (within spread) | -0.00% (null control: program identical) |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,167.5 | 73,162.4 | 73,249.8 | 33.9 | 1.000x | 1.000x | - | - |

- Δ detail: `pcrec_b8337c33_auto-nocaps-simdna` vs previous `pcrec_7388f1c0_auto-nocaps-simdna`: worst now: `s-057`, 19,072.8 ns, 10,252 B; largest Δ: `s-064`, -2.5 ns (now 7,646.3 ns), 4,110 B

### `factored` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | `plain` | same program | 3,714.1 | 3,710.3 | 3,722.9 | 5.2 | 1.000x | 1.000x | unchanged (within spread) | -0.00% (null control: program identical) | 77 | 48.2 | 12.9 | 100% |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | `plain` | same program | 3,714.2 | 3,713.0 | 3,717.5 | 1.7 | 1.000x | 1.000x | - | - | 77 | 48.2 | 17.2 | 100% |

- Δ detail: `pcrec_b8337c33_auto-nocaps-simdna` vs previous `pcrec_7388f1c0_auto-nocaps-simdna`: worst now: `s-004`, 124.9 ns, 33 B; largest Δ: `s-084`, +0.9 ns (now 8.7 ns), 10 B

### `floor` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | `plain` | same program | 660,358.3 | 0.1260 | 660,047.6 | 660,926.8 | 287.5 | 1.000x | 1.000x | faster ×1.06 | -5.56% vs bar 0.05% (IQR-only) → **improve (IQR only: band n=4 < 10)** |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | `plain` | same program | 699,272.2 | 0.1334 | 699,048.7 | 699,713.6 | 249.8 | 1.059x | 1.059x | - | - |

#### `floor` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_b8337c33_auto-nocaps-simdna` | 576,758.3 | 0.5500 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 614,985.7 | 0.5865 |
| `t-b-no-at` | 1,048,576 | `pcrec_b8337c33_auto-nocaps-simdna` | 17,713.3 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,737.2 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_b8337c33_auto-nocaps-simdna` | 17,681.5 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,700.9 | 0.0169 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_b8337c33_auto-nocaps-simdna` | 30,472.3 | 0.0291 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 31,117.9 | 0.0297 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_b8337c33_auto-nocaps-simdna` | 17,737.8 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,722.6 | 0.0169 |

- Δ detail: `pcrec_b8337c33_auto-nocaps-simdna` vs previous `pcrec_7388f1c0_auto-nocaps-simdna`: worst now (also the largest Δ): `t-a-valid-addrs`, 576,758.3 ns, 1,048,576 B

### `floor` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 759.4 | 759.1 | 762.2 | 1.1 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 759.7 | 759.4 | 760.6 | 0.4 | 1.000x | 1.000x | unchanged (within spread) | +0.04% (null control: program identical) |

- Δ detail: `pcrec_b8337c33_auto-nocaps-simdna` vs previous `pcrec_7388f1c0_auto-nocaps-simdna`: worst now: `s-082`, 13.0 ns, 1 B; largest Δ: `s-083`, +0.1 ns (now 8.9 ns), 43 B

### `floor` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | `plain` | same program | 990.0 | 987.7 | 992.4 | 1.6 | 1.000x | 1.000x | faster ×1.34 | -25.21% vs bar 0.12% (IQR-only) → **improve (IQR only: band n=4 < 10)** | 77 | 12.9 | 100% |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | `plain` | same program | 1,323.7 | 1,321.9 | 1,325.0 | 1.1 | 1.337x | 1.337x | - | - | 77 | 17.2 | 100% |

- Δ detail: `pcrec_b8337c33_auto-nocaps-simdna` vs previous `pcrec_7388f1c0_auto-nocaps-simdna`: worst now: `s-004`, 13.4 ns, 33 B; largest Δ: `s-042`, -4.9 ns (now 12.6 ns), 5 B

### `orig` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | `plain` | same program | 7,059,574.8 | 1.3465 | 7,058,560.9 | 7,062,570.8 | 1,770.2 | 1.000x | 1.000x | unchanged (within spread) | -0.02% (null control: program identical) |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | `plain` | same program | 7,060,912.1 | 1.3468 | 7,057,952.3 | 7,070,624.0 | 4,611.7 | 1.000x | 1.000x | - | - |

#### `orig` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_b8337c33_auto-nocaps-simdna` | 3,784,037.5 | 3.6087 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 3,786,407.2 | 3.6110 |
| `t-b-no-at` | 1,048,576 | `pcrec_b8337c33_auto-nocaps-simdna` | 17,793.3 | 0.0170 |
| `t-b-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,780.8 | 0.0170 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_b8337c33_auto-nocaps-simdna` | 17,709.5 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,746.6 | 0.0169 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_b8337c33_auto-nocaps-simdna` | 3,223,524.5 | 3.0742 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 3,222,623.3 | 3.0733 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_b8337c33_auto-nocaps-simdna` | 17,693.9 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,739.4 | 0.0169 |

- Δ detail: `pcrec_b8337c33_auto-nocaps-simdna` vs previous `pcrec_7388f1c0_auto-nocaps-simdna`: worst now (also the largest Δ): `t-a-valid-addrs`, 3,784,037.5 ns, 1,048,576 B

### `orig` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,157.4 | 73,151.5 | 73,175.3 | 8.4 | 1.000x | 1.000x | unchanged (within spread) | -0.00% (null control: program identical) |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,160.0 | 73,152.4 | 73,177.6 | 9.2 | 1.000x | 1.000x | - | - |

- Δ detail: `pcrec_b8337c33_auto-nocaps-simdna` vs previous `pcrec_7388f1c0_auto-nocaps-simdna`: worst now: `s-057`, 19,071.2 ns, 10,252 B; largest Δ: `s-059`, -2.0 ns (now 9,551.0 ns), 5,134 B

### `orig` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | `plain` | same program | 3,714.1 | 3,710.3 | 3,759.4 | 18.4 | 1.000x | 1.000x | unchanged (within spread) | -0.00% (null control: program identical) | 77 | 48.2 | 12.9 | 100% |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | `plain` | same program | 3,714.2 | 3,709.9 | 3,718.5 | 2.9 | 1.000x | 1.000x | - | - | 77 | 48.2 | 17.2 | 100% |

- Δ detail: `pcrec_b8337c33_auto-nocaps-simdna` vs previous `pcrec_7388f1c0_auto-nocaps-simdna`: worst now: `s-004`, 125.1 ns, 33 B; largest Δ: `s-084`, +1.0 ns (now 8.7 ns), 10 B

## Ranking -- MIXED CLASSES, never compare across cells (per pattern x regime, SET grain: sum over the subject set; best median first)

_D119 bar in this view: |Δ%| > max(IQR%, null band), the `D119 bar` column (definition, strata and bands in the null-control section above). This view's own threshold population: 18 cross-pin cell(s): 4 improve, 0 regress, 0 within the bar, 14 null-control (program identical -- the band's own population); 4 of the verdicts are IQR-only (their stratum's band is not usable)._

### `factored` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | `plain` | same program | 7,020,269.0 | 1.3390 | 7,015,479.6 | 7,028,927.5 | 4,629.1 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 7,023,275.0 | 1.3396 | 7,021,446.1 | 7,026,596.2 | 1,860.0 | 1.000x | 1.000x | unchanged (within spread) | +0.04% (null control: program identical) |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | `plain` | same program | 7,058,665.0 | 1.3463 | 7,054,442.3 | 7,060,286.6 | 2,387.7 | 1.005x | 1.005x | unchanged (within spread) | -0.09% (null control: program identical) |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | `plain` | same program | 7,064,912.5 | 1.3475 | 7,055,808.0 | 7,067,316.3 | 4,576.8 | 1.006x | 1.006x | - | - |

#### `factored` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 3,805,462.8 | 3.6292 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 3,807,136.4 | 3.6308 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_b8337c33_auto-nocaps-simdna` | 3,783,423.4 | 3.6082 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 3,784,653.7 | 3.6093 |
| `t-b-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 17,678.9 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 17,677.9 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_b8337c33_auto-nocaps-simdna` | 17,720.0 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,745.9 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 17,689.5 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 17,703.1 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_b8337c33_auto-nocaps-simdna` | 17,722.6 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,698.6 | 0.0169 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 3,162,541.5 | 3.0160 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 3,162,106.4 | 3.0156 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_b8337c33_auto-nocaps-simdna` | 3,219,462.6 | 3.0703 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 3,221,767.3 | 3.0725 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 17,689.1 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 17,683.5 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_b8337c33_auto-nocaps-simdna` | 17,732.0 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,716.3 | 0.0169 |

- Δ detail: `pcrec_b8337c33_auto-caps-simdna` vs previous `pcrec_7388f1c0_auto-caps-simdna`: worst now (also the largest Δ): `t-a-valid-addrs`, 3,807,136.4 ns, 1,048,576 B
- Δ detail: `pcrec_b8337c33_auto-nocaps-simdna` vs previous `pcrec_7388f1c0_auto-nocaps-simdna`: worst now: `t-a-valid-addrs`, 3,783,423.4 ns, 1,048,576 B; largest Δ: `t-d-prose-sparse-addrs`, -2,304.8 ns (now 3,219,462.6 ns), 1,048,576 B

### `factored` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,164.9 | 73,152.1 | 73,179.5 | 8.7 | 1.000x | 1.000x | unchanged (within spread) | -0.00% (null control: program identical) |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,167.5 | 73,162.4 | 73,249.8 | 33.9 | 1.000x | 1.000x | - | - |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,228.5 | 73,223.7 | 73,239.2 | 5.4 | 1.001x | 1.001x | - | - |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,257.1 | 73,247.6 | 73,260.8 | 4.7 | 1.001x | 1.001x | slower ×1.00 | +0.04% (null control: program identical) |

- Δ detail: `pcrec_b8337c33_auto-nocaps-simdna` vs previous `pcrec_7388f1c0_auto-nocaps-simdna`: worst now: `s-057`, 19,072.8 ns, 10,252 B; largest Δ: `s-064`, -2.5 ns (now 7,646.3 ns), 4,110 B
- Δ detail: `pcrec_b8337c33_auto-caps-simdna` vs previous `pcrec_7388f1c0_auto-caps-simdna`: worst now: `s-057`, 19,071.1 ns, 10,252 B; largest Δ: `s-060`, +8.9 ns (now 19,045.2 ns), 10,240 B

### `factored` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | `plain` | same program | 3,714.1 | 3,710.3 | 3,722.9 | 5.2 | 1.000x | 1.000x | unchanged (within spread) | -0.00% (null control: program identical) | 77 | 48.2 | 12.9 | 100% |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | `plain` | same program | 3,714.2 | 3,713.0 | 3,717.5 | 1.7 | 1.000x | 1.000x | - | - | 77 | 48.2 | 17.2 | 100% |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | `plain` | same program | 3,896.4 | 3,895.4 | 3,900.9 | 2.5 | 1.049x | 1.049x | - | - | 77 | 50.6 | 17.2 | 100% |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 3,899.7 | 3,897.3 | 3,902.3 | 1.7 | 1.050x | 1.050x | unchanged (within spread) | +0.09% (null control: program identical) | 77 | 50.6 | 12.8 | 100% |

- Δ detail: `pcrec_b8337c33_auto-nocaps-simdna` vs previous `pcrec_7388f1c0_auto-nocaps-simdna`: worst now: `s-004`, 124.9 ns, 33 B; largest Δ: `s-084`, +0.9 ns (now 8.7 ns), 10 B
- Δ detail: `pcrec_b8337c33_auto-caps-simdna` vs previous `pcrec_7388f1c0_auto-caps-simdna`: worst now: `s-004`, 129.0 ns, 33 B; largest Δ: `s-081`, +1.1 ns (now 5.0 ns), 0 B

### `floor` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 659,860.4 | 0.1259 | 659,768.9 | 660,219.0 | 191.5 | 1.000x | 1.000x | faster ×1.06 | -5.59% vs bar 0.30% (IQR-only) → **improve (IQR only: band n=4 < 10)** |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | `plain` | same program | 660,358.3 | 0.1260 | 660,047.6 | 660,926.8 | 287.5 | 1.001x | 1.001x | faster ×1.06 | -5.56% vs bar 0.05% (IQR-only) → **improve (IQR only: band n=4 < 10)** |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | `plain` | same program | 698,908.1 | 0.1333 | 698,528.6 | 713,705.5 | 5,822.2 | 1.059x | 1.059x | - | - |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | `plain` | same program | 699,272.2 | 0.1334 | 699,048.7 | 699,713.6 | 249.8 | 1.060x | 1.060x | - | - |

#### `floor` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 576,391.5 | 0.5497 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_b8337c33_auto-nocaps-simdna` | 576,758.3 | 0.5500 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 614,889.3 | 0.5864 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 614,985.7 | 0.5865 |
| `t-b-no-at` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 17,728.5 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_b8337c33_auto-nocaps-simdna` | 17,713.3 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 17,669.3 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,737.2 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 17,710.2 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_b8337c33_auto-nocaps-simdna` | 17,681.5 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 17,713.4 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,700.9 | 0.0169 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 30,309.3 | 0.0289 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_b8337c33_auto-nocaps-simdna` | 30,472.3 | 0.0291 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 30,963.8 | 0.0295 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 31,117.9 | 0.0297 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 17,700.6 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_b8337c33_auto-nocaps-simdna` | 17,737.8 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 17,689.1 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,722.6 | 0.0169 |

- Δ detail: `pcrec_b8337c33_auto-caps-simdna` vs previous `pcrec_7388f1c0_auto-caps-simdna`: worst now (also the largest Δ): `t-a-valid-addrs`, 576,391.5 ns, 1,048,576 B
- Δ detail: `pcrec_b8337c33_auto-nocaps-simdna` vs previous `pcrec_7388f1c0_auto-nocaps-simdna`: worst now (also the largest Δ): `t-a-valid-addrs`, 576,758.3 ns, 1,048,576 B

### `floor` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 759.2 | 758.5 | 761.4 | 1.1 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 759.4 | 759.1 | 762.2 | 1.1 | 1.000x | 1.000x | - | - |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 759.7 | 759.4 | 760.6 | 0.4 | 1.001x | 1.001x | unchanged (within spread) | +0.04% (null control: program identical) |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 759.8 | 759.0 | 762.1 | 1.3 | 1.001x | 1.001x | unchanged (within spread) | +0.08% (null control: program identical) |

- Δ detail: `pcrec_b8337c33_auto-nocaps-simdna` vs previous `pcrec_7388f1c0_auto-nocaps-simdna`: worst now: `s-082`, 13.0 ns, 1 B; largest Δ: `s-083`, +0.1 ns (now 8.9 ns), 43 B
- Δ detail: `pcrec_b8337c33_auto-caps-simdna` vs previous `pcrec_7388f1c0_auto-caps-simdna`: worst now: `s-082`, 13.1 ns, 1 B; largest Δ: `s-081`, +0.1 ns (now 10.2 ns), 0 B

### `floor` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 986.1 | 984.9 | 988.0 | 1.1 | 1.000x | 1.000x | faster ×1.34 | -25.61% vs bar 0.11% (IQR-only) → **improve (IQR only: band n=4 < 10)** | 77 | 12.8 | 100% |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | `plain` | same program | 990.0 | 987.7 | 992.4 | 1.6 | 1.004x | 1.004x | faster ×1.34 | -25.21% vs bar 0.12% (IQR-only) → **improve (IQR only: band n=4 < 10)** | 77 | 12.9 | 100% |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | `plain` | same program | 1,323.7 | 1,321.9 | 1,325.0 | 1.1 | 1.342x | 1.342x | - | - | 77 | 17.2 | 100% |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | `plain` | same program | 1,325.6 | 1,324.6 | 1,328.4 | 1.3 | 1.344x | 1.344x | - | - | 77 | 17.2 | 100% |

- Δ detail: `pcrec_b8337c33_auto-caps-simdna` vs previous `pcrec_7388f1c0_auto-caps-simdna`: worst now: `s-004`, 13.5 ns, 33 B; largest Δ: `s-042`, -4.9 ns (now 12.6 ns), 5 B
- Δ detail: `pcrec_b8337c33_auto-nocaps-simdna` vs previous `pcrec_7388f1c0_auto-nocaps-simdna`: worst now: `s-004`, 13.4 ns, 33 B; largest Δ: `s-042`, -4.9 ns (now 12.6 ns), 5 B

### `orig` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | `plain` | same program | 7,053,695.9 | 1.3454 | 7,046,971.8 | 7,061,389.3 | 4,682.7 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | `plain` | same program | 7,059,574.8 | 1.3465 | 7,058,560.9 | 7,062,570.8 | 1,770.2 | 1.001x | 1.001x | unchanged (within spread) | -0.02% (null control: program identical) |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 7,059,721.9 | 1.3465 | 7,053,019.5 | 7,079,510.2 | 9,117.6 | 1.001x | 1.001x | unchanged (within spread) | +0.09% (null control: program identical) |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | `plain` | same program | 7,060,912.1 | 1.3468 | 7,057,952.3 | 7,070,624.0 | 4,611.7 | 1.001x | 1.001x | - | - |

#### `orig` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 3,781,204.7 | 3.6060 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_b8337c33_auto-nocaps-simdna` | 3,784,037.5 | 3.6087 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 3,782,965.9 | 3.6077 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 3,786,407.2 | 3.6110 |
| `t-b-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 17,685.7 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_b8337c33_auto-nocaps-simdna` | 17,793.3 | 0.0170 |
| `t-b-no-at` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 17,715.8 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,780.8 | 0.0170 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 17,682.7 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_b8337c33_auto-nocaps-simdna` | 17,709.5 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 17,680.9 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,746.6 | 0.0169 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 3,218,037.1 | 3.0690 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_b8337c33_auto-nocaps-simdna` | 3,223,524.5 | 3.0742 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 3,224,086.7 | 3.0747 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 3,222,623.3 | 3.0733 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-caps-simdna` | 17,689.6 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_b8337c33_auto-nocaps-simdna` | 17,693.9 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_b8337c33_auto-caps-simdna` | 17,704.7 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,739.4 | 0.0169 |

- Δ detail: `pcrec_b8337c33_auto-nocaps-simdna` vs previous `pcrec_7388f1c0_auto-nocaps-simdna`: worst now (also the largest Δ): `t-a-valid-addrs`, 3,784,037.5 ns, 1,048,576 B
- Δ detail: `pcrec_b8337c33_auto-caps-simdna` vs previous `pcrec_7388f1c0_auto-caps-simdna`: worst now: `t-a-valid-addrs`, 3,782,965.9 ns, 1,048,576 B; largest Δ: `t-d-prose-sparse-addrs`, +6,049.6 ns (now 3,224,086.7 ns), 1,048,576 B

### `orig` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,126.2 | 73,125.1 | 73,161.0 | 13.7 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,157.4 | 73,151.5 | 73,175.3 | 8.4 | 1.000x | 1.000x | unchanged (within spread) | -0.00% (null control: program identical) |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,160.0 | 73,152.4 | 73,177.6 | 9.2 | 1.000x | 1.000x | - | - |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,165.0 | 73,135.6 | 73,256.5 | 42.5 | 1.001x | 1.001x | unchanged (within spread) | +0.05% (null control: program identical) |

- Δ detail: `pcrec_b8337c33_auto-nocaps-simdna` vs previous `pcrec_7388f1c0_auto-nocaps-simdna`: worst now: `s-057`, 19,071.2 ns, 10,252 B; largest Δ: `s-059`, -2.0 ns (now 9,551.0 ns), 5,134 B
- Δ detail: `pcrec_b8337c33_auto-caps-simdna` vs previous `pcrec_7388f1c0_auto-caps-simdna`: worst now (also the largest Δ): `s-057`, 19,067.5 ns, 10,252 B

### `orig` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | `plain` | same program | 3,710.3 | 3,707.6 | 3,723.2 | 5.6 | 1.000x | 1.000x | - | - | 77 | 48.2 | 17.2 | 100% |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | `plain` | same program | 3,714.1 | 3,710.3 | 3,759.4 | 18.4 | 1.001x | 1.001x | unchanged (within spread) | -0.00% (null control: program identical) | 77 | 48.2 | 12.9 | 100% |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | `plain` | same program | 3,714.2 | 3,709.9 | 3,718.5 | 2.9 | 1.001x | 1.001x | - | - | 77 | 48.2 | 17.2 | 100% |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | `plain` | same program | 3,718.2 | 3,714.5 | 3,718.9 | 1.6 | 1.002x | 1.002x | unchanged (within spread) | +0.21% (null control: program identical) | 77 | 48.3 | 12.8 | 100% |

- Δ detail: `pcrec_b8337c33_auto-nocaps-simdna` vs previous `pcrec_7388f1c0_auto-nocaps-simdna`: worst now: `s-004`, 125.1 ns, 33 B; largest Δ: `s-084`, +1.0 ns (now 8.7 ns), 10 B
- Δ detail: `pcrec_b8337c33_auto-caps-simdna` vs previous `pcrec_7388f1c0_auto-caps-simdna`: worst now: `s-004`, 125.1 ns, 33 B; largest Δ: `s-040`, +1.1 ns (now 8.7 ns), 15 B

## Standing cross-class query (inbox I-101; Frank's own anomaly check -- a QUERY, never a ranking; every hit below is a finding on pcrec's side by definition)

**9 hit(s)** -- each is a finding on pcrec's side by definition (I-101):

| pattern | regime | pcrec auto-nocaps testee | auto-nocaps ns/call | competitor testee | competitor ns/call | ratio (competitor / auto-nocaps) | clears IQR / null band |
|---|---|---|---|---|---|---|---|
| `factored` | `large-subject-throughput` | `pcrec_7388f1c0_auto-nocaps-simdna` | 7,064,912.5 | `pcrec_7388f1c0_auto-caps-simdna` | 7,020,269.0 | 0.994x | clears IQR only: gap 0.63%; IQR 0.11% (clears); band n/a (pcrec 7388f1c0 -> b8337c33, large-subject-throughput / >=1us: n=4 < 10) |
| `factored` | `large-subject-throughput` | `pcrec_b8337c33_auto-nocaps-simdna` | 7,058,665.0 | `pcrec_b8337c33_auto-caps-simdna` | 7,023,275.0 | 0.995x | clears IQR only: gap 0.50%; IQR 0.06% (clears); band n/a (pcrec 7388f1c0 -> b8337c33, large-subject-throughput / >=1us: n=4 < 10) |
| `floor` | `large-subject-throughput` | `pcrec_7388f1c0_auto-nocaps-simdna` | 699,272.2 | `pcrec_7388f1c0_auto-caps-simdna` | 698,908.1 | 0.999x | within IQR: gap 0.05%; IQR 0.30% (within); band n/a (pcrec 7388f1c0 -> b8337c33, large-subject-throughput / >=1us: n=4 < 10) |
| `floor` | `large-subject-throughput` | `pcrec_b8337c33_auto-nocaps-simdna` | 660,358.3 | `pcrec_b8337c33_auto-caps-simdna` | 659,860.4 | 0.999x | clears IQR only: gap 0.08%; IQR 0.06% (clears); band n/a (pcrec 7388f1c0 -> b8337c33, large-subject-throughput / >=1us: n=4 < 10) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 759.4 | `pcrec_7388f1c0_auto-caps-simdna` | 759.2 | 1.000x | within IQR: gap 0.02%; IQR 0.18% (within); band n/a (pcrec 7388f1c0 -> b8337c33, match-compliance / 100ns-1us: n=2 < 10) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 990.0 | `pcrec_b8337c33_auto-caps-simdna` | 986.1 | 0.996x | clears IQR only: gap 0.39%; IQR 0.21% (clears); band n/a (pcrec 7388f1c0 -> b8337c33, short-subject-search / 100ns-1us: n=0 < 10) |
| `orig` | `large-subject-throughput` | `pcrec_7388f1c0_auto-nocaps-simdna` | 7,060,912.1 | `pcrec_7388f1c0_auto-caps-simdna` | 7,053,695.9 | 0.999x | clears IQR only: gap 0.10%; IQR 0.09% (clears); band n/a (pcrec 7388f1c0 -> b8337c33, large-subject-throughput / >=1us: n=4 < 10) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 73,160.0 | `pcrec_7388f1c0_auto-caps-simdna` | 73,126.2 | 1.000x | clears IQR only: gap 0.05%; IQR 0.02% (clears); band n/a (pcrec 7388f1c0 -> b8337c33, match-compliance / >=1us: n=4 < 10) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 3,714.2 | `pcrec_7388f1c0_auto-caps-simdna` | 3,710.3 | 0.999x | clears IQR only: gap 0.11%; IQR 0.07% (clears); band n/a (pcrec 7388f1c0 -> b8337c33, short-subject-search / >=1us: n=4 < 10) |

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
- `pcrec_b8337c33_auto-caps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-nocaps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-nocaps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-nocaps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-nocaps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-nocaps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-nocaps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
    - sel = pcrec's `RX_ENGINE_SEL`; `DFA fallback tripped` = sel not in (selected, forced), and NOTHING else -- since pcrec 263b013 ([LIM-1] / [OPT-4.1]) every fallback has its own token (`overflowed-dfa`, `overflowed-prefilter`, `collapsed-prefilter`, `declined-nullable`, `size-cap-retry`), the size-cap rescue included; at pcrec 96e44c2 that rescue stamped `sel=selected` and only its `lang=count-collapsed (size cap retry, ...)` clause says so.
    - edge = pcrec's `RX_DFA_SCAN_EDGE` ([OPT-5] STEP 1, abi 13+), how a DFA scan tests a SCAN EDGE's byte class: `range` = a contiguous run (subtract-and-compare against two immediates); `bitmap` = a non-contiguous class (a 256-byte membership read); `mixed` = one artifact whose machines took both forms; `none` = no collapsible run (an attempt/empty scan, or -fno-scan-edge).
    - edges = pcrec's `scan_edges` ([B32]): how many [OPT-5] SCAN EDGES this artifact's SEARCH-side machines carry (`rx_search`/`rx_prefilter`), the per-scan-iteration compare-count covariate `edge`'s single shape token cannot separate (I-33: the cost is one compare per edge per iteration); the `(match: M)` parenthetical, when carried, is the SAME count on the anchored `rx_match` machine, kept apart because the measured [OPT-EDGE] regression is search-band only. `0` is a real, recorded value.
    - start = pcrec's `RX_DFA_START` ([OPT-5] STEP 2, abi 16+), how the SEARCH entry recovers the match START: `pinned` = the forward machine's start state accepts unconditionally, so the match provably begins at `search_from` and THE ARTIFACT CARRIES NO REVERSE MACHINE at all (no reverse tables, accessor block or scan loop); `reverse-pass` = it carries one and walks it backwards from the match end. The two forms are ANSWER-IDENTICAL by contract -- `caps[0][0]`'s absolute offsets and the zero-length-match convention hold under both -- so this explains a row's SIZE and pass count, never its answer.
      - start=end-minus-width: every match is one fixed byte width W, so the start is the verified end minus W; NO reverse machine (abi 74, [START-LANDING])
    - folds = pcrec's `RX_DFA_UNIFORM_FOLDS` ([CC-DIFF] STEP 1, abi 17+): how many of this artifact's DFA tables (two per machine it contains -- forward always, reverse unless `start=pinned`, anchored under `match=unwrapped`; so 0..6) had ALL-EQUAL cells and were NOT EMITTED, the accessor returning the constant. `table=` keeps naming the encoding that was SELECTED, so `premultiplied` beside `folds=4` is an artifact carrying NO transition table at all -- a SIZE fact, never an answer one. `0` is a real, recorded value.

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | emit bytes | code bytes | jitter | outcomes | emit-c ns | gcc ns | load ns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `pcrec_7388f1c0_auto-caps-simdna` | 183,364,750.0 | 183,169,307.0 | 195,276,771.0 | 4,758,516.4 | 5 | 49,472 | 85,071 | 16,377 | 0.026 (max is trial 1) | compiled=5 | 9,485,779.0 | 173,662,847.0 | 221,130.0 |
| `factored` | `whole-subject` | `pcrec_7388f1c0_auto-caps-simdna` | 178,806,804.0 | 172,689,703.0 | 187,691,044.0 | 6,452,235.3 | 5 | 37,040 | 42,326 | 16,649 | 0.036 | compiled=5 | 9,580,703.0 | 163,914,435.0 | 104,492.0 |
| `factored` | `plain` | `pcrec_7388f1c0_auto-nocaps-simdna` | 180,362,043.0 | 179,151,257.0 | 191,095,150.0 | 4,622,010.6 | 5 | 49,472 | 84,868 | 16,170 | 0.026 (max is trial 1) | compiled=5 | 9,519,133.0 | 170,781,742.0 | 101,849.0 |
| `factored` | `whole-subject` | `pcrec_7388f1c0_auto-nocaps-simdna` | 182,921,516.0 | 176,804,644.0 | 195,038,624.0 | 7,408,307.9 | 5 | 37,040 | 42,143 | 16,462 | 0.040 | compiled=5 | 11,574,223.0 | 168,974,192.0 | 187,501.0 |
| `factored` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 212,941,107.0 | 190,569,548.0 | 220,192,927.0 | 12,562,001.7 | 5 | 49,472 | 85,071 | 16,377 | 0.059 (max is trial 1) | compiled=5 | 20,469,919.0 | 184,779,176.0 | 170,721.0 |
| `factored` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 173,326,956.0 | 172,159,429.0 | 191,772,975.0 | 7,466,710.7 | 5 | 37,040 | 42,326 | 16,649 | 0.043 (max is trial 1) | compiled=5 | 9,484,881.0 | 163,650,874.0 | 190,611.0 |
| `factored` | `plain` | `pcrec_b8337c33_auto-nocaps-simdna` | 178,865,825.0 | 178,528,114.0 | 197,356,525.0 | 7,561,763.1 | 5 | 49,472 | 84,868 | 16,170 | 0.042 | compiled=5 | 9,734,283.0 | 168,847,711.0 | 185,351.0 |
| `factored` | `whole-subject` | `pcrec_b8337c33_auto-nocaps-simdna` | 172,855,484.0 | 169,225,045.0 | 185,951,632.0 | 6,589,063.4 | 5 | 37,040 | 42,143 | 16,462 | 0.038 | compiled=5 | 9,566,162.0 | 160,340,495.0 | 194,781.0 |
| `floor` | `plain` | `pcrec_7388f1c0_auto-caps-simdna` | 170,410,710.0 | 159,328,642.0 | 172,537,731.0 | 4,681,503.0 | 5 | 28,912 | 20,571 | 15,574 | 0.027 (max is trial 1) | compiled=5 | 2,203,342.0 | 167,694,325.0 | 105,822.0 |
| `floor` | `whole-subject` | `pcrec_7388f1c0_auto-caps-simdna` | 160,104,955.0 | 155,466,821.0 | 172,009,567.0 | 5,785,265.1 | 5 | 28,808 | 19,474 | 15,916 | 0.036 (max is trial 1) | compiled=5 | 2,072,261.0 | 157,862,122.0 | 182,231.0 |
| `floor` | `plain` | `pcrec_7388f1c0_auto-nocaps-simdna` | 166,718,038.0 | 157,746,712.0 | 169,966,727.0 | 4,395,334.5 | 5 | 28,912 | 20,571 | 15,574 | 0.026 | compiled=5 | 2,187,802.0 | 164,433,436.0 | 98,450.0 |
| `floor` | `whole-subject` | `pcrec_7388f1c0_auto-nocaps-simdna` | 166,959,222.0 | 160,255,104.0 | 168,755,031.0 | 3,588,272.0 | 5 | 28,808 | 19,474 | 15,916 | 0.021 | compiled=5 | 2,076,193.0 | 164,792,188.0 | 105,320.0 |
| `floor` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 163,842,254.0 | 158,834,258.0 | 169,532,206.0 | 3,656,715.2 | 5 | 28,768 | 17,888 | 14,557 | 0.022 | compiled=5 | 2,159,611.0 | 161,576,962.0 | 107,590.0 |
| `floor` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 164,567,540.0 | 158,942,109.0 | 168,981,751.0 | 3,274,019.5 | 5 | 28,808 | 19,474 | 15,916 | 0.020 | compiled=5 | 2,087,561.0 | 162,379,287.0 | 202,301.0 |
| `floor` | `plain` | `pcrec_b8337c33_auto-nocaps-simdna` | 160,812,067.0 | 153,906,159.0 | 165,340,862.0 | 3,678,380.7 | 5 | 28,768 | 17,888 | 14,557 | 0.023 | compiled=5 | 2,148,771.0 | 158,276,344.0 | 185,191.0 |
| `floor` | `whole-subject` | `pcrec_b8337c33_auto-nocaps-simdna` | 169,634,056.0 | 162,871,298.0 | 172,958,303.0 | 3,507,701.0 | 5 | 28,808 | 19,474 | 15,916 | 0.021 | compiled=5 | 2,081,211.0 | 164,870,830.0 | 204,111.0 |
| `orig` | `plain` | `pcrec_7388f1c0_auto-caps-simdna` | 182,954,393.0 | 178,691,073.0 | 190,871,808.0 | 4,569,826.4 | 5 | 49,440 | 84,644 | 16,117 | 0.025 | compiled=5 | 9,077,639.0 | 169,604,234.0 | 120,169.0 |
| `orig` | `whole-subject` | `pcrec_7388f1c0_auto-caps-simdna` | 174,538,901.0 | 173,513,145.0 | 177,638,087.0 | 1,417,535.9 | 5 | 32,904 | 41,919 | 16,409 | 0.008 (max is trial 1) | compiled=5 | 8,801,677.0 | 165,062,550.0 | 188,581.0 |
| `orig` | `plain` | `pcrec_7388f1c0_auto-nocaps-simdna` | 189,011,509.0 | 167,988,099.0 | 201,753,867.0 | 11,160,035.5 | 5 | 49,440 | 84,644 | 16,117 | 0.059 | compiled=5 | 9,155,119.0 | 172,079,120.0 | 103,900.0 |
| `orig` | `whole-subject` | `pcrec_7388f1c0_auto-nocaps-simdna` | 177,383,977.0 | 167,952,017.0 | 178,377,491.0 | 4,689,219.7 | 5 | 32,904 | 41,919 | 16,409 | 0.026 | compiled=5 | 8,791,647.0 | 159,103,649.0 | 100,500.0 |
| `orig` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 188,982,029.0 | 179,142,686.0 | 192,938,429.0 | 4,591,232.2 | 5 | 49,440 | 84,644 | 16,117 | 0.024 (max is trial 1) | compiled=5 | 10,521,636.0 | 170,299,529.0 | 194,311.0 |
| `orig` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 175,038,255.0 | 168,213,757.0 | 178,014,081.0 | 3,662,283.4 | 5 | 32,904 | 41,919 | 16,409 | 0.021 | compiled=5 | 8,801,987.0 | 166,042,626.0 | 184,800.0 |
| `orig` | `plain` | `pcrec_b8337c33_auto-nocaps-simdna` | 188,146,249.0 | 178,986,966.0 | 217,998,886.0 | 14,085,930.2 | 5 | 49,440 | 84,644 | 16,117 | 0.075 | compiled=5 | 9,258,171.0 | 178,611,674.0 | 208,572.0 |
| `orig` | `whole-subject` | `pcrec_b8337c33_auto-nocaps-simdna` | 177,609,097.0 | 167,674,894.0 | 185,866,384.0 | 6,017,568.9 | 5 | 32,904 | 41,919 | 16,409 | 0.034 | compiled=5 | 8,825,699.0 | 165,175,871.0 | 96,901.0 |

