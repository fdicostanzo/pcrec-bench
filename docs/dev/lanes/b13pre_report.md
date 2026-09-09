# lane `b13pre` — [B13.2] reporter preconditions P-1/P-2 (+ a manager-ruled fix)

Branch `lane/b13pre`, worktree `worktrees/b13pre`. Commits so far:
`18d70ac` (P-1/P-2), `17a28cf` (cwd-independent provenance paths).

## Brief

Implement `docs/design/interpreter_v1.md` §2.5's two reporter
preconditions the [B13] interpreter design depends on — **P-1**
(`floor_pattern:` header key, for R-FLOOR-2) and **P-2** (give-up
smallest-subject metric rows, for R-STATUS-12) — one `REPORTER_VERSION`
bump, one full regeneration of `reports/`.

## Status in one line

**Code, tests and docs: DONE and committed. The `reports/` regeneration
is OWED** — the store load that regeneration needs has been killed
twice as a harness-tracked task on this box tonight (a real, documented
hazard, not a bug in the regeneration script); a third, DETACHED attempt
is running now (see "Regeneration: OWED" below) and a fresh agent should
verify its marker and finish from there.

## P-1 — `floor_pattern:` header key

Implemented exactly as specified. `_floor_pattern_header_value(rd)`
(`pcrecbench/report.py`) takes the DISTINCT set of `ReportData.
floor_pattern_by_sb.values()` ([B14] R9, derived from the records' own
`patterns[].role`, never from `bench/`): zero → the literal `none`;
exactly one → that pattern id; more than one → the sorted ids joined
with `,`. Appended as the LAST key of `render_tsv`'s header comment,
after `worst_other_core_busy` — no existing key's position moves.

**The multi-subbench case does not fire on any committed report**: every
committed query is one sub-bench, confirmed by the regen script's own
per-file `floor_pattern=` printout (see below) — every value is `none`
or a single pattern id (`floor` for every set that has adopted [B15]'s
floor pattern; `none` for the two pre-1.3 email-specimen@0.1 reports).
Tested directly with a synthetic two-subbench, two-distinct-floor-pattern
report in `test_floor_pattern_header_key_p1` (the `,`-joined case no
committed report exercises).

## P-2 — give-up smallest-subject metric rows

Implemented exactly as specified. One extra `excluded`-section row per
DISTINCT give-up code, immediately after its base row, in the same
sorted-code order `_gave_up_cell_summary` already renders. Refactored
`_gave_up_cell_summary` to build its grouping through a new pure helper,
`_gave_up_cell_detail(failing_detail, subject_bytes)` →
`[(code, smallest_subject_id, smallest_bytes_or_None, n_subjects), ...]`
sorted by code — the ONE derivation both the human string and the new
TSV rows read (never a second re-derivation). Row shape: the base row's
`pattern`/`regime_or_na`/`form`/`fact`/`testee`/`status`/`tier` copied
verbatim; `subject_or_na` = the code's smallest subject id; `rank_or_na`
= `""`; `metric` = `giveup_smallest`; `value` = the code; `n` = the
smallest subject's byte count (`""` when unknown, matching the human
render's `?`); `pass_rate` = `""`; `n_gave_up` = the SUBJECT count for
this code (deliberately not `r.n_gave_up`'s trial count — the base
row's own column keeps its old meaning; the new rows read the same
column name per-code); `n_wrong`/`gave_up_summary`/`delta_verdict` =
`""`. 18 columns throughout; the base row is byte-identical to before.

**Grain decision, stated as the brief asked**: P-2 fires at **set grain
only**, and not via a bespoke guard — `failing_detail` is a `SetCell`
-only field (`reduce.py`'s `MatchCell.__slots__` carries no such
attribute), so at `--grain subject` the pre-existing
`hasattr(r, "failing_detail")` gate that already decides the base row's
`gave_up_summary` is `False`, and P-2's loop shares that exact gate. No
committed report is at subject grain (every `.tsv` under `reports/` is
set-grain; `--grain subject` renders only to `.subject-grain.md`, which
has no TSV sibling at all), so this is untested against a real subject-
grain TSV, but the code path cannot diverge from the base row's own
established behavior.

