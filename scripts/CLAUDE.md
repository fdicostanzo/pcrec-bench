# scripts/ — committed operational scripts

Scripts that used to live only as one-off scratchpad copies a manager
session re-typed by hand each time it opened a quiet window. Committing
them here means the SLEEP-15 / retry fix (OD-B12, 2026-08-28) lives in
one place instead of in whichever session's scratchpad happened to have
the latest edit.

| file | role |
|---|---|
| `run_window.sh` | one quiet-window measurement run: `pcrecbench quiet` warm-up, then `pcrecbench run` per testee in `$TESTEES` (env-overridable, see its own header), retrying an `rc == 3` quiet-gate refusal thrice with a 20 s backoff, plus a flat `sleep 15` before every cell AFTER the first (the post-cell transient every cell but the first needed a retry for on 2026-08-28); `pcrecbench index` at the end; a `WINDOW_RUN_COMPLETE` sentinel line. `--dry-run` (or the `EXTRA`/`STORE`/`TRIALS` env vars it sets for you) makes every cell synthetic, skips the quiet gate, and runs one trial into a scratch store — see the script's own header for the exact combination and the refusal it applies if `STORE` still resolves to the canonical `store/`. |

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
