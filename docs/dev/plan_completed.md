# pcrec-bench — completed plan rows (archive)

Rows move here verbatim when they reach STATE:completed, grouped by
completion date, newest group at the bottom.

## 2026-08-24

- [B0] STATE:completed — HOUSEKEEPING (first session, 2026-08-24): the
  docs/{dev,design} shape mirroring ~/pcrec/docs (plan, plan_completed,
  journal, decisions, gitignored wake brief, the pcrec references map),
  CLAUDE.md at every directory level, .gitignore, and the
  `pcrec-bench-manager` project skill (.claude/skills/) modelled on
  pcrec's `pcrec-manager` with this repo's references and the two-session
  box rules. No code.

## 2026-08-25

- [B1] STATE:completed 2026-08-25 (ADOPTED requirements.md v3 after the R1 panel; rulings: narrow blocking scope; variants must reproduce results exactly and preserve the sub-bench objective) — REQUIREMENTS: the overall-requirements discussion
  with Frank (opened 2026-08-24, first session; R1-R11 RULED the same
  evening — docs/design/requirements.md DRAFT v1 written from them;
  the D6 critic panel is the next step, then adoption). Inputs: APPROACH.md (the
  four principles, §8's five open questions), pcrec's R-BENCH-1..9
  (docs/design/dd13_format/requirements.md §5), pcrec [BENCH-1]/
  [BENCH-CEIL]/[ENG-PGO]'s cross-note, Frank's post-spine-loop direction
  (pcrec journal 2026-08-24), the pcrec manager's reference dump (all in
  docs/dev/pcrec_references.md). Output: docs/design/requirements.md —
  what is measured (axes: match throughput, compile/startup cost, latency
  on short subjects, memory later?), for whom (the pcrec optimization
  loop first; positioning second), the testee roster and its admission
  rule, the correctness policy, the artifact's minimum schema, the set's
  sources and versioning, the feedback shape into pcrec's plan, box/
  measurement discipline, public posture; §8 Q1-Q5 each ruled or
  explicitly deferred; then a D6 critic panel on the note before it is
  adopted.
- [B2] STATE:completed 2026-08-25 (MERGED from lane/b2schema b37122b, 6 commits: docs/design/record_schema.md 718 lines, schema/record.schema.json, validate.py X1-X17, check_fields.py, 2 synthetic examples + 15 named sabotages, make check-schema 2/15/0; accepted at merge: per-subject crashed/timed-out, dense trial numbering, lazy-JIT derivation row; S1/S2 critic panel → 22 findings → schema v1.1 MERGED ae9b0d0 from lane/b2fix 1962ac8: 27 rules / 53 controls / check_rules.py; review docs/dev/reviews/2026-08-25-r2-record-schema.md) — THE RECORD SCHEMA (APPROACH §3, §8 Q2; requirements.md §2, §4.2-4.4, §6):
  the versioned per-testee output file — environment header (CPU, kernel,
  compiler, load/quiet-box attestation, per-core occupancy), per-case
  compile outcome / match outcome / correctness verdict / timings with
  COMPILE and MATCH separated — plus the tiny validator the comparator
  shares. Design note → panel → ruled.
- [B3] STATE:completed 2026-08-25 (MERGED 42c0557 from lane/b3harness f437952, 18 commits; make check 21/21 on master; docs/design/harness_notes.md + quiet_baseline.md; OD-B8 measured under load: occupancy is the detector, load1 the backstop — proposed limits busy ≤ 10 %, load1 < 2.0, re-measure quiet) — THE HARNESS CORE: the sub-bench DIRECTORY
  conventions (goal, canonical patterns, generated subjects + manifest,
  expectations with verification method, tags, engine notes and
  declared variants, regime declaration), the run-cells driver (one
  cell or a chosen few, never the gamut), the store layout + index
  (OD-B6), and the QUIET-BOX INSTRUMENT — load before/after, mpstat
  per-core occupancy machine-readable, the numeric meaning of "quiet"
  MEASURED on this box (OD-B8). The pattern/case FORMAT is owned by
  pcrec's [DD-13] and is NOT invented here (requirements.md §5); under
  Frank's NARROW blocking reading this row may parse today's `.rxt`
  as-is and wrap the email specimen's files as the first sub-bench with
  a plain per-sub-bench sidecar (R-BENCH-1..9 fields, no grammar);
  under the BROAD reading it wraps the specimen's files only.
