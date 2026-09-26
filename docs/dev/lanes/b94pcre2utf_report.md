# [B94] report — the pcre2 driver's own VALIDATE-ONCE find-all

Lane `b94pcre2utf`. Charter: `docs/dev/plan.md`'s `[B94]` row, ruled as
`docs/dev/decisions.md` BD15 (Frank: "keeping the check handicaps pcre2
times, so I want it removed after the first"). utf8@0.1's first window
lost `pcre2-utf-interp` (CELL_CAP, rc=124, 5400 s) and `pcre2-utf-jit`
(~10/75 patterns at 76 min, capped ~00:35) because `testees/pcre2/
driver.c`'s find-all never passed `PCRE2_NO_UTF_CHECK`, so libpcre2
re-validated the rest of the subject on every call under `PCRE2_UTF` --
the same quadratic shape BD14 already fixed in the oracle.

## Charter-vs-committed checklist

| charter item | committed | where |
|---|---|---|
| Call 1 validates the whole subject (offset 0, no flag) | YES | `testees/pcre2/driver.c` find-all loop |
| Calls 2..n on the same buffer pass `PCRE2_NO_UTF_CHECK` | YES | same, `utf_once && validated` branch |
| Every such start offset ASSERTED a character boundary (never silently trusted) | YES | `die()` on a non-boundary offset; negative control passes |
| Mirror the oracle's semantics, NOT its code (independent implementations) | YES | driver.c's own logic, no import from `oracle_pcre2.py`; the DFA/JIT dispatch differs structurally too |
| JIT checked, cited pcre2api/pcre2jit | YES | driver.c header comment + testees/pcre2/CLAUDE.md; MEASURED 71x-1811x, byte-identical answers |
| DFA checked too (not asked for by name, but the same call site) | YES | measured 167x-1289x, byte-identical answers; man pcre2api's dfa_match option list cited |
| search_short/match single-call path: decide by measurement, document | YES, NO FIX NEEDED | measured LINEAR in `--iters`, negligible at real subject sizes; see below |
| CONTROL: validate-once == always-check on bench/utf8 short + <=64 KB throughput | YES | `check_pcre2_utf_validate_once` (i), 7,200 cells, ~54 s |
| CONTROL: ill-formed subject still refused by name | YES | same check (ii), plus the boundary-assertion NEGATIVE |
| CONTROL: byte-mode configs untouched (argv/behaviour + testee_id) | YES | same check (iii): a real byte-mode run byte-identical with/without `--utf-always-check`; `pcre2-interp`'s build_flags carries no [B94]/BD15 note (`pcre2-utf-interp`'s does, the control); both testee_id SHAPES unchanged |
| Timing probe archived, source header | YES | `docs/dev/measurements/2026-09-26-b94-pcre2-driver-validate-once.txt` + `probe_b94_driver_validate_once.py` |
| Audit re2/onig/vectorscan/rust, measure don't assume | YES | see "The audit" below |
| Update testees/pcre2/CLAUDE.md | YES | new "[B94] VALIDATE-ONCE" section + two stale-note fixes |
| Identity question answered, reasoned not asserted | YES | "Identity" section below; testee_id/build_flags unaffected except the (uncommitted-anywhere) `pcre2-utf-*` note wording |
| Report with checklist + exact re-run command + projected cell time | YES | this file |
| Don't touch store/ or run a pinned window | YES | neither touched |
| Commit incrementally | YES | see git log on this branch |

## The fix, in one paragraph

