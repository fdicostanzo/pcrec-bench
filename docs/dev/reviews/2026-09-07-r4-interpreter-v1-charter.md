# R4 — the interpreter design note (`docs/design/interpreter_v1.md`), lens: CHARTER FIDELITY AND SCOPE DISCIPLINE

Critic: read-only lane, 2026-09-07. Target: `docs/design/interpreter_v1.md`
(1,228 lines, DESIGN ONLY). Judged against: `docs/dev/plan.md`'s `[B13]`
row; `docs/dev/dev_journal.md` second session parts 5 and 7 (the
2026-08-25 chartering); `docs/dev/feedback_pcrecdev1_2026-08-25-repin.md`
and `-repin-v2.md` (the note's two stated grounding inputs).

Everything numeric below was recomputed from the committed corpus
(`reports/*.tsv`, 42 files) or read out of `pcrecbench/report.py` at
master. Where the note's own numbers were checkable, they checked out —
my independent implementation of the R-RANK-1 predicate reproduced the
note's census exactly (69 firings, 9 files, 40 concentrated in
`2026-09-05-altwide-0.2-…-after-334fd10e.tsv`, the tail 7/7/4/4/2). The
note is unusually honest about its own weak points and invites attack on
two of them by name (§10 A.4, §10 C.3). Both invitations are accepted
below, and both are findings.

Fourteen findings: 4 BLOCKING, 6 SHOULD-FIX, 4 WORTH-NOTING.

---

## F1 — BLOCKING. The opinion firewall constrains slot VALUES and the NUMBER of sentences, but nothing constrains what a TEMPLATE says. The one place an opinion can live is the one place §7 does not look.

§7 claims three structural properties deliver "no opinions": one
`str.format` template per rule id (§7.1), slot values copied or declared
arithmetic (§7.2), links validated against committed files (§7.3). Read
them together and note what they cover: the *number* of sentence shapes,
the *values* substituted into them, and the *pointers* appended to them.
None of the three says anything about the fixed prose between the braces.

The design's own catalogue contains a counter-example. R-STATUS-12's
template (§4.1):

> "Subject `{subject}` ({subject_bytes} B) gives up as **{code_a}** on
> {pattern_a} and **{code_b}** on {pattern_b}, on `{testee}` in
> {regime}: **a different budget binds on the two spellings.**"

Everything before the colon is fact. Everything after it is a mechanism
claim — an assertion about *why* two codes differ, which is exactly what
§1.1 ("Causes") forbids and what §7.3 says can only appear as a
validated link. It appears here as literal template text, with
`links = []` implied (the note declares no link for R-STATUS-12). The
sentence is traceable — a human wrote it in
`feedback_…-repin-v2.md` §2 — but the design's machinery neither knows
that nor requires it.

§8(5), the "no-prose check", cannot catch this: it asserts that every
line in a sidecar is reproducible by `render(rule_id, slots)`. A
template that carries an opinion satisfies that check *by construction*.
The firewall's own test is blind in exactly the direction the firewall
claims to be strongest.

This generalises. `interpret --render` has no way to say a cause, true —
but a *catalogue author* has, once per rule, permanently, at whatever
review bar a catalogue MINOR bump carries. The design has moved the
opinion from run time to authoring time and then stopped auditing it.

**Remedy.** Make template text a first-class checked object: every
clause in a template that is not a slot and not definitional must either
(a) be traceable to a `threshold_src`/`links` entry that the renderer
appends, or (b) be removed. Concretely, R-STATUS-12 renders the two
codes and stops; the "different budget binds" reading becomes a `links`
entry to `feedback_pcrecdev1_2026-08-25-repin-v2.md` §2, where a human
already committed it. And §8 gains a sixth section: a human-reviewed
diff gate on `template` fields, since it is the only unmechanised prose
in the system.

---

## F2 — BLOCKING. R-BUCKET-KB, the design's self-declared strongest claim, cannot express the signatures it is specified against — measured, not argued.

