# R4 critic panel — `interpreter_v1.md`, the IMPLEMENTABILITY lens

Reviewer: read-only critic lane, 2026-09-07. Target:
`docs/design/interpreter_v1.md` (1,228 lines, DESIGN ONLY, [B13]).
Grounding read: `pcrecbench/report.py` (`render_tsv`, `_cross_pin_info`,
`_cross_pin_verdict`, `_is_reference`, `_jitter_flag`, `_floor_mean_for`,
`_dominant_subject`, `_gave_up_cell_summary`, `_ranking_groups`,
`_n_and_pass_rate`, the header-comment builder), `pcrecbench/reduce.py`
(`agreement_line` + the v1.4 constants), `pcrecbench/__main__.py` (the
`main()` dispatch), `schema/examples/bad/` + `schema/check_rules.py` +
the `check-schema` recipe, and `Makefile`.

Every number below was measured against the committed corpus (42 report
TSVs, 135,891 data rows, `store/index.tsv` at 160 rows) by scripts run
in the session scratchpad. Nothing was written outside this file.

**The lens.** Assume the design is approved as-is; what surprises,
blocks or slows the lane that has to build it. I have deliberately NOT
argued with the design's purpose, its scope boundary (§1.1) or the
firewall's philosophy (§7) — other panel seats own those.

---

## Summary of severities

| # | severity | finding |
|---|---|---|
| 1 | BLOCKING | §10 A.2's R-DELTA-3 requirement is unsatisfiable under §4.2's own predicate — measured 0 firings in the whole corpus |
| 2 | BLOCKING | §2.1 misstates where the agreement string sits in a `record` row; §4.1 states it correctly. The note contradicts itself about its primary input |
| 3 | BLOCKING | R-STATUS-9's predicate fires on `n/a`; §9.2 asserts it does not. 9 firings on acceptance Report A either way it is read |
| 4 | BLOCKING | §8(2)/(3) golden + freshness checks are coupled to `store/index.tsv` and to `REPORTER_VERSION`, both of which churn. This is KB-8's failure mode, re-created |
| 5 | BLOCKING | §5's facts TSV has no firing ordinal, so one-slot-per-row output cannot be reassembled into firings — which §8(5) requires |
| 6 | BLOCKING | R-BUCKET-SPAN needs "the pin history", which is in neither declared input and is nowhere defined |
| 7 | SHOULD-FIX | the header comment's `; ` delimiter also occurs INSIDE `x13_rules` (3 committed reports). No parse rule is stated |
| 8 | SHOULD-FIX | §7.2's three permitted slot kinds do not cover the note's own templates (at least three rendering-parses and one id decomposition) |
| 9 | SHOULD-FIX | the "row view" is easy to build but is the wrong shape for ≥6 of the 31 rules, and the `inputs` grammar is unspecified |
| 10 | SHOULD-FIX | the fixture plan mis-describes the precedent it claims to mirror; "minimum number of bytes" is not an implementable predicate |
| 11 | SHOULD-FIX | R-STATUS-3's template renders a causeless sentence on excluded rows that exist today |
| 12 | SHOULD-FIX | measured firing volume on the acceptance set is ~420 (B) and ~290 (C) vs §9.2's ~15-bullet specimen; §1.1 forbids any v1 mechanism to compress it |
| 13 | SHOULD-FIX | `grain` is declared on R-DELTA only; `n` means two different things by grain and R-FLOOR-2's arithmetic depends on it |
| 14 | SHOULD-FIX | Q1's `subbench.toml` fallback re-creates KB-2 exactly, and the version mismatch is live today |
| 15 | WORTH-NOTING | the predictions closed set omits the derived lazy-JIT compile metric |
| 16 | WORTH-NOTING | `subject_or_na` has two "absent" spellings across sections |
| 17 | WORTH-NOTING | `×` / `→` in verdict strings — explicit UTF-8 required for determinism on a stranger's box |
| 18 | WORTH-NOTING | §9.2's own firing counts disagree with the data it claims to render |
| 19 | WORTH-NOTING | the CLI needs no restructuring; the `report` early-dispatch is the pattern to copy |
| 20 | WORTH-NOTING | the runtime budget claim is credible (measured); the growth risk is git weight and reviewer time, not CPU |

---

## 1. BLOCKING — the acceptance test contains a claim the predicates cannot satisfy