`testees/pcre2/driver.c`'s find-all loop now tracks `validated` (call 1,
offset 0, always runs WITHOUT `PCRE2_NO_UTF_CHECK` -- libpcre2 validates
the whole subject there; an ill-formed one is refused, loudly, through
the existing `giveup:<code>:<message>` protocol, and the loop breaks
before any call 2 could happen). Calls 2..n pass `PCRE2_NO_UTF_CHECK`,
with the start offset asserted a character boundary first (`die()`, never
trusted). One call site, `do_match()`, dispatches to `pcre2_match` or
`pcre2_dfa_match` depending on `--dfa`; since `pcre2_match()` itself
dispatches internally to JIT-compiled code when present (man pcre2jit),
the SAME branch covers `pcre2-utf-interp`, `pcre2-utf-jit` and
`pcre2-utf-dfa` alike. `--utf-always-check` is a new, DRIVER-ONLY CLI flag
(never in the driver protocol at the top of `pcrecbench/adapters.py`,
never passed by `testees/pcre2/adapter.py`) that disables validate-once
and restores the pre-fix always-check path -- reachable only from
`make check-harness`'s new control and the archived probe.

## Measurements

All numbers below are from `docs/dev/measurements/2026-09-26-b94-pcre2-
driver-validate-once.txt` (verbatim raw output included) and from ad hoc
probes run in this session (cited inline); box: ubuntubudu, loadavg
0.71-1.45 (another lane's work in progress -- not a gated run; a
>1000x-scale timing win and byte-for-byte answer identity are not moved
by ordinary box load).

**pcre2 driver, `.` find-all under PCRE2_UTF, validate-once (default) vs
`--utf-always-check` (pre-fix control), interp/jit/dfa x 7 throughput
subjects (t-1m's always-check arm skipped by design -- projected ~2.5 h
from the quadratic scaling):**

| engine | subject | size | validate-once | always-check | ratio | answers |
|---|---|---:|---:|---:|---:|---|
| interp | t-64k | 65,536 B | 0.0139 s | 2.2336 s | 160.8x | identical |
| interp | t-256k | 262,144 B | 0.0311 s | 35.998 s | 1159.2x | identical |
| interp | t-1m | 1,048,576 B | 0.0859 s | SKIPPED | -- | -- |
| jit | t-64k | 65,536 B | 0.0078 s | 2.2439 s | 286.5x | identical |
| jit | t-256k | 262,144 B | 0.0199 s | 36.006 s | 1810.6x | identical |
| dfa | t-64k | 65,536 B | 0.0066 s | 2.2419 s | 338.4x | identical |
| dfa | t-256k | 262,144 B | 0.0280 s | 36.041 s | 1289.1x | identical |

(the four per-script 64 KB rungs -- lat/cyr/cjk/asc -- move the same way,
70.9x-441.1x; full table in the archive.)

**Ill-formed subject** (a lone `0xFF` far past the first match), both
paths: `giveup:-23:UTF-8 error: illegal byte (0xfe or 0xff)` -- identical.

**Search regime (no `--find-all`), scaling with `--iters`:**

| subject | iters | elapsed | per-call |
|---|---:|---:|---:|
| largest real short subject (30 B) | 1 | 11 us | 10.6 us |
| largest real short subject (30 B) | 1000 | 152 us | 0.15 us |
| t-256k (262,144 B, never a real search_short subject) | 1 | 1.017 ms | 1.017 ms |
| t-256k (262,144 B) | 1000 | 389.5 ms | 0.390 ms |

Total time is `iters x n`, never `n^2` (a single call, always at offset
0, never compounding across positions) -- confirmed by an isolated probe
against `libpcre2-8` directly (`p_match` with/without
`PCRE2_NO_UTF_CHECK` on the same 256 KB subject, 2,000 calls each):
opts=0 (checked) 394 us/call, opts=NO_UTF_CHECK 0.25 ns/call -- the
validation cost IS the whole per-call cost at this subject size, but it
is FLAT per call, and the harness's own calibration (which trims
`--iters` when a call is slow) absorbs it; find-all's own cost compounds
WITHIN one `iters=1` call as `pos` advances, which calibration cannot
touch. **No fix needed for search_short/match; documented in
`testees/pcre2/CLAUDE.md`.**

## The audit (re2/onig/vectorscan/rust)

