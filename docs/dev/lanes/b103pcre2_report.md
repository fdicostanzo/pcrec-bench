# Lane b103pcre2 report — libpcre2 proving batch (U1, U2, U4, U5)

Branch `lane/b103pcre2`, worktree `worktrees/b103pcre2`, based on
master `f6a7345` then merged forward to pick up `b103infra`'s
registry/tool/skill. Commits: `bb8af27` (first delivery), `5b5a392`
(first report), plus this round's fix-wave commit(s) addressing the
manager's three change requests below.

## Scope

Per brief: write ONLY `docs/dev/upstream/repro/U{1,2,4,5}/` and
`docs/dev/upstream/notes/pcre2-2026-09-27.md` plus this report;
`findings.tsv`/`upstream_findings.md` untouched (the manager applies
each finding's reached status). One small additive edit to
`docs/dev/upstream/CLAUDE.md` (a standing process rule).

## Manager's three change requests — what changed and what it found

**(1) U5 may be inherent to the pattern, not an interpreter defect.**
Confirmed exactly as the manager's hypothesis predicted, with a
stronger evidence base than asked for. `repro/U5/run.sh` now runs a
FOUR-WAY ablation every time: {interpreter, JIT} x {ORIGINAL subject
(unbalanced parens present), CONTROL subject (same seed/RNG stream,
unbalanced tails suppressed via a new `gen_subject.py` parameter)}.
Result: BOTH engines are flat (ratio ~0.7-0.9x, well inside the "still
linear" band) on the balanced-only control, and BOTH are super-linear
(interp 9.2-9.3x, JIT 12.45x for a 16x size step) on the original.
JIT needed `jitstack` raised from its 32 KiB default to 65536 KiB to
even COMPLETE the same work the interpreter does — at the default it
aborts partway through with a real, correctly-reported
`PCRE2_ERROR_JIT_STACKLIMIT` (error -46), a genuinely different
resource-limit event from anything in U1 (see below). As a THIRD,
independent cross-check (part (c) of the ask, done because it was
cheap — headers/lib already on the box): a from-scratch Oniguruma
6.9.10 probe (`onig_probe.c`, its own find-all loop, no shared code
with pcre2test or this project's harness) shows the SAME shape,
control flat (0.42x), original super-linear (1.76x — milder than
libpcre2's, but unambiguously above flat). **Conclusion, stated in
`repro/U5/README.md`: NOT-A-BUG — pattern-inherent backtracking cost
(an unclosed `(` forces any backtracker to scan to the subject's end
before failing).** U5 is REMOVED from `notes/pcre2-2026-09-27.md`
entirely; the note now covers only U1/U2/U4. This is OWED to
findings.tsv as `status U5 NOT-A-BUG` (I did not write it, per the
standing brief).

**(2) U1's cliff — checked for a resource threshold, found none.**
`repro/U1/run.sh` now runs an embedded ablation at a fixed, smaller
subject (N=501,000 B, ~4s by default) at `jitstack=1` KiB vs
`jitstack=65536` KiB (64 MiB): BOTH give the identical clean "No
match" (rc 0, no error of any kind) in statistically the same ~4.1
seconds. This is a genuinely different outcome from U5's mechanism
(where jitstack size determines how much work completes before a real
error) — for U1, jitstack is provably irrelevant, and no PCRE2 error
code (`MATCHLIMIT`/`DEPTHLIMIT`/`JIT_STACKLIMIT`) fires on either side
of the ~500,000-byte threshold at any subject size tested, including
the full 1,048,576-byte original observation (75-90s, still a clean
"No match", never a timeout-that-was-really-an-error). What flips at
the threshold: nothing discrete that we could find — `repro/U1/README.md`
now carries a fine-grained timing table (500,200 B → 0.81s through
502,000 B → 8.16s) showing a steep, LOCALLY near-linear growth (~4 ms
per additional byte in that narrow band) that does NOT extrapolate
globally (a straight line from that slope would predict >30 minutes
at 1,048,576 B; the actual measured time is 75-90s), so the growth
rate itself changes further out — stated as an honest, unresolved gap
rather than papered over (a `find_limits` characterization was
attempted and abandoned: it re-runs the match many times to bisect a
limit, and at this per-attempt cost that bisection itself does not
finish in reasonable time). **U1 stays REPORTABLE** (unlike U5): the
interpreter, by default, entirely avoids this cost class via a real,
effective optimization (`Last code unit = '@'`) that the JIT's
compiled matcher does not apply once the pattern reaches its body
through subroutine calls — this is ONE execution route of the SAME
library failing to use an optimization the OTHER route already
computes and uses, not "any backtracker would be slow here" (U5's
shape, now independently ruled out on a second engine).

**(3) The note must be self-sufficient.** `notes/pcre2-2026-09-27.md`
is rewritten: every finding now inlines its exact pattern text, a
copy-pasteable one-line subject generator (`python3 -c "print(...)"`),
the exact `pcre2test` input-building commands (with the correct
delimiter for each pattern — U1/U2 use `,` since both patterns contain
`/`; U4 uses `~` since ITS pattern also contains a literal `/`, in
`HTTP/1` — an error in the first draft, caught and fixed by literally
re-running every command in the note verbatim before finalizing), and
the measured numbers. Nothing says "available on request" any more.
Every command block in the note was RE-RUN verbatim in a scratch
directory as part of this fix wave to confirm it reproduces the quoted
numbers (U1: timeout as expected; U2: 2825.6/22.8 µs, ratio ~124x; U4:
560.1/18.4 µs, ratio ~30x; the jitstack side-by-side: 4.55s/4.71s).

## Per-finding status reached (updated)

| id | status reached | classification | latest_checked (OWED) | tracker (OWED) |
|---|---|---|---|---|
| U1 | REPRODUCED, UNDERSTOOD | reportable (JIT-specific optimization gap) | `10.48@2026-09-27` | `searched:2026-09-27:none-found` |
| U2 | REPRODUCED | reportable | `10.48@2026-09-27` | `searched:2026-09-27:none-found` |
| U4 | REPRODUCED | reportable (1 MiB grain robust; short-subject grain named as a gap) | `10.48@2026-09-27` | `searched:2026-09-27:none-found` |
| U5 | REPRODUCED | **NOT-A-BUG** (pattern-inherent, confirmed on 2 engines + JIT-with-raised-stack) | `10.48@2026-09-27` | `searched:2026-09-27:none-found` |

The manager can apply these with, e.g.:

    python3 tools/upstream.py status U1 UNDERSTOOD
    python3 tools/upstream.py repro U1 --engine-build <path-to-10.48-pcre2test> --record
    python3 tools/upstream.py status U1 DRAFTED --note docs/dev/upstream/notes/pcre2-2026-09-27.md
    python3 tools/upstream.py status U5 NOT-A-BUG

(repeated per id for U2/U4; U5 gets ONLY the `NOT-A-BUG` line, no
`--note`, since it is deliberately excluded from the note.)

## Latest-release check (unchanged from first delivery, still valid)

PCRE2 **10.48** (2026-08-31, current release) built from the official
source tarball, `./configure --enable-jit --disable-shared && make`.
All four (including U5, on its own merits) still reproduce identically
on 10.48. ChangeLog read in full for 10.47/10.48; nothing matches any
of the four mechanisms.

## Tracker search (unchanged)

`gh search issues --repo PCRE2Project/pcre2`, ~15 query variants per
finding plus a broad `in:title jit` sweep — nothing found for any of
the four.

## Charter-vs-committed checklist

| item | status |
|---|---|
| repro/U1 (README, run.sh incl. jitstack ablation, expected.txt) | COMMITTED, re-verified |
| repro/U2 | COMMITTED, re-verified |
| repro/U4 | COMMITTED, re-verified |
| repro/U5 (README, run.sh incl. 4-way ablation, gen_subject.py, onig_probe.c, expected.txt) | COMMITTED, re-verified — reclassified NOT-A-BUG |
| notes/pcre2-2026-09-27.md (U1/U2/U4 only, self-sufficient, every command re-run) | COMMITTED, DRAFT only, approval line blank |
| U1 jitstack ablation (manager item 2) | DONE, embedded in run.sh, no resource-limit cause found |
| U5 control-subject + JIT + Oniguruma ablation (manager item 1) | DONE, all three point the same way |
| latest-release check (all four) | DONE (10.48, all four still reproduce) |
| tracker search (all four) | DONE, none found |
| findings.tsv / upstream_findings.md status moves (incl. U5 NOT-A-BUG) | OWED to the manager (brief: do not touch) |
| `make check-upstream` | PASS (13/13 self-test cases, 0 registry issues) |

No background jobs outstanding. Nothing left running. Ending here.
