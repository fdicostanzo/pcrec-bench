# U2 repro — libpcre2 JIT lacks the interpreter's whole-subject
required-code-unit dismissal

**What it shows.** On a pattern whose compiled form has a known
required ("last") code unit (here `@`, from the RFC 5322 address-spec
grammar `bench/email/patterns/orig.rx`, no subroutine calls — see U1's
repro for the subroutine-calling sibling, whose gap is catastrophic
rather than a fixed multiplier), matching a 1 MB subject that never
contains that byte is ~150-175× SLOWER via the JIT-compiled matcher
than via the plain interpreter, though both correctly answer "no
match" and both routes' cost is linear in the subject length (this is
NOT a hang — see U1 for that). The interpreter's cost (~18 µs total,
~0.017 ns/byte) is consistent with one `memchr`-class scan that never
finds `@` and gives up; the JIT's cost (~2.4-3.2 ms, ~2.5-3 ns/byte) is
consistent with a genuine byte-by-byte scan attempt at every position,
without the interpreter's single up-front dismissal.

**Engine + version.** libpcre2 10.46 (2025-08-27), `pcre2_jit_compile`
vs plain `pcre2_compile`+`pcre2_match`. System `pcre2test`
(`libpcre2-8-0`/`pcre2-utils` 10.46-1build1), the same version
pcrec-bench's own `pcre2-jit`/`pcre2-interp` testees link.

**Build/run.**

    UPSTREAM_SCRATCH=/tmp/scratch bash run.sh

Generates one 1,048,576-byte subject (the byte `a`, repeated) into
`$UPSTREAM_SCRATCH`, then runs `pcre2test -tm 50` (50 repeated match
calls, in-process, no per-call startup cost) once with the `jit`
modifier and once without, and reports the MEDIAN "Match time" each
way. `$UPSTREAM_ENGINE_BUILD` points the same run at a different
`pcre2test` binary (the latest-release check).

**Pattern file**: `pattern_orig.txt`, verbatim from
`bench/email/patterns/orig.rx`. `pcre2test ...,info` on this pattern
reports `Last code unit = '@'` — a compile-time fact available
identically to both the interpreter and the JIT-compiled matcher; the
finding is that only the interpreter's runtime actually exploits it at
this speed.

**Expected PRESENT output.** stdout's final line:

    U2 PRESENT pcre2 <version> <ratio>x

where `<ratio>` is the JIT:interpreter median-match-time ratio.
`expected.txt` is a captured PRESENT run (ratio 159.28x) against
system libpcre2 10.46, box ubuntubudu, 2026-09-27 — within the
142-175× band pcrec-bench's own `email-specimen@0.2` records reported
across several distinct 1 MB no-`@` subjects (2026-08-28,
`docs/dev/upstream_findings.md` §U2).

**What ABSENT (fixed) looks like.** The ratio drops toward ~1× (the
JIT would need to apply the same required-code-unit-absent dismissal
the interpreter does). `run.sh` exits 1 and prints
`U2 ABSENT pcre2 <version> <ratio>x` when the ratio is under 20 —
comfortably below anything observed here and comfortably above what a
noise-only difference between two engine routes would show.

**CANNOT-RUN.** No `pcre2test` binary found (on `$PATH` or at
`$UPSTREAM_ENGINE_BUILD`) — exit 2. A `-tm` run that produces no
"Match time" line at all (an unexpected pcre2test build) also reports
CANNOT-RUN rather than a false ABSENT/PRESENT.
