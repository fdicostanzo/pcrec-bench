# Lane b103other — U6/U7/U8 repros, latest-release checks, tracker searches

Branch `lane/b103other`, worktree `worktrees/b103other`. Task: for the
three findings assigned (U6 TRE, U7 vectorscan, U8 RE2), per
`docs/design/upstream_pipeline_v1.md` §2.2/§4: a minimal standalone
reproduction, a check against the newest upstream release, a tracker
search, `expected.txt`, and (for findings still PRESENT and not
NOT-A-BUG) a per-engine note draft. Sibling lane `b103infra` owns
`findings.tsv`/`tools/upstream.py`/the skill; this lane wrote only
`docs/dev/upstream/repro/U{6,7,8}/`, `docs/dev/upstream/notes/
{tre,vectorscan}-2026-09-27.md`, `docs/dev/measurements/
{probe_tre_bracket_escape_census.py,probe_tre_bracket_escape_followups.c,
2026-09-27-tre-bracket-escape-census.txt}` (the U6 correction's follow-up,
below), and this report. `findings.tsv` and `docs/dev/upstream_findings.md`
are untouched — the statuses below are what I reached; the manager
applies them.

## U6 — TRE 0.9.0, `[\x80-\xff]{2,4}` — CORRECTED to NOT-A-BUG (2026-09-27, manager review)

**This lane's first pass called this a TRE defect and nearly sent a
note to its maintainers. It was wrong. Corrected the same day on
manager review**, before anything was sent (nothing ever is without
Frank's approval, but the DRAFTED note was itself the wrong artifact to
have written). What follows is the corrected state; the original
mis-framing is preserved nowhere except this sentence and git history.

**Status reached: NOT-A-BUG** (POSIX bracket-expression semantics).

- **Repro** (unchanged in mechanics, `docs/dev/upstream/repro/U6/repro.c`):
  self-contained, `#include <tre/tre.h>` + `-ltre` only. Two cases:
  plain ASCII text ("GET /products?...") MATCHES `[0,3)`; the genuine
  high-byte pair `0x81 0x82` does not match. `run.sh` builds+runs it,
  prints the contract's final line. Verified: `U6 PRESENT tre 0.9.0 1`,
  exit 0 — PRESENT still means "TRE disagrees with a PCRE-style
  reading", which is still literally true; only the INTERPRETATION of
  that fact changed.
