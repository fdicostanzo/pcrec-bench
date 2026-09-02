# bench/altwide — the width ladder, the structure arms, and what the numbers mean

Requirements §4.5 and §5: the per-engine notes, the declared variants, and the
statement of what this sub-bench exists to exercise. Read with
`pattern_facts.tsv` (the structure facts, PCRE2's analysis and the m/n per
regime, all DERIVED) and `oracle_limits.tsv` (where the oracle itself stops on
each skeleton).

## The objective, and what would defeat it

> Alternations of MANY literal branches, on both axes: what an engine pays to
> COMPILE one as the branch count grows — through to the width at which it
> refuses — and what it pays to SEARCH mostly-failing prose with one, as the
> STRUCTURE that decides a start-of-match optimization changes underneath it.
> Crossed with the two things only a leftmost-first engine pays for: which
> branch INDEX carries the hit, and what ORDER the branches are written in.

**Where it comes from.** Plan row [B11.2] and requirements §5's "hand-designed
hazard-class families … wide alternations". Three claims are in the row, and
each one is a column of the design.

1. **The start optimization is the axis.** A backtracker with no usable
   first-byte test must enter every branch at every candidate start; one with a
   single first code unit does a `memchr`; one with a required code unit can
   dismiss a whole subject without scanning it (`bench/loglines`' own axis, at
   width). Those are three different machines and this set spells all three:
   `sh1-*` (one first byte), `nar4-*` (four), `w-*` / `s-*` (twenty-six, on
   prose that is three-quarters lowercase, so the bitmap dismisses almost
   nothing), `pfx3-512` (three fixed bytes deep) and `sfx-*` (a shared suffix,
   the only patterns here PCRE2 gives a required code unit).
2. **A 4096-way alternation is a compile-SIZE question.** For anything that
   lowers one branch to one node, emitted size grows with total branch bytes,
   and pcrec bounds that with two hard caps. The width ladder is where a size
   curve becomes visible and where a refusal becomes a first-class outcome.
3. **Order and index are real costs for one family of engines and free for
   another.** `srt-512` and `w-512` are the SAME 512 branches — same bytes to
   within the reordering, same trie, same answers on every subject — differing
   only in the longest run of adjacent branches sharing a first byte (2 against
   28); since 0.2 the same pair exists at 256, where both halves COMPILE on
   every testee in the bench (2 against 15). A subject carrying `main` word 7
   is the LAST branch of `w-8` and the eighth of `w-2048`. Neither difference
   can cost an automaton anything.

**What would defeat the objective.** On the search axis: a subject that fails
at byte 0, or a background that matches by accident. Every line here is prose
whose background is branch-free BY CONSTRUCTION and asserted per subject
(`altwidetext.py`'s guard; without it, several accidental hits per line is the
expected number at width 4096), and every hit is one the generator placed at a
designed position with a designed branch index. On the compile axis: an engine
that caches an artifact across trials, or that reports a compile it did not
perform. An engine that absorbs width at constant cost is not defeating
anything — that IS the answer, and the ladder is built so it shows as a flat
line against one that grows.

## The patterns

`pattern_facts.tsv` is the authority; the table below is that file at the time
of writing, with the purpose beside it. `max_first_run` is the longest run of
ADJACENT branches sharing a first byte — the quantity a prefix-factoring pass
works on, and the only thing `srt-512` changes about `w-512`. `trie_nodes` is
the count of distinct prefixes over the branch set: the forward trie's node
count, a text-derived size proxy and *not* a claim about any engine's state
count. m/n is match · search_short · throughput.

### The width ladder (the compile axis, and the flat-versus-growing test)

Nested slices of one word pool, so a rung-to-rung difference is a width
difference and nothing else. Fourteen rungs since 0.2, which densified
64..512 to a uniform factor of about 1.4 — the band an AOT compiler is known
to compile, where 0.1 had three points.

| pattern | branches | branch B | bytes | trie | first CU | m/n |
|---|---|---|---|---|---|---|
| `w-8` | 8 | 4-12 | 56 | 43 | bitmap | 2/40 · 9/40 · 3/4 |
| `w-64` | 64 | 3-12 | 526 | 413 | bitmap | 2/40 · 9/40 · 3/4 |
| `w-96` | 96 | 3-12 | 804 | 624 | bitmap | 2/40 · 9/40 · 3/4 |
| `w-128` | 128 | 3-12 | 1056 | 809 | bitmap | 2/40 · 9/40 · 3/4 |
| `w-192` | 192 | 3-12 | 1573 | 1189 | bitmap | 2/40 · 9/40 · 3/4 |
| `w-256` | 256 | 3-12 | 2101 | 1575 | bitmap | 3/40 · 11/40 · 3/4 |
| `w-384` | 384 | 3-12 | 3177 | 2346 | bitmap | 3/40 · 11/40 · 3/4 |
| `w-512` | 512 | 3-12 | 4264 | 3118 | bitmap | 4/40 · 13/40 · 3/4 |
| `w-1024` | 1024 | 3-12 | 8705 | 6169 | bitmap | 4/40 · 14/40 · 3/4 |
| `w-2048` | 2048 | 3-12 | 17495 | 11918 | bitmap | 5/40 · 16/40 · 3/4 |
| `s-256` | 256 | 3-6 | 1495 | 957 | bitmap | 2/40 · 3/40 · 3/4 |
| `s-512` | 512 | 3-6 | 3023 | 1874 | bitmap | 2/40 · 3/40 · 3/4 |
| `s-2048` | 2048 | 3-6 | 12140 | 6566 | bitmap | 2/40 · 3/40 · 3/4 |
| `s-4096` | 4096 | 3-6 | 24343 | 12363 | bitmap | 3/40 · 5/40 · 3/4 |

The `s-*` rungs are the `w-*` rungs' controlled pairs: same width, same
first-byte spread, branch LENGTH is the only thing that moved. Since 0.2 the
pair exists three times — at 256 (1,495 B of pattern against 2,101; 957 trie
nodes against 1,575), at 512 (3,023 against 4,264; 1,874 against 3,118) and
at 2048 (12,140 against 17,495; 6,566 against 11,918) — and the first of the
three is the only one at a width no engine in this bench is known to refuse.
`s-4096` is the brief's 4096-way alternation and the widest pattern in the
set. The short pool exists because libpcre2 refuses `w-4096` outright — see
"The oracle's own ceiling" below.

### The structure arms (the search axis)

At 64, at the 256 ANCHOR and at 512, so structure is crossed with width
rather than measured at one point. 0.2 added the middle column: 256 is the
widest rung every engine in this bench is known to COMPILE, so it is the
width at which a structure arm can be read against a compiled `w-256` rather
than against a refusal diagnostic.