- [B4] STATE:completed 2026-08-25 (MERGED with [B3] at 42c0557: testees/pcre2 interp+jit via a dlopen driver; testees/pcrec auto/nocaps/vm pinned at 8da6120 via pin.sh, the (?:P)\z whole-subject artifact with `form`, give-up range rule from the artifact's exported PCREC_ERR_FLOOR; pcre2 give-up set {−47,−53,−63,−46} measured; two pcrec findings filed with the pcrec manager: no DFA prefilter stamp, the \z skip loop cannot skip the last byte) — TESTEE ADAPTERS, first two (plus OD-B10, the large-subject size measured at 1 MB vs 8 MB): pcrec (as its
  several configuration testees, pinned by commit) and libpcre2 (interp AND
  jit as separate testees). Each pins its version and records build flags;
  "unsupported" is a first-class per-case result.
- [B5] STATE:completed 2026-08-25 (MERGED from lane/b5report 0d6ab1d: pcrecbench/report.py, --grain set|subject, gave-up apart from wrong, form beside numbers, lazy-JIT over lowest seq, 18 tests + v1.1 fixtures, make check-report; the manager resolved the Makefile/__main__/__init__/CLAUDE.md seams — report dispatched before argparse; make check on master = schema 2/53/0 + harness 21/21 + report 18/18) — THE REPORTER MVP: static over two or more
  artifacts — per-case diffs, per-tag rollups, correctness disagreement
  tables, rankings that exclude wrong answers by default. Never runs an
  engine.
