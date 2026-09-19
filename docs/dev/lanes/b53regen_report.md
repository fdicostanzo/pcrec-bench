# lane `b53regen` — the reporter-v18 FULL-REPORT REGENERATION WAVE

Branch `lane/b53regen`, worktree `worktrees/b53regen`. Charter item 2 of
Frank's matrix-standard ruling ([B52], merged to master 8689d8e/a3c1485
the same afternoon this lane opened): re-render every committed
`reports/` group against reporter v18, back-fill the new `.matrix.tsv`/
`.matrix.html` siblings, refresh the committed `.interpretation.md`
sidecars, and confirm `make check-interpret`. Never touched `store/`;
never merged (the manager merges).

## What was produced

**All 45 committed report groups** (138 files: 45 `.tsv` + 45 `.md` +
45 `.subject-grain.md` + 3 `.subject-grain.tsv`) re-rendered from each
file's own committed query, parsed out of its header line (`filters:`/
`grain:` — KB-16 is closed, so every render is a narrow CLI invocation
against the store, never a whole-store load). Diff-classified against
the last commit with a purpose-built (disposable, session-scratchpad-
only) driver, `regen_all.py`.

**Diff classification, final tally (138 renders):**

| class | count |
|---|---|
| `identical` | 0 |
| `expected` (version-line replace and/or `baseline` row insert only) | 138 |
| `anomaly` (unexplained delta) | 0 |
| subprocess failures | 0 |

Every group's diff was individually confirmed (spot-checked in full on
several groups, `git diff` read end to end) to contain ONLY the two
classes the [B52] charter predicts: the `reporter: v17` → `v18`
version-line replace, and the new unconditional `baseline` bullet
(`.md`) / row (`.tsv`) — item 3's baseline-identity fact — on every
rankable group. Zero unexplained deltas, unlike the 2026-09-17 KB-18
wave (which found two genuinely-moving groups it had to diagnose).

**New: `.matrix.tsv` + `.matrix.html` per group** (45 + 45, all
rendered clean via `scripts/matrix_page.py`, 0 failures). Every
`.matrix.tsv` carries the group's own provenance comment; every
`.matrix.html` is the derived self-contained page.