| pattern | what it spells | distinct first | max_first_run | first CU | required CU |
|---|---|---|---|---|---|
| `sh1-64`, `sh1-256`, `sh1-512` | every branch starts `k` | 1 | 64, 256, 512 | `k` | NONE |
| `pfx3-256`, `pfx3-512` | every branch starts `qux` | 1 | 256, 512 | `q` | NONE |
| `nar4-64`, `nar4-256`, `nar4-512` | four first bytes | 4 | 4, 4, 7 | bitmap | NONE |
| `sfx-64`, `sfx-256`, `sfx-512` | every branch ends `ing` | 25, 26, 26 | 2, 2, 3 | bitmap | **`g`** |
| `w-256`, `w-512` (the anchors) | first bytes spread over 26 | 26 | 2 | bitmap | NONE |

`sfx-*` are the only patterns in the whole set with a PCRE2 required code
unit, which is what makes them the required-byte arm rather than "another
structure". `pfx3-*`'s `min_length` is 6 where every other member's is 3 or
4 — a second, independent dismissal PCRE2 gets on that arm alone.

### Order and the wrappers

| pattern | what it is | how it differs from its pair |
|---|---|---|
| `srt-256` | `w-256`'s own 256 branches, sorted by first byte | `max_first_run` 15 against 2. Identical bytes (2101), identical trie (1575), identical answers on all 44 subjects. **The order pair that COMPILES** — 0.2's reason for existing (see "What 0.2 added") |
| `srt-512` | `w-512`'s own 512 branches, sorted by first byte | `max_first_run` 28 against 2. Identical bytes (4264), identical trie (3118), identical answers on all 44 subjects |
| `ci-256` | `w-256` under `(?i)` | +4 bytes; picks up the two upper-cased subjects (search 13/40 against 11/40) |
| `ci-512` | `w-512` under `(?i)` | +4 bytes; picks up the two upper-cased subjects (search 15/40 against 13/40) |
| `cnt-64` | `w-64` under `{1,3}` | the bridge to `bench/bounded`: the counter rung and the alternation width multiply. Match 3/40 against 2/40 — `f-cnt2`, two adjacent branches taken whole |
| `wb-256` | `w-256` inside `\b…\b` | search 7/40 against 11/40 |
| `wb-512` | `w-512` inside `\b…\b` | search 9/40 against 13/40: the four subjects whose branch sits inside a longer LETTER RUN — the two glued and the two doubled — are hits for `w-512` and misses here |

Every one of these is `w-256` or `w-512` or `w-64` plus exactly one
construct, so each is a one-variable comparison against a member already in
the set. Since 0.2 the order, caseless and word-boundary arms each exist at
BOTH 256 and 512, which is what lets a reading at the anchor width be
checked against the same lever one octave up.

## What the ladder brackets: the predictions

Every prediction below was written from pcrec's `docs/spec/` alone, before any
testee ran, and is stated so a window can CONFIRM or REFUTE it rather than
narrate around it. The blinding is stated in "Origin".

**P1 — this set is the [OPT-ALTCLS] pass's own measured surface, and
`srt-512` is its lever.** `tuning.md` §2.6/§2.7: stage 1 merges a maximal run
of SINGLE-CHARACTER branches into one class; stage 2 prefix-factors a maximal
run sharing a literal FIRST BYTE, on stage 1's output; both stamp
`<PREFIX>_ALTCLS_MERGES` / `_ALTCLS_FACTORED`, and both run before either
engine is built, so a pure-DFA artifact carries them too.

- Every branch here is at least 3 bytes, so stage 1 has nothing to merge
  anywhere in the set. **Predict `RX_ALTCLS_MERGES = 0` on all twenty
  patterns** — which is what makes any `_ALTCLS_FACTORED` movement
  unambiguously stage 2's.
- Stage 2 works on a maximal run of ADJACENT branches, which is
  `pattern_facts.tsv`'s `max_first_run` column. **Predict `_ALTCLS_FACTORED`
  large on `sh1-64` / `sh1-512` / `pfx3-512` (one run as wide as the whole
  alternation), moderate on `srt-512` (about 26 runs averaging 20) and
  `nar4-512` (runs to 7), and near zero on `w-*` and `s-*` (runs of 2-3).**
- The falsifiable form: `srt-512` and `w-512` differ in nothing else. If their
  two artifacts come out identical, the pass does not see branch order — a
  finding, and one no other set in this bench can produce.

**P2 — the DFA is predicted to absorb width at constant match cost; nothing
else is.** A capture-free alternation of literals carries none of the
constructs `tuning.md` §2.11 lists as do-or-die for the DFA, so **predict
`RX_ENGINE "dfa"` on every member under `pcrec-auto` and `pcrec-nocaps`, at
every width**. A DFA's per-byte cost does not depend on branch count.
**Predict the search-band and throughput per-byte numbers FLAT across the
eight ladder rungs for those two testees, and rising roughly linearly in
width for `pcre2-interp`, `pcre2-jit` and `pcrec-vm`.** That is the set's
headline comparison, and it is why the ladder is geometric: a flat line
against a line of slope 1.

**P3 — the pre-multiplied table bound is predicted to be crossed INSIDE the
ladder, and this would be the first artifact in this bench to reach it
naturally.** `tuning.md` §2.13: the pre-multiplied transition-table form is
refused at generation time, per machine, when `states * classes` exceeds
**65,535** — a correctness condition (a cell must fit `unsigned short` and stay
distinguishable from the dead sentinel), decided separately for the forward and
reverse machines, which is why `"mixed"` exists. The spec records that every
pattern in pcrec's own 2,487-pattern corpus is inside the bound (largest 40,010
entries), and this bench has only ever reached `RX_DFA_TABLE "indexed"` by
passing `-fno-premul-table` as a control ([B16]).

- `trie_nodes` is a lower bound on the forward machine's state count: 413 at
  `w-64`, 1,575 at `w-256`, 3,118 at `w-512`, 6,169 at `w-1024`, 11,918 at
  `w-2048`. For any byte-class count at or above 6, `states * classes` crosses
  65,535 between `w-256` and `w-1024`; near 27 classes it crosses between
  `w-64` and `w-256`.
- **Predict `RX_DFA_TABLE "premultiplied"` at `w-8` and `w-64`, `"indexed"` or
  `"mixed"` at `w-1024` and `w-2048`, with the transition at `w-256` or
  `w-512`.** The rungs are dense there for exactly this reason. If it never
  moves, the machine's class count is far smaller than the branch alphabet
  suggests; if it moves at `w-64`, the forward machine is several times the
  trie. Either is worth the rung.
- `ci-512` is a second, independent lever on the same prediction at ONE width:
  `cli.md` says pcrec folds case at PARSE time into the automaton, so **predict
  roughly twice the classes at unchanged state count**, and therefore
  `RX_DFA_TABLE` at `ci-512` no later than at `w-512`.

