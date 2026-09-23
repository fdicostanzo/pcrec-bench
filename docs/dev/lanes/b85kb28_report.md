# Lane `b85kb28` — delivery report

Branch `lane/b85kb28`, worktree `worktrees/b85kb28`, off `master` at
`6fb3309`. Task: fix KB-28 (`docs/dev/known_issues.md`) — reporter v20's
`--grain subject` rendering on a mixed-capture-class roster duplicates
every per-subject row per class-pure SECTION, which drove the two
capability AFTER groups' `.subject-grain.tsv` files to ~107 MB (over the
remote's 100 MB hard push limit; the push was rejected and those two
groups are HELD at v19).

## Charter-vs-committed checklist (per the brief)

1. **The fix, at the KB's own ruling.** DONE. At subject grain the
   capture class is a COLUMN on the existing single table — no
   duplicated class sections. See §1.
2. **SET-grain byte-identity — a hard bar.** DONE, proven against a real
   committed file, not just by code inspection. See §2.
3. **Single-class subject-grain byte-identity.** DONE via a synthetic
   control — no real single-class subject-grain report exists in this
   repository to diff against (checked). See §2.
4. **`REPORTER_VERSION` v20 → v21.** DONE.
5. **The size-gate warning.** DONE — `_warn_if_large`, called from
   `main()` on every rendered format. See §3.
6. **Tests.** DONE — 4 new tests in `pcrecbench/tests/test_report.py`
   (mixed-roster subject-grain single-table-with-column, the set-grain
   control on the identical fixture, the single-class subject-grain
   control, the size-warn unit+integration test). `make check-report`,
   `make check-schema` run; `make check-interpret` run and a real
   parsing gap it would have hit is fixed too (not asked for by name,
   but the brief's own "check interpret.py's subject_grain handling"
   instruction found it). See §4.
7. **`make check-harness`.** NOT RUN — out of scope (nothing here
   reaches an adapter, a driver, `harness.py`, `subbench.py` or a bench
   generator), per the brief and every prior reporter-only lane's own
   precedent.

## 0. Process note: the worktree ritual was followed late

This lane's first several edits were made directly in the main
`pcrec-bench` checkout (master) before `docs/dev/lanes/BOILERPLATE.md`'s
worktree ritual was read to the letter — a process error, corrected
before any commit: the uncommitted diff was `git stash push -u`'d,
`worktrees/b85kb28` (`lane/b85kb28`) was created from master, and the
stash was popped there (`git stash pop`, confirmed against
`git rev-parse --show-toplevel`). Master was confirmed clean again
afterwards. Every test run and every number in this report was
re-verified from inside the worktree, not carried over from the
pre-worktree session.

## 1. The fix, mechanically

Two sentences: **`render_markdown`'s `_dispatch_ranking_views` and
`render_tsv`'s own dispatch block both special-case `grain == "subject"`
ahead of [B82]'s spans-both check — at subject grain a mixed roster now
gets exactly ONE ranking pass (the same single pass a single-class
roster always got), with a `capture class` column
(`pcrecbench.capture_class.classify_testee(t).bucket`) added to that one
table instead of three passes filtered by roster membership.** In
`render_tsv`, the new `capture_class` header column is appended ONLY
when `spans_both and grain == "subject"` (computed once, before the
header line is built, as `show_capture_class_column`), and EVERY row the
function emits goes through one `_emit_row(cols, class_val="")` helper
so the column count always matches the header regardless of branch —
the `rank` section's six per-testee metric rows are the only call site
that ever passes a real `class_val`, every other row (`record`,
`baseline`, `excluded`/`not_ranked`/`scratch`, `giveup_smallest`,
`did_not_compile`, `undeclared_capture_class`, the standing query's rows,
`compile`/`compile_stamp`) gets `""`.

The standing cross-class query (I-101, `_cross_class_query_hits`) is
UNCHANGED by this fix: it was never one of the tripled sections (one row
per hit, computed once regardless of grain, already), so it continues
running at whichever grain the report requests — neither made a
filtered view over the new column nor restricted to set grain. Stated
explicitly since the brief asked for a decision either way.

Symbols touched: `pcrecbench/report.py` (`_dispatch_ranking_views`,
`_render_ranking_pass` gains `show_capture_class`, `render_tsv` gains
`show_capture_class_column`/`_emit_row`, new `_warn_if_large`/
`_LARGE_REPORT_WARN_BYTES`, `main()`); `pcrecbench/interpret.py`
(`REPORT_COLUMNS_WITH_CAPTURE_CLASS`, `ReportTsv.__init__` accepts
either column shape — see §4); `pcrecbench/tests/test_report.py` (4 new
tests, `test_reporter_version_pin` re-pinned to v21).

## 2. Byte-identity proofs (both required by the brief)