**Section scope**: `excluded` only. `not_ranked`/`scratch` rows can also
carry a non-empty `gave_up_summary` today, but R-STATUS-12's own input
is `report:excluded` (interpreter_v1.md §4.1) and the design's row shape
names `section=excluded` explicitly, so P-2 does not fire on those
sections even when they carry give-ups.

**No deviation from §2.5 as written.**

## The manager-ruled addition: cwd-independent provenance paths

Found while regenerating `reports/`, not part of the original brief —
ruled in-scope by the manager mid-lane. `render_markdown`'s two
per-record-listing `os.path.relpath(path)` call sites (the included-
records bullet, the excluded-invalid-records bullet;
`pcrecbench/report.py` — grep `rd.store_parent` for both) rendered a
path relative to the **process's current working directory at render
time**. Ten of the 42 committed report groups (every 2026-09-05 file,
listed below) were originally rendered from a lane worktree two levels
below the repo root and read `../../store/records/...`; every other
file reads `store/records/...` for the identical shape of query —
`fixtures/golden/store_v8.md`'s own note already flagged this
fragility ("same cwd, so the paths match").

**Fix**: a new `ReportData.store_parent = os.path.dirname(os.path.
abspath(args.store))` (the STORE directory's own PARENT, set once in
`build_report`), and both call sites now read `os.path.relpath(path,
rd.store_parent)`. The same query now renders byte-identically from any
cwd. New test `test_provenance_path_cwd_independent` renders the same
fixture record from two different cwds and asserts byte-identical
output, plus that the path is store-parent-anchored (`store/records/...`)
with no `../` segment from either cwd.

`fixtures/golden/store_v8.md`'s three affected lines were corrected in
place (not a full re-render — every other line was already diffed
byte-identical against the pre-fix v15 rendering before the edit),
documented in `pcrecbench/tests/fixtures/CLAUDE.md`'s golden entry.

**The ten files this normalizes** (their `.md` and `.subject-grain.md`
siblings both carry the old prefix; `.tsv` never does — `render_tsv`
carries no path at all):

```
2026-09-05-altwide-0.2-budu-ryzen1600-after-334fd10e
2026-09-05-altwide-0.2-budu-ryzen1600-island-334fd10e
2026-09-05-bounded-0.3-budu-ryzen1600-ccboth-288d505
2026-09-05-bounded-0.3-budu-ryzen1600-fold-334fd10e
2026-09-05-bounded-0.3-budu-ryzen1600-step2-after-288d505
2026-09-05-email-specimen-0.2-budu-ryzen1600-after-288d505
2026-09-05-loglines-0.1-budu-ryzen1600-noedge-288d505
2026-09-05-loglines-0.1-budu-ryzen1600-noedge-334fd10e
2026-09-05-loglines-0.1-budu-ryzen1600-noedge-3pins-334fd10e
2026-09-05-loglines-0.1-budu-ryzen1600-noedge-vs-1989c62-288d505
```

(found by grep: `grep -oE '\([./]*store/records/' reports/*.md`, then
the prefix before `/records/` per file — 64 lines read `store`, 20 read
`../../store` across the 84 real `.md` files (42 `.md` + 42
`.subject-grain.md`), grouped exactly onto these 10 basenames × 2 files
each.)

## `REPORTER_VERSION`

`v15 (2026-09-05)` → **`v16 (2026-09-08)`**. History recorded in both
`report.py`'s module docstring (two dated sections: the P-1/P-2 wave,
then the cwd-independence addition) and `pcrecbench/CLAUDE.md`'s
per-version log, in the file's own established style.

## Tests

Four new tests in `pcrecbench/tests/test_report.py`:
`test_floor_pattern_header_key_p1`, `test_giveup_smallest_rows_p2`,
`test_giveup_smallest_rows_two_codes_p2` (hand-built two-code cell no
fixture had; also proves `n=""` on an unknown-bytes subject, never `?`
or `None`), `test_provenance_path_cwd_independent`.
`test_reporter_version_pin` updated to `v16`.

**Count**: 75 tests in `test_report.py` (was 71) + `test_quick.py`'s 7 =
**82 reporter-side tests**.

