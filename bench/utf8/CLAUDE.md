# bench/utf8/ — the UTF-8 encoding set (`utf8@0.1`)

WHAT THIS DIRECTORY IS TODAY ([B77] U3 + U4 + U5). The SUBJECTS (U3), the
PATTERNS + SIDECAR (U4), and the REAL oracle-derived EXPECTATIONS +
`NOTES.md` (U5) — a complete, ENUMERABLE sub-bench, ready for its first
window. Design: `docs/design/utf8_set_v1.md` v0.2 (plan row [B77], inbox
I-90/I-94). Lane reports: `docs/dev/lanes/b77u3_report.md`,
`b77u4_report.md`, `b77u5_report.md`.

## What IS built (U3 + U4 + U5)

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
| `gen_expectations.py` | **(U5) THE REAL DERIVATION**: the shared `pcrecbench.expectations.main` over all 76 patterns, declaring ONE oracle refusal (`EXPECTED_ORACLE_REFUSALS = {prp-ingreek}`; an undeclared refusal or this pattern compiling fails BY NAME). ~34 s, `--check` included (validate-once, below) |
| `expectations.tsv` | **(U5) 7,350 rows**, oracle-derived (`libpcre2-differential`, 10.46): 75 compiling patterns × (91 `search_short` + 7 `throughput`); `prp-ingreek` has NONE, by design. The floor's 98 rows are byte-identical to U4's stub |
| `NOTES.md` | **(U5)** the objective + the limitation sentence, the oracle's method (option word, VALIDATE-ONCE, the declared refusal, what it settled about `prp-greek`/`-sc` and U+00B7), the outlier rule R0-R8, the predictions P1-P11 with what the transcription changed, the growth plan, engine neutrality, cell time. Stated before any run |
| `provenance.tsv` | (U4) one row per pattern: `pattern_id, family, provenance_source, source_url, source_ref, license, retrieved, fidelity, adaptation, attribution` — every row `authored`/`synthesized`/`n-a` (this is a correctness/encoding census, not a wild-provenance set — `capability_set_v1.md`'s realism rule does not apply here) |

## The oracle derivation (U5)

`gen_expectations.py` calls the SAME shared chain every set uses
(`pcrecbench/expectations.py`), under the set-wide `PCRE2_UTF` word plus
`PCRE2_UCP` on the five `requires-unicode-class-scope` patterns ([B77] U1).
Two things are this set's own:

- **VALIDATE-ONCE** (`docs/design/utf8_set_v1.md` 8.2 as AMENDED by the
  manager's ruling, 2026-09-25): the throughput find-all passes
  `PCRE2_NO_UTF_CHECK` only on calls 2..n after libpcre2's own call-1 check
  of the whole subject (`pcrecbench/oracle_pcre2.py` `_find_all_impl`).
  Without it the derivation is quadratic in subject length (~59 min
  modelled; `docs/dev/measurements/2026-09-25-b77u5-validate-once-probe.txt`);
  with it, ~34 s, so `check_expectations` re-derives this set inside `make
  check`. `tools/selfcheck.py check_utf8_validate_once` is the control
  (rows identical to the always-check path on every short + ≤64 KB subject;
  an ill-formed subject refused by name; byte sets untouched).
- **The declared refusal, `prp-ingreek`**: no expectation rows, the
  first-class `did-not-compile` compile-axis outcome (utf8_set_v1.md 5(f)).
  `derive(expected_refusals=)` is what makes that legal — and only for a
  DECLARED pattern.

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
    python3 bench/utf8/gen_expectations.py         # expectations.tsv (~34 s, all 76 patterns)

`subbench.toml`'s own `[[patterns]]` array is pasted by hand from
`gen_patterns.py --sidecar`'s output whenever a pattern is added, removed
or re-tagged — the same convention `bench/capability/subbench.toml` uses.
All generators support `--check` and are picked up automatically by
`make check-harness`'s generic `bench/*/` gates now that `subbench.toml`
exists (`tools/selfcheck.py`'s `subbench_dirs()`).

## What is NOT built here

- The FIRST SAMPLE (no `utf8@0.1` record exists yet) — §14 Q6's seven cells.
- A `pcrec-*-bigcap-utf8` config (P7's raised-cap half has no testee) and
  the 0.2 `-e byte` mirror (P8) — roster growth, NOTES.md.
- **`prp-ingreek`** (the REFUSAL witness) has **no typed subject**,
  deliberately — a refusal has no speed, so nothing here needs to hit
  or miss it.
