# pcrec-bench known issues — bugs in this project's own harness, adapters and reporter

Rows `KB-n`, never deleted; a fixed row says so in place with the commit.

## KB-1 (2026-08-25) — `runtime_options` records a bare flag whose value is the NEXT argv token as `{"--features": true}`

testees/pcrec/adapter.py splits flags on `=` only, so `["--features",
"all"]` records `{"name": "--features", "value": true}` and the value
`all` is lost (it is still in `build_flags` as text). Found by lane
b10loop. Fix: pair a bare flag with a following non-flag token. Owner:
the pcrec adapter; a one-line change plus a check. Not urgent — the
testee_id and build_flags carry the truth.
