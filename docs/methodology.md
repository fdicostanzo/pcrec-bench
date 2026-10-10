# Methodology

How the numbers on the [front page](../README.md) are produced. Tables marked generated are written by `tools/frontpage.py` from the records in `store/`; every record used is listed in [frontpage_provenance.tsv](frontpage_provenance.tsv).

## Excluded cases by side and reason

The front-page table shows one count per competitor in its Excluded column; this is the breakdown.

<!-- frontpage:excluded:begin -->
| Competitor | Excluded | pcrec side | Engine side |
|---|--:|---|---|
| PCRE2 10.46 JIT | 8 | 4 unsupported or refused, 1 no oracle expectation to judge against | 3 gave up |
| RE2 11.0.0 | 58 | 4 unsupported or refused, 1 no oracle expectation to judge against | 3 wrong answer, 50 unsupported or refused |
| RE2 11.0.0 (longest-match) | 61 | 4 unsupported or refused, 1 no oracle expectation to judge against | 6 wrong answer, 50 unsupported or refused |
| Rust regex 1.13.1 | 52 | 4 unsupported or refused, 1 no oracle expectation to judge against | 3 wrong answer, 44 unsupported or refused |
| Vectorscan 5.4.11 (SOM) | 60 | 4 unsupported or refused, 1 no oracle expectation to judge against | 3 wrong answer, 52 unsupported or refused |
| Vectorscan 5.4.11 (no SOM) | 51 | 4 unsupported or refused, 1 no oracle expectation to judge against | 46 unsupported or refused |
| PCRE2 10.46 interpreter | 8 | 4 unsupported or refused, 1 no oracle expectation to judge against | 3 gave up |
| PCRE2 10.46 DFA | 23 | 4 unsupported or refused, 1 no oracle expectation to judge against | 4 wrong answer, 12 unsupported or refused, 2 not measured |
| Oniguruma 6.9.10 | 11 | 4 unsupported or refused, 1 no oracle expectation to judge against | 4 gave up, 2 unsupported or refused |
| TRE 0.9.0 | 69 | 4 unsupported or refused, 1 no oracle expectation to judge against | 7 wrong answer, 56 unsupported or refused, 1 not measured |

A pair is excluded when one side has no verified number; it is attributed to the pcrec side first, else to the engine's. "Unsupported or refused" covers a pattern the engine does not support or declined to compile.
<!-- frontpage:excluded:end -->

## Hardware and software

