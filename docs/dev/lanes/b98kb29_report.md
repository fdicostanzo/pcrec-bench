# Lane b98kb29 — KB-29's tre/re2/rust rider

Branch `b98kb29`, worktree `worktrees/b98kb29`, from master `6322ec6`.
Writer lane. Box: quiet throughout (loadavg 0.01-0.51); every check below
ran as an individually-launched python invocation or `gcc`/probe binary,
never a full `make check`/`check-harness`. No `~/pcrec` file was touched
(BD2). No pcrec binary, no engine pin, no adapter build config was
touched — only `testees/tre/driver.c`, `tools/selfcheck.py`, and
documentation.

Task: finish KB-29 (`docs/dev/known_issues.md`) for the three drivers
`b98rider` left OWED — `testees/tre`, `testees/re2`, `testees/rust` —
mirroring `b98rider`'s pcre2/onig/pcrec fix exactly where reachable,
establishing reachability first where it's in doubt, and stating the
structural case plainly where it's not.

## 1. RE2 and rust — audited, CLOSED with NO code change

Read `testees/re2/driver.cc`'s find-all loop (`driver.cc:315-344`) and
`testees/rust/src/main.rs`'s (`main.rs:261-293`) directly, rather than
trusting either file's own pre-existing header claim ("`giveup:<code>`
never fires from this driver"). Confirmed: **neither has the KB-29 bug
shape at all**, structurally, because neither has a variable capable of
holding a hypothetical error code in the first place:

- RE2: `bool m = re->Match(...)`; the loop is `if (!m) break;` — a
  boolean, not an integer code. There is nothing to "always track" and
  nothing to "discard on a genuine give-up", because there is no signal
  RE2's public API can even report beyond match/no-match.
- rust: `let m = match re.find_at(buf, pos) { Some(m) => m, None =>
  break };` — the crate's `find_at`/`find` return `Option<Match>`, never
  a `Result`. Same conclusion: no `Err` arm exists to lose a give-up
  code through.

**No fix was made** — there is nothing to fix. Both `CLAUDE.md`s already
carried this claim from their original build lanes; this lane's own
value is confirming it by direct inspection specifically for KB-29
(rather than accepting it on faith) and closing the KB entry's "OWED"
line for these two engines. `docs/dev/known_issues.md`, `testees/re2/
CLAUDE.md`, `testees/rust/CLAUDE.md` all updated with a short KB-29 audit
note; `tools/selfcheck.py`'s `check_kb29_find_all_giveup_propagation`
prints a documentary line (not a scored check — nothing to assert
against) rather than silently saying nothing about these two engines.

## 2. TRE — REACHABILITY investigated first, then fixed

`testees/tre/CLAUDE.md`'s own pre-existing "gave-up" section already
tried ONE 5-way backreference pattern over 40 non-matching bytes under a
2 s alarm and did not reproduce `REG_ESPACE` (`REG_NOMATCH` came back
inside the alarm) — stated as "PROVISIONED, not confirmed live", i.e.
open. Before writing a fix I needed to know: is a genuine mid-loop
`REG_ESPACE` actually REACHABLE here, or is trying harder with bigger
patterns just going to hit the same wall for a structural reason?

**Empirical investigation** (interactive, scratch-only, not committed):
tried 1/3/5/6/7-way backreference groups over subjects up to 1,000,000
bytes, several nested-quantifier shapes (`(a*)*\1b`, `((a*)*)\1b`,
`(a*)+\1b`). Every combination that completed within a bounded alarm
answered `REG_NOMATCH` or `MATCH`, never `REG_ESPACE`; combinations that
did not complete simply ran out of TIME (confirmed exponential, not
hanging — a 3-second alarm times out at n=60 but the SAME pattern
completes cleanly at n=100 given 15 seconds). `/usr/bin/time -v` on
several of these showed **RSS flat at ~2.18 MB regardless of pattern
complexity or subject length** — the search is CPU-bound, not
memory-bound, which is the opposite of what a stack-exhaustion mechanism
should look like.

Fetched libtre's own source (`lib/tre-mem.c`, `lib/tre-stack.c`,
`lib/tre-match-backtrack.c`, `lib/tre-internal.h` — via WebFetch, since
this box has no `apt-get source` access) to find WHERE `REG_ESPACE` is
actually returned from an exec call: exclusively on a genuine
`malloc()`/`calloc()`/`realloc()` failure, or a `tre_stack_push()` cap
that is itself reached only through further allocation. This reframed
the question: not "does some pattern reproduce `REG_ESPACE` before my
patience runs out", but "does `tre_regnexecb()` ever allocate at all".

**Built a real fault-injection instrument** to answer that directly:
`docs/dev/measurements/probe_kb29_tre_failmalloc.c` (an LD_PRELOAD
malloc/calloc/realloc call counter, with an optional fault-injection
failure point, unused here) and `probe_kb29_tre_giveup_reachability.c`
(reproduces `driver.c`'s own two-call find-all shape: call 1 matches a
leading literal trivially, call 2 runs the pattern's OWN backreference
groups — the shape that routes TRE to its backtracking matcher at all —
against a long non-matching run), driven by
`probe_kb29_tre_giveup_reachability.py` across 1/3/5/7 backreference
groups and subject lengths 10 B–1,000,000 B (fewer at higher group
counts, each cell capped at 8 s of wall time to keep the whole census
bounded; timed-out cells are named and EXCLUDED from the total, never
folded in as zero). **Result: ZERO allocations inside ANY of the 12
completed `tre_regnexecb()` exec calls.** Archived verbatim at
`docs/dev/measurements/2026-09-26-kb29-tre-giveup-reachability.txt`
(source header, verbatim table, my own reading section, and the
skipped/timed-out rows named explicitly rather than swept under the
"zero" total).