**Six committed `reports/*.interpretation.md` sidecars regenerated**
(`scripts/regen_sidecars.py`, 0 failures, ALL determinism-checked — a
second, independent `interpret` invocation to stdout diffs clean
against each committed file). Every sidecar's stamp lines (`report_
sha256`, `reporter`, and — after the KB-22 fix below —
`subject_grain_sha256` on the two that carry one) move to match the new
report content; every line below the stamp (the fired/not-fired rule
sections) is byte-identical to the pre-regen committed content on all
six.

**The 65-fixture `catalogue/fixtures/` corpus regenerated**
(`python3 catalogue/fixtures/gen.py`, 211 files) — a consequence of the
report regen this lane's brief did not originally name, but which
`make check-interpret` surfaced immediately (see incident 2 below) and
which has a direct precedent (commit `b6ee4e4`, the KB-18 wave's own
"the regen the v17 bump requires that the repdiag lane's list missed").
`gen.py --check` clean; every one of the 68 changed fixture files
carries only the same two expected delta classes as the report regen
itself (confirmed by a filtered `git diff` before committing).

**`make check-interpret`: 149 passed, 0 FAILED** (final run, this
lane's own worktree, after both incidents below were fixed).

## Two incidents, both found and fixed inside this lane

### Incident 1 — the classifier itself was quadratic and hung ~4 h

The first-pass diff classifier (`regen_all.py`'s `classify()`) used
`difflib.SequenceMatcher`, worst-case O(n²). It hung inside group
18/45's (`2026-09-02-bounded-0.3-...-cc-1989c62`) multi-million-line
`.subject-grain.md` diff; the manager caught it from OUTSIDE this lane
(CPU/no-child-process forensics on the detached PID, since a chatty
per-line Monitor is not itself a liveness proof once the process stops
emitting) and flagged it. Diagnosis confirmed exactly: PID 1252674 (cwd-
verified as this lane's own scratchpad script) had been inside
`classify()` for over 4 h at ~84% CPU with the render subprocesses for
that group already finished.

Fix: `classify()` rewritten as a linear two-pointer walk. The only two
expected delta shapes (a version-line replace, a `baseline` row insert)
are both locally resolvable by looking at only the current pair of
lines — equal lines advance both pointers, a recognized `baseline`
insert advances only the new pointer, a recognized version-line replace
advances both, anything else is recorded as ONE bounded anomaly and the
walk stops (no alignment search — that unbounded cost is exactly what
this rewrite removes). O(n) in the total line count. Verified before
resuming: a real already-regenerated group classifies as `identical` in
0.000s; a synthetic 500,000-line file with one inserted `baseline` row
classifies in 0.202s (the old classifier had no such bound at all).

Killed pid 1252674 by verified PID (never `pkill -f`), resumed from
group 18 with `RESUME_SKIP_GROUPS=17` + `RESUME_SKIP_KINDS=tsv,md` for
group 18 specifically (its `tsv`/`md` had already landed correctly
before the hang, confirmed by diffing their headers against v18 and
checking `sg_md`/`matrix.tsv` were still untouched). The resumed run
completed cleanly to group 45/45 with the same zero-anomaly result.

KB-18's own lesson two waves ago was "a legitimate class the classifier
missed" (an escaping rule it hadn't anticipated); this wave's lesson is
classifier *complexity* — a classifier that was CORRECT but could not
finish. Both are the same genus: a regen wave's own tooling is exactly
as fallible as the thing it verifies, and needs the same scrutiny.

### Incident 2 — `scripts/regen_sidecars.py` silently dropped a sidecar's subject-grain input (KB-22)

Found regenerating the six committed sidecars against the moved report
content: `regen_one()` recovered `report`/`index`/`predictions` from a
sidecar's own stamp but never `subject_grain` — so regenerating either
of the two `.subject-grain.tsv`-backed capability sidecars
(`2026-09-18-capability-0.1-...-after-cf0962e3` and
`...-ext-first-cf0962e3`) silently dropped R-BUCKET-DOMINATED's whole
section (33 firings, aggregated to 8 by testee, on the `after` sidecar)
while still passing the script's OWN determinism check — it agreed with
itself, just not with the original. Invisible until now: only one
sidecar carried a `subject_grain` stamp before [B47]/[B48], and this
script had never been run against a subject-grain-stamped one before
this wave.

Fixed in `scripts/regen_sidecars.py`: read `stamp.get("subject_grain")`
the same way `predictions` is read (absent/`(none)` handled
identically; a stamped-but-missing path is a NAMED failure, never a
silent narrowing) and pass `--subject-grain <path>` when present. Both
affected sidecars re-verified byte-identical below the stamp to their
pre-regen committed content, with R-BUCKET-DOMINATED's section
restored and `subject_grain`/`subject_grain_sha256` correctly stamped.
`docs/dev/known_issues.md` KB-22 and `scripts/CLAUDE.md` updated.

This is the SECOND time `make check-interpret`'s own gates caught a
regen-tooling defect the reports/CLAUDE.md "diff-classify against the
last commit" step could not have (sidecars aren't diffed against a
prior sidecar in this wave's own classifier — they're a downstream
render checked by `check-interpret` section 3's sha256 re-derive). The
`gen.py --check` fixture failure (68 files, "does not re-derive") that
first surfaced incident 2's investigation was itself a THIRD, separate,
already-precedented consequence (not a bug) — the fixture corpus is
literally projected out of `reports/*.tsv`, so moving those files
without regenerating fixtures is the same v17-bump miss commit
`b6ee4e4` already fixed once; this lane just paid it again and
regenerated the fixtures.

## Charter-vs-committed checklist

| charter item (team-lead's brief) | status |
|---|---|
| 1. Read `reports/CLAUDE.md` + `pcrecbench/CLAUDE.md` KB-18 method | DONE |
| 2. Re-render every committed group from its own header-derived query | DONE — 45/45 groups, 138 renders, 0 failures |
| 3. Diff-classify; only two expected classes; STOP on anything else | DONE — 0 anomalies across all 138 renders; two SEPARATE regen-tooling defects (not report-content anomalies) were found and fixed, not silently absorbed |
| 4. New `.matrix.tsv` + `.matrix.html` per group | DONE — 45 + 45, 0 failures |
| 5. Regenerate `.interpretation.md` sidecars, determinism-checked | DONE — 6/6, 0 failures, all determinism-checked; ALSO fixed KB-22 mid-step rather than committing a silently-incomplete regen |
| 6. `make check-interpret`; state the count; NOT check-harness/check | DONE — 149 passed, 0 FAILED. check-harness/full check NOT run (out of scope, per brief) |
| 7. Update `reports/CLAUDE.md`'s regen ledger section; note the wave where prior waves did | DONE — `reports/CLAUDE.md`'s `[B52]` matrix section (the back-fill paragraph replaces "NOT YET BACK-FILLED"), `pcrecbench/CLAUDE.md`'s `[B52]` section (a closing paragraph) |

**Owed to the manager:** merge this lane's four commits
(`d1c4756`, `d370ad8`, `70a2d3b`, `941193e`) onto master; nothing else —
every promise above is committed, not owed.

## Commits, in order

1. `d1c4756` — the 228-file report regen (138 modified + 90 new
   `.matrix.tsv`/`.matrix.html`).
2. `d370ad8` — KB-22 fix + the six sidecars refreshed correctly.
3. `70a2d3b` — the 68-file fixture corpus regen (`gen.py` write mode).
4. `941193e` — `reports/CLAUDE.md` + `pcrecbench/CLAUDE.md` documentation
   of the wave and its two incidents.

Head: `941193e`.
