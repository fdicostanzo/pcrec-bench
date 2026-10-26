# pcrec-bench report

reporter: v28 (2026-10-25)

## Query

- filters: subbench=email-specimen, version=0.2, machine=ryzen7700x, since=2026-10-25T19:30:00Z, until=2026-10-26T08:00:00Z, testee=pcrec_6b2dbd3e_auto-caps-simdna, testee=pcrec_9ae59f5d4_auto-caps-simdna
- record source: store/index.tsv (2 record(s) matching this query)
- records included: 2
- worst other-core busy: 6.04% (`pcrec_9ae59f5d4_auto-caps-simdna` / `factored` / `short-subject-search`)
    - `email-specimen@0.2__pcrec_6b2dbd3e_auto-caps-simdna__ryzen7700x__20261026T054355Z` (store/records/email-specimen@0.2/pcrec_6b2dbd3e_auto-caps-simdna/email-specimen@0.2__pcrec_6b2dbd3e_auto-caps-simdna__ryzen7700x__20261026T054355Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials); after: occ 11.29%
    - `email-specimen@0.2__pcrec_9ae59f5d4_auto-caps-simdna__ryzen7700x__20261026T053647Z` (store/records/email-specimen@0.2/pcrec_9ae59f5d4_auto-caps-simdna/email-specimen@0.2__pcrec_9ae59f5d4_auto-caps-simdna__ryzen7700x__20261026T053647Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials); after: occ 11.85%
- sub-bench version(s): email-specimen@0.2
- machine(s): ryzen7700x
- schema version(s): 1.10
- grain: set (sum of per-subject ns/call over the whole subject set, reduced over trials; a set cell is excluded if ANY subject in it fails)
- reduction: median/min/max/stddev (population) over per-trial `elapsed_ns / iterations`; lazy-JIT compile cost is DERIVED as first-match-row-minus-steady-state (lowest `seq` timed row for the pattern, minus the median of every other timed row), one value per (pattern, testee), never pooled with another execution-model class's compile cost
- `form`: this report includes a `whole-subject` artifact beside `plain` for at least one cell (schema v1.1: a testee with no end-anchored mode compiles and times a SEPARATE artifact for match-compliance, e.g. `(?:pattern)\z`, where another testee reaches the same regime via runtime flags on its ordinary artifact) -- shown as a per-row COLUMN, not a split: both forms answer the same regime and RANK TOGETHER in one table (`form` is a key only for compile-cost rows, where a whole-subject artifact is genuinely a separate compile with its own cost); `fact` restates it as 'same program' / 'separate artifact' (R4)
- status policy (OD-B14): a ranking row whose record `status` is not `measured` is excluded from ranking by default, listed under its table as `not ranked: <testee> -- <status> (<status_detail excerpt>)`; `--include-unmeasured` ranks it instead, with `status` shown
- trial-agreement policy (schema v1.4, rule v1.10-group, X31-X33): a record's five trials must agree to within k=1.5 on every group of its rows — one slow trial of five tolerated; two, or one fast, is a disagreeing row; a group disagrees at >= 2 disagreeing rows reaching a third of it (d_min=2, c=3); a record with a disagreeing group, or with fewer than five odd trials, is `inconclusive-spread` and unranked like `inconclusive-load`; the after-run load/occupancy samples are provenance (v1.4 X13), shown under --include-provenance; under v1.10-group a `substitution` row's one-iteration trials are timed and judged (X32 versioned, [B144])
- status rule: v1.4 X13 (pre-flight + trial agreement) on 2 record(s)
- tier policy (R3, schema v1.2 `tier`, absent = `pinned`): a `scratch`-tier row is excluded from ranking by default, listed as `scratch: <testee>`; `--include-scratch` ranks it instead, with a `tier` column
- duplicate-record policy (OD-B15, amended 2026-08-25): the NEWEST MEASURED record per (subbench@version, testee_id, machine) ranks by default -- a newer record that is NOT measured does not supersede a measured one of the same testee and version (listed as "newer, not measured" instead); only when no record in the group is measured does the newest record overall stand (itself unranked per the status policy above, unless --include-unmeasured). `--all-records` shows every record as its own row, its testee id suffixed `@<timestamp>`

