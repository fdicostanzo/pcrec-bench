# bench/syntax/ — the syntax census sub-bench (`syntax@0.1`)

WHAT IT IS FOR. A wide-net CENSUS across the PCRE syntax an engine may
support (plan row [B36]; Frank's charter is inbox I-42): ninety-five
patterns, one construct each in an otherwise plain body, enumerated from
pcrec's `--list-syntax` construct REGISTRY at our pin (the seed, copied
verbatim) so that nothing is listed from either side's head — and the same
subjects, regimes and instrument as every other set, so that a testee's
outlier on one family points at ONE mechanism. Its output is not a verdict
but a RANKED LIST OF QUESTIONS for Frank (I-42 (4)), each of which becomes
a depth probe of the bounded-rung shape before any pcrec row is chartered.

**Read `NOTES.md` first** — the objective, the pattern table by family,
what was left out and why, the blinding statement, the subjects, the
OUTLIER RULE (R0-R7, stated before any run), the predictions P1-P13, the
room left for a utf sibling set, the floor, and the cell-time estimate with
its premise.

WHERE IT CAME FROM. Nothing is copied but the seed. Authored 2026-09-05 by
a lane blinded per pcrec D27: the patterns and subjects come from `man
pcre2pattern` and the seed's construct list; the author did not open
`testees/pcrec/`, `pcrecbench/adapters.py`, pcrec's sources or corpora, or
this repo's stores, reports and ledgers (NOTES.md, "Blinded authorship",
names the two pcrec documents that WERE read).