- [B6] STATE:completed 2026-08-25 (the FIRST PRODUCTION SAMPLE: five `measured` records for email-specimen@0.1 in pcrecdev1's quiet window 02:22-02:56 EDT, 5 trials, CPU 11, pin 8da6120; reports/2026-08-25-email-specimen-0.1-budu-ryzen1600.{md,subject-grain.md,tsv}; commit bf4a415; sent to pcrecdev1 with the feedback request and the higher-priority-sub-bench question; findings: pcrec-vm beats pcrec-DFA 2.3× on whole-subject compliance; factored loses 5.4× on short search (wave-G target); U1 pcre2-jit timeout on factored × 1 MB 'a') — THE FIRST HONEST DIFF and the first feedback
  row into pcrec: run the two adapters on set v0 on a quiet box, compare,
  and hand the pcrec manager the first outlier in the agreed feedback
  shape. Closes M1 as APPROACH §8 Q5 proposed it.

- [B8] STATE:completed — RE-PIN pcrec to `692c2e8` (inbox I-1; the
  [DD-14] close merge, compiler byte-identical to `17469b6`, the tree the
  battery was scored on: matrix 180/0/6/0, test 26,560/0, san both axes).
  Steps: testees/pcrec/configs.toml `pin`; the adapter records `abi` as a
  pair (no `== 2` check exists — verify the new records say 3 and that
  the four FB sizing fields and `_FRAMES`/`_FRAME_SIZE` land in
  `engine_metadata`; a stamped 0 means no buffers); pin.sh builds
  build/pcrec-692c2e8/; the five email-specimen cells in a new quiet
  window (WINDOW OPEN/CLOSED handshake with pcrecdev1, --trials 5); then
  the FIRST BEFORE/AFTER report over both pins. Expected: factored/
  short-search collapses to orig's (wave G — one DFA artifact); if it
  does NOT, that is pcrec's first real outlier; FRAMES give-ups on the
  five deep subjects remain until a caller-provided frame buffer is used
  (pcrec D73). BUILT (lane b8repin, merged 08602ed): generic `_in`
  plumbing (any config may carry `buffer_frames`/`buffer_trail`,
  capacities never bytes); `pcrec-vm-in` is the MEASURED roster entry
  (at 692c2e8 `auto` selects the DFA for both email patterns, so
  `pcrec-auto-in` is defined but inert here — not measured); capacities
  32768/131072 chosen by measurement (s-059 needs 10245/46100); contract
  pcrec docs/spec/match_api.md §10; the record carries the capacities
  used. Remaining: the six-cell window run and the before/after report.
  DONE 2026-08-25 (second session): merged 08602ed; the window run
  0cf336c (six cells 13:34-14:10 EDT, CPU 11, 5 trials; pcre2-jit,
  pcrec-vm, pcrec-vm-in `measured`; pcre2-interp, pcrec-auto, pcrec-nocaps
  `inconclusive-load` on a 1-s AFTER-sample transient — re-measure in the
  next window); the before/after report
  reports/2026-08-25-email-specimen-0.1-budu-ryzen1600-repin-692c2e8.*.
  RESULT: factored/short-search collapsed 84,076 → 6,284 ns/call (= orig;
  2.4× faster than pcre2-jit); factored compliance and throughput now 100 %
  under auto; vm-in completes the five deep subjects; NEW finding: vm-in
  beats vm on every regime at the same pin (outbox O-4).

- [B9] STATE:completed — REPORTER FOLLOW-UPS from pcrecdev1's feedback
  (feedback_pcrecdev1_2026-08-25.md §1a/§1c/§2a) + the open OD-Bs:
  (1a) the artifact's strategy stamps (`RX_ENGINE`, `RX_ENGINE_WHY`,
  `RX_VM_PREFILTER`, `RX_VM_RUNGS/STRATS/PRUNES`, `RX_VM_CALL_*`) as
  bucket COLUMNS — the records carry them as `engine_metadata` pairs;
  build against the VM stamps now, the DFA stamps pick up on the pin
  that ships inbox I-3 (pcrec-owned, behind [CHK-1]; until then DFA rows
  bucket by `rx_info.engine` only); (1c) the compile axis split by phase
  (pcrec / gcc / dlopen — in every compile row already); (2a) the
  match-compliance `whole-subject` result bucketed as a REGIME ARTIFACT
  (the `\z` form is a different program from ANCHORED|ENDANCHORED),
  kept out of the outlier queue until pcrec [OS-4]; OD-B11 (labels for
  `timed-out`/`crashed`), OD-B13 (`--subbench` accepts the directory
  name as well as the sidecar id), OD-B12 (a --wait-quiet retry /
  multi-sample gate — the transients are the managers' own processes;
  pcrecdev1's suggestion: per-core busy AVERAGED over the cell, or a
  load1/nproc ratio, instead of a 1-s sample). NEW from the [B8] sample:
  OD-B14 — the reporter shows NO record `status`: `inconclusive-load`
  records rank beside `measured` ones unmarked (show the status per row,
  exclude non-measured from rankings by default with a flag to include);
  OD-B15 — two records of the SAME testee_id in one query (pcre2 at two
  dates): the reporter neither states nor lets the reader choose whether
  it pooled trials or took the newest — rule it, state it in the header.
  From pcrecdev1's repin feedback (docs/dev/feedback_pcrecdev1_2026-08-25-
  repin.md §2, all columns): form semantics (same program / separate
  artifact) as a column — the regime-artifact bucket IS that fact; ratio
  vs best AND vs the named baseline; per-subject mean + timer floor on
  short-search rows; give-up code + smallest firing subject per cell;
  a cross-pin Δ verdict column (collapsed / unchanged within noise /
  regressed) + a worst-subject line per cell; mechanism stamps incl.
  the ENTRY used and buffer sizes; compile phases split; a "stddev >
  median = timer jitter" flag on compile rows.
  DONE 2026-08-25 (lane b9report, sonnet; merged): reporter v2 — status
  per row + non-measured unranked by default (--include-unmeasured);
  newest MEASURED record per testee wins, newer non-measured listed
  (--all-records); tier-aware (scratch unranked, --include-scratch);
  form-semantics column (same program / separate artifact) + the
  regime-artifact statement; ratio vs baseline AND vs best; per-subject
  mean + floor note; give-ups by code with the smallest firing subject;
  cross-pin Δ verdict column + worst-subject line; mechanism-stamp and
  compile-phase columns + jitter flag; --subbench by directory; the two
  committed reports re-rendered (`reporter: v2` header); 31 tests;
  OD-B11/B13/B14/B15 closed; imports pcrecbench.reduce (shared with
  quick). OD-B12 (the gate) stays open.

