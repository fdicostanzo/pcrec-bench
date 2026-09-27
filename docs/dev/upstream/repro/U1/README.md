# U1 repro — libpcre2 JIT catastrophic-backtracking cliff on a
subroutine-factored email pattern

**What it shows.** `pcre2_jit_compile()`'s compiled matcher takes
dramatically longer than `pcre2_match()`'s plain interpreter on a
pattern that uses PCRE2 subroutine calls (`(?&name)`), over a subject
made entirely of a byte that can never match (no `@` in a pattern that
requires one). The interpreter answers in well under a millisecond
(it uses the compiled pattern's own "last code unit" fact, `@`, to
dismiss the subject in one linear scan); the JIT does not get the same
benefit once the pattern reaches its literal body through subroutine
calls, and instead performs real per-start-position backtracking. Cost
grows so fast with subject length that it crosses from "instant" to
"tens of seconds" between roughly 500,000 and 505,000 bytes on this
box — the ORIGINAL observation (pcrec-bench's own bench/email set,
2026-08-25) used a 1,048,576-byte subject and reported a 60-second
per-subject timeout; this repro uses a 524,288-byte (512 KiB) subject
by default so a maintainer's run finishes in under a minute either
way.

**Engine + version.** libpcre2 10.46 (2025-08-27), specifically
`pcre2_jit_compile(PCRE2_JIT_COMPLETE)` + `pcre2_match()` (JIT-compiled
patterns are still called through `pcre2_match()`; see man pcre2jit).
Tested via the system `pcre2test` (Debian/Ubuntu package
`libpcre2-8-0`/`pcre2-utils` 10.46-1build1), the same version
pcrec-bench's own `pcre2-jit`/`pcre2-interp` testees link
(`testees/pcre2/CLAUDE.md`).

**Build/run.** `run.sh` needs only a `pcre2test` binary linked against
libpcre2 with JIT support (`pcre2test -C jit` reports `1`) — no
compilation of anything is needed against the system package. It
writes one generated subject into `$UPSTREAM_SCRATCH` (a 512 KiB file
of the byte `a`) and runs three `pcre2test` invocations:

    UPSTREAM_SCRATCH=/tmp/scratch bash run.sh

To point it at a different `pcre2test` build (e.g. a fresh release
tarball build, for the "does this still reproduce" check):

    UPSTREAM_ENGINE_BUILD=/path/to/pcre2test UPSTREAM_SCRATCH=/tmp/scratch bash run.sh

To reproduce the FULL, exact original observation (1,048,576-byte
subject, ~60-90s hang) rather than the faster 512 KiB default, edit the
`N=524288` line in `run.sh` to `N=1048576`; this was confirmed to
reproduce on this box (a 75-second budget was enough to see the
timeout fire) but is left out of the default run to keep a maintainer's
first pass under a minute.

**Pattern files** (verbatim from pcrec-bench's `bench/email/patterns/`,
its own hand-authored RFC 5322 address-spec regex in two spellings):
`pattern_factored.txt` (uses `(?&atom)`/`(?&label)`/`(?&qchar)`/`(?&octet)`
subroutine calls onto four `{0}`-guarded definition groups) and
`pattern_orig.txt` (the same grammar HAND-INLINED, no subroutine calls
at all — the control that shows the cliff is specific to subroutine
use, not to the grammar itself).

**Mechanism, confirmed by ablation** (not merely read from
documentation): `pcre2test ...,info` on `pattern_factored.txt` reports
`Last code unit = '@'` — this compile-time fact is available
regardless of whether the pattern is later JIT-compiled. Turning the
interpreter's own use of it off (`no_start_optimize`) makes the
INTERPRETER just as catastrophic on the identical subject as the JIT
already is (both then fail to finish in the same run.sh timeout budget
that the plain interpreter clears in ~0.1 s) — proving the
interpreter's speed comes entirely from that check, and that the JIT's
matcher does not get the same benefit for this pattern shape. The
`pattern_orig.txt` control (same grammar, no subroutines) stays instant
under JIT at the same subject size, isolating the cause to subroutine
calls specifically, not to "this pattern" in general.

