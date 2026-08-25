# docs/design/ — living design documents

Documents that describe a design AND the process/learning of building it —
panel-outcome blocks and refutations recorded inline rather than edited
away. Living: revised as the design is reviewed and built, unlike
docs/dev/'s append-only records.

## Files

- `requirements.md` — **[B1] the requirements note, ADOPTED v3 2026-08-25** (v1 from R1-R11; v2 after the R1 panel; v3 = Frank's rulings: narrow blocking scope, variants reproduce results exactly and preserve the sub-bench objective),
  written from Frank's rulings R1-R11: the loop-first purpose, the
  vocabulary (sub-bench / testee / record / store / report), the three
  subject regimes + compile cost, testee dimensions and the outcome and
  syntax-variant axes, the sub-bench directory model (format BLOCKING on
  pcrec [DD-13]), the two-layer record, correctness by intention, the
  query-driven report, box discipline, the provisional first cut, the
  APPROACH §8 dispositions, the OD-B* ledger and the panel attack list.
  The governing requirements; [B2]-[B7] build against it.

- `record_schema.md` — **[B2] the record schema design note, DRAFT 1
  2026-08-25**: what a record is (one cell, one run, one file, JSONL,
  never edited), the file naming rule, the record identity and its
  content hash, schema versioning and the mixing/migration policy,
  OD-B4's answer in both halves (the FIXED ENUMS and the NORMALIZATION
  RULES for engine name/version, testee id, hardware id, CPU model,
  kernel, compiler), the per-testee `engine_metadata` declaration with
  pcrec worked as the example (read from `rx_info` and the `RX_VM_*`
  stamps, never from the prose `ENGINE_WHY`), the full field tables for
  the setup layer and both row kinds, the cross-line rules X1..X17, the
  reserved extension points, and a "for the panel" list of what the
  author is least sure of. This note is what APPROACH.md §3 called the
  `artifact_schema` — the requirements note's vocabulary settled on
  RECORD, and the file is named for it. Implemented by `../../schema/`
  and gated by `make check-schema`.

Expected next residents, in the order the plan reaches them:
- `set_format.md` — the bench set format position: what this project needs
  from pcrec's [DD-13] unified format (R-BENCH-1..9 in
  ~/pcrec/docs/design/dd13_format/requirements.md §5) and what it uses in
  the interim.
- `<engine>_adapter.md` — per-testee adapter notes where an engine's
  semantics or build needs recording (Vectorscan's no-leftmost-first
  caveat, TRE's POSIX convention, pcrec's testee matrix).
- `<topic>_measurements/` — measurement directories: scripts, raw logs,
  and a README that states the question, the method, and the numbers,
  in the shape of ~/pcrec/docs/design/subroutines_measurements/.

Maintenance: update this file when files are added/removed or change role.
