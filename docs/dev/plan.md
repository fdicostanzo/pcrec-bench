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

- [B11] STATE:started — (2026-08-28: #2 DONE as [B11.1], archived. 2026-08-30: #4 DONE as [B11.4], measured at 36d5963 and archived; O-9 sent; #3 wide alternations = [B11.2] is NEXT after the abi-12 windows. 2026-08-29: #4 BOUNDED-REPEAT ruled NEXT — inbox I-14 (iv) recommended, I-15 (c) and I-17 (c) confirmed with Frank's "advance these bench requests" — expanded as [B11.4] below; #3 wide alternations follows it as [B11.2]; Frank's ruling that the pcrec manager may run bench sessions AS the bench when pcrecdev2 is down — one repo per session) SUB-BENCHES #2..#6, in Frank's ruled order
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
- [B12] STATE:started — (2026-08-29: lane b12close MERGED ef87b5d — the three quick items below DONE; the `reports/` regeneration was FINISHED by the manager the same evening: every committed set at v7, and the two 2026-08-28 sets' queries gained `--until 2026-08-29T00:00:00Z` the day the 36d5963 records entered the store, since the pcre2 testee_ids carry no pin and newest-measured-wins would otherwise pull the new pcre2 records into the 35e1ab1 sample's files. NEW CANDIDATES from the 36d5963 window (journal fourth session part 2): (i) DONE 2026-08-30 as BD7 — the occupancy instrument is `mpstat -P ALL 1 5` judged on its Average block (the 2026-08-30 bounded window added three more one-shot after-sample losses: 10.10 / 20.2 % and one more, `pidstat` naming the VS Code server, the streaming manager and a `gh` refresher), `check_occupancy_average` (7 controls), quiet_baseline.md's 2026-08-30 section; ORIGINALLY: OD-B12 now has EVIDENCE — two records (`email × pcrec-vm` 19:29Z, `loglines × pcrec-nocaps` 20:11Z) were stamped `inconclusive-load` on a single 1-s post-cell occupancy sample of 11.1 % / 13.0 % with load1 ≈ 1.1 and nothing else on the box — average the after-sample (or take the min of N) rather than one shot; (ii) the quiet gate's per-core limit (10 %) was derived with ONE manager on the box; two streaming claude processes leave an 11 % residue — either both managers idle for a window (today's protocol) or the limit is re-derived for the two-manager box (`docs/design/quiet_baseline.md`); (iii) `scripts/run_window.sh`'s gate budget: 3×20 s lost cells today, 12×30 s carried every cell — commit that budget; (iv) a HOLD relayed to a peer lane is not a hold until its processes are gone: a `verify by cwd` step before OPEN and after every cell belongs in the script or the skill.) M1 CLOSE ITEMS, lane b12close, 2026-08-29: [ADDED 2026-08-28] a DID-NOT-COMPILE cell must appear under its ranking table as `not ranked: <testee> — did-not-compile (<diagnostic>)`, not only in the compile-cost table (loglines/level-context under pcrec-auto vanished from the ranking, journal part 6) — DONE: reporter R10 (`pcrecbench/report.py`'s `[B12]` docstring section, `ReportData.did_not_compile_by_pattern`), `REPORTER_VERSION` v6 → v7, every committed report under `reports/` re-rendered (the loglines first-sample report is the one whose ranking content changed — `level-context`/`pcrec-auto` now carries the bullet; every other report's only diff is the version-line bump), `test_did_not_compile_ranking_line_r10` added; the window script's post-cell gate transient (a `sleep 15` before the first sample; every cell after the first needed a retry on 2026-08-28) belongs in a committed `scripts/run_window.sh` rather than a scratchpad copy — DONE: `scripts/run_window.sh` + `scripts/CLAUDE.md` committed, `--dry-run` rehearsal mode added (env-var-free shorthand for `EXTRA="--synthetic --force-unquiet" STORE=<scratch> TRIALS=1`, refuses to point at the canonical store), exercised once end to end against a scratch store; [NOTED BY THE MANAGER, not in the original row text] `pcrecbench.tests.test_report`'s runtime exceeded `make check`'s working budget — DONE: `_load_store(REAL_STORE)` (jsonschema validation over every record in `store/`, ~39 s/call once bench/loglines and email-specimen@0.2 joined email-specimen@0.1 there) was paid independently at seven call sites; a module-level cache (`_load_real_store()`) shares one load across all seven, safe because nothing downstream mutates a `LoadedRecord`; measured 274.6s → 47.6s on the same box, same 51 tests, all green both times. Also corrected in passing: the [B16]/[B14] test-count lines in `pcrecbench/CLAUDE.md` and `pcrecbench/tests/CLAUDE.md` had drifted ("49 total" when the actual `TESTS` list already held 50) — found while counting for this row's own +1; now 51/51. `make check` green: 3/56/0, 75/75, 51/51.
  the M1 close panel (D6) over harness_contract.md + harness_notes.md +
  the report; U1's discriminating measurement (the pcre2 INTERPRETER
  with PCRE2_NO_START_OPTIMIZE on the same cell, K34-probe shape; then
  the pcre2test reproduction — docs/dev/upstream_findings.md); OD-B10
  (1 MB vs 8 MB spread).

- [B21] STATE:not-started — bench/bounded@0.2: THE KNEE RUNGS (chartered by inbox I-19 (2) WITH pcrec's [OPT-5], the `{0,n}` class-count selection knee Frank chose from O-9 candidate 2, preceded by pcrec's [LIM-1] single limits table / `pcrec --list-limits`): intermediate class rungs between 256 / 4096 / 16384 (both the letter and the digit throughput subjects, both forms — bounded brackets the knee: the DFA wins at 256/4096 on digits and loses 6× at 4096/16384 on letters) and the group-vs-class rung `[a-z]{0,1024}` beside `grp-upto-1024` (NOTES.md's untestable size-term prediction; O-9 ask (vi)); a version bump (0.1 → 0.2, new manifests/expectations/facts by the same generators, the author's discipline as 0.1); pcrec states the PREDICTED knee rung and winner BEFORE our AFTER at that pin — PER THROUGHPUT SUBJECT, because the abi-12 ledger (docs/dev/ledgers/2026-08-30-abi12-after-96e44c2.md §7-8) shows the counted DFA losing 5.1-5.9× to pcrec's own VM on the letter runs at EVERY rung from 256 and winning 1.75× on the digits run at every rung: on this evidence the knee is a property of the SUBJECT, not the count, so the set adds rungs at 64 and 128 as well (to bracket a knee below 256 on the letters axis) and reads each rung per subject; `--list-limits` becomes a third archive target beside list_axes/list_definitions when it lands. HELD for the [OPT-4.1] pin (inbox I-21: one re-pin instead of two). READING FRAME from I-21 (2), falsifiable: letters (t-letters-004k/016k/064k) → the VM wins at EVERY rung including the new 64 and 128; digits (t-digits-016k) → the DFA wins at every rung; NO count crossover on either axis — a letters rung where the DFA wins IS the knee and [OPT-5]'s mechanism-first re-scope is wrong; say so if found. The cut itself (a blinded-author lane as 0.1's) may be prepared before the pin; its window waits for [B22].
- [B22] STATE:not-started — RE-PIN to pcrec's [OPT-4.1] pin (inbox I-21 (1): the count-collapsed rescue GATED on the collapsed language being NON-NULLABLE — O-10 candidate 1 / ask (i), chartered ahead of [OPT-5]; a declined rescue stamps a NEW `_VM_PREFILTER_LANG_WHY` value naming nullability — a value, no abi bump; the pin follows its battery). The adapter reads the new value (STAMP_SCOPE unchanged; a by-value control on `cls-upto-32768`: declined, `overflowed-dfa`, no prefilter); then the windows read against the TEN LABELLED POINTS of O-10 items 3/7 with I-21's PREDICTIONS AS CORRECTED (the I-21 CORRECTION, 2026-08-30 ~15:1x, code-derived minw analysis): DECLINE (nullable, `RX_ENGINE_SEL "declined-nullable"` — a SIXTH engine-route value, so `--list-axes` gains a row and the adapter's enum, scope and by-value controls read it; NO prefilter macros on a declined artifact, the §6.3 iff holds) = cls-upto-32768 plain AND whole, cls-upto-16384 whole, cls-lazy-16384 whole — these return to the BEFORE's numbers; KEEP the rescue and its bytes = the four ctx rungs (minw 8), level-context (minw 10), AND nest2-64/nest3-16 whole (minw 1, NON-nullable — I-21's "four whole-subject-only rescues return to flat" was wrong for these two, which O-10 called flat, not losses): the five wins (ctx × 4, level-context) keep their abi-12 numbers within spread; the three `cls-*` losses return to the 36d5963 `overflowed-dfa` numbers (auto = its VM within spread on those cells); the four whole-subject-only rescues return to flat with their +376…+4,560 B gone. bounded@0.2 ([B21]) is cut for THIS pin and measured in the same window. I-22 (2026-08-30 ~18:2x) ANSWERED ii-v and adds to THIS row: the PIN CANDIDATE is main cdaae0b ([OPT-4.1] merged; battery 5 runs on it to ~21:50, the pin line follows its green; the lane's predict_check confirmed 11/11 of the corrected predictions, exact-NFA counts byte-identical to O-10's; the four `\z` forms overflow by the K7 subset-elements route, stamped distinctly in `_WHY`). (ii) the {0,32768} byte comparison is INVALID ACROSS PINS (the artifact changed kind: hybrid → declined plain-VM; their six counting-rule readings all miss 24,414) — [B22]'s lane RE-COMPARES AT ONE PIN, the port vs the pin's own --warn-emit-bytes, stating the counting rule (theirs: docs/dev/lanes/opt41_report.md §15). (iii) year4's +4,096 B = ELF page alignment (inferred): [B22] PROVES it from the source-bytes columns at the re-pin (source ~+220 B vs .so +4,096). (iv) the AFTER's declined artifacts are read by "nullable AND `RX_DFA_PREFILTER "none"`", NEVER minw alone (three nullable hybrids have WORKING prefilters — the $-view shapes; the census caveat). (v) closed: tests/resource carries the size-cap witness pair; [LIM-1] inherits it.
- [B23] STATE:not-started — THE SPREAD RULE'S MEASURED POSITIVE CONTROL (gate_shape_v14.md §9 Q3, the panel's recommendation): one deliberate scratch-tier cell measured with a competitor pinned to CPU 5 (the target's SMT sibling) for exactly two passes of one group, archived under docs/dev/measurements/ (D35), showing the rule FLAGGING a genuinely moved cell — the instrument's positive case, which the store cannot supply. A MEASUREMENT: gated on Frank lifting the performance-test hold, and announce-and-idle per BD6 even at the scratch tier (the competitor is deliberate load).
- [B24] STATE:not-started — THE PARTIAL CC AXIS (inbox I-22 / pcrec [CC-CLANG]; Frank's probe: clang 21.1.8 agrees cell-for-cell on DFA/recursion/backtracking-VM artifacts; the frameless VM's `&&label` resume dispatch is the one incompatibility, fixed on pcrec's queue with an abi bump): the same artifacts compiled gcc vs clang on a few cells of ONE sub-bench — a testee-config VARIANT (like `-caps-simdna`; no sub-bench version bump), our build of their .c files — to measure whether the compiler moves the numbers. QUEUED BEHIND [B21]/[B22]; a MEASUREMENT, gated on Frank lifting the perf hold.
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
