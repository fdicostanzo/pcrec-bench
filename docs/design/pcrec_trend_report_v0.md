# pcrec trend report — requirements (v0.2)

Status: v0.2, 2026-10-09. Asked for by Frank. v0.1 went to pcrecdev1 as
outbox O-93; v0.2 folds in their answer, inbox I-141 (§6 below). Nothing
is built yet. Plan row [B130].

## 1. Purpose

A STANDARD report that regenerates on every pinned bench run and answers one
question: **how did pcrec's numbers move, version by version?** It comes in two
forms over one dataset:

- **A. AI data:** machine-readable pcrec values per pin, with the change from
  the previous pin wherever the comparison is like for like. pcrec's sessions
  and the interpreter read it; nobody has to parse prose.
- **B. Human report:** highlights, charts, and an AI interpretation that is
  clearly labelled as such and cites the A-form rows it rests on.

Today this question is answered by hand, as the cross-pin probes behind O-12,
O-16 and O-92. This report makes it routine.

## 2. Scope

- **Subject:** pcrec testees only, every pinned config (auto, nocaps, vm,
  deny-flag twins, ...). Other engines appear only as DRIFT CONTROLS (R5).
- **Sets:** every `bench/*` set with pcrec records at two or more pins. The
  set@version boundary is handled by R3.
- **Axes:** match time per set cell; compile time; artifact size
  (`emit_bytes` / `emit_code_bytes`); correctness counts (wrong / gave-up /
  unsupported); and the route stamps (engine, prefilter, start, ...), so a
  move can be read beside the mechanism that moved.
- **Out of scope:** cross-engine rankings (the front page and `reports/` do
  that) and pcrec's own regression gate (pcrec's tests/bench/compare).

## 3. Requirements

**R1. One source, the store.**
- Every number comes from `store/` through `pcrecbench.reduce`, the reporter's
  own arithmetic.
- Every row carries the record paths it came from.
- Nothing is typed by hand (the front-page rule, [B127]).

**R2. Pin order.**
- Versions are ordered by `catalogue/rules.toml [[pin_order]]`.
- "Previous" means the newest EARLIER pin that has a comparable record for the
  same config and cell. A pin with no records, e.g. 60366d747 today, is
  skipped and named as skipped.

**R3. Like for like only.**
- A Δ is computed only on cells whose pattern bytes and subject bytes are
  identical across the two records (`canonical_sha256` plus subject sha), on
  the common subjects only. This is the rule O-92 used across
  capability@0.1 -> 0.2.
- A cell that is new or changed reads `new` / `not comparable`, never a Δ.

