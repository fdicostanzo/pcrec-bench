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

- [B8] STATE:not-started — RE-PIN pcrec to `692c2e8` (inbox I-1; the
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
  (pcrec D73). A `pcrec-auto-in` config (the `_in` entries with a sized
  buffer) is a SEPARATE ROSTER ENTRY per requirements 4.2 (a testee
  triple, like nocaps), not a variant — added in this row if Frank
  agrees, else queued.
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
  multi-sample gate — the transients are the managers' own processes).
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

- [B7] STATE:not-started — ROSTER EXPANSION (APPROACH §4): RE2, Rust
  `regex`, Oniguruma, TRE (POSIX-tagged), Vectorscan (semantics-tagged),
  python `re`, perl; the hand-C ceiling arm (pcrec [BENCH-CEIL]'s testee
  triple). One adapter per lane; each admits with its semantics recorded.
