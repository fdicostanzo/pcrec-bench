# scripts/ — committed operational scripts

Scripts that used to live only as one-off scratchpad copies a manager
session re-typed by hand each time it opened a quiet window. Committing
them here means the SLEEP-15 / retry fix (OD-B12, 2026-08-28) lives in
one place instead of in whichever session's scratchpad happened to have
the latest edit.

| file | role |
|---|---|
| `run_window.sh` | one quiet-window measurement run: `pcrecbench quiet` warm-up (ADVISORY — its exit code is discarded by the pipe on purpose; since [B20] the CLI judges through the same `gate()` a run does, and the per-cell `run` below makes the binding decision), then `pcrecbench run` per testee in `$TESTEES` (env-overridable, see its own header), re-measuring an `rc == 4` `inconclusive-spread` cell ONCE (schema v1.4, ruling R-6 — the first record stays; a spread is not a gate transient) and retrying an `rc == 3` quiet-gate refusal up to twelve times with a 30 s backoff (3 × 20 s lost cells on 2026-08-29 — the header says why), plus a flat `sleep 15` before every cell AFTER the first (the post-cell transient every cell but the first needed a retry for on 2026-08-28); `pcrecbench index` at the end; a `WINDOW_RUN_COMPLETE` sentinel line. `--dry-run` (or the `EXTRA`/`STORE`/`TRIALS` env vars it sets for you) makes every cell synthetic, skips the quiet gate, and runs one trial into a scratch store — see the script's own header for the exact combination and the refusal it applies if `STORE` still resolves to the canonical `store/`. |
| `run_suite.sh` | ([B26], 2026-09-01) one quiet window over SEVERAL sub-benches in a stated PRIORITY order (`SUITE="bounded loglines email"`), each through `run_window.sh` unchanged; a per-set testee list via `TESTEES_<set>` and a second pass of one set with other testees as `<set>:<label>` + `TESTEES_<set>_<label>`; a broken set never stops the suite (its rc is in the summary); `--dry-run` passes through; ends with per-set `rc`/minutes lines and a `SUITE_RUN_COMPLETE` sentinel in its own log (`build/windows/suite_*.log`). Launch under `setsid` as `run_window.sh`. |

## Running it

    setsid scripts/run_window.sh > /dev/null 2>&1 &

MUST be launched under `setsid`: a harness background task has a
10-minute cap and a real window runs far longer. `set -u` and
`LC_ALL=C` throughout, per this project's measurement conventions
(root CLAUDE.md).

Rehearsal (provably light — no engine measurement, no quiet gate, one
trial, into a store this cannot corrupt):

    SUBBENCH=email TESTEES=pcre2-interp scripts/run_window.sh --dry-run

Env vars (`SUBBENCH`, `PIN`, `TRIALS`, `STORE`, `TESTEES`, `NOTE`,
`EXTRA`, `LOG`) are documented in the script's own header comment —
read that before changing a default, not this file.

## Maintenance

Update this file when a script is added, removed, or changes role.
