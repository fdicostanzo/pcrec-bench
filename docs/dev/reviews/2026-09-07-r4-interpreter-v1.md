# R4 — the interpreter design note (`docs/design/interpreter_v1.md`), consolidated

Panel: three independent read-only critics, 2026-09-07 — `r4critic-source`
(source-verification lens), `r4critic-charter` (charter-fidelity/scope
lens), `r4critic-build` (implementability lens). Full individual reports:
`2026-09-07-r4-interpreter-v1-source.md`, `-charter.md`, `-build.md`
(kept, never edited). This file consolidates, deduplicates and
dispositions. Target: `docs/design/interpreter_v1.md` (merged `651a7ce`,
DESIGN ONLY — no code exists).

**Method note.** The manager independently re-verified a sample of the
sharpest claims from each critic directly against `pcrecbench/report.py`,
`pcrecbench/reduce.py`, `schema/record.schema.json` and the committed
report/store files before compiling this file (not merely trusting the
critics' own citations) — every one checked out exactly. The three
critics also converged independently on the same core defects from three
different angles (source citations, charter fidelity, buildability),
which is strong triangulation, not redundancy.

**Overall verdict, all three lenses agree on this much:** the
architecture is sound and unusually well-grounded — no rule invents a
tuned constant; every threshold is read as a string the reporter already
computed (`_cross_pin_verdict`, `_jitter_flag`'s `timer-floor`,
`agreement_line`), so the interpreter can never disagree with the report
about whether something moved. **This note is not yet the thing to
build.** Several rules as specified don't match what the TSV actually
emits, the acceptance test (§10) cannot be satisfied as written by any
implementation, and the "no opinions" firewall has a real gap. A revision
pass is required before an implementation lane opens — not a rewrite from
scratch.

---

## Consolidated findings and dispositions

Numbered by severity tier. `[from: source Dn / charter Fn / build #n]`
cites provenance; multiple citations mean independent convergence.

### BLOCKING — must be fixed in the note before implementation starts

**B1. The record row's agreement string is misdocumented in §2.1, contradicting §4.1.**
`[source D1, build #2]` §2.1 says the agreement string sits in
`gave_up_summary`'s slot; it is actually in `value` (col 12, paired with
`metric=agreement`) — `gave_up_summary` (col 17) is empty on every
`record` row. §4.1's own Inputs line already has this right. The note
inherited `report.py`'s own stale code comment rather than reading the
emitted row.
**Disposition: accepted.** Fix §2.1 to match §4.1; build the R-STATUS-9
fixture from a real extracted row so the column position is pinned by
data, not prose.

