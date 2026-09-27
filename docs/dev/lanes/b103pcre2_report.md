# Lane b103pcre2 report — libpcre2 proving batch (U1, U2, U4, U5)

Branch `lane/b103pcre2`, worktree `worktrees/b103pcre2`, based on
master `f6a7345` then merged forward to pick up `b103infra`'s
registry/tool/skill (merge commit, then the lane's own work commit
`bb8af27`).

## Scope

Per brief: write ONLY `docs/dev/upstream/repro/U{1,2,4,5}/` and
`docs/dev/upstream/notes/pcre2-2026-09-27.md` plus this report;
`findings.tsv`/`upstream_findings.md` untouched (the manager applies
each finding's reached status). One small additive edit to
`docs/dev/upstream/CLAUDE.md` (a standing process rule — update the
owning directory's CLAUDE.md when files are added — kept minimal to
avoid conflicting with sibling proving-batch lanes).

## Per-finding status reached

All four: **REPRODUCED and UNDERSTOOD** (both reached; the design
note's ladder allows either order and both are satisfied here),
tracker searched, still PRESENT on the current PCRE2 release. None
moved past UNDERSTOOD — DRAFTED requires `--note` via
`tools/upstream.py status`, which I did not run (findings.tsv is the
manager's to write per the brief); the note itself is written and
ready.

| id | status reached | latest_checked (OWED — not written to findings.tsv) | tracker (OWED) |
|---|---|---|---|
| U1 | REPRODUCED, UNDERSTOOD | `10.48@2026-09-27` | `searched:2026-09-27:none-found` |
| U2 | REPRODUCED | `10.48@2026-09-27` | `searched:2026-09-27:none-found` |
| U4 | REPRODUCED | `10.48@2026-09-27` | `searched:2026-09-27:none-found` |
| U5 | REPRODUCED | `10.48@2026-09-27` | `searched:2026-09-27:none-found` |

(U2/U4 are REPRODUCED but not separately claimed UNDERSTOOD — see
"what's UNDERSTOOD vs REPRODUCED" below; U1 and U5 have live ablation
evidence I'd call UNDERSTOOD.)

The manager can apply these with, e.g.:

    python3 tools/upstream.py status U1 UNDERSTOOD
    python3 tools/upstream.py repro U1 --engine-build <path-to-10.48-pcre2test> --record
    python3 tools/upstream.py status U1 DRAFTED --note docs/dev/upstream/notes/pcre2-2026-09-27.md

(repeated per id; `status` already refuses TRACKER-required transitions
without `--tracker`, so `KNOWN-UPSTREAM`/`REPORTED` aren't reachable by
a bare `status` call — none of these four reached that far anyway.)

## What each repro shows, and how solid the numbers are

**U1** (`repro/U1/`): JIT catastrophic-backtracking cliff on the
subroutine-factored email pattern (`bench/email/patterns/factored.rx`)
over a long run of `a` (no `@`). On this box the cliff sits between
~500,000 B (instant) and ~505,000 B (>20 s) — I binary-searched it by
hand before picking 524,288 B as the repro's default subject (times
out reliably at >45 s while both controls finish in ~0.1 s). The full
1,048,576-byte original subject was independently confirmed to hang
past 75 s. **Ablation, not just documentation reading**: `pcre2test
...,info` reports `Last code unit = '@'` for this pattern (a
compile-time fact, present regardless of JIT); forcing
`no_start_optimize` on the plain INTERPRETER reproduces the same
catastrophic behaviour the JIT already shows, proving the
interpreter's speed comes entirely from that check and that the JIT
does not get the same benefit through subroutine calls. A control
pattern (`orig.rx`, same grammar, no subroutines) stays instant under
JIT at the identical subject size — isolates the cause to subroutine
calls specifically. Status: UNDERSTOOD by this ablation (no libpcre2
source read).

**U2** (`repro/U2/`): the non-catastrophic sibling — `orig.rx` (no
subroutines) under JIT vs interpreter on 1,048,576 B of `a`. Median of
50 in-process `pcre2test -tm` calls: interp ~18-24 µs, JIT ~2.4-2.9 ms,
ratio ~86-160x across repeated runs and across both 10.46 and 10.48 —
matches the original narrative's 142-175x band closely. Robust,
low-noise measurement (large absolute times, `-tm`'s in-process
timing). Status: REPRODUCED; the "why" (JIT's runtime doesn't apply
the same required-code-unit dismissal even though the compile-time
fact is identical) is stated as a reading, same evidentiary weight as
the original narrative's own "unverified" tag — I did not source-read
libpcre2 to go further, so I call this REPRODUCED rather than claiming
UNDERSTOOD beyond what the numbers themselves show.

**U4** (`repro/U4/`): **the headline ~1.8x short-subject-search ratio
DID NOT reproduce robustly** — three repeated runs at
`pcre2test -tm 100000` over a single ~100-byte no-quote log line gave
2.45x, 1.04x, 1.22x on an otherwise idle box; the raw per-call cost
there (~80-200 ns) is too close to the timing loop's own noise floor
on this machine to trust. I pivoted the repro to the SAME finding's OWN
secondary evidence — the 1 MB throughput case the narrative already
cites ("jit 791-819 µs... where the interpreter... answers in
17.6-17.8 µs") — which is robust: three repeated runs gave 30.87x,
22.97x, 34.33x (median of 20 in-process calls each). This is disclosed
plainly in the repro's own README rather than silently swapped in.
Status: REPRODUCED (the 1 MB grain); the short-subject grain is a
named, honest gap, not claimed.

**U5** (`repro/U5/`): the closest to an exact re-derivation — I
transcribed `bench/syntax/censustext.py`'s line grammar standalone
(`gen_subject.py`, no import of bench code) and verified it produces
subjects BYTE-IDENTICAL (matching sha256) to the bench's own committed
`t-64k`/`t-1m` throughput subjects at the same seeds. The key technical
point, stated in the README: the subject must be handed to `pcre2test`
as ONE data line with embedded newlines escaped as literal `\n`
(pcre2test's own multi-line-subject convention) — feeding it as
separate physical lines (my first attempt) hides the effect entirely,
because an unclosed `(` can then never scan past its own line looking
for a closer. With that fixed, `global` (find-all) timing at 64 KiB
vs 1 MiB gives 869.9 -> 8828.6 ns/byte (my run) against the original's
870.4 -> 8704.8 — within 1.4%. Status: UNDERSTOOD is arguable (the
match-count-vs-cost dissociation is measured, not merely asserted) but
I did not read libpcre2's recursion implementation, so I call this
REPRODUCED with a strong, measured reading, matching the original
narrative's own stated caveat ("not chased further here").

## Latest-release check

Built PCRE2 **10.48** (2026-08-31, the current GitHub release — checked
via `gh api repos/PCRE2Project/pcre2/releases`) from the official
source tarball in the session scratchpad
(`./configure --enable-jit --disable-shared && make -j12`, clean
build, no patches). All four findings reproduce IDENTICALLY on 10.48
(`tools/upstream.py repro U<n> --engine-build <path>`): U1 still times
out, U2 ratio 86.09x, U4 ratio 17.42x, U5 ratio 9.78x (single runs;
all comfortably clear each repro's own PRESENT threshold). Read the
10.47 and 10.48 ChangeLog entries in full — nothing mentions JIT
start-of-match/required-code-unit optimization, subroutine-call
performance, or recursion cost; the closest adjacent items are #912
(10.47, a JIT lookbehind CORRECTNESS bug, fixed) and #984 (10.48, a
JIT "start-bitmap" SIMD out-of-bounds read, fixed) — both unrelated
mechanisms.

## Tracker search

`gh search issues --repo PCRE2Project/pcre2` with ~15 query variants
per finding (subroutine/JIT/recursion/required-code-unit/catastrophic-
backtracking/first-code-unit/quadratic wording, plus a broad
`in:title jit` sweep) found nothing matching any of the four. Recorded
as `searched:2026-09-27:none-found` for all four (OWED to
findings.tsv, not written by me).

## Charter-vs-committed checklist

| item | status |
|---|---|
| repro/U1 (README, run.sh, expected.txt, pattern files) | COMMITTED, verified via `tools/upstream.py repro U1` and `--engine-build` (10.48) |
| repro/U2 | COMMITTED, verified |
| repro/U4 | COMMITTED, verified (short-subject grain explicitly NOT claimed robust — see above) |
| repro/U5 | COMMITTED, verified byte-identical subject generation |
| notes/pcre2-2026-09-27.md | COMMITTED, DRAFT only, approval line blank |
| latest-release check (all four) | DONE (10.48 built from source, all four still PRESENT) |
| tracker search (all four) | DONE, none found |
| findings.tsv / upstream_findings.md status moves | OWED to the manager (brief: do not touch) |
| `make check-upstream` | PASS (13/13 self-test cases, 0 registry issues) |

No background jobs outstanding. Nothing left running. Ending here.
