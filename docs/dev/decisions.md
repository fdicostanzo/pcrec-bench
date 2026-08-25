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

## D78 — pcrec ↔ pcrec-bench: DURABLE rulings, priorities and pins travel by two single-writer files in the bench repo; live coordination stays interprocess; the pcrec manager RUNS the bench, the bench session BUILDS it (Frank, 2026-08-25)

**Context.** The post-spine loop is edit → measure. Its priorities and
pins were being sent by SendMessage to pcrecdev2, which might be down or
mid-task, and its runs went through `git archive` + build + a whole
sub-bench (many minutes) for every question.

**Decision (Frank).** (1) `pcrec-bench/docs/dev/inbox_from_pcrec.md` —
written and committed (single-file, `[inbox]` prefix) ONLY by the pcrec
manager; pcrec-bench's session reads it at wake, moves items to its
plan.md, and appends one `ack:` line per item. `outbox_to_pcrec.md` is
the reverse, read by the pcrec manager at wake. Numbered items, never
deleted. This is NOT a ban on interprocess messages — when both
sessions are up, questions and coordination flow live as before; the
files are the avenue for what must survive a session boundary. pcrec
stays read-only from the bench (bench BD2); nothing flows into pcrec's
tree. (2) The bench session's purpose is building and expanding the
bench; the pcrec manager runs it as needed from a bench WORKTREE (not a
clone — the store is append-only and must not fork). (3) The loop is
made fast by three bench features (inbox I-4): a SCRATCH record tier
that never enters the canonical store; `quick`, one cell inline; and a
`pcrec-local` testee taking a provided binary + flags, scratch-tier by
construction. First inbox: I-1 re-pin 692c2e8, I-2 the ruled sub-bench
order, I-3 the DFA stamp blocker, I-4 the loop features. CLAUDE.md's
situation index carries the wake-time read.