**B2. R-STATUS-9's firing predicate is stated two incompatible ways, and it decides 9 firings on the acceptance report.**
`[source D2, build #3]` §4.1 fires on an agreement string starting
`disagree` **or `n/a`**; §9.2's did-not-fire table says the rule does
NOT fire on Report A specifically because all nine records read `n/a
(v1.x)`. All nine of Report A's records do read `n/a (v1.1)`/`n/a
(v1.2)` — so §4.1's own definition fires nine times, and §9.2's rendered
specimen is wrong under that definition.
**Disposition: accepted-amended.** Rule: `n/a (v<schema>)` (pre-1.4
records) is **provenance about the record's age**, not a trial-agreement
finding — it belongs with R-STATUS-6's mixed-schema-population fact, not
R-STATUS-9. `n/a (N trials)` (a genuinely short run) and `agree 0/0 —
nothing judged` are each their own case and must be enumerated in
`threshold_src` with the `reduce.py` citation. Only `disagree` fires
R-STATUS-9 as revised. §9.2 must be re-rendered to match.

**B3. R-DELTA-3's predicate cannot fire on any committed report, including its own acceptance report — the verdict column is a `; `-joined list of clauses, not a token.**
`[source D5, build #1]` `^now measured \(was: ` requires the string to
*start* with that text; every occurrence in the 42-report corpus is a
suffix of `selection changed (vm → dfa); now measured (was: gave-up)`,
built deliberately by `_cross_pin_info` (report.py:2520-2535). §10 A.2
requires R-DELTA-3 to fire on exactly those cells. As written it never
can.
**Disposition: accepted.** State the verdict column's grammar explicitly
in §2.1: "a `; `-separated list of independent clauses; each R-DELTA rule
matches its own anchor against each clause, not against the whole
string." Add a co-firing fixture (R-DELTA-2 + R-DELTA-3 compound)
alongside the existing R-DELTA-1/R-DELTA-2 mutual-exclusion fixture.

**B4. R-BUCKET-KB's headline claim — recognising KB-13/KB-14 "from their signatures" — cannot be done from the declared inputs; the signature text lives in known_issues.md and the record JSONL, neither of which `interpret` reads.**
`[source D7, charter F2]` Measured: the excluded rows the acceptance test
names carry `gave_up_summary=0`; the "expected N…observed M" text is not
in the TSV at any grain (§2.4 explicitly excludes the record JSONL from
`interpret`'s inputs). What the TSV actually supports is `(regime, form,
n_wrong>0, n_gave_up==0)` — which cannot discriminate KB-13's rows from
KB-14's, or from a future unrelated defect with the same shape. §10 C.3
calls this "v1's strongest claim"; it is currently v1's least honest one,
since a false positive would attach a diagnosed cause in the voice of a
fact with a source.
**Disposition: accepted-amended.** Drop R-BUCKET-KB from v1's acceptance
test (§10 C.3 downgraded from MUST to a stated known gap) unless a
one-line reporter change adds a discriminating column (an
`expectation_detail` slot in `gave_up_summary`'s own style — the shape
[B9] R7 already established for give-ups). If that reporter change is
made, R-BUCKET-KB may re-enter v1's acceptance test; either way,
signature registration becomes a **MAJOR** catalogue bump (not MINOR as
drafted) once it is reachable at all — the more a rule asserts, the more
review it costs, not less.

**B5. The ranking-group key in §4.3 (`pattern, regime, form`) is wrong; `report.py` deliberately excludes `form` from the key, and says so in its own docstring. This makes R-BUCKET-FORM unsatisfiable by construction and inflates R-RANK-3's fallback population from 35% to 45% of all groups.**
`[from charter F4, source D11]` `report.py:3161-3176`'s docstring states,
in capitals, that `form` is deliberately not part of the group key
(reversing the module's own first cut on a 2026-08-25 manager fix
request) specifically so a compliance regime's pcrec whole-subject rows
rank against libpcre2's plain rows. §4.6's own worked example describes
the group correctly; §4.3 contradicts it.
**Disposition: accepted.** Every rule in §4 that says "group" must be
re-derived from `_ranking_groups`'s actual key before implementation,
not from the TSV's column list. This is the single highest-value fix in
the note — it is cited as evidence the note was written "from the TSV's
columns rather than from the reducer's semantics," and that method
concern should inform how the revision is checked, not just this one
rule.

**B6. R-RANK-1's template asserts "the reference arm" unconditionally; the reporter silently falls back to the best row when no reference arm is rankable, and the design's own detector (R-RANK-3) isn't wired as a guard.**
`[from charter F5, source finding 21 confirmed]` `report.py:4136`:
`ref_ns = ref.median_ns if ref else (rankable[0][2].median_ns ...)`. Does
not bite today (all 69 current R-RANK-1 firings sit in groups that do
have a reference arm) but 891 of 2,514 groups don't, concentrated in
exactly the set (altwide) that generates 40 of the 69 firings.
**Disposition: accepted.** R-RANK-1 must not fire in a group R-RANK-3
also fires on. Better: ask the reporter for a `baseline_is:
reference|best` header/column (one line, rides with Q1's `floor_pattern:`
proposal in the same reporter change).

**B7. The acceptance test's own MUST list omits the charter's highest-value finding class: no rule reaches the `vm-in` result (`[OPT-1]`), because all six classes are cross-pin or status-shaped and `[OPT-1]` is a same-pin, cross-config comparison.**
`[from charter F6]` Frank's original blinded test names four things to
find unprompted; the design covers three with real rules and, for the
fourth (`vm-in`), concedes in §10 A.4 itself that it cannot be surfaced
without a human pointing at it. Three of the five candidate rows in the
note's own grounding feedback document (`[OPT-1]`, `[OPT-2]`, `[OPT-C]`)
are same-pin, cross-config comparisons and fall outside all six classes.
**Disposition: accepted.** Add a seventh class, **R-ARM**: two testee ids
in one ranking group differing in exactly one config token (`vm` vs
`vm-in`, `auto` vs `auto-noedge`, `caps` vs `nocaps`, gcc vs `-clang`), at
the same pin, whose medians differ by more than `2 × max(stddev)` — the
identical, already-copied threshold R-DELTA-1 inherits from
`_cross_pin_verdict`, applied within-report instead of across-pin. No new
constant introduced (§4's core property survives). This is the single
largest coverage improvement available and directly serves every
deny-flag testee this project has built (`-noedge`, `-noisland`,
`-noclsfold`, `-align64`, `-bigcap`) — they exist to be read exactly this
way and today nothing in the design reads them.

**B8. The golden-file determinism check and the sidecar-freshness check are both coupled to inputs that churn — `store/index.tsv` (grows every window) and `REPORTER_VERSION` (bumps roughly once a working day) — recreating KB-8's failure mode one layer up.**
`[from build #4]` R-STATUS-2's whole purpose is reading outside the
report into the live index; the moment any future window measures
another record in a covered (subbench, version, machine), the facts for
an already-committed, unmodified report change, and `make check` fails on
a commit whose only content is new records. Similarly, every
`REPORTER_VERSION` bump (thirteen since 2026-08-25) triggers full-report
regeneration per `reports/CLAUDE.md`'s standing rule, which invalidates
every committed sidecar's stamp and every golden file.
**Disposition: accepted.** (i) The golden/determinism check (§8(2)) must
run against a FROZEN index snapshot committed beside the golden files
(`catalogue/golden/index@<date>.tsv`), never against live
`store/index.tsv` — the live index stays `interpret`'s default for an
actual human run, just not for the pinned check. (ii) State explicitly,
before implementation, whether `check-interpret` may fail a records-only
or reporter-version-bump commit, and who owns re-generating sidecars when
it does (the reporter-bump case is not addressed at all in §3.3, which
only covers a *catalogue* bump).

**B9. The facts TSV (§5) has no firing ordinal, so one-slot-per-row output cannot be reassembled into firing-scoped slot sets — which §8(5), the firewall's own no-prose check, requires.**
`[from build #5]` At least four rule shapes break the "identify a firing
by (pattern, regime, form, testee)" assumption: R-STATUS-12 needs two
pattern slots against one `pattern` column; R-STATUS-5 is a header fact
with no key columns; R-BUCKET-FORM/VSBEST/R-RANK-3 are group-scoped;
R-PRED-* are keyed by `prediction_id`, not a TSV column.
**Disposition: accepted.** Add a `firing_seq` integer column (per rule,
declaration/emit order) and either a `prediction_id` column or an
explicit rule that `record_id` doubles for it. Small, and required for
§8(5) to be implementable as anything other than a self-consistency
check against a freshly-run `interpret`.

**B10. R-BUCKET-SPAN needs "the pin history," which exists in neither declared input and is not defined anywhere machine-readable.**
`[from build #6]` `store/index.tsv` has no pin-order column; approximating
via earliest-timestamp-per-pin in the index breaks exactly on the
example §10 B.3 itself gives (a `vm-in` row whose Δ partner skipped an
intervening pin because that pin was never measured with a `vm-in` row on
that sub-bench — store-adjacency and pin-history-adjacency are different
predicates here).
**Disposition: accepted-amended.** Make the pin order catalogue DATA — a
`[[pin_order]]` table maintained by hand at each re-pin (one line per
re-pin; the same precedent B4's R-BUCKET-KB signature registration
already establishes for the catalogue). More honest than an approximation
and avoids two lanes building two different rules.

**B11. The opinion firewall constrains slot values and sentence count but nothing constrains the fixed prose *inside* a template — and the catalogue's own R-STATUS-12 template already smuggles in a mechanism claim ("a different budget binds on the two spellings") with no link.**
`[from charter F1]` §8(5)'s no-prose check passes this by construction,
since it only asks whether a line is reproducible template output — a
template that itself asserts a cause satisfies that test. The design has
moved the opinion from run time to catalogue-authoring time and stopped
auditing it there, at exactly the review bar (MINOR) that requires the
least scrutiny.
**Disposition: accepted-amended, and ruled together with Q4 (below) per the charter critic's own synthesis (F12), which the manager adopts rather than escalating.**
Every clause in a template that is not a slot and not definitional must
either (a) be a `links` entry the renderer appends, or (b) be removed.
Concretely: R-STATUS-12 renders the two give-up codes and stops; "a
different budget binds" becomes a `links` entry to
`feedback_pcrecdev1_2026-08-25-repin-v2.md` §2, where a human already
committed the reading. §8 gains a sixth section: a human-reviewed
template-diff gate, since template text is the one unmechanised prose
surface in the system. This also answers §7.4's Q4 (the charter-deviation
question) without needing Frank's ruling: **the renderer phrases; the
templates are reviewed prose, authored once, before any run** — which is
the charter's letter (a person's phrasing) satisfied by *authoring-time*
review rather than *run-time* generation, and preserves byte-
reproducibility. The note's offered fallback (an unchecked `## Reader's
note` section) is rejected outright, per F12 — it recreates exactly the
unaudited-prose channel this finding closes.

### SHOULD-FIX — required before implementation, smaller in scope

**S1. On the current (denser) corpus, the rules fire in proportion to report size, and §1.1 forbids the only two mechanisms (ranking, bands) that would keep the output legible — on a modern report the acceptance items are unfindable among hundreds of undifferentiated bullets.**
`[from charter F3, build #12]` Measured: R-DELTA-1 fires 202/384 times
(53%) on bounded@0.3; with no predictions file (exactly how §10 runs the
test) R-DELTA-4 then fires on all 202, degenerating "flag the unpredicted
Δ loudly" into flagging everything. Total firing volume: ~40 (Report A,
the smallest/oldest) vs ~420 (Report B) vs ~275 (Report C).
**Disposition: accepted-amended.** This is not a ranking-by-interest
mechanism, so it does not reopen §1.1: a rule may declare `aggregate =
"group"` and render ONE firing carrying a count plus the extremal rows
(e.g. R-FLOOR-1 as "190 compile rows read `timer-floor`"), which is a
purely arithmetic reduction, not a judgment about importance. Required
before implementation. Also required as a one-line fix regardless: when
no predictions file is supplied, R-DELTA-4 must report
`did-not-fire: input-absent` like the rest of R-PRED (§9.2's own mock-up
already does this; §4.2's table contradicts it) — "uncovered" is vacuous
with no predictions to be covered by.

**S2. The predictions format (§6) cannot express most of the project's real, already-scored predictions.** `[from charter F7]` Checked against the
one committed, fully-scored prediction set (`bench/syntax/NOTES.md`
P1-P13, scored in the 2026-09-07 syntax ledger): the format is missing a
set-membership/count shape (P1), a cross-pattern ordering shape (P5,
compounded by `rank` meaning something different in the TSV than in a
prediction author's intent), any way to predict an answer or a span
(P2/P9/P10 — the exact predictions that found KB-14), a way to represent
a compound/per-clause verdict (10 of 13 real predictions are scored
per-clause), and a `PARTIAL` verdict (the modal outcome, 5 of 13, with no
rule).
**Disposition: accepted.** Before implementation, transcribe P1-P13 into
the proposed format as a validation exercise (not a full back-fill — that
stays out of scope per §6.5) and require the format to express ≥ 9 of 13
and reproduce the ledger's 3/5/5 tally, adding a fourth `partial` verdict
or ruling that compound predictions decompose into clause-suffixed
sub-ids at authoring time. A format that clears only 4 of 13 needs
redesign now, cheaply, rather than after a loader exists.

**S3. §10 is not falsifiable as written: two MUST items self-cancel, there is no null control, and there is no false-positive budget.** `[from
charter F8]` A.4 is both a numbered MUST-surface item and explicitly
"stated as a risk, not a pass" in the same section; C.3 states two
different bars in one paragraph; nothing in the acceptance test is a
report where the tool should stay quiet; the MUST-NOT lists cover three
hand-picked claims per report and say nothing about the other ~275
bullets.
**Disposition: accepted.** Resolve A.4 per B7's R-ARM fix (it should pass,
not remain a risk) and C.3 per B4 (it fails outright, stated plainly, not
softened). Add a synthetic "clean" fixture — a report where every record
is `measured`, no cell is excluded, no Δ is outside spread — required to
fire on zero of the ~30 rules, as the missing null control.

**S4. §7.2's three permitted slot-value kinds (verbatim copy / row count / declared arithmetic) do not cover the note's own templates — at least four rules parse a rendered string rather than reading a column.** `[from
build #8]` R-RANK-1 decomposes `testee_id` by regex; R-STATUS-5 parses
the `source:` header rendering; R-STATUS-12 parses
`_gave_up_cell_summary`'s rendering (already flagged as Q8); R-STATUS-9
would need to parse `agreement_line`'s rendering for its token. The
`_gave_up_cell_summary` parse is also harder than Q8 implies — its
non-pcrec fallback clause may itself contain `;`, `,` and parentheses,
untested by any committed report.
**Disposition: accepted.** Add a fourth permitted slot kind — "a declared
decomposition, its regex written out in the catalogue's own field" — so
the firewall's audit surface stays complete rather than silently
incomplete. Promote Q8's option (b) (the reporter emitting
`smallest_giveup_subject`/`_bytes` as real columns) from recommendation to
precondition for R-STATUS-12, since the note itself says a v1 without it
"has implemented half the charter."

