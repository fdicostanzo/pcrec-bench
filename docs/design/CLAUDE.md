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
  **CORRECTED 2026-09-12 ([B42], `rxt_needs_v1.md` §1.9 M11):** Q4's
  claim that the pcrec→bench import direction is lossless because
  "`foo_bar` is a legal slug" is WRONG — this project's own slug rule
  (`^[a-z0-9]([a-z0-9-]*[a-z0-9])?$`) has no `_`, so a pcrec block name
  like `iso_ts` is not a legal bench `pattern_id`, MEASURED. §3.2's
  "63 of 77 illegal" count is separately SUPERSEDED: 0/185 at the
  format's now-widened block-name grammar (research note
  `2026-09-12-b42-rxt-as-source.md` §1.2). Neither correction rewrites
  the note otherwise.

- `interpreter_v1.md` — **[B13] the interpreter design note, at **v1.3**
  (2026-09-11, [B41] (c), a HYGIENE revision folding lane `b13impl`'s 17
  build deviations back into the note plus Frank's ruling adding an
  R-ARM-1 `legend` field, catalogue 1.1 — no rule's predicate, threshold
  or `inputs` changed), and since 2026-09-09 **IMPLEMENTED** (lane
  `b13impl`): part 1 is built against it — `catalogue/rules.toml`
  (catalogue 1.1, 31 rules), `pcrecbench/interpret.py`,
  `docs/dev/predictions/`, `catalogue/fixtures/` + `catalogue/golden/`,
  `make check-interpret` (six sections, 129 checks) — and §10's
  acceptance test RAN 25/25. Part 2 (the skill and the
  committed sidecars) is [B13.4]. The design as v1.2 stated it:**
  (2026-09-08, lane `b13v12`): v1.1 revised under the pcrec manager
  session's cross-review of it, inbox I-58 — APPROVED CONDITIONAL, four
  spec edits, no re-panel. In one paragraph each: (1) §2.1's header parse
  now makes the KNOWN-KEY split normative (not "equivalent" to the
  regex-rejoin form, which are shown to diverge in both directions — a
  new header key vs a value that happens to look like `word: `), with
  the regex form demoted to a heuristic note; (2) R-STATUS-3's predicate
  is scoped to `metric = pass_rate`, since precondition P-2's
  `giveup_smallest` rows land in the SAME `excluded` section and would
  otherwise double-fire it once P-2 ships (checked against every other
  reader of that section — only R-STATUS-3 needed the fix); (3) `section`
  is added to §6.3's closed selector key list, which §6.6's own P1
  transcription already relied on without it being declared; (4) the
  R-DELTA-1 aggregate key's `config`/`direction` and R-DELTA-2/3's
  `config` are now declared decompositions in `arith`, extending §7.2's
  table — mechanical firewall bookkeeping, no semantics change. Two
  minors landed in the same commit: an aggregated bullet's rendering is
  now defined for a rule with no numeric slot (a full sorted id list, per
  the specimen's own behaviour) and a rule may declare its own
  `extremal` slot (R-DELTA-1 now uses `ratio`, the biggest mover, instead
  of the default `median_ns`, the largest-median cell); and one honesty
  edit: §6.5's `stated_utc` check now reads the earliest INDEX timestamp
  for the population including superseded records, closing the
  supersession window a report-scoped check left open, with the
  residual limit named plainly rather than claimed away. v1.1 was
  revised in place under every
  disposition of the r4 critic panel
  (`../dev/reviews/2026-09-07-r4-interpreter-v1.md`, 11 BLOCKING +
  8 SHOULD-FIX + ~14 documentation corrections). Still DESIGN ONLY — no
  code, no catalogue file, no skill — but the panel's blockers are
  applied, so an implementation lane can open against it once the
  revision is itself confirmed.** What v1.1 changed, in one list: the
  record row's agreement string is in `value` not `gave_up_summary`
  (B1); `delta_verdict` is a `; `-separated CLAUSE LIST, so R-DELTA-3
  can fire at all (B3); R-STATUS-9 fires on `disagree` ONLY, with
  `n/a (v<schema>)` folded into R-STATUS-6 as age provenance (B2);
  every "group" re-derived from `_ranking_groups`'s real key
  `(subbench, pattern, regime)` — `form` is deliberately NOT in it, and
  v1's cut made R-BUCKET-FORM unsatisfiable (B5); a SEVENTH rule class
  **R-ARM** (same pin, two arms one config token apart, beyond
  `2 × max(stddev)`), which is what makes Frank's `vm-in` acceptance
  item pass by rule instead of remaining "a risk" (B7); R-RANK-3 moved
  to R-STATUS-13 and made R-RANK-1's guard (B6), R-RANK-2 dropped as
  incoherent; an `aggregate` counted-collapse so a modern report renders
  ~44 bullets instead of ~420 (S1); `firing_seq` + `prediction_id` in
  the facts TSV (B9); `[[pin_order]]` as catalogue data (B10); the
  opinion firewall extended to TEMPLATE PROSE with a human-reviewed
  template-diff gate as §8's sixth section, and Q4 ruled (the renderer
  phrases, templates are reviewed prose authored once; the "Reader's
  note" fallback REJECTED) (B11); the golden check pinned to a FROZEN
  index snapshot with a stated table of which commits may fail it and
  who regenerates (B8); the predictions format redesigned and TESTED
  against `bench/syntax/NOTES.md`'s P1-P13 (12 of 13 expressible; a
  `partial` verdict, clause-suffixed ids, `set_of`/`rank_over`, and an
  explicit statement that answers and spans are out of reach) (S2); the
  fixture plan re-cast as generated-base-plus-one-declared-mutation
  mirroring `gen_example_14.py --check`, plus a synthetic CLEAN null
  control (S6, S3); two reporter PRECONDITIONS (a `floor_pattern:`
  header key, killing v1's KB-2-shaped `subbench.toml` read; the
  give-up smallest subject as its own metric rows, killing the one
  string parse) (S8, S4); `grain` mandatory (S7); the `inputs` grammar
  and view contract stated (S5); and R-BUCKET-KB downgraded to a class
  that ships with NO registered signature, with §10 C.3 stated as a
  plain known gap (B4). Underneath, unchanged: `pcrecbench interpret`,
  a deterministic fact-finder over a report TSV + `store/index.tsv`
  (never the markdown), and the `/pcrec-bench-interpret` skill that
  commits a `reports/<name>.interpretation.md` sidecar. Carries the
  versioned rule catalogue's file format (`catalogue/rules.toml`,
  MAJOR.MINOR, with the regeneration rule that keeps a sidecar from
  going stale), **thirty-one rules in seven classes** with each rule's
  exact TSV/index inputs, grain, aggregate key, threshold AND that
  threshold's source in `report.py`/`reduce.py` (no rule introduces a
  constant of its own — R-DELTA reads `_cross_pin_verdict`'s own verdict
  string, R-FLOOR-1 reads `_jitter_flag`'s `timer-floor` token,
  R-STATUS-9 reads `agreement_line`'s `disagree` verdict, R-ARM copies
  `_cross_pin_verdict`'s arithmetic rather than choosing a bound), and a
  worked example per rule citing a real committed report row; the
  OPINION FIREWALL as four structural properties (one `str.format`
  template per rule id whose FIXED PROSE is itself audited, four
  permitted slot-value kinds incl. declared decompositions, links
  validated against committed files, and a human-reviewed template-diff
  gate) plus §0's honest framing — the catalogue is where this
  project's opinions are deliberately CONCENTRATED, not where they are
  impossible; the machine-readable PREDICTIONS format
  (`docs/dev/predictions/<slug>.tsv` — none exists today, checked),
  transcription-tested against P1-P13; `make check-interpret`'s six
  sections; and §10, the ACCEPTANCE TEST — three named committed
  reports plus a synthetic clean null control, with the numbered
  findings catalogue v1 must surface unprompted on each (Frank's
  2026-08-25 blinded test, updated), written down before implementation
  so a later lane cannot weaken it. **One open question remains, Q3
  (should set-local `NOTES.md` bands become catalogue-readable data?) —
  Frank's, pre-existing, untouched by the panel**; Q1/Q2/Q4-Q8 are ruled
  in §11, and two new non-blocking ones (Q9 an exclusion-cause column,
  Q10 where the `[[pin_order]]` append belongs in the re-pin checklist)
  are recorded there. **v1.2 is the design a step-2 confirmation pass has
  now run against** (`../dev/reviews/2026-09-07-r4-interpreter-v1.md`'s
  closing section, run by the pcrec manager session at Frank's ask: 19/19
  dispositions confirmed-resolved or resolved-with-a-flagged-deviation,
  zero silent) — still DESIGN ONLY, no code, no catalogue file, no
  skill; an implementation lane may open against v1.2 once the two
  reporter preconditions P-1/P-2 (§2.5) land.

