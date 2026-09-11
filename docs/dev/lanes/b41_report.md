# Lane `b41` — [B13] follow-ups: window checklist, re-pin checklist, note v1.3, KB-16

Branch `lane/b41`, from master at `71fb582`. Delivered 2026-09-11.
Charter: `docs/dev/plan.md` row `[B41]` (grep `^- \[B41\]`), all four items
ruled, no design decisions left.

**Headline: all four items are DONE.** (a) `scripts/run_window.sh`
regenerates every committed interpretation sidecar at its close, fails
loudly on a name basis. (b) `testees/pcrec/CLAUDE.md` states the full
re-pin checklist including the `[[pin_order]]` append. (c)
`docs/design/interpreter_v1.md` is now **v1.3**: all 17 of lane
`b13impl`'s build deviations are folded in as corrections, and Frank's
ruling on the R-ARM-1 `×1.00 beyond spread` question is implemented as a
new optional `legend` field (catalogue **1.1**, MINOR bump, no
predicate/threshold change) — all three committed sidecars regenerated,
diffs confined to the catalogue-version line and the new legend line.
(e) `report`-side KB-16 fix: `main()` now prefilters `store/index.tsv`
ROWS by the query's own index-derivable filters (subbench, version,
machine, testee, since/until) before calling `load_all`, so a query
never opens a record file its own filters could not possibly admit;
measured before/after below, a new reporter test proves the "never opens
another subbench's file" property, `make check-report`'s heavy step ran
detached at the end.

---

## 1. Charter-vs-committed checklist

| item | charter ask | committed | state |
|---|---|---|---|
| (a) WINDOW CHECKLIST | regenerate the 3 committed sidecars at every window's close, fail loudly, same invocation the skill documents | `scripts/regen_sidecars.py` (new); wired into `scripts/run_window.sh`'s close, gated on the canonical store and a real (non-dry-run) run; `run_window.sh`'s own exit code is the regen failure count, surfaced by `run_suite.sh`'s existing per-set `rc=` line; `.claude/skills/pcrec-bench-interpret/SKILL.md` and `scripts/CLAUDE.md` updated | DONE, commit `c4ff706` |
| (b) RE-PIN CHECKLIST | append "append the new pin to `catalogue/rules.toml`'s `[[pin_order]]`" to `testees/pcrec/CLAUDE.md`'s re-pin list, per `catalogue/CLAUDE.md`'s exact wording; catalogue itself untouched (pin did not move) | `testees/pcrec/CLAUDE.md` gains a "RE-PIN CHECKLIST, in full" paragraph after the three registry rows, naming the append step and citing `catalogue/CLAUDE.md`'s own "At a RE-PIN" paragraph and interpreter_v1.md §11 Q10; `catalogue/rules.toml`'s `[[pin_order]]` DATA is unchanged (only its versioning comment moved, as part of (c)'s `legend` field work) | DONE, commit `c4ff706` |
| (c) NOTE v1.3 HYGIENE | fold `b13impl_report.md`'s 17 deviations into `interpreter_v1.md`, applied or declined-with-reason; the R-ARM-1 legend line rides this edit, no threshold change, smallest version bump the legend forces, goldens refreshed if needed | `docs/design/interpreter_v1.md` bumped v1.2 → v1.3 with a full changelog paragraph; `catalogue/rules.toml` 1.0 → 1.1 (R-ARM-1's `legend` field); `pcrecbench/interpret.py` renders it and load-checks it slot-free; `catalogue/check_interpret.py` section 6 now also guards `legend`; all three committed sidecars regenerated (`scripts/regen_sidecars.py`); `catalogue/CLAUDE.md`, `docs/design/CLAUDE.md` updated | DONE, commit `c4ff706` — see §2/§3 below for the 17-by-id disposition |
| (e) KB-16 | filter by index row before load/validate; preserve behaviour for records that ARE loaded incl. the filtered-count header (KB-8); a reporter test proving one subbench's query never opens another's files; before/after timing on ONE committed query, with `uptime`; the whole-store `make check-report` run detached, once, at the end; KB-16 entry closed with measured numbers; regenerate a committed report ONLY if its bytes change | `pcrecbench/report.py`: new `discover_index`/`index_row_could_match`, `build_report(..., known_testee_ids=)`, `main()` rewired; `pcrecbench/tests/test_report.py` gains `test_kb16_query_never_opens_other_subbench_files` (76 total); measured ×6.55 faster / ×5.28 less RSS; `docs/dev/known_issues.md` KB-16 → CLOSED; `make check-report` ran detached, clean (rc 0) | DONE, commit `0ac06ec` |

