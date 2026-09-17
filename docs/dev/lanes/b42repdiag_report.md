# lane b42repdiag — reporter did-not-compile diagnostic truncation (KB-18)

Brief: [B42] follow-up (v) from the 2026-09-17 reset (plan.md's [B42] row,
OWED FOLLOW-UPS item (v)) — the capability@0.1 first-sample ledger
(`docs/dev/ledgers/2026-09-17-capability-0.1-first-a770139e.md` 2 Finding F)
found the reporter truncates a did-not-compile diagnostic to its first
line, so `wild-waf-crs-942500-comment-obfuscation`'s real gcc diagnostic
(a genuine pcrec DFA-emitter bug) had to be read out of the raw JSONL
record by hand.

## What is DONE and COMMITTED (branch `lane/b42repdiag`, commit `12b2d00`)

1. **KB-18** appended to `docs/dev/known_issues.md` (next free number after
   KB-17): the truncation site (`_diagnostic_first_line`,
   `pcrecbench/report.py`, since [B12] R10), the finding that produced it,
   and the fix.
2. **The fix**: `_diagnostic_first_line` REPLACED by `_diagnostic_full`
   (`pcrecbench/report.py`) — a did-not-compile row's `diagnostic` is
   carried VERBATIM and IN FULL, bounded only by `record.FREE_TEXT_MAX`
   (1,048,576 chars, schema v1.5's hygiene bound, [B30]) as a defensive
   ceiling (the schema itself caps `diagnostic` at 8192 chars today, well
   under it). Both call sites (the markdown `not ranked: ... did-not-
   compile (<diagnostic>)` bullet, the TSV `did_not_compile` row) are
   one-physical-line contexts, so an embedded newline/tab/backslash is
   rendered VISIBLY (backslash-escaped, backslash escaped FIRST so the
   mapping is losslessly reversible) rather than executed — nothing is
   dropped. `pcrecbench/__main__.py`'s own, separate `_diagnostic_first_line`
   (KB-10's `quick --vs` refused-arm one-liner, genuinely one-line-by-design)
   is UNCHANGED — different function, different call site, not touched.
3. **`REPORTER_VERSION` bumps `v16 (2026-09-08)` → `v17 (2026-09-17)`**,
   with a new dated module-docstring section in `report.py` (matching the
   convention of every prior version bump) and the corresponding history
   line added to `pcrecbench/CLAUDE.md`... **CORRECTION, see OWED (4)
   below: `pcrecbench/CLAUDE.md`'s own reporter-history section was NOT
   updated by this lane** — only `report.py`'s module docstring and
   `known_issues.md` carry the KB-18 account. `pcrecbench/CLAUDE.md`'s
   `## The reporter, [B13.2] ...` section is the place a future reader
   would look for the v17 entry; it is stale until that file gets a KB-18
   paragraph appended the same way v10/v11/v12/... each did.
4. **`pcrecbench/tests/test_report.py`**: `test_reporter_version_pin`
   re-pinned to v17 (history note extended); new test
   `test_diagnostic_full_kb18` (unit-level: multi-line diagnostic escapes
   visibly and survives whole; single-line unchanged; `None`/empty render
   `(no diagnostic)`; a literal two-character `\n` in the SOURCE renders
   distinguishably from a real embedded newline, the reversibility
   control; end-to-end: both `render_markdown` and `render_tsv` carry
   every line of a synthetic multi-line diagnostic with the old
   `[truncated, diagnostic continues]` marker asserted ABSENT).
   Registered in `TESTS`.

**Manual proof the fix does what the ledger asked for**, run interactively
before the batch regen (not committed, reproduced from any checkout):

    python3 -m pcrecbench report --store store --subbench capability \
        --version 0.1 --machine budu-ryzen1600 \
        --since 2026-09-17T00:00:00Z --until 2026-09-17T08:00:00Z \
        --testee libpcre2_10.46_interp-caps-simdna \
        --testee libpcre2_10.46_jit-caps-simdna \
        --testee libpcre2_10.46_dfa-nocaps-simdna \
        --testee pcrec_a770139e_auto-caps-simdna \
        --testee pcrec_a770139e_auto-nocaps-simdna \
        --testee pcrec_a770139e_vm-caps-simdna \
        --testee pcrec_a770139e_vm-in-caps-simdna --format tsv

against the committed `reports/2026-09-17-capability-0.1-budu-ryzen1600-
first-a770139e.tsv`: the ONLY body deltas are the `wild-waf-crs-942500-
comment-obfuscation` did-not-compile rows on `pcrec_a770139e_auto-caps-
simdna` and `pcrec_a770139e_auto-nocaps-simdna`, each `plain` /
`large-subject-throughput` and `plain` / `short-subject-search` (4 rows
total) — the old `"the artifact did not build: [truncated, diagnostic
continues]"` becomes the FULL gcc transcript (the two `missing terminating
" character` errors on the pattern's own `/*!*/` bytes, the two cascading
`rx_forward_next_state`/`rx_reverse_next_state`/`rx_anchored_next_state`
undeclared-identifier errors — exactly Finding F's account), escaped to
one line with visible `\n`s. Every other line of that 8,217-line TSV is
untouched but for the `reporter: v16` → `v17` header stamp.

## What is OWED — two background jobs, NEITHER has its completion marker yet

Per the manager's explicit check-the-marker-now instruction
(2026-09-17, this session): both markers were checked and are ABSENT as
of this report. **Do not trust a "still running" claim from any later
message without re-checking these same two commands first.**

**(1) `make check-report`'s core, run early for a REAL_STORE-scale signal
before committing the regen wave.**

    grep -n '^DONE rc=' /tmp/claude-1001/-home-duxevents-pcrec-bench/18ca7e26-4ced-4281-a92d-0330c831ba9e/scratchpad/test_report_run1.log

Absent as of this writing. Launched via
`setsid bash -c "gnutimeout 1800 python3 -m pcrecbench.tests.test_report > '<log>' 2>&1; echo DONE rc=\$? >> '<log>'" </dev/null & disown`
(PID tree 1562365/1562366/1562367 at launch; NOT harness-tracked — no
notification will ever arrive for it, check the marker by name). At the
last check (this session) it had run 694 s at 3.53 GB RSS, which is
squarely inside the box's known profile for this suite against the real
store (KB-16: ~745–766 s / ~3.6 GB peak at the store's current size) — it
is very likely to finish within a couple more minutes of whenever this is
next checked, not stalled. **On completion**: read the log's tail for the
pass/fail summary (the suite prints one line per failing `_check` if any,
nothing if clean) and fold the pass/fail count into the handback. This
run's OWN result does not block committing the regen wave (it is a
pre-check against the small, already-updated `TESTS` list) but a FAILURE
in it — most likely in `test_diagnostic_full_kb18` or
`test_reporter_version_pin` — must be fixed before that commit lands.

**(2) The full report + sidecar regeneration — NOT YET RUN TO COMPLETION,
and reports/ is in a MIXED, UNCOMMITTED state on disk right now.**

    grep -n '^DONE rc=' /tmp/claude-1001/-home-duxevents-pcrec-bench/18ca7e26-4ced-4281-a92d-0330c831ba9e/scratchpad/regen_reports_run1.log

Absent as of this writing. Driver script (one-off, NOT committed, per the
mandate — session-temporary tooling):
`/tmp/claude-1001/-home-duxevents-pcrec-bench/18ca7e26-4ced-4281-a92d-0330c831ba9e/scratchpad/regen_reports.py`
(read it before trusting this account of what it does). It walks every
committed `reports/*.tsv` (43 groups), parses each one's OWN header line
(`pcrecbench.interpret.split_header`/`HEADER_KEYS`, the same grammar the
interpreter uses) to recover its exact `--subbench`/`--version`/
`--machine`/`--since`/`--until`/`--testee`(repeated)/`--where`/
`--include-synthetic`/`--grain`/`--include-unmeasured`/`--include-scratch`/
`--all-records`/`--include-provenance` flags, then re-runs the REAL CLI
three ways per group (`--format tsv`, `--format md`, the same filters plus
`--grain subject --format md`) and overwrites the `.tsv`/`.md`/
`.subject-grain.md` triad in place, classifying each diff as
`unchanged` / `version-line-only` / `diagnostic-or-version` / `OTHER`.
This is the KB-16-fixed CLI path (per-query index prefilter,
`report.py main()`), not a whole-store `load_all` — chosen specifically
so this regen would NOT need the store-loading memory/time profile KB-16
named, and it was launched detached anyway out of caution (BOILERPLATE's
blanket rule for anything touching store rendering).

Launched via
`setsid bash -c "cd <worktree> && gnutimeout 1800 python3 <script> > '<log>' 2>&1; echo DONE rc=\$? >> '<log>'" </dev/null & disown`
(PID tree 1564945/1564946/1564947 at launch) — **also not harness-tracked;
no notification will ever arrive for this one either.**

**Progress at last check (this session): 6 of 43 groups written** (`git
status --short | wc -l` = 18 = 6 groups × 3 files; verified by file
mtimes earlier in the run, roughly one group per 20–90 s depending on the
group's own record sizes — the `email-specimen`/`loglines` early groups
are small and fast, `syntax@0.1`/`altwide@0.2`/`bounded@0.3` groups later
in alphabetical order carry far larger `.subject-grain.md` files
historically (10+ MB) and will each cost noticeably more).

**REAL RISK, stated plainly: 43 groups at the observed pace projects to
roughly 40–65 minutes total, which is LIKELY TO EXCEED the script's own
`gnutimeout 1800` (30 min) cap.** If the marker line reads `DONE rc=124`
(or the log simply ends mid-group with no trailing summary line), the
run was cut off partway — check how many `OK <stem>: ...` lines are in
the log, cross-reference against `git status --short` in the worktree
(each `OK` line's group should have exactly 3 modified files), and either
(a) re-run the SAME script with a larger cap (`gnutimeout 5400 python3
<script>`) — it is safe to re-run over files it already regenerated: a
v17 report re-queried against itself re-renders byte-identical, so
already-done groups just get overwritten with the same bytes — or
(b) edit its `stems` loop to skip the ones already done (cheaper, not
necessary for correctness). **Do not assume `rc=0` means all 43 succeeded
without reading the log's own last two lines** — the script's exit code
is `1` if EITHER any group hit an `OTHER` (unexplained) classification OR
any group failed outright, `0` only if every group is `unchanged`,
`version-line-only` or `diagnostic-or-version`.

**Once regen_reports.py's marker reads `DONE rc=0` with a clean summary
line (`N group(s), 0 with an unexplained delta, 0 failed`), the remaining
steps — NONE done yet — are:**

  a. `git status --short -- reports/` in the worktree should show exactly
     129 modified files (43 groups × 3) and NOTHING added/removed (a
     changed file COUNT is itself a check the script's own per-group
     parsing didn't skip or duplicate a group).
  b. Confirm by hand that the ONLY non-version-line deltas anywhere in
     `reports/*.tsv`/`*.md`/`*.subject-grain.md` are the four
     `wild-waf-crs-942500-comment-obfuscation` did-not-compile rows on the
     TWO `2026-09-17-capability-0.1-budu-ryzen1600-first-a770139e.*`
     files (`.tsv` and `.md`; NOT `.subject-grain.md` — that pattern's
     regime rows are `large-subject-throughput`/`short-subject-search`,
     both SET-grain-only cells per the ledger, so the subject-grain
     sibling for this pattern may carry no did-not-compile row change at
     all — VERIFY this rather than assuming it) — e.g.
     `git diff --stat -- reports/*.tsv reports/*.md
     reports/*.subject-grain.md | awk '$3+$4 > 2'` and eyeball the
     handful of files it lists beyond the universal one-line version
     stamp change.
  c. Run `python3 scripts/regen_sidecars.py` from the repo root (fast, 4
     sidecars) and confirm its own exit code is 0 (it prints `OK`/`FAIL`
     per sidecar and a summary line) — this is REQUIRED because
     `make check-interpret` section 3 requires byte equality between a
     committed sidecar and its own re-render, and every sidecar's report
     path may now carry a `reporter: v17` line the sidecar's stamp does
     not yet reflect being fresh against.
  d. Add a KB-18 wave paragraph to `reports/CLAUDE.md`, immediately after
     the file's opening `.interpretation.md sidecars` section and BEFORE
     the existing `**[B13.2] (2026-09-08...` paragraph (reverse-
     chronological order, confirmed: this file has exactly one `##`
     header and every wave is a bold paragraph under it) — cite the real
     diffstat from (b)/(c) once known, following the v10/v11/v12/v16
     paragraphs' own template (what changed, why, proof of
     mechanicalness).
  e. ONE commit: every regenerated `reports/*.{tsv,md,subject-grain.md}`
     + the 4 regenerated `.interpretation.md` sidecars + the
     `reports/CLAUDE.md` wave paragraph. (The code fix is ALREADY
     committed separately, commit `12b2d00` — see the top of this
     report; that is fine, lanes commit incrementally and the manager
     folds them into one merge.)
  f. `pcrecbench/CLAUDE.md`'s reporter-history section (see the
     correction under item 3 above) needs its own KB-18 paragraph added —
     this lane did not do it; flagged here so it is not silently
     forgotten a second time.
  g. Run `make check-report` FOR REAL (not just the early `test_report`
     pre-check) and `make check-interpret`, and quote both targets' exact
     printed counts in the final handback — neither has been run to
     completion by this lane; `make check-report`'s own fixture-based run
     is fast (does not touch the live store) and was not yet attempted
     because the regen above touches `reports/` files `make check-report`
     does not read, but running the real `make` target is still the
     charter's own acceptance bar and must be quoted, not inferred from
     the standalone `test_report.py` run.

## Numbers this handback does NOT have (all OWED, per above)

- `make check-report` exact pass count.
- `make check-interpret` exact pass count.
- The full diffstat proving the regen is mechanical across all 43 groups
  (only the ONE group manually verified above).
- Whether `regen_reports.py` finished inside its 1800 s cap or needs a
  re-run/resume.

## Files touched by this lane so far

- `pcrecbench/report.py` — `_diagnostic_full` (replaces
  `_diagnostic_first_line`), `REPORTER_VERSION` v17, new module-docstring
  section, `record.FREE_TEXT_MAX` import.
- `pcrecbench/tests/test_report.py` — `test_diagnostic_full_kb18`,
  `test_reporter_version_pin` updated.
- `docs/dev/known_issues.md` — KB-18.
- `docs/dev/lanes/b42repdiag_report.md` — this file.
- NOT YET touched, OWED: `reports/*` (regen in flight on disk,
  uncommitted), `reports/*.interpretation.md` (not yet regenerated),
  `reports/CLAUDE.md`, `pcrecbench/CLAUDE.md`.

## Marker commands for whoever picks this up (copy-paste)

    grep -n '^DONE rc=' /tmp/claude-1001/-home-duxevents-pcrec-bench/18ca7e26-4ced-4281-a92d-0330c831ba9e/scratchpad/test_report_run1.log
    grep -n '^DONE rc=' /tmp/claude-1001/-home-duxevents-pcrec-bench/18ca7e26-4ced-4281-a92d-0330c831ba9e/scratchpad/regen_reports_run1.log
    cd /home/duxevents/pcrec-bench/worktrees/b42repdiag && git status --short -- reports/ | wc -l
