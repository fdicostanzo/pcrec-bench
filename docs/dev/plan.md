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

- [B3] STATE:started (2026-08-25 ~00:0x, lane/b3harness with [B4], worktrees/b3harness, opus, brief scratchpad/brief_b3harness.md; pin 8da6120 building in build/pcrec-8da6120) — THE HARNESS CORE: the sub-bench DIRECTORY
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
- [B4] STATE:started (2026-08-25, rides lane/b3harness) — TESTEE ADAPTERS, first two (plus OD-B10, the large-subject size measured at 1 MB vs 8 MB): pcrec (as its
  several configuration testees, pinned by commit) and libpcre2 (interp AND
  jit as separate testees). Each pins its version and records build flags;
  "unsupported" is a first-class per-case result.
- [B5] STATE:started (2026-08-25 ~00:0x, lane/b5report, worktrees/b5report, sonnet, brief scratchpad/brief_b5report.md) — THE REPORTER MVP: static over two or more
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
