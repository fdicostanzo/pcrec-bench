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
a blocking foreground call, never a Monitor on a progress log. The Bash
tool's `run_in_background: true` is the DEFAULT launch: it is
harness-tracked and notifies on exit, and its 600 s `timeout` maximum
is NOT an execution deadline for a background task — tracked runs of
~20 min (lane b13pre) and ~30 min (I-59's build+test) completed and
notified on 2026-09-08 (the older "10-min cap" belief came from a
memory-pressure kill, not a clock). BUT a tracked task the harness
kills for memory pressure (a 3.6 GB store load + a 317 MB pickle dump,
b13pre run 4, same night, with 11 GB `available`) dies WITHOUT a
notification and without your marker — so the marker rule below is
what saves you, and a lane waiting "for the notification" must ALSO
check the marker at every reinvocation. Keep peak RSS low (stream,
don't hold the store twice). Multi-hour windows still run under setsid
with a marker (below). python3 (BD4).

**Every background job ends with a durable completion marker, checked
by a command, never inferred from `ps`.** ([B33]'s b33cc lane, twice,
2026-09-07: an idle notification said "I'll report back once it
completes," the job finished minutes later with nobody — lane or
manager — noticing until asked; the only evidence of "done" was `ps
aux` forensics run from outside.) Chain every backgrounded command with
`; echo "DONE rc=$?" >> <logfile>` (or a `touch <marker>` beside the
worktree) and treat that line/file, not a live-process check, as the
ONLY source of truth for "has this finished". **A job you launched
with `setsid … & disown` (or any plain `&`) is NOT a harness task: NO
completion notification will EVER reach you** — "I'll resume once the
notification arrives" is waiting on nothing (lane b13pre, 2026-09-08,
announced exactly that for a disowned job; it had in fact polled the
marker and relaunched, but the announced plan would have hung the
lane). For a run under the Bash tool's cap, use
`run_in_background: true` (harness-tracked, it DOES notify); for a
longer one, DO-THEN-FINISH below — commit, report the marker as OWED,
launch, END; a fresh agent checks the marker. Before sending ANY idle
notification, status message, or handback while a background job is
outstanding, run the check for its marker and quote the result inline
— a claim of "still running" or "waiting for X" is not credible without
it. On EVERY reinvocation (a background-task notification, a message
from the manager, a fresh turn after any gap), check every marker you
are tracking before doing anything else — the notification firing is
not proof you acted on it last time.

## Process rules
- COMMIT INCREMENTALLY (WIP commits) — commit age is your liveness signal.
- Records: pinned tier (canonical store) vs scratch (`quick`, pcrec-local)
  — scratch NEVER enters the store. Variants must give IDENTICAL results
  and preserve the sub-bench's OBJECTIVE.
- Measurements: interleaved trials, load stated, pre-flight controls; a
  prediction is stated BEFORE the run wherever the charter allows.
- Update the owning directory's CLAUDE.md for file adds/removes/role
  changes.

## Lifecycle (Frank's ruling 2026-09-06 — no keepalive doctrine survives;
refined 2026-09-08 by the DO-THEN-FINISH rule, `docs/dev/
session_discipline.md` §2, inbox I-60)
- NO self-keepalive crons: subagent caches are 5-minute TTL; periodic
  ticks pay a full context rewrite for zero warmth.
- Work continuously to your deliverable. Blocked on a ruling: send the
  question and keep working on what does not depend on it, or say you
  are stopping and why.
- **DO-THEN-FINISH**: a run longer than ~4 minutes is your LAST act.
  Commit and write your report FIRST — mark any number the run will
  produce as OWED, name the log path and the exact completion line the
  run will emit — THEN launch the run in the background and END. Do not
  stay alive polling it; a follow-up that folds in the OWED numbers goes
  to a FRESH agent resuming from your committed report, never to you
  kept warm (your cache is cold again in 5 minutes regardless). Runs
  ≤4 minutes may be polled by you directly.
- WHEN DONE: commit everything, write your report (docs/dev/lanes/
  <lane>_report.md, committed), send the manager a handback whose text is
  complete on its own (numbers inline, log paths, OWED items named), and
  END — do not idle awaiting review or awaiting a background job's
  completion (see DO-THEN-FINISH above).
- A handback names its validation COMPLETE or says exactly what is owed,
  per `docs/dev/session_discipline.md` §7(c)'s charter-vs-committed
  checklist: every promise in your brief either points at its committed
  artifact or is listed OWED with an owner and a trigger.

## Delivery bar
Branch lane/<lane>, committed, report committed, targeted validation run
with numbers in the handback. Re-pin every manifest/count/pin your change
moves in the same delivery (readers found by grep). The manager merges;
never merge yourself. Before a measurement window starts, every lane is
STOPPED (TaskStop) — a "delivered" lane once resurrected its worktree and
ran tests on the box mid-window.
