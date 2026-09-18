# r7 — predicate_audit_v1.md, lens: catalogue/interpreter versioning and contract consistency

Read-only critic pass on `docs/design/predicate_audit_v1.md` (lane
`b50predaudit`). Lens: for every proposed fix and every §7 question, is
its MINOR/MAJOR label correct against `catalogue/rules.toml`'s own
stated bump rules and `interpreter_v1.md` §3.3's derivability test; does
any fix silently move a committed sidecar without the regeneration the
version rules require; does the note respect the full regen surface set;
does it cite its contracts accurately; and does F27's fix need a version
signal anywhere, with the stated-before-the-run discipline argued both
ways.

Numbered r7ver-1..9, BLOCKING / SHOULD-FIX / WORTH-NOTING. Nine findings:
four BLOCKING, four SHOULD-FIX, one WORTH-NOTING.

---

### r7ver-1 — BLOCKING. F7's Group-1 placement ("no sidecar regeneration") contradicts the finding's own committed witness

`predicate_audit_v1.md` §4 F7 (lines 367–382) proposes scoping
`_ELSEWHERE` by quantity class, and its own witness paragraph (lines
375–379) quotes a **currently committed** sidecar rendering the bug:

> *"P13 … confirmed: … measured P13: worst … = 2.543 over 834 value(s);
> also present in: did_not_compile (172), excluded (23)"*

and says the fix removes the false `excluded (23)` clause on exactly
this line. That is a change to what a **committed** `reports/*.
interpretation.md` sidecar renders. Yet §6 (line 847) files F7 under
**"Group 1 — code only, no catalogue bump, no sidecar regeneration"**
alongside F7b, F15, F16, F19.

