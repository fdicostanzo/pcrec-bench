# bench/bounded/ — the bounded-repeat sub-bench (`bounded@0.3`)

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
ladder brackets [ENG-COUNT]'s `[a-z]{0,30000}`. 0.2 ([B21]) filled the
class ladder to ELEVEN factor-of-2 rungs (64..65535, the KNEE-bracketing
ladder), made `[a-z]{0,1024}` the group-vs-class pair with `grp-upto-1024`
(same count, same language, body representation the only difference), and
added the 4 KB digits run so both content axes have a small and a large
throughput subject; every 0.1 pattern and subject is byte-identical, and
0.1/0.2 records never pool (NOTES.md, "What 0.2 added").

0.3 ([B27], inbox I-29 asks (ii)/(iv)) made the set an ACCEPTANCE
INSTRUMENT for pcrec's [OPT-5] STEP 2 (the two-pass `_match` elision) and a
BOUNDARY INSTRUMENT for its per-run scan-edge selection. Three additions,
one version bump: (1) MATCH-REGIME cells where the elision must show —
letters runs at 4 / 8 / 16 / 32 / 64 / 128 / 512 / 1024, one per class-ladder
rung, so every rung has a whole-subject match and the rungs at 1024 and above
have a TWELVE-POINT length sweep from which a per-byte slope and a per-call
intercept separate; the mechanism is `short_search_max_bytes` 512 → 258 (a
number that moves no 0.2 subject) plus the fact that `subjects_for()` filters
only the search band, so a run over the cap is MATCH-ONLY with no new regime
and no schema change. (2) the LOW RUNGS `cls-upto-4/8/16/32` and the
SHORT-RUN DIGIT FAMILY `dig-exact-{2,8,16,32}` / `dig-upto-{2,4,8,16,32}`
(`year4` is the family's 4-rung, byte for byte) over one digit LENGTH LADDER
1 … 33 that gives every rung an exact match, a near-miss one short and an
over-run. (3) the predictions those instruments are read against, written
before the first sample. Every 0.2 pattern, subject and expectation is
byte-identical, and 0.2/0.3 records never pool (NOTES.md, "What 0.3 added" —
read it before touching a length or a rung; it also carries the same-pin
control that tests the two-pass account without a second pin).

**Read `NOTES.md` first** — the objective, the pattern table with purpose
and m/n, the ladder and the PREDICTED first refusal per engine (stated from
pcrec's published caps so the window can confirm or refute), the oracle's
own edge, why the subjects stop at the lengths they do, the floor, and the
cell-time estimate with what was cut.

WHERE IT CAME FROM. Nothing is copied. Authored from the GOAL by an author
blinded to pcrec's `tests/`, `src/` and corpora and to this repo's
`testees/`, `store/` and `reports/` ([B11.4]'s brief, pcrec's D27
discipline): only pcrec's `docs/spec/` was read. The subjects are generated
here. 0.2 and 0.3 kept that discipline for the SET's shape but not for its
predictions: both extend a measured set against measured ledgers, and 0.3's
predictions cite the [OPT-5] acceptance ledger and the hybrid-gained-edge
census by name (NOTES.md, "Origin").

| file | role |
|---|---|
| `subbench.toml` | the SIDECAR: fields only, no grammar ([DD-13] untouched). Declares `match` + `search_short` + `throughput` and `short_search_max_bytes = 258` (0.3; 512 through 0.2, same membership — the cap is now also what makes a long run MATCH-ONLY) |
| `patterns/*.rx` | the 42 members + `floor.rx`, raw bytes, no trailing newline. Every group is `(?:…)`: no capture participates anywhere |
| `boundedtext.py` | the subject GRAMMAR both generators draw from: `Rng` (the one randomness primitive), the near-miss ops vocabulary, the everyday shapes; re-exports `pcrecbench.periodic` |
| `gen_subjects.py` | writes `subjects/` (gitignored) + `manifest.tsv`: 13 fields + 8 lines + 28 runs (9 from 0.2, 19 appended LAST by 0.3's `runs_0_3()` so the 0.2 draws reproduce), 1-1024 B, seed 20260829; shapes ALLOCATED exactly over the pool lines; `nonperiodic()` draws every subject until the `periodic` column reads `no` |
| `gen_throughput_subjects.py` | writes `throughput/` (gitignored) + `manifest_throughput.tsv`: the five LARGE runs (4 / 16 / 64 KB letters, 4 / 16 KB digits; `t-digits-004k` appended LAST so the four 0.1 draws reproduce byte for byte), seed 20260830 — the ladder's top rungs under find-all, NOT a size sweep |
| `manifest.tsv`, `manifest_throughput.tsv` | committed: id, len, sha256, description (family and ARM in a fixed spelling: `field/near-miss`, `line/ctx-gap-160`, `run/digits` …), **periodic** (`no` on all 54) |
| `gen_expectations.py` | the entry point; the derivation is shared (`pcrecbench/expectations.py`). `--check` re-derives and diffs |
| `expectations.tsv` | 4300 rows: 43 patterns × (49 match + 46 search_short + 5 throughput) |
| `gen_pattern_facts.py` | derives `pattern_facts.tsv`: the COUNT facts from the pattern text (max count, nesting depth, count product, lazy) + PCRE2's own analysis (first / required code unit, min length) + m/n per regime |
| `pattern_facts.tsv` | one row per pattern; the table NOTES.md's pattern tables are read from |
| `gen_oracle_limits.py` | probes each ladder skeleton BEYOND the set's rungs on the oracle (compile only, doubling) and derives `oracle_limits.tsv` |
| `oracle_limits.tsv` | 10 skeletons (0.3 added `dig-exact` and `dig-upto`): the rungs probed, the last the oracle accepted, the first it refused, its diagnostic verbatim — PCRE2's count ceiling (65535, which every single-unit repeat reaches, the two digit skeletons included) and its compiled-size ceiling on replicated groups (`grp-upto` 2048, `nest2` 4096, `nest3` 96) |
| `NOTES.md` | the objective, the tables, the predictions, the engine notes, the cell-time estimate |

REGENERATING. `python3 bench/bounded/gen_subjects.py`,
`gen_throughput_subjects.py`, `gen_expectations.py`, `gen_pattern_facts.py`,
`gen_oracle_limits.py`. All five are deterministic; `make check` runs the
first two and re-derives the last three in `--check` mode, over every
sub-bench under `bench/` by enumeration (`tools/selfcheck.py:subbench_dirs`),
and fails on any drift. The whole derivation runs in well under a second:
every cell is one the oracle FINISHES (below).

FOUR THINGS A FUTURE EDITOR SHOULD NOT UNDO WITHOUT READING WHY (all in
`NOTES.md`, all measured on the oracle or on the harness's own arithmetic):

1. **The digit runs stop where the ambiguous nests still finish, and the
   letters nest is `{1,6}`.** A near-miss LONGER than a nested rung's maximum
   is catastrophic for a backtracker: `(?:\d{1,16}){1,16}` on 257 digits
   exhausts the oracle's match limit, and an expectation the oracle cannot
   state is a cell the harness cannot judge. 0.2 read this as "stop at 256".
   0.3 states the RULE it stands for: both large nests have count product
   **4096**, so a digit run of 1024 is a greedy first-try MATCH and costs
   time linear in its length, while **4097** would be the catastrophic
   near-miss. 0.3's longest digit run is therefore 1024 — an octave short of
   the cliff, not beside it. Every near-miss in the set is one the oracle
   finishes in milliseconds ("The runs and the oracle").
2. **The 4 KB+ runs are a `throughput` regime, not `match` subjects — and
   1024 B is where the match side stops.** The harness calibrates on the
   MEDIAN subject and caps a trial at 20 s; a 16 KB run beside a 36 B median
   puts every length-proportional pattern's match trial on the cap (the first
   cut: 13 patterns × 5 trials × 20 s, Σ/median ≈ 570). 0.3 DOES put long
   runs in `match`, deliberately and in the same arithmetic: its whole added
   set is Σ/median ≈ 50, ≈ 2.5 s a trial, one eighth of the cap. Raising the
   top of that ladder is what would break this, and "What 0.3 added" carries
   the arithmetic to redo before anyone does.
3. **The lines are ≤ 256 B and the two whole ctx lines and the gap line are
   outside the shape-allocation pool.** The band keeps the search regime's
   Σ/median inside what the batched loop tolerates; an injected token would
   break "ends with the context word" on the whole lines and pushed the gap
   line past 256 B (cutting its context word off) when it was in the pool.
4. **`short_search_max_bytes = 258` is load-bearing twice.** It admits the
   257-byte over-run of the 256 rung (0.2's reason for 512) AND it is the
   only thing that makes 0.3's long runs match-only: `subjects_for()` filters
   `search_short` by this number and does NOT filter `match`. Raising it
   would silently put 512 B and 1024 B runs into the search band on every one
   of 43 patterns; lowering it below 258 would drop `r-00257`.

BUMPING THE VERSION is a deliberate, logged event (requirements §5): any
change to a pattern, a subject, or an expectation makes existing records
incomparable, so `version` in `subbench.toml` goes up in the same commit and
the reason goes in the journal. A change to `boundedtext.py` changes BOTH
subject trees.