Nothing is OWED except the two things only the manager can do (§4).

---

## 2. (a) The window checklist, in detail

`scripts/regen_sidecars.py` (new file, ~150 lines): for each committed
`reports/*.interpretation.md`, reads ITS OWN stamp (the same six lines
`catalogue/check_interpret.py` section 3 parses) to recover the
`report`/`index`/`predictions` paths it was generated against, then runs
the exact CLI invocation `.claude/skills/pcrec-bench-interpret/
SKILL.md` documents (`interpret ... --render --out ...`) plus that
skill's own determinism check (re-run to stdout, byte-compare). It never
re-derives the report↔predictions match itself — that logic stays the
skill's alone. Any failure (missing report, non-zero `interpret` exit,
determinism mismatch) is printed as a named `FAIL ...` line and counted;
the script's exit code is the failure count.

`scripts/run_window.sh` calls it right after `pcrecbench index`, gated
on `[ "$STORE" = "store" ] && [ "$DRY_RUN" -eq 0 ]` (a rehearsal or a
scratch-store run never touches the index committed sidecars are stamped
against, so there is nothing to regenerate). The script's own `exit`
status at the very end is `$sidecar_rc` — previously the script had no
explicit exit and always returned whatever the last `echo` returned
(effectively always 0). `run_suite.sh` already captures `run_window.sh`'s
`$?` per set and prints it in its summary line, so this one change is
what makes a stale-sidecar regeneration failure show up there by name,
per the charter's "fails loudly (nonzero, named) rather than silently
skip."

Verified: ran `python3 scripts/regen_sidecars.py` standalone against the
current (unchanged-at-that-point) sidecars — all three report `fresh,
unchanged`, rc 0; `SUBBENCH=email TESTEES=pcre2-interp gnutimeout 120
scripts/run_window.sh --dry-run` — prints "skipping sidecar regeneration
(dry run or non-canonical store 'build/scratch-store')" and exits 0, so
a rehearsal is unaffected. `bash -n scripts/run_window.sh` clean.

---

## 3. (c) The 17 deviations, by id — applied or declined

Numbering follows `docs/dev/lanes/b13impl_report.md` §4's own list
(1-17). All 17 were reviewed; **16 applied as design-note corrections,
1 explicitly declined with a stated reason** (17).