- [B10] STATE:completed — THE EDIT-TEST LOOP (inbox I-4, Frank's
  ruling; AFTER [B8]; in this order): (a) a SCRATCH TIER for records —
  same schema, one setup field (`tier: scratch` + what the binary was),
  a scratch store the reporter can read but that NEVER enters `store/`,
  `store/index.tsv` or the rankings; pinned records stay canonical
  exactly as today; (b) `pcrecbench quick` — one cell (one pattern × one
  regime) against one or two testees, a scratch record, the comparable
  printed inline; seconds, no report file unless asked; (c) a
  `pcrec-local` testee — `PCREC_BIN=/path` + extra flags, no pin.sh;
  `version` = `local:<sha256 of the binary>` + the tree's `git describe
  --dirty` when a repo sits beside it; scratch-tier BY CONSTRUCTION
  (the adapter refuses the canonical store). Division of labour (pcrec
  D78 / BD5): this session BUILDS the bench; the pcrec manager RUNS it
  from a worktree of this repo (never a clone). Scratch runs are light
  and announce nothing; pinned runs keep the window handshake.
  DONE 2026-08-25 (lane b10loop; merged): schema v1.2 (`tier`
  pinned|scratch, absent = pinned; `testee.binary`; `local:` versions;
  X28/X29 with failing examples; 3/55/0); store/.canonical marker with
  write() AND index() refusals proven by sabotage; `run --tier scratch`
  → build/scratch-store/ (gate skipped, box still sampled, status
  honest); `pcrecbench quick` (one pattern × one regime × first-k
  subjects, 1-2 testees, 3 trials, 2 s calibration budget, the
  comparable inline via the shared pcrecbench/reduce.py; ~5-8 s);
  `pcrec-local` ($PCREC_BIN + $PCREC_LOCAL_FLAGS, `local:<sha12>[+describe
  --dirty]`, engine_commit null when dirty, scratch by construction, the
  canonical store refused); 50 harness checks.

- [B15] STATE:completed — THE PER-CALL FLOOR PATTERN in every short-subject
  set (pcrecdev1 feedback 1d/1a, both readings; the reporter's "floor:
  n/a"): bench/email gains `floor.rx` = the literal `@` with sidecar
  `role = "floor"` (default `member`), oracle-derived expectations over
  the same subjects (all three regimes), manifests/NOTES/CLAUDE.md;
  schema v1.3 (additive): optional `patterns[].role` enum member|floor,
  the harness copying it from the sidecar; the reporter ([B14]) prints
  the floor pattern's per-subject mean beside every short-search row of
  the same record. Plus KB-1 (runtime_options bare-flag pairing) in the
  pcrec adapter with a check. Lane b15floor (sonnet); disjoint from
  report.py. Design rule for [B11]+: every set carries a floor pattern.
  DONE 2026-08-25 (lane b15floor, sonnet; merged bf4949d): floor.rx =
  `@`, role floor; expectations 330 → 495 rows oracle-derived (search 73
  match / 4 nomatch; match 1/84; throughput 40330 / 0 / 0 find-all); 80
  of 85 subjects contain `@`; schema v1.3 `patterns[].role` + X30
  (3/56/0); harness stamps the role; KB-1 FIXED; requirements §5 and
  APPROACH §3 state the rule; make check 3/56/0, 56/56, 31/31. Scratch,
  under load, direction only: on the floor pcre2-jit is SLOWER than
  pcrec-auto (3,440 vs 1,468 ns per 77-subject set ≈ 45 vs 19 ns/call)
  — pcre2's per-call setup exceeds a dlopen'd C call; a pinned floor
  record is the next window's business.

- [B14] STATE:completed — REPORTER FOLLOW-UPS from pcrecdev1's reading
  of the reporter-v2 repin report (docs/dev/feedback_pcrecdev1_2026-08-25-
  repin-v2.md §1, §2, §4): print the STAMPED DEFAULT capacities
  (`resume_frames`/`trail_frames`) on plain-entry rows where
  `buffer_frames`/`buffer_trail` now print "-" (the plain entry HAS a
  buffer — its size is what [OPT-1]'s cost is proportional to); a 3-row
  per-subject sub-table for sets of ≤ 3 subjects (throughput) + ns/byte
  beside ns/call; the MATCHING-subject count per compliance cell; the
  artifact SIZE (emitted bytes) as a compile-cost column; `jitter`
  computed (stddev/median, or "timer-floor" when min < 20 µs) or dropped;
  `resume_frame_size` legend: `-` = not stamped at that pin, `0` =
  stamped no buffers (render `0 (DFA)` / `n/s`); "Δ detail: worst
  subject" — say whether it is the new record's worst or the largest Δ,
  print both when they differ; SHORTEN: the superseded-record ids in the
  header → a count + "--all-records lists them"; the per-testee constant
  columns of the compile-cost table → a one-line-per-testee legend above
  it. When pcrec's I-5 pin (abi 4: RX_ENGINE unconditional, RX_DFA_SCAN,
  RX_DFA_PREFILTER) ships: the DFA stamp columns (I-3 closes). Sonnet
  lane; disjoint from everything but report.py/tests/reports.
  DONE 2026-08-25 (lane b14report, sonnet; merged): reporter v3 — stamped-
  default capacities on plain-entry rows; `n/s` vs `0 (DFA)` legend;
  per-subject sub-tables + ns/byte for ≤3-subject sets; matches m/n on
  compliance groups (from the sub-bench sidecar — KB-2: derive from the
  record instead); computed jitter (ratio / timer-floor), empty columns
  dropped; worst-now vs largest-Δ; artifact-bytes column; per-testee
  legend replacing repeated columns; superseded list collapsed; the
  floor column wired to `patterns[].role`; 41 tests; both report sets
  re-rendered. DFA stamp columns wait for pcrec's I-5 pin.


- [B17] STATE:completed (2026-08-28, merged as the parent of a78d1cc; email-specimen@0.2; measured in the abi-8 window of the same day) — NON-PERIODIC THROUGHPUT SUBJECTS (inbox I-10): `bench/email` gains at least one non-periodic 1 MB subject per throughput construction (matching-bearing prose with drawn word lengths and a low density of addresses; failing prose with no `@`), generated with a recorded seed, beside the periodic three (kept: they isolate the steady-state loop); `manifest_throughput.tsv` gains a `periodic` column (the period in bytes, or `no`) so the interpreter can flag "branch-predictor-friendly" beside a per-byte number; expectations re-derived. A SUBJECT change bumps the version (requirements §5): `email-specimen@0.2`; measured for the throughput regime in a second window after [B16]'s at 0.1 (the cross-pin ledger stays at 0.1; the periodic/non-periodic contrast is within-pin at 0.2).

- [B16] STATE:completed (2026-08-28: adapter + reporter v5 merged bbcd7ae; the window ran 10:16-10:59, six cells measured, reports/2026-08-28-email-specimen-0.2-…-repin-35e1ab1.*; the ledger is journal third session part 5 — P1-P3, P7-P9', P11 hold; P5, P6, P10' do not; I-10's confound measured at 1.64×) — RE-PIN to pcrec `35e1ab1` (abi 8; inbox I-5, I-6, I-11, I-12, I-13 — one adapter change for five pins, as I-5 asked). Adapter: `configs.toml` pin; the shim reads `RX_DFA_SCAN` / `RX_DFA_PREFILTER` (abi 4+), `RX_FAST_FRAMES` / `RX_FAST_TRAIL` (abi 5+, VM-only), `RX_DFA_TABLE` (abi 7+), and `rx_info.scan` / `.prefilter` (abi 6+, appended fields) — never inferring an engine from a stamp's ABSENCE (I-5's hazard); METADATA_DECL grows the same way. Reporter: the DFA mechanism columns; I-7 §3's two legend rules (an unstamped pin's engine printed as "inferred"; a give-up code that names the other engine, or a compile-cost class that contradicts it, turns a cross-pin Δ into "selection changed"); I-7 §5's "max is trial 1" fact beside jitter and the "dominated" flag on a set-grain ratio when one subject is >90 % of the sum. Then THE WINDOW (the manager runs it): six cells + the floor pattern at `email-specimen@0.1` against the 692c2e8 records — the ledger of predictions P1-P7 (I-7), P2's exact figure (I-8), P8'-P11' (I-11) tested one by one in the report/journal; the pinned floor row (P7). Reports re-rendered.

- [B11.1] STATE:completed (2026-08-28: built by lane b11loglines, merged; measured the same day in window C — six cells at pcrec 35e1ab1, reports/2026-08-28-loglines-0.1-…-first-sample-35e1ab1.*; the number: the required-byte precheck is ~parity on the search band, the real outlier is the offset-k prefix scan — journal third session part 6, outbox O-7 items 4-6) — SUB-BENCH #2: LOG-LINE SEARCH (`bench/loglines/`, 2026-08-28). THE NUMBER THIS ROW EXISTS TO PRODUCE (inbox I-7 §1, pcrec [OPT-5]): on mostly-FAILING 256 B–4 KB subjects, what pcrec's DFA pays for having no REQUIRED-BYTE (any-position) precheck where pcre2-interp dismisses a subject at memchr speed — the regime where that dominates; the number decides pcrec's build (pcrec D77). Shape: typical ops patterns (timestamps, IPv4/IPv6, key=value, quoted fields, a status-code/level filter, a multi-token "error with context" shape), each with a documented REQUIRED literal where one exists and at least one pattern with NONE (the control: a required-byte precheck cannot help it); subjects = generated log lines, NON-PERIODIC by construction (drawn field lengths and vocab, seeded generator, seed + `periodic` fact recorded in the manifest — I-10), a matching-rate per pattern that is low (the 95 % path) but not zero; a size sweep for the give-up outcome (256 B → 4 KB → beyond, until any testee gives up, the first size recorded — I-2 §1b); the FLOOR pattern (one literal, `role = "floor"`, the rule since [B15]); oracle chain as bench/email (`gen_expectations.py` from libpcre2, `--check` mode, sha256 manifests, `make check` coverage). Patterns authored from the GOAL (D27-style: the author reads no pcrec source or corpus). Measured in a window after the [B16] re-pin so the number is at abi 8.
- [B18] STATE:completed (2026-08-29: (e) lane b18repin merged a541cbf, 107/107 after all merges; (a) MEASURED — 12 cells every one `measured` after three re-runs, store index 41, reports `reports/2026-08-29-*-repin-36d5963.*`; (b) level-context = the VM, 13.4× behind the JIT, compile pays the DFA attempt first; (d) the probe archived under docs/dev/measurements/; the ledger read and every finding → outbox O-8 (739ccdd); journal fourth session parts 1-3) — RE-PIN pcrec **36d5963** (abi 11; inbox I-17 superseding I-15 8ab6152 abi 9 and I-16 808740c abi 10) — lane b18repin, 2026-08-29. ONE adapter change absorbing three pins, as [B16] did: (e) `shim.c`/`adapter.py`/`driver.c` read the abi 9-11 stamps BY VALUE — `RX_DFA_PREFILTER`'s new values `offset-set` / `offset-set-bounded` (I-15), the unconditional `<P>_DFA_PREFILTER_OFFSETS` (`"0,8*,13"` / `"none"`), `RX_DFA_MATCH` ∈ {`unwrapped`, `search-filter`} on DFA artifacts only + `rx_info.match_form` (I-16), `<P>_MAX_EMIT_CODE_BYTES` / `<P>_MAX_EMIT_BYTES` on every artifact and `<P>_UNROLL_K` / `<P>_UNROLL_K_WHY` (seven values) on every VM artifact (I-17); the deny flags `-fno-offset-skip` (bit 16), `-fno-anchored-dfa` (bit 17), `-fno-size-term` (bit 18) as the CONTROL builds; the flag/stamp map derived from (or checked against) `pcrec --list-axes` (47 rows / 19 axes at abi 11) instead of a hand table; `PB_SHIM_MIN_ABI` raised iff the shim reads a field appended after 6; `make check-harness` asserts the new stamps by value on a real artifact of each kind (a k-set skip artifact — loglines `uuid` should stamp `"0,8*,13"`, `iso-ts` `"0,4*"`, `stack-frame` `"0,1*"`; a declined one `"none"`; `unwrapped` vs `search-filter`; `K=8`/`default`), the `-fno-*` controls reaching the other value, and the sabotaged-abi refusal as before; the [SEL-1] fallback: loglines `level-context` under `pcrec-auto` now COMPILES as a VM artifact with `RX_ENGINE_WHY "dfa overflowed: …"` — the reporter must bucket it (the mechanism stamp), and [B12]'s did-not-compile ranking line stays for the next such cell. (a) THE WINDOW: re-measure email-specimen@0.2 (six cells) and loglines@0.1 (six cells) at 36d5963 into `store/`; reports `reports/2026-08-29-*-repin-36d5963.*`. THE LEDGER (pcrec's stated predictions, read PER SUBJECT against the 35e1ab1 records): [OPT-K] on loglines search band — stack-frame 10.18×/6.19× (match/fail arms), uuid 4.45×/9.58×, iso-ts 6.13×/5.75× faster than at abi 8; ipv4 1.02×, hex32-id 1.00×, http-5xx 1.01× (controls within spread); ipv6/kv-quoted/bignum declined (`"none"`); the three outliers to within 2× of pcre2-jit on the search band (I-14 (ii)); BOTH email patterns declined — email search rows flat; DFA artifacts +1.4-1.9 KB where selected, +40 B declined; gcc time ±5 %. [ENG-ABS] on email MATCH regime — matching subjects DFA/VM 1.031× [r41 1.036×] from 2.077×; the 35 short valid emails 0.482× [0.489×] (DFA 2.07× faster than VM, from 1.207× behind); ALL 85 2.132× → 1.161×; non-matching 2.306× → 1.550×; SEARCH rows flat (nothing in `_search` moved at abi 10 or 11); DFA artifacts +2,605 B source median but `.o` +2-11 % of that; VM +63 B. [ART-SIZE]: 54/54 bench emits accept, 0 K movements (every VM artifact `K=8`/`default`), largest artifact 76,304 B, `level-context` 22,905 B; ordinary compile cost unchanged. (b) FRANK'S ASK (I-15 b, I-17 b): for every pattern where auto's DFA fallback trips (`RX_ENGINE_WHY` starts "dfa overflowed"), pcrec-auto (a VM artifact) vs pcre2-jit — `level-context` first, out of the loglines window (at 35e1ab1 the VM was 1.55 ms/set vs the JIT's 115 µs, 13.4× behind — the prediction is that pcrec-auto now equals pcrec-vm there). (d) I-16 (c) / I-17 (d): a LONG-SUBJECT FAILING-`_match` probe — a failing anchored match at byte ~3 of a 1 MB subject (pcrec: 5.5 ns flat at every length vs 1.99 ms before, O(divergence)); bench/email's `throughput` regime is search-only and adding `match` to it would bump the version and break (a)'s comparability, so this is a SCRATCH-tier probe first (`quick` if it can address the throughput subjects in the match regime; else an archived driver probe, D35 style) reported in O-8, and a set change only as a ruled item. Outbox O-8 carries the ledger outcomes, the fallback row and the probe.
- [B11.4] STATE:completed — (COMPLETED 2026-08-30 ~07:3x EDT: MEASURED at 36d5963 6/6 (store 50, reports 0c2d9a2), the ledger docs/dev/ledgers/2026-08-30-bounded-0.1-first-sample-36d5963.md, outbox O-9 sent (six ranked candidates, six asks; the three numbers this row exists to produce: (1) the compile axis — emit-c O(n^1.8-2.0) vs a linear .so at ~12 B/count, the wasted DFA build ×315-×687, K moved once (nest3-16, depth not product); (2) the K23/K32 band — all four ctx rungs VM in both forms, 4-5× behind the JIT in search, the [SEL-1] fallback exactly the forced VM; (3) the refusal — 65535 by the NFA cap (not the emit cap), auto refusing what pcrec-vm builds in 2.9 ms; KB-3/KB-4 filed; the AFTER sample is [B19] (b); the split-axes question deferred to a 0.2 with the O-9 (iii)/(vi) rungs if pcrec asks for them) — 2026-08-29: BUILT and MERGED 485a230, lane b114bounded, blinded; 24 patterns, 30 + 4 subjects, 1536 expectations, `oracle_limits.tsv`, predictions on record in NOTES.md; the author recommends SPLITTING the two axes into two sub-benches — a scope ruling for the manager; FIRST SAMPLE 2026-08-30 00:21-01:21 EDT at 36d5963: 3 measured (pcre2-interp, pcrec-nocaps, pcrec-vm), 3 inconclusive-load on the 1-s after-sample alone (pcre2-jit, pcrec-auto, pcrec-vm-in) → re-run under BD7 as the gate-shape TEST RUN after pcrecdev1's battery 3; the first cell was also lost once to the note-length harness bug, 3bda38b; I-18 MEASURED the class ladder at 96e44c2 — the set's predicted first refusal at the 32768 rung is RESCUED there (a 32 KB VM artifact, prefilter `[a-z]*`, `_ENGINE_SEL collapsed-prefilter`) and 65535 is refused by the NFA cap (131072 states) at EVERY pin including 36d5963, so this sample's `did-not-compile` rows read: 65535 = the NFA cap, 32768 = the abi-11 size cap that abi 12 rescues; the AFTER sample is [B19] (b)) SUB-BENCH #4: BOUNDED-REPEAT (`bench/bounded/`, 2026-08-29, lane b114bounded, a BLINDED author — D27 discipline as [B11.1]). THE NUMBERS THIS ROW EXISTS TO PRODUCE: (1) the COMPILE axis of bounded repeats — pcrec's counter-rung body replication under NESTED bounded repeats is where every artifact-size outlier in pcrec's own census lives (inbox I-15 (c): `.o` median 6.8 KB / p99 14 KB over 2,772 patterns; I-17: two size caps + a K ladder now decide the artifact, and the `.o`-size column on THIS set is the design input for the size term); (2) the MATCH axis in the K23/K32 band — a bounded lazy repeat before a `\b` alternation reaching the DFA's 32,000-state cap under `auto` (loglines `level-context`, the [SEL-1] witness) and large DFA-side counts like `[a-z]{0,30000}` (pcrec [ENG-COUNT], filed unscheduled 2026-08-29, "would find its measured need here if one exists"); (3) the give-up / refusal as a FIRST-CLASS outcome with the count at which it first fires (I-2 §1b: a count sweep, not a size sweep, is this set's sweep). Shape: everyday shapes with bounded counts (fixed-width fields `\d{4}`, hex ids `[0-9a-f]{32}`, line-length and password rules `.{8,64}` / `.{80,}`, a bounded-context "error … cause" shape `.{0,200}?`), plus a count LADDER on a few skeletons (greedy/lazy, class/literal/group body, nested `(?:X{a,b}){c,d}`, `{n}` / `{n,m}` / `{n,}`), counts from small to huge; every set carries the FLOOR pattern; expectations oracle-verified by the shared chain (`pcrecbench/expectations.py`, `--check`, sha256 manifests, `make check` by enumeration); subjects generated, non-periodic (`periodic` column), matching and failing arms both present; no pattern copied from pcrec's tests or corpora (the author is denied them). Measured in a window after [B18] lands so the number is at abi 11.
