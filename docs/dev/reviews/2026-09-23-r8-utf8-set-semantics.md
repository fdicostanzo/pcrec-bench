# R8 critic review — engine semantics vs. the oracle

**Subject:** `docs/design/utf8_set_v1.md` v0.1 + inbox I-90.
**Lens:** engine semantics vs. the oracle (one of several D6 panel lenses,
2026-09-23). Read-only; no builds; two witness compiles run (both under a
second, both reported below).

---

## Findings

### F-S1 — MAJOR — §8.5's "three cells" / U+0300 claim is not supported by pcrec's own arbitrating tool, though the mitigation it recommends still happens to be safe

**Cite:** `utf8_set_v1.md` §8.5 and §15 R6: *"AX's [M5.0] stage-5 section
records that the two local libpcre2 builds on the pcrec author's box
DISAGREED with the 10.46 reference on three cells (U+00B7 and U+0300 under
`\p{Greek}`/`\p{scx=Greek}`)... The affected characters (U+00B7, U+0300) are
avoided in the subject pair."*

**Evidence:**
- `~/pcrec/tests/utf8/axis12_scripts.rxt:1-15` (the actual AX source cited)
  states counts, not "three": *"Homebrew 10.48 ... Unicode 17.0.0 agrees on
  57 of them and macOS's system 10.42 ... Unicode 14.0.0 on 54"* — i.e. 2
  and 5 disagreements respectively, against two *different* comparison
  pairs, neither of which is 3.
- The same header names its own arbitrating source: *"See
  tests/uprops/uprops_compare.py's RECLASSIFIED/SCX_REVISED."* Read
  directly (`~/pcrec/tests/uprops/uprops_compare.py:122-138`): the dict
  entry for the 14.0.0→16.0.0 drift the design doc is describing names
  **U+00B7 only**, with its own comment stating so explicitly: *"It is
  therefore the **single** code point on which a 10.42 oracle disagrees
  with pcrec ... and — because it is Latin-1 — the **only** script
  disagreement the byte arm sees at all."* `SCX_REVISED`'s other fifteen
  members (0x0306, 0x0308, 0x0320, 0x0323, 0x0331, 0x0951, 0x0952,
  0x1CD5-0x1CED) are the *16.0.0→17.0.0* drift, a different version pair
  than the one the design doc cites (14.0.0/16.0.0) — and **U+0300 is not a
  key in either tier of the dict** (`grep -n "0x0300" uprops_compare.py`
  returns nothing under either RECLASSIFIED or SCX_REVISED).
- U+0342 (the code point the design doc actually recommends using,
  `prp-greek`'s live subject) is likewise absent from both tiers, so the
  RECOMMENDATION (avoid U+00B7, use U+0342) is not undermined by this
  finding — only the stated EVIDENCE for it is wrong. AX's own header
  appears to conflate "the two code points that flip between the bare and
  `sc=` spellings *within* the 16.0.0 pin" (U+0342, U+0300 — a Script vs.
  Script_Extensions membership question, orthogonal to version drift) with
  "the code points whose Script_Extensions membership is version-sensitive"
  (U+00B7 alone, confirmed) — and the design doc inherited that conflation
  as fact rather than checking it against the tool AX itself names as
  authoritative.

**Disposition:** correct the sentence to name **U+00B7 alone** as the
version-drift-sensitive code point (14.0.0→16.0.0), drop "U+0300" from that
specific claim (it may still be worth avoiding for the *spelling-flip*
reason, but that is a different property and should be stated as such), and
replace "three cells" with the actual counts (57/59, 54/59) or simply "a
minority of the 59-cell sweep." The chosen mitigation (U+0342) does not need
to change. This is exactly the R2 "UNCONFIRMED shipped as fact" risk the
note itself charters against (§15 R2) — an instance the note's own author
did not catch because the wrong claim originates in AX's prose header, one
level removed from the tool it names.

---

### F-S2 — MAJOR — the blanket `utf8-encoding` exclusion drops TRE as a comparator on exactly the rows where it would agree