§4.6 registers KB-13's signature as: *"a `large-subject-throughput` cell
whose exclusion reads `expected N non-overlapping match(es); observed M`
with M < N and no give-up."* §10 C.3 makes recognising KB-13 and KB-14
from their signatures "v1's strongest claim", and invites the panel to
say so if the class is under-designed.

It is. The report TSV does not carry that text. From
`reports/2026-09-07-syntax-0.1-…-first-d34c9131.tsv`, every excluded row
the acceptance test names:

```
rec-1     | large-subject-throughput | plain          | pcrec_… | gave_up_summary=0 | n_wrong=15 | n_gave_up=0
asr-k-uc  | match-compliance         | whole-subject  | pcrec_… | gave_up_summary=0 | n_wrong=5  | n_gave_up=0
```

`gave_up_summary` is `0`. The expected-vs-observed detail is not in the
TSV at any grain. What R-BUCKET-KB can actually read is
`(regime, form, n_wrong > 0, n_gave_up == 0)` — and by that predicate
KB-13's rows and KB-14's rows are *identical in evidence* and separable
only by their coordinates (regime and form). So the rule would attach a
diagnosed cause to a cell on the strength of "this is the regime the bug
was found in", which is not a signature; it is a coordinate lookup
wearing a signature's clothes. On a later set with an unrelated
wrong-answer-without-give-up in `large-subject-throughput`, it
mis-attributes, and it mis-attributes *in the voice of a fact with a
source*.

Compounding it: §4.6 states the signature is "DATA in the catalogue, so
adding a newly-filed KB is a MINOR catalogue bump and no code change."
That puts the single most interpretive object in the design behind the
*lowest* review bar it defines. The inversion is backwards — the more a
rule asserts, the more review it should cost.

**Remedy.** Either (a) drop R-BUCKET-KB from v1 and re-file it once the
reporter emits a discriminating column (an `expectation_detail` slot in
`gave_up_summary`'s style — the same shape [B9] R7 already established
for give-ups), or (b) keep it but require every registered signature to
name a column-level discriminator that no other registered signature
matches, checked by `make check-interpret` against the committed corpus,
and make signature registration a MAJOR bump. Until then §10 C.3 should
be marked as a known failure of v1, not its strongest claim.

---

## F3 — BLOCKING. The rules fire in proportion to report size, and §1.1 forbids the only two mechanisms (ranking, bands) that would keep them readable. On the current corpus the acceptance items are needles in the tool's own haystack.

Firing counts, computed against the three acceptance reports:

| | Report A (email repin) | Report B (bounded@0.3 after) | Report C (syntax first) |
|---|---|---|---|
| R-DELTA-1 | 3 | **202** | 0 |
| R-DELTA-2 | 6 | 1 | 0 |
| R-STATUS-3 | 13 | 0 | 23 |
| R-STATUS-4 (distinct pattern×testee) | 0 | 2 | **60** |
| R-FLOOR-1 | 2 | 81 | **190** |
| rank groups (→ R-BUCKET-VSBEST candidates) | 6 | 129 | 285 |

Report B carries 384 cross-pin cells with a Δ verdict, of which 181 read
`unchanged (within spread)` and **202 read faster/slower ×N**. R-DELTA-1
therefore fires on 53 % of its own population. A rule that fires on the
majority of the rows it examines is a census, not a finding.