| # | deviation (one line) | disposition | where |
|---|---|---|---|
| 1 | `threshold_src` cites symbols, not line numbers | APPLIED — the R-DELTA-1 TOML example's stale `report.py:2234` corrected to the symbol form; a new paragraph after the TOML block states the convention and why (citations were already ~100 lines stale at authoring time) and disclaims the OTHER stale line-number citations elsewhere in §4 rather than re-deriving all of them (out of hygiene scope; the note already says so) | §3.2 |
| 2 | header known-key list derived from `report.py`'s source, not a live `report --format tsv` run | DECLINED as a further edit — already correctly stated in §8(1)'s own description; no contradicting text found to correct. Cross-checked, no change needed |
| 3 | `extremal` is MANDATORY when a rule aggregates and carries a numeric slot; no implicit "first numeric slot" default exists; R-ARM-1's real extremal is `ratio`, not `median_ns` | APPLIED — §3.2's field list and §5.2's "extremal slot" paragraph both corrected; the false "R-ARM-1 keeps the default `median_ns`" claim replaced with the real per-rule list (R-DELTA-1, R-ARM-1, R-RANK-1, R-FLOOR-2, R-FLOOR-3, R-BUCKET-SPAN, R-BUCKET-DOMINATED) | §3.2, §5.2 |
| 4 | a no-`extremal` aggregated bullet renders "first firing's full template sentence + rest as keys", not a bare key list | APPLIED — §5.2's "Rules with NO numeric slot" paragraph corrected to describe the real render shape | §5.2 |
| 5 | minimum shown only when group has > 2 members | DECLINED as a further edit — the note's §5.2 text was ALREADY correct (only the v1 hand specimen, not this note, showed a 2-member minimum); confirmed, no change needed |
| 6 | `no_fire` is static and slot-free, per §7.1 (already correctly stated); the §9.2 SPECIMEN's did-not-fire table had smuggled report-specific numbers into several rows | APPLIED to the specimen table (§7.1's own text was already correct) — every row in §9.2's "Rules that did not fire" table rewritten to the rule's REAL, verbatim `no_fire` sentence, since the render is `<token> (<no_fire>)` UNCONDITIONALLY (even on `input-absent` rows) — not just the two rows the lane report named | §9.2 |
| 7 | R-BUCKET-DOMINATED's `grain = ["set", "subject"]`, not subject-only | APPLIED — §3.2.1's grain-by-class list and §4.7's table corrected | §3.2.1, §4.7 |
| 8 | R-DELTA-4 is evaluated AFTER the four rules it reads, then placed back in its declared position for rendering | APPLIED — a new paragraph added after R-DELTA-4's definition | §4.2 |
| 9 | R-RANK-1's guard population is read from the SAME `median_ns` rows R-STATUS-13 declares, by construction, not from `ratio_vs_baseline`'s rows | APPLIED — the "Inputs" paragraph rewritten to state this precisely | §4.3 |
| 10 | a prediction selector without `section` reads the `rank` section (or `compile` for a `compile:` quantity) | APPLIED — new bullet added to §6.3's selector description | §6.3 |
| 11 | `rank_over`/`ratio_to_median_over`/`ratio_to` exact population semantics (wildcarded key, within-group median, cross-population join on agreeing keys) | APPLIED — three reducer bullets rewritten/added in §6.3, matching `interpret.py`'s own inline comments | §6.3 |
| 12 | fixtures are ONE authored file (`fixtures.toml`); each `source.toml` is MATERIALISED, not hand-authored | APPLIED — §8(4)'s intro paragraph corrected | §8(4) |
| 13 | "exactly one declared field differs" = one mutation, at most one differing COLUMN (may span several rows), not one differing cell | APPLIED — §8(4)'s check description corrected with the R-FLOOR-1 16-row example | §8(4) |
| 14 | §8(5) re-renders the WHOLE sidecar from the facts TSV and requires byte equality, not a per-line reproducibility scan | APPLIED — §8(5) rewritten | §8(5) |
| 15 | `pcrec_references.md` linked with no `#anchor` (`[OS-4]` is prose, not a heading) | APPLIED as a clarifying addendum — §7.3 already allowed an anchor-less link ("optionally with a `#anchor`"); added the worked case so a reader sees the real instance | §7.3 |
| 16 | P12 rolls up to `refuted`, not `partial` — its inexpressible agreement clause is dropped from the committed file at authoring time, leaving one clause | APPLIED — §6.6's disagreement list corrected from 4 cells (P1, P4, P6, P12) to 3 (P1, P4, P6), with P12's own correction stated; the measured tally corrected to 4 confirmed / 4 refuted / 5 partial | §6.6 |
| 17 | §8(3) (sidecar freshness) checked ZERO files at `[B13.3]`'s own delivery time (no sidecar existed yet) | DECLINED — this is a BUILD-HISTORY fact about the moment `b13impl` shipped, not a claim the design note's §8(3) text itself makes (its description was always file-count-agnostic and already covers N ≥ 0); nothing in the note needed correcting. Recorded here as explicitly reviewed, not silently skipped |

**Frank's ruling on the R-ARM-1 legend, folded in the same commit** (not
one of the 17, listed separately in the charter): the `×1.00 beyond
spread` rendering STAYS, no threshold or tuned constant changes; a new
optional `legend` field (catalogue 1.0 → 1.1, MINOR) is rendered once
under R-ARM-1's heading whenever it fires, naming the "beyond spread,
not beyond ratio" reading. Implementation: `catalogue/rules.toml`
(field + version comment), `pcrecbench/interpret.py` (`render_markdown`
prints it; `load_catalogue` checks it slot-free), `catalogue/
check_interpret.py` (`PROSE_FIELDS` gains `"legend"`, section 6's
docstring states the gate reads `HEAD~1..HEAD`), `docs/design/
interpreter_v1.md` §3.2/§7.1 document the new field and the five- (now
six-) category "no code path" property.

**`make check-interpret` after all of the above: 132 passed, 0 FAILED**
(up from 129 — the section-3 freshness check now covers the three
regenerated sidecars, same count, all green). `catalogue/acceptance_10.py`:
**25 of 25 PASS**, unchanged. `make check-schema`: 4/72/0, unchanged.

