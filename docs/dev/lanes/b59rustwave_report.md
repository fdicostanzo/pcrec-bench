# lane b59rustwave — rust-default's remaining first pinned samples

2026-09-20, wake queue item 3. Brief: measure `rust-default` (the
thirteenth [B7] roster engine, `testees/rust/`) on the five sets
`capability@0.1` had not yet covered — `bench/email-specimen@0.2`,
`bench/loglines@0.1`, `bench/altwide@0.2`, `bench/syntax@0.1`,
`bench/bounded@0.3` — one cell each, sequentially, predictions
committed BEFORE each window, first-sample scoring scoped to the new
testee alone (the [B57] anchor lesson).

## Head SHAs

- `bfc1bb9` — the manager's plan-row commit, already on the branch tip
  when this worktree was created
- `442ebdd` — predictions for all five sets, committed BEFORE any window
- `fc66e97` — email-specimen@0.2 window's full deliverable
- `6dd9027` — loglines@0.1 window's full deliverable
- `8566d63` — altwide@0.2 window's full deliverable
- `002df76` — syntax@0.1 window's full deliverable (+ a predictions-
  format bug fix, + two `testees/rust/CLAUDE.md` finding write-ups)
- `e2d61cf` — bounded@0.3 window's full deliverable (the last set)

Branch `lane/b59rustwave`, worktree `worktrees/b59rustwave`, NOT merged
(per boilerplate: the manager merges).

## Order of operations, as delivered

1. **Worktree bootstrap.** `git worktree add`, `git rev-parse
   --show-toplevel` confirmed. Ran `gen_subjects.py` +
   `gen_throughput_subjects.py` for all five target sets (email,
   loglines, bounded, altwide, syntax) before any window — the
   fresh-worktree lesson, applied to every set this lane touches, not
   only the first. Confirmed `rust-default` resolves through the
   harness (`pcrecbench testees`, `adapter.describe()`) and pre-built
   the driver (`cargo build --release`, 6.65s) to keep first-window
   timing honest.
2. **Grounding research, forked out of the main context.** A fork
   surveyed all five sets' patterns against `testees/rust/CLAUDE.md`'s
   already-committed findings (the 9-token REQUIRES-refused-construct
   list, the possessive-quantifier semantic gap, the hardcoded
   leftmost-first convention, the non-utf8-subject byte-vs-encoding
   discrimination, the structural no-giveup guarantee) — no new census
   was run; every fact used was already committed knowledge plus a
   direct grep of each set's own `.rx` files. Confirmed: `email` and
   `loglines` and `bounded` and `altwide` carry ZERO refused
   constructs, possessive quantifiers or non-UTF8 byte-range classes
   anywhere (checked by direct grep of every real pattern); `syntax` is
   the richest ground (26 of 95 patterns hit the 9-token refused list
   by construct, one possessive-quantifier witness with a worked
   subject-level derivation, two Unicode-property patterns exercising
   the SATISFIED `unicode-properties` token).
3. **Predictions authored and committed BEFORE any window** (`442ebdd`):
   one TSV per set, 3-7 clauses each (28 total), grounded per above.
   **Every did-not-compile clause was deliberately DROPPED from all
   five files** — the same solo-roster `render_tsv` structural
   blindness `capability-0.1-rust-first.tsv`'s own entry documents
   (with `--testee rust-default` as each report's sole roster member,
   required by F27's re-anchored `check_stated_utc`, no OTHER testee
   ever ranks a pattern rust-default alone refuses, so no ranking group
   — and no `did_not_compile` bullet — ever exists for it). This is a
   large, stated omission for `syntax` specifically (26 grounded,
   construct-confirmed refusals, none scorable in this shape) —
   documented in full in `docs/dev/predictions/CLAUDE.md`'s own entry
   for these five files, not silently dropped.