`interpreter_v1.md` §3.3's bump rule (`docs/design/interpreter_v1.md:
752-760`) is explicit that regeneration is forced by content, not by
version-label bookkeeping: *"a committed sidecar is generated, and `make
check-interpret` re-renders every committed `reports/*.interpretation.md`
from its recorded inputs and requires byte equality. So a … change that
changes any rendering forces regeneration of every affected sidecar **in
the same commit**."* F7 is exactly this case — a fix whose own write-up
names the committed file it moves. Placing it in the "no regeneration"
bucket is not merely an omission; it directly misstates what `make
check-interpret` section 3 will do the moment this fix lands, and the
recommended order in §6 (F7 lands early, in "Group 1 entire," before the
panel has approved any regeneration) does not budget for that failure.

**Fix:** move F7 (and audit F7b — see r7ver-2) into a group that pays for
sidecar regeneration; the syntax sidecar cited above must be listed as
an affected file the same way F1/F2/F5/F8/F9/F18/F20/F21/F22 already are
under Group 2.

### r7ver-2 — BLOCKING. F7b's own fix shape requires a catalogue MINOR bump; Group 1 says "no catalogue bump"

F7b (lines 384–397) closes with **"Fix: … Code + `example` correction"**
— an edit to R-PRED-3's `example` field in `catalogue/rules.toml`. The
catalogue's own versioning rule, stated identically in three places —
`catalogue/rules.toml:19-23`, `catalogue/CLAUDE.md:66-68`, and
`interpreter_v1.md:730-733` — lists **"an `example` refreshed"** as one
of the enumerated MINOR-bump triggers, on the same footing as a template
wording change or a link add. F7b's own stated fix therefore *is* a
catalogue change by the contract's own text, and by §3.3's discipline a
MINOR bump forces the same full-sidecar regeneration r7ver-1 already
flags. §6 nonetheless files F7 **and** F7b together under "Group 1 —
code only, no catalogue bump, no sidecar regeneration" (line 847).

This is not a nitpick about which bucket a fix sits in: F7b's finding
text (line 391) quotes the exact catalogue string the fix corrects
(`interpret_subject_grain_v1.md` §1.4's grain blindness, "the pattern is
a refusal at this pin … cell is in the `did_not_compile` section"), so
the note has already identified the literal field to edit — it just
mis-costs the edit two sentences later.

**Fix:** split F7b into its code half (Group 1, if it stands alone) and
its `example`-field half (Group 2, MINOR + regeneration — note that an
`example` edit is *not* one of the four fields (`template`/`no_fire`/
`legend`/`links`) `catalogue/CLAUDE.md`'s §8(6) reviewer-approval gate
names, so this half needs the version bump and regen but not necessarily
the named-reviewer commit line; state that distinction rather than
folding it into "code only").

### r7ver-3 — BLOCKING. The note never addresses `INTERPRET_VERSION`, a second, independent version stamp every sidecar carries, whose bump rule no design document states

Every rendered sidecar's stamp block carries two separate version
fields, built in one place (`build_stamp`, `pcrecbench/interpret.py:
2173-2204`):

```
("catalogue", cat["catalogue_version"]),   # interpret.py:2200
("interpret", INTERPRET_VERSION),          # interpret.py:2201
```

`INTERPRET_VERSION = "v1"` (`pcrecbench/interpret.py:54`). A repo-wide
search of `interpreter_v1.md`, `interpret_subject_grain_v1.md`,
`predicate_audit_v1.md` and `catalogue/CLAUDE.md` for `INTERPRET_VERSION`
returns **zero hits outside the code itself** — no document states when
this field should bump. `git log -p -- pcrecbench/interpret.py` shows it
has never moved from `"v1"` since it was introduced, across every
catalogue bump from 1.0 to 2.0 and across multiple documented code
changes to `interpret.py` (the `[B47]` subject-grain routing/`build_stamp`
change, among others).

`interpreter_v1.md` §3.3 (line 757) explicitly models the catalogue's
own regeneration discipline on `REPORTER_VERSION`'s precedent: *"This is
exactly the precedent `REPORTER_VERSION` set … 'bump whenever rendering
changes, so two reports are never mistaken for each other,' applied one
layer up."* That same logic, applied one layer up **again**, argues
`INTERPRET_VERSION` should bump whenever a pure code change (no catalogue
text moves) alters what a sidecar renders — precisely the situation
r7ver-1 shows F7 creates, and the situation F15, F16, F19 and F27's
`check_stated_utc` fix all create by the note's own account (§6: "Group
1 — code only…"; Group 5: "F27 … Code only, no catalogue change, but it
changes what the tool REFUSES"). The note proposes **no version signal
of any kind** for any of these — not a catalogue bump (correctly, since
none of these touch `rules.toml`), but also not an `INTERPRET_VERSION`
bump, which is the one mechanism that exists for exactly this class of
change and which the note never mentions.

The practical consequence: `make check-interpret`'s byte-equality
freshness check (§3) will still force every affected sidecar to be
literally regenerated (content drives the check, not the stamp), so
nothing is *silently* stale — but the regenerated sidecar's own stamp
line will read `interpret: v1` both before and after F7/F15/F16/F19/F27
land, so a reader (a Claude session, per Frank's directive that this
audit itself executes) has **no way to tell from the stamp** that any of
these fixes has been applied to the tool that produced the file they are
reading. This is the exact class of "context around the numbers" defect
Frank's 2026-09-17 directive named, applied here to the interpreter's own
provenance rather than to a rule's population — and it is untouched by
this audit despite the audit covering `build_stamp`'s cousin fields
(`report_sha256`, `predictions_sha256`, `subject_grain_sha256`) closely
enough to cite them by name in F27's fix shape.

**Fix:** add a §7 question: should `INTERPRET_VERSION` bump on any code
change that moves a committed sidecar's rendering (the `REPORTER_VERSION`
rule, one layer up), and if so, which of F3/F7/F7b/F11/F15/F16/F19/F27
require it. This changes several of §6's "no catalogue bump" claims from
"free" to "free of a catalogue bump, not free of a version bump" and
changes the true cost accounting the panel is asked to buy into.

### r7ver-4 — BLOCKING. §6's cost groups name only ONE of the four regen surfaces (sidecars); fixtures and goldens are never mentioned

`catalogue/CLAUDE.md`'s own file table names two further generated
surfaces the sidecars sit beside: `fixtures/fixtures.toml` (line 25:
*"65 fixtures … each a real reporter-produced slice plus at most one
declared mutation"*) and `golden/<report>.facts.tsv` (line 31: *"The
pinned facts for §10's acceptance reports"*). `pcrecbench/CLAUDE.md`
describes `make check-interpret`'s fixture section as asserting *"each
rule fires on its sabotage and not on its control, exactly one DECLARED
field apart."* A **new rule** is therefore not just a `[[rule]]` block —
it needs its own control/sabotage fixture pair before `check-interpret`
can certify it, by the same mechanical requirement every one of the 31
existing rules already satisfies.

F9 (lines 419–440) proposes exactly a new rule, **R-ARM-2**, and labels
its version cost *"MINOR (§3.3's own list) and introduces no threshold —
it is an existence rule"* (line 439) with no mention of the fixture pair
`fixtures.toml` would need, nor of whether `acceptance_10.py`'s frozen
Reports A–D fire it (a new rule with a real corpus population — 532
witnessed triples — plausibly fires on at least one of the three named
acceptance reports, which would move `golden/<report>.facts.tsv` too, a
change §8(2)'s table gates separately from a records-only commit). F3
and F4 (Group 3, MAJOR predicate/`inputs`-shape changes) carry the same
exposure: if the fixed coverage computation (F3) or the fixed
denominator (F4) changes which cells fire on any of the three acceptance
reports, `acceptance_10.py`'s pinned facts must be re-derived via
`refresh_golden.py`, which `catalogue/CLAUDE.md` restricts to *"a commit
entitled to move a golden fact."*

§6's four groups and its "recommended order" (lines 842–885) discuss
only two costs — **catalogue bump** and **sidecar regeneration** — for
every fix that touches the catalogue. The fixture and golden surfaces are
never named, so the ordering a panel is asked to approve ("Group 2's F8
and F1/F2 …, then Group 1 entire, then F9, then Group 3's F3 and F4 …")
is priced against an incomplete cost model: F9 in particular is
presented as a cheap, isolated MINOR addition when the project's own
"31 rules, one fixture pair each" discipline says it is not.

**Fix:** add fixtures and goldens as named columns in §6's cost table
(sidecars / fixtures / goldens / reports), state which of F1–F27 touch
which, and re-derive the recommended order against the fuller cost —
in particular checking whether F9's new fixture pair and F3/F4's
possible golden movement change any acceptance-report fact before the
panel is asked to approve the order as cheap-then-expensive.

---

### r7ver-5 — SHOULD-FIX. Q2's MINOR-vs-MAJOR framing is a false dichotomy: neither label is literally triggered when the catalogue text does not move at all

Q2 (`predicate_audit_v1.md:897-902`) asks the panel to rule MINOR or
MAJOR "when the code and the catalogue's `predicate`/`threshold_src`
disagree and the PROSE is right (F3, F11)," and recommends MAJOR because
"the firing set moves and a sidecar stamped at the old version is no
longer derivable — §3.3's own test."

Checked directly against the catalogue text: R-DELTA-4's `predicate`
field (`catalogue/rules.toml:678-683`) already reads *"An R-DELTA-1 /
R-RANK-1 / R-ARM-1 / R-FLOOR-2 firing whose cell no prediction's selector
covers,"* and its `threshold_src` (685–689) already reads *"the coverage
test is a prediction selector's own glob match."* R-BUCKET-SPAN's
`threshold_src` (`catalogue/rules.toml:1213-1220`) already reads *"The
partner is `_cross_pin_info`'s own choice (report.py: same engine and
config, a different version slug, the newest record timestamp strictly
older than this testee's)"* — the FULL population F11 says the code
should search but does not. In both cases F3/F11 fix, **zero characters
of `predicate`, `threshold`, `threshold_src`, `inputs`, or any other
`rules.toml` field would change**, because the declared text is already
correct; only the interpret.py function is wrong.

§3.3's MAJOR/MINOR definitions (`interpreter_v1.md:730-737`,
`catalogue/rules.toml:19-23`) are worded entirely as edits to catalogue
*fields*: "a rule's PREDICATE or THRESHOLD changes," "`inputs` change in
a way that reads a different column." Read literally, a fix that edits
no field triggers neither definition, and `catalogue_version` need not
move at all — there is nothing in `rules.toml` for a diff to touch. That
reading is not academic: if nothing in `rules.toml` changes,
`catalogue_version` cannot be bumped by any mechanical process this
project uses (every historical bump, 1.1 through 2.0, corresponds to an
actual `rules.toml` header-comment-documented text change — confirmed by
`grep -n "^# 1\.\|^# 2\."` returning the four historical entries, each
naming a concrete field move). Recommending "MAJOR" without addressing
that the vehicle for a MAJOR bump (a `rules.toml` diff) does not exist
here is incomplete: what actually needs to happen is either (a) editing
`predicate`/`threshold_src` anyway, purely to re-timestamp the contract
even though its prose is unchanged (an odd, cosmetic diff), or (b)
recognizing this is a code-version question, not a catalogue-version
question — see r7ver-3's `INTERPRET_VERSION` finding, which is the
missing third option Q2's binary framing forecloses.

The recommendation (MAJOR) is defensible as the pragmatic answer — see
r7ver-6 for the precedent that supports it — but the note should say
*why* MAJOR is chosen over "no catalogue change at all," not treat
`catalogue_version` movement as the only lever, when `INTERPRET_VERSION`
sits unused for exactly this purpose.

### r7ver-6 — SHOULD-FIX. Q2 frames the question as novel; the project's own 2.0 bump already set this precedent, uncited

The 2.0 bump's own justification, `catalogue/rules.toml:39-49`, reads:
*"the `_select`'s DEFAULT section read for the four failure-population
quantities … widens … closing a corpus-wide tautology … Both are
`inputs`-shape changes to what R-PRED-1..4 can see, at the SAME MAJOR
bump."* This is the *identical* reasoning shape Q2 recommends for F3/F11:
a change to what a rule's code effectively reads (a "shape" change),
classified MAJOR, without every rule's individual `predicate`/`inputs`
text being edited line-by-line to match (`R-PRED-1`'s own inputs array,
`catalogue/rules.toml:912-940`, is unaffected by the (α) widening's
mechanics — the widening lives in `_select`, a shared helper, exactly
where F3/F11's fixes would live too).

Q2's framing — *"The panel should settle this once; it will recur"*
(line 902) — states this is an open, first-time question. It is not:
the 2.0 bump comment, written by this same project three weeks earlier
in this same file, already answered it for a structurally identical
case. Citing it would strengthen Q2's own recommendation (a working
precedent beats a hypothetical one) and correct the "first time this
arises" framing that undersells how settled the practice already is.

### r7ver-7 — SHOULD-FIX. F27's fix trades a global, unpickable anchor for a report-scoped one, and the note argues only the honesty gain, not the new exploitability

F27 (lines 748–786) and Q7 (929–938) recommend re-anchoring
`check_stated_utc` from "the earliest `store/index.tsv` timestamp for
this `(subbench, version)`" (global, monotonically non-decreasing as the
set accumulates history) to "the earliest index timestamp of the records
**this report actually includes**" (report-scoped, closed over
supersession). The note argues only the direction that motivates the
fix: *"That is strictly what §6.5 wants to prove, it moves forward with
each sample, and it is still store-free"* (line 779).

Argued the other way: the current, global anchor cannot be gamed by
choosing what a `report` command's `--since`/`--until`/`--where` filters
select, because it does not read the report's filters at all — it reads
the whole set's history. The proposed anchor is a function of a
**scope decision made after the predictions were authored** (whatever
report a lane later chooses to generate and interpret). An author who
already knows a later sample's numbers (the exact honesty failure §6.5
exists to catch) could, in principle, construct or select a report whose
`--since`/`--until` window excludes the early records that would make
`stated_utc` fail the check, and pass a `stated_utc` the global anchor
would have refused. This is not a stretch scenario for this project:
`docs/design/predicate_audit_v1.md` §0 itself documents that reports are
built with named, deliberate `--since`/`--until`/`--where` queries
routinely (`reports/CLAUDE.md`'s convention), so report-scope narrowing
is an ordinary, everyday act here, not an adversarial edge case that
needs inventing.

The fix may still be the right one on balance — the false-refusal the
global anchor causes today is a live, blocking problem, and the gaming
scenario requires an author already acting in bad faith, which the check
was never going to catch in every case regardless. But §7 Q7's
"Recommend YES, and first" gives the panel only the honesty gain and
omits the honesty cost, and the note's closing sentence — *"a
`--no-check-utc` style escape is NOT recommended, because an escape
hatch on the one check that keeps a prediction honest is the wrong
default to add"* — reads oddly next to a fix that itself loosens the
same check's floor from a global one to a scope-chosen one, without
remarking on the parallel.

**Fix:** state the trade-off explicitly in F27/Q7 (global-vs-scoped,
un-gameable-vs-scope-dependent) and let the panel weigh it rather than
presenting the re-anchor as a strict improvement.

### r7ver-8 — SHOULD-FIX. Group 5's cost for F27 omits updating `interpreter_v1.md` §6.5 itself, which the finding says is now inaccurate

F27 (line 771) states plainly: *"`interpreter_v1.md` §6.5's own honesty
paragraph names what the check cannot PROVE; it does not name that the
check makes a whole legitimate class mechanically unscoreable."* That is
a claim that a **design document's own prose** is incomplete relative to
the fixed behavior — the same class of drift `interpreter_v1.md`'s own
revision history (v1.0 → v1.4, each bump folding in exactly this kind of
built-vs-designed correction) exists to prevent. Group 5's cost line
(line 877) reads only *"Code only, no catalogue change, but it changes
what the tool REFUSES."* It does not list revising `interpreter_v1.md`
§6.5 as part of the fix's cost, even though the note's own words two
sections earlier establish that the design note is now wrong about what
the check can and cannot prove.

**Fix:** add "`interpreter_v1.md` §6.5 revision" to Group 5's cost list
— consistent with how this project has always folded a built-fix back
into the design note of record (v1.1 through v1.4 each did exactly this)
rather than letting code and design prose diverge silently.

---

### r7ver-9 — WORTH-NOTING. F1/F2's MINOR label is the one in this note that is fully precedent-grounded; use it as the template for the others

F1/F2 (lines 244–266) recommend *"Version: MINOR + §8(6) review + full
sidecar regeneration"* for the did-not-fire reason channel — a new,
declared, slot-free prose field on a rule's own block. This tracks the
catalogue's own history exactly: the 1.0 → 1.1 bump
(`catalogue/rules.toml:66-68`; `interpreter_v1.md` line 58) was *"entirely
the new `legend` field"* — the same shape (a new declared per-rule prose
field, MINOR, §8(6)-reviewed, full regeneration). F1/F2 is the strongest-
argued version label in the note precisely because it cites a structural
analogue rather than asserting the label. r7ver-2/r7ver-5/r7ver-6 ask
for the same discipline elsewhere; this finding is recorded so the
manager does not "fix" F1/F2's treatment along with the others — it
already meets the bar.

---

## Summary for the manager

Four BLOCKING findings (r7ver-1, r7ver-2, r7ver-3, r7ver-4) show that
§6's cost-grouping table cannot be approved as costed: two fixes are
placed in the wrong group by the note's own evidence (F7's committed
witness; F7b's stated `example`-field fix), a whole version surface the
project uses for exactly this class of change (`INTERPRET_VERSION`) is
never discussed for any of the "code only" fixes including F27, and two
of the four regeneration surfaces this project's own tooling gates on
(fixtures, goldens) are absent from every cost estimate in §6. Four
SHOULD-FIX findings sharpen Q2 (a real precedent already answers it,
uncited, and the MINOR/MAJOR binary itself doesn't obviously apply when
no catalogue text moves) and F27 (the fix's own exploitability trade-off
and its owed design-note revision are both unstated). One WORTH-NOTING
finding names F1/F2 as the version-labeling model to copy.

No finding disputes that the underlying predicates the audit identifies
(F1–F27) are real defects — this review is scoped to whether the note's
proposed *versioning* treatment of each fix is internally consistent and
correctly grounded in `catalogue/rules.toml`'s and `interpreter_v1.md`
§3.3's own stated rules, and on that axis four of the note's claims do
not hold as written.
