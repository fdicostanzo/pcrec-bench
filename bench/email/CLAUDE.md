# bench/email/ — the RFC 5322 email specimen (`email-specimen@0.1`)

WHERE IT CAME FROM. Copied from pcrec
`docs/design/subroutines_measurements/email_specimen/` (READ-ONLY
origin, never written to). `orig.rx`, `factored.rx`, the 85-subject list
inside `gen_subjects.py` and the three throughput constructions are that
origin's, verbatim; the subject BYTES were verified identical by
regenerating both trees and comparing all 88 files. Everything else here
is new: the sidecar, the sha256 manifests, the expectations and their
oracle.

Read `NOTES.md` first — the objective, why the two patterns are one
measurement, what would defeat the objective, how a pcrec give-up is
recorded, and (added [B15]) the floor pattern.

| file | role |
|---|---|
| `subbench.toml` | the SIDECAR: fields only, no grammar ([DD-13] untouched) |
| `patterns/orig.rx` | the hand-inlined pattern, raw bytes, no trailing newline |
| `patterns/factored.rx` | the same language via four `{0}` definitions + `(?&name)` calls |
| `patterns/floor.rx` | the FLOOR pattern ([B15]): the one-byte literal `@`, `role = "floor"` in the sidecar (schema v1.3) — a per-call baseline `orig`/`factored`'s numbers read against, not a third member of the language pair. See NOTES.md |
| `gen_subjects.py` | writes `subjects/` (gitignored) + `manifest.tsv` (committed) |
| `gen_throughput_subjects.py` | writes `throughput/` (gitignored) + `manifest_throughput.tsv` |
| `manifest.tsv` | 85 subjects: id, len, sha256, description |
| `manifest_throughput.tsv` | 3 subjects of 1 MB each |
| `gen_expectations.py` | derives `expectations.tsv` from the libpcre2 oracle for EVERY declared pattern (`orig`, `factored`, `floor`), generically; `--check` re-derives and diffs |
| `expectations.tsv` | 495 rows (three patterns x 165 (pattern, subject, regime) cells each): pattern, subject, regime, expected, start, end, nmatches, method, oracle |
| `selfcheck/` | the fixtures behind `make check`'s positive controls |
| `NOTES.md` | engine notes, declared variants (none), the objective, the floor pattern |

REGENERATING. `python3 bench/email/gen_subjects.py`,
`python3 bench/email/gen_throughput_subjects.py`,
`python3 bench/email/gen_expectations.py`. All three are deterministic;
`make check` runs them in `--check` mode and fails on any drift.

BUMPING THE VERSION is a deliberate, logged event (requirements §5): any
change to a pattern, a subject, or an expectation makes existing records
incomparable, so `version` in `subbench.toml` goes up in the same commit
and the reason goes in the journal.