**S5. The "row view" correspondence-check mechanism is easy to build but does not fit at least six of the ~30 rules (group-scoped and cross-pattern rules need a table-shaped view), and the `inputs` string grammar mixes three different addressing schemes with no stated parser.** `[from build #9]`
**Disposition: accepted.** State the `inputs` grammar
(`<file>:<section>[?<col>=<val>][.<column>|.{<col>,…}]`) and a view
contract (`rows(section, **eq) → Sequence[Mapping]` with undeclared-column
raising, plus `header(key)` and `index_rows(**eq)`) as part of the design,
not left to the implementation lane per §12 — this is the one part of
"module layout" that two competent implementations could reasonably do
differently while each passing their own tests, so it is a contract, not
an implementation detail.

**S6. The fixture plan (§8(4)) mis-describes its own cited precedent and specifies an unimplementable check.** `[from build #10]` `schema/
examples/bad/` is generated-base-plus-one-declared-mutation (pinned by
`gen_example_14.py --check`), not hand-written as the note claims; a
hand-typed fixture at the scale required (~190 files across ~30 rules ×
2, some needing 18+ tab-separated rank rows to be realistic) risks
producing shapes `render_tsv` cannot actually emit, which proves a rule
fires on data that doesn't exist. "The minimum number of bytes" is also
not a computable predicate as worded.
**Disposition: accepted.** Adopt a `catalogue/fixtures/gen.py` generator
mirroring `gen_example_14.py --check`'s actual precedent: each fixture
directory names a real committed report, a row selector, and (for the
sabotage) one declared field mutation; the generator projects a real
reporter-produced slice. "Minimum diff" becomes the well-defined "exactly
one declared field differs."