<!-- frontpage:env:begin -->
| Item | Value (from the records' `environment` blocks) |
|---|---|
| Machine | `budu-ryzen1600` (ubuntubudu) |
| CPU | AMD Ryzen 5 1600 Six-Core Processor, 12 hardware threads |
| Kernel | Linux 7.0.0-29-generic |
| Compiler for drivers and for pcrec's emitted C | gcc (Ubuntu 15.2.0-16ubuntu1) 15.2.0 |
| Governor / turbo | schedutil / enabled |
| Timed process pinning | taskset cpu 11 |
| Quiet-box pre-flight verdict | quiet |
<!-- frontpage:env:end -->

## Engines

Kind and match semantics are the records' own `testee` fields. Per-engine adapter notes: `testees/<engine>/CLAUDE.md`.

<!-- frontpage:engines:begin -->
| Engine | Testee | Version | Mode | Compile-cost class | Automaton class | Match semantics | Captures | Measured | Trial agreement |
|---|---|---|---|---|---|---|---|---|---|
| pcrec 0.2.0-beta+255bcdd8 | `pcrec_255bcdd8_auto-caps-simdna` | 255bcdd8 | auto | compiled-aot | hybrid | perl-leftmost-first | on | 2026-10-08 | agree |
| PCRE2 10.46 DFA | `libpcre2_10.46_dfa-nocaps-simdna` | 10.46 | dfa | interpretive | nfa-simulation | perl-leftmost-first | off | 2026-10-08 | agree |
| PCRE2 10.46 interpreter | `libpcre2_10.46_interp-caps-simdna` | 10.46 | interp | interpretive | backtracking | perl-leftmost-first | on | 2026-10-08 | agree |
| PCRE2 10.46 JIT | `libpcre2_10.46_jit-caps-simdna` | 10.46 | jit | eager-jit | backtracking | perl-leftmost-first | on | 2026-10-08 | agree |
| Oniguruma 6.9.10 | `oniguruma_6.9.10_default-caps-simdna` | 6.9.10 | default | interpretive | backtracking | perl-leftmost-first | on | 2026-10-09 | agree |
| RE2 11.0.0 | `re2_11.0.0_default-caps-simdna` | 11.0.0 | default | eager-jit | nfa-simulation | perl-leftmost-first | on | 2026-10-09 | agree |
| RE2 11.0.0 (longest-match) | `re2_11.0.0_longest-caps-simdna` | 11.0.0 | longest | eager-jit | nfa-simulation | posix-leftmost-longest | on | 2026-10-09 | agree |
| Rust regex 1.13.1 | `rust_1.13.1_default-caps-simdna` | 1.13.1 | default | eager-jit | nfa-simulation | perl-leftmost-first | on | 2026-10-09 | agree |
| TRE 0.9.0 | `tre_0.9.0_default-caps-simdna` | 0.9.0 | default | interpretive | hybrid | posix-leftmost-longest | on | 2026-10-09 | agree |
| Vectorscan 5.4.11 (no SOM) | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 5.4.11 | block-nosom | eager-jit | simd-multipattern | all-ends | off | 2026-10-09 | agree |
| Vectorscan 5.4.11 (SOM) | `vectorscan_5.4.11_block-som-nocaps-simd` | 5.4.11 | block-som | eager-jit | simd-multipattern | all-ends | off | 2026-10-09 | agree |

Compile-cost class is the record's `execution_model` field: WHEN the engine builds its matcher, not how. `eager-jit` means the matcher is built in full at compile time; only PCRE2 JIT emits machine code at runtime, while RE2, Rust regex and Vectorscan build automata. `compiled-aot` means the matcher is C source compiled before the program runs.
<!-- frontpage:engines:end -->

Semantic caveats that affect what a "match" means:

- `re2 ... (longest)` runs RE2 with `set_longest_match(true)`: POSIX leftmost-longest, unlike the other engines' leftmost-first. Where the two differ the oracle's expectation is leftmost-first, so the cell is a wrong answer and is excluded (testees/re2/CLAUDE.md).
- `tre` implements POSIX leftmost-longest and a different syntax from PCRE; features it lacks make the pattern unsupported (testees/tre/CLAUDE.md).
- `vectorscan ... (block-nosom)` reports only whether a match exists (boolean grain); it never reports a span or a match count, and is scored on match versus no match. Its driver stops scanning at the first match (testees/vectorscan/CLAUDE.md), so on a subject that matches it does less work than an engine that reports a span.
- `libpcre2 ... (dfa)` is PCRE2's DFA matcher, an NFA simulation without backtracking and without captures.
- Rust `regex` and RE2 guarantee linear-time matching and have no backreferences or lookaround; patterns needing them are unsupported there.

## What is timed

Compile and match are separate axes in every record. The front-page headline uses match time only, with compile excluded: the question it answers is how fast an already-built matcher runs. That is fair to the extent that the engines are used the same way, with a pattern built once and reused for many matches; it is unfair to pcrec when a pattern is used once, since pcrec's build step runs a C compiler, and it is unfair to the runtime engines in that they pay their build cost on every program start while pcrec pays it at build time. Both views are reported; the compile table is below.

A cell's number is the sum over all subjects of the regime of the per-subject time per call, taken per trial; the cell reports the median over trials with min and max. Each subject's iteration count is calibrated per engine toward a fixed timed-work target so engines with very different speeds are timed over comparable durations.

**Warm-up.** Each trial compiles the pattern once, then times a loop of repeated calls to the same compiled matcher, so an engine's match-time caches stay warm across calls. RE2 and Rust `regex` build part of their automaton lazily on the first call, and that first call falls inside the timed loop. We tested whether an untimed priming call per subject changes any result, applying it symmetrically to every engine. On a 10-pattern sample, re-measured primed and unprimed back to back, no win/loss/tie classification changed. The one measurable effect was on three RE2 large-subject cells where RE2 already leads pcrec by orders of magnitude; there priming made RE2 faster, and a repeated unprimed run confirmed it as warming rather than drift. pcrec, which has nothing to warm, did not move. The published numbers are unprimed. Measurements and scripts: [docs/dev/measurements/2026-10-09-b129-prime-sample.txt](dev/measurements/2026-10-09-b129-prime-sample.txt).

**The timed loop.** Everything between a subject's two clock reads lives in one small function per driver (`timed_run`), compiled in its own translation unit, never inlined, and aligned to a 64-byte boundary (Rust: its own crate, section-aligned). We did this because adding unrelated stamp-reading lines to a driver's `main()` once moved short-call timings by 10-17% (about 40-50 ns per call) on programs that were byte-for-byte identical, a bench-side shift that had been read as an engine regression. A proof script adds forty dummy lines to each driver and checks that the timed function's instruction stream is unchanged and still 64-byte aligned, and a small fixed set of short-call cells is timed first in every measurement window beside pcre2-jit, so a shift in the instrument shows up as a shift there with the control flat. Records written before and after the change are told apart by the harness commit they carry. Details: [docs/dev/decisions.md](dev/decisions.md) BD16.

<!-- frontpage:trials:begin -->
Trials per cell in these records: 5. Per-row calibration target (ns of timed work per trial): 50000000. Trial-agreement rule in these records: v1.4-group (k=1.5, d_min=2, share_c=3).
<!-- frontpage:trials:end -->

### Compile cost

<!-- frontpage:compile:begin -->
| Engine | Cost class | Patterns compiled | Median compile cost | pcrec compile ÷ this engine (median over common patterns) |
|---|---|--:|--:|--:|
| pcrec 0.2.0-beta+255bcdd8 | compiled-aot | 69 | 224 ms | — |
| PCRE2 10.46 DFA | interpretive | 65 | 2.04 µs | ×111,000 |
| PCRE2 10.46 interpreter | interpretive | 71 | 2.45 µs | ×101,000 |
| PCRE2 10.46 JIT | eager-jit | 71 | 16.7 µs | ×13,100 |
| Oniguruma 6.9.10 | interpretive | 69 | 6.03 µs | ×38,300 |
| RE2 11.0.0 | eager-jit | 45 | 21.7 µs | ×10,500 |
| RE2 11.0.0 (longest-match) | eager-jit | 45 | 23.2 µs | ×10,800 |
| Rust regex 1.13.1 | eager-jit | 48 | 105 µs | ×2,710 |
| TRE 0.9.0 | interpretive | 41 | 10.8 µs | ×20,200 |
| Vectorscan 5.4.11 (no SOM) | eager-jit | 47 | 660 µs | ×327 |
| Vectorscan 5.4.11 (SOM) | eager-jit | 44 | 743 µs | ×251 |

Median over patterns of each pattern's median `cost.total_ns` across trials, plain form, compile rows only. A ratio above ×1 means pcrec's compile is slower. pcrec's figure includes the C compiler run that turns the emitted source into a loadable object.
<!-- frontpage:compile:end -->

## Sets and corpus provenance

The headline set is `bench/capability`: patterns taken from real deployed regexes where a permissively licensed source could be fetched (OWASP validation repository and CRS ruleset, Elastic grok patterns, rebar corpora, VS Code grammar, PCRE2 and rust-regex test corpora) and authored fresh under the same realism rule where none exists. Each pattern's source, license, retrieval date and fidelity (verbatim or adapted) is in `bench/capability/provenance.tsv`; the design is in `bench/capability/NOTES.md` and `docs/design/capability_set_v1.md`. The other sets (`email-specimen`, `loglines`, `bounded`, `altwide`, `syntax`, `utf8`, `litrun`) are described in their own `bench/<set>/NOTES.md`.

## Quiet-box pre-flight and trial agreement

A pinned run is refused unless the box is quiet (load average and per-core occupancy, including the timed core, judged before the run). Each cell runs five trials, interleaved. After the run a trial-agreement rule decides whether the five trials agree; a record whose trials do not agree is stored as `inconclusive-spread` and is not used here. The rule and its constants are in `docs/design/gate_shape_v14.md`; the harness is specified in `docs/design/harness_contract.md`. The timed process is pinned to one core.

## Correctness

Every expected answer (match or no match, span, captures) is computed by libpcre2 as the oracle; the method used for each expectation is recorded with it (`docs/design/expectation_methods_v1.md`). A cell is scored `matched-as-expected` only if the engine's answer equals the expectation. A wrong answer, a give-up (the engine hit its own limit), or an unsupported or refused pattern leaves the cell without a number. Such cells are excluded from the speedup statistics and counted in the Excluded column of the front-page table by side and reason; they are never dropped silently.

## Statistics

Speedup = competitor median ÷ pcrec median per case. A tie is overlapping closed [min, max] trial ranges. The median and geometric mean are over the cases where both engines have a number. Ratios are printed to three significant digits, rounding half to even.
