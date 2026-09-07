# Decisions (ADR-lite)

One entry per significant decision. Format: id, date, decision, why,
revisit-when. Ids are `BDn` so they never collide with pcrec's `Dn`;
pcrec decisions are cited as `pcrec D52`.

## BD1 — 2026-08-24 — Docs and process shape mirror ~/pcrec, lighter

docs/{dev,design}, the plan's grep'able STATE tags, an append-only journal,
this log, a gitignored wake brief, a CLAUDE.md per directory, and a project
skill for the manager session — the same shape as pcrec (Frank, 2026-08-24:
"use ~/pcrec project as an example"). Lighter: no spec/ or reviews/ until a
first resident exists; known_issues/upstream_findings created at their first
row. Why: one set of habits across two repos, and a reader of either finds
the same file in the same place. Revisit: never expected.

## BD2 — 2026-08-24 — ~/pcrec is READ-ONLY from this project; writes go through the pcrec manager session

Two manager sessions share the box: pcrecdev1 (pcrec) and pcrecdev2
(pcrec-bench). This project reads pcrec freely (docs, harnesses, corpora,
`git archive`/read-only checkouts elsewhere) and NEVER writes to pcrec's
main, branches, worktrees/ or build trees. Anything pcrec-bench needs
changed in pcrec — a set-format the harness reads, a plan row, a
known_issues row from a bench finding — is handed to the pcrec manager as
a request (SendMessage), who cuts a branch/worktree or lands it. pcrec
does not touch this repo (pcrec D52: dependencies live here).
Why: the pcrec session runs long batteries whose evidence a foreign write
would corrupt; the mandate names both directories but ownership is per
project. Revisit: if the two projects are ever managed by one session
again, collapse this to the plain mandate.

## BD3 — 2026-08-24 — Box rules while both sessions are active (measured lessons from pcrec, 2026-08-24)

