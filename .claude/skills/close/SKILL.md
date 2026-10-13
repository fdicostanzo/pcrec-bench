---
name: close
description: Frank's request to reset the pcrec-bench manager session. Look for the next natural session-reset opportunity, honouring any urgency or modification Frank adds (e.g. "shutdown now as house on fire"). Use when Frank types /close.
---

# /close — find a session-reset opportunity

Frank wants the session reset. Your job is to find the right moment for it and get
there. HOW to close is not in this skill. The close procedure belongs to the manager
skill: `pcrec-bench-manager` §7 ("Session end or pause — rewrite wake.md"). Follow
that procedure as written. Add nothing to it here. (Copied from pcrec main's
`/close`, 2026-10-13, and adapted to this project.)

## What to do

1. **Read Frank's arguments first.** Anything he adds after `/close` OVERRIDES the
   default below: urgency ("now", "house on fire"), a deadline, or any other
   modification. Do what he says, at the speed he says.
2. **With no modifier, wait for the next natural opportunity.** That is the point
   where closing loses the least. In this project that is one of:
   - a lane delivery accepted, merged, and its worktree pruned (`scripts/wtprune`);
   - a window's records committed (explicit paths, never `commit -a`) and the
     WINDOW CLOSED sent to pcrecdev1;
   - a read's verdict merged and its outbox entry committed;
   - an inbox item acked into plan.md, or a ruling recorded.

   Do not start new work, and do not take on work that would push the opportunity
   further out: no new lane, no new window, no re-pin.
3. **What may keep running across the reset.** A detached window
   (`setsid ... & disown`, completion marker in its log) survives the session. If
   waiting for it would cost hours, closing while it runs is acceptable, but only
   when wake.md names it, its log and its marker, and says what the next session
   does when the marker appears (commit the records, send WINDOW CLOSED, launch the
   read). A live LANE does not survive the session: wait for its delivery, or stop
   it and record in wake.md what it left on its branch.
4. **Before acting, tell Frank in one or two lines** what you are waiting for (or
   that you are closing now), so he knows when the reset will be safe.
5. **Then run `pcrec-bench-manager` §7.** That covers the journal, plan.md STATE
   tags, the wake.md rewrite, the commit and push, `make wtprune`, `CronDelete` of
   the heartbeat, `TaskStop` of any live agent, and telling pcrecdev1 if a run of
   ours is still on the box. When it is done, say so plainly. Frank does the
   shutdown himself.
