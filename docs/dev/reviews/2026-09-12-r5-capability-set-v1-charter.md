# R5 — the capability survey set design (`docs/design/capability_set_v1.md`), lens: CHARTER FIDELITY, PROVENANCE/LICENSING, BUILD PLAN

Critic: read-only lane `r5critic-charter`, worktree, 2026-09-12. Target:
`docs/design/capability_set_v1.md` v0.1 "draft for panel" (1,361 lines,
DESIGN ONLY). Judged against: Frank's charter verbatim in
`docs/dev/plan.md`'s `[B42]` row; `docs/design/requirements.md` v3 (ADOPTED
2026-08-25); `bench/syntax/NOTES.md` and
`docs/dev/ledgers/2026-09-07-b36-syntax-first-d34c9131.md` (the Tier A
Q2/Q3 wrapper defect the design cites to cut the `match` regime);
`testees/pcrec/configs.toml`; and, per the brief's provenance ask, direct
fetches of the design's own cited sources.

Eight findings: 1 BLOCKING, 4 SHOULD-FIX, 3 WORTH-NOTING.

---

## F1 — BLOCKING. One of the design's three "OWED" fetches — cited as live evidence for the risk that would refute the whole design — resolves cleanly on the first retry. The `noseyparker.txt` literal text is not owed; it is sitting at the URL the design itself names.

§3.1 family 4 (`wild-secrets`) states the source's "pattern text fetched?"
column as **NO — categorical description only. Literal text STILL OWED**
(N1 §1). Appendix A repeats it identically, and closes with "**Three OWED
fetches gate L1**, none of them blocking this design: the
`noseyparker.txt`'s literal patterns, CRS 942360's full text, and the CVE
index for family 10's inspirations." §13 finding 3 — one of the THREE
named things that "would refute the whole design" — cites exactly this
gap as live evidence: "the wild share collapses" if "the verbatim-quotable
text is much thinner than N1's fetches suggest (rebar's `noseyparker.txt`
literal text is still OWED; no Suricata sample was obtainable in three
attempts)."

I fetched `https://raw.githubusercontent.com/BurntSushi/rebar/master/benchmarks/regexes/wild/noseyparker.txt`
directly — the exact path N1 §1 (as corrected by its own `b42wild2`
follow-up, quoted in the design's citation chain) already names — in one
WebFetch call. It returned real, quotable, Unlicense-covered regex text
immediately: 30+ verbatim patterns for AWS access keys, GitHub/GCP/Azure/
Dynatrace/Figma tokens, generic `username=...password=...` pairs, and
more — exactly family 4's stress mechanism ("many short, first-byte-
distinct token patterns; high-entropy literals with structure"). There
was no categorical-description wall; the file is a plain text file, one
pattern per line, and it worked on the first attempt.

This means: (a) family 4's "designed members" fallback ("2-3 authored
token shapes in the same idiom if the re-fetch fails") is unnecessary —
the wild source is available and should supply verbatim members instead;
(b) the target-member count for family 4 (currently 4, §3.1) is
under-provisioned against what the source actually offers; (c) most
importantly, §13's finding-3 refutation condition is graded on stale
evidence — the panel and Frank are being asked to weigh a "what would
refute this design" risk that a five-minute re-fetch already narrows from
three OWED items to (at most) two. The design should not present this as
an open risk without first spending the trivial re-fetch it already knows
the URL for.

**Remedy.** Before this note goes to Frank: re-fetch `noseyparker.txt`
(confirmed working above), pull its licence-permitted verbatim patterns
into family 4's target-member table, and correct Appendix A's "three
OWED" count. Independently re-attempt the other two OWED items (CRS
942360, the CVE index) with the same directness before treating §13
finding 3 as a live, unresolved risk to carry to the panel.

---

## F2 — SHOULD-FIX. §2.2's reason 3 for rejecting `bench/syntax@0.2` proves too much: it disqualifies a version bump this same design plans to make for itself.

§2.2 reason 3 argues a version bump to `syntax@0.2` "throws away the
first sample" because "records compare only within one `id@version`
(`requirements.md §5`), so `@0.2` makes the ledger's 285 rankings
incomparable with anything measured after it. That is a real cost with no
offsetting benefit."