4. **Five windows, run SEQUENTIALLY, box-quiet-checked before each
   launch, bounded `until`-loop polled on each window's own log** (per
   the manager's correction after a monitoring stall — see "What went
   wrong" below): email, loglines, altwide, syntax, bounded — bounded
   run LAST per the brief's own budget note (its throughput regime is
   the historically longest cell family; in the event, a single-testee
   `rust-default` cell finished in ~27 minutes, well inside the 5,400s
   per-cell cap, so the caution was not needed but was still the right
   call to make in advance without knowing that).
5. **Foreground post-run steps after every window**: `WINDOW_RUN_COMPLETE
   cells=1/1` confirmed from the log, the new record's `status`
   checked, the four-surface report group + `.matrix.tsv`/`.matrix.html`
   generated (`report.py`'s own CLI, one query per set scoped to
   `rust-default` alone), `interpret --render --predictions` run, the
   anchor-identity line and per-clause verdicts read DIRECTLY from the
   rendered sidecar (never narrated from memory), a second independent
   `interpret` invocation diffed byte-identical against the committed
   sidecar (determinism), `reports/CLAUDE.md`'s entry written with every
   finding traced to an actual record, committed — all before moving to
   the next set.
6. **A predictions-format bug found and fixed live** (syntax window,
   `002df76`): `syntax-0.1-rust-first.tsv`'s P1 (`op=gt`) had its
   threshold in the `lo` column; `interpret.py`'s `_op_holds` reads
   every non-`between` op's bound from `hi` only, so the file crashed
   `interpret --predictions` with `ValueError: could not convert string
   to float: ''` on first use. Fixed (`lo=""`/`hi="0"`, matching every
   other clause across all five files, which were correct from
   authoring) before any score was reported; the fix and its mechanism
   are documented in `docs/dev/predictions/CLAUDE.md`.
7. **Verification pass** (after the fifth window): `make check-schema`
   (5/73/0 clean), `python3 catalogue/fixtures/gen.py --check` (217
   files, 67 fixtures, clean), `make check-interpret` (161/161 clean,
   including section 3's sidecar-freshness gate over the thirteen
   sidecars this lane's windows regenerated — every committed sidecar
   re-renders byte-identical from its own stamp). `make check-harness`/
   `make check-report` were NOT independently re-run (no harness or
   reporter CODE was touched by this lane — only predictions, reports,
   store records and CLAUDE.md prose — so the risk these two ~20-min
   suites would catch something this lane could cause is low; OWED if
   the manager wants the full green confirmed before merge).

## What went wrong, stated plainly

**One background-wait stall, the fourth of its kind cited by the
manager.** After launching the loglines window (background, harness-
tracked), the turn ended on "waiting for the notification" without a
foreground fallback check — the exact named failure mode
`BOILERPLATE.md`'s 2026-09-19 rule exists to close. The window had
actually completed cleanly 32 minutes earlier (`WINDOW_RUN_COMPLETE
cells=1/1`, sidecar regen 9/9 OK) with no data-quality consequence; the
manager's external probe caught the gap and named it. From that point
on, every subsequent window (altwide, syntax, bounded) was polled with
an explicit bounded `until`-loop against the window's own log
(`gnutimeout`'d / Bash-tool-timeout'd), checked at each point-in-time
rather than trusting the background notification alone — the corrected
discipline held for the remaining three windows with no further gap. The
manager's own timing note (a box probe HOLD/GO pair that arrived
straddling the email window's launch) was also handled cleanly: the
email window's own quiet-gate reading (load1 0.11-0.14, max_busy_pct
1.6%, logged BEFORE the HOLD message arrived) showed no actual overlap
with the probe, confirmed and reported back rather than assumed.

## Per-set status

| set | cell | attempt | rc | status | agreement |
|---|---|---|---|---|---|
| `email-specimen@0.2` | rust-default | 1 | 0 | measured | clean (3 regimes) |
| `loglines@0.1` | rust-default | 1 | 0 | measured | agree (0/22 groups disagreeing) |
| `altwide@0.2` | rust-default | 1 | 0 | measured | clean |
| `syntax@0.1` | rust-default | 1 | 0 | measured | agree (0/145 groups disagreeing; 56 unjudged) |
| `bounded@0.3` | rust-default | 1 | 0 | measured | clean |