Worse for the charter: with no predictions file — which is exactly how
§10 runs the acceptance test — **R-DELTA-4 fires on all 202 of them**,
since "no prediction covers this cell" is universally true. The rule
`feedback_…-repin-v2.md` §2 asked for ("flag an UNPREDICTED Δ as loudly
as a regression") degenerates to flagging every Δ, which is flagging
none. Report C's sidecar would run to roughly 275 bullets before
R-BUCKET-VSBEST and R-RANK are counted.

§1.1 then removes both escapes on principle: no importance ranking
("output order is the catalogue's declaration order") and no set-local
bands. So the design has committed to emitting hundreds of undifferenti-
ated bullets and to never telling the reader which three matter. §0
promises to mechanise the fraction of a ledger that is not judgment; at
this density the sidecar is a *second report*, and reading it is a new
judgment task of comparable size.

Note the shape of the evidence: the one report where the tool is
obviously legible (A, 24 firings) is the smallest and oldest in the
corpus and is the one Frank chartered against in 2026-08-25. Both modern
reports are an order of magnitude denser. The design has been validated
against the era it was written in.

**Remedy** — three options, none of which is "rank by interestingness":
(a) an acceptance criterion on output size (e.g. no rule may fire on
more than X % of its own population without collapsing to a *counted
summary line plus the N extremes* — a purely arithmetic reduction, no
judgment); (b) R-DELTA-4 suppressed entirely when no predictions file is
supplied, since "uncovered" is then vacuous — it should report
`did-not-fire: input-absent` like the rest of R-PRED, which §9.2's own
mock-up does and §4.2's table contradicts; (c) `--only <class>` /
`--since <pin>` scoping so a reader can ask one question. (b) is a
one-line fix and should happen regardless.

---

## F4 — BLOCKING. §4.3 defines the ranking group as `(pattern, regime, form)`. `report.py`'s ranking group is `(subbench, pattern, regime)` — form was deliberately removed from the key on a manager fix request. Two rules are broken by the mismatch, one of them by construction.

`pcrecbench/report.py:3161-3176`, verbatim in its docstring:

> `form` (schema v1.1) is DELIBERATELY NOT part of the group key
> (manager fix request, 2026-08-25, reversing this module's first cut):
> … both answer the SAME question and MUST rank together, or the
> compliance regime … never compares anything.

§4.3 reintroduces the exact cut the reporter already made and reversed,
inside the rule class Frank named ("rank flips vs the reference arm").
Consequences:

1. **R-BUCKET-FORM can never fire.** Its predicate is "a ranking group
   whose rankable rows carry both `same program` and `separate
   artifact`". If `form` is part of the group key, a group is
   single-form by construction and the predicate is unsatisfiable. §4.6's
   own worked example describes the group correctly (7 whole-subject +
   2 plain rows in *one* `orig` / match-compliance group) — so §4.3 and
   §4.6 contradict each other, and §10 A.6 depends on the §4.6 reading.
2. **R-RANK-3 inflates.** Groups with no reference arm: **891 of 2,514**
   under the reporter's real key (35 %), **1,323 of 2,946** under §4.3's
   (45 %) — because every pcrec `whole-subject` sub-group loses libpcre2,
   which reaches the same regime as `plain`. Under §4.3 the rule fires on
   nearly half of every report, permanently, for a reason that is a
   property of the schema rather than of any sample.

This is the kind of defect a design note is *for* — it costs one line to
fix now and a lane later. But it also says something about method: the
note cites `report.py` line numbers extensively and accurately, and
still got the group definition wrong, which suggests the rules were
written from the TSV's *columns* rather than from the reducer's
*semantics*. Every rule that says "group" should be re-derived from
`_ranking_groups` before implementation.

---

## F5 — SHOULD-FIX. `ratio_vs_baseline` silently falls back to the best row when the reference arm is absent. R-RANK-1's template asserts "the reference arm" unconditionally. 0 of 69 firings are exposed today; 891 groups are.

`report.py:4136` — `ref_ns = ref.median_ns if ref else (rankable[0][2].median_ns …)`.
When no `libpcre2_*_interp-*` row is rankable in a group (it refused, it
gave up, it was not in the roster), `ratio_vs_baseline` becomes a ratio
to the *best row*, and the TSV emits no marker distinguishing the two
cases.

R-RANK-1's template then reads "vs the reference arm `{reference}`, …
the cell crossed the reference arm" about a number that has nothing to
do with the reference arm. Two outcomes, both bad: the `{reference}`
slot is unfillable and §7.1's strict-slot renderer raises → exit 2 on a
legitimate committed report; or the implementer fills it with the
fallback row and the sidecar states a falsehood in template voice.

I checked whether this bites today: **it does not.** All 69 R-RANK-1
firings across the corpus sit in groups that do contain the reference
arm. But 891 of 2,514 ranking groups lack one, and altwide — where 40 of
the 69 firings concentrate, and where libpcre2 refuses at its own
compiled-size ceiling — is precisely the set that generates them. This
is one re-pin away from firing.

The design already has the detector (R-RANK-3) and does not wire it as a
guard. **Remedy:** R-RANK-1 must not fire in a group R-RANK-3 fires on;
better, ask the reporter for a `baseline_is: reference|best` header or
column (a one-line reporter change of the same shape as Q1's
`floor_pattern:` proposal, and it should ride with it).

---

## F6 — BLOCKING (scope gap). The charter's own acceptance test names four findings. One of them — the `vm-in` result, i.e. `[OPT-1]`, the single most valuable row the grounding feedback produced — has no rule, and no rule CLASS, in the design. The six classes are all cross-pin or status-shaped; `[OPT-1]` is same-pin, cross-config.

Frank's blinded test (plan.md:92-95): *"catalogue v1 must find,
unprompted, the collapse, the three inconclusive records, the give-ups
and the vm-in result."* The design covers three of four with real rules
(R-DELTA-2, R-STATUS-2, R-STATUS-3/12). For the fourth, §10 A.4 offers
"R-BUCKET-VSBEST plus the ranked rows themselves" and then concedes:
*"if v1 cannot make a reader see this pair without a human pointing at
it, that is a finding against the design."*

It cannot, and it is. R-BUCKET-VSBEST fires on the *group* and says
nothing about `vm-in` versus `vm`; it says "two pins are present, read
the Δ column". The two rows it is supposed to surface (12,546 ns vs
28,997 ns, both at pin 692c2e8) are the *same pin*, so no Δ rule reaches
them, no rank rule reaches them (cross-pin pairing by construction,
§4.3), and no bucket names them. On Report B the sidecar would print
~130 R-BUCKET-VSBEST bullets, one of which is adjacent to the pair.

The gap is structural, not accidental. Look at what the two grounding
documents actually produced: `feedback_…-repin.md` §1 lists five
candidate rows, and (a) `vm-in` vs `vm`, (c) the DFA `\z` form 3.7×
slower than the VM form, and (d) VM compile cost 3-4× DFA's are **all
same-pin comparisons between two arms of one engine**. Three of the five
highest-value readings in the corpus that chartered this tool fall
outside all six classes. `[OPT-1]`, `[OPT-2]` and `[OPT-C]` were all
chartered at pcrec off same-pin cross-config gaps.

The six classes came from Frank's list, and the design is faithful to
the list — but the same journal entries that gave the list gave the
`vm-in` acceptance item, and the design should have noticed that its
classes do not span its own acceptance test. Under-delivery against the
charter, not scope creep.

**Remedy.** A seventh class, and it needs no new threshold: R-ARM — two
testee ids in one ranking group that differ in exactly one config token
(`vm` vs `vm-in`, `auto` vs `auto-noedge`, `caps` vs `nocaps`, gcc vs
`-clang`), at the same pin, whose medians differ by more than the
reporter's own spread rule (`2 × max(stddev)` — the identical
arithmetic R-DELTA-1 inherits from `_cross_pin_verdict`, applied
within-report instead of across-pin). That is a copied threshold, not a
new one, so §4's "no tuned constant" survives; the testee-id composition
rule (`record_schema.md` §6.4) already gives the token split; and the
deny-flag testees (`-noedge`, `-noisland`, `-noclsfold`, `-align64`,
`-bigcap`) exist *only* to be read this way, so the class would fire on
every AFTER window the project runs. This is the single largest
improvement available to the design.