**S7. `grain` is declared on the R-DELTA class only, but at least two other classes are set-grain-only without saying so, and `n` means a different quantity by grain.** `[from build #13]` `_n_and_pass_rate` returns
`n_subjects` at set grain and `n_trials` at subject grain into the same
column; R-FLOOR-2's `median_ns / n` arithmetic is meaningful only at set
grain; R-RANK-1/2 depend on `delta_verdict`, which the reporter only
populates at set grain, and say nothing about grain in §4.3.
**Disposition: accepted.** Make `grain` mandatory on every `[[rule]]`,
checked at load (§8(1)); declare R-FLOOR-2 and R-RANK-* as `["set"]`.

**S8. Q1's stated v1 behavior (read `bench/<dir>/subbench.toml` for the floor pattern) re-creates KB-2 exactly, and the version skew is live today, not hypothetical.** `[from build #14]` `report.py` deliberately stopped
reading `pcrecbench.subbench` after KB-2 for precisely this reason
(a record from another box or an older sub-bench version has no matching
checkout beside it). Report A is `email-specimen@0.1`; the tree's
`bench/email/` is at `@0.2` today — reading today's sidecar to interpret
an older report's floor pattern is reading the wrong file, and because
`role` defaults silently to `member`, the failure is a silent
`no-matching-rows`, not an error.
**Disposition: accepted — Q1's own recommendation becomes a
precondition, not an option.** The reporter emits a `floor_pattern:
<id|none>` header key (one line at report.py:4068-4091, a
`REPORTER_VERSION` bump, every report regenerated — a motion this project
has executed thirteen times already). `interpret` then has exactly the
two declared inputs §2.4 already claims it has.