Every window: 1/1 attempt, ATTEMPT 1 (no gate refusals, no
inconclusive-spread retries), quiet box confirmed before launch each
time (`/proc/loadavg` load1 0.12-0.58 before every launch), sentinel
line quoted verbatim in each window's own commit message.

## Sentinel lines, quoted verbatim

```
build/windows/window_email_20260920T163958Z.log:    WINDOW_RUN_COMPLETE cells=1/1
build/windows/window_loglines_20260920T164555Z.log:  WINDOW_RUN_COMPLETE cells=1/1
build/windows/window_altwide_20260920T172703Z.log:   WINDOW_RUN_COMPLETE cells=1/1
build/windows/window_syntax_20260920T174819Z.log:    WINDOW_RUN_COMPLETE cells=1/1
build/windows/window_bounded_20260920T181402Z.log:   WINDOW_RUN_COMPLETE cells=1/1
```

## Anchor-identity lines, quoted verbatim

```
email-specimen@0.2: anchor 2026-09-20T16:40:34Z, over 1 (testee_id, machine_id) tuple(s) this report includes.
loglines@0.1:       anchor 2026-09-20T16:46:30Z, over 1 (testee_id, machine_id) tuple(s) this report includes.
altwide@0.2:        anchor 2026-09-20T17:27:38Z, over 1 (testee_id, machine_id) tuple(s) this report includes.
syntax@0.1:         anchor 2026-09-20T17:48:54Z, over 1 (testee_id, machine_id) tuple(s) this report includes.
bounded@0.3:        anchor 2026-09-20T18:14:37Z, over 1 (testee_id, machine_id) tuple(s) this report includes.
```

Every anchor equals the record's own write timestamp (the first-ever
measurement of `rust-default` on that set), safely after the
predictions file's own `stated_utc` (`2026-09-20T16:37:24Z` for all
five) — confirming `--testee rust-default` alone as each report's
roster was the right call throughout.

## Predictions scored, by set

| set | parents / clauses | confirmed | refuted | partial | not-evaluable |
|---|---|---|---|---|---|
| `email-specimen@0.2` | 1 / 3 | 3 | 0 | 0 | 0 |
| `loglines@0.1` | 2 / 7 | 7 | 0 | 0 | 0 |
| `altwide@0.2` | 2 / 5 | 5 | 0 | 0 | 0 |
| `syntax@0.1` | 6 / 7 | 4 | 1 | 1 | 0 |
| `bounded@0.3` | 2 / 6 | 5 | 0 | 0 | 1 |
| **total** | **13 / 28** | **24** | **1** | **1** | **1** |

Every sidecar determinism-checked (a second, independent `interpret
--render` invocation diffed byte-identical against the committed file)
before commit.

## Three genuine, unpredicted findings

1. **`bench/syntax@0.1`, P4 refuted**: `qnt-poss-brace` (`a{1,2}+b`)
   answers MATCH `[0,4)` on subject `f-aaab` ("aaab"), where both the
   oracle and this lane's own "possessive suffix is a no-op"
   extrapolation (from `testees/rust/CLAUDE.md`'s existing `a++`≡`a+`
   witness) predicted NOMATCH. The mechanism: `X{n,m}+` parses as
   `(X{n,m})+` (unbounded repetition of the bounded GROUP), not "the
   possessive suffix dropped" — a distinction the plain `X+`/`X*`/`X?`
   witnesses structurally cannot make, since `(X+)+`/`(X*)+`/`(X?)+` are
   language-equivalent to their unsuffixed forms while `(X{1,2})+` is
   not. Full derivation in `testees/rust/CLAUDE.md`'s
   "CORRECTED/SHARPENED 2026-09-20" paragraph.