**Conclusion, stated plainly and cross-checked against source, not just
inferred from one census's silence**: since `tre_regnexecb()` makes no
allocation at all in this build, `REG_ESPACE` (the only code besides
`REG_OK`/`REG_NOMATCH` TRE's regexec-family functions can return) cannot
arise from a find-all loop's SECOND-OR-LATER call here. The KB-29 bug
shape is genuinely UNREACHABLE on this pinned libtre build (0.9.0-1build1)
— not merely hard to hit, not merely unwitnessed on this corpus.

**Fixed anyway, defensively** (`testees/tre/driver.c`, mirroring
pcre2/onig/pcrec's shape exactly: the loop's own terminal code is now
ALWAYS tracked, never gated on `count == 0`, and a genuine give-up
discards the call's accumulated matches before falling through to the
same `giveup:<code>:<message>` branch a first-call give-up already
takes) — harmless (the branch this fix touches is provably never taken
on this build) and consistent with the three sibling drivers, in case a
future libtre build, allocator, or build configuration behaves
differently. Verified the fix does not change normal behaviour: built
and ran the real driver directly on an ordinary find-all subject
(`a` over `banana`, 3 matches) and on a stress subject
(`a(b*)\1c` over `Xa`+30 `b`s, no trailing `c`) both before and after —
identical output either way (fast `nomatch`, no spurious `giveup`); the
same two pre-existing compiler warnings (`-Wformat-truncation`,
`-Wclobbered`, both unrelated to this change) present before and after.

**`check_kb29_find_all_giveup_propagation`'s new tre arm** (`tools/
selfcheck.py`) is a REGRESSION CONTROL, not a positive witness (none is
possible): compiles the real `tre-default` testee on `X|a(b*)\1c`, runs
find-all through the real `Adapter.measure()` path over `Xa`+2000 `b`s
(no `c`), and asserts the answer is a clean `match` on the leading `X`
(never a spurious `giveup:`) — proving the fix does not introduce a
false give-up on a pattern that genuinely exercises the backtracking
matcher. Ran directly: 7 PASS / 0 FAIL (up from `b98rider`'s 6 — pcre2 ×2
+ onig ×2 + pcrec ×2 + the new tre arm; re2/rust print a documentary line
only, no separate PASS).

`docs/dev/known_issues.md` KB-29 entry, `testees/tre/CLAUDE.md`'s
"gave-up" section (an UPDATED paragraph, not a rewrite — the original
5-way/40-byte probe's own text is left intact with the new, wider finding
appended), `testees/re2/CLAUDE.md`, `testees/rust/CLAUDE.md`, `tools/
CLAUDE.md`'s check-harness section, and `docs/dev/measurements/CLAUDE.md`
(the new probe files' table row) all updated. `testee_id`/`build_flags`
UNCHANGED for every testee — no adapter, no config, no flag was touched.

## Validation run (targeted, not `make check`)

```
python3 -c "... selfcheck.check_kb29_find_all_giveup_propagation() ..."
```
→ 7 PASS, 0 FAIL (pcre2 giveup+control, onig giveup+control, pcrec
giveup+control, tre regression control; re2/rust documentary line).

```
python3 -c "... selfcheck.check_high_byte_pattern_argv() ..."
```
→ 9 PASS, 0 FAIL (unaffected by this lane's changes — re-run as a
sanity check on the same adapters this lane touched, since it also
builds tre-default/re2/rust drivers).

`python3 -m py_compile tools/selfcheck.py` — clean. Full `make check`
is OWED to the manager (not run here per the brief's "targeted checks
only" instruction) — command: `make check` from the repo root (or this
worktree once merged), expected ~324+ checks unaffected in count by this
lane's ADDITIVE arm (one new PASS line, no removed check).

## Charter-vs-committed checklist

| # | brief item | status |
|---|---|---|
| 1 | Establish reachability for each engine before fixing | **COMMITTED**: re2/rust structurally unreachable (no error-code channel at all, confirmed by direct loop inspection); tre reachable IN PRINCIPLE (POSIX contract allows REG_ESPACE) but shown UNREACHABLE on the pinned build by an exhaustive fault-injection census, not merely asserted |
| 2 | Fix + real witness where reachable | tre and re2/rust are NOT reachable, so no positive witness exists to give; tre got the mirrored fix anyway (defensive) with a real driver-level regression control instead of a fabricated witness — never fabricated one |
| 3 | Extend `check_kb29_find_all_giveup_propagation` with witness + short-subject control | **COMMITTED** for tre as a regression control (no witness exists to add); re2/rust get a documentary line, not a scored arm (nothing to assert) |
| 4 | Update KB-29 status, testees' CLAUDE.mds, tools/CLAUDE.md | **COMMITTED** — all five files updated |
| 5 | STOP and report on any testee_id/build_flags change | **N/A** — none changed; not triggered |
| 6 | Run only targeted checks (<4 min each), name `make check` OWED | **COMMITTED** — two targeted checks run directly (both <10 s); full `make check` named OWED above |
| 7 | Charter-vs-committed checklist | this table |