### WORTH-NOTING — accepted as documentation fixes, no design change required

Deduplicated list; each accepted as a note/wording correction in the
revision pass, no further disposition needed: the header-comment's `; `
delimiter collides with `x13_rules`'s own `; `-joined value and needs a
stated parse rule (`[build #7]`); §9.2's own worked output omits eight
rules that genuinely don't fire on that report and understates R-DELTA-1
to two firings where a third (`×1.00`) exists (`[source D4, D15]`);
R-PRED-4 and R-DELTA-4 are declared identical but defined with different
scopes (`[source D16]`); R-RANK-2's predicate is likely incoherent (no
reason a rank position and a cross-pin delta direction must agree) and is
the one rule in §4 with no worked example — the pattern the charter's
own "example per rule" discipline exists to catch (`[charter F11]`);
R-RANK-3 is filed under "rank flips" but is really a population caveat
that belongs in R-STATUS and should gate R-RANK-1 (`[charter F11]`, ties
to B6); the "26/23/23/23 real ratios" figure in §4.4 is off by an order
of magnitude (644 rows, 161 per pcrec testee) (`[source D3]`); §9.2's
sidecar contains at least six sentences that are not any declared
template, which §8(5) as specified would itself reject (`[source D14]`);
the `schema/examples/bad/` count is 72 sabotage files + one CLAUDE.md,
not 73 sabotages (`[source D9]`); "the project reads TOML in three
places" should not include `pyproject.toml` (consumed by build tooling
only, never at runtime) (`[source D18]`); `subject_or_na` has two
"absent" spellings across sections, worth one sentence in §2.1
(`[build #16]`); every `open()`/`write()` in the future `interpret.py`
should pass `encoding="utf-8"` explicitly, since `delta_verdict` carries
`×`/`→` (`[build #17]`); a handful of cosmetic mis-citations (a "the
eighth row" that is the seventh; `§10 Q2` that is `§11 Q2`; abbreviated
testee ids in one worked example; the `_ranking_groups`
form-vs-group-key distinction stated loosely in §4.3) — all individually
trivial, collected in the individual critic files for the revision lane
to sweep in one pass.