`requirements.md §5` actually says: "a sub-bench version is a frozen
snapshot; records compare only within the same sub-bench version; bumping
is a deliberate, logged event." Nothing in that rule destroys the old
version's records — `syntax@0.1`'s 285 rankings stay exactly as valid and
citable as they are today. The only real cost is that *future*
measurements land in a new version and no longer compare directly against
the old baseline — which is the cost of *every* version bump, unavoidably,
by the rule's own definition.

The design's own §4.5 and Q8 propose exactly this cost for itself: Davis
et al.'s corpus is explicitly deferred to "`capability@0.2`... the first
candidate," described as "one sidecar line plus an expectation
re-derivation, not a redesign" (§3.5's closing paragraph, on the `match`
regime, uses the identical framing for its own future 0.2). If reason 3
is decisive against extending `bench/syntax`, it is equally decisive
against ever adding Davis to `bench/capability`, which the design does
not treat as disqualifying there. Reasons 1 (registry-enumeration
mismatch), 2 (incompatible bodies) and 4 (blinding-discipline conflict) in
§2.2 look independently sufficient to support the §2 decision on their
own; reason 3 should be dropped or reframed as "a cost every version bump
shares, not a decisive one," so the panel does not read §2 as more
overdetermined than it actually is.

---

## F3 — SHOULD-FIX. Q3 (Vectorscan's boolean-grain relaxation) is marked DEFAULT, but it is not an open design question — it is a proposed exception to an explicit, dated Frank ruling, and DEFAULT's own definition doesn't fit that shape.

§5.6 states plainly that option (B) "narrows `requirements.md §4.5`
constraint 1 ('results identical on EVERY subject') for one engine. That
is a real relaxation of a Frank ruling and must be visible in every
report row, not a footnote." `requirements.md §4.5` constraint 1 is not a
default this design is filling in — it is Frank's own words, ADOPTED v3,
dated 2026-08-25: "The results must be the same — no variation in
results... There is no 'approximates with stated differences' grade: a
variant whose answers differ from the expectations anywhere is INVALID
for that testee." §12's preamble defines DEFAULT as "this note's
recommendation stands unless Frank says otherwise" — a sound default for
a genuinely open question, but backwards for a proposed carve-out from a
rule Frank stated in his own voice: silence should not carry an exception
to an existing personal ruling, only a fresh answer to an unruled
question.

The design's own trigger for Q3 ("[B7]'s Vectorscan lane") means nothing
is built on this question today, so marking it BLOCK costs nothing now —
Frank can rule it whenever he reads this note, and the ruling simply
travels forward to [B7]. Recommend re-marking Q3 BLOCK (or at minimum
flagging it to the manager as requiring an explicit ruling before [B7]
opens, never a silent default), consistent with how Q1/Q2/Q10 are already
treated as needing Frank's word rather than the design's own.

---

## F4 — SHOULD-FIX. §7.4's own reasoning for scoping `ru_maxrss` to native-driver testees is the apples-to-apples cut charter requirement (3) asks for — yet the design still blanket-excludes it from ranking, undermining its own traceability claim in §1.1.

