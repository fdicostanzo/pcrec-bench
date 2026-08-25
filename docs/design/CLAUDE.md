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

- `harness_contract.md` — manager design (2026-08-25) for [B3]/[B4]/[B5]
  to build against in parallel: the python package layout, the sub-bench
  directory + `subbench.toml` sidecar, the adapter interface and the
  shared DRIVER PROTOCOL (batched in-process timing), the store layout
  and `run`/`index`/`report` CLI, the quiet instrument, self-checks.
  Paneled at the M1 close.
- `record_schema.md` — **[B2] the record schema design note, merged
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

- `harness_notes.md` — **[B3]/[B4]'s list of where the BUILD differs from
  `harness_contract.md`, and why**: the two regime spellings, the two
  testee-id spaces, the sidecar's second generator/manifest pair, the
  driver-protocol columns the contract omitted, the resume rule, the
  `iters` calibration rule, the `consumed_length` claim, the give-up
  policy, the `subbench.content_hash` rule, and what is not built. Item
  9 is the one with a real hole in it — the MATCH regime presumes an
  end-anchor and pcrec has none. For the M1 panel.

- `quiet_baseline.md` — **[B3]'s answer to OD-B8, MEASURED 2026-08-25**:
  what "quiet" means numerically on this box, the 12 samples behind it,
  and the two thresholds `pcrecbench/quiet.py` defaults to. It carries a
  caveat that must not be lost — a genuinely IDLE baseline was not
  obtainable (another session held the box for the whole window), so the
  idle floor is inferred from the quietest-core column rather than
  sampled. Its load finding is the one for the panel: the load1 gate did
  not fire once while the per-core occupancy gate refused all 12 samples,
  so load1 is the WEAKER instrument and occupancy is the detector.

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