### What the design gets right (preserved, not to be "fixed" away)

Recorded per `charter F14` so the revision does not sand off the note's
real strengths: no rule introduces a tuned constant — every threshold
re-derives to a token, a header integer, or a definitional 1.0 named as
such; "the interpreter must never be able to disagree with the report
about whether something moved" (§4.2) is architecturally correct and
correctly implemented; reading the TSV and never the markdown, with the
reason stated; §6.4's `stated_utc`-precedes-earliest-record-timestamp
check, which makes post-hoc prediction mechanically visible; §8(4)'s
minimum-diff control requirement, correctly generalizing this project's
controls-share-no-source discipline to a new surface; and writing §10
*before* any code exists, which is exactly why this panel could find
these gaps now rather than after a lane had built around them.

---

## Open questions from the note (§11), ruled or carried forward

- **Q1** (floor pattern source) — **ruled: the header-key fix (B/S8 above)
  is now a precondition, not a recommendation.**
- **Q2** (subject-grain input for R-BUCKET-DOMINATED) — **ruled: (a),
  the note's own recommendation** — `input-absent` until a separate
  reporter change lands `<name>.subject-grain.tsv`.
- **Q3** (should set-local NOTES.md bands become catalogue-readable
  data?) — **carried forward, Frank's call**, unchanged by this panel;
  no finding above bears on it either way.
