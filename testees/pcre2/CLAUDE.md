# testees/pcre2/ — the libpcre2 adapter

Provides three testees:

| config id | execution model | automaton_class | compile phases |
|---|---|---|---|
| `pcre2-interp` | `interpretive` | `backtracking` | `compile` |
| `pcre2-jit` | `eager-jit` | `backtracking` | `compile`, `jit-compile` |
| `pcre2-dfa` | `interpretive` | `nfa-simulation` | `compile` |

| file | role |
|---|---|
| `adapter.py` | `describe`/`prepare`/`compile`/`measure`; the engine-metadata DECLARATION |
| `driver.c` | the batched in-process timing driver (the protocol is in `pcrecbench/adapters.py`) |
| `configs.toml` | the two config ids; **no version is written here** |

## Why dlopen and hand-declared prototypes

This box has the PCRE2 8-bit RUNTIME (`libpcre2-8.so.0`) but not the `-dev`
package: no `pcre2.h`, no unversioned `.so`, no pkg-config file. The
precedent is pcrec's `tests/fuzz/pcre2_abi.h` and the email specimen's
`pcre2_throughput.c`. Every function is read off the library's exported
symbols; every constant that is not a symbol — the anchoring bits, the
`pcre2_pattern_info` codes, `PCRE2_CONFIG_VERSION` — carries a `[measured]`
note in `driver.c` saying how its value was established by probing.

## The compile-cost definition

- **`pcre2-interp`** — one phase: `pcre2_compile_8`, timed in-driver.
- **`pcre2-jit`** — two: that call, then
  `pcre2_jit_compile_8(PCRE2_JIT_COMPLETE)`. An eager JIT has a separable
  call, so there is a number to take. `warmup_trials` is 0: nothing warms
  after the compile. (A LAZY JIT is the one whose cost is "trial 1 minus
  steady state" — pcre2's is not one, and modelling it as one would put a
  fabricated number on the compile axis.)

## `consumed_length`: the convention, stated plainly

**`consumed_length` is the subject length the driver passed and pcre2
accepted — i.e. the whole subject.** `pcre2_match` takes a `size_t` length,
has no subject-size ceiling to truncate against, and exposes no scan
high-water mark. So the honest claim behind a `truncation_check = verified`
row is *"no byte was withheld or refused"*, never *"the engine looked at
every byte"*. Anyone comparing a throughput number against an engine that
DOES report a scan position should read this paragraph first.

## Engine metadata

Three structured facts, all from `pcre2_pattern_info_8`, all declared in
`adapter.py` before use (record_schema.md §7 rule 1):
`capturecount`, `compiled_size_bytes` (requirements §4.2's "program size" for
this engine) and `jit_size_bytes` (jit testee only — an ABSENT pair is not an
error; an UNDECLARED one is).

## `pcre2-dfa` ([B42] L6a, 2026-09-16) — the DFA-match testee

A THIRD execution model on the SAME library, SAME version, SAME `driver.c`
file: `pcre2_dfa_match_8` instead of `pcre2_match_8`, chosen by `--dfa` at
MATCH time only (`pcre2_compile_8` does not know or care which matcher will
run — capability_set_v1.md §8: "no new dependency, no new build machinery,
no new driver"). This box now has `libpcre2-dev` installed (a side finding
of `docs/dev/research/2026-09-12-b42-engine-landscape.md` (3), unactioned
there — the "Why dlopen" note above still applies to the two ORIGINAL
testees for consistency and because the box that first wrote it did not
have the header; every constant this section adds was independently
VERIFIED against `/usr/include/pcre2.h` in addition to being reproduced
live, one step stronger than that note's own "[measured]" discipline).

### The semantics, precisely (man `pcre2matching`, PCRE2 10.46, quoted where
it matters — the full text is in `docs/dev/research/2026-09-12-b42-engine-
landscape.md` (3))

