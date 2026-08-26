# pcrec-bench known issues — bugs in this project's own harness, adapters and reporter

Rows `KB-n`, never deleted; a fixed row says so in place with the commit.

## KB-1 (2026-08-25) — `runtime_options` records a bare flag whose value is the NEXT argv token as `{"--features": true}`

testees/pcrec/adapter.py splits flags on `=` only, so `["--features",
"all"]` records `{"name": "--features", "value": true}` and the value
`all` is lost (it is still in `build_flags` as text). Found by lane
b10loop. Fix: pair a bare flag with a following non-flag token. Owner:
the pcrec adapter; a one-line change plus a check. Not urgent — the
testee_id and build_flags carry the truth.

**FIXED 2026-08-25 (lane/b15floor, commit 3f5131da54cacb23203553ff9f98116c1708c46a).**
`testees/pcrec/adapter.py` gained `runtime_options(flags)`: it walks the
flag list and pairs a BARE flag (no `=`) with the token that follows it
when that token is not itself a flag — `["--features", "all"]` now
records `{"name": "--features", "value": "all"}`. An `=` flag
(`--engine=vm`) is unchanged; a trailing bare flag, or one immediately
followed by another flag, is still `{"value": true}`. Checked by
`tools/selfcheck.py`'s `check_kb1_runtime_options` (`pcrec-auto`'s
`describe()` must show `--features` paired with `"all"`).

## KB-2 (2026-08-25) — the record carries NO expected answer on an agreeing match row, so `matches m/n` cannot be derived from records; the reporter prints `n/s` until the schema says it

History: reporter v3 ([B14] R3) read the count from bench/<dir>/
expectations.tsv (a sidecar — the reporter must work from RECORDS
alone); the first draft of this row claimed the count is derivable from
`match_outcome` + `observed`. Lane b14report MEASURED that it is not: on
a `matched-as-expected` row the harness writes `observed: null` (it is
populated only on a DISAGREEING row), so deriving m from records would
undercount systematically. Reporter v4 (c07d0f6) therefore prints
`matches: n/s` and imports no sidecar. FIX (a schema/harness change,
v1.4 additive): every match row carries the EXPECTED answer class
(`expected: match | nomatch`, plus the expected span when known) — the
expectation's verification method already travels with the sub-bench,
and the record is then self-describing; the reporter's m/n returns,
records-only. Owner: the next schema/harness row; small.
