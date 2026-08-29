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
| `year4` | `\d{4}` | a fixed-width digit field; the near-miss is 3 digits | 1/30 · 13/30 · 1/4 |
| `hex32` | `[0-9a-f]{32}` | a 32-hex id; the near-miss is 31 hex (fails at the 32nd repetition) | 1/30 · 4/30 · 1/4 |
| `pw-8-64` | `.{8,64}` | a password length rule; 7 bytes fails at the 8th repetition, 65 fails at `\z` after 64 | 16/30 · 27/30 · 4/4 |
| `line-80` | `.{80,}` | a line-length rule: an OPEN count; the everyday `{n,}` | 10/30 · 10/30 · 4/4 |
| `dotted4` | `(?:\d{1,3}\.){3}\d{1,3}` | nested counts with a literal separator: unambiguous; three octets fails inside the 3rd group repetition, a 4-digit last octet fails at `\z` | 1/30 · 4/30 · 0/4 |
| `csv5` | `(?:[^,\n]{0,32},){4}[^,\n]{0,32}` | a five-field record: a bounded negated class under a bounded group; four fields fails at the 4th comma | 1/30 · 3/30 · 0/4 |
| `ctx-lazy-64` | `\b(?:fail\|abort\|panic)\b.{0,64}?\b(?:disk\|memory\|socket\|quota)\b` | the bounded-context shape, rung 64 | 1/30 · 1/30 · 0/4 |
| `ctx-lazy-256` | … `.{0,256}?` … | rung 256 — one rung above the count the loglines witness overflowed pcrec's DFA at | 2/30 · 3/30 · 0/4 |
| `ctx-lazy-1024` | … `.{0,1024}?` … | rung 1024 | 2/30 · 3/30 · 0/4 |
| `ctx-greedy-256` | … `.{0,256}` … | the greedy twin of rung 256: same language, same count, greedy gap — separates "lazy" from "a bounded gap before a `\b` alternation" as the cause | 2/30 · 3/30 · 0/4 |

