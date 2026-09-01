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
   28). A subject carrying `main` word 7 is the LAST branch of `w-8` and the
   eighth of `w-2048`. Neither difference can cost an automaton anything.

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
difference and nothing else.

| pattern | branches | branch B | bytes | trie | first CU | m/n |
|---|---|---|---|---|---|---|
| `w-8` | 8 | 4-12 | 56 | 43 | bitmap | 2/38 · 9/38 · 3/4 |
| `w-64` | 64 | 3-12 | 526 | 413 | bitmap | 2/38 · 9/38 · 3/4 |
| `w-256` | 256 | 3-12 | 2101 | 1575 | bitmap | 3/38 · 11/38 · 3/4 |
| `w-512` | 512 | 3-12 | 4264 | 3118 | bitmap | 4/38 · 13/38 · 3/4 |
| `w-1024` | 1024 | 3-12 | 8705 | 6169 | bitmap | 4/38 · 14/38 · 3/4 |
| `w-2048` | 2048 | 3-12 | 17495 | 11918 | bitmap | 5/38 · 16/38 · 3/4 |
| `s-2048` | 2048 | 3-6 | 12140 | 6566 | bitmap | 1/38 · 1/38 · 3/4 |
| `s-4096` | 4096 | 3-6 | 24343 | 12363 | bitmap | 2/38 · 3/38 · 3/4 |

`s-2048` is `w-2048`'s controlled pair: same width, same first-byte spread,
branch LENGTH is the only thing that moved (17,495 B of pattern against 12,140,
11,918 trie nodes against 6,566). `s-4096` is the brief's 4096-way alternation
and the widest pattern in the set. The short pool exists because libpcre2
refuses `w-4096` outright — see "The oracle's own ceiling" below.

### The structure arms (the search axis)

At 64 and at 512 where affordable, so structure is crossed with width rather
than measured at one point.

| pattern | what it spells | distinct first | max_first_run | first CU | required CU |
|---|---|---|---|---|---|
| `sh1-64`, `sh1-512` | every branch starts `k` | 1 | 64, 512 | `k` | NONE |
| `pfx3-512` | every branch starts `qux` | 1 | 512 | `q` | NONE |
| `nar4-64`, `nar4-512` | four first bytes | 4 | 4, 7 | bitmap | NONE |
| `sfx-64`, `sfx-512` | every branch ends `ing` | 25, 26 | 2, 3 | bitmap | **`g`** |
| `w-512` (the anchor) | first bytes spread over 26 | 26 | 2 | bitmap | NONE |

`sfx-*` are the only patterns in the whole set with a PCRE2 required code
unit, which is what makes them the required-byte arm rather than "another
structure". `pfx3-512`'s `min_length` is 6 where every other member's is 3 or
4 — a second, independent dismissal PCRE2 gets on that arm alone.

### Order and the wrappers

| pattern | what it is | how it differs from its pair |
|---|---|---|
| `srt-512` | `w-512`'s own 512 branches, sorted by first byte | `max_first_run` 28 against 2. Identical bytes (4264), identical trie (3118), identical answers on all 42 subjects |
| `ci-512` | `w-512` under `(?i)` | +4 bytes; picks up the two upper-cased subjects (search 15/38 against 13/38) |
| `cnt-64` | `w-64` under `{1,3}` | the bridge to `bench/bounded`: the counter rung and the alternation width multiply. Match 3/38 against 2/38 — `f-cnt2`, two adjacent branches taken whole |
| `wb-512` | `w-512` inside `\b…\b` | search 9/38 against 13/38: the four subjects whose branch sits inside a longer LETTER RUN — the two glued and the two doubled — are hits for `w-512` and misses here |

`ci-512`, `cnt-64` and `wb-512` are `w-512`/`w-64` plus exactly one construct,
so each is a one-variable comparison against a member already in the set.

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

