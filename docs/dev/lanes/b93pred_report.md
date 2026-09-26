# Lane `b93pred` — delivery report

[B93] per `docs/dev/plan.md`'s `[B93]` row — Frank's ruling on
`docs/dev/lanes/b72smalls_report.md` §5 (candidate (b)): apply
`b42predhyg`'s reasoning to `docs/dev/predictions/capability-0.1-first.tsv`
P2.a/P2.b as a SANCTIONED SYNTAX-ONLY CORRECTION, state the standing rule
in `docs/dev/predictions/CLAUDE.md`, retire `[B72smalls]`'s Q6 (i)
stopgap, and regenerate the four blocked sidecars.

Environment note: this session runs in a harness-managed isolated
worktree (`worktree-agent-a1f679211aceefebd`), not a hand-created
`worktrees/b93pred` — the manager should treat it the same as any other
lane branch at merge time.

## Charter-vs-committed checklist

1. **Apply b42predhyg's fix to P2.a/P2.b, dated, naming the defect and
   the ruling, no predicted value changed.** BUILT, but WIDER than the
   single-key removal the brief names — see "What actually needed
   fixing" below for why, and item 2 for the proof. Both clauses'
   `regime_or_na=n/a` selector clause is dropped (the literal Q6 (i)
   fix) AND their `ratio_to(...)` reducer argument is corrected to name
   `pattern=`/`testee=` explicitly (a companion fix this task's own
   deliverable — a working, evaluable clause, not a crash — turned out
   to require). `docs/dev/predictions/capability-0.1-first.tsv` diff:
   only the two P2 rows change; original bytes are in git history at
   this commit's parent.
2. **PROVE no predicted value changed; show it selects the same rows on
   the committed reports.** DONE, with the honest complication named:
   see below.
3. **State the rule in `docs/dev/predictions/CLAUDE.md`.** BUILT — a new
   "Revising an already-scored file" section, dated, four numbered
   conditions, pointing at this report.
4. **Retire the stopgap; Q6 (i) must now pass on every predictions file
   with no exception.** BUILT for Q6 (i) — confirmed by `make
   check-interpret` section 1 (21/21, no `_KNOWN_HISTORICAL_LOAD_
   DEFECTS` table left in `catalogue/check_interpret.py`, no per-file
   carve-out in the load loop). **UPDATE, 2026-09-26: also true of Q6
   (ii)/section 3 now** — the manager ruled on the P4 finding below the
   same day; see "Follow-up (2026-09-26)". ALL THREE named exceptions
   this file's history ever carried are gone.
5. **Regenerate the four blocked sidecars, 0 failures.** **DONE,
   2026-09-26** (was NOT DONE at first delivery — see "Follow-up
   (2026-09-26)" below for the full P4 fix, the hand-verification table,
   and the fact-diff review).

## What actually needed fixing (found empirically, not assumed)

The brief's own framing ("apply b42predhyg's fix ... as a syntax-only
correction ... show it selects the same rows") describes the SHAPE
`interpret_subject_grain_v1.md` §4 P2 recommends: "drop the
`regime_or_na=n/a` clause entirely." I built exactly that first, in a
scratch predictions TSV in the session scratchpad (never committed),
and ran it against the four real committed reports this file is stamped
against — the same empirical-verification discipline `b42predhyg` used
for P5, and the standard `docs/dev/predictions/CLAUDE.md`'s new section
now writes down as a REQUIREMENT (item 3), not merely a nicety.

