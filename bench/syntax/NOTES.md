# bench/syntax — the syntax census: one construct per pattern, and what an outlier means

Plan row [B36]; the charter is inbox I-42 (Frank, 2026-09-03). Written
BEFORE any run: every prediction below is dated 2026-09-05 and is what the
author believed from the PCRE2 reference and the registry seed alone. The
first sample will confirm or refute each one by name.

## The objective, and what would defeat it

The depth sets (`bounded`, `loglines`, `email`, `altwide`) each ask ONE
mechanism question and answer it to the rung. What they cannot do is find
the question nobody has asked yet: the construct whose cost, refusal, wrong
route or wrong answer hides in a corner of the syntax no depth set visits.
The census visits every corner ONCE, cheaply, with the same instrument, and
its output is not a verdict but a ranked list of QUESTIONS (I-42 (4)), each
of which becomes a depth probe of the bounded-rung shape before any pcrec
row is chartered.

Three things would defeat it, and the design is shaped against each:

1. **Enumerating from a head.** A set written from what its author
   remembers of PCRE omits what the author forgot. The construct list is
   pcrec's `--list-syntax` REGISTRY at our pin (`list_syntax_9a1583ba.tsv`, re-seeded at the [B39] pin from the 334fd10e seed it was authored from — one description row moved, nothing machine-read,
   copied verbatim with a source header), and `coverage.tsv` is DERIVED
   from the pattern table × the seed: every one of the seed's 138 rows is
   covered by a pattern, covered through the seed's own `family` column (a
   spelling of a covered construct), excused by a stated reason, or a
   PCRE2 reject the oracle cannot judge. A row nobody covers and nobody
   excuses FAILS `gen_patterns.py --check` by name, so a re-seed at a later
   pin (pcrec's rows move; at abi 23 `\x{...}` and utf8 moved to the base
   grammar) widens the census rather than silently under-covering it.

2. **Inheriting the code author's alphabet** (pcrec D27). The patterns
   were written from `man pcre2pattern` and the seed's `syntax` column
   only. See "Origin" for exactly what the author did and did not read.

3. **An outlier that points at three things.** Every pattern exercises
   ONE construct in an otherwise plain body drawn from one small
   vocabulary, and most constructs have a body TWIN that spells the same
   language without the construct (`a++ab` / `a+ab`, `(?>a+)b` / `a+b`,
   `(cat)` / `cat`, `item\Rdone` / `item\r\ndone`, the five subroutine-call
   spellings of "four digits"). A cell that stands out from its twin is a
   construct cost; one that stands out with its twin is a body cost, and
   the body is the same everywhere in the set.

## The patterns

Ninety-five, in eighteen mechanism FAMILIES (the `fam-*` tag; the family is
a mechanism class, not a seed module — `anchors` holds a `bare` row, an
`assertions` row and a `modifiers` row). The authoritative table is
`gen_patterns.py`'s `PATTERNS` (id, family, seed rows exercised, text,
note) and the derived `pattern_facts.tsv` (PCRE2's own start-of-match
facts, capture / backreference / lookbehind / match-empty facts, m/n per
regime). This is the reader's summary:

