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