**Dropping only `regime_or_na=n/a` does not "select the same rows" —
it selects rows for the FIRST time ever** (Cause B guaranteed a
permanent, zero-row match; the clause has never once been evaluated in
this file's history). On the two reports that carry
`wild-waf-crs-942360-concat-sqli`'s and
`wild-datetime-datefinder-alternation`'s jit/interp compile rows, the
selector now matches three `compile`-section rows per side
(`median_total_ns`, `jitter`, `artifact_bytes`). That is the intended,
correct consequence of Cause B's fix, not a defect in it — but it also
means "no predicted value changed" cannot be read as "the same rows
match before and after"; it has to be read as "the same `quantity`/
`op`/`hi`/`unit`/`note` are being asked about a population the clause
could not previously reach at all."

**The naive fix then CRASHES `interpret()` outright**, uncaught, exit
code 2, for EVERY report scored against this file:

    interpret: .../capability-0.1-first.tsv:2 (P2.a): selector clause
    'libpcre2_*_interp-*' is not <key>=<glob>

`_reduce`'s `ratio_to` reducer (`pcrecbench/interpret.py:2549`) parses
its OWN argument as a `<key>=<glob>` selector string
(`interpreter_v1.md` line ~1872's own documented syntax, `ratio_to(pattern=
cls-upto-1024;regime=match-compliance;form=plain;testee=<same>)`).
P2.a/P2.b's argument, `libpcre2_*_interp-*`, is BARE — a second,
pre-existing authoring defect in the same two clauses, masked from day
one by Cause B (the selector never matched anything, so `_reduce` was
never reached). This is NOT a hypothetical: I reproduced it directly,
with the real predictions file (patched only by dropping
`regime_or_na=n/a`) against all four committed reports; see the session
scratchpad transcript quoted in `docs/dev/predictions/CLAUDE.md`'s new
addendum for the exact command and output shape.

**Prefixing the argument with only `testee=` avoids the crash but
produces a WRONG number.** `ratio_to`'s own join rule
(`interpreter_v1.md` §"ratio_to", `_reduce` lines ~2540-2560) joins the
two populations on every key column BOTH selectors state with the SAME
literal glob text. P2.a's outer selector has `pattern=wild-waf-crs-
942360-concat-sqli` and `testee=libpcre2_*_jit-*`; an argument of only
`testee=libpcre2_*_interp-*` shares NEITHER key's literal text with the
outer selector (`testee` differs on purpose — jit vs interp — and
`pattern` is simply absent from the argument), so `join = []` and the
"baseline" is computed as the MEDIAN `median_total_ns` over EVERY
pattern the interp testee ever compiled, pooled — not the one pattern
the prediction is actually about. Measured: **116.674**, not the
ledger's own hand-derived **5.29** (`docs/dev/ledgers/2026-09-17-
capability-0.1-first-a770139e.md` §3: 386,192 ÷ 73,020 ns = 5.29). A
confident-looking but SILENTLY WRONG confirm is worse than a crash —
exactly the class of defect `docs/design/predicate_audit_v1.md` and
this project's whole "context around the numbers" discipline exist to
catch, and I checked for it rather than shipping the first number that
came back.

**The fix that actually reproduces the ledger's own hand-derived
number**: repeat `pattern=<the same pattern text>` in the reducer
argument alongside `testee=`, so the join scopes the comparison to the
SAME pattern (which is what P2's own note plainly means: "pcre2-jit
compiles **this pattern** measurably slower than pcre2-interp").
Verified against every one of the four committed reports:

| report | P2.a (wild-waf-crs-942360-concat-sqli) | P2.b (wild-datetime-datefinder-alternation) |
|---|---|---|
| 2026-09-17-...-first-a770139e | **confirmed**, ratio 5.289 | **confirmed**, ratio 6.976 |
| 2026-09-18-...-after-cf0962e3 | **confirmed**, ratio 5.289 | **confirmed**, ratio 6.976 |
| 2026-09-18-...-ext-first-cf0962e3 | not evaluable (pattern/testee absent from this roster) | not evaluable (same) |
| 2026-09-19-...-ext-second-cf0962e3 | not evaluable (same) | not evaluable (same) |

5.289 matches the ledger's own hand-derivation (386,192 ÷ 73,020 =
5.29) to three decimals — an independent cross-check, not a coincidence
of my arithmetic. 6.976 (1,970,240 ÷ 282,442) is a NEW number: the
2026-09-17 ledger's own P2 row talks about `wild-datetime-datefinder-
alternation` only in terms of a pcrec compile REFUSAL (a different,
unrelated finding, not this clause's own jit-vs-interp claim) and never
actually states a ratio for it — so this is the first time P2.b's own
claim has been checked against real numbers by anyone, machine or
human, and it holds.

### Every OTHER field of both clauses, before vs. after (item 2's proof)

| field | P2.a before | P2.a after | changed? |
|---|---|---|---|
| `prediction_id`/`clause` | P2/.a | P2/.a | no |
| `source`/`source_ref` | NOTES.md/P2 | NOTES.md/P2 | no |
| `stated_utc` | 2026-09-16T00:00:00Z | 2026-09-16T00:00:00Z | no |
| `subbench`/`version` | capability/0.1 | capability/0.1 | no |
| `selector` pattern= | wild-waf-crs-942360-concat-sqli | (same) | no |
| `selector` testee= | libpcre2_\*_jit-\* | (same) | no |
| `selector` regime_or_na= | n/a | (absent) | **REMOVED — the Q6 (i) fix** |
| `quantity` | compile:median_total_ns | (same) | no |
| `reducer` HEAD | ratio_to | ratio_to | no |
| `reducer` arg | libpcre2_\*_interp-\* | pattern=wild-waf-crs-942360-concat-sqli;testee=libpcre2_\*_interp-\* | **CORRECTED — the companion fix** |
| `op` | gt | gt | no |
| `lo`/`hi`/`unit` | (empty)/1/x | (empty)/1/x | no |
| `note` | (verbatim) | (verbatim) | no |

(P2.b's table is identical in shape, substituting the pattern name.)
Every field that states WHAT is predicted — the quantity measured, the
comparator, the threshold, the unit, the prose claim — is byte-identical.
Only the TEXT that decides which rows the machine can reach changed: one
clause dropped (Cause B) and one reducer argument's `<key>=<glob>`
syntax completed (its own pre-existing, masked defect). No number in
`lo`/`hi` moved; the note's own English claim is what got verified for
the first time, and it held.

## A second, separate finding: P4.a/P4.b block the sidecar regen too

Retiring Q6 (i)'s stopgap and fixing P2 lets `interpret()` proceed past
`load_predictions` for real, for the first time, against this file.
Doing so surfaces `check_testee_globs` (Q6 (ii), the SAME
`[B72smalls]` lane's OTHER load-time check), which raises on
P4.a/P4.b's OWN already-diagnosed Cause C (`testee=pcrec_*-auto-*` — a
hyphen where every real testee_id has an underscore before `auto`;
`interpret_subject_grain_v1.md` §1.2/§4, `docs/dev/lanes/
b42subgrain_report.md`). This defect was ALSO always there; it was
simply unreachable because Cause B's crash fired first, on an earlier
row (`load_predictions` and `check_testee_globs` both raise on the
FIRST bad row they see, and P2 sorts before P4).

I did not fix it, for a reason concrete enough to name precisely: this
lane's own new standing rule (item 3 of "Revising an already-scored
file") requires a syntax-only correction to be verified EMPIRICALLY
against a known-good number, the way P2's companion fix was checked
against the ledger's 5.29. No ledger or design note states a
hand-derived number for P4.a/P4.b, and — worse — repairing the glob
alone is not enough to unblock anything: P4.a's `ratio_to(logparse-
atomic-removed)` has the SAME bare-argument defect P2 had, and P4.b's
`ratio_to_median_over(logparse-atomic-removed)` is a different kind of
wrong entirely — `ratio_to_median_over`'s argument must be a KEY COLUMN
NAME (`pattern`, `testee`, ...), never a pattern VALUE, so P4.b appears
to have been authored for the WRONG REDUCER altogether (its own note,
"the atomic form's search cost ... is lower than the non-atomic
control's", describes a cross-PATTERN comparison — `ratio_to`'s job,
not `ratio_to_median_over`'s). Choosing the right reducer and selector
shape for P4 is a judgment call about what its author meant, not a
mechanical syntax repair — exactly the kind of edit this task's own
narrow charter (and the standing rule it establishes) does not license
a lane to make unilaterally.

**Filed, not fixed, on `b72smalls`'s own precedent**: `catalogue/
check_interpret.py` carries a new, narrowly-named, dated stopgap
(`_SIDECARS_BLOCKED_ON_CAPABILITY_FIRST_P4_CAUSE_C`) that skips exactly
these four sidecars in section 3, reported as a SEPARATE "BLOCKED ON A
RULING" count, never folded into "fresh" — the same shape `[B72smalls]`
used for Cause B, for the same reason (a real, already-diagnosed,
out-of-scope defect that would otherwise either crash the whole check
or need an unauthorized invention to paper over). `docs/dev/predictions/
CLAUDE.md`'s and `catalogue/CLAUDE.md`'s file entries both name this
explicitly. **The four sidecars remain UN-regenerated**; regenerating
them is OWED, blocked on a ruling for P4 (candidates: (a) charter a
follow-up lane to work out P4's correct reducer/selector shape and
verify it the way P2 was verified here; (b) rule that P4.a/P4.b should
simply be RETIRED from this file as un-recoverable authoring mistakes,
carried forward only in prose the way syntax's own inexpressible
clauses are; (c) some other resolution this lane did not consider).

## Follow-up (2026-09-26) — the manager's P4 ruling, applied

The manager sent a ruling on the P4 finding above while this lane was
still open: **within Frank's option (b), because the notes state the
meaning unambiguously.** P4.a is the atomic pattern's `artifact_bytes`
÷ the non-atomic control's (`logparse-atomic-removed`), same testee;
P4.b is the atomic pattern's `median_ns` ÷ the control's on the same
subject (`lp-atomic-nonmatch`), same regime, same testee — both a
cross-pattern `ratio_to` comparison, exactly P2's own shape. The
instruction: fix the glob (`pcrec_*_auto-*`, checked against the real
index), give P4.a `ratio_to(pattern=logparse-atomic-removed;testee=...)`
in P2's corrected shape, give P4.b `ratio_to` (not
`ratio_to_median_over`) with the same argument shape plus the
subject/regime keys it needs so the denominator is the SAME subject/
regime/testee cell, keep op/lo/hi/unit/note byte-identical, hand-derive
the raw cells from the report TSV (or the records) for every committed
report and show interpret's evaluated value equals it to the printed
digits, and STOP rather than adjust if they ever disagree.

**Applied exactly as instructed, verified, no disagreement found.**
`docs/dev/predictions/capability-0.1-first.tsv`'s P4.a/P4.b:

    P4.a selector:  pattern=logparse-atomic;testee=pcrec_*_auto-*
    P4.a reducer:   ratio_to(pattern=logparse-atomic-removed;testee=pcrec_*_auto-*)
    P4.b selector:  pattern=logparse-atomic;subject_or_na=lp-atomic-nonmatch;
                    regime_or_na=short-subject-search;testee=pcrec_*_auto-*
    P4.b reducer:   ratio_to(pattern=logparse-atomic-removed;subject_or_na=
                    lp-atomic-nonmatch;regime_or_na=short-subject-search;
                    testee=pcrec_*_auto-*)

`quantity`/`op`/`lo`/`hi`/`unit`/`note` unchanged on both clauses (only
the testee glob's hyphen and both reducers' argument text moved).

**P4.a — hand-derived vs. interpreted, every committed report:**

| report | raw cells (`compile:artifact_bytes`, atomic / removed) | hand ratio (worst) | `interpret`'s value | match? |
|---|---|---|---|---|
| 2026-09-17-...-first-a770139e | auto-caps 82,840/82,840 & 82,800/82,800 (=1.000); auto-nocaps 82,840/74,496 (=1.112006) & 82,800/74,448 (=**1.112186**) | 1.112 (worst of 4) | `refuted`, worst 1.112 over 4 value(s) | **yes** |
| 2026-09-18-...-after-cf0962e3 | SAME four byte pairs, on BOTH a770139e and cf0962e3 (pcrec's own artifact is byte-identical across the two pins for this pattern — confirmed by direct read of the report's own compile rows) | 1.112 (worst of 8) | `refuted`, worst 1.112 over 8 value(s) | **yes** |
| 2026-09-18-...-ext-first-cf0962e3 | no `pcrec_*` compile row at all (roster is the 5-engine ext sample) | n/a | `not evaluable`: no row matches the selector | **yes** (a real absence, not a defect — verified by grep of the report's own testee column) |
| 2026-09-19-...-ext-second-cf0962e3 | same as above | n/a | `not evaluable`: same reason | **yes** |

**P4.b — hand-derived from the underlying JSONL records (the set-grain
report TSV cannot carry a real subject id at all, see below), cross-
checked against the committed `.subject-grain.tsv` for the one report
that has one and reproduces to six decimals:**

| testee (pin a770139e) | atomic median_ns (5 trials) | removed median_ns (5 trials) | ratio |
|---|---|---|---|
| auto-caps | 14.802902 | 12.431209 | 1.191 |
| auto-nocaps | 13.516966 | 8.571827 | 1.577 |

(cf0962e3's own rows, read from the same subject-grain TSV: auto-caps
13.736282/12.464492 = 1.102; auto-nocaps 13.359327/8.579463 = 1.557 —
same direction, same order of magnitude, a different pin's own
measurement.) **`interpret` itself reports `not evaluable` for P4.b on
every one of the four reports** — not a disagreement with the hand
derivation (there is no crash and no wrong number to disagree about),
but a THIRD, separate structural fact found while verifying this exact
clause: P4.b's own selector names `subject_or_na=lp-atomic-nonmatch`
and `regime_or_na=short-subject-search` (unchanged — this was already
in the file before either fix), and every one of these four reports is
rendered at `grain=set`, where `render_tsv` writes the literal string
`(set)` into every rank row's `subject_or_na`, never a real subject id
(Cause A, `interpret_subject_grain_v1.md` §1.2/§4 — the identical gap
P3/P6/P7/P10 already carry). Reaching a real subject id needs an
explicit `grain=subject` key on the selector, routing the clause to the
`--subject-grain` sibling file (two of the four reports have one
committed) — outside the manager's own three-part description of the
fix, so **not added here**, per "STOP and report; don't adjust until
they match" and per "Revising an already-scored file"'s own item 3 (a
further change needs its own verification and its own go-ahead). Had it
been reachable, both testees' ratios are > 1 on every pin (1.10-1.58),
which would **REFUTE** the clause's own claim ("the atomic form's search
cost … is LOWER", i.e. predicting < 1) rather than confirm it — stated
here for the record, not acted on.

**The four sidecars are regenerated for real** (`python3 -m pcrecbench
interpret <report> --index store/index.tsv --predictions docs/dev/
predictions/capability-0.1-first.tsv [--subject-grain <sibling>]
--render --out <sidecar>`, the exact invocation `scripts/
regen_sidecars.py` uses per file, run directly rather than through that
script since only these four — not all 35 committed sidecars, a
memory-heavy whole-store operation — needed it); each one's determinism
re-checked (a second run to stdout, byte-compared, all four identical).
`catalogue/check_interpret.py`'s Cause-C stopgap
(`_SIDECARS_BLOCKED_ON_CAPABILITY_FIRST_P4_CAUSE_C`) and its module
comment are retired; section 3 is the plain unconditional loop again.

**Fact-diff review, all four** (`git diff -- reports/*.interpretation.md`):
- `2026-09-17-...-first-a770139e` and `2026-09-18-...-after-cf0962e3`:
  P2 moves `not evaluable` → `confirmed` (R-PRED-1, exactly the [B93]
  first-delivery numbers, 5.289/6.976); P4 moves `not evaluable` →
  `partial` (R-PRED-4, firing in this project for the FIRST time: 0
  confirmed, 1 refuted, 1 not-evaluable, "P4.a refuted; P4.b
  not-evaluable" — matching the roll-up rule exactly, `interpreter_v1.md`
  §4.6's "any mix → partial"); the `catalogue: 3.2 → 3.8` stamp pulls in
  two unrelated, already-landed rules (R-STATUS-15, R-DELTA-5) into the
  "did not fire" table — explained by catalogue growth since these four
  sidecars' last regeneration, not by this fix.
- `2026-09-18-...-ext-first-cf0962e3` and `2026-09-19-...-ext-second-
  cf0962e3`: the R-PRED section is **UNCHANGED** — only the stamp lines
  (index/predictions sha256, `catalogue: 3.2 → 3.8`) and the SAME two
  catalogue-growth rows move. This independently confirms neither P2
  nor P4's fix touches these two reports at all (their roster carries
  no pcrec testee, exactly as expected), and that the four-sidecar
  regeneration this task asked for was blocked ONLY by the two load-time
  checks, never by anything about these reports' own content.

## Follow-up 2 (2026-09-26) — the manager's `grain=subject` ruling, applied

The manager sent a second ruling on the residual P4.b finding above,
the SAME day: **add `grain=subject` to P4.b — same repair class, since
the note names one subject (`lp-atomic-nonmatch`) and a subject key can
only be reached through that grain, so the clause's meaning was never
set-grain.** Instruction: keep `op`/`lo`/`hi`/`unit`/`note`
byte-identical, add a line to the header correction note, show
`interpret`'s P4.b value equals the hand-derived 1.10-1.58 per report
to the printed digits (every report whose sidecar carries
`--subject-grain`; say which ones can't and why), regenerate the
affected sidecars, review the fact diffs, re-run the three checks, and
— "if P4.b now reads REFUTED, that is the truth and stands."

**Applied**: P4.b's selector gains one clause, `;grain=subject` (no
other text moved — `docs/dev/predictions/capability-0.1-first.tsv`
diff is a single `;grain=subject` insertion at the end of P4.b's
selector column, nothing else). `docs/dev/predictions/CLAUDE.md`'s
header addendum line and the file's own P4 entry are both updated,
dated, naming this second ruling explicitly.

**Interpreted vs. hand-derived, every committed report, to the printed
digit — the table the ruling asked for:**

| report | has `--subject-grain`? | `interpret`'s P4.b | hand-derived | match |
|---|---|---|---|---|
| 2026-09-17-...-first-a770139e | **no** (`subject_grain: (none)`) | not evaluable: "the clause selects grain=subject but no --subject-grain input was supplied" | n/a (no subject-grain input to derive against) | n/a — correctly explained, can't be evaluated here |
| 2026-09-18-...-after-cf0962e3 | **yes** | **1.577** (worst, `pcrec_a770139e_auto-nocaps-simdna`, over 4 values) | **1.577** (13.516966÷8.571827, from the record; cross-checked to six decimals against the report's own committed `.subject-grain.tsv`) | **EXACT MATCH** |
| 2026-09-18-...-ext-first-cf0962e3 | **yes** | not evaluable: "no row in this report matches the selector" | n/a (this report's roster has NO pcrec testee at all — verified by grep of its own compile rows; the glob matches nothing regardless of grain) | n/a — correctly explained, can't be evaluated here |
| 2026-09-19-...-ext-second-cf0962e3 | **no** (`subject_grain: (none)`) | not evaluable: "the clause selects grain=subject but no --subject-grain input was supplied" | n/a (no subject-grain input) | n/a — correctly explained, can't be evaluated here |

No disagreement anywhere — the ONE report where evaluation is actually
possible (subject-grain present AND a pcrec testee in the roster)
matches the hand derivation exactly, so nothing required stopping.
**P4 as a whole now reads `refuted` on `2026-09-18-...-after-cf0962e3`**
(P4.a and P4.b both evaluate and both fail their own threshold — the
truth stands, per the ruling's own instruction), still `partial` on
`2026-09-17-...-first-a770139e` (P4.a refuted, P4.b not-evaluable there,
correctly, for lack of a subject-grain sibling), and still `not
evaluable` on both `ext-*` reports (no pcrec testee, independent of
grain).

**All four sidecars regenerated again** (same direct invocation as
Follow-up 1, since only these four are stamped against this file);
determinism re-checked on all four (second run to stdout, byte-compared,
identical). Fact diffs reviewed:
- `2026-09-18-...-after-cf0962e3`: P4 moves `partial` (R-PRED-4) →
  `refuted` (R-PRED-2, now 3 firings) with the exact measured line
  `P4.a: ... = 1.112 over 8 value(s); P4.b: ... = 1.577 over 4
  value(s)`; R-PRED-4 correspondingly drops out of the "fired" section
  back into "did not fire" (no compound prediction disagrees any more,
  since P4 no longer does).
- `2026-09-17-...-first-a770139e`: **stamp-only** (`predictions_sha256`
  moves; no other line changes) — P4 was already `partial` before and
  after (P4.b's INTERNAL reason changed, from "no row matches" to "no
  --subject-grain supplied", verified by calling `evaluate_predictions`
  directly, but the sidecar's own rendering of a `partial` parent never
  prints per-clause reasons — the SAME known, documented limitation
  `docs/design/predicate_audit_v1.md` already names — so nothing visible
  moves here).
- `2026-09-18-...-ext-first-cf0962e3`: **stamp-only**, confirming this
  report is unaffected either way.
- `2026-09-19-...-ext-second-cf0962e3`: ONE visible line changes — P4's
  rendered not-evaluable reason for P4.b goes from "no row in this
  report matches the selector" to "the clause selects grain=subject but
  no --subject-grain input was supplied", a MORE PRECISE, MORE HONEST
  reason (the `grain=subject` check now fires before the row-match
  check ever runs) — not a regression, an improvement in what the tool
  says about why it can't answer.

`catalogue/check_interpret.py` was not touched in this follow-up (no
new load-time behavior; `grain=subject` is an existing, already-tested
selector key, `catalogue/fixtures/predictions-subject-grain.tsv`'s own
precedent).

## Validation

    $ make check-interpret
    == check-interpret ==
    gen.py: checked 243 file(s) in 75 fixture(s) -- ok

    check-interpret section 1: 21 check(s) passed
    check-interpret section 2: 8 check(s) passed
    check-interpret section 3: 36 check(s) passed
    check-interpret section 4: 133 check(s) passed
    check-interpret section 5: 4 check(s) passed
    check-interpret section 6: 1 check(s) passed
    check-interpret: 203 passed, 0 FAILED

    $ python3 catalogue/fixtures/gen.py --check
    gen.py: checked 243 file(s) in 75 fixture(s) -- ok

    $ make check-schema
    check-schema: 6 example(s) accepted, 74 sabotage(s) rejected for the
    intended rule, 0 sabotage(s) WRONG

All three green, 0 failures, 0 named exceptions anywhere in
`check_interpret.py` for this file. `make check-harness`/`make
check-report` were not run (neither touches a file this task changed;
the boilerplate reserves long runs for the manager and neither is on
the task's own validation list). `catalogue/rules.toml`'s
`catalogue_version` is unchanged at 3.8 (no rule, threshold or
predicate moved by this lane) — no `[[pin_order]]` append is owed.

## Files changed

- `docs/dev/predictions/capability-0.1-first.tsv` — P2.a/P2.b's and
  P4.a/P4.b's selectors and reducer arguments corrected (four rows
  total, across three commits: the P2 fix, the P4 glob+reducer fix,
  P4.b's `;grain=subject` addition); everything else (every OTHER
  clause, every column but selector/reducer on these four) byte-
  identical to the committed history.
- `docs/dev/predictions/CLAUDE.md` — new "Revising an already-scored
  file" standing-rule section; the `capability-0.1-first.tsv` entry's
  header addendum names all three fixes and all three dates/rulings;
  the P2 and P4 addenda (after the historical P9 discussion) carry the
  full hand-verification tables, including the final per-report
  `grain=subject` table the second ruling asked for.
- `catalogue/check_interpret.py` — ALL THREE named exceptions this
  file's history ever carried are gone: the Q6 (i) one
  (`_KNOWN_HISTORICAL_LOAD_DEFECTS`, `_load_predictions_with_named_
  exceptions`, retired at first delivery) and the Q6 (ii)/Cause-C one
  (`_SIDECARS_BLOCKED_ON_CAPABILITY_FIRST_P4_CAUSE_C`, retired in this
  follow-up). Section 1 and section 3 are both the plain, unconditional
  form; the general per-sidecar `try`/`except` (added at first delivery,
  kept) still catches any OTHER, future `InterpretError` as a named
  failure rather than an uncaught crash.
- `catalogue/CLAUDE.md` — the stopgap paragraph rewritten again to
  describe both retirements and the manager's P4 ruling, in place.
- `reports/2026-09-17-capability-0.1-budu-ryzen1600-first-a770139e.interpretation.md`,
  `reports/2026-09-18-capability-0.1-budu-ryzen1600-after-cf0962e3.interpretation.md`,
  `reports/2026-09-18-capability-0.1-budu-ryzen1600-ext-first-cf0962e3.interpretation.md`,
  `reports/2026-09-19-capability-0.1-budu-ryzen1600-ext-second-cf0962e3.interpretation.md`
  — regenerated (determinism-checked, fact diffs reviewed above).
- `docs/dev/plan.md` — `[B93]` row: `STATE:blocked` → `STATE:started`
  (per the manager's instruction; the manager closes it at merge).
- `docs/dev/dev_journal.md` — a matching follow-up entry.
- `docs/dev/lanes/b93pred_report.md` — this report.

## Handback

All five charter items are now DELIVERED and independently verified
across three rulings, all applied the same day (2026-09-26): P2.a/P2.b
(first delivery, cross-checked against the 2026-09-17 ledger's 5.29),
P4.a/P4.b's glob+reducer fix (second ruling, hand-verified against the
report TSVs and the underlying JSONL records for every committed
report), and P4.b's `grain=subject` addition (third ruling — the
residual Cause-A finding from the second ruling, resolved rather than
merely left as found). The one report where P4.b is genuinely
evaluable now matches its hand-derivation EXACTLY (1.577) and reads
`refuted` — the manager's own instruction ("if P4.b now reads REFUTED,
that is the truth and stands") — while the other three reports each
read `not evaluable` for a distinct, correctly-explained, verified
reason (two lack a subject-grain sibling; one lacks a pcrec testee).
No hand-derived/interpreted disagreement occurred at any point, so
nothing required stopping. The standing rule is written, all three
named exceptions this file's history ever carried are retired from
`check_interpret.py`, and the four sidecars are regenerated for real —
`make check-interpret` 203/0, `gen.py --check` clean, `make check-schema`
6/74/0. `docs/dev/plan.md`'s `[B93]` row is `STATE:started`, per the
manager's own instruction, for them to close at merge. Nothing is OWED.