## Null-control band (D119 bar; [B79], inbox I-93 block B / I-104)

- D119 bar (inbox I-93 block B / I-104): a cross-pin cell moved iff |Δ%| > max(IQR%, null band) -- Δ% = (after - before) / before; IQR% = the BEFORE side's Type-7 IQR of its per-trial set sums over the before median; null band = the largest |Δ%| any PROGRAM-IDENTICAL cell of the same (regime, baseline scale) stratum reached across the same pin pair (symmetric); a stratum with fewer than 10 program-identical cells has NO usable band and its verdicts say `IQR only` by name.
- baseline scale: the BEFORE (older pin) set-grain median -- `>=1us` / `100ns-1us` / `<100ns`; strata are per REGIME (I-104).
- sufficiency: a stratum needs >= 10 program-identical cells -- the band is a sample maximum, and one more null cell exceeds the maximum of n with chance 1/(n+1) (<= 9.1% at n = 10).
- identity: the records' own `engine_metadata.program_sha256` ([B88], schema v1.7) where BOTH compile rows of a cell carry it; otherwise OUR OWN census (`tools/program_identity.py`: both pins re-emitted with the pinned binaries under each config's recorded flags, `.c` + `.h` compared after dropping ONLY the generated-by line, the `.abi` integer and one-sided `#define` stamps). Which records carry the field, per side: `pcrec 6b2dbd3e -> 9ae59f5d4`: the BEFORE (`6b2dbd3e`) records carry `program_sha256` (6 of 6 compiled cell(s)), the AFTER (`9ae59f5d4`) records carry `program_sha256` (6 of 6 compiled cell(s)).

### `pcrec 6b2dbd3e -> 9ae59f5d4` (email-specimen@0.2)

- identity from the records ([B88], schema v1.7): 9 cell(s) read `engine_metadata.program_sha256` on BOTH compile rows, 0 fell back to the census, criterion v3 (`program_sha256_v3`) on 9 cell(s), v2 (`program_sha256`) on 0; no census for this pair
- cells: 9 cross-pin set cell(s) measured on both sides; 9 program-identical (the null population)

| regime | baseline scale | n null cells | min Δ% | median Δ% | max Δ% | band (±) | status |
|---|---|---|---|---|---|---|---|
| `large-subject-throughput` | `>=1us` | 3 | -0.16% | -0.11% | -0.01% | n/a | insufficient (n=3 < 10) |
| `large-subject-throughput` | `100ns-1us` | 0 | - | - | - | n/a | empty (n=0) |
| `large-subject-throughput` | `<100ns` | 0 | - | - | - | n/a | empty (n=0) |
| `match-compliance` | `>=1us` | 2 | -0.02% | +0.01% | +0.03% | n/a | insufficient (n=2 < 10) |
| `match-compliance` | `100ns-1us` | 1 | -0.16% | -0.16% | -0.16% | n/a | insufficient (n=1 < 10) |
| `match-compliance` | `<100ns` | 0 | - | - | - | n/a | empty (n=0) |
| `short-subject-search` | `>=1us` | 2 | +0.07% | +0.26% | +0.46% | n/a | insufficient (n=2 < 10) |
| `short-subject-search` | `100ns-1us` | 1 | -0.48% | -0.48% | -0.48% | n/a | insufficient (n=1 < 10) |
| `short-subject-search` | `<100ns` | 0 | - | - | - | n/a | empty (n=0) |

## Ranking (per pattern x regime, SET grain: sum over the subject set; best median first)