**Run so far** (everything that does NOT need the real 160-record
`store/` — i.e. everything except the 7 tests that read `REAL_STORE`
for real `engine_metadata` across two pcrec pins, none of which this
lane's changes touch): **68/68 passed, 1.8 s**
(`python3 -m pcrecbench.tests.test_report`'s `TESTS` list minus the 7
`REAL_STORE`-sourced ones, run directly — command and full transcript in
this lane's shell history; re-run trivially with the snippet below).

```
python3 -c "
import sys, inspect
sys.path.insert(0, '.'); sys.path.insert(0, 'pcrecbench/tests')
import test_report as tr
skip = {n for n in dir(tr) if n.startswith('test_')
        and 'REAL_STORE' in inspect.getsource(getattr(tr, n))}
ok = sum(1 for t in tr.TESTS if t.__name__ not in skip and (t() or True))
print(ok, 'passed')
"
```

`make check-schema`: **4 example(s) accepted, 72 sabotage(s) rejected
for the intended rule, 0 WRONG** — unaffected by this lane, re-verified
after these changes.

`python3 -m pcrecbench.tests.test_quick`: **7/7 passed** — unaffected,
re-verified.

**OWED: the full `python3 -m pcrecbench.tests.test_report`** (all 82,
including the 7 `REAL_STORE` ones) **and `make check-report`** (which
runs the same module plus `test_quick` plus a CLI smoke). Both need the
real `store/` loaded, which is exactly the operation currently failing
under the harness's memory heuristic (see "Findings" below) — not
expected to fail on its merits (nothing in the 7 REAL_STORE tests
touches P-1, P-2, or the two `render_markdown` call sites this lane
edited; they test `_mechanism_stamp_columns`/jitter/buffer legends/
artifact-bytes/superseded-shortening/engine-reading, none of which this
lane's diff moves), but not run end to end this session. A fresh agent:
run `make check-report` DETACHED per the pattern below (it pays the
same ~750 s load) and quote the tail.

## Regeneration: OWED

**Not yet landed.** A hand-written, one-off in-process script
(`/tmp/claude-1001/.../scratchpad/regen_b132.py` — SESSION scratchpad,
gone with this session; a fresh agent regenerating from scratch should
rewrite it from this report's description, not hunt for the file)
reconstructs each of the 42 committed `<date>-...` report groups'
exact query from its own committed `.tsv` header line (the interpreter
design's own header-parsing rule, §2.1: split on `; `, rejoin any
fragment not matching a known `key: `), loads `store/` ONCE, renders
`.tsv` + `.md` + `.subject-grain.md` for each group, and — BEFORE
writing anything for a given group — classifies its diff against the
committed content: the ONLY allowed deltas are (a) the version-line
stamp, (b) on `.tsv` only, the new trailing `; floor_pattern: ...` key
and any number of NEW lines whose 11th tab column reads
`giveup_smallest`, (c) on the ten files above, the `../../store` →
`store` provenance-path normalization. A group whose diff carries
anything else ABORTS the whole run (nothing further is written) so a
partial, silently-wrong regeneration can never land; each group is
written to disk immediately once it classifies clean (streamed, not
accumulated, to keep peak memory down).

**Three attempts died, all for the SAME underlying reason — not a bug
in the regeneration logic** (see Findings #3): the store load itself
(160 records, 597 MB on disk) was killed as a harness-tracked
background task twice (runs 4 and 5), the second time before even
finishing the load. **Run 6 is currently in flight, launched DETACHED**
(outside the harness's tracked-task memory heuristic, per the box's own
history — see Findings #3):

```
LOG=/tmp/claude-1001/-home-duxevents-pcrec-bench/01ae41ff-6171-48d8-8bc2-5ffd2cd96f47/scratchpad/regen_run6.log
```

**Completion marker**: the line `DONE rc=0` appended to that log
(`DONE rc=<n>` for any other exit). On success the log's tail also
carries, per file, `OK <name>: +<n> giveup_smallest row(s),
floor_pattern=<value>, cwd_path_fix=<True|False>`, then a
`--- PER-FILE SUMMARY ---` table repeating those four fields per file,
the store load's measured wall time and byte count, and the count of
files the cwd-path fix touched (expected: exactly the 10 above).

**On the marker landing (`DONE rc=0`), a fresh agent should**:
1. `tail -100` (or the whole thing — it is short once past the load) the
   log and confirm `REGEN_COMPLETE` and `DONE rc=0` both appear, no
   `ABORT` line anywhere.
2. `git status --short reports/` — expect exactly 126 modified files
   (42 `.tsv` + 42 `.md` + 42 `.subject-grain.md`; `git add reports/`
   entire directory).
3. Prove the delta is exactly the intended one, per this lane's own
   design: for every `.tsv`, `git diff` filtered to drop (i) the header
   line's `reporter:` stamp and its new trailing `floor_pattern:` key
   and (ii) added rows with `$11 == "giveup_smallest"` must be EMPTY —
   e.g.
   ```
   git diff -- reports/*.tsv | grep -E '^[+-][^+-]' \
     | grep -v '^[+-]# reporter:' \
     | awk -F'\t' '{ f=substr($0,1,1); $0=substr($0,2) } NF<11 || $11!="giveup_smallest"'
   ```
   should print nothing (adjust the awk field split to account for the
   leading +/- already stripped above — verify by hand on one file
   first, since the diff's leading `+`/`-` sits before the TSV's own
   tab-separated fields and shifts column counting by one character,
   not one field).
4. For `.md`/`.subject-grain.md`: `git diff -- reports/*.md` should show
   ONLY the version-line change everywhere, plus the `../../store` →
   `store` line-pair on the ten named files' provenance bullets —
   nothing else.
5. Fill this report's per-file table below from the log's own printed
   summary (copy verbatim — do not recompute), commit `reports/` with a
   message citing this lane and the log's summary, update
   `reports/CLAUDE.md` with a `[B13.2]` entry in the file's own
   established style (who/when/why, the delta shape, per-file counts —
   the `[B32] (b)` entry is the closest precedent for wording), send the
   manager a handback naming this report's completion.

**Per-file table: OWED — to be filled from `regen_run6.log`'s own
`--- PER-FILE SUMMARY ---` block once `DONE rc=0` lands.** Columns:
`file | reporter (before → v16) | giveup_smallest rows added |
floor_pattern | cwd_path_fix`. The "before" reporter version per file,
measured directly (`head -1 reports/*.tsv | grep reporter:`) before
this lane's regeneration: **26 files at `v12 (2026-09-02)`, 5 at
`v13 (2026-09-03)`, 5 at `v14 (2026-09-05)`, 6 at `v15 (2026-09-05)`**
(26+5+5+6 = 42) — cross-check the post-regeneration `git diff`'s own
removed header line per file rather than retyping this table by hand.

## Findings (for the manager to file)

1. **Store load time**: `report.load_all()` over the current 160-record
   `store/` (597 MB of `.jsonl` on disk) takes on the order of **750 s**
   on this box (consistent with the `[B36]` precedent's own measured
   748 s at the same 160-record store) and holds roughly **3.6 GB RSS**
   while loaded — `schema/validate.py`'s jsonschema validation is the
   cost center (per the `[B12]` test-suite note), and it validates the
   WHOLE store regardless of how narrow a query's own filters are. The
   `[B13.3]` interpreter implementation lane (which reads the same two
   inputs, TSV + `store/index.tsv`, per `docs/design/interpreter_v1.md`
   §2.2/§8(2)) will want a FROZEN fixture store for `make check-interpret`
   rather than re-paying this cost per check run — the design note
   already says as much (§3.1's `golden/index@<date>.tsv` snapshot).
2. **The cwd-dependent provenance-path defect** (fixed this lane, see
   above) — recorded here as the historical shape of the bug for
   whoever next touches `render_markdown`'s path rendering.
3. **Tracked-task memory kills, twice, silent or late.** Two
   `run_in_background: true` invocations of the regeneration script
   (runs 4 and 5) were killed by the harness's own memory heuristic
   while holding the loaded store (~3.6 GB RSS) — `free`/`available`
   readings at the time (per the manager's own read) showed no real
   shortage (11 GB `available`, later 5 GB `free`). Run 4's kill
   notification did not reach this session in a useful window — the
   manager caught it first by reading the dead log directly; run 5's
   "killed / low on memory" notification arrived once polled for. A
   THIRD attempt, run 6, is
   running DETACHED (`setsid ... & disown`, a marker appended by the
   wrapping `bash -c`) specifically to sidestep this heuristic, per this
   session's own updated `docs/dev/lanes/BOILERPLATE.md` box-facts
   section and the `long-runs-setsid-not-background-tasks` memory this
   session wrote. Filed here as a finding, not re-litigated as a
   decision — the manager already amended BOILERPLATE with the rule
   this lane's own three attempts established.

## Charter-vs-committed checklist

| brief item | status |
|---|---|
| P-1 `floor_pattern:` header key | **DONE**, committed `18d70ac` |
| P-2 `giveup_smallest` rows | **DONE**, committed `18d70ac` |
| `REPORTER_VERSION` → v16 | **DONE** |
| History block (report.py + pcrecbench/CLAUDE.md) | **DONE**, two dated sections (P-1/P-2; the cwd fix) |
| Tests (P-1 present/absent/multi; P-2 one-code/two-code/no-giveup/18-col/byte-identical base row) | **DONE**, 4 new tests, all passing |
| Grain decision stated | **DONE** — set-grain-only, via the existing `failing_detail` gate, no new branch |
| `make check-schema` | **DONE**, green (4/72/0), re-verified after this lane's changes |
| `make check-report` (full, incl. `REAL_STORE` tests + CLI smoke) | **OWED** — needs the same store load; not expected to fail on its merits, not run end to end this session |
| Regenerate all 42 committed reports | **OWED** — run 6 in flight, detached, marker `DONE rc=0` in `regen_run6.log` (see above); three earlier attempts (2 tracked, memory-killed; 1 pre-cwd-fix, abandoned) are why this is owed rather than done |
| `reports/CLAUDE.md` `[B13.2]` entry | **OWED** — write after regeneration lands, from the log's own summary |
| Per-file diff proof (git diff filtered, must be empty) | **OWED** — script and exact command given above |
| `pcrecbench/CLAUDE.md` report.py entry | **DONE**, committed `17a28cf` |
| Deviations from §2.5 | **NONE** |

## Regeneration, run 7 (lane `b13regen`, 2026-09-09)

Fresh follow-up lane, same worktree/branch. Run 6 (above) loaded the
store in 745.7 s and WROTE 26 of the 42 groups (every v12-stamped file,
alphabetically first) before ABORTING on group 27
(`2026-09-05-altwide-0.2-budu-ryzen1600-after-334fd10e.md`, `DONE rc=1`
in `regen_run6.log`) on an "unexplained diff" confined to the `shape=`
legend bullet's line. Cause confirmed: that file (and 15 more --
5 stamped v13, 5 stamped v14, 6 stamped v15) predates one or more of
the v13/v14/v15 reporter bumps, none of which regenerated any committed
report (`pcrecbench/CLAUDE.md`'s per-version log says so explicitly for
each), so jumping a v13/v14-stamped file straight to v16 legitimately
picks up that backlog of LEGEND wording (v14: `folds=`/`islands=`/
`shape=` clauses as brand-new bullets on a v13 file; v15: an appended
paragraph on the `shape=` bullet, I-50 1's reconcile, as a same-line
wording change on a v14 file) on top of P-1/P-2's own deltas -- not a
bug in the regeneration script's classifier, which run 6 correctly did
not yet know how to explain.

**Two changes to `regen_b132.py`** (script only; `pcrecbench/report.py`
untouched):

1. **Skip already-v16 groups.** Before opening a group's `.md`
   siblings or touching the store, its `.tsv`'s header is checked; a
   header already reading `reporter: v16 (2026-09-08)` prints `SKIP
   <base> (already v16)` and moves on. Verified against the real
   `reports/` directory (no store load needed for this check): all 26
   files run 6 wrote skip, all 16 remaining (5 v13 / 5 v14 / 6 v15)
   fall through to processing.
2. **`classify_md_diff` accepts LEGEND-BULLET deltas on a v13/v14-before
   file.** A new `legend_reference` parameter (`{token: exact_line_text}`,
   built once by `_legend_reference_map` from every CURRENTLY COMMITTED
   v15-stamped `.md`/`.subject-grain.md` report, grouped by sub-bench,
   read straight off disk before this run writes anything) is passed
   only when the file's OWN before-stamp is v13 or v14
   (`_version_number`/`OLD_VERSION_FOR` on its `.tsv` header). Per
   difflib opcode: a same-line-count REPLACE or a pure INSERT is
   accepted iff every line in `removed` is itself a legend-definition
   line (`_legend_token`, the `    - <token> = ` shape report.py's
   `out.append("    - ` call sites use -- confirmed by grep that the
   two OTHER `    - ` bullets in report.py, the excluded-invalid-record
   listing and `newer, not measured: ...`, do NOT match this shape and
   so cannot be swept in by accident) and every line in `added` is a
   legend line whose text is BYTE-IDENTICAL to
   `legend_reference[token]` -- the proof the delta is the reporter's
   own already-shipped v14/v15 wording, not something else. A removed
   line that is not a legend line, an added line that is not a legend
   line, or a legend line whose new text does not match the v15
   reference still aborts the whole run, same as any other unexplained
   diff. Counted as its own delta, `legend_v13_v15`, printed per file
   and totalled, beside `giveup_smallest`/`floor_pattern`/`cwd_path_fix`.

**Verified before launching** (no store load required for any of
this): `python3 -m py_compile` clean; the classifier tested directly
against the EXACT old/new `shape=` lines from run 6's own ABORT message
(accepted, `n_legend=1`, WITH a matching reference; correctly rejected
WITHOUT one and when the new text does not match a given reference); a
synthetic pure-insertion case (two brand-new legend lines with no
`removed` counterpart) accepted; `_legend_reference_map` run against
the real `reports/` directory returns the five sub-benches needing a
fix (`altwide`, `bounded`, `email-specimen`, `loglines`, `syntax` --
`syntax` is not itself owed a legend fix but its v15 file is a valid
reference source for the others) with plausible token sets per
sub-bench (`email-specimen`'s is the narrowest: `edge`, `edges`,
`folds`, `sel`, `start` only -- no VM-only tokens, consistent with that
set's simpler patterns); the skip check against the real 42 `.tsv`
files matches the predicted 26-skip / 16-process split exactly.

**Launched, DETACHED, per BOILERPLATE** (the store load is the same
~750 s / ~3.6 GB RSS operation that killed two earlier tracked
attempts):

```
LOG=/tmp/claude-1001/-home-duxevents-pcrec-bench/01ae41ff-6171-48d8-8bc2-5ffd2cd96f47/scratchpad/regen_run7.log
```

**Completion marker**: the line `DONE rc=0` appended to that log (any
other `rc` is a failure). On success the tail carries `REGEN_COMPLETE`,
the per-file `OK`/`SKIP` lines (16 `OK`, 26 `SKIP`), and a
`--- PER-FILE SUMMARY ---` block with `giveup_smallest`/
`floor_pattern`/`cwd_path_fix`/`legend_v13_v15` per file plus the
aggregate totals -- the store load time is repeated here as its own
finding, same as run 6's.

**On the marker landing (`DONE rc=0`), a fresh agent should**, in
addition to run 6's own five resume steps (still accurate: the giveup/
floor_pattern/cwd-path proof commands are unchanged) --

6. Confirm exactly 16 `OK` lines and 26 `SKIP` lines in the log, no
   `ABORT` anywhere.
7. For the `legend_v13_v15` delta specifically: `git diff` on the 5
   v13-before and 5 v14-before files' `.md`/`.subject-grain.md`, filtered
   to drop the version-line change, should show ONLY lines matching
   `    - <token> = ` (new or changed) -- e.g. spot-check
   `2026-09-05-altwide-0.2-budu-ryzen1600-after-334fd10e.md`'s `shape=`
   line against the log's own `legend_v13_v15` count for that file, and
   confirm the new text is byte-for-byte what
   `2026-09-06-altwide-0.2-budu-ryzen1600-after-d34c9131.md` (a v15 file,
   same sub-bench) already carries for that token.
8. `git status --short reports/` should now show all 126 files (42×3)
   modified (78 from run 6 + 48 from run 7's 16 groups); `git add
   reports/` the whole directory, then proceed with run 6's steps 5
   (fill the per-file table, commit, update `reports/CLAUDE.md`'s
   `[B13.2]` entry -- note the `legend_v13_v15` delta in that entry
   too, since it is a real, if incidental, effect of this regeneration)
   and send the manager the completion handback.

## Handback

Sent to the manager alongside this report's commit: code/tests/docs
complete and green on everything that does not need the real store;
the `reports/` regeneration is the one OWED item. Run 7 is launched
DETACHED with the classifier fix above; log path and exact resume
steps (both run 6's and run 7's) are in this report. Not committing
the regenerated `reports/` files themselves -- that, and the diff
proof, is the next agent's job once `DONE rc=0` lands.