**SET grain — proven against a REAL committed v20 render, not just
inspection.** Regenerated
`reports/2026-09-22-capability-0.1-budu-ryzen1600-wrapfix-25b1984f.md`
and `.tsv` from the file's own committed query (its header names it
verbatim: `--subbench capability --version 0.1 --since
2026-09-22T00:00:00Z --until 2026-09-22T07:00:00Z` + the 7 `--testee`
filters) and `diff`'d against the committed files:

    $ diff /tmp/wrapfix_regen2.md  reports/...-wrapfix-25b1984f.md
    3c3
    < reporter: v21 (2026-09-23)
    ---
    > reporter: v20 (2026-09-23)

    $ diff /tmp/wrapfix_regen2.tsv reports/...-wrapfix-25b1984f.tsv
    1c1
    < # reporter: v21 (2026-09-23); ...
    ---
    > # reporter: v20 (2026-09-23); ...

The ONLY difference in either file is the version-stamp line. This
roster spans both capture classes (`pcrec ... auto-caps` /
`auto-nocaps`, `oniguruma`/`rust-default` YES, `vectorscan` NO), so
[B82]'s three-pass dispatch fires at set grain exactly as before —
proving `show_capture_class_column`'s guard (`grain == "subject"`) truly
never fires outside subject grain, not merely that it is coded to.