- `quiet_baseline.md` — **[B3]'s answer to OD-B8, MEASURED 2026-08-25**:
  what "quiet" means numerically on this box, the 12 samples behind it,
  and the two thresholds `pcrecbench/quiet.py` defaults to. It carries a
  caveat that must not be lost — a genuinely IDLE baseline was not
  obtainable (another session held the box for the whole window), so the
  idle floor is inferred from the quietest-core column rather than
  sampled. Its load finding is the one for the panel: the load1 gate did
  not fire once while the per-core occupancy gate refused all 12 samples,
  so load1 is the WEAKER instrument and occupancy is the detector.

- `capability_set_v1.md` — **[B42] phase (b), the CAPABILITY SURVEY SET's
  design, REVISED to v0.2 (2026-09-12, lane `b42rev`): "revised under R5;
  BUILD PARKED on pcrec's `.rxt` delivery (O-26)". DESIGN ONLY: nothing
  built, no file under `bench/`, `schema/`, `pcrecbench/` or `testees/`
  touched.** v0.2 applies every disposition of the R5 D6 critic panel
  (`../dev/reviews/2026-09-12-r5-capability-set-v1.md`: 8 BLOCKING + 8
  SHOULD-FIX + 8 WORTH-NOTING, all ratified) plus three amendments from
  Frank's same-day live rulings: family 11's v1 scope narrowed to the
  shared-convention population pending a harness expectation-override
  that doesn't exist yet (CB1); `variant.kind` rendering corrected from
  "Already built" to UNBUILT, resized as an L5 build task (CB2);
  wild/designed provenance bucketing promoted from a dead `patterns[].tags`
  convention to real enumerated schema fields, `provenance_source` +
  `fidelity` (CB3); `hazard_class` assigned per family, at minimum 2, 5
  and 10 (CB7); family 10's ReDoS calibration risk stated with a fixed
  `--iters` mitigation (CB8); the `match`-regime exclusion's family list
  corrected and its set-wide scope stated explicitly (CS1); `ru_maxrss`
  now RANKED within the native-driver population (CS4); §4.3's ratio
  argument REPLACED wholesale by Frank's ruling that "from the wild" is a
  REALISM framing, not a percentage to hit — every member, imported or
  authored, must be a shape someone would plausibly deploy, families 7-12
  included; and **§9 REPLACED WHOLESALE**: Frank's Q3 ruling
  ("This is as much a driver of the rxt format as anything") withdraws
  N3's Option B entirely — the set is built ON `.rxt` for real, not a
  sidecar hybrid — so §9 is now a POINTER to `rxt_needs_v1.md` (the
  detailed capability feedback already sent to pcrecdev1, outbox O-26)
  and its 41-check restart acceptance checklist, with the six roadblocks
  and the restart procedure stated inline. §12's question list is
  REWRITTEN for the parked state: Q1/Q2 RESOLVED (Frank ruled both live),
  Q10-Q12 SUPERSEDED (moot under Q3), Q3 moved from a silent DEFAULT to
  BLOCK-at-the-restart, Q5/Q6/Q14 keep DEFAULT with stated amendments, two
  new DEFAULT items record design amendments (CB1, CB3) made on this
  revision's own authority rather than Frank's. A full disposition-by-id
  table (24 ids) is in `../dev/lanes/b42rev_report.md`. **v0.1** (2026-09-12,
  lane `b42design`) was the pre-panel draft: thirteen sections against
  Frank's eight charter requirements with a traceability table (§1.1); a
  NEW sub-bench `bench/capability@0.1` rather than an extension of
  `bench/syntax` (§2); twelve families / 60 patterns / 36 short subjects +
  a three-rung size sweep (§3); the provenance/licensing/capability model
  (§4-§5); the rewrite table and hazard rule (§6); the metrics table
  (§7); the config roster incl. `pcre2-dfa` (§8); N3's Option B for
  `.rxt`, since withdrawn (§9, v0.1); what a later public UI would
  consume (§10); the lane plan (§11); fourteen questions for Frank (§12,
  since rewritten); the risk table (§13, since revised). Both documents
  are cited from `../dev/plan.md`'s `[B42]` row. Next: the restart, on
  pcrecdev1's `.rxt` delivery.