(1) ONE HEAVY SUITE ON THE BOX AT A TIME — this 12-core box's CPU-bounded
checks lie under load (pcrec K31 addendum / [TT-10]: load 31-85 made
tests/resource's cap and D45's compile budgets fail spuriously); bench
runs are the most load-sensitive thing either project does, so a bench
run announces itself to the pcrec session first and runs on a quiet box,
and records load in its artifact. (2) `/tmp` is a 7.6 GB tmpfs shared by
every suite's scratch, with a per-user quota that fails writes while `df`
shows space (pcrec tests/bench/CLAUDE.md) — large scratch goes under the
session scratchpad or `/var/tmp`, never `/tmp` root. (3) NEVER `pkill -f
<pattern>` — kill by PID with the cwd verified via /proc/<pid>/cwd
(pcrec lost a lane's sweep to a name-pattern kill). (4) A pcrec test
failure seen from here is reported to the pcrec session before anything is
concluded from it. (5) `timeout` (gnutimeout — pcrec docs/testing.md
:2407, the uutils timeout costs ~108 ms/call) on every command of uncertain
length. Revisit: when a single session owns the box.

## BD4 — 2026-08-25 — Python 3 is the project language for the harness, validator and reporter; standard python project files

Frank, 2026-08-25: "if we are adopting python as project language then
setup usual python project files e.g. requirements.txt so we can specify
these modules." So: the harness core, the record validator, the store
tooling and the reporter are python 3 (>=3.11; the box runs 3.14.4).
`pyproject.toml` states the package and its compatibility ranges;
`requirements.txt` carries EXACT pins measured working on the box (today:
jsonschema==4.19.2); the two are updated together. Testee ADAPTERS are
not python packages — each lives under testees/<name>/ with whatever its
engine demands (C shims, cmake, cargo), pinned there (pcrec D52:
dependencies live here). Why: one language for everything that is ours,
with pinned modules so a record produced on another machine was made by
the same tooling. Revisit: if a hot path (the in-process timing loops)
needs C — those belong to the adapters anyway.

## BD5 — 2026-08-25 — The durable channel with the pcrec manager (inbox/outbox, one writer each) and the build-vs-run division of labour are pcrec D78; this repo carries the files and the skill, not a second copy of the ruling

Frank, 2026-08-25, recorded by the pcrec manager as pcrec D78
(~/pcrec/docs/dev/decisions.md, grep D78). The ruling was first committed
INTO this repo's decisions.md by that session (d12abed) and reverted
(91e9251) as a wrong-repo commit: pcrec's decisions live in pcrec. What
this repo holds: `docs/dev/inbox_from_pcrec.md` (written and committed
ONLY by the pcrec manager, single-file `[inbox]` commits; this session
appends one `ack:` line per item and nothing else), `docs/dev/
outbox_to_pcrec.md` (written ONLY by this session; the pcrec manager
reads it at wake), and the `pcrec-bench-manager` skill's §0 text. Items
are numbered and never deleted; the files carry what must survive a
session boundary; live coordination stays interprocess (SendMessage)
when both sessions are up. Division of labour: this session BUILDS and
EXPANDS the bench; the pcrec manager RUNS it from a WORKTREE of this repo
(never a clone — the store is append-only and must not fork). Two record
tiers: PINNED (committed pcrec SHA via pin.sh, quiet window, the full
protocol) → canonical `store/`; SCRATCH (a provided binary, a `quick`
cell) → a scratch store the reporter can read but that never enters
`store/index.tsv` or the rankings ([B10]). Why: a SendMessage to a
session that is down or mid-task is lost; a file in the repo is not.
Revisit: if the inbox grows past what a wake-time read can absorb, split
it by topic — but keep one writer per file.

## BD6 — 2026-08-29 — A pinned window needs BOTH manager sessions IDLE, and a peer's HOLD is verified by cwd, not by relay

Measured in the 36d5963 window (journal fourth session part 2). The quiet
gate's per-core limit (10 % busy on any non-target core,
docs/design/quiet_baseline.md) was derived with ONE manager session on
the box; two claude processes streaming at once leave an 11 % residue on
a core with load1 ≈ 1.4, and the gate refused cell after cell until both
sessions stopped issuing tool calls. Rule: WINDOW OPEN means both
managers idle — no tool calls, no streaming — except the window owner's
reaction to its own Monitor events; the owner announces OPEN with the
cell list and expected end, CLOSED with the index count. Second rule,
also measured that day (two HOLD breaches by a peer lane, both after the
peer manager had relayed the hold): a hold is not a hold until the peer's
processes are gone — the window owner verifies by `/proc/<pid>/cwd`
under ~/pcrec/worktrees/ before OPEN and after any gate refusal that will
not clear in 60 s, and pauses its own launcher (kill by PID; the cells
already written stay) rather than letting the gate cascade through the
remaining cells. Third: the script's gate budget is 12 × 30 s
(scripts/run_window.sh) — 3 × 20 s lost cells; the post-cell 1-s
transient (OD-B12) still refuses the first attempt of nearly every cell
and a single-sample after-check can stamp a clean cell
`inconclusive-load` (two records that day) — OD-B12's fix (average or
min-of-N) is queued under [B12].

## BD7 — 2026-08-30 — The occupancy instrument is five 1-s mpstat intervals judged on their AVERAGE, not one 1-s sample (OD-B12 closed)

Five of five `inconclusive-load` records from the pinned windows of
2026-08-29 and 2026-08-30 failed on the AFTER occupancy sample alone:
one non-target core at 10.1-20.2 % on a single `mpstat -P ALL 1 1`
interval, load1 quiet, the before-sample clean, nothing sustained on the
box. `pidstat` during the bounded window named the bursts (the VS Code
remote server waking on the store write, a streaming Claude session's
~9 %, a half-second `gh pr list` from the status line). A one-second
sample cannot distinguish a burst from a competitor; three of six
bounded cells (about 60 minutes of a quiet window) were lost to it.

Ruled: `pcrecbench.quiet` samples `mpstat -P ALL 1 5` and judges the
`Average:` block (per-core busy averaged over five seconds), same
instrument at both ends, bar unchanged at 10 %; `occupancy.tool` names
the command so the two instruments' records are distinguishable; `raw`
keeps the Average block and the per-second peaks; X26 unchanged; no
schema change. Average, not min-of-N: the question the after-sample
answers is "was something else working on the box while this was
measured", and an average over five seconds is that quantity; a
minimum would also hide a competitor that paused. Why not raise the
bar: the measured noise floor (docs/design/quiet_baseline.md, 2-7 % per
core) has not moved, and a bar that admits an 11 % steady residue
admits a second manager streaming through a window, which BD6 forbids
for a reason. Controls: `tools/selfcheck.py check_occupancy_average`.
Records judged by the old instrument keep their verdicts; the three
bounded cells are re-measured under the new one in the next window.

