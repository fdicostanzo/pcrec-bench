# lane b42dfa — [B42] L6a: the `pcre2-dfa` testee

Branch `lane/b42dfa`, from master `c2eb2a9`. Commit `a290f35`.

## What this lane built

A fourth pcre2 testee — `pcre2-dfa`, driving `pcre2_dfa_match_8` instead of
`pcre2_match_8` — on the EXISTING `testees/pcre2/driver.c` and
`adapter.py`. No new dependency (libpcre2-dev is already installed on this
box — a side finding this lane confirmed and used, see below), no new
build machinery, no new driver file (capability_set_v1.md §11.1's own
framing, ratified by Frank as Q13 today).

1. **`testees/pcre2/driver.c`** — a `--dfa` CLI flag; `pcre2_dfa_match_8`
   + `pcre2_match_data_create_8` dlsym'd (never
   `pcre2_match_data_create_from_pattern_8` for DFA, per man
   `pcre2_dfa_match`); a malloc'd, generously-sized workspace
   (`PCRE2_DFA_WS_ELEMS = 100000`, sized against this project's own worst
   case — `bench/bounded`'s `[a-z]{0,65535}` — and never assumed
   sufficient: a real exhaustion is `PCRE2_ERROR_DFA_WSSIZE`, handled, not
   crashed); one `do_match()` call site shared by both matchers (the
   `rc>=0`/`ov[0..1]` reading is IDENTICAL for both — man
   `pcre2_dfa_match`'s own text: the longest match is always the first
   ovector pair, regardless of return-code convention); captures forced
   to `npairs=0`/`caps="-"` for DFA (man item 2: "no captured substrings
   are available"); `--dfa --jit` together refused by name (no JIT on
   this route).
