# lane b42repfin — KB-18 regen wave finished, syntax delta diagnosed (not drift)

Resumed lane b42repdiag's committed state (branch `lane/b42repdiag`,
existing worktree, no new worktree created). Read
`docs/dev/lanes/b42repdiag_report.md` and the BOILERPLATE first, per
brief.

## Marker check (done first, per the boilerplate's on-every-reinvocation rule)

Both markers b42repdiag left OWED were checked before anything else:

    grep -n '^DONE rc=' .../test_report_run1.log     -> "81:DONE rc=0" (78 passed, 0 failed)
    grep -n '^DONE rc=' .../regen_reports_run1.log   -> "1:DONE rc=124" (timed out, as b42repdiag predicted)

Two MORE regen attempts existed beyond what b42repdiag's report knew
about (`regen_reports_run2.log`: `DONE rc=124`, another timeout;
`regen_reports_run3.log`: completed cleanly, `DONE rc=1` — the "1" is
the script's own "N with an unexplained delta" convention, not a
crash). run3's full log confirmed **43 group(s), 1 with an unexplained
delta, 0 failed** — the "unexplained" one being the syntax group this
lane was asked to diagnose. The regen had therefore already run to
completion before this lane started; the disk was in the mixed,
uncommitted state b42repdiag's report described.

## Task 1-2: the syntax delta — diagnosed, NOT store drift

The manager's brief's own first hypothesis (the [B12] precedent:
no `--until` clause, newest-measured-wins population drift) was
**tested and REFUTED**, not assumed:

- The group's committed query already carries an explicit
  `--since 2026-09-07T00:00:00Z --until 2026-09-07T05:00:00Z` pair (the
  2026-08-30 rule) — visible in the file's own header line.