**FIELDS (17, 4-18 B, the `match` regime).** One whole-string hit from every
rung and every structure pool, so no pattern's match row is empty: `main` words
0, 7, 255, 511 and 2047 (each the last branch of a different rung), `short`
words 0 and 4095, and one branch from each of `sh1`, `pfx3`, `sfx`, `nar4`.
Plus four designed MISSES that fail for four different reasons — a branch with
its last byte changed, a proper PREFIX of a branch (which no shorter branch
rescues, because the pools are substring-free), a branch buried in a longer
letter run, and a word in no pool at all — and two derived hits: the
upper-cased form (`ci-512` alone) and two adjacent branches (`cnt-64` alone
takes both).

**LINES (21, ≤ 256 B, the `search_short` regime).** Machine prose whose
background is branch-free by construction and re-asserted per subject. Twelve
carry exactly one branch at a designed POSITION — early (token 2), mid, or last
— and a designed branch INDEX; three carry a derived token (upper-cased,
glued, doubled); six are pure background. The position and the identity are
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
is the same 38 subjects unanchored — the set's main axis, mostly failing by
design. `throughput` is the four large prose subjects under find-all.

## The floor pattern

`#`, one literal byte, `role = "floor"` (requirements §5, the rule since
[B15]). It occurs in this set ONLY as the first byte of a line subject, which
gives one pattern three different readings of the harness's own per-call
overhead:

- on the 21 LINES, a hit at offset 0 — the closest thing to pure per-call
  overhead the set can measure (search 21/38);
- on the 17 FIELDS, a whole-subject miss on 4-18 bytes;
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

**No variants.** All twenty patterns are canonical PCRE2 spellings and every
adapter runs the canonical text (requirements §4.5; the record still states
that, as `patterns[].variant = null`). Neither adapter passes a compile option.

**pcre2-interp / pcre2-jit.** The whole-subject regime is
`PCRE2_ANCHORED|PCRE2_ENDANCHORED` on the plain compile (harness contract §2).
`pattern_facts.tsv`'s `first_code_unit` / `required_code_unit` / `min_length`
columns are PCRE2's own analysis, read live off the oracle, and are the honest
statement of what its start optimization has to work with on each arm. They are
NOT evidence about any other engine: a testee that disagrees with those columns
is a finding, not an error.

**pcrec (all configs).** One pattern uses `\b` (`assertions`, built but not in
the frozen `std1` set), for which `--features all` is already on every pcrec
testee config — a flag of the TESTEE, not a variant of the pattern, and the
text is byte-identical either way. `(?i)` is the `modifiers` module, which IS
in `std1`, so `ci-512` needs nothing. Every pcrec testee also compiles a second
artifact from `(?:<pattern>)\z` for the whole-subject regime, which doubles the
compile-axis cost on a set whose widest patterns are 17 KB and 24 KB — see the
estimate below.

## Cell-time estimate, and what was cut to get there

One cell = one testee x 20 patterns x three regimes at `--trials 5`. The
harness calibrates each (pattern, regime) loop so the MEDIAN subject's loop is
50 ms, and caps a trial's predicted sweep at 20 s by lowering `iters` --
never below 1, so a regime whose single pass already exceeds the budget runs
at one iteration and takes what it takes (`harness.py`, `calibrate`). The
throughput probe itself runs at `iters = 1`, so a trial-set is SIX passes:
one probe and five trials.

The numbers below are anchored on a design-time probe of the ORACLE
(libpcre2 10.46, the interpreter, no JIT) over this set's own subjects, one
pass per pattern per regime -- archived with its own caveats at
`docs/dev/measurements/2026-09-01-altwide-oracle-pass-cost.txt`. That probe
is a SIZING INPUT, not a measurement: it ran on a box carrying another
session's battery (load average 6.7-8.0 on 12 cores), unrepeated and
ungated. Read it as an upper bound on an interpreter's per-pass cost.

| regime | one pass, all 20 patterns | per trial-set (x6) |
|---|---|---|
| `match` (38 subjects) | 0.007 s | calibrated up to ~50 ms x 20 x Sigma/median |
| `search_short` (38 subjects) | 0.63 s | same |
| `throughput` (4 subjects, 896 KB) | **138 s** | **~14 min** |

