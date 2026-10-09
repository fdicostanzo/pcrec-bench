# [B129] priming A/B -- lane b129prime report (2026-10-09)

STATUS: implementation COMPLETE and committed; measurement RUNNING (detached);
analysis + verdict OWED (see "OWED").

## Charter-vs-committed checklist

| Brief item | State | Artifact |
|---|---|---|
| `--prime` on every driver (pcre2, pcrec, re2, rust, onig, tre, vectorscan) | DONE | `testees/*/driver.c|cc`, `testees/rust/src/main.rs`: the loop runs from `-prime`; the clock is re-read at `it == 0`; the primed pass is the loop body itself (same operation, find-all pass included), answer overwritten by the timed iterations. Without the flag: `prime = 0`, loop bounds and clock unchanged. |
| adapter handle kwarg | DONE | every `testees/*/adapter.py` appends `--prime` iff `handle["prime"]` |
| `run` / `quick` `--prime` | DONE | `pcrecbench/__main__.py`, `harness.run_cell(prime=)` |
| record sentence, no schema change | DONE | `harness.PRIME_NOTE` appended to the note |
| pinned-tier refusal by name | DONE | `harness.PRIME_PINNED_REFUSAL`, raised before the store rule |
| `check_prime_flag` + tools/CLAUDE.md | DONE | `tools/selfcheck.py` (registered in `main()`); 14 driver rows (7 engines x 2 regimes) + refusal + control PASS |
| check-report, check-frontpage | DONE | both rc 0 (detached run) |
| experiment | RUNNING | `docs/dev/measurements/2026-10-09-b129-prime-run.sh`, log `build/b129-prime-run.log` in the worktree, marker line `DONE rc=` |
| analysis, archive, verdict, methodology wording | OWED | `docs/dev/measurements/2026-10-09-b129-prime-analysis.py` written; output archive `2026-10-09-b129-prime-ab.txt` owed |

Not run (by instruction): the whole `make check-harness`.

## Design notes
- The primed pass uses the loop body unchanged, so "exactly one untimed
  execution of the same operation" holds by construction for single-match and
  find-all modes; rust's per-subject worker thread and the C drivers' alarm
  both cover the priming call (a priming call that exceeds the subject
  timeout is a timed-out subject, not a silent hang).
- Calibration passes (iters=1 sweeps) are primed too when `--prime` is set;
  the flag is a property of the whole cell.
- `check_prime_flag`'s control stops at a sentinel in `quiet.check`; an
  earlier draft let the control run a real cell on a quiet box (caught and
  fixed before the experiment).
