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

- `gate_shape_v14.md` — **IMPLEMENTED (2026-08-30, the [B20]
  implementation lane, branch b20-impl): §4-§8 landed as schema v1.4, the
  harness, reporter v9 and the ten selfcheck checks; §9 Q1/Q3 remain the
  follow-ups (the first v1.4 window's target-core distribution; the
  measured positive control as its own plan row).** Before that: SPEC,
  the r3 critic panel applied (2026-08-30, plan row [B20]) (ruled by inbox
  I-19 (1): BD7 ratified as the gate, Frank's (2)-(4) the v1.4 spread
  rule; the panel's 45 findings and the manager's rulings R-1..R-20 in
  `docs/dev/reviews/2026-08-30-r3-gate-shape-v14.md`): record schema
  v1.4 — the pre-flight (BD7's per-core 5-s average, plus the TARGET
  core's own reading as `occupancy.<sample>.target_busy_pct`, a
  TRI-STATE keyed on `pinning.cpu` with a missing target row refused
  BEFORE the run, X26 untouched), the AFTER samples as provenance (X13
  revised by version: `load.before`, `occupancy.before`, the target
  clause, trial agreement; the status-deciding sentence first and never
  elided, today's `note`/`status_detail` split kept), TRIAL AGREEMENT as
  a GROUP rule `v1.4-group` with its constants MEASURED over all 68
  store records (`docs/dev/measurements/2026-08-30-trial-agreement-
  census.txt` the row census, `-census-groups.txt` the group census:
  k = 1.5, a group disagrees at d ≥ 2 and 3·d ≥ n, N ≥ 5 and odd —
  zero disagreeing groups on the store, the margin in k stated as
  0.05-0.10 and the store uninformative above 1.55, the three blind
  bands and the power table stated), the `trial_agreement` setup block
  (`trials`, the group and row counts, `rows_unjudged`, a two-integer
  `worst_group`, verdict `agree`/`disagree`/`n/a-trials`) and the
  `inconclusive-spread` status, §3.5 the arithmetic both
  implementations follow, §3.6 a per-group `/proc/stat` timeline as
  provenance only, the enumerated validator/schema (MINOR under a
  drafted §4 amendment, X13 versioned, X31-X33, KB-4's schema half, the
  examples plan against the examples that exist), harness (the status
  decision table, exit code 4, the `quiet` CLI through `gate()`),
  reporter and check changes (every check with its control), the
  migration (the NINE historical `inconclusive-load` records left as
  history), §9 the three escalations E-1..E-3 (ruled the same day) and the residue; the
  proposal it grew from is kept verbatim as its §H, the panel's summary
  as §H.2. quiet_baseline.md's 2026-08-30 section is what the harness
  DOES now.
- `subbench_directory_model.md` — **[B29] the scoping note, 2026-09-01
  (DESIGN ONLY — no code, no schema change, no sidecar change)**: the
  sub-bench DIRECTORY model's pcrec half against pcrec's
  `--source` / `--target` / `--lib-path` ([DD-13b.W1.2], merged to pcrec
  main as abi 15). What the directory model and its sidecar are today
  and how each field answers R-BENCH-1..9; what W1.2 delivers exactly
  (the four `.rxt` head declarations, the `-o` shape rule, D88's one
  artifact per TU, D93's file-wins-over-flag, `rx_info.name`/`nentries`)
  and what it does not — the sidecar's descriptive needs are the
  format's own W2/W3, which name pcrec-bench as their waiting consumer;
  the field-by-field MAPPING with the two measured obstacles (the `.rx`
  → `pattern`-line encoding is lossless in all 77 files; 63 of 77
  pattern names are illegal as a `.rxt` block name); the compile-cost
  axis the bench cannot give up (one `--source` clock for N targets
  cannot fill N compile rows); and the recommendation — DO NOTHING now,
  an optional exporter only if pcrec wants the artifact, `--source` in
  the adapter not before W3 — with six open questions and who rules
  each. Partially covers the `set_format.md` slot below; see its Q1.

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