## BD8 — 2026-09-04 — pcrec development lives on ANOTHER MACHINE; the D78 files stay canonical HERE (transport is ssh on pcrec's side), the live channel is Remote Control session messages, and the box is the bench's at night without a handshake

Frank moved pcrec development off the shared box on 2026-09-04 (inbox
I-44, 18:4x; the convention I-45 the same evening, commit 4475226, from
pcrecdev1 on the new machine). What holds unchanged: BD5 — one writer each
way, `docs/dev/inbox_from_pcrec.md` written and committed only by the
pcrec manager, `docs/dev/outbox_to_pcrec.md` only by this session; items
numbered, never deleted; every ruling and pin lands in the files, never
only in a live message. What changed, transport only: pcrec reads and
writes the two files over ssh from the new box; this session needs no
cross-machine access; the pcrec-bench copy on the new machine is a dead
snapshot nobody reads for current facts. LIVE coordination when both
managers are awake goes over Remote Control session messages (the
`pcrecdev1` name now resolves to the remote session; the UDS peer on this
box is gone), replacing the old same-box socket. Consequences for the
bench: (a) the box is the bench's at night with NO handshake to wait for —
BD6's "both sessions idle" reduces to "nothing of ours runs"; the quiet
gate and BD3's one-heavy-suite rule still apply to OUR OWN lanes; any heavy
load pcrec would ever want on this box (none planned) still goes through
the WINDOW OPEN / CLOSED handshake in the files; (b) pcrec's timings are
taken on a different machine from ours from now on — NEVER compared to
our numbers, only to their own baselines (I-44); (c) daytime `make check`
bursts here contend with nothing of pcrec's. Why: the two sessions had
been trading the box by handshake for two weeks and losing whole nights
to the other's batteries (journal, ninth session). Revisit: if pcrec ever
returns validation to this box, BD6's cwd-verified HOLD comes back with it.