---

## F7 — SHOULD-FIX. R-PRED is the thinnest of the six classes: its input format cannot express the majority of the project's real predictions, its verdict vocabulary is missing the verdict the ledgers actually use, and the acceptance test runs with the class switched off.

§6.2 surveys three predictions, declares them the three shapes, and
concludes "All three are the same shape". The survey is too small. The
project's only committed, scored prediction set is
`bench/syntax/NOTES.md` P1-P13, scored in
`docs/dev/ledgers/2026-09-07-b36-syntax-first-d34c9131.md` §7. Against
that ground truth:

- **A fourth shape: exact set identity / count over a population.** P1 —
  *"exactly these fifteen patterns are `did-not-compile`, each naming a
  module … any refusal outside the fifteen is an R1 outlier."* §6.3 has
  no `count` reducer, no numeric `eq` (only `eq-token`), and no
  set-membership op. Inexpressible.
- **A fifth shape: an ordering claim across patterns.** P5 — *"`^item`,
  `\Aitem` and `\Gitem` are the three cheapest throughput cells in the
  set on every testee."* Scored by the ledger with pattern-ranks
  ("`\Gitem` is rank 12 on `vm`"). §6.3 offers `quantity rank`, but
  `rank_or_na` in the TSV is the rank of a **testee within a
  (pattern, regime) group** (`report.py:4137`), not of a pattern within
  a set. A prediction author reaching for `rank` will get a number that
  means something else — a live trap, and one §6 does not warn about.
  Computing the real quantity needs a cross-pattern ordering the TSV
  does not carry, which §2.4 forbids `interpret` from deriving.
