# scripts/ — committed operational scripts

Scripts that used to live only as one-off scratchpad copies a manager
session re-typed by hand each time it opened a quiet window. Committing
them here means the SLEEP-15 / retry fix (OD-B12, 2026-08-28) lives in
one place instead of in whichever session's scratchpad happened to have
the latest edit.

| file | role |
|---|---|
| `run_window.sh` | one quiet-window measurement run: `pcrecbench quiet` warm-up (ADVISORY — its exit code is discarded by the pipe on purpose; since [B20] the CLI judges through the same `gate()` a run does, and the per-cell `run` below makes the binding decision), then `pcrecbench run` per testee in `$TESTEES` (env-overridable, see its own header), re-measuring an `rc == 4` `inconclusive-spread` cell ONCE (schema v1.4, ruling R-6 — the first record stays; a spread is not a gate transient) and retrying an `rc == 3` quiet-gate refusal up to twelve times with a 30 s backoff (3 × 20 s lost cells on 2026-08-29 — the header says why), plus a flat `sleep 15` before every cell AFTER the first (the post-cell transient every cell but the first needed a retry for on 2026-08-28); `pcrecbench index` at the end; a `WINDOW_RUN_COMPLETE` sentinel line. The PER-CELL wall-clock cap is `$CELL_CAP` ([B32]; seconds, default 5400 — the value and the measurement that chose it unchanged), printed in the log header and on every attempt line, with an explicit named line when `rc == 124` says the cap killed a cell and no record was written. `--dry-run` (or the `EXTRA`/`STORE`/`TRIALS` env vars it sets for you) makes every cell synthetic, skips the quiet gate, and runs one trial AT THE SCRATCH TIER into a scratch store (since 2026-09-01: a one-trial pinned record is `inconclusive-spread` by rule R-12 and was re-measured once per rehearsal cell) — see the script's own header for the exact combination and the refusal it applies if `STORE` still resolves to the canonical `store/`. |
| `run_suite.sh` | ([B26], 2026-09-01) one quiet window over SEVERAL sub-benches in a stated PRIORITY order (`SUITE="bounded loglines email"`), each through `run_window.sh` unchanged; a per-set testee list via `TESTEES_<set>` and a second pass of one set with other testees as `<set>:<label>` + `TESTEES_<set>_<label>`; a per-set cap the same way, `CELL_CAP_<set>` and `CELL_CAP_<set>_<label>` ([B32]), passed through only where set so a silent set keeps `run_window.sh`'s own default; a broken set never stops the suite (its rc is in the summary); `--dry-run` passes through; ends with per-set `rc`/minutes lines and a `SUITE_RUN_COMPLETE` sentinel in its own log (`build/windows/suite_*.log`). Launch under `setsid` as `run_window.sh`. |

## Running it

    setsid scripts/run_window.sh > /dev/null 2>&1 &

MUST be launched under `setsid`: a harness background task has a
10-minute cap and a real window runs far longer. `set -u` and
`LC_ALL=C` throughout, per this project's measurement conventions
(root CLAUDE.md).

Rehearsal (provably light — no engine measurement, no quiet gate, one
trial, into a store this cannot corrupt):

    SUBBENCH=email TESTEES=pcre2-interp scripts/run_window.sh --dry-run

Env vars (`SUBBENCH`, `PIN`, `TRIALS`, `STORE`, `TESTEES`, `CELL_CAP`,
`NOTE`, `EXTRA`, `LOG`) are documented in the script's own header comment —
read that before changing a default, not this file.

## How long a cell takes — the table a window planner reads ([B32])

`$CELL_CAP` is a budget, and a budget is only as good as the numbers it
is set against. A cell killed by the cap exits 124 and writes NOTHING;
the suite summary cannot distinguish that from a clean set, because a
set's rc is its `index` call's. So: what the longest cell of each set
ACTUALLY took at pin `1989c62`, per testee family.