- Both the committed (`git show HEAD:`) and the re-rendered header read
  `records: 6; excluded_invalid: 0; superseded: 0; newer_not_measured:
  0` — byte-identical population facts, not a shifted store (the store
  went 134 → 168 in absolute terms since 2026-09-07, but nothing in
  that growth falls inside this query's population).

With drift ruled out, I inspected every one of the 85 (tsv/md) / 2437
(subject-grain) differing lines directly (`git diff -U0` against the
last commit, not against the script's own progressive re-comparison,
which had been confounded by two earlier timed-out runs partially
rewriting disk before run3 completed). **Every single changed line is a
`did_not_compile` row (or its subject-grain expansion) on one of SEVEN
pattern ids** — `esc-ctrl` (`\c`), `esc-octal-o` (`\o`), `msc-c-uc`
(`\C`), `msc-r-uc` (`\R`), `msc-x-uc` (`\x`), `unp-p-lc`/`unp-p-uc`
(`\p{...}`) — plus the one-line version stamp. Nothing else moved: no
ranking row, no compile-cost number, no header field beyond the version
line and the record count (which is unchanged).

**Verdict: this is the SAME KB-18 escaping rule firing as designed, not
a bug and not drift.** `_diagnostic_full` doubles EVERY literal
backslash in a diagnostic unconditionally — this is necessary, not
incidental: the docstring's own rationale is that a diagnostic
containing the literal two characters `\n` must render distinguishably
from one with a real embedded newline, which requires escaping every
backslash, not only ones adjacent to an actual control character. These
seven bench/syntax patterns' pcrec diagnostics happen to quote a
literal backslash-letter regex escape sequence (e.g. "module 'misc' is
enabled but `\c` is not implemented yet") with **no embedded newline at
all** — ordinary single-line text — so under the new rule `\c` renders
as `\\c`. b42repdiag's own manual proof only checked ONE record
(capability's multi-line gcc transcript); the disposable
`regen_reports.py` classifier only recognised the OLD truncation-marker
pattern as an expected "diagnostic-or-version" class, so it correctly
flagged this as unrecognized rather than silently accepting it — the
script did its job by refusing to guess.

No code change was made to `_diagnostic_full` — the behavior is correct
per its own stated contract. I did not apply the `--until` fix (it
would have been the wrong medicine for a cause that turned out not to
be population drift).

## Task 3: b42repdiag's OWED list, completed

- **(a)** `git status --short -- reports/` showed exactly 129 modified
  files (43 × 3) before the sidecars; 133 after adding the 4 sidecars.
  Nothing added/removed.
- **(b)** Confirmed by hand (not assumed): the ONLY non-version-line
  deltas anywhere in `reports/*.tsv`/`*.md`/`*.subject-grain.md` are the
  capability group (5/5/157 lines) and — newly found by this lane, not
  anticipated by b42repdiag — the syntax group (85/85/2437 lines),
  diagnosed above. `git diff --stat` over every one of the other 41
  groups' 123 files confirms each is a single changed line pair (2 diff
  lines beyond the `---`/`+++` file headers).
- **(c)** `python3 scripts/regen_sidecars.py` run (niced, `gnutimeout
  300`, ~seconds total — it reads only `store/index.tsv`, never loads
  full records, so it does not conflict with the box's "no full
  suites" rule): **4 sidecars, 0 failures**, all determinism-checked.
  The capability sidecar's own finding line changed from the old
  truncation marker to the full gcc transcript — proof the fix reaches
  `pcrecbench interpret`'s fact-finding path, not only the reporter's
  render. The other three sidecars changed only their `report_sha256`/
  `reporter:` stamp lines (2 lines each).
- **(d)** `reports/CLAUDE.md`: KB-18 wave paragraph inserted immediately
  after the `.interpretation.md sidecars` section, before the existing
  `[B13.2]` (v16) paragraph — reverse-chronological, matching the
  file's own convention.
- **(e)** One commit (`f851d2e` on `lane/b42repdiag`): every regenerated
  `reports/*.{tsv,md,subject-grain.md}` (129 files) + the 4 regenerated
  `.interpretation.md` sidecars + the `reports/CLAUDE.md` paragraph +
  the `pcrecbench/CLAUDE.md` paragraph — 135 files changed total. The
  code fix stays in its own earlier commit (`12b2d00`), per the
  boilerplate's incremental-commit convention; the manager folds both
  at merge.
- **(f)** `pcrecbench/CLAUDE.md` KB-18 paragraph added (new "## The
  reporter, KB-18 (2026-09-17)" section, appended after "## The
  interpreter, [B13.3]" — the file's current tail) — the gap
  b42repdiag's own report flagged as forgotten the first time.
- **(g)** NOT run — see OWED below, per the hard box rule this lane's
  brief stated explicitly (pcrec's solo battery owns the box until
  ~18:00 EDT; current time at commit was 13:37 EDT). `make check-report`
  runs `python3 -m pcrecbench.tests.test_report` (the REAL_STORE-scale
  suite already run standalone pre-regen: **78 passed, 0 failed**,
  `test_report_run1.log`, `DONE rc=0`) followed by
  `python3 -m pcrecbench.tests.test_quick` (light, not yet run under
  the real `make` target). `make check-interpret` (132 checks, ~28 s,
  never loads the store) was also not run — conservatively deferred
  rather than judged against the ambiguous "single-group render"
  carve-out, since the brief named it explicitly as an OWED item to
  quote post-battery.

## Numbers this handback has

- 43 report groups regenerated; 129 report files + 4 sidecars = 133
  files changed, 135 including the two CLAUDE.md paragraphs.
- 41/43 groups: version-line-only delta (one line each).
- 1/43 groups (capability-0.1): the intended KB-18 fix, 5/5/157 lines
  (tsv/md/subject-grain).
- 1/43 groups (syntax-0.1): the same KB-18 rule firing on 7 ordinary
  single-line diagnostics containing a literal backslash, 85/85/2437
  lines — diagnosed, confirmed NOT drift, evidence above.
- Sidecars: 4/4 regenerated, 0 failures.
- `test_report.py` standalone: 78 passed, 0 failed.

## OWED (numbers this handback does NOT have)

- `make check-report`'s exact pass count (both `test_report.py` — result
  known standalone above but not re-run under the real target — and
  `test_quick.py`, not run at all yet).
- `make check-interpret`'s exact pass count.

Both are blocked by this lane's own hard rule (no full suites until
pcrec's solo battery clears, ~18:00 EDT) and are NOT run in this
handback. Run them for real and quote both targets' printed counts
once the battery clears — that is the one remaining step before this
branch's validation is COMPLETE.

## Delivery

Branch `lane/b42repdiag` (unchanged — this lane resumed it, did not
create a new one), commit `f851d2e` on top of `12b2d00`/`674235e`, this
report committed. Not merged — the manager merges.
