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

- [B9] STATE:not-started — REPORTER FOLLOW-UPS from pcrecdev1's feedback
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
- [B10] STATE:not-started — THE EDIT-TEST LOOP (inbox I-4, Frank's
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
