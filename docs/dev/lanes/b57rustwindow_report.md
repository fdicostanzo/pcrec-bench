# lane b57rustwindow — rust-default's capability@0.1 first pinned sample

2026-09-19, wake.md queue item 1. Brief: measure `rust-default` (the
twelfth [B7] roster engine, `testees/rust/`) against `bench/capability@0.1`
into the canonical store, predictions file authored and committed BEFORE
the run.

## Head SHAs

- `04cee1d` — predictions committed BEFORE the run
- `826c1f6` — the window's full deliverable (record, index, report group,
  sidecar refresh, docs)

Branch `lane/b57rustwindow`, worktree `worktrees/b57rustwindow`, NOT
merged (per boilerplate: the manager merges).

## Order of operations, as delivered

1. **Worktree bootstrap.** `git worktree add`, `git rev-parse --show-toplevel`
   confirmed, both subject-tree generators run for every `bench/*/` (not
   only capability — the boilerplate's fresh-worktree lesson, applied
   generically). Confirmed `python3 -m pcrecbench testees` lists
   `rust-default` and the driver builds clean (`cargo build --release
   --locked`, 6.69s) with `cargo`/`rustc` resolving via the `~/.cargo/bin`
   fallback (not directly on `$PATH`). The adapter's own `describe()` call
   was exercised directly (not just `cargo build`) to confirm the harness
   path, not only the raw toolchain.
2. **Predictions authored and committed** (`04cee1d`, BEFORE any
   measurement): `docs/dev/predictions/capability-0.1-rust-first.tsv`, 3
   parents / 5 clauses, grounded in the r1131 witness census
   (`docs/dev/measurements/2026-09-19-rust-capability-census-r1131.txt`),
   `testees/rust/CLAUDE.md`'s semantic findings, and a direct read of
   `bench/capability/expectations.tsv` for `high-byte-run`'s two
   should-match subjects. Verified it loads cleanly through
   `interpret.load_predictions` before committing. `docs/dev/predictions/
   CLAUDE.md` gained its entry in the same commit, including the
   DELIBERATELY DROPPED did-not-compile-exhaustiveness clause and why (see
   below).
3. **Quiet gate + the window.** `python3 -m pcrecbench quiet --samples 5`:
   VERDICT quiet (load1 0.09-0.13, max_busy_pct 1.0-2.81%). Box also
   independently confirmed idle via `uptime`/`ps` and pcrec's own battery
   trailer (`BATTERY DONE rc=0 2026-09-19T15:34:36-04:00`, well before this
   launch at 17:33). Launched `scripts/run_window.sh` under `setsid
   gnutimeout 5400` with `SUBBENCH=capability TESTEES=rust-default
   TRIALS=5 STORE=store`, detached with a durable log marker, per the
   script's own required launch shape.
4. **A genuine duplicate-launch incident, caught and fixed.** The first
   launch attempt's shell output appeared to fail (an empty `$LOGFILE`
   echo from a subshell-expansion quirk in the compound command), so a
   second launch was issued. Both had in fact started. Caught within
   seconds by `ps aux` + `/proc/<pid>/cwd` + `/proc/<pid>/environ`
   inspection: the FIRST launch (log `...173348Z.log`) was already past
   its own quiet gate and compiling all 64 patterns; the SECOND (log
   `...173401Z.log`) read the first one's CPU usage on the target core
   (53.01%) and correctly self-refused as NOT QUIET, sitting in its own
   12-attempt retry backoff with no python child running yet. Killed the
   second's process tree (`sleep`, `gnutimeout`, `bash`) by VERIFIED PID
   and cwd (both matched this worktree) — never `pkill -f`. Zero records
   written by the killed duplicate; the stray empty log file was removed.
   This is exactly the "duplicate window" hazard the box-sharing rules
   exist for, caught and fixed within the same minute it occurred, not
   discovered after the fact.
5. **The wait.** Armed a `Bash run_in_background` until-loop polling the
   log for `WINDOW_RUN_COMPLETE` rather than a bare `setsid …disown`
   (which the boilerplate states will NEVER notify) — but the notification
   did not reach a live turn before ~30 minutes had passed with no
   further action taken; see "What went wrong" below.
6. **Foreground finish**, on the team lead's direct instruction after the
   idle gap: verified `WINDOW_RUN_COMPLETE cells=1/1` directly from the
   log, confirmed the one new index row and its `status: measured`,
   generated the four report surfaces + matrix siblings, cross-checked
   the matrix's compile-outcome census against the census file's raw
   numbers (finding the `unsup`-vs-`refused` split, a real finding — see
   below), ran `interpret --render --predictions` and read the anchor
   line and per-clause verdicts DIRECTLY from the rendered sidecar and
   the TSV (not narrated from memory), determinism-checked the sidecar
   (second independent render, byte-identical diff), wrote `reports/
   CLAUDE.md`'s entry, committed everything, wrote this report.

## What went wrong, stated plainly