- `rxt_needs_v1.md` — **[B42], the `.rxt` CAPABILITY FEEDBACK to pcrec
  (`pcrecdev1`), 2026-09-12, lane `b42rxtneeds`. FEEDBACK, not a design
  of this project's own: nothing is built, nothing under `bench/`,
  `schema/`, `pcrecbench/` or `testees/` is touched, and it revises
  neither `capability_set_v1.md` nor the research note it supersedes.**
  Written on Frank's ruling of the same day (plan row `[B42]`, RULINGS
  Q3): the capability survey set is built ON `.rxt` FOR REAL, not on the
  hybrid; where the format cannot carry what the set needs the effort
  PARKS and this project sends pcrecdev1 detailed feedback; pcrecdev1
  builds it; the effort restarts and this project reviews and VERIFIES.
  Frank: *"This is as much a driver of the rxt format as anything."*
  Five parts. **§0** states the ruling and maps the note onto
  R-BENCH-1..9 (`~/pcrec/docs/design/dd13_format/requirements.md:316-411`)
  — which of the nine it confirms, extends, finds insufficient, or (one:
  R-BENCH-8) CORRECTS. **§1 is THE NEED TABLE**: fifty needs in eight
  blocks (pattern text; identity and descriptive metadata; provenance;
  the capability model; subjects; expectations, conventions and the
  oracle; per-testee variants and the testee roster; set-level identity
  and tooling), each with where it lives today by `file:line`, the
  EXISTING W2/W3 production that would carry it spelled as
  `format_design.md` §1.3 spells it or **NEW** where none does, whether
  that production's designed semantics actually FIT, its wave and status
  at the current pin, and a MUST/SHOULD/COULD priority — 36 MUST, 9
  SHOULD, 5 COULD; 14 BUILT, 2 BUILT AND LOSSY, 20 REFUSED BY NAME, 15
  ABSENT. §1.9 carries THIRTEEN MEASURED facts from twenty parse-only
  probes of the pinned binary (archived with its script:
  `../dev/measurements/2026-09-12-rxt-format-probes-d34c9131.txt`,
  `probe_rxt_format.py`), two of which are SILENT DATA LOSS in shipped
  behaviour (a NUL truncates a `pattern` line; a second `description`
  overwrites the first) and one of which corrects a claim
  `subbench_directory_model.md:554-560` Q4 makes today (a pcrec block
  name like `iso_ts` is NOT a legal bench `pattern_id` — the slug
  alphabet has no `_`). **§2** proposes TWELVE productions — a
  `provenance` block modelled on the `freq` data block's required-line
  discipline, a `vocabulary` declaration that closes a `tag` key's value
  set, a per-config `capable` line, `under <convention>` case
  qualifiers, `@file:` with a subject id and an optional sha256, a
  config-scoping rule for D93, a `pattern-esc` spelling for the bytes
  `pattern` cannot hold, `variant kind` plus a quoted `tag` value,
  `oracle` widened to any engine at a version, `mc`'s counting rule
  stated, a regime mechanism that survives hyphenated ids, and a
  `--list-source` extension for the descriptive productions — each with
  a grammar sketch in the format's own EBNF style, a worked example on a
  real capability-set pattern, and what pcrec's OWN harness gets from it.
  **§3 is the ACCEPTANCE CHECKLIST for the restart**: 41 checks in seven
  groups, every one with a negative arm per this repo's own check-design
  rule, and with the MEASURED BEFORE quoted where one exists. **§4**
  sequences Tier 1 (what blocks a first sample — and says candidly that
  Tier 1 is most of W2 plus part of W3, with W2-alone named as the
  honest smaller cut), Tier 2, Tier 3, and what this project does in the
  interim (nothing under `bench/`; three R5-panel follow-ups that are
  ours regardless). **§5** puts nine questions to pcrecdev1 and three to
  Frank. The Appendix lists the SIX ROADBLOCKS in one table. The
  manager distils an outbox item from this file; the file itself is the
  full form.

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
