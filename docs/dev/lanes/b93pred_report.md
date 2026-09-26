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
   with no exception.** BUILT for Q6 (i) specifically — confirmed by
   `make check-interpret` section 1 (21/21, no `_KNOWN_HISTORICAL_LOAD_
   DEFECTS` table left in `catalogue/check_interpret.py`, no per-file
   carve-out in the load loop). **NOT fully true for `make check-
   interpret` as a whole** — see the P4 finding below, which needed a
   NEW, narrower, differently-caused stopgap to keep the suite green.
5. **Regenerate the four blocked sidecars, 0 failures.** NOT DONE — see
   the P4 finding. `make check-interpret` is green (200/200, 0 FAILED)
   but by SKIPPING the four sidecars again, for a different, real
   reason, not by regenerating them.

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

## Validation

    $ make check-interpret
    == check-interpret ==
    gen.py: checked 243 file(s) in 75 fixture(s) -- ok

    check-interpret section 1: 21 check(s) passed
    check-interpret section 2: 8 check(s) passed
    check-interpret section 3: 33 check(s) passed
    check-interpret section 4: 133 check(s) passed
    check-interpret section 5: 4 check(s) passed
    check-interpret section 6: 1 check(s) passed
    check-interpret: 200 passed, 0 FAILED

    $ python3 catalogue/fixtures/gen.py --check
    gen.py: checked 243 file(s) in 75 fixture(s) -- ok

    $ make check-schema
    check-schema: 6 example(s) accepted, 74 sabotage(s) rejected for the
    intended rule, 0 sabotage(s) WRONG

All three green. `make check-harness`/`make check-report` were not run
(no file either touches; the boilerplate reserves long runs for the
manager, and neither is on this task's own validation list). `catalogue/
rules.toml`'s `catalogue_version` is unchanged at 3.8 (no rule, no
threshold, no predicate moved) — no `[[pin_order]]` append is owed.

## Files changed

- `docs/dev/predictions/capability-0.1-first.tsv` — P2.a/P2.b's selector
  and reducer argument corrected (two rows, both companion fixes);
  everything else byte-identical to the committed history.
- `docs/dev/predictions/CLAUDE.md` — new "Revising an already-scored
  file" standing-rule section; the `capability-0.1-first.tsv` entry
  gains a dated header addendum (naming the [B93] fix and pointing at
  this report) and a dated addendum after the historical P9 discussion
  (the applied fix, the ledger cross-check, and the filed P4 finding).
- `catalogue/check_interpret.py` — the Q6 (i) named exception
  (`_KNOWN_HISTORICAL_LOAD_DEFECTS`, `_load_predictions_with_named_
  exceptions`) is GONE; section 1's load loop is unconditional. A NEW,
  differently-named, differently-caused stopgap for P4's Cause C
  (`_SIDECARS_BLOCKED_ON_CAPABILITY_FIRST_P4_CAUSE_C`) replaces it in
  section 3, plus a general per-sidecar `try`/`except` so any OTHER
  future `InterpretError` reports as a named failure rather than an
  uncaught crash that would silently stop sections 4-6 from running.
- `catalogue/CLAUDE.md` — the stopgap paragraph rewritten to describe
  retirement (Cause B) and the new filing (Cause C), in place.
- `docs/dev/lanes/b93pred_report.md` — this report.

## Handback

Item 1-4 of the charter are DELIVERED and independently verified (the
ledger cross-check, the four-report empirical table, the byte-field
diff table). Item 5 is NOT delivered: the four sidecars stay
un-regenerated, blocked on a SECOND, separate, already-diagnosed defect
(P4.a/P4.b's Cause C + malformed reducers) that Cause B's fix was
masking and that this lane's own narrower charter does not license a
unilateral fix for. `make check-interpret`/`gen.py --check`/`make
check-schema` are all green. Nothing else is OWED beyond the P4 ruling
named above.
