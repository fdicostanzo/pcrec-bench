# testees/vectorscan/ — the Vectorscan adapter (BOOLEAN GRAIN)

Provides one testee: `vectorscan-block-nosom`. `vectorscan-block-som` is
documented below as a LATER config (capability_set_v1.md §8's own roster
row); this lane does not wire it.

Built [B7]/L6b wave 2 (`capability_set_v1.md` §11.1's per-engine lane
row), lane `l6bvs`, 2026-09-17. Vectorscan (the actively-maintained,
Hyperscan-ABI-compatible fork) 5.4.11-2ubuntu2, `libvectorscan-dev`
(`scripts/install_l6b_deps.sh` verified it installed, and verified
`libhyperscan-dev` — its CONFLICTING sibling package — is NOT installed,
before this lane started); `/usr/include/hs/*.h`, `pkg-config libhs`.

| file | role |
|---|---|
| `adapter.py` | `describe`/`prepare`/`compile`/`measure`; the engine-metadata DECLARATION (`min_width`, `max_width`, `unordered_matches`, `matches_at_eod`, `matches_only_at_eod`, `compiled_size_bytes`); the (empty) `GAVE_UP_CODES` set |
| `driver.c` | the batched in-process timing driver (the protocol is in `pcrecbench/adapters.py`); direct-linked against `libhs.so.5` (`#include <hs/hs.h>`, `-lhs`) |
| `configs.toml` | the one config id, `vectorscan-block-nosom` |
| `_probe.rx` | one byte, `a` — the version-probe pattern (`testees/pcre2/_probe.rx`'s own convention) |

## THE GOVERNING RULING: BOOLEAN GRAIN (Frank, Q3, 2026-09-16)

`docs/design/capability_set_v1.md` §5.6 states three options for
Hyperscan/Vectorscan's "all-ends" semantics, which genuinely does not fit
this bench's `--find-all` non-overlapping-count protocol or its
leftmost-first span convention. Frank ruled **option (B): boolean
grain** — this testee is measured ONLY on whether a pattern matches a
subject at all, plus compile/refusal comparisons, never a span or a
non-overlapping match count. This is a real, explicit relaxation of
`requirements.md` §4.5 constraint 1 ("no variation in results... no
'approximates with stated differences' grade") for ONE engine, and it
must stay visible in every report row, not become a silent footnote —
this file, `driver.c`'s header, and `adapter.py`'s module docstring all
state it plainly for that reason.

### What "correct" means at boolean grain, precisely

A subject the pattern genuinely does NOT match: `row.matched = False`,
scored normally against `expectation.matched = False` — these cells
work exactly like any other testee's and land on `matched-as-expected`.

A subject the pattern genuinely DOES match: this driver reports
`answer = "match"` with **`start = end = None`** (printed `-,-` on the
wire, per the driver protocol's own stated degenerate shape, "START,END
the FIRST match's span, **or `-`**" — `pcrecbench/adapters.py`'s own
comment). It NEVER reports a real end offset, even though Hyperscan's
match callback hands this driver one on every call: printing a real END
while START stays `-` would be a half-measure the protocol comment does
not describe, and it would STILL fail the harness's span comparison on
any pattern whose end offset is not the very first byte after the
match's start — no more honest than `-`, and less honest about what a
`nosom` config actually knows (§5.6's own text: "measure Vectorscan only
where the canonical expectation is 'does this match anywhere'").

**THE FINDING (measured, not merely predicted): `harness.outcome_for`
has NO boolean-grain accommodation today.** Its span check
(`pcrecbench/harness.py`):

```python
if row.matched and (row.start != expectation.start
                    or row.end != expectation.end):
    return ("wrong-span-or-captures", ...)
```

fires unconditionally whenever `row.matched` is true, comparing `None`
against the oracle's real integer span. Reproduced directly against the
real `harness.outcome_for` function (not merely read from the source),
this lane's own committed proof:

```
TRUE MATCH row scored:   wrong-span-or-captures -- expected span [6,9]; observed [None,None]
TRUE NOMATCH row scored: matched-as-expected -- None
```

**Consequence, stated for the manager rather than routed around: every
subject this testee genuinely MATCHES will score `wrong-span-or-
captures` in every report and every `quick`/`run` cell — never
`matched-as-expected` — while every subject it correctly does NOT match
scores normally.** This is the SAME shape `testees/pcre2/CLAUDE.md`'s
own "pcre2-dfa" family-11 divergence table and its "THE STRUCTURAL-
REFUSAL GAP" section describe for a testee whose correct, documented
answer the current harness's own comparison marks wrong — EXPECTED,
DOCUMENTED, and NOT a defect in this adapter. It is a real gap in the
CURRENT harness that an adapter lane cannot close unilaterally: the fix
would be a `grain` (or similar) declaration on `testee`/`Adapter`, the
same shape `convention` already has (R5 B1/CB1, `harness.outcome_for`'s
own `convention` parameter, added for exactly this "a real answer scored
against the wrong yardstick" shape), read by `outcome_for` to skip the
span/capture comparison for a testee that declares it structurally never
produces one. **Filed as a finding for the manager/outbox, not built
here** — a harness change needs a ruling, the same posture pcre2-dfa's
own "structural-refusal gap" section states for its own schema-adjacent
finding.

**A reader who wants a genuinely correct-vs-wrong verdict for this
testee today** must read the `did-not-match-as-expected` count (real
false positives/negatives — this testee CAN produce those, on a subject
whose boolean answer it gets wrong) separately from the `wrong-span-or-
captures` count (which, for THIS testee only, means "matched, and we
cannot say more" rather than "matched at the wrong place") — a caveat
worth restating in any report or ledger that ranks this testee, the same
way `reports/CLAUDE.md` already carries a reader's caveat for the
"8192 inversion" cross-pin mis-reading.

**ESCALATION — MEASURED, not merely a scoring nuance: a matching cell
does not even VALIDATE, let alone rank wrong.** Reproduced end to end
through the real harness (`pcrecbench quick --subbench email --pattern
orig --regime search_short --testee vectorscan-block-nosom --subjects
5`, this lane, 2026-09-17): the `wrong-span-or-captures` branch's
`observed = {"matched": True, "span": [row.start, row.end], ...}`
constructs `span: [None, None]` whenever this testee reports a match —
an ARRAY, never `None` as a whole. `schema/record.schema.json`'s own
`span` definition allows the WHOLE field to be `null`, but an array
value's two ITEMS must each be `{"type": "integer", "minimum": 0}` — no
`null` item is schema-legal. The result, verbatim from the real run:

```
pcrecbench quick: the record FAILED validation and was NOT written to the store -- this is a harness bug, not a measurement result (harness contract 4 step 5).
validate.py: observed.span.0: None is not of type 'integer' [SCHEMA]
validate.py: observed.span.1: None is not of type 'integer' [SCHEMA]
```

**Consequence, stated plainly: `vectorscan-block-nosom` cannot produce a
schema-valid record for ANY cell that contains at least one subject the
pattern genuinely matches, on ANY set, at ANY tier — pinned or scratch —
today.** A cell whose every subject is a true NOMATCH writes fine (the
span/observed machinery is never reached — see "TRUE NOMATCH row
scored" above); this bench/email `orig`/`search_short` cell, which
matches on real email subjects, does not. This is the concrete,
load-bearing form of the brief's own question ("if the protocol has no
such representation, that is a FINDING"): the driver protocol's
degenerate `-` DOES have a representation on the WIRE (the TSV column),
but `harness.outcome_for`'s `wrong-span-or-captures` branch has no path
that turns "matched, no span known" into a record the schema accepts —
it always builds a two-element span array, never the bare `null` the
schema would accept for "no span at all". **Closing this needs, at
minimum, the SAME `grain`-declaration harness change "THE FINDING" above
already asks for**: a boolean-grain testee's match rows need a code path
that returns `matched-as-expected` (or some new outcome) with
`observed.span = null` rather than attempting `wrong-span-or-captures`'s
two-integer array at all. **Filed as the single most consequential
finding of this lane** — not routed around, not worked around with a
schema-violating write, and not something this adapter lane can fix
unilaterally (the fix lives in `pcrecbench/harness.py` and/or
`schema/record.schema.json`, shared infrastructure this lane was told
not to touch while pcrec's battery owns the box, and a schema/harness
change needs a ruling regardless of the box).

### `NMATCHES` (throughput regime): also unavailable, also honest

pcrec match_api.md S3.1's non-overlapping-match COUNT (KB-17's advance
rule) needs each match's START offset to de-duplicate correctly — that
is exactly what `HS_FLAG_SOM_LEFTMOST` supplies, and this `nosom` config
does not carry it by construction. `docs/dev/research/2026-09-12-b42-
engine-landscape.md`'s own §11 gap states this precisely: "Hyperscan's
natural one-pass 'all ends' callback does not produce that count on its
own" and describes an adapter-side reduction as the fix. **This lane
does NOT build that reduction** — `driver.c` accepts `--find-all` for
protocol compliance but always prints `NMATCHES = -`, honestly, rather
than a raw Hyperscan match-callback count that is NOT the same quantity
every other engine's `NMATCHES` column reports (a raw count double-counts
every overlapping start point a non-overlapping rule would collapse).
OWED, named in the lane report.

## (a) The compile-cost definition

**One phase, `compile`** — `hs_compile()`, timed in-driver.
`execution_model = "eager-jit"` (`docs/dev/research/2026-09-12-b42-
engine-landscape.md`'s own recommendation: "the closest existing token:
one explicit, timeable call that produces a ready-to-run artifact" —
Vectorscan's own compiled DATABASE, not machine code via a real
compiler+linker, but the closest class this schema has short of pcrec's
own AOT phases). `compile_phases = ["compile"]`, `warmup_trials = 0`
(the research note's own characterization: "explicitly documented as the
heavyweight, famously-slow-relative-to-match-speed step... a huge
compile-time investment for fast scanning" — an EAGER cost, not a lazy
one that needs a warm-up convention).

**Scratch allocation (`hs_alloc_scratch`) happens ONCE, immediately
after the LAST compile trial, UNTIMED** — the brief's own instruction,
matching this project's convention that driver setup around an engine's
own semantic compile call is never charged to that call's number
(mirrors pcre2/onig's convention of timing only `pcre2_compile_8`/
`onig_new`, never the surrounding driver bookkeeping). A scratch
allocation failure `die()`s loudly (a driver-level defect, not a
per-pattern compile outcome) rather than being folded into
`did-not-compile`.

## (b) `consumed_length`: the convention, stated plainly

**`consumed_length` is the subject length the driver passed and
`hs_scan()` accepted — i.e. the whole subject.** `hs_scan()` takes an
explicit `unsigned int length` with no subject-size ceiling to truncate
against, and exposes no scan high-water mark — the SAME honest claim
`testees/pcre2/CLAUDE.md` and `testees/onig/CLAUDE.md` state for their
engines: *"no byte was withheld or refused"*, never *"the engine looked
at every byte"*.

## (c) The config: block mode, no SOM, and the flag choice that costs
5 corpus patterns for zero measured gain

**`HS_MODE_BLOCK`** — a one-shot scan of a whole in-memory buffer, the
closest fit to this bench's batched-in-memory subjects (`docs/dev/
research/2026-09-12-b42-engine-landscape.md`'s own recommendation:
"BLOCK trades nothing extra... recommend BLOCK only for v1"). Streaming
and vectored modes are out of scope (irrelevant to this bench's subject
shape).

**NO `HS_FLAG_SOM_LEFTMOST`** — the `nosom` config's entire reason to
exist (see "THE GOVERNING RULING" above). **NO `HS_FLAG_UTF8`** — this
driver is byte-oriented by construction, Vectorscan's own documented
default ("ASCII by default"), matching every other testee's default
8-bit non-UTF convention on this roster and satisfying
`non-utf8-subject`.

**`VS_DRIVER_FLAGS` is `0` — NOT `HS_FLAG_UCP`, on MEASURED evidence,
not assumption.** The first cut of this driver set `HS_FLAG_UCP`
unconditionally, reasoning (wrongly, unchecked) that `\p{...}` Unicode-
property classes would need it. A direct A/B census through the real
adapter (`docs/dev/measurements/2026-09-17-vectorscan-capability-
witness-census-5.4.11.txt` carries both runs) found:

- **`\p{L}` compiles IDENTICALLY with `HS_FLAG_UCP` set or NOT set at
  all** — the flag buys `unicode-properties` NOTHING.
- **Setting `HS_FLAG_UCP` BREAKS `\b` (word-boundary) compilation
  outright**: `"\b unsupported in UCP mode at index N"`, on FIVE real
  `bench/capability` corpus patterns that carry NO `requires-unicode-
  properties` tag at all and have nothing to do with the token
  (`wild-waf-crs-942140-dbnames`, `wild-waf-crs-942360-concat-sqli`,
  `wild-secrets-aws-access-key-id`, `wild-secrets-github-pat`,
  `wild-codegrammar-json-constant`).

Corpus compile count: **35/64 with `HS_FLAG_UCP` set, 40/64 with it
unset** — a strictly worse choice for zero gain, caught by measuring
rather than reasoning from the flag's name. `VS_DRIVER_FLAGS = 0` is
therefore the driver's ONLY compile flag, for both forms, every pattern.

## (d) The boolean-grain `outcome_for` statement

See "THE GOVERNING RULING" above — restated here because it is this
adapter's single most consequential design fact and a reader should not
have to find it twice.

## (e) `hs_populate_platform`/SIMD notes

**NOT called.** `hs_compile()`'s `platform` parameter is passed `NULL`
throughout (`driver.c`), which the header states produces "a database
suitable for running on the current host platform" — exactly what a
same-box compile-then-measure driver wants; `hs_populate_platform()`
exists to target a DIFFERENT host than the one compiling, which this
bench never does. `testee.simd = "on"`: Vectorscan/Hyperscan's whole
raison d'être is SIMD-accelerated multi-pattern scanning
(`automaton_class = "simd-multipattern"`, the roster's only engine
carrying that token) — this project's SIMD axis is a fact about the
ENGINE's architecture here, not a runtime dial this adapter turns (there
is no `HS_CPU_FEATURES_*` override in play; `hs_compile()`'s implicit
platform detection is what selects the actual dispatch at compile time).

## The capability declaration (`bench/capability/gen_patterns.py`'s
`EXT_BENCH_ROSTER`, regenerated — never hand-edited — into `patterns.rxt`)

**5 of 17 REQUIRES tokens SATISFIED — the NARROWEST on the roster**, per
capability_set_v1.md §5.1's own prediction for this engine:
`unicode-properties`, `named-groups`, `free-spacing`, `non-utf8-subject`,
`true-end-anchor`. **12 NOT**: `backrefs`, `lookaround`,
`lookbehind-variable`, `possessive-quantifier`, `atomic-group`,
`recursion`, `conditionals`, `k-reset`, `control-verbs`, `callouts`,
`span-reporting`, `captures`.

The full derivation, an isolated witness per token PLUS all 64 real
`bench/capability` corpus patterns through the real adapter, is
`docs/dev/measurements/2026-09-17-vectorscan-capability-witness-census-
5.4.11.txt` (`probe_vectorscan_capability_census.py` beside it as the
reproducing script — mirroring `testees/onig/`'s own l6bonig-lane
discipline: "mandatory BEFORE the `ext bench` capability matrix declares
anything", the [B42] L5 "wrong first-cut" lesson).

**`span-reporting` and `captures` are EXECUTION-MODEL facts, not
compile witnesses** (capability_set_v1.md §5.1's own note, the SAME
class of exclusion `testees/pcre2/CLAUDE.md`'s `pcre2-dfa` section makes
for its own `captures` withhold): `span-reporting` is withheld because
this config never carries `HS_FLAG_SOM_LEFTMOST`, structurally, not
because any construct refuses; `captures` is withheld because Hyperscan
has **NO capturing-group mechanism at all** — confirmed live: `(?<name>a)`
and `(?P<name>a)` BOTH compile clean (`named-groups` is SATISFIED), which
is only possible because Hyperscan silently treats every group, named or
unnamed, as non-capturing. A pattern with a named group compiles; asking
Hyperscan to report what it captured is a question its API has no answer
for.

**Every other exclusion is a REAL `hs_compile()` refusal**, witnessed
live with Vectorscan's own diagnostic text (a closed structural signal
this adapter deliberately does NOT turn into a `refusal_class` pair —
see "Refusals, first-class" below):

| token | witness | Vectorscan's own message |
|---|---|---|
| `backrefs` | `(a)\1` | "Back-references are unsupported." |
| `lookaround` | `(?=a)a`, `(?<=a)b` | "Zero-width assertions are not supported." |
| `lookbehind-variable` | `(?<=a\|bc)x` | (same — no lookaround at all, so no variable-width lookbehind either) |
| `possessive-quantifier` | `a*+` | "Possessive quantifiers are not supported." |
| `atomic-group` | `(?>a*)b` | "Atomic groups are unsupported." |
| `recursion` | `(?R)`, `(?1)` | "Unrecognised character after (?" / "Subpattern reference unsupported" |
| `conditionals` | `(?(1)a\|b)(a)?` | "Conditional references are not supported." |
| `k-reset` | `a\Kb` | "\K at index N not supported." |
| `control-verbs` | `(*ACCEPT)`, `(*FAIL)`, `(*SKIP)` | "Unknown control verb (*NAME)" (all three) |
| `callouts` | `a(?C1)b` | "Callout at index N not supported." |

**One token's REAL corpus behaviour is more nuanced than its isolated
witness, stated rather than hidden**: `free-spacing`'s witness
(`(?x) a b c`) compiles clean, but TWO real corpus patterns tagged
`requires-free-spacing` — `wild-codegrammar-json-number-extended` and
`wild-codegrammar-json-stringcontent-escape`, both genuine multi-line
`(?x)` patterns with `#`-to-end-of-line comments — REFUSE with
"Unterminated comment." Vectorscan's `(?x)` parser does not accept a
`#` comment terminated by a real newline across a multi-line pattern the
way PCRE's does. The TOKEN stays declared SATISFIED (the isolated
construct genuinely works; the corpus failure is a real, separate
`did-not-compile` row, not a mis-declaration) — the SAME precedent
`testees/pcre2/CLAUDE.md`'s "pcre2-dfa" family-11 table and
`testees/onig/CLAUDE.md`'s recursion-spelling gap both set: an isolated
witness settles the token; a real corpus divergence under a satisfied
token is documented prose, never a second vocabulary value.

**`unicode-properties` is the opposite finding from Oniguruma's own
census** (`testees/onig/CLAUDE.md`'s "wrong first-cut" catch: onig's
`\p{Alpha}` compiles but `\p{L}` — a REAL Unicode category — does not,
under `ONIG_ENCODING_ASCII`). Vectorscan is the other way round: `\p{L}`
compiles, `\p{Alpha}` (a POSIX-style ctype name) does **NOT**
("Unknown property at index 3"). Vectorscan's vocabulary is real Unicode
General Categories, not POSIX names — the SHAPE virtually every real
PCRE corpus pattern actually uses, so `unicode-properties` is declared
SATISFIED here on stronger corpus-relevance grounds than onig's own
narrower declaration.

**Corpus confirmation, not merely isolated witnesses**: 40 of 64 real
`bench/capability` patterns compile through `vectorscan-block-nosom`.
Every one of the 24 refusals cites a token this roster row withholds,
with ONE exception worth naming rather than silently absorbing:
`tag-depth3-bound` (`<(\w+)>(?:[^<]|...)*</\1>`) uses backreferences but
carries NO `requires-backrefs` tag at all in the committed corpus (its
family tag is `family-cap-recursion`) — a pre-existing corpus-tagging
gap, not a capability-declaration error on this lane's part; it still
refuses honestly via the ordinary `did-not-compile` path regardless of
what this roster row declares.

## Refusals, first-class

`hs_compile()` failure → `did-not-compile` BY NAME, `diagnostic` carrying
`hs_compile_error_t`'s own `message` (plus the zero-based `expression`
index, always 0 for this single-pattern-per-database adapter) —
Vectorscan's own text, never re-typed or re-classified by this adapter.

**NO `refusal_class` pair.** `capability_set_v1.md` §5.5 states plainly:
"Never declared by Vectorscan or perl, whose refusal is free text only"
— `hs_compile_error_t` is `{message, expression}`, no closed reason enum
the way RE2's `ErrorCode` or Oniguruma's `ONIGERR_*` are (`docs/dev/
research/2026-09-12-b42-engine-landscape.md`'s own table row: "no closed
enum of REASONS... only free text"). Declaring one anyway would be
exactly the dishonest invention `record_schema.md` §7 rule 1 exists to
prevent — the same discipline `testees/onig/adapter.py`'s OWN
`refusal_class` declaration demonstrates by contrast (Oniguruma's
`ONIGERR_*` IS a closed structural signal; Hyperscan's is not).

A construct the `ext bench` matrix DECLARES missing never reaches this
adapter's own refusal path at all — `pcrecbench.capability`'s
pre-compile policy intercepts it first (`unsupported-by-declaration`,
with `declaration_ref` naming this file's own census).

## `gave-up`: the EMPTY SET, and why

Vectorscan/Hyperscan's entire architectural pitch is a BOUNDED automaton
with no backtracking — `docs/dev/research/2026-09-12-b42-engine-
landscape.md` line 122: "Hyperscan/Vectorscan all guarantee no
catastrophic backtracking." There is no documented `hs_scan()` return
code shaped like `PCRE2_ERROR_MATCHLIMIT` or Oniguruma's
`ONIGERR_RETRY_LIMIT_*` — a configurable resource budget the engine can
exhaust and decline to answer from. `GAVE_UP_CODES = frozenset()`:
`harness.classify_giveup` therefore NEVER returns `True` for this
testee, by construction — any negative `hs_scan()` return this driver
did not itself cause (via its own callback returning 1 to request an
early stop, which surfaces as `HS_SCAN_TERMINATED` and is treated as an
ordinary match, never a refusal) is `crashed`, correctly, because
Vectorscan structurally has nothing else to report there. **Untested
against a real catastrophic-backtracking corpus witness this lane**
(unlike `testees/onig/CLAUDE.md`'s own `(a+)+$` demonstration of
`onig-default`'s DEFAULT retry-limit budget firing) — there is nothing
this engine COULD give up on to demonstrate; the absence is the finding.

## The I-72 lesson: pattern bytes end to end

This adapter passes the pattern via a FILE (`_compile_one`'s
`patfile`/`--pattern`), exactly like `testees/pcre2/adapter.py`'s and
`testees/onig/adapter.py`'s own convention — never raw pattern bytes
through argv text, which is where I-72's mojibake bug lived on the pcrec
side (`pattern.decode("latin-1")` + subprocess's own `os.fsencode`
UTF-8 re-encoding of a `str` argv element). **Verified live, end to end,
through the REAL adapter** (never the raw driver binary alone): pattern
`\x93[\x20-\x7e]*\x94` (a file, written as raw bytes by
`Adapter.compile()`), subject `\x93hello\x94` (also a file). This
adapter's `_compile_one` writes `pattern` with `open(patfile, "wb")`
(raw bytes, no encode/decode step at all — there IS no `str` conversion
anywhere on this path, so the latin-1/fsencode failure mode I-72 found
cannot occur here structurally, not merely "was tested and passed").
`Adapter.compile()` + `Adapter.measure()` end to end:

```
high-byte end-to-end via real adapter (file-based pattern delivery): hb match 7
```

**The additive `check_high_byte_pattern_argv` arm, adapted for boolean
grain**: the pcrec/pcre2/onig arms in `tools/selfcheck.py` assert a
SPAN (`[0,7)`) — this testee cannot honestly assert that (see "THE
GOVERNING RULING" above: `start`/`end` are always `-`). The correct
Vectorscan arm asserts **`answer == "match"`** only, on the same
(pattern, subject) pair every other engine's arm uses, so a reader sees
all four engines confirm the SAME high-byte witness at whatever grain
each can honestly support. **NOT YET ADDED to `tools/selfcheck.py`
itself** — that file is shared, `make check-harness` infrastructure this
lane was told NOT to touch while pcrec's battery owns the box (see the
lane report's OWED section); verified here in isolation instead, exactly
as the brief asked.

## Two forms, and why the whole-subject one is NOT `record.whole_subject_text()`

Vectorscan block mode's `hs_scan()` has **NO runtime anchoring dial at
all** — unlike `PCRE2_ANCHORED`/`PCRE2_ENDANCHORED` (pcre2) and unlike
`onig_match`-at-a-fixed-position (Oniguruma): it scans the WHOLE buffer
for a match starting anywhere. So `pcrecbench.record.whole_subject_text()`'s
bytes (`(?:pattern)\z`, which supplies only the END anchor and relies on
the CALLER supplying the START anchor some other way) are not enough by
themselves. `driver.c`'s `--form whole-subject` builds its OWN, WIDER
wrapper — `^(?:pattern)\z` — a real, DOCUMENTED divergence from the
shared helper's bytes, not an oversight: `^` (no `HS_FLAG_MULTILINE` is
ever set, so `^` behaves as buffer-start, identically to `\A`) supplies
the START anchor Hyperscan's API has no other way to express in block
mode. `adapter.py`'s `compile()` passes the SAME plain pattern bytes for
both `--form plain` and `--form whole-subject` and lets `driver.c` do
the wrapping, so there is exactly ONE place that knows the whole-subject
artifact's real expression text.

CONFIRMED (this lane's own smoke, `docs/dev/lanes/l6bvs_report.md`):
`foo|bar` under `--form whole-subject`: subject `foo` → `match`; subject
`xfoo` → `nomatch` (the `^` anchor rejects the leading garbage a bare
`(?:foo|bar)\z` would not).

## `--utf8`: the character-boundary find-all advance ([B77] U1)

The driver protocol's `--utf8` flag (`pcrecbench/adapters.py`'s header;
`docs/design/utf8_set_v1.md` 8.4) switches the find-all EMPTY-MATCH
advance from `start + 1` to the next CHARACTER boundary -- pcrec
match_api.md S3.1.1's normative utf8 rule: from `start + 1`, skip every
byte in 0x80-0xBF, stop at the first byte outside that range or at the
subject's end (`utf8_next_start` in the driver, the same rule as
`oracle_pcre2.next_start`). `adapter.py` passes it iff the harness set
the handle's `utf8_advance`, which it does iff the pattern's ORACLE
OPTION WORD carries PCRE2_UTF (a set declaring `[expectations] encoding
= "utf8"`) -- so on every byte set the argv and the advance are exactly
what they were. Checked by `make check-harness`'s
`check_utf8_find_all_advance` (the boolean-grain arm: the flag accepted, the
answer unchanged).

Here the flag is ACCEPTED and INERT: this driver has no find-all loop at
boolean grain (`NMATCHES` is always `-`, above), so there is no advance for
it to move. It never sets HS_FLAG_UTF8 -- that is a config's choice
(`vectorscan-block-nosom-utf8`, lane U2).