- **Predictions about answers and spans.** P2 (the wrapper changes two
  specific answers), P9 (`asr-k-uc` reports span [4,9]), P10 (semantics
  on two subjects). The report TSV carries `n_wrong` and `pass_rate`,
  never an answer or a span. These are the predictions that found
  KB-14 — the class the tool most wants and least can have.
- **Compound predictions are the norm, not the exception.** Ten of
  thirteen were scored per-clause: *"half CONFIRMED, half untestable"*
  (P2), *"CONFIRMED on 4/6, REFUTED on the forced VM"* (P5), *"answers
  CONFIRMED, cost REFUTED everywhere"* (P12), *"short CONFIRMED, tput
  clause REFUTED"* (P8). §6's one-row-one-bound format forces
  decomposition into independent rows, which is defensible — but then
  the ledger's actual headline finding, *"the clause the author was most
  confident in failed; the one with least confidence held"* (P3),
  is not a thing the format can even represent.
- **The verdict vocabulary is missing a verdict.** The ledger's tally is
  *"three CONFIRMED outright, five REFUTED, five PARTIAL."* R-PRED's
  trichotomy is confirmed / refuted / not-evaluable. `PARTIAL` — the
  modal outcome, 5 of 13 — has no rule.

And §6.5 declines to back-fill, while §10 runs all three acceptance
reports **with no predictions file**. So the class Frank named — and
arguably the one with the highest value, since a prediction not scored
is the failure mode `feedback_…-repin.md` §3's eighth row records
literally ("UNCOVERED by any prediction") — ships with a format never
tested against real data and an acceptance test that cannot detect the
gap.

**Remedy.** Transcribe P1-P13 *before* implementation and use them as
the format's acceptance test: a format that can express ≥ 9 of 13 and
reproduce the ledger's 3/5/5 tally (with `partial` as a fourth verdict,
or an explicit ruling that compound predictions must be decomposed at
authoring time and P-ids get clause suffixes) is a format worth
building. One that expresses 4 of 13 should be redesigned now, not after
a lane has written the loader. This is cheap: the data exists and the
answers exist.

---

## F8 — SHOULD-FIX. §10 is not falsifiable as written: two of its own MUST items are self-cancelling, and it has no null control and no false-positive budget.

The section's virtue is real — writing the acceptance test before any
code, naming reports and numbers, is exactly right, and it should
survive into the implementation lane unchanged in that respect. But as a
pass/fail instrument it leaks:

1. **A.4 is both required and not.** It is a numbered MUST-surface item
   and then: *"Stated as a risk, not a pass."* §10's closing sentence
   says acceptance is "iff … it surfaces every numbered MUST item". A
   later lane can cite either sentence. (Per F6 the honest resolution is
   that A.4 fails today and needs R-ARM.)
2. **C.3 states two different bars in one paragraph** — "R-BUCKET-KB
   fires on both of those, and names them" versus "at least two of the
   three must be recognised" (of KB-13/14/15, only two are claimed at
   all). Per F2 the answer is zero.