- **A different algorithm, not a dial.** `pcre2_match` is a depth-first
  backtracking search (an "NFA algorithm" in Friedl's terms);
  `pcre2_dfa_match` is a breadth-first scan that "keeps multiple states
  active simultaneously" — in the engine's own words, "it is not
  implemented as a traditional finite state machine". `automaton_class` is
  therefore `nfa-simulation`, never `dfa-only` (capability_set_v1.md §8;
  the C function's NAME is not evidence of its algorithm).
- **The real semantic difference (§5.6's own callout): LONGEST match, not
  FIRST alternative.** At one (leftmost) starting point, `pcre2_dfa_match`
  finds and returns EVERY possible match, longest first; this driver reads
  only the first (longest). `pcre2_match` returns the first one its
  depth-first, leftmost-first search reaches. When a pattern has only one
  possible answer at a point, the two agree (the common case, and every
  smoke pattern in this repo but the ones built to demonstrate the
  divergence). When it does not — an alternation where one branch is a
  prefix of another, or a repeat whose possessiveness the DFA route
  ignores (item 1 below) — they can differ. `conventions` is still
  declared `["perl-leftmost-first"]` ("at the API shape the driver uses" —
  §5.6), because no second token exists for "leftmost-start,
  longest-at-that-point"; the divergence is stated here, in prose, not
  invented as a schema value.
  **CONFIRMED on this project's own corpus** (`pcre2test -dfa` vs plain,
  reproduced by `tools/selfcheck.py check_pcre2_dfa` through the REAL
  driver/adapter): `\.tar|\.tar\.gz` over `archive.tar.gz` — NFA `[7,11)`
  (`.tar`), DFA `[7,14)` (`.tar.gz`); `in|instanceof` over `instanceof` —
  NFA `[0,2)` (`in`), DFA `[0,10)` (`instanceof`); `/user|/users` over
  `/users` — NFA `[0,5)` (`/user`), DFA `[0,6)` (`/users`). CONFIRMED
  UNCHANGED on `foo|bar`-shaped controls and `(a|)*\d`-shaped ones (the
  auto-possessification edge case, below) — see "family 11" below for the
  full census against `bench/capability`'s own semantics-divergence
  patterns.
- **No captures, structurally, ever** (man item 2: "no captured
  substrings are available" — "dealing with multiple paths through the
  tree simultaneously, it is not straightforward to keep track of
  captured substrings"). `captures = "off"` in `configs.toml`; the driver
  forces `npairs = 0` immediately after every DFA match (never reads
  `rc` as a capture-pair count — `rc` is the SIMULTANEOUS-match count, a
  different number) and prints the CAPS column as `-` (parses back to
  `None`, the same value every OTHER testee's "no captures" row carries)
  regardless of `pcre2_pattern_info_8(PCRE2_INFO_CAPTURECOUNT)`, which
  still reports the pattern's LEXICAL group count as a structural,
  compile-time fact (`engine_metadata.capturecount`, unchanged — it says
  what the pattern COULD capture under a different matcher, never that
  this one did).
- **No JIT** (man `pcre2jit`: "It does not apply when the DFA matching
  function is being used"). The driver REFUSES `--dfa --jit` together, by
  name, rather than silently ignoring one flag.
- **No separate compile step** — `pcre2_dfa_match` reuses the exact same
  `pcre2_compile_8` artifact `pcre2_match` would use. `compile_phases =
  ["compile"]`, and `pcre2-dfa`'s compile-cost NUMBER should be
  statistically indistinguishable from `pcre2-interp`'s on the same
  pattern (capability_set_v1.md §8's own "a control this bench can check
  for free" — not asserted anywhere yet; a future reporter/interpreter
  rule's natural first customer).
- **STRUCTURAL refusals — a construct `pcre2_compile_8` cannot see, only
  discovered at MATCH time**, because the SAME compiled pattern serves
  every matcher. Man item 3(a)+item 4: backreferences and `\K` raise
  `PCRE2_ERROR_DFA_UITEM` (-42, "pattern contains an item that is not
  supported for DFA matching"); item 3(b): a conditional whose condition
  is a backreference or a specific-group-recursion test raises
  `PCRE2_ERROR_DFA_UCOND` (-40, "backreference condition or recursion
  test is not supported for DFA matching"); item 7: every backtracking
  control verb except `(*FAIL)` is the same shape (this vocabulary has no
  finer token for "FAIL only", so `control-verbs` is withheld wholesale
  for `pcre2-dfa`, below). LIVE TRANSCRIPTS (`pcre2test -dfa`, this box,
  2026-09-16):

      /(\1)(a)/                              /a\Kb/
      aa                                     ab
      Failed: error -42: pattern contains    Failed: error -42: pattern contains
      an item that is not supported for DFA  an item that is not supported for DFA
      matching                               matching

      /(?(1)a|b)(a)?/
      ba
      Failed: error -40: backreference condition or recursion test is not
      supported for DFA matching

  On the REAL, UNTAGGED corpus: `bench/syntax`'s own `bak-1` (`(\w+)
  \1`, no `requires-*` tag — it predates [B42]) refuses cleanly on its
  `f-dup` subject ("the the") and answers `nomatch` cleanly on every
  subject with no doubled word — the DFA scan only reaches the
  unsupported opcode when the earlier, supported part of the pattern
  actually matches; it does not refuse merely because the CONSTRUCT is
  present somewhere in the pattern text.
- **RESOURCE-shaped refusals**, the same SHAPE as `pcre2-match`'s
  MATCHLIMIT/DEPTHLIMIT/HEAPLIMIT above, never JIT_STACKLIMIT (no JIT
  exists on this route): `PCRE2_ERROR_DFA_WSSIZE` (-43, this driver's
  own caller-owned workspace, `driver.c`'s `PCRE2_DFA_WS_ELEMS`
  (100,000 ints), chosen against the project's own worst case —
  `bench/bounded`'s `cls-upto-65535` (`[a-z]{0,65535}`) matches cleanly
  under `pcre2test -dfa`'s own default workspace against a 70,000-byte
  all-matching subject in single-digit milliseconds; a real exhaustion
  is this code, never assumed impossible) and `PCRE2_ERROR_DFA_RECURSE`
  (-39, man: "extremely rare", the internal per-recursion ovector).

### THE STRUCTURAL-REFUSAL GAP, stated plainly (flagged for the schema owner)

`record_schema.md`'s `match_outcome` enum has no dedicated STRUCTURAL
value — only `matched-as-expected / did-not-match-as-expected /
wrong-span-or-captures / truncated-subject / crashed / timed-out /
gave-up`. `gave-up`'s own definition (requirements.md §4.4) is "the
engine's OWN resource limit", which is a stretch for DFA_UITEM/DFA_UCOND
(a permanent, subject-size-independent, structural incapability, not a
budget). `testees/pcre2/adapter.py`'s `GAVE_UP_CODES_DFA` buckets both
shapes there anyway, DELIBERATELY, because it is the LEAST WRONG of the
outcomes that already exist: `crashed` would claim an engine defect that
is not one, and a silent `nomatch` would be a wrong answer dressed as a
right one. `gave-up`'s own by-CODE distinguishability (`-42`/`-40` vs
`-47`/`-53`/`-63`/`-43`/`-39`) is what keeps a reader from conflating the
two shapes even though the schema does not. A per-subject
STRUCTURAL-refusal outcome is genuinely future schema work — the same
open list `docs/design/capability_set_v1.md` §5.4 already keeps for
other "adopt no new value, but note the seam" shapes — not routed around
quietly here. Where a set DECLARES the missing construct in advance
(`bench/capability`'s `ext bench` matrix, below), the PRE-COMPILE
capability policy (`docs/design/capability_set_v1.md` §5.3,
`pcrecbench/capability.py`) intercepts it first and the schema-legal
`unsupported-by-declaration` compile-row outcome is used instead — this
gap is therefore reached only by a set that authors NO `requires-*`
tags at all (every set but `bench/capability` today; `bench/syntax`'s
five untagged backreference/`\K`/control-verb/conditional/recursion
patterns are real, present witnesses of exactly this path, not a
hypothetical).

### The `ext bench` capability declaration (`bench/capability/gen_patterns.py`'s
`EXT_BENCH_ROSTER`, regenerated — never hand-edited — into `patterns.rxt`)

`pcre2-dfa` declares it satisfies every `REQUIRES` token EXCEPT:
`backrefs`, `conditionals`, `k-reset`, `control-verbs`, `captures` — each
witnessed live above. Every other token (`lookaround`,
`lookbehind-variable`, `possessive-quantifier`, `atomic-group`,
`recursion`, `unicode-properties`, `named-groups`, `free-spacing`,
`callouts`, `span-reporting`, `non-utf8-subject`, `true-end-anchor`) is
KEPT: the man page discusses lookaround, possessive quantifiers and
atomic groups as WORKING (just without capture reporting, already
handled by the separate `captures` exclusion); `\p{...}`, named groups
and free-spacing are compile-time / orthogonal to which matcher runs;
`callouts` are explicitly "supported" (item 5, with weaker
`capture_top`/`capture_last` fields this bench does not read);
`span-reporting` and `true-end-anchor` are this driver's own
`PCRE2_ANCHORED`/`PCRE2_ENDANCHORED` runtime options, which
`pcre2_dfa_match`'s own synopsis lists as accepted options identically
to `pcre2_match`'s. `recursion` is kept DESPITE `DFA_RECURSE` existing,
because that code is resource-shaped ("extremely rare" internal-ovector
exhaustion), not a structural "recursion does not work" refusal — the
construct itself runs via the same internal recursive call `pcre2_match`
uses.

### Family 11 (`semantics-divergence`) — the census this lane ran before
touching the roster (capability_set_v1.md §5.6's own precondition:
"`pcre2-dfa` ... once its decreasing-length-order difference below is
confirmed not to change the answer on family 11's own cases")

All six `bench/capability` `semantics-divergence` patterns, checked
against `pcre2-dfa` with `pcre2test -dfa` (this box, 2026-09-16),
cross-referenced against the set's own `expectations.tsv`:

| pattern | divergence exists? | evidence |
|---|---|---|
| `file-ext-order` (`\.tar\|\.tar\.gz`) | **YES**, and IT FIRES on this corpus: the set's only `match` expectation for this pattern is `sd-fileext-short` (`archive.tar.gz`), oracle-derived under NFA as `[7,11)` — DFA answers `[7,14)`, a real, would-be `wrong-span-or-captures` if scored against that row |
| `keyword-prefix-order` (`in\|instanceof`) | **YES on ONE subject**: `sd-keyword-short` (the literal text `instanceof`) diverges `[0,2)` vs `[0,10)`; the other three `match` subjects (`waf-dbnames`, `br-quoted-delim`, `rec-comment-nested`) and the three `throughput` ones do NOT — "in" is the only alternative present at the matched position in every one of them |
| `router-prefix-order` (`/user\|/users`) | **YES on ONE subject**: `sd-router-short` (`/users`) diverges `[0,5)` vs `[0,6)`; not checked exhaustively on the three `throughput` subjects (out of scope for this lane; flagged below) |
| `wild-semdiv-altorder-foo-foobar-rustregex` (`foo\|foobar`) | mechanism confirmed (`foo` vs `foobar` over `foobar` diverges `[0,3)`/`[0,6)`, live), but **MOOT on this corpus**: every one of its 78 `expectations.tsv` rows is `nomatch` — neither literal substring appears in any committed subject |
| `wild-semdiv-dollar-trailing-newline-pcre2` (`abc$`) | **NO divergence, confirmed**: `abc`, `abc\n` and `abc\ndef` answer identically under both matchers (the `$`/newline convention is a compile-time NEWLINE setting, orthogonal to which matcher scans) — consistent with the corpus's own 78/78 `nomatch` rows |
| `wild-semdiv-empty-alt-repeat-pcre2` (`(a\|)*\d`) | **NO divergence, confirmed structurally AND empirically**: at any one start offset this pattern has exactly ONE valid total match length (the group's repeat can only stop where a digit immediately follows; a shorter stop always hits another `a`, not a digit — no ambiguity for the DFA route to resolve differently), checked on `v-ipv4`, the `sd-empty-alt-hit`/`sd-empty-alt-miss` stress pair (60 `a`s +/- a trailing digit) and both are answer-identical between matchers |

**Consequence, stated for the manager rather than worked around:** three
of six family-11 patterns have at least one (pattern, subject) cell where
`pcre2-dfa`'s CORRECT, DOCUMENTED answer differs from the NFA-oracled
`expectations.tsv` row — `file-ext-order`/`sd-fileext-short`,
`keyword-prefix-order`/`sd-keyword-short`,
`router-prefix-order`/`sd-router-short` (three cells today; the two
`router-prefix-order` throughput subjects are UNCHECKED, an honest gap).
`harness.outcome_for`'s `convention` parameter (R5 B1/CB1) exists for
exactly this shape but is a documented no-op until a real `under
<convention>`-qualified expectation row exists (none does, on any set,
at this pin) — this lane does NOT build that (out of scope: a
harness/schema-adjacent change, not a testee adapter's call to make
unilaterally). **A `quick`/`run` cell measuring `pcre2-dfa` against
`bench/capability`'s `file-ext-order`/`keyword-prefix-order`/
`router-prefix-order` patterns WILL show `wrong-span-or-captures` on
these three named cells — this is EXPECTED, DOCUMENTED, and NOT a
`pcre2-dfa` defect**, not a silent surprise for whoever reads that
report first. Closing it needs the convention-scoring machinery
`capability_set_v1.md` §5.6 already scopes to a later lane.

### `--find-all` (throughput regime)

Uses the SAME advance rule as every other testee (`ov[0]`/`ov[1]` of the
LONGEST match at each start point; `pos = end if end > start else
start + 1`) — the non-overlapping match COUNT can still differ from
`pcre2-interp`'s on a pattern with a real alternation-order divergence
(confirmed on `in|instanceof` over a synthetic multi-occurrence subject:
same COUNT, 5, because every occurrence in that witness has only one
alternative present — the divergence changes WHICH span is reported, not
whether a match exists at that position). `bench/loglines`'s own ten
patterns and `bench/capability`'s throughput subjects are unchecked for
a genuine count divergence; none is known, none is ruled out.

### Workspace and ovector sizing (`driver.c`)

`PCRE2_DFA_WS_ELEMS` (100,000 `int`s, malloc'd once) and a 16-pair
`pcre2_match_data_create_8` block (never
`pcre2_match_data_create_from_pattern_8` — man `pcre2_dfa_match`: sizing
from the pattern's capture count "is therefore not advisable" for DFA).
16 pairs is generous headroom, not a tight fit: man `pcre2_dfa_match`'s
own "Successful returns" section states the ovector's first pair is
ALWAYS the longest match regardless of how many simultaneous matches
were found or whether the vector could hold them all ("stored ... in
reverse order of length ... the longest matching string is first ...
If there were too many matches to fit ... the vector is filled with the
longest matches") — this driver never reads past `ov[0]`/`ov[1]`, so
even `oveccount=1` would be correct; the headroom costs nothing.