_D119 bar in this view: |Δ%| > max(IQR%, null band), the `D119 bar` column (definition, strata and bands in the null-control section above). This view's own threshold population: 9 cross-pin cell(s): 0 improve, 0 regress, 0 within the bar, 9 null-control (program identical -- the band's own population); 0 of the verdicts are IQR-only (their stratum's band is not usable)._

### `factored` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 4,204,701.9 | 0.8020 | 4,186,838.5 | 4,221,537.0 | 12,086.6 | 1.000x | 1.000x | unchanged (within spread) | -0.01% (null control: program identical) |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 4,204,979.1 | 0.8020 | 4,201,055.2 | 4,210,434.6 | 3,160.0 | 1.000x | 1.000x | - | - |

#### `factored` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_9ae59f5d4_auto-caps-simdna` | 2,224,791.6 | 2.1217 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 2,232,208.0 | 2.1288 |
| `t-b-no-at` | 1,048,576 | `pcrec_9ae59f5d4_auto-caps-simdna` | 7,458.3 | 0.0071 |
| `t-b-no-at` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 7,495.7 | 0.0071 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_9ae59f5d4_auto-caps-simdna` | 7,485.3 | 0.0071 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 7,490.0 | 0.0071 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_9ae59f5d4_auto-caps-simdna` | 1,943,996.8 | 1.8539 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,950,171.3 | 1.8598 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_9ae59f5d4_auto-caps-simdna` | 7,475.9 | 0.0071 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 7,562.9 | 0.0072 |

- Δ detail: `pcrec_9ae59f5d4_auto-caps-simdna` vs previous `pcrec_6b2dbd3e_auto-caps-simdna`: worst now (also the largest Δ): `t-a-valid-addrs`, 2,224,791.6 ns, 1,048,576 B

### `factored` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 43,697.1 | 43,692.8 | 43,704.5 | 4.1 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 43,711.4 | 43,672.4 | 43,730.0 | 20.2 | 1.000x | 1.000x | unchanged (within spread) | +0.03% (null control: program identical) |

- Δ detail: `pcrec_9ae59f5d4_auto-caps-simdna` vs previous `pcrec_6b2dbd3e_auto-caps-simdna`: worst now: `s-057`, 11,403.4 ns, 10,252 B; largest Δ: `s-064`, +55.1 ns (now 4,616.0 ns), 4,110 B

### `factored` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 2,032.6 | 2,029.5 | 2,052.4 | 10.7 | 1.000x | 1.000x | - | - | 77 | 26.4 | 6.5 | 100% |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 2,041.9 | 2,031.8 | 2,061.8 | 11.4 | 1.005x | 1.005x | unchanged (within spread) | +0.46% (null control: program identical) | 77 | 26.5 | 6.5 | 100% |

- Δ detail: `pcrec_9ae59f5d4_auto-caps-simdna` vs previous `pcrec_6b2dbd3e_auto-caps-simdna`: worst now: `s-004`, 72.5 ns, 33 B; largest Δ: `s-027`, +0.7 ns (now 48.5 ns), 22 B

### `floor` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 341,730.2 | 0.0652 | 341,460.9 | 342,346.1 | 299.4 | 1.000x | 1.000x | unchanged (within spread) | -0.16% (null control: program identical) |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 342,272.3 | 0.0653 | 341,852.8 | 345,417.4 | 1,412.0 | 1.002x | 1.002x | - | - |

#### `floor` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_9ae59f5d4_auto-caps-simdna` | 307,194.2 | 0.2930 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 307,498.0 | 0.2933 |
| `t-b-no-at` | 1,048,576 | `pcrec_9ae59f5d4_auto-caps-simdna` | 7,509.9 | 0.0072 |
| `t-b-no-at` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 7,566.0 | 0.0072 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_9ae59f5d4_auto-caps-simdna` | 7,546.3 | 0.0072 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 7,599.4 | 0.0072 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_9ae59f5d4_auto-caps-simdna` | 11,969.9 | 0.0114 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 12,144.5 | 0.0116 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_9ae59f5d4_auto-caps-simdna` | 7,564.5 | 0.0072 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 7,437.6 | 0.0071 |

- Δ detail: `pcrec_9ae59f5d4_auto-caps-simdna` vs previous `pcrec_6b2dbd3e_auto-caps-simdna`: worst now (also the largest Δ): `t-a-valid-addrs`, 307,194.2 ns, 1,048,576 B

### `floor` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 377.5 | 376.7 | 382.6 | 2.3 | 1.000x | 1.000x | unchanged (within spread) | -0.16% (null control: program identical) |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 378.1 | 377.6 | 381.6 | 1.5 | 1.002x | 1.002x | - | - |

- Δ detail: `pcrec_9ae59f5d4_auto-caps-simdna` vs previous `pcrec_6b2dbd3e_auto-caps-simdna`: worst now: `s-082`, 6.4 ns, 1 B; largest Δ: `s-083`, +0.3 ns (now 4.8 ns), 43 B

### `floor` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 501.9 | 501.8 | 518.2 | 6.4 | 1.000x | 1.000x | unchanged (within spread) | -0.48% (null control: program identical) | 77 | 6.5 | 100% |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 504.3 | 502.0 | 505.7 | 1.3 | 1.005x | 1.005x | - | - | 77 | 6.5 | 100% |

- Δ detail: `pcrec_9ae59f5d4_auto-caps-simdna` vs previous `pcrec_6b2dbd3e_auto-caps-simdna`: worst now: `s-023`, 6.7 ns, 18 B; largest Δ: `s-040`, -0.3 ns (now 3.8 ns), 15 B

### `orig` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 4,187,248.5 | 0.7987 | 4,172,124.8 | 4,208,983.7 | 14,945.1 | 1.000x | 1.000x | unchanged (within spread) | -0.11% (null control: program identical) |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 4,191,724.4 | 0.7995 | 4,178,053.9 | 4,201,231.2 | 7,491.1 | 1.001x | 1.001x | - | - |

#### `orig` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_9ae59f5d4_auto-caps-simdna` | 2,210,364.7 | 2.1080 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 2,211,338.7 | 2.1089 |
| `t-b-no-at` | 1,048,576 | `pcrec_9ae59f5d4_auto-caps-simdna` | 7,415.0 | 0.0071 |
| `t-b-no-at` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 7,473.8 | 0.0071 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_9ae59f5d4_auto-caps-simdna` | 7,587.7 | 0.0072 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 7,545.0 | 0.0072 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_9ae59f5d4_auto-caps-simdna` | 1,944,686.2 | 1.8546 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,957,341.7 | 1.8667 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_9ae59f5d4_auto-caps-simdna` | 7,540.1 | 0.0072 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 7,535.5 | 0.0072 |

- Δ detail: `pcrec_9ae59f5d4_auto-caps-simdna` vs previous `pcrec_6b2dbd3e_auto-caps-simdna`: worst now: `t-a-valid-addrs`, 2,210,364.7 ns, 1,048,576 B; largest Δ: `t-d-prose-sparse-addrs`, -12,655.5 ns (now 1,944,686.2 ns), 1,048,576 B

### `orig` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_9ae59f5d4_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 43,618.2 | 43,584.3 | 43,777.0 | 68.5 | 1.000x | 1.000x | unchanged (within spread) | -0.02% (null control: program identical) |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 43,625.9 | 43,568.9 | 43,670.8 | 33.6 | 1.000x | 1.000x | - | - |

- Δ detail: `pcrec_9ae59f5d4_auto-caps-simdna` vs previous `pcrec_6b2dbd3e_auto-caps-simdna`: worst now (also the largest Δ): `s-057`, 11,363.3 ns, 10,252 B

### `orig` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 2,025.0 | 2,019.5 | 2,055.5 | 13.1 | 1.000x | 1.000x | - | - | 77 | 26.3 | 6.5 | 100% |
| 2 | `pcrec_9ae59f5d4_auto-caps-simdna` | measured | `plain` | same program | 2,026.4 | 2,018.3 | 2,043.0 | 10.3 | 1.001x | 1.001x | unchanged (within spread) | +0.07% (null control: program identical) | 77 | 26.3 | 6.5 | 100% |

- Δ detail: `pcrec_9ae59f5d4_auto-caps-simdna` vs previous `pcrec_6b2dbd3e_auto-caps-simdna`: worst now: `s-004`, 72.2 ns, 33 B; largest Δ: `s-012`, -0.5 ns (now 38.8 ns), 18 B

## Standing cross-class query (inbox I-101; Frank's own anomaly check -- a QUERY, never a ranking; every hit below is a finding on pcrec's side by definition)

_0 hits: no included YES-class config's median beats any pcrec `auto-nocaps` row's median in this report's roster._

## Compile cost (by execution-model class; never pooled across classes)

### `compiled-aot`

- `pcrec_6b2dbd3e_auto-caps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_9ae59f5d4_auto-caps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_9ae59f5d4_auto-caps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_9ae59f5d4_auto-caps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_9ae59f5d4_auto-caps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_9ae59f5d4_auto-caps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_9ae59f5d4_auto-caps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
    - sel = pcrec's `RX_ENGINE_SEL`; `DFA fallback tripped` = sel not in (selected, forced), and NOTHING else -- since pcrec 263b013 ([LIM-1] / [OPT-4.1]) every fallback has its own token (`overflowed-dfa`, `overflowed-prefilter`, `collapsed-prefilter`, `declined-nullable`, `size-cap-retry`), the size-cap rescue included; at pcrec 96e44c2 that rescue stamped `sel=selected` and only its `lang=count-collapsed (size cap retry, ...)` clause says so.
    - edge = pcrec's `RX_DFA_SCAN_EDGE` ([OPT-5] STEP 1, abi 13+), how a DFA scan tests a SCAN EDGE's byte class: `range` = a contiguous run (subtract-and-compare against two immediates); `bitmap` = a non-contiguous class (a 256-byte membership read); `mixed` = one artifact whose machines took both forms; `none` = no collapsible run (an attempt/empty scan, or -fno-scan-edge).
    - edges = pcrec's `scan_edges` ([B32]): how many [OPT-5] SCAN EDGES this artifact's SEARCH-side machines carry (`rx_search`/`rx_prefilter`), the per-scan-iteration compare-count covariate `edge`'s single shape token cannot separate (I-33: the cost is one compare per edge per iteration); the `(match: M)` parenthetical, when carried, is the SAME count on the anchored `rx_match` machine, kept apart because the measured [OPT-EDGE] regression is search-band only. `0` is a real, recorded value.
    - start = pcrec's `RX_DFA_START` ([OPT-5] STEP 2, abi 16+), how the SEARCH entry recovers the match START: `pinned` = the forward machine's start state accepts unconditionally, so the match provably begins at `search_from` and THE ARTIFACT CARRIES NO REVERSE MACHINE at all (no reverse tables, accessor block or scan loop); `reverse-pass` = it carries one and walks it backwards from the match end. The two forms are ANSWER-IDENTICAL by contract -- `caps[0][0]`'s absolute offsets and the zero-length-match convention hold under both -- so this explains a row's SIZE and pass count, never its answer.
      - start=end-minus-width: every match is one fixed byte width W, so the start is the verified end minus W; NO reverse machine (abi 74, [START-LANDING])
    - folds = pcrec's `RX_DFA_UNIFORM_FOLDS` ([CC-DIFF] STEP 1, abi 17+): how many of this artifact's DFA tables (two per machine it contains -- forward always, reverse unless `start=pinned`, anchored under `match=unwrapped`; so 0..6) had ALL-EQUAL cells and were NOT EMITTED, the accessor returning the constant. `table=` keeps naming the encoding that was SELECTED, so `premultiplied` beside `folds=4` is an artifact carrying NO transition table at all -- a SIZE fact, never an answer one. `0` is a real, recorded value.

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | emit bytes | code bytes | jitter | outcomes | emit-c ns | gcc ns | load ns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 78,962,809.0 | 78,096,939.0 | 79,347,985.0 | 440,446.0 | 5 | 49,472 | 85,071 | 16,377 | 0.006 | compiled=5 | 4,396,386.0 | 74,349,905.0 | 53,641.0 |
| `factored` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 73,857,769.0 | 73,315,796.0 | 75,048,904.0 | 611,448.3 | 5 | 37,040 | 42,326 | 16,649 | 0.008 | compiled=5 | 3,908,857.0 | 69,891,393.0 | 46,768.0 |
| `factored` | `plain` | `pcrec_9ae59f5d4_auto-caps-simdna` | 93,815,091.0 | 92,591,955.0 | 95,061,610.0 | 970,400.1 | 5 | 53,680 | 85,177 | 16,483 | 0.010 | compiled=5 | 6,641,016.0 | 86,831,970.0 | 46,618.0 |
| `factored` | `whole-subject` | `pcrec_9ae59f5d4_auto-caps-simdna` | 88,918,513.0 | 88,366,924.0 | 89,940,850.0 | 554,329.1 | 5 | 41,248 | 42,432 | 16,755 | 0.006 | compiled=5 | 4,685,431.0 | 84,165,996.0 | 42,731.0 |
| `floor` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 66,046,005.0 | 64,789,087.0 | 67,090,202.0 | 783,546.0 | 5 | 28,768 | 17,888 | 14,557 | 0.012 (max is trial 1) | compiled=5 | 1,035,782.0 | 64,887,702.0 | 49,142.0 |
| `floor` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 66,803,783.0 | 66,567,579.0 | 67,731,924.0 | 415,028.2 | 5 | 28,808 | 19,474 | 15,916 | 0.006 (max is trial 1) | compiled=5 | 1,002,380.0 | 65,715,622.0 | 51,788.0 |
| `floor` | `plain` | `pcrec_9ae59f5d4_auto-caps-simdna` | 81,178,315.0 | 80,240,948.0 | 81,443,154.0 | 485,707.4 | 5 | 28,880 | 17,994 | 14,663 | 0.006 (max is trial 1) | compiled=5 | 2,050,505.0 | 79,097,313.0 | 45,325.0 |
| `floor` | `whole-subject` | `pcrec_9ae59f5d4_auto-caps-simdna` | 80,724,359.0 | 79,947,625.0 | 82,080,927.0 | 776,525.0 | 5 | 28,920 | 19,580 | 16,022 | 0.010 (max is trial 1) | compiled=5 | 1,641,875.0 | 78,986,374.0 | 54,072.0 |
| `orig` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 76,225,301.0 | 75,842,499.0 | 77,158,690.0 | 582,513.7 | 5 | 49,440 | 84,644 | 16,117 | 0.008 | compiled=5 | 4,140,684.0 | 72,035,915.0 | 49,113.0 |
| `orig` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 72,180,306.0 | 71,225,448.0 | 72,977,800.0 | 561,080.9 | 5 | 32,904 | 41,919 | 16,409 | 0.008 | compiled=5 | 3,728,346.0 | 68,022,100.0 | 52,339.0 |
| `orig` | `plain` | `pcrec_9ae59f5d4_auto-caps-simdna` | 91,152,163.0 | 90,111,772.0 | 92,658,973.0 | 1,015,432.5 | 5 | 53,648 | 84,750 | 16,223 | 0.011 (max is trial 1) | compiled=5 | 6,377,941.0 | 84,746,129.0 | 49,894.0 |
| `orig` | `whole-subject` | `pcrec_9ae59f5d4_auto-caps-simdna` | 84,887,134.0 | 84,485,639.0 | 86,586,258.0 | 764,067.0 | 5 | 37,112 | 42,025 | 16,515 | 0.009 | compiled=5 | 4,911,166.0 | 79,897,301.0 | 55,995.0 |
    - emit/code bytes across abi 77: pcrec's size definition moves at the boundary -- a flat ~+106 B of counted stamp and initializer lines on a typical artifact (`RX_COMPOUND`, `RX_MEASURES`, `.measures`/`.next`/`.next_n`), and from abi 83 the find-all iterator scaffold (`_next`, the forwarder twins) is EXCLUDED from both counts with no marker in the emitted text. Read a Delta that spans the boundary against that, not as a program change; the DFA retry machine (`RX_ITER_RETRY=retry`) is NOT scaffold and counts (b142prep: +3-4 KB on narrow DFAs).