**Cite:** `utf8_set_v1.md` §7.3 (*"tre-default runs NO (a)-(f) cell in
utf8@0.1 ... every pattern is a clean unsupported-by-declaration compile
row"*) and §7.4's table row (*"(a)-(f) all | tre-default, via
`utf8-encoding` (§7.3) | CONFIRMED"*).

**Argument:** §7.3's three reasons (byte-decomposition, the wide-char
driver-model cost, "the honest alternative is already covered") are sound
for the population they were written against — patterns whose behaviour
genuinely differs between byte and character reading. But the exclusion as
written is **set-wide**, not per-pattern: it removes TRE from every one of
the 74 members including the ones deliberately authored to have **no**
encoding-dependent content at all — the floor `~`, `ci-ascii-control`
(`(?i)abc`), `asr-b-ascii` (`\bcat\b`), and by construction every pattern's
row against the `asc` (byte-clean ASCII) subject population (§4.2's own
description: *"the CONTROL. What does the encoding cost when there is
nothing to encode?"*). On a pure-ASCII pattern read over pure-ASCII text,
`tre_regncompb`'s byte-literal reading and any UTF-8 engine's
character-aware reading MUST agree — there is no multi-byte content for the
two readings to diverge over. TRE is not "the honest alternative already
covered" here either: reason 3 in §7.3 names growth (k)'s *same-engine*
pcrec byte mirror as the substitute, but that is a different engine from
TRE, so TRE's presence on the ASCII control rows is not redundant with
anything else on the roster — it is the ONE genuinely independent
byte-mode engine this repo has (rust/re2/onig/vectorscan are all UTF-8- or
Unicode-default already per §7.1's own table), and it is precisely on the
`asc`-subject / pure-ASCII-pattern rows that R3 (§12, "the ENCODING band")
and Q1's ranked-`asc`-control decision (§14) most want an independent
cross-engine baseline.

Concretely, this loses a comparator on: the floor `~` (all regimes, all
subject corpora — a pattern that literally cannot see the encoding),
`ci-ascii-control` on `asc`, `asr-b-ascii` on `asc`, and any (a)-(f) member's
row specifically against the `asc` subject (§4.2's fifth corpus), which by
its own charter is the row where every engine's answer should coincide
regardless of internal encoding handling.

**Disposition:** narrow §7.3's ruling from a set-wide `requires =
utf8-encoding` declaration to a genuinely per-pattern one (which is also
how `REQUIRES` is modelled everywhere else in this repo —
`pcrecbench/capability.py:98`'s docstring: *"a pattern's `tags` list"*, a
per-pattern fact, not a per-set one). At minimum, the floor and the named
ASCII controls (`ci-ascii-control`, `asr-b-ascii`, and — by subject rather
than by pattern, which the current REQUIRES model cannot express — every
member's `asc`-subject rows) should NOT carry `requires = utf8-encoding`,
and `tre-default` should be measured on them. If the REQUIRES model's
pattern-not-subject grain makes the `asc`-only carve-out inexpressible
cleanly, that limitation should be named explicitly (a companion gap to
§3.3's already-honest gap list) rather than silently absorbed into the
blanket exclusion.

---

### F-S3 — MINOR — the new `utf8-encoding` token is specified as a blanket set fact, in tension with the REQUIRES model it is added to

**Cite:** `utf8_set_v1.md` §7.5's token table and §7.3's ruling, against
`pcrecbench/capability.py:87-88`'s `REQUIRES_VOCAB` and its surrounding
docstring (`:1-16`), which frames every existing token (`backrefs`,
`lookaround`, `non-utf8-subject`, etc.) as a fact about ONE PATTERN's
construct, checked per-pattern against a config's declared capabilities.

**Argument:** this is the same defect as F-S2 from the other side: §5's
family tables never show a per-pattern `requires=utf8-encoding` tag on any
of the 74 members (only `ascii-class-scope`, `unicode-class-scope` and
`true-end-anchor` appear as explicit per-row REQUIRES in the tables), yet
§7.3/§7.4 talk about the token as though it applies uniformly to "every
pattern" in the set. Either every member is meant to carry it (in which
case §5's tables are incomplete — a real pattern under this repo's own
"REQUIRES is closed and machine-checked" discipline needs the tag written
down, not implied by which directory the pattern lives in), or it is meant
to be selective and §7.3/§7.4 overstate its reach (which is F-S2's finding
from the config side). The note does not currently make clear which.

**Disposition:** state explicitly in §5 or in a new subsection of §7 which
members carry `requires = utf8-encoding` and which do not, resolving F-S2
in the same edit.

---

### F-S4 — NOTE — the caseless-fold family's UCP-independence is correct but unstated, leaving a plausible future "fix" trap

**Cite:** `utf8_set_v1.md` §5(c) and §8.1 (UCP is applied "to exactly those
patterns declaring `unicode-class-scope`" — the twelve named in (a)/(e),
never any `ci-*` pattern).

**Verification:** this is right. `~/pcrec/docs/design/utf8_design.md`
§4.5 (`out/caseless.txt` §7) measures fold behaviour as a function of
`PCRE2_CASELESS` alone vs. `PCRE2_UCP|PCRE2_CASELESS` **without** `PCRE2_UTF`
(pcrec's byte-encoding comparator); UD §4.1-§4.4's actual fold-closure
measurements that back family (c)'s expectations (`out/caseless.txt` §3,
§3b, §4, §5) are run under plain `PCRE2_UTF`, and UD §4.4 states outright
that "full simple case folding ships" under `-e utf8` with no UCP tier to
defer. So the (c) family's expectations are correctly UCP-independent, and
the oracle policy in §8.1 is correctly scoped. But the design doc never
states the REASON — that UCP governs class SCOPE (`\w`/`\d`/`\s`/POSIX),
not fold membership, and the two are orthogonal PCRE2 options — so a reader
who does not already know UD §4.5's finding may reasonably wonder why every
`ci-*` pattern is missing the `_ucp` twin every `cls-*`/`asr-*` UCP-affected
pattern gets, and "fix" it by adding one that would then measure nothing
new (fold answers are identical either way) at real `search_short`/
`throughput` cost.

**Disposition:** add one sentence to §8.1 or §5(c)'s intro citing UD §4.5's
scope-vs-fold distinction, so the omission reads as a decision rather than
a gap.

---

### F-S5 — MINOR — §14 Q10's "no cross-engine canonical answer" framing understates pcrec's own precedent for growth (h)

**Cite:** `utf8_set_v1.md` §8.3, §14 Q10.

**Evidence:** `~/pcrec/tests/utf8/axis03_invalid_utf8.rxt:9-11` states its
own oracle rule in nearly the same words §8.3 uses to justify the opposite
default: *"the oracle for every case below is libpcre2 under
PCRE2_MATCH_INVALID_UTF, never plain PCRE2_UTF."* That is, pcrec's own
acceptance corpus for this exact axis already treats
`PCRE2_MATCH_INVALID_UTF` as THE canonical differential oracle against
pcrec, and has done so since promotion. §8.3's argument ("there is no
cross-engine canonical answer to be right about... RE2, Rust and Vectorscan
each have their own documented posture, none of them established in this
repo today") is true for the OTHER five engines, but for the pcrec-vs-PCRE2
pair specifically, a working, precedented differential already exists and
is running today one repository over. This doesn't necessarily change Q10's
answer (documented-behaviour-only remains the right default for the
SIX-ENGINE table §8.3 is actually about), but the framing as stated could
mislead whoever rules Q10 at (h)'s charter into thinking the pcrec/PCRE2
pair starts from the same "nothing established" position as the other four.

**Disposition:** note in §8.3 (or leave for (h)'s own charter, since Q10 is
already marked BLOCK-at-(h)) that a pcrec-vs-`PCRE2_MATCH_INVALID_UTF`
differential is not a new instrument to build — it is AX's own axis03
oracle, reusable as-is for a two-engine SECOND canonical column alongside
the six-engine documented-behaviour table, without contradicting §8.2's
"never `PCRE2_NO_UTF_CHECK`" rule (axis03 does not use it either).

---

## Confirmed-clean (no defect, checked because the lens asked)

- §7.1's roster table: every "how it is told" claim was checked against
  the cited file:line and is byte-for-byte accurate — `testees/pcre2/
  driver.c:325` (`p_compile(pat, patlen, 0, ...)`, options hard-coded to
  0), `testees/onig/driver.c:91` (`#define ONIG_DRIVER_ENCODING
  ONIG_ENCODING_ASCII`), `testees/re2/driver.cc:220`
  (`EncodingLatin1`), `testees/vectorscan/driver.c:50-59`'s UCP/`\b` A/B
  (40/64 vs 35/64, quoted correctly), `testees/rust/CLAUDE.md`'s
  unicode-mode-default-true finding. `--encoding=utf8` (not just `-e
  utf8`) is a real, second CLI spelling — confirmed at `~/pcrec/cli/
  main.c:885` (`!strncmp(a, "--encoding=", 11)`) and `:160` (help text) —
  so the doc's "UD §9.2 stage 2's own spelling" citation is accurate; my
  first pass mis-grepped and would have flagged this as a defect.
- §7.4's REFUSAL claims: TRE's `\p{L}`/`\p{Alpha}` → code 10 (`testees/
  tre/CLAUDE.md:157`), re2/rust/vectorscan's blanket lookaround refusal —
  all confirmed against the cited CLAUDE.mds.
- (c)'s fold-set semantics (`ci-kelvin`, `ci-long-s`, `ci-sigma`,
  `ci-strasse`, `ci-turkish-i`, `ci-neg-fold`, `ci-class-range`) all match
  UD §4.1-§4.3's measured cells exactly, including the closure-reaches-
  outside-range property and fold-before-negate ordering.
- (a)'s negation-universe claim (`cls-neg-single`, `cls-neg-allhigh`:
  complement within `[0, 0x10FFFF]`) matches UD §2.7.1's repair exactly,
  including the `MAXCP(enc)` formulation.
- (e)'s lookbehind var-width claims match UD §5.6's measured table
  (`PCRE2_INFO_MAXLOOKBEHIND == 1` character spanning 1-4 byte widths)
  exactly, including the `[a\x{3b1}]`-bodied witness.
- §6.3's `cls-lead-pair` "memchr can't use a two-byte lead set" claim
  matches UD §6.3's own worked row exactly (2 lead bytes, 0xCE/0xCF,
  "the single-byte arm declines and the bitmap-skip arm takes it").
- §3.3 gap 4's `-e byte` range-refusal-above-0xFF claim is confirmed
  against `~/pcrec/tests/utf8/axis01_encoded_length_byte.rxt` and
  `axis02_class_boundary_byte.rxt`'s own headers (L2/L3/L4-esc-* blocks
  "refuse ... with a RANGE error").
- §8.2's ill-formed-subject error-code enumeration matches
  `axis03_invalid_utf8.rxt`'s header exactly (9 kinds, same codes,
  correctly attributed to libpcre2 10.37, not 10.46 — the note is careful
  about this version distinction where it matters).

---

## Q9 / Q10 — argued both ways, my rule

**Q9 (shared `oracle_pcre2.py` parameter vs. a second oracle module).**
*For a second module:* a UTF-8-aware option word touches every existing
consumer of `oracle_pcre2.py` (six sets), and a bug in the shared function
risks silently re-deriving every existing set's `expectations.tsv`
differently — a blast radius a dedicated module would not have. *For the
shared parameter (the note's own recommendation):* the alternative creates
two independent implementations of "what is the oracle" that must be kept
in lockstep by hand, and `bench/syntax/NOTES.md`'s own forward-looking
note already predicted the single-parameter shape — a second module built
against that prediction would be building around a wall someone else
already tore down. **My rule: the shared parameter, with the note's own
mitigation (byte-identical re-derivation of every other set's
`expectations.tsv` under the changed oracle with no UTF option) treated as
load-bearing, not optional — it is the only thing that makes "shared code"
safe rather than merely cheap.** Agree with the note as written.

**Q10 (declare `PCRE2_MATCH_INVALID_UTF` a second canonical answer for
growth (h), or documented-behaviour-only).** *For a second canonical
column:* F-S5 above — the differential already exists, is running, and
would give (h) at least ONE ranked comparison (pcrec vs. PCRE2) instead of
zero, at no extra engineering cost. *For documented-behaviour-only (the
note's recommendation):* a two-engine "canonical" column sitting beside a
four-engine documented-behaviour table for the SAME subjects invites a
reader to treat pcrec/PCRE2's agreement as "correctness" and the other
four's disagreement as "wrongness," when actually all six are internally
consistent with their own documented contract and the whole point of §8.3
is that there is no single right answer to rank against. Mixing a ranked
column into what is otherwise explicitly a non-ranked table is also a
harness-shape complication (one section, two different scoring rules) for
a growth stage that is not chartered yet. **My rule: documented-behaviour-
only, as the note proposes — but explicitly RECORD the existing
pcrec/PCRE2 differential (AX's axis03) as a fact available to whoever
writes (h)'s ledger, not a ranked cell.** This keeps §8.3's honesty intact
while not pretending the two-engine comparison doesn't already exist
somewhere in this project's dependency tree.

---

## Witness compiles run

Two, both under a second, both confirmatory rather than diagnostic (no
built pcrec binary matching this design's own pin was invoked — none of
the findings above turned on a live compile; both were used only to
confirm CLI surface claims already found by source reading):

    build/pcrec-8d716693/build/pcrec -e utf8 --pattern '(?i)k' -o /tmp/x_r8.rx
    build/pcrec-8d716693/build/pcrec --encoding=utf8 --pattern '(?i)k' -o /tmp/y_r8.rx

Both ran under a second and exited 0. A first `cmp` showed the two outputs
differing at byte 330 — re-run with `-fcomments` to see why: the only
difference is the `#include "x_r8.rx.h"` / `#include "y_r8.rx.h"` line,
which is the OUTPUT FILENAME's own basename, an artifact of using two
different `-o` paths, not of the two encoding spellings. Confirms `-e utf8`
and `--encoding=utf8` are true synonyms — consistent with F-S1's
"confirmed-clean" list above — and is not otherwise load-bearing to any
finding.

---

## Verdict

`utf8_set_v1.md` v0.1's engine-semantics claims are, overwhelmingly,
correctly derived and correctly cited — every roster-table capability
claim, every fold/lookbehind/negation/prefilter semantic citation to UD,
and every AX header-derived axis description checked against its named
source came back accurate, which for a document making this many
file:line claims is a strong result. The two MAJOR findings are both
instances of the exact failure mode the note itself charters against in
its own R2 risk (an unconfirmed or overstated claim shipped as settled
fact): one is a citation that does not survive checking against the tool
its own source names as authoritative (the Script_Extensions "three
cells" / U+0300 claim, F-S1), and the other is a scope decision (TRE's
blanket exclusion, F-S2) that is right for most of the population it
covers but demonstrably wrong for the pure-ASCII control rows the set's
own R3 rule and Q1 ranking decision depend on most — an exclusion that
quietly weakens the set's own headline "what does the encoding cost"
question by removing an independent comparator from exactly the cells
built to answer it. Neither finding blocks the design's overall shape;
both are one-paragraph fixes (F-S1 to the citation, F-S2/F-S3 to the
REQUIRES-token grain) that should land before U2 (the roster lane) opens,
since U2 is where the TRE declaration and the token vocabulary actually
get written down.

**Counts:** 2 MAJOR (F-S1, F-S2), 1 MINOR carrying F-S2's fix (F-S3), 2
MINOR/NOTE (F-S4, F-S5). 0 BLOCKER.