**P4 — the candidate-start route is predicted to split on STRUCTURE, not on
width.** `tuning.md` §2.14: a DFA artifact's forward scan filters candidate
starts on the byte AT the candidate — one `memchr` for a single value, a
256-entry bitmap walk for a set — and with offset-skip live may instead derive
a SET of `(offset k, byte-set)` tests, scan for the rarest with one `memchr`
and verify the rest.

- **Predict a single-byte `memchr` route on `sh1-64` / `sh1-512`, and on
  `pfx3-512` an OFFSET SET of three positions** (`RX_DFA_PREFILTER
  "offset-set"` with `RX_DFA_PREFILTER_OFFSETS` = 3): three fixed bytes at
  three fixed offsets is the shape §2.14's own worked example describes.
- **Predict a bitmap with four bits set on `nar4-*`**, and on `w-*` / `s-*` /
  `srt-512` a bitmap covering all 26 lowercase letters — which on prose that is
  about three-quarters lowercase dismisses almost nothing. **Predict the
  prefilter buys the least on the ladder and that the failing scan dominates
  there**, which is why the ladder and the structure arms have to be read
  against each other rather than separately.
- `sfx-*` is the open one. PCRE2 has a required code unit (`g`); whether pcrec
  derives an equivalent trailing-byte test has no stamp this bench can read, so
  the evidence is the TIMING against `w-512` at the same width and the same
  subjects. That is why `sfx-512` sits at the anchor width.

**P5 — an emitted-size cap is predicted to fire at the top of the ladder, and
only on the VM route.** `limits.md` §8: `PCREC_MAX_VM_EMIT_CODE_BYTES` is
500,000 (bytes outside table initializers) and `PCREC_MAX_EMIT_BYTES` is
1,000,000; both are checked after emission and before anything is written, so
crossing one is a clean refusal with no file, never a truncation. The CODE cap
is stamped only on a VM artifact — a pure-DFA artifact has no counter rung and
so no code/table split to bound.

- A branch-per-node lowering emits work proportional to total branch bytes:
  24,343 for `s-4096`, 17,495 for `w-2048`, 12,140 for `s-2048`. **Predict for
  `pcrec-vm` that the widest one or two rungs are a first-class
  `did-not-compile` naming an emitted-size cap, and that the `--warn-emit-bytes`
  advisory fires several rungs earlier.** **Predict no refusal at any rung for
  `pcrec-auto`**, because the DFA route these patterns select has neither cap
  in play.
- The gcc term is the other half and is the cell-time estimate's dominant
  unknown: `limits.md` §8 measures a VM node at 5.37 ms of gcc against 0.905 µs
  for a data-table entry, a factor of about 5,900. If `w-2048` lowers to a few
  thousand VM nodes, one emit is tens of seconds of gcc and a compile trial is
  two forms times five trials.

**P6 — the DFA state ceiling is OUT OF REACH of this set, and the oracle is
why.** `limits.md` §3.3: `PCREC_MAX_DFA_STATES_TABLE` is 32,000 and
`PCREC_MAX_TABLE_ENTRIES` 2,000,000, and under `auto` crossing one is a
SELECTION outcome ([SEL-1]) — fall back to the VM with `RX_ENGINE_WHY` naming
the cap, or drop an auto-selected prefilter — rather than a refusal. The widest
trie this set can carry is 12,363 nodes, because libpcre2 refuses anything
wider. **Predict NO [SEL-1] state-cap fallback anywhere in this set**; if one
appears, the forward machine is more than 2.5× the trie, which is itself the
finding. Reaching 32,000 states with oracle-verifiable expectations needs a
differently-shaped set — a note for the manager, not a change here.

**P7 — `cnt-64` is the bridge, and the oracle has already measured half of
it.** `oracle_limits.tsv` shows the `cnt` skeleton refused at 2048 where the
plain one is refused at 4096: PCRE2 replicates the group per count, and the
count wrapper halves the width ceiling. For pcrec, `tuning.md` §2.10 and
`limits.md` §8a put the counter rung's unroll factor on a size ladder;
**predict `RX_UNROLL_K` and `_WHY` present on the VM route and an emitted size
about 3× `w-64`'s.**

**P8 — nothing here should move `RX_DFA_SCAN_EDGE` off `"none"`.**
`tuning.md` §2.18: a scan edge collapses a run of states differing only in how
many bytes of ONE fixed class have been counted. An alternation of distinct
literals has no such run. **Predict `RX_DFA_SCAN_EDGE "none"` on every member
except possibly `cnt-64`**, whose `{1,3}` is the only counted construct in the
set. This is the negative control for [OPT-5]'s pass on a set built for a
different mechanism entirely.

## What 0.2 added ([B31]): the dense ladder, the 256 arms, the length pair

**What changed, and what did not.** THIRTEEN patterns — four dense ladder
rungs (`w-96`, `w-128`, `w-192`, `w-384`), seven arms twinned at 256
(`sh1-256`, `pfx3-256`, `sfx-256`, `nar4-256`, `srt-256`, `ci-256`,
`wb-256`) and two short-pool rungs (`s-256`, `s-512`) — and TWO subjects
(`f-s255`, `l-s255-mid`). NOTHING ELSE. Every 0.1 pattern keeps its id and
its exact bytes: `gen_patterns.py` was re-run in full and `git` reports the
twenty 0.1 `.rx` files unmodified. Every 0.1 subject reproduces byte for
byte, because the two new carriers are drawn LAST (`gen_subjects.py`'s
`extras()`), so the 0.1 draws are an unchanged prefix of the same rng
stream — `manifest.tsv` is a two-row APPEND and `manifest_throughput.tsv`
is untouched. All 1,600 0.1 expectation rows appear byte-identical among
0.2's 2,772, checked TRIPLE BY TRIPLE rather than by line number: the two
new subjects interleave two rows into every pattern's `match` and
`search_short` block, so the file is an extension by ROW and not a prefix by
line. `oracle_limits.tsv` moves only in its `set_rungs` column — every
oracle refusal width and every diagnostic is unchanged.

**0.1 and 0.2 records NEVER POOL.** The pattern set and the subject set both
differ (33 patterns against 20, 44 subject slots against 42), so a set-grain
sum or median over `altwide@0.1` and one over `altwide@0.2` are sums over
different work, and the reporter's version filter keeps them apart. What
remains comparable across the bump, by construction: any (pattern, subject,
regime) cell whose pattern id and subject id appear in both — every 0.1
pattern and every 0.1 subject — read cell against cell, never sum against
sum.

**Why: the refusal that the full-suite reading measured.** 0.1's ladder was
built to locate a refusal, and it did — but higher and wider than P5
predicted. At pcrec pin 1989c62 every 0.1 pattern at width ≥ 512 is refused
in BOTH forms on ALL FOUR pcrec configs: the auto/DFA route at the
1,000,000 B emitted-SOURCE cap, the VM route at the 500,000 B emitted-CODE
cap. Twelve of the twenty patterns are therefore unmeasurable on pcrec, and
three consequences shaped 0.2.

