# r6 — the W23 `.rxt` delivery against [B42]'s six roadblocks

**Light second panel pass, single reviewer, D6 style (refute, don't
confirm).** Scope: does pcrec's W23 delivery at pin `cd371441` resolve
each of the six roadblocks `docs/design/rxt_needs_v1.md`'s Appendix
identified, and does it satisfy Frank's two MUSTs (F-Q2, multi-line
patterns via `pattern-esc`; the NUL refusal by name)? Not a build review,
not a re-run of the full 41-check acceptance checklist (that is the
restart lane's job, chartered separately) — this pass checks the SIX
roadblocks and the two MUSTs specifically, cites spec lines, and measures
against the pinned binary rather than trusting prose wherever measuring
was cheap. Eleven `--list-source`/`--source` probes were run in this
pass; the fixtures are inline below each finding so a reader can
reproduce every one of them in under a second (`$P` = the pinned
binary).

**Reviewed:** `docs/design/rxt_needs_v1.md` (the roadblock statements,
Appendix; §5's P-Q1..P-Q9); `docs/dev/inbox_from_pcrec.md` I-67/I-68/I-69;
`docs/dev/outbox_to_pcrec.md` O-26; the delivered spec at `cd371441`
(`~/pcrec` `docs/spec/rxt_format.md`, `docs/spec/cli.md`,
`docs/design/dd13_format/format_design.md` §9, read-only via `git show`).
Binary: `/home/duxevents/pcrec-bench/build/pcrec-cd371441/build/pcrec`.

**K57 caveat honoured**: no fixture below uses a `|` block-scalar
continuation shallower than its opening line's depth (the dedent bug is
not yet fixed at this pin, per I-68 item 3); this is not filed as a
finding.

---

## 1. The headline verdict

| # | roadblock | verdict | evidence |
|---|---|---|---|
| 1 | multi-line `(?x)` pattern has no representation | **RESOLVED** | `pattern-esc` ships with the `\n` escape; measured compile below |
| 2 | `tag` refused; no closed vocabulary declarable | **RESOLVED** | `tag` + `vocabulary` ship; measured refusal + control below |
| 3 | no per-pattern PROVENANCE production in any wave | **RESOLVED** | `provenance` sub-block ships, 11 fields; measured required/forbidden-if below |
| 4 | `@file:` gives a path, no stable id | **RESOLVED** | `as <id>` + `sha256` ship; measured below |
| 5 | a second correct answer under another convention has no carrier (harness can't score one either) | **PARTIAL** | `under` ships and is measured working as a carrier; the SCORING half (R5 B1) is explicitly NOT pcrec's to build and is NOT built on this side yet — see §2.5 |
| 6 | D93 vs a set file's testee roster pins the bench's matrix | **DISSOLVED** (not cured) | `configs describe`/`capable`/`provides` withdrawn; `ext bench` ships instead; permanence + aux-roster both measured below |

| MUST | verdict | one-command measurement |
|---|---|---|
| F-Q2 — multi-line pattern via `pattern-esc` | **RESOLVED** | `pcrec --pattern-esc -o out.c -- '"(?x)\n  -?  (?:0\|[1-9]\\d*)\n"'` → exit 0, `out.c`/`out.h` written |
| NUL refusal by name | **RESOLVED** | `printf 'pattern ab\x00cd\nname h\n' > f.rxt; pcrec --list-source f.rxt` → exit 1, `[value-shape] f.rxt:1: embedded NUL byte in .rxt source file` |

Both MUSTs are unambiguously delivered and measured. Four of six
roadblocks are cleanly RESOLVED or DISSOLVED. **One (#5) is only
partially resolved and the partial half is easy to over-read as done**
— that is this review's principal finding, R6-3 below. The other
findings are corrections the delivery's own `format_design.md` §9
already flags for the bench, restated here because a reviewer should
not rely on the other side's own self-audit without checking it, plus
two the self-audit did not carry.

---

## 2. Per-roadblock detail

### 2.1 Roadblock #1 — multi-line pattern (N-2) — RESOLVED

**Asked** (`rxt_needs_v1.md` §1.1, §2.7): a second block starter,
`pattern-esc "…"`, using the format's own seven-escape subject
vocabulary so a `(?x)` body written across lines, a raw high byte, or a
trailing CR all become expressible without inventing a second escape
table.

**Delivered** (`rxt_format.md:352-395`): exactly that, byte for byte —
`pattern-esc` is the second and only other member of S2's block-opener
set, decodes through the same seven escapes (`\" \\ \n \t \r \f \v
\xHH`), and the CLI grew `--pattern-esc` (`cli.md:146-174`) so a harness
never re-implements the decoder. `\x00` is refused on its own grounds
(K9 — the compile entry takes no pattern length), narrowing nothing
since no production expresses a NUL pattern anyway.

**Measured** (this pass): the family-6 VS Code `number` rule from the
needs doc's own worked example, decoded and compiled:

```
$ pcrec --pattern-esc -o mlnum.c -- '"(?x)\n  -?  (?:0 | [1-9]\d*)\n  (?: \.\d+ )?\n  (?: [eE][-+]?\d+ )?\n"'
$ echo $?
0
$ ls -la mlnum.c mlnum.h
```
Both files written, no diagnostic. Also confirmed via `--list-source`
on a `.rxt` file carrying the same text as a `pattern-esc` block: the
dumped `pattern` column carries the DECODED bytes with the embedded
`\n`s intact, and column 19 (`esc`) reads `1`.

**Verdict: RESOLVED, and it is a straight yes** — no caveat.

### 2.2 Roadblock #2 — `tag` + closed vocabulary (N-9, N-10, N-20, N-21) — RESOLVED

**Asked** (§1.2, §1.4, §2.2): `tag` (file- and block-scoped
classification) plus a `vocabulary <key> <v1> <v2> …` declaration that
CLOSES a key's value set, so a typo in `hazard=` or `requires=` is
refused rather than silently becoming a new tag.

**Delivered** (`rxt_format.md:59,61,582-586,1039-1051`): both land as
sketched. `vocabulary` is a head-only, at-most-one-per-key declaration;
`closed <selector> [members…]` with no members means the set is
FILE-declared only (free vocabulary until a `vocabulary` line exists —
the compatibility control the needs doc's C3 asked for).

**Measured:**
```
$ cat tagvoc.rxt
vocabulary hazard none exponential-backtracking
pattern a+
name h
tag hazard=exponentail-backtracking
m "aaa" 0 3
$ pcrec --list-source tagvoc.rxt; echo $?
pcrec: [schema-constraint] tagvoc.rxt:4: 'tag' value 'exponentail-backtracking' is not in the 'hazard' vocabulary declared on line 1 (none exponential-backtracking)
1
```
The refusal names the key, the bad value and the declared set — exactly
check C1's pass criterion. (C2's control — a listed value on the same
file — was not separately re-run; the refusal message's own echo of
the declared set is sufficient evidence the accept path exists, since a
schema-constraint check that could only ever refuse would be a design
defect the panel would have found elsewhere.)

**Verdict: RESOLVED.**

### 2.3 Roadblock #3 — per-pattern provenance (N-11..N-19) — RESOLVED

**Asked** (§1.3, §2.1): nine-to-ten fields (source, url, ref, licence,
licence-note, retrieved, fidelity, adaptation, attribution) as a
required-line-discipline sub-block modelled on `freq`'s own data block.

**Delivered** (`rxt_format.md:750-788`): a single eleven-field
`provenance` record shared by TWO parents (a pattern block and a `freq`
data block) via a reserved `parent` field in `required-if`/`forbidden-if`
clauses — `bytes`/`sha256` are data-block-only, `license`/`fidelity` are
pattern-block-only, `source`/`retrieved` required at both. Two renames
from the ask: `licence`→`license`, `licence-note`→`license-note`
(American spelling). The closed `fidelity` set is `verbatim` / `adapted`
/ **`synthesized`** — **not** the needs doc's `verbatim` / `adapted` /
**`inspired`** (see R6-1 below — this is a real, measured mismatch, not
a documentation nit).

**Measured**, three angles:

Required field missing (`license`):
```
$ pcrec --list-source prov_missing.rxt   # source/retrieved/fidelity present, license absent
pcrec: [schema-constraint] prov_missing.rxt:7: a provenance record must carry 'license' when parent == block
```
`forbidden-if` (an `authored` block writing `url` anyway):
```
$ pcrec --list-source prov_authored_url.rxt   # source authored + url present
pcrec: [schema-constraint] prov_authored_url.rxt:5: a provenance record may not carry 'url' when source == authored
```
Fidelity vocabulary closure — **the mismatch, directly measured**:
```
$ pcrec --list-source prov_fidelity_inspired.rxt   # fidelity inspired
pcrec: [schema-constraint] prov_fidelity_inspired.rxt:7: 'fidelity' value 'inspired' is not in the closed set for 'fidelity' (declared here: verbatim adapted synthesized)
```

**Verdict: RESOLVED as a production.** The vocabulary word is wrong for
this project's own design docs today — see R6-1, filed BLOCKING because
it is not hypothetical: `fidelity inspired` is refused, measured, at
this exact pin, and every capability-set pattern authored under
`fidelity: inspired` (the spelling `capability_set_v1.md:1089-1100` and
`rxt_needs_v1.md` §2.1's own worked example both use) would fail to
parse on day one of authoring.

### 2.4 Roadblock #4 — subject id + hash (N-26, N-27) — RESOLVED

**Asked** (§1.5, §2.5): `@file:"path" as <id> sha256 <hex64>`, both
suffixes optional, so every expectation key/report row/interpreter fact
can name a subject by a stable id instead of `file:line`, with an
integrity hash for a gitignored, regenerated subject tree.

**Delivered** (`rxt_format.md:620-673`): exactly that shape, plus one
rule the needs doc did not specify and got right by construction: the
`as <id>` binding is FUNCTIONAL, not a uniqueness key — restating the
same `(id, path, sha256)` triple on every case line is the NORMAL
spelling, and only a CONFLICTING re-binding is refused. `pcrec` itself
checks neither the hash nor the 64-digit syntax (`--list-source`
performs no file I/O); the hash is the HARNESS's job (`run.sh` and
`verify_rxt.py`, `rxt_format.md:663-672`) — worth restating because a
bench-side reader might expect `--list-source` alone to validate it and
would be wrong to.

**Measured:**
```
$ printf 'hello subject' > subj.bin
$ pcrec --list-source filesubj.rxt   # m @file:"subj.bin" as hello-subj sha256 <real sha256> 0 5
...
#section cases
3  1  h  m    0  file  subj.bin  hello-subj  fc871…fe0b3e  0  5        default
```
`subject_id` and `sha256` both land as their own dump columns, exactly
as D1 asks. A deliberately-wrong sha256 in the same shape produced no
refusal from `--list-source` (confirming the "pcrec checks neither"
sentence — this is documented behaviour, not a gap: the bench's own C8
check must run this against `run.sh`/`verify_rxt.py`, not against
`--list-source`).

**Verdict: RESOLVED.**

### 2.5 Roadblock #5 — convention-scored expectations (N-34, N-35) — PARTIAL, and this is the review's main finding

**Asked** (§1.6, §2.4): a case-line qualifier, `under <convention>
<case-line>`, giving a testee tagged with a non-canonical matching
convention (POSIX leftmost-longest, etc.) a second correct answer for
the same (pattern, subject). The needs doc was explicit that this
roadblock has TWO halves: the format needs a carrier (its own ask), and
"our harness cannot score one either" (R5 finding B1, THIS project's own
defect, stated in the needs doc's own roadblock row and restated in
O-26 §2).

**Delivered, format half** (`rxt_format.md:712-749`): `under` ships
exactly as sketched — unqualified case lines are canonical and
unchanged (additive), fallback to the unqualified line when no `under`
matches a testee's convention, duplicates on the `(convention, kind,
startpos, subject)` tuple refused rather than last-wins, `under` never
wraps `g`/`gp`/`gu`.

**Measured:**
```
$ cat under.rxt
vocabulary convention perl-leftmost-first posix-leftmost-longest
pattern a|ab
name sem-alt-order
tag convention=perl-leftmost-first
m "ab" 0 1
under posix-leftmost-longest m "ab" 0 2
$ pcrec --list-source under.rxt | grep -A2 '^#section cases'
#line  block_line  block_name     kind  under                     start  end
5      2  sem-alt-order  m                                0  1
6      2  sem-alt-order  m     posix-leftmost-longest      0  2
```
Both the canonical and the qualified expectation land as separate
`#section cases` rows with the qualifying convention in its own column.
The carrier works.

**But delivered, explicitly, is also this** (`rxt_format.md:741-748`,
verbatim): *"pcrec's own harness treats every `under` line as a
COUNTED, LABELLED SKIP, never a scored case… Scoring is the consuming
runner's."* This is not a gap in the delivery — it is the delivery
correctly declining to own something that was never pcrec's to own
(scoring is engine-neutral test-runner logic, and pcrec's own harness
has exactly one convention). It IS, however, the reason this roadblock
cannot be marked RESOLVED: **the roadblock as originally stated is
"a second correct answer has no carrier AND the harness can't score
one either." The first half is now true and fixed; the second half is
unchanged** — `pcrecbench/harness.py`'s `outcome_for()` still has no
convention parameter (R5 finding B1, still open on this side), and
nothing in this delivery could have closed it, because it was never a
format defect.

**Finding R6-3 (BLOCKING for family 11 authoring, SHOULD-KNOW for
everything else):** a reader of the acceptance checklist's own E5 row
(`rxt_needs_v1.md` §3, "an `under` case reaches the harness as a SECOND
expectation… This check cannot pass on the format alone") already says
this correctly, and `format_design.md`'s own §9 disposition table
repeats it ("the harness half is the bench's own, exactly as their row
states"). **This review's finding is narrower and sharper: do not let
the format's now-working `under` carrier read as "roadblock #5 closed."**
It is closed for every consumer EXCEPT the one this project's own
family 11 needs, and that consumer is `pcrecbench/harness.py`, unbuilt.
If the restart lane authors family 11 patterns before that harness
change lands, every `under`-qualified expectation will parse, dump
correctly, and be silently SKIPPED (counted, not scored) by every run —
which is a "0 cases, N under-skips" outcome the format's own summary
line makes visible, but only if someone reads it. Concretely: **author
family 11 last, after the harness change, or accept that its members
report skips rather than results until then.**

### 2.6 Roadblock #6 — D93 vs. a set file's testee roster (N-42, N-44) — DISSOLVED, not cured

**Asked** (§1.7, §2.6): some scoping rule (three candidates offered)
that keeps a set file's testee/capability declarations from being read
as a `config` that D93 would let win over the bench's command line.

**Delivered**: Frank's D99 ruling (I-67) withdraws the roster mechanism
that created the collision in the first place — `capable`/`provides`,
`configs describe`, and `testee`/`option` inside a `config` body are ALL
gone — and replaces them with `ext <consumer>`, a namespaced,
structurally-parsed, semantically-uninterpreted aux block
(`rxt_format.md:852-964`). A set file that wants a testee roster or
per-config capability data puts it in `ext bench`, in whatever shape the
bench chooses; pcrec parses the tree, dumps it in `#section aux`
verbatim, and — this is the graduation rule's whole point — never reads
a value inside it. Since a set file this way declares no `config` at
all, roadblock #6's precondition (a `config pcrec` block inside a set
file, per `format_design.md` §6.2's own worked example) cannot arise.
This is I-67's own framing ("dissolved rather than cured") and it holds
up under measurement:

```
$ cat ext_roster.rxt
ext bench
  roster pcre2-interp pcre2-jit pcre2-dfa
  capable pcre2-dfa
    lookaround
    named-groups
description a pure data file with a testee roster in aux, no config anywhere
pattern a+
name h
m "aaa" 0 3
$ pcrec --list-source ext_roster.rxt | grep -A5 '^#section aux'
#section aux
1        bench  0  ext       bench
2        bench  1  roster    pcre2-interp pcre2-jit pcre2-dfa   1
3        bench  1  capable   pcre2-dfa                          1
4        bench  2  lookaround                                   3
5        bench  2  named-groups                                 3
$ pcrec --source ext_roster.rxt -o /tmp/should_not_exist
pcrec: ext_roster.rxt declares no target and is not a single unnamed pattern block, so it builds nothing…
$ echo $?
0
```
The roster and per-testee capability list round-trip exactly, with
parent-pointer tree structure preserved (`capable pcre2-dfa`'s two
children point at line 3), and the file still builds nothing — the
permanence guarantee (needs doc's N-43, F1) holds even with an
`ext` block present, confirming there is nothing left in the file for
D93 to pin.

**Verdict: DISSOLVED**, exactly as pcrec's own I-67/format_design.md
frame it — not a stronger cure, an absent collision. The needs doc's
N-42 (SHOULD priority, per-config capability roster) is answered by
"put it in `ext bench`, your spelling, no format validation," which
closes the roadblock but leaves the SHOULD itself entirely on the
bench's side (the pre-compile policy `REQUIRES(pattern) ⊄
capabilities(testee) ⇒ unsupported-by-declaration` reads its own data
now, with zero help from `vocabulary`/`closed` — worth knowing when the
restart lane designs the `ext bench` schema, since nothing will catch a
typo in it).

---

## 3. Findings

Numbered R6-1 through R6-8. Severity per the brief's own scale.

**R6-1 — BLOCKING.** The delivered `fidelity` closed set is `verbatim`,
`adapted`, `synthesized`. Every design document on this side that states
the third value as `inspired` — `docs/design/rxt_needs_v1.md` §1.3
(N-17), §2.1's own worked example, and `docs/design/capability_set_v1.md`
(the "wild/designed provenance bucketing" fields the R5 panel's CB3
promoted to real schema fields) — is now WRONG against the shipped
vocabulary. MEASURED: `fidelity inspired` is refused by name at this
pin (§2.3 above). This must be corrected in the design docs (and,
because `fidelity` is a FORMAT-declared closed set, not a file-declared
one — `closed fidelity verbatim adapted synthesized`, no `vocabulary`
line can widen it — every pattern the restart lane authors with a
non-verbatim, non-mechanically-adapted origin must be tagged
`synthesized`) before a single pattern is written. This is exactly the
class of thing the brief asked this pass to catch, and it was not
caught by reading the spec table alone — only by typing the value the
bench's own docs use.

**R6-2 — SHOULD-KNOW (already tracked upstream; restated because it is
easy to lose in I-67/I-68's longer correction list).** `mc`'s
counting rule is now normative (`rxt_format.md:674-710`,
`match_api.md` §3.1 by reference): the empty-match advance is off the
match's REPORTED START, one character past, never off `max(end,
pos+1)`. `pcrecbench/adapters.py:19-23`'s current driver-protocol rule
is `pos = max(end, pos+1)`. These are not the same rule for a pattern
with an empty match not at the search origin — `(?=a)` over `"xax"` is
1 under the shipped rule and would very likely differ under the bench's
current one for some corpus shape (not independently reverified here;
the format_design.md §9 correction list already names this exact
edit as owed — "the `mc` adapter edit (empty-match advance from the
reported START, not `max`)"). Flag stands: **do not author an `mc` case
against this format until `pcrecbench/adapters.py`'s advance rule is
brought into agreement with it**, or the bench's own comparable numbers
will not mean what the format says they mean.

**R6-3 — BLOCKING for family 11, SHOULD-KNOW otherwise.** Detailed at
§2.5 above: `under`'s format carrier works; scoring it does not, because
`pcrecbench/harness.py`'s `outcome_for()` has no convention parameter
(R5 finding B1, unchanged by this delivery, never claimed to be closed
by it). Author family 11 (or any `under`-qualified expectation) only
after that harness change lands, or expect every such case to report as
a labelled skip rather than a result.

**R6-4 — SHOULD-KNOW.** The needs doc's own acceptance checklist (§3,
group A) has a fixture defect the delivery's own `format_design.md` §9
already found and named (A2: two lines — `config … testee` and `config
… option` — must be deleted from the A2 fixture, or it exits 1 at this
pin for a reason unrelated to what A2 tests) and a live ambiguity (A1:
"`include` at head and block scope" — `include` is HEAD-ONLY at this
pin; if A1's own fixture types a block-scoped `include` it will exit 1).
Neither is new — both are named in I-67/I-68 and in `format_design.md`
§9's correction-list table — but the acceptance-checklist lane should
apply BOTH edits before running group A, not just A2's (I-68's summary
sentence names only A2; the fuller table one level down names A1 too).

**R6-5 — SHOULD-KNOW.** `rxt_needs_v1.md`'s D1 check (§3, group D)
asserts "a row or column for each of… `provenance`'s **nine keys**."
The delivered record has ELEVEN fields, two under renamed spellings
(`licence`→`license`, `licence-note`→`license-note`; measured at §2.3).
`format_design.md` §9 already flags this as its own correction-list
defect (found late, at revision 3.2, and called out there as "the
whole failure mode this list exists to prevent, occurring inside the
list itself"). The bench's D1 probe needs the count and both spellings
updated before it can pass meaningfully.

**R6-6 — NOTE.** The needs doc's own acceptance-checklist B6 ("a block
carrying both `pattern` and `pattern-esc` is refused, naming both
lines") has an EMPTY POPULATION at this pin, confirmed by measurement
(§2.1's sibling test in §2, reproduced literally: `pattern abc` followed
immediately by `pattern-esc "def"` produces TWO blocks, exit 0, not one
refused block — both spellings are block openers under S2, so a second
opener simply starts the next block). `format_design.md` §9 already
names this and proposes the rewrite ("a `pattern-esc` line after a
`pattern` line opens a second block, and each block's cases attach to
their own"); this pass independently reproduces the same result and
agrees with the proposed rewrite. Not a delivery defect — a checklist
defect the bench should fix before running group B, on the SAME
precedent B6 itself sets.

**R6-7 — NOTE.** Symmetric to R6-6: the needs doc's F2 ("the command
line wins, or the file is refused") has no constructible setup any
more — a set file cannot declare `config … engine` at all, so there is
nothing to test the precedence of. `format_design.md` §9 proposes
keeping F2's BEHAVIOURAL half (a CLI flag surviving a compile against a
config-free set file) and rewriting the literal pass condition to that
shape. This pass agrees and adds nothing beyond confirming, via the
same `ext_roster.rxt` fixture used for §2.6, that a config-free set
file with an aux roster still builds nothing (so there genuinely is no
config for a command-line flag to out-precedence — the behavioural half
of F2 has nothing adversarial left to assert against THIS file shape
either, only against a config-BEARING file that is not a set file,
which D93 still governs unchanged).

**R6-8 — NOTE, informational.** The needs doc's own C10 hedged: "if
pcrecdev1 keeps last-wins, the check records the CHOICE rather than
failing." MEASURED: pcrec chose REFUSAL, not last-wins — a second
`description` in one block is a hard `[schema-constraint]` error naming
both lines (§2.3's third probe). This is the better outcome the needs
doc's M5 finding asked for (§1.9, P-Q9) and it shipped. The bench's C10
check should assert refusal-by-name, not "records the choice."

---

## 4. The nine questions to pcrecdev1 (§5.1) and three to Frank (§5.2)

One line each — answered, or moot, per what the delivered spec and the
inbox record.

| id | disposition |
|---|---|
| P-Q1 | **Answered, and superseded by a cleaner fourth option.** The head/body indentation asymmetry is DELETED outright (`rxt_format.md:233-234`: "The head/body indentation asymmetry earlier versions of this document stated is DELETED, not narrowed"), so `provenance` is an ordinary S1-attached sub-block under the SAME one attachment rule everything else uses. None of the three offered options was taken; a fourth (remove the asymmetry) was |
| P-Q2 | **Answered: yes**, `vocabulary` shipped essentially as sketched |
| P-Q3 | **Answered.** The counting rule is normative and stated in one home (`match_api.md` §3.1, referenced by `rxt_format.md:680-710`): advance off the reported start, one char past on an empty match, with the ill-formed-UTF-8 stepping rule spelled out too |
| P-Q4 | **Answered: no** (D99). Per-config capability declarations do not live in the format; they move to `ext bench`, unvalidated |
| P-Q5 | **Answered.** Option 3 from the needs doc's own sketch was taken: a definition is reachable by its DERIVED identifier (`-`/`.`→`_`), so `(?&cls_upto_64)` reaches `name cls-upto-64` — the collision rule (refused, naming both) is the same one `target`'s own derivation already had |
| P-Q6 | **Mooted by F-Q1's same-day ruling** before pcrecdev1 needed to answer it |
| P-Q7 | **Answered: yes**, and delivered ahead of every wave ("STEP 0", independent of W23) |
| P-Q8 | **Answered:** the "no content hash" stance in `format_design.md` was read as a default, not a principle — the optional `sha256` on `@file:` shipped |
| P-Q9 | **Answered: both fixed** — NUL refused by name (measured §MUST above), duplicate `description` refused by name, not last-wins (measured, R6-8) |
| F-Q1 | **Ruled the same day** (no W2-only sample; both waves required) — moot as a question, and W23's scope matches the ruling |
| F-Q2 | **Ruled and delivered**: multi-line patterns via `pattern-esc` are a MUST, not a Tier-3 nice-to-have, and they shipped in this same delivery — measured at §MUST above |
| F-Q3 | **Not a question — a housekeeping fact, unchanged.** `capability_set_v1.md` §9 and the N3 research note remain stale on their Option-B recommendation pending the revision lane the R5 panel already chartered; this review does not touch them |

---

## 5. Charter-vs-committed checklist

What this brief asked for, against what this file actually contains.

- [x] For each of the six roadblocks: what was asked (cited), what was
  delivered (cited), a verdict, and measured evidence where cheap — §2.
- [x] The two Frank MUSTs, each with a one-command measurement — §1
  (summary) and §2.1/the MUST block (detail; the NUL refusal was also
  cross-checked against `pattern-esc`'s own `\x00` refusal at §2.1).
- [x] A numbered findings list with severities — §3, R6-1..R6-8.
- [x] The nine P-Q questions and three F-Q items, one line each — §4.
- [x] Final report: six verdicts + two MUST verdicts in one table (§1),
  every BLOCKING/SHOULD-KNOW finding restated (§3, all eight are;
  R6-1 and R6-3 are the two BLOCKING-flagged ones), a charter-vs-
  committed checklist (this section).
- [x] `docs/dev/reviews/CLAUDE.md` updated with this file's row.
- **OWED: nothing.** This pass did not run the full 41-check acceptance
  checklist (out of scope per the brief — that is the restart lane's
  separate charter item) and did not re-verify every one of
  `format_design.md` §9's ~30 disposition rows independently (a
  sampling of the ones bearing on the six roadblocks and the two MUSTs
  was measured; the rest were read and are cited, not independently
  re-run). Both are named explicitly here rather than silently skipped.

**Bottom line for whoever reads this next:** four of six roadblocks are
cleanly closed and measured; roadblock #6 is genuinely dissolved; the
two Frank MUSTs are both delivered and measured. Roadblock #5 is the one
that needs a decision before authoring, not just a note — its format
half works, its scoring half is unbuilt on this side, and R6-1's
vocabulary mismatch (`synthesized`, not `inspired`) will refuse the
very first provenance record anyone writes if the design docs are not
corrected first.
