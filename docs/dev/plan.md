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

- [B11] STATE:not-started — SUB-BENCHES #2..#6, in Frank's ruled order
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
- [B12] STATE:not-started — M1 CLOSE ITEMS (candidates, unordered):
  the M1 close panel (D6) over harness_contract.md + harness_notes.md +
  the report; U1's discriminating measurement (the pcre2 INTERPRETER
  with PCRE2_NO_START_OPTIMIZE on the same cell, K34-probe shape; then
  the pcre2test reproduction — docs/dev/upstream_findings.md); OD-B10
  (1 MB vs 8 MB spread).

- [B14] STATE:started — REPORTER FOLLOW-UPS from pcrecdev1's reading
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
- [B15] STATE:started — THE PER-CALL FLOOR PATTERN in every short-subject
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