1. **The ladder had three points under the line.** `w-8`, `w-64`, `w-256`
   are the only rungs pcrec compiles, and their set-grain medians (2.24 →
   3.43 → 2.93 ms) are the headline claim: the auto route is FLAT in width
   where every other testee rises 74-90×. Three points, one of them
   non-monotone, is not yet a line. 0.2 makes it seven (8, 64, 96, 128,
   192, 256, 384) at a uniform factor of about 1.4, so a knee anywhere in
   the band is bracketed within 1.5× and 384 brackets the refusal boundary
   from below.
2. **Every structure, order and wrapper arm sat at 512** — that is, at a
   refusal. `srt-512` against `w-512` is the set's sharpest lever (the same
   512 branches, reordered) and 0.1 could only ever read it off two refusal
   diagnostics: 1 byte apart on the DFA route, 93,508 B (13.8 %) apart on
   the VM route. 0.2 twins all seven at 256, where both halves of every pair
   COMPILE and the lever produces two artifacts and two match times instead.
3. **The branch-LENGTH pair existed only at 2048**, where both halves are
   refused. `s-256` puts it at a width nothing is at the ceiling of, and
   `s-512` makes it a probe of the cap itself (below).

**The 256 anchor.** Seven arms, each one existing member plus exactly one
construct, so each is a one-variable comparison: `sh1-256` / `pfx3-256` /
`nar4-256` / `sfx-256` are the four structure pools at `w-256`'s width;
`srt-256` is `w-256`'s own branches reordered; `ci-256` and `wb-256` are
`w-256` under `(?i)` and inside `\b…\b`. The 512 arms are KEPT — they are
the point under a raised cap, and the pair of widths is what lets a reading
at 256 be checked one octave up.

**`s-512`: byte or count?** It carries the identical branch COUNT as `w-512`
at 71 % of its branch bytes (3,023 B against 4,264). If the refusal at 512
tracks emitted SIZE — which is what `limits.md` §8 says both caps are — this
rung compiles where `w-512` refuses. If it tracks branch count, both refuse.
One rung, two outcomes, and they say different things about what the cap
actually bounds. The arithmetic is in P13, and it is knife-edge on the VM
route.

**The two carriers, and why only two.** Through 0.1 the `short` pool's only
hit inside width 2048 was the field `f-s0` — branch 1 — and it had no prose
LINE carrier at all, so every `s-*` pattern had exactly one hit in the whole
set, at one index, with no designed position. That is nothing to read a
length pair's cost-at-a-hit on. `f-s255` and `l-s255-mid` carry `short` word
255, the last branch of `s-256`, so the pair reads arm-for-arm against
`main` word 255 (`f-w255`, `l-w255-mid`), the last branch of `w-256`. They
lift `s-2048` and `s-4096` off their single hit too.

