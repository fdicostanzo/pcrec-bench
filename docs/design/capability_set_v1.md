# The capability survey set — design, v0.2

**[B42] phase (b), REVISED under R5. Plan row `[B42]`; Frank's charter,
2026-09-12.** STATUS: **v0.2 — "revised under R5; BUILD PARKED on
pcrec's `.rxt` delivery (O-26)"**. v0.1 went to a D6 adversarial critic
panel (three lenses, 26 findings: 8 BLOCKING / 10 SHOULD-FIX / 8
WORTH-NOTING) the same day it was drafted; the panel's consolidation
(`docs/dev/reviews/2026-09-12-r5-capability-set-v1.md`) dispositioned
every finding, and the manager ratified all of them with three
amendments from Frank's same-day live rulings. This revision applies
every ratified disposition and amendment. **The set's DESIGN stands**
(families, capability model, provenance, metrics, roster, Q1/Q2 as
Frank ruled them); **the BUILD is PARKED**: Frank's Q3 ruling (2026-09-12)
makes this set a driver of the `.rxt` format itself — it is built ON
`.rxt` for real, not on §9's old hybrid — and the effort parks at the
format's own capability roadblocks. §9 is now a pointer to
`docs/design/rxt_needs_v1.md` (the detailed capability feedback already
sent to pcrecdev1, outbox O-26) rather than a design of its own. Nothing
here is built; nothing under `bench/`, `schema/`, `pcrecbench/` or
`testees/` is touched. **On restart:** run `rxt_needs_v1.md` §3's
41-check acceptance checklist against pcrecdev1's delivery, review the
deltas against this note (a second, lighter panel pass — does the
delivery actually resolve the six roadblocks), then reopen §11's lanes.

### Revision log, v0.1 → v0.2

One line per applied disposition id (`docs/dev/reviews/2026-09-12-r5-capability-set-v1.md`).
Ids not applied here are noted with where they actually land (several
targeted the old §9, which this revision replaces wholesale per the Q3
ruling, and so travel forward to `rxt_needs_v1.md`'s own restart
material rather than being re-fixed in a section that no longer makes
the design it was fixing).

| id | disposition | where in v0.2 |
|---|---|---|
| CB1 | family 11 narrowed to v1's shared-convention population; cross-convention scoring machinery deferred | §3.1 row 11, §5.6, §11.1, new §12 question |
| CB2 | §5.7's "Already built" corrected to UNBUILT; L5 reclassified from a check to a build task | §5.7, §11.1 |
| CB3 | wild/designed bucketing promoted from `patterns[].tags` to real enumerated fields | §4.1, §1.1, §10(d) |
| CB4 | `noseyparker.txt` re-fetch confirmed; family 4 target members raised; Appendix A's "three OWED" corrected to two | §3.1 family 4, Appendix A |
| CB5 | `atomic-possessive` split into two tags; Oniguruma's atomic-group claim flagged for independent re-derivation | §5.1 |
| CB6 | `k-reset`'s Oniguruma gap resolved before an `onig-*` config declares it | §5.1 |
| CB7 | `hazard_class` assigned per family in §3.1 (families 2, 5, 10 at minimum) | §3.1 |
| CB8 | family 10's calibration risk stated explicitly; a mitigation adopted | §3.5, §13 R6 |
| CS1 | `match`-regime exclusion's family list corrected (drop 7/8 absent a `\K` member); scope stated | §3.5 |
| CS2 | §2.2 reason 3 dropped | §2.2 |
| CS3 | Q3 re-marked BLOCK, folded into Frank's ratification amendment 3 (asked at the restart, not before) | §12 |
| CS4 | `ru_maxrss` ranked within the native-driver population | §7.4, §7.5, §12 Q6 |
| CS5 | TRE `named-groups`/`free-spacing` rows cited or marked UNCONFIRMED | §5.1 |
| CS6 | §13 R2's family list corrected, "2, 7-10" → "2, 7-9" | §13 |
| CS7 | §8.1 states the permanent `inconclusive-spread` caveat | §8.1, §12 Q14 |
| CS8 | superseded — the "no build directives" gate's mechanism lives in `rxt_needs_v1.md` now, not in a v0.2 §9 | §9 (pointer) |
| F5 | `pcre2-dfa`'s §8 row corrected: not a dial, a fourth engine identity | §8 |
| F6 | pcrec's §8 row maps dials vs diagnostic controls explicitly | §8, §1.1 |
| F8 | L3/L4 sequencing gap — superseded with §9; the restart's lane plan re-derives sequencing against the actual delivery | §9 (pointer), §11.1 note |
| S9 | `automaton_class` column added for TRE/Oniguruma | §7.1 |
| S10 | family 12's non-UTF-8 `canonical_text` omission stated (relocated from the old §9.5) | §3.1 family 12 |
| S11 | Vectorscan boolean-grain cost grounded directly in the driver protocol's degenerate `START`/`END` allowance | §5.6 |
| B6 | superseded — the `subbench.py` loader surface is now the restart's to scope against the actual delivery | §9 (pointer) |
| B7 | `unsupported-by-declaration` and `testee.conventions` noted as first production exercises | §5.3 |

Three further changes follow directly from Frank's ratification (not
individual review findings): **Q2** is answered (realism, not a ratio —
§4.3 rewritten); **Q10-Q12** are superseded (§9 replaced); and **§12**
carries a revised, restart-scoped question list.

**How to read it.** Every decision states its alternatives and why this
one. Every open choice carries a RECOMMENDATION and the consequence of
each answer. Nothing is asserted that one of the three research notes did
not establish, and every such fact is cited by note and section:

| short form | file |
|---|---|
| **N1 §x** | `docs/dev/research/2026-09-12-b42-rx-in-the-wild.md` (regexes in the wild), incl. its `b42wild2` follow-up |
| **N2 §x** | `docs/dev/research/2026-09-12-b42-engine-landscape.md` (engine capability/option landscape), incl. its `b42engines2` follow-up |
| **N3 §x** | `docs/dev/research/2026-09-12-b42-rxt-as-source.md` (`.rxt` as a set source) |

This repo's own documents are cited as `requirements.md §N`,
`record_schema.md §N`, `subbench_directory_model.md §N`,
`bench/syntax/NOTES.md`, and by `file:line` where a line matters.

A claim the notes marked UNCONFIRMED is repeated here as unconfirmed, or
not at all. Where this note goes beyond the notes it says so in the
sentence.

---

## 1. The charter restated, and where each requirement is satisfied

Frank's eight requirements, verbatim in substance from the `[B42]` plan
row:

1. Patterns from the WILD where possible, provenance recorded per pattern.
2. EDGE CASES teased out beside the common shapes, both chosen to stress
   the engines.
3. OTHER METRICS recorded — compile time first (AOT + cc vs JIT vs
   constructor), artifact size, memory — apples-to-apples where
   reasonable, the non-comparable stated.
4. BUILT ON the `.rxt` file format (pcrec DD-13), saying which artifact is
   the source of truth and how R-BENCH-4 engine neutrality survives.
5. MULTIPLE REPRESENTATIVE MODELS per engine under different OPTION SETS,
   a named config roster per engine.
6. A research + design pass WITH A DESIGN REVIEW before any build.
7. A PUBLIC-FACING INTERFACE considered as a LATER effort — leave room,
   build nothing.
8. The approach + open questions come BACK TO FRANK before the build.

Plus the charter's two standing clauses: CAPABILITY is first-class (every
pattern carries what an engine must support to run it; an engine that
cannot is a recorded `unsupported` outcome, never an error), and SLIGHT
SYNTACTIC ADJUSTMENT per engine is allowed when semantics are preserved
(a per-engine spelling table, equivalence stated and oracle-checked).

### 1.1 Traceability

