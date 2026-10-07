# lane u18up report — U14, libpcre2 `(?R)` auto-possessification correctness finding

**Task**: run the upstream-findings pipeline's File → Reproduce → Triage →
Draft steps for one new libpcre2 CORRECTNESS finding: PCRE2 10.46's
auto-possessification is not call-aware for whole-pattern recursion
`(?R)` — a finding Frank asked be reported upstream (pcrec inbox I-133,
[B124]; pcrec's own `docs/dev/upstream_issues.md` U18 at pin
`60366d74`). Do not send/post/comment anywhere; tracker/changelog
searches (read-only `gh` GETs / web) are fine.

**Branch**: `lane/u18up`, `worktrees/u18up`. WIP commits throughout.

## What was done

1. **File**: `tools/upstream.py new --engine pcre2 --kind correctness
   --summary "..."` allocated **U14** (the pipeline's own next id — the
   bench's registry and pcrec's own "U18" numbering are independent
   sequences over different sets of findings; this note cites pcrec's
   U18 as the source, not as this registry's id).

2. **Reproduce**: confirmed the inbox's three stated subjects on the
   system libpcre2 10.46 (`pcre2test`) *before* writing anything —
   `(?:b(?R)a|a+)` on `baa`/`bbaaa`/`baaa` gives `(1,3)`/`(2,5)`/`(1,4)`
   by default and `(0,3)`/`(0,5)`/`(0,4)` under
   `PCRE2_NO_AUTO_POSSESS`, exactly as I-133 states, and the numbered-
   group control `^(b(?1)a|a+)$` gives `(0,3)` under both options.
   Wrote `docs/dev/upstream/repro/U14/{README.md,run.sh,expected.txt}`
   (standalone — `pcre2test` only, no bench code, no store access);
   `run.sh` runs all four cases and exits PRESENT iff the `(?R)` form
   disagrees across the two options AND the numbered-group control
   agrees (the structural signature that isolates this from recursion
   divergence in general). `tools/upstream.py repro U14` → PRESENT;
   `status U14 REPRODUCED`.

3. **A second independent witness beyond the charter's ask**: Perl
   5.40.1 (`perl -E`) on the same unanchored pattern agrees with the
   `NO_AUTO_POSSESS`/sound answer on all three subjects (`(0,3)`/
   `(0,5)`/`(0,4)`), not with PCRE2's default — recorded in both the
   README and the narrative.

4. **UNDERSTOOD, from source, not just behaviour**: fetched
   `src/pcre2_auto_possess.c` at the installed version (10.46) and the
   latest GitHub release (10.49, 2026-09-28) and diffed them —
   byte-identical in the relevant region (modulo comment/fallthrough-
   annotation reformatting). Found the root cause directly: the
   `OP_KET`/`OP_KETRPOS` case (closing bracket of a bracketed group)
   checks `cb->had_recurse` only for the four CAPTURING-bracket opcodes
   (`OP_CBRA`/`OP_SCBRA`/`OP_CBRAPOS`/`OP_SCBRAPOS`) — the fix PCRE2
   shipped in 10.31 (2018, ChangeLog item 31, Bugzilla #2232) for
   exactly this class of bug, but scoped to capturing-group recursion
   (`(?1)`/`(?&name)`). The `OP_END` case (reached when the iterator's
   "what follows" walk runs off the end of the compiled program — where
   a top-level non-capturing group lands, and where `(?R)` re-enters,
   since it recurses into the whole pattern with no enclosing bracket
   of its own) has **no equivalent check at all** — confirmed by
   reading the code (quoted in both the README and the narrative) and
   by `git log -- src/pcre2_auto_possess.c` on the real
   PCRE2Project/pcre2 clone showing nothing has touched this path since
   (the only later recursion/auto-possess-adjacent fixes, `1415565`/
   `0820852`, are about variable-length lookbehinds, a different code
   path). `status U14 UNDERSTOOD`.

5. **Triage — latest release**: built libpcre2 **10.49** (2026-09-28,
   current GitHub release) from the official tarball,
   `./configure --disable-shared --enable-jit && make pcre2test`
   (~2-3 minutes, gcc + autotools only, no extra deps). Ran the repro
   against it directly and via `tools/upstream.py repro U14
   --engine-build .../pcre2test --record`: **PRESENT, identical to
   10.46** — not STALE, not FIXED. `latest_checked` =
   `10.49@2026-10-07`.

6. **Triage — tracker search**: `gh search issues --repo
   PCRE2Project/pcre2` across several term sets (`possessif`,
   `recursion`, `auto-possess`, `NO_AUTO_POSSESS`, `(?R)`, `2232`,
   `wrong answer recursion`), open and closed. The two candidates that
   surfaced on a `recursion` search (#367 "Another recursion
   inconsistency corner case", #334 "Incorrect fix for `(?0)` with
   endanchored") were read in full and are about a DIFFERENT mechanism
   (the nested-recursion-loop detector's `-52` error / fuzzer
   equivalence checking), not auto-possessification correctness.
   Nothing covers this finding. `tracker` = `searched:2026-10-07:
   none-found`.

7. **Draft**: `docs/dev/upstream/notes/pcre2-2026-10-07.md` — one
   finding (U14), written for the maintainer (no bench jargon, the
   minimal case inline, the `OP_END`-vs-`OP_KET` source citation, the
   10.31/#2232 precedent, Perl as the second witness, box + method),
   approval line blank. `status U14 DRAFTED --note
   docs/dev/upstream/notes/pcre2-2026-10-07.md`.

8. **Narrative**: `docs/dev/upstream_findings.md`'s `## U14` section
   filled in (was a stub from `new`) with the source (I-133, pcrec's
   U18, the no-stakes oracle probe), the finding, the bug-vs-semantics
   check, the 10.31 precedent and the `OP_END` gap, the triage results,
   and the current status.

9. **`findings.tsv`** row filled in by hand (the fields `tools/
   upstream.py new`/`status` don't set): `engine_version 10.46`,
   `route -` (the bug is in `pcre2_compile()`'s auto-possess pass,
   before the interp/JIT/DFA split — not route-specific), `evidence`
   (I-133, pcrec's U18 citation via `git -C ~/pcrec show
   refs/pins/i133:...`, the oracle probe), `tracker
   searched:2026-10-07:none-found`.

Nothing was sent, posted, commented or opened anywhere — every `gh`
call used was a read-only `search`/`issue view`. No status beyond
DRAFTED was set (APPROVED/REPORTED need Frank's word, per the hard
rule).

## make check-upstream

Green: `test_upstream.py` 23/23 self-test cases, then
`check-upstream: OK -- 14 finding(s), 2 thread(s), 0 issues` over the
real registry (13 pre-existing + U14).

`make check-schema` was also run (unrelated to this lane's scope, but
free and fast) and is unaffected: `6 example(s) accepted, 74
sabotage(s) rejected for the intended rule, 0 sabotage(s) WRONG`. The
harness/report/interpret gates were not run — this lane touches only
`docs/dev/upstream/` + `docs/dev/upstream_findings.md`, which neither
gate reads.

## Charter-vs-committed checklist (session_discipline.md §7(c))

| Charter item | Status |
|---|---|
| File a new libpcre2 correctness finding via `tools/upstream.py new` | **COMPLETE** — U14 |
| Reproduce in `repro/U14/` (README, run.sh, expected.txt), standalone | **COMPLETE** — verified PRESENT on 10.46; `run.sh` exits 0/1/2 per spec |
| `repro U14` → REPRODUCED | **COMPLETE** |
| Move to UNDERSTOOD if source reading confirms cause, citing lines | **COMPLETE** — `pcre2_auto_possess.c`'s `OP_END` vs `OP_KET`/capturing-bracket `had_recurse` check, both 10.46 and 10.49, `git log` checked for later fixes |
| Check documented semantics before calling it a bug (NO_AUTO_POSSESS, recursion-processing docs) | **COMPLETE** — `man pcre2api`/`man pcre2pattern` quoted; Perl run as a second witness |
| Triage: find latest release, build if modest, `repro --engine-build PATH --record` | **COMPLETE** — 10.49 built and run, PRESENT, `latest_checked` recorded |
| Search tracker/changelog for an existing report | **COMPLETE** — `searched:2026-10-07:none-found`, two near-miss issues read and ruled unrelated |
| Draft `notes/pcre2-2026-10-07.md`, self-contained, blank approval line | **COMPLETE** |
| `status U14 DRAFTED --note ...` | **COMPLETE** |
| `make check-upstream` green | **COMPLETE** — 23/23 + 0 issues |
| `docs/dev/lanes/u18up_report.md` | **COMPLETE** (this file) |
| Do not send/post/comment anywhere | **HONORED** — no `gh issue create`/`comment`/PR, no APPROVED/REPORTED status set |
| Do not merge or push | **HONORED** — branch left for the manager |

Nothing OWED. The only thing outside this lane's authority is Frank's
approval to send `notes/pcre2-2026-10-07.md` (and, separately, whether
he wants it as its own issue or folded into another pcre2 batch —
`notes/pcre2-2026-09-27.md`'s U1/U2/U4 are already REPORTED under
https://github.com/PCRE2Project/pcre2/issues/1015, which is a
performance-only thread; U14 is correctness, and a fresh issue reads
more natural to me, but that's the manager's/Frank's call to make at
send time, not mine to decide here).
