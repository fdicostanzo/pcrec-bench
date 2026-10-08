# bench/capability/ — the capability survey set (`capability@0.2`)

**@0.2 ([B125], 2026-10-08, lane b125cap; Frank's I-136).** Built in place, the
altwide@0.1 -> 0.2 way: the 64 patterns, 75 short subjects, 3 throughput texts
and 4,990 expectation rows of 0.1 are byte-identical; 0.2 appends SEVEN
patterns (family wild-logparse: the end-anchored tail family `tail-*`,
`letters-bounded-tail-z`, `hex8-bounded`), EIGHT throughput subjects
(`t-evil-*-60k`, `t-trim-*-60k`, `t-mixed-runs-4k`, `t-tail-*-1m`; see
`gen_throughput_subjects.extra_subjects`, `captext.letter_run/ws_run/
mixed_runs/prose`) and a SECOND EXPECTATION METHOD,
`libpcre2-dfa-fallback` (`[expectations] fallback_method` in `subbench.toml`;
`docs/design/expectation_methods_v1.md`; `pcrecbench/expectations.py`
`dfa_fallback`/`DfaControl`). NOTES.md's last section is the 0.2 text, with
P11-P16 and R9-R11. The counts below this paragraph that say sixty-four
describe 0.1's first 64 patterns; 0.2 has 71.

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
--list-source patterns.rxt` cleanly. Since the [B42] SIDECAR SWITCH
(2026-09-16, runbook step 5, at the O-29 fix pin a770139e) the sidecar's
`rxt_source = "patterns.rxt"` key makes it the LOADED source too
(`pcrecbench/rxt_source.py`), not just the declared one — the 64/64
provenance-agreement gate flipped refuse→load at that pin
(docs/dev/measurements/2026-09-16-o29-verify-a770139e.txt).

**Read `NOTES.md` first** — the objective, the twelve families, L1's and
L2's blinding statements, the twin-pairing reconciliation (two designed
near-miss twins were authored blind against a guessed family that turned
out wrong; kept with corrected metadata, not re-authored), the subjects,
the outlier rule (stated before any run), the predictions, and what this
lane did NOT build (family 11's cross-convention scoring, the pre-compile
capability policy, `variant.kind` rendering — all future lanes' scope).

| file | role |
|---|---|
| `patterns.rxt` | THE PATTERN SOURCE OF TRUTH: 64 blocks, each with a native `provenance` sub-block and a `tag family=/hazard=/requires=` line, plus one file-scope `ext bench` roster/capability block. Derived by `gen_patterns.py` from `curation/wild/members.tsv` + `curation/designed/members.tsv`; `--list-source`-clean at pin cd371441 and dump-complete (64/64 provenance rows) at a770139e |
| `gen_patterns.py` | THE MASTER TABLE: reads both curation TSVs, applies the twin-pairing reconciliation and the REQUIRES-tag derivation, and renders both `patterns.rxt` and `patterns/*.rx`. `--check` re-derives both AND round-trips `patterns.rxt` through a real pcrec binary, comparing the DECODED `pattern` column against the table's own canonical bytes for every block (the DD-13b.W23.5 dump-value seam). `--sidecar` prints `subbench.toml`'s `[[patterns]]` blocks; `--provenance` prints `provenance.tsv`'s rows |
| `patterns/*.rx` | one raw-bytes file per pattern, DERIVED from the table — was the load path before the [B42] sidecar switch (the `.rxt` loader now reads `patterns.rxt` directly); kept as a derived export for reference. `patterns.rxt` is authoritative |
| `subbench.toml` | the SIDECAR: `id="capability"`, `version="0.1"`, `regimes = ["search_short", "throughput"]` (no `match` — capability_set_v1.md 3.5's set-wide exclusion), `short_search_max_bytes = 512`, and since the [B42] switch `rxt_source = "patterns.rxt"` (the loaded source). Its `[[patterns]]` array is `gen_patterns.py --sidecar`'s own output |
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
| `_diag_worker.py`, `diag_expectations_timing.py` | diagnostic tooling (not part of the generator chain `make check-harness` runs): one pattern's full oracle derivation timed cell-by-cell, driven per-pattern under `gnutimeout`. Built to root-cause the `codegrammar-flat` CSV-quoting bug below; kept for any future set-authoring bug of the same shape |

**A TSV-QUOTING BUG THIS LANE FOUND AND FIXED (read before touching
`_read_tsv()`).** `gen_patterns.py`'s curation-table reader originally
used `csv.DictReader`'s DEFAULT quoting on a plain tab-delimited file.
Exactly one field across both curation TSVs starts with a literal `"`
(`codegrammar-flat`'s canonical text) and CSV's default quoting
silently swallowed it, shipping a pattern missing its leading `"` —
which cost the whole set its PCRE2 required-first-byte optimization on
that ONE pattern and turned a 1 MB unanchored throughput search into a
multi-hour quadratic backtrack (root-caused by `diag_expectations_
timing.py`, not by inspection). Fixed three ways: `_read_tsv()` now
passes `quoting=csv.QUOTE_NONE`; `load_designed()` cross-checks every
parsed pattern against `curation/designed/patterns/SHA256SUMS.txt`'s
independently-staged hash; `captext.py`'s throughput grammar now emits
a quoted string in roughly half its source lines as a second,
independent guard against the same HAZARD CLASS recurring from a
different cause. Full account: `docs/dev/lanes/b42set_report.md`.

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
11's cross-convention SCORING machinery (an `under`-qualified expectation
row, still unauthored); the six [B7] non-pcre2/pcrec adapters. (The
`.rxt` loader gap this list used to carry closed at the O-29 fix pin
a770139e — the sidecar switch above.)

**[B42] L5 (lane b42cap, 2026-09-16) CORRECTS the two claims above that
used to read "not built":** the pre-compile REQUIRES capability policy
IS wired into `pcrecbench/harness.py` (`pcrecbench/capability.py`), read
from this set's own `ext bench` block via the sidecar/shim load path
(`rxt_source.load_aux_rows()`, which does not trip O-29 -- an `ext`
block lives outside the per-pattern content those gates scan); and
`variant.kind` IS rendered by the reporter now, though never exercised
by this set (`gen_variants.py`'s table is deliberately empty in v1).
L5's own witness-compile census also corrected three wrong `pcrec-*`
declarations the first cut staged (`conditionals`, `control-verbs`,
`lookbehind-variable` -- all three actually REFUSED at the pinned
pcrec); see `NOTES.md` and `docs/dev/lanes/b42cap_report.md` for the
full matrix.

**The REQUIRES-TAG CORRECTION WAVE (lane b46tags, 2026-09-17) fixed six
under-tagged patterns** (`quoted-delim-match`, `utf8-lead-no-cont`,
`tag-depth3-bound`, `codegrammar-xflag`, `bracket-array-define`,
`nested-comment-rec` — all in `curation/designed/members.tsv`, all
missing a `lookaround`/`named-groups`/`backrefs` token their own text
actually uses), triggered by `l6btre`'s census finding two of them; see
`NOTES.md`'s own section for the full evidence table and
`docs/dev/lanes/b46tags_report.md` for the audit method and the
behavioral witnesses (`tre-default`/`vectorscan-block-nosom` flipping a
raw driver refusal to a clean `unsupported-by-declaration`). No pattern
was found over-tagged.

**[B117] (lane b117prep, 2026-09-29) adds the eight COMPILEE
OPTIMIZATION-LEVEL testees to the `ext bench` roster**
(`pcrec-{auto,vm}-o{0,1,3,s}`; `patterns.rxt` regenerated, `--check`
clean): each declares EXACTLY its base's (`pcrec-auto`/`pcrec-vm`) own
token set — the axis is a `cflags`-carried gcc/clang `-O` flag on OUR OWN
phase-2 compile, never passed to pcrec's own argv, so it cannot move
what the PARSER accepts (the same [B111] reasoning `pcrec-auto-align64`
above already states verbatim). No separate witness compile: the
reasoning is structural, not measured, the same disposition [B111]'s
own compiler/buffer/cap-axis rows take. See `testees/pcrec/CLAUDE.md`'s
"[B117]" row and `docs/dev/plan.md`'s [B117] entry.

**[B101] (lane b101repin, 2026-09-26) adds `pcrec-auto-noreqbyte` to the
`ext bench` roster** (pcrec-auto + `-fno-req-byte`, inbox I-111's
[OPT-REQBYTE] twin; `patterns.rxt` regenerated, `--check` clean): exactly
`pcrec-auto`'s tokens -- the denial is emit-side, and MEASURED the two
configs' refusal sets over all 64 patterns x both forms are identical
(4 refused both, 0 movers; docs/dev/measurements/2026-09-26-b101-twin-
stamps.txt). Without the row the twin would read every requires-tagged
pattern `unsupported-by-declaration` (the fail-closed rule).

**[B7]/L6b (lane l6bonig, 2026-09-17) adds `onig-default` to the `ext
bench` roster** (`EXT_BENCH_ROSTER` in `gen_patterns.py`, `patterns.rxt`
regenerated): 13 of 17 REQUIRES tokens satisfied, withholding
`lookbehind-variable`, `control-verbs`, `unicode-properties` and
`callouts` -- each independently witnessed (isolated witness + all 64
real corpus patterns compiled through the real adapter) in
`docs/dev/measurements/2026-09-17-onig-capability-witness-census-
6.9.10.txt` and `testees/onig/CLAUDE.md`. 62/64 corpus patterns compile
under `onig-default`; the two refusals
(`negation-scope-lookbehind-var`, `balanced-parens-rec`) reproduce their
isolated witness's exact `ONIGERR_*` code and are left to fail HONESTLY
as real `did-not-compile` rows rather than being hidden behind a token
withhold that would misrepresent the other patterns in their own
families.

**[B111] (lane b111roster, 2026-09-28) closes THE ROSTER GAP,
STRUCTURALLY.** `EXT_BENCH_ROSTER` was hand-listed per testee with no
gate on it, so a new pinned testee (a deny-flag twin, a compiler
sibling, a buffer variant) silently read `unsupported-by-declaration`
on all 27 `requires-*`-tagged patterns until someone happened to run it
against this set and noticed — it bit twice in three days (outbox O-64
-> O-65 on `pcrec-auto-nolitrun`; O-67 item 4 on the two [B110]
`align64loops` testees the very next day). Two things now exist beside
`EXT_BENCH_ROSTER`:

- **`EXCLUDED_TESTEES`** (`gen_patterns.py`, right after the roster
  list): every pinned testee id deliberately NOT on the roster, by
  name, with why — `pcrec-local` (no fixed pin, scratch tier, never
  ranked) and every `-utf8` engine-encoding sibling (this set is
  byte-mode-only; `-utf8` configs are `bench/utf8`'s, per the
  convention `testees/vectorscan/CLAUDE.md` already states for
  `vectorscan-block-som-utf8`).
- **`tools/selfcheck.py`'s `check_capability_roster_coverage`**, in
  `make check-harness`: every testee id `pcrecbench.adapters.
  all_testees()` finds across EVERY `testees/*/configs.toml` must
  appear in `EXT_BENCH_ROSTER` OR `EXCLUDED_TESTEES` — a testee in
  NEITHER fails the check by name, before any window runs it and finds
  27/64 patterns silently blocked.

**A NEW TESTEE (any `testees/*/configs.toml` addition, on ANY engine,
not only pcrec) needs a roster row or an `EXCLUDED_TESTEES` entry in
the SAME commit that pins it**, or `make check-harness` fails by name.
Add a row to `EXT_BENCH_ROSTER` (citing why its declared token set is
what it is — measured where cheap, as the `pcrec-auto-noreqbyte`/
`pcrec-auto-nolitrun` rows above do, or reasoned from an existing row's
own measurement where the new axis is provably parse-invariant, as the
twenty [B111] deny-flag/compiler/buffer/cap rows do) or, when the
testee should never run against this set, an `EXCLUDED_TESTEES` entry
naming the reason. Either way, regenerate `patterns.rxt`
(`python3 bench/capability/gen_patterns.py`, then `--check`).
