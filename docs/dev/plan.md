# pcrec-bench Project Plan

Working plan derived from ../../APPROACH.md. Row ids carry a `B` prefix so
they never collide with pcrec's `[Mx.y]`/`[DD-n]` rows in cross-references.

## Step-state format (grep'able)

Every step line matches exactly:

    - [Bn] STATE:<state> — <title>

States: `not-started` | `started` | `completed` | `blocked` | `deferred`

Find work:

    grep -n "STATE:started" docs/dev/plan.md
    grep -n "STATE:not-started" docs/dev/plan.md
    grep -c "STATE:completed" docs/dev/plan_completed.md

Completed rows are archived in docs/dev/plan_completed.md (this file keeps
zero STATE:completed rows).

Rules: update the STATE tag in place when a step changes state; expand a
milestone into substeps only when work on it begins (replace its single
`[Bn]` line); note blockers inline after the title with `(blocked: reason)`.
Milestones start with Frank; nothing below [B1] starts unprompted.

## Queue

M1 ([B0]..[B6]) is COMPLETE and archived (2026-08-25). The rows below are
the M2 queue: [B8]..[B11] transcribe the pcrec manager's inbox items
I-1..I-4 (docs/dev/inbox_from_pcrec.md, Frank's rulings of 2026-08-25)
and pcrecdev1's feedback on the first sample
(docs/dev/feedback_pcrecdev1_2026-08-25.md); [B7] and [B12] carry the
older candidates. Proposed order (Frank confirms): [B8] → [B10] (ruled
"after the re-pin", in its (a)(b)(c) order) ∥ [B9] (a disjoint reporter
lane) → [B11] sub-bench #2 → the rest. Nothing starts unprompted.

- [B11] STATE:started — (2026-08-28: #2 DONE as [B11.1], archived. 2026-08-29: #4 BOUNDED-REPEAT ruled NEXT — inbox I-14 (iv) recommended, I-15 (c) and I-17 (c) confirmed with Frank's "advance these bench requests" — expanded as [B11.4] below; #3 wide alternations follows it as [B11.2]; Frank's ruling that the pcrec manager may run bench sessions AS the bench when pcrecdev2 is down — one repo per session) SUB-BENCHES #2..#6, in Frank's ruled order
  (inbox I-2): (1) LOG-LINE SEARCH, 256 B–4 KB subjects, mostly-failing
  (the 95 % path): timestamps, IPv4/IPv6, key=value, quoted fields,
  typical ops patterns; (2) WIDE ALTERNATIONS / keyword tries (10, 100,
  1000 words; mixed lengths; common prefixes); (3) LOOKAROUND +
  BACKREFERENCE real-world shapes (password rules, HTML/XML tags, CSV
  with quoted fields, `(?<=...)` at 1 KB; pcrec's tests/lookaround as
  seed input, read-only); (4) BOUNDED-REPEAT / K23 / K32 band —
  compile AND match axes; (5) UTF-8 classes/properties — LAST (M5 is
  unbuilt in pcrec; today it would measure a missing milestone). Every
  set carries a per-call FLOOR control pattern (feedback §1d) and the
  give-up as a first-class outcome with the size at which it first
  fires (§1b: a size-sweep design item). Blinded set authors (D27-style)
  where the set has expectations to write. Expand into [B11.n] when
  work on the first begins.
- [B11.4] STATE:started — (2026-08-29: BUILT and MERGED 485a230, lane b114bounded, blinded; 24 patterns, 30 + 4 subjects, 1536 expectations, `oracle_limits.tsv`, predictions on record in NOTES.md; the author recommends SPLITTING the two axes into two sub-benches — a scope ruling for the manager; FIRST SAMPLE 2026-08-30 00:21-01:21 EDT at 36d5963: 3 measured (pcre2-interp, pcrec-nocaps, pcrec-vm), 3 inconclusive-load on the 1-s after-sample alone (pcre2-jit, pcrec-auto, pcrec-vm-in) → re-run under BD7 as the gate-shape TEST RUN after pcrecdev1's battery 3; the first cell was also lost once to the note-length harness bug, 3bda38b; I-18 MEASURED the class ladder at 96e44c2 — the set's predicted first refusal at the 32768 rung is RESCUED there (a 32 KB VM artifact, prefilter `[a-z]*`, `_ENGINE_SEL collapsed-prefilter`) and 65535 is refused by the NFA cap (131072 states) at EVERY pin including 36d5963, so this sample's `did-not-compile` rows read: 65535 = the NFA cap, 32768 = the abi-11 size cap that abi 12 rescues; the AFTER sample is [B19] (b)) SUB-BENCH #4: BOUNDED-REPEAT (`bench/bounded/`, 2026-08-29, lane b114bounded, a BLINDED author — D27 discipline as [B11.1]). THE NUMBERS THIS ROW EXISTS TO PRODUCE: (1) the COMPILE axis of bounded repeats — pcrec's counter-rung body replication under NESTED bounded repeats is where every artifact-size outlier in pcrec's own census lives (inbox I-15 (c): `.o` median 6.8 KB / p99 14 KB over 2,772 patterns; I-17: two size caps + a K ladder now decide the artifact, and the `.o`-size column on THIS set is the design input for the size term); (2) the MATCH axis in the K23/K32 band — a bounded lazy repeat before a `\b` alternation reaching the DFA's 32,000-state cap under `auto` (loglines `level-context`, the [SEL-1] witness) and large DFA-side counts like `[a-z]{0,30000}` (pcrec [ENG-COUNT], filed unscheduled 2026-08-29, "would find its measured need here if one exists"); (3) the give-up / refusal as a FIRST-CLASS outcome with the count at which it first fires (I-2 §1b: a count sweep, not a size sweep, is this set's sweep). Shape: everyday shapes with bounded counts (fixed-width fields `\d{4}`, hex ids `[0-9a-f]{32}`, line-length and password rules `.{8,64}` / `.{80,}`, a bounded-context "error … cause" shape `.{0,200}?`), plus a count LADDER on a few skeletons (greedy/lazy, class/literal/group body, nested `(?:X{a,b}){c,d}`, `{n}` / `{n,m}` / `{n,}`), counts from small to huge; every set carries the FLOOR pattern; expectations oracle-verified by the shared chain (`pcrecbench/expectations.py`, `--check`, sha256 manifests, `make check` by enumeration); subjects generated, non-periodic (`periodic` column), matching and failing arms both present; no pattern copied from pcrec's tests or corpora (the author is denied them). Measured in a window after [B18] lands so the number is at abi 11.
- [B12] STATE:started — (2026-08-29: lane b12close MERGED ef87b5d — the three quick items below DONE; the `reports/` regeneration was FINISHED by the manager the same evening: every committed set at v7, and the two 2026-08-28 sets' queries gained `--until 2026-08-29T00:00:00Z` the day the 36d5963 records entered the store, since the pcre2 testee_ids carry no pin and newest-measured-wins would otherwise pull the new pcre2 records into the 35e1ab1 sample's files. NEW CANDIDATES from the 36d5963 window (journal fourth session part 2): (i) DONE 2026-08-30 as BD7 — the occupancy instrument is `mpstat -P ALL 1 5` judged on its Average block (the 2026-08-30 bounded window added three more one-shot after-sample losses: 10.10 / 20.2 % and one more, `pidstat` naming the VS Code server, the streaming manager and a `gh` refresher), `check_occupancy_average` (7 controls), quiet_baseline.md's 2026-08-30 section; ORIGINALLY: OD-B12 now has EVIDENCE — two records (`email × pcrec-vm` 19:29Z, `loglines × pcrec-nocaps` 20:11Z) were stamped `inconclusive-load` on a single 1-s post-cell occupancy sample of 11.1 % / 13.0 % with load1 ≈ 1.1 and nothing else on the box — average the after-sample (or take the min of N) rather than one shot; (ii) the quiet gate's per-core limit (10 %) was derived with ONE manager on the box; two streaming claude processes leave an 11 % residue — either both managers idle for a window (today's protocol) or the limit is re-derived for the two-manager box (`docs/design/quiet_baseline.md`); (iii) `scripts/run_window.sh`'s gate budget: 3×20 s lost cells today, 12×30 s carried every cell — commit that budget; (iv) a HOLD relayed to a peer lane is not a hold until its processes are gone: a `verify by cwd` step before OPEN and after every cell belongs in the script or the skill.) M1 CLOSE ITEMS, lane b12close, 2026-08-29: [ADDED 2026-08-28] a DID-NOT-COMPILE cell must appear under its ranking table as `not ranked: <testee> — did-not-compile (<diagnostic>)`, not only in the compile-cost table (loglines/level-context under pcrec-auto vanished from the ranking, journal part 6) — DONE: reporter R10 (`pcrecbench/report.py`'s `[B12]` docstring section, `ReportData.did_not_compile_by_pattern`), `REPORTER_VERSION` v6 → v7, every committed report under `reports/` re-rendered (the loglines first-sample report is the one whose ranking content changed — `level-context`/`pcrec-auto` now carries the bullet; every other report's only diff is the version-line bump), `test_did_not_compile_ranking_line_r10` added; the window script's post-cell gate transient (a `sleep 15` before the first sample; every cell after the first needed a retry on 2026-08-28) belongs in a committed `scripts/run_window.sh` rather than a scratchpad copy — DONE: `scripts/run_window.sh` + `scripts/CLAUDE.md` committed, `--dry-run` rehearsal mode added (env-var-free shorthand for `EXTRA="--synthetic --force-unquiet" STORE=<scratch> TRIALS=1`, refuses to point at the canonical store), exercised once end to end against a scratch store; [NOTED BY THE MANAGER, not in the original row text] `pcrecbench.tests.test_report`'s runtime exceeded `make check`'s working budget — DONE: `_load_store(REAL_STORE)` (jsonschema validation over every record in `store/`, ~39 s/call once bench/loglines and email-specimen@0.2 joined email-specimen@0.1 there) was paid independently at seven call sites; a module-level cache (`_load_real_store()`) shares one load across all seven, safe because nothing downstream mutates a `LoadedRecord`; measured 274.6s → 47.6s on the same box, same 51 tests, all green both times. Also corrected in passing: the [B16]/[B14] test-count lines in `pcrecbench/CLAUDE.md` and `pcrecbench/tests/CLAUDE.md` had drifted ("49 total" when the actual `TESTS` list already held 50) — found while counting for this row's own +1; now 51/51. `make check` green: 3/56/0, 75/75, 51/51.
  the M1 close panel (D6) over harness_contract.md + harness_notes.md +
  the report; U1's discriminating measurement (the pcre2 INTERPRETER
  with PCRE2_NO_START_OPTIMIZE on the same cell, K34-probe shape; then
  the pcre2test reproduction — docs/dev/upstream_findings.md); OD-B10
  (1 MB vs 8 MB spread).

- [B19] STATE:not-started — RE-PIN pcrec to **96e44c2** (abi 12; inbox I-18, 2026-08-30 05:2x; CODE 0f5a98f = [OPT-4] ruling B — the exact prefilter is the default, the count-collapsed language a ladder RESCUE only — + [DD-11]; battery-proven by diagnosis: san 34/0, mech 189/0/6/0/0, codegen 198/0, cli 287/0). ONE adapter change absorbing I-18's worklist: (a) `pin.sh` to 96e44c2, `testees/pcrec/list_axes.tsv` re-archived and diffed (54 rows / 21 axes; new axes `prefilter-lang` 2, `engine-route` 5) and `list_definitions.tsv` archived beside it ([DD-11]'s fifth registry surface, `--list-definitions | grep -v '^#'`); (c) the shim reads `<P>_ENGINE_SEL` on EVERY artifact (one `engine-route` token: selected / forced / overflowed-dfa / overflowed-prefilter / collapsed-prefilter — O-8 6(d) RULED as a stamp) and `<P>_VM_PREFILTER_LANG` ∈ {exact, count-collapsed} + `_LANG_WHY` on every VM artifact, checked PRESENT in scope at abi 12 (`STAMP_SCOPE`), asserted BY VALUE on a real artifact of each kind in `make check-harness` (level-context predicted `collapsed-prefilter` / `count-collapsed` / "dfa overflow retry, exact nfa 462"; `-fno-prefilter-collapse` (bit 19) as the control that turns the rescue into a refusal, `-fprefilter-collapse` (bit 20) as the other); Frank's ask (b) buckets on `_ENGINE_SEL not in (selected, forced)`; (d) TWO source-bytes columns beside the .so in the compile table (O-8 ask (iv), YES): total emitted C bytes and comment-excluded code bytes, the census's own definitions; (e) `--warn-emit-bytes` (default 250,000; advisory, stderr, no exit-code change) recorded as a stamp-like fact, never a failure — bounded's `[a-z]{0,16384}` WILL warn; `PB_SHIM_MIN_ABI` stays 10 unless a read requires 12. THEN the windows at 96e44c2 with pcrecdev1: (b) bounded@0.1's AFTER sample (six cells; the [OPT-4] ledger is I-18's class-ladder table: 32768 RESCUED as a 32 KB collapsed-prefilter VM artifact, 65535 refused by the NFA cap at every pin, 16384 warns; predictions for the ctx/nests rows on record), email-specimen@0.2 and loglines@0.1 as the flat controls. Lane: strong model, worktree, the [B18] (e) brief as the template; NOT before the 36d5963 test-run window has CLOSED (one heavy suite on the box).
- [B20] STATE:not-started — THE GATE'S SHAPE, schema v1.4 (Frank, 2026-08-30 ~01:2x EDT via pcrecdev1; DURABLE COPY = inbox I-18 "FRANK'S GATE RULING", with d39135f's spread data attached; Frank's v1.4 ruling returns as I-19 — until then BD7 is what the harness does): the AFTER occupancy sample becomes PROVENANCE (X13 revised to the pre-flight only), TRIAL AGREEMENT decides `measured` vs a new `inconclusive-spread`, the pre-flight stays PER-CORE (the manager's correction, accepted: a steady competitor or one on CPU 11's SMT sibling CPU 5 is invisible to trial agreement) and also reads the TARGET core. Proposal written: `docs/design/gate_shape_v14.md` (P1-P4, migration, the open spread-rule question and the per-row outliers to characterise first). DECIDED BY: the gate-shape TEST RUN (the three inconclusive bounded cells under BD7; `docs/dev/measurements/probe_gate_shape.py` archives status, spread distribution and the recomputed old 1-s verdict per cell) → Frank's ruling → critic panel → schema v1.4 + validator + reporter R1. Not before.
- [B13] STATE:not-started — THE INTERPRETER (Frank, 2026-08-25: "reads
  and provides interpretation to these reports as an add-on … no
  opinions, all based on facts"; agreed design, journal part 5). Two
  parts: (1) a DETERMINISTIC fact-finder, `pcrecbench interpret`, reading
  the report TSV + store/index.tsv (never the markdown), emitting the
  FIRED RULES with rows, numbers and record ids, plus the rules that did
  NOT fire; a versioned RULE CATALOGUE (id, definition, threshold WITH
  its source — spread-based, never a magic number — a worked example
  from a real report): status caveats (inconclusive-load, excluded
  cells, give-ups with code + subject), cross-pin deltas beyond spread,
  rank flips vs the reference arm, ratios inside the timer floor,
  PREDICTIONS vs OUTCOMES (the inbox's stated expectations as input:
  confirmed / refuted / result no prediction covered), registered
  buckets (known readings that are facts with a source, e.g. the `\z`
  regime artifact per feedback 2a); `make check-interpret` (same input →
  same facts; a sabotaged report fires the rule its name claims). (2) a
  project skill `/pcrec-bench-interpret <report>` that phrases the fired
  rules into a SIDECAR `reports/<name>.interpretation.md` stamped with
  the report's sha256 and the catalogue version — never a section in the
  report (the reporter stays deterministic and diffable); committed
  beside every report. OPINION FIREWALL: every sentence cites a fired
  rule; hypotheses appear only as LINKS to where they are already
  recorded (outbox, known_issues), never generated. Sits after [B9]
  (needs OD-B14 status per row and OD-B15 pooled-vs-newest). Frank:
  "let it sit a bit before we do it." INPUT TO COLLECT FIRST: pcrecdev1's
  feedback on the repin report as it reads — actionability and
  interpretation (outbox O-5; answer → docs/dev/feedback_pcrecdev1_
  <date>-repin.md, cited here). Blinded first test: catalogue v1 must
  find, unprompted, the collapse, the three inconclusive records, the
  give-ups and the vm-in result in the two existing reports.
- [B7] STATE:not-started — ROSTER EXPANSION (APPROACH §4): RE2, Rust
  `regex`, Oniguruma, TRE (POSIX-tagged), Vectorscan (semantics-tagged),
  python `re`, perl; the hand-C ceiling arm (pcrec [BENCH-CEIL]'s testee
  triple). One adapter per lane; each admits with its semantics recorded.
