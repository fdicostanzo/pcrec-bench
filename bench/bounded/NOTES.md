# bench/bounded — the count ladder, the everyday shapes, and what the numbers mean

Requirements §4.5 and §5: the per-engine notes, the declared variants, and the
statement of what this sub-bench exists to exercise. Read with
`pattern_facts.tsv` (the count facts, PCRE2's analysis and the m/n per
regime, all DERIVED) and `oracle_limits.tsv` (where the oracle itself stops
on each skeleton).

## The objective, and what would defeat it

> Bounded repeats on both axes: what an engine pays to COMPILE a counted
> repeat as the count grows, nests and changes body — through to the count at
> which it refuses, which is a first-class outcome and the number the count
> ladder exists to locate — and what it pays to MATCH the everyday bounded
> shapes and the hazard-band ones on subjects that match, that fail at the
> last repetition, and that over-run the count and fail only at the end
> anchor.

**Where it comes from.** Plan row [B11.4] names three numbers. (1) The
COMPILE axis: pcrec's own artifact-size census (inbox I-15 (c)) found every
size outlier in "counter-rung body replication under nested bounded
repeats", and pcrec's abi 11 ([ART-SIZE], inbox I-17) now decides an
artifact by two emitted-size caps and a size ladder for the counter rung's
unroll K — this set's artifact-size and compile-time columns, against the
COUNT, are the design input for that size term. (2) The MATCH axis in the
K23/K32 band: inbox I-14 (iii) filed "why a bounded lazy repeat before a
`\b` alternation reaches 32,000 DFA states" as a measurement here, and
[ENG-COUNT] (I-17 (c)) said large DFA-side counts like `[a-z]{0,30000}`
"would find their measured need here if one exists". (3) The give-up or
refusal as a first-class outcome with THE COUNT AT WHICH IT FIRST FIRES —
inbox I-2 §1(b)'s "size at which it first fires", which for this set is a
count sweep in the patterns rather than a size sweep in the subjects.

**What would defeat the objective.** On the compile axis: a testee that
compiles a bounded repeat as an unbounded loop plus a runtime counter and
never pays for the count at all is not defeating anything — that IS an
answer, and the ladder is built so that answer shows as a flat line against
a line that grows. What would defeat it is an engine that caches a compiled
artifact across trials, or that reports a compile it did not perform. On
the match axis: a subject that fails at byte 0. Every near-miss here fails
at the LAST repetition or at the end anchor, and every background line is
built from near-misses of the everyday shapes (`boundedtext.py`), so a
failing cell is the cost of getting the count nearly right, not of rejecting
the first byte.

## The patterns

