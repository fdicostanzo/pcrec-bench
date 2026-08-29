# bench/bounded/ — the bounded-repeat sub-bench (`bounded@0.1`)

WHAT IT IS FOR. Bounded repeats on BOTH axes (plan row [B11.4]): what an
engine pays to COMPILE a counted repeat as the count grows, nests and changes
body — through to the count at which it refuses, a first-class outcome and
the number the count ladder exists to locate — and what it pays to MATCH the
everyday bounded shapes (a 4-digit year, a 32-hex id, `.{8,64}`, `.{80,}`, a
dotted quad, a CSV record) and the hazard-band ones (a bounded lazy gap
before a `\b` alternation, at three counts; an ambiguous nest) on subjects
that match, that fail at the LAST repetition, and that over-run the count
and fail only at the end anchor. The compile-side columns are the design
input pcrec's [ART-SIZE] size term asked for (inbox I-15 (c), I-17); the
`ctx-*` ladder is the [SEL-1] witness's shape at three counts; the class
ladder brackets [ENG-COUNT]'s `[a-z]{0,30000}`.

**Read `NOTES.md` first** — the objective, the pattern table with purpose
and m/n, the ladder and the PREDICTED first refusal per engine (stated from
pcrec's published caps so the window can confirm or refute), the oracle's
own edge, why the subjects stop at the lengths they do, the floor, and the
cell-time estimate with what was cut.

WHERE IT CAME FROM. Nothing is copied. Authored from the GOAL by an author
blinded to pcrec's `tests/`, `src/` and corpora and to this repo's
`testees/`, `store/` and `reports/` ([B11.4]'s brief, pcrec's D27
discipline): only pcrec's `docs/spec/` was read. The subjects are generated
here.

| file | role |
|---|---|
| `subbench.toml` | the SIDECAR: fields only, no grammar ([DD-13] untouched). Declares `match` + `search_short` + `throughput` and `short_search_max_bytes = 512` |
| `patterns/*.rx` | the 23 members + `floor.rx`, raw bytes, no trailing newline. Every group is `(?:…)`: no capture participates anywhere |
| `boundedtext.py` | the subject GRAMMAR both generators draw from: `Rng` (the one randomness primitive), the near-miss ops vocabulary, the everyday shapes; re-exports `pcrecbench.periodic` |
| `gen_subjects.py` | writes `subjects/` (gitignored) + `manifest.tsv`: 13 fields + 8 lines + 9 runs, 3-257 B, seed 20260829; shapes ALLOCATED exactly over the pool lines; `nonperiodic()` draws every subject until the `periodic` column reads `no` |
| `gen_throughput_subjects.py` | writes `throughput/` (gitignored) + `manifest_throughput.tsv`: the four LARGE runs (4 KB / 16 KB / 64 KB letters, 16 KB digits), seed 20260830 — the ladder's top rungs under find-all, NOT a size sweep |
| `manifest.tsv`, `manifest_throughput.tsv` | committed: id, len, sha256, description (family and ARM in a fixed spelling: `field/near-miss`, `line/ctx-gap-160`, `run/digits` …), **periodic** (`no` on all 34) |
| `gen_expectations.py` | the entry point; the derivation is shared (`pcrecbench/expectations.py`). `--check` re-derives and diffs |
| `expectations.tsv` | 1536 rows: 24 patterns × (30 match + 30 search_short + 4 throughput) |
| `gen_pattern_facts.py` | derives `pattern_facts.tsv`: the COUNT facts from the pattern text (max count, nesting depth, count product, lazy) + PCRE2's own analysis (first / required code unit, min length) + m/n per regime |
| `pattern_facts.tsv` | one row per pattern; the table NOTES.md's pattern tables are read from |
| `gen_oracle_limits.py` | probes each ladder skeleton BEYOND the set's rungs on the oracle (compile only, doubling) and derives `oracle_limits.tsv` |
| `oracle_limits.tsv` | per skeleton: the rungs probed, the last the oracle accepted, the first it refused, its diagnostic verbatim — PCRE2's count ceiling (65535) and its compiled-size ceiling on replicated groups (`grp-upto` 2048, `nest2` 4096, `nest3` 96) |
| `NOTES.md` | the objective, the tables, the predictions, the engine notes, the cell-time estimate |

REGENERATING. `python3 bench/bounded/gen_subjects.py`,
`gen_throughput_subjects.py`, `gen_expectations.py`, `gen_pattern_facts.py`,
`gen_oracle_limits.py`. All five are deterministic; `make check` runs the
first two and re-derives the last three in `--check` mode, over every
sub-bench under `bench/` by enumeration (`tools/selfcheck.py:subbench_dirs`),
and fails on any drift. The whole derivation runs in well under a second:
every cell is one the oracle FINISHES (below).

THREE THINGS A FUTURE EDITOR SHOULD NOT UNDO WITHOUT READING WHY (all in
`NOTES.md`, all measured on the oracle or on the harness's own arithmetic):

1. **The digit runs stop at 256 and the letters nest is `{1,6}`.** A
   near-miss LONGER than a nested rung's maximum is catastrophic for a
   backtracker: `(?:\d{1,16}){1,16}` on 257 digits exhausts the oracle's
   match limit, and an expectation the oracle cannot state is a cell the
   harness cannot judge. Every near-miss in the set is one the oracle
   finishes in milliseconds ("The runs and the oracle").
2. **The large runs are a `throughput` regime, not `match` subjects.** The
   harness calibrates on the MEDIAN subject and caps a trial at 20 s; a
   16 KB run beside a 36 B median puts every length-proportional pattern's
   match trial on the cap (the first cut: 13 patterns × 5 trials × 20 s).
   Under find-all search the same runs drive every counter to its full
   value at ≈ 0.3 s a trial ("Regimes"; `gen_throughput_subjects.py`).
3. **The lines are ≤ 256 B and the two whole ctx lines and the gap line are
   outside the shape-allocation pool.** The band keeps the search regime's
   Σ/median inside what the batched loop tolerates; an injected token would
   break "ends with the context word" on the whole lines and pushed the gap
   line past 256 B (cutting its context word off) when it was in the pool.

BUMPING THE VERSION is a deliberate, logged event (requirements §5): any
change to a pattern, a subject, or an expectation makes existing records
incomparable, so `version` in `subbench.toml` goes up in the same commit and
the reason goes in the journal. A change to `boundedtext.py` changes BOTH
subject trees.