- **NEW: `control_glibc.c`**, added per the manager's ask — links ONLY
  glibc's own `<regex.h>` (no TRE at all), runs the identical pattern
  and both subjects through `regcomp()`/`regexec()`, `REG_EXTENDED`.
  Result: **glibc shows the exact same split** (case A matches `[0,3)`,
  case B does not) — see `expected.txt`'s CONTROL block, archived
  verbatim. `run.sh` now builds and runs both, the control's result
  informational-only (never affects the script's exit code).
- **Why this settles it**: POSIX.1-2017 XBD 9.3.5: *"The special
  characters `.`, `*`, `[`, and `\` shall lose their special meaning
  within a bracket expression."* TRE ("a lightweight, robust, and
  efficient **POSIX compliant** regexp matching library", its own
  package description) is reading `[\x80-\xff]` correctly by the rules
  it implements; `\xHH` inside `[...]` was never valid POSIX syntax to
  begin with. glibc's `regcomp` — nobody's idea of a broken POSIX
  implementation — agrees with TRE byte for byte. Full citation and the
  corrected README in `docs/dev/upstream/repro/U6/README.md`.
- **latest_checked** (unchanged): `0.9.0@2026-09-27`, same as installed;
  also confirmed against a pristine `v0.9.0` source build (identical
  output) — see the earlier note in this file's git history / the
  README for the full build detail.
- **tracker**: `searched:2026-09-27:none-found` (unchanged — moot now
  that the answer is NOT-A-BUG; recorded for completeness only).
- **Note deleted**: `docs/dev/upstream/notes/tre-2026-09-27.md` REMOVED.
  Telling TRE's maintainers their POSIX-conforming bracket parser is
  wrong would have been exactly backwards.
- **The real, actionable finding is BENCH-SIDE**, not upstream's problem
  at all: this project's `tre-default` adapter hands PCRE-dialect
  pattern text (with `\xHH`/`\w`/`\s`-style escapes inside `[...]`) to a
  POSIX-only engine that reads those bytes under different rules.
  Already partially documented: `testees/tre/CLAUDE.md` (d)4 names the
  identical mechanism's REFUSAL manifestation on three patterns
  (`wild-datetime-datefinder-alternation`,
  `wild-secrets-username-password-pair`,
  `wild-waf-crs-942500-comment-obfuscation` — a descending range,
  `REG_ERANGE`) but nothing today documents or handles the
  SILENT-WRONG-ANSWER manifestation this repro demonstrates. Neither
  `testees/tre/adapter.py` nor `configs.toml` translates or intercepts
  any bracket-escape pattern — verified by reading both files: no
  string in either mentions `\x`, `\w`, `\s`, or any bracket-content
  rewriting at all; the pattern travels to `tre_regncompb` byte for
  byte, unmodified.

### The corpus census (the manager's asks 2-4)

New: `docs/dev/measurements/probe_tre_bracket_escape_census.py` +
`2026-09-27-tre-bracket-escape-census.txt` (source-headered, per D35;
`probe_tre_bracket_escape_followups.c` alongside it for three targeted
witnesses). Scans every `bench/*/patterns/*.rx` file (all seven
sub-benches, not just capability) for a bracket expression containing a
backslash.

**98 bracket-span hits across 30 distinct (subbench, pattern) pairs**:
bounded 1 (`csv5`), capability 20, email 2 (`orig`, `factored`),
loglines 1 (`kv-quoted`), utf8 6. `tre-default` has **only ever been
measured against `bench/capability@0.1`** (confirmed:
`find store/records -iname '*tre_*' -maxdepth 2 -type d` returns exactly
one subbench dir) — so only the 20 capability hits have a "scored wrong
today" answer at all; the other 10 are unmeasured (utf8's six are also
MOOT: `utf8_set_v1.md` F-S2/F-S3 excludes TRE from ranking on every
pattern except three byte-safe controls, none of which is among these
six — TRE is never run against them by the set's own design).

Of the 20 capability@0.1 hits, read against the committed cross-pin
report (`reports/2026-09-19-capability-0.1-budu-ryzen1600-ext-second-cf0962e3.tsv`):

- **11 never reach `tre_regncompb` at all** — an existing
  `unsupported-by-declaration` policy intercepts them first, for
  reasons unrelated to bracket escapes (backrefs, lookaround, etc.):
  `bracket-array-define`, `codegrammar-xflag`, `float-literal-bound`,
  `pwd-strength-chain`, `quoted-delim-match`, `utf8-lead-no-cont`,
  `wild-codegrammar-json-stringcontent-escape`,
  `wild-logparse-quotedstring-grok`, `wild-logparse-quotedstring-noatomic`,
  `wild-logparse-syslogbase-expanded`, `wild-logparse-winpath-grok`.
- **3 already `did-not-compile`** (the `REG_ERANGE` descending-range
  refusal `testees/tre/CLAUDE.md` (d)4 already documents, unchanged by
  this census): `wild-datetime-datefinder-alternation`,
  `wild-secrets-username-password-pair`,
  `wild-waf-crs-942500-comment-obfuscation`.
- **6 compile and are scored WRONG today, at least partially** —
  `high-byte-run` (`n_wrong=15/15` throughput, `195/375` search, the
  worst by far), `tag-pair-match`/`wild-waf-crs-942360-concat-sqli`/
  `mojibake-curly-quote` (each `n_wrong=5/75` search only, `0` on
  throughput), `codegrammar-flat`/`winpath-near-miss` (`n_wrong=0`
  everywhere DESPITE the mechanism — see below).

**Not every hit is harmful.** `codegrammar-flat` (`[^"\\]`) and
`winpath-near-miss` (`[^<>:"/\\|?*]`) both use the common
"escape-the-backslash" idiom — a DOUBLED backslash (two raw pattern
bytes) that, read literally under POSIX, still ends up excluding one
backslash character; the doubled escape happens to mean the same thing
whether or not backslash is special. `probe_tre_bracket_escape_followups.c`
isolates this witness directly (a lone backslash byte and a lone `"`
byte are both correctly excluded). Contrast `tag-pair-match`'s `[\w:-]`,
which is NOT coincidentally safe: it accepts a literal backslash or the
letter `w` as if they were "word chars" and rejects real digits — the
same probe shows this directly (`[\w:-]+` vs `"5"`: nomatch, wrong;
vs a lone backslash: MATCH, wrong).

A third probe result, outside capability entirely: `bench/bounded/
patterns/csv5.rx` is `(?:[^,\n]{0,32},){4}[^,\n]{0,32}` — `[^,\n]` is
meant to exclude comma-or-newline; under TRE's literal parse it excludes
`{',', '\\', 'n'}` instead, so a REAL embedded newline byte is not
excluded and the class crosses it. Checked against the corpus: NO
committed `bench/bounded` subject today contains an embedded newline
(a `python3 -c "...count(b'\n')"` sweep over every file in
`bench/bounded/subjects/`), so this is DORMANT, not a live wrong answer
— but a real semantic gap if that set ever grows multi-line subjects,
and `tre-default` has never been run against `bench/bounded` regardless
(no store/scratch record), so there is nothing to score today either way.

### Proposed fix (not implemented, per the brief)

Two shapes, either is workable; I did not build either:

1. **Translate, in `testees/tre/adapter.py`, before the pattern reaches
   `tre_regncompb`**: rewrite `\xHH` → the raw byte, `\w`/`\W`/`\s`/`\S`/
   `\d`/`\D` → their POSIX `[:alnum:]`-family equivalents, ONLY inside
   bracket-expression spans (the same span-finder this census's script
   already implements could be reused/hardened for this). Preserves the
   PATTERN AUTHOR's intent; the adapter already does comparable
   compile-time work (`refusal_class` derivation) so this is not an
   unprecedented shape for this file. Risk: a translation bug becomes a
   SECOND silent-wrong-answer source, one this project owns instead of
   TRE.
2. **Declare unsupported**: extend the existing pre-compile capability
   declaration (the same mechanism that already intercepts 11 of these
   20 patterns for other reasons) to also refuse any pattern whose
   bracket expression contains a backslash — turning today's SILENT
   wrong answer into a named, honest `unsupported-by-declaration` /
   `did-not-compile`-shaped exclusion, at the cost of narrowing
   `tre-default`'s measured population further (it is already the
   narrowest on the roster).

I lean toward (2) as the lower-risk near-term move (it costs nothing
but coverage, and TRE is already this project's narrowest-declared
engine) with (1) as a possible follow-up if `tre-default`'s coverage
becomes a stated priority — but this is a recommendation, not a
ruling; PROPOSING only, as asked. A natural adjacent follow-up neither
asked for nor done here: a `testees/tre/CLAUDE.md` addendum recording
this census's own finding (the WRONG-ANSWER manifestation) alongside
(d)4's existing REFUSAL one, so a future reader of that file gets the
whole mechanism in one place.

## U7 — vectorscan 5.4.11, `(?x)` pattern ending in an unterminated `#` comment

**Status reached: REPRODUCED, UNDERSTOOD** (source mechanism was
already stated in the narrative; this lane adds the latest-release
check and the tracker search).

- **Repro**: `docs/dev/upstream/repro/U7/repro.c` — self-contained,
  `#include <hs/hs.h>` + `-lhs` only, reduced from the two real corpus
  patterns to `"(?x) abc  # trailing comment, no newline"`. `run.sh`
  builds+runs it. Verified: `U7 PRESENT vectorscan 5.4.11 1`, exit 0.
- **latest_checked**: source-diffed only, NOT built —
  `vectorscan/5.4.13` (2026-08-23) is the newest release (`5.4.12`,
  2025-07-22, sits between it and our pinned `5.4.11`, 2023-11-21).
  Building vectorscan needs `ragel` + CMake + Boost *development*
  headers; this box has none of the three (`ragel`/`cmake` absent;
  only Boost's runtime `.so` packages installed, no `-dev`), so per the
  brief's own "CANNOT-RUN for latest... check its changelog/source
  instead" fallback, I fetched `src/parser/Parser.rl` for all three
  tags (5.4.11/5.4.12/5.4.13) and diffed them pairwise: the
  `inComment`/`readNewlineTerminatedComment`/end-of-input-throws logic
  is **byte-for-byte identical** across all three; the only changes in
  that file between releases are unrelated (a cppcheck suppression, two
  `reinterpret_cast` style changes, a `std::move` removal, and issue
  #210's new nested-character-class refusal in 5.4.12). So: confirmed
  unchanged by source, not confirmed by running the newest binary.
  Recorded as `latest_checked: 5.4.13 (source-diff only, not built) @
  2026-09-27` — the manager should decide how `findings.tsv` should
  spell "diffed, not run" if that distinction matters to the registry.
- **tracker**: `searched:2026-09-27:none-found` on
  `VectorCamp/vectorscan` (`gh search issues` for "comment",
  "free-spacing", "(?x)"; a GitHub code search for "Unterminated
  comment" in that repo also returned zero). Also checked
  `intel/hyperscan` (the original project vectorscan forked from —
  NOT archived, still receives pushes as of 2026-09-25) with the same
  keywords: no match there either.
- **Note**: `docs/dev/upstream/notes/vectorscan-2026-09-27.md`, drafted,
  approval line blank. Framed candidly as possibly-intentional
  strictness (Hyperscan's PCRE-*subset* posture is a stated project
  stance), since I can't rule that out without a maintainer answer.

## U8 — RE2 11.0.0, `\B` between the bytes of one UTF-8 character

**Status reached: NOT-A-BUG** (this is new — the existing narrative
left U8 at plain OBSERVED with the question open). **No note drafted**
for RE2 — see reasoning below; flagging this as a judgment call for the
manager to confirm or overrule.

- **Repro**: `docs/dev/upstream/repro/U8/repro.cc` — self-contained
  C++, `#include <re2/re2.h>` built via `pkg-config --cflags/--libs
  re2` only (the same line `testees/re2/adapter.py` uses). Subject
  `"a" + U+00E9` as raw UTF-8 bytes `61 C3 A9`; walks `RE2::Match()`
  with an advancing `startpos` (the same empty-match advance rule as
  this project's own drivers, KB-17). Finds `\B` at byte `[2,2)` —
  strictly INSIDE the two-byte encoding of U+00E9 — and `[3,3)`.
  Verified: `U8 PRESENT re2 11.0.0 1`, exit 0.
- **latest_checked**: `2025-11-05@2026-09-27` (a genuine upstream
  build, not just source-reading). `pkg-config --modversion re2`
  reports "11.0.0" for the installed package — this is RE2's own
  `.pc`-file version scheme (matches this project's `re2_11.0.0`
  testee id), not a date tag; the Debian package version
  `20250805-1build3` maps to the nearby upstream tag `2025-08-05`.
  `google/re2`'s newest tag is `2025-11-05` (`gh api
  repos/google/re2/tags`) — genuinely newer. I downloaded that tag's
  tarball and built `obj/libre2.a` with RE2's own plain `make` against
  this box's system `libabsl-dev 20260107.0-4` (no cmake needed, ~1
  min build) and linked the repro against it directly: **byte-for-byte
  identical output** to the distribution package.
- **tracker**: checked `google/re2` issues for "\B", "\b UTF",
  "word boundary utf8" (`gh search issues`). Found **google/re2#344**
  ("`\b` not working with Unicode characters", opened 2024, still
  OPEN) — the maintainer (`junyer`) replies: *"Sorry, RE2 supports
  `\b`, `\d`, `\s`, `\w` and their counterparts for ASCII only."* This
  is the SAME underlying restriction (ASCII-only word semantics) but a
  DIFFERENT specific claim (that issue is about which CHARACTERS count
  as `\w`, e.g. `ä`; U8 is about the byte-vs-character POSITION a
  zero-width `\b`/`\B` lands at) — so I recorded `tracker:
  searched:2026-09-27:https://github.com/google/re2/issues/344` as
  strong supporting context rather than a byte-identical duplicate.
  Not marking it KNOWN-UPSTREAM outright; the manager may reasonably
  disagree and fold it in.
- **Why NOT-A-BUG (§3's ask 3, established)**: RE2's own upstream
  `doc/syntax.txt` (fetched from the `main` branch, 2026-09-27) states
  both assertions explicitly:

      \b   at ASCII word boundary («\w» on one side and «\W», «\A», or «\z» on the other)
      \B   not at ASCII word boundary

  and separately that its Perl character classes (`\w` included) are
  "all ASCII-only". There is no UTF-8-aware `\b`/`\B` at any encoding
  setting, by design — this isn't a UTF-8-specific defect, it's the
  documented ASCII-only rule applying uniformly to a byte-oriented
  automaton that has no separate "decode to characters first" pass.
  The observed mid-character position is the predictable, mechanical
  consequence of that documented design, not an inconsistency within
  it. Full citation and reasoning in `docs/dev/upstream/repro/U8/
  README.md`.
- Because the finding resolves to NOT-A-BUG, I did not draft
  `docs/dev/upstream/notes/re2-2026-09-27.md` — per the brief, notes
  are for engines with "at least one REPRODUCED non-NOT-A-BUG finding",
  and RE2's only assigned finding here is that one. If the manager
  judges this worth a documentation-clarity request to RE2 (asking
  `doc/syntax.txt` to state explicitly that byte offsets, not rune
  offsets, are what `\b`/`\B` operate on under `EncodingUTF8`) rather
  than a correctness report, that's a different, smaller note than
  what this brief asked me to draft, and I left it undrafted rather
  than guess at the framing.

## Charter-vs-committed checklist

**The manager's U6 change request (this session's second pass):**

| ask | status |
|---|---|
| (1) glibc regcomp/regexec CONTROL on case A/B, in the U6 repro dir, archived in expected.txt | COMMITTED `docs/dev/upstream/repro/U6/control_glibc.c`; wired into `run.sh` (informational, never changes exit code); output archived in `expected.txt`'s CONTROL block. Result: glibc AGREES with TRE |
| (2) since glibc agrees: NOT-A-BUG; delete the TRE note; rewrite README's reading | COMMITTED — `notes/tre-2026-09-27.md` deleted; `repro/U6/README.md` rewritten around the POSIX citation + the glibc control |
| Look at `testees/tre/` for an existing declaration/translation | COMMITTED (investigated, not edited) — NONE exists for the wrong-answer manifestation; `adapter.py`/`configs.toml` contain no bracket-escape handling at all; `CLAUDE.md` (d)4 documents only the REFUSAL manifestation on 3 different patterns |
| Which bench/*/ patterns contain a backslash inside `[...]` sent to tre, committed under docs/dev/measurements/ with a source header | COMMITTED `docs/dev/measurements/probe_tre_bracket_escape_census.py` + `2026-09-27-tre-bracket-escape-census.txt` + `probe_tre_bracket_escape_followups.c` — 30 patterns across 5 sub-benches; only capability@0.1 has ever been measured |
| State whether those rows are scored wrong for tre today | COMMITTED — 6/20 capability patterns wrong (1 badly, 3 partially, 2 not at all despite the mechanism); the other 24 (14 capability + 10 elsewhere) are moot/unmeasured, each named with why |
| Propose the fix (don't implement) | COMMITTED — two shapes (translate vs. declare-unsupported) in the U6 section above, no code changed under `testees/tre/` |
| Commit on the same branch, update the report, hand back | COMMITTED — this same commit; report updated (this file) |

**The original brief:**

| brief item | status |
|---|---|
| U6 repro (min. standalone C, links only TRE) | COMMITTED `docs/dev/upstream/repro/U6/{repro.c,run.sh,expected.txt,README.md,control_glibc.c}` |
| U7 repro (min. standalone C, links only vectorscan) | COMMITTED `docs/dev/upstream/repro/U7/{repro.c,run.sh,expected.txt,README.md}` |
| U8 repro (min. standalone C++, links only RE2; "upstream-canonical way to show it") | COMMITTED `docs/dev/upstream/repro/U8/{repro.cc,run.sh,expected.txt,README.md}` — the repro IS the canonical few-line RE2::Options/RE2::Match C++ shape |
| latest-release check, each engine | COMMITTED: U6 built+ran pristine v0.9.0 (identical); U7 CANNOT-RUN a real build (heavy deps absent), source-diffed 5.4.12/5.4.13 instead (identical); U8 built+ran pristine 2025-11-05 (identical) |
| tracker search, each engine | COMMITTED: U6 none-found; U7 none-found (both vectorscan and hyperscan); U8 found #344 (related, not identical) — none touch `findings.tsv`, all stated above and in each README |
| U8: does RE2 document `\B` under UTF-8 as intended | COMMITTED — yes, `doc/syntax.txt`'s ASCII-only wording, cited in `repro/U8/README.md` and above; verdict NOT-A-BUG |
| `expected.txt` per repro, source-information header | COMMITTED, all three |
| note per engine with ≥1 REPRODUCED non-NOT-A-BUG finding | COMMITTED: `notes/vectorscan-2026-09-27.md` only. NOT drafted: `notes/tre-2026-09-27.md` (U6 corrected to NOT-A-BUG this session — the note was drafted then DELETED, see above), `notes/re2-2026-09-27.md` (U8 resolved NOT-A-BUG — see above; both flagged, neither silently skipped) |
| findings.tsv / upstream_findings.md | NOT TOUCHED (b103infra's / the manager's, per brief) |
| nothing sent anywhere | TRUE — no issue created, no post made on any tracker; only read-only `gh`/`curl`/`WebSearch`-equivalent calls |

## Scratch / box notes

All builds ran in `/var/tmp/b103other-*-scratch` (session scratchpad
rule honoured — nothing under `/tmp` root, nothing committed). Box was
not used for any bench measurement; these are all engine-only,
sub-minute compiles/runs, no heavy suite, no coordination needed with
`pcrecdev1`. `gh` was used read-only (issue/tag/release listing) under
the session's own authenticated account; no write calls were made.

Validation: all three `run.sh` scripts re-run clean from a fresh
`$UPSTREAM_SCRATCH` immediately before this report was written (see the
`U<n> PRESENT ... 1` / exit-0 lines quoted above for each).