AMENDMENT (I-46, 2026-09-04 evening, commit 2e44f58): the GitHub remote
(origin = github.com/fdicostanzo/pcrec-bench, Frank's) joins the channel as
READ transport — pcrec reads the two files by PULLING its clone; pcrec's
inbox WRITES stay ssh commits on this checkout (one committing checkout =
linear history, no push races; local-commit-plus-push only as a fallback
if ssh is down, and such a commit says so). The NEW HABIT: master is
PUSHED after every channel commit (outbox entries, inbox acks, BD
rulings). `git push` has been classifier-blocked from the manager session
(ninth session's lesson): each push is Frank's `! git push`, requested in
the session's closing line whenever channel commits are pending, or a
session-level allow if Frank grants one. This checkout stays canonical on
any disagreement until a push lands.

SECOND AMENDMENT (I-48, 2026-09-04 evening, commit 9d912d3): Frank parked
pcrec's cloud validation while travelling, so pcrec's full suites and
batteries RETURN to this box — over ssh in /home/duxevents/pcrec, detached,
inside /home/duxevents/{pcrec,pcrec-bench} only. The handshake resumes
INVERTED: pcrec REQUESTS a slot (live and/or as an inbox item) and waits
for the bench's current run; nothing of pcrec's starts without this
session's ack; the bench's windows keep priority under the I-47 grant —
slots are carved out of it by request, never by right. Consequence (a)
above is narrowed accordingly: the box is the bench's by default, and a
granted slot is a BD3 heavy run to plan around like our own (no pinned
cell, no `make check`, no build lane beside it). BD6's cwd-verified HOLD
applies to a granted slot for its duration.

## BD9 — 2026-09-06 — a HISTORY REWRITE of master to drop six refused records committed by mistake (Frank's ruling, done the same evening)

DECISION. bench/syntax's refused first sample left six `.staging-*/
*.jsonl.rejected` files (~90 MB) in `store/records/syntax@0.1/`; a blind
`git add store/` in a commit chain committed and pushed them (d5c645b).
They were removed from the tree the same hour (02d7f7e) and `.staging-*/`
+ `*.rejected` made .gitignore rules; the BLOBS stayed in history. Frank
ruled "proceed with filter repo to remove history blob" (typed into the
bench session, 2026-09-06 ~20:4x EDT); pcrecdev1 was told to HOLD pushes
first and confirmed its clone clean. Done in a fresh `--mirror` clone of
origin with `git filter-branch --index-filter 'git rm -r --cached
--ignore-unmatch -- store/records/syntax@0.1' --prune-empty -- --all`
(git-filter-repo's download was blocked by the session's classifier;
filter-branch on 589 commits took ~1 min): d5c645b pruned (it held
nothing else), every descendant re-hashed (5eb4402 → 43fdf8d at the tip;
pcrec's I-56 aad6242 → 517b6f8), every commit up to 26dad5d byte-identical
with the same SHA. VERIFIED before pushing: the tip's TREE identical
(`rev-parse ^{tree}` equal), 0 `.rejected` objects reachable, 588 vs 589
commits. Force-pushed from the LOCAL repo via a temporary ref (a push
FROM a mirror clone reports "up-to-date" because its branch refs double
as remote-tracking refs, and a `git fetch origin` inside a mirror
re-syncs every ref — both bit once); local master `reset --hard` onto
origin; pcrecdev1 resets its clone on DONE. The pre-rewrite mirror stays
at /var/tmp/pcrec-bench-mirror.git for a day as the fallback; the six
rejected files at /var/tmp/pcrecbench-rejected-2026-09-06/.

WHY. The store is the canonical measurement record; refused records
never belong in it, and 90 MB of them in every clone (pcrec's Mac clone
included) is weight paid on every fetch forever. Correctness was never
at stake (the files were never indexed); the rewrite is cheap now and
impossible later.

RULES THAT FOLLOW. (1) Never `git add` a store directory blind: add
`store/index.tsv` and the record paths the run log names, AFTER
`pcrecbench index` reports the count moved. (2) Any lane branch based on
a rewritten commit is REBASED (`git rebase --onto <new-base> <old-base>`)
before merge — merging it would resurrect the pruned history (lane/b36ids,
based on the old 6a0a764, is the live case at this writing). (3) A
history rewrite is Frank's call each time; the hold/DONE handshake with
pcrec's clone precedes and follows it.

REVISIT WHEN. Another rewrite is contemplated — check whether
git-filter-repo can be installed (a permission rule for the session), and
whether pcrec's clone has unpushed commits (then it rebases, not resets).

## BD10 — 2026-09-06 — the TRAVEL-MONTH EXECUTOR ARRANGEMENT (Frank's ruling, inbox I-57): this session runs pcrec's Linux commands on request, by exact-command inbox items

DECISION. From 2026-09-07 (Frank away with the Mac; the Linux box up with
no terminal for him) for about a month, the bench manager session
EXECUTES pcrec commands on this box when the pcrec manager asks. A
request is an inbox item carrying the exact command sequence verbatim,
the expected counts / green criteria, a log path under
/home/duxevents/pcrec/build/, and a done-signal trailer to quote back.
The executor reports — counts, the trailer, a red's log tail — and never
diagnoses or fixes (the session is Sonnet from its next start; I-54's
promote-don't-thin rule covers the bench's own analysis, and this role
asks for none). The bench's windows keep priority; BD3's one-heavy-suite
rule binds both sides. Live ssh light ops continue over a tailnet if it
comes up; the executor path is the fallback and the heavy-run path.

WHY. pcrec's owed Linux arm (the battery + mech + the stage-3 utf8
exact-agreement differential against this box's libpcre2 10.46) needs
this box's gcc 15.2 and oracle; nobody else can drive it for a month.

BD2 AMENDMENT (narrow). ~/pcrec stays read-only from this project EXCEPT
the pull / checkout of the commit an executor request NAMES (pcrec pushes
to github first): `git -C ~/pcrec pull --ff-only` or `git -C ~/pcrec
checkout <named-sha>` inside such a request, nothing else — never a
branch, worktree, build-tree or file write of our own devising. pin.sh's
`git archive` reads are unchanged.

REVISIT WHEN. Frank returns (~2026-10-07) or the tailnet makes the path
unnecessary; and if a request ever asks for judgment (a fix, a
re-aim, an interpretation) — decline it back to the inbox by name.
