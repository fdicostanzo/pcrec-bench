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

## KB-2 (2026-08-25) — the reporter's `matches m/n` reads the sub-bench sidecar, not the record

pcrecbench/report.py (reporter v3, [B14] R3) counts matching subjects
from bench/<dir>/expectations.tsv via pcrecbench.subbench and omits the
figure when the sub-bench cannot be resolved. The reporter must work from
RECORDS alone: a match row's `match_outcome` + `observed` answer says
whether the expected answer was a match (`matched-as-expected` with an
observed match ⇒ expected match). Fix: derive m from the record's rows;
keep the sidecar out of the reporter. Owner: the next reporter row.

