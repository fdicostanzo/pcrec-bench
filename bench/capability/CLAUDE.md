# bench/capability/ — the capability survey set (`capability@0.1`)

WHAT IT IS FOR. A CAPABILITY CONTRAST across the [B7] engine roster: what
each engine can EXPRESS, what it REFUSES, and what the expressible
patterns COST (plan row [B42]; Frank's charter). Sixty-four patterns (63
members + the floor) in twelve provenance/capability families — six WILD
(imported from a permissive-licensed real source, provenance-tracked) and
six CAPABILITY/HAZARD (designed, held to the same realism rule Frank
ruled for the whole set: "from the wild" is a framing, not a ratio).

**BUILT ON pcrec's `.rxt` format** (Frank's Q3 ruling, 2026-09-12): this
is the first pcrec-bench set whose pattern text lives in a `.rxt` file as
its SOURCE OF TRUTH, not a derived export. `patterns.rxt` carries every
pattern's text, native `provenance` sub-block, `tag family=/hazard=/
requires=` classification and one file-scope `ext bench` block (the
testee roster + REQUIRES capability matrix); it passes `pcrec
--list-source patterns.rxt` cleanly.

**Read `NOTES.md` first** — the objective, the twelve families, L1's and
L2's blinding statements, the twin-pairing reconciliation (two designed
near-miss twins were authored blind against a guessed family that turned
out wrong; kept with corrected metadata, not re-authored), the subjects,
the outlier rule (stated before any run), the predictions, and what this
lane did NOT build (family 11's cross-convention scoring, the pre-compile
capability policy, `variant.kind` rendering — all future lanes' scope).

| file | role |
|---|---|
| `patterns.rxt` | THE PATTERN SOURCE OF TRUTH: 64 blocks, each with a native `provenance` sub-block and a `tag family=/hazard=/requires=` line, plus one file-scope `ext bench` roster/capability block. Derived by `gen_patterns.py` from `curation/wild/members.tsv` + `curation/designed/members.tsv`; `--list-source`-clean at pin cd371441 |
| `gen_patterns.py` | THE MASTER TABLE: reads both curation TSVs, applies the twin-pairing reconciliation and the REQUIRES-tag derivation, and renders both `patterns.rxt` and `patterns/*.rx`. `--check` re-derives both AND round-trips `patterns.rxt` through a real pcrec binary, comparing the DECODED `pattern` column against the table's own canonical bytes for every block (the DD-13b.W23.5 dump-value seam). `--sidecar` prints `subbench.toml`'s `[[patterns]]` blocks; `--provenance` prints `provenance.tsv`'s rows |
| `patterns/*.rx` | one raw-bytes file per pattern, DERIVED from the table — kept so `pcrecbench.subbench` (no `.rxt` reader yet; that is L4's build) can load this set with today's loader. `patterns.rxt` is authoritative |
| `subbench.toml` | the SIDECAR: `id="capability"`, `version="0.1"`, `regimes = ["search_short", "throughput"]` (no `match` — capability_set_v1.md 3.5's set-wide exclusion), `short_search_max_bytes = 512`. Its `[[patterns]]` array is `gen_patterns.py --sidecar`'s own output |
| `captext.py` | the shared randomness primitive (xorshift64*, in `bench/syntax/censustext.py`'s shape) + the throughput grammar: mixed log-line/HTTP/source-code/prose text (capability_set_v1.md 3.4's own words), re-exports `pcrecbench.periodic.periodic_field` |
| `gen_subjects.py` | writes `subjects/` (gitignored) + `manifest.tsv`: 75 typed short subjects, grouped and typed BY FAMILY (not one shared vocabulary — `bench/syntax`'s R3/R4 outlier rules do not transfer to a wild-provenance set). Three subjects carry genuine raw non-UTF-8 bytes for family 12 |
| `gen_throughput_subjects.py` | writes `throughput/` (gitignored) + `manifest_throughput.tsv`: `t-64k`/`t-256k`/`t-1m` from `captext.text()`. Carries an empirical REDOS SAFETY CHECK (`_redos_safety_check`): every `redos-nested` pattern's `find_all` over all three texts is timed and asserted under a 2 s guard, the belt-and-braces control beyond the structural `^`-anchor argument NOTES.md states |
| `manifest.tsv`, `manifest_throughput.tsv` | committed: id, len, sha256, description, periodic |
| `gen_expectations.py` | the entry point; the derivation is shared (`pcrecbench/expectations.py`). `--check` re-derives and diffs against the committed `expectations.tsv` |
| `expectations.tsv` | oracle-verified (`method = libpcre2-differential`) match/no-match/find-all expectations for every (pattern, subject, declared regime) triple |
| `gen_provenance.py` | derives `provenance.tsv` from `gen_patterns.py`'s own table; `--check` re-derives AND runs the gate (capability_set_v1.md 4.1: licence allowlist, `fidelity != verbatim` needs `adaptation`, a CC-BY-SA row needs `attribution`) plus the SIMILARITY-CHECK arm (Frank's Q1 not-a-copy gate: a character-4-gram Jaccard score against every `synthesized` pattern's own cited inspiration, failing by name above 0.85) |
| `provenance.tsv` | one row per pattern: source, licence, fidelity, adaptation, attribution, the twin-pairing fields |
| `gen_variants.py` | derives `variants.tsv` — DELIBERATELY EMPTY in v1 (no roster testee needs a per-engine spelling rewrite; see its own docstring for why this is checked, not merely asserted) |
| `variants.tsv` | empty (header only) in v1 |
| `NOTES.md` | the objective, the family table, the twin-pairing reconciliation, the subjects, the outlier rule, the predictions, what is deferred |
| `curation/` | L1's and L2's staging output — kept as PROVENANCE-OF-AUTHORSHIP (the blinding statements, the raw fetch excerpts, the per-lane reports this set's `gen_patterns.py` reads from), not deleted now that L3 has built on it. See its own CLAUDE.md |

REGENERATING. `python3 bench/capability/gen_patterns.py`, `gen_subjects.py`,
`gen_throughput_subjects.py`, `gen_expectations.py`, `gen_provenance.py`,
`gen_variants.py`, in that order (patterns before anything that reads
`patterns/*.rx`). All are deterministic; `make check` runs the two
subject generators and re-derives the rest in `--check` mode over every
sub-bench under `bench/` by enumeration (`tools/selfcheck.py:
subbench_dirs`).

THINGS A FUTURE EDITOR SHOULD NOT UNDO WITHOUT READING NOTES.md FIRST:

1. **`patterns.rxt` is the source; `patterns/*.rx` is derived.** Never
   hand-edit a `.rx` file — edit `curation/wild/members.tsv` or
   `curation/designed/members.tsv` (or, for a genuinely new L3-only
   pattern, `gen_patterns.py`'s own hand-authored data) and regenerate.
2. **The twin-pairing reconciliation (NOTES.md) is deliberate.**
   `base10num-near-miss` and `winpath-near-miss` carry `family =
   wild-logparse`, not `wild-validator` — this is a REPAIR of a blinded
   authoring lane's guess, not a typo to "fix" back.
3. **`ipv4-near-miss` answering identically to `wild-validator-ipv4-
   owasp` on every subject is the checked, expected finding**, not a
   broken control pair (NOTES.md's outlier rule R8).
4. **`redos-nested`'s six patterns are all `^`-anchored on purpose**
   (the throughput-safety argument `gen_throughput_subjects.py`'s own
   safety check depends on). A future edit that adds an unanchored
   ReDoS pattern must re-derive that safety margin, not assume it.
5. **`mojibake-curly-quote` omits `canonical_text`** (S10's rule — its
   raw bytes are not valid UTF-8); its identity is `canonical_sha256`
   alone, carried from `curation/designed/patterns/SHA256SUMS.txt`'s
   own convention, re-derived by `gen_patterns.py`.

WHAT IS NOT BUILT HERE (see NOTES.md for the full list and why): family
11's cross-convention scoring; the pre-compile REQUIRES capability
policy in `pcrecbench/harness.py` (the `ext bench` block is
documentation for that future lane, not enforcement); `variant.kind`
rendering; the `.rxt` loader in `pcrecbench.subbench` (L4); the six
[B7] non-pcre2/pcrec adapters.