3. **No null control.** The panel brief's instinct is correct: there is
   no report in the acceptance set on which the tool should stay quiet.
   Nor can there be — R-STATUS-5 and R-FLOOR-1 fire on essentially every
   committed report. The equivalent that *is* constructible is a
   synthetic clean report as a §8 fixture ("a report where every record
   is `measured`, no cell is excluded, no Δ is outside spread → zero
   firings across all 27 rules"), and it should be required.
4. **No false-positive budget.** The MUST-NOT lists are three
   hand-picked claims per report; they say nothing about the other ~275
   bullets (F3). The only whole-report opinion check is §8(5), which F1
   shows is vacuous.
5. **Coverage.** Of ~27 rules, the acceptance test exercises about 12.
   R-PRED (4 rules) is inert by construction; R-RANK-2, R-RANK-3,
   R-FLOOR-3, R-BUCKET-SPAN, R-BUCKET-DOMINATED, R-STATUS-7/8/9/11 are
   named only in did-not-fire tables or not at all. All three reports
   are `budu-ryzen1600`, so R-STATUS-6-style population mixing is
   sampled once by accident.

---

## F9 — SHOULD-FIX. §1.1 excludes "rankings of importance"; §9.2 then renders one. The design's real position — that the catalogue IS the opinion, made once and reviewed — is defensible and is never stated.

§5 says output order is the catalogue's declaration order, "which is
stable and therefore diffable". §9.2's specification-of-output orders
sections R-STATUS-5, R-STATUS-2, R-STATUS-6, R-STATUS-3, R-STATUS-12,
R-DELTA-1, R-DELTA-2, R-DELTA-4, R-BUCKET-FORM, R-BUCKET-VSBEST,
R-FLOOR-1. That is neither id order nor class order; it is a *reading
order* — population summary first, then the headline absence, then the
exclusions. Either §9.2 contradicts §5, or declaration order is an
editorial ranking and §1.1's exclusion is nominal.

I do not think the ranking is wrong. I think the note's framing is. The
choice of which 27 questions exist, their grouping into six classes, and
the order they are asked in are all editorial acts — unavoidable ones,
since a fact-finder that asks *every* expressible question of a TSV is
`grep`. §0's claim that the design "*cannot* creep past" its scope
overstates what architecture can do, and the overstatement is what makes
F1 and F2 possible: if opinions are structurally impossible, no one
needs to review the templates or the signatures.

The stronger and truer claim is available: **the catalogue is where this
project's opinions are deliberately concentrated** — stated once, in one
versioned file, with a threshold source per rule, diffable, reviewable,
and bumpable — rather than re-improvised in prose every time a report is
read. That claim survives F1 and F2 and turns them into requirements
(review the templates; raise the bar on signatures) instead of
contradictions. §0 and §7 should say it.

---

## F10 — SHOULD-FIX. The did-not-fire reason is specified as a closed token set and rendered as free text.

§5: *"A non-firing rule always emits a row with `fired=0` and a reason
in `value`: `no-matching-rows | input-absent | grain | reporter-version
| retired`."* §9.2 renders: `no-matching-rows (mixed_x13: False)`,
`no-matching-rows (every record reads `agree` or `n/a (v1.x)`)`,
`no-matching-rows (no `role: floor` pattern in email-specimen@0.1)`,
`input-absent (no subject-grain TSV supplied)`.

Those parentheticals are useful and are also a second prose channel that
§7.1's renderer contract does not cover (they are not `template.format`
output). Either they come from a per-rule `no_fire_template` with
declared slots — same discipline, one more field — or they go. As
written they are the second place (with F1's templates) where a lane can
add a sentence nobody checks.

---

## F11 — WORTH-NOTING. R-RANK-2 is probably incoherent, and R-RANK-3 is misfiled. The "rank flips" class is one real rule wearing three.

R-RANK-2 fires on *"a cross-pin pair whose `rank_or_na` order
contradicts its own `delta_verdict` direction"*. But `rank_or_na` is a
position among **all testees in the group** and `delta_verdict` is a
comparison of **one testee against its older pin**. There is no reason
these must agree: a cell can get faster across a pin and still lose
rank because a different testee got faster still. So the rule's
predicate encodes an expectation that is simply false in general, and
"contradicts" is an interpretive word for what is usually an ordinary
consequence of a third row moving. It is also the only rule in §4 with
no worked example — which is itself the tell.

R-RANK-3 (reference arm absent from a group) is a population caveat, not
a rank flip; it belongs in R-STATUS, and per F5 its real job is to gate
R-RANK-1. As it stands the class Frank named contains one rule that does
what he asked (R-RANK-1), one that probably should not exist, and one
that is filed under the wrong heading. Compare R-STATUS's twelve. Class
sizes are not obligations, but a reader of §4 will read three rules as
three rules' worth of coverage.

Related: the plan row requires the catalogue to carry *"a worked example
from a real report"* per rule. The note supplies real examples for about
11 of ~27. The twelve without one — R-STATUS-5..11, R-DELTA-3, R-RANK-2,
R-FLOOR-3, R-BUCKET-SPAN, R-BUCKET-DOMINATED, all four R-PRED — are
where the false positives will concentrate, and the charter's
example-per-rule requirement is precisely the discipline that would have
caught R-RANK-2 at design time.

---

## F12 — WORTH-NOTING. Q4 (§7.4) is framed as a charter deviation more dramatic than it is, and the fallback it offers is worse than either horn.

The plan row says the skill "phrases the fired rules into a SIDECAR".
The note reads "phrases" as "generates prose at run time", finds that
incompatible with byte-reproducibility, and escalates.

There is a third reading the note does not consider: the phrasing *is*
the skill's, authored once by a human or a model as the catalogue's
`template` fields, committed, reviewed, and then applied
deterministically by the renderer the skill invokes. Under that reading
nothing is deviated from — the sentences are written by the same kind of
author the charter imagined, just written *before* the run rather than
during it, which is strictly better for a project whose whole discipline
is stating things before measuring them. The byte-reproducibility goal
and the charter's letter are both satisfied.

That reading has a condition, and it is F1: it only holds if template
text is reviewed *as prose*, by a person, at authoring time. So Q4 and
F1 should be ruled together — "the renderer phrases; the templates are
reviewed prose; §8 gains a template-diff gate" answers both, and Frank
need not adjudicate a deviation at all.

The offered fallback — a `## Reader's note` section excluded from the
byte-equality check — should be explicitly rejected rather than held in
reserve. It creates exactly the unchecked prose channel the firewall
exists to prevent, inside the artifact the firewall is about, and it
would make §8(3) and §8(5) both partial. If Frank wants a human note, it
belongs in the ledger, which is where human readings already live and
which nothing here proposes to change.

---

## F13 — WORTH-NOTING. The design's value proposition is real but smaller than §0 implies, and its strongest acceptance claim is circular. Say so, and the tool is easier to accept.

§0: a ledger is 1,085 lines, most of it judgment, but "a measurable
fraction is not judgment at all". The fraction is never measured. From
the firing counts in F3 and the [B36] ledger's structure, the honest
estimate is: the interpreter mechanises the *inventory* sections of a
ledger (which records, which exclusions, which refusals, which Δs) and
touches almost none of the *reading* sections.

The circularity is in §10 C.3. The three findings that headline the
[B36] read — KB-13, KB-14, KB-15 — are offered as proof of the tool's
reach. But they were found by an opus lane reasoning about driver
semantics against expectations, and the interpreter's claim is only that
it can recognise them *after* they were diagnosed and registered (and
per F2 it cannot even do that). On the sample where they mattered — the
first syntax sample, 2026-09-07 — `interpret` would have printed 23
R-STATUS-3 bullets among ~275 and named no defect. That is not a
criticism of the design's honesty (it is careful to say the interpreter
never diagnoses); it is a criticism of using post-hoc registration as
evidence of strength.

