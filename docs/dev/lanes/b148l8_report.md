# b148l8 -- [B148] L8: `tools/check_unusual.py` + `make check-unusual`

Branch lane/b148l8. Checks/Makefile only; no timing, no download, ~/pcrec untouched.

## Decision: where the existing checks live
MOVED. `check_calls`, `check_vars`, `check_callouts`, `check_assist` are no longer called from
`tools/selfcheck.py` main() (four calls removed); `tools/check_unusual.py` runs them as sections
(imports, same `run(ok, bad)` interface). `check_unusual_gate_skips` STAYS in selfcheck (it is about the
generic gates over every set). `tools/tokcount.py ledger-check` stays in `make check-tokcount` (counter vs
ledger: tokens/lines/sha256/verdict/duplicates/one file per row) and is NOT repeated. `bench/unusual/check_set.py`
(previously wired nowhere) is now the `set` section. `check-unusual` is in `make check` (once). Consequence:
`check-harness`'s count drops by the four slices' checks and `check-unusual` carries them.

## Coverage table: L8 row of unusual_set_v1.md section 10 -> where
| item | covered by | status |
|---|---|---|
| `UNUSUAL_GATE_SKIPS` + self-test | selfcheck.py `check_unusual_gate_skips` | already (b148land) |
| counting build (no fire log in timed builds) | check_callouts.py section 1 | already (L5) |
| calibration | tools/callout_calib.py -- a TIMING read | deliberately NOT in a smoke suite; stream calibration of iters is check_calls/run_cell |
| pass == twin (and pass-nofn == twin) | check_callouts.py section 3 | already (L5) |
| assist ledger vs counter (tokens, sha256) | tools/tokcount.py ledger-check (`make check-tokcount`) | already (L2), not repeated |
| assist ledger vs the 3.0 table: 43 pairs, each exactly once, family column | check_unusual.py `assist-tree` | ADDED |
| every member x non-native engine present (derived from 3.0, not from the ledger) | `assist-tree` | ADDED |
| file set under assists/<member>/<engine>/ == ledger pairs (no lane deleted/orphaned another's assist) | `assist-tree` | ADDED |
| reviewer_verdict not `pending`/empty; author + reviewer lanes named; one author lane per (family, engine); author != reviewer | `assist-tree` | ADDED |
| ledger verdict counts == r10a/r10b `Counts` lines (42 accepted, 1 not-idiomatic) | `assist-tree` | ADDED |
| negative controls for the above (pending, deleted file, orphan file, dropped/duplicated row, native-engine row) | `assist-tree` controls | ADDED |
| memo counts (vars) | check_vars.py section 2 (miss count == d, stream length fixed, == values/streams.tsv) | already (L7) |
| Onig witnesses | check_callouts.py section 5 | already (L5) |
| `expectations_stream` re-derive | check_vars.py section 2 (`gen_expectations.py --streams-only --check`, whole file); full `--check` = `check_set.py --full` (minutes, not in make check) | already |
| generators / reference scanner / host references / F2 pins | bench/unusual/check_set.py | already, now wired |
| assist pipeline smoke (templates, selftests, echo, run_cell, X50, grant rule) | check_assist.py | already (b148aw) |
| calls streams / limits / high-water | check_calls.py | already (L4) |

## Counts and runtimes
assist-tree: 16 checks (9 + 7 controls), 0.0 s. Other sections' counts/runtimes: OWED below (the
section summary at the end of the `check-unusual` log prints each section's passed/failed/seconds).
Earlier per-module estimates from tools/CLAUDE.md: calls ~70 s, callouts ~4 min, assist ~15 s warm, set ~1 min.

## make check
OWED. Launched detached after this commit:
  cwd: /home/pcrec/projects/pcrec-bench/worktrees/b148l8
  command: `make check` ; log /var/tmp/pcrecbench/b148l8/make_check.log ; marker line `DONE rc=<n>` at its end.
Read: the `check-unusual:` summary line and the per-section table; `check-harness: N check(s) passed, M FAILED`.
The email quick-cell check is load-sensitive -- if it is the only red, say so.
