# b146wrap report -- [B146] box-queue reservation wrapper (inbox I-161)

Lane b146wrap, branch lane/b146wrap. Nothing heavy was run (fake state, sleep chains).

## Charter vs committed

| promise | artifact |
|---|---|
| 1 `scripts/boxq_window --name --prio --cap [--patience --idle-ok --start-s] -- CHAIN ARGS` | `scripts/boxq_window` |
| 1a `.window` with every contract key; log = own run log; done_ere/expect/witness/fail_ere; once per name | written atomically (tmp + mv); log `/var/tmp/pcrecbench/<name>win/run.log`; `done_ere=^BENCH_WINDOW_COMPLETE rc=`, `expect=0`, `witness=BENCH_WINDOW_COMPLETE rc=0`, `fail_ere=^BENCH_WINDOW_FAILED `; refuses an existing `.window`, `.cancel`, or `*-bench-NAME.state` at ANY prio |
| 1b poll state read-only, 30 s (`BQ_POLL`), `BQ_STATE_DIR` | done; QUEUED waits and logs changes; DONE before start exits 3 without running |
| 1c start under setsid, keep polling, kill group BY PID on leaving RUNNING | done (TERM, `BQ_KILL_GRACE` 10 s, KILL; kill is `kill -- -PID`, no pkill) |
| 1d complete line on success; trap prints fail line on any abnormal path | done: rc 0 -> `BENCH_WINDOW_COMPLETE rc=0`; chain rc!=0 / signal / state left RUNNING / error -> `BENCH_WINDOW_FAILED <why>` (EXIT trap + INT/TERM/HUP) |
| 1e `--no-queue` | done, no reservation, no log |
| 1f `--cancel NAME` | done, writes `NAME.cancel` |
| 2 self-test, all listed cases, checked against the log | `scripts/tests/test_boxq_window.sh`, 41/41, ~25 s; plus a SIGTERM-to-wrapper case |
| 2 make slot | `make check-boxq-window`, added to `make check` (a sibling of `check-wtprune`) |
| 3 docs | `scripts/CLAUDE.md`, `scripts/tests/CLAUDE.md`, `docs/dev/lanes/BOILERPLATE.md`, manager SKILL.md |

Design choices: the chain's own output goes to `run.log.chain`, so no chain line can match
done_ere/fail_ere; a chain that exits nonzero prints the FAIL line, never `complete rc=N`
(so a window-script exit code, e.g. sidecar-regen failure count, reads as `failed BENCH-FAIL`,
not `red POPULATION`). Contract lines carry no timestamp prefix (they are anchored with `^`).

## Questions for pcrec-main (contract ambiguities)

1. Is `log` required to be ABSENT before RUNNING, or only to exist within `start_s` after it?
   The wrapper creates the log when it writes the `.window` (queue-wait lines are logged), so it
   exists before RUNNING. If NO-START is judged by creation time or mtime, say so.
2. Is the log scanned from the start or only from RUNNING onward? The wrapper can write a
   fail line before RUNNING (state DONE before start); presumably irrelevant, as pcrec is DONE.
3. Does a `.window` that parses ok but never gets a state file (not imported) have any signal?
   The wrapper waits `BQ_IMPORT_WAIT` (900 s) for the file to appear, then fails; what is the real
   import cadence?
4. `patience` and `start_s`: no defaults given. The wrapper defaults patience=86400, start_s=300.
5. Is the state file's `<prio>` the one in the `.window`, with no renumbering on import?
   The wrapper derives the filename as `<prio>-bench-<name>.state`.
6. Is the state file replaced atomically (rename) or truncated and rewritten in place ("rewritten in
   place")? The wrapper reads one line; a torn read of an empty file is treated as absent (before RUNNING:
   keep waiting; after RUNNING: two consecutive empty/absent reads (1 s apart) are required before the
   chain is stopped, an explicit non-RUNNING word stops it at once). Does pcrec replace atomically?
7. Any `DONE green` written while our chain is still running (e.g. done_ere matched early)?
   The wrapper treats any non-RUNNING state as a stop signal.
