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
- [B11.4] STATE:started — (2026-08-29: BUILT and MERGED 485a230, lane b114bounded, blinded; 24 patterns, 30 + 4 subjects, 1536 expectations, `oracle_limits.tsv`, predictions on record in NOTES.md; the author recommends SPLITTING the two axes into two sub-benches — a scope ruling for the manager; NOT YET MEASURED: six cells ≈ 80 min in the next window) SUB-BENCH #4: BOUNDED-REPEAT (`bench/bounded/`, 2026-08-29, lane b114bounded, a BLINDED author — D27 discipline as [B11.1]). THE NUMBERS THIS ROW EXISTS TO PRODUCE: (1) the COMPILE axis of bounded repeats — pcrec's counter-rung body replication under NESTED bounded repeats is where every artifact-size outlier in pcrec's own census lives (inbox I-15 (c): `.o` median 6.8 KB / p99 14 KB over 2,772 patterns; I-17: two size caps + a K ladder now decide the artifact, and the `.o`-size column on THIS set is the design input for the size term); (2) the MATCH axis in the K23/K32 band — a bounded lazy repeat before a `\b` alternation reaching the DFA's 32,000-state cap under `auto` (loglines `level-context`, the [SEL-1] witness) and large DFA-side counts like `[a-z]{0,30000}` (pcrec [ENG-COUNT], filed unscheduled 2026-08-29, "would find its measured need here if one exists"); (3) the give-up / refusal as a FIRST-CLASS outcome with the count at which it first fires (I-2 §1b: a count sweep, not a size sweep, is this set's sweep). Shape: everyday shapes with bounded counts (fixed-width fields `\d{4}`, hex ids `[0-9a-f]{32}`, line-length and password rules `.{8,64}` / `.{80,}`, a bounded-context "error … cause" shape `.{0,200}?`), plus a count LADDER on a few skeletons (greedy/lazy, class/literal/group body, nested `(?:X{a,b}){c,d}`, `{n}` / `{n,m}` / `{n,}`), counts from small to huge; every set carries the FLOOR pattern; expectations oracle-verified by the shared chain (`pcrecbench/expectations.py`, `--check`, sha256 manifests, `make check` by enumeration); subjects generated, non-periodic (`periodic` column), matching and failing arms both present; no pattern copied from pcrec's tests or corpora (the author is denied them). Measured in a window after [B18] lands so the number is at abi 11.
- [B12] STATE:started — (2026-08-29: lane b12close MERGED ef87b5d — the three quick items below DONE; the `reports/` regeneration was FINISHED by the manager the same evening: every committed set at v7, and the two 2026-08-28 sets' queries gained `--until 2026-08-29T00:00:00Z` the day the 36d5963 records entered the store, since the pcre2 testee_ids carry no pin and newest-measured-wins would otherwise pull the new pcre2 records into the 35e1ab1 sample's files. NEW CANDIDATES from the 36d5963 window (journal fourth session part 2): (i) OD-B12 now has EVIDENCE — two records (`email × pcrec-vm` 19:29Z, `loglines × pcrec-nocaps` 20:11Z) were stamped `inconclusive-load` on a single 1-s post-cell occupancy sample of 11.1 % / 13.0 % with load1 ≈ 1.1 and nothing else on the box — average the after-sample (or take the min of N) rather than one shot; (ii) the quiet gate's per-core limit (10 %) was derived with ONE manager on the box; two streaming claude processes leave an 11 % residue — either both managers idle for a window (today's protocol) or the limit is re-derived for the two-manager box (`docs/design/quiet_baseline.md`); (iii) `scripts/run_window.sh`'s gate budget: 3×20 s lost cells today, 12×30 s carried every cell — commit that budget; (iv) a HOLD relayed to a peer lane is not a hold until its processes are gone: a `verify by cwd` step before OPEN and after every cell belongs in the script or the skill.) M1 CLOSE ITEMS, lane b12close, 2026-08-29: [ADDED 2026-08-28] a DID-NOT-COMPILE cell must appear under its ranking table as `not ranked: <testee> — did-not-compile (<diagnostic>)`, not only in the compile-cost table (loglines/level-context under pcrec-auto vanished from the ranking, journal part 6) — DONE: reporter R10 (`pcrecbench/report.py`'s `[B12]` docstring section, `ReportData.did_not_compile_by_pattern`), `REPORTER_VERSION` v6 → v7, every committed report under `reports/` re-rendered (the loglines first-sample report is the one whose ranking content changed — `level-context`/`pcrec-auto` now carries the bullet; every other report's only diff is the version-line bump), `test_did_not_compile_ranking_line_r10` added; the window script's post-cell gate transient (a `sleep 15` before the first sample; every cell after the first needed a retry on 2026-08-28) belongs in a committed `scripts/run_window.sh` rather than a scratchpad copy — DONE: `scripts/run_window.sh` + `scripts/CLAUDE.md` committed, `--dry-run` rehearsal mode added (env-var-free shorthand for `EXTRA="--synthetic --force-unquiet" STORE=<scratch> TRIALS=1`, refuses to point at the canonical store), exercised once end to end against a scratch store; [NOTED BY THE MANAGER, not in the original row text] `pcrecbench.tests.test_report`'s runtime exceeded `make check`'s working budget — DONE: `_load_store(REAL_STORE)` (jsonschema validation over every record in `store/`, ~39 s/call once bench/loglines and email-specimen@0.2 joined email-specimen@0.1 there) was paid independently at seven call sites; a module-level cache (`_load_real_store()`) shares one load across all seven, safe because nothing downstream mutates a `LoadedRecord`; measured 274.6s → 47.6s on the same box, same 51 tests, all green both times. Also corrected in passing: the [B16]/[B14] test-count lines in `pcrecbench/CLAUDE.md` and `pcrecbench/tests/CLAUDE.md` had drifted ("49 total" when the actual `TESTS` list already held 50) — found while counting for this row's own +1; now 51/51. `make check` green: 3/56/0, 75/75, 51/51.
  the M1 close panel (D6) over harness_contract.md + harness_notes.md +
  the report; U1's discriminating measurement (the pcre2 INTERPRETER
  with PCRE2_NO_START_OPTIMIZE on the same cell, K34-probe shape; then
  the pcre2test reproduction — docs/dev/upstream_findings.md); OD-B10
  (1 MB vs 8 MB spread).

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