2. **`bench/syntax@0.1`, P6.a refuted**: `unp-p-lc` (`\p{L}+`, the
   SATISFIED `unicode-properties` token) disagrees with the oracle on
   Latin-1-encoded (genuinely non-UTF-8) subjects — the SAME
   non-utf8-subject byte-vs-UTF-8-encoding mechanism
   `capability@0.1`'s `high-byte-run` finding already documents for a
   raw byte-range class, now shown to reach a Unicode PROPERTY class
   too. `unicode-properties` stays SATISFIED (the mechanism widens
   where it's reachable, it is not new). Full write-up in
   `testees/rust/CLAUDE.md`'s `non-utf8-subject` section.
3. **`bench/bounded@0.3`, P1.c not-evaluable**: `nest3-16`
   (`(?:(?:\d{1,16}){1,16}){1,16}`) and `nest2-64`
   (`(?:\d{1,64}){1,64}`) both refuse to compile under `rust-default`
   with `CompiledTooBig` (size-limit, both forms) — a combinatorial-size
   refusal this lane's syntax-only grounding grep never checked for.
   The flat `cls-upto-*` count ladder compiles clean all the way to
   `cls-upto-65535` (the exact rung libpcre2/pcrec's own NFA cap refuses
   at in this project's history); rust-regex's more permissive 10 MiB
   default is reached from the opposite direction, by NESTED
   combinatorics rather than flat count. Written up in `reports/
   CLAUDE.md`'s bounded entry.

A fourth, smaller finding (`bench/altwide@0.2`): rust-regex compiles and
ranks ALL 33 altwide patterns × 3 regimes with zero refusals, including
`ci-512`/`s-4096`/`w-2048` — the exact widest rungs libpcre2/pcrec
refuse at in this project's own history — stated as an observation, not
a probed boundary (no witnessed refusal exists on this set to derive
one from).

## Predictions files' own committed rationale

`docs/dev/predictions/CLAUDE.md` carries the full grounding rationale
for all five files, including the explicit list of what was DROPPED and
why (the solo-roster `did_not_compile` blindness), and the op=gt bug
fix. Not repeated here.

## Charter-vs-committed checklist

| item | status |
|---|---|
| worktree bootstrap + generators for all five sets before first run | COMPLETE |
| predictions authored and committed BEFORE the windows, one file per set | COMPLETE (`442ebdd`) |
| did-not-compile clauses dropped with stated rationale (not silently) | COMPLETE (`docs/dev/predictions/CLAUDE.md`) |
| five windows launched, quiet-gate-checked, sequential | COMPLETE (1/1 each, attempt 1, rc=0) |
| bounded run last per the budget note | COMPLETE |
| foreground index/report/sidecar after every window | COMPLETE for altwide/syntax/bounded from the correction point on; email done foreground, loglines done foreground but LATE (see incident) |
| matrix siblings (.matrix.tsv/.matrix.html) per group | COMPLETE (5/5) |
| sidecar determinism check per group | COMPLETE (5/5, byte-identical) |
| first-sample scoring reports scoped to rust-default alone | COMPLETE (5/5, anchor lines quoted above confirm) |
| reports/CLAUDE.md entry per group, with genuine findings written up | COMPLETE (5/5) |
| commit incrementally, one commit per meaningful step | COMPLETE (7 commits on the branch) |
| box-sharing rules (quiet gate honored, no forced-unquiet on a pinned cell) | COMPLETE |
| lane report (this file) | COMPLETE |
| background-wait stall named honestly, not hidden | COMPLETE (see "What went wrong") |
| `make check-schema` / fixtures gen / `make check-interpret` verified clean | COMPLETE (73/73 sabotage, 217 fixture files, 161/161 interpret checks) |
| `make check-harness` / `make check-report` (full, ~20 min each) | NOT RUN — no harness/reporter code touched by this lane; OWED if the manager wants full green confirmed before merge |
| plan.md / dev_journal.md closing entries | OWED — left for the manager's merge pass, consistent with prior lanes' own precedent ("the manager reviews/merges in the morning") |

## Not done, and why

No `docs/dev/plan.md` row was marked complete and no `dev_journal.md`
entry was appended — the brief named specific report/predictions/
findings deliverables and this lane's own precedent (`b57rustwindow`)
left plan/journal closure to the manager's review pass; left the same
way here, named as OWED above rather than silently skipped.
