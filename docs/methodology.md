# Methodology

How the numbers on the [front page](../README.md) are produced. Tables marked generated are written by `tools/frontpage.py` from the records in `store/`; every record used is listed in [frontpage_provenance.tsv](frontpage_provenance.tsv).

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
| Engine | Testee | Version | Mode | Execution model | Automaton class | Match semantics | Captures | Measured | Trial agreement |
|---|---|---|---|---|---|---|---|---|---|
| pcrec 0.2.0-beta+c4c70f2c | `pcrec_c4c70f2c_auto-caps-simdna` | c4c70f2c | auto | compiled-aot | hybrid | perl-leftmost-first | on | 2026-10-05 | agree |
| PCRE2 10.46 DFA | `libpcre2_10.46_dfa-nocaps-simdna` | 10.46 | dfa | interpretive | nfa-simulation | perl-leftmost-first | off | 2026-09-17 | agree |
| PCRE2 10.46 interpreter | `libpcre2_10.46_interp-caps-simdna` | 10.46 | interp | interpretive | backtracking | perl-leftmost-first | on | 2026-09-17 | agree |
| PCRE2 10.46 JIT | `libpcre2_10.46_jit-caps-simdna` | 10.46 | jit | eager-jit | backtracking | perl-leftmost-first | on | 2026-09-17 | agree |
| Oniguruma 6.9.10 | `oniguruma_6.9.10_default-caps-simdna` | 6.9.10 | default | interpretive | backtracking | perl-leftmost-first | on | 2026-09-22 | agree |
| RE2 11.0.0 | `re2_11.0.0_default-caps-simdna` | 11.0.0 | default | eager-jit | nfa-simulation | perl-leftmost-first | on | 2026-09-19 | agree |
| RE2 11.0.0 (longest-match) | `re2_11.0.0_longest-caps-simdna` | 11.0.0 | longest | eager-jit | nfa-simulation | posix-leftmost-longest | on | 2026-09-18 | agree |
| Rust regex 1.13.1 | `rust_1.13.1_default-caps-simdna` | 1.13.1 | default | eager-jit | nfa-simulation | perl-leftmost-first | on | 2026-09-22 | agree |
| TRE 0.9.0 | `tre_0.9.0_default-caps-simdna` | 0.9.0 | default | interpretive | hybrid | posix-leftmost-longest | on | 2026-09-19 | agree |
| Vectorscan 5.4.11 (no SOM) | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 5.4.11 | block-nosom | eager-jit | simd-multipattern | all-ends | off | 2026-09-22 | agree |
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

<!-- frontpage:trials:begin -->
Trials per cell in these records: 5. Per-row calibration target (ns of timed work per trial): 50000000. Trial-agreement rule in these records: v1.4-group (k=1.5, d_min=2, share_c=3).
<!-- frontpage:trials:end -->

### Compile cost

<!-- frontpage:compile:begin -->
| Engine | Cost class | Patterns compiled | Median compile cost | pcrec compile ÷ this engine (median over common patterns) |
|---|---|--:|--:|--:|
| pcrec 0.2.0-beta+c4c70f2c | compiled-aot | 62 | 224 ms | — |
| PCRE2 10.46 DFA | interpretive | 59 | 2.68 µs | ×78400 |
| PCRE2 10.46 interpreter | interpretive | 64 | 3.20 µs | ×72600 |
| PCRE2 10.46 JIT | eager-jit | 64 | 19.8 µs | ×10400 |
| Oniguruma 6.9.10 | interpretive | 62 | 6.94 µs | ×28400 |
| RE2 11.0.0 | eager-jit | 39 | 22.2 µs | ×9750 |
| RE2 11.0.0 (longest-match) | eager-jit | 39 | 18.9 µs | ×9890 |
| Rust regex 1.13.1 | eager-jit | 41 | 107 µs | ×2290 |
| TRE 0.9.0 | interpretive | 41 | 18.1 µs | ×9750 |
| Vectorscan 5.4.11 (no SOM) | eager-jit | 40 | 1.07 ms | ×242 |

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