Between arming the background wait (~17:49 window completion) and the
team lead's message (~30+ minutes later), no foreground action was taken
to check the marker directly — the turn ended on "I'll continue once
that notification arrives" without a fallback check. The boilerplate's
own rule ("Before sending ANY idle notification... run the check for its
marker and quote the result inline") was not followed here: nothing was
sent, but nothing was checked either, for the whole gap. The team lead's
message named this as "the known lane failure mode from last night" —
consistent with the boilerplate's own b13pre precedent it documents. The
actual measurement was UNAFFECTED (the window itself completed cleanly
at 17:49:18 EDT, attempt 1, rc=0, no re-measurement needed) — this is a
process/monitoring gap, not a data-quality one.

## Per-cell status

One cell: `capability@0.1 × rust-default`. Attempt 1, rc=0,
`WINDOW_RUN_COMPLETE cells=1/1`. Record status `measured`, agreement
`agree (0 of 82 groups; 0 of 3194 rows; 4 unjudged; k=1.5, 2/3; 5
trials)`. Store index: 181 records total (170 measured / 9
inconclusive-load / 2 inconclusive-spread, store-wide — not just this
window's own record).

## Anchor-identity line (quoted verbatim from the sidecar)

> **Predictions anchor (§6.5, r7code-1).** ... `capability@0.1`: anchor
> 2026-09-19T21:34:23Z, over 1 (testee_id, machine_id) tuple(s) this
> report includes.

This is the record's own write timestamp — the first-ever measurement of
`rust-default` on this set — safely after the predictions file's
`stated_utc` of `2026-09-19T21:32:08Z`. Confirms `--testee rust-default`
as the report's sole roster member was the right call: any second,
already-measured testee in the roster would have pulled its own older
history into this same anchor key and refused the file.

## Scored clause verdicts

**3 confirmed / 0 refuted / 0 not-evaluable** (of 3 parents, 5 clauses):

- **P1** (`high-byte-run`, `n_wrong eq 10`) — confirmed. Measured
  `n_wrong = 10` exactly (2 of 75 subjects wrong × 5 trials): the crate's
  default Unicode mode reads `[\x80-\xff]` as a Unicode-scalar-value
  class matched against its UTF-8 encoding, not the raw byte, so neither
  `nu-high-byte` (two raw bytes, no valid decode) nor `nu-lead-with-cont`
  (one valid codepoint, short of the pattern's `{2,4}` repeat minimum)
  can produce the required 2-4 consecutive in-range codepoints — both
  read NOMATCH against the oracle's byte-level MATCH.
- **P2.a/.b/.c** (`file-ext-order`/`keyword-prefix-order`/
  `router-prefix-order`, `n_wrong eq 0` each) — confirmed. rust-regex's
  hardcoded `MatchKind::LeftmostFirst` agrees with the oracle's own
  convention on all three.
- **P3** (`evil-alt-nested`, `n_wrong gt 0`) — confirmed at `n_wrong =
  10`. The same family-10 non-backtracking-automaton shape
  `capability-0.1-ext-roster.tsv`'s P9.a documents `re2-default`
  independently wrong on; can only render as `n_wrong` (never
  `n_gave_up`) per this driver's structural no-giveup-code guarantee.

## A genuine finding beyond the predictions file

The matrix surface's compile-outcome census (22 `unsup` + 1 `refused` +
2 `wrong` + 39 clean) does not decompose the same way as the raw r1131
census's "42 compiled / 22 refused" split, because the harness's
pre-compile capability policy (`pcrecbench/capability.py`) intercepts
patterns the raw driver-only census never reaches. This 22-vs-22 overlap
was NOT re-derived to the exact pattern-name level (flagged in `reports/
CLAUDE.md`'s entry as owed to the next reader who wants the set
difference) — a genuine, stated gap, not silently glossed.

## Charter-vs-committed checklist

| item | status |
|---|---|
| worktree bootstrap + generators before first run | COMPLETE |
| predictions file authored and committed BEFORE the run | COMPLETE (`04cee1d`) |
| quiet gate verified | COMPLETE (`quiet` CLI + independent `uptime`/battery-trailer check) |
| window launched detached, cell measured | COMPLETE (1/1, attempt 1, rc=0) |
| duplicate-launch hazard caught and fixed | COMPLETE (verified-PID kill, zero contamination) |
| index (store count stated) | COMPLETE (181 records; 170/9/2 by status) |
| report group: four surfaces + matrix siblings | COMPLETE (.md/.tsv/.subject-grain.tsv/.matrix.tsv/.matrix.html) |
| interpretation sidecar with --predictions | COMPLETE (3/3 confirmed, anchor line quoted above) |
| sidecar determinism check | COMPLETE (second render, byte-identical) |
| lane report | COMPLETE (this file) |
| exact refused-set overlap (raw census vs. harness unsup/refused split) | OWED — flagged in `reports/CLAUDE.md`'s entry, not blocking, no clause depends on it |
| ~30-min monitoring gap after the window finished | NAMED ABOVE, not hidden; no data-quality consequence |

## Not done, and why

No `docs/dev/plan.md` / `dev_journal.md` entry was written — the brief
named specific report deliverables and did not ask for a plan-row update;
left for the manager's review pass, consistent with "the manager reviews/
merges in the morning."
