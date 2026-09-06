# LANE BOILERPLATE — read this FIRST, follow all of it

Standing rules for every pcrec-bench subagent lane. Your brief names your
task, model tier, and deliverable; everything below applies without
restatement. (Frank's ruling 2026-09-06, mirrored from pcrec's
docs/dev/lanes/BOILERPLATE.md — cut brief size and lane startup cost.)

## Scope mandate (BD2/BD3)
Touch ONLY this repository (pcrec-bench), and inside it ONLY your own
worktree under worktrees/. ~/pcrec is READ-ONLY, always (BD2). No other
directories, no system config. Session-temporary files go in the session
scratchpad named in your environment, never committed. ONE heavy suite on
the box at a time; measurement windows are the manager's to grant (BD3).
Subagents you spawn inherit this mandate. Disclosure: you inherit the
session-root CLAUDE.md and memory index at spawn — context, not tasking.

## Worktree setup (writers)
1. `git worktree add worktrees/<lane> -b lane/<lane>` (absolute paths /
   `git -C` — a cd in a compound command persists to its tail).
2. cd there; FIRST command: `git rev-parse --show-toplevel` — no edit
   until it prints your worktree path.
Read-only critics work in the main tree and never build.

## Box facts (ubuntubudu, Linux)
Use `gnutimeout` on every command of uncertain length (bare `timeout` is
uutils, ~105 ms/call); a firing timeout is a FINDING. Kill by PID only —
NEVER pkill -f/pgrep -f. Long runs go in a BACKGROUND task writing a log;
poll the log TAIL and act the moment the completion line appears — never
a blocking foreground call, never a Monitor on a progress log. Windows
run under setsid (the background-task 10-min cap). python3 (BD4).

## Process rules
- COMMIT INCREMENTALLY (WIP commits) — commit age is your liveness signal.
- Records: pinned tier (canonical store) vs scratch (`quick`, pcrec-local)
  — scratch NEVER enters the store. Variants must give IDENTICAL results
  and preserve the sub-bench's OBJECTIVE.
- Measurements: interleaved trials, load stated, pre-flight controls; a
  prediction is stated BEFORE the run wherever the charter allows.
- Update the owning directory's CLAUDE.md for file adds/removes/role
  changes.

## Lifecycle (Frank's ruling 2026-09-06 — no keepalive doctrine survives)
- NO self-keepalive crons: subagent caches are 5-minute TTL; periodic
  ticks pay a full context rewrite for zero warmth.
- Work continuously to your deliverable. Blocked on a ruling: send the
  question and keep working on what does not depend on it, or say you
  are stopping and why.
- WHEN DONE: commit everything, write your report (docs/dev/lanes/
  <lane>_report.md, committed), send the manager a handback whose text is
  complete on its own (numbers inline, log paths), and END — do not idle
  awaiting review. A plausible follow-up round resumes from your
  committed report in a FRESH agent; write the report so that works.
- A handback names its validation COMPLETE or says exactly what is owed.

## Delivery bar
Branch lane/<lane>, committed, report committed, targeted validation run
with numbers in the handback. Re-pin every manifest/count/pin your change
moves in the same delivery (readers found by grep). The manager merges;
never merge yourself. Before a measurement window starts, every lane is
STOPPED (TaskStop) — a "delivered" lane once resurrected its worktree and
ran tests on the box mid-window.
