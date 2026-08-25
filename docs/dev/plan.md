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

- [B6] STATE:started (2026-08-25 ~01:3x — the window run: run_window.sh staged, cells email × {pcre2-interp, pcre2-jit, pcrec-auto, pcrec-nocaps, pcrec-vm}, --trials 5 --pin 11, in pcrecdev1's quiet window ~02:50) — THE FIRST HONEST DIFF and the first feedback
  row into pcrec: run the two adapters on set v0 on a quiet box, compare,
  and hand the pcrec manager the first outlier in the agreed feedback
  shape. Closes M1 as APPROACH §8 Q5 proposed it.
- [B7] STATE:not-started — ROSTER EXPANSION (APPROACH §4): RE2, Rust
  `regex`, Oniguruma, TRE (POSIX-tagged), Vectorscan (semantics-tagged),
  python `re`, perl; the hand-C ceiling arm (pcrec [BENCH-CEIL]'s testee
  triple). One adapter per lane; each admits with its semantics recorded.
