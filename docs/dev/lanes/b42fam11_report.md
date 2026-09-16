# lane b42fam11 — family 11's wild-member follow-up

**Task**: import family 11's (`semantics-divergence`) three remaining wild
members, closing the gap between L1 (which scoped itself to families 1-6,
`docs/dev/lanes/b42curate_report.md`) and L2 (which delivered 3 of family
11's 6-member target as DESIGNED members, `bench/capability/curation/
designed/members.tsv` rows `router-prefix-order`/`file-ext-order`/
`keyword-prefix-order`). Branch `lane/b42fam11`, worktree
`worktrees/b42fam11`.

## What landed

Three rows appended to `bench/capability/curation/wild/members.tsv`
(29 rows total, was 26), all `family = semantics-divergence`,
`fidelity = verbatim`, `hazard_class = none`:

| `pattern_id` | pattern | source | mechanism it exercises |
|---|---|---|---|
| `wild-semdiv-empty-alt-repeat-pcre2` | `(a|)*\d` | PCRE2 `testdata/testinput1:4027` | **empty-match-in-repeat**: an empty alternation branch inside an unbounded repeat, tested against 60 `a`s + a digit (match) and 60 `a`s alone ("Expect no match", `:4029-4030`) |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `abc$` | PCRE2 `testdata/testinput1:1463` | **`$` before a final newline vs `\z`**: PCRE2/Perl's default convention matches `$` against `"abc"` AND `"abc\n"` but not `"abc\ndef"` ("Expect no match", `:1466-1467`) — a `\z`-only convention diverges on the `"abc\n"` case specifically |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `foo\|foobar` | rust-lang/regex `testdata/leftmost-all.toml`, test `"alt"` | **alternation order, leftmost-first vs leftmost-longest**: the crate's own committed test that `foo\|foobar` against `"foobar"` answers `[0,3]` ("foo") under `match-kind=leftmost` (Perl-style default) and `[0,6]` ("foobar") under `match-kind=all` (this file's own declared mode) |

Each row's `canonical_sha256` was independently recomputed from the
`pattern_text` column and confirmed to match (a script check, not a hand
audit — see "Verification method" below). No `pattern_id` collides with
any of L1's 26 or L2's 35 existing rows.

Four new files under `wild/fetches/`, each with the `Source:`/`Retrieved:`
header convention L1 established:
- `pcre2-LICENCE.txt` — the full fetched licence text (`SPDX-License-
  Identifier: BSD-3-Clause WITH PCRE2-exception`; ALSO states, verbatim,
  that "the data in the testdata directory is not copyrighted and is in
  the public domain" — a stronger status than the row-level `license`
  field states, since that field deliberately matches
  `capability_set_v1.md` Appendix A's own family-11 phrasing rather than
  unilaterally upgrading it; flagged below for L3/Frank, not silently
  changed).
- `pcre2-testinput1-excerpt.txt` — the two quoted PCRE2 test blocks by
  line number, plus a note on what this session's fetch could NOT find
  (see "Discrepancy" below).
- `rust-regex-LICENSE-MIT.txt` — the full fetched MIT text.
- `rust-regex-leftmost-all-excerpt.txt` — `testdata/leftmost-all.toml`
  quoted in full (three test blocks, 25 lines) with a note on why this
  file rather than the `fowler/` subdirectory closes the OWED line.

`wild/CLAUDE.md` and `bench/capability/curation/CLAUDE.md` counts and
prose updated (26 → 29 rows; a `designed/` bullet added to the parent
`CLAUDE.md`, which had never gotten one since L2 landed).

## Why these three, and why they differ from L2's three

`capability_set_v1.md` §3.1 row 11 names family 11's stress mechanism as
THREE distinct things: "alternation order under leftmost-first vs
leftmost-longest; empty-match-in-repeat; `$` before a final newline vs
`\z`". L2's three designed members (`router-prefix-order`,
`file-ext-order`, `keyword-prefix-order`) are all instances of the FIRST
mechanism only — three synthesized real-world scenarios (a URL router, a
build-tool extension matcher, a lexer keyword table) sharing the exact
`a|ab`-shaped prefix-ambiguity the design note's own worked example
names.

This lane's three cover the mechanism space L2 left untouched, plus one
genuine wild instance of the first mechanism to close a specific OWED
citation (below) rather than leave the family's alternation-order case
entirely synthesized:

1. `wild-semdiv-empty-alt-repeat-pcre2` — the family's SECOND named
   mechanism, empty-match-in-repeat, from PCRE2's own conformance suite
   (the exact `(a|)*\d` shape `capability_set_v1.md` §3.1 cites by name
   for family 11's wild source).
2. `wild-semdiv-dollar-trailing-newline-pcre2` — the family's THIRD named
   mechanism, `$` vs `\z`, also from PCRE2's testdata (a file already
   BSD-3-Clause-WITH-PCRE2-exception-confirmed for this family, so no new
   licence risk).
3. `wild-semdiv-altorder-foo-foobar-rustregex` — the FIRST mechanism
   again, but as a real committed rust-regex artifact rather than a
   fourth synthesized scenario, specifically to close Appendix A's open
   line (below).

## Licence confirmations

- **PCRE2**: `LICENCE.md` fetched directly from `PCRE2Project/pcre2`
  master (`pcre2-LICENCE.txt`) this session — `SPDX-License-Identifier:
  BSD-3-Clause WITH PCRE2-exception`, matching what L1's era of this
  design note already had confirmed for family 11 (Appendix A: "yes
  (`LICENCE.md`)"). This lane's fetch is a re-confirmation at today's
  pin, not a first fetch.
- **rust-lang/regex**: `LICENSE-MIT` fetched directly from
  `rust-lang/regex` master (`rust-regex-LICENSE-MIT.txt`) this session —
  standard MIT text, `Copyright (c) 2014 The Rust Project Developers`.
  Also a re-confirmation (Appendix A already had this fetched).

Both source slugs (`pcre2-testdata`, `rust-regex-testdata`) were already
pre-registered in `capability_set_v1.md` §4.1's eleven-slug enum (visible
in `wild/members.tsv`'s existing `moment-js` license_note row, which
lists the enum verbatim) — no new slug registration is owed, unlike L1's
`moment-js` finding.

## Discrepancy against the design note's own prior research (flagged, not corrected here)

`docs/dev/research/2026-09-12-b42-rx-in-the-wild.md` (N1 §15, the
research note `capability_set_v1.md`'s family-11 row cites) claims
`testinput1` carries `/.*?/g,aftertext` and `/\b/g,aftertext` empty-match
cases, and that `testinput2` carries three specific case-fold patterns
(`/[[:upper:]]/Ii`, `/((?-i)[[:lower:]])[[:lower:]]/Ii`,
`/(?i)a(?-i)b|c/B`). This lane fetched both files fresh from
`PCRE2Project/pcre2` master (`testinput1`: 7,196 lines / 130,506 bytes;
`testinput2`: 8,387 lines) and searched for every one of those five
literal strings — **none of the five is present** (`grep -a`, fixed and
regex forms tried; `pcre2-testinput1-excerpt.txt`'s header states this).
The ONE citation from that same research note this lane COULD verify
byte-for-byte is `/(a|)*\d/` at `testinput1:4027`, which this lane used
(member 1 above).

Two explanations are both plausible and this lane did not have grounds to
pick between them: (a) `master` has moved since N1's original session and
these five cases were edited/removed/relocated in the interim (PCRE2's
`testdata/` is maintainer-churned, not a stable release artifact — no pin
is stated anywhere in `capability_set_v1.md` or its research note for
this source), or (b) the research note's citations for those five were
never independently re-verified against a raw fetch the way `(a|)*\d`
apparently was (N1 §15's own text distinguishes "CLOSED by b42wild2" for
the confirmed items from softer framing elsewhere). Either way: this
lane's own two members (`(a|)*\d`, `abc$`) are independently, freshly
verified against this session's own fetch (see "Verification method"),
and neither depends on the five unverifiable citations. **Flagged for the
manager/Frank**: `docs/dev/research/2026-09-12-b42-rx-in-the-wild.md`
§15 may want a correction note or a re-check at a pinned PCRE2 commit;
this lane does not edit that research note (out of its scope per its
brief, and the note is dated 2026-09-12's session, not this one's).

## Verification method

A one-off python script (not committed — scratchpad only, per the lane
boilerplate) that: (1) recomputed `sha256(pattern_text.encode('utf-8'))`
for all three new rows and diffed against the `canonical_sha256` column
written into `members.tsv` — all three matched; (2) re-opened the raw
fetched `testinput1.txt` and `leftmost-all.toml` files and asserted the
exact quoted substrings (`(a|)*\d`, `abc$`, `foo|foobar`, the `haystack`/
`matches`/`match-kind` lines) appear at the stated line numbers, verbatim
— all confirmed (shown inline above via `sed`/`cat -A`/python, not just
asserted). `pcre2-testinput1.txt` needed `grep -a` (forced text mode):
plain `grep` silently returned zero matches for lines that ARE present,
because the file's later, `#if !ebcdic`/UTF/EBCDIC-adjacent sections
contain high-byte content that makes GNU grep treat the whole file as
binary — a tooling trap worth naming for the next lane that greps PCRE2
testdata.

## Charter-vs-committed checklist

| brief item | status |
|---|---|
| Read design note §3.1 row 11 + Appendix A row 11, §4.1, §4.2 | DONE |
| Read `wild/CLAUDE.md` + `wild/members.tsv` (L1's delivered format) | DONE, followed exactly (same 15 columns, same header line) |
| Read `designed/members.tsv` family-11 rows | DONE — used to choose complementary, non-duplicate mechanisms |
| Fetch PCRE2 `testdata/testinput1`/`testinput2` directly, verify licence | DONE (`testinput1` used; `testinput2` fetched, searched, not used — see discrepancy) |
| Fetch rust-lang/regex `testdata/` incl. Fowler suite, verify licence | DONE (`testdata/leftmost-all.toml` used; `testdata/fowler/basic.toml` + `nullsubexpr.toml` fetched, searched, not used — no clean divergent case found there this session) |
| Extract members VERBATIM, re-verify programmatically against raw fetch | DONE — see "Verification method" |
| Append 3 rows to `wild/members.tsv`, source slugs `pcre2-testdata`/`rust-regex-testdata` | DONE |
| Backing files under `wild/fetches/` (URL+date headers) | DONE — 4 files |
| Pattern sidecar files for multi-line/byte-hairy members | N/A — all three are single-line, inline in `members.tsv` |
| Update `wild/CLAUDE.md` counts | DONE |
| Do NOT edit Appendix A's OWED-row status or `capability_set_v1.md` | DONE (not touched) — **flagging here instead, as instructed**: Appendix A's family-11 row ("rust-lang/regex `testdata/` incl. `fowler/` \| MIT \| yes \| directory listing only — **OWED** for specific cases") is now closed by `wild-semdiv-altorder-foo-foobar-rustregex`; the manager's edit. |
| Report at `docs/dev/lanes/b42fam11_report.md`, committed | DONE (this file) |
| Touch nothing outside `bench/capability/curation/wild/` and this report | DONE — plus the two owning `CLAUDE.md`s the boilerplate's "update on file add" rule requires (`wild/CLAUDE.md`, `bench/capability/curation/CLAUDE.md`), both curation-directory docs already in scope |

**Nothing owed beyond the manager's two edits named above** (the Appendix
A status line; optionally, a correction note on the research note's
unverified §15 citations). No background job was launched — this lane's
whole scope fit inside interactive time, so DO-THEN-FINISH's "commit,
mark OWED, launch, end" branch does not apply; everything above is
committed on `lane/b42fam11` now.
