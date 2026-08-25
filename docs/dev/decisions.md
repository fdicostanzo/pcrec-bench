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