**Is this a resource-limit artifact, or genuine cost? (manager review
2026-09-27, item 2 — ruled out, not assumed.)** `run.sh` itself now
runs a STACK-LIMIT ABLATION: the JIT case at a fixed, smaller subject
(N=501,000 B, already inside the cliff, ~4 s by default) at two very
different `jitstack` sizes, 1 KiB and 65536 KiB (man pcre2test
"Setting the JIT stack size"; this IS the resource U5's OWN finding —
a different pattern, a different mechanism — genuinely runs out of,
`PCRE2_ERROR_JIT_STACKLIMIT`/error -46, see `repro/U5/README.md`).
Here, on THIS pattern, both sizes return the identical clean "No
match" (rc 0) in statistically the same ~4.1 seconds — no error code
of any kind on either side of the threshold, at any subject size
tested (up to the full 1,048,576-byte original observation). This
rules out a JIT-stack cause specifically, and more generally: neither
side of the ~500,000-byte threshold ever returns
`PCRE2_ERROR_MATCHLIMIT`/`_DEPTHLIMIT`/`_JIT_STACKLIMIT` or any other
documented resource-cap error — both sides return an honest, complete
"No match". The cost is real computation, not a silently-capped
one.

**What we did NOT fully characterize**: the exact closed-form growth
law. Fine-grained timing in a narrow band (jitstack irrelevant,
default settings, single core) —

| N (bytes) | elapsed (s) |
|---|---|
| 500,200 | 0.81 |
| 500,500 | 2.03 |
| 500,800 | 3.24 |
| 501,000 | 4.06 |
| 501,300 | 5.27 |
| 501,600 | 6.52 |
| 502,000 | 8.16 |

— is well-approximated LOCALLY by an arithmetic (linear) rate of
roughly 4 ms per additional byte in this narrow 1,800-byte band, a
very large per-byte constant once past the threshold. That LOCAL rate
does not, however, extrapolate globally: a straight line from this
slope would predict well over half an hour at the full 1,048,576-byte
subject, where the actual measured time is ~75-90 seconds — so the
growth rate itself must be changing (moderating) further out, and we
did not identify why. A `pcre2test find_limits` characterization
(which reports the minimum match/depth limit PCRE2's own accounting
would need) was attempted and abandoned: it re-runs the match many
times to bisect the limit, and at this subject's already-large
per-attempt cost that search does not complete in a reasonable time
either. **What we can state confidently: this is not a resource-limit
artifact, and its growth is dramatically steeper than the ~O(n)
required-code-unit-scan cost U2/U4 describe on the same/similar
patterns — but the exact algorithmic shape driving specifically the
~500,000-byte threshold and the rate beyond it was not identified from
source.**

**Why this stays reportable (unlike U5, which the SAME manager review
reclassified NOT-A-BUG for a different pattern).** The interpreter, BY
DEFAULT, entirely avoids this cost class for this exact subject —
its "last code unit" check is a genuine, effective, O(1)-ish dismissal
that only the JIT's compiled matcher fails to apply once the pattern's
body is reached through subroutine calls. This is not "any backtracking
engine would be slow on this input" (U5's shape, confirmed on a THIRD,
independent engine, Oniguruma, in `repro/U5/`) — it is specifically
that ONE EXECUTION ROUTE of the SAME LIBRARY does not use an
optimization the OTHER ROUTE already computes and already uses.

**Expected PRESENT output.** `run.sh` prints one diagnostic block to
stderr (elapsed times for the two controls and the JIT-on-`factored`
case) and one final line to stdout:

    U1 PRESENT pcre2 <version> <timeoutNNs|elapsed-seconds>

`expected.txt` is a captured PRESENT run against system libpcre2
10.46, box ubuntubudu, 2026-09-27.

**What ABSENT (fixed) looks like.** The third (`factored.rx`, jit)
timing finishes in well under 2 seconds (like the two controls,
each ~0.1 s here) instead of timing out — i.e. the JIT-compiled
matcher would have to apply the same "last code unit" dismissal the
interpreter does, even through subroutine calls. `run.sh` exits 1 and
prints `U1 ABSENT pcre2 <version> <elapsed-seconds>` in that case.

**CANNOT-RUN.** No `pcre2test` binary found on `$PATH` (or at
`$UPSTREAM_ENGINE_BUILD` if set) — exits 2, prints
`U1 CANNOT-RUN pcre2 - -` or `U1 CANNOT-RUN pcre2 unknown -`.