Nothing else 0.2 added needs a carrier, and this was checked rather than
assumed. The dense rungs are nested slices, so `main` words 0 and 7 are
branches 1 and 8 of every one of them. The 256-wide structure arms take the
same pool-word-0 field and pool-word-3 line their 64- and 512-wide twins do.
And the ORDER pair's index swap is ALREADY at its extreme in the 0.1
subjects: `main` word 0 is branch 1 of `w-256` and branch **240** of
`srt-256` (the largest index move any word of the 256-slice makes — it is
the seed's own accident that word 0 begins with `y`), while `main` word 255
moves the other way, branch 256 of `w-256` and branch 111 of `srt-256`. Two
subjects, in opposite directions, at the extremes; a third would be a
confirmation.

**What was considered and left out.**

- **`cnt-256`.** The one-variable rule permits it (`w-256` plus `{1,3}`),
  but the count wrapper's own arm is already measured UNDER the cap:
  `cnt-64` and `w-64` both compile, so the size multiplier and the unroll
  stamps are readable at 64 already. `cnt-256` would confirm at a second
  width and cost a rung whose throughput pass is the most expensive kind
  here (a counted alternation restarts the whole alternation per
  repetition). The brief offered `cnt-256` OR the short-pool pair; the pair
  answers a question nothing else in the set can (the length axis at a
  compiling width), and the count arm answers one `cnt-64` already answers.
- **A sort-last carrier for `srt-512`.** The order lever's extreme subject
  at 512 would mirror the 256 one, but 0.2's rule is to add a carrier only
  where a NEW pattern needs a branch index the existing subjects do not
  provide, and `srt-512` is not new. `main` word 0 is branch 481 of
  `srt-512` against branch 1 of `w-512`, which is the same lever at 512
  already.
- **A "last branch" carrier per dense rung** (`main` words 95, 127, 191,
  383). The dense ladder's job is the COMPILE axis and the flat-versus-
  growing line, both of which are read off the failing scan and the
  artifact, not off a hit's branch index; four more subjects would cost
  every one of the 33 patterns four more expectation cells to add a
  confirmation.
- **A new throughput subject.** `gen_throughput_subjects.py`'s sixteen
  planted words already give every 0.2 pattern the same 3/4 as every 0.1
  one, and adding a word would change all four large subjects' bytes —
  the one edit that would break the byte-identical extension outright.
- **A `pcrec_limits.tsv`.** RULED OUT by Frank on 2026-09-02: the sets are
  oracled on libpcre2 only, and pcrec's refusal widths live in the reports.
  `oracle_limits.tsv` remains the oracle's edge of the ladder and nothing
  else's.

**How blind this author was, and where the numbers above came from.** The
0.1 author read pcrec's `docs/spec/` and nothing else. This one worked under
the same rule for pcrec (`docs/spec/` only; no `src/`, no `tests/`, no
corpora, no `docs/dev`) and for this repo (no `testees/`, no `store/`, no
`reports/`, no `docs/dev/`, no adapter or reporter source), but was HANDED
five measured facts from the 2026-09-02 full-suite reading at pin 1989c62:
the refusal width and both cap names, the flat-line medians at 8/64/256, the
`srt-512`-versus-`w-512` refusal differential, the fact that both caps are
raise-only per compile, and Frank's ruling on `pcrec_limits.tsv`. Every
number in this section attributed to a measurement is one of those five;
everything else — the 13 patterns, the 2 subjects, and P9-P18 below — is
derived from the set's own committed tables and from `docs/spec/`. So 0.2 is
NOT a blind design in 0.1's sense, and should not be read as one: it is a
blind design steered by five numbers, each of which is named where it is
used.

## The 0.2 predictions (P9-P18)

P1-P8 above are 0.1's, left exactly as written — a record of what was
predicted before anything ran, including the two the full-suite reading
settled (P5 REFUTED: the DFA route refuses more and lower than the VM, not
the other way round; P8 REFUTED: `edge=range` on every compiled DFA but the
floor) and the two it left untestable (P3, P4, whose subjects were all at
512 and above). P9-P18 are 0.2's, written before any 0.2 cell ran, and each
is stated so a window can CONFIRM or REFUTE it.

**P9 — the flat auto line stays flat across the dense band.** The three
measured points are 2.24 / 3.43 / 2.93 ms at `w-8` / `w-64` / `w-256`, a
band with no trend and a 1.5× spread. **Predict `w-96`, `w-128`, `w-192`
and `w-384` all land inside 2.0-4.0 ms on `pcrec-auto` at the set grain,
with no monotone rise across the seven rungs**, and predict the same seven
rungs on `pcre2-jit` and `pcre2-interp` rise monotonically with a slope
near 1 in width. The falsifier is sharp: any monotone climb across
96 → 128 → 192 → 256 → 384 that leaves the 0.1 band is a width cost in the
DFA route, and 384 is where it would first be visible.

**P10 — the table-encoding bound is bracketed by the dense rungs, if it is
crossed at all.** 0.1's P3 predicted `RX_DFA_TABLE` moving off
`"premultiplied"` when `states × classes` crosses 65,535, and put the
transition at `w-256` or `w-512`. With 26 classes that is 2,520 states;
`trie_nodes` runs 1,575 (`w-256`) → 2,346 (`w-384`) → 3,118 (`w-512`).
**Predict the transition at `w-384` or `w-512` if the forward machine is
about the size of the trie** — which makes `w-384` the rung that decides it,
and makes the answer readable WITHOUT a raised cap for the first time.
`ci-256` is the independent lever: `cli.md` folds case at parse time, so
**predict `ci-256` reaches `"indexed"` or `"mixed"` no later than `w-384`
does**, at an unchanged state count (its trie is `w-256`'s, 1,575).

**P11 — the VM route does not CROSS the JIT inside the ladder.** Both are
per-candidate-per-branch machines, so their ratio should be a constant in
width, not a function of it. **Predict `pcrec-vm` / `pcre2-jit` on the
search band is within a factor of 1.5 of itself across the seven `w-*` rungs
8..384** — flat, whatever its level. A ratio that moves monotonically with
width means one of the two has a width term the other does not, which is the
finding; a crossing inside the ladder would locate it.

**P12 — `srt-256` against `w-256`: the ALTCLS lever, as artifacts.** The
two patterns are byte-for-byte the same 256 branches reordered (2,101 B
each, 1,575 trie nodes each, identical answers on all 44 subjects);
`max_first_run` is 15 against 2. At 512 the two refusals were 1 B apart on
the DFA route and 93,508 B (13.8 %) apart on the VM route. **Predict at 256:
the two DFA artifacts within a handful of bytes of each other (the order is
invisible to a subset construction), and the two VM artifacts 10-15 % apart
with the SAME SIGN as at 512.** **Predict `RX_ALTCLS_FACTORED` differs
between the pair on both routes** — a stage-2 prefix-factoring pass works on
runs of adjacent branches, which is the one thing that moved. If the two
artifacts come out identical on both routes, the pass does not see branch
order, and 0.2 is the first place in this bench that can say so from two
compiled artifacts rather than two diagnostics.

**P13 — `s-512`: the cap is a SIZE cap, and this rung is knife-edge on the
VM route.** The `srt-512` differential fixes `w-512`'s VM emitted code
between about 584 KB and 771 KB (93,508 B being 13.8 % of one of the pair),
and `s-512` carries 70.9 % of `w-512`'s branch bytes at the identical branch
count. If emitted code is proportional to branch bytes, `s-512` lands
between 414 KB and 547 KB against a 500,000 B cap. **Predict `s-512`'s VM
emitted code within ±10 % of the cap, so that which side it falls on is what
the rung measures** — and **predict that whatever it does, `s-512`'s
reported size is 0.71 × `w-512`'s to within 10 %**, which is the part that
is a clean confirm-or-refute regardless of the outcome. On the SOURCE route
the same ratio says **`s-512` compiles iff `w-512`'s emitted source is under
1.41 MB**. If instead `s-512` refuses with a size EQUAL to `w-512`'s, the
cap is being reached by branch count and not by bytes, and `limits.md` §8's
description of both caps is wrong about this shape.

**P14 — the branch-length pair at 256, both halves compiling.** `s-256` is
71.2 % of `w-256`'s pattern bytes and 60.8 % of its trie nodes. **Predict
the emitted size ratio tracks the TRIE ratio (0.61) rather than the byte
ratio (0.71) on the DFA route, and the byte ratio rather than the trie ratio
on the VM route** — the first lowers a branch set to a state machine, the
second lowers it to code per branch. That is one number per route and the
two predictions point in different directions, so the pair cannot both be
right by accident. On the match side, **predict `pcrec-auto` equal on
`w-256` and `s-256` to within the flat band, and `pcre2-jit` / `pcrec-vm`
measurably cheaper on `s-256`** (fewer branch bytes entered per candidate
start at the identical branch count).

**P15 — 0.1's P4 restated at a width where it can be read.** All of it was
predicted at 512 and none of it could be measured. **Predict at 256:
`RX_DFA_PREFILTER` a single-byte `memchr` route on `sh1-256`; an
`"offset-set"` with `RX_DFA_PREFILTER_OFFSETS` = 3 on `pfx3-256`; a bitmap
with four bits set on `nar4-256`; and a bitmap over all 26 lowercase letters
on `w-256`, `s-256` and `srt-256`.** **Predict the prefilter buys the LEAST
on the spread arms** — prose that is about three-quarters lowercase — so
that `sh1-256` and `pfx3-256` are several times faster than `w-256` on the
search band for every testee, while `pcrec-auto`'s throughput numbers stay
within the flat band across all of them. `sfx-256` is the open one, as
`sfx-512` was: PCRE2 has a required code unit (`g`, `min_length` 6) and
whether pcrec derives a trailing-byte equivalent has no stamp this bench
reads, so the evidence is `sfx-256`'s timing against `w-256` at the same
width, the same 44 subjects and — for the first time — two compiled
artifacts.

**P16 — under the RAISE, the flat line extends but the ARTIFACT grows.**
Both caps are raise-only per compile (`--max-emit-bytes`,
`--max-emit-code-bytes`), so a raised-cap config turns all thirteen wide
rungs from refusals into artifacts. **Predict `pcrec-auto-bigcap`'s match
and throughput numbers at 512, 1024 and 2048 stay inside the same flat band
P9 predicts for 8..384** — a DFA's per-byte cost does not depend on how many
branches built it, and if it does the flat line was never about the DFA.
**Predict emitted SOURCE grows roughly linearly and the two candidate
models separate at `s-4096`:** `w-512`'s source is above 1,000,000 B (it
refused), so it is at least 235 B per branch byte or at least 320 B per trie
node; carried up, a per-trie-node model puts `w-2048` near 3.8 MB and
`s-4096` near 4.0 MB, while a per-branch-byte model puts them near 4.1 MB
and 5.7 MB. `s-4096` is where they differ by 40 %, because the short pool's
trie is dense relative to its bytes. **The reading that decides it is one
raised-cap `pcrec-auto` cell's `emit_bytes` column on `w-2048` and
`s-4096`.**

**P17 — nothing about the 0.1 stamps changes, and the two refuted ones stay
refuted.** Every 0.2 branch is at least 3 bytes, so **predict
`RX_ALTCLS_MERGES` = 0 on all thirty-three patterns** (0.1's P1, restated
over the wider set: it is what makes any `_ALTCLS_FACTORED` movement
unambiguously stage 2's). And since the full-suite reading refuted P8,
**predict `RX_DFA_SCAN_EDGE "range"` on every compiled DFA member of 0.2 and
`"none"` on the floor** — the corrected form, stated so it can be refuted in
turn. **Predict no [SEL-1] state-cap fallback at any 0.2 rung** (0.1's P6:
the widest new trie is 2,346 nodes, an order below the 32,000 ceiling).

**P18 — the compile axis is where 0.2 costs, and the raised-cap VM cell is
the one that may not fit.** The auto refusals were measured at 8.7-36.0 s
EACH, because the source cap is checked on the emitted bytes after emission;
the VM refusals at 0.01-0.07 s, because the code cap is reached earlier.
**Predict this asymmetry is unchanged at 0.2 and that `s-512` is the one
rung whose auto refusal (if it refuses) costs least** — its emitted source
is the smallest of the thirteen. **Predict the raised-cap VM cell's compile
time is dominated by gcc on the wide rungs and exceeds the auto one by an
order of magnitude**, for the reason `limits.md` §8 gives: 5.37 ms of gcc
per VM node against 0.905 µs per data-table entry, a factor of about 5,900.
The estimate below turns that into minutes, and says what to measure first
rather than committing a cell on it.

## The oracle's own ceiling, and what it forced

`oracle_limits.tsv` is the committed probe: each skeleton compiled at doubling
widths until libpcre2 refuses.

| skeleton | branch bytes | last accepted | first refused | diagnostic |
|---|---|---|---|---|
| `w`, `sh1`, `pfx3`, `sfx`, `nar4`, `srt`, `ci`, `wb` | 3-12 (6-12 for two) | 2048 | 4096 | regular expression is too large |
| `s` | 3-6 | 4096 | 8192 | regular expression is too large |
| `cnt` (`{1,3}`) | 3-12 | 1024 | 2048 | regular expression is too large |

Three things follow, and all three shaped the set.

1. **The `main` ladder stops at 2048.** An expectation the oracle cannot state
   is a cell the harness cannot judge (the rule `bench/bounded` set at PCRE2's
   65535 count ceiling). The brief's 4096-way rung is therefore carried by
   3-6 byte branches, with `s-2048` beside `w-2048` as the control that says
   what the length change cost.
2. **The ceiling is a compiled-SIZE one, not a count one.** `bench/bounded`
   hit "number too big in `{}` quantifier"; a wide alternation has no counts
   and reaches "regular expression is too large" alone — in a default 8-bit
   build, the LINK_SIZE 2 bound on the compiled pattern, roughly two code units
   per literal byte plus three per branch. That is why branch LENGTH moves the
   ceiling as much as branch COUNT does, and the `s` row measures the trade:
   halving the average branch doubles the reachable width.
3. **`ci` refuses at exactly the same width as `w`.** PCRE2's caseless folding
   costs no compiled size (the same opcode carries the flag), which is a fact
   about the ORACLE that P3's pcrec prediction is deliberately the opposite of.

## The subjects

Two short families and one large one; `gen_subjects.py` and
`gen_throughput_subjects.py` carry the per-family reasoning.

**FIELDS (18, 4-18 B, the `match` regime).** One whole-string hit from every
rung and every structure pool, so no pattern's match row is empty: `main` words
0, 7, 255, 511 and 2047 (each the last branch of a different rung), `short`
words 0, 255 and 4095 (the middle one added at 0.2 — the last branch of the
new `s-256` rung, and the short ladder's only anchored hit above branch 1),
and one branch from each of `sh1`, `pfx3`, `sfx`, `nar4`.
Plus four designed MISSES that fail for four different reasons — a branch with
its last byte changed, a proper PREFIX of a branch (which no shorter branch
rescues, because the pools are substring-free), a branch buried in a longer
letter run, and a word in no pool at all — and two derived hits: the
upper-cased form (`ci-512` alone) and two adjacent branches (`cnt-64` alone
takes both).

**LINES (22, ≤ 256 B, the `search_short` regime).** Machine prose whose
background is branch-free by construction and re-asserted per subject.
Thirteen carry exactly one branch at a designed POSITION — early (token 2),
mid, or last — and a designed branch INDEX (the thirteenth is 0.2's
`l-s255-mid`, the short pool's only prose carrier inside 2048); three carry a
derived token (upper-cased, glued, doubled); six are pure background. The position and the identity are
separate arms on purpose: a backtracker's cost at a hit is (bytes scanned while
failing) × (branches entered per byte) + (the hit branch's index), and only
moving one term at a time separates them. An automaton pays neither.

**THE LARGE SUBJECTS (4, the `throughput` regime).** Prose crossing hit DENSITY
(0, 1 per 8 KB, 1 per 128 B) at 128 KB with SIZE (128 KB, 512 KB) at one
density. Under find-all search a subject's cost splits into a failing scan and
a cost per match, and those two scale differently with width; `t-128k-clean`
isolates the first, `t-128k-dense` weights the second, and the two `sparse`
subjects at 4× the bytes test whether the per-byte cost is flat in subject
length. The sixteen planted words are chosen so every pattern has some, and so
a subject's occurrence count is a function of the PATTERN's width — which is
the number `expectations.tsv`'s `nmatches` column then carries per rung.

**Why 128 KB and 512 KB rather than 1 MB.** A backtracker enters every branch
at every candidate start; at width 2048 one pass over 1 MB is tens of seconds,
and the harness caps a trial's predicted sweep at 20 s, so the cap would bind
on the widest rungs of every backtracking testee at five trials each. At
128 KB nothing hits the cap, and the regime still sits two orders of magnitude
above the search band and above `bench/bounded`'s own largest subject.

## Regimes

All three are declared. `match` is the fields and the lines, anchored and
end-anchored: the lines are all whole-subject misses (a 256 B prose line is not
one branch), which costs almost nothing and gives every pattern a large,
uniform miss population against which its 1-5 field hits read. `search_short`
is the same 40 subjects unanchored — the set's main axis, mostly failing by
design. `throughput` is the four large prose subjects under find-all.

## The floor pattern

`#`, one literal byte, `role = "floor"` (requirements §5, the rule since
[B15]). It occurs in this set ONLY as the first byte of a line subject, which
gives one pattern three different readings of the harness's own per-call
overhead:

- on the 22 LINES, a hit at offset 0 — the closest thing to pure per-call
  overhead the set can measure (search 22/40);
- on the 18 FIELDS, a whole-subject miss on 4-18 bytes;
- on the four THROUGHPUT subjects, a full-length `memchr` MISS over 128 KB and
  512 KB (0/4) — the per-byte floor every wide rung's throughput number is
  read against.

## Give-ups and refusals are results

A pattern a testee refuses is a `did-not-compile` row with that engine's own
diagnostic (requirements §4.4), not an error and not a missing cell. This set
expects them: P5 predicts the widest rungs refuse on `pcrec-vm`, and the width
at which that first happens is the compile axis's own number, the way the count
was in `bench/bounded`. The oracle's refusals are different in kind — they
bound what the SET can contain, and they are the committed
`oracle_limits.tsv`, not a testee result.

## Per-engine notes

**No variants.** All thirty-three patterns are canonical PCRE2 spellings and
every adapter runs the canonical text (requirements §4.5; the record still states
that, as `patterns[].variant = null`). Neither adapter passes a compile option.

**pcre2-interp / pcre2-jit.** The whole-subject regime is
`PCRE2_ANCHORED|PCRE2_ENDANCHORED` on the plain compile (harness contract §2).
`pattern_facts.tsv`'s `first_code_unit` / `required_code_unit` / `min_length`
columns are PCRE2's own analysis, read live off the oracle, and are the honest
statement of what its start optimization has to work with on each arm. They are
NOT evidence about any other engine: a testee that disagrees with those columns
is a finding, not an error.

**pcrec (all configs).** Two patterns use `\b` (`assertions`, built but not in
the frozen `std1` set), for which `--features all` is already on every pcrec
testee config — a flag of the TESTEE, not a variant of the pattern, and the
text is byte-identical either way. `(?i)` is the `modifiers` module, which IS
in `std1`, so `ci-512` needs nothing. Every pcrec testee also compiles a second
artifact from `(?:<pattern>)\z` for the whole-subject regime, which doubles the
compile-axis cost on a set whose widest patterns are 17 KB and 24 KB — see the
estimate below.

## Cell-time estimate, and what was cut to get there

One cell = one testee × 33 patterns × three regimes at `--trials 5`. The
harness calibrates each (pattern, regime) loop so the MEDIAN subject's loop
is 50 ms, and caps a trial's predicted sweep at 20 s by lowering `iters` --
never below 1, so a regime whose single pass already exceeds the budget runs
at one iteration and takes what it takes (`harness.py`, `calibrate`). The
throughput probe itself runs at `iters = 1`, so a trial-set is SIX passes:
one probe and five trials.

The numbers below are anchored on a design-time probe of the ORACLE
(libpcre2 10.46, the interpreter, no JIT) over 0.1's own subjects, one pass
per pattern per regime -- archived with its own caveats under
`docs/dev/measurements/` (`2026-09-01-altwide-oracle-pass-cost.txt`). That
probe is a SIZING INPUT, not a measurement: it ran on a box carrying another
session's battery (load average 6.7-8.0 on 12 cores), unrepeated and
ungated. Read it as an upper bound on an interpreter's per-pass cost. 0.2's
rows are the same probe CARRIED FORWARD by a stated model rather than
re-probed: within a pool family a backtracker's per-pass cost is taken
linear in branch count, which fits 0.1's own numbers (its four widest rungs,
9,216 branches, are 104 s of the 138 s total -- 11.3 ms per branch -- and
`s-4096` alone at 4,096 branches is 44 s, 10.7 ms per branch).

| regime | one pass, all 33 patterns | per trial-set (×6) |
|---|---|---|
| `match` (40 subjects) | ~0.009 s | calibrated up to ~50 ms × 33 × Σ/median |
| `search_short` (40 subjects) | ~0.8 s | same |
| `throughput` (4 subjects, 896 KB) | **~168 s** | **~17 min** |

The throughput row is 0.1's measured 138 s plus 29.6 s: 2,336 new branches
in the spread family at 11.3 ms (`w-96`, `w-128`, `w-192`, `w-384`, `s-256`,
`s-512`, `srt-256`, `ci-256`, `wb-256`) and 1,024 new branches in the
structure family at the 3.1 ms/branch the 0.1 structure arms imply -- those
arms filter candidate starts on one byte or four, so they cost a third of a
spread rung of the same width.

- **The two short regimes cost about 5 minutes of a trial-set** on any
  testee: 33 patterns × 5 trials × ~1.7 s ≈ 280 s, plus the two probes.
  Their passes are milliseconds, so `iters` calibrates UP to the 50 ms
  target and each pattern's trial sweep is 50 ms × Σ/median.
- **The throughput regime IS the cell on a backtracking testee**, ~17 min,
  of which `s-4096` alone is still 44 s per pass and the four widest rungs
  are 104 s. Every one of those is already at `iters = 1`.

**The six pinned testees.**

| testee | 0.1 estimate | 0.2 estimate | what moved |
|---|---|---|---|
| `pcre2-interp` | ~18 min | **~22 min** | 13 more patterns, all ≤ 512 wide |
| `pcre2-jit` | ~5-6 min | **~7 min** | same |
| `pcrec-auto`, `pcrec-nocaps` | ~5 min + compile | **~8 min + ~30-40 min compile** | see below: the compile term is now the cell |
| `pcrec-vm`, `pcrec-vm-in` | ~18-45 min + compile | **~25-80 min** | the open number, unchanged in kind |

**The compile term on a plain pcrec config is now the dominant one, and 0.1's
estimate did not know it.** Thirteen 0.2 patterns are at width ≥ 512, and on
the auto/DFA route each refusal was MEASURED at 8.7-36.0 s -- the source cap
is checked on the emitted bytes AFTER emission, so a refusal costs a full
emit. At 2 forms × 5 trials that is 130 emits per cell. Modelling the
measured range against width (8.7 s at the nine 512-wide rungs, ~14 s at
`w-1024`, ~23 s at `w-2048` and `s-2048`, 36 s at `s-4096`) gives 174 s per
emit-set and **≈ 29 minutes of refusal per `pcrec-auto` or `pcrec-nocaps`
cell**, before the twenty compiling patterns' own emit and gcc (predicted
small on the DFA route: `limits.md` §8's 0.905 µs per table entry makes even
a 2,000,000-entry table 1.8 s). If P13 is confirmed and `s-512` compiles,
twelve rungs refuse rather than thirteen and the term drops by about 2
minutes. On the VM route the same thirteen refusals cost 0.01-0.07 s in
total, and the compile term is instead the twenty COMPILING patterns: 3,433
branches or 29,056 branch bytes, at 5.37 ms of gcc per VM node, is 18 s per
emit-set if a branch lowers to a node and 156 s if a branch BYTE does --
**3 to 26 minutes over the ten emits**, which is the widest genuine
uncertainty in this table.

**The two raised-cap configs** (`pcrec-auto-bigcap`, `pcrec-vm-bigcap`,
built by raising `--max-emit-bytes` / `--max-emit-code-bytes` per compile).
The raise does not make emission cheaper -- it makes emission be followed by
gcc instead of by a refusal.

- **`pcrec-auto-bigcap` ≈ 41 min**: the same 29 min of emission, plus gcc on
  1-6 MB of mostly table initializer per artifact (~1-2 s each by
  `limits.md` §8's per-entry figure, so 2-4 min over 130 emits), plus ~8 min
  of match and throughput. Comfortably inside the 5400 s per-cell cap.
- **`pcrec-vm-bigcap` is the one that may not fit: 12 to 91 min of compile
  ALONE.** The thirteen wide rungs carry 102,045 branch bytes and 13,824
  branches; at 5.37 ms of gcc per VM node that is 74 s per emit-set under a
  node-per-branch model and 548 s under a node-per-branch-BYTE model, so
  ten emits are 12 min or 91 min. The pessimistic end is over the cap before
  the twenty compiling patterns (another 3-26 min) and before the match side
  (~22-55 min). The differential in P13 says which model is closer: `w-512`
  emits roughly 678 KB of C from 4,264 branch bytes, about 159 B of C per
  branch byte, which is 16 MB of straight-line C per emit-set across the
  thirteen -- nearer the pessimistic end than the optimistic one.

**What to measure before committing the raised-cap VM cell.** One rung, one
trial: `pcrec-vm-bigcap` on `w-512` at `--trials 1`, and read the per-emit
cost off it. If it exceeds ~40 s, the full five-trial cell will not fit and
the levers are `--trials 3` (worth about 40 %) or splitting the thirteen
wide rungs into a cell of their own. This estimate should not be spent
without that one number.

**The general lever, unchanged from 0.1: drop `t-512k-sparse`.** It is 57 %
of the throughput bytes, so removing it takes every backtracking cell down
by rather more than half and costs only the SIZE arm -- the density arm,
which is what separates the failing scan from the cost at a hit, is entirely
at 128 KB. `--trials 3` is the second lever, worth about 40 %.

**The expectation derivation** (`make check`'s slow half) went from 1,600
rows to 2,772 and from a set of 20 patterns to 33. Measured on this box:
`make check-harness` 449 s before 0.2 and 468 s after, over every sub-bench;
`gen_expectations.py` alone is 135 s. That is +4 %, nowhere near the ~2×
`bench/altwide/CLAUDE.md` sets as the point at which the fix (fewer
throughput bytes, never fewer rungs) has to be proposed. No cut is needed
and none is proposed.

**What was cut to get here.**

- **The throughput subjects went from three 1 MB prose subjects to
  128 KB / 512 KB** (0.1). That was the first design and it is what plan row
  [B11.2] asks for; the probe is why it changed. Extrapolating the table
  above, `s-4096` over 1 MB is ~50 s for ONE subject, so a four-subject 1 MB
  regime is ~200 s per pass and ~20 min per trial-set for `s-4096` alone --
  with `pcre2-interp` and `pcrec-vm` each spending over an hour in a regime
  whose numbers the 128 KB subjects give just as well. The DENSITY axis was
  kept whole and the SIZE axis reduced to one pair.
- **`w-4096` at 3-12 byte branches** (0.1), which libpcre2 refuses outright;
  the short-word pool carries the 4096-way rung instead, and since 0.2 it
  carries the length pair at three widths.
- **`cnt-256`** (0.2): the count arm is already measured under the cap at 64,
  and a counted alternation is this set's most expensive kind of throughput
  pass. See "What was considered and left out" above.
- **A `srt-64` and a `srt-2048`.** The order arm now sits at two widths, 256
  and 512, which is what 0.2 needed: one of them compiles. A third width
  would add a confirmation rather than a fact.
- **A single-character-branch rung.** ALTCLS stage 1 merges runs of
  single-character branches, and `(?:a|b|c|...)` would measure it -- but the
  brief fixes branch literals at 3-12 bytes, and keeping every branch above
  the merge threshold is what makes P1/P17's "`_ALTCLS_MERGES` = 0
  everywhere" a clean statement about stage 2 alone. It is the obvious next
  arm if the manager wants stage 1 covered, and it is one cheap rung.
- **Structure arms at 1024 and 2048.** Each structure pool would have to be
  redrawn four times as large -- and a redraw changes the pools, which are
  the set. The width-by-structure question is answered by three widths plus
  the ladder.

The one structural note this author would give the manager rather than act
on: **the DFA state ceiling cannot be reached by any set that takes its
expectations from libpcre2**, because PCRE2's own compiled-size ceiling
fires first (P6, unchanged at 0.2 -- the widest new trie is 2,346 nodes). If
pcrec's behaviour at 32,000 states matters, it needs either a non-PCRE2
oracle or a pattern family whose state count grows faster than its compiled
size -- a state-explosion shape like `[01]*1[01]{k}` rather than a wide
alternation. That is a scope question, not a change to this set.

## Origin

0.2 ([B31], 2026-09-02) extended the set without changing it: thirteen
patterns and two subjects APPENDED, every 0.1 pattern byte, every 0.1 subject
byte and every 0.1 expectation row unchanged. Its author worked under the
same pcrec blinding the 0.1 author did (`docs/spec/` only) and under this
repo's, but was handed five measured facts from the 2026-09-02 full-suite
reading and is therefore not blind in 0.1's sense — "How blind this author
was" says exactly which five and where each is used. What follows is 0.1's
statement, unchanged.

Nothing here is copied. The patterns, the subjects and the predictions were
authored from the GOAL — plan row [B11.2], requirements §5's wide-alternation
family — by an author working under [B11.2]'s blinding: pcrec's `docs/spec/`
was read (`tuning.md` for the ALTCLS pass, the prefilter and offset-skip axes,
the table encoding and the scan edge; `limits.md` for the state ceilings and
the emitted-size caps; `cli.md` for the module roster and the `std1` set), and
pcrec's `tests/`, `src/`, corpora, `docs/dev` and `docs/design` were NOT, nor
this repo's `testees/`, `store/`, `reports/`, `docs/dev/ledgers/` or either
pcrec-facing mailbox. `bench/bounded/` and `bench/loglines/` were read in full
as TEMPLATES — the discipline (a derived-and-committed facts table, an oracle
limits probe, an exactly allocated hit population, a floor with a stated m/n, a
cell-time estimate with what was cut) is theirs; not one pattern or subject
byte is. That is pcrec's D27 lesson applied to a bench: tests derived from the
code inherit the code author's blind spots, and this sub-bench's job is to find
one.