- **Q4** (the charter deviation: renderer phrases, not the skill) —
  **ruled by the manager per B11 above**, no escalation needed: the
  renderer phrases, the templates are human-reviewed prose authored once
  before any run, §8 gains a template-diff gate. The note's own fallback
  (an unchecked reader's-note section) is rejected.
- **Q5** (back-fill sidecars for all 42 reports, or only the three
  acceptance reports?) — **ruled: the note's own recommendation stands**
  (three at landing, the rest on demand) — build critic's finding 20
  confirms the cost that matters is review weight, not CPU, which
  supports keeping the blast radius small.
- **Q6** (should a fired R-STATUS-9/R-BUCKET-KB ever be a non-zero exit?)
  — **ruled: no**, the note's own recommendation stands (instrument/gate
  separation, consistent with BD7 and schema v1.4's own precedent).
- **Q7** (catalogue-as-data vs. executable predicate split) — **ruled:
  keep the split**, the note's own recommendation stands; build critic's
  finding 9 confirms the correspondence mechanism is genuinely easy to
  build this way (~30 lines).
- **Q8** (R-STATUS-12 parses a rendering) — **ruled: option (b) promoted
  from recommendation to precondition** per S4 above.

No item in this panel rises to a Frank-level ruling except Q3, which was
already his to answer and is untouched by anything found here.

---

## Disposition summary

| tier | count | disposition |
|---|---:|---|
| BLOCKING | 11 (B1-B11) | all accepted or accepted-amended; each names the exact fix required before an implementation lane opens |
| SHOULD-FIX | 8 (S1-S8) | all accepted; required before implementation, smaller in scope than the blockers |
| WORTH-NOTING | ~14, deduplicated | accepted as documentation/wording fixes, folded into the revision pass |
| escalated to Frank | 0 new (Q3 carried forward, pre-existing) | everything else is mechanism, not value, and is ruled above |

## What happens next

1. **A revision lane** (not implementation) produces
   `docs/design/interpreter_v1.md` → a revised note (v1.1, or v2 if the
   scope of change to §4's rule table warrants a version note) applying
   every disposition above. This mirrors the `[B20]` r3 precedent: the
   panel's findings are applied to the SPEC before any code is written,
   under manager rulings recorded here.
2. Only after that revision is itself confirmed (a lighter check — does
   the revised note actually resolve B1-B11/S1-S8, re-verified against
   source the way this panel did) does an implementation lane open,
   building `catalogue/rules.toml`, `pcrecbench/interpret.py`,
   `make check-interpret` and the skill, against the (by then corrected)
   §10 acceptance test.
3. `docs/dev/plan.md`'s `[B13]` row stays `STATE:not-started` through
   both steps — it becomes `started` only when the implementation lane
   opens.