| req | satisfied by | in one line |
|---|---|---|
| (1) wild patterns + per-pattern provenance | **§4** (+ §3's per-family source column) | a closed provenance record per pattern, a licensing floor, real enumerated `provenance_source`/`fidelity` record fields (CB3), a `provenance.tsv` re-derived under `--check`. Requirement (1) is REALISM, not a ratio — §4.3 |
| (2) edge cases beside common shapes | **§3** | six wild families and six capability/hazard families, each with designed members beside the imported ones |
| (3) other metrics | **§7** | one table saying what is RECORDED, what is SCORED, what is CAVEATED, per metric and per engine class — `ru_maxrss` now ranked within the native-driver population (CS4), not caveated-and-shown-only |
| (4) built on `.rxt` | **§9** | SUPERSEDED by Frank's 2026-09-12 Q3 ruling: the set is built ON `.rxt` for real, not on a sidecar hybrid. §9 is now a pointer to `docs/design/rxt_needs_v1.md`; the build is PARKED until pcrecdev1's delivery |
| (5) option sets per engine | **§8** | a named config roster per engine, v1 vs later, on the existing `testee_id` composition rule. `pcre2-dfa` is a fourth engine identity, not a dial (F5); pcrec's own roster is mapped explicitly onto genuine user-facing dials vs this project's own diagnostic denial flags (F6) |
| (6) research + design review | this note + phase (c) | the three research notes are §0's citation base; the panel is the next step |
| (7) public interface, later | **§10** | the data shapes a later UI consumes, what is already sufficient, what is missing; nothing built |
| (8) approach + questions to Frank | **§12** | one consolidated, deduplicated question list, each with a recommendation, a consequence per answer, and a BLOCK/DEFAULT mark |
| capability first-class | **§5** | a closed REQUIRES vocabulary, per-config capability declarations, a pre-compile `unsupported-by-declaration` policy, no new outcome enum value |
| syntactic adjustment | **§6** | the adopted rewrite table, the rule that hazard-class possessive/atomic rewrites are NOT variants, and the equivalence gate |

Two cross-cutting sections carry no single requirement: **§2** (set
identity) and **§11** (the build plan), **§13** (risks).

---

## 2. Set identity — a new sub-bench, not an extension of `bench/syntax`

**DECISION: a new sub-bench, `bench/capability/`, id `capability`,
version `0.1`.**

### 2.1 The alternatives

| option | what it means | why not |
|---|---|---|
| **A. Extend `bench/syntax@0.1` → `@0.2`** | add the wild + capability patterns to the existing census | rejected — three independent reasons below (a fourth, that a version bump strands the measured first sample, is dropped: `requirements.md §5` doesn't destroy old records on a bump, and this design's own §4.5/Q8 plans an identical bump for itself — CS2) |
| **B. A new sub-bench** | a sixth directory under `bench/` | **CHOSEN** |
| **C. Several new sub-benches** (one per family group) | e.g. `bench/wild/` + `bench/redos/` + `bench/semantics/` | rejected — the charter is one set; three sets triple the sidecar/generator/expectation surface for no analytic gain, and the families share one subject vocabulary and one instrument |

### 2.2 Why not extend `bench/syntax`

1. **The census is registry-ENUMERATED and the new set is not.**
   `bench/syntax`'s defining discipline is that its pattern list comes
   from pcrec's `--list-syntax` seed and that `coverage.tsv` is DERIVED
   from the pattern table × the seed, with `gen_patterns.py --check`
   failing BY NAME on any seed row no pattern covers and no reason
   excuses (`bench/syntax/CLAUDE.md`, `NOTES.md` "Enumerating from a
   head"). A wild pattern covers no seed row and excuses none. Adding
   sixty of them makes the coverage gate meaningless — it would pass with
   the wild rows simply absent from the table, which is exactly the
   silent under-coverage the gate exists to prevent.
2. **The bodies are incompatible by construction.** Every census pattern
   is ONE construct in an otherwise plain body from one small vocabulary,
   so an outlier points at one mechanism (`NOTES.md`, "An outlier that
   points at three things"). A wild pattern is many constructs in an
   author's own body — the opposite property, deliberately. Rules R3 (the
   spelling rule) and R4 (the family rule) both read against that shared
   body and would be unusable on the new members.
3. **The blinding statements differ.** The census author was blinded per
   pcrec D27 and read only `man pcre2pattern` and the seed
   (`NOTES.md`, "Blinded authorship"). The capability set's wild members
   REQUIRE their author to read external corpora — that is the point of
   requirement (1). Two incompatible authorship disciplines cannot both
   be true of one directory's `NOTES.md`.

### 2.3 The name and version

`bench/capability/`, sidecar `id = "capability"`, `version = "0.1"`.

- The directory name and the sidecar id are deliberately the same, so
  `--subbench capability` resolves either way (OD-B13's rule, closed at
  [B9]).
- `0.1` because every existing set opened at `0.1` and the version is a
  frozen snapshot bumped on any pattern/subject/expectation change
  (`requirements.md §5`).
- `capability-survey` was considered and rejected as the id: `bench/`
  directory names are one word everywhere else (`email`, `loglines`,
  `bounded`, `altwide`, `syntax`) and a testee/report filter reads better
  short.

### 2.4 Relationship to the five existing sets — cite, never duplicate

N1 §iv enumerates what is already covered. The rule this set follows:
**a mechanism a depth set already measures to the rung is CITED in
`NOTES.md` and is not a family here.** Where the capability set touches
one of those mechanisms at all, it touches it for a reason the depth set
structurally cannot serve — cross-engine capability, or wild provenance.

| existing set | what it owns (N1 §iv) | what the capability set may still do, and why |
|---|---|---|
| `bench/syntax@0.1` | the construct census: 95 patterns, 18 families, one construct per plain body, registry-enumerated | **nothing at the construct grain.** The capability set's `cap-*` families use the SAME constructs but in wild/composite bodies, and their purpose is the cross-engine REQUIRES contrast (§5), not the construct's cost — which syntax already measured |
| `bench/altwide@0.2` | wide alternation as a ladder, 8..4096 branches × structure | **wild alternations only** — CRS keyword lists and rebar's `datefinder` pattern are alternations that GREW (N1 §8, §1). altwide measures width; this measures what an organically-grown one costs. No ladder here |
| `bench/bounded@0.3` | counted repeats, a rung ladder to PCRE2's 65535 ceiling, refusal as a first-class outcome | **nothing.** Counted repeats appear inside wild patterns incidentally and are never a family here |
| `bench/loglines@0.1` | mostly-failing search text shaped around PCRE2's required-code-unit dismissal | **the grok family's subjects may not reuse loglines' subjects** — see §3.4. The mechanism (prefilter dismissal) is loglines'; the patterns (real grok, Oniguruma dialect) are new |
| `bench/email` | one real-world-shaped family in depth, a floor, 1 MB subjects | **nothing.** Email validators appear once in `wild-validator` as the canonical everyday shape with wild provenance; the depth is email's |

**Consequence if this rule is broken:** the set becomes a shallow
re-measurement of four depth sets on a sixth night, which is the exact
failure N1 §iv warns about and the reason its taxonomy marks four rows
"cite, don't duplicate".

---

## 3. The family taxonomy

Source: N1 §ii (the eighteen-row taxonomy), N1 §iii (the edge-case
catalogue), N2 §3 (the per-engine construct table), N2 §7 item 5 (the
REQUIRES tags). Four of N1 §ii's rows are dropped as depth-set duplicates
per §2.4 (`huge-bounded-repeat`, `wide-alternation`, `long-literal-
prefilter`, `case-fold-pair`); `deep-nesting` is folded into
`cap-recursion`; `regex-set-priority` is DEFERRED (§12 Q7).

### 3.1 The twelve families

"Expected `unsupported`" columns are derived from N2 §3's table; each is
an expectation the first sample tests, not an assertion.

| # | family | stress mechanism | wild source(s) — licence, retrieval status | designed members | expected `unsupported` (and why) | target members |
|---|---|---|---|---|---|---|
| 1 | `wild-validator` | everyday validator shapes as actually pasted into code: class-heavy, anchored, alternation-of-ranges | OWASP Validation Regex Repository (**CC BY-SA 4.0**, page fetched, three patterns quoted verbatim, N1 §9); Elastic grok `UUID`/`BASE10NUM`/`WINPATH` (**Apache-2.0**, `LICENSE` fetched, four quoted verbatim, N1 §10) | one near-miss twin per imported validator (a subject-shaped edge the original gets wrong) | **none.** Every roster engine runs these; the point is the baseline everything else reads against | 8 |
| 2 | `wild-logparse` | macro-expanded compositional alternation over sparse-hit log text; atomic groups the ORIGINAL author added to fight backtracking | grok base patterns (**Apache-2.0**, fetched; `QUOTEDSTRING`'s nested atomic groups and `BASE10NUM`'s `(?>...)` quoted verbatim, N1 §10) | the same pattern with the atomic groups REMOVED — the author's own fix as a control pair | atomic/possessive: **RE2, Rust `regex`, Vectorscan, TRE** refuse (N2 §3). This family is where the §6 hazard rule bites hardest: the atomic group is the objective | 6 |
| 3 | `wild-waf` | large keyword alternations grown over years of community patches, over adversarial input | OWASP CRS `REQUEST-942-*` `@rx` rules (**Apache-2.0**, `LICENSE` fetched; five rules quoted verbatim with their CRS ids, N1 §8) | none — the imports ARE the edge cases | **none expected** to refuse (no exotic constructs in the five quoted); `(?i:...)` inline-scoped folding is the one thing to verify per engine | 5 |
| 4 | `wild-secrets` | many short, first-byte-distinct token patterns; high-entropy literals with structure | rebar `regexes/wild/noseyparker.txt` (**Unlicense**, RE-FETCHED and CONFIRMED — CB4/F1: 30+ verbatim patterns for AWS/GitHub/GCP/Azure/Dynatrace/Figma tokens and generic `username=...password=...` pairs, quoted directly from the raw file. The "literal text STILL OWED" line and the authored fallback below are both retracted) | none — the wild source supplies verbatim members directly; no authored fallback needed | **none** | 4 |
| 5 | `wild-datetime` | one enormous multi-language alternation with ambiguous decomposition; the COMPILE-time and SIZE axis, not the match axis | rebar `regexes/wild/date.txt` = `datefinder`'s production pattern (**Unlicense**, fetched, fragment quoted, N1 §1) | none | **none refuse to compile** expected; RE2's `max_mem` and Rust's `size_limit` are the ones to watch (N2 §4) | 2 |
| 6 | `wild-codegrammar` | small patterns applied per line/token in a latency-sensitive editor loop; `(?x)` free-spacing | VS Code `JSON.tmLanguage.json` (**MIT**, five regexes fetched and quoted, N1 §18) | one flattened `(?x)` twin (the multi-line-to-one-line question is now OPEN for Frank at the restart, `rxt_needs_v1.md` F-Q2 — §9) | free-spacing `(?x)`: supported by pcre2/Oniguruma/RE2/Rust; **TRE** has no inline-flag syntax at all (N2 §3) | 5 |
| 7 | `cap-backref` | backreference semantics — the cleanest capability line on the roster | grep's `tests/backref*` family located (**GPLv3** — import blocked pending §4.2's ruling, N1 §17); Oniguruma `test_syntax.c`'s `(?<=a\|(.))\1` (**BSD-2**, quoted, N1 §16) | doubled-word, tag-pair and palindrome shapes AUTHORED fresh (so no GPLv3 question arises) | **RE2, Rust `regex`, Vectorscan** all refuse (N2 §3, all three fetched from upstream docs). pcre2, Oniguruma, TRE, python, perl, pcrec run them | 5 |
| 8 | `cap-lookaround` | chained and nested lookahead/lookbehind, incl. VARIABLE-length lookbehind | Oniguruma `test_syntax.c` (**BSD-2**, quoted: variable-length lookbehind combined with a backref, N1 §16) | 3 chained-lookaround shapes authored; one fixed-width and one variable-width lookbehind pair | **RE2, Rust, Vectorscan** refuse all lookaround; **python `re`** refuses VARIABLE-length lookbehind specifically (CPython 3.14 docs, N2 §8 (8)); **TRE** has no lookaround (its parser's escape switch has only `\b\B\<\>`, N2 §5) | 5 |
| 9 | `cap-recursion` | recursion/subroutine calls, and deep nesting | grok's compositional expansion is the nearest wild analogue (N1 §10) | balanced-paren and DEFINE shapes authored; a 3-level nested-group body | **RE2, Rust, Vectorscan, TRE, python `re`** all refuse (N2 §3). perl, pcre2, Oniguruma (`\g<name>`, flag-confirmed), pcrec run them | 4 |
| 10 | `redos-nested` | nested/ambiguous quantifiers — the headline linear-time contrast | `engn33r/awesome-redos-security`'s CVE index as the INSPIRATION source (CVE text is factual/public); `vuln-regex-detector` **MIT** (`LICENSE` fetched, N1 §13); RE2's `Hard` pattern `[ -~]*ABC…Z$` (**BSD**, quoted, N1 §4) | the hazard shapes AUTHORED fresh from the CVE descriptions (`fidelity: inspired`, §4.1) | **none refuse to compile.** The finding is that RE2/Rust/Vectorscan/TRE are IMMUNE by construction and the backtrackers are not — this is the family where `hazard_class` matters and the §6 rule forbids possessive rewrites | 6 |
| 11 | `semantics-divergence` | one pattern, two DIFFERENT correct answers: alternation order under leftmost-first vs leftmost-longest; empty-match-in-repeat; `$` before a final newline vs `\z` | PCRE2 `testdata/testinput1`'s empty-match cases and `(a\|)*\d` (**BSD-3 WITH PCRE2-exception**, fetched, quoted, N1 §15); rust-regex `testdata/` incl. the Fowler suite (**MIT**, `LICENSE-MIT` fetched, N1 §5) | `a\|ab` against `"ab"` and its family — the leftmost-first/longest separator named in N2 §2.1 | **none refuse.** This is the `conventions[]` family: TRE answers `posix-leftmost-longest`, RE2 answers either depending on `longest_match` (§8), everyone else `perl-leftmost-first`. A testee is scored against its OWN convention (`requirements.md §7`) | 6 |
| 12 | `binary-nonutf8` | patterns and subjects over bytes that are not valid UTF-8 | Suricata `pcre:` rules are the real-use evidence but **no sample was obtainable in three attempts** (N1 §7 — the fetch failure is itself recorded) | authored: byte-class and high-byte literal shapes over non-UTF-8 subjects | **Rust `regex`'s default `str` API** refuses non-UTF-8 input outright (N1 §ii); rebar's own `ruff.toml` excludes engines for exactly this reason, a HAYSTACK-driven exclusion class (N1 §1) | 3 |
| — | `floor` | `requirements.md §5`'s per-call control | — | one literal byte (§3.3) | — | 1 |

**Total: 60 patterns** (59 members + the floor).

**Per-family `hazard_class` (CB7).** `hazard_class` is a required,
closed-enum field per PATTERN (`record_schema.md §8`;
`schema/record.schema.json:298`), and §6.3's hazard-rewrite rule is
keyed on it — but no family above states one, which would leave an
authoring lane's default read as `hazard_class: none` and route family
2's atomic groups (and family 10's whole point) to the ordinary §6.2
rewrite table instead of §6.3's protection. Assigned here, at minimum
for the two families the design's own prose already treats as
hazard-bearing (2, 10), plus one more whose own stress-mechanism text
names the same enum value (5):

| family | `hazard_class` | why |
|---|---|---|
| 2 `wild-logparse` | `exponential-backtracking` | the imported atomic groups exist to defend against it — §6.3's own worked example |
| 5 `wild-datetime` | `ambiguous-decomposition` | the family's own stress mechanism, verbatim: "ambiguous decomposition" |
| 10 `redos-nested` | `exponential-backtracking` | the family's entire objective |
| every other family, and the floor | `none` | no member is authored or imported to exercise a specific hazard |

**Family 11's v1 scope, narrowed (CB1).** §5.6 claims family 11
"exercises [convention-based scoring] for the first time in this
repo," but no code path scores a testee against its own declared
convention: `outcome_for` (`pcrecbench/harness.py:106`) has no
convention parameter, and `Subbench.expectation`
(`pcrecbench/subbench.py:268`) is keyed on `(pattern, subject_id,
regime)` only — every testee in a cell is graded against one
canonical, `perl-leftmost-first` expectation row. **v1's family 11 is
therefore scoped to the shared-convention population**: pcre2-interp,
pcre2-jit and pcrec, all `perl-leftmost-first` (§5.6's own table), plus
`pcre2-dfa` once its decreasing-length-order difference is confirmed
not to change the leftmost-first answer on family 11's own cases. The
cross-convention value family 11 is named for — scoring `re2-longest`
or `tre-default` against their OWN correct answer — is DEFERRED to
whichever lane lands the first divergent-convention testee (§8, both
`later`), and building the missing per-testee/variant expectation
override is that lane's own scope, not v1's. This is a design amendment
this note makes on its own logic (CB1's disposition: "answerable inside
the design's own logic... does not require a Frank-level ruling"), not
a Frank ruling — see §12's new question, which states it for the record
rather than deciding it silently.

**Family 12's `canonical_text` (S10).** Family 12's designed members
are byte-class and high-byte literal shapes whose canonical pattern
text may not be valid UTF-8. `patterns[].canonical_text` is a JSON
string (`schema/record.schema.json:92,302`) and cannot losslessly hold
an arbitrary non-UTF-8 byte sequence. It is not in the pattern entry's
required-field list, so the same omission escape hatch KB-7/[B30]
already established for an oversized pattern applies here for a
different reason (encoding validity, not size): **a family-12 pattern
whose canonical text is not valid UTF-8 omits `canonical_text` in the
record, citing `canonical_sha256` for identity instead.**

### 3.2 Why twelve families and sixty patterns

- Sixty is chosen against the cell-time budget (§3.5), not the other way
  round. The census is 95 patterns at ~47-52 min/cell with three regimes;
  60 patterns at two regimes lands comfortably inside `CELL_CAP`.
- The 6 / 5 / 1 split (six wild families, five capability/hazard families,
  one floor) puts the wild share at 30 of 59 members. **This is no
  longer a ratio decision** (Frank ruled it moot, 2026-09-12 — §4.3):
  the split is what REALISM produced once each family's members were
  chosen honestly, not a target hit by construction.
- Every family has at least one CONTROL PAIR, following the census's own
  lesson that "an outlier without its control is not a question, it is a
  number" (`bench/syntax/CLAUDE.md`, thing 2). The pairs are named in
  §3.1's "designed members" column.

### 3.3 The floor pattern

`requirements.md §5` requires one per short-subject search set. Proposal:
a single literal byte that occurs rarely in the subject vocabulary, in
the census's own idiom (`bench/syntax` uses `#`). The exact byte is the
authoring lane's, chosen so the floor is a full-length MISS on every
throughput run and a hit on 1-2 short subjects — the three readings
`bench/syntax/NOTES.md` names under "The floor pattern".

### 3.4 Subjects

**Thirty-six typed short subjects** (the `search_short` regime) plus
**three throughput runs** (64 KB / 256 KB / 1 MB), by the census's own
shape and for its stated reason: a size sweep at fixed hit density gives
one per-byte number per pattern plus the statement that the number is
flat in subject length (`bench/syntax/NOTES.md`, "Regimes").

- The short subjects are **typed per family**, not drawn: each is at
  least one family member's designed hit and, where a family has a
  semantic edge, another member's designed miss. That is the census's
  discipline and it is what makes `semantics-divergence` measurable at
  all (the divergence shows up as two engines' different-but-correct
  answers on ONE typed subject).
- The throughput runs come from a **set-local grammar module**
  (`captext.py`, in the shape of `bench/syntax/censustext.py`) mixing
  log-line, HTTP-request-ish, source-code and prose parts so every family
  has sparse hits on a background where most candidate starts fail.
- **The grok family does NOT reuse `bench/loglines`' subjects.** N1 §10
  raises this as a design question. Decision: no. Reasons: (a) a
  sub-bench's subjects are part of its `content_hash` and its version
  (`subbench_directory_model.md §1.3`), so sharing a subject tree couples
  two sets' version lifetimes; (b) loglines' subjects are shaped around
  PCRE2's required-code-unit dismissal, which is loglines' axis, not
  this one; (c) the capability set's subjects must carry non-UTF-8 bytes
  for family 12, which loglines' do not.
- **Subject provenance is SYNTHETIC** — see §4.4 for the decision, its
  two alternatives, and what it costs.

### 3.5 Regimes, and the cell-time arithmetic

**DECISION: `search_short` + `throughput` in v1. NOT `match`.**

`requirements.md §3` makes a declared subset legitimate and `loglines`
already exercises the precedent (`bench/CLAUDE.md`: "a sub-bench declares
WHICH REGIMES it exercises and a SUBSET is legitimate").

Why `match` is out of v1, with the alternative stated:

- The `match-compliance` regime reaches a testee with no end-anchored
  mode through a LEXICAL whole-subject wrapper, `(?:<pattern>)\z`
  (`record_schema.md §5` ADDITIONS 3). The syntax census's first sample
  found that wrapper producing three distinct wrong results from one
  cause — `(?R)` recursing into the wrapper, `\K` unable to report a
  non-zero start, and a `(?x)` comment swallowing the `)\z` so the
  pattern does not compile at all — ranked **Tier A, Q2 and Q3** of
  `docs/dev/ledgers/2026-09-07-b36-syntax-first-d34c9131.md` §9, i.e. "the
  instrument; nothing below this is trustworthy until these are
  answered".
- Families 6 (`(?x)`) and 9 (recursion) would inherit that defect
  directly — both failure modes are named in the cited ledger's Q3,
  under the one lexical-wrapper cause. **Families 7 and 8 are corrected
  out of this list (CS1):** the ledger's Q2 (`\K` unable to report a
  non-zero start) is a SEPARATE finding from Q3, and its own "Source"
  line attributes it to `testees/pcrec/driver.c`'s anchored branch
  hard-coding `first_s = 0` — a pcrec-specific driver bug, not a lexical
  consequence of the wrapper the way `(?x)`'s comment-eating and `(?R)`'s
  recursion are. Neither family 7 (`cap-backref`) nor family 8
  (`cap-lookaround`)'s designed-member roster names a `\K`-bearing
  member, so their exclusion needs its own reason if one is ever
  claimed. Family 11 (`$` vs `\z`, the wrapper's own anchor) is
  unaffected by this correction and stays excluded on its own grounds.
- **Scope, stated explicitly (CS1):** this exclusion is deliberately
  SET-WIDE, not pcrec-specific, even though the two confirmed defects
  (family 6, family 9) and the corrected-out one (family 7/8's `\K`
  case) are all properties of pcrec's own lexical wrapper. The harness
  declares regimes per SUB-BENCH, not per testee (`bench/CLAUDE.md`), so
  scoping `match` to "every testee except pcrec" would need a harness
  change this design does not propose. The tradeoff this accepts: most
  [B7] roster engines (RE2's `FullMatch`, likely Oniguruma's/TRE's own
  anchor options) have a native anchored-match call and would not need
  pcrec's lexical wrapper at all, so this decision forecloses
  `match`-regime compliance measurement (family 1's own stated purpose)
  for every future non-pcrec engine too, on a defect only one testee
  structurally has. That tradeoff is accepted for v1 rather than
  building a per-testee regime carve-out; a future revision could name
  the harness change as its own lane if the cost is judged worth
  paying.
- **The alternative** — declare `match` anyway and accept the R0 cells —
  buys compliance-shaped readings for family 1 (validators) at the price
  of pre-known wrong answers in four families and roughly doubled cell
  time.
- **The consequence of the decision:** the set cannot answer "is this
  input compliant" at the whole-string grain in v1. `bench/email` already
  answers that question for one real-world family. A `capability@0.2`
  adds `match` once Tier A Q2/Q3 close — that is the stated trigger, and
  it is one sidecar line plus an expectation re-derivation, not a
  redesign. **This is §12 Q5, defaultable.**

**The arithmetic**, following `bench/syntax/NOTES.md`'s own model and its
premise (the harness calibrates each (pattern, regime) loop so the median
subject's loop is 50 ms, so a (pattern, regime, trial) costs ≈ 50 ms ×
n_subjects and is INDEPENDENT of the testee's speed):

| term | arithmetic | per cell |
|---|---|---|
| `search_short` | 60 patterns × 1 regime × 6 passes (1 probe + 5 trials) × (50 ms × 36 subjects ≈ 1.8 s) | **~11 min** |
| `throughput`, 6 passes × 60 patterns over 1.3 MB | 2-100 ms per pass for most; the class-run and wide-alternation members up to ~1 s per pass on an interpreter | ~2-8 min |
| pcrec compile, ONE form × 60 (no `whole-subject` form without the `match` regime) | ~1-3 s each | ~1-3 min, compiled testees only |

**Estimate: ~15 min per `pcre2-*` cell, ~18 min per pcrec cell.**

Calibration points, both measured, both in `scripts/CLAUDE.md`'s table
at pin `1989c62`: `loglines@0.1` (11 patterns, 1 regime + throughput)
measured **9.1 min** per pcre2 cell; `bounded@0.3` (42 patterns, all
three regimes, a long ladder) measured **42-49 min**. Sixty patterns at
two regimes sitting between them at ~15-18 min is consistent with both.
Against `CELL_CAP`'s 5,400 s default that is **~5× headroom** — the
largest margin of any set in the repo, deliberately, because a capability
set's refusal arms and its wide `wild-datetime` compiles are the least
predictable cells here.

**Six pinned testees ≈ 1.7 h**, which fits a single window with room for
a re-measure (the v1.4 spread rule's re-measure-once contract,
`scripts/run_window.sh`).

**Family 10's calibration risk, stated explicitly (CB8).** The
arithmetic above assumes a (pattern, regime, trial) costs `50 ms ×
n_subjects`, INDEPENDENT of the testee's speed, validated on
`bench/syntax`'s deliberately homogeneous population (one construct, one
plain body, no subject engineered to be asymptotically slower than its
siblings). Family 10 (`redos-nested`) is the opposite by design: a
subject engineered to be catastrophically slow on a backtracker and fast
on everything else, and `pcre2-interp`/`pcre2-jit` — both backtrackers —
are in the v1 first-sample roster (§11.4). `calibrate()`
(`pcrecbench/harness.py:290-343`) picks `iters` ONCE from the MEDIAN
subject's per-iteration cost and applies it uniformly across the whole
(pattern, regime) loop; a ReDoS witness's own per-iteration cost, far
above the median, then runs for `iters × its_own_per_iter_cost`, not the
model's ~50 ms — that one subject's total, not the cell's assumed total,
can dominate. **Mitigation adopted:** family 10's typed subjects use a
fixed, small `--iters` override (`harness.py:296` already supports a
non-calibrated `iters`) rather than `search_short`'s calibrated
probe-then-scale loop, sized by L3 against the worst ReDoS witness on
`pcre2-interp` specifically. This is stated here rather than left to be
discovered as the most likely single cause of a `CELL_CAP` timeout in
v1's first run (§13 R6 carries the risk forward).

---

## 4. Provenance

### 4.1 The per-pattern provenance record

A closed set of fields, one row per pattern, in the sidecar's
`[[patterns]]` entry and re-derived into a committed `provenance.tsv`:

| field | type | required | what it is |
|---|---|---|---|
| `source_name` | slug | R | a registered source slug (`owasp-validation`, `grok`, `crs`, `rebar-wild`, `pcre2-testdata`, `rust-regex-testdata`, `oniguruma-test`, `re2-bench`, `vscode-json-grammar`, `cve`, `authored`) |
| `source_url` | string | R | the exact URL fetched, raw where a raw URL exists |
| `source_ref` | string | c | the file/rule/line inside the source (`rules/REQUEST-942-APPLICATION-ATTACK-SQLI.conf#942160`); required unless `source_name = authored` |
| `licence` | SPDX id | R | from the source's own LICENSE/COPYING, fetched; `n-a` for `authored` |
| `licence_note` | string | o | required where a source's licence metadata disagrees with itself (the Davis Zenodo/GitHub mismatch, §4.5) |
| `retrieved_utc` | RFC 3339 | R | the date of the fetch that produced THIS text |
| `fidelity` | enum | R | `verbatim` / `adapted` / `inspired` |
| `adaptation` | string | c | required when `fidelity ≠ verbatim`: what changed and why, in one sentence a reviewer can check against the source |
| `attribution` | string | c | required when the licence demands it (CC BY-SA 4.0 — N1 §9) |

`fidelity`'s three values, precisely:

- **`verbatim`** — the pattern text is byte-identical to the source's.
- **`adapted`** — a mechanical, stated change to a verbatim original: a
  ModSecurity transformation chain dropped, a `%{NAME}` grok macro
  expanded, a multi-line `(?x)` body flattened to one line (now an OPEN
  question for Frank at the restart, `rxt_needs_v1.md` F-Q2 — §9). The
  `adaptation` sentence names which.
- **`inspired`** — AUTHORED fresh from a description, never copied. This
  is the value that makes families 10 and 12 possible without a licence
  question: a ReDoS shape written from a CVE's prose description is our
  text, and the CVE is cited as the reason it exists, not as its source.

**Why a closed field set rather than free prose in `description`:** N3
§1.3 establishes that `.rxt` has NO pattern-level provenance production
in any wave, and that its only prose home today (`description`, W1, one
line in a pattern block) is prose. A reviewer checking sixty attributions
against sixty prose sentences is the failure mode `provenance.tsv`
exists to close — the same argument `bench/syntax`'s `coverage.tsv`
makes for its seed.

**Where it is CHECKED:** `gen_provenance.py --check` re-derives
`provenance.tsv` from the sidecar and fails by name on: a pattern with no
provenance row; a `fidelity ≠ verbatim` row with no `adaptation`; a
licence outside the allowlist (§4.2); a CC BY-SA row with no
`attribution`; **and, per Frank's 2026-09-12 Q1 ruling, an `inspired`
pattern that fails a mechanical similarity check against its cited
source** (a normalized-text similarity score above a stated threshold
fails the gate by name, plus a human review pass — the ruling's own
mitigation for R8, "`fidelity: inspired` becomes a laundering
mechanism", folded in here rather than carried forward as an open risk).
This is the generic `gen_*.py --check` hook `make check-harness` already
runs over every `bench/*/` directory by enumeration
(`bench/CLAUDE.md`), so it costs no new harness machinery beyond the one
new check.

**What the RECORD carries (CB3, revised).** §0.1's original claim — that
`patterns[].tags` (`src:<source_name>` / `fid:<fidelity>`) buckets wild
against designed "without a schema MINOR" — is WRONG. `patterns[].tags`
is DIAGNOSTIC (`record_schema.md:841-846`, the field-table preamble
governing the row at `record_schema.md:1025`): "DIAGNOSTIC /
REPRODUCIBILITY-ONLY fields are free text... and the reporter must NOT
offer them as filters." Bucketing wild-vs-designed IS filtering/grouping
— the one operation the field's own rule forbids. Worse, the identical
mechanism already exists and is already dead: `pcrecbench/record.py:
215-221` writes `tier:<feature_tier>` and `convention:<convention>` into
`patterns[].tags` on every record today, and the reporter has never once
read a `patterns[].tags` value for either existing family. **Revised
decision: promote provenance bucketing to real enumerated, FILTERABLE
schema fields** — `patterns[].provenance_source` (a closed slug enum,
the same vocabulary as `source_name` above) and `patterns[].fidelity`
(the closed three-value enum §4.1 already defines in substance). This
**IS a schema MINOR** (contradicting v0.1's "no schema change" claim and
§1.1's traceability row for requirement (1), both corrected). The full
provenance row (URL, licence, attribution, `adaptation`) stays in the
set directory, which is where the sub-bench's own truth lives; the
record's `subbench.content_hash` covers it because it covers every
committed file in the directory (`subbench_directory_model.md §1.3`).
The two promoted record fields exist so a REPORT can bucket wild against
designed; the full row is never duplicated into the record.

### 4.2 The licensing floor — options and recommendation

N1's survey splits eighteen sources three ways: permissive-confirmed,
copyleft (GNU grep, **GPLv3, `COPYING` fetched directly** — N1 §17), and
genuinely unknown (regexlib.com, regex101's library, Suricata rules by
sid range, TextMate grammars per-repo). N1 §(v)1 puts the ruling to
Frank. The three options, each with its consequence:

| option | rule | consequence |
|---|---|---|
| **(a) permissive-confirmed only** | verbatim import only from a source whose LICENSE/COPYING was fetched directly and is on an allowlist | grep's BRE/ERE + Turkish-I fold corpus is OUT as a verbatim source; Suricata is OUT until a per-sid audit; regexlib/regex101 are OUT. Six families are unaffected (their sources are all confirmed permissive) |
| **(b) small-number individual attribution regardless of repo licence** | a handful of individually-attributed, individually-quoted patterns is fair research use whatever the repo says | brings grep's locale fold tests and Suricata rules into reach; puts this repo in the position of asserting a legal judgment it is not equipped to make, on someone else's copyleft |
| **(c) hybrid — (a) for verbatim, `inspired` for everything else** | verbatim import per (a); a non-allowlisted source may be cited as INSPIRATION for a freshly-authored pattern (`fidelity: inspired`), never copied, AND validated as not an actual copy (a mechanical similarity check in the provenance gate, plus review) | **RULED (c) — Frank, live, 2026-09-12** |

**RULED: (c), with the similarity-check addition above.** It costs nothing the
`fidelity: inspired` machinery already has to exist for families 10 and
12 (CVE descriptions and the un-obtainable Suricata sample), and every
family whose value is real-use EVIDENCE — the Turkish dotless-ı fold
divergence, a `pcre:` rule's byte-offset shape — is expressible as an
authored pattern with the source cited as the reason. The allowlist:

**Allowed for verbatim import** (each licence fetched directly, per N1's
own follow-up): Unlicense (rebar), MIT (rust-lang/regex, mariomka,
`vuln-regex-detector`, VS Code), BSD-2-Clause (Oniguruma), BSD-3-Clause
(RE2, Hyperscan/Vectorscan), BSD-3-Clause-WITH-PCRE2-exception (PCRE2
testdata), Apache-2.0 (Elastic grok, OWASP CRS), CC BY-SA 4.0 (OWASP
Validation Repository — **with the `attribution` field populated**, which
is why that field exists).

**Never verbatim:** GPLv3 (GNU grep — copyleft, and this repo carries no
GPL obligation); any source whose terms this project could not fetch
(regexlib.com, regex101's library, Suricata rules whose sid range was not
individually audited).

**Consequence of (a) instead:** family 12's authored members would lose
their stated inspiration and become unmotivated toys; the Turkish fold
case is simply lost. **Consequence of (b) instead:** faster import, a
legal exposure nobody in this project is qualified to size, and a
precedent that outlives the set.

### 4.3 Wild vs designed — REALISM, not a ratio (RULED)

N1 §(v)2 put a ratio question to Frank ("a number or rough ratio would
help size phase (e)"). **Frank ruled, live, 2026-09-12: it is not a
ratio.** The "from the wild" requirement is a FRAMING — realism over
contrivance. No `ab+c`-class toy is a set member, whether imported or
authored: **every member, wild or designed, must be a shape someone
would plausibly deploy.** Provenance is recorded where a real source
exists (§4.1); where none does — families 7-12's designed members, the
control twins inside families 1-6 — the pattern must still be the kind
of thing a real regex author would write for that purpose, not a
constructed edge case whose only job is to be hard. **The actual
percentage is not important**, and this note no longer sizes the set
against one.

**Consequence for §3.1's roster, stated plainly:** the 30-wild/29-designed
split that fell out of building each family honestly (§3.2) is kept, but
it is now a DESCRIPTION of what the set turned out to contain, not a
target that was hit. Every authored member in families 7-12 — the
doubled-word and palindrome backreference shapes, the chained-lookaround
cases, the balanced-paren recursion shapes, the CVE-inspired ReDoS
witnesses, the byte-class non-UTF-8 literals — is held to the SAME
realism rule as the imported members of families 1-6: each is a
plausible thing a working regex author would write to exercise that
capability, not a toy built to be refused. L2 (§11.1) authors against
this rule, and its blinding statement in `NOTES.md` should say so.

**The Davis et al. corpus** stays a `capability@0.2` candidate (§4.5),
unchanged by this ruling — the ruling settles the ratio question Davis's
count was meant to help size, not whether Davis itself is worth
importing.

### 4.4 Subject-data provenance

N1 §(v)3's two options, plus the decision:

| option | what it means | consequence |
|---|---|---|
| **(a) synthetic, typed, generated with a manifest** | what all five existing sets do | **RECOMMENDED.** The set claims wild PATTERNS, not wild DATA, and `NOTES.md` says so in those words |
| (b) a licence-clear public corpus per family | CPython source for family 6, a public pcap for family 12, OpenSubtitles for prose | rebar does this and its own README shows the cost: the OpenSubtitles haystacks' upstream terms are **not independently resolved even by rebar** (N1 §1, `haystacks/opensubtitles/README.md` fetched) — the set would inherit an unresolved licence question in its *data*, where the manifest and the `content_hash` make it permanent |

**RECOMMENDATION: (a), with one stated limitation.** Deterministic
generation with a committed sha256 manifest is the existing discipline
(`requirements.md §5`: "generated deterministically by a script with a
committed manifest by default, real corpora only when licensing is
clean"), it is what `make check` already verifies byte-for-byte for every
set by enumeration, and it is the only option under which family 12's
non-UTF-8 subjects are constructible at all.

**The limitation, stated plainly in `NOTES.md`:** a wild pattern over
synthetic text measures the pattern's structure against a background we
chose. A pattern whose real cost depends on its real haystack's
statistics — CRS rules against real HTTP bodies above all — is measured
here against a background that resembles one. That is a weaker claim than
"wild data too" and the set must not be read as making the stronger one.

### 4.5 The Davis et al. corpus specifically

N1 §12 (as rewritten by `b42wild2`) establishes: the artifact is
<https://doi.org/10.5281/zenodo.3257777>, backed by
`VTLeeLab/LinguaFranca-FSE19`, 34.1 MB, NDJSON, 537,806 regexes from
~200,000 projects in 8 languages. Two facts and one gap matter:

1. **The licence mismatch is real.** Zenodo's own licence FIELD reads
   "Other (Open)" with no description; the backing GitHub repo carries an
   MIT `LICENSE`. N1 could not settle which governs and says so.
2. **Per-regex provenance may not survive.** The README confirms the
   extraction method but does NOT document a per-regex field carrying the
   source project/file. If the NDJSON rows carry only pattern text and
   target language, requirement (1)'s "provenance recorded per pattern"
   degrades to LANGUAGE-level provenance for every Davis-derived row.
3. **The zip is unopened.** N1 marks this OWED and names it as the first
   move any lane makes on this source.

**RECOMMENDATION: Davis is OUT of v1, named as the first candidate for
v0.2.** Reasons: the set reaches sixty patterns without it (§3.1); every
other source is already fetched and quotable; and admitting it requires a
download-and-inspect lane whose FIRST finding might be that the
provenance requirement cannot be met. Deferring costs nothing and
removes the set's single largest unknown from the critical path.

**If Frank rules it IN for v1**, the sampling protocol is:

| step | rule |
|---|---|
| licence | treat the GitHub repo's **MIT** as governing; record `licence = MIT` and `licence_note = "Zenodo record 3257777's own licence field reads 'Other (Open)'; the backing repo VTLeeLab/LinguaFranca-FSE19 states MIT"`. Both facts travel with every row |
| schema inspection FIRST | no pattern is admitted until the zip's NDJSON schema is read and the per-record fields listed in the lane's report. If project-level provenance is absent, every Davis row is `fidelity: adapted`, `source_ref = "language=<lang>"`, and `NOTES.md` states that these rows carry weaker provenance than the rest |
| stratify | by the §5 REQUIRES tags, not by language: one stratum per tag, so the sample covers the capability axis the set exists to measure rather than the popularity distribution |
| deduplicate | by sha256 of the NORMALIZED pattern text (trailing-whitespace-stripped, delimiters removed); the corpus mines ~200 k projects and near-duplicate validators are its most common row |
| size-bound | reject pattern text > 4 KiB. The record's `free_text` cap is 1 MiB (`record_schema.md` v1.5, KB-7) so this is a cell-time bound, not a schema one: a 4 KiB pattern already exceeds `altwide`'s `s-4096` in spirit and belongs in that set's ladder, not here |
| cap the count | **≤ 10 Davis-derived patterns**, so the set does not rest on an unresolved licence mismatch |

---

## 5. The capability model

### 5.1 The closed REQUIRES vocabulary

Derived from N2 §3's per-engine table and N2 §7 item 5, with four
additions this note makes explicit (marked †) because N2's own table
distinguishes them and its tag list did not:

| tag | what a pattern needs | engines that do NOT satisfy it (N2 §3) |
|---|---|---|
| `backrefs` | a backreference, numbered or named | RE2, Rust `regex`, Vectorscan |
| `lookaround` | any lookahead or lookbehind | RE2, Rust, Vectorscan, TRE |
| `lookbehind-variable` † | a lookbehind whose body is not fixed-width | + python `re` (CPython 3.14 docs, N2 §8 (8)) |
| `possessive-quantifier` (CB5, split from `atomic-possessive`) | `x*+`, `x++`, `x?+`, `x{n,m}+` | RE2, Rust, Vectorscan, TRE. Oniguruma HAS these — flag-confirmed in `regsyntax.c` (`ONIG_SYN_OP2_PLUS_POSSESSIVE_REPEAT`/`_INTERVAL`, N2 §4 (4)) |
| `atomic-group` (CB5, split from `atomic-possessive`) | `(?>...)` | RE2, Rust, Vectorscan, TRE. **Oniguruma's support is UNCONFIRMED at the evidence quality of the row above**: `(?>...)` is "not controlled by a distinct op2 flag... not independently re-derived from the group-parser source" (N2 §4 (4)) — a wrong-direction risk (a wrongly-CLAIMED capability, which §5.3's fail-closed default does nothing to protect against, unlike a wrongly-UNCLAIMED one). **Before an `onig-*` config declares `atomic-group`, its support must be independently re-derived from `regparse.c`** — Oniguruma is not in v1's roster (§8, `later`), so this does not block L1-L5 or the first sample |
| `recursion` | `(?R)`, `(?1)`, `(?&name)`, `\g<n>`, `(?P>name)` | RE2, Rust, Vectorscan, TRE, python `re` |
| `conditionals` | `(?(cond)yes\|no)` | RE2, Rust, Vectorscan, TRE, python `re` |
| `k-reset` | `\K` | RE2, Rust, Vectorscan, TRE, python `re`, **and `pcre2_dfa_match`** (man `pcre2matching` item 4, N2 §4 (3)). **Oniguruma is deliberately NOT listed here (CB6) and must not be read as satisfying it by omission**: N2 states Oniguruma has "not general PCRE-style `\K`; has its own reset-point extensions under some syntaxes" — neither a clean yes nor a clean no. **Before an `onig-*` config declares `k-reset`, this must be resolved**: either confirm behavioral equivalence to `\K` for this bench's own family 7-9 `\K`-tagged patterns, or declare `k-reset: false` for Oniguruma and route those patterns to `unsupported-by-declaration`. Not in v1's roster, so not before L6b |
| `control-verbs` † | `(*ACCEPT)`, `(*SKIP)`, `(*PRUNE)`, … | RE2, Rust, Vectorscan, TRE, python `re`; `pcre2_dfa_match` supports `(*FAIL)` only (item 7) |
| `unicode-properties` | `\p{...}` / `\P{...}` | TRE (locale classes, not properties); python `re` spells Unicode categories differently and has no `\p{Greek}` token |
| `named-groups` † | any named-group spelling | TRE — **UNCONFIRMED (CS5)**: N2 §3's table has no column for named-group spelling at all; neither research note states this for TRE. The natural primary source is POSIX ERE's own grammar (TRE's default mode), not yet cited. Route through §5.3's witness-refusal check either way before an `onig-*`/`tre-default` config declares it |
| `free-spacing` † | `(?x)` / extended mode | TRE — **UNCONFIRMED (CS5)**, same gap and same remedy as `named-groups` above |
| `callouts` | `(?C1)` and friends | everything but pcre2/perl |
| `span-reporting` | the driver must report a match START, not just "matched" | **Vectorscan without `HS_FLAG_SOM_LEFTMOST`** (N2 §4) |
| `non-utf8-subject` | the subject bytes are not valid UTF-8 | Rust `regex`'s default `str` API (N1 §ii) |
| `captures` | the engine must report capture spans | `pcre2_dfa_match` ("no captured substrings are available", man `pcre2matching` item 2) |

**The vocabulary is CLOSED and validated at set load.** A tag outside it
is a load error naming the closed set — the same discipline
`docs/dev/predictions/CLAUDE.md` states for the prediction format's
closed sets, and the same reason: a typo that silently becomes a new tag
is a capability claim nobody checked.

**Note the two rows that are NOT about an exotic construct.**
`span-reporting` and `captures` are capability lines the roster crosses on
its *execution model*, not its syntax — which is why `pcre2-dfa` (§8) is
a genuinely interesting fourth pcre2 testee and not a curiosity.

### 5.2 Per-engine capability declarations

**DECISION: declared PER CONFIG, in the adapter's own directory, not per
engine.**

The alternatives: per ENGINE (one table per `testees/<engine>/`), or per
CONFIG (a key on each entry in `testees/<engine>/configs.toml`).

Per-config wins on evidence, not taste: `pcre2-dfa` and `pcre2-interp`
are the same library at the same version and satisfy different tag sets
(no `captures`, no `k-reset`, no `backrefs`, no `control-verbs` beyond
`(*FAIL)` for the DFA-match path — man `pcre2matching`'s eight-item list,
quoted in full at N2 §4 (3)). A `vectorscan-block-nosom` config would
likewise differ from `vectorscan-block-som` on `span-reporting` alone
(N2 §4). Per-engine declaration cannot express either.

Shape: `capabilities = ["backrefs", "lookaround", ...]` on each config
entry, listing the tags that config SATISFIES. Absent ⇒ the config
satisfies nothing and every tagged pattern is `unsupported-by-declaration`
— a fail-closed default, deliberately, so a new adapter cannot
accidentally claim capabilities by omission.

### 5.3 The pre-compile policy

> **REQUIRES(pattern) ⊄ capabilities(config) ⇒ `unsupported-by-declaration`,
> decided BEFORE any compile is attempted.**

This turns N2 §3's whole table into executable policy rather than prose a
reviewer re-checks by hand every time the roster grows (N2 §7 item 5's
own argument).

The record shape is already defined and needs nothing new: the compile
row carries `compile_outcome = "unsupported-by-declaration"` and
`declaration_ref`, which is REQUIRED for that outcome precisely so the
outcome cites the note rather than being "an unfalsifiable excuse"
(`record_schema.md §8`, compile table). The `declaration_ref` value is
the sidecar's engine-notes row for that (pattern, testee).

**Why pre-compile rather than post-refusal:** an engine that refuses a
backreference reports a SYNTAX error indistinguishable, at the string
level, from a typo (Hyperscan and perl give free text only — N2 §3's
"structural observation"). Deciding from OUR declaration means the
outcome is the same whether the engine's message is a closed enum or
prose, and it means a NEW engine's first run does not depend on
string-matching its diagnostics.

**What it costs:** a declaration that is WRONG (we say an engine lacks a
capability it has) silently converts a measurable cell into an
`unsupported` row. The mitigation is a `make check` arm: for each
(config, tag) pair declared UNSATISFIED, one witness pattern is actually
compiled and the refusal asserted by name — the same "a check with no
failing case proves nothing" discipline `record_schema.md §9` states for
X1..X33 and `make check-harness` already applies to pcrec's deny flags.

**Noted, not a defect (B7):** `compile_outcome = "unsupported-by-
declaration"` is schema-legal today (`schema/record.schema.json:122,
690-692`) but no adapter or the harness has ever produced it as a value
— it is described in `report.py`'s prose only. `testee.conventions`
(§5.6) is likewise required on every record today but never read by any
validator rule or reducer. **This design is the first real producer of
both.** Neither is a defect; both are exactly the kind of first-class
capability this design elsewhere states it is exercising for the first
time (§5.6, §9). It means the witness-check arm above carries extra
weight: its POSITIVE case (a real `unsupported-by-declaration` compile
row surviving `store.write()`) has never existed in the store before.

### 5.4 Outcome enums — adopt N2's finding, no new value

N2 §7 argues the existing enums are wide enough. **ADOPTED**, with the
reasoning re-derived rather than taken on trust:

| new shape N2 found | where it lands | why no new enum value |
|---|---|---|
| a SIZE/LIMIT refusal (Rust's `CompiledTooBig(usize)`, RE2's `ErrorPatternTooLarge`) | `did-not-compile` + a `refusal_class` engine_metadata pair (§5.5) | pcrec's own emitted-size cap already lands on `did-not-compile` in this repo's practice ([B22]'s size-cap rung). A second spelling for the same outcome would split existing records from new ones |
| a graceful runtime DEGRADE (RE2's DFA-cache flush under `max_mem`; Rust's `dfa_size_limit` engine switch) | `engine_metadata`, `match` scope — NOT an outcome | it is MECHANISM, which is exactly what `requirements.md §4.2` says `engine_metadata` is for ("bucket outliers by MECHANISM"). Nothing failed; a different internal engine answered |
| a REQUIRES miss | `unsupported-by-declaration` (§5.3) | the enum value exists for this and its `declaration_ref` requirement is already written |

**The one place this is worth re-testing in the panel:** `gave-up`
(per-subject) was added at schema v1.1 for an engine refusing a subject
on its OWN resource limit, "with the engine's code in the diagnostic"
(`requirements.md §4.4`). Oniguruma's `ONIGERR_RETRY_LIMIT_IN_MATCH_OVER`
(-17) and `ONIGERR_MATCH_STACK_LIMIT_OVER` (-15) are exactly that shape
(N2 §4 (4)) and are what an `onig-lowretry` config exists to produce
(§8). So `gave-up` gains a second engine and needs no change — but a
panel should check that claim against the enum's wording rather than
accept it here.

### 5.5 The `refusal_class` engine_metadata pair

Per N2 §7 item 1, and following `record_schema.md §7`'s three declaration
rules (declare before use; pattern-scope vs match-scope; a mask is an
array of bit names):

    refusal_class : enum { syntax, size-limit, resource-limit }, scope = pattern

**Declared ONLY by a config whose engine gives a closed, structural
signal** — RE2 (`ErrorCode`, the sixteen-value enum quoted verbatim from
`re2.h` at N2 §3), Rust `regex` (`CompiledTooBig` vs `Syntax`), python
`re` (`re.error`'s `.msg`/`.pos`), POSIX/TRE (`REG_*`, incl. `REG_ESPACE`
from `TRE_MAX_RE` overflow — N2 §5), Oniguruma (`ONIGERR_*`). **Never
declared by Vectorscan or perl**, whose refusal is free text only (N2 §3,
§6) — an adapter that cannot populate it honestly must not declare it,
which is `record_schema.md §7` rule 1 read forward.

And `dfa_cache_flushed : enum { yes, no }, scope = match` for RE2, per
N2 §7 item 2, if RE2's API exposes it. **UNVERIFIED**: N2 does not
establish that RE2 reports a cache flush to the caller. The RE2 adapter
lane checks this and, if it does not, declares nothing — a missing
mechanism stamp is honest, an invented one is not.

### 5.6 The three conventions, per case — and Hyperscan's all-ends

`record_schema.md §5` already carries the three tokens as `conventions[]`
(`perl-leftmost-first`, `posix-leftmost-longest`, `all-ends`), and
`requirements.md §7` already says convention is a per-CASE expectation tag
and testees are scored against their own. **Neither claim is a working
mechanism today (CB1):** `outcome_for` (`pcrecbench/harness.py:106`) has
no convention parameter and `Subbench.expectation`
(`pcrecbench/subbench.py:268`) is keyed on `(pattern, subject_id,
regime)` only, so every testee in a cell is graded against one
canonical expectation row regardless of its declared convention. **v1's
family 11 is therefore scoped to the shared-convention population**
(§3.1's note on family 11) — pcre2-interp, pcre2-jit, pcrec, and
`pcre2-dfa` once its decreasing-length-order difference below is
confirmed not to change the answer on family 11's own cases, all
`perl-leftmost-first`. The cross-convention scoring this section
otherwise describes is what family 11 will exercise once a
divergent-convention testee (`re2-longest`, `tre-default`) lands and the
missing per-testee/variant expectation override is built — that lane's
own scope, not v1's.

How each roster engine is tagged (N2 §2):

| engine | convention | note |
|---|---|---|
| pcre2 (interp/jit), perl, python `re`, Oniguruma, pcrec | `perl-leftmost-first` | |
| `pcre2-dfa` | `perl-leftmost-first` at the API shape the driver uses, but it returns ALL matches at one start point in DECREASING length order (man `pcre2matching`, N2 §4 (3)) — the driver takes the first, which is the longest | **this is a real semantic difference the adapter must state**, not a convention token |
| RE2 | `perl-leftmost-first` by default; `posix-leftmost-longest` with `set_longest_match(true)` — a per-COMPILE choice (N2 §2.2) | the `re2-longest` config (§8) is the second reading, and the record says which via `runtime_options` |
| Rust `regex` | `perl-leftmost-first` (the crate's documented claim; **N2 §2.2 flags it as not independently reproduced**) | the set's family 11 subjects are what verify it |
| TRE | `posix-leftmost-longest` | its home dialect |
| Vectorscan | `all-ends` | see below |

**Hyperscan/Vectorscan's all-ends semantics — the options.** N2 §7 item 3
and §8 item 4 put this to Frank. Hyperscan reports EVERY match end-offset
for every pattern in a scan, in an order that may be unordered for
assertion-bearing patterns (`hs_expr_info_t.unordered_matches`, fetched);
the driver protocol's `--find-all` NON-OVERLAPPING count
(`pcrecbench/adapters.py:20-22`) is the wrong shape for it outright.

| option | what it means | consequence |
|---|---|---|
| **(A) span grain via a declared variant** restating the expectation as a SET of end-offsets | the honest reading of what the engine does | needs a THIRD driver invocation mode and a LIST-VALUED row shape — which is **OD-B3**, explicitly unruled (`requirements.md §12`), and a schema change. Large |
| **(B) boolean grain for this engine only** — measure Vectorscan only where the canonical expectation is "does this match anywhere", plus compile/refusal comparisons | cheap, ships now, **grounded directly in the driver protocol (S11)**: the protocol already tolerates a degenerate `subject` line — "START,END the FIRST match's span, **or `-`**" (`pcrecbench/adapters.py`) — so a Vectorscan driver reporting `ANSWER=match/nomatch` with `START=END=-` fits the EXISTING protocol with no new invocation mode. This strengthens, not merely asserts, "cheap, ships now" | **narrows `requirements.md §4.5` constraint 1 ("results identical on EVERY subject") for one engine**. That is a real relaxation of a Frank ruling and must be visible in every report row, not a footnote |
| (C) Vectorscan out of v1 | no relaxation, no schema change | loses the roster's only `simd-multipattern` automaton class and the only engine whose REFUSAL SET is the interesting datum |

**RECOMMENDATION: (B), with a ruling required before the Vectorscan
adapter lane opens — not before the set is built, and not a silent
DEFAULT (CS3).** §5.6's own text above states this narrows an explicit,
dated Frank ruling (`requirements.md §4.5` constraint 1, ADOPTED v3,
2026-08-25: "no variation in results... no 'approximates with stated
differences' grade"). A proposed exception to Frank's own prior word is
not the shape a silent DEFAULT should carry, even though nothing is
built on the answer today. **§12 Q3 is marked BLOCK, asked at the
RESTART** — Vectorscan is not in the v1 first-sample roster (§8, §11)
and the build itself is parked (§9) well before [B7]'s Vectorscan lane
would open, so this costs nothing now.

**One throughput-regime gap this note now states rather than leaves
implicit (S11):** if (B) is ruled, the throughput regime's `NMATCHES`
for an all-ends engine needs an adapter-side reduction to the driver's
own `pos = max(end, pos+1)` non-overlapping rule
(`pcrecbench/adapters.py:20-22`) to produce a comparable count at all —
Hyperscan's natural one-pass "all ends" callback does not produce that
count on its own. If (B) is ruled: the set declares a Vectorscan-scoped
boolean-grain arm in the sidecar's `[testees.<id>]` section, the
reporter shows the grain beside the number the way it already shows
`variant.kind`, and `NOTES.md` states in one sentence that a Vectorscan
cell answers a weaker question than every other cell in its row.

### 5.7 How the scoreboard shows an engine that ran a rewritten spelling

**Corrected (CB2): the write side is built; the RENDER side is not.**
v0.1 stated this section was "Already built and already ruled, needing
only a check at this set's scale" — that is false for `variant.kind`'s
rendering. An exhaustive grep of `pcrecbench/report.py` for `variant`
returns exactly two hits, both unrelated prose; `pcrecbench/reduce.py`
has zero. The only code that touches `variant` at all is
`pcrecbench/record.py:177-187`, the WRITE side (`"variant": None`).
Nothing in this project's five existing sub-benches has ever exercised a
testee variant whose `variant.kind` needed showing, so the render path
was never built to begin with.

- `patterns[].variant` is REQUIRED on every pattern entry and is `null`
  when the testee ran the canonical text — "a variant is never a silent
  fork; the record states one either way" (`record_schema.md §8`). **This
  half is built.**
- `variant.kind` (`syntax-only` / `restructured`) is informational
  (OD-B5) and `requirements.md §4.5`'s closing sentence describes an
  intended rendering rule for it. **This half is UNBUILT.**
- **The build task, restated and re-sized:** every existing sub-bench
  runs zero or a handful of variants; this one will run many (§6). L5
  (§11) must **design and build** the `variant.kind` rendering from
  nothing — not merely check an existing path at scale — and validate it
  against a synthetic many-variant report BEFORE the set ships. Its
  absence would silently make every one of family 2, 6, 7, 8's designed
  control-twin variants invisible in a rendered report table.

---

## 6. Per-engine spelling variants

### 6.1 Where a variant lives

**Today: the sidecar's `[testees.<id>]` section** — `variant`,
`variant_kind`, `objective_preserved`, `capture_map`, `options`,
`unsupported` (`subbench_directory_model.md §1.2`, quoting
`harness_contract.md:41-55`).

**Later: `.rxt`'s W3 `variant <testee> <text>` / `variant <testee>
unsupported <reason>` production** — which is NOT BUILT and is "recognised
and refused BY NAME, as NOT IN THIS BUILD" at the current pin (N3 §1.1,
quoting `rxt_format.md:57-62`). The format's own wave table names
"pcrec-bench sub-benches with a non-pcrec testee" as W3's waiting
consumer (N3 §1.1) — i.e. this set is the named trigger.

**Superseded by the Q3 ruling (§9):** where a variant lives at the
restart is one of `rxt_needs_v1.md`'s own asks — its §2.8 proposes a
`variant kind` production plus a quoted `tag` value, precisely to close
the gap this subsection described. Until the restart, variants remain
where they are today (the sidecar's `[testees.<id>]` section, above);
this is a statement of the current shape, not a decision this note
still owns.

### 6.2 The adopted rewrite table

From N2 §6, adopted as written with one column added (the fidelity
consequence):

| rewrite | targets | preserving? | `variant.kind` | equivalence check |
|---|---|---|---|---|
| `\d`/`\w`/`\s` → `[0-9]`/`[A-Za-z0-9_]`/`[ \t\n\r\f\v]` | engines whose default class scope diverges from the canonical pattern's compiled options (RE2 is ASCII by default for these even under UTF-8 — N2 §2.4) | **only if** the canonical pattern did not request Unicode-widened classes. If it did, the rewrite changes the answer set on any non-ASCII digit subject and is NOT a variant | `syntax-only` | oracle on EVERY subject |
| drop a possessive suffix (`x*+` → `x*`) | RE2, Rust, Vectorscan, TRE | **NO on a hazard-class pattern** — see §6.3 | — | refused outright |
| `(?>...)` → `(?:...)` | RE2, Rust, Vectorscan, TRE | same reasoning as possessive | — | refused outright |
| inline-flag placement (`(?i)` at start vs `(?i:...)` scoped) | Oniguruma, TRE, python, perl, RE2 | preserving; a genuine syntax-only re-spelling | `syntax-only` | token-by-token review PLUS an oracle run — inline-flag SCOPE bugs are an observed class of engine divergence (N2 §6) |
| `\h` → `[ \t]` | RE2, Rust, TRE, Oniguruma (varies by syntax profile) | preserving only if the subjects never exercise the wider horizontal-whitespace set `\h` matches under UCP | `restructured` (the answer set COULD diverge on a subject outside this set even where it does not diverge here) | oracle on every subject |
| POSIX bracket classes `[:alpha:]` etc. | near-universal (pcre2, RE2, Oniguruma, TRE, Vectorscan, python, perl) | preserving | `syntax-only` | still oracled — constraint 1 has no low-risk exemption |
| `$` → `\z` for a true-end anchor | every new adapter | this is not a rewrite; it is **this project's own existing whole-subject convention travelling** (`record_schema.md §5` ADDITIONS 3) | n/a | the same check every adapter already passes |

**Two facts that bound the table**, both established in N2's follow-up
rather than assumed: Vectorscan DOES support `\z` (Intel's and
VectorCamp's docs list "the anchors `^`, `$`, `\A`, `\Z` and `\z`",
byte-identical prose on both forks — N2 §6 (6)); **TRE does NOT** — its
parser's escape switch has cases only for `\b`/`\B`/`\<`/`\>`, with no
`z`, `A` or `Z` case at all (N2 §5). So a TRE testee cannot express a
true-end anchor and any pattern requiring one is
`unsupported-by-declaration` for TRE, not a variant. That is a
capability-tag consequence the §5.1 vocabulary should carry — **this note
adds `true-end-anchor` as a sixteenth REQUIRES tag on that evidence.**

### 6.3 The rule: a hazard-class rewrite is not a variant

N2 §6's sharpest finding, adopted verbatim in substance and stated here
as a rule of the set:

> A possessive quantifier or an atomic group in a pattern tagged
> `hazard_class: exponential-backtracking` (or
> `ambiguous-decomposition`) exists SPECIFICALLY to demonstrate the
> engine's own defence against catastrophic backtracking. Dropping it for
> an engine that has no backtracking to defend against is not a rewrite
> that preserves the objective — it is the objective ITSELF being
> answered by construction. Such a pattern is
> `unsupported-by-declaration` for that engine, so the report can say
> "this engine structurally cannot exhibit this hazard" instead of
> implying it was tested and passed.

This is `requirements.md §4.5` constraint 2 applied ("a variant that
reaches the same answers by rewriting the objective AWAY … is not a
variant"). It bites hardest on family 2 (grok's atomic groups, where the
author's own anti-backtracking fix IS the imported artifact) and family
10 (the ReDoS shapes).

**Consequence:** RE2, Rust `regex`, Vectorscan and TRE will show a LARGE
`unsupported-by-declaration` share on families 2, 7, 8, 9 and 10. N2 §6
is explicit that this "is the correct, honest outcome … not a gap to
paper over". The reporter must render it as such — a count, not an
absence.

### 6.4 The equivalence check, and the gate

> **Every declared variant is oracled on EVERY subject the canonical
> pattern is measured on. A rewrite that changes one answer fails the
> build.**

`requirements.md §4.5` constraint 1 with no grades (OD-B5, ruled).

**Where the gate lives:** a `gen_variants.py` in the set directory that
derives a committed `variants.tsv` — one row per (pattern, testee,
subject) carrying the canonical expectation and the variant's oracled
answer — and re-derives it under `--check`. This uses the generic
`gen_*.py --check` hook `make check-harness` already runs over every
`bench/*/` directory by enumeration (`bench/CLAUDE.md`), exactly as
`altwide` uses it for its DERIVED patterns and `syntax` for its coverage
table. No new harness machinery; one new generator.

**The one thing that generator cannot check:** `variant.objective_
preservation` is "REVIEWED text, not machine-checked"
(`record_schema.md §8`). §6.3's rule is what makes the review tractable —
it converts the hardest class of judgment (does this rewrite still
exercise the hazard?) into a mechanical test on `hazard_class`.

---

## 7. Metrics beyond match time

### 7.1 Compile time per execution-model class

`requirements.md §3` rules the shape: compile/setup cost is its own axis,
defined PER EXECUTION-MODEL CLASS, never folded across classes; the
record encodes it as `cost_class` (MUST equal
`setup.testee.execution_model`) and `cost.phases[]` (names and order must
equal `setup.testee.compile_phases`).

Per N2 §5, extended to the roster, with `automaton_class` (a separate,
required fixed enum, `requirements.md:124-128`) stated for every engine
this note can source it for (S9 — v0.1 left it blank for the two new
engines the cited research already answers):

| testee | `execution_model` | `automaton_class` | `compile_phases` | what the timed call actually builds |
|---|---|---|---|---|
| `pcre2-interp` | `interpretive` | `backtracking` | `compile` | the whole compiled pattern |
| `pcre2-jit` | `eager-jit` | `backtracking` | `compile`, `jit-compile` | as above + machine code |
| **`pcre2-dfa`** (new) | `interpretive` | `nfa-simulation` (man `pcre2matching`: "not implemented as a traditional finite state machine") | `compile` | the SAME compiled pattern `pcre2_match` uses — `pcre2_dfa_match` has no separate compile step (N2 §5). **A free control: its compile number should be statistically identical to `pcre2-interp`'s** |
| `pcrec` (16 configs) | `compiled-aot` | `hybrid` (already declared, `testees/pcrec/adapter.py:2828`) | `emit-c`, `gcc`/`clang`, `load` | a real compiler + linker |
| RE2 | `eager-jit` † | `nfa-simulation` (a `Prog`, not backtracking) | `compile` | a forward/reverse `Prog`; the runtime DFA is built LAZILY at match time and can be flushed (N2 §5) |
| Rust `regex` | `eager-jit` † | `nfa-simulation` | `compile` | parse + AST + HIR + literal/prefilter analysis; the lazy DFA is built at match time (N2 §5) |
| Oniguruma | `interpretive` | `backtracking` (N2 §2.1's own match-strategy read) | `compile` | `onig_new` builds the FULL internal program eagerly — the closest fit to pcre2-interp's own definition (N2 §5) |
| TRE | `interpretive` | `nfa-simulation` — "a tagged-NFA / bit-parallel simulation... not literal backtracking, so it shares RE2/Rust's 'no catastrophic backtracking' property" (`2026-09-12-b42-engine-landscape.md:168-176`) | `compile` | one eager `regcomp` |
| Vectorscan | `eager-jit` † | `simd-multipattern` (the SIMD multi-pattern enum value, not a generic NFA simulation — §7.5's own "roster's only `simd-multipattern` automaton class" is this row) | `compile` | the database IS fully built at compile time — the cleanest `eager-jit` fit of the three † engines (N2 §5) |
| python `re` | `interpretive` | `backtracking` | `compile` | **the driver must bypass CPython's internal pattern cache explicitly**; CPython publishes no numeric cache-size guarantee (N2 §8 (8)) |
| perl | `interpretive` | `backtracking` | `compile` | same caching concern for `qr//` (N2 §5) |

### 7.2 The `cost_class` fifth-token question

N2 §5's recurring finding: RE2, Rust `regex` and Vectorscan all have a
compile call that is EXPENSIVE and TIMEABLE but does not build the full
runtime automaton — a shape the four existing tokens were not defined
against (`requirements.md §3`'s four bullets cite only pcrec and pcre2).

| option | consequence |
|---|---|
| **a fifth token** (`eager-with-lazy-runtime`) | a schema MINOR touching `execution_model` AND `cost_class` (the two must be literally equal, `record_schema.md §8`), the validator, the reporter's class labels, and every report legend. Three engines share the shape, which is the argument FOR |
| **keep `eager-jit` + require the adapter note to say what the timed call does and does not build** | **RECOMMENDED** — costs nothing schema-wise and matches existing practice (`testees/pcre2/CLAUDE.md`'s `consumed_length` paragraph is the precedent: a plain-English convention statement for a testee-specific fact) |

**RECOMMENDATION: the second, with one addition this note makes.** The
record ALREADY carries a required field for exactly this:
`testee.compile_cost_definition`, a required DIAGNOSTIC string, carried
"so a number is never read without its definition"
(`record_schema.md §8`). The addition is a REPORTER rule, not a schema
one: **when one table pools `eager-jit` testees whose
`compile_cost_definition` strings differ, the reporter prints a footnote
naming the differing definitions.** That gives the fifth token's benefit
(the reader cannot silently compare two different quantities) at the cost
of one reporter clause.

**Consequence of the fifth token instead:** cleaner filtering (a query
can select the class directly), at a schema bump plus a migration
question for every existing record — none of which carries the new value,
so `eager-jit` would mean two things depending on record age. That is the
decisive argument against. **§12 Q4, defaultable.**

### 7.3 Artifact / program size, and its non-comparability

| engine | what it can report | source |
|---|---|---|
| pcre2 | `PCRE2_INFO_SIZE`, `PCRE2_INFO_JITSIZE` | already this project's `compiled_size_bytes` |
| RE2 | `ProgramSize()`, `ReverseProgramSize()` — `re2.h`'s own words: "a very approximate measure of a regexp's cost" | N2 §5 |
| Vectorscan | `hs_database_size()`, `hs_serialized_database_size()` | N2 §4 |
| Rust `regex` | **UNAVAILABLE.** `regex_automata::meta::Regex::memory_usage()` exists but the higher-level `regex::Regex` — the type `rure`/`regex-capi` wraps — has no such method, and exposing it means patching upstream `regex-capi` | N2 §5 (7), a CLOSED question, not an unfound one |
| Oniguruma | **NONE.** Confirmed ABSENT by a full re-read of `doc/API`, not merely unfound | N2 §4 (4) |
| TRE | **NONE** | N2 §4 |
| pcrec | `emit_bytes`, `emit_code_bytes`, `artifact_bytes` | already declared (`record_schema.md §7`) |

These are four different definitions of "size": a compiled bytecode
program (RE2, PCRE2), a relocatable database blob (Vectorscan),
comment-excluded generated C source plus a linked `.so` (pcrec).
`requirements.md §3` already rules the posture — "deferred, recorded if
free but not scored".

### 7.4 Peak memory

N2 §5's close is the honest statement and this note adopts it without
softening: the available measurement is `ru_maxrss` of the DRIVER
PROCESS, which measures the whole process (allocator overhead, harness
buffers, interpreter startup) and not the engine's own allocation; pcrec's
AOT artifacts barely allocate at compile time by design.

**RECOMMENDATION (revised, CS4): record `ru_maxrss` for NATIVE-driver
testees only (pcre2, RE2, Rust, Oniguruma, TRE, Vectorscan, pcrec);
never for python or perl; RANK it within the native-driver population.**
v0.1 recorded it native-only for exactly this reasoning — pooling it with
python/perl would compare a process-level number dominated by
interpreter startup against one that is not — and then declared it
"never ranked, on any testee" anyway, with no argument for why
native-vs-native comparison specifically remains unreasonable once the
incomparable population is already excluded. That undermined §1.1's own
traceability claim for requirement (3) ("apples-to-apples where
reasonable... the non-comparable stated"): the native-only cut IS the
apples-to-apples population requirement (3) asks for. **Revised: rank
`ru_maxrss` within the native-driver population**, mirroring how compile
time is ranked "within `cost_class` only" (§7.2). N2 §8 item 7 puts the
scope question to Frank; **§12 Q6, amended (not a silent DEFAULT).**

**Consequence of recording it for python/perl too:** a number dominated
by interpreter startup, sitting in a column beside native numbers, which
a later chart will eventually plot. **Consequence of never recording OR
ranking it:** the one metric that would show RE2's `max_mem` dial doing
anything is present but permanently unranked, which is caveated-and-
shown-only for a metric requirement (3) names as a first-class one.
Native-only-but-ranked is the honest middle.

### 7.5 The summary table — recorded / scored / caveated

| metric | RECORDED | SCORED (ranked) | CAVEAT the report must carry |
|---|---|---|---|
| match time (per-call, `search_short`) | every timed cell | yes, within regime | none beyond the existing N + pass-rate rule |
| match time (per-byte, `throughput`) | every timed cell | yes, within regime | none |
| compile time | every compile row, median of N with spread | yes, **within `cost_class` only** | §7.2's footnote when pooled `eager-jit` definitions differ |
| compile PHASES | pcrec (3), pcre2-jit (2); one phase elsewhere | no — shown, not ranked | phase names differ per testee by construction |
| artifact / program size | where the API gives it (§7.3) | **no** | four incompatible definitions; UNAVAILABLE for Rust, NONE for Oniguruma/TRE |
| peak memory (`ru_maxrss`) | native-driver testees only | yes, **within the native-driver population only** (CS4) | process-level, not engine-level |
| refusal counts (`did-not-compile`, `unsupported-by-declaration`) | every compile row | **not a ranking, a CENSUS** | this set's headline output; §6.3's large `unsupported` shares are a finding, not missing data |
| give-ups (`gave-up`) | every match row that hits an engine limit | no — counted apart | `requirements.md §4.4`: "a give-up is the result the bench most wants to see" |

---

## 8. The option-set roster

Requirement (5). The `testee_id` composition rule is unchanged and
already in use (`record_schema.md §6.4`):

    testee_id = <engine_name> "_" <version_slug> "_" <config_slug>
                              [ "_" <config_extra> ]
    config_slug = <engine_mode> "-" <caps> "-" <simd>

`config_extra` is the escape hatch for two testees differing only in
unfiltered build flags — the mechanism `pcrec-*-bigcap` ([B31]) and the
`-clang` siblings ([B24]) already use.

**Two rows in this table are corrected from v0.1's own "the dial" column
(F5, F6): a column headed "the dial" should hold a genuine space-vs-speed
tradeoff, and two rows in v0.1 held something else.**

| engine | config | v1? | the dial | source |
|---|---|---|---|---|
| libpcre2 | `pcre2-interp` | **v1** (exists) | — | |
| libpcre2 | `pcre2-jit` | **v1** (exists) | JIT vs none | |
| libpcre2 | **`pcre2-dfa`** | **v1 (NEW)** | **NOT A DIAL (F5) — a fourth engine identity that costs nothing.** `pcre2_dfa_match` has no separate compile step (§7.1's own free control: statistically identical to `pcre2-interp`'s) and zero space cost; what it adds is a THIRD execution model and two capability lines (`captures`, `k-reset`) no current testee crosses, `automaton_class = nfa-simulation` (man `pcre2matching`: "it is not implemented as a traditional finite state machine") | N2 §4 (3) |
| pcrec | the sixteen pinned configs | **v1: the six used by every window** (`auto`, `nocaps`, `vm`, `vm-in`, + 2) | **Mapped explicitly, not asserted (F6):** genuine user-facing dials are engine mode (`auto`/`vm`/`nocaps` — `nocaps` removes capture-reporting overhead, a real speed dial) and `cc` (gcc vs clang). The `-bigcap` pair is a capability/size trade in reverse — MORE space to admit compiles that would otherwise refuse, not less space for less speed. `-noedge`/`-noisland`/`-noclsfold` are this project's OWN optimization-denial diagnostic controls, built to isolate a pcrec mechanism for pcrec-bench's measurement purposes, not choices an end user of pcrec would pick between | `testees/pcrec/CLAUDE.md` |
| RE2 | `re2-default` (`max_mem` 8 MiB) | v1 **if** the adapter lands | — | N2 §4 |
| RE2 | `re2-longest` (`set_longest_match(true)`) | v1 **if** the adapter lands | POSIX leftmost-longest — the second convention reading family 11 needs | N2 §2.2 |
| RE2 | `re2-bigmem` (64 MiB) | later | the space dial in reverse (more memory ⇒ fewer DFA cache flushes) | N2 §4 |
| Rust `regex` | `regex-default` | later | — | N2 §4 |
| Rust `regex` | `regex-smallsize` (a LOW `size_limit`) | later | exercises `CompiledTooBig` as a first-class refusal | N2 §4 |
| Oniguruma | `onig-default` | later | — | N2 §4 |
| Oniguruma | `onig-lowretry` (small `onig_set_retry_limit_in_match`) | later | exercises `ONIGERR_RETRY_LIMIT_IN_MATCH_OVER` as a `gave-up` on a ReDoS witness — family 10's natural counterpart | N2 §4 (4) |
| TRE | `tre-default` | later | **no second config is proposable** — TRE offers no space/speed dial at all; its three bounds (`TRE_MAX_RE` 65536, `TRE_MAX_STRING` INT_MAX, `TRE_MAX_STACK` 1 MiB) are fixed compile-time constants with no `tre_set_*` function | N2 §4/§5 |
| Vectorscan | `vectorscan-block-som` | later, gated on §5.6 | `HS_FLAG_SOM_LEFTMOST` is MANDATORY for this bench's protocol (the driver always reports a START) — an unconditional space cost, not a dial | N2 §4 |
| Vectorscan | `vectorscan-block-nosom` | later | the honest capability gap: END offsets and match/no-match only | N2 §4 |
| python `re` | `python-re` | later, **compile + correctness only** | no size dial exists | §8.1 |
| perl | `perl-default` | later, **compile + correctness only** | perl's internal limits not surveyed (N2 §8, still open) | §8.1 |

**A note on `pcre2-dfa` being new and free.** It needs no new dependency,
no new build machinery and no new driver — `libpcre2-dev` 10.46 is
installed and its `pcre2_dfa_match` entry point is in the same library
the existing adapter already links. It adds a third execution model, a
second `automaton_class`, and two capability lines (`captures`,
`k-reset`) that no current testee crosses. It is the cheapest roster
growth available and should land first (§11 L6a).

### 8.1 python `re` and perl — compile + correctness only in v1

N2 §1's finding: neither fits the driver protocol without EMBEDDING the
interpreter (`Py_Initialize` / `libperl`), because shelling out breaks
the protocol's own reason for existing — an external per-call wrapper
costs ~108.7 ms per call on this box (`adapters.py:34-35` citing
`requirements.md §3` C5), which at these subject sizes IS the entire
signal.

**ADOPTED: compile-cost and correctness only, no match timing, in v1.**

**And a finding this note adds:** that shape needs **no schema change and
no "partial regime" concept.** A record with compile rows and NO match
rows is already legal — `subjects[]` "may be empty (a record with no
match rows)" (`record_schema.md §8`) and `trial_agreement` is already
defined for it (`n/a-trials` with `trials: 0`, required at ≥ 1.4 "even a
record with no match rows"). So a python/perl testee produces a record
that is structurally complete and simply carries no timings. N2 §1
framed this as needing the regime coverage "marked partial"; it does not.

**Consequence:** python and perl answer the CAPABILITY and CORRECTNESS
questions (which constructs compile, which answers agree) and contribute
nothing to any speed ranking. Given that perl is "the one engine on the
roster whose question INVERTS" — what does it do DIFFERENTLY from pcre2,
not what does it lack (N2 §3) — that is most of its value anyway.

**The caveat "no schema change" left out (CS7): such a record can never
reach `status: measured`, run pinned.** Schema-validity is true;
usability is not. `judge_trial_agreement` correctly stamps `n/a-trials`
on zero match rows, but `derive_status`
(`pcrecbench/harness.py:400-426`) routes an `n/a-trials` verdict to
`STATUS_MEASURED` only on a **scratch**-tier record — a **pinned**
record (which is what a python/perl testee run in a normal window is,
having no `local:` binary shape) is unconditionally
`inconclusive-spread`, permanently: no re-measurement changes a record
that structurally has zero match rows. **Stated plainly: python/perl
testees, run pinned, are permanently `inconclusive-spread`** — excluded
from ranking by default and requiring `--include-unmeasured` to query.
`scripts/run_window.sh`'s one-retry contract should special-case a
zero-match-row cell to skip the re-measure it can never resolve; this is
a harness change beyond what this note otherwise proposes, named here
rather than left to be discovered when L6b opens (§12 Q14 carries the
amendment).

---

## 9. `.rxt` as the source — SUPERSEDED, now a pointer (Q3 ruling)

**v0.1's §9 adopted N3's Option B: `.rxt` as the source of pattern TEXT
and IDENTITY, a sidecar for everything else. Frank's Q3 ruling
(2026-09-12, live, this session) supersedes that decision outright: the
capability survey set is a DRIVER of the `.rxt` format itself.** Verbatim:
*"This is as much a driver of the rxt format as anything."* The set is
built ON `.rxt` for real — not on the sidecar hybrid Option B proposed --
and where the format cannot yet carry what the set needs, **the effort
PARKS at that roadblock**, this project sends pcrecdev1 detailed
capability feedback, pcrecdev1 builds the needed productions, and the
effort RESTARTS with this project reviewing and VERIFYING the delivery.

**This section is therefore not a design of its own any more.** The
detailed feedback already exists and has already been sent:
`docs/design/rxt_needs_v1.md` (lane `b42rxtneeds`, 2026-09-12) is the
full form — fifty needs across eight blocks mapped onto pcrec's own
R-BENCH-1..9, thirteen MEASURED facts from twenty parse-only probes
(including two silent-data-loss defects in shipped `--list-source`
behaviour), twelve proposed productions with EBNF sketches and worked
examples, a 41-check ACCEPTANCE CHECKLIST for the restart, and a
Tier 1/2/3 sequencing of what blocks a first sample versus what can land
later. Outbox O-26 (`docs/dev/outbox_to_pcrec.md`) is the distilled form
pcrecdev1 received. Both documents are BUILD ONLY — nothing under
`bench/`, `schema/`, `pcrecbench/` or `testees/` is touched by either.

**What v0.1's Option B leaves behind, corrected rather than silently
dropped:**

- Its file-layout mechanics (§9.2's "no build directives" gate, in
  particular) described `flags`/`engine`/`budget`/`encoding` as
  distinct `--list-source` row *kinds*; they are `pattern`-kind row
  *columns*, populated only under block-scoped directives
  (`~/pcrec/docs/spec/rxt_format.md:425-442`; CS8). This mechanism
  correction, and the loader-surface understatement B6 found
  (`Pattern.__init__`'s required-field tuple and `pattern_bytes()` both
  hard-require `file` today, not just a sidecar key drop), both travel
  forward into `rxt_needs_v1.md`'s own acceptance checklist rather than
  being re-fixed in a section this ruling replaces — the checklist
  already reasons about the delivered format directly, which is the
  right place for both corrections now.
- The 185/0 block-name-legality re-measurement N3 §1.2 made for Option B
  still stands as a fact about the format's `name` grammar; it is
  reproduced and extended in `rxt_needs_v1.md` §1.9's own thirteen
  MEASURED facts (M11 in particular corrects a related claim in
  `subbench_directory_model.md` — see that file's own dated correction,
  cited from `docs/design/CLAUDE.md`).
- §9.5's two stated limitations (no literal newline in a `.rxt` pattern
  line; an unverified literal NUL) are RESTATED as `rxt_needs_v1.md`'s
  own roadblock #1 (`N-2`) and its NUL-refusal ask (§2.7, check B3) — the
  multi-line `(?x)` flattening question v0.1 answered for itself is now
  an OPEN question for Frank at the restart (`rxt_needs_v1.md` F-Q2),
  not a decision this note carries forward, because Frank's Q3 ruling
  changes what "acceptable accommodation" even means once the set's
  truth is meant to live in `.rxt` rather than a sidecar.

**The restart procedure**, stated here so a reader of this file alone
knows what happens next:

1. Run `rxt_needs_v1.md` §3's 41-check acceptance checklist against
   pcrecdev1's actual delivery (seven groups: productions parse, raw
   bytes round-trip, refusal by name, `--list-source` columns, the set
   loads and measures, D93/engine neutrality, the format's own
   regressions — §1.9's thirteen MEASURED facts re-run and diffed).
2. Review the deltas against this note and against `rxt_needs_v1.md`
   itself — a lighter panel pass than R5's, checking whether the
   delivery actually resolves the six roadblocks (Appendix, below), not
   re-litigating the design.
3. Reopen §11's lanes, re-sequenced against what actually shipped rather
   than against Tier 1/2/3's prediction (`rxt_needs_v1.md` §4.2 states
   candidly that even "Tier 1" is most of W2 plus part of W3, and names
   "W2 alone" as the honest smaller cut if pcrecdev1 prefers a smaller
   first delivery — `rxt_needs_v1.md` P-Q6).

**The six roadblocks** (`rxt_needs_v1.md` Appendix, reproduced here so
this file states what it is waiting on without requiring a second
document open): (1) no representation for a multi-line `(?x)` pattern;
(2) `tag` refused, so no per-pattern classification or closed vocabulary
is expressible; (3) no pattern-level PROVENANCE production in any wave;
(4) `@file:` gives a subject a path and no stable id; (5) a second
correct answer under another convention has no carrier in the format --
AND the harness could not score one either (CB1, above); (6) D93 vs. a
set file carrying a testee roster.

---

## 10. The public-facing interface — what to leave room for

Requirement (7) is explicitly a LATER effort. This section names only
what THIS design must not foreclose, and builds nothing.

A later charts/tables UI with selectable engines, versions and sets
consumes three data shapes that already exist:

| shape | what it carries today | sufficient? |
|---|---|---|
| `store/index.tsv` | `path subbench version testee_id machine_id timestamp status rows` | **sufficient as a record index**, insufficient as a DIMENSION source — see (a) below |
| the report TSV | a `#`-prefixed self-describing header (query, records, versions, machines, schema versions, grain, floor pattern) plus 18 key/metric columns (`section pattern subject_or_na regime_or_na form fact testee status tier rank_or_na metric value n pass_rate n_gave_up n_wrong gave_up_summary delta_verdict`) | **sufficient** for a chart of one query's results |
| the interpreter facts TSV (`pcrecbench interpret`) | one row per fired rule with `firing_seq`, `prediction_id`, the rule's inputs and slots | **sufficient** for "what did this sample find" |

**What is missing, named but not built:**

- **(a) Engine and version as their own index columns.** `index.tsv`
  carries `testee_id`, a composed string (`§6.4`). A UI offering "select
  engines" must today split that string — reimplementing the composition
  rule. The fix, when someone builds the UI, is two derived columns
  (`engine_name`, `engine_version`) in `index.tsv`, derivable from
  records with no schema change. **Leave room:** nothing in this design
  depends on `testee_id` being opaque.
- **(b) A per-set family/REQUIRES manifest.** A UI offering "select a
  capability family" needs the family list and the REQUIRES tags as data.
  §4.1's `provenance.tsv` and §5.1's tag vocabulary give it, in the set
  directory. **Leave room:** both are TSVs with stable column names, not
  prose.
- **(c) The capability matrix as data.** engine-config × REQUIRES tag is
  the single most chartable artifact this whole set produces, and §5.2
  puts it in `testees/<engine>/configs.toml` — machine-readable, but
  scattered across adapter directories. A trivial later collector can
  union them; nothing here blocks it.
- **(d) Provenance and licence are not in the record at all.** §4.1
  (revised, CB3) puts two real enumerated FILTERABLE fields
  (`patterns[].provenance_source`, `patterns[].fidelity`) in the record
  so a REPORT can bucket wild vs designed; the full provenance row (URL,
  licence, attribution) stays in the set directory. A public interface
  that displays a wild pattern MUST display its attribution — CC BY-SA
  4.0 requires it (N1 §9). **Leave room, and flag:** the day a public page
  renders an OWASP-sourced pattern, the attribution must travel with it,
  and today nothing but the set directory carries it. That is a
  requirement on the later UI, recorded here so it is not discovered
  then.

---

## 11. The build plan

**This whole section is PARKED and will be RE-SEQUENCED at the restart
(F8, and the §9 supersession above).** The lane plan below still states
what the set needs done — its shape is unaffected by the Q3 ruling — but
its dependency edges assumed §9's old Option B (a sidecar-hybrid loader
L4 would build against a file L3 authored by hand). Under the restart,
L3's `patterns.rxt`-equivalent and L4's loader are built against whatever
pcrecdev1 actually delivers, checked against `rxt_needs_v1.md`'s
acceptance checklist rather than v0.1's §9.2-§9.4. F8's own finding —
that L3 shipped its file with no automated proof its block names matched
the sidecar until L4's gates landed — is superseded the same way: the
restart's block↔sidecar gate is scoped and built once, against the
delivered grammar, not staged across two lanes whose sequencing this
note can no longer specify honestly.

### 11.1 Lanes and order

| lane | what | tier | depends on | size |
|---|---|---|---|---|
| **L1 import/curation** | fetch the confirmed-permissive sources; extract the wild members verbatim; write `provenance.tsv`'s rows; record every fetch URL + licence + date. **NOT blinded** — reading the sources is the task | Sonnet | Frank's §4.2 ruling | 1 session |
| **L2 designed members** | author families 7-12's designed members and every control twin, **blinded per D27**: `man pcre2pattern` and the engine docs only; no `testees/`, no `pcrecbench/adapters.py`, no `store/`, no `reports/`, no ledgers. May read L1's `provenance.tsv` for the `inspired` citations but NOT the wild pattern TEXT until its own patterns are committed. Held to §4.3's REALISM rule, same as L1's imports | Sonnet | §4.3's realism rule (Q2 RESOLVED — not a ratio to size against) | 1 session, parallel with L1 |
| **L3 the set** | pattern source (shape depends on the restart's delivery — §9), `subbench.toml`, `captext.py`, `gen_subjects.py`, `gen_throughput_subjects.py`, `gen_expectations.py`, `gen_provenance.py`, `gen_variants.py`, manifests, `NOTES.md` (objective, families, blinding statement, subjects, **the outlier rule and the predictions, both stated before any run**), `CLAUDE.md` | Sonnet | L1 + L2 | 1-2 sessions |
| **L4 the pattern-source loader** | `subbench.py`'s loader path for the delivered format; the block↔sidecar and no-build-directive gates, restated against the actual grammar (CS8) with their positive controls; `export_rxt.py`'s skip | Sonnet | L3's file shape; `rxt_needs_v1.md`'s delivered productions | 1 session |
| **L5 the capability machinery** | the closed tag vocabulary + load-time validation; `capabilities = [...]` per config; the pre-compile policy in `harness.py`; the §5.3 witness-refusal check arm; **design and build the `variant.kind` rendering from nothing** (CB2 — not a check against existing code, a new one); family 11's shared-convention scoping (CB1) confirmed in the harness's expectation lookup | Sonnet | L3, L4 | 1 session, larger than v0.1 scoped (CB2) |
| **L6a `pcre2-dfa`** | the fourth pcre2 testee — no new dependency, no new build machinery | Sonnet | L5 | 1 session |
| **L6b.. one lane per new engine** ([B7]) | RE2 (direct C++ driver), Oniguruma, TRE, Vectorscan, Rust `regex` — each its own lane with its own adapter note. Oniguruma's lane independently re-derives `atomic-group` support from `regparse.c` (CB5) and resolves `k-reset` (CB6) and the TRE `named-groups`/`free-spacing` citations (CS5) before declaring them | Sonnet each | Frank's install line; L5 | 1 session each |

**Order:** L1 ∥ L2 → L3 → L4 → L5 → **first sample** → L6a → L6b…, with
each new engine measured as its adapter lands. The first sample does NOT
wait for a single new engine — see §11.3.

### 11.2 What needs Frank's install line

Nothing in L1-L5 or L6a. From L6b on, quoted verbatim from N2 §9 (which
checked every package with `apt-cache policy` on this box and installed
none):

    sudo apt install libonig-dev libtre-dev libvectorscan-dev libabsl-dev

and, only if/when the Rust testee is actually built:

    sudo apt install cargo rustc

Two warnings from the same section, both worth carrying: **do not install
`libhyperscan-dev` alongside `libvectorscan-dev`** (Ubuntu marks them
Replaces/Provides/Conflicts; apt will refuse or remove one), and `cmake`
is **not needed** for anything on this roster.

RE2's route: N2 §2 (follow-up) recommends a **direct RE2 C++ driver over
vendoring `cre2`**, on two independent grounds — `cre2` needs a
four-package autotools bootstrap this box lacks and has never been
release-tagged (zero GitHub Releases, checked), while `libre2-dev` is
already installed and pkg-config-discoverable; and the driver protocol
imposes no language constraint (it specifies argv/stdout SHAPE only, and
an adapter's `prepare()` may run its own `g++` step). `g++` 15.2.0 and
`clang++` 21.1.6 are already installed.

### 11.3 Predictions and the outlier rule — before the first run

Both are stated in `NOTES.md` BEFORE any cell runs, following
`bench/syntax`'s own discipline and for its stated reason ("every
prediction below is dated … and is what the author believed from the
reference alone. The first sample will confirm or refute each one by
name").

- **The outlier rule** is this set's R0-Rn, authored by L3. It will not be
  syntax's: rules R3 (spelling groups) and R4 (family median against one
  shared body) do not apply to wild bodies. The shapes that DO carry over
  are R0 (wrong answers first), R1 (a refusal on a pattern whose REQUIRES
  the config claims to satisfy — this set's version is sharper, because
  the REQUIRES tags make "should have compiled" machine-checkable), R2
  (the `pcre2-jit` band), R5 (compile/size cliffs) and R7 (a non-flat
  sweep). The authoring lane writes them; this note does not pre-empt it.
- **The predictions** go in TWO places, as [B13] requires: prose P-rows
  in `NOTES.md`, and a machine-readable
  `docs/dev/predictions/capability-0.1-first.tsv` transcribed per
  `docs/dev/predictions/CLAUDE.md`'s fifteen-column format, committed
  before the run so `stated_utc` predates the population's earliest index
  timestamp.
- **A constraint the prediction format imposes on how predictions are
  phrased**: the report TSV carries `n_wrong` and `pass_rate` and never
  an answer, a span or a capture. "Engine X answers the leftmost-longest
  match" is NOT expressible and would be a LOAD ERROR, not a silent skip
  (`docs/dev/predictions/CLAUDE.md`). Family 11's predictions must
  therefore be phrased as `n_wrong eq 0` on the cell plus `eq 0` on its
  controls. The authoring lane must know this before it writes them.

### 11.4 The first sample's night

| item | value |
|---|---|
| testees | the **six pinned** `pcre2-*`/`pcrec-*` configs every window already runs, plus `pcre2-dfa` if L6a landed |
| cells | 6 (or 7) |
| estimated wall | **~1.7 h** at §3.5's 15-18 min/cell, plus the per-cell `sleep 15` and quiet-gate warm-up |
| cap | `CELL_CAP`'s 5,400 s default, untouched — ~5× headroom |
| script | `scripts/run_window.sh` unchanged, `SUBBENCH=capability` |
| close-out | the window regenerates every committed `*.interpretation.md` sidecar ([B41] (a)) and the read produces a ledger + an outbox item, as every sample does |

**Why the first sample runs on the existing six rather than waiting for a
new engine:** it validates the instrument on a set whose answers we can
already check (the two pcre2 arms and the oracle agree by construction),
and it is the only way to find out whether a sixty-pattern wild set has a
cell-time or a refusal-handling surprise before six new adapters are
built against it. If the set is wrong, one night finds it.

---

## 12. Questions for Frank — REVISED under R5, marked for the parked state

**Three items are now RESOLVED** (Frank ruled them live, 2026-09-12, this
session): Q1 (the licensing floor), Q2 (wild vs. designed is realism, not
a ratio). **Three items are SUPERSEDED** by the same session's Q3 ruling
(§9): Option B is withdrawn, so the questions that assumed it no longer
apply. **Everything else is unresolved and asked at the RESTART**, not
before — nothing is built until pcrecdev1's `.rxt` delivery lands and the
acceptance checklist passes (§9), so no unresolved question here blocks
anything today. **BLOCK** = a ruling required before the item's own
trigger (an L-lane, or [B7]'s Vectorscan lane) opens; **DEFAULT** = this
note's recommendation stands unless Frank says otherwise, and the
trigger is named; **RESOLVED** = ruled this session; **SUPERSEDED** =
moot under the Q3 ruling.

| # | question | status | recommendation / ruling | note |
|---|---|---|---|---|
| **Q1** | The licensing floor | **RESOLVED** | Frank ruled §4.2 option (c) — permissive allowlist for verbatim, `fidelity: inspired` for everything else, PLUS an `inspired` pattern validated as not an actual copy (a mechanical similarity check in the provenance gate, plus review) | this also closes §13 R8 as a ruled mitigation, not an open risk |
| **Q2** | Wild-vs-designed ratio | **RESOLVED** | NOT a ratio — REALISM over contrivance: every member, imported or authored, a shape someone would plausibly deploy; provenance recorded where a real source exists; the percentage unimportant (§4.3) | families 7-12's authored members are held to the same rule as 1-6's imports; Davis stays a `@0.2` candidate, unaffected |
| **Q3** | Hyperscan/Vectorscan's all-ends grain (boolean grain vs. a declared span variant) | **BLOCK, asked at the RESTART** | boolean grain (§5.6 option B) | CS3: this narrows an existing, dated Frank ruling (`requirements.md §4.5` constraint 1) rather than answering an open question — DEFAULT's own definition didn't fit it, so it is marked BLOCK. Costs nothing now: Vectorscan is not in the v1 roster and the build itself is parked well before [B7]'s Vectorscan lane would open |
| **Q4** | The `cost_class` fifth-token question | DEFAULT, asked at the restart | prose + a reporter footnote (§7.2) | unchanged by R5 |
| **Q5** | Declare `match` in v1? | DEFAULT, reworded, asked at the restart | No — `search_short` + `throughput` only (§3.5) | CS1: the answer is unchanged, but the note now states the exclusion is deliberately SET-WIDE (not pcrec-specific) and corrects the family list (drops 7/8 absent a `\K`-bearing member) |
| **Q6** | Peak memory (`ru_maxrss`) scope | DEFAULT, amended, asked at the restart | native-driver testees only, **ranked within that population** (§7.4) | CS4: v0.1 recorded it native-only (the apples-to-apples cut) then declared it never ranked with no argument why native-vs-native comparison remained unreasonable; revised to rank it, mirroring compile time's `cost_class`-scoped ranking |
| **Q7** | The `regex-set-priority` shape in scope? | DEFAULT, asked at the restart | Out of v1 | unchanged by R5 |
| **Q8** | Davis et al.'s corpus in v1? | DEFAULT, asked at the restart | Out of v1, first `@0.2` candidate | unchanged by R5; CS2 removes an argument (§2.2 reason 3) that would otherwise apply equally against this same future bump, strengthening rather than weakening "defer" |
| **Q9** | Subject-data provenance | DEFAULT, asked at the restart | synthetic (§4.4) | unchanged by R5 |
| **Q10** | Is Option B an acceptable reading of "BUILT ON the .rxt format"? | **SUPERSEDED** | — | Frank's Q3 ruling replaces the whole question: the set is built ON `.rxt` for real, not via Option B's hybrid. §9 is now a pointer to `docs/design/rxt_needs_v1.md` |
| **Q11** | File the W2/W3 format asks now, or after the panel? | **SUPERSEDED** | — | the format asks are filed NOW, all of them, as the effort's blocking dependency — `rxt_needs_v1.md` §5 and outbox O-26 already did this |
| **Q12** | Should the set also be buildable by pcrec's own `--source`? | **SUPERSEDED** | — | becomes a question for the format's OWN design at the restart (`rxt_needs_v1.md`'s own P-Q4/P-Q5 territory), not for this note |
| **Q13** | `pcre2-dfa` as a fourth pcre2 testee in v1? | DEFAULT, asked at the restart | yes (§8) | F5's finding (it's not a "dial") is a wording correction to §8's table, not a reason to change this answer |
| **Q14** | Python `re` and perl: compile + correctness only in v1? | DEFAULT, amended, asked at the restart | yes (§8.1) | CS7: the "no schema change" framing now carries the permanent-`inconclusive-spread` caveat (a pinned zero-match-row record can never reach `status: measured`) before this is treated as costless |
| **new** | Is family 11's v1 scope the shared-convention population only, deferring cross-convention scoring machinery? | DEFAULT | yes — already applied in §3.1/§5.6 (CB1) | CB1: answerable by design amendment, not a Frank-level ruling; stated here so Frank sees it was narrowed, not silently assumed |
| **new** | Promote `patterns[].tags` provenance bucketing to real enumerated schema fields (`provenance_source`, `fidelity`)? | DEFAULT | yes — already applied in §4.1 (CB3) | CB3: an implementation decision, not a ruling; stated here because it reverses v0.1's "no schema change" claim in the note Frank read |

**Net change from v0.1: Q1 and Q2 move to RESOLVED (Frank ruled both live);
Q10-Q12 move to SUPERSEDED (Frank's Q3 ruling replaces the question they
were asking); Q3 moves from a silent DEFAULT to BLOCK; Q5, Q6, Q14 keep
their DEFAULT status but each now carries a stated amendment; two new
DEFAULT items record design amendments this revision made on its own
authority. Every unresolved item is asked at the RESTART — none blocks
`rxt_needs_v1.md`'s delivery or its acceptance checklist.**

## 13. Risks, and what would refute this design

| # | risk | what would refute / what it costs | mitigation in this design |
|---|---|---|---|
| R1 | **The wild patterns turn out to measure nothing new.** If every wild member's cost is explained by its length and its first byte, the set is `bench/loglines` with worse provenance | the first sample shows no family whose members diverge from each other or from the floor by more than the R2 band | the control twins (§3.2) are the instrument: a wild pattern beside its designed twin isolates structure from length. If they agree everywhere, that IS the finding, and it is a cheap one to reach |
| R2 | **The `unsupported-by-declaration` share swamps the set.** Families 2, 7-9 (CS6: corrected from "2, 7-10" — family 10 is explicitly the OPPOSITE case, §3.1's own headline finding) are unsupported on RE2/Rust/Vectorscan/TRE; if that is most of the set, half the roster produces mostly empty records | count it before building: 20 of 59 members carry a REQUIRES tag those four engines fail | that is ~1/3, which is a census result, not an empty record. §6.3 is explicit that it is the honest outcome. But a panel should check the count against §3.1's targets |
| R3 | **The pre-compile capability policy is WRONG somewhere** and silently converts measurable cells into `unsupported` rows | a declared-unsatisfied tag that the engine actually supports | §5.3's witness check: for every (config, tag) declared UNSATISFIED, one witness pattern is compiled and the refusal asserted BY NAME. A check with no failing case proves nothing |
| R4 | **SUPERSEDED, restated.** v0.1 framed this as "the `.rxt` format moves under the set mid-build" and cited Option B's sidecar as its own mitigation. Under the Q3 ruling (§9) that framing is backwards: the format moving IS the plan, not a risk to it — the effort deliberately parks and restarts once pcrecdev1 delivers. The residual risk is narrower: **the delivered format does not actually satisfy what `rxt_needs_v1.md` asked for** | the restart's acceptance checklist (41 checks, `rxt_needs_v1.md` §3) fails on a delivered production | the checklist's own negative arms, and the manager's lighter panel pass (§9's restart procedure, step 2) before any lane reopens |
| R5 | **A licence claim is wrong.** Six of N1's LICENSE confirmations came from direct fetches; several sources' terms are still genuinely unknown | any allowlisted licence that turns out not to govern the file we copied | §4.1 records the exact URL and date per pattern, so a wrong claim is traceable to one row and one fetch, not to "the set". §4.2's allowlist is confirmed-by-direct-fetch only |
| R6 | **Cell time is underestimated.** §3.5's model is `bench/syntax`'s, and a wild pattern's throughput cell may not behave like a census pattern's — **family 10's calibration risk is the sharpest named instance (CB8)**: `calibrate()` picks `iters` once from the median subject and a ReDoS witness's own per-iteration cost, far above the median, is what actually dominates the cell's wall time, not the model's flat 50 ms | any cell exceeding ~45 min in the first sample | ~5× `CELL_CAP` headroom, the largest of any set here, chosen for exactly this. A cell killed by the cap exits 124 and writes NOTHING (`scripts/CLAUDE.md`), which is why the margin is deliberate. §3.5's fixed small `--iters` override for family 10's typed subjects is the targeted mitigation |
| R7 | **The reporter cannot render a dozen-plus variant rows in one table.** Never exercised (N2 §7 item 4), and confirmed UNBUILT rather than merely unexercised (CB2 — §5.7) | a synthetic many-variant report that renders wrongly | L5 designs and builds the rendering BEFORE the set ships, against a synthetic report, not against the first sample |
| R8 | **RESOLVED, not merely mitigated.** `fidelity: inspired` becoming a laundering mechanism — "authored from a description" applied to something that is really a copy — was an open risk in v0.1. **Frank's Q1 ruling (2026-09-12) closes it**: an `inspired` pattern is validated as not an actual copy, by a mechanical similarity check in the provenance gate PLUS review, folded into §4.1's `gen_provenance.py --check` | a reviewer or the similarity check finding an `inspired` pattern substantially the same as its cited source | `gen_provenance.py --check`'s new similarity-check arm (§4.1), plus the review Frank's ruling also requires |
| R9 | **The set's objective is too broad to state.** `requirements.md §4.5` constraint 2 requires a declared OBJECTIVE against which every variant is judged; twelve families may not share one | L3 cannot write a single `objective` string a variant declaration can be checked against | the objective is the CAPABILITY CONTRAST itself — "what each roster engine can express, what it refuses, and what the expressible ones cost" — and §6.3's hazard rule is the one place where "objective preserved" needs a per-family reading. If the panel finds a second such place, the objective is too broad and the set should split (§2.1 option C) |

### What would refute the whole design

Two things still stand from v0.1; the third is retired by this revision
and one new item takes its place:

1. **The capability contrast is already answered by documentation.** N2
   §3's table IS the capability matrix, fetched from upstream docs. If
   the only thing a measurement adds is confirmation, the set's value is
   the PERFORMANCE half, and its family taxonomy should be rebuilt around
   cost rather than capability.
2. **RETIRED (superseded by the Q3 ruling).** v0.1's item 1 ("Requirement
   (4) is not satisfied by Option B... re-opens D93 and [B29]'s
   compile-cost objection") no longer applies: there is no Option B to
   fail to satisfy. Requirement (4) is now satisfied by construction — the
   set is built on `.rxt` directly, and the only open question is whether
   pcrecdev1's delivery actually carries what `rxt_needs_v1.md` asked
   for, which is what the restart's acceptance checklist exists to
   settle (R4, above), not a design-level refutation.
3. **RETIRED (Q2 resolved).** v0.1's item 3 ("Sixty wild patterns cannot
   be provenance-recorded honestly... the wild share collapses and Q2's
   answer has to change") assumed Q2 was a ratio to hit. It is not
   (§4.3): there is no target percentage to collapse below. The
   underlying provenance-honesty concern survives in a narrower form —
   **a family cannot produce enough REALISTIC members, imported or
   authored, to reach its target count** — but that is a per-family
   sizing risk L1/L2 report on, not a whole-design refutation.
4. **The `.rxt` delivery restart never happens, or happens on a
   timescale that makes this design stale.** If pcrecdev1's delivery
   diverges materially from `rxt_needs_v1.md`'s twelve proposed
   productions — a different grammar shape for the same needs, say — the
   restart's step 2 (a lighter panel pass) may find this note's family
   taxonomy, provenance model or capability model need a second revision
   before L1 reopens. That is a normal restart outcome, not evidence the
   design was wrong; it is named here so a reader of this note alone
   knows the design's stability is conditioned on the delivery matching
   its own request.

---

## Appendix A — source-fetch status of every family's wild source

Carried forward from N1 so the build lane does not re-derive it. "Fetched"
means a direct WebFetch of a raw/primary URL in N1's own session or its
follow-up.

| family | source | licence | licence fetched? | pattern text fetched? |
|---|---|---|---|---|
| 1 | OWASP Validation Regex Repository | CC BY-SA 4.0 | yes (page footer) | **yes** — 3 quoted verbatim |
| 1, 2 | Elastic `logstash-patterns-core` grok | Apache-2.0 | **yes** (direct fetch) | **yes** — 4 quoted verbatim |
| 3 | OWASP CRS `REQUEST-942-*` | Apache-2.0 | **yes** (direct fetch) | **yes** — 5 rules quoted, one truncated by the fetcher (942360 — **re-fetch before use**) |
| 4 | rebar `regexes/wild/noseyparker.txt` | Unlicense | yes | **yes (CB4/F1) — RE-FETCHED and CONFIRMED**: 30+ verbatim patterns for AWS/GitHub/GCP/Azure/Dynatrace/Figma tokens and `username=...password=...` pairs, quoted directly from the raw file on the first attempt. v0.1's "categorical description only, OWED" claim was stale |
| 5 | rebar `regexes/wild/date.txt` | Unlicense | yes | **yes** — fragment quoted, full file located |
| 6 | VS Code `JSON.tmLanguage.json` | MIT | not re-fetched (well-known) | **yes** — 5 quoted verbatim |
| 7, 8 | Oniguruma `test/test_syntax.c` | BSD-2-Clause | **yes** (`COPYING` fetched) | **yes** — 5 `x2()` cases quoted |
| 10 | RE2 `regexp_benchmark.cc` | BSD-3-Clause | yes (header quoted) | **yes** — 5 quoted verbatim |
| 10 | `awesome-redos-security` CVE index | n/a (inspiration) | — | **NO** — not deep-fetched. **OWED** |
| 11 | PCRE2 `testdata/testinput1`, `testinput2` | BSD-3-Clause WITH PCRE2-exception | **yes** (`LICENCE.md`) | **yes** — empty-match and fold cases quoted |
| 11 | rust-lang/regex `testdata/` incl. `fowler/` | MIT | **yes** (`LICENSE-MIT`) | directory listing only — **OWED** for specific cases |
| 12 | Suricata/ET `pcre:` rules | mixed by sid range | no | **NO** — three attempts failed. Family 12 is authored |
| — | GNU grep `tests/` (`Turkish-I`, `backref*`, `bre`/`ere`) | **GPLv3** | **yes** (`COPYING`) | tree located, contents characterized — **import blocked by Q1** |

**Two OWED fetches gate L1** (corrected from three, CB4 —
`noseyparker.txt`'s literal text is confirmed above, not owed), neither
blocking this design: CRS 942360's full text, and the CVE index for
family 10's inspirations.