**Method, and its one caveat.** Every figure below is the gap between
one record's own start timestamp and the next record's, over
`store/index.tsv`'s thirty rows from the [B26] full-suite window
(2026-09-02T02:45Z → 13:55Z) — the same derivation
`docs/dev/ledgers/2026-09-02-full-suite-1989c62.md` §1.1 uses, because a
record carries its START (`run.timestamp`) and no end. A gap therefore
OVER-states its cell by the `sleep 15` and the next cell's quiet-gate
warm-up (~30 s), which is the right side to err on for a budget. Two
cells have no gap that means anything and are taken from the ledger
instead: `auto-clang` on bounded (its gap spans the two cells the old
3000 s cap then killed) and `vm-clang` (the window's last cell).

| set | pcre2 interp / jit | pcrec, gcc | pcrec, clang |
|---|---|---|---|
| `bounded@0.3` | **42.3 min** (interp) | **48.4 min** (`vm-in`) | **49.4 min** (`auto-clang`, ledger §1.1) |
| `loglines@0.1` | 9.1 min (interp) | 8.8 min (`vm-in`) | 10.6 min (`vm-clang`) |
| `email-specimen@0.2` | 11.3 min (jit) | 7.2 min (`vm-in`) | — not measured |
| `altwide@0.1` | **41.9 min** (interp) | 5.0 min (`auto`) | — not measured |

Against the 5,400 s (90 min) default that is roughly 2× headroom on the
worst cell measured, which is what the default was set for on the same
night — after the 3,000 s cap it replaced killed two of bounded's clang
cells outright.

**Where the default does NOT hold: `bench/altwide@0.2`'s raised-cap
pass.** MEASURED and projected in
`docs/dev/measurements/2026-09-02-altwide-raised-cap-sizes.txt` §2, over
the set's thirteen wide rungs at five trials:

| cell | COMPILE alone, both forms, 5 trials | against the 5,400 s default |
|---|---|---|
| `pcrec-vm-bigcap` | **4,499 s** (75.0 min) | over it before one match is measured |
| `pcrec-auto-bigcap` | 705 s (11.8 min) | fits easily |

The two routes have opposite cost structures — a forced-VM artifact is
straight-line code that pcrec emits in 0.01-0.06 s and gcc pays
5.1-333.8 s for, an auto-route one is a table that pcrec pays 11.0-36.6 s
to build and gcc barely notices — so they need separate budgets rather
than one number. And gcc is SUPERLINEAR in emitted code bytes and
accelerates, so a rate times a total under-projects badly: the linear
figure for that VM cell is 290 s per trial, one third of the measured
per-rung sum.

Two levers, and only one of them keeps the trial count the v1.4 spread
rule needs:

    # (a) split the two largest rungs into their own labelled pass
    #     (w-2048 + s-4096 are 3,354 s of the 4,499); the other eleven
    #     then run at full five trials inside the default cap
    SUITE="altwide:bigcap altwide:bigwide"     TESTEES_altwide_bigcap="pcrec-auto-bigcap pcrec-vm-bigcap"     CELL_CAP_altwide_bigwide=10800 setsid scripts/run_suite.sh

    # (b) or raise the cap and run the thirteen rungs as one cell
    CELL_CAP_altwide_bigcap=10800 SUBBENCH=altwide     TESTEES="pcrec-auto-bigcap pcrec-vm-bigcap" setsid scripts/run_window.sh

Re-derive this table after any window that measures a new set or a new
testee family; the derivation is eight lines over `store/index.tsv`.

**`pcrec-auto-noisland` ([B37], 2026-09-05; not yet measured).** Estimate
from its sibling `pcrec-auto`: the same route on every set (the island is
a VM-program lowering, so the DFA-selected cells are the same artifact but
for three stamp lines), and on altwide's VM-selected forms the chain
program is 1.1-1.4x the island's in code bytes (w-256 341,301 vs 292,043 B
at the same pin) with gcc superlinear in it -- budget the `auto` figure
plus a third on altwide, the `auto` figure elsewhere.

## Maintenance

Update this file when a script is added, removed, or changes role.