What the tool would genuinely have bought on that sample: the three
`inconclusive-load` records nobody would have listed by hand (A.1 — the
one claim that requires `store/index.tsv`, and the design is right to
put it first), the give-up code pairing (A.3b), and the refusal
inventory. Those are worth having *every time*, cheaply, forever. That
is a good enough case; it does not need the KB claim.

Two costs to weigh against it, neither stated: §8(3)'s freshness check
couples every future reporter change to a regeneration of every
committed sidecar (Q5's recommendation — three at landing — correctly
limits the blast radius, and should be adopted); and a generated
artifact committed beside every report is a thing future readers must
learn *not* to mistake for a reading.

---

## F14 — WORTH-NOTING. What the design gets right, so the rulings do not sand it off.

Recorded deliberately, because several findings above ask for additions
and the note should not be re-opened on its good parts:

- **No rule introduces a tuned constant.** I checked every threshold in
  §4: each is either a token the reporter already computed
  (`timer-floor`, `faster ×N`, `selection changed`, `agree`), a header
  integer, or a definitional 1.0 named as definitional. This is the
  single best property of the design and the reason it is safe to build
  at all.
- **"The interpreter must never be able to disagree with the report
  about whether something moved"** (§4.2) is the correct architectural
  choice, correctly implemented by reading `_cross_pin_verdict`'s string
  rather than re-deriving the comparison.