**R4. Noise rule.**
- A move counts only when the two cells' trial [min, max] ranges are disjoint
  (the front page's tie rule).
- Otherwise it reads `within noise`, and the ratio is still printed.

**R5. Drift control.**
- Each Δ table carries the same-cell ratio of a non-pcrec engine measured in
  both windows (default pcre2-jit, whose version is unchanged). This puts a
  number on box drift.
- If the control's median ratio leaves a declared band (proposed 0.97-1.03),
  the pair is flagged `drift-suspect`.

**R6. Attribution hints, not claims.**
- Each Δ row carries the abi span and the [[pin_order]] notes between the two
  pins, plus whether the program is identical (`program_sha256`, v2 identity).
- Program-identical with a moved time means drift or layout. Program changed
  means pcrec's own change. The report never names a cause beyond these facts.

**R7. Form A, the AI data.**
- TSV files under `reports/trend/`, schema-stable and versioned:
  - `cells.tsv`: one row per (set@ver, config, pattern, regime, form, pin),
    with value, trial min/max, correctness and stamps;
  - `deltas.tsv`: one row per comparable (cell, pin, previous pin), with
    ratio, noise verdict, control ratio, identity and abi span;
  - `summary.tsv`: per (set, config, pin pair): moved-faster, moved-slower,
    within-noise, median and geomean ratio, the largest movers.
- A header carries the generator version, the index sha and the generation
  time.

**R8. Form B, the human report.**
- One page per new pin, plus a rolling index page:
  - top highlights: the largest improvements and regressions beyond noise,
    and correctness changes, especially gave-up -> judged and judged -> wrong;
  - charts: per-set ratio distributions per pin pair, and a per-config
    timeline of the set median;
  - an "AI interpretation" section, labelled as such.
- Published like the front page: HTML on the Pages site, with a markdown copy
  in `reports/`.

**R9. AI interpretation discipline.**
- The interpretation is GROUNDED: every sentence cites `deltas.tsv` /
  `summary.tsv` row ids, or interpreter facts (`pcrecbench interpret`).
- It may connect facts to attribution hints (R6) and name what is NOT known.
- It never states a cause as fact without a citation.
- The deterministic facts are generated first; the prose is generated from
  them, and a check verifies that every cited id exists.

**R10. Updates with runs.**
- `make trend-report` regenerates both forms.
- `scripts/run_window.sh` and the window-close routine call it after a pinned
  window, the way the interpretation sidecars regenerate today ([B41]).
- It runs detached, because it loads the store (KB-16).
- `--check` detects drift between the committed files and the store.

**R11. Corrections.** When a record is superseded, e.g. an
inconclusive-spread record followed by a re-measure, the report uses the
superseding record and says so. It never silently mixes the two.

## 4. Open questions (for pcrecdev1 / Frank)

- **Q1.** Which pcrec configs matter for the TREND view: all pinned configs, or
  auto / nocaps / vm plus the twins of the current acceptance items?
- **Q2.** Should compile time and artifact size get their own highlight
  section, or only appear in A-form data?
- **Q3.** Is pcre2-jit the right single drift control, or should each set name
  its own?
- **Q4.** Does pcrec want the A-form deltas pushed to the outbox at each pin,
  as an O-n pointer, or just committed?
- **Q5.** Should the trend use a single "headline config", pcrec-auto, as the
  front page does, plus a full table?
- **Q6.** Anything pcrec's optimisation loop needs that a per-pin delta table
  does not give? For example, a per-pattern history across many pins, or
  movers grouped by mechanism stamp.

## 6. v0.2: pcrecdev1's answer folded in (inbox I-141)

**Amendments to R1-R11 (all accepted):**
- **R4+.** A disjoint trial range is a WITHIN-window rule. A cross-window
  pair must also clear the identical-program band (R6+); otherwise it is
  flagged.
- **R5+.** Carry the control ratio PER CELL and a drift-suspect cell count,
  not only a median verdict. O-92's control had balanced-parens-rec at
  x1.17 inside a 0.999 median.
- **R6+.** Name the program-identity criterion in the header. Two criteria
  have given 15 vs 16 identical cells; ours is program_sha256 v2, which is
  blind across abi 67's text normalization. Report the count of cells that
  are program-identical AND moved: that is the per-pair noise estimate.
  pcrec's cycle-1 null control saw identical programs move by up to +8.46%
  a day apart.
- **R9+.** The interpretation check draws the cited ids from the TSV, not
  from the generator's own list, so that it shares no source with what it
  checks.

**Q6, additions to the A-form (all accepted; pcrec keeps the cause
bucketing and the carve-out judgement):**
- **R12.** A per-cell competitor ratio at each pin, against the fastest
  automata engine measured in that set and against pcre2-jit.
- **R13.** Movers GROUPED by stamp value (engine, dfa_prefilter, dfa_start,
  req_why, vm_start_scan). The report groups; it never names a cause.
- **R14.** `history/<set>/<config>.tsv`: one append-only row per (cell,
  pin) across all pins.
- **R15.** Regime split everywhere: short-call and throughput medians are
  always separate, never pooled.
- **R16.** Absolute ns on both sides of every delta, plus per-call ns.
- **R17.** A pcrec-supplied cells-of-interest file (mechanism, target
  cells, carve-out cells), rendered as one section per mechanism, plus a
  deny-twin delta (NEW vs DENY at one pin) wherever the deny config is
  pinned.
- **R18.** "Pin gap too wide" when the abi span between two pins exceeds N
  bumps (N to be set at build time).

- **R19 (pcrecdev1, live, 2026-10-09).** INSTRUMENT version per pin.
  - Every cell row carries the sha256 of each bench source that enters the
    timed artifact or loop: `testees/<engine>/shim.c` and `driver.c` (or
    `driver.cc` / `src/main.rs`). Derive them from the record's own
    `run.harness_commit` via `git show <commit>:<path>`; no schema change.
  - A pair whose instrument shas differ is flagged `instrument-changed`,
    the way a wide abi span is, so a harness edit never reads as a pcrec
    move.
  - Prompted by [B132]: O-92's short-search slowdown sits in
    program-identical cells across a window pair where our shim grew.

**Q1-Q5 ruled by pcrec:**
- Q1: configs auto-caps, auto-nocaps and vm, plus the deny twins of the
  current acceptance item. The two auto classes are always separate.
- Q2: size and compile time get a highlights section past a stated
  threshold.
- Q3: pcre2-jit by default; a set may name a second control.
- Q4: commit only, plus an O-n pointer when a pair is drift-suspect or has a
  correctness change.
- Q5: an auto-caps headline and a nocaps headline, plus the full table.

## 5. Not decided here

The TSV column lists, the chart forms and the HTML layout come at build time.
The interpretation's model and prompt get their own short design note before
they are built.

## 7. Implementation note (2026-10-09, lane b130trend, [B130])

Built: `tools/trend.py` (generator), `tools/trend_html.py` (human form),
`tools/trend_cite_check.py` (R9+), `reports/trend/config.toml`,
`make trend` / `trend-check` / `check-trend` (in `make check`),
`tools/tests/test_trend.py` (synthetic store, hand-computed). Outputs and
roles: `reports/trend/CLAUDE.md`. Deviations and decisions:

- **Header.** "Generation time" is replaced by `as_of` (newest record
  timestamp used) so regeneration is byte-identical; the index sha, config
  sha and pin-order sha are in every header.
- **Delta definition.** ratio = new/old of the set-grain median over the
  subjects present in both records with equal subject sha (R3), pattern sha
  equal; "previous" = newest record at a strictly EARLIER pin in
  `[[pin_order]]` (R2) for the same config. Cells whose pattern changed read
  `not-comparable`; first appearances `new`; a state change (gave-up ->
  judged, judged -> wrong, ...) is the `transition` column.
- **Noise (R4/R4+).** `within-noise` when trial [min, max] ranges overlap.
  Disjoint ranges must also exceed the pair+regime band: q95 of |ratio-1|
  over program-identical cells when there are >= 10, else the declared
  fallback 0.0846 (pcrec's cycle-1 null control); else `within-identical-band`.
  A band measured on a pair whose instrument changed inherits the instrument
  bias (it is the bias estimate); the flag says so.
- **Identity (R6+).** `program_sha256` equal -> `yes`; unequal across abi 67
  -> `unknown-abi67`; unequal otherwise -> `no`; missing -> `unknown`.
  Summary carries `n_identical` and `n_identical_moved` (the per-pair noise
  estimate). Highlights list only non-`yes` movers.
- **Drift (R5/R5+).** Control = the pcre2-jit record nearest in time in each
  side's set@version (config `control_globs`); per-cell control ratio on the
  subjects common to all four records; pair `drift_suspect` when the median
  leaves 0.97-1.03; `cell_drift_suspect` outside 0.90-1.10; both counted.
  Same control record on both sides reads `control-same-record` (no ratio).
- **R12.** `jit_ratio` and `auto_best_*` in `cells.tsv` (pcrec / competitor on
  common subjects; best = largest ratio among `competitor_globs` present in
  the set@version).
- **R13/R15/R16.** `movers_by_stamp.tsv` (engine, dfa_prefilter, dfa_start,
  req_why, vm_start_scan; prev > new); every aggregate is per regime; every
  delta carries ns both sides and per-call ns.
- **R17.** `cells_of_interest.tsv` (empty template) -> `interest.tsv` and one
  HTML section per mechanism; `deny_twins.tsv` for every `_no*` config at a
  pin where its base exists (window gap in hours, `cross_window` beyond 24 h).
- **R18: N = 8 abi bumps** (`wide_gap_abi`): `wide-pin-gap` above it. 8 is one
  below the nine-step [OPTLOOP] round 1 (50 -> 59), so that pin step flags and
  routine re-pins do not.
- **R19 (era-aware, manager ruling 2026-10-09).** `instrument` per record is
  `era=N|file:sha12,...` at `run.harness_commit` (`git show`). Era 2 = a
  `testees/<engine>/timed.c`/`timed.cc`/`timed/src/lib.rs` exists at that
  commit ([B133], lane b133loop moves every timed loop into `timed.*`): the
  hashed set is {timed.*, shim.c where present}. Era 1 (every earlier
  commit): {driver.c / driver.cc / src/main.rs, shim.c}. `instrument_changed`
  (boolean, kept) is true when the strings differ; `instrument_changed_files`
  (deltas.tsv, summary.tsv) names the files that differ, plus `era` when the
  two records sit in different eras (a straddling pair is instrument-changed
  by definition). The historical flag stays ~always on (the shim grew at
  nearly every re-pin: 450 of 466 summary rows); it is expected to quiet down
  after [B133], when timed code lives in its own file. Verified on capability
  c4c70f2c -> 255bcdd8: flagged `instrument-changed` and `wide-pin-gap`.
- **Q2** thresholds: emit_code_bytes +-10%, compile total +-25% with disjoint
  ranges (`compile_deltas.tsv`, HTML section). **Q5**: headline tables for
  `auto-caps-simdna` and `auto-nocaps-simdna`, plus the all-config table.
- **Charts:** a dot strip of log ratio per set-regime (circle faster,
  triangle slower, hollow noise; color never alone) and a chained-geomean
  timeline per (config, set) with direct labels. Inline SVG, light/dark.
- **Not built / owed:** `pin_order` notes between pins (R6: only the abi span
  and the pin list are carried; `[[pin_order]]` has no per-pin note field);
  Q4's O-n pointer is the manager's act; the interpretation text and its
  skill (trend_interpretation_v0.md).
- **Regeneration at window close** (manager's routine, after the index
  update and the [B41] sidecars): `make trend` detached with a DONE marker,
  then `make trend-check`, then write `interpretation/<pin>.md` for the new
  pin and `make check-trend`.
- **R18 N = 8** is accepted (manager, 2026-10-09); it stays the
  `wide_gap_abi` constant in `reports/trend/config.toml`.
- **cells.tsv is untracked** (gitignored); `make trend` writes it,
  `trend.py --check` exempts it (`UNTRACKED`) and stays deterministic over the
  tracked outputs. `history/` is the other derivable output (a projection of
  cells.tsv + deltas.tsv); nothing else is untracked.

## 8. Per-version snapshots (2026-10-09, lane b130snap, [B130.2])

Frank's design (approved 2026-10-09): the report compares SNAPSHOT FILES, not
the store, so records become deletable ([B96]) and a regeneration is
deterministic from committed inputs. Built: `tools/trend_snapshot.py` (format,
reader, writer, verifier), `trend.py snapshot` / `links` / the store-free
comparison, `reports/trend/snapshots/`, `reports/trend/links.tsv`,
`make trend-snapshot` / `trend-links`, the skill `/pcrec-bench-report-trend`.

- **One immutable file per pinned pcrec version**,
  `reports/trend/snapshots/<pin>.tsv.gz`: deterministic gzip (mtime 0, no
  filename, level 9), UTF-8 text, tagged rows; schema `trend-snapshot-2`, the
  LOSSLESSLY COMPACT encoding (v1 was 81 MB; v2 is 29.9 MB, same content, no
  rounding). Header: schema, pin, generator, the store index sha and config sha
  at snapshot time (provenance; no clock). `OUT` = the file's outcome-code
  table. `REC` = one row per index record considered at that pin (used /
  superseded / excluded-*, keyed by a short integer `rid`, with machine,
  timestamp, record path, harness commit, **era-aware instrument string** (R19),
  abi, and `data` = `inline` | `ref:<pin>` | `none`). `SB` = the subject table
  (subject id + sha256, stored once per file). Inline records carry `PAT`
  (pattern sha), `CMP` (the compile row: outcome, compile ns, the R13 stamps /
  `program_sha256` / emit bytes / `engine_sel` / abi), `CEL` (the set-grain row
  per cell over all its subjects, keyed `cid`: median, trial min/max, wrong /
  gave-up / no-expectation counts, pattern sha, subject-set sha) and `SUBJ`
  (**per-subject**, `cid sbid iters trials`: the full per-trial list as
  `trial:outcome-code:elapsed_ns` items, `:diag` only when non-empty; ns/call is
  recomputed as elapsed/iters, bit-identical to the original float, checked at
  write time, with an `f<float>` escape). The subject's median is derived
  (`subject_median`), not stored. The per-subject rows keep a pair's
  common-subject rule valid when a set version adds or drops subjects (Frank's
  choice); `CEL` is a self-check that `trend_snapshot.verify_snapshot`
  recomputes.
- **The same window's controls.** A snapshot also holds, for every set@version
  it has a used pcrec record in, the control record(s) nearest in time to those
  records (pcre2-jit by `control_globs`) and every competitor record
  (`competitor_globs`, so R12's fastest automata engine is computable per cell).
  A control/competitor record already stored inline in an earlier snapshot is
  `ref:<pin>`, not repeated (size). The comparison resolves a ref across the
  committed snapshots; the R5 drift control of a pair is the control of each
  side's OWN snapshot.
- **Immutability.** `snapshot` refuses to overwrite (`--force` only on the
  manager's word). `--all-pins` is resumable (existing pins are skipped).
- **The comparison reads snapshots + links.tsv + config.toml only** (plus
  `catalogue/rules.toml` for the pin order). `tools/tests/test_trend.py` deletes
  the synthetic store before comparing and traces every `open()`.
- **links.tsv** replaces what the generator used to infer silently. The old code
  paired a cell with the newest earlier record of the same config and set NAME
  across set versions (capability@0.1 -> @0.2): that is now a `set-version` row
  (an undirected pair of versions). A `config-rename` row (from -> to) reads the
  records of an old config name as the new one (none needed today). A pair that
  would need an unlisted link is `unlinked` in `deltas.tsv` (verdict, `why`
  naming the missing pair, no ratio; `# unlinked_cells: N` in the header; a
  compile/size delta across an unlinked pair is simply not produced). `source`
  is `inferred` (proposed by `trend.py links`, in force, awaiting confirmation)
  or `confirmed`. The skill proposes; the manager/Frank confirms.
- **Headers.** `index_sha256` is replaced by `snapshots_sha256` (over the file
  names + sha256 of every snapshot), `links_sha256` and `links` (count,
  confirmed/inferred). Row ids are unchanged.
- **Differences from the pre-snapshot committed output** (backfill check):
  see docs/dev/lanes/b130snap_report.md.