The four `ctx-*` patterns are a count ladder of their own, on the MATCH-axis
shape. `pattern_facts.tsv` says what PCRE2's analysis makes of them: NO
required code unit (the alternation's branches end in different bytes),
exactly as `bench/loglines`'s `level-context` — so no required-byte
precheck helps them and every engine scans.

### The count ladder (the compile axis)

| pattern | text | rung / product | what it isolates | m/n |
|---|---|---|---|---|
| `cls-upto-256` | `[a-z]{0,256}` | 256 | the class-body `{0,n}` skeleton — [ENG-COUNT]'s shape — at its small end | 3/30 · 30/30 · 4/4 |
| `cls-upto-4096` | `[a-z]{0,4096}` | 4096 | ″ | 4/30 · 30/30 · 4/4 |
| `cls-upto-16384` | `[a-z]{0,16384}` | 16384 | ″ — predicted the LARGEST ACCEPTED artifact in the bench (below) | 4/30 · 30/30 · 4/4 |
| `cls-upto-32768` | `[a-z]{0,32768}` | 32768 | ″ — the predicted first REFUSAL for pcrec (below) | 4/30 · 30/30 · 4/4 |
| `cls-upto-65535` | `[a-z]{0,65535}` | 65535 | ″ at PCRE2's own count ceiling (`{0,65536}` is refused by the oracle) | 4/30 · 30/30 · 4/4 |
| `cls-atleast-4096` | `[a-z]{4096,}` | 4096 / open | the OPEN count: 4096 mandatory repetitions then a loop — the control with no upper bound to unroll | 0/30 · 0/30 · 3/4 |
| `cls-lazy-16384` | `[a-z]{0,16384}?` | 16384 | the lazy twin of the 16384 rung (greedy vs lazy at a large count) | 4/30 · 30/30 · 4/4 |
| `grp-upto-1024` | `(?:a\|[b-z]){0,1024}` | 1024 | the GROUP body, same language as `[a-z]{0,1024}`: a DFA sees a class, a body-replicating compiler sees a group, PCRE2 replicates it per count (its last accepted octave: 2048 is refused, `oracle_limits.tsv`) | 4/30 · 30/30 · 4/4 |
| `nest2-4` | `(?:\d{1,4}){1,4}` | 4 / 16 | two-deep nest, small: 17 digits is a near-miss the oracle finishes | 3/30 · 26/30 · 1/4 |
| `nest2-64` | `(?:\d{1,64}){1,64}` | 64 / 4096 | two-deep nest, large: the census's "nested bounded repeat" shape at product 4096 | 7/30 · 26/30 · 1/4 |
| `nest3-3` | `(?:(?:\d{1,3}){1,3}){1,3}` | 3 / 27 | three-deep nest, small: 28 digits is a near-miss the oracle finishes (≈ 3 ms on the interpreter) | 5/30 · 26/30 · 1/4 |
| `nest3-16` | `(?:(?:\d{1,16}){1,16}){1,16}` | 16 / 4096 | three-deep nest, large: product 4096 at depth 3 vs `nest2-64`'s at depth 2 | 7/30 · 26/30 · 1/4 |
| `nest2-letters-6` | `(?:[a-z]{1,6}){1,6}` | 6 / 36 | the ambiguous nest the MATCH axis pays for: every letter run over 36 is a near-miss a backtracker decomposes 7^6 ways (≈ 1.7 ms on the interpreter, measured on the oracle) while a DFA is linear | 1/30 · 20/30 · 3/4 |
| `floor` | `:` | — | the per-call floor control (below) | 0/30 · 6/30 · 0/4 |

**Why `{0,n}` in search reads 30/30.** An optional repeat matches the empty
string at offset 0 on every subject, so every `cls-upto-*`, `cls-lazy-*`
and `grp-upto-*` search cell is a match of length 0..n at 0 — the
expectation is honest and the number is dispatch plus the run's length.
The regimes where those rungs do work are `match` (the run must be the
whole subject: 256 letters match `{0,256}`, 257 fail at `\z`) and
`throughput` (find-all over a 4/16/64 KB run drives the counter to its full
value: `cls-upto-65535` on the 64 KB run is one match of 65535 bytes and a
1-byte remainder). `cls-lazy-16384` under find-all is 4097 / 16385 / 65537
EMPTY matches — the lazy quantifier's honest answer, and a per-call number.

**Everything nests non-capturing.** Every group in the set is `(?:…)`;
`gen_expectations.py` re-checks on every run that no capturing group
participated in any match and says so on stderr (shared code,
`pcrecbench/expectations.py`). The span is the whole observable answer.

**Declared variants: none.** All twenty-four patterns are canonical PCRE2
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
to within 2×. A refusal is recorded by the harness as `did-not-compile` with
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

## The subjects

`gen_subjects.py`, seed **20260829**; `gen_throughput_subjects.py`, seed
**20260830**. Both draw from `boundedtext.py`, whose only randomness
primitive is `random.Random(seed).getrandbits(32)` — `choice`, `sample`,
`randrange` and `shuffle` are avoided because their internals have moved
between CPython releases and a committed manifest cannot rest on that.

**Three families, 30 short subjects (3-257 B) + 4 large runs.** The
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
| RUNS `r-*`, `d-*` | 9 | 16-257 B | random letters at 36 / 37 (the `nest2-letters-6` exact maximum and its near-miss) and 256 / 257 (the 256 rung's exact maximum and its over-run); random digits at 16 / 17 (`nest2-4`), 27 / 28 (`nest3-3`) and 256 (`nest2-64`'s and `nest3-16`'s territory, below every large rung's maximum) |
| LARGE RUNS `t-*` | 4 | 4-64 KB | `throughput/`: letters at 4096, 16384, 65536 and digits at 16384 — the ladder's top rungs driven to their full count under find-all search (`gen_throughput_subjects.py` says why they live here) |

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

**Match rates by DESIGN.** The everyday shapes are injected into the lines
by exact allocation without replacement (`gen_subjects.COUNTS`), not by a
per-line coin flip — `bench/loglines`'s lesson at n = 112 applies with more
force at n = 8. The realised m/n per pattern is the oracle's
(`pattern_facts.tsv`), and the everyday shapes sit at 1/30 in `match` (the
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
| `match` | all 30 short | `PCRE2_ANCHORED\|PCRE2_ENDANCHORED` at 0 | 87 of 720 cells match |
| `search_short` | all 30 short (`short_search_max_bytes = 512`; every subject is ≤ 257 B) | unanchored at offset 0 | first-match span; 411 of 720 cells match, most of them the `{0,n}` rungs' empty-or-leading matches at 0 |
| `throughput` | the 4 large runs | unanchored, find-all | first span + count; 48 of 96 cells match |

`short_search_max_bytes = 512` — between `bench/email`'s 256 and
`bench/loglines`'s 4096: the LINES are held to ≤ 256 B by the generator
(requirements §3's "~256-byte subjects (log lines, fields)" for this
regime), and 512 rather than 256 only so the 257-byte over-run of the 256
rung is not dropped from the search band by one byte. The two short regimes
therefore see the same 30 subjects.

**The `throughput` regime is declared for the ladder's TOP RUNGS, not for a
size sweep** — a declaration, not an omission, and the opposite choice from
`bench/loglines`. This set's give-up axis is the COUNT in the pattern
(above); the subject size is not swept for its own sake, and the four large
runs sit on the ladder's rungs (4096 / 16384 / 65536) so `[a-z]{0,4096}`,
the 16384 rungs and `[a-z]{0,65535}` are each driven to their full count.
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
search m/n 6/30, first-match span [9,10) on all six), and NOWHERE ELSE in
this set: the two whole ctx lines carry no prefix, no field contains one,
no run does. So the floor's search number on 24 of the 30 subjects is a
memchr-class MISS over 3-257 bytes, its match number is a miss on all 30,
and its throughput number is a full-subject miss on the 4 runs. That is a
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
  appears twice per record, and the cell-time estimate counts 240 compiles
  per cell rather than 120. An `_in` (caller-provided frame buffer) entry
  has something to bind only on VM artifacts, i.e. the `ctx-*` fallbacks and
  whatever `auto` sends to the VM; on a pure-DFA cell the `-in` testees read
  nothing, as on the two earlier sets.
- **No engine note claims a measurement.** The only figures in this file
  are properties of the corpus, of PCRE2's compile-time analysis
  (re-derived by `make check`), of the oracle's compile ceilings (same), of
  design-time oracle probes (stated as such), and of pcrec's published
  contract (`docs/spec/limits.md`, cited by section).

## Cell-time estimate, and what was cut to get there

One cell = one testee × 24 patterns × three regimes, at `--trials 5`. The
harness calibrates each (pattern, regime) loop so the MEDIAN subject's loop
is 50 ms and caps a trial's predicted sweep at 20 s (`harness.py`), so a
trial's sweep is 50 ms × Σᵢ(costᵢ / cost_median) — ≈ n × 50 ms when costs
are uniform, and more when they are not.

- `match`: 30 subjects, median 32-36 B. Most patterns diverge within a few
  bytes on most subjects → ≈ 1.5 s per trial; the length-proportional ones
  (`line-80`, the `cls-*` rungs on the 256/257 runs) ≤ 3.8 s (Σ bytes /
  median ≈ 76). → ≈ 24 × ~2 s ≈ **48 s per trial**. Two hazard rows on
  BACKTRACKING testees are the exception: `nest2-letters-6` (three
  near-misses at ≈ 1.7 ms against a microsecond median) and `nest3-3` (two
  at ≈ 3 ms) predict the 20 s cap → **+ 2 × 20 s** on `pcre2-*` and
  `pcrec-vm`, not on `pcrec-auto`.
- `search_short`: 30 subjects; a failing search scans the subject, so the
  mostly-failing everyday shapes cost up to Σ/median ≈ 76 × 50 ms ≈ 3.8 s,
  while the `{0,n}` rungs match at 0 and cost ≈ 1.5 s → ≈ **60 s per trial**.
- `throughput`: 4 runs, median 16 KB → Σ/median ≈ 6.25 → ≈ 0.3 s per
  pattern → **≈ 8 s per trial** (`cls-lazy-16384`'s 65537 empty matches on
  the 64 KB run are ≈ 2 ms per iteration; inside that).
- compile, pcrec only: 24 patterns × 2 forms × 5 trials = 240 emits. The
  table artifacts are predicted cheap for gcc (the spec's 0.34 s for
  1.37 MB), the two predicted refusals cost only pcrec's own emit, and the
  unknown is the two large nests under body replication — 1-30 s of gcc
  each, × 10. → **1-6 min**, dominated by `nest2-64` / `nest3-16`.

**≈ 10 min for a pcrec-auto cell before compile (11-16 with it), ≈ 13 min
for a pcre2 or pcrec-vm cell** (the two cap-hitting hazard rows are 3 of
those minutes). At `--trials 3`: ≈ 6 / 8 min. The dominant term is
`n_subjects × 50 ms × patterns × regimes × trials` — 24 × 64 slots × 0.05 s
× 5 = 6.4 min as a FLOOR before any skew — so the levers are, in order,
`--trials`, the pattern count, and the subject count.

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