Built each engine's real driver via its own adapter's `prepare_driver()`
and ran `.` find-all directly (t-64k vs t-1m, a 16x size step -- an
O(n^2) mechanism would show ~256x):

| engine | t-64k | t-1m | ratio for 16x size | verdict |
|---|---:|---:|---:|---|
| onig-utf8 | 18.1 ms | 147.4 ms | 8.1x | (sub)linear, MEASURED |
| re2-utf8 | 14.4 ms | 147.8 ms | 10.3x | (sub)linear, MEASURED |
| rust-default | 7.1 ms | 58.9 ms | 8.3x | (sub)linear, MEASURED |
| vectorscan-block-nosom-utf8 | 16 ms | 13 ms | flat (noise) | STRUCTURALLY IMMUNE: `--find-all` is a documented no-op at boolean grain (`driver.c`: `(void)find_all;`) -- there is no loop to compound |

`rust-default`'s `regex::bytes::Regex::find_at` operates over `&[u8]`
with no subject-validity check at all (`src/main.rs`; unicode mode
affects how CLASSES match, never whether the subject is pre-validated as
UTF-8) -- read from source AND confirmed empirically above. Neither
RE2's nor Oniguruma's C/C++ API exposes anything analogous to
`PCRE2_NO_UTF_CHECK` to misuse in the first place. **No further work
needed on any of the four.**

## Identity: does this change the testee?