2. **`testees/pcre2/adapter.py`** — `automaton_class = "nfa-simulation"`
   for `dfa` (never `dfa-only` — the man page's own words: "not
   implemented as a traditional finite state machine"), `captures =
   "off"`, a `compile_cost_definition` stating the zero-separate-compile
   fact; `GAVE_UP_CODES_DFA` (the interp/jit set minus JIT_STACKLIMIT,
   plus `DFA_WSSIZE`/`DFA_RECURSE` resource-shaped and
   `DFA_UITEM`/`DFA_UCOND` STRUCTURAL codes); `--dfa` threaded through
   `compile()`/`measure()`.
3. **`testees/pcre2/configs.toml`** — the `pcre2-dfa` entry.
4. **`bench/capability/gen_patterns.py`** — a `pcre2-dfa` row in
   `EXT_BENCH_ROSTER` (satisfies every `REQUIRES` token except
   `backrefs`/`conditionals`/`k-reset`/`control-verbs`/`captures`, each
   witnessed live); `patterns.rxt` regenerated (never hand-edited) and
   re-verified against the pinned pcrec's `--list-source` (`gen_patterns.py
   --check`, clean).
5. **`testees/pcre2/CLAUDE.md`** — the full semantics account: the
   restricted-construct list quoted and cross-referenced against this
   project's own `REQUIRES` vocabulary, live transcripts, the structural-
   vs-resource refusal split and the schema gap it exposes (stated
   plainly, not routed around), the family-11 census (below), and the
   workspace/ovector sizing rationale.
6. **`tools/selfcheck.py`** — `check_pcre2_dfa`, 12 checks in four arms,
   every one with its control: `describe()` facts; the no-captures shape
   + the documented longest-match divergence in one witness cell; the
   structural refusal classified `gave-up` by name, never `crashed`,
   driven on an UNTAGGED real corpus pattern (`bench/syntax`'s own
   `bak-1`/`f-dup`, no `requires-*` involved — the driver-level fallback
   path, not the capability policy); two real `quick` cells into a
   scratch store (one showing `bench/capability`'s new ext-bench row
   blocking `doubled-word` pre-compile, one a full measured record on
   `bench/email`).

## The semantics table (full citations in `testees/pcre2/CLAUDE.md`)

| construct | pcre2-dfa | evidence |
|---|---|---|
| backreferences | REFUSED, match-time, structural | `PCRE2_ERROR_DFA_UITEM` (-42), live: `(\1)(a)` over `aa`, and `bak-1`/`f-dup` (untagged, real corpus) |
| `\K` | REFUSED, same code | live: `a\Kb` over `ab` |
| conditional on backref/recursion-test | REFUSED, structural | `PCRE2_ERROR_DFA_UCOND` (-40), live: `(?(1)a|b)(a)?` over `ba` |
| control verbs except `(*FAIL)` | withheld (no finer vocabulary token) | man item 7 |
| captures | NEVER reported | man item 2; driver forces `ncaps=0`/`caps=None` unconditionally |
| lookaround, possessive quantifiers, atomic groups, `\p{...}`, named groups, free-spacing, callouts, span-reporting, true-end-anchor | WORK | man's own discussion; kept in the `ext bench` matrix |
| workspace exhaustion | `PCRE2_ERROR_DFA_WSSIZE` (-43), resource-shaped, `gave-up` | this driver's own budget |
| recursion ovector exhaustion | `PCRE2_ERROR_DFA_RECURSE` (-39), "extremely rare" | man's own words |
| JIT | absent, no dial | man `pcre2jit` |
| answer, when multiple alternatives match at one point | **LONGEST**, not first-tried | man's own words; three corpus cells confirmed to diverge (below) |

## Family 11 (`semantics-divergence`) census — run BEFORE touching the roster

Per capability_set_v1.md §5.6's own precondition. All six patterns checked
live with `pcre2test -dfa`, cross-referenced against `expectations.tsv`:

- **`file-ext-order`** (`\.tar|\.tar\.gz`): DIVERGES, and IT FIRES — the
  set's one `match` expectation (`sd-fileext-short`, "archive.tar.gz")
  is oracled `[7,11)` under NFA; DFA answers `[7,14)`.
- **`keyword-prefix-order`** (`in|instanceof`): DIVERGES on exactly ONE
  of four `search_short` subjects (`sd-keyword-short` = the literal text
  `instanceof`); the other three (and the three throughput ones) do not.
- **`router-prefix-order`** (`/user|/users`): DIVERGES on
  `sd-router-short` (`/users`); the three throughput subjects are
  UNCHECKED (an honest gap, named).
- **`wild-semdiv-altorder-foo-foobar-rustregex`** (`foo|foobar`):
  mechanism confirmed live, but MOOT — 78/78 corpus expectations are
  `nomatch` (neither literal substring appears anywhere in the set).
- **`wild-semdiv-dollar-trailing-newline-pcre2`** (`abc$`): NO
  divergence, confirmed both by direct witness and by the corpus's own
  78/78 `nomatch` rows.
- **`wild-semdiv-empty-alt-repeat-pcre2`** (`(a|)*\d`): NO divergence,
  confirmed STRUCTURALLY (at most one valid total match length per start
  offset — no ambiguity for DFA to resolve differently) and empirically
  on the stress pair and a real matching subject.

**Consequence, flagged rather than worked around:** three named cells
(`file-ext-order`/`sd-fileext-short`, `keyword-prefix-order`/
`sd-keyword-short`, `router-prefix-order`/`sd-router-short`) will read
`wrong-span-or-captures` if `pcre2-dfa` is measured against
`bench/capability` — a DOCUMENTED, EXPECTED divergence, not a `pcre2-dfa`
defect. `harness.outcome_for`'s `convention` parameter (R5 B1/CB1) exists
for exactly this and is a stated no-op until a real `under
<convention>`-qualified expectation row exists — building that is a
harness/schema-adjacent change outside this lane's scope, per the brief's
own instruction ("if the harness cannot yet express it, flag it for the
manager").

## The structural-refusal schema gap

`record_schema.md`'s `match_outcome` enum has no dedicated STRUCTURAL
value. `GAVE_UP_CODES_DFA` buckets `DFA_UITEM`/`DFA_UCOND` under
`gave-up` anyway — the least-wrong existing outcome (never `crashed`,
never a silent wrong answer), by-code distinguishable from a true
resource refusal. Stated plainly in `testees/pcre2/CLAUDE.md` as a real,
documented gap for the schema owner, in the same spirit as
`capability_set_v1.md` §5.4's own open list — not routed around quietly.

## Side finding, used (not a scope excursion): `libpcre2-dev` is installed

`docs/dev/research/2026-09-12-b42-engine-landscape.md` (3) found this and
left it "unactioned... for whoever next touches that adapter" — that was
this lane. `/usr/include/pcre2.h` was used to VERIFY every constant this
lane added (an extra step beyond the existing file's own "[measured]"
discipline), but the driver still reads every pcre2 symbol via `dlopen` +
hand-declared prototypes, matching the existing two testees' convention
rather than switching to the header — a deliberate consistency choice,
not an oversight.

## Charter-vs-committed checklist

| brief item | status |
|---|---|
| (1) `pcre2-dfa` config + driver mode, workspace sizing recorded | DONE, committed |
| (2) unsupported outcomes BY NAME from pcre2's own codes, never a crash; no-captures shape structural | DONE — `gave-up` is the closest schema-legal bucket, the gap is DOCUMENTED (not silently routed around) since no dedicated enum value exists |
| (3) conventions/family-11 divergence handling | DONE — census run, 3 diverging cells named, EXCLUSION not built into the harness (out of scope per the brief's own instruction), flagged here and in the CLAUDE.md for the manager |
| (4) CLAUDE.md + adapter note + selfcheck arms | DONE — `testees/pcre2/CLAUDE.md`'s new section, 12 selfcheck checks (unsupported-by-name + control, no-captures shape, two real quick cells) |
| targeted checks green standalone | `check-schema` GREEN (4/72/0, ran to completion); `check_pcre2_dfa` (12/12) and `check_driver_smokes` (2/2, now exercising `pcre2-dfa` as pcre2's alphabetically-first testee — a harmless coverage shift, unhardcoded elsewhere) run in isolation and GREEN |
| full `make check-harness` | **OWED** — launched in the background (harness-tracked, not disowned), log `/tmp/claude-1001/-home-duxevents-pcrec-bench/932894fa-f62e-4029-8fb0-f23809c3696f/scratchpad/b42dfa_check_harness.log`, completion line `DONE rc=<N>` appended; started 2026-09-16 09:09 EDT on an otherwise-idle box (the main tree's own `make check` had already finished) |
| `make check-report` | **OWED** — first attempt (180s timeout, piped through `tail`) was killed before flushing any output (exit 143) while contending with `check-harness` for CPU; RELAUNCHED disowned with a 900s budget and its own `DONE rc=` marker (NOT harness-tracked — no notification will arrive; check the marker), log `/tmp/claude-1001/-home-duxevents-pcrec-bench/932894fa-f62e-4029-8fb0-f23809c3696f/scratchpad/b42dfa_check_report.log` |
| `make check-interpret` | not run this lane (no catalogue/report change) — expected unaffected |

## What is NOT built here (by brief and by design)

- The convention-scoring machinery that would let family 11's three
  diverging cells score correctly under `pcre2-dfa`'s own convention
  rather than against the NFA oracle — `capability_set_v1.md` §5.6's own
  scope line, a harness/schema-adjacent change.
- A per-subject STRUCTURAL-refusal schema outcome — the gap `gave-up`'s
  bucket papers over honestly; future schema work.
- The two `router-prefix-order` throughput subjects' own divergence
  status (unchecked, named as a gap, not asserted either way).
- Any change to `pcre2-interp`/`pcre2-jit`'s existing dlopen convention
  despite `libpcre2-dev` now being available — deliberate, for
  consistency (see above).