§4.2 declares R-DELTA-3 as fires on `delta_verdict` matching
`^now measured \(was: `. §10 Report A item 2 requires it to fire on the
`large-subject-throughput` pair ("the latter pair also carrying `now
measured (was: gave-up)` → R-DELTA-3").

Measured over all 42 committed report TSVs, the distinct verdicts
containing either token are exactly three:

```
selection changed (dfa → vm)
selection changed (vm → dfa)
selection changed (vm → dfa); now measured (was: gave-up)
```

There is **no bare `now measured` verdict anywhere in the corpus.** The
only occurrence is inside the compound, four rows of it, all in Report A.
Under `^now measured`, R-DELTA-3 fires **zero** times on its own
acceptance report and zero times on the corpus.

The cause is in the source the note itself cites: `_cross_pin_info`
(report.py:2520-2535) builds the compound deliberately — "A selection
change EXPLAINS a 'now measured' rather than replacing it". So the
verdict column is a `; `-joined LIST of clauses, not a single token, and
§4.2's four `^`-anchored predicates are written against a shape the
reporter does not emit.

Note in fairness that §4.2's *other* exclusivity claim is CORRECT and
verified: `_cross_pin_info` returns either a `selection changed` verdict
or a `faster/slower` one, never both, so R-DELTA-1 and R-DELTA-2 genuinely
cannot co-fire on one cell (report.py:2533-2540). It is R-DELTA-3's
relationship to R-DELTA-2 that the note gets wrong — they are not
alternatives, they are co-occurring clauses of one string.

**What the panel should require before an implementation lane starts.**
State the verdict column's grammar explicitly — "a `; `-separated list of
clauses; each R-DELTA rule matches its own anchor against each CLAUSE" —
and add a co-firing fixture for the R-DELTA-2 + R-DELTA-3 compound
alongside §8(4)'s mutual-exclusion fixture for R-DELTA-1/2. Without this
the lane's first act is to discover that the acceptance test — which §10
says is written down precisely so a later lane cannot weaken it — cannot
pass, and it will have to weaken it.

## 2. BLOCKING — §2.1 and §4.1 disagree about where the agreement string lives

§2.1, describing "two shapes [that] matter and are easy to get wrong":

> a `record` row carries the RECORD ID in the `testee` column, **the
> agreement string in `gave_up_summary`'s slot**, and the after-sample
> failure in `delta_verdict`'s (report.py:4100-4107)

The cited lines say otherwise. `render_tsv` emits (report.py:4104-4107):

```python
lines.append("\t".join(["record", "", "", "", "", "", rid, "", "", "", "agreement",
                         _agreement_display(...),
                         "", "", "", "", "", ("after: " + after) if after else ""]))
```

Column 11 is `metric` = `"agreement"`; column 12 is `value` = the
agreement string; column 17 (`gave_up_summary`) is **empty**. Confirmed
against Report A: every `record` row reads `metric=agreement`,
`value=n/a (v1.2)`, `gave_up_summary=`.

§4.1's own Inputs line gets it right (`report:record.{testee,value,
delta_verdict}`). So the note states the input format two ways, one of
them wrong, in the section whose entire purpose is "two shapes matter and
are easy to get wrong". A lane reading §2.1 first — the natural order —
writes a rule that reads an empty column and reports `no-matching-rows`
for R-STATUS-9 on every report forever, which looks exactly like a
correct non-firing.

**Require:** §2.1 corrected, and the fixture for R-STATUS-9 built from a
real `record` row rather than by hand, so the column position is pinned
by data rather than by prose.

## 3. BLOCKING — R-STATUS-9's predicate is stated twice, incompatibly, and the choice is not cosmetic

§4.1: R-STATUS-9 fires on "a `record` row whose agreement string starts
`disagree` or **`n/a`**".

§9.2's did-not-fire table for the same report: "R-STATUS-9 |
no-matching-rows (every record reads `agree` or **`n/a (v1.x)`**)".

Measured: across the whole corpus the agreement column takes exactly three
shapes —

```
agree (N of N groups; N of N rows; N unjudged; k=N.N, N/N; N trials)
agree (N of N groups; ... N unjudged (N all-timed-out); ...)
n/a (vN.N)
```

— and **all nine of Report A's records read `n/a (v1.x)`** (they are
schema 1.1/1.2, before the block existed; `_agreement_display`,
report.py:2788-2792). So under §4.1 the rule fires nine times on the
acceptance report and §9.2's specimen output is wrong; under §9.2 the
rule never fires on any pre-1.4 population and §4.1's predicate is wrong.

A third case the predicate covers under neither reading:
`agreement_line` (reduce.py:351-376) can also return
`agree 0/0 groups -- nothing judged (N rows unjudged)` and
`n/a (%d trials)` — the second is a scratch/short-run record, a genuinely
different caveat from "this record predates the rule". `startswith("n/a")`
merges them.

**Require:** a ruling on the predicate (my read: `disagree` should fire;
`n/a (v1.x)` is provenance about the record's AGE, not about its trials,
and belongs with R-STATUS-6's mixed-schema fact; `n/a (N trials)` and
`nothing judged` are each their own thing), and the enumeration of the
four possible strings written into `threshold_src` with the reduce.py
citation, since the interpreter is reading a rendering here too (see
finding 8).

## 4. BLOCKING — the golden and freshness checks are coupled to two things that churn

§8(2) commits `catalogue/golden/<report-basename>.facts.tsv` for three
named reports and requires byte equality. §8(3) re-renders every committed
`reports/*.interpretation.md` "from its recorded inputs (the stamp names
them and their sha256)" and requires byte equality. Both go into
`make check`.

Two inputs make that unstable in a way the note does not address:

**(a) `store/index.tsv` grows.** R-STATUS-2 reads the index for records
the query did NOT include. `store/index.tsv` has been rewritten in 16
commits and stands at 160 rows. The moment a window measures another
`email-specimen@0.1` cell on `budu-ryzen1600` — or any future record with
a non-`measured` status in a covered (subbench, version, machine) — the
facts for the *already-committed, unmodified* Report A change, and
`make check` fails on a commit whose only content is new records.

This is not hypothetical: it is **KB-8, one layer up**. The reporter's own
header count printed `len(paths)` — the whole store's candidate count —
and moved on 42 of 48 reports when the store grew; [B32] fixed it by
making the count query-filtered. The interpreter re-creates the same
coupling deliberately, because R-STATUS-2's whole point (§2.2, and §10
A.1: "This is the claim that requires `store/index.tsv` as an input") is
to look outside the report.

**(b) reports are regenerated on every `REPORTER_VERSION` bump.** The
sidecar stamp carries `report_sha256`. `REPORTER_VERSION` has gone v2 →
v15 between 2026-08-25 and 2026-09-06, and `reports/CLAUDE.md`'s standing
rule is that every committed report is regenerated on a rendering bump.
Every such bump therefore invalidates every committed sidecar's stamp and
every golden file — roughly one bump per working day at the current rate.
§3.3 accepts "a catalogue bump regenerates every sidecar in the same
commit"; it does not consider that a *reporter* bump does the same, nor
that a *record* commit does.

**Require, before a lane starts:** (i) golden runs against a FROZEN index
snapshot committed beside the golden (`catalogue/golden/index@<date>.tsv`),
never against live `store/index.tsv` — the live index stays `interpret`'s
default for a human run; (ii) an explicit statement of who regenerates
sidecars on a reporter bump and whether `check-interpret` is allowed to
fail a records-only commit; (iii) if (i) is rejected, R-STATUS-2 must be
scoped by the report's own `filters:` header (a record excluded because
the query named a roster is not the same fact as a record excluded because
it was not `measured`), which is a rule change, not an implementation
detail.

## 5. BLOCKING — the facts TSV cannot be reassembled into firings

§5 fixes the columns:

```
rule_id  fired  pattern  subject_or_na  regime  form  testee  record_id  slot  value
```

and states "Slots are emitted one per row". §8(5) then requires that
every sidecar line "be reproducible by `render(rule_id, slots)` for some
rule and some slot set present in the facts TSV" — i.e. the check must
group slot rows back into slot SETS.

For most rules the key columns do that (a firing is identified by
pattern/regime/form/testee). For at least four they do not:

- **R-STATUS-12** names TWO patterns (`{pattern_a}`, `{pattern_b}`) as
  slots, and there is ONE `pattern` key column. Two firings on the same
  testee and regime over different pattern pairs are indistinguishable.
  Measured: this rule fires **3×** on Report A (see finding 18), all in
  `large-subject-throughput`, differing only by testee — so today it
  happens to separate, but the shape does not guarantee it.
- **R-STATUS-5** is a header fact with no key columns at all.
- **R-BUCKET-FORM / R-BUCKET-VSBEST / R-RANK-3** are group-scoped: their
  key is (pattern, regime), and their slots include counts computed over
  the group's rows.
- **R-PRED-\*** are keyed by `prediction_id`, which is not a column.

**Require:** add a `firing_seq` (integer, per rule, in declaration/emit
order) column, and a `prediction_id` column or an agreement that
`record_id` doubles for it. Ten minutes of design now; otherwise §8(5) —
the firewall's own test, and the note's most valuable check — is
un-implementable without re-running `interpret` inside the checker, which
would make it a self-consistency test rather than a check of the committed
artifact.

## 6. BLOCKING — R-BUCKET-SPAN reads an input the design does not have

§4.6: fires on "a cross-pin pair whose two pins are **not adjacent in the
pin history**". §10 B.3 makes it a MUST for Report B.

Neither declared input carries a pin history. `store/index.tsv`'s columns
are `path subbench version testee_id machine_id timestamp status rows`;
the report TSV carries testee ids and record ids. The pin ORDER
(288d505 → 334fd10e → d34c9131, abi 16 → 22 → 23) exists in this repo as
prose in `CLAUDE.md`, `testees/pcrec/CLAUDE.md` and the ledgers.

You can *approximate* it — order the pin slugs of one engine by earliest
`timestamp` in `store/index.tsv` — and on Report B that works (all three
pins are in the store). It fails whenever an intervening pin was never
measured on that sub-bench, which is the normal case: `[B22]`'s 263b013
and `[B25]`'s a7e0bdf were each measured on some sets and not others, and
the note's own §10 B.3 example is a `vm-in` arm whose Δ partner skipped
334fd10e *because 334fd10e has no `vm-in` row in that report*. So
"adjacent in the store" and "adjacent in the pin history" are different
predicates, and the rule's stated wording is the second one.

**Require:** either (a) declare the derivation explicitly ("pins of this
engine present in the INDEX, ordered by earliest timestamp; the rule
states store-adjacency and says so in its template"), or (b) make the pin
order catalogue DATA — a `[[pin_order]]` table maintained by hand at each
re-pin, exactly the R-BUCKET-KB precedent the note already accepts ("the
signature is DATA in the catalogue, so adding a newly-filed KB is a MINOR
catalogue bump and no code change"). (b) is more honest and costs one
line per re-pin. Leaving it as written guarantees two reasonable lanes
build two different rules.

## 7. SHOULD-FIX — the header comment is not `; `-delimited in practice

§2.1: "A header comment line, `# k: v; k: v; …`" and a table of the keys
`interpret` reads by name. No parse rule is given, and the obvious one
(`split("; ")` then `split(": ", 1)`) is wrong on committed data:

- `x13_rules` is itself built with `"; ".join(...)` (report.py:4084-4085).
  Three committed reports carry a two-entry value, e.g.
  `x13_rules: v1.1-1.3 X13 (both samples quiet) on 14; v1.4 X13
  (pre-flight + trial agreement) on 2`. A naive split yields a bogus
  key-less fragment and shifts every following key by one.
- `filters` contains `, ` and `=` and, on the `--testee` roster queries
  ([B28] KB-5), up to six `testee=<id>` clauses.
- `worst_other_core_busy` contains `%`, ` / ` and parentheses.

Trivially fixable (`re.split(r"; (?=(?:%s): )" % "|".join(KNOWN_KEYS))`,
or split on `; ` and re-join any fragment that does not match
`^[a-z0-9_]+: `), but the fix must be SPECIFIED, because §8(1) requires
"every declared `inputs` column exists in `render_tsv`'s header … read
from the source, not retyped". The header KEY list is the one part of the
input that cannot be read from `render_tsv`'s `header` list (that is the
data-row header); it is a literal in the f-string block at
report.py:4068-4091. Say how the check reads it — parsing the source, or
running `report --format tsv` on the fixture store and reading the keys
back out. The second is cheaper and is already a `check-report` motion.

## 8. SHOULD-FIX — §7.2's slot-value rules do not cover the note's own templates

§7.2 permits exactly three kinds of slot value: a verbatim cell copy, an
integer count of matched rows, or "a number produced by an arithmetic
written out in full in the catalogue's `arith` field (v1 has exactly two)".
§4.1 separately claims R-STATUS-12 is "the ONE place a rule reads a
formatted string rather than a column".

Against the note's own templates that is at least four violations:

1. **R-RANK-1**'s slots `{config}`, `{old_pin}`, `{new_pin}`,
   `{reference}` come from splitting `testee_id` on
   `^pcrec_(?P<pin>[0-9a-f]+)_(?P<config>.*)$` (§4.3). A regex
   decomposition is neither a copy, a count, nor an arithmetic.
2. **R-STATUS-5**'s `{candidates}` is parsed out of the `source:` header
   value's rendering — `store/index.tsv (14 record(s) matching this
   query)` — as §2.1's own table admits.
3. **R-STATUS-12**'s `{subject}` / `{subject_bytes}` are parsed out of
   `_gave_up_cell_summary`'s rendering (Q8, acknowledged).
4. **R-STATUS-9**'s `{agreement}` is `agreement_line`'s rendering, and if
   the rule ever wants the verdict token it must parse it.

And R-DELTA's clause-splitting (finding 1) makes a fifth.

The `_gave_up_cell_summary` parse is also harder than Q8 implies. Its
output (report.py:1216-1222) is `"; ".join` over per-code clauses of the
form `<code>×<n> (smallest: <id>, <bytes:,> B)`, where `<bytes>` may be
`?`, and where `<code>` for a non-pcrec engine is `reduce.giveup_code`'s
FALLBACK — "the raw diagnostic (truncated to 64 chars)" — which may itself
contain `;`, `,` and parentheses. No committed report exercises the
fallback (the corpus carries only `-2:PCREC_ERR_STEPS`,
`-3:PCREC_ERR_FRAMES`, `-4:PCREC_ERR_WORK`) and no committed report
carries a multi-clause summary, so the first pcre2 give-up ever recorded
is the day the parse breaks silently.

**Require:** a fourth permitted slot kind — "a declared decomposition,
its regex written out in the catalogue's own field" — with the regex
stated per rule, so the firewall's audit surface stays complete; and
Q8's option (b) (the reporter emitting `smallest_giveup_subject` /
`_bytes` as columns) promoted from "recommendation" to a precondition for
R-STATUS-12, since it is the acceptance test's item A.3b and the note
itself says a v1 without it "has implemented half the charter".

## 9. SHOULD-FIX — the row view is easy; it is also the wrong shape, and the `inputs` grammar is unspecified

The panel's question was whether the correspondence mechanism needs
significant plumbing. **The mechanism itself does not.** `tomllib.load` +
`getattr(module, rule_id.lower().replace("-", "_"))` + a set difference
against `inspect.getmembers` gives §8(1)'s two directions in about 20
lines, and a Mapping subclass whose `__getitem__` raises on an undeclared
key is another 10. `schema/check_rules.py` already does the harder version
of this by parsing a markdown table out of a design note; TOML makes it
easier, not harder.

Three real problems sit around it:

**(a) The guarantee is weaker than §3.2 claims.** A raising row view
enforces "the rule did not touch an undeclared column *on the paths this
fixture exercised*". §3.2 words it as "every function's declared `inputs`
are the only columns it touches". With one sabotage + one control per rule
the coverage is two paths. That is fine as a check; it should not be
described as a property.

**(b) A ROW view does not fit at least six of the 31 rules.** R-STATUS-12
joins across patterns; R-RANK-1/R-RANK-2 pair across testees within a
group; R-RANK-3, R-BUCKET-FORM, R-BUCKET-VSBEST are group-scoped and
compute counts over the group's rows; R-FLOOR-2 reads a DIFFERENT
pattern's cell (`_floor_mean_for`'s arithmetic, report.py:2582-2595).
These need a table-shaped view, not a row-shaped one.

**(c) The `inputs` grammar is not stated.** The examples mix three
different things in one string list:

```
"report:rank.delta_verdict"                  # file : section . column
"report:rank.metric=median_ns.value"         # ... with a ROW FILTER embedded
"index:status"                               # a different file, no section
"report:excluded.{pattern,regime_or_na,...}" # §4.1's brace shorthand
```

Two lanes will formalise that four ways.

**Require, and it is small:** a stated grammar —
`<file>:<section>[?<col>=<val>][.<column>|.{<col>,…}]` — and a stated
view contract: one object per rule exposing `rows(section, **eq)` →
`Sequence[Mapping]` where each Mapping raises `UndeclaredColumn` on any
key outside the rule's `inputs`, plus `header(key)` with the same
restriction and `index_rows(**eq)` for the join. Sixty lines, but it is
the one thing §12's "the exact python module layout is not decided" MUST
decide, because it is the contract §8(1) is written against and the only
part of the module layout that two implementations can get differently
while both passing their own tests.

## 10. SHOULD-FIX — the fixture plan mis-describes the precedent, and one of its checks is not implementable

§8(4): "Mirroring `schema/examples/bad/`'s pattern exactly (73 files, each
rejected 'FOR THE RULE ITS NAME CLAIMS')" and "Fixtures are hand-written,
small, and share no source with the rule functions".

What `schema/examples/bad/` actually is: 73 files totalling **1.6 MB**
(~22 KB each — record JSONL is not small), and, per the Makefile's own
`check-schema` comment (item 5), "the GENERATED 1.4 example reproduces
byte for byte from `schema/examples/gen_example_14.py` — **every v1.4
sabotage in bad/ is a one-field mutation of that output**, so the output
must be pinned." The precedent is *generated base + declared mutation*,
not hand-authoring. The naming discipline and `check_rules.py`'s
listing-vs-note correspondence are the parts worth copying.

Two concrete consequences for a hand-written plan:

**(a) A realistic fixture is not small.** A minimal R-RANK-1 fixture needs
a reference arm plus two pins of one config in one group; `render_tsv`
emits six metric rows per (group, testee, form) (report.py:4146-4153), so
that is 18 rank rows of 18 tab-separated columns, plus a 19-key header
comment, plus `record` rows for the join. Times 31 rules times two
(sabotage + control), plus the co-firing fixtures, plus `index.tsv` and
`expect.txt` per directory: ~190 files a human types by hand, each of
which must stay consistent with `render_tsv`'s column order forever.

**(b) A hand-typed fixture is not a report.** `ratio_vs_baseline` is
derived by the reporter from `median_ns` and the reference row
(report.py:4138); `pass_rate`, `n`, `fact` likewise. A hand-typed fixture
will carry combinations `render_tsv` cannot produce, so the rule is proven
to fire on a shape that does not exist. That is the opposite of a control.

**(c) "The minimum number of bytes" is not a predicate.** §8(4): "the
check asserts … that the control differs from the sabotage in the
minimum number of bytes". Minimum over what? There is no way to compute
"the minimal mutation that flips this rule" without solving for the rule.
As written the check cannot be implemented and will be silently dropped or
turned into something else by the lane.

**Propose instead** (and this is a small change that removes most of the
lane's day-one cost): `catalogue/fixtures/gen.py`, run with `--check` in
`check-interpret` exactly as `gen_example_14.py --check` runs in
`check-schema`. Each fixture directory carries a `source.toml` naming (i)
a committed report, (ii) a row selector (the group / testees to project),
and (iii) for the sabotage, ONE declared field mutation. `gen.py`
projects a real, reporter-produced slice and applies the mutation; the
files on disk are still committed and diffable, so the "shares no source
with the rule functions" discipline holds (the generator shares source
with `report.py`'s OUTPUT, not with `interpret.py`); and "minimum number
of bytes" becomes the definable "exactly one declared field differs".

## 11. SHOULD-FIX — R-STATUS-3's template is unsound on rows that exist today

Template: `"… is EXCLUDED from ranking: pass-rate {pass_rate}, {n_wrong}
wrong answer(s), {n_gave_up} give-up trial(s){give_up_clause}."`

Report A's thirteen excluded rows include:

```
factored | large-subject-throughput | plain | libpcre2_10.46_jit-caps-simdna | 0.6667 | 0 | 0 | 0
```

`n_gave_up = 0`, `n_wrong = 0`, `gave_up_summary = "0"`. The template
renders "pass-rate 0.6667, 0 wrong answer(s), 0 give-up trial(s)" — a
sentence that names no cause, on a row whose cause the TSV does not carry.
`render_tsv` routes three distinct conditions into the `excluded`
section (report.py:4123-4124): `r.expectation_failing`, and separately
`not n_timed` — and `expectation_failing` itself covers wrong answers,
give-ups, crashes and timed-out subjects, of which only the first two have
count columns.

§10 A.3 makes "all thirteen excluded cells" a MUST, so this row is in the
acceptance set.

**Require:** either the template says what the columns support ("excluded
from ranking: pass-rate {pass_rate}; {n_wrong} wrong, {n_gave_up}
gave-up; the TSV does not carry the cause of the remaining failures") or
the reporter gains an exclusion-cause column. The second is the better
fix and is one line in `_set_cell_failure_reason` (report.py:2251-2264),
which already computes exactly this string for R8's `now measured (was:
…)` verdict and throws it away for the excluded row.

## 12. SHOULD-FIX — the measured output volume is ~25× the specimen, and v1 has no mechanism to compress it

§9.2 presents "a specification of output, not an example of style" — about
15 bullets. Measured firing counts for catalogue v1 as specified, on the
three acceptance reports:

| rule | Report A (email repin) | Report B (bounded@0.3) | Report C (syntax@0.1) |
|---|---:|---:|---:|
| R-DELTA-1 | 3 | **202** | 0 |
| R-DELTA-2 | 6 | 1 | 0 |
| R-RANK-1 | 0 | 7 | 0 |
| R-BUCKET-VSBEST | 4 | **129** | 0 |
| R-FLOOR-1 | 2 | **81** | **190** |
| R-FLOOR-3 | 0 | 1 | 0 |
| R-STATUS-3 | 13 | 0 | 23 |
| R-STATUS-4 (distinct pattern×testee) | 0 | 2 | **60** |
| R-STATUS-9 (if `n/a` fires, finding 3) | 9 | 0 | 0 |
| **rough total** | **~40** | **~420** | **~275** |

Report B's 202 R-DELTA-1 firings include **95 at ×1.05 or below** (the
verdict is "beyond spread" because stddev was small, not because the cell
moved). The design is explicit that this is intended — §4.2's whole point
is that the interpreter must never disagree with the reporter about
whether something moved, and I agree with that decision. But §1.1 also
forbids per-set bands and §1.1's third bullet forbids ranking by
interest, so **nothing in v1 can compress 420 bullets**, and the note
never states what the output actually looks like at that size.

Two costs the lane will hit on day one: the golden facts TSV for Report B
is ~2,500 rows at one-slot-per-row, committed and diffed on every
catalogue change; and Q5's "back-filling 42 sidecars is cheap to generate
and expensive to review" understates the per-file review cost by an order
of magnitude.

**Require, before a lane starts:** a stated aggregation rule for the
high-count rules — the obvious one being that a rule may declare
`aggregate = "group"` and render ONE firing carrying a count plus the row
list (R-FLOOR-1 as "190 compile rows read `timer-floor`; the 26 that do
not are: …"; R-BUCKET-VSBEST once per report with its group list), which
is a rendering rule and not an opinion — and §9.2 re-rendered against
Report B rather than Report A, so the specification of output is a
specification of the WORST case rather than the friendliest one.

## 13. SHOULD-FIX — `grain` is declared on one class, and `n` means two things

§3.2's rule block carries `grain = ["set"]`; §4.2 states it for R-DELTA
and says a subject-grain TSV makes all four report `did-not-fire: grain`.
No other class declares it.

It matters for at least two rules. `_n_and_pass_rate` (report.py:3196-3200)
returns `n_subjects` at set grain and `n_trials` at subject grain into the
same `n` column. R-FLOOR-2's declared arithmetic is `median_ns / n`
"per_subject_mean" — correct at set grain, meaningless at subject grain,
where it would divide a per-call median by a trial count and still produce
a number. R-RANK-1/2 depend on `delta_verdict`, which `render_tsv` only
populates at set grain (report.py:4143-4145), so they are set-only too but
say so nowhere.

**Require:** `grain` mandatory on every `[[rule]]`, checked at load by
§8(1), and R-FLOOR-2 / R-RANK-\* declared `["set"]`.

## 14. SHOULD-FIX — Q1's fallback re-creates KB-2, and the version skew is live

§4.4: "v1 identifies it by the sub-bench's `subbench.toml` — *the one
place `interpret` reads outside its two inputs*". Q1 offers the
`floor_pattern:` header key as the alternative and recommends it; the note
nonetheless specifies the `subbench.toml` read as what v1 does.

This is KB-2 exactly, one layer up. The reporter's [B14] R3 first cut read
`bench/<dir>/expectations.tsv` through `pcrecbench.subbench` and was
corrected (KB-2, manager steer 2026-08-25) because "a record measured on
another box, or against a later sub-bench version, has no sidecar checkout
to read beside it, so a reporter that reaches into `bench/` is answering
from the WRONG machine's sub-bench tree". `report.py` "no longer imports
`pcrecbench.subbench` at all".

The skew is not theoretical here. Acceptance Report A is
`email-specimen@0.1`; `bench/email/` is at `@0.2` today. Report B is
`bounded@0.3`. An interpreter reading today's `bench/<dir>/subbench.toml`
to interpret an older version's report is reading the wrong file, and
because `role` defaults to `member` it will silently find no floor and
report `no-matching-rows` — the same silent-wrong-answer shape KB-2 had.

Confirming that the TSV really carries no signal: in Report C the `floor`
pattern is emitted as an **ordinary rank row at rank 4** (median
800.098671 ns, n 42) — [B14] R9's "retitled a control rather than ranked"
applies to the markdown render only.

**Require:** Q1's own recommendation as a PRECONDITION. The reporter emits
`floor_pattern: <id|none>` in the header comment (one line in the block at
report.py:4068-4091, a `REPORTER_VERSION` bump, every report regenerated —
a motion this project has executed thirteen times). Then `interpret` has
exactly two inputs, as §2.4 claims it does, and R-FLOOR-2 works on an
archived report from any sub-bench version.

## 15. WORTH-NOTING — the predictions closed set omits a metric the reporter emits

§6.3's `quantity` closed set includes `compile:median_total_ns`.
`render_tsv` emits the compile metric as EITHER `median_total_ns` OR
`derived_first_match_row_minus_steady_state_ns` (report.py:4177), the
latter for a `lazy-jit` cost class. No committed report exercises it
(measured: the corpus's compile metrics are `median_total_ns`,
`artifact_bytes`, `jitter`, `emit_bytes`, `emit_code_bytes`,
`warned_emit_bytes`), but the code path exists, so a prediction about a
lazy-JIT compile cost is inexpressible and would fail load as "a quantity
outside the set". Add the token, or declare `compile:median_total_ns` to
mean "whichever compile-cost metric the row carries" and say so.

## 16. WORTH-NOTING — two spellings of "absent" in `subject_or_na`

Measured across the corpus: `rank`, `excluded` and `did_not_compile` rows
carry the literal `(set)` at set grain (report.py:4115); `record`,
`compile` and `compile_stamp` rows carry the empty string. A rule keying
on emptiness to mean "not subject-scoped" is wrong for half the sections.
Worth one sentence in §2.1 beside the two shapes it already flags.

## 17. WORTH-NOTING — encoding, for the stranger's-box posture

`delta_verdict` carries `×` (U+00D7) and `→` (U+2192); `_gave_up_cell_summary`
carries `×`. On this box `LC_ALL=C python3` still reports
`getpreferredencoding` = utf-8 and a default `open()` reads a report fine,
so nothing breaks here. `report.py`'s `main()` sets `LC_ALL=C` and the
Makefile sets it for `check-harness`; on a box where that yields an ASCII
default encoding, `interpret` would raise on read and the golden compare
would be non-reproducible. One line: every `open()` in `interpret.py`
passes `encoding="utf-8"`, and every write too. Cheap insurance for D2's
"a stranger's `make` must work".

## 18. WORTH-NOTING — §9.2's own counts disagree with the data

§9.2 renders "## R-STATUS-12 — one subject, two give-up codes across two
spellings (**1 firing**)". Measured on Report A, the rule as specified
(one subject, one testee, one regime, two patterns, different codes)
fires **three** times: `pcrec_692c2e8_vm-caps-simdna`,
`pcrec_692c2e8_vm-in-caps-simdna` and `pcrec_8da6120_vm-caps-simdna` each
carry `-2:PCREC_ERR_STEPS` on `factored` and `-4:PCREC_ERR_WORK` on
`orig`, all in `large-subject-throughput`, all on subject
`t-c-long-atom-run`.

Small on its own, but §9.2 is labelled "a specification of output" and
§8(2)/(3) make it byte-checkable, so a lane building the first golden
file from it will produce a file that disagrees with the tool and will
have to guess which is authoritative. Either regenerate §9.2 from a
running tool once one exists (and mark it provisional until then), or
correct the counts now.

## 19. WORTH-NOTING — the CLI accommodates `interpret` with no restructuring

`pcrecbench/__main__.py:509-513`:

```python
def main(argv=None):
    argv = sys.argv[1:] if argv is None else list(argv)
    if argv and argv[0] == "report":
        from pcrecbench import report
        return report.main(argv[1:])
    args = build_parser().parse_args(argv)
    return args.func(args)
```

`report` is early-dispatched before argparse "so the reporter owns its own
flags", with a `cmd_report` stub (`__main__.py:313-317`, marked "Never
reached") and a `rep` subparser existing only so `--help` lists it.
`interpret` copies that exactly: one branch, one stub, one subparser, plus
its line in the module docstring's command table. Nothing in §5's flag set
conflicts. `check-interpret` slots into `check: check-schema check-harness
check-report` in the Makefile the way the note says. No finding here — the
panel's question 7 answers cleanly in the design's favour.

## 20. WORTH-NOTING — the runtime claim is credible; the growth risk is elsewhere

Measured: parsing all 42 committed report TSVs (135,891 data rows,
`csv.reader`, no rules) takes **0.25 s**. The largest single file is the
syntax first-sample at 9,090 rank + 3,906 compile rows. Adding 31 rules
over that, three golden compares and ~190 tiny fixtures will not approach
`check-harness`'s ~20 minutes; §8's "seconds, not minutes" is right.

The unbounded thing is not CPU. It is (a) the golden corpus's git weight
and review cost (finding 12: ~2,500 facts rows for Report B alone, moving
on every catalogue MINOR that touches a template), and (b) §8(3)'s
re-render of every committed sidecar, which under Q5's recommendation
starts at three and grows by one per report from the landing forward —
one per window, so roughly one per working day at the current cadence.
Neither threatens the time budget; both threaten the *review* budget,
which is the resource `make check` is actually protecting. Worth a stated
cap or a stated rotation policy in §8.

---

## Verdict

**An implementation lane could not start today from this note alone, and
the gap is small and specific rather than structural.** The architecture
is sound and unusually well-grounded: the decision to read the reporter's
own verdict strings rather than recompute thresholds (§4.2) is right and
is what makes the tool trustworthy; the correspondence check (§8(1)) has a
working precedent in `schema/check_rules.py`; the CLI needs no
restructuring; the runtime budget is real; and the note's arithmetic about
the store (nine `inconclusive-load` + one `inconclusive-spread`; the three
Report A record ids; the R-RANK-1 census's 7 firings on Report B; the
R-FLOOR-2 worked example's 246.458/42 vs 800.099/42) reproduced exactly
against the committed data every time I checked it, which is more than
most design notes survive. What is missing is not judgment, it is
*contract*: the note specifies rules richly and specifies the machinery
they run on thinly, so the six BLOCKING items are all places where two
competent lanes would build two different things, or where the acceptance
test as written cannot be passed by any implementation (findings 1 and 3
in particular — R-DELTA-3 fires zero times in the entire committed corpus
under its own predicate, and R-STATUS-9's predicate is stated two
incompatible ways within the same note). I would ask for one revision pass
delivering: the verdict-column and header-comment grammars, the corrected
§2.1 record-row shape, a ruling on R-STATUS-9, the `inputs` grammar and
view contract, a `firing_seq` column, the pin-order input for
R-BUCKET-SPAN, a frozen-index rule for the golden, the `floor_pattern:`
header key as a precondition, an aggregation rule for the high-count
rules, and the fixture plan re-cast as generated-base-plus-declared-
mutation. That is a day of design work on a note that already did the hard
part; done first, it converts what would otherwise be a lane spending its
first week rediscovering these against real files into a lane that can
write code on day one.
