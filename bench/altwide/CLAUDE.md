# bench/altwide/ — the wide-alternation sub-bench (`altwide@0.2`)

WHAT IT IS FOR. Alternations of MANY literal branches, on both axes (plan
row [B11.2]): what an engine pays to COMPILE one as the branch count grows —
through to the width at which it refuses, a first-class outcome and the
number the width ladder exists to locate — and what it pays to SEARCH
mostly-failing prose with one, as the STRUCTURE that decides a start-of-match
optimization changes underneath it. This is the shape where a backtracker's
leftmost-first trial order, PCRE2's first-code-unit / required-code-unit
dismissal and an AOT compiler's DFA-or-prefilter route diverge most, and
where a 4096-way alternation becomes a compile-SIZE question for anything
that lowers a branch to a node. Two things only a leftmost-first engine pays
for are crossed in on purpose: which branch INDEX carries the hit, and what
ORDER the branches are written in.

**Read `NOTES.md` first** — the objective, the pattern table with each arm's
purpose and realised structure, what the ladder brackets and why the rungs
sit where they do, the predictions stated from pcrec's `docs/spec/` before
anything ran, the oracle's own width ceiling and what it forced, the floor,
and the cell-time estimate with what was cut.

WHERE IT CAME FROM. Nothing is copied. Authored from the GOAL by an author
blinded to pcrec's `tests/`, `src/` and corpora and to this repo's
`testees/`, `store/`, `reports/` and pcrec-facing ledgers ([B11.2]'s brief,
pcrec's D27 discipline): only pcrec's `docs/spec/` was read. Every branch
literal and every subject byte is generated here.

**0.2** ([B31], 2026-09-02) EXTENDED it: thirteen patterns (the dense ladder
`w-96`/`-128`/`-192`/`-384`, the seven arms twinned at the 256 anchor, and
the short-pool rungs `s-256`/`s-512`) and two subjects (`f-s255`,
`l-s255-mid`). Every 0.1 pattern keeps its exact bytes, every 0.1 subject
reproduces byte for byte (the new carriers are drawn LAST, so the 0.1 rng
draws are an unchanged stream prefix), and all 1600 0.1 expectation rows are
byte-identical among 0.2's 2772. The reason is measured: at pcrec pin
1989c62 every 0.1 pattern at width ≥ 512 is REFUSED at one of pcrec's two
emitted-size caps, so twelve of twenty were unmeasurable there and the whole
ladder had three points below the refusal. 0.2's author kept 0.1's pcrec
blinding but was handed five measured facts, which NOTES.md names one by one
("How blind this author was").

| file | role |
|---|---|
| `subbench.toml` | the SIDECAR: fields only, no grammar ([DD-13] untouched). Declares `match` + `search_short` + `throughput` and `short_search_max_bytes = 512` |
| `altwidetext.py` | the GRAMMAR every generator draws from: `Rng` (the one randomness primitive), the six branch word POOLS and the four properties they hold (distinct, globally SUBSTRING-free, nested, first bytes per the arm), the branch-free background guard, `BranchIndex` (substring search for any branch, used as the guard AND as the per-subject assertion); re-exports `pcrecbench.periodic` |
| `gen_patterns.py` | writes `patterns/*.rx` — the thirty-three patterns are DERIVED, not typed, because `w-2048` is 17 KB and `s-4096` is 24 KB of alternation. `SPECS` is the set: (name, pool, width, wrapper). `--check` re-derives and diffs |
| `patterns/*.rx` | the 32 members + `floor.rx`, raw bytes, no trailing newline, committed. Every group is `(?:…)`: no capture participates anywhere |
| `gen_subjects.py` | writes `subjects/` (gitignored) + `manifest.tsv`: 18 fields + 22 lines, 4-244 B, seed 20260901. Each carrying line's occurrence list is ASSERTED to be exactly the one branch the file placed. `extras()` holds 0.2's two carriers and is called LAST, which is what keeps every 0.1 subject byte-identical |
| `gen_throughput_subjects.py` | writes `throughput/` (gitignored) + `manifest_throughput.tsv`: four prose subjects crossing hit DENSITY (0 / 1 per 8 KB / 1 per 128 B) with SIZE (128 KB, 512 KB), seed 20260902; the planted occurrences are exact, not expected, and re-asserted per subject |
| `manifest.tsv`, `manifest_throughput.tsv` | committed: id, len, sha256, description (family and ARM in a fixed spelling: `field/hit`, `field/near-miss`, `line/carry-early`, `line/background`, `run/prose`), **periodic** (`no` on all 42) |
| `gen_expectations.py` | the entry point; the derivation is shared (`pcrecbench/expectations.py`). `--check` re-derives and diffs |
| `expectations.tsv` | 2772 rows: 33 patterns × (40 match + 40 search_short + 4 throughput). The 1600 rows of 0.1 are all present byte-identically, checked triple by triple — 0.2's two subjects interleave rows into every pattern's block, so the file extends by ROW, not by line |
| `gen_pattern_facts.py` | derives `pattern_facts.tsv`: the STRUCTURE facts parsed from each committed `.rx` (branch count, branch bytes, distinct first bytes, the longest run of adjacent branches sharing a first byte, shared prefix/suffix, trie nodes) + PCRE2's own analysis (first / required code unit, min length) + m/n per regime |
| `pattern_facts.tsv` | one row per pattern; the table NOTES.md's pattern tables are read from |
| `gen_oracle_limits.py` | probes each skeleton BEYOND the set's rungs on the oracle (compile only, doubling) and derives `oracle_limits.tsv` |
| `oracle_limits.tsv` | per skeleton: the widths probed, the last the oracle accepted, the first it refused, its diagnostic verbatim — libpcre2's compiled-size ceiling at 4096 branches of 3-12 bytes, at 8192 of 3-6, and at 2048 under `{1,3}`. 0.2 moved its `set_rungs` column only; no probed width, refusal or diagnostic changed. There is NO `pcrec_limits.tsv` and there will not be one (Frank, 2026-09-02): the sets are oracled on libpcre2 alone and pcrec's refusal widths live in the reports |
| `NOTES.md` | the objective, the tables, the predictions, the engine notes, the cell-time estimate |

REGENERATING. `python3 bench/altwide/gen_patterns.py`, `gen_subjects.py`,
`gen_throughput_subjects.py`, `gen_expectations.py`, `gen_pattern_facts.py`,
`gen_oracle_limits.py`. All six are deterministic; `make check` runs the two
subject generators and re-derives the other four in `--check` mode, over
every sub-bench under `bench/` by enumeration
(`tools/selfcheck.py:subbench_dirs`), and fails on any drift. **This set is
the slow one**: the expectation derivation is minutes, not the sub-second
every other set here takes, because the oracle is an interpreter and the
widest rungs enter thousands of branches per candidate start over 128 KB and
512 KB subjects. Measured on this box at 0.2: `gen_expectations.py` alone is
135 s, and `make check-harness` over EVERY sub-bench is 501 s against 449 s
before 0.2 (+11.6 % for 13 more patterns and 2 more subjects; both taken on a
box shared with another session, so same order, not to the second). That cost IS the
measurement's subject matter (NOTES.md, "Cell-time estimate"); it is not a
symptom, and the fix if it ever becomes intolerable is fewer throughput
bytes, not fewer rungs.

FIVE THINGS A FUTURE EDITOR SHOULD NOT UNDO WITHOUT READING WHY (all in
`NOTES.md`, all forced by something measured on the oracle, on a testee, or
by the harness's own arithmetic):

1. **The pools are globally SUBSTRING-free, not merely prefix-free.**
   Prefix-freeness alone buys the order arm (leftmost-first cannot return a
   different span, so `w-512` and `srt-512` are answer-identical). It does
   NOT buy "this subject carries exactly one branch", which every hit
   allocation and every per-subject assertion here rests on — `main` word 0
   carried two shorter branches of its own under the prefix-free draw, and
   the glue and concatenation subjects could not be built at all.
2. **The width ladder stops at 2048 on 3-12 byte branches, and the 4096-way
   rung uses 3-6 byte ones.** libpcre2 REFUSES the former ("regular
   expression is too large"; `oracle_limits.tsv`), and an expectation the
   oracle cannot state is a cell the harness cannot judge. `s-2048` beside
   `w-2048` is the control that says what the length change cost.
3. **The throughput subjects are 128 KB and 512 KB, not 1 MB.** A
   backtracker enters every branch at every candidate start; at width 2048
   one pass over 1 MB is tens of seconds, so the harness's 20 s per-trial cap
   would bind on the widest rungs of every backtracking testee, five trials
   each. At 128 KB nothing hits the cap and the regime still sits an order of
   magnitude above the search band.
4. **The background prose is branch-free by construction and the claim is
   ASSERTED per subject, not argued.** At width 4096 roughly one branch in
   ten is three bytes long and a 256 B line has ~250 three-byte windows, so
   several accidental hits per line is the EXPECTED number. Without the guard
   the match rate would be an accident of the seed rather than a design.
5. **0.2's ladder is DENSE from 64 to 512 and every 512 arm is twinned at
   256, because pcrec refuses everything at width ≥ 512.** Thinning the band
   back out — or dropping a 256 twin as "a duplicate of the 512 one" — takes
   the flat-line claim back to three points and puts the structure, order and
   wrapper arms back where no artifact exists to read. The 512 arms are the
   point under a RAISED cap and are kept for that; they are not the
   measurable ones today (NOTES.md, "What 0.2 added").

BUMPING THE VERSION is a deliberate, logged event (requirements §5): any
change to a pattern, a subject, or an expectation makes existing records
incomparable, so `version` in `subbench.toml` goes up in the same commit and
the reason goes in the journal. A change to `altwidetext.py`'s pool specs or
seed changes EVERY pattern and EVERY subject at once — the pools are the set.

0.1 → 0.2 is this set's worked example of a BYTE-IDENTICAL EXTENSION
(bench/bounded's 0.1 → 0.2 → 0.3 is the precedent): new patterns are new
`SPECS` rows over the UNCHANGED pools, new subjects are drawn LAST so the
old rng draws are the same stream prefix, and the check that it worked is
that `git` reports no modified `.rx`, that `manifest.tsv` is a pure append,
and that every old (pattern, subject, regime) expectation row is present
byte-identically in the new file. Records still never pool across the bump;
what stays comparable is a cell whose pattern id and subject id are in both.