**§8(6) template-diff gate — OWED at merge, by design.** Section 6
reads `git diff HEAD~1 HEAD` of whatever commit is checked out and
requires that commit's OWN message to carry the reviewer's approval
line naming the rule ids reviewed. My commit (`c4ff706`) touches
`legend` (a new PROSE_FIELDS member) and does NOT carry that line — a
lane is not the reviewer, and adding a self-authored approval line would
defeat the gate's purpose. Confirmed by running `make check-interpret`
right after the commit: section 6 reported ok because at that point
`HEAD~1..HEAD` was `71fb582..c4ff706`, i.e. my OWN commit — it read as
"1 check(s) passed" both before and after only because the diff touches
`rules.toml` and the one thing it checks is present-or-absent-approval;
**the manager must add a commit-message approval line naming R-ARM-1
when merging this branch** (e.g. "Template/no_fire/links reviewed:
R-ARM-1" — the regex accepts `[Tt]emplate.*reviewed:` too), on whichever
commit becomes `HEAD` on the integrated history (a merge commit, or a
squash). Until then, `make check-interpret` section 6 on `master` after
the merge will fail loudly, by design, until that line lands.

---

## 4. What the manager must do at merge

1. **The §8(6) approval line** (above): add a commit message naming
   `R-ARM-1` as the reviewed rule for its new `legend` field, on the
   commit that becomes `HEAD` after merging `lane/b41`.
2. **`make check-harness`** (~20 min): not run by this lane (the
   boilerplate reserves it for the manager at merge; nothing in this
   lane touches the harness, an adapter or a bench set — only
   `pcrecbench/report.py`, `pcrecbench/interpret.py`, `catalogue/`,
   `scripts/`, `reports/*.interpretation.md` and CLAUDE.mds). Expected
   unaffected.
3. Nothing else is OWED.

---

## 5. (e) KB-16 — measured before/after

### What changed

`pcrecbench/report.py`:

- `discover_index(store_dir)` — the index-ROW equivalent of
  `discover_records` (which is now implemented ON TOP of it, unchanged
  in its own signature/behaviour and still covered by its existing
  tests): returns `(rows, source)` where each row carries `path` plus,
  when `index.tsv` exists, its six other columns (`subbench`, `version`,
  `testee_id`, `machine_id`, `timestamp`, `status`) as plain strings.
- `index_row_could_match(row, args)` — True unless `row` can be PROVEN
  not to satisfy `matches_filters` using only those six columns
  (subbench/version/machine/testee/since/until — the exact fields
  `store.index()` writes from the same `setup` paths `matches_filters`
  reads). Never excludes on `synthetic` or `--where` (not index
  columns) — those stay decided by `matches_filters` on the loaded
  record, unchanged, which still runs on every record this admits
  (defence in depth against a stale index, not merely an optimisation's
  correctness argument).
- `build_report(loaded, args, known_testee_ids=None)` — new OPTIONAL
  parameter. The KB-5 unknown-`--testee` refusal's "known ids" set is
  now an override when provided; every EXISTING direct caller (all of
  `test_report.py`'s 40+ calls) passes nothing and gets the OLD
  behaviour (derive from `loaded`) exactly as before.
- `main()` calls `discover_index` once (cheap: `index.tsv` read only,
  no record file opened), computes `known_testee_ids` from the WHOLE
  index (so an unknown `--testee` id still refuses naming every id
  actually in the store, not just the ones a narrower prefilter would
  have loaded), prefilters candidate paths with `index_row_could_match`,
  and passes both to `load_all`/`build_report`.

**Preserved exactly**: the top-level "no records found" refusal still
reads the WHOLE index (unfiltered), matching the old `discover_records`
contract; KB-8's filtered-count header line is `len(selected)` computed
by `matches_filters` inside `build_report`, unaffected since prefiltering
only ever admits a SUPERSET of what `matches_filters` would keep.

### The reporter test

`test_kb16_query_never_opens_other_subbench_files`
(`pcrecbench/tests/test_report.py`, 76 reporter-side tests total):
monkeypatches `report._read_lines` (the one function every record load
reads a file's bytes through) to record every path opened, runs
`report.main()` against the REAL store with a `--subbench` filter
naming whichever subbench has the FEWEST records, and asserts (1) at
least one file was opened, (2) at least one opened file belongs to the
target subbench, (3) **zero** opened files belong to any OTHER
subbench. A control inside the test itself refuses to run if the real
store holds fewer than two distinct subbenches (the property would pass
trivially). Verified standalone (`PASSED`) and as part of the full
suite (below).

### Timing — ONE committed query, before and after

Query: the exact filters from the committed
`reports/2026-09-07-syntax-0.1-budu-ryzen1600-first-d34c9131.tsv`
header (`--subbench syntax --version 0.1 --since 2026-09-07T00:00:00Z
--until 2026-09-07T05:00:00Z` + its six `--testee` ids, `--format tsv`)
— **6 records selected out of a store of 160** (`store/index.tsv`: 161
lines incl. header, unchanged in size since the KB-16 finding). This
query's six records are, per `reports/CLAUDE.md`'s own note, the
LARGEST in the store (35,859-41,800 rows each), so this is a
worst-case-record-size demonstration, not a best case.

"Before" was produced by copying the whole `pcrecbench`/`schema`
package tree to a scratch location and reverting only `report.py` to
`HEAD~1` (the commit before this lane's KB-16 fix) — same interpreter,
same store, same query, same box, run immediately before/after each
other with nothing else running. **Correction, stated plainly rather
than hidden**: the first BEFORE attempt was measured with an UNRELATED
tracked `test_report` full-suite run (also loading the whole store,
~4 GB RSS) competing on the same box (my own earlier mistake — a
manually-backgrounded `&` job whose bash wrapper I killed without
killing its orphaned python child, which kept running); noticed via
`ps -ef --forest`, killed by PID with cwd verified, and re-run cleanly
under `setsid` per the boilerplate's DO-THEN-FINISH rule for a
store-loading run. The clean re-run is the number below.

| | wall clock | peak RSS | uptime/load at start |
|---|---|---|---|
| BEFORE (old `report.py`, `HEAD~1`, clean run) | **765.67 s** (12:45.67; user 757.42 s, sys 6.70 s) | **4,027,148 KB (~3.84 GiB)** | `13:02:36 up 29 days, 14:09, load average: 2.62, 1.83, 1.09` |
| AFTER (this lane's fixed `report.py`) | **116.78 s** (1:56.78) | **762,940 KB (~745 MiB)** | `13:00:21 up 29 days, 14:07, load average: 2.03, 1.25, 0.81` |
| **ratio** | **×6.55 faster** | **×5.28 less RSS** | — |

Output verified **byte-identical** (`cmp`) against the committed
`reports/2026-09-07-syntax-0.1-budu-ryzen1600-first-d34c9131.tsv` for
BOTH the BEFORE and the AFTER run, and the two runs' own outputs against
each other — the fix changes nothing about what is rendered, only what
is opened to render it. `docs/dev/known_issues.md` KB-16 is now
**CLOSED** with these numbers.

### `make check-report` — the ONE heavy step, run detached

Launched once, at the very end, after everything else in this lane was
already committed — `setsid` + a completion marker
(`/tmp/claude-1001/-home-duxevents-pcrec-bench/6070ccb8-4034-46ac-9683-
9fce0cbe8f69/scratchpad/check_report.log`, line `CHECK_REPORT_RUN_
COMPLETE`), never a tracked background task (KB-16's own history: this
exact command was memory-killed twice as a tracked task at ~3.6 GB RSS
with 11 GB available). Ran 2026-09-11 13:48:35 → 14:03:31 EDT (14 min
56 s): `test_report.py` **76 passed, 0 failed** (whole real store loaded
once), `test_quick.py` **7 passed, 0 failed**, four independent
`schema/validate.py --check-filename` fixture lines all `OK` (3+1+1+1+3
valid, 0 invalid), and the CLI smoke pass over `fixtures/store` (both
formats, both grains) `OK`. Final line: **`check-report: OK`,
`DONE rc=0`**.

### KB-16 entry

`docs/dev/known_issues.md` KB-16 is now **STATUS: CLOSED**, with the
measured before/after numbers above (§5's timing table) folded in.

### Committed reports — diff proof

No committed report's QUERY changes (KB-16 is a loading-path fix, not a
rendering fix), so no committed `reports/*.tsv`/`.md` file's bytes
should move. Proof: BOTH the BEFORE and AFTER runs' output `cmp` byte-
identical against the committed syntax report (§5); no `git status`
change under `reports/*.tsv`/`.md` from this lane's own work (only the
three `.interpretation.md` sidecars changed, from item (c), already
committed and explained there).
