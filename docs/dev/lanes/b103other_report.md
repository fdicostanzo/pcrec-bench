# Lane b103other — U6/U7/U8 repros, latest-release checks, tracker searches

Branch `lane/b103other`, worktree `worktrees/b103other`. Task: for the
three findings assigned (U6 TRE, U7 vectorscan, U8 RE2), per
`docs/design/upstream_pipeline_v1.md` §2.2/§4: a minimal standalone
reproduction, a check against the newest upstream release, a tracker
search, `expected.txt`, and (for findings still PRESENT and not
NOT-A-BUG) a per-engine note draft. Sibling lane `b103infra` owns
`findings.tsv`/`tools/upstream.py`/the skill; this lane wrote only
`docs/dev/upstream/repro/U{6,7,8}/`, `docs/dev/upstream/notes/
{tre,vectorscan}-2026-09-27.md`, and this report. `findings.tsv` and
`docs/dev/upstream_findings.md` are untouched — the statuses below are
what I reached; the manager applies them.

## U6 — TRE 0.9.0, `[\x80-\xff]{2,4}` (and any bracket-expression escape)

**Status reached: UNDERSTOOD** (upgraded from the narrative's "not yet
UNDERSTOOD" — new since the narrative was last written).

- **Repro**: `docs/dev/upstream/repro/U6/repro.c` — self-contained,
  `#include <tre/tre.h>` + `-ltre` only. Two cases: plain ASCII text
  ("GET /products?...") spuriously MATCHES `[0,3)` where the oracle
  says nomatch; the genuine high-byte pair `0x81 0x82` fails to match
  where the oracle says `[0,2)`. `run.sh` builds+runs it, prints the
  contract's final line. Verified: `U6 PRESENT tre 0.9.0 1`, exit 0.
- **latest_checked**: `0.9.0@2026-09-27`. TRE's newest GitHub *release*
  is `v0.9.0` (2024-09-20) — the SAME version already installed
  (`libtre-dev 0.9.0-1build1`), confirmed via `gh api
  repos/laurikari/tre/{tags,releases}`. To rule out a Debian/Ubuntu
  packaging-patch explanation, I also downloaded the `v0.9.0` release
  tarball, built it from source (`./configure --disable-shared
  --enable-static && make`, ~2 min, no extra deps needed) and linked
  the repro statically against that `libtre.a`: **byte-for-byte
  identical output** to the distribution package (see
  `expected.txt`'s header). So this is confirmed against the true
  current upstream release, not just the distro build.
- **tracker**: `searched:2026-09-27:none-found`. Checked
  `laurikari/tre`'s full issue list (all 45+ issues, open and closed,
  via `gh issue list --state all`) plus keyword searches for "byte" and
  "regncompb". Nearest related issues are #143 ("Heap out-of-bounds
  read in byte-mode approximate regex matching") and #120 ("Unicode
  range matched mistake") — neither is this mechanism.
- **Cause, source-confirmed**: fetched TRE 0.9.0's
  `lib/tre-parse.c` from GitHub and read `tre_parse_bracket_items()`
  (~lines 256-365): it builds ranges/literals directly off raw
  characters (`min = *re; max = *(re + 2);` / `min = max = *re++;`)
  with **no escape processing at all** — contrast the top-level atom
  parser's `case L'x':` (~line 1466 of the same file), which DOES
  decode `\xHH`, a thousand-plus lines away and never reached from
  inside `[...]`. A behavioural scan (`^[\x80-\xff]$` against all 256
  byte values) matches this exactly: the matched set is precisely
  `{0x30-0x5C} ∪ {0x66, 0x78}` (the literal-parse of `\x80-\xff` as
  `\ x 8 0 - \ x f f`), nowhere near 0x80-0xFF. This generalises: the
  SAME parser gap explains the two other wrong patterns the bench
  already observed (`tag-pair-match`'s `[\w:-]`, the SQLi pattern's
  `[\s\x0b]`) — every one of them puts a backslash escape inside `[...]`.
- **Note**: `docs/dev/upstream/notes/tre-2026-09-27.md`, drafted,
  approval line blank.

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

| brief item | status |
|---|---|
| U6 repro (min. standalone C, links only TRE) | COMMITTED `docs/dev/upstream/repro/U6/{repro.c,run.sh,expected.txt,README.md}` |
| U7 repro (min. standalone C, links only vectorscan) | COMMITTED `docs/dev/upstream/repro/U7/{repro.c,run.sh,expected.txt,README.md}` |
| U8 repro (min. standalone C++, links only RE2; "upstream-canonical way to show it") | COMMITTED `docs/dev/upstream/repro/U8/{repro.cc,run.sh,expected.txt,README.md}` — the repro IS the canonical few-line RE2::Options/RE2::Match C++ shape |
| latest-release check, each engine | COMMITTED: U6 built+ran pristine v0.9.0 (identical); U7 CANNOT-RUN a real build (heavy deps absent), source-diffed 5.4.12/5.4.13 instead (identical); U8 built+ran pristine 2025-11-05 (identical) |
| tracker search, each engine | COMMITTED: U6 none-found; U7 none-found (both vectorscan and hyperscan); U8 found #344 (related, not identical) — none touch `findings.tsv`, all stated above and in each README |
| U8: does RE2 document `\B` under UTF-8 as intended | COMMITTED — yes, `doc/syntax.txt`'s ASCII-only wording, cited in `repro/U8/README.md` and above; verdict NOT-A-BUG |
| `expected.txt` per repro, source-information header | COMMITTED, all three |
| note per engine with ≥1 REPRODUCED non-NOT-A-BUG finding | COMMITTED: `notes/tre-2026-09-27.md`, `notes/vectorscan-2026-09-27.md`. NOT drafted: `notes/re2-2026-09-27.md` (U8 resolved NOT-A-BUG — see above; flagged, not silently skipped) |
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