**No.** `record_schema.md` 6.4 derives `testee_id` from (engine_name,
engine_version, engine_mode, captures, simd) + `config_extra`; this fix
touches none of them. The new branch in the find-all loop is INERT for
every byte config (`pcre2-interp`/`-jit`/`-dfa`): `copts` never carries
`PCRE2_UTF` for them, so `utf_once` is always false -- their argv and
answers are byte-for-byte what they were (measured, `check_pcre2_utf_
validate_once` (iii), not merely reasoned). No new CLI flag reaches any
real testee's argv: `--utf-always-check` is driver-only, appended only by
the control and the archived probe, never by `adapter.py`. The one
OBSERVABLE change for the `pcre2-utf-*` siblings is a wording fix to
their `build_flags` (`UTF_BUILD_NOTE` in `testees/pcre2/adapter.py`,
distinguishing compile-time from match-time `PCRE2_NO_UTF_CHECK`, since
the old text's blanket "never" was stale) -- and `store/index.tsv` has
NO `pcre2-utf-*` record at all (the only prior attempt at these two
testees lost to CELL_CAP and wrote nothing), so there is no risk of
mixing incomparable records under one id. A driver change that altered
ANSWERS would need a new id; this one is checked, byte for byte, not to.

## Re-running the two lost cells

Command (the manager launches it, per the boilerplate's long-run rule):

    SUBBENCH=utf8 TESTEES="pcre2-utf-interp pcre2-utf-jit" setsid scripts/run_window.sh > /dev/null 2>&1 &

No extra env needed beyond `SUBBENCH`/`TESTEES` -- the fix needs no
config change, no new axis, no new flag on any real testee, and the
script's own defaults are otherwise unchanged (`PIN=11`, `TRIALS=5`,
`STORE=store`, `CELL_CAP=5400` -- the same cap the OLD driver hit; this
lane's whole point is that the fixed driver clears it by five-plus
orders of magnitude, not that the cap needs raising). `LOG` defaults to
`build/windows/window_utf8_<UTC timestamp>.log`; the script's own
completion line and its printed per-cell `rc=` are the durable markers.

**Projected cell time** (grounded in the measurements above, not a
guess): `check_pcre2_utf_validate_once`'s own real-driver sweep across
ALL 75 compiling bench/utf8 patterns x 96 subjects (91 short_search +
5 <=64 KB throughput) completed in ~54 s WALL for BOTH the validate-once
AND the always-check arm combined (150 subprocess launches) -- so
validate-once's own share of a single full-pattern sweep is a small
fraction of that. A tighter, pattern-scaled bound: `.` (a near-worst-case
witness -- it matches every position, so it makes the MOST find-all
calls of any pattern in the set) sums to 0.167 s across all 7 throughput
subjects (INCLUDING t-1m) for `pcre2-utf-interp` in one pass; scaled to
75 patterns and 5 trials that is `0.167 x 75 x 5 ~= 63 s` for the
THROUGHPUT regime alone -- an upper bound, since call count (and so
total time) scales with how often a pattern matches, and few of
bench/utf8's 75 feature-specific patterns match as densely as `.` does.
The search_short regime adds microseconds per pattern at these subject
sizes (measured above) and is negligible in comparison. `pcre2-utf-jit`
adds one `pcre2_jit_compile` call per compile trial (sub-millisecond,
unaffected by this fix) and is expected to land within the same order of
magnitude. **Projected: each cell completes in well under two minutes**,
five-plus orders of magnitude inside the 5400 s CELL_CAP that stopped it
before.

## make check status

Ran directly (not the full ~20-min `make check-harness`, which is a
long run per the boilerplate's DO-THEN-FINISH rule -- OWED to the
manager, see below): `check_pcre2_utf_validate_once` (7/7 PASS, ~54 s),
`check_pcre2_dfa` (11/12 PASS -- the one failure,
"a real quick cell on bench/email writes a MEASURED scratch record", is
a PRE-EXISTING environment gap in this scratch worktree: bench/email's
subject trees are gitignored and had not yet been generated here; fixed
by running `python3 bench/email/gen_subjects.py` +
`gen_throughput_subjects.py`, which `make check`'s own target does
automatically -- not a regression from this change), `check_kb17_find_
all_advance` (4/4 PASS), `check_utf8_find_all_advance` (24/24 PASS). All
four exercise `testees/pcre2/driver.c` directly and pass clean against
this lane's edit.

**OWED to the manager** (per the boilerplate: a run longer than ~4
minutes is launched by the manager, not this lane):

    make check

Working directory: this worktree's root. No log path is pre-created (the
Makefile's own targets write nothing to a fixed log by default) --
whoever launches it should redirect stdout/stderr to a file and treat
the process's own exit code as the completion signal (0 = green). Based
on `docs/dev/plan.md`'s STATUS line, the last confirmed count was
`4/72/0, 227/227, 62` at [B29]'s pin and has grown at every subsequent
lane merge; this lane adds 7 new checks to `check-harness` and touches
no schema/report/interpret code, so the expected shape is the prior
green count plus 7 on the harness section, exit 0.

## Files touched

- `testees/pcre2/driver.c` -- the fix (VALIDATE-ONCE find-all,
  `--utf-always-check`, `PCRE2_NO_UTF_CHECK` define)
- `testees/pcre2/adapter.py` -- `UTF_BUILD_NOTE` wording fix (compile-time
  vs match-time `PCRE2_NO_UTF_CHECK`)
- `testees/pcre2/CLAUDE.md` -- new "[B94] VALIDATE-ONCE" section, two
  stale "never PCRE2_NO_UTF_CHECK" mentions corrected
- `tools/selfcheck.py` -- `check_pcre2_utf_validate_once` (7 checks),
  wired into `main()`
- `docs/dev/measurements/probe_b94_driver_validate_once.py` +
  `2026-09-26-b94-pcre2-driver-validate-once.txt` -- the archived probe
- `docs/dev/measurements/CLAUDE.md` -- the new archive's entry
- `docs/dev/plan.md` -- `[B94]` row marked `STATE:completed` with a full
  summary (not yet relocated to `plan_completed.md` -- eighteen other
  `STATE:completed` rows currently sit in `plan.md` too; the manager's
  batch housekeeping, per precedent)
- `docs/dev/dev_journal.md` -- session entry
- this file
