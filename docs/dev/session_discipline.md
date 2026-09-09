# session_discipline.md — the manager-session discipline package (I-60)

Adopted 2026-09-08 on Frank's ruling (inbox I-60, `docs/dev/
inbox_from_pcrec.md`): the manager session returns to **Fable** from its
next start, superseding I-54's Sonnet ruling. Frank's diagnosis: the
token concern that motivated I-54 (2026-09-06) was **process waste**, not
model choice — keepalive context re-reads, forks from giant contexts,
managers doing mechanical work, lanes idling across busted caches — and
the three concrete failures under Sonnet ([B13]'s dropped consolidation
findings and un-run step-2 pass; subagent tracking breaking down when
subagents watched processes themselves; follow-through stopping at
intermediary steps) are judgment/persistence-shaped or process-shaped,
not fixed by a weaker model. This file is the mechanical half — the
package that travels with the model regardless of which model is
running. `docs/dev/lanes/BOILERPLATE.md` already carries most of items
2-4/6 from the 2026-09-06 ruling; this file is the single canonical
statement of the full package, cross-referenced from both
`docs/dev/lanes/BOILERPLATE.md` and `.claude/skills/pcrec-bench-manager/
SKILL.md` rather than duplicated into either.

## 1. Model split

Manager session: **Fable**. Every lane DEFAULTS to **Sonnet** (Haiku for
mechanical sweeps) — this is the default, not a ceiling: per Frank's
I-60 addendum (2026-09-08), Opus is on the table for a lane that
genuinely needs it, same tiering as pcrec-side (Sonnet wherever it fits,
Opus for the genuinely difficult lanes, the manager's own model never
used for a lane — unchanged from the pre-existing per-lane-tiering
guardrail in `docs/dev/lanes/BOILERPLATE.md`/skill §4, e.g. D27 blinded
authors and design-heavy adapter semantics). The strong (manager) model
NEVER does mechanical work — its spend is briefs, review verdicts,
merges, rulings, and design judgment only. The executor hat (I-57/BD10)
is unchanged by this — its protocol already asks for no judgment.

## 2. DO-THEN-FINISH lane lifecycle

Subagent prompt caches are 5-minute TTL. A run longer than ~4 minutes is
a lane's LAST act:
- All heavy-context phases end at **commit + report FIRST** — numbers
  the run will produce are marked OWED, with the log path and the exact
  completion line the lane will emit named in the report.
- The run is launched in the BACKGROUND, and the lane ENDS. It does not
  stay alive polling its own job.
- Follow-up (filling the OWED numbers once the run completes) goes to a
  FRESH agent resuming from the committed report — never the same lane
  kept warm (a lane's cache is cold again after ~5 minutes regardless).
- Runs ≤4 minutes may be polled by the lane itself.
- Mid-task long runs: fill the wait with independent work or deliver in
  stages; never idle-wait.
- NO lane self-keepalive crons, ever (unchanged from 2026-09-06).

This refines `docs/dev/lanes/BOILERPLATE.md`'s existing lifecycle section
(which described folding results back into the *same* lane's report on
completion): the new rule is that the lane does not wait around for that
completion at all once the report-with-OWED-numbers is committed.

## 3. Closure is the MANAGER'S act

At delivery acceptance, the manager stops the agent explicitly
(`TaskStop`). The manager checks for live agents at every delivery
acceptance and at session pause. Follow-ups go to fresh agents resuming
from the committed report, never to a lane kept warm on the chance of a
follow-up.

## 4. The monitoring ladder

Who watches a long run — matched to what kind of watching it needs:

| Rung | What it watches for | Who/what watches |
|---|---|---|
| (i) | Pure liveness/completion | A zero-model BACKGROUND WATCHER SCRIPT that exits with one notification only on actionable state (never a model-turn tick) |
| (ii) | Post-run mechanical follow-up (read log, fill owed numbers, re-pin) | A FRESH small-context Sonnet/Haiku agent |
| (iii) | Genuine mid-run judgment (staged runs, triage-on-first-fail) | A dedicated watcher AGENT with a CONCISE brief — tiny context, so its 5-min cache dying costs ~nothing; it blocks in a timeout-bounded script and acts on exit |
| (iv) | Merge/ruling | The manager |

A watcher agent (rung iii) never inherits a lane's design context — it
gets a brief written for exactly the watching task.

## 5. Main-session heartbeat

A 30-minute cron (two off-minute marks, e.g. `11,41 * * * *`) is
legitimate for the MANAGER session only — its cache is 1-hour TTL, so a
sparse heartbeat during a hold (a peer's battery, someone else's window,
an overnight hand-off) costs little. The prompt does the minimum: one
liveness check, one line on whether the awaited signal arrived, "if not:
do nothing else." Delete it at session close. This is not a precedent
for lanes (5-minute TTL — see §2's no-self-keepalive rule).

**A WAKE-RITUAL STEP, not a hold-time option (inbox I-62, Frank's
ruling 2026-09-09 after a full-day test on the pcrec manager session:
~30 ticks, one line each, cache-hit throughout, his usage read
confirming).** At EVERY manager-session start, right after reading
wake.md, create ONE recurring 30-minute cron (`CronCreate`, session-only
— it does not survive the session, so create it each start) at two
off-minute marks, never :00/:30. Its prompt is MINIMAL-ACTION: act only
on a delivered result, a notification or a completed run that has
arrived since the last tick; otherwise reply in one line and do nothing
else — never start new work from a tick. Delete it (`CronDelete`) as
part of the session-close routine (skill §7). Manager session ONLY;
lanes stay 5-minute TTL and never self-keepalive (§2). The pcrec manager
skill carries the same step as its step 0.

## 6. No forks/panels from giant contexts

Fresh agents get written briefs; critic panels convene early or from
compact contexts, never forked off a manager session whose context has
grown large over a long session.

## 7. Completion contracts (from [B13]'s post-mortem)

Three mechanical rituals, adopted because [B13]'s design cycle showed
each gap costing real rework:

- **(a) Panel consolidation ends with a by-id completeness check.**
  Every numbered finding in every critic file must appear in the
  consolidated review with a disposition — even "declined" — and that
  must be greppable by finding id. ([B13]'s r4 consolidation dropped two
  numbered findings — build #11, charter F10 — recovered only when the
  revision lane re-read the raw critic files.)
- **(b) A design cycle ends with the step-2 verification pass RUN, not
  scheduled.** "Owed" is not a terminal state for a design cycle; the
  pass runs before the cycle is called closed.
- **(c) Every delivery ends with a charter-vs-committed checklist.**
  Each promise in the originating brief either points at its committed
  artifact, or is listed OWED with an owner and a trigger for when it
  will land.

## Provenance

Full ruling text: `docs/dev/inbox_from_pcrec.md` I-60 (2026-09-08). Prior
model ruling (superseded): I-54 (2026-09-06), `docs/dev/decisions.md`
BD10's inline reference. See also `docs/dev/lanes/BOILERPLATE.md` (lane-
facing standing rules; §2-4/6 here overlap it deliberately — the lane
file states the mechanics lanes need, this file is the fuller record)
and `.claude/skills/pcrec-bench-manager/SKILL.md` §4 (the manager
process doc referenced by I-60).
