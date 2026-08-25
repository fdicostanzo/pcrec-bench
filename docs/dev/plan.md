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

The rows after [B1] are PLACEHOLDERS transcribed from APPROACH.md §8 Q5's
proposed first cut ("M1 = set format ruled + schema ruled + two adapters
(pcrec, libpcre2) + comparator MVP producing its first honest diff"). The
requirements discussion ([B1]) may reorder, merge, split or strike them;
none is a commitment until Frank rules the requirements.

- [B1] STATE:started — REQUIREMENTS: the overall-requirements discussion
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
- [B2] STATE:not-started — THE ARTIFACT SCHEMA (APPROACH §3, §8 Q2):
  the versioned per-testee output file — environment header (CPU, kernel,
  compiler, load/quiet-box attestation, per-core occupancy), per-case
  compile outcome / match outcome / correctness verdict / timings with
  COMPILE and MATCH separated — plus the tiny validator the comparator
  shares. Design note → panel → ruled.
- [B3] STATE:not-started — THE SET, v0: the interim set carrier and the
  first versioned set. The FORMAT is owned by pcrec's [DD-13] (APPROACH §8
  Q1, resolved in direction); until [DD-13b/c] land this project needs an
  interim that imports .rxt (R-BENCH-8) and carries the per-case tags
  (R-BENCH-1) without inventing a competing grammar. First contents: the
  email specimen (a ready-made row), imports from pcrec's oracle-verified
  corpora, and the hazard classes APPROACH §2.1 names.
- [B4] STATE:not-started — TESTEE ADAPTERS, first two: pcrec (as its
  several configuration testees, pinned by commit) and libpcre2 (interp AND
  jit as separate testees). Each pins its version and records build flags;
  "unsupported" is a first-class per-case result.
- [B5] STATE:not-started — THE COMPARATOR MVP: static over two or more
  artifacts — per-case diffs, per-tag rollups, correctness disagreement
  tables, rankings that exclude wrong answers by default. Never runs an
  engine.
- [B6] STATE:not-started — THE FIRST HONEST DIFF and the first feedback
  row into pcrec: run the two adapters on set v0 on a quiet box, compare,
  and hand the pcrec manager the first outlier in the agreed feedback
  shape. Closes M1 as APPROACH §8 Q5 proposed it.
- [B7] STATE:not-started — ROSTER EXPANSION (APPROACH §4): RE2, Rust
  `regex`, Oniguruma, TRE (POSIX-tagged), Vectorscan (semantics-tagged),
  python `re`, perl; the hand-C ceiling arm (pcrec [BENCH-CEIL]'s testee
  triple). One adapter per lane; each admits with its semantics recorded.