| file | role |
|---|---|
| `list_syntax_9a1583ba.tsv` | THE SEED: pcrec's `--list-syntax` registry at pin 9a1583ba (abi 23; = the [B39] pin d34c9131 minus this file; the RE-SEED of I-52 — one description row moved vs the 334fd10e seed the set was authored from, no status/module/built column), verbatim under a source header (origin path, commit, date, generator, and what the file is and is not used for). Only `kind`, `syntax`, `status`, `family` are read; `module`/`engines`/`built` are copied into coverage.tsv as `seed_*` provenance and shape nothing (R-BENCH-4) |
| `subbench.toml` | the SIDECAR: fields only, no grammar ([DD-13] untouched). Declares all three regimes and `short_search_max_bytes = 256`. Its `[[patterns]]` block is DERIVED (`gen_patterns.py --sidecar` prints it; `--check` compares it entry for entry) |
| `censustext.py` | the one randomness primitive (`Rng`, xorshift64*) and the shared VOCABULARY + line grammar (prose with doubled and Latin-1 words, order lines, tag pairs, balanced parens, key=value, quoted strings) the throughput texts are drawn from and the short subjects are typed from; re-exports `pcrecbench.periodic.periodic_field` |
| `gen_patterns.py` | THE PATTERN TABLE (`PATTERNS`: id, family, seed rows exercised, text, note), `NOT_EXERCISED` (every seed row left out, with its reason) and `FOLD_WITNESSES` (the five fold-pair witnesses, tagged `fold-pair-witness`). Writes `patterns/*.rx` and derives `coverage.tsv` from the table × the seed; `--check` re-derives both and checks the sidecar; `--seed PATH` re-derives coverage from a re-seeded registry and FAILS BY NAME on any row no pattern covers and no reason excuses |
| `patterns/*.rx` | the 94 members + `floor.rx`, printable ASCII, no trailing newline, committed |
| `coverage.tsv` | derived: one row per seed row — `covered` (77), `covered-by-family` (32, the seed's own `family` column), `not-exercised` (19) / `not-exercised-by-family` (5) with reasons, `pcre2-rejects` (5) — then the base-grammar constructs (no seed row) the set exercises |
| `gen_subjects.py` | writes `subjects/` (gitignored) + `manifest.tsv`: 30 typed FIELDS (2-14 B, one construct's whole-string hit or semantic edge each) + 12 typed LINES (≤ 86 B) of the same vocabulary. Typed, not drawn: deterministic by construction |
| `gen_throughput_subjects.py` | writes `throughput/` (gitignored) + `manifest_throughput.tsv`: `t-64k`, `t-256k`, `t-1m` from `censustext.text()` at three seeds — a SIZE SWEEP at fixed hit density, no `#`, no `\r`, no control bytes, `periodic = no` (computed) |
| `manifest.tsv`, `manifest_throughput.tsv` | committed: id, len, sha256, description (family/arm in a fixed spelling: `field/hit`, `field/edge`, `line/prose`, `line/structured`, `run/mixed`), periodic |
| `gen_expectations.py` | the entry point; the derivation is shared (`pcrecbench/expectations.py`). `--check` re-derives and diffs. Prints one expected NOTE per pattern whose captures participate (the backreference, recursion, named-group and conditional patterns — the construct under census IS the capture) |
| `expectations.tsv` | 8,265 rows: 95 patterns × (42 match + 42 search_short + 3 throughput), method `libpcre2-differential`, oracle 10.46 |
| `gen_pattern_facts.py` | derives `pattern_facts.tsv`: family, seed rows and the seed's module per pattern, bytes, PCRE2's capture count / backref max / match-empty / max lookbehind (four PCRE2_INFO codes verified by construction on every run) and first / required code unit / min length, m/n per regime, oracle version |
| `pattern_facts.tsv` | one row per pattern; the table NOTES.md's rules R4 and R6 read (which patterns are REGULAR, what PCRE2 knows about each start) |
| `NOTES.md` | the objective, the tables, the outlier rule, the predictions, the utf room, the estimate |

REGENERATING. `python3 bench/syntax/gen_patterns.py`, `gen_subjects.py`,
`gen_throughput_subjects.py`, `gen_expectations.py`, `gen_pattern_facts.py`.
All five are deterministic; `make check` runs the two subject generators
and re-derives the other three in `--check` mode over every sub-bench under
`bench/` by enumeration (`tools/selfcheck.py:subbench_dirs`) and fails on
any drift. The expectation derivation is the one slow step here: about 3.3
minutes wall on this box while another session's battery ran (the six
dense class patterns — `\w+`, `\p{L}+`, … — find-all ~200 k matches per MB
through one ctypes call each; the other 89 patterns are seconds). The
`--check` pass costs the same, so `make check-harness` grows by about
3-4 minutes with this set.

THREE THINGS A FUTURE EDITOR SHOULD NOT UNDO WITHOUT READING WHY (all in
`NOTES.md`):

1. **The seed enumerates; it does not shape.** `built`, `module` and
   `engines` are copied into coverage.tsv as the seed's own values,
   labelled, for a reader of the first sample; a pattern exists for an
   `unbuilt` construct exactly as for a built one, and the refusal is the
   result (P1 predicts fifteen per pcrec testee). Filtering the table by
   `built` would make the set pcrec-shaped (R-BENCH-4) and would hide the
   day a construct becomes built.
2. **The control pairs stay.** `qnt-plus-ctl` (`a+ab`) beside `a++ab`,
   `lit-cat` beside the fourteen `cat`-language spellings, the four
   "four digits" call spellings and the three balanced-paren recursions:
   an outlier without its same-language twin is a number, not a question
   (rule R3).
3. **No unbounded `.` repeat under `(?s)`, and 1 MB is the top run.** The
   set has no backtracking hazard by design; a `(?s).*` over a 1 MB
   subject with no newline barrier is quadratic and would bind the
   harness's 20 s per-trial budget on every backtracking testee.

RE-SEEDING (the next pcrec pin moves rows: at abi 23 `\x{...}` and utf8
moved to the base grammar). Copy the new `--list-syntax` output under the
same source-header discipline as `list_syntax_<sha>.tsv`, point
`gen_patterns.py`'s `SEED` at it, run `--check`, and read the failures by
name: a new row needs a pattern or a `NOT_EXERCISED` reason; a row whose
`syntax` spelling changed needs the pattern table's `constructs` updated.
Then regenerate coverage.tsv and pattern_facts.tsv (their `seed_*` columns
move) and BUMP THE VERSION if any pattern's bytes changed — coverage and
facts moving alone is not a version bump (the records' `content_hash`
moves, which is what it is for).

BUMPING THE VERSION is a deliberate, logged event (requirements §5): any
change to a pattern, a subject or an expectation makes existing records
incomparable, so `version` in `subbench.toml` goes up in the same commit and
the reason goes in the journal. A change to `censustext.py`'s vocabulary or
grammar changes every throughput text at once.

THE UTF SIBLING (I-42 (e)) is `bench/syntaxutf/`, not a bump of this set:
NOTES.md, "Room for a utf family".