`pattern_facts.tsv` is the authority; the table below is that file at the
time of writing, with the purpose beside it. `max_count` is the ladder's
rung, `nest_depth` how deep the counted repeats nest, `count_product` the
product of the maxima through the nest (the most repetitions of the
innermost body a match can contain — the quantity a body-replicating
compiler's size follows). m/n is match / search_short / throughput.

### The everyday shapes (the match axis)

| pattern | text | purpose | m/n |
|---|---|---|---|
| `year4` | `\d{4}` | a fixed-width digit field; the near-miss is 3 digits | 1/49 · 21/46 · 2/5 |
| `hex32` | `[0-9a-f]{32}` | a 32-hex id; the near-miss is 31 hex (fails at the 32nd repetition) | 2/49 · 6/46 · 2/5 |
| `pw-8-64` | `.{8,64}` | a password length rule; 7 bytes fails at the 8th repetition, 65 fails at `\z` after 64 | 26/49 · 38/46 · 5/5 |
| `line-80` | `.{80,}` | a line-length rule: an OPEN count; the everyday `{n,}` | 14/49 · 11/46 · 5/5 |
| `dotted4` | `(?:\d{1,3}\.){3}\d{1,3}` | nested counts with a literal separator: unambiguous; three octets fails inside the 3rd group repetition, a 4-digit last octet fails at `\z` | 1/49 · 4/46 · 0/5 |
| `csv5` | `(?:[^,\n]{0,32},){4}[^,\n]{0,32}` | a five-field record: a bounded negated class under a bounded group; four fields fails at the 4th comma | 1/49 · 3/46 · 0/5 |
| `ctx-lazy-64` | `\b(?:fail\|abort\|panic)\b.{0,64}?\b(?:disk\|memory\|socket\|quota)\b` | the bounded-context shape, rung 64 | 1/49 · 1/46 · 0/5 |
| `ctx-lazy-256` | … `.{0,256}?` … | rung 256 — one rung above the count the loglines witness overflowed pcrec's DFA at | 2/49 · 3/46 · 0/5 |
| `ctx-lazy-1024` | … `.{0,1024}?` … | rung 1024 | 2/49 · 3/46 · 0/5 |
| `ctx-greedy-256` | … `.{0,256}` … | the greedy twin of rung 256: same language, same count, greedy gap — separates "lazy" from "a bounded gap before a `\b` alternation" as the cause | 2/49 · 3/46 · 0/5 |

The four `ctx-*` patterns are a count ladder of their own, on the MATCH-axis
shape. `pattern_facts.tsv` says what PCRE2's analysis makes of them: NO
required code unit (the alternation's branches end in different bytes),
exactly as `bench/loglines`'s `level-context` — so no required-byte
precheck helps them and every engine scans.

### The short-run digit family (0.3, the match axis at small counts)

`year4` shaped as a ladder, both ways of spelling a short run. The pair at
each rung is the point: `\d{k}` fixes the length, `\d{1,k}` bounds it, and
the difference is what an engine can know before it scans. Their subjects are
0.3's digit length ladder, on which for each rung one subject matches
exactly, one is a near-miss one short, and one over-runs.

| pattern | text | rung | purpose | m/n |
|---|---|---|---|---|
| `dig-exact-2` | `\d{2}` | 2 | the shortest fixed run in the set | 1/49 · 33/46 · 2/5 |
| `year4` | `\d{4}` | 4 | (the everyday shape above; the family's 4-rung, byte for byte) | 1/49 · 21/46 · 2/5 |
| `dig-exact-8` | `\d{8}` | 8 | | 1/49 · 12/46 · 2/5 |
| `dig-exact-16` | `\d{16}` | 16 | | 1/49 · 8/46 · 2/5 |
| `dig-exact-32` | `\d{32}` | 32 | the rung `hex32` sits at, on the digit axis | 1/49 · 3/46 · 2/5 |
| `dig-upto-2` | `\d{1,2}` | 2 | the bounded twin: no last-repetition boundary to miss | 2/49 · 36/46 · 2/5 |
| `dig-upto-4` | `\d{1,4}` | 4 | `year4`'s own twin | 4/49 · 36/46 · 2/5 |
| `dig-upto-8` | `\d{1,8}` | 8 | | 7/49 · 36/46 · 2/5 |
| `dig-upto-16` | `\d{1,16}` | 16 | | 10/49 · 36/46 · 2/5 |
| `dig-upto-32` | `\d{1,32}` | 32 | | 15/49 · 36/46 · 2/5 |

The `match` column IS the ladder: `\d{k}` matches exactly the one digit
subject of length k, and `\d{1,k}` matches every digit subject of length
<= k (2, 4, 7, 10, 15 of them at k = 2, 4, 8, 16, 32), so the two halves
read against each other rung by rung with no other variable moving. In
`search_short` both halves are mostly-MATCHING by nature (a digit run of the
required length occurs inside every timestamp and every hex token), which is
why the compile and match axes carry this family's question and the search
column is stated rather than relied on.

### The count ladder (the compile axis)

| pattern | text | rung / product | what it isolates | m/n |
|---|---|---|---|---|
| `cls-upto-4` | `[a-z]{0,4}` | 4 | 0.3 LOW rung (ask (ii)) | 1/49 · 46/46 · 5/5 |
| `cls-upto-8` | `[a-z]{0,8}` | 8 | 0.3 low rung | 2/49 · 46/46 · 5/5 |
| `cls-upto-16` | `[a-z]{0,16}` | 16 | 0.3 low rung | 3/49 · 46/46 · 5/5 |
| `cls-upto-32` | `[a-z]{0,32}` | 32 | 0.3 low rung: the everyday band's floor (`hex32`'s count) | 4/49 · 46/46 · 5/5 |
| `cls-upto-64` | `[a-z]{0,64}` | 64 | 0.2 knee rung: the skeleton below the everyday band (`pw-8-64`'s count) | 7/49 · 46/46 · 5/5 |
| `cls-upto-128` | `[a-z]{0,128}` | 128 | 0.2 knee rung: the 64/256 midpoint | 8/49 · 46/46 · 5/5 |
| `cls-upto-256` | `[a-z]{0,256}` | 256 | the class-body `{0,n}` skeleton — [ENG-COUNT]'s shape — the 0.1 ladder's small end | 9/49 · 46/46 · 5/5 |
| `cls-upto-512` | `[a-z]{0,512}` | 512 | 0.2 knee rung | 11/49 · 46/46 · 5/5 |
| `cls-upto-1024` | `[a-z]{0,1024}` | 1024 | 0.2: the group-vs-class pair's class half — same count and language as `grp-upto-1024` | 12/49 · 46/46 · 5/5 |
| `cls-upto-2048` | `[a-z]{0,2048}` | 2048 | 0.2 knee rung | 12/49 · 46/46 · 5/5 |
| `cls-upto-4096` | `[a-z]{0,4096}` | 4096 | the skeleton at 4096 (0.1) | 12/49 · 46/46 · 5/5 |
| `cls-upto-8192` | `[a-z]{0,8192}` | 8192 | 0.2 knee rung | 12/49 · 46/46 · 5/5 |
| `cls-upto-16384` | `[a-z]{0,16384}` | 16384 | (0.1) — predicted the LARGEST ACCEPTED artifact in the bench (below) | 12/49 · 46/46 · 5/5 |
| `cls-upto-32768` | `[a-z]{0,32768}` | 32768 | (0.1) — the predicted first REFUSAL for pcrec (below) | 12/49 · 46/46 · 5/5 |
| `cls-upto-65535` | `[a-z]{0,65535}` | 65535 | (0.1) at PCRE2's own count ceiling (`{0,65536}` is refused by the oracle) | 12/49 · 46/46 · 5/5 |
| `cls-atleast-4096` | `[a-z]{4096,}` | 4096 / open | the OPEN count: 4096 mandatory repetitions then a loop — the control with no upper bound to unroll | 0/49 · 0/46 · 3/5 |
| `cls-lazy-16384` | `[a-z]{0,16384}?` | 16384 | the lazy twin of the 16384 rung (greedy vs lazy at a large count) | 12/49 · 46/46 · 5/5 |
| `grp-upto-1024` | `(?:a\|[b-z]){0,1024}` | 1024 | the GROUP body, same language as `[a-z]{0,1024}`: a DFA sees a class, a body-replicating compiler sees a group, PCRE2 replicates it per count (its last accepted octave: 2048 is refused, `oracle_limits.tsv`) | 12/49 · 46/46 · 5/5 |
| `nest2-4` | `(?:\d{1,4}){1,4}` | 4 / 16 | two-deep nest, small: 17 digits is a near-miss the oracle finishes | 10/49 · 36/46 · 2/5 |
| `nest2-64` | `(?:\d{1,64}){1,64}` | 64 / 4096 | two-deep nest, large: the census's "nested bounded repeat" shape at product 4096 | 18/49 · 36/46 · 2/5 |
| `nest3-3` | `(?:(?:\d{1,3}){1,3}){1,3}` | 3 / 27 | three-deep nest, small: 28 digits is a near-miss the oracle finishes (≈ 3 ms on the interpreter) | 12/49 · 36/46 · 2/5 |
| `nest3-16` | `(?:(?:\d{1,16}){1,16}){1,16}` | 16 / 4096 | three-deep nest, large: product 4096 at depth 3 vs `nest2-64`'s at depth 2 | 18/49 · 36/46 · 2/5 |
| `nest2-letters-6` | `(?:[a-z]{1,6}){1,6}` | 6 / 36 | the ambiguous nest the MATCH axis pays for: every letter run over 36 is a near-miss a backtracker decomposes 7^6 ways (≈ 1.7 ms on the interpreter, measured on the oracle) while a DFA is linear | 5/49 · 26/46 · 3/5 |
| `floor` | `:` | — | the per-call floor control (below) | 0/49 · 6/46 · 0/5 |

**Why `{0,n}` in search reads 46/46.** An optional repeat matches the empty
string at offset 0 on every subject, so every `cls-upto-*`, `cls-lazy-*`
and `grp-upto-*` search cell is a match of length 0..n at 0 — the
expectation is honest and the number is dispatch plus the run's length.
The regimes where those rungs do work are `match` (the run must be the
whole subject: 256 letters match `{0,256}`, 257 fail at `\z`; since 0.3
EVERY rung from 4 up has at least one letters run it matches whole, and the
rungs at 1024 and above have twelve of them, 4 B to 1024 B — a length
sweep, not a point) and
`throughput` (find-all over a 4/16/64 KB run drives the counter to its full
value: `cls-upto-65535` on the 64 KB run is one match of 65535 bytes and a
1-byte remainder). `cls-lazy-16384` under find-all is 4097 / 16385 / 65537 empty
matches on the letter runs and 4097 / 16385 on the digit runs — the lazy
quantifier's honest answer, and a per-call number.

**Everything nests non-capturing.** Every group in the set is `(?:…)`;
`gen_expectations.py` re-checks on every run that no capturing group
participated in any match and says so on stderr (shared code,
`pcrecbench/expectations.py`). The span is the whole observable answer.

**Declared variants: none.** All thirty patterns are canonical PCRE2
spellings and every adapter runs the canonical text byte for byte, so every
record carries `patterns[].variant = null`.

**Feature tiers.** `base` is pcrec's frozen `std1` set. The four `ctx-*`
patterns use `\b` (the `assertions` module, built but not in `std1`), for
which every pcrec testee already passes `--features all` — a flag of the
TESTEE, not a variant of the pattern; the text is byte-identical either way
(the same posture as `bench/loglines`).

## The ladder, the predicted first refusal, and the oracle's own edge

Inbox I-2 §1(b) makes a give-up a first-class outcome and asks for the
point at which it first fires. Here that point is a COUNT. The ladder is
geometric where growth is the question (256 → 4096 → 16384: three accepted
points spanning two decades) and dense where the refusal is predicted
(16384 → 32768 → 65535), so the first refusing rung brackets the boundary
to within 2×; since 0.2 ([B21]) the class-body skeleton is FILLED to a
uniform factor-of-2 spacing from 64 up ("What 0.2 added", below), so a
strategy change anywhere on it is bracketed the same way. A refusal is recorded by the harness as `did-not-compile` with
the engine's own diagnostic, per pattern and per form, and the cell simply
has no match rows under it (harness.py: a pattern that did not compile is
skipped, never an error). NOTHING BELOW IS A MEASUREMENT — every line is a
prediction from the goal and from pcrec's published contract
(`docs/spec/limits.md`, the only pcrec document this author read), stated
so the window can confirm or refute it.

**The oracle's own edge (`oracle_limits.tsv`, derived, re-checked by `make
check`).** Two ceilings, told apart by PCRE2's diagnostic. The COUNT ceiling
is 65535: `{0,65536}` on any skeleton is "number too big in {} quantifier",
so 65535 is the last rung any PCRE2-dialect engine can be asked for and the
class ladder stops there. The COMPILED-SIZE ceiling ("regular expression is
too large") fires only where PCRE2 replicates per count — a repeated GROUP,
never a repeated single unit — and it fires far below 65535: `grp-upto`
refuses at 2048, `nest2` at 4096, `nest3` at 96, `nest2-letters` at 1536.
Every rung in the set is below these by construction: a rung the oracle
cannot compile can carry no expectation, and a cell without an expectation
is one the harness cannot judge (it would be labelled
`did-not-match-as-expected` with "no expectation exists"). So the pcre2
TESTEES are predicted to compile every pattern here, and their refusals are
documented by the probe table rather than measured — a limitation this set
accepts and states (below, "What was cut").

**pcrec at abi 11 — predictions.**

- **Class-body ladder: the first refusal is at 32768.** `docs/spec/limits.md`
  §8 states that `[a-z]{0,30000}` emits 1,323,371 bytes, `a{0,25000}`
  1,103,367 and `a{1,31000}` 1,367,865 — table-dominated, ≈ 44 bytes per
  count — and that the total-emitted cap is 1,000,000 bytes, raise-only. At
  44 B/count the cap is crossed near count 22,700, so `cls-upto-16384`
  (≈ 720 KB emitted, `.o` ≈ 17 % of that ≈ 120 KB) is ACCEPTED and is
  predicted to be the largest artifact in the bench so far (the loglines
  window's largest was 76,304 B), while `cls-upto-32768` and
  `cls-upto-65535` are REFUSED by `PCREC_MAX_EMIT_BYTES` with the documented
  diagnostic — `did-not-compile` on both forms, both pcrec engines, since
  the table is the DFA's and the VM's alike. `cls-lazy-16384` and
  `cls-atleast-4096` are accepted. gcc time on the accepted table artifacts
  is predicted SMALL (the spec's 0.34 s for 1.37 MB of table): the ladder's
  compile-TIME growth on this skeleton is pcrec's own emit, not gcc's.
- **Group body: `grp-upto-1024` is accepted and its DFA artifact is the same
  size as `[a-z]{0,1024}`'s would be** (a DFA sees a one-class language); the
  VM artifact is where a body-replicating emitter would differ from the
  class rung, which is why the rung exists.
- **The nests are where `_UNROLL_K` first moves, if it moves anywhere in
  the bench.** The abi-11 window saw 0 K movements over 54 bench emits
  (inbox I-17: every VM artifact `K=8 / default`). `nest2-64` and `nest3-16`
  (product 4096 under body replication) are the census's outlier shape;
  the prediction is a stamped `_UNROLL_K_WHY` of `size-model` or
  `cap-rescue` on one of them, with `nest2-4` / `nest3-3` (products 16 / 27)
  as the same skeletons at `default`. A code-cap REFUSAL
  (`PCREC_MAX_VM_EMIT_CODE_BYTES`, 500,000) on a nest is possible and is
  bracketed rather than predicted: if it fires, the small rung of the same
  skeleton is the accepted side.
- **The `ctx-*` ladder: 256 and 1024 overflow the DFA's state cap and fall
  back to the VM under `auto`; 64 fits.** `bench/loglines`'s `level-context`
  (`.{0,200}?`) overflowed 32,000 states at abi 8 and did not compile; at
  abi 9+ ([SEL-1]) that is a selection outcome — a VM artifact stamped
  `RX_ENGINE_WHY "dfa overflowed: …"`. If the state count grows with the gap
  count, 256 and 1024 overflow and 64 does not; and `ctx-greedy-256` is
  predicted to overflow TOO, because the states come from tracking
  "position in the gap × progress into the alternation", not from laziness.
  The pair is what makes that a testable claim. `pcrec-vm` compiles all four
  either way.
- **DFA-class engines are linear on every match cell here; backtracking
  engines pay the near-misses.** `nest2-letters-6` on `r-00037` / `r-00256` /
  `r-00257` in the match regime is the cliff: ≈ 1.7 ms on the oracle
  against microseconds on `r-00036` one byte shorter; `nest3-3` on
  `d-00028` / `d-00256` ≈ 3 ms. Under pcrec's `auto` those rows are predicted
  DFA and flat; under `pcrec-vm` and the two pcre2 testees they are the
  hazard number (and, because the harness calibrates on the median subject
  and caps a trial at 20 s, those two patterns' match trials are predicted to
  hit the cap on the backtracking testees — a cost of the protocol, stated
  in the estimate below, not a give-up). On the `ctx-*` failing arm
  (`l-03`, `l-04`: a trigger and no context word) the lazy walk is bounded by
  the LINE, not the count, so the three lazy rungs are predicted to cost the
  same per call on a backtracker — the 1024 rung's number should not exceed
  the 64 rung's there.

## What 0.2 added ([B21]): the knee rungs, the group-vs-class pair, t-digits-004k

**What changed, and what did not.** Six class-ladder rungs (`cls-upto-64`,
`-128`, `-512`, `-1024`, `-2048`, `-8192`) and one throughput subject
(`t-digits-004k`, 4096 random digits). NOTHING ELSE: every 0.1 pattern keeps
its id and its exact bytes, `manifest.tsv` is byte-identical, and the four
0.1 throughput subjects reproduce byte for byte — the new run is drawn AFTER
them in `gen_throughput_subjects.py`, so their rng draws are the same stream
prefix, and `manifest_throughput.tsv`'s four 0.1 sha256s are unchanged.

**Why: the knee.** The 0.1 class ladder was three points spanning two
decades (256 / 4096 / 16384) plus the dense refusal band. If an
implementation changes strategy for `[a-z]{0,n}` somewhere — a count at
which one way of compiling or running the repeat stops being the faster
choice — three points two decades apart can only say "somewhere in here". At
uniform factor-of-2 spacing (64, 128, 256, 512, 1024, 2048, 4096, 8192,
16384, 32768, 65535) any knee in 64..65535 is bracketed within 2× by
adjacent rungs, and 64/128 bracket BELOW the everyday band (`hex32` at 32,
`pw-8-64` at 64), where 0.1 had no ladder point at all.

**The group-vs-class pair.** `cls-upto-1024` is `[a-z]{0,1024}` beside 0.1's
`grp-upto-1024` (`(?:a|[b-z]){0,1024}`): the same count, the same language
cardinality, group vs class body — so the difference between the two rows in
artifact size or compile time, on any engine, is the body representation and
nothing else. On the ORACLE the pair is already a reading: `oracle_limits
.tsv` has the class skeleton accepting every count to the 65535 ceiling
while the group skeleton's compiled-size ceiling refuses at 2048 — a
repeated group is replicated per count, a repeated single unit is one
opcode with a counter.

**t-digits-004k.** With it both content axes have a small and a large run
(letters 4 / 16 / 64 KB; digits 4 / 16 KB), so the knee is readable PER
SUBJECT on the matching-content axis (letters: the counter runs to the rung
or the run end) and on the non-matching axis (digits: `{0,n}` of `[a-z]` is
empty matches at every offset — pure per-call dispatch).

**Predicted readings — the oracle's own behaviour, nothing else** (this
author is blinded to engine internals, as 0.1's was; whether any TESTEE has
a knee, and at which rung, is exactly what the window measures):

- On the letter runs the find-all match count halves as the rung doubles,
  until the rung reaches the run: on `t-letters-004k` the ladder reads
  65 / 33 / 17 / 9 / 5 / 3 / 2 / 2 / 2 / 2 / 2 matches (`expectations.tsv`)
  — a known 1/n curve, so a testee's per-subject time read against it
  separates per-match dispatch from per-byte scanning, rung by rung.
- On the digit runs every `cls-upto-*` cell is 4097 / 16385 empty matches:
  identical answers at every rung, so a digit-run time that MOVES with the
  rung is a count-dependent per-call cost — the knee's signature on the
  non-matching axis.
- In `match` the new rungs read 2 / 2 / 4 / 4 / 4 / 4 of 30 (the 36/37-
  letter runs fit every rung; 256/257 fit from 512 up); in `search_short`
  all six are 30/30 empty-or-leading matches at 0, like every `{0,n}` rung
  (above) — dispatch-dominated by design.
- The oracle compiles all six new rungs (single-unit repeats below its
  count ceiling; the re-derived `cls-upto` row of `oracle_limits.tsv` is
  the proof), and no oracle give-up occurred on any of the 1950
  expectation cells.

**0.1 and 0.2 records NEVER POOL.** The subject sets differ (65 subject
slots per pattern against 64) and the pattern sets differ, so a set-grain
sum or median over `bounded@0.1` and one over `bounded@0.2` are sums over
different work; the reporter's version filter keeps them apart (records
compare only within one `id@version`, bench/CLAUDE.md). What REMAINS
comparable across the bump, by construction: any (pattern, subject, regime)
cell whose pattern id and subject appear in both versions — every 0.1
pattern and every 0.1 subject is byte-identical in 0.2 — read cell against
cell, never sum against sum.

**The cost.** Patterns 24 → 30, subject slots 64 → 65: the estimate below
(updated in place) grows by ≈ 2 min per cell, all of it dispatch-dominated
`{0,n}` cells — the price of reading the knee's location to within 2×. The
six new rungs are predicted on the compile axis to behave as the 0.1 rungs
below 16384 do (all sit below the smallest predicted refusal), so the
refusal predictions above are untouched by 0.2.

## What 0.3 added ([B27]): the STEP 2 match instrument, the low rungs, the short-run family

**What changed, and what did not.** THIRTEEN patterns (four low class-ladder
rungs `cls-upto-4/8/16/32`; the short-run digit family `dig-exact-2/8/16/32`
and `dig-upto-2/4/8/16/32`), NINETEEN subjects (letters runs at 4 / 8 / 16 /
32 / 64 / 128 / 512 / 1024; digit runs at 1 / 2 / 5 / 7 / 8 / 9 / 15 / 31 /
32 / 33 and 1024), and `short_search_max_bytes` 512 → 258. NOTHING ELSE:
every 0.2 pattern keeps its id and its exact bytes, every 0.2 subject
reproduces byte for byte (the new ones are drawn LAST, so the old draws are
the same stream prefix — the rule 0.2 followed for `t-digits-004k`), every
0.2 expectation row is unchanged, and no 0.2 subject changes regime (they
are all ≤ 257 B, on the same side of 258 as of 512). **0.2 and 0.3 records
never pool** — the pattern and subject sets differ, so a set-grain sum over
one is a sum over different work from a sum over the other, and the
reporter's version filter keeps them apart. What stays comparable across the
bump, by construction: any (pattern, subject, regime) cell whose pattern id
and subject appear in both, read cell against cell, never sum against sum.

**Why: two asks and a census.** Inbox I-29 chartered pcrec's two-pass fix
([OPT-5] STEP 2) and asked this set to "keep the 9-rung surface warm and add
MATCH-REGIME cells where the elision must show" (ask (iv)); asked for a
sweep over a VARIETY of low run-counts so the per-run edge-selection boundary
is "read off your instrument rather than argued" (ask (ii)); and asked for
the hybrid-gained-edge population (ask (v)). The third is answered in
`docs/dev/measurements/2026-09-01-hybrid-gained-edge-census.md`, and what it
found sets the shape of the first two: the edge's cost is a FIXED +6 to
+12 ns paid per matching call, so the ×1.07–1.11 the acceptance ledger
measured on `year4` is that term on a 24 ns call, and the number that decides
a knob is the COUNT at which a run is long enough to pay for it. No ladder
existed to read that count off. 0.3 is that ladder, on both content axes.

### (1) The match-regime cells: the mechanism, and why this one

**The problem.** The 9-rung `cls-upto-*` surface is measured on the LARGE
runs under `throughput`, which is find-all SEARCH — and pcrec's fix is to the
`_match` entry, which search keeps. The large runs are deliberately NOT
`match` subjects (`bench/bounded/CLAUDE.md` caveat 2: a 16 KB run beside a
36 B median puts every length-proportional pattern's match trial on the
harness's 20 s per-trial cap). So the regime where the elision must show had
no long-subject cells at all.

**The mechanism chosen: long runs appended to the SHORT manifest.**
`subbench.subjects_for()` returns EVERY short subject for `match` and filters
ONLY `search_short`, by `short_search_max_bytes`. A subject longer than that
cap is therefore a match-only subject already, with no code change anywhere:
no new regime, no `record.schema.json` enum entry, no `REGIME_TO_ENUM` /
`REGIME_MODE` / `PROBE_ITERS` row, no reporter legend, no reader that
switches on the regime. The cap moves 512 → 258 to put the line just above
this set's longest 0.2 subject, and moves no 0.2 subject across it.

**Why not a fourth regime.** It would be a record-schema change (the regime
enum is closed; growing it is a version bump under `record_schema.md` §4)
plus four harness tables and the reporter, to obtain a match semantics
(`PCRE2_ANCHORED|PCRE2_ENDANCHORED` at offset 0) that `match` ALREADY has.
The one thing it would buy is a separate calibration pool, so a long subject
could not skew a short one's `iters`; the estimate below is what says the
shared pool is affordable, and it is affordable by an order of magnitude.

**Why caveat 2's failure does not recur, in caveat 2's own arithmetic.**
`harness.calibrate()` predicts a trial's sweep as 50 ms × Σᵢ(costᵢ /
cost_median) and lowers `iters` until that is ≤ 20 s. Caveat 2's case was
4 KB and 16 KB runs against a ~36 B median: Σ/median ≈ 570 for a
length-proportional pattern, ≈ 28 s a trial from those subjects alone.
0.3's longest match subject is 1024 B. For the rungs that match it whole the
ENTIRE added set — letters 4 … 1024 plus the digit ladder plus the 1024 B
digit run — is Σ/median ≈ 50, about **2.5 s a trial**, one eighth of the cap
and one eleventh of caveat 2's number. The cap is not approached on any
pattern; the two rows that do hit it are the ones that hit it in 0.2
(`nest2-letters-6`, `nest3-3` on backtracking testees), for the same
near-miss reason and not because of a subject's length.

**Why 1024 B is enough, and why the sweep matters more than the top.** The
reverse pass is length-proportional, so what has to clear the noise is a
fraction of the scan, not the scan. At the acceptance ledger's own measured
`auto` letters rate (1.19–1.82 ns/B at a7e0bdf) a 1024 B whole-subject match
is 1.2–1.9 µs against a per-call floor of ~13–25 ns on this set's match
rows: dropping one of two passes is a ~600–900 ns move on a ~1.5 µs cell,
about fifty times the floor and far outside anything the v1.4 trial-agreement
rule tolerates. Going to 16 KB would buy another factor in absolute size and
cost the cap. What 0.3 buys instead is the LENGTH SWEEP: one rung at 1024 and
above now has twelve matching match cells at 4, 8, 16, 32, 36, 37, 64, 128,
256, 257, 512 and 1024 B, from which a per-byte SLOPE and a per-call
INTERCEPT separate. An elision of one of two length-proportional passes
halves the slope and leaves the intercept; a per-call change does the
opposite. One length could not tell those apart; twelve can.

**The reading frame — and the same-pin control that makes it self-checking.**
The `match` regime is measured on the WHOLE-SUBJECT artifact
(`adapters.py:form_for_regime()`), and at pin a7e0bdf those artifacts are NOT
uniform in their `_match` entry. Read from the store's own compile rows
(`RX_DFA_MATCH` / `rx_info.match_form`, abi 10, `pcrec-auto`, `bounded@0.2`):

| whole-subject artifact | engine | `_match` entry |
|---|---|---|
| `cls-upto-64` … `cls-upto-1024`, `grp-upto-1024` | dfa | `unwrapped` |
| `cls-upto-2048`, `cls-upto-4096`, `cls-upto-8192`, `cls-atleast-4096` | dfa | **`search-filter`** |
| `cls-upto-16384`, `cls-upto-32768`, `cls-lazy-16384` | vm | (no stamp — the scope iff) |
| `cls-upto-65535` | — | refused |

`search-filter` is [ENG-ABS]'s name for "the unanchored search with non-`pos`
starts rejected", i.e. the two-pass entry; `unwrapped` is the anchored
forward machine run from `ctx->pos`, i.e. the entry STEP 2 is described as
moving everything to. So **STEP 2's customers in the `match` regime are the
four `search-filter` wholes, and the five `unwrapped` rungs are its control
— same skeleton, same subject, adjacent count, already elided.** Two things
follow, and both are worth more than a BEFORE sample:

- The frame as stated in I-29 (iv) — "letters ~2.0× → ~parity on MATCH" at
  every rung — does not survive the census: on the artifact `match` actually
  measures, five of the nine rungs are already unwrapped and are predicted
  NOT to move. If they do move, the movement is not the elision.
- **The residual is testable on ONE pin.** `cls-upto-1024` (unwrapped) and
  `cls-upto-2048` (search-filter) both match `r-01024` whole, over the same
  1024 bytes, on the same engine, one rung apart. If the ×2.0 residual is the
  reverse pass, the 2048 rung's ns/B on that cell is already about twice the
  1024 rung's, TODAY, with no second pin. If it is not, the two-pass story is
  wrong and STEP 2 will not deliver parity — and this set says so before
  pcrec writes the code.

The census above is read at a7e0bdf and the stamps are re-read from every
window's own records; if I-30's pin moves an artifact between entry forms,
the frame moves with it, which is why the frame is stated as a stamp and not
as a list of rungs.

### (2) The low rungs and the short-run digit family

Ask (ii) wants the per-run edge-selection boundary read off an instrument.
Two ladders, one per content axis, both anchored on shapes the acceptance
ledger already measured:

- **`cls-upto-4/8/16/32`** extend the class ladder DOWN by four factor-of-2
  rungs below its 0.2 floor of 64, so the uniform bracketing runs 4 … 65535
  and a strategy change anywhere in it — including the count at which a scan
  edge stops being worth extracting — is bracketed within 2× by adjacent
  rungs. Through 0.2 these rungs would have had NO matching match cell (the
  shortest letters run was 36); 0.3's per-rung letters runs give each of them
  one.
- **The short-run digit family** is `year4` turned into a ladder in both
  spellings: `\d{k}` at k = 2 / 8 / 16 / 32 (k = 4 is `year4` itself, byte
  for byte) beside `\d{1,k}` at k = 2 / 4 / 8 / 16 / 32. The pair at each
  rung holds the class, the maximum and the subjects fixed and varies only
  whether the length is FIXED or BOUNDED — which is the difference between
  what an engine can know before it scans and what it must discover, and the
  plausible input to a skip-below-k decision.
- **One digit LENGTH LADDER serves every rung's three arms.** A digit run of
  length L matches `\d{k}` iff L = k and `\d{1,k}` iff L ≤ k, so the runs at
  1, 2, 3, 4, 5, 7, 8, 9, 15, 16, 17, 31, 32, 33 give every rung its exact
  match, its near-miss one short and its over-run at once (3, 4, 16 and 17
  are 0.2 subjects; ten are new). Three arms per rung as separate subjects
  would have cost thirty; the ladder costs ten, and every cell is one the
  oracle finishes in microseconds.

### (3) Predictions, written BEFORE the first sample

Stated from the acceptance ledger `2026-08-31-opt5-step1-acceptance-a7e0bdf.md`,
the hybrid-gained-edge census, and pcrec's published contract — nothing here
is measured on 0.3, and every line is meant to be confirmable or refutable by
one window. (This lane was NOT blinded: 0.3 extends a measured set against
measured ledgers, unlike the 0.1/0.2 authors.)

**P1 — the entry cost is a FIXED per-call term, so the short-run family's
loss falls as 1/k.** The census measured +5.9 to +7.9 ns on `nest2-64` across
call costs spanning ×13. Predicted on `dig-exact-k` / `dig-upto-k` matching
cells, `pcrec-auto` at a scan-edge pin against the same shapes at a pin
without one: a roughly constant absolute delta, so the RATIO is worst at
k = 2 and decays monotonically through k = 32. Refuted if the delta grows
with k (then the term is proportional and no skip-below-k knob helps).

**P2 — the boundary is a STAMP before it is a time.** `dfa_scan_edge` is
stamped per artifact. Either pcrec extracts a scan edge at every rung down to
2 (the stamp reads `range` on all ten digit patterns and all fifteen class
rungs, and the boundary is purely economic, to be read off P1's curve), or it
declines below some count (the stamp reads `none` at the low rungs and
`range` above, and the boundary is a NUMBER the ladder brackets within 2×).
Both are answers; the second is the cheaper one for pcrec to act on. The
prediction is that this set will distinguish them at the first window, which
is what "read off an instrument" was asked for.

**P3 — fixed and bounded runs are not the same decision.** `\d{k}` gives the
scan a length it knows; `\d{1,k}` does not. Predicted: at the same k the two
carry the same `dfa_scan_edge` value (the class is the same and the edge is a
property of the class run), and any difference between the pair is in
`engine_sel` or in the per-call time, not in the edge. A DIFFERING edge value
across a pair is a finding and the most interesting outcome available here.

**P4 — the two-pass residual, on one pin (above).** On `r-01024`, `auto`,
`match`: `cls-upto-2048` / `cls-upto-1024` ≈ 2.0 in ns per byte, with
`cls-upto-4096` and `cls-upto-8192` joining the 2048 rung and `cls-upto-512`
joining the 1024 rung. A ratio near 1.0 refutes the reverse-pass account of
the ×2.0 throughput residual before STEP 2 is written.

**P5 — the digits control must not move.** `[a-z]{0,n}` on a digit run fails
at byte 0 or 1 in `match`, so `d-01024` is a per-call cell on every class
rung and is predicted flat at the dispatch floor (~13–25 ns) at every rung
and every pin. Its job is to catch a per-call regression masquerading as a
scan win.

**P6 — the oracle's own facts, already re-derived** (`oracle_limits.tsv`,
`make check` re-derives them): both new skeletons `\d{N}` and `\d{1,N}` are
single-unit repeats, so they reach PCRE2's COUNT ceiling (65536 refused,
"number too big in {} quantifier") and never its compiled-size ceiling — the
same row shape as `cls-upto`, and a compiled-size refusal on either would
mean PCRE2 is replicating something this set assumes it does not.

**P7 — nothing about the refusals changes.** Every 0.3 rung and every 0.3
subject sits below the counts the 0.2 predictions are about, so the predicted
pcrec refusals (the emitted-size cap at `cls-upto-32768` and `-65535`) and
the `ctx-*` fallbacks are untouched by 0.3.

## The subjects

`gen_subjects.py`, seed **20260829**; `gen_throughput_subjects.py`, seed
**20260830**. Both draw from `boundedtext.py`, whose only randomness
primitive is `random.Random(seed).getrandbits(32)` — `choice`, `sample`,
`randrange` and `shuffle` are avoided because their internals have moved
between CPython releases and a committed manifest cannot rest on that.

**Three families, 49 short subjects (1-1024 B) + 5 large runs.** The
manifest's `description` names the family and the arm in a fixed spelling
(`field/match`, `field/near-miss`, `field/over-run`, `line/ctx-gap-N`,
`line/ctx-no-context`, `line/ctx-wrong-order`, `line/ctx-near-miss`,
`line/background`, `run/letters`, `run/digits`) so a reader of a record can
group cells by what the subject was built to do without a sixth manifest
column (the loader accepts four or five).

| family | n | sizes | what it is |
|---|---|---|---|
| FIELDS `f-*` | 13 | 3-65 B | whole-string candidates for the everyday shapes: each shape's exact match, its NEAR-MISS ONE UNIT SHORT (fails at the last repetition: `f-year-3`, `f-hex-31`, `f-pw-7`, `f-quad-3`, `f-csv-4`), and for `pw-8-64` and `dotted4` an OVER-RUN that satisfies the repeat and fails only at `\z` (`f-pw-65`, `f-quad-4x`) |
| LINES `l-*` | 8 | 50-254 B | ops prose of near-misses (`boundedtext.py`: numbers of ≤ 3 digits, hex of ≤ 12, three-part versions, five-group MACs, `failure`/`aborted`/`panicked`/`disks` where the ctx patterns want whole words); the everyday shapes injected into an exactly allocated minority (`COUNTS`: year4 2, hex32 2, dotted4 2, csv5 2 over the five pool lines); and the ctx structure per line — two WHOLE lines that start with a trigger and end with a context word at gaps 39 and 100 B (`l-00`, `l-01`: the match arm), a mid-line pair at gap 169 (`l-02`), two trigger-and-NO-context lines (`l-03`, `l-04`: the lazy walk finds nothing), one context-before-trigger (`l-05`), one near-miss-words-only (`l-06`), one background (`l-07`) |
| RUNS `r-*`, `d-*` | 28 | 1-1024 B | **0.2's nine**: random letters at 36 / 37 (the `nest2-letters-6` exact maximum and its near-miss) and 256 / 257 (the 256 rung's exact maximum and its over-run); random digits at 16 / 17 (`nest2-4`), 27 / 28 (`nest3-3`) and 256 (`nest2-64`'s and `nest3-16`'s territory, below every large rung's maximum). **0.3's nineteen** ([B27], drawn last so the nine above reproduce byte for byte): letters at 4 / 8 / 16 / 32 / 64 / 128 / 512 / 1024, one per class-ladder rung, so every rung has a whole-subject MATCH and the top rungs have a twelve-point length sweep; digits as a LENGTH LADDER at 1 / 2 / 5 / 7 / 8 / 9 / 15 / 31 / 32 / 33, which gives the short-run family's every rung an exact match, a near-miss one short and an over-run out of one ladder (the 3, 4, 16 and 17 rungs of it are 0.2 subjects already); and one 1024 B digit run as the letters run's control on the non-matching content axis. The three over 258 B are MATCH-ONLY (see "Regimes") |
| LARGE RUNS `t-*` | 5 | 4-64 KB | `throughput/`: letters at 4096, 16384, 65536 and digits at 4096 (0.2) and 16384 — the ladder's top rungs driven to their full count under find-all search, a small and a large run on BOTH content axes since 0.2 (`gen_throughput_subjects.py` says why they live here) |

**The runs are random WITHIN their class, not a repeated byte, and every
subject reads `periodic: no`.** Inbox I-10 / [B17]: a periodic subject makes
a loop's one data-dependent branch perfectly predictable and flatters any
per-byte number. A run of random `[a-z]` is still every byte in the class —
all the class ladder tests — and `gen_subjects.nonperiodic` DRAWS UNTIL the
`periodic` column (`pcrecbench.periodic`, the same function every manifest
uses) reads `no`, because that column's definition calls a string whose last
byte equals its first "periodic at n-1" and a 3-byte `202` periodic at 2:
the first cut had `d-00256` at period 255 and `f-hex-32` at 31 by that
accident, and a column that exists to say "non-periodic by construction"
should not carry an asterisk on one subject in ten. The price is that a
LITERAL-body rung (`a{0,n}`) would have nothing here it matches at length;
the body axis is therefore class vs group, and the literal body is not in
the set (it is one byte-test either way for a DFA; a body-replicating
compiler's difference between a literal and a class is the group rung's
question in miniature).

**The runs and the oracle — why the run lengths stop where they do.** A
nested bounded repeat is ambiguous: a run of the body class decomposes into
iterations many ways, and a near-miss LONGER than the pattern's maximum
makes a backtracking engine try every one. MEASURED on the oracle while
designing this set: `(?:\d{1,16}){1,16}` on 257 digits and
`(?:(?:\d{1,4}){1,4}){1,4}` on 65 digits both exhaust PCRE2's match limit
(`-47`, ≈ 1-1.4 s each); `(?:[a-z]{1,8}){1,8}` on 71 letters takes 0.5 s
without giving up. An expectation the oracle cannot state is a cell the
harness cannot judge, and a 0.5 s cell in a batched loop calibrated on a
microsecond median is a trial that hits the 20 s cap on every testee. So:
the digit runs are 16 / 17 (the k=4 rung's exact maximum and near-miss: 4^4
= 256 decompositions), 27 / 28 (the triple k=3 rung's: 3^9 ≈ 20k, ≈ 3 ms)
and 256 (the k=16 territory's maximum, and below every larger rung's, so
`nest2-64` and `nest3-16` have NO near-miss beyond their maximum — stated,
not hidden: their near-miss would be catastrophic for every backtracker
including the oracle); the letters nest is `{1,6}` (7^6 ≈ 118k, ≈ 1.7 ms)
rather than `{1,8}`. The oracle finishes every cell in the set (the whole
derivation runs in 0.14 s), and `gen_expectations.py` prints any give-up as
a DROPPED triple, which would be a design regression here.

**0.3's longer runs obey the same rule, and it is what caps them at 1024 B.**
Both large nests have count product 4096, so a digit run of 1024 (or 2048, or
4096) is not a near-miss at all: `nest2-64` takes it as 16 iterations of 64
and `nest3-16` as 8 × 16 × 16, greedily, on the first try, in time linear in
the run. A digit run of **4097** would be the catastrophic case — one past
both maxima — so 0.3 stops an octave short of it rather than beside it, and
the reason is in `gen_subjects.runs_0_3()` where a future editor will meet it.
The other two ambiguous nests are unaffected in kind: `nest2-4` (max 16) and
`nest3-3` (max 27) fail on every run longer than their maximum, but the work
is bounded by 4^4 and 3^9 decompositions no matter HOW much longer the run
is, so 0.3's extra digit subjects add ≈ 3 ms cells to `nest3-3` and nothing
measurable to `nest2-4`. Same for `nest2-letters-6` (max 36) on the new
letters runs: ≈ 1.7 ms each, the identical cost it already pays on `r-00037`.
The whole 4300-cell derivation runs in 4.0 s with no give-up.

**Match rates by DESIGN.** The everyday shapes are injected into the lines
by exact allocation without replacement (`gen_subjects.COUNTS`), not by a
per-line coin flip — `bench/loglines`'s lesson at n = 112 applies with more
force at n = 8. The realised m/n per pattern is the oracle's
(`pattern_facts.tsv`), and the everyday shapes sit at 1/49 in `match` (the
one exact-match field) and 1-4/30 in `search_short`: mostly-failing, with
the near-misses doing the failing. `year4` in search is 13/30 because a
4-digit run occurs inside every digit run and inside the 32-hex fields — the
honest answer, stated rather than engineered away. `pw-8-64` and `line-80`
are mostly-PASSING in search by nature (any 8+ byte subject satisfies
`.{8,64}` somewhere) and do their failing in `match`, where the length rule
is a whole-string question.

## Regimes: `match`, `search_short`, and a `throughput` that is not a size sweep

| regime | subjects | semantics | expectations |
|---|---|---|---|
| `match` | all 49 short (no length filter — `subjects_for()` filters only the search band) | `PCRE2_ANCHORED\|PCRE2_ENDANCHORED` at 0 | 310 of 2107 cells match |
| `search_short` | the 46 short subjects ≤ `short_search_max_bytes` = 258 | unanchored at offset 0 | first-match span; 1287 of 1978 cells match, most of them the `{0,n}` rungs' empty-or-leading matches at 0 |
| `throughput` | the 5 large runs | unanchored, find-all | first span + count; 131 of 215 cells match |

`short_search_max_bytes = 258` — between `bench/email`'s 256 and
`bench/loglines`'s 4096: the LINES are held to ≤ 256 B by the generator
(requirements §3's "~256-byte subjects (log lines, fields)" for this
regime), and 258 rather than 256 only so the 257-byte over-run of the 256
rung is not dropped from the search band by one byte. Through 0.2 the
number was 512 with that same one rationale, and every subject was ≤ 257 B,
so the two short regimes saw the same 30 — **the change to 258 moves no 0.2
subject across the line.** What it adds is a second job, and the whole of
0.3's match-regime mechanism: `subjects_for()` filters `search_short` by
this cap and does NOT filter `match` at all, so a subject longer than 258 B
is MATCH-ONLY. 0.3's three longest runs (512 and 1024 letters, 1024 digits)
are exactly that, which is why the two short regimes now see 49 and 46
subjects rather than one number twice.

**The `throughput` regime is declared for the ladder's TOP RUNGS, not for a
size sweep** — a declaration, not an omission, and the opposite choice from
`bench/loglines`. This set's give-up axis is the COUNT in the pattern
(above); the subject size is not swept for its own sake, and the five large
runs sit on the ladder's rungs (4 / 16 / 64 KB letters, 4 / 16 KB digits) so
`[a-z]{0,4096}`, the 16384 rungs and `[a-z]{0,65535}` are each driven to
their full count, on both content axes since 0.2 (`t-digits-004k`).
They live in their own regime rather than in `subjects/` for two reasons
`gen_throughput_subjects.py` states in full: the harness calibrates a
regime's loop on its MEDIAN subject and caps a trial at 20 s, so a 16 KB
run beside a 36 B median would put every length-proportional pattern's
match trial on the cap; and whole-subject match on a 16 KB digit run is
exactly the catastrophic near-miss for `nest2-64` (max 4096) that the runs
above are sized to avoid, whereas find-all search has no end anchor and
takes the greedy maximum at once — 4 matches of `nest2-64`, 1024 of
`nest2-4`, every one the counter run to its top.

## The floor pattern

`patterns/floor.rx` is the one-byte literal `:`, `role = "floor"` in the
sidecar (schema v1.3; the rule for every short-subject set since [B15]). It
runs over the SAME subjects the members do, in all three regimes.

`:` is in every prefixed line's timestamp at offset 9 (`l-02` … `l-07`:
search m/n 6/46, first-match span [9,10) on all six), and NOWHERE ELSE in
this set: the two whole ctx lines carry no prefix, no field contains one,
no run does. So the floor's search number on 40 of the 46 subjects is a
memchr-class MISS over 1-258 bytes, its match number is a miss on all 49,
and its throughput number is a full-subject miss on the 5 runs. That is a
different floor from `bench/loglines`'s (a hit within 30 bytes on 112/112)
and it is stated so the reader reads it right: here the floor is dispatch
plus a short memchr, and a member's per-call number read net of it is the
member's own work on a subject the floor scanned once. What it is NOT: a
cross-engine ranking. Each engine's floor is its own dispatch cost.

## Give-ups and refusals are results

Requirements §4.4 and schema v1.1: a compile refusal is `did-not-compile`
with the engine's diagnostic, a match-time budget refusal is `gave-up` with
the engine's code, neither is timed, both are excluded from rankings and
listed. This set is built so that (a) the pcrec size-cap refusals on the
class ladder's top rungs are the EXPECTED, cheap outcome of those cells —
the harness writes the compile rows and moves on — and (b) NO match-time
give-up is expected on any testee: every subject is sized below the point
where the oracle itself gave up, and pcrec's step budget (500,000,000,
`limits.md` §3.1) is two orders above the largest decomposition count here.
An observed match-time give-up is therefore a finding, with the subject
named.

## Per-engine notes

- **libpcre2 (`pcre2-interp`, `pcre2-jit`)** — none needed for the
  patterns: libpcre2 is the oracle and runs the canonical text under the
  canonical semantics by construction; every pattern in the set compiles on
  it by construction (`oracle_limits.tsv` is where its own ceilings are).
  Two things a reader should expect, both from PCRE2's own behaviour and
  neither a measurement of this set: a repeated GROUP is compiled by
  replication (per `oracle_limits.tsv`, `grp-upto` at 2048 and `nest2` at
  4096 exceed its compiled-size ceiling), so its compile cost and size on
  `grp-upto-1024`, `nest2-64` and `nest3-16` grow with the count where a
  repeated class's do not; and PCRE2's match limit (the oracle's `-47`) is
  the give-up a backtracking near-miss would produce — none is expected on
  the subjects here (above).
- **pcrec (`pcrec-auto`, `pcrec-nocaps`, `pcrec-vm`, the `-in` entries)** —
  `--features all` for the four `\b` patterns (above). The predictions are
  in "The ladder, the predicted first refusal" and are the reason the set
  has the rungs it has: two class-ladder REFUSALS by the emitted-size cap
  (`did-not-compile`, both forms), a DFA-overflow VM fallback on the `ctx-*`
  ladder's upper rungs stamped `RX_ENGINE_WHY`, and the nests as the
  `_UNROLL_K` candidates. Because pcrec compiles a `plain` and a
  `whole-subject` artifact per pattern, every refusal and every stamp
  appears twice per record, and the cell-time estimate counts 300 compiles
  per cell rather than 150. An `_in` (caller-provided frame buffer) entry
  has something to bind only on VM artifacts, i.e. the `ctx-*` fallbacks and
  whatever `auto` sends to the VM; on a pure-DFA cell the `-in` testees read
  nothing, as on the two earlier sets.
- **No engine note claims a measurement.** The only figures in this file
  are properties of the corpus, of PCRE2's compile-time analysis
  (re-derived by `make check`), of the oracle's compile ceilings (same), of
  design-time oracle probes (stated as such), and of pcrec's published
  contract (`docs/spec/limits.md`, cited by section).

## Cell-time estimate, and what was cut to get there

One cell = one testee × 43 patterns × three regimes, at `--trials 5`
(re-done in place for 0.3's thirteen patterns and nineteen subjects; "What
0.3 added"). The harness calibrates each (pattern, regime) loop so the MEDIAN
subject's loop is 50 ms and caps a trial's predicted sweep at 20 s
(`harness.py`), so a trial's sweep is 50 ms × Σᵢ(costᵢ / cost_median) —
≈ n × 50 ms when costs are uniform, and more when they are not.

**The floor, which is the term that dominates**: `patterns × slots × 50 ms ×
trials`, where `slots` is 49 match + 46 search + 5 throughput = 100. At
43 × 100 × 0.05 s × 5 that is **17.9 min** before any skew, against 0.2's
8.1 min (30 × 65). 0.2's measured cells ran 12-15 min against its 8.1 min
floor, a skew of ×1.5-1.85, all of it the length-proportional rows.

- `match`: 49 subjects, median still ~32-36 B (0.3 added ten subjects below
  it and nine above). Most patterns diverge within a few bytes → ≈ 2.5 s per
  trial; the length-proportional ones (`line-80`, the `cls-*` rungs on the
  256/257/512/1024 runs) ≈ 5-6 s (Σ bytes / median ≈ 110 on the worst,
  `line-80`, which matches every run whole). → ≈ **110-140 s per trial**.
  Two hazard rows on BACKTRACKING testees are still the exception, and are
  the SAME two: `nest2-letters-6` (seven near-misses at ≈ 1.7 ms now, was
  three) and `nest3-3` (six at ≈ 3 ms, was two) predict the 20 s cap →
  **+ 2 × 20 s** on `pcre2-*` and `pcrec-vm`, not on `pcrec-auto`. More
  near-miss subjects do not cost more once a row is capped.
- `search_short`: 46 subjects, none over 258 B; a failing search scans the
  subject, so the mostly-failing everyday shapes cost up to Σ/median ≈ 90 ×
  50 ms ≈ 4.5 s while the `{0,n}` rungs match at 0 and cost ≈ 2.3 s →
  ≈ **130 s per trial**.
- `throughput`: unchanged — 5 runs, median 16 KB, Σ/median ≈ 6.5 → ≈ 0.33 s
  per pattern → **≈ 14 s per trial** at 43 patterns.
- compile, pcrec only: 43 patterns × 2 forms × 5 trials = 430 emits (was
  300). The thirteen new patterns are all tiny counts whose artifacts are
  cheap for gcc; the unknown is unchanged and is the two large nests under
  body replication. → **1.5-8 min**, still dominated by `nest2-64` /
  `nest3-16`.

**≈ 30-36 min for a pcrec-auto cell before compile (32-44 with it), ≈ 33-40
min for a pcre2 or pcrec-vm cell** (the two cap-hitting hazard rows are
3.3 of those minutes). At `--trials 3`: **≈ 19-27 min**. Six testees:
≈ 3.2-4.5 h at trials 5, ≈ 1.9-2.7 h at trials 3.

**That is ≈ 1.5× a `bounded@0.2` cell, and the levers, in order.** (1)
`--trials 3` — ≈ 0.6×, and the v1.4 spread rule wants N ≥ 5 odd, so this
costs the trial-agreement verdict and is a manager's call, not a default.
(2) `--regimes match` — 49 of the 100 slots, ≈ 16-20 min a cell at trials 5,
and it is the WHOLE of the STEP 2 instrument and most of the short-run
family's; the search band is the one axis I-29 (iv) predicts will not move.
(3) The pattern count, then the subject count, as in 0.2.

**What 0.3 cost, and what was NOT spent.** The thirteen patterns are 4.6 min
of the floor and the nineteen subjects are 5.2 min of it; the long runs add
≈ 2.5 s per trial to a length-proportional pattern, ≈ 3.4 min a cell, which
is the price of having any long-subject match cell at all. What was declined:
a 2048 B and a 4096 B letters run (another ≈ 3 min a cell for one more octave
of a sweep that already spans 4 B to 1024 B — and 4097 digits is the
catastrophic near-miss, so the digit axis could not follow); three separate
arm subjects per short-run rung (thirty subjects where the shared length
ladder costs ten); and a fourth regime (which would have bought a separate
calibration pool the estimate above shows is not needed).

**What was cut to get here** (the first cut was 30 patterns × 43 short
subjects to 16 KB, estimated at 20-25 min because the 4 KB / 16 KB runs in
`match` put 13 patterns' trials on the 20 s cap): the large runs moved to
the `throughput` regime (above); `mac6` (a second nested-group-with-literal-
separator shape beside `dotted4`) and its two fields; three shape-free
background lines and three fields (`f-year-5`, `f-hex-32g` — a 31-hex-then-
`g` near-miss on a wrong byte, whose cost is `f-hex-31`'s — and the runs at
16 / 17 / 255); the lines held to ≤ 256 B (they were 43-999 B, which alone
made the search band's Σ/median ≈ 150); and five ladder rungs —
`cls-upto-16` (the 256 rung is the small end), `grp-upto-256` (1024 stands
alone; growth on the group body is readable from the 1024 rung against the
class rung at the same count), `cls-exact-256` and `cls-exact-16384` (the
exact `{n}` form; `hex32` and `year4` are exact counts with near-misses at
small n, and the 16384 exact rung's only work was one throughput match),
and `nest2-16` (the middle of the nest ladder; 4 and 64 bracket it). The
one structural fix this author would recommend over further cuts is
SPLITTING the two axes into two sub-benches — the everyday shapes over
fields and lines, the ladder over runs — because in one directory every
ladder rung is timed over every field (`[a-z]{0,65535}` against `2005`, 13
× 13 rungs × 2 regimes × 5 trials × 50 ms ≈ 1.4 min of every cell measuring
dispatch) and every everyday shape over every run; that is a scope change
for the manager, not for this lane.

## Origin

Nothing here is copied. The patterns were authored from the GOAL — plan row
[B11.4]'s three numbers, inbox I-14 (iii)/(iv), I-15 (c) and I-17 (c) — by
an author working under the [B11.4] blinding: pcrec's `docs/spec/` was read
(the module roster, the `--features` gate, and `limits.md` for the
published caps every prediction above cites), and pcrec's `tests/`, `src/`
and corpora, this repo's `testees/`, `store/` and `reports/` were NOT. The
one pattern text the brief itself quotes, `[a-z]{0,30000}` ([ENG-COUNT]),
is not in the set: the ladder brackets it (16384 / 32768) rather than
repeating it. That is pcrec's D27 lesson applied to a bench: tests derived
from the code inherit the code author's blind spots, and this sub-bench's
job is to find one.

**0.2 and 0.3 are not blinded, and say so.** Both extend a set whose first
samples are measured, against ledgers that are committed. 0.3's rungs and
run lengths are chosen from `docs/dev/ledgers/2026-08-31-opt5-step1-
acceptance-a7e0bdf.md`, from `docs/dev/measurements/2026-09-01-hybrid-gained-
edge-census.md` and from the `RX_DFA_MATCH` census in "What 0.3 added" — all
of them readings of THIS bench's own records, none of them pcrec source. The
blinding that mattered was of the set's SHAPE, and that shape is 0.1's,
unchanged.