- **Reading the TSV and never the markdown** (§1), with the reason given
  (parsing a rendering makes a reader depend on a legend's wording).
- **§6.4's `stated_utc` precedence check** — asserting a prediction's
  timestamp precedes the earliest record timestamp in the report's
  population, so post-hoc prediction "is mechanically impossible to
  commit unnoticed". That is a genuinely excellent piece of design and
  is worth keeping even if §6 is otherwise rebuilt per F7.
- **§8(4)'s minimum-diff control requirement** ("a fixture pair that
  diverges in ten places does not prove which byte fired the rule") —
  the project's controls-share-no-source discipline applied correctly to
  a new surface.
- **§10 written before any code exists**, and Q1/Q2/Q8's recommendations
  (ask the reporter for the column rather than reaching outside the two
  declared inputs) all point the right way.

---

## Overall verdict

The design honors "no opinions, all based on facts" at the layer it
looked at, and does it unusually well: no rule invents a threshold, the
one boundary that matters is read as a string from the reporter so the
two can never disagree, and the acceptance test was written before the
code. But the firewall is built around the run-time surface — slots,
links, sentence count — and the opinions in this system do not live
there. They live in the catalogue: in the fixed prose between the slots
(F1, where R-STATUS-12 asserts a mechanism in template voice), in which
signatures get registered as "facts with a source" on evidence that
cannot discriminate them (F2, measured: the KB-13 signature is not in
the TSV), and in the declaration order that §1.1 says is not a ranking
and §9.2 renders as one (F9). Three of those are governed by a MINOR
bump, the lowest bar the design defines. Against scope, the design holds
its exclusions honestly but under-delivers in two places that the
charter itself names: R-PRED ships a format that cannot express most of
the project's real predictions and an acceptance test that never
exercises it (F7), and no rule or class reaches the same-pin,
cross-config comparison that produced `[OPT-1]`, `[OPT-2]` and `[OPT-C]`
— three of the five candidate rows in the very feedback document this
design cites as its grounding input, and one of the four items in
Frank's own blinded test (F6). Add to that a group-key definition that
contradicts `report.py`'s deliberate one and silently breaks
R-BUCKET-FORM (F4), and a firing density on modern reports — 202
R-DELTA-1 bullets on bounded@0.3, 190 R-FLOOR-1 and 60 refusals on
syntax, with ranking and bands both excluded on principle — under which
the acceptance items are present but not findable (F3). My verdict:
**the architecture is sound and worth building, and this note is not yet
the thing to build.** Rule on F1/F2/F4/F6 and the density question,
re-derive the rules from `_ranking_groups` rather than from the TSV
header, test §6 against P1-P13 before a loader exists, and re-state §0's
claim as "the opinions are concentrated in one reviewed, versioned file"
rather than "opinions are impossible" — with those, v1 delivers what
Frank asked and can be defended when it is wrong.
