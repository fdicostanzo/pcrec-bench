# bench/email/ — the RFC 5322 email specimen (`email-specimen@0.2`)

WHERE IT CAME FROM. Copied from pcrec
`docs/design/subroutines_measurements/email_specimen/` (READ-ONLY
origin, never written to). `orig.rx`, `factored.rx`, the 85-subject list
inside `gen_subjects.py` and the original three throughput constructions
(`t-a-valid-addrs`, `t-b-no-at`, `t-c-long-atom-run`) are that origin's,
verbatim; the subject BYTES were verified identical by regenerating both
trees and comparing all 88 files. Everything else here is new: the
sidecar, the sha256 manifests, the expectations and their oracle, the
`periodic` column and its two new throughput subjects ([B17]).

Read `NOTES.md` first — the objective, why the two patterns are one
measurement, what would defeat the objective, how a pcrec give-up is
recorded, the floor pattern ([B15]), and (added [B17]) periodic vs
non-periodic throughput subjects.

| file | role |
|---|---|
| `subbench.toml` | the SIDECAR: fields only, no grammar ([DD-13] untouched) |
| `patterns/orig.rx` | the hand-inlined pattern, raw bytes, no trailing newline |
| `patterns/factored.rx` | the same language via four `{0}` definitions + `(?&name)` calls |
| `patterns/floor.rx` | the FLOOR pattern ([B15]): the one-byte literal `@`, `role = "floor"` in the sidecar (schema v1.3) — a per-call baseline `orig`/`factored`'s numbers read against, not a third member of the language pair. See NOTES.md |
| — | the `periodic` fact ([B17]) lives in `pcrecbench/periodic.py`, MOVED there from this directory when `bench/loglines` became its second caller ([B11.1]): `smallest_period`/`periodic_field`, the smallest exact repeat period in [1, 4096] bytes or `no`, so the definition is the same wherever the column appears in ANY manifest. Both generators below import it. See NOTES.md "Periodic and non-periodic subjects" |
| `gen_subjects.py` | writes `subjects/` (gitignored) + `manifest.tsv` (committed) |
| `gen_throughput_subjects.py` | writes `throughput/` (gitignored) + `manifest_throughput.tsv`; ([B17]) also the generated-prose builder (`build_prose`, seeded `random.Random(GEN_SEED)`) behind `t-d-prose-sparse-addrs`/`t-e-prose-no-at` |
| `manifest.tsv` | 85 subjects: id, len, sha256, description, periodic ([B17]: gained the last column, uniform with the throughput manifest — all 85 are tiny enough that the period scan costs nothing) |
| `manifest_throughput.tsv` | 5 subjects of 1 MB each ([B17], inbox I-10: was 3; `t-d-prose-sparse-addrs` and `t-e-prose-no-at` added, both non-periodic, beside the three periodic originals which are KEPT — they isolate the steady-state loop cost): id, len, sha256, description, periodic |
| `gen_expectations.py` | derives `expectations.tsv` from the libpcre2 oracle for EVERY declared pattern (`orig`, `factored`, `floor`), generically; `--check` re-derives and diffs |
| `expectations.tsv` | 501 rows (three patterns × 167 (pattern, subject, regime) cells each — 85 match + 77 search_short + 5 throughput): pattern, subject, regime, expected, start, end, nmatches, method, oracle |
| `selfcheck/` | the fixtures behind `make check`'s positive controls |
| `NOTES.md` | engine notes, declared variants (none), the objective, the floor pattern, periodic vs non-periodic throughput subjects |

REGENERATING. `python3 bench/email/gen_subjects.py`,
`python3 bench/email/gen_throughput_subjects.py`,
`python3 bench/email/gen_expectations.py`. All three are deterministic;
`make check` runs them in `--check` mode and fails on any drift.

`pcrecbench/subbench.py`'s manifest reader is GENERIC on column count (4
or 5) — it does not assume `periodic` is present, so a future manifest
that drops or re-adds the column still loads.

BUMPING THE VERSION is a deliberate, logged event (requirements §5): any
change to a pattern, a subject, or an expectation makes existing records
incomparable, so `version` in `subbench.toml` goes up in the same commit
and the reason goes in the journal. `0.1` → `0.2` ([B17], 2026-08-28):
the throughput subject set and both manifests' shape changed (see
`subbench.toml`'s version comment); no pattern text and none of the
original subjects' bytes changed.
