# The UTF-8 encoding set — design, v0.1

**Plan row `[B77]`. Frank's charter, relayed as inbox `I-90`
(2026-09-22 ~23:4x, pcrec manager; `docs/dev/inbox_from_pcrec.md`).**
STATUS: **v0.1 — PROPOSED, DESIGN ONLY.** Nothing is built. No file
under `bench/`, `schema/`, `pcrecbench/`, `testees/` or `store/` is
touched by this note or by the lane that wrote it. `bench/utf8/` does
not exist and this note does not create it: the build lanes open after
the design panel, per `capability_set_v1.md`'s own precedent (§11's lane
plan opened only after R5).

**Frank's word, verbatim in substance** (I-90's own quotation): *"Build
the utf bench. But make it somewhat complete, not 'small' — or at least
specify that it will grow. It should, at least eventually, exercise any
functionality which might be affected by encoding. Classes come to
mind."*

## How to read it

The shape is `docs/design/capability_set_v1.md`'s, which I-90 names as
the model: numbered sections, a family table with per-member ids, R-/P-
numbering for the outlier rule and the predictions, a roster-restriction
table, an explicit oracle chain, and a question list where a decision is
genuinely someone else's. Every decision states its alternatives and why
this one; every open choice carries a RECOMMENDATION and the consequence
of each answer.

Facts about pcrec are cited from ~/pcrec by `file:line` or by section;
~/pcrec is READ-ONLY from here (BD2) and nothing in it was modified.
Facts about this repo's own adapters are cited the same way and were
read, not assumed. Where a claim is UNCONFIRMED it says so and names the
witness that would settle it, in the house style (`capability_set_v1.md`
§5.1's `†`/UNCONFIRMED rows).

| short form | file |
|---|---|
| **I-90** | `docs/dev/inbox_from_pcrec.md`, item I-90 |
| **UD §x** | `~/pcrec/docs/design/utf8_design.md` (the [M5.0] UTF-8 design) |
| **FP §x** | `~/pcrec/docs/design/reqbyte_freq_pick.md` (at `main` c051a69b) |
| **AX** | `~/pcrec/tests/utf8/` — `CLAUDE.md` and the twelve `axisNN_*.rxt` headers |
| **CAP §x** | `docs/design/capability_set_v1.md` v0.2 |

---

## 1. The charter restated, and where each clause is satisfied

I-90's five charter clauses, verbatim in substance:

1. NAME `utf8`; `capability`'s shape (a `patterns.rxt` with families,
   derived `.rx` exports, expectations from the PCRE2 10.46 oracle
   compiled with `PCRE2_UTF`, regimes `throughput` + `search_short`, the
   D119 bar per cell, the 13-engine roster RESTRICTED to the engines
   that speak UTF-8 — say which do and how each is told).
2. SUBJECTS are UTF-8 TEXT, several scripts, because the whole point is
   a byte histogram unlike English: Latin-1-Supplement-heavy (fr/de/es),
   Cyrillic, CJK, mixed with emoji/symbols, plus one byte-clean ASCII
   control; the throughput sizes `capability` uses (64k/256k/1m) with
   committed sha256 manifests; the `search_short` subjects derived per
   family as `capability` derives them; provenance recorded.
3. PATTERN FAMILIES — "any functionality which might be affected by
   encoding"; the first release ships at least (a)-(f), and the file's
   header names the rest as the GROWTH PLAN with a version per stage
   (g)-(k).
4. pcrec TESTEES: the usual four, all compiled `-e utf8` (and the mirror
   arm under `-e byte` for (k)); pin = main at the time of the first run.
5. FIRST CUSTOMERS, said in the ledger: the offset-skip rows, the
   required-byte rows whose necessary byte is a high byte, and (c)'s
   fold sets.

### 1.1 Traceability

| clause | satisfied by | in one line |
|---|---|---|
| (1) name, shape, roster restriction | **§2, §7, §8, §10** | `bench/utf8@0.1`, built on `patterns.rxt` exactly as `bench/capability` is; a per-engine UTF-8 surface table with the adapter change priced per engine; the oracle chain stated as a rule, not a habit |
| (2) subjects | **§4** | five script corpora, deterministically generated from committed per-script word pools, sha256-manifested; 90 short subjects typed per family; a 64k/256k/1m mixed sweep plus a per-script 64 KB arm; the byte-histogram claim stated as the thing the set actually asserts |
| (3) families + growth | **§5** (the six first-release families, 73 members + floor), **§6** (growth (g)-(k), a version each), **§3** (the twelve-axis coverage spine, with its gaps named) |
| (4) pcrec testees | **§7.2** | four `-e utf8` configs on the existing `flags` mechanism, which is how the encoding becomes part of `testee_id` rather than an invisible run-time choice; the `-e byte` mirror scoped to growth (k) and kept a TESTEE fact, never a set fact (§9) |
| (5) first customers | **§11** | ten predictions, P1-P10, each written so `pcrecbench interpret` can score it; the TSV is NOT committed here (§11's own immutability note) |

Two cross-cutting sections carry no single clause: **§12** (the outlier
rule, stated before any run) and **§13** (the build plan), **§14** (the
questions), **§15** (the risks).

---

## 2. Set identity

**DECISION: a new sub-bench, `bench/utf8/`, sidecar `id = "utf8"`,
version `0.1`.**

### 2.1 The alternatives

| option | what it means | why not |
|---|---|---|
| **A. `bench/syntaxutf/`, the reserved slot** | `bench/syntax/NOTES.md`'s "Room for a utf family" reserves exactly this name for a UTF sibling of the syntax census | rejected — §2.2 |
| **B. `bench/utf8/`, a new set** | a seventh directory under `bench/` | **CHOSEN** |
| **C. a version bump of `bench/syntax@0.1`** | add a UTF family to the census | rejected for the reason that `NOTES.md` section already gives: the census's subjects are bytes and its oracle binding is byte-oriented, so a UTF family inside it would need two oracle bindings in one `expectations.tsv` — and `bench/syntax`'s defining discipline, that `coverage.tsv` is DERIVED from the pattern table × the `--list-syntax` seed, does not extend to a set whose members are chosen by ENCODING DEPENDENCE rather than by registry row |
| **D. several sets, one per script** | `bench/utf8latin/`, `bench/utf8cjk/`, … | rejected — the script is a SUBJECT axis, not a set axis. Splitting it triples the generator/manifest/expectation surface and makes the one question the set exists to answer ("does the byte histogram move the mechanism?") a cross-set comparison instead of a within-set one |

### 2.2 Why not the reserved `bench/syntaxutf/` slot

`bench/syntax/NOTES.md`'s "Room for a utf family" reserves
`bench/syntaxutf/` and describes it as the census re-read under UTF: the
same registry seed, the same `encoding-bytes`/`encoding-utf8` tag pair,
"the seed's rows re-read with `status`/`family` unchanged and the
utf-only rows moving from `not-exercised` to `covered`."

That is a DIFFERENT set from the one I-90 charters, and both are
legitimate:

1. **`syntaxutf` is enumerated; `utf8` is not.** `syntaxutf`'s
   population would come from pcrec's `--list-syntax` seed — its
   completeness claim is "every registry row accounted for". This set's
   population comes from ENCODING DEPENDENCE — its completeness claim is
   "every one of the twelve axes in `~/pcrec/tests/utf8/` accounted for,
   or its absence stated" (§3). A registry row and an encoding axis are
   not the same enumeration, and a set cannot make both claims about one
   pattern table without one of them going soft.
2. **`syntaxutf`'s bodies are the census's plain ones; this set's are
   not.** The census's discipline is one construct in an otherwise plain
   body from one small vocabulary. `[a-é]`, `(?i)straße` and
   `\p{Greek}` vs `\p{sc=Greek}` are not one construct in a plain body —
   they are the ENCODING's own behaviour, and several of them (the
   Script/Script_Extensions pair, the fold-closure-reaches-outside case)
   are only visible as a PAIR.
3. **The subjects differ in kind.** `syntaxutf` would re-read the
   census's own `censustext.py` grammar transcoded; this set's whole
   point is five script corpora with five different byte histograms
   (I-90 clause 2).

**DECISION: `bench/utf8/` is built; `bench/syntaxutf/` stays reserved
and unbuilt, and `bench/syntax/NOTES.md`'s "Room for a utf family"
section gains one sentence pointing here so a reader does not build the
same set twice.** Retiring a documented reservation outright is a
ruling, not a design choice — **§14 Q5**, and the recommendation is to
keep the reservation rather than retire it: the two sets answer
different questions and `syntaxutf` remains the cheaper of the two to
build later, on this set's own machinery.

### 2.3 The name and version

`bench/utf8/`, id `utf8`, version `0.1`.

- Directory name and sidecar id deliberately identical, so
  `--subbench utf8` resolves either way (OD-B13, closed at [B9]).
- `0.1` because every existing set opened at `0.1` and the version is a
  frozen snapshot bumped on any pattern/subject/expectation change
  (`requirements.md §5`). The growth stages of §6 each name their own
  version.
- The id is one word, like every other (`email`, `loglines`, `bounded`,
  `altwide`, `syntax`, `capability`).

### 2.4 Relationship to the six existing sets — cite, never duplicate

`capability_set_v1.md` §2.4's rule, applied: **a mechanism a depth set
already measures to the rung is CITED in `NOTES.md` and is not a family
here.** Where this set touches such a mechanism it does so for a reason
the depth set structurally cannot serve — namely that the depth set is
byte-mode and this one is not.

| existing set | what it owns | what `utf8` may still do, and why |
|---|---|---|
| `bench/syntax@0.1` | the construct census, registry-enumerated, byte mode | **the same constructs under `-e utf8`, but only where the ENCODING changes the answer.** A construct whose behaviour is identical under both encodings is the census's, not this set's |
| `bench/altwide@0.2` | alternation width as a ladder, 8..4096 | **no ladder.** §5(d) carries ONE 64-branch Cyrillic alternation as a bridge rung, so a reader can place the utf8 alternation cost against `altwide`'s own curve. Width is altwide's |
| `bench/bounded@0.3` | counted repeats, a rung ladder to 65535, refusal first-class | **no ladder.** §5(d) carries three counted repeats over multi-byte units (2-, 3- and 4-byte) as the encoded-length reading of a counted repeat, not as a count axis |
| `bench/loglines@0.1` | mostly-failing search text, the required-code-unit axis | **the required-BYTE axis under a non-English histogram** — which is I-90's whole reason for existing (FP §3.2's inversion). loglines owns the mechanism in English ASCII; this set owns what happens to it when the histogram moves |
| `bench/email` | one real-world family in depth | **nothing** |
| `bench/capability@0.1` | cross-engine capability contrast, wild provenance | **nothing at the capability grain.** This set reuses capability's `REQUIRES`/`unsupported-by-declaration` MACHINERY (§7.4) and adds three tokens to its vocabulary; it does not re-measure its families |

**Consequence if this rule is broken:** the set becomes "the six other
sets, transcoded", which measures the transcoding and nothing else.

---

## 3. The twelve encoding-dependence axes — the coverage spine

I-90 clause 3's closing sentence: *"pcrec's `tests/utf8/axis01-12` name
the twelve encoding-dependence axes we test for CORRECTNESS; the
subbench measures SPEED on the same axes."* That sentence is this set's
completeness claim, and this section is where it is made checkable.

