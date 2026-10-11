# Lane b135r8 report -- [B135] KB-37: R8 "previous version" by pin order, not timestamp

Branch `lane/b135r8` (worktree `worktrees/b135r8`), not merged, not pushed.

## Fix
- `pcrecbench/report.py` `_previous_pin_testee` (the ONE rule behind R8's `Δ vs previous version`,
  the D119 bar and the [B79] null band): partner = nearest EARLIER PIN by catalogue/rules.toml
  `[[pin_order]]` (new `_catalogue_pin_order`, reads the same table `tools/trend.py` and
  `interpret.py` read). A pcrec pin missing from the table raises `report.UnorderedPinError`
  naming the pin; it is consulted only when a cross-pin candidate exists (a single-pin report
  never needs the table; the fixtures' ~15 synthetic pin slugs would otherwise all refuse).
  Engines with no `[[pin_order]]` (pcre2, re2, ...) keep the older-timestamp rule: nothing else
  orders their versions (justified, documented in the docstring).
- `pcrecbench/interpret.py` `r_bucket_span` made the same timestamp assumption in its own partner
  search; now `ctx.pin_index` (raises by name). Its dead `ts_by_testee` removed.
- Other timestamp orderings grepped: `--since/--until`, `ts_key`, duplicate-record "newest measured
  record per (subbench, testee, machine)" (report.py ~4187), `--all-records` suffix -- all order
  RECORDS OF ONE TESTEE or filter by time, never mean "older pin"; untouched.
- Reporter VERSION string NOT bumped (a bump re-stamps every committed report; manager's call).

## Tests
- `test_kb37_r8_orders_by_pin_not_timestamp_abba` (ABBA: caps a15fb77b early / nocaps a15fb77b late;
  asserts partner, Δ detail orientation, "faster x2.50" for both configs, and UnorderedPinError by
  name). Verified FAILS on the old rule ("auto-nocaps-simdna: the previous pin of 7388f1c0 must be
  a15fb77b"), passes on the new.
- test_report.py registers its synthetic pin slugs into the cached order at import.
- No new interpret fixture: with two pins the span rule is direction-blind (abs); the partner choice
  differs only with >=3 pins, which no existing fixture has. Offered as a follow-up.

## Regeneration (scripts/regen_reports.py --only revend-7388f1c0; scripts/regen_sidecars.py)
4 groups, 20 files written, 0 failures; 80 sidecars, only the 4 revend ones changed.
Diff proof (python, `git show HEAD:` vs working tree):
- matrix.tsv x4 and subject-grain.md x4: byte-identical (not modified).
- median_ns rows: identical in all 4 set TSVs and 4 subject-grain TSVs.
- set TSVs: all non-Δ columns of every ranking/record row identical; the only changes are
  `delta_verdict` on nocaps rows (1668 + 1668 rows capability, 216 email, 1008 litrun, 528 loglines:
  the verdict moved from the BEFORE testee's row to the AFTER testee's row), the `d119` rows of
  nocaps (move to the AFTER testee; caps d119 rows change only `band_pct`, the band being pooled over
  both configs), the `d119_view` summary rows, `null_band` rows (14->7, 20->10: the inverted
  `7388f1c0 -> a15fb77b` pair rows removed), and the `null_band_clearance=` text of
  `query_yes_beats_nocaps` rows. Subject-grain TSV: only the one inverted `null_band` identity line.
- Sidecars: report/subject_grain sha stamps + R-DELTA/null-band rows only.

## Validation
- check-report: OK (test_report 102 passed, 0 failed = 101 prior + the new test; test_quick, test_matrix_page, fixtures, CLI smoke all OK).
- check-interpret: 254 passed, 0 FAILED. check-trend: ALL PASS, trend_cite_check 0 problems.

## Charter vs committed
| item | artifact |
|---|---|
| 1 fix report.py/interpret.py, pin order, loud on unknown | commit on lane/b135r8 |
| 2 ABBA test fails before / passes after | test_report.py |
| 3 KB entry + caveat removed | docs/dev/known_issues.md KB-37; reports/CLAUDE.md |
| 4 regenerate 4 groups + sidecars, diff-prove | reports/2026-10-10-*-revend-7388f1c0.*, above |
| 5 checks | above / handback |
| OWED | reporter VERSION bump decision (manager); interpret 3-pin fixture (optional); O-92 draft should cite the corrected nocaps Δ |