| family | patterns | what the family reads |
|---|---|---|
| `literal` | `lit-cat` = `cat` | the three-byte literal fourteen other patterns spell with one construct added |
| `anchors` | `^item` `done$` `\Aitem` `done\Z` `done\z` `\Gitem` `(?m)^item` `(?m)done$` | does an engine KNOW the pattern is anchored (P5), and the `$`/`\Z`/`\z` final-newline edge |
| `assertions` | `\bcat\b` `\Bcat\B` `key=\K\w+` | the boundary tests, and a reported start that is not the match start |
| `classes` | `\d+` `cat\s+sat` `\S+@\S+` `\w+` `key\h*=\h*value` `item\v+done` `it\Nm` `[[:alpha:]]+` `c[^aeiou]t` `0x[0-9a-fA-F]+` `c.t` `c[aA]t` `c[ac]t` `c[a-zA-Z]t` `(?i)c[aeiou]t` | eight class escapes, the POSIX bracket, the three base bracket shapes, and four of the five FOLD-PAIR WITNESSES (below) |
| `quantifiers` | `ca*t` `a+b` `colou?r` `".*?"` `a*+b` `a++ab` `a+ab` `a?+a` `a{1,2}+b` | greedy, lazy, the four possessive suffixes; `a++ab` can never match and `a+ab` is its control |
| `groups` | `(cat)` `(?:ab)+` `(?<w>cat)` `(?'w'cat)` `(?>a+)b` `(?>a\|ab)c` `ca(?#comment)t` `(?\|(cat)\|(dog))` `ca(?C1)t` | capture and its spellings, atomic over a repeat and over an alternation (the latter FAILS on `abc`), comment, branch-reset, callout |
| `alternation` | `cat\|dog` `(?:c\|d)(?:at\|og)` | two branches, and nested branches (bench/altwide carries the width) |
| `backrefs` | `(\w+) \1` `(\w)(\w)\2\1` `(\w+) \g{-1}` `<(?<t>\w+)>[^<]*</\k<t>>` `(?P<t>\w+) (?P=t)` | a doubled word four ways, a palindrome, a tag pair |
| `lookaround` | `item(?= done)` `item(?! done)` `(?<=item )done` `(?<!item )done` `(?*item)item` `item(*pla: done)` | the four, the non-atomic lookahead, one alpha spelling |
| `conditionals` | `(<)?item(?(1)>)` | a group-number condition |
| `recursion` | `\((?:[^()]\|(?R))*\)` `(\((?:[^()]\|(?1))*\))` `(?<p>\((?:[^()]\|(?&p))*\))` `(?(DEFINE)(?<d>\d{2}))(?&d):(?&d)` `(\d{2})\g<1>` `(?P<d>\d{2})(?P>d)` `(?+1)(\d{2})` `(\d{2})(?-1)` | balanced parens three ways, DEFINE, and "four digits" as a call four ways |
| `modifiers` | `(?i)cat` `(?s)item.done` `(?x) c a t # comment` `(?n)(ca)t` `(?U)".+"` `(?J)(?:(?<w>the)\|(?<w>\w+)) \k<w>` `(?a)\w+` `(?ir)cat` `(?i)c(?^)at` `(?i)c(?-i)at` | ten option settings; `(?m)` lives with the anchors |
| `escapes` | `key\tvalue` `item\ndone` `item\r\ndone` `\x63at` `caf\x{e9}` `bell\cGend` `\o{143}at` `item\040done` `\Qf(x)\E` | single-byte spellings and quoting |
| `misc` | `item\Rdone` `c\Xt` `c\Ct` | the three "misc" escapes in byte mode |
| `uniprop` | `\p{L}+` `\P{L}+` | Unicode properties over Latin-1 bytes, no UTF |
| `verbs` | `item(*ACCEPT)done` `a+(*SKIP)b` | two backtracking verbs |
| `extclass` | `(?[[a-z]-[aeiou]])+` | a set difference (the seed's `(?[[a]])` row; `--` and `&&` are NOT PCRE2 spellings, `-` and `&` are) |
| `floor` | `#` | requirements §5's per-call control |

**What was left out, and why** (all in `gen_patterns.py`'s
`NOT_EXERCISED`, each re-checked against the seed): the four complement
escapes `\D \W \H \V` (the same class mechanism with the set inverted),
`\3`..`\9` (the index is read; `\1` and `\2` witness it), `\a \e \f` (fixed
bytes; `\t \n \r \cG` witness the mechanism), the quoted call spelling
`\g'1'` and the root spelling `(?0)` (one pattern per spelling family),
the empty option `(?)`, the non-atomic LOOKBEHIND `(?<*...)` (its lookahead
twin is exercised), and `\N{U+0041}`, which PCRE2 accepts in UTF mode only
(the utf family's). The seed's five `rejected` rows (`\N{name}`, `(?PX)`,
`(?q)`, `[[.a.]]`, `[[=a=]]`) are PCRE2's own refusals: no oracle
expectation exists, so no pattern. The fourteen unicode-only / unbuilt
constructs are IN (P1): a refusal is a result here, and an engine that
does compile them gets measured.

**Why ninety-five.** Frank's charter said ~60-90 and the first table had
102; what came out were duplicate spellings (one per family, the rest by
the seed's `family` column), complements, and the inert `(?)`. What
stayed in over the count: the control pairs (`a+ab`, `lit-cat`) — an
outlier without its control is not a question, it is a number. The
four fold-pair witnesses were added after the first build on the
manager's ask (below).

**The five FOLD-PAIR WITNESSES** (tag `fold-pair-witness`; the manager's
ask of 2026-09-05 from the [B39] prep lane's census: no set in the bench
but altwide's `ci-256` / `ci-512` carries `(?i)` or a two-letter ASCII
fold-pair class, and pcrec's abi-23 [FORM-CHAR] STEP 1 turns exactly
that shape into a masked compare on the VM route, counted by the new
`RX_VM_CLS_FOLDS` stamp, so the next pin's AFTER needs witnesses here
with the `-fno-cls-fold` arm as their control).
Plain PCRE, oracled like the rest, one body: `(?i)cat` (`mod-i`, the
option over a literal), `(?i)c[aeiou]t` (`cls-i-class`, the option over a
class), `c[aA]t` (`cls-fold-pair`, an explicit two-member class that IS
a fold pair), `c[ac]t` (`cls-pair-ctl`, the CONTROL: two members, not a
fold pair — the same class size, a different set), and `c[a-zA-Z]t`
(`cls-mixed-case`, 52 members with every letter's pair present). All
five read against `lit-cat`; `cls-fold-pair` against `cls-pair-ctl` is
the one-variable pair (R3 does not apply: their languages differ).

## Blinded authorship — what the author read (D27)

The patterns and subjects were written from `man pcre2pattern` (PCRE2
10.46 on this box, the oracle's own version) and the seed's `syntax` /
`note` columns. The author did NOT open `testees/pcrec/`,
`pcrecbench/adapters.py`, pcrec's `src/`, `tests/` or corpora, this repo's
`store/`, `reports/` or the pcrec-facing ledgers while authoring. Two
pcrec documents WERE read, and are named so the reader can judge the
leak: the seed itself (its `note` column describes each construct in
PCRE2's terms, which is the seed's purpose), and the "How to read the
generated index" section of pcrec's docs/pcre2_compliance.md that I-42
points at for the `built` column's semantics — that section carries one
sentence on which call and atomic shapes force pcrec's VM, and the author
read it. No pattern here was shaped by that sentence: the recursion and
atomic patterns are the textbook forms (balanced parentheses; `(?>a|ab)c`
is the reference's own atomic-alternation example). The harness contract
(`docs/design/harness_contract.md` §2) was read in full as the set format,
and it documents the `(?:...)\z` whole-subject wrapper — that is where P2
comes from.

## The subjects

**Thirty FIELDS (2-14 B)** for the `match` regime, each typed as at least
one construct's whole-string hit and, where a construct has a semantic
edge, another's designed miss:

- `item done` / `item done\n` / `item\ndone` / `item\r\ndone` separate
  `$` and `\Z` (before a final newline) from `\z` (never), `\R` (one token
  for `\r\n`) from `\v+` (two bytes) from `item\ndone` (neither), and
  `(?s)item.done` from `it\Nm`.
- `aaab` is the possessive edge: `a+ab`, `a+b`, `(?>a+)b`, `a*+b`,
  `a{1,2}+b`, `a+(*SKIP)b` take it (whole or under search); `a++ab` cannot.
  `abc` is the atomic-alternation edge (`(?>a|ab)c` fails; `ac` is its hit).
- `Cat` / `CAT`: `(?i)cat` takes both; `(?i)c(?^)at` and `(?i)c(?-i)at`
  take `Cat` only.
- `caf\xe9`: `\p{L}+` and `caf\x{e9}` take it whole; `\w+` and
  `[[:alpha:]]+` stop at the Latin-1 byte (PCRE2's default C-locale
  tables — `pattern_facts.tsv`'s m/n columns say so per pattern).
- `the the`, `abba`, `<b>bold</b>`, `(a(b)c)` / `(a(bc)`, `12:34`, `2026`,
  `"hello"`, `f(x)`, `key=value`, `key\tvalue`, `bell\x07end`, `#42`:
  one construct family's whole-string hit each.

**Twelve LINES (≤ 86 B)** of the same vocabulary for `search_short`:
prose with and without doubled words, an order line (integer, date,
time, address, price, hex, `#42`), a tag line with one mis-closed pair
and a bare `<item>`, a paren line with one unbalanced open, `key=value` in
four spellings, LF and CRLF multi-line blocks, five casings of `cat`, a
quoted line with one unterminated quote, a Latin-1 line, and a 40-byte
`a` run followed by the possessive shapes.

**Three RUNS** (`t-64k`, `t-256k`, `t-1m`; 1.3 MB in all) of
`censustext.py`'s line grammar: eight parts prose to two parts order
lines and one part each of tags, balanced parens, key=value and quoted
strings, so every construct has SPARSE hits on a background where most
candidate starts fail. `#` never occurs (the floor is a full-length miss),
`\r` and control bytes never occur (the CR and control escapes are
throughput misses by design — their per-byte cost is a failing scan for a
byte the text does not contain), and the grammar has no fixed-length
repeating unit (`periodic = no` on all three, computed).

Both manifests' `description` column spells the family and arm in a fixed
vocabulary (`field/hit`, `field/edge`, `line/prose`, `line/structured`,
`run/mixed`) so records group without a sixth manifest column.

## Regimes

All three. `match` (anchored + end-anchored, whole subject) is the regime
the semantic edges are typed for. `search_short` reads each construct's
per-call cost on twelve lines. `throughput` is a SIZE SWEEP at fixed
density (64 KB / 256 KB / 1 MB, separate draws so no text is another's
prefix), because what a census needs from the regime is one per-byte
number per construct read against `pcre2-jit` and the floor, plus the
statement that the number is flat in the subject length; a construct whose
cost turns out to hinge on hit density gets a depth probe with a density
cross of its own (bench/altwide's shape).

Two regime facts a reader must carry:

- **The `match` regime cannot see lookbehind, lookahead-at-end or a
  `$` before a final newline**: under `PCRE2_ANCHORED|ENDANCHORED` nothing
  precedes offset 0 and nothing follows the match end, so
  `(?<=item )done`, `item(?= done)` and `done$` on `item done\n` are
  `nomatch` whole and hits under search. `pattern_facts.tsv`'s
  `match_m_n` column reads 0/42 for those by construction, not by
  accident.
- **`\G` is `\A` on this set's answers.** No subject has a second
  consecutive `item` at the cursor, so an engine that implements `\G` as
  `\A` answers every cell here correctly. The census measures `\G`'s
  cost; a depth probe with `itemitem` under find-all measures its
  semantics.

## The outlier rule — stated before any run

A CELL is (pattern × regime × testee); its number is the trial median the
harness records. Reads are per cell, in this order, and a cell is listed
under the FIRST rule it trips:

- **R0, wrong answers first.** Any cell whose answer disagrees with the
  oracle is excluded from every ratio and listed at the top of the
  questions (correctness before speed, APPROACH principle 1). P2 predicts
  two such cells and names the mechanism; any other is a question.
- **R1, refusals on a built row.** A `did-not-compile` on a pattern
  whose seed rows are all `built` (or base grammar) is an outlier. A
  refusal on a pattern that names an `unbuilt` row is the census's
  `unsupported` reading, listed in its own block, not ranked.
- **R2, the JIT band** (Frank's proposal, I-42 (3)): the cell against
  `pcre2-jit`'s same cell, worse than **×2** or better than **×20**. ×2 is
  the trial-agreement rule's k = 1.5 with headroom for a body difference;
  ×20 is the point past which a JIT loses to an ahead-of-time artifact
  only by a MECHANISM the JIT lacks (an anchoring fact it did not use, a
  scan it did not do), never by tuning — both directions are questions.
- **R3, the spelling rule.** Within a SPELLING GROUP — patterns whose
  answers are identical on every subject and regime, VERIFIED over
  `expectations.tsv` on 2026-09-05 (all 8,265 rows; re-verified after the four fold-pair witnesses were added): the four "four
  digits" calls `rec-g-angle`/`rec-py`/`rec-fwd`/`rec-back`; the three
  balanced-paren recursions `rec-r-uc`/`rec-1`/`rec-name`;
  `bak-1`/`bak-g-rel`/`bak-py`/`mod-j-uc`; `lka-pos`/`lka-verb`;
  `mod-reset`/`mod-unset`; `mod-i`/`mod-r`; `qnt-lazy`/`mod-u-uc`;
  `qnt-plus`/`grp-atomic-rep`; `anc-caret`/`anc-a-uc`/`anc-g-uc`;
  `anc-dollar`/`anc-z-uc`; `mod-a`/`cls-w`; and the `cat` group
  `lit-cat`/`grp-cap`/`grp-named`/`grp-named-quote`/`grp-comment`/
  `grp-callout`/`mod-x`/`mod-n`/`esc-hex`/`esc-octal-o`/`cls-dot` — any
  two members of one group on one testee that differ by more than
  **×1.5** (the v1.4 spread rule's k, so the difference is bigger than
  the instrument's own agreement band). A spelling that costs is a
  mechanism question by construction. (`lka-nonatomic` is NOT
  `lka-neg`'s twin: they differ on five cells, as they should.)
- **R4, the family rule.** A cell against the MEDIAN of the same
  testee's cells in the same family, in the same regime, beyond **×3**.
  Bodies inside a family differ in `min_length` by up to ×3 (3-byte
  `cat` to 9-byte `key=value`), so ×3 is the smallest band that does not
  flag body length; anything beyond it is the construct.
- **R5, compile and size cliffs** (compiled testees only): a pattern's
  compile time or emitted-artifact size beyond **×10** the testee's own
  median over the set. Every pattern here is under 34 bytes; a ×10 is a
  mechanism, not a body.
- **R6, engine-selection surprises**, read off the record's mechanism
  stamps (requirements §4.2): a backtracking route on a pattern
  `pattern_facts.tsv` shows REGULAR (captures 0, backref_max 0,
  max_lookbehind 0, no recursion, no verb) where the same testee took an
  automaton route on its twin; a declined prefilter on a pattern with a
  PCRE2 required code unit; a frameless artifact that pushes. The
  author cannot name the stamps blind; the report's buckets can.
- **R7, a non-flat sweep.** `t-1m` per-byte against `t-64k` per-byte
  outside **[0.7, 1.4]** on one pattern and testee: a per-byte cost that
  is not per-byte.

**Ranking** (I-42's direction, Frank: "algorithmically and generally
first, SIMD at the end"): R0, then R1, then any R2-R7 cell whose likely
fix is a GENERAL mechanism (an anchoring fact unused, a spelling that
costs, a route chosen wrongly, a wrapper that changes semantics), then
cells whose fix is a constant factor in one construct's matcher, and LAST
the scan-tier gaps on the dense class runs and literal scans (`\w+`,
`\p{L}+`, `[[:alpha:]]+`, `lit-cat`'s throughput cell) where "SIMD would
help" is the honest answer. Each question is phrased as a mechanism
question with its cell id, its twin's cell and its stamps.

## Predictions (P1-P13), 2026-09-05, before any run

- **P1 (the `unsupported` block, from the seed's own `built` column).**
  On every pcrec testee at the pin (the seed's `built` column is 334fd10e's, unmoved by the 9a1583ba re-seed; first sample at d34c9131), exactly these fifteen patterns
  are `did-not-compile`, each naming a module: `grp-comment` (comments),
  `grp-branch-reset` (branch-reset), `grp-callout` (callouts),
  `cnd-group` (conditionals), `msc-r-uc` `msc-x-uc` `msc-c-uc` `esc-ctrl`
  `esc-octal-o` (misc), `unp-p-lc` `unp-p-uc` (unicode-props), `vrb-accept`
  `vrb-skip` (verbs), `xcl-minus` (extended-classes), and
  `esc-hex-braced` (the braced `\x{...}` spelling requires
  `unicode-props` at this pin per the seed's note; at the abi-23 re-seed
  it moves to the base grammar and this one becomes an R1 candidate).
  The other eighty compile on every pcrec testee. Any refusal
  outside the fifteen is an R1 outlier; any of the fifteen compiling is
  a re-seed request.
- **P2 (the whole-subject wrapper changes two answers).** The harness
  contract builds a testee's whole-subject form as `(?:<pattern>)\z`.
  Under that wrapper `(?R)` recurses into the WRAPPER, so `rec-r-uc`'s
  match-regime answer on `(a(b)c)` differs from the oracle's
  (`(?:\((?:[^()]|(?R))*\))\z` cannot recurse past the `\z`); `rec-1`
  and `rec-name`, whose call targets are groups, are the controls and
  answer correctly. Likewise `vrb-accept` under the wrapper reports
  `item` (0-4) on `item done` where `ENDANCHORED` says `nomatch`. Both
  are R0 cells on every testee that wraps, and the question is the
  wrapper's, not the engine's — the census's first mechanism question is
  about the instrument.
- **P3 (spelling parity).** Every spelling group in R3 agrees within
  ×1.5 on `pcre2-interp` and `pcre2-jit` in every regime: PCRE2 compiles
  spellings to one opcode stream. The same on the compiled testees is
  the prediction with the least confidence in this list, and the one
  the census most wants to test.
- **P4 (possessive vs control).** `qnt-poss-plus` (`a++ab`) is no slower
  than `qnt-plus-ctl` (`a+ab`) in any regime on any testee: both fail
  everywhere on the runs, and a possessive can only prune.
- **P5 (start anchors are free).** `^item`, `\Aitem` and `\Gitem` are
  the three cheapest throughput cells in the set on every testee, at or
  below the floor's own per-byte number: an engine knows an anchored
  pattern fails at offset 0 and stops. `done$`, `done\Z`, `done\z` are
  at the literal-scan tier (PCRE2 gives them first code unit `d`): no
  engine in the roster is predicted to scan from the end. `(?m)^item`
  and `(?m)done$` are per-line: between the two tiers.
- **P6 (lookbehind costs what its body costs).** `(?<=item )done` and
  `(?<!item )done` are within ×1.5 of `lka-pos`/`lka-neg` on
  `pcre2-*` in every regime — PCRE2 starts both at the `d`.
- **P7 (the dense runs are per-MATCH cells).** `\w+`, `[[:alpha:]]+`,
  `\p{L}+`, `\P{L}+`, `(?a)\w+` and `(?[[a-z]-[aeiou]])+` match every
  word of every run (~200 k matches per MB), so their throughput
  numbers are dominated by the per-match restart, not the scan; the
  reader must not rank them as scan cells. Within that group `\p{L}+`
  against `\w+` on `pcre2-*` measures the property lookup: predicted
  under ×2.
- **P8 (`(?i)` on a literal).** `mod-i` against `lit-cat` on every
  testee: under ×1.5 in the short regimes; on the runs, a caseless
  first-byte scan against an exact one — the JIT band is not predicted
  to trip.
- **P9 (`\K`).** `asr-k-uc`'s reported span begins at offset 4 on
  `key=value` on every testee (R0 if not); its cost is `key`'s literal
  scan.
- **P10 (the atomic alternation).** `(?>a|ab)c` is `nomatch` on `abc`
  and `match` on `ac` on every testee (R0 if not); its throughput cost
  is within ×1.5 of `grp-atomic-rep`'s on `pcre2-*`.
- **P11 (recursion on the runs).** The three balanced-paren spellings
  cost the same (P3) and sit within ×3 of the backreference cells on
  `pcre2-*`: both start at one byte (`(` / a word byte) and do bounded
  work per start.
- **P12 (`(?J)`).** `mod-j-uc` agrees with `bak-1` on every subject and
  regime (a duplicate-name backreference resolves to the group that
  set), and costs within ×1.5 of it on `pcre2-*`.
- **P13 (compile-time flatness).** On every compiled testee, no
  pattern's compile time is beyond ×10 the median (R5): the largest
  pattern is 33 bytes. The recursion and backreference patterns are the
  candidates if one is.

## Room for a utf family (I-42, the [UTF-RW] harvest)

This set is BYTE MODE: the oracle binding is byte-oriented (`PCRE2_UTF`
unused, `oracle_pcre2.py`), the harness's subjects are bytes, and the
seed's UTF-only rows (`\N{U+0041}`, `\x{100}` and above, `(*UTF)`) are out
by that fact. The room is two conventions, documented here and carried by
the artifacts, with nothing built:

1. **Every pattern carries the tag `encoding-bytes`.** A utf family's
   patterns carry `encoding-utf8`; a report can bucket on the pair.
2. **The utf family is a SIBLING SET, `bench/syntaxutf/`, not a version
   bump of this one.** Its patterns need `(*UTF)` (or a compile option),
   its subjects are UTF-8 text, and its expectations need the oracle
   compiled with `PCRE2_UTF` — a design change to `oracle_pcre2.py`
   (one option argument) and to the sub-bench contract's "raw bytes"
   subjects, which is [DD-13]'s and the pcrec manager's territory
   (requirements §5, R6). A sibling directory keeps this set's records
   comparable and lets the two be run on the same night as two cells.
   The seed's rows would be re-read with `status`/`family` unchanged and
   the utf-only rows moving from `not-exercised` to `covered`.

## The floor pattern

`#`, one literal byte, `role = "floor"` (requirements §5). It occurs in
`#42` (a field) and once in the order line, and nowhere in the runs, so
the one pattern gives the harness's per-call overhead three readings: a
whole-subject hit on one field and misses on twenty-nine, a search hit on
two subjects and misses on forty, and a full-length `memchr` MISS over
64 KB, 256 KB and 1 MB — the per-byte floor every anchor and literal cell
is read against (P5).

## Give-ups and refusals are results

A pattern a testee refuses is a `did-not-compile` row with that engine's
own diagnostic (requirements §4.4). This set EXPECTS fifteen of them per
pcrec testee (P1) and treats them as its `unsupported` reading; a refusal
outside P1's list is R1. Nothing here should give up at match time —
there is no backtracking hazard by design (the one shape held out on
purpose is an unbounded `.` repeat under `(?s)`, quadratic on a 1 MB
subject with no newline barrier) — and the oracle derivation reported no
give-up on any of the 8,265 triples.

## Per-engine notes

- **libpcre2 (interp, jit).** Every pattern compiles at 10.46 in byte
  mode, callouts fire into no function (`(?C1)` is inert), `\p{L}` uses
  the library's Unicode tables over Latin-1 code points, and `(?a)` /
  `(?r)` are accepted (10.43+) and inert under the default tables. The
  JIT is the R2 reference.
- **pcrec (every pinned config).** No variant, no option: the canonical
  text is the artifact's source, and `--features all` is a testee flag.
  P1 names the predicted refusals from the seed's `built` column; P2
  names the wrapper's two wrong answers from the harness contract.
  Nothing else about pcrec's behaviour on these patterns is predicted,
  by design.

## Cell-time estimate, and its premise

One cell = one testee × 95 patterns × three regimes at `--trials 5`. The
harness calibrates each (pattern, regime) loop so the MEDIAN subject's
loop is 50 ms and caps a trial's predicted sweep at 20 s
(`pcrecbench/harness.py`, `calibrate`); a trial-set is one probe pass and
five trials.

**Premise.** For the two short regimes the calibrated loop makes a
(pattern, regime, trial) cost ≈ 50 ms × Σ cost_i / median cost over the
42 subjects, which for subjects of similar cost is ≈ 50 ms × 42 ≈ 2.1 s
and INDEPENDENT of the testee's speed (the loop count absorbs it). So:

| term | arithmetic | per cell |
|---|---|---|
| the two short regimes | 95 × 2 × 6 × ~2.1 s | **~40 min** |
| throughput, 6 passes × 95 patterns over 1.3 MB | 2-100 ms per pass for most patterns; the six dense-run patterns (P7) up to ~1 s per pass on an interpreter | ~2-10 min |
| pcrec compile, two forms × 95 | ~1-3 s each (pcrec + gcc on a ≤ 33 B pattern) | ~3-9 min, compiled testees only |

**Estimate: ~47 min per `pcre2-*` cell, ~52 min per pcrec cell; six pinned
testees ≈ 5 h**, inside one night's window (the 2026-09-03 window ran
11 cells in 6.3 h) and inside `CELL_CAP`'s 5,400 s default with ~1.8×
headroom. Cross-check against scripts/CLAUDE.md's measured table: the
model gives bounded@0.3's short regimes 42 × 2 × 6 × 2.45 s ≈ 21 min of
its measured 42-49 min (the rest is its ladder-rung throughput), and
loglines' 11 × 1 × 6 × 5.6 s ≈ 6 min of its measured 9. If the night is
short, the six cells split cleanly into two passes of three; the set has
no cell that needs a raised cap.

**What was cut to get there.** The first subject list was 47 (34 fields,
13 lines); nine fields whose only purpose was a whole-string hit already
present under search were dropped, and the control-byte line folded into
`f-bell`. A fourth run (CRLF-ended text, for `\R` and `\v` at density) was
not built: the two CRLF short subjects carry that edge and a density
question is a depth probe's.

## Origin

Authored 2026-09-05 for [B36] by a lane blinded per D27 (see "Blinded
authorship"). Nothing is copied: the vocabulary, the grammar, the
subjects and the patterns are this directory's. The seed is pcrec's,
verbatim, with its source header. Frank's charter is inbox I-42; the seed
landed per I-49.