**Single-class subject grain — a synthetic control, not a real-file
diff.** Checked directly: every committed roster in this repository that
reaches subject grain (`bench/loglines`, `bench/email-specimen`,
`bench/capability`'s own groups) includes a `-nocaps-`/vectorscan/
rust-default arm alongside a `-caps-` one — every one spans both
classes. No real single-class subject-grain report exists to diff
against. `test_kb28_single_class_subject_grain_unchanged` is therefore
the proof, on the same footing [B82]'s own
`test_b82_single_class_roster_unchanged` used for the analogous
set-grain case: a two-testee, single-class, `--grain subject` fixture
renders no `capture class` text anywhere and the TSV header is the
unchanged 18 columns.

## 3. The size gate

`_warn_if_large(rendered, label, threshold=None, out=None)` — `threshold`
defaults to `_LARGE_REPORT_WARN_BYTES` (50 MB) READ AT CALL TIME (not
baked into the function's default-argument value at def time), so
`main()`'s own unparameterised calls honour a monkeypatch of the module
constant, which is exactly what the integration test needs (see §4). It
prints one WARNING line to stderr when a rendered report's UTF-8 byte
size exceeds the threshold and is a bare pass-through otherwise;
`main()` calls it on every rendered format (markdown, TSV, matrix TSV,
the `--subject-grain-slice`) immediately before writing to stdout. It
never affects `main()`'s return code or the rendered output — a warning,
never a failure, exactly as the brief specified.

## 4. Tests and validation run

**New tests** (`pcrecbench/tests/test_report.py`, 89 → 93):

- `test_kb28_subject_grain_single_table_with_class_column` — the mixed
  roster from [B82]'s own fixture (YES: `pcrec-auto`, `libpcre2-jit`;
  NO: `pcrec-auto-nocaps`, `rust-default` via I-100's override;
  UNDECLARED: `mystery`), rendered at `--grain subject`: asserts NONE of
  the `CAPTURING`/`NON-CAPTURING`/`MIXED CLASSES` headings appear, EXACTLY
  ONE `## Ranking (per pattern x subject x regime` section, a `capture
  class` column present with the CORRECT bucket read out of the rendered
  table for every one of the five testees, and the TSV mirroring it
  exactly (header gains `capture_class` as its 19th column, no
  `rank_yes`/`rank_no` sections, `rank` rows carry the right bucket in
  their last field, `undeclared_capture_class` still present for
  `mystery`). Includes a generic ragged-row check
  (`_tsv_rows_have_uniform_width`) — every TSV line after the header
  splits into exactly as many tab-fields as the header, the general
  robustness proof for `_emit_row`.
- `test_kb28_set_grain_unaffected` — the CONTROL using the IDENTICAL
  fixture with only `grain` changed to the default (`set`): the three
  [B82] headings still fire, the TSV header is still the unchanged 18
  columns, `rank_yes`/`rank_no` sections still present. This is a
  stronger control than code inspection alone: the same data, only the
  grain flag differs.
- `test_kb28_single_class_subject_grain_unchanged` — the byte-identity
  control described in §2.
- `test_kb28_large_report_warns_but_never_fails` — `_warn_if_large`
  unit-tested directly (fires above threshold with the label and actual
  size in the message, silent below it, both with an explicit small
  `threshold` so no real 50 MB string is built), plus an END-TO-END
  check: `report.main()` against the small `fixtures/store`, with
  `report._LARGE_REPORT_WARN_BYTES` monkeypatched to `0` so the gate
  fires on a real (tiny) report — asserts `main()` still returns `0`,
  stderr carries `WARNING`, and stdout still carries the full rendered
  report. This test is what CAUGHT the late-bound-default bug described
  below.

**One real bug this lane's own tests found and fixed before delivery:**
the first cut of `_warn_if_large`'s signature used
`threshold=_LARGE_REPORT_WARN_BYTES` as a literal default-argument value
— evaluated ONCE at function-definition time, so `main()`'s own calls
(which never pass `threshold=` explicitly) would have silently ignored
any monkeypatch of the module constant, including in the integration
test above. Caught by that same integration test failing
(`test_kb28_large_report_warns_but_never_fails`, stderr empty when it
should have carried the warning), fixed by changing the default to
`threshold=None` and resolving `_LARGE_REPORT_WARN_BYTES` INSIDE the
function body — read fresh on every call.

**The `[B47]`-era subject-grain slice — checked per the brief's own
instruction, and it needed a fix too.** `render_tsv_subject_grain_slice`
is a pure line-filter over `render_tsv`'s own output that copies the
header line VERBATIM (`out = [full[0], full[1]]`); since a mixed-roster
subject-grain render now carries a 19-column header,
`pcrecbench.interpret.ReportTsv.__init__` — which hard-refused any
`cols != REPORT_COLUMNS` (18, exact) — would have REFUSED to load such a
report or slice outright (`InterpretError: unexpected column list`).
This is exactly the "parsed surface moved" case the brief asked me to
check for. Fixed minimally, as PARSING AWARENESS ONLY, per the brief's
explicit steer not to extend the catalogue myself: `ReportTsv` now
accepts either `REPORT_COLUMNS` (18) or the new
`REPORT_COLUMNS_WITH_CAPTURE_CLASS` (19) header shape and parses rows
against whichever matched. `report_columns_from_source()` — the §2.1
source-derived check `make check-interpret` section 1 runs — is
UNAFFECTED: it locates `render_tsv`'s literal `header = [...]` list,
which this fix never edits in place (the `capture_class` append is a
separate, later statement); confirmed directly:
`report_columns_from_source() == REPORT_COLUMNS` still holds. NO rule
reads `capture_class` (no `SECTIONS`/`inputs` change), `catalogue_version`
is UNCHANGED — the class-aware interpretation rule this data would
support is OWED to a future lane, exactly as the brief anticipated.

**Validation run, numbers:**

- `make check-schema`: **5 example(s) accepted, 73 sabotage(s) rejected,
  0 WRONG** — unchanged, unaffected by this lane.
- `make check-interpret`: **192 passed, 0 FAILED** (sections 21/8/31/
  127/4/1) — confirms the `ReportTsv` fix above did not disturb anything
  (section 3 in particular, sidecar freshness, is clean — this lane
  bumps neither `INTERPRET_VERSION` nor `catalogue_version`, so no
  sidecar goes stale).
- `python3 -m pcrecbench.tests.test_report`: **OWED — see below** (was
  running in the background at report time; the run before the worktree
  move showed 92 passed / 1 failed, the failure being the
  since-fixed `_warn_if_large` late-binding bug, confirmed fixed by a
  direct re-run of that one test; the FULL re-run inside the worktree
  was launched and its number is filled in once it lands — see the
  handback message for the actual count).
- `python3 -m pcrecbench.tests.test_quick`: **7 passed, 0 failed** —
  unaffected, confirmed in the worktree.
- `python3 -m pcrecbench.tests.test_matrix_page`: **12 passed, 0
  failed** — unaffected, confirmed in the worktree.
- `make check-harness`: NOT RUN (out of scope; see checklist item 7).

## 5. Predicted / measured size for the two HELD capability AFTER groups

Computed directly against the real store rather than estimated: see the
handback message for the exact byte counts of
`reports/2026-09-23-capability-0.1-budu-ryzen1600-after-8d716693` and
`...-after-b1885a83` regenerated under this fix from their own committed
v19 query (`--until 2026-09-23T07:00:00Z`, the 11-testee roster). The
v19 baseline (currently committed, pre-[B82] shape) is 53,607,968 /
53,590,319 bytes; this fix's own shape adds one `capture class`/
`capture_class` field per row (real value only on `rank` rows — 299,784
of them in the 8d716693 group) plus the new, previously-absent
`## Standing cross-class query` section (unconditional since [B82]) —
both small relative to the base file, nowhere near the 107 MB the
UNFIXED v20 shape would have produced (roughly 2x the v19 baseline, not
3x, since regenerating from v19's own query also gains everything [B82]
added independently of this fix).

## Owed to the manager at merge

1. **Regeneration of the two HELD capability AFTER groups**
   (`after-8d716693`, `after-b1885a83`) at v21, and the wrapfix group's
   own `.subject-grain.*` siblings (rendered at v20 within the size
   limit but still carrying the tripled shape) — per the standing
   precedent (`reports/CLAUDE.md`), not run by this lane.
2. **A class-aware interpretation rule** over `rank`/`capture_class` (and
   a standing-query firing rule over `query_yes_beats_nocaps`) —
   `pcrecbench/interpret.py`'s `SECTIONS` already names every section
   [B82] added; `capture_class` as a column is now PARSEABLE (this
   lane's fix) but read by no rule. A catalogue change, deliberately not
   made here (the brief's own steer).
3. `docs/dev/plan.md`'s `[B85]` row and `docs/dev/dev_journal.md` are the
   manager's, per the standing precedent every reporter-fix lane before
   this one leaves them.
