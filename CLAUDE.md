# pcrec-bench — comparative regex-engine benchmark

Sibling project to ~/pcrec (the ahead-of-time PCRE→C regex compiler).
This repo measures regex engines against each other — pcrec among them,
as several pinned testees — on a harder and wider set than the usual
microbenchmarks, emits standardized per-testee artifacts, compares them
statically, and feeds the outliers back to pcrec as optimization work.

STATUS (2026-08-24): charter seeded 2026-08-17 (APPROACH.md); housekeeping
done; the REQUIREMENTS discussion with Frank ([B1]) is the open step. No
set, schema, adapter or comparator code exists yet. Manager sessions start
with the `pcrec-bench-manager` skill (.claude/skills/).

## MANDATE: repository scope

Work in this project touches ONLY the two mandated repositories
(~/pcrec-bench and ~/pcrec). Session-temporary files go in the session
scratchpad, never committed. Subagents inherit this mandate; state it in
their task briefs.

**~/pcrec is READ-ONLY from here** (docs/dev/decisions.md BD2): read its
docs, harnesses and corpora freely; never write to its main, branches,
`worktrees/` or build trees. Changes pcrec-bench needs in pcrec go to the
pcrec manager session as a request. pcrec does not touch this repo
(pcrec D52: dependencies live here, never there).

## Two sessions, one box (2026-08-24)

A pcrec manager session (`pcrecdev1`) and this project's (`pcrecdev2`)
may run concurrently on the same 12-core box. Rules (BD3, all measured
lessons): ONE heavy suite on the box at a time — announce heavy runs to
the other session first; the box's CPU-bounded checks lie under load, so
bench on a quiet box and record load in the artifact; large scratch under
the session scratchpad or `/var/tmp`, never `/tmp` root (7.6 GB tmpfs,
per-user quota); NEVER `pkill -f` — kill by PID with the cwd verified;
report a pcrec test failure to the pcrec session before concluding
anything from it; `gnutimeout` on every command of uncertain length.

## What this repo is

Versioned test sets (feature spread, backrefs, hazard classes, big
subjects, real-world shapes), one thin adapter per open-source engine, a
standardized per-testee output artifact with compile and match time
separated and its environment recorded, and a static comparator over
artifacts whose scoreboard excludes wrong answers. Read APPROACH.md first
— it carries the four founding principles, the architecture sketch, the
candidate roster, the correctness policy and the open questions (§8).

What it is NOT: pcrec's regression gate (pcrec keeps its own absolute
floors in tests/bench/compare). Dependencies (engines, build systems,
bindings) live here, vendored or system, pinned either way.

## Where things are

- `APPROACH.md` — the charter.
- `docs/dev/` — plan.md (grep'able `[Bn] STATE:` rows), plan_completed.md,
  dev_journal.md (append-only), decisions.md (BDn), pcrec_references.md
  (the map of every pcrec document this project depends on), wake.md
  (gitignored hand-off brief). See docs/dev/CLAUDE.md.
- `docs/design/` — living design notes (requirements, artifact schema, set
  format position, adapter notes, measurement dirs). See its CLAUDE.md.
- `.claude/skills/pcrec-bench-manager/` — the manager-session skill.
- Planned (not yet created): `set/`, `testees/<name>/`, `schema/`,
  `compare/` per APPROACH.md §3 — created when their plan rows start.

## Build & test

None yet. When they exist: plain `make` for what is ours; each testee
adapter may use whatever its engine demands (cmake, cargo, meson).

## Conventions (inherited from pcrec where they apply)

- Every directory has a CLAUDE.md describing purpose and files; update it
  when files are added/removed or change roles.
- Update the STATE tag in docs/dev/plan.md when starting/finishing a step;
  expand a milestone into substeps only when work on it begins; append a
  dev_journal.md entry after every significant session and at every stage
  boundary of an autonomous run (journal defensively).
- Measurement discipline travels from pcrec (its docs/dev/learnings.md
  §1-3, D12/D14/D15/D17/D35): quiet-box runs, medians with spread, per-core
  occupancy checked before pinned runs, environment recorded, archived
  probes with source headers, controls that share no source with what
  they control.
- Subagents as needed, lower models where the work fits; writers in
  worktrees under `worktrees/`; critics read-only; every brief restates
  the mandate and the box rules; long runs asynchronous with a stall
  watchdog. Details in the skill.
