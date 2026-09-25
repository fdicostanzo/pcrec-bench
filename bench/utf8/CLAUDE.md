# bench/utf8/ — the UTF-8 encoding set (`utf8@0.1`)

WHAT THIS DIRECTORY IS TODAY ([B77] U3 + U4). The SUBJECTS (U3), the
PATTERNS + SIDECAR (U4) — a real, ENUMERABLE sub-bench (`subbench.toml`
exists), with a FLOOR-ONLY stub `expectations.tsv` (see "What is a STUB"
below). Design: `docs/design/utf8_set_v1.md` v0.2 (plan row [B77], inbox
I-90/I-94). `NOTES.md` and the REAL 76-pattern oracle derivation are
**U5's own scope, not yet built** — see `docs/dev/lanes/b77u4_report.md`
for U4's charter-vs-committed checklist and the U5 cost estimate.

## What IS built (U3 + U4)

| file | role |
|---|---|
| `pool_lat.tsv`, `pool_cyr.tsv`, `pool_cjk.tsv`, `pool_asc.tsv`, `pool_mix.tsv` | (U3) the FIVE COMMITTED WORD POOLS — see the U3 section below |
| `utf8text.py` | (U3) the shared xorshift64* primitive + the size-fitting boundary rule + the decode gate — see below |
| `gen_subjects.py` | (U3, edited by U4) writes `subjects/` (gitignored) + `manifest.tsv`: **91 typed short subjects**. U4 CONFIRMED (not merely typed) the `alt-cyr64-hit`/`alt-cyr64-miss` descriptions against the real `alt-cyr-64` pattern and the real oracle — see "The alt-cyr-64 word list" below |
| `gen_throughput_subjects.py` | (U3) writes `throughput/` (gitignored) + `manifest_throughput.tsv`: **seven throughput texts**, ~1.56 MB total |
| `manifest.tsv`, `manifest_throughput.tsv` | (U3) committed: `id, len, sha256, description, periodic` |
| `gen_subject_facts.py` | (U3) writes `subject_facts.tsv`: the per-subject UTF-8 LEAD-BYTE HISTOGRAM, over every subject in both manifests |
| `subject_facts.tsv` | (U3) committed, 98 rows (91 + 7) |
| `subjects/`, `throughput/` | GENERATED and gitignored |
| `patterns.rxt` | **(U4) THE PATTERN SOURCE OF TRUTH**: 76 blocks (75 members + the floor across families `cls`/`lit`/`ci`/`alt-qnt`/`asr`/`prp`), each with a native `provenance` sub-block (`source authored`, `fidelity synthesized`, `retrieved 2026-09-25`, an `adaptation` line citing `utf8_set_v1.md` 5's own table row) and a `tag family=/hazard=/requires=` line, plus one file-scope `ext bench` block — the twelve-config UTF-8 roster + REQUIRES capability matrix, TRANSCRIBED from lane b77u2's own witness census (never re-guessed — see "The ext bench roster" below). Sits beside `subbench.toml` with **no `rxt_source =` key** — see "Why no rxt_source" below |
| `gen_patterns.py` | **(U4) THE MASTER PATTERN TABLE**: every pattern's text authored fresh (transcribed verbatim from `utf8_set_v1.md` 5's own tables, one exception — see below), renders `patterns.rxt` + `patterns/*.rx` + (`--sidecar`) `subbench.toml`'s own `[[patterns]]` array + (`--provenance`) `provenance.tsv`. `--check` re-derives all three and diffs (structural only — no pcrec `--list-source` round-trip is wired; see the report for why) |
| `patterns/*.rx` | (U4) one raw-bytes file per pattern, DERIVED from the table — the harness's LOADED pattern source (via `subbench.toml`'s `[[patterns]]` array, not `rxt_source`) |
| `subbench.toml` | **(U4) THE SIDECAR**: `id="utf8"`, `version="0.1"`, `regimes = ["search_short", "throughput"]` (no `match`, per `utf8_set_v1.md` 10.1), `short_search_max_bytes = 512`, `[expectations] encoding = "utf8"` (the SET-WIDE `PCRE2_UTF` oracle flag, `pcrecbench/subbench.py`'s `SET_ENCODINGS` — [B77] U1), and the `[[patterns]]` array (`gen_patterns.py --sidecar`'s own output) |
| `gen_expectations.py` | **(U4) A STUB, not U5's real derivation** — see "What is a STUB" below |
| `expectations.tsv` | **(U4) STUB: 98 rows, the FLOOR PATTERN ONLY** (91 search_short + 7 throughput), real oracle-derived, `libpcre2-differential` |
| `provenance.tsv` | (U4) one row per pattern: `pattern_id, family, provenance_source, source_url, source_ref, license, retrieved, fidelity, adaptation, attribution` — every row `authored`/`synthesized`/`n-a` (this is a correctness/encoding census, not a wild-provenance set — `capability_set_v1.md`'s realism rule does not apply here) |

## What is a STUB (read before touching `expectations.tsv`)

U4's brief is explicit: expectations and `NOTES.md` are U5's scope
**unless the generic `make check-harness` gates require a stub — then
say so and make the smallest possible one.** They do, the moment
`subbench.toml` exists and this directory is ENUMERATED by
`tools/selfcheck.py`'s `subbench_dirs()`:

- `check_expectations()` unconditionally runs `gen_expectations.py
  --check` on every enumerated sub-bench.
- `check_floor_pattern()` runs a real `pcrecbench quick --testee
  pcre2-jit --regime search --pattern floor --subjects 5` cell on every
  enumerated sub-bench's floor pattern — which needs a real expectation
  row for the floor pattern against whichever 5 `search_short` subjects
  `quick` picks.

`gen_expectations.py` here derives REAL rows (the SAME shared oracle,
`pcrecbench.expectations.derive`, never faked) but restricted to the ONE
pattern those two gates actually need: the floor (`~`), over EVERY
subject in EVERY regime this set declares (91 search_short + 7
throughput = 98 rows) — cheap, since the floor is byte-safe and pure
ASCII. **The other 75 patterns carry NO expectation rows.** A `quick`/
`run` cell against any of them will raise until U5's real derivation
lands — the honest consequence of a stub, stated here rather than hidden.
See `bench/utf8/gen_expectations.py`'s own docstring and
`docs/dev/lanes/b77u4_report.md` for the timed cost estimate of the real
76-pattern derivation (the UTF oracle is reported ~30× slower than byte
mode).

## The alt-cyr-64 word list

`utf8_set_v1.md` 5(d) charters `alt-cyr-64` as "64 Cyrillic words,
`|`-joined" without naming them. `gen_patterns.py`'s `_alt_cyr_64_words()`
derives them from the committed `pool_cyr.tsv` (175 rows): **the LAST 64
rows, in file order** — chosen (not arbitrary) so that "дом" (house), the
word U3's `alt-cyr64-hit` subject was typed against, IS one of the 64
branches (row 144 of 176, inside the slice) and "квинтэссенция", the word
`alt-cyr64-miss` was typed against, is absent from the pool ENTIRELY (no
selection could include it). Both facts are asserted structurally
(`_alt_cyr_64_words()`'s own two `assert`s) AND verified against the real
libpcre2 oracle under `PCRE2_UTF` (`docs/dev/lanes/b77u4_report.md`):
`дом` answers `match[0,6)`, `квинтэссенция` answers `nomatch`. U4 updated
`gen_subjects.py`'s two descriptions from "assumes .../U4 COORDINATION"
hedges to "CONFIRMED", and regenerated `manifest.tsv`.

## The ext bench roster

Transcribed from lane b77u2's own witness census
(`docs/dev/measurements/2026-09-25-b77u2-utf8-witness-census.txt`, its
DECLARATIONS block) and `utf8_set_v1.md` 7.4's table, never re-guessed.
Six REQUIRES tokens (this set's own subset of `pcrecbench.capability`'s
20-token closed vocabulary): the three [B77] U1 tokens (`utf8-encoding`,
`ascii-class-scope`, `unicode-class-scope`) plus `lookaround`,
`true-end-anchor`, `unicode-properties`, carried per config in
`gen_patterns.py`'s `EXT_BENCH_ROSTER`. **Two corrections this lane made
on its own evidence, not silently inherited:**

1. **`tre-default` does NOT get `true-end-anchor` here**, though
   `bench/capability/patterns.rxt`'s own roster declares it for
   `tre-default`. `testees/tre/CLAUDE.md`'s OWN measured finding is that
   TRE has NO `\z`/`\A`/`\Z` tokens at all (a literal `\z` compiles as
   literal `z`), and `utf8_set_v1.md` 7.4 cites exactly this fact for
   `asr-a-z`'s exclusion. This is a candidate finding for
   `bench/capability`'s own owner (its roster's `true-end-anchor` row for
   `tre-default` looks wrong), not fixed here — out of this lane's scope.
2. **`onig-utf8`/`re2-utf8`/`vectorscan-block-nosom-utf8`'s
   `unicode-class-scope` satisfaction is the b77u2 RE-CENSUS result**:
   vectorscan SATISFIED (inline `(*UCP)` honoured per pattern, correcting
   `utf8_set_v1.md` 7.6's v0.2 draft prediction); onig/re2 NOT satisfied
   (`(*UCP)` refused outright).

## Why no `rxt_source =`

`bench/capability/subbench.toml` sets `rxt_source = "patterns.rxt"`
(the [B42] sidecar switch, 2026-09-16), which makes `patterns.rxt` the
FULLY LOADED pattern source (`pcrecbench/rxt_source.py`'s loader path).
This set does NOT set that key: `subbench.toml`'s own `[[patterns]]`
array (pointing at `patterns/*.rx`) is the loaded pattern source, and
`patterns.rxt`'s `ext bench` block is read separately, through
`pcrecbench.capability`'s SIDECAR/SHIM path
(`rxt_source.load_aux_rows()`, triggered by the file's mere PRESENCE
beside `subbench.toml` — no key needed, `pcrecbench/capability.py`'s own
`_load_matrix()` path (b)). This is the SAME two-artifact split
`bench/capability` used BEFORE its own sidecar switch — chosen
deliberately here rather than adopting `rxt_source =`, since the full
loader path was untested against this set and not asked for by the U4
brief. A future lane may switch it, following `bench/capability`'s own
precedent, once it re-verifies the round-trip.

## The 90-vs-91 arithmetic, stated once

`utf8_set_v1.md` 4.3/10.3 computes "90 typed short subjects" as 15 × 6
families and does not separately count the floor. This generator states
BOTH numbers rather than silently picking one convention: **90 family
subjects + 1 floor witness (`floor-hit`, the literal `~`) = 91 total**.

## Regenerating

In order (each reads the previous stage's output):

    python3 bench/utf8/gen_patterns.py            # patterns.rxt + patterns/*.rx
    python3 bench/utf8/gen_patterns.py --provenance > bench/utf8/provenance.tsv
    python3 bench/utf8/gen_subjects.py             # subjects/ + manifest.tsv
    python3 bench/utf8/gen_throughput_subjects.py  # throughput/ + manifest_throughput.tsv
    python3 bench/utf8/gen_subject_facts.py        # subject_facts.tsv (reads both trees)
    python3 bench/utf8/gen_expectations.py         # expectations.tsv (STUB: floor only)

`subbench.toml`'s own `[[patterns]]` array is pasted by hand from
`gen_patterns.py --sidecar`'s output whenever a pattern is added, removed
or re-tagged — the same convention `bench/capability/subbench.toml` uses.
All generators support `--check` and are picked up automatically by
`make check-harness`'s generic `bench/*/` gates now that `subbench.toml`
exists (`tools/selfcheck.py`'s `subbench_dirs()`).

## What is NOT built here — U5's own scope

- **The REAL `expectations.tsv`** (76 patterns × 91 search_short + 76 × 7
  throughput rows, oracle-derived under the per-pattern UTF/UCP option
  word `utf8_set_v1.md` 8.1 specifies) — U4's `gen_expectations.py` is a
  floor-only STUB (above); U5 replaces its body with the real
  76-pattern derivation (the shared `pcrecbench.expectations.derive`
  call, unrestricted). See `docs/dev/lanes/b77u4_report.md` for a timed
  cost estimate.
- **`NOTES.md`** — the objective, the outlier rule R0-R8, the growth
  plan (0.2/0.3), the predictions TSV transcription (P1-P10, dry-run
  BEFORE the first window per `utf8_set_v1.md` 11's F-M2 ruling).
- **`prp-ingreek`** (the REFUSAL witness) has **no typed subject**,
  deliberately — a refusal has no speed, so nothing here needs to hit
  or miss it.
