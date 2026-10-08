# pcrec-bench

A benchmark harness that compares [pcrec](https://github.com/fdicostanzo/pcrec), an ahead-of-time PCRE-to-C regex compiler, against major regex engines: libpcre2 (interpreter, JIT, DFA), RE2, Rust `regex`, Oniguruma, TRE and Vectorscan.

## Headline

<!-- frontpage:headline:begin -->
On `capability@0.1` (128 pattern-regime cells), pcrec 0.2.0-beta+c4c70f2c (config `pcrec-auto`, measured 2026-10-05) is faster in 753 of 850 compared cases (88.6%), tied in 2 (0.2%) and slower in 95 (11.2%); a further 302 pairs have no verified number on one side and are excluded (counted below). Competitors: 9 configurations of 6 engines (libpcre2, oniguruma, re2, rust, tre, vectorscan). Match time, compile excluded.[^rate]

[^rate]: Win rate = wins / (wins + losses + ties) over all competitor × case pairs; a case is one (pattern, regime) cell where both engines produced a verified number; a tie is overlapping [min, max] trial ranges. Competitor records were measured 2026-09-17 to 2026-09-22, pcrec's on 2026-10-05, all on one machine (`budu-ryzen1600`).
<!-- frontpage:headline:end -->

<!-- frontpage:table:begin -->
| Competitor | Kind | Cases | pcrec wins | Losses | Ties | Median speedup | Geo-mean speedup | Excluded |
|---|---|--:|--:|--:|--:|--:|--:|---|
| PCRE2 10.46 DFA | DFA | 108 | 103 | 5 | 0 | ×4.93 | ×5.55 | 20 (pcrec side: 1 gave up, 4 unsupported or refused; engine side: 4 wrong answer, 1 gave up, 10 unsupported or refused) |
| PCRE2 10.46 interpreter | interpreter (backtracking) | 123 | 116 | 5 | 2 | ×4.70 | ×6.30 | 5 (pcrec side: 1 gave up, 4 unsupported or refused) |
| PCRE2 10.46 JIT | JIT | 123 | 100 | 23 | 0 | ×2.87 | ×2.74 | 5 (pcrec side: 1 gave up, 4 unsupported or refused) |
| Oniguruma 6.9.10 | interpreter (backtracking) | 121 | 118 | 3 | 0 | ×6.31 | ×10.2 | 7 (pcrec side: 1 gave up, 4 unsupported or refused; engine side: 2 unsupported or refused) |
| RE2 11.0.0 | automata (lazy DFA etc.) | 75 | 66 | 9 | 0 | ×8.62 | ×4.97 | 53 (pcrec side: 1 gave up, 4 unsupported or refused; engine side: 48 unsupported or refused) |
| RE2 11.0.0 (longest-match) | automata (lazy DFA etc.) | 72 | 63 | 9 | 0 | ×8.57 | ×4.82 | 56 (pcrec side: 1 gave up, 4 unsupported or refused; engine side: 3 wrong answer, 48 unsupported or refused) |
| Rust regex 1.13.1 | automata (lazy DFA etc.) | 78 | 61 | 17 | 0 | ×1.93 | ×1.33 | 50 (pcrec side: 1 gave up, 4 unsupported or refused; engine side: 1 wrong answer, 44 unsupported or refused) |
| TRE 0.9.0 | interpreter (POSIX matcher, backtracking fallback) | 73 | 72 | 1 | 0 | ×69.1 | ×265 | 55 (pcrec side: 1 gave up, 4 unsupported or refused; engine side: 8 wrong answer, 42 unsupported or refused) |
| Vectorscan 5.4.11 (no SOM) | automata (SIMD multi-pattern) | 77 | 54 | 23 | 0 | ×1.80 | ×0.849 | 51 (pcrec side: 1 gave up, 4 unsupported or refused; engine side: 46 unsupported or refused) |
| **all pairs** |  | 850 | 753 | 95 | 2 | ×4.45 | ×5.62 |  |

Speedup = competitor median ÷ pcrec median, per case (> 1 means pcrec is faster); the median and geometric mean run over all of that engine's cases, ties included. Excluded cases are counted, never dropped silently; a pair failing on both sides is attributed to the pcrec side.
<!-- frontpage:table:end -->

<!-- frontpage:chart:begin -->
![Per-case speedup of pcrec over each competitor, log scale](docs/img/speedup_distribution.svg)
<!-- frontpage:chart:end -->

Each dot is one case (a pattern in one regime). Right of the dashed 1× line pcrec is faster. The box spans the quartiles of that engine's cases and the thick bar is the median.

## Explore the full results

[**Results viewer**](https://fdicostanzo.github.io/pcrec-bench/) is a static page over every measured set, engine, pattern and regime in the store: pick engines and sets, choose a metric, and the matrix re-renders in the browser. Cell values come from the same reduction code that produced the tables on this page. The viewer is a reading aid; the records under `store/` are the canonical data.

## Where pcrec loses

Taken from the same comparison as the table above, worst first, with nothing filtered out. A cause is shown only where a committed ledger or notes file states one, quoted with its source; otherwise it says "cause not yet analysed".

<!-- frontpage:losses:begin -->
The 20 worst of 95 losing cases across all competitors (pcrec slower, trial ranges disjoint; "slower by" is pcrec median ÷ competitor median), grouped by pattern family; families ordered by their worst case. Vectorscan's `nosom` configuration reports only match or no match and its driver stops at the first match (testees/vectorscan/CLAUDE.md), so on a subject that matches it does less work than an engine that reports a span; read its rows with that in mind.

**semantics-divergence**

| Pattern | Regime | Engine | pcrec slower by | Why |
|---|---|---|--:|---|
| `wild-semdiv-empty-alt-repeat-pcre2` | large-subject-throughput | Vectorscan 5.4.11 (no SOM) | ×28,500 | cause not yet analysed |
| `keyword-prefix-order` | large-subject-throughput | Vectorscan 5.4.11 (no SOM) | ×2,370 | cause not yet analysed |
| `router-prefix-order` | large-subject-throughput | Vectorscan 5.4.11 (no SOM) | ×274 | cause not yet analysed |

**redos-nested**

| Pattern | Regime | Engine | pcrec slower by | Why |
|---|---|---|--:|---|
| `trim-nested-star` | short-subject-search | Vectorscan 5.4.11 (no SOM) | ×5,470 | cause not yet analysed |
| `trim-nested-star` | short-subject-search | Rust regex 1.13.1 | ×5,120 | cause not yet analysed |
| `trim-nested-star` | short-subject-search | RE2 11.0.0 | ×1,080 | cause not yet analysed |
| `trim-nested-star` | short-subject-search | RE2 11.0.0 (longest-match) | ×1,080 | cause not yet analysed |
| `trim-nested-star` | short-subject-search | PCRE2 10.46 DFA | ×747 | cause not yet analysed |
| `trim-nested-star` | short-subject-search | TRE 0.9.0 | ×524 | cause not yet analysed |
| `evil-alt-nested` | large-subject-throughput | Rust regex 1.13.1 | ×133 | cause not yet analysed |
| `evil-alt-nested` | large-subject-throughput | Vectorscan 5.4.11 (no SOM) | ×68.6 | cause not yet analysed |
| `evil-alt-nested` | large-subject-throughput | RE2 11.0.0 (longest-match) | ×37.6 | cause not yet analysed |
| `evil-alt-nested` | large-subject-throughput | RE2 11.0.0 | ×37.2 | cause not yet analysed |

**wild-codegrammar**

| Pattern | Regime | Engine | pcrec slower by | Why |
|---|---|---|--:|---|
| `wild-codegrammar-json-array-begin` | large-subject-throughput | Vectorscan 5.4.11 (no SOM) | ×1,760 | cause not yet analysed |
| `wild-codegrammar-json-constant` | large-subject-throughput | Vectorscan 5.4.11 (no SOM) | ×23.0 | cause not yet analysed |

**wild-secrets**

| Pattern | Regime | Engine | pcrec slower by | Why |
|---|---|---|--:|---|
| `wild-secrets-username-password-pair` | large-subject-throughput | PCRE2 10.46 interpreter | ×55.4 | cause not yet analysed |
| `wild-secrets-username-password-pair` | large-subject-throughput | PCRE2 10.46 DFA | ×55.3 | cause not yet analysed |
| `wild-secrets-aws-access-key-id` | large-subject-throughput | PCRE2 10.46 JIT | ×43.9 | cause not yet analysed |
| `wild-secrets-aws-access-key-id` | large-subject-throughput | Rust regex 1.13.1 | ×29.6 | cause not yet analysed |

**cap-backref**

| Pattern | Regime | Engine | pcrec slower by | Why |
|---|---|---|--:|---|
| `quoted-delim-match` | large-subject-throughput | PCRE2 10.46 JIT | ×21.5 | cause not yet analysed |

Losses by family, over every case:

| Family | Cases | Losses | Loss rate |
|---|--:|--:|--:|
| wild-secrets | 70 | 20 | 28.6% |
| cap-backref | 37 | 10 | 27.0% |
| wild-waf | 87 | 18 | 20.7% |
| semantics-divergence | 99 | 17 | 17.2% |
| redos-nested | 99 | 13 | 13.1% |
| cap-recursion | 31 | 3 | 9.7% |
| binary-nonutf8 | 38 | 3 | 7.9% |
| wild-codegrammar | 104 | 8 | 7.7% |
| cap-lookaround | 32 | 1 | 3.1% |
| wild-validator | 108 | 2 | 1.9% |
| wild-logparse | 109 | 0 | 0.0% |
| floor | 18 | 0 | 0.0% |
| wild-datetime | 18 | 0 | 0.0% |
<!-- frontpage:losses:end -->

## Second look: the other sets

The same metric, for the latest `pcrec-auto` record against each competitor's latest record on each other set in the store. Pin and date are shown per row because these records were not all measured in one window.

<!-- frontpage:othersets:begin -->
| Set | Competitor | pcrec-auto (pin, date) | Competitor date | Cases | Wins | Losses | Ties | Median speedup | Excluded |
|---|---|---|---|--:|--:|--:|--:|--:|---|
| `litrun@0.1` | PCRE2 10.46 JIT | c4c70f2c (2026-10-05) | 2026-09-28 | 28 | 19 | 8 | 1 | ×1.76 | 14 (pcrec side: 14 not measured) |

- `litrun@0.1`: competitors measured: libpcre2.
<!-- frontpage:othersets:end -->

## Methodology

Short version; the full text, with the engine, hardware and compile-cost tables, is in [docs/methodology.md](docs/methodology.md).

- **What is timed.** Match time and compile time are separate axes. The headline is match time with compile excluded. Compile cost is reported separately in [docs/methodology.md](docs/methodology.md#compile-cost), and for pcrec it is large because compiling runs a C compiler.
- **Cases.** One case is one pattern in one regime (short-subject search, large-subject throughput), reduced over every subject of that regime. The set-grain arithmetic is `pcrecbench/reduce.py`, shared with the reporter.
- **Trials.** Five trials per cell, median with min and max. A tie means the two engines' min-max trial ranges overlap. Records are produced only after a quiet-box pre-flight and a trial-agreement check.
- **Correctness.** Every expected answer comes from libpcre2 as the oracle. A cell where an engine answers wrongly, gives up, or does not support the pattern gets no number: it is left out of the comparison and counted in the Excluded column.
- **Semantics differ by engine.** RE2 in `longest` mode and TRE are leftmost-longest (TRE is POSIX), Vectorscan in its `nosom` configuration reports only match or no match. Their expectations and caveats are in the methodology page.

### Fairness

pcrec compiles a known pattern ahead of time, which is an inherent advantage when the pattern is fixed before the program runs; a runtime engine pays its compile cost at startup or per pattern. The like-for-like rows are the other engines that also compile a pattern into specialised code or automata before matching: libpcre2 with JIT, Vectorscan, RE2 and Rust `regex` (each builds its automata at runtime). The compile-time table in the methodology page shows what pcrec pays for its approach.

## Reproduce

```sh
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
python3 -m pcrecbench testees                                  # configured engines
python3 -m pcrecbench run --subbench capability --testee pcre2-jit --trials 5
python3 -m pcrecbench index
make frontpage      # regenerate this page's tables, chart and provenance from store/
make viewer-data    # regenerate the viewer's data files
```

Engine build prerequisites are listed by `make deps`. Every number on this page is listed with its source record in [docs/frontpage_provenance.tsv](docs/frontpage_provenance.tsv).

## Status

pcrec is at 0.2.0-beta; the pinned commit measured here is main after that tag, not a release. Optimization work on pcrec is ongoing and driven by this benchmark, so results change. This page shows the latest run only.

## How it was built

pcrec-bench was built by directed AI agents (Claude) as a sibling project of pcrec; see pcrec's [APPROACH.md](https://github.com/fdicostanzo/pcrec/blob/main/APPROACH.md). The design record is in [APPROACH.md](APPROACH.md) and `docs/`.

License: MIT ([LICENSE](LICENSE)).