- **The two short regimes cost about 4 minutes of a trial-set** on any
  testee. Their passes are milliseconds, so `iters` calibrates UP to the
  50 ms target and each pattern's trial sweep is 50 ms x Sigma/median --
  about 1 s for the search band (Sigma/median ~= 20 over 38 subjects) and
  about 0.6 s for the anchored one. 20 patterns x 5 trials x ~1.6 s ~= 160 s,
  plus the two probes.
- **The throughput regime IS the cell on a backtracking testee.** One pass is
  138 s, of which `s-4096` alone is 44 s and the four widest rungs are 104 s.
  Every one of those is already at `iters = 1`, so nothing calibrates it
  down: six passes is **~14 min**.
- **compile, pcrec only**: 20 patterns x 2 forms x 5 trials = 200 emits. The
  DFA route's table artifacts are predicted cheap for gcc (`limits.md` 8's
  0.905 us per table entry: even 300,000 entries is 0.27 s). The dominant
  unknown is `pcrec-vm` on the four widest rungs, where a VM node costs gcc
  5.37 ms -- 2,000 nodes is 11 s, x 10 emits per pattern -- and P5 predicts
  those rungs may refuse before gcc ever sees them.

**~5 min for an automaton cell (`pcrec-auto`, `pcrec-nocaps`) plus compile,
~5-6 min for `pcre2-jit`, and ~18 min for `pcre2-interp`.** `pcrec-vm` is the
one genuinely open number: its throughput cost on a wide alternation is what
this set was built to find out, and if it runs 3x the interpreter's that cell
is ~45 min rather than ~18. **The lever, if the manager needs one, is
dropping `t-512k-sparse`**: it is 57 % of the throughput bytes, so removing it
takes every backtracking cell down by rather more than half and costs only the
size arm (the density arm, which is the one that separates the failing scan
from the cost at a hit, is entirely at 128 KB). `--trials 3` is the second
lever, worth about 40 %.

**What was cut to get here.**

- **The throughput subjects went from three 1 MB prose subjects to
  128 KB / 512 KB.** That was the first design and it is what plan row
  [B11.2] asks for; the probe is why it changed. Extrapolating the table
  above, `s-4096` over 1 MB is ~50 s for ONE subject, so a four-subject 1 MB
  regime is ~200 s per pass and ~20 min per trial-set for `s-4096` alone --
  with `pcre2-interp` and `pcrec-vm` each spending over an hour in a regime
  whose numbers the 128 KB subjects give just as well. The DENSITY axis was
  kept whole and the SIZE axis reduced to one pair, because density is what
  separates the failing scan from the cost at a hit and size only confirms
  linearity.
- **`w-4096` at 3-12 byte branches**, which libpcre2 refuses outright; the
  short-word pool carries the 4096-way rung instead and `s-2048` beside
  `w-2048` pays for the comparison.
- **A `srt-64` and a `srt-2048`.** The order arm is measured at one width:
  the stamp it targets (`_ALTCLS_FACTORED`) is per artifact, so a second
  width would add a confirmation rather than a fact.
- **A single-character-branch rung.** ALTCLS stage 1 merges runs of
  single-character branches, and `(?:a|b|c|...)` would measure it -- but the
  brief fixes branch literals at 3-12 bytes, and keeping every branch above
  the merge threshold is what makes P1's "`_ALTCLS_MERGES` = 0 everywhere" a
  clean statement about stage 2 alone. It is the obvious next arm if the
  manager wants stage 1 covered, and it is one cheap rung.
- **Structure arms at 1024 and 2048.** Each structure pool would have to be
  redrawn four times as large, and the width-by-structure question is
  answered by two widths plus the ladder; four would be a surface, not a
  cross.

The one structural note this author would give the manager rather than act
on: **the DFA state ceiling cannot be reached by any set that takes its
expectations from libpcre2**, because PCRE2's own compiled-size ceiling fires
first (P6). If pcrec's behaviour at 32,000 states matters, it needs either a
non-PCRE2 oracle or a pattern family whose state count grows faster than its
compiled size -- a state-explosion shape like `[01]*1[01]{k}` rather than a
wide alternation. That is a scope question, not a change to this set.

## Origin

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
