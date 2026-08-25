# pcrec-bench Development Journal

Append-only log for restart/status recovery. Newest entries at the bottom.
Each entry: date — summary; accomplishments, issues, decisions, next steps.
Cross-reference docs/dev/plan.md row ids ([Bn]) and docs/dev/decisions.md
ids (BDn); pcrec's as `pcrec D52` / `pcrec [BENCH-1]`.

---

## 2026-08-24 (EDT), first session (pcrecdev2) — housekeeping; the requirements discussion opens

Context: Frank opened a SECOND manager session on the box (`claude -n
pcrecdev2`, started in ~/pcrec for access to its docs) and assigned it
~/pcrec-bench, which had sat at its 2026-08-17 seed (APPROACH.md +
CLAUDE.md, two commits, no code) while pcrec built its feature spine.
The pcrec manager session (pcrecdev1, the thirty-ninth pcrec session,
mid-[DD-14] with waves A-F merged, wave G and a D27 landing in flight, a
`make san` on main) is live on the same box; Frank asked the two to
coordinate directly. pcrecdev1 sent its box rules (load, git, /tmp, no
pkill -f, report failures) — accepted and recorded as BD2/BD3 — and a
complete reference dump of every pcrec-bench mention in pcrec (now
docs/dev/pcrec_references.md).

Accomplished ([B0], archived to plan_completed.md):
- docs/{dev,design} in pcrec's shape: plan.md ([B1] started, [B2]-[B7]
  placeholders from APPROACH §8 Q5, explicitly not commitments),
  plan_completed.md, this journal, decisions.md (BD1-BD3), wake.md
  (gitignored), pcrec_references.md (the map: D52, D12/D14/D15/D17/D35,
  [BENCH-1], [BENCH-CEIL], [ENG-PGO]'s profile cross-note, [DD-13]'s
  R-BENCH-1..9 and Frank's format inputs, the email specimen harness,
  the libpcre2 ctypes binding, learnings §1-3, K31/K32/[TT-10]).
- CLAUDE.md at every level (root rewritten from SEED to "housekeeping
  done, requirements open"; docs/, docs/dev/, docs/design/).
- .gitignore (wake.md, worktrees/, build trees).
- `.claude/skills/pcrec-bench-manager/SKILL.md` — the manager skill,
  modelled on pcrec's `pcrec-manager` with this repo's wake order, the
  two-session rules, and the delegation/watchdog/async conventions that
  pcrec paid for.

Read this session (pcrec, read-only): wake.md (pcrecdev1's mid-session
checkpoint), journal parts 1-18 of the thirty-ninth session, plan rows
[DD-14.*]/[BENCH-1]/[BENCH-CEIL]/[DD-13], D52/D71-D73, dd13_format
requirements §5 + frank_inputs.md, tests/bench + compare/ CLAUDE.md, the
email specimen README.

Facts worth carrying: (a) APPROACH §8 Q1 (set format) is resolved IN
DIRECTION — owned by pcrec's [DD-13], whose design/panel steps have not
started; an interim carrier is this project's problem. (b) No feedback
mechanism into pcrec's plan exists; pcrecdev1 proposes rows keyed by the
artifact's mechanism stamps (engine, RX_VM_PREFILTER, RX_VM_RUNGS) so
outliers bucket by mechanism. (c) Engines Frank has named: libpcre2 10.46,
perl 5.40.1, python re; no roster ruled. (d) The email specimen is a
ready-made first row with a dlopen libpcre2 throughput harness (no
pcre2.h on the box). (e) The box lies under load; bench on a quiet box.

Next: [B1] — the overall-requirements discussion with Frank (points to
put to him listed in wake.md), then docs/design/requirements.md and its
critic panel.

## 2026-08-24 (EDT), first session (part 2) — the requirements RULED (R1-R11); requirements.md DRAFT v1; the critic panel opens

Frank ruled the eleven requirement points in conversation (~22:5x-23:3x):
R1 loop-first (positioning second); R2 three subject regimes — large-
subject throughput, short-subject search (~256 B), and MATCH/compliance
on 10..1000 B subjects (bands TBD) — plus compile/setup cost on its own
axis; R3 HARNESS FIRST — the roster is for design and grows later,
COMPILERS included; per-(pattern, testee) OUTCOME is an axis (compiled /
did-not-compile / crashed / timed-out / unsupported), and a SYNTAX-VARIANT
axis admits engines that are not PCRE2-exact (same intention, declared
adaptation); testee dimensions = hardware, version, categorization
(interpretive/compiled/JIT; DFA/NFA/backtracking/hybrid); the hand-C
ceiling arm explained and ruled NOT in the first cut; R4 pcrec is the
special case — its variations are separate testee engines (later SIMD
on/off); R5 the SUB-BENCH is the unit: a self-contained DIRECTORY with a
goal, possibly several related patterns, data files, engine-specific
notes/adjustments; a RECORD = one sub-bench × one testee configuration
with all factors (date, hardware...); records gathered INDEPENDENTLY,
never the whole gamut; the product is data gathering + reporting; R6
the pattern format BLOCKS on pcrec's [DD-13] ("the rxt should be coming
pretty soon") — design and gather until blocked, then stop, no interim
carrier; R7 JSONL record with a general-setup layer + N raw results
reduced to comparables (min/max/stddev... TBD); R8 correctness as
chartered, tempered by the goal of RELATABLE, ACTIONABLE data — the same
pattern INTENTION may be expressed by a modified pattern per engine and
still compare (deviation grades = manager's sharpening, unruled); R9 the
deliverable is a QUERY-DRIVEN REPORT over the store ("sub-bench A1,
open-source, compiler-only"); delivery into pcrec case by case until the
model is clear (pcrecdev1 may not be running); R10 check load and wait
until quiet; R11 the first cut agreed in substance, changeable after
design.

Written: docs/design/requirements.md DRAFT v1 (13 sections: purpose,
vocabulary, regimes, testees + outcome + variant axes, sub-benches,
record, correctness, reporting, box discipline, first cut, APPROACH §8
dispositions, OD-B1..B8, the panel attack list). General rule from
Frank: commit often, push as needed (no remote configured yet; branch
here is `master`). Housekeeping committed 7789bd1. Next: the D6 panel
(three read-only sonnet critics: data model/report completeness;
semantics/variant axis/charter consistency; blocking point/first cut/
measurement validity) → triage → Frank adopts → [B2].