### 3.1 The twelve axes, by name

Read from each file's own header comment in `~/pcrec/tests/utf8/`.

| axis | file | the property it pins |
|---|---|---|
| **1** | `axis01_encoded_length.rxt` | ENCODED LENGTH: a construct's unit is one CHARACTER (1-4 bytes), not one byte — sixteen pattern shapes × four byte-widths. `.` matches one character; a literal of width *w* costs *w* bytes |
| **2** | `axis02_class_boundary.rxt` | THE 1-BYTE ↔ MULTI-BYTE CLASS BOUNDARY: ranges, classes and negations spanning it (`[a\x{3b1}]`); a class wrapping a multi-byte literal is BYTE-DECOMPOSED under `byte` and is not under `utf8` (the mirror's own discriminator) |
| **3** | `axis03_invalid_utf8.rxt` | INVALID UTF-8: nine ill-formed kinds × three positions (before / after / THROUGH the bad bytes). pcrec's ruling (UD §2.6): an ill-formed sequence matches NOTHING — no validation pass, no error return; PCRE2's equivalent is `PCRE2_MATCH_INVALID_UTF`'s barrier answer, never plain `PCRE2_UTF` (which refuses the whole subject) |
| **4** | `axis04_p_categories.rxt` | `\p{...}`/`\P{...}` GENERAL CATEGORIES: 37 accepted spellings × 2 polarities × 2 focus shapes |
| **5** | `axis05_p_refusals.rxt` | `\p` REFUSALS: 34 well-formed-but-unknown property bodies that PCRE2 10.46 itself refuses with error 147 — permanent refusals, one case each |
| **6** | `axis06_caseless_fold.rxt` | CASELESS FOLD: cross-block pairs, non-folds, the fold CLOSURE (which reaches outside the written range — UD §4.2), and fold-before-negate |
| **7** | `axis07_caseless_1ton.rxt` | CASELESS 1:n NON-matching: eleven historically-tempting one-to-many candidates (ß/SS, ﬁ/fi, …) that must NOT match, because 10.46 does SIMPLE folding only (UD §4.1) |
| **8** | `axis08_lookbehind_varwidth.rxt` | LOOKBEHIND over variable-BYTE-width bodies at fixed CHARACTER width — `PCRE2_INFO_MAXLOOKBEHIND == 1` character spanning several byte widths (UD §5.6's width finding: the analysis is in characters where pcrec computed bytes) |
| **9** | `axis09_nextpos_findall.rxt` | `next_pos` / FIND-ALL over multi-byte subjects: the advance between matches walks CHARACTER boundaries, and a caller-supplied mid-character `startpos` has its own ruled answer (UD §2.6.1.1) |
| **10** | `axis10_surrogate_witness.rxt` | SURROGATE SUBJECTS: three surrogate encodings × three patterns; a correct artifact REJECTS every one — the surrogate range has no path in a correctly-lowered automaton |
| **11** | `axis11_startpos_boundary.rxt` | CANDIDATE MATCH STARTS ARE CHARACTER BOUNDARIES: the positions the ENGINE invents, not the ones a caller supplies. Only a pattern that can match EMPTY at a mid-character position can detect a violation (K50's own lesson) |
| **12** | `axis12_scripts.rxt` | SCRIPT properties: `\p{Greek}` is `Script \| Script_Extensions` while `\p{sc=Greek}` is `Script` alone — measured, and the file's own point |

### 3.2 The coverage table — axis × where × release

| axis | exercised by | release | note |
|---|---|---|---|
| 1 encoded length | (a) `cls-dot`, `cls-dot-rep`; (b) every `lit-1ch-*`; (d) `alt-mixed-width`, `qnt-dot-bounded` | **0.1** | the sharpest single witness is `cls-dot-rep` (`^.{5}$` matching a 12-byte, 5-character subject) |
| 2 class boundary | (a), all fourteen members | **0.1** | Frank's own named example; the largest first-release family |
| 3 invalid UTF-8 | growth **(h)** | **0.3** | documented-behaviour table, never a ranked cell — §8.3 |
| 4 `\p` categories | (f) `prp-L`, `prp-Lu`, `prp-N`, `prp-notL`, `prp-Zs`, `prp-L-anchored` | **0.1** | six of 37 spellings; the set measures the MECHANISM's cost, not the table's coverage — §3.3 gap 2 |
| 5 `\p` refusals | (f) `prp-ingreek` — ONE witness | **0.1**, permanently partial | §3.3 gap 2 |
| 6 caseless fold | (c), all twelve members | **0.1** | I-90 §5's third named first customer |
| 7 caseless 1:n | (c) `ci-strasse`, `ci-sigma`, `ci-turkish-i` | **0.1** | authored as designed MISSES, per the house near-miss rule |
| 8 lookbehind var-width | (e) `asr-lb-fixed`, `asr-lb-varwidth`, `asr-lb-neg`, `asr-lb-class` | **0.1** | |
| 9 next_pos / find-all | **every `throughput` cell at 0.1** (the regime IS a find-all loop, `--find-all`/`NMATCHES`, `pcrecbench/adapters.py`'s protocol) + growth **(g)** for the search-grain shapes | **0.1 partial → 0.2** | §8.4 is the harness change this axis forces |
| 10 surrogate witness | growth **(j)** | **0.3** | shares (h)'s machinery |
| 11 startpos boundary | (e) `asr-B-midchar` — the ENGINE-invented half only | **0.1 partial; caller half STRUCTURALLY UNREACHABLE** | §3.3 gap 3 |
| 12 scripts | (f) `prp-cyrillic`, `prp-han`, `prp-latin`, `prp-greek`, `prp-greek-sc`, `prp-nothan` | **0.1** | `prp-greek`/`prp-greek-sc` is the Script vs Script_Extensions pair, authored as a spelling pair so the difference is readable |

### 3.3 The gaps, stated honestly

A coverage claim with no gap list is a coverage claim nobody checked.

1. **Axes 3, 10 and the caller half of 11 are NOT in the first
   release.** They are growth (h), (j) and (i). This is a sequencing
   choice, not a structural one: all three need the same thing — a
   policy for a subject the oracle will not answer under plain
   `PCRE2_UTF` (§8.3) — and shipping that policy half-built is worse
   than shipping (a)-(f) without it.
2. **Axis 5's 34-spelling refusal census is NOT reproduced, and never
   will be.** ONE witness (`prp-ingreek`) ships, as the compile-axis
   proof that a well-formed-but-unknown property body is a first-class
   `did-not-compile` row with the engine's own diagnostic. The other 33
   are a CORRECTNESS census — a refusal has no speed — and
   `~/pcrec/tests/utf8/axis05_p_refusals.rxt` already owns it. The same
   applies to axis 4's 37 spellings: this set carries six, because the
   thirty-seventh `\p` spelling costs what the sixth does and the
   difference is a table, not a mechanism. **Permanent, by design.**
3. **Axis 11's caller-supplied mid-character `startpos` is
   STRUCTURALLY UNREACHABLE from this bench at any release.** The
   driver protocol (`pcrecbench/adapters.py`, stated in full at the top
   of that file) has no `--startpos`: every measured call starts at
   offset 0 and subsequent positions come from the find-all advance
   rule. A caller-supplied mid-character start cannot be expressed. What
   IS reachable is the half K50 was actually about — the positions the
   ENGINE invents during an unanchored scan — and `asr-B-midchar` is
   that witness. Naming a `--startpos` protocol extension is a HARNESS
   question, not a set one; **§14 Q8** records it and recommends
   leaving it out.
4. **The `byte` MIRROR axes** (`axis01_encoded_length_byte`,
   `axis02_class_boundary_byte`, `axis03_invalid_utf8_byte`) are
   reachable only under growth (k), and only for the sub-population
   pcrec compiles under `-e byte`: `\x{...}` above 0xFF is
   range-refused there (AX, axis01 mirror header), so a large part of
   family (a) has no mirror cell at all. §6(k) states the expected
   refusal census rather than promising a full mirror.
5. **UCP has no pcrec axis.** UD §4.5, verbatim: *"pcrec has no `UCP`
   axis today, so pcrec's `byte` encoding reproduces PCRE2 at
   `CASELESS` and diverges at `UCP|CASELESS`."* Every `unicode-class-
   scope` pattern in this set is therefore
   `unsupported-by-declaration` on every pcrec config — a census row
   (§7.4), and **P5**.

---

## 4. Subjects

### 4.1 The sourcing decision

| option | what it means | consequence |
|---|---|---|
| **(a) GENERATED from committed per-script word pools, deterministic, sha256-manifested** | the house rule (`requirements.md §5`: "generated deterministically by a script with a committed manifest by default, real corpora only when licensing is clean"), with a small hand-authored vocabulary per script supplying the words | **CHOSEN** |
| (b) a licence-clear public-domain corpus per script | Project Gutenberg fr/de/es/ru, a public-domain CJK text, a CLDR/emoji sample | rejected — for CAP §4.4's own measured reason (rebar's OpenSubtitles haystacks carry an upstream licence question *rebar itself did not resolve*), and for a second reason specific to this set: a scraped corpus's byte histogram is whatever that text happens to be, and this set's whole claim is ABOUT the byte histogram. A generated corpus lets the histogram be a committed, re-derived FACT per subject rather than a property nobody measured |
| (c) synthetic random bytes in the right ranges | cheapest | rejected — a random 3-byte-lead stream is not CJK text: it has no word boundaries, no punctuation, no ASCII interleaving, and every first-byte filter reads the same on it. The mechanisms under test are exactly the ones that notice |

**DECISION: (a).** Each script gets a committed `pool_<script>.tsv` of
roughly 200 common words plus a punctuation/whitespace vocabulary, and
`utf8text.py` — the shared xorshift64\* primitive in
`bench/syntax/censustext.py`'s shape, which `bench/capability/captext.py`
already reuses — composes them into sentences and paragraphs.

**The limitation, stated plainly and repeated in `NOTES.md`:** these are
our sentences made of real words. The set claims a realistic BYTE
HISTOGRAM and realistic character-width statistics — which is what every
mechanism under test actually reads (a required byte, a lead-byte scan,
an offset-k skip, a fold set) — and does NOT claim realistic prose
statistics at the word or sentence grain. A finding that depends on
word-frequency structure rather than byte structure is not this set's to
make.

**Provenance.** Each pool row is `fidelity = synthesized`,
`source_name = authored`, in `capability`'s own provenance vocabulary
(CAP §4.1): individual common words of a natural language are not a
copyrightable source and there is no URL to cite. Whether that counts as
"generated" for the house rule or as "sourced" needing a provenance
record is **§14 Q2** (recommendation: generated; commit the pools and
state the sentence above).

### 4.2 The five script corpora

| corpus | content | dominant lead bytes | why it is here |
|---|---|---|---|
| `lat` | French / German / Spanish prose (é è à ü ö ß ñ ç), Latin-1 Supplement heavy | **0xC3** near-universal (the lead byte of all of Latin-1 Supplement), 0xC2 for punctuation/NBSP | FP §3.1's own worked example: the same text is one histogram as UTF-8 and a completely different one as latin1. The corpus the frequency-prior inversion is about |
| `cyr` | Russian prose | **0xD0 / 0xD1** — only two lead bytes for the entire alphabet | the WEAKEST possible first-byte filter: a two-value lead set covering ~half the corpus's bytes |
| `cjk` | Japanese and Chinese prose, kana + han, with ASCII interleaved (numbers, latin proper nouns) | **0xE3-0xE9** — 3-byte characters, a wide lead-byte spread | the opposite end: three bytes per character, leads spread over seven values, and a real ASCII minority |
| `mix` | all four above interleaved at a stated ratio, plus emoji and symbols (4-byte, leads 0xF0) | all of the above + **0xF0** | the only corpus carrying 4-byte characters; the throughput sweep's own grammar |
| `asc` | byte-clean ASCII: the same grammar, English word pool, no byte ≥ 0x80 | none | the CONTROL. What does the encoding cost when there is nothing to encode? |

**Each corpus's lead-byte histogram is a committed, re-derived column of
the manifest** — a sixth column is not accepted by the loader
(`bench/CLAUDE.md`: "the loader takes 4 or 5"), so the histogram lives
in its own committed `subject_facts.tsv`, re-derived under
`gen_subject_facts.py --check` through the generic `gen_*.py --check`
hook `make check-harness` already runs over every `bench/*/` directory
by enumeration. That table is what makes "the histogram is unlike
English" a fact rather than a claim.

**Does `asc` RANK, or is it provenance-only?** The brief flags this as
the manager's or Frank's. **§14 Q1**; recommendation: **it RANKS.**
Excluding it makes the set's central question — what does the encoding
cost — unanswerable from inside the set, and it is the cheapest reading
of the (k) mirror this release can carry (`asc` under `-e utf8` against
`asc` under `-e byte` is one variable). The counter-argument (a pure-
ASCII subject in a UTF-8 set is not what the set is about, and its rows
will dominate any "best" column) is real and is why the question is
asked rather than decided silently.

### 4.3 Sizes and manifests

- **`throughput`:** the three sizes `capability` uses — **64 KB /
  256 KB / 1 MB** — built from the `mix` grammar, PLUS a **per-script
  64 KB arm** (`lat`, `cyr`, `cjk`, `asc`; `mix` at 64 KB is already
  the sweep's first rung). Seven throughput subjects, ~1.58 MB total.
  The size sweep gives one per-byte number per pattern plus the
  statement that the number is flat in subject length (R7); the
  per-script arm at one fixed size is where the histogram axis is read.
- **`search_short`:** **90 typed short subjects**, `short_search_max_
  bytes = 512`. Derived per family exactly as `capability` derives
  them (CAP §3.4): each short subject is at least one family member's
  designed HIT and, where the family has a semantic edge, another
  member's designed MISS. Fifteen per family, each typed in that
  family's own script, and each serving two or three of that family's
  members rather than one — which is the lever §10's arithmetic
  depends on.
- Both manifests committed with `id, len, sha256, description,
  periodic`; `make check` regenerates both trees and requires them to
  reproduce byte for byte, by enumeration, as it does for every set.
- Subjects live as raw `.bin` files, so a subject carrying bytes that
  are not valid UTF-8 (growth (h)/(j)) is expressible without a schema
  question — `bench/capability`'s family 12 already established this
  (three `nu-*` subjects with genuine raw high bytes).

### 4.4 The floor pattern

`~`, one literal ASCII byte, `role = "floor"` (`requirements.md §5`),
chosen so it occurs a handful of times in the punctuation vocabulary and
never inside a multi-byte sequence. It gives three readings, in the
census's own idiom: a search hit on a small number of short subjects and
misses on the rest, and a full-length `memchr` MISS over 64 KB, 256 KB
and 1 MB — **and, uniquely here, a fourth**: it is the one pattern in
the set whose compiled artifact should be IDENTICAL under `-e utf8` and
`-e byte`, which makes it the (k) mirror's own zero point (**P8**).

---

## 5. The six first-release families

**73 members + the floor = 74 patterns.** Ids are `<family>-<slug>`;
every member carries `tag family=`, `tag requires=` and, where it has
one, `tag hazard=` — `bench/capability`'s own `patterns.rxt` shape.

Every family carries at least one CONTROL PAIR and at least one designed
NEAR-MISS — a subject that shares a prefix with a hit and fails at the
last character — per the house rule (`bench/bounded`'s "fail at the last
repetition", `bench/syntax`'s spelling groups, CAP §3.2).

**Notation.** `\x{...}` is written in the pattern text where the code
point matters more than the glyph; a literal glyph is written where the
byte sequence is the point. Both are UTF-8 in the file.

### (a) CLASSES — `cls-*`, 14 members — Frank's own example

The 1-byte/multi-byte boundary, negation over the encoding's universe,
and the class-scope question. Axes 1, 2 (+ the UCP split).

| id | pattern | axis | what it isolates |
|---|---|---|---|
| `cls-boundary-range` | `[a-é]+` | 2 | a range SPANNING the boundary: U+0061..U+00E9, half 1-byte and half 2-byte, the shape that must not be byte-decomposed |
| `cls-high-range` | `[\x{100}-\x{2000}]+` | 1, 2 | a wholly-multi-byte range crossing the 2-byte/3-byte width boundary at U+0800 |
| `cls-neg-single` | `[^é]` | 2 | negation of ONE non-ASCII character — the complement is taken within `[0, 0x10FFFF]` (UD §2.7.1), not within 256 |
| `cls-neg-allhigh` | `[^\x{80}-\x{10FFFF}]+` | 2 | the negation whose complement is exactly ASCII; the cheapest statement of "what is the universe here?" |
| `cls-mixed` | `[a-zé\x{430}-\x{44F}]+` | 2 | ASCII + Latin-1 Supplement + Cyrillic members in one class: three lead-byte groups from one construct |
| `cls-dot` | `.` | 1 | `.` is ONE CHARACTER, not one byte |
| `cls-dot-rep` | `^.{5}$` | 1 | the sharpest encoded-length witness: matches a 5-character / 12-byte subject, refuses a 5-BYTE one that is 3 characters |
| `cls-w-ascii` | `\w+` | 2 | `\w` WITHOUT UCP under `-e utf8`: ASCII-scoped, so a Cyrillic letter is a NON-member (AX axis08's own oracle basis, verbatim). `requires = ascii-class-scope` |
| `cls-w-ucp` | `(*UCP)\w+` | 2 | the UCP twin — `requires = unicode-class-scope`. The control pair with `cls-w-ascii`; the pair is the whole point |
| `cls-d-ascii` | `\d{4}` | 2 | designed NEAR-MISS: against a subject of four Arabic-Indic digits (U+0660-0669), must NOT match under ASCII class scope. `requires = ascii-class-scope` |
| `cls-s-nbsp` | `a\sb` | 2 | designed NEAR-MISS: against `a` U+00A0 `b`, must NOT match without UCP. `requires = ascii-class-scope` |
| `cls-posix-alpha` | `[[:alpha:]]+` | 2 | the POSIX-class spelling of the same scope question — a genuine cross-engine divergence candidate. `requires = ascii-class-scope` |
| `cls-lead-pair` | `[α-ω]+` | 2 | **a FIRST CUSTOMER.** UD §6.3's own worked row: a TWO-lead-byte class (0xCE, 0xCF) is an excellent filter that `memchr` cannot use because `memchr` takes one byte; the bitmap-skip arm must take it |
| `cls-neg-cjk` | `[^\x{4E00}-\x{9FFF}]+` | 2 | a negated 3-byte range, read over the `cjk` corpus where it mostly FAILS — the loglines-shaped reading of a multi-byte class |

Control pairs: `cls-w-ascii`/`cls-w-ucp`; `cls-lead-pair` against
`cls-high-range` (two leads vs many). Near-misses: `cls-d-ascii`,
`cls-s-nbsp`, `cls-dot-rep`'s 5-byte subject.

### (b) LITERALS of multi-byte characters — `lit-*`, 12 members

The required-byte / required-run / offset-skip shapes over high bytes.
Axes 1, 9. **I-90 §5's first two named first customers live here.**

| id | pattern | axis | what it isolates |
|---|---|---|---|
| `lit-1ch-2b` | `é` | 1 | one 2-byte character (C3 A9) |
| `lit-1ch-3b` | `日` | 1 | one 3-byte character (E6 97 A5) |
| `lit-1ch-4b` | `😀` | 1 | one 4-byte character (F0 9F 98 80) — the only lead byte in the F0 range |
| `lit-run-3` | `日本語` | 1 | a 9-byte run of 3-byte characters: the required-RUN shape, and a pattern whose necessary byte is necessarily HIGH |
| `lit-mixed-ascii` | `user@例え.jp` | 1, 9 | mixed widths with an ASCII `@` and `.` available as the necessary byte — the CONTROL for `lit-run-3` (same length class, an ASCII byte to pick) |
| `lit-cyr-run` | `Москва` | 1 | a 12-byte run whose every lead byte is 0xD0 or 0xD1 — the weak-filter literal, against `lit-run-3`'s spread |
| `lit-offset-at-tail` | `é@` | 9 | **THE FIRST CUSTOMER.** FP §3.1's own live witness: under `-e utf8` this lowers to `{0xC3, 0xA9, 0x40}` and today's rightmost rule stamps `@` (0x40, 665 ppm) |
| `lit-offset-at-head` | `@é` | 9 | its ORDER PAIR: the same three bytes, the necessary byte at the other end. FP §3.1 measured `RX_REQ_BYTE "169"` (0xA9) for one ordering and `"64"` (0x40) for the other on the shipped compiler |
| `lit-nearmiss-run` | `日本語` (against `日本人`) | 1 | the designed NEAR-MISS: shares two characters and six bytes, fails at the last character — the house shape |
| `lit-anchored-run` | `^日本語$` | 1 | the anchored reading of `lit-run-3`; with no `match` regime (§10) the anchor lives in the pattern |
| `lit-nfc-pair` | `café` (precomposed) | 1 | a designed MISS against a DECOMPOSED subject (`cafe` + U+0301). **Not a normalization claim** — the point is that no engine here normalizes, and a set that did not say so would look like it had forgotten |
| `lit-sharp-s` | `Straße` | 1 | the German 2-byte ß in an otherwise ASCII literal; the body `ci-strasse` folds |

Control pairs: `lit-run-3`/`lit-mixed-ascii` (high necessary byte vs
ASCII one); `lit-offset-at-tail`/`lit-offset-at-head` (the order pair);
`lit-run-3`/`lit-cyr-run` (lead spread).

### (c) CASELESS over non-ASCII — `ci-*`, 12 members

The fold-set shapes. Axes 6, 7. **I-90 §5's third named first
customer.** Non-ASCII caseless folding SHIPPED in pcrec at [M5.0] stage
4 (AX, "THE STAGE-4 GAP IS CLOSED", 2026-09-08), so every member below
is a live cell on pcrec, not a refusal.

| id | pattern | axis | what it isolates |
|---|---|---|---|
| `ci-e-acute` | `(?i)é` | 6 | the simplest non-ASCII fold pair (U+00E9 / U+00C9), both 2 bytes |
| `ci-moskva` | `(?i)москва` | 6 | a six-character Cyrillic fold set — twelve bytes, twelve fold partners |
| `ci-greek-run` | `(?i)αβγ` | 6 | a Greek fold set whose partners sit in a different lead-byte group |
| `ci-kelvin` | `(?i)k` | 6 | **the closure reaching OUTSIDE the range** (UD §4.2): `k`/`K` plus U+212A KELVIN SIGN, a 3-byte character pulled in by a 1-byte pattern. A designed HIT on a subject carrying U+212A |
| `ci-long-s` | `(?i)s` | 6 | the same shape with U+017F LATIN SMALL LETTER LONG S — a 2-byte partner for a 1-byte pattern |
| `ci-class-range` | `(?i)[a-z]+` | 6 | fold over a RANGE, which pulls in partners outside the written range (UD §4.2(c) — the case `fold.rxt` exists for) |
| `ci-neg-fold` | `(?i)[^é]` | 6 | FOLD BEFORE NEGATE (UD §4.3): the fold closure is applied to the interval set, then complemented |
| `ci-strasse` | `(?i)straße` | 7 | designed NEAR-MISS: must NOT match `STRASSE`. 10.46 does SIMPLE folding only, so there are no one-to-many foldings (UD §4.1) |
| `ci-sigma` | `(?i)σ` | 7 | σ / Σ / ς — the final-sigma case; a designed HIT on Σ and ς, a designed MISS on nothing (all three fold together under simple folding) |
| `ci-turkish-i` | `(?i)i` | 7 | designed NEAR-MISS: must NOT match U+0130 or U+0131. Locale-free simple folding, stated as an expectation rather than assumed |
| `ci-ascii-control` | `(?i)abc` | 6 | **the CONTROL.** A pure-ASCII fold under `-e utf8`: the abi-23 `RX_VM_CLS_FOLDS` customer at its cheapest, and the row every fold-set size above is read against |
| `ci-ucp-invariance` | `(*UCP)(?i)é` | 6 | the control that says the fold is NOT UCP-gated: same answer as `ci-e-acute`. `requires = unicode-class-scope` — so it is a pcre2-only row, and its agreement with `ci-e-acute` is the finding |

### (d) ALTERNATION and QUANTIFIERS over multi-byte units — `alt-*` / `qnt-*`, 12 members

Axes 1, 2, 9. The DFA/island/prefilter route question under a
non-English histogram.

| id | pattern | axis | what it isolates |
|---|---|---|---|
| `alt-shared-char` | `日本\|日曜\|日付` | 1, 9 | three branches sharing the whole first CHARACTER (three bytes) — a required-run every branch has |
| `alt-shared-lead` | `α\|β\|γ` | 2 | three branches sharing only the LEAD BYTE (0xCE) — a first-byte filter that cannot discriminate |
| `alt-distinct-lead` | `日本\|Москва\|café` | 1 | three branches, three lead-byte groups — the filter's best case |
| `alt-mixed-width` | `a\|é\|日\|😀` | 1 | one branch per encoded length: the 1/2/3/4-byte alternation, and the cheapest reading of "how does width enter the automaton?" |
| `alt-cyr-64` | 64 Cyrillic words, `\|`-joined | 2 | the BRIDGE rung to `bench/altwide@0.2`'s own width curve. ONE rung, not a ladder (§2.4) |
| `alt-nearmiss` | `日本語\|日本国` | 1 | designed NEAR-MISS against `日本人`: shares six of nine bytes on both branches |
| `qnt-plus-2b` | `é+` | 1 | a quantified 2-byte character — under `byte` this is BYTE-DECOMPOSED (AX axis01 mirror header), which is the mirror's own discriminator |
| `qnt-lazy-2b` | `é+?` | 1 | the lazy twin — the control pair for `qnt-plus-2b` |
| `qnt-counted-3b` | `(?:日本){2,}` | 1 | a counted repeat of a two-character (6-byte) group |
| `qnt-bounded-4b` | `😀{2,4}` | 1 | a counted repeat of a 4-byte character: 8 to 16 bytes from one rung |
| `qnt-dot-bounded` | `.{3,8}` | 1 | a counted repeat of `.` — characters, not bytes; 3 to 32 bytes from one rung |
| `qnt-class-run` | `[\x{400}-\x{4FF}]{4,16}` | 1, 2 | a counted repeat over a multi-byte CLASS: the byte-decomposition cost at its most visible |

### (e) ASSERTIONS under `-e utf8` — `asr-*`, 11 members

Axes 8, 11 (+ the UCP split on `\b`).

| id | pattern | axis | what it isolates |
|---|---|---|---|
| `asr-b-ascii` | `\bcat\b` | — | the pure-ASCII CONTROL, in the same subject vocabulary |
| `asr-b-cyr` | `\bМосква\b` | 11 | designed NEAR-MISS: without UCP a Cyrillic letter is NOT a word character, so `\b` sits at a different place than a reader expects. `requires = ascii-class-scope` |
| `asr-b-cyr-ucp` | `(*UCP)\bМосква\b` | 11 | the UCP twin and the control pair. `requires = unicode-class-scope` |
| `asr-B-midchar` | `\B` | **11** | K50's own witness shape, and the only half of axis 11 this bench can reach (§3.3 gap 3): a pattern that can match EMPTY is the only thing that can ANSWER at a mid-character position |
| `asr-lb-fixed` | `(?<=é)x` | 8 | a lookbehind of fixed CHARACTER width 1 and BYTE width 2 — UD §5.6's finding in one pattern |
| `asr-lb-varwidth` | `(?<=a\|é)x` | 8 | branches of differing BYTE width at identical CHARACTER width — the discriminating promise axis 8 exists to pin |
| `asr-lb-neg` | `(?<!日)本` | 8 | negative lookbehind over a 3-byte body |
| `asr-lb-class` | `(?<=[\x{400}-\x{4FF}])\s` | 8 | a lookbehind over a multi-byte CLASS rather than a literal |
| `asr-caret-ml` | `(?m)^日` | 1 | multiline `^` over lines that begin with a 3-byte character |
| `asr-dollar-ml` | `(?m)語$` | 1 | multiline `$` at the end of a multi-byte line |
| `asr-a-z` | `\A日本語\z` | 1 | true-end anchor over a multi-byte subject; `requires = true-end-anchor` (CAP §6.2's sixteenth token) |

### (f) PROPERTIES — `prp-*`, 12 members

Axes 4, 5, 12. `\p` needs pcrec module `unicode-props` (shipped, [M5.0]
stage 3); script names shipped at stage 5 (UD §3.4's staging table, and
`axis12_scripts.rxt` is live).

| id | pattern | axis | what it isolates |
|---|---|---|---|
| `prp-l` | `\p{L}+` | 4 | the general category every `\p` user reaches for first; UD §6.3 measures its lead-byte set at **97** — a weak filter, deliberately |
| `prp-lu` | `\p{Lu}` | 4 | 47 lead bytes — a usable bitmap filter, the contrast row |
| `prp-n` | `\p{N}+` | 4 | numbers, incl. non-ASCII digits — the positive twin of `cls-d-ascii`'s near-miss |
| `prp-notl` | `\P{L}+` | 4 | the negated category: complement over the whole code-point universe |
| `prp-zs` | `\p{Zs}` | 4 | space separators, incl. U+00A0 and U+3000 — the positive twin of `cls-s-nbsp` |
| `prp-l-anchored` | `^\p{L}{4}$` | 1, 4 | a counted property class: four CHARACTERS of unknown byte width |
| `prp-cyrillic` | `\p{Cyrillic}+` | 12 | a script with two lead bytes — the strongest script filter in the set |
| `prp-han` | `\p{Han}+` | 12 | a script with a wide 3-byte lead spread |
| `prp-latin` | `\p{Latin}+` | 12 | a script spanning the 1-byte/multi-byte boundary — ASCII letters and Latin-1 Supplement in one property |
| `prp-greek` | `\p{Greek}` | 12 | **the SPELLING PAIR**, half one: `Script \| Script_Extensions` |
| `prp-greek-sc` | `\p{sc=Greek}` | 12 | half two: `Script` alone. U+0342 and U+0300 are the characters that flip (AX, [M5.0] stage 5) — authored as a subject pair so the difference is a measured answer, not a claim |
| `prp-ingreek` | `\p{InGreek}` | **5** | **the REFUSAL WITNESS.** PCRE2 10.46 refuses block names with error 147 and pcrec refuses them PERMANENTLY (UD §3.4: "REFUSE PERMANENTLY … Reproducing a refusal is free and correct"). A compile-axis row with a `did-not-compile` outcome on every engine and NO match rows — legal today (`bounded`'s own 65535-cap rung is the precedent, KB-4) |

**`prp-ingreek` and R-BENCH-4.** Its refusal is a PCRE2 fact (error 147)
and a Unicode fact (there is no `InGreek` property), not a pcrec-oracled
boundary. No limit, cap or refusal edge anywhere in this set is derived
from pcrec — §9.

### 5.1 Counts and hazard classes

| family | members | `hazard_class` |
|---|---|---|
| (a) `cls-*` | 14 | `none` |
| (b) `lit-*` | 12 | `none` |
| (c) `ci-*` | 12 | `none` |
| (d) `alt-*` / `qnt-*` | 12 | `none` |
| (e) `asr-*` | 11 | `none` |
| (f) `prp-*` | 12 | `none` |
| floor | 1 | `none` |
| **total** | **74** | |

No member is authored to exercise a backtracking hazard: this set's
objective is the ENCODING, and a ReDoS shape would confound it.
`bench/capability`'s family 10 owns that axis (§2.4's rule). Stated
explicitly because `hazard_class` is a required closed-enum field per
pattern and an authoring lane's silent default would otherwise be an
unstated choice (CAP §3.1's CB7 lesson).

---

## 6. The growth plan — (g) through (k), a version each

I-90 clause 3 requires the growth stages to be NAMED NOW with a version
each, and requires the plan to live in `bench/utf8/NOTES.md`. This
section is the source that `NOTES.md` will carry.

| stage | what it adds | axis | version | why it is not in 0.1 |
|---|---|---|---|---|
| **(g)** find-all / `next_pos` over multi-byte subjects at the SEARCH grain | explicit find-all shapes whose advance crosses character boundaries: an empty-matching pattern over multi-byte text, a zero-width assertion repeated, the `\G` chain | 9 | **0.2** | the `throughput` regime already exercises the find-all ADVANCE at 0.1 (§3.2); (g) is the search-grain reading, and it depends on §8.4's harness change having been made and measured once |
| **(k)** the `-e byte` MIRROR arm | the same patterns and the same subjects, compiled `-e byte`, so the ledger states the ENCODING COST per cell | 1b, 2b | **0.2** | it needs nothing new from the SET (§9: the mirror is a testee-config fact) — only four more pcrec configs and a large, expected `did-not-compile` census where `\x{...}` above 0xFF is range-refused. Shipped WITH (g) because together they are one night's window |
| **(h)** INVALID UTF-8 subjects | pcrec's axis-3 shapes: nine ill-formed kinds × three positions, as a per-engine DOCUMENTED-BEHAVIOUR TABLE, never a ranked cell (§8.3) | 3 | **0.3** | it needs the policy of §8.3 ruled (§14 Q10) and each engine's documented behaviour RECORDED, not assumed — which is a research pass per engine, not a generator |
| **(i)** START-POSITION-inside-a-character search | the reachable half only: engine-invented candidate starts, widened beyond `asr-B-midchar` | 11 | **0.3** | the caller-supplied half is structurally unreachable (§3.3 gap 3); what remains is a small family that belongs beside (h)'s ill-formed subjects |
| **(j)** SURROGATE / OVERLONG witnesses | the three surrogate encodings and the overlong forms as subjects every correct engine must reject | 10 | **0.3** | same machinery and same policy as (h) |

**Sequencing recommendation, for the record:** 0.2 = (g) + (k), 0.3 =
(h) + (i) + (j). (h)/(i)/(j) share one policy and one subject-generation
problem; splitting them across two versions would ship that policy
twice. **§14 Q7**, defaultable.

**One further stage named but not numbered by I-90:** a `tre-wide`
configuration (§7.3) and any second non-UTF-8-native engine's UTF-8
config are ROSTER growth, not set growth, and land whenever their lane
does — they change no pattern, subject or expectation.

---

## 7. The roster — who speaks UTF-8, and how each is told

I-90 clause 1: *"the 13-engine roster restricted to engines that speak
UTF-8 — say which do and how each is told."*

**The finding that shapes this whole section: every adapter in this
repo is deliberately BYTE-MODE today, and each one says so in its own
file.** That is not an oversight — it is what makes
`bench/capability`'s family 12 (`binary-nonutf8`) measurable at all, and
three adapters cite that family by name as the reason. So a UTF-8 set
does not "turn on" a mode; it adds a SECOND CONFIG per engine, with the
encoding visible in `testee_id`.

### 7.1 The surface table

| engine | UTF-8 surface | how it is told TODAY | v1? | the adapter change, concretely |
|---|---|---|---|---|
| **pcre2** (`interp`, `jit`, `dfa`) | `PCRE2_UTF` (0x00080000), plus `PCRE2_UCP` where a family needs it | **nothing** — `driver.c:325` calls `p_compile(pat, patlen, 0, …)` with the options word HARD-CODED to `0` | **v1: three NEW configs** `pcre2-utf-interp` / `-jit` / `-dfa` | `driver.c`: two argv flags (`--utf`, `--ucp`) folded into the options word, and the find-all advance made character-boundary-aware (§8.4 — PCRE2 rejects a mid-character `startoffset` under `PCRE2_UTF`). `adapter.py`: two config keys → driver args → `config_extra`. `configs.toml`: three rows |
| **pcrec** (`auto`, `nocaps`, `vm`, `vm-in`) | `-e utf8` / `--encoding=utf8` (UD §9.2 stage 2's own spelling) | `flags = ["--features", "all", …]` in `configs.toml` | **v1: four NEW configs** at `-e utf8` | `configs.toml` only: four rows whose `flags` carry `"-e", "utf8"`. Because `flags` land in `build_flags` AND in the derived `testee_id`, the encoding becomes an IDENTITY exactly the way `-bigcap` and `-noclsfold` already are — no adapter code changes |
| **rust** (`rust-default`) | **already UTF-8-semantic.** `RegexBuilder::unicode` defaults to **true** and `regex::bytes` matches a code point against its UTF-8 ENCODING in the haystack — `testees/rust/CLAUDE.md`'s own measured section ("`non-utf8-subject`: RESOLVED — the class matches the UTF-8 ENCODING, not the raw byte, under this config's default unicode mode") | nothing to tell it | **v1, UNCHANGED** | **zero.** The finding worth stating: `rust-default`'s presence in this repo's BYTE sets is the anomaly, not its presence here |
| **re2** (`re2-default`, `re2-longest`) | `RE2::Options::EncodingUTF8` — RE2's own DEFAULT, which this driver deliberately overrides | `driver.cc:220`: `opts.set_encoding(RE2::Options::EncodingLatin1);`, with the header comment naming family 12 as the reason | **v1: one NEW config** `re2-utf8` | `driver.cc`: one argv flag selecting the encoding; `configs.toml`: one row. The cheapest change on the roster |
| **onig** (`onig-default`) | `ONIG_ENCODING_UTF8` | `driver.c:91`: `#define ONIG_DRIVER_ENCODING ONIG_ENCODING_ASCII` — a COMPILE-TIME constant, so a second config cannot be a flag without a small change | **v1: one NEW config** `onig-utf8` | `driver.c`: make the encoding a runtime choice between two `OnigEncoding` pointers (`--encoding utf8\|ascii`); `configs.toml`: one row. **AND a re-census**: `testees/onig/CLAUDE.md` withholds `unicode-properties` under ASCII encoding — under UTF-8 it is expected to be SATISFIED, which must be witnessed per (config, token) before the declaration changes (the L5 lesson, CAP §5.3) |
| **vectorscan** (`vectorscan-block-nosom`) | `HS_FLAG_UTF8`, plus `HS_FLAG_UCP` | `driver.c:125`: `VS_DRIVER_FLAGS` is `0`; the header (`:50-59`) states `HS_FLAG_UTF8` is NEVER set and why (byte-oriented, matching the roster's 8-bit convention, satisfying `non-utf8-subject`) | **v1, BOOLEAN GRAIN ONLY** — one new config `vectorscan-block-nosom-utf8` | `driver.c`: flags from argv; `configs.toml`: one row. Frank's Q3 ruling stands unchanged: match/no-match and compile/refusal comparisons, never a span or a count. **A warning this set inherits (§7.6):** the same header records a MEASURED A/B in which setting `HS_FLAG_UCP` BREAKS `\b` on five real corpus patterns (40/64 corpus compiles at flags 0 against 35/64 under UCP) |
| **tre** (`tre-default`) | **no byte-mode UTF-8 path exists** — see §7.3 | `tre_regncompb`, byte-literal by construction; `driver.c:19` states the convention ("a byte ≥ 0x80 is one [character]") | **EXCLUDED from v1** — §7.3 | — |
| **python `re`, perl** | both are UTF-8-native | not wired (CAP §8.1: compile + correctness only, and permanently `inconclusive-spread` run pinned) | not in v1, as elsewhere | — |

### 7.2 pcrec's four configs, and why the flag mechanism matters

I-90 clause 4 asks for "the usual four, all compiled `-e utf8`". The
four are `pcrec-auto`, `pcrec-nocaps`, `pcrec-vm`, `pcrec-vm-in` — the
set every window uses (CAP §8's own v1 row).

The important property is that `-e utf8` goes in `configs.toml`'s
`flags` list and NOT into a hidden protocol token. `testees/pcrec/
adapter.py:2370` records the distinction already: *"[flags] are NEVER
passed to pcrec: pcrec's own `flags` (its argv, `--features` …)"* — the
project's OWN phase-2 flags (`-falign-functions=64`) are separate, and
the `-fcomments` protocol token added at the 25b1984f re-pin is
deliberately invisible in `testee_id`. `-e utf8` must be the opposite:
**visible**, because two records differing only in encoding must be two
testees, not one testee measured twice.

Proposed ids, by the composition rule: `pcrec-auto-utf8`,
`pcrec-nocaps-utf8`, `pcrec-vm-utf8`, `pcrec-vm-in-utf8`, deriving
`config_extra = utf8` in the record — the same escape hatch
`pcrec-*-bigcap` ([B31]) and the `-clang` siblings ([B24]) already use.
Twenty pinned pcrec configs after this set lands.

### 7.3 The TRE ruling — EXCLUDED from v1, by declaration, not by omission

**PROPOSED RULING: `tre-default` runs NO (a)-(f) cell in `utf8@0.1`.
The exclusion is a `requires = utf8-encoding` token the config declares
UNSATISFIED, so every pattern is a clean `unsupported-by-declaration`
compile row citing the token by name — a CENSUS row, never an absence.**

Three reasons, in order of weight:

1. **TRE has no byte-mode UTF-8.** `tre_regncompb` is byte-literal by
   construction; `testees/tre/driver.c:19` states the convention this
   project adopted for it ("a byte ≥ 0x80 is one [character]"), and
   `testees/tre/CLAUDE.md` item (d).1 measures a related consequence
   (`\xHH` does not exist at all; `\x93` compiles as three literal
   characters). Every (a)-(f) pattern would get a BYTE-DECOMPOSED
   reading — which answers a *different question* from the one the set
   asks, and would sit in the same ranking column as the answers to the
   right one.
2. **The only UTF-8 path is the WIDE-CHARACTER family, and it is a
   second driver model.** `/usr/include/tre/tre.h:207-236` declares
   `tre_regwcomp`, `tre_regwexec`, `tre_regwncomp` and `tre_regwnexec`,
   all taking `wchar_t`. Using them means: transcoding both the pattern
   and every subject to `wchar_t`; calling `setlocale(LC_CTYPE, …)` to a
   UTF-8 locale inside the driver, so the engine's behaviour becomes a
   property of the PROCESS ENVIRONMENT rather than of the config; and a
   length unit of CHARACTERS rather than bytes, which breaks the
   `consumed_length` convention `testees/tre/CLAUDE.md` (b) states and
   makes every per-byte throughput number non-comparable with every
   other row in the table. That is a new adapter, not a new config.
3. **The honest alternative is already covered.** Running `tre-default`
   (byte) over UTF-8 subjects measures what a byte engine does to UTF-8
   text — which is exactly what growth (k)'s `pcrec -e byte` mirror
   measures, more cheaply, with a SAME-ENGINE control on the other side
   of one variable. A cross-engine byte-vs-utf8 comparison confounds the
   encoding with the engine.

**What is named, not built:** a `tre-wide` config, as roster growth
(§6's closing note). The two things that must be settled before it opens
are in reason 2 — the locale dependency and the length unit — and both
are adapter-design questions, not set questions. **§14 Q4** puts the
ruling to the manager; the recommendation is the exclusion above.

### 7.4 Which engines sit OUT of which family

Derived from each adapter's own declaration and CLAUDE.md. **Every
UNCONFIRMED row below must be settled by a WITNESS COMPILE per (config,
token) before that config's declaration ships** — the L5 lesson, which
found three wrong `pcrec-*` declarations in `bench/capability`'s first
cut (`bench/capability/NOTES.md`, "L5's re-verification").

| family | who sits out, and why | confidence |
|---|---|---|
| **(a)** `cls-w-ucp`, `cls-w-ascii`, `cls-d-ascii`, `cls-s-nbsp`, `cls-posix-alpha` | the class-SCOPE split (§7.5) — `pcrec-*` has NO UCP axis (UD §4.5) so every `unicode-class-scope` pattern is unsupported there; `rust-default`'s `\w` is Unicode-aware by default so every `ascii-class-scope` pattern is unsupported there | pcrec: **CONFIRMED** (UD §4.5). rust: **CONFIRMED** (`testees/rust/CLAUDE.md`, unicode mode default true) |
| **(a)-(f)** all | `tre-default`, via `utf8-encoding` (§7.3) | **CONFIRMED** |
| **(f)** all `prp-*` | `tre-default` only (no `\p` construct exists at all — `testees/tre/CLAUDE.md` item 3, measured: `\p{L}` and `\p{Alpha}` both refuse with code 10). **Vectorscan does NOT sit out**: `testees/vectorscan/driver.c:50-53` records a MEASURED A/B — `\p{L}` compiles identically with and without `HS_FLAG_UCP` — so the general-category family is live there | tre: **CONFIRMED**. vectorscan: **CONFIRMED** (measured, this repo's own A/B) |
| **(f)** `prp-greek-sc`, `prp-cyrillic`, `prp-han`, `prp-latin` | Script and Script_Extensions spellings differ by engine: RE2 documents `\p{Greek}` script support but **`scx=`/Script_Extensions is not established**; the Rust `regex` crate documents both but **not verified at crate 1.13.1 here**; `onig-utf8` is a re-census (§7.1) | **UNCONFIRMED across three engines** — one witness each |
| **(c)** all `ci-*` | none expected to sit out — every roster engine has a caseless mode — but `ci-kelvin` / `ci-long-s` (the closure reaching outside the range) are where an engine with a PAIRWISE rather than a CLOSURE fold would diverge in ANSWER, not in capability | the divergence is the finding, not a gap |
| **(e)** `asr-lb-*` | `re2`, `rust`, `vectorscan` refuse all lookaround (CAP §5.1, three sources fetched); `tre` excluded | **CONFIRMED** |
| **(e)** `asr-a-z` | `tre` has no `\z` (CAP §6.2's measured finding, `true-end-anchor`) — excluded anyway | **CONFIRMED** |

**Consequence, and it is the correct outcome, not a gap:** the
`unsupported-by-declaration` share on this set will be LARGE — larger
than on `bench/capability`, because `utf8-encoding` alone removes one
engine entirely and the class-scope split removes a handful of patterns
from two more. CAP §6.3's rule applies verbatim: *the reporter must
render it as a count, not an absence.*

### 7.5 Three new REQUIRES tokens

The vocabulary is closed and global today
(`pcrecbench/capability.py:87`). This set needs three additions:

| token | what a pattern needs | who does NOT satisfy it |
|---|---|---|
| `utf8-encoding` | the engine must interpret pattern AND subject as UTF-8 character sequences, not byte sequences | `tre-default` (§7.3); every existing BYTE-mode config of every engine |
| `ascii-class-scope` | `\w` / `\d` / `\s` / POSIX classes must be ASCII-scoped under UTF-8 (PCRE2's default absent `PCRE2_UCP`) | `rust-default` (unicode mode on by default); any engine whose class scope is Unicode-by-default |
| `unicode-class-scope` | `\w` / `\d` / `\s` must be Unicode-widened (PCRE2's `PCRE2_UCP`, Vectorscan's `HS_FLAG_UCP`) | every `pcrec-*` config (UD §4.5: no UCP axis); any engine with no widening dial |

**Why two class-scope tokens rather than one per-config dial.** A dial
would make the class scope a TESTEE property and the pattern's answer
ambiguous — the same pattern would have two correct answers depending on
who ran it, which is exactly the cross-convention scoring machinery
`bench/capability` family 11 is still waiting on (CAP §5.6, CB1).
Two tokens make the scope a PATTERN property with one canonical answer
each, scored by the machinery that already ships. It also reads forward
from CAP §6.2's own rewrite-table row: `\d` → `[0-9]` "only if the
canonical pattern did not request Unicode-widened classes", which is the
same distinction named as a variant question rather than a capability
one.

Adding tokens to a GLOBAL vocabulary touches shared code and every
adapter's declaration. **§14 Q3**; recommendation: keep the vocabulary
global and add the three — a capability token is a cross-engine fact,
and making the vocabulary per-set would let two sets disagree about what
`lookaround` means.

### 7.6 Vectorscan's UCP flag breaks `\b` — a measured warning this set inherits

`testees/vectorscan/driver.c:50-53` carries a MEASURED A/B that bears
directly on family (e) and on the `unicode-class-scope` token, and it is
recorded here rather than rediscovered by the U2 lane:

> `VS_DRIVER_FLAGS` is 0 — `HS_FLAG_UCP` is NEVER set, on the MEASURED
> A/B in CLAUDE.md: `\p{L}` compiles identically with or without it,
> while setting it BREAKS `\b` on five real corpus patterns (40/64
> corpus compiles at 0 vs 35/64 under UCP).

Two consequences:

1. **`unicode-class-scope` is NOT satisfiable by simply setting
   `HS_FLAG_UCP` on a vectorscan config.** A flag that widens class
   scope and simultaneously makes five `\b`-bearing patterns refuse is
   not the same dial `PCRE2_UCP` is. The `vectorscan-block-nosom-utf8`
   config proposed in §7.1 therefore declares `ascii-class-scope`
   SATISFIED and `unicode-class-scope` UNSATISFIED, with the A/B above
   as its `declaration_ref` — and `asr-b-cyr-ucp` becomes a
   `pcre2-utf-*`-only row.
2. **A second vectorscan config carrying `HS_FLAG_UTF8|HS_FLAG_UCP` is
   named, not built.** If it is ever wanted, its acceptance is the same
   A/B re-run over THIS set's patterns, and its expected shape is a
   larger refusal census on family (e), not a wider capability. That is
   roster growth (§6's closing note), and it should not be smuggled into
   the first config on the theory that "UCP is what UTF-8 sets use".

This is also the sharpest available argument for §7.5's decision to make
class scope a PATTERN property with two tokens rather than a per-config
dial: on one roster engine the "dial" is not a dial at all.

---

## 8. The oracle

### 8.1 The chain

> **Every expectation in `utf8@0.1` is derived from libpcre2 10.46
> compiled with `PCRE2_UTF`, plus `PCRE2_UCP` on exactly those patterns
> declaring `unicode-class-scope`, and `PCRE2_MULTILINE` on exactly
> those declaring it. `method = libpcre2-differential`, as every other
> set.**

- `PCRE2_UTF` on EVERYTHING expectation-gated. There is no per-subject
  or per-regime variation: a set whose oracle option word varied by
  subject would have two definitions of "correct" in one
  `expectations.tsv`.
- `PCRE2_UCP` is a **per-pattern DECLARED FACT**, carried as the
  `unicode-class-scope` REQUIRES token (§7.5) and as the oracle's own
  option word for that pattern's rows. The twelve patterns affected are
  named in §5 and the pairs are stated: `cls-w-ascii`/`cls-w-ucp`,
  `asr-b-cyr`/`asr-b-cyr-ucp`, `ci-e-acute`/`ci-ucp-invariance`.
- **The oracle module does not do this today.** `pcrecbench/oracle_
  pcre2.py:47` declares `PCRE2_UTF` with the comment *"not used: this
  module stays byte-oriented like pcrec"*, and `:308` says *"this bench
  never compiles a utf8 artifact."* Both lines stop being true. The
  change is the one `bench/syntax/NOTES.md`'s own "Room for a utf
  family" predicted — "a design change to `oracle_pcre2.py` (one option
  argument)" — and §8.4 is the part that prediction did not see.

### 8.2 `PCRE2_NO_UTF_CHECK` — the rule

> **`PCRE2_NO_UTF_CHECK` is NEVER passed on expectation derivation, at
> any release, for any pattern or subject.**

`NO_UTF_CHECK` makes the subject's validity the CALLER's promise. Pass
it over a subject that is not valid UTF-8 and the library's behaviour is
undefined — so a derivation that used it over growth (h)'s ill-formed
subjects would not be recording a documented answer, it would be
recording whatever this build did today. The rule is stated here, before
(h) exists, because the temptation arrives exactly when (h) is being
built and the oracle starts refusing subjects.

The consequence, stated so the build lane cannot mistake it for an
obstacle: **plain `PCRE2_UTF` REFUSES an ill-formed subject outright**
(AX axis03's header enumerates the nine measured error codes at
libpcre2 10.37: `isolated-continuation = -22`, `illegal-fe-ff = -23`,
`overlong-2byte = -17`, `surrogate = -16`, `above-10ffff = -15`, …).
That refusal is a DOCUMENTED ANSWER and is exactly what (h) records for
PCRE2 — it is not a failure of the derivation.

### 8.3 Growth (h)/(i)/(j): documented behaviour, not a ranked cell

**PROPOSED POLICY:** the ill-formed-subject, surrogate and overlong
families are recorded as a **per-engine documented-behaviour TABLE**,
one row per (engine, ill-formed kind, position), each row carrying that
engine's own documented answer WITH ITS CITATION and the witnessed
behaviour beside it. They are **not** expectation-gated ranked cells.

The reason is that there is no cross-engine canonical answer to be
right about:

- PCRE2 under plain `PCRE2_UTF` REFUSES the subject; under
  `PCRE2_MATCH_INVALID_UTF` it gives a BARRIER answer (the ill-formed
  bytes match nothing and are not crossed).
- pcrec's ruled semantics are the barrier answer *without* a validation
  pass — UD §2.6, and AX axis03's header states it as the ruling under
  test: *"an ill-formed byte sequence matches NOTHING under pcrec's
  `utf8` encoding — no validation pass, no error return."*
- RE2, Rust and Vectorscan each have their own documented posture, none
  of them established in this repo today.

Ranking three different documented behaviours against one canonical
expectation would manufacture wrong answers out of correct ones. The
table is the honest instrument, and it is what `~/pcrec/tests/utf8`'s
own axis-3 file does on the correctness side.

**Whether the bench may instead declare `PCRE2_MATCH_INVALID_UTF` as a
SECOND canonical answer for (h) is a ruling, not a design choice —
§14 Q10**, asked at (h)'s own charter rather than now.

### 8.4 The find-all advance — the sharpest harness change this set forces

`pcrecbench/oracle_pcre2.py`'s `_find_all_impl` advances
`pos = e if e > s else s + 1`, and its own docstring says why that is
safe today: *"Byte encoding: S3.1.1's `<prefix>_next_pos` residual is
`start + 1` (every position is a character boundary); this bench never
compiles a utf8 artifact."*

Under UTF-8 that is false in both directions:

1. `s + 1` after an EMPTY match at a multi-byte character lands
   MID-CHARACTER. PCRE2 with `PCRE2_UTF` rejects a mid-character
   `startoffset` with `PCRE2_ERROR_BADUTFOFFSET` — so the derivation
   would ERROR, loudly, which is the good case.
2. Every DRIVER's find-all loop has the same shape (the protocol is
   stated once, at the top of `pcrecbench/adapters.py`, and KB-17 adopted
   pcrec's `match_api.md` S3.1 rule BY REFERENCE). A driver that steps
   one byte would produce a different NMATCHES from one that steps one
   character — a harness difference masquerading as an engine
   difference, which is precisely what the shared protocol exists to
   prevent.

**The change:** the advance becomes "the next CHARACTER boundary at or
after `s + 1`", in the oracle and in every driver, applied only under a
UTF-8 config. This is KB-17's rule re-derived per encoding rather than a
new rule. It is a HARNESS change, it is the single largest piece of work
this set requires outside the set directory, and it must land and be
checked (a `make check-harness` arm with its own negative case: a
byte-stepping advance must FAIL the check) **before** the first
expectation is derived — not after, because an expectation derived under
the wrong advance is a committed wrong answer.

This is also why axis 9 is marked "0.1 partial" in §3.2 rather than
"0.1": the throughput regime exercises the advance on day one, so the
change is not deferrable to (g).

### 8.5 What the oracle cannot settle

`prp-greek` vs `prp-greek-sc` is oracled from libpcre2 10.46 like
everything else — but AX's [M5.0] stage-5 section records that the two
local libpcre2 builds on the pcrec author's box DISAGREED with the
10.46 reference on three cells (U+00B7 and U+0300 under
`\p{Greek}`/`\p{scx=Greek}`), because Unicode revised those characters'
Script_Extensions between 14.0.0 and 16.0.0. **Consequence for this
set:** the Unicode version behind the oracle library is a PROVENANCE
fact that must be recorded beside the expectation, and a re-derivation
on a different box can legitimately differ on exactly those cells. The
subject pair for `prp-greek`/`prp-greek-sc` should therefore AVOID
U+00B7 and U+0300 and use U+0342 (which AX names as a stable flipper),
with the avoided pair stated in `NOTES.md` as a known version-sensitive
region rather than silently unused.

---

## 9. Engine neutrality — R-BENCH-4, and the mirror boundary

**No pcrec-oracled limit, cap or refusal boundary appears anywhere in
this set's patterns, subjects or expectations.** This is the ruling
Frank cleared `bench/altwide@0.2` under ([B31], 2026-09-02: "NO
pcrec-oracled limits file in the set"), and it binds here for a sharper
reason than usual: this set's own subject matter is a pcrec milestone,
so the temptation to shape a rung against a pcrec limit is structural.

Concretely:

- **No `oracle_limits.tsv`.** `bench/bounded` and `bench/altwide` each
  carry one because their give-up axis is a COUNT or a WIDTH with a
  measurable first refusal. This set's axis is the ENCODING, which has
  no rung ladder, and no pattern here is positioned against a pcrec cap.
- **`prp-ingreek`'s refusal is a PCRE2/Unicode fact** (error 147, and
  there is no `InGreek` property), not a pcrec boundary — §5(f).
- **The expected `\p` size cliff is a PREDICTION, not a design
  input.** AX's K53 story records that `\p` general-category blocks
  exceeded the emitted-source cap under `utf8` at default axes and were
  parked for four days, and UD §3.3 is titled "The table-size problem".
  That is a real expectation about what family (f) will do on a pcrec
  config — and it lives in **P7**, a prediction scored after the fact,
  never in the choice of which properties to carry.
- **The `-e byte` MIRROR is a TESTEE-CONFIG fact, not a set fact.** The
  set's patterns and subjects do not change for it; four more pcrec
  configs run the same `utf8@0.2` cells under a different encoding flag.
  The mirror's INTERPRETATION (that a class wrapping a multi-byte
  literal is byte-decomposed, AX axis01/02 mirror headers) belongs in
  the ledger, and the large `did-not-compile` census where `\x{...}`
  above 0xFF is range-refused is an expected outcome of running a
  UTF-8-shaped corpus under a byte config — a census, not a set defect.

The boundary in one sentence: **the SET says what the patterns and
subjects are; the ROSTER says under which encoding each engine reads
them; the LEDGER says what the difference means.**

---

## 10. Regimes, metrics, and the cell-time arithmetic

### 10.1 Regimes

**DECISION: `search_short` + `throughput`. NOT `match`.**

I-90 clause 1 names exactly these two. The set-wide `match` exclusion
follows `bench/capability`'s (CAP §3.5) and gains one reason of its own:
the lexical whole-subject wrapper `(?:<pattern>)\z` is applied per
adapter with three different spellings today (pcrec's `\z`, TRE's
`^(?:…)$`, rust's `\A(?:…)\z`), and a wrapper is exactly the kind of
lexical edit whose interaction with an ENCODING nobody has checked. The
three patterns that need a whole-subject reading carry their own anchors
instead (`cls-dot-rep`, `lit-anchored-run`, `asr-a-z`, `prp-l-anchored`)
— which is what `bench/loglines` does for the same reason.

`short_search_max_bytes = 512`, matching `bench/capability`.

### 10.2 Metrics

CAP §7.5's table applies unchanged; two rows need a sentence here:

- **`emit_bytes` / `emit_code_bytes`** on pcrec compile rows are where
  the encoding's cost is most visible (a multi-byte class lowers to a
  byte-sequence automaton; a fold set over Cyrillic is twelve closures).
  R5 and P7 both read them.
- **The lead-byte histogram** of each subject is set-directory data
  (§4.2), not a record field. It is read at ledger time to explain a
  throughput number, never scored.

### 10.3 The arithmetic

Following `bench/syntax/NOTES.md`'s model and its premise: the harness
calibrates each (pattern, regime) loop so the median subject's loop is
50 ms, so a (pattern, regime, trial) costs ≈ 50 ms × n_subjects,
independent of the testee's speed.

| term | arithmetic | per cell |
|---|---|---|
| `search_short` | 74 patterns × 6 passes (1 probe + 5 trials) × (50 ms × 90 subjects ≈ 4.5 s) | **~33 min** |
| `throughput` | 6 passes × 74 patterns over ~1.58 MB | **~5-12 min** (the property classes and the 64-branch alternation are the slow members) |
| pcrec compile, one form × 74 | ~1-3 s each | **~2-4 min**, compiled testees only |

**Estimate: ~40 min per `pcre2-*`/`re2`/`rust`/`onig` cell, ~45 min per
pcrec cell.** Against `CELL_CAP`'s 5,400 s default that is **~2×
headroom** — thinner than `capability@0.1`'s (~2-2.5×) and much thinner
than the design's original 5×, so it is stated as a risk (§15 R3) with
its lever named: **dropping the per-script 64 KB throughput arm
(§4.3) removes four subjects and recovers ~4 min/cell**, and reducing
the short set from 90 to 75 recovers ~5 min. Both are one-line changes
to a generator.

**Window sizing.** Twelve v1 configs (pcre2 ×3, pcrec ×4, re2, rust,
onig, vectorscan) × ~42 min ≈ **8.5 h** — more than one night under
BD7. **§14 Q6** proposes the first sample as **seven cells**
(pcrec ×4 + `pcre2-utf-interp` + `pcre2-utf-jit` + `rust-default`
≈ 5 h), with the remaining five at `@0.1`'s second window. That cut is
chosen so the first sample carries I-90 §5's three named first
customers in full and the widest capability contrast (rust) at once.

---

## 11. The predictions — P1-P10

Stated before any cell runs. **The machine-readable TSV is NOT committed
by this note**: `docs/dev/predictions/CLAUDE.md`'s `stated_utc` is
checked against the earliest `store/index.tsv` timestamp for this
(subbench, version), and the transcription happens at first-run time, on
the built set's real pattern ids. What follows is the source that
transcription reads, in the house's fifteen-column shape (selector /
quantity / reducer / op / bounds), with each clause written so it is
expressible — `n_wrong`, `pass_rate`, `median_ns`, `status`,
`compile_outcome` and the size columns, never an answer or a span
(§6.4's limit).

- **P1 — the offset-skip ORDER PAIR (I-90 §5's first named customer).**
  `lit-offset-at-head` (`@é`) and `lit-offset-at-tail` (`é@`) differ in
  `search_short` `median_ns` on the `lat` subjects by more than ×1.5 (the
  v1.4 spread rule's own k) on every `pcrec-*-utf8` config. **Clause
  P1.b, NOT machine-scoreable and stated as prose:** the two artifacts
  stamp DIFFERENT `RX_REQ_BYTE` values — FP §3.1 measured 0x40 for one
  ordering and 0xA9 (é's continuation byte) for the other on the shipped
  compiler — which is the mechanism behind P1.a.
- **P2 — the high necessary byte (I-90 §5's second).** `lit-run-3`
  (`日本語`, every necessary byte ≥ 0xE6) has a `throughput` ns/byte on
  the `cjk` 64 KB subject at least **×2** `lit-mixed-ascii`'s on the same
  subject, on `pcre2-utf-interp` and on every `pcrec-*-utf8`. The
  mechanism: 0xE3-0xE9 leads are roughly a third of CJK text's bytes, so
  a required-byte filter on a high byte dismisses almost nothing, where
  the ASCII `@` in `lit-mixed-ascii` dismisses nearly everything. **This
  is FP §3.2's inversion, restated as a measurable cell.**
- **P3 — the same inversion does NOT hold on the ASCII control.** On
  the `asc` 64 KB subject, `lit-run-3` and `lit-mixed-ascii` both find
  zero matches and their ns/byte agree within ×1.5 — the control that
  says P2 is about the histogram and not about the pattern.
- **P4 — the fold sets (I-90 §5's third).** On every `pcrec-*-utf8`
  config, `ci-moskva`'s `emit_bytes` exceeds `ci-ascii-control`'s by more
  than **×1.5**; and no `ci-*` pattern's `search_short` cell carries
  `n_wrong > 0` on any roster testee — in particular `ci-strasse` does
  NOT match `STRASSE` and `ci-turkish-i` does NOT match U+0130/U+0131,
  which is axis 7's simple-folding claim (UD §4.1) read as a
  cross-engine expectation.
- **P5 — the UCP census.** Every pattern declaring
  `unicode-class-scope` (`cls-w-ucp`, `asr-b-cyr-ucp`,
  `ci-ucp-invariance`) carries `compile_outcome =
  unsupported-by-declaration` on all four `pcrec-*-utf8` configs (UD
  §4.5: pcrec has no UCP axis) and compiles cleanly on every `pcre2-utf-*`
  config.
- **P6 — encoded length.** `cls-dot-rep` (`^.{5}$`) reads `n_wrong eq 0`
  on every testee that compiles it, against a subject pair containing a
  5-character / 12-byte hit and a 5-BYTE / 3-character miss — the
  encoded-length claim as a checkable answer rather than a belief.
- **P7 — the property size cliff.** At least one family-(f) pattern
  carries `compile_outcome = did-not-compile` on a default-cap
  `pcrec-*-utf8` config and compiles on the raised-cap sibling. Basis:
  AX's K53 record (twelve `\p` general-category blocks exceeded the
  emitted-source cap under `utf8` at default axes) and UD §3.3's
  "table-size problem". `prp-l`'s `emit_bytes` exceeds the family-(b)
  literal median by more than **×10** on every compiled config (R5's own
  band).
- **P8 — the floor is free.** The floor `~`'s `throughput` ns/byte
  agrees within the spread band between `pcrec-auto-utf8` and
  `pcrec-auto` (byte) on the `asc` subjects — i.e. the encoding costs
  nothing on a single-ASCII-byte pattern over ASCII text. **Scored at
  0.2**, when (k)'s mirror arm exists; stated now because it is the
  mirror's zero point and a prediction stated late is a prediction
  nobody believed.
- **P9 — rust is correct, not lucky.** `rust-default` reads
  `n_wrong eq 0` on every (a)-(f) pattern it compiles, with the
  `ascii-class-scope` patterns appearing as
  `unsupported-by-declaration` rather than as wrong answers. Basis:
  `testees/rust/CLAUDE.md`'s measured unicode-mode finding. **A refuted
  P9 is a finding about this repo's byte-mode sets**, not only about
  this one.
- **P10 — vectorscan agrees at the grain it has.** On every (a)-(f)
  pattern `vectorscan-block-nosom-utf8` compiles, its boolean
  match/no-match answer agrees with `pcre2-utf-interp`'s
  (`n_wrong eq 0`). The population this is scored over is expected to be
  SMALL — the lookaround and property families are mostly out (§7.4) —
  and that smallness is itself the census reading.

---

## 12. The outlier rule (R0-R8), stated before any run

To live in `bench/utf8/NOTES.md`, in `bench/syntax`'s and
`bench/capability`'s own shape. A CELL is (pattern × regime × testee);
a cell is listed under the FIRST rule it trips.

- **R0 — a wrong answer is read first**, before any speed comparison, on
  every cell (correctness before speed, APPROACH principle 1). P4, P6
  and P9 each predict `n_wrong eq 0` over a named population; any other
  wrong answer is a question.
- **R1 — a refusal on a pattern whose REQUIRES the config claims to
  satisfy is a finding, not a footnote.** Every `requires=` tag is a
  machine-checkable claim, so "should have compiled" is a fact the
  record can be checked against. `prp-ingreek` is the one expected
  refusal on every engine (§5(f)); P7 names the expected size-cap ones.
- **R2 — the `pcre2-jit` band** (Frank's own, I-42 (3)): a cell against
  `pcre2-utf-jit`'s same cell, worse than ×2 or better than ×20, in
  either direction.
- **R3 — the ENCODING band, this set's own rule.** A cell whose
  `median_ns` differs from the SAME pattern's same cell on the `asc`
  subject population by more than **×3**, where the pattern is
  PURE ASCII (the floor, `ci-ascii-control`, `asr-b-ascii`). Those three
  patterns should cost the same whatever corpus they run over; a
  difference is the SUBJECT's byte structure reaching a mechanism that
  should not have noticed.
- **R4 — the script band.** Within one family, a cell's ns/byte across
  the four per-script 64 KB throughput subjects, spread by more than
  **×4**. Four is chosen against the encoded-length ratio the corpora
  themselves carry (1 byte/char for `asc` to ~3 for `cjk`), so anything
  beyond it is not width.
- **R5 — compile and size cliffs** (compiled testees only): a pattern's
  compile time or `emit_bytes` beyond **×10** the testee's own median
  over the set. Family (f) is the predicted population (P7); a family
  (a) or (c) member tripping it is the question.
- **R6 — engine-selection surprises**, read off the record's mechanism
  stamps: a declined prefilter on a pattern with a strong lead-byte set;
  a `memchr` arm chosen where the class has two lead bytes
  (`cls-lead-pair` — UD §6.3's own row says the bitmap arm must take
  it); an engine route that differs between a pattern and its control
  twin.
- **R7 — a non-flat sweep.** `t-1m` ns/byte against `t-64k` ns/byte
  outside **[0.7, 1.4]** on one pattern and testee. Carried from
  `bench/syntax` R7 and `bench/capability` R6 unchanged, and read on
  EVERY pattern rather than on one named candidate — `bench/capability`'s
  own lesson (an unanchored negated-class pattern can go quadratic
  against a background lacking its terminator).
- **R8 — an `unsupported-by-declaration` share is a CENSUS finding, not
  missing data.** This set's share will be the largest in the repo
  (§7.4). It is read as a count per (engine, family) and never as an
  absence.

**Ranking** (I-42's direction, Frank: "algorithmically and generally
first, SIMD at the end"): R0, then R1, then any R2-R7 cell whose likely
fix is a GENERAL mechanism (a filter declined, a route chosen wrongly, a
fold set lowered expensively), then the rest, then anything whose fix
would be a SIMD one.

---

## 13. The build plan

Five lanes, in dependency order. None opens before the design panel.

| lane | what it builds | depends on |
|---|---|---|
| **U1** | the HARNESS half: `oracle_pcre2.py`'s per-pattern option word, the character-boundary find-all advance in the oracle and in every driver, the `make check-harness` arm with its NEGATIVE case (a byte-stepping advance must fail), and the three REQUIRES tokens in `pcrecbench/capability.py` | §8.1, §8.4, §7.5 — **nothing else can start** |
| **U2** | the ROSTER half: the new configs per engine (§7.1), each with a WITNESS COMPILE per (config, token) before its declaration ships, and the UNCONFIRMED rows of §7.4 settled | U1's tokens |
| **U3** | the SUBJECTS: the five word pools, `utf8text.py`, `gen_subjects.py`, `gen_throughput_subjects.py`, the two manifests and `subject_facts.tsv` with its `--check` | — (parallel with U1/U2) |
| **U4** | the PATTERNS: `patterns.rxt` as the source of truth with its `ext bench` roster block, `gen_patterns.py` rendering `patterns/*.rx`, the sidecar, `provenance.tsv` | U3 (for the typed short subjects), U2 (for the `ext bench` roster) |
| **U5** | the EXPECTATIONS and the set's `NOTES.md`: `gen_expectations.py` over the UTF-aware oracle, the outlier rule and growth plan transcribed from §6/§12, the predictions TSV transcribed at first-run time | U1, U3, U4 |

**U1 is the one that cannot be parallelised away and the one most
likely to surprise**: it changes shared code that six sets already
depend on, so its acceptance is that every existing set's
`expectations.tsv` re-derives BYTE-IDENTICALLY under the changed
oracle when no UTF option is requested. That check is the lane's first
deliverable, not its last.

---

## 14. Questions

Each carries a recommendation and the consequence of each answer.
**BLOCK** = a build lane should not open before it is answered.
**DEFAULT** = the recommendation is taken if nobody rules otherwise.

| # | question | recommendation | mark |
|---|---|---|---|
| **Q1** | Does the byte-clean ASCII control corpus (`asc`) RANK, or is it provenance-only? (Frank's own flagged item) | **RANK it.** It is the encoding-cost control (R3), the mirror's zero point (P8) and the only row that answers "what does UTF-8 cost when there is nothing to encode". Consequence if provenance-only: R3 and P8 both become unscoreable and the set can describe the encoding's cost only by comparing two testees, never two subjects | DEFAULT |
| **Q2** | Is a hand-authored per-script WORD POOL "generated" (house rule satisfied, no provenance record owed) or "sourced" (a provenance row per pool)? | **Generated.** Commit the pools, record `fidelity = synthesized` / `source_name = authored`, and state §4.1's limitation sentence in `NOTES.md`. Consequence of "sourced": a provenance gate over five word lists with no URL to cite, which the gate cannot check | DEFAULT |
| **Q3** | Is the REQUIRES vocabulary GLOBAL (`pcrecbench/capability.py:87`) or per-set? Adding three tokens (§7.5) touches shared code and every adapter's declaration | **Keep it global; add the three.** A capability token is a cross-engine fact. Consequence of per-set: two sets could disagree about what `lookaround` means, and the closed-vocabulary load check loses its point | DEFAULT |
| **Q4** | The TRE ruling (§7.3): EXCLUDED from v1 by an unsatisfied `utf8-encoding` token, with `tre-wide` named as roster growth? | **Yes, as proposed.** Consequence of including `tre-default` in byte mode: a BYTE-DECOMPOSED reading sits in the same ranking column as the UTF-8 ones. Consequence of building `tre-wide` now: a second driver model, a process-locale dependency and a character-not-byte length unit, all before the set's first sample | DEFAULT |
| **Q5** | `bench/syntax/NOTES.md` reserves `bench/syntaxutf/` for a UTF sibling. Does `bench/utf8/` RETIRE that reservation, or do both stand? | **Both stand.** They are different sets (§2.2) and `syntaxutf` gets cheaper once this one's machinery exists. Add one pointer sentence to the reservation. Consequence of retiring it: the registry-enumerated coverage claim for UTF-only seed rows is silently abandoned | **BLOCK** (it touches a documented commitment) |
| **Q6** | Which cells are the FIRST sample? Twelve v1 configs ≈ 8.5 h is more than one night (§10.3) | **Seven cells**: `pcrec-*-utf8` ×4 + `pcre2-utf-interp` + `pcre2-utf-jit` + `rust-default` ≈ 5 h. It carries all three of I-90 §5's first customers and the widest capability contrast. The other five at `@0.1`'s second window | DEFAULT |
| **Q7** | Growth ordering: 0.2 = (g)+(k), 0.3 = (h)+(i)+(j)? | **Yes.** (h)/(i)/(j) share one policy (§8.3) and one subject-generation problem; splitting them ships the policy twice | DEFAULT |
| **Q8** | Axis 11's caller-supplied mid-character `startpos` needs a driver-protocol `--startpos` (§3.3 gap 3). Worth a protocol extension? | **No, and say so in `NOTES.md`.** It is a correctness question `~/pcrec/tests/utf8/axis11` already owns, and a protocol parameter used by one family of one set is a maintenance cost six other sets pay | DEFAULT |
| **Q9** | Does the per-pattern oracle option word live as a parameter on the shared `oracle_pcre2.py`, or does this set get its own oracle module? | **A parameter on the shared module** — `bench/syntax/NOTES.md` predicted exactly this ("one option argument"), and a second oracle module would mean two definitions of "the oracle" in one repo. Consequence: U1 changes shared code and owes the byte-identical re-derivation check (§13) | DEFAULT |
| **Q10** | At growth (h): may the bench declare `PCRE2_MATCH_INVALID_UTF` as a SECOND canonical expectation, or is (h) documented-behaviour-only? | **Documented-behaviour-only** (§8.3). Asked at (h)'s own charter, not now | **BLOCK at (h)** |

---

## 15. Risks

| # | risk | mitigation |
|---|---|---|
| **R1** | **U1's shared-code change breaks six existing sets.** The oracle and every driver's find-all advance are shared by `email`, `loglines`, `bounded`, `altwide`, `syntax`, `capability` | the lane's FIRST deliverable is the byte-identical re-derivation of every existing `expectations.tsv` under the changed oracle with no UTF option requested (§13), with a negative arm |
| **R2** | **An UNCONFIRMED capability row ships as a declaration.** §7.4's remaining UNCONFIRMED row is the Script / Script_Extensions spelling support across re2, rust and onig (vectorscan's `\p` row was CONFIRMED from this repo's own measured A/B while this note was being written — §7.6, which is itself the evidence for how easily such a row goes unchecked) | U2 requires a WITNESS COMPILE per (config, token) before any declaration ships — the L5 lesson, which caught three wrong `pcrec-*` declarations in `bench/capability`'s first cut |
| **R3** | **Cell time at ~2× `CELL_CAP` headroom** (§10.3), thinner than any existing set | two one-line levers named and pre-priced: drop the per-script 64 KB throughput arm (~4 min) or cut the short set 90 → 75 (~5 min). Neither changes a pattern |
| **R4** | **Family (f) refuses on default-cap pcrec configs**, taking a twelfth of the set with it | this is P7, not a surprise — and it is a FINDING (AX's K53 is the same shape on the correctness side). If it happens broadly, the `-bigcap` sibling is the arm that reads it, and the refusal census is the result |
| **R5** | **The generated corpora do not resemble real text closely enough** for the histogram claim to carry | the claim is deliberately narrow (§4.1's limitation sentence: byte histogram and character-width statistics, NOT word or sentence statistics) and the histogram is a committed, re-derived table (§4.2), so a reader can check the claim rather than trust it |
| **R6** | **The Unicode version behind the oracle library shifts the Script_Extensions answers** (§8.5) | the affected characters (U+00B7, U+0300) are avoided in the subject pair; the Unicode version is recorded as provenance; `NOTES.md` names the region as version-sensitive |
| **R7** | **The set is read as a pcrec milestone's acceptance test.** Its subject matter IS a pcrec milestone, which makes engine-neutral authorship harder than usual | §9's boundary, stated three ways, plus the R-BENCH-4 check that no limits file exists; and the cross-engine roster (§7.1) is six engines wide precisely so no single engine's behaviour can be mistaken for the axis |
