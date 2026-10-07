# U14 repro — libpcre2 auto-possessification is not aware of `(?R)`
whole-pattern recursion, and the wrong answer it gives is not merely
"the optimization skips backtracking" — the optimization is
documented to never change which strings match.

**What it shows.** `pcre2_compile()`'s auto-possessification pass
turns a greedy iterator into a possessive one wherever it can prove
the optimization can never change the result (the one it applies, for
example, to turn `a+b` into `a++b`). For the pattern
`/(?:b(?R)a|a+)/` — a top-level non-capturing group whose second
branch is a bare `a+`, and whose first branch recursively re-enters
the WHOLE PATTERN via `(?R)` — the pass possessifies that top-level
`a+` without noticing that the pattern contains a recursion that can
re-enter that exact position with a different continuation than "end
of pattern". The result is a genuinely different match, not merely a
suppressed backtrack:

| subject | default (10.46/10.49) | `PCRE2_NO_AUTO_POSSESS` |
|---|---|---|
| `baa`   | `(1,3)` = `"aa"`   | `(0,3)` = `"baa"`   |
| `bbaaa` | `(2,5)` = `"aaa"`  | `(0,5)` = `"bbaaa"` |
| `baaa`  | `(1,4)` = `"aaa"`  | `(0,4)` = `"baaa"`  |

A **second, independent witness** agrees with the `NO_AUTO_POSSESS`
answer: Perl (5.40.1, which PCRE2 aims to be compatible with and which
supports the identical `(?R)` recursion syntax) matches `baa`/`bbaaa`/
`baaa` against the unanchored `/(?:b(?R)a|a+)/` as `(0,3)`/`(0,5)`/
`(0,4)` — the un-possessified answer, not PCRE2's default one.

**Why this is a bug, not a documented semantics difference** (checked
against the docs before filing, per this project's own rule): `man
pcre2api`'s description of `PCRE2_NO_AUTO_POSSESS` says the option
"disables ... an optimization that ... turns `a+b` into `a++b` in
order to avoid backtracks into `a+` **that can never be successful**".
That is the documented contract of auto-possessification everywhere it
is described: it is only supposed to prune paths that were always
going to fail. Here the pruned path is NOT always going to fail — full
backtracking recovers a real match the possessified form loses. An
optimization that changes which strings match is not what either the
option's documentation or its ordinary English name ("auto-
possessification", not "partial backtracking removal") describes.

**This is not a new class of bug for this subsystem.** PCRE2's own
ChangeLog documents the *identical* mechanism already fixed once, for
a narrower case: 10.31 (2018), item 31, fixing Bugzilla #2232 —
*"Auto-possessification at the end of a capturing group was dependent
on what follows the group ... but this caused incorrect behaviour when
the group was called recursively from elsewhere in the pattern where
something different might follow. ... Iterators at the ends of
capturing groups are no longer considered for auto-possessification if
the pattern contains any recursions."* That fix is visible and
working today: `^(b(?1)a|a+)$` (the same shape, but recursing into a
**numbered, capturing** group via `(?1)` rather than the whole pattern
via `(?R)`) answers `(0,3)` identically under both options — the 10.31
fix holds for this case.

**The gap: `(?R)` recurses into the whole pattern, which has no
enclosing "capturing group" at all**, so the 10.31 fix's guard never
applies to it. Confirmed by reading `src/pcre2_auto_possess.c`
directly (10.46 and 10.49 — the two files diff as byte-identical in
this region modulo comment/fallthrough-annotation reformatting, so the
bug is unmoved between the installed version and the latest release):

```c
    case OP_END:
    return base_list[1] != 0;          /* <-- no cb->had_recurse check */

    case OP_KET:
    case OP_KETRPOS:
    if (base_list[1] == 0) return FALSE;
    bracode = code - GET(code, 1);
    switch(*bracode)
      {
      case OP_CBRA:
      case OP_SCBRA:
      case OP_CBRAPOS:
      case OP_SCBRAPOS:
      if (cb->had_recurse) return FALSE;   /* <-- the 10.31 fix, capturing-group-only */
      break;
      ...
```

`OP_END` is reached (per the code's own preceding comment, "We can
always possessify a greedy iterator at the end of the pattern, which
is reached after skipping over the final `OP_KET`") exactly when the
"what follows this iterator" walk runs off the end of the compiled
program — which is where a **non-capturing** group `(?:...)` at the
top level lands, and where `(?R)`'s own call site re-enters (`(?R)` is
textually and operationally "recurse into the program from its
start", with no numbered/named bracket of its own to carry a
`had_recurse`-gated flag). The `OP_KET`/`OP_KETRPOS` branch's fix
checks `had_recurse` only for the four CAPTURING bracket opcodes
(`OP_CBRA`/`OP_SCBRA`/`OP_CBRAPOS`/`OP_SCBRAPOS`); the `OP_END` branch
has no equivalent check at all, so the possessification still fires
whenever the pattern recurses through `(?R)`/`(?0)` rather than through
a numbered/named group call.

**Engine + version.** libpcre2 10.46 (2025-08-27, the Ubuntu
`libpcre2-8-0`/`pcre2-utils` 10.46-1build1 system package) and, as the
"is this still present on the latest release" check, libpcre2 10.49
(2026-09-28, the current GitHub release), built from the official
release tarball with `./configure --disable-shared --enable-jit && make
pcre2test` (a 2-3 minute build, no special dependencies beyond a C
compiler). Both reproduce identically; the relevant source region of
`pcre2_auto_possess.c` is unchanged between them.

**Build/run.** `run.sh` needs only a `pcre2test` binary on `$PATH` (no
compilation needed against the system package):

    UPSTREAM_SCRATCH=/tmp/scratch bash run.sh

To point it at a different build (the latest-release check above):

    UPSTREAM_ENGINE_BUILD=/path/to/pcre2test UPSTREAM_SCRATCH=/tmp/scratch bash run.sh

**Expected PRESENT output.** `run.sh` prints a labeled trace of all
four `pcre2test` runs to stderr and one final line to stdout:

    U14 PRESENT pcre2 <version> <evidence>

`expected.txt` is a captured PRESENT run against the system libpcre2
10.46, box ubuntubudu, 2026-10-07.

**What ABSENT (fixed) looks like.** The default-vs-`no_auto_possess`
match reports for `(?:b(?R)a|a+)` would agree (the `(?R)` recursion
case would stop being possessified, matching the already-fixed
numbered-group case) — `run.sh` exits 1 and prints
`U14 ABSENT pcre2 <version> <evidence>` in that case.

**CANNOT-RUN.** No `pcre2test` binary found on `$PATH` (or at
`$UPSTREAM_ENGINE_BUILD` if set) — exits 2, prints
`U14 CANNOT-RUN pcre2 - -` or `U14 CANNOT-RUN pcre2 unknown -`.

**Does this matter for pcrec-bench itself?** No measured stakes: see
`docs/dev/measurements/2026-10-07-recursion-auto-possess-oracle-probe.txt`
— a prior probe ran libpcre2 10.46's default vs `NO_AUTO_POSSESS` over
every committed expectation row (1,097 rows) of this bench's twelve
subroutine/recursion-call patterns and found zero answer flips; none
of this bench's own `(?R)`/`(?N)` patterns happen to have a top-level
quantifier whose only lexical follow is the pattern's own end, the
shape this finding needs. This note exists purely as a correctness
report to the upstream maintainer, not because the bench's own
rankings are at risk.
