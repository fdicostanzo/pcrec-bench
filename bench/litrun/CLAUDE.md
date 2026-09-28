# bench/litrun/ — the literal-run sub-bench (`litrun@0.1`)

WHAT IT IS FOR. An ACCEPTANCE INSTRUMENT for pcrec's [OPT-LITSCAN] S2a
(plan row [B108]; inbox I-113, pcrec `docs/dev/lanes/s2a_report.md` at pin
a32bc86e, abi 41): the VM's own literal run of two or more consecutive
exact bytes as one bounds check plus one `memcmp`, replacing a per-byte
compare chain. The lane report's own D77 section asked for two things it
could not measure itself — whether a factoring pass and the lit-run
lowering interact (§7.1's 2×2) and whether the compare carries a per-call
constant or a toolchain-specific length cliff (§7.2's L-sweep, cross-
checked against `docs/dev/memcmp_lowering_study.md`'s finding that gcc-16
calls `memcmp()` out of line at exactly `L = 31` and nowhere else from 1 to
64). This set is the bench built to answer both, at the exact cells and
lengths the lane report names.

**Read `NOTES.md` first** — the objective, the 2×2 pattern table with the
lane's own predicted compile-time stamps, the L-sweep's regime choice and
the mechanical proof its tiling cannot accidentally match or miss at the
wrong offset, the predictions transcribed from I-113 (which live here and
which live in bounded/loglines/capability), and the cell-time estimate.

WHERE IT CAME FROM. **This set is deliberately NOT blinded** (NOTES.md,
"Objective", states why) — unlike every other `bench/*/` set, it is built
directly from pcrec's own lane report and memcmp study, not from a
blinded reading of `docs/spec/` alone. `wild-secrets-aws-access-key-id`
and `wild-secrets-github-pat` are copied VERBATIM from
`bench/capability/patterns/` (see `provenance.tsv` for the full chain back
to rebar-wild's `noseyparker.txt`, Unlicense); `ctrl-abc-dollar` (`abc$`)
is the same pcre2-testdata pattern `bench/capability`'s own
`wild-semdiv-dollar-trailing-newline-pcre2` already carries. Every other
pattern and every subject is authored here.

| file | role |
|---|---|
| `subbench.toml` | the SIDECAR: fields only, no grammar ([DD-13] untouched). Declares `match` + `search_short` + `throughput` and `short_search_max_bytes = 200` |
| `littext.py` | the ONE shared module: `ALPHABET`/`L_SWEEP`/`FLOOR_BYTE` and `literal(L)` (so `gen_patterns.py`, `gen_subjects.py`, `gen_throughput_subjects.py` and `gen_pattern_facts.py` can never disagree about a literal's text), the three throughput UNIT builders (`unit_match`/`unit_first_byte_flip`/`unit_last_byte_flip`), and `pcrecbench.periodic`'s re-export. Carries NO randomness primitive — unlike every other generator sub-bench, every byte here is an explicit, named construction (see the module's own header for why) |
| `gen_patterns.py` | writes `patterns/*.rx`: the 2×2 set's four patterns (two copied verbatim from `bench/capability`, byte-checked against it at generation time), the L-sweep's nine exact literals (via `littext.literal`, with `check_no_internal_repeat` asserted at generation time) and the floor. `--check` re-derives and diffs; also asserts the floor byte occurs in no other pattern |
| `patterns/*.rx` | the 13 members + `floor.rx`, raw bytes, no trailing newline, committed |
| `provenance.tsv` | the two copied `wild-secrets-*` patterns' full chain: `bench/capability`'s own rebar-wild/noseyparker.txt provenance, plus this file's own `adaptation` note (copied verbatim from bench/capability, byte-checked) |
| `gen_subjects.py` | writes `subjects/` (gitignored) + `manifest.tsv`: 27 SHORT subjects — 18 typed hit/near-miss fields for the 2×2 set (AWS's own published example access key id, pcre2's own testdata cases for `abc$`) and 9 `bnd-l<L>` boundary subjects (S7.2's "length L-1" arm, exactly `L-1` bytes, never tiled — NOTES.md explains why) |
| `gen_throughput_subjects.py` | writes `throughput/` (gitignored) + `manifest_throughput.tsv`: 27 DENSE tiled subjects (`mat-l<L>`/`fbf-l<L>`/`lbf-l<L>`, ~64 KiB each), S7.2's per-attempt-cost instrument. `check_no_accidental_match` proves the tiling mechanically at generation time |
| `manifest.tsv`, `manifest_throughput.tsv` | committed: id, len, sha256, description, **periodic** (the tiled subjects ARE periodic by construction, at period `L` — stated, not hidden, per [B17]/I-10's own rule) |
| `gen_expectations.py` | the entry point; the derivation is shared (`pcrecbench/expectations.py`). `--check` re-derives and diffs |
| `expectations.tsv` | 1,134 rows: 14 patterns × (27 match + 27 search_short + 27 throughput). One genuine cross-term worth knowing about, not a bug: `lit-l3`'s literal is `"abc"`, so it shares hits with `ctrl-abc-dollar` on several subjects (NOTES.md, "Subjects") |
| `gen_pattern_facts.py` | derives `pattern_facts.tsv`: PCRE2's first/required code unit (an exact literal's required byte is measured to be its OWN LAST BYTE, not its first — a PCRE2 fact this column makes checkable), min length, m/n per regime |
| `pattern_facts.tsv` | one row per pattern |
| `NOTES.md` | the objective, the tables, the regime choice, the predictions, the cell-time estimate |
| `export/litrun.rxt` | GENERATED ([B38], `tools/export_rxt.py`): a `.rxt` SOURCE file (no cases) for pcrec's own harnesses to pull this set's patterns in via `--source`. Never hand-edited; `make check-harness` re-derives and round-trips it against `--list-source` on every run |

REGENERATING. `python3 bench/litrun/gen_subjects.py`,
`gen_throughput_subjects.py`, `gen_expectations.py`, `gen_pattern_facts.py`.
All four (plus `gen_patterns.py`) are deterministic; `make check` runs the
two subject generators and re-derives the other three (plus patterns) in
`--check` mode, over every sub-bench under `bench/` by enumeration
(`tools/selfcheck.py:subbench_dirs`), and fails on any drift. This is the
FAST set among `bench/*/`: 14 patterns, no recursion, no unbounded class
repeat, ~1.8 MB of throughput subjects total (`bench/altwide`'s own
throughput arm alone is 1.28 MB across four subjects, and its expectation
derivation is minutes, not the sub-second this set takes).

ONE THING A FUTURE EDITOR SHOULD NOT UNDO WITHOUT READING WHY (`NOTES.md`,
"Regime choice"): **the L-sweep's `mat`/`fbf`/`lbf` subjects are built
PERIODIC on purpose**, at period `L`, DENSE in candidate starts — the
opposite of [B17]/I-10's usual rule against accidentally-periodic
throughput subjects. Here the periodicity is not an accident that flatters
a per-byte branch predictor; it is the mechanism that turns "one 2-40 byte
compare, too fast to time" into "tens of thousands of independent
per-attempt samples in one committed subject", and it is stated plainly by
the `periodic` manifest column (never hidden) rather than avoided.

WHAT THIS SET DOES NOT DO. It carries no pcrec-specific pattern, flag, or
testee shape (R-BENCH-4): the 2×2's `{default, -fno-altcls-factor} ×
{default, -fno-lit-run}` crossing and the L-sweep's `{default, -fno-req-run
-fno-req-byte}` labelling are the WINDOW's testee configs (lane
`b108repin`'s `configs.toml`), never this set's. It measures nothing about
DFA-routed cells (S2a writes no DFA byte; P3's own null claim is scored
against pcrec generally, not against a litrun pattern).

BUMPING THE VERSION is a deliberate, logged event (requirements §5): any
change to a pattern, a subject, or an expectation makes existing records
incomparable, so `version` in `subbench.toml` goes up in the same commit
and the reason goes in the journal. A change to `littext.py`'s alphabet or
length ladder changes every `lit-l<L>` pattern AND every L-sweep subject
at once.
