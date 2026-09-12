# R5 — the capability survey set design (`docs/design/capability_set_v1.md`), consolidated

Panel: three independent read-only critics, 2026-09-12 — `r5critic-charter`
(charter fidelity / provenance-licensing / build-plan lens),
`r5critic-semantics` (engine semantics / measurement-validity lens),
`r5critic-schema` (schema / harness / reporter / `.rxt` consistency lens).
Full individual reports: `2026-09-12-r5-capability-set-v1-charter.md`,
`-semantics.md`, `-schema.md` (kept, never edited). This file consolidates,
deduplicates and dispositions. Target: `docs/design/capability_set_v1.md`
v0.1 "draft for panel" (1,361 lines, [B42] phase (b), merged `08b1815`,
DESIGN ONLY — no code, no schema change, nothing under `bench/`,
`schema/`, `pcrecbench/` or `testees/` touched).

**Method note.** This consolidation independently re-verified the central
claim of every finding cited below directly against the source the critic
cited — not merely trusting the critic's own citation — before assigning
a disposition, per the brief's ask. All spot-checks are recorded inline
with `file:line` (or, for F1, a direct re-fetch of the same URL in this
session). Every claim checked came back **VERIFIED** against source;
none was refuted. The three critics converged independently from three
different lenses on two shared defects (the `match`-regime cut's
overclaimed scope, and family 11's convention-scoring machinery), which
is triangulation, not redundancy, and is merged below rather than listed
twice.

**Overall verdict, all three lenses agree on this much:** the design is
unusually well-grounded — nearly every claim spot-checked against
`requirements.md`, `record_schema.md`, `schema/record.schema.json`,
`pcrecbench/{harness,subbench,report,record,adapters}.py`,
`testees/*/configs.toml` and `~/pcrec/docs/spec/rxt_format.md` held up
verbatim or in substance, and the core structural decisions — a new
sub-bench (§2), Option B for `.rxt` (§9), the fail-closed capability
policy (§5.3), the hazard-rewrite rule (§6.3) — are correctly reasoned
and none of the 24 consolidated findings below overturns any of them.
**This note is not yet the thing to build**, in the same shape R4 found
for the interpreter design: it treats several schema fields
(`testee.conventions`, `patterns[].variant`, `patterns[].tags`) as
working mechanisms when they are declared-but-never-read machinery this
project would be building for the first time, its cell-time model is
validated on a population that excludes the one family engineered to
violate its own premise, and one of its three named "would refute the
whole design" risks is graded on stale evidence that a five-minute
re-fetch (performed in this pass) already narrows. A revision pass is
required before an implementation lane opens.

---

## Consolidated findings and dispositions

Numbered fresh per severity tier; `[from: Fn / Sn / Bn]` cites the raw
finding(s) this consolidated item covers — a raw id prefixed `F` is from
`-charter.md`, `S` from `-semantics.md`, `B` from `-schema.md`.

### BLOCKING — must be fixed in the note before implementation starts

**CB1. Family 11's convention-based correctness scoring has no
implementation on either side — authoring OR scoring.**
`[from: B1, S8]` §5.6 claims family 11 "exercises" per-convention scoring
"for the first time in this repo," citing `record_schema.md §5`'s
`conventions[]` field and `requirements.md §7`'s escape hatch. **VERIFIED
against source, independently:** `grep -n conventions schema/validate.py`
returns nothing — no cross-line rule ever checks it. `outcome_for`
(`pcrecbench/harness.py:106-121`) has no parameter for a testee's
declared convention and no branch that reads one. `Subbench.expectation`
(`pcrecbench/subbench.py:268-271`) is keyed on `(pattern, subject_id,
regime)` only — no testee or variant axis — so every testee in a cell is
graded against the identical expectation row. `patterns[].variant`
(`record_schema.md:1026-1038`) carries no field that overrides the
expected match/span for a variant. Separately, `requirements.md §7`'s
promised alternative — "a testee that cannot produce a case's convention
either runs a declared variant with its own convention-tagged
expectations" — has no authoring precedent either: every existing
`gen_expectations.py` derives its one expectation set from the libpcre2
oracle only, and no mechanism exists to author a second,
POSIX-conformant expectation set (S8). The gap is invisible in the v1
first-sample roster only because all six/seven testees share
`perl-leftmost-first`.
**Disposition: PROPOSED accept-amended.** Narrow family 11's v1 scope
explicitly to the shared-convention population (which is what the v1
first-sample roster already is), and defer the cross-convention scoring
machinery (a per-testee/variant expectation override, on both the
authoring and harness sides) to whichever lane lands the first
divergent-convention testee (`re2-longest` or `tre-default`, both
`later` per §8). This is answerable inside the design's own logic — §5.6
already anticipates exactly this shape for `pcre2-dfa`'s decreasing-length
order ("a real semantic difference the adapter must state, not a
convention token") — so it does not require a Frank-level ruling; it
does change what family 11 measures in v1 and must be stated as such in
§3.1's family table and §11's build plan, not left implicit. See the
revised question list for how this reframes the charter's own family-11
value claim.

**CB2. `variant.kind` rendering is claimed "Already built"; it does not exist.**
`[from: B2]` §5.7 states "`variant.kind`... is informational (OD-B5) and
the reporter shows it beside the number," and §11's L5 lists only "the
reporter's many-variant rendering check" as a validation task. **VERIFIED:**
`grep -n variant pcrecbench/report.py` returns exactly two hits, both
unrelated prose (lines 679, 3276) about an unconnected re-render
invariant — zero hits for the schema field. `grep -n variant
pcrecbench/reduce.py` returns nothing. The only code that touches
`variant` at all is `pcrecbench/record.py:177-187`, the WRITE side
(`"variant": None`), confirmed by its own comment. §13 R7's framing
("never exercised") is correct read literally, but §5.7's "Already
built" directly and incorrectly contradicts it.
**Disposition: PROPOSED accept.** Correct §5.7 to state plainly that
variant rendering is UNBUILT. Reclassify L5's deliverable from "a check"
to "design and build the `variant.kind` rendering," sized accordingly —
this is a materially larger L5 task than scoped, and its absence would
make every control-twin variant in families 2, 6, 7, 8 invisible in a
rendered report.

**CB3. `patterns[].tags` bucketing violates the schema's own filterability rule, and the identical mechanism is already proven write-only.**
`[from: B3]` §4.1 proposes bucketing wild-vs-designed via two new
`key:value` tokens (`src:`, `fid:`) in `patterns[].tags`, calling it "No
schema change." **VERIFIED, independently, in two parts.** (1)
`docs/design/record_schema.md:841-846`, the field-table preamble
governing every table below it including `patterns[].tags`
(`record_schema.md:1025`): "DIAGNOSTIC / REPRODUCIBILITY-ONLY fields are
free text... and the reporter must NOT offer them as filters" — bucketing
by wild-vs-designed is exactly "filter or group on it." (2) The identical
mechanism already exists and is already dead: `pcrecbench/record.py:214-220`
already writes `tier:<feature_tier>` and `convention:<convention>` into
`patterns[].tags` on every record, today, for all five existing
sub-benches — and `grep -n '"tags"\|\.tags\b' pcrecbench/report.py`
returns zero hits. The reporter has never read a `patterns[].tags` value
for either existing tag family. `patterns[].tags` also has no grammar
(an unconstrained `{"type": "array", "items": {"maxLength": 64}}` string
array per `schema/record.schema.json:305`), so a typo (`src:owasp-validaton`)
would silently corrupt the bucketing with nothing in `make check-schema`
to catch it.
**Disposition: PROPOSED accept-amended.** Promote provenance bucketing to
real enumerated, FILTERABLE fields (`patterns[].provenance_source` as a
closed slug enum, `patterns[].fidelity` as the closed three-value enum
§4.1 already defines in substance) — a genuine schema MINOR. Correct
§4.1's "no schema change" claim and §1.1's traceability row for
requirement (1) accordingly. This is an implementation-level design fix,
not a question for Frank.

**CB4. One of the design's three "OWED" fetches, cited as evidence for a stated risk that would refute the whole design, resolves cleanly on direct re-fetch.**
`[from: F1]` §3.1 family 4 and Appendix A both state the
`rebar/regexes/wild/noseyparker.txt` literal text is "STILL OWED," and
§13 finding 3 — one of three named things that "would refute the whole
design" — cites this gap as live evidence that "the wild share collapses"
if verbatim-quotable text is thinner than assumed.
**INDEPENDENTLY RE-VERIFIED in this pass:** a direct fetch of
`https://raw.githubusercontent.com/BurntSushi/rebar/master/benchmarks/regexes/wild/noseyparker.txt`
returned real, quotable, Unlicense-covered text immediately — over 100
verbatim patterns for AWS/GitHub/GCP/Azure/Dynatrace/Figma tokens and
generic credential pairs, confirming the critic's own fetch and finding
exactly (30+ patterns is a floor estimate; direct count in this pass:
100+). There was no categorical-description wall.
**Disposition: PROPOSED accept.** Before this note reaches Frank:
(a) re-fetch `noseyparker.txt` (now confirmed working twice,
independently, by two different sessions) and pull its licence-permitted
verbatim patterns into family 4's target-member table, dropping the
"2-3 authored token shapes" fallback plan; (b) correct Appendix A's
"three OWED fetches" to two (CRS 942360's full text, the CVE index for
family 10 — neither re-verified in this pass, both still genuinely
open); (c) re-attempt those two with the same directness before §13
finding 3 is presented to the panel/Frank as a live, unresolved risk —
as written it is graded on evidence one of its three legs already
retracts.

**CB5. The `atomic-possessive` tag bundles two constructs with materially different evidence quality for Oniguruma, read as one clean fact.**
`[from: S1]` §5.1's row cites Oniguruma as satisfying `atomic-possessive`
with one citation ("HAS possessive intervals — flag-confirmed in
`regsyntax.c`"). **VERIFIED against `docs/dev/research/2026-09-12-b42-engine-landscape.md:213`**
directly: possessive quantifiers are confirmed from `regsyntax.c`
(`ONIG_SYN_OP2_PLUS_POSSESSIVE_REPEAT`/`_INTERVAL`), but the same cell
states atomic groups are "not controlled by a distinct op2 flag... not
independently re-derived from the group-parser source, so stated with
lower confidence than the possessive-quantifier finding." One row, one
citation, two different confidence levels folded together.
**Disposition: PROPOSED accept-amended.** Split the tag
(`possessive-quantifier` / `atomic-group`), or require Oniguruma's
atomic-group support to be independently re-derived from `regparse.c`
before an `onig-*` config declares `atomic-possessive` (§5.2/§5.3). §5.3's
fail-closed default protects an absent declaration; it does nothing for
a wrongly-CLAIMED one, which is exactly this row's risk. **Scope: must
resolve before L6b's Oniguruma lane opens — Oniguruma is not in v1's
roster, so this does not block L1-L5 or the first sample.**

**CB6. The `k-reset` row's does-not-satisfy list silently reads as a positive claim for Oniguruma that the source does not make.**
`[from: S3]` §5.1 lists engines that do NOT satisfy `k-reset` as "RE2,
Rust, Vectorscan, TRE, python `re`, and `pcre2_dfa_match`" — Oniguruma is
absent, which under the closed-vocabulary per-config declaration model
reads as "Oniguruma satisfies k-reset." **VERIFIED against
`2026-09-12-b42-engine-landscape.md:213`** directly: "not general
PCRE-style `\K`; has its own reset-point extensions under some
syntaxes" — neither a clean yes nor a clean no, a different
syntax-dependent construct.
**Disposition: PROPOSED accept.** Resolve before an `onig-*` config
declares `k-reset`: either confirm behavioral equivalence to `\K` for
this bench's own family 7-9 `\K`-tagged patterns, or declare
`k-reset: false` for Oniguruma and route those patterns to
`unsupported-by-declaration`. **Scope: before L6b, not before v1.**

**CB7. §6.3's hazard-rewrite rule is keyed on `hazard_class`, but no family in §3.1 is ever assigned one.**
`[from: S4]` §6.3's rule (a possessive/atomic construct in a
`hazard_class: exponential-backtracking`/`ambiguous-decomposition`
pattern must be `unsupported-by-declaration`, never rewritten) is worked
through explicitly for family 2 ("this family is where the §6.3 hazard
rule bites hardest") — but `hazard_class` is a required, per-PATTERN
closed-enum field, and §3.1's family table has no `hazard_class` column
and never assigns a value to any family, including family 10, the family
explicitly about hazard. **VERIFIED:** `schema/record.schema.json:298`
(`"required": ["pattern_id", "canonical_sha256", "hazard_class",
"size_class"]`) confirms the field is required per pattern; §3.1 (read
directly, lines 176-191) has no such column anywhere. Absent an explicit
instruction, the default an authoring lane reaches for is `hazard_class:
none`, which would silently route family 2's atomic groups to the
ordinary §6.2 rewrite table instead of §6.3's protection.
**Disposition: PROPOSED accept.** Add an explicit `hazard_class`
assignment per family (at minimum families 2 and 10) to §3.1 or §11's
build plan before L2 (designed members) or L3 (the set) opens. This is
v1-blocking: both lanes are in the critical path before the first
sample.

**CB8. The cell-time model is validated on a homogeneous census and silently assumed to transfer to family 10, whose whole purpose is to violate that homogeneity on exactly the v1 roster's backtracking testees.**
`[from: S6]` §3.5's arithmetic treats a (pattern, regime, trial) as
costing `50 ms × n_subjects`, "INDEPENDENT of the testee's speed," citing
`bench/syntax`'s calibration premise — validated on deliberately
homogeneous, one-construct-in-a-plain-body patterns. Family 10
(`redos-nested`) is the opposite by design: a subject engineered to be
catastrophically slow on a backtracker and fast on everything else, and
`pcre2-interp`/`pcre2-jit` are both in the v1 first-sample roster.
**VERIFIED against `pcrecbench/harness.py:290-343`** (`calibrate()`)
directly: `iters` is chosen once from the median subject's per-iteration
cost and applied uniformly to the whole (pattern, regime) loop — there is
no per-subject override. A subject whose per-iteration cost is orders of
magnitude above the median runs its loop for `iters × its_own_per_iter_cost`,
not ~50 ms; that one subject's total time, not the cell's assumed total,
can dominate.
**Disposition: PROPOSED accept.** State family 10's calibration risk
explicitly in §3.5/§13 (currently absent from both). Adopt at least one
of: a more conservative `--iters`/`--subject-timeout` cap specifically
for family 10's typed subjects, or a fixed small `--iters` override
(already supported by the harness per `harness.py:296`) in place of
`search_short`'s calibrated loop for the worst ReDoS witnesses. This
affects the first-sample night's wall-clock estimate directly and is the
most likely single cause of a `CELL_CAP` timeout in v1's first run.

### SHOULD-FIX — required before implementation, smaller in scope

**CS1. The `match`-regime exclusion overclaims its evidentiary support for two of the five families it names, and generalizes a pcrec-specific defect to every future testee.**
`[from: F7, S7]` §3.5 excludes `match` for every testee in v1, citing the
syntax ledger's Tier A Q2/Q3 as the reason families "6 (`(?x)`), 7-9
(`\K`-adjacent, recursion) and 11... would each inherit that defect."
**VERIFIED by reading `docs/dev/ledgers/2026-09-07-b36-syntax-first-d34c9131.md`
§9 directly.** Q3 names exactly three failure modes under one lexical-
wrapper cause: `(?R)` recursing into the wrapper (family 9), `(?x)`'s
comment swallowing `)\z` (family 6), and Q2's `\K` case cited in passing.
But **Q2 is a SEPARATE finding**, with its own "Source" line attributing
the defect to `testees/pcrec/driver.c`'s anchored branch hard-coding
`first_s = 0` — a pcrec-specific driver bug, not a lexical consequence of
the wrapper the way `(?x)`'s comment-eating and `(?R)`'s recursion are.
Neither family 7 (`cap-backref`) nor family 8 (`cap-lookaround`)'s
designed-member roster (§3.1, read directly) mentions `\K` at all —
"7-9 (`\K`-adjacent...)" reads as three families cut by association with
one shared parenthetical, not three families each shown to hit the
defect. Separately: the exclusion is set-WIDE (every future testee, not
just pcrec), but most [B7] roster engines (RE2's `FullMatch`, likely
Oniguruma's/TRE's own anchor options) have a native anchored-match call
and would not need pcrec's lexical `(?:pattern)\z` wrapper at all —
foreclosing `match`-regime compliance measurement (family 1's own stated
purpose) for every future non-pcrec engine too, on a defect only one
testee has.
**Disposition: PROPOSED accept-amended.** (a) Correct the family list:
drop 7 and 8 from the "would inherit" enumeration in §3.5 unless a
`\K`-bearing member is added to their rosters, or a separately-stated
reason is given. (b) State explicitly in §3.5 whether the exclusion is
scoped to pcrec specifically (noting this may need a harness change,
since the regime declaration is currently sub-bench-scoped, not
per-testee, per `bench/CLAUDE.md`) or is deliberately set-wide as a
matter of policy, and name that as a stated tradeoff rather than an
implicit one. This changes Q5's shape — see the revised question list.

**CS2. §2.2's reason 3 against extending `bench/syntax` proves too much — the design's own §4.5/Q8 plans an identical version bump for itself.**
`[from: F2]` §2.2 reason 3 argues a version bump to `syntax@0.2` "throws
away the first sample" because future records land in a new,
incomparable version. **VERIFIED against `requirements.md §5`** directly:
"a sub-bench version is a frozen snapshot; records compare only within
the same sub-bench version; bumping is a deliberate, logged event" — this
does not destroy the old version's records, and it is the cost of *every*
version bump. The design's own §4.5/Q8 defers Davis's corpus to
`capability@0.2` using the identical framing ("one sidecar line... not a
redesign") without treating that cost as disqualifying there.
**Disposition: PROPOSED accept.** Drop reason 3 from §2.2, or reframe it
as "a cost every version bump shares, not a decisive one." Reasons 1
(registry-enumeration mismatch), 2 (incompatible bodies) and 4
(blinding-discipline conflict) are independently sufficient for §2's
decision.

**CS3. Q3 (Vectorscan's boolean-grain relaxation) is marked DEFAULT but is a proposed exception to an existing, dated Frank ruling, not an answer to an open question.**
`[from: F3]` §5.6 itself states option (B) "narrows `requirements.md §4.5`
constraint 1... for one engine. That is a real relaxation of a Frank
ruling." **VERIFIED against `requirements.md:173-176`** directly: "The
results must be the same — no variation in results... There is no
'approximates with stated differences' grade." §12's own definition of
DEFAULT ("this note's recommendation stands unless Frank says otherwise")
fits an unruled question, not a carve-out from Frank's own prior word —
silence should not be read as granting an exception to an existing
personal ruling.
**Disposition: PROPOSED accept.** Re-mark Q3 **BLOCK** in the revised
question list. Costs nothing now — nothing is built on it until [B7]'s
Vectorscan lane opens, so this can sit answered-when-convenient without
slowing L1-L6a.

**CS4. §7.4's own justification for restricting `ru_maxrss` to native-driver testees is the apples-to-apples cut requirement (3) asks for, yet the metric is then blanket-excluded from ranking with no argument for why native-vs-native comparison remains unreasonable.**
`[from: F4]` §7.4 scopes `ru_maxrss` recording to native-driver testees
specifically to avoid pooling a python/perl-interpreter-startup-dominated
number against a native one — then §7.4/§7.5 declare it "never ranked, on
any testee," **VERIFIED against the design's own §7.4/§7.5 text** (read
directly) with no stated reason why the population the cut already
purified remains unreasonable to rank.
**Disposition: PROPOSED accept-amended.** Either rank `ru_maxrss` within
the native-driver population (mirroring compile time's "within
`cost_class` only" rule, §7.2), or state explicitly why native-vs-native
comparison is still unreasonable. This amends Q6 — see the revised
question list.

**CS5. Two REQUIRES rows (`named-groups`, `free-spacing`) assert TRE as the sole failing engine with no supporting citation anywhere in the cited research.**
`[from: S2]` §5.1 presents both rows as facts the note "makes explicit
because N2's own table distinguishes them" (§5.1's preamble). **VERIFIED:**
`2026-09-12-b42-engine-landscape.md`'s per-engine table (lines 208-218,
read directly) has no column for named-group spelling or `(?x)`/
free-spacing support at all, and neither the base note nor its
`b42engines2` follow-up (which explicitly re-derived six other TRE facts
from primary source) states anything about either construct for TRE.
This is precisely the failure the design's own preamble rules out
("nothing is asserted that one of the three research notes did not
establish").
**Disposition: PROPOSED accept.** Cite a primary source (POSIX ERE's own
grammar is the natural one for TRE's default mode) or mark both rows
UNCONFIRMED and route them through the §5.3 witness-refusal check either
way.

**CS6. §13 risk R2's family list and count are internally inconsistent, and contradict §3.1's own headline finding for family 10.**
`[from: S5]` R2 states "Families 2, 7-10... 20 of 59 members carry a
REQUIRES tag those four engines fail." **VERIFIED by arithmetic against
§3.1's own table** (read directly, line 187): family 10 is explicitly
the OPPOSITE case ("none refuse to compile... RE2/Rust/Vectorscan/TRE
are IMMUNE by construction"), and summing families {2,7,8,9} alone
(6+5+5+4 target members) gives exactly 20, matching R2's own number
precisely; adding family 10's 6 gives 26, not 20.
**Disposition: PROPOSED accept.** Trivial fix — change "Families 2,
7-10" to "Families 2, 7-9" in R2's row.

**CS7. A compile-only, zero-match-row PINNED record can never reach `status: measured`, though it is schema-valid.**
`[from: B4]` §8.1 states the python/perl compile-only shape "needs no
schema change and no 'partial regime' concept," citing `subjects[]`
legally being empty and `trial_agreement`'s `n/a-trials` verdict already
being defined for it. Schema-validity is true; **usability is not, and
the section does not say so. VERIFIED exactly against
`pcrecbench/harness.py:400-426`** (`derive_status`): line 424-425 routes
a **pinned** `n/a-trials` verdict to `STATUS_SPREAD` unconditionally
(`inconclusive-spread`); only a **scratch**-tier record gets
`STATUS_MEASURED` there (line 426). A python/perl testee run in a normal
window is pinned by construction (no `local:` binary shape).
**Disposition: PROPOSED accept.** State plainly in §8.1/Q14 that these
testees, run pinned, are permanently `inconclusive-spread` — excluded
from ranking by default, must be queried with `--include-unmeasured` —
and consider whether `scripts/run_window.sh` should skip its one-retry
contract for a zero-match-row cell (a condition no re-measure can ever
resolve). Does not block v1 (§8 marks python/perl "later") but must be
resolved, or the "no schema change" framing corrected, before L6b opens
for either and before Q14 is treated as costless.

**CS8. The "no build directives" `.rxt` gate names column-scoped attributes as if they were row kinds.**
`[from: B5]` §9.2/§9.4 describe the gate as checking for "no `target`,
`config`, `flags`, `engine`, `budget` or `encoding` **line**."
**VERIFIED exactly against `~/pcrec/docs/spec/rxt_format.md:427`**
(quoted verbatim by the critic and confirmed on direct read): the `kind`
column's five legal values are `lib | target | config | description |
pattern` — `flags`/`engine`/`budget`/`encoding` are never row kinds; they
are per-`pattern`-row *columns*, populated only by block-scoped
directives.
**Disposition: PROPOSED accept.** Rewrite §9.2 rule 1 and §9.4's gate
description as: "no `target`/`config`-kind row, and every `pattern`-kind
row's flags/features/encoding/engine/budget columns are empty" — same
outcome, correct mechanism for L4 to build against.

### WORTH-NOTING — accepted as documentation fixes, no design change required

Deduplicated; each accepted as a wording/table correction in the revision
pass: `[F5]` `pcre2-dfa`'s §8 row sits in the "dial" column but describes
a third execution model and two capability lines, never a space/speed
tradeoff — restate as "not a dial, a fourth engine identity that costs
nothing"; `[F6]` §8's pcrec row lists axes, not dials — `nocaps` is a
genuine user-facing tradeoff, `-noedge`/`-noisland`/`-noclsfold` are
diagnostic controls this project built for itself, and collapsing all
five into "the dial" is asserted, not shown — map explicitly or drop the
§1.1 claim; `[F8]` `patterns.rxt` (L3) ships with no automated proof its
block names match the sidecar until L4's gates land — narrower than a
full L3-depends-on-L4 problem (`gen_provenance.py --check` is
unaffected), but a typo is invisible in the interim — move the
block↔sidecar name comparison into L3 as a standalone check or name the
gap and its owner; `[S9]` §7.1's compile-cost table never states
`automaton_class` though the cited research already answers it for two
engines (TRE: `nfa-simulation`; Oniguruma: `backtracking`) — add a
column/footnote; `[S10]` family 12's non-UTF-8 pattern text needs the
same `canonical_text`-omission escape hatch KB-7/[B30] established for
oversized patterns, for a different reason (encoding validity, not
size) — state this in §9.5; `[S11]` option (B)'s "cheap, ships now"
Vectorscan claim is correct but uncited against the driver protocol's
own degenerate `START`/`END` allowance (VERIFIED: `pcrecbench/adapters.py:54`
documents "`START,END` the FIRST match's span, or `-`" exactly as cited)
— cite it directly and add one sentence on how the throughput regime's
`NMATCHES` is computed for an all-ends engine; `[B6]` §9.3 undersells the
`subbench.py` change — `Pattern.__init__` hard-requires `file` in its
required-field tuple and `pattern_bytes()` opens it directly (VERIFIED
exactly against `pcrecbench/subbench.py:93-108,242-246`), so dropping
`file` needs a required-field-list change plus a second `pattern_bytes()`
implementation, not just "key on name instead" — squarely inside L4's
stated scope, worth naming so the lane is not surprised; `[B7]`
`unsupported-by-declaration` and `testee.conventions` are both
schema-legal today with zero production use anywhere in the harness —
this design is their first real exercise, raising the review bar on L5's
witness-check arm; not a defect, a documentation note.

### What the design gets right (preserved, not to be "fixed" away)

No rule invents a tuned constant — every REQUIRES tag, hazard rewrite and
outcome-enum decision re-derives to a citation in one of the three
research notes or this project's own schema/requirements text (§0's own
discipline, honored throughout and independently spot-checked in this
pass). The core structural calls — a new sub-bench rather than a
`bench/syntax` extension (§2, all four independent reasons individually
sufficient once CS2's reason 3 is dropped), Option B for `.rxt` (§9,
correctly grounded in the block-name grammar's own widening and in D93's
hazard), the fail-closed pre-compile capability policy with its
witness-refusal control (§5.3), and the hazard-rewrite rule that turns a
judgment call into a mechanical `hazard_class` test (§6.3) — are all
well-argued and, on this consolidation's independent read, correctly
decided. `pcre2-dfa` as a fourth, free pcre2 testee (§8) is a genuinely
sharp, low-cost addition. The provenance model's closed field set
(`fidelity: verbatim/adapted/inspired`, §4.1) is the right shape for the
licensing floor Frank has now ruled on (below).

---

## Frank's rulings already given this session, and how this panel's findings interact with them

**Q1 (licensing floor) = option (c)**, ruled: permissive allowlist for
verbatim text, everything else `fidelity: inspired`, **and** an
`inspired` pattern must be validated as not an actual copy of its source
(a mechanical similarity check in the provenance gate, plus review).
This directly subsumes §13 risk R8 ("`fidelity: inspired` becomes a
laundering mechanism") — Frank's ruling already specifies R8's own
mitigation. **Action for the revision lane:** fold Frank's similarity-check
requirement into §4.1's `gen_provenance.py --check` gate description and
into R8's row (mitigation now ruled, not merely recommended), rather than
carrying R8 forward as an open risk.

**Q2 (wild ratio) is pending.** CB4 (F1's noseyparker re-fetch) narrows
one of the two facts §4.3's ratio argument rests on (the licence-messy
sources being "kept off the critical path") but does not resolve Q2
itself — the ~50% recommendation and its consequence table are unchanged
by this finding. Q2 stays **BLOCK** pending Frank's word, now on
slightly stronger evidence than the draft the ruling will be made against.

---

## Revised question list for Frank

Starting from §12's Q1-Q14, applying this panel's findings. **BLOCK** =
build cannot proceed correctly without a ruling; **DEFAULT** = the
note's recommendation (as amended below where noted) stands unless
overruled; **RESOLVED** = ruled this session, listed for completeness.

| # | question | mark | why (this panel's finding, if any) |
|---|---|---|---|
| Q1 | licensing floor | **RESOLVED** | Frank ruled (c) + the inspired-pattern similarity-check requirement, which also resolves R8 (above) |
| Q2 | wild-vs-designed ratio | **BLOCK** (unchanged) | CB4 narrows the evidence behind §13 finding 3 but does not decide the ratio; pending Frank |
| Q3 | Vectorscan boolean grain | **BLOCK** (was DEFAULT) | CS3: this is a relaxation of an existing Frank ruling (`requirements.md §4.5` constraint 1), not an open question — DEFAULT's own definition doesn't fit. Costs nothing now; [B7]'s Vectorscan lane is the trigger, so this can be answered whenever convenient |
| Q4 | `cost_class` fifth token | DEFAULT (unchanged) | no finding bears on it |
| Q5 | declare `match` in v1? | **DEFAULT, reworded** | CS1: keep the "no" recommendation for v1, but the note must now state explicitly whether the exclusion is pcrec-specific (possibly needing a per-testee regime-scoping harness change) or deliberately set-wide, and correct the family list to drop 7/8 absent a `\K`-bearing member. The ANSWER doesn't change; the STATED REASON and its scope must |
| Q6 | `ru_maxrss` scope | **DEFAULT, amended** | CS4: keep native-driver-only recording, but either rank it within that population or state explicitly why native-vs-native comparison is still unreasonable — the current "never ranked" is unargued for the population the cut already purified |
| Q7 | `regex-set-priority` in scope? | DEFAULT (unchanged) | no finding bears on it |
| Q8 | Davis corpus in v1? | DEFAULT (unchanged) | no finding bears on it directly; note CS2 removes one argument (§2.2 reason 3) that would otherwise apply equally to this planned 0.2 bump, strengthening rather than weakening the "defer" recommendation's consistency |
| Q9 | subject-data provenance | DEFAULT (unchanged) | no finding bears on it |
| Q10 | Option B satisfies "BUILT ON .rxt"? | **BLOCK** (unchanged) | CB2/CB3/CS8 correct mechanism details around the `.rxt` gates but do not touch the Option B decision itself; still pending Frank as scoped |
| Q11 | file W2/W3 asks now or later? | DEFAULT (unchanged) | no finding bears on it |
| Q12 | buildable by `pcrec --source`? | DEFAULT (unchanged) | no finding bears on it |
| Q13 | `pcre2-dfa` in v1? | DEFAULT (unchanged) | F5's finding (it's not a "dial") is a wording correction to §8's table, not a reason to change this answer |
| Q14 | python/perl compile+correctness only? | **DEFAULT, amended** | CS7: the "no schema change" framing needs the permanent-`inconclusive-spread` caveat stated (B4) before this is treated as costless; the yes/no answer is unaffected |
| **new** | is family 11's v1 scope the shared-convention population only, deferring cross-convention scoring machinery? | **DEFAULT** | CB1: this is answerable by design amendment (narrow scope), not a Frank-level call, but it changes what family 11 claims to measure in v1 and should be stated in the note Frank reads, not silently narrowed after his approval |
| **new** | promote `patterns[].tags` provenance bucketing to real enumerated fields (`provenance_source`, `fidelity`) as a schema MINOR? | **DEFAULT** | CB3: an implementation decision, not a ruling — flagged only because it reverses §4.1's "no schema change" claim in the note Frank will read |

**Net change from §12: three items move off silent-DEFAULT status (Q3 to
BLOCK; Q5, Q6, Q14 to DEFAULT-with-a-required-amendment), one item is
RESOLVED and its associated risk (R8) closed by the same ruling, and two
new DEFAULT items surface design amendments the revision lane makes
without needing Frank's word.** Q1, Q2 and Q10 remain the three BLOCKING
items — Q2 unchanged, Q1 now resolved, Q10 unaffected by any finding
here.

---

## Disposition summary

| tier | consolidated findings | raw ids covered | disposition |
|---|---:|---:|---|
| BLOCKING | 8 (CB1-CB8) | 9 (F1; S1,S3,S4,S6; B1,B2,B3; +S8 merged into CB1) | all PROPOSED accept or accept-amended; each names the exact fix required, and the scope (before L1-L5/first sample, vs. before a later lane) where the fix is not v1-critical |
| SHOULD-FIX | 8 (CS1-CS8) | 9 (F2,F3,F4; +F7 merged into CS1; S2,S5; +S7 merged into CS1; B4,B5) | all PROPOSED accept or accept-amended |
| WORTH-NOTING | 8 | 8 (F5,F6,F8; S9,S10,S11; B6,B7) | all PROPOSED accept as documentation/wording fixes |
| escalated to Frank | 0 new (Q2, Q10 carried forward, pre-existing; Q3 moved to BLOCK by this panel, not escalated as new) | — | everything else is mechanism, not value, and is dispositioned above |

## What happens next

1. **A revision lane** (not implementation) produces
   `docs/design/capability_set_v1.md` v0.2 applying every disposition
   above, mirroring the `[B20]`/`[B13]` r3/r4 precedent: findings applied
   to the SPEC before any code is written, under manager rulings recorded
   here (all marked PROPOSED — the manager ratifies at merge).
2. The revised note goes to Frank with the amended §12 question list
   above (not the original), since three of his answers now carry a
   materially different shape (Q5's stated scope, Q6's amended
   recommendation, Q14's caveat) and one new BLOCK item (Q3) needs his
   word before [B7]'s Vectorscan lane, though not before L1 opens.
3. Only after the revision is itself confirmed (a lighter pass — does
   v0.2 actually resolve CB1-CB8/CS1-CS8, re-verified against source the
   way this panel did) does an implementation lane (L1 onward) open.
4. `docs/dev/plan.md`'s `[B42]` row stays at its current phase through
   this step — phase (c) (the panel) is what this file records; phase
   (d) (Frank) follows the revision, not this file directly.

---

## By-id completeness

Per `docs/dev/session_discipline.md` §7(a): every numbered finding in
every critic file appears below with a disposition, greppable by id.

| id | raw finding (one line) | cited in THIS review? | where handled |
|---|---|---|---|
| F1 | noseyparker.txt "OWED" fetch resolves cleanly on direct re-fetch | yes | CB4 |
| F2 | §2.2 reason 3 disqualifies a version bump the design plans for itself | yes | CS2 |
| F3 | Q3 is a relaxation of a Frank ruling, not an open question; DEFAULT doesn't fit | yes | CS3 |
| F4 | §7.4's own native-only cut reasoning supports ranking `ru_maxrss`, not excluding it | yes | CS4 |
| F5 | `pcre2-dfa` sits in the "dial" column with no space/speed tradeoff stated | yes | WORTH-NOTING |
| F6 | §8's pcrec row conflates real dials with diagnostic-only controls | yes | WORTH-NOTING |
| F7 | the `match`-regime cut's cited ledger names only one of three families with a matching failure mode | yes | CS1 (merged with S7) |
| F8 | L3 ships `patterns.rxt` with no automated proof against the sidecar until L4 | yes | WORTH-NOTING |
| S1 | `atomic-possessive` bundles two constructs of different evidence quality for Oniguruma | yes | CB5 |
| S2 | `named-groups`/`free-spacing` TRE claims have no citation anywhere in the research | yes | CS5 |
| S3 | `k-reset`'s does-not-satisfy list silently reads as a positive Oniguruma claim | yes | CB6 |
| S4 | §6.3's hazard rule is keyed on an unassigned field | yes | CB7 |
| S5 | §13 R2's family list/count is internally inconsistent | yes | CS6 |
| S6 | the cell-time model doesn't account for family 10's calibration risk | yes | CB8 |
| S7 | the `match`-regime cut generalizes a pcrec-specific bug to the whole roster | yes | CS1 (merged with F7) |
| S8 | family 11's expectation-authoring machinery for a second convention doesn't exist | yes | CB1 (merged with B1) |
| S9 | `automaton_class` never stated for the new engines | yes | WORTH-NOTING |
| S10 | family 12's non-UTF-8 pattern text needs the `canonical_text` omission escape hatch | yes | WORTH-NOTING |
| S11 | option (B)'s "cheap, ships now" claim is correct but uncited against the driver protocol | yes | WORTH-NOTING |
| B1 | family 11's convention-based scoring has no harness mechanism | yes | CB1 (merged with S8) |
| B2 | `variant.kind` rendering claimed "Already built"; it does not exist | yes | CB2 |
| B3 | `patterns[].tags` bucketing violates the schema's own filterability rule | yes | CB3 |
| B4 | a compile-only pinned record can never reach `status: measured` | yes | CS7 |
| B5 | the "no build directives" gate names columns as if they were row kinds | yes | CS8 |
| B6 | §9.3 undersells the `subbench.py` change (`file` is hard-required) | yes | WORTH-NOTING |
| B7 | `unsupported-by-declaration` and `testee.conventions` are exercised for the first time here | yes | WORTH-NOTING |

**26/26 raw ids accounted for, all cited by id in this file** (unlike R4,
where three ids were found dropped in the first pass — this consolidation
was built with the by-id table checked against all three raw files
directly during drafting, not after, per the standing rule
`session_discipline.md` §7(a) now requires).
