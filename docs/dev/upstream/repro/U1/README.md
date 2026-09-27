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