§1.1 claims requirement (3) ("other metrics... apples-to-apples where
reasonable, the non-comparable stated") is satisfied by §7, "one table
saying what is RECORDED, what is SCORED, what is CAVEATED... per metric
and per engine class." §7.4 restricts `ru_maxrss` recording to
NATIVE-driver testees specifically *because* pooling it with python/perl
would compare a process-level number dominated by interpreter startup
against one that is not — i.e., the design's own stated reason for the
native-only cut is to reach an apples-to-apples population. Having made
that cut, §7.4 and §7.5 then declare the metric "never ranked, on any
testee" with no argument for why native-vs-native comparison specifically
remains unreasonable once the incomparable population (python/perl) is
already excluded.

This is the metric requirement (3) most directly names ("memory...
apples-to-apples where reasonable") and the design's own scoping already
does the reasonableness work; declining to rank it at all — rather than
ranking it within the native-driver population it just carved out — reads
as a metric requirement (3) would expect scored quietly demoted to
caveated-and-shown-only, which is exactly the failure mode the brief
asked this lens to check for. Recommend either ranking `ru_maxrss` within
the native-driver class (mirroring how compile time is ranked "within
`cost_class` only," §7.2) or stating explicitly why native-vs-native
`ru_maxrss` is still not reasonable to compare, since as written the
design refutes its own caveat.

---

## F5 — WORTH-NOTING. `pcre2-dfa` sits in §8's "the dial" column without the design ever stating what space-vs-speed tradeoff it represents — and the charter's own wording suggests Frank expected one.

Plan.md's `[B42]` row names, as Frank's own example of requirement (5)'s
"space-saving vs speed dials," the phrase "pcre2 JIT/interp/DFA." The
design's §7.1 states plainly that `pcre2_dfa_match` "has no separate
compile step" and runs "the SAME compiled pattern `pcre2_match` uses" —
i.e., zero space difference and (per §7.1's own note) "a free control:
its compile number should be statistically identical to `pcre2-interp`'s"
— zero speed-dial framing either. §8's row for `pcre2-dfa` puts, in the
column literally headed "the dial," a description of a THIRD EXECUTION
MODEL and two capability lines it crosses (`captures`, `k-reset`), never
a space or speed tradeoff. That is a legitimate and valuable thing to add
to the roster (§5.1's note on `span-reporting`/`captures` being
execution-model capability lines, not exotic syntax, is a genuinely sharp
observation) — but it is not the dial requirement (5) asked for, and the
design should say so explicitly (e.g. "not a dial; a fourth engine
identity that happens to cost nothing") rather than let it occupy the
dial column silently.

---

## F6 — WORTH-NOTING. §8's pcrec row lists axes, not dials — the traceability table's claim that "pcrec's own dial set... is represented as such" is asserted, not shown.

§8's pcrec row under "the dial" reads: "engine mode, captures, caps, cc,
deny flags" — a list of `testees/pcrec/configs.toml`'s axes, not a
statement of which of them trade space for speed. Reading
`testees/pcrec/CLAUDE.md`/`configs.toml`'s own vocabulary: `nocaps`
removes capture-reporting overhead (a genuine speed dial); the `-bigcap`
pair raises an emitted-size cap to let compiles SUCCEED that would
otherwise refuse (a capability/size trade, arguably the "space-saving"
half, but framed backwards — it trades MORE space for fewer refusals, not
less space for less speed); `-noedge`/`-noisland`/`-noclsfold` are
pcrec's own optimization-denial controls, built to isolate a pcrec
mechanism for pcrec-bench's OWN measurement purposes, not user-facing
space/speed choices an end user of pcrec would pick between. Calling all
five "the dial" collapses two different kinds of axis (a real user-facing
tradeoff vs. an internal diagnostic denial flag) into one column. Since
the brief's charter-fidelity check for requirement (5) asks exactly this
("is pcrec's own dial set... represented as such"), the design should
either map pcrec's roster explicitly onto space-vs-speed (naming which
configs are genuinely dials Frank would recognize and which are
diagnostic controls carried along for other reasons) or drop the framing
that it already does so in §1.1's traceability table.

---

## F7 — SHOULD-FIX. §3.5 cuts the `match` regime from families 7-9 by attributing the Tier A Q3 wrapper defect to them, but the cited ledger names only ONE of those three families with a matching failure mode, and one of the three "inherited" defects is independently shown to be a pcrec-specific bug, not a property of the wrapper mechanism the other two are.

§3.5 states: "Families 6 (`(?x)`), 7-9 (`\K`-adjacent, recursion) and 11
(`$` vs `\z`...) would each inherit that defect," citing
`docs/dev/ledgers/2026-09-07-b36-syntax-first-d34c9131.md` §9's Q2/Q3.
Reading that ledger directly: Q3 names exactly three failure modes under
ONE cause (the lexical `(?:...)\z` wrapper) — `(?R)` recursing into the
wrapper (`f-parens`, a recursion pattern — family 9), `(?x)`'s comment
swallowing `)\z` so the pattern refuses to compile (`mod-x` — family 6),
and Q2's `\K` case. But Q2 is a SEPARATE finding from Q3, and its own
"Source" line attributes the defect to `testees/pcrec/driver.c`'s
anchored branch hard-coding `first_s = 0` — a pcrec-specific bug in the
driver's own code, not a structural property of the `(?:...)\z` wrapper
the way `(?x)`'s comment-eating and `(?R)`'s recursion are (both of which
are lexical consequences of wrapping ANY pattern in those constructs,
regardless of driver). Q2's own text even separates the two: "the same
defect silently converts every `\K`... into a wrong answer on **one whole
testee family**" (singular defect, not folded into Q3's "one mechanism").

More importantly: nothing in §3.1's family 7 (`cap-backref`) or family 8
(`cap-lookaround`) "stress mechanism" or "designed members" columns
mentions `\K` at all, and no member of either family is shown anywhere in
the design to use it. The citation for excluding `match` from families 7
and 8 specifically is therefore unsupported as written — family 9's
exclusion is well-grounded (recursion, directly in Q3), family 6's is
well-grounded (`(?x)`, directly in Q3), but 7 and 8 need either a
`\K`-bearing member actually named in their rosters or a different,
independently-stated reason for their exclusion. As written, the
grouping "7-9 (`\K`-adjacent, recursion)" reads as three families cut by
association with one shared parenthetical rather than three families each
shown to hit the cited defect.

---

## F8 — WORTH-NOTING. The build plan's lane order has the sequencing gap the brief asked about, though a mild one: L3 is credited with `patterns.rxt` and the §4.1 provenance generator, but the §9.4 gates that VERIFY `patterns.rxt` against the sidecar are explicitly L4's, so L3 cannot self-check the file it authors.

§11.1 assigns `patterns.rxt` to L3 and, separately, "the four §9.4 gates
with their positive controls" to L4 ("the `.rxt` loader"). Of those four
gates, "block ↔ sidecar" (do the `.rxt` block names equal the sidecar's
`[[patterns]]` names, both directions) and the "head-parser seam"
(`pcrec --list-source` agreeing with the sidecar) both require either the
harness's new `source_format = "rxt"` loader or a standalone reader —
neither of which exists until L4 lands. `gen_provenance.py --check`
(§4.1, an L3 deliverable) is unaffected since provenance lives entirely
in the sidecar and never touches pattern text, so this is narrower than a
full L3-depends-on-L4 problem — but it does mean L3 ships a `patterns.rxt`
file with no automated proof that its block names match the sidecar's
`[[patterns]]` entries until a whole later lane closes the loop, during
which any authoring slip (a typo in one block's `name`) is invisible.
Recommend either moving the "block ↔ sidecar" gate's core comparison
(which needs only `.rxt`'s block-name grammar, not the full loader) into
L3 as a standalone check, or stating explicitly in §11.1 that `patterns.rxt`
is UNVERIFIED against the sidecar for the L3→L4 gap and naming who is
responsible for catching a mismatch in the interim.

---

## Overall verdict

The design is unusually well-cited — nearly every claim I spot-checked
against the underlying research notes, `requirements.md`,
`record_schema.md`, and pcrec's own `rxt_format.md` held up verbatim or
in substance (the two `rxt_format.md` quotes I checked directly matched
the design's paraphrase closely). The charter traceability table (§1.1)
is honest about what each section does, with one exception worth the
panel's attention: requirement (3) is more caveated than scored in
practice (F4), and requirement (5)'s "named config roster... represented
as such" claim is not actually demonstrated for either `pcre2-dfa` or
pcrec's own roster (F5, F6). The single BLOCKING finding (F1) is the most
consequential: the design asks Frank to weigh a stated refutation risk
(§13 finding 3) against evidence that a direct fetch shows to be partly
stale, and that should be corrected before this note reaches him, not
after. The `match`-regime cut (§3.5) is directionally sound but
overclaims its evidentiary support for two of the five families it
touches (F7). None of these findings challenges the core structural
decisions — a new sub-bench (§2), Option B for `.rxt` (§9), the
pre-compile capability policy (§5.3), the hazard-rewrite rule (§6.3) —
which are all well-argued and, on my read, correctly decided.
