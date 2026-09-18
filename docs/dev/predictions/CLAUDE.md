# docs/dev/predictions/ — machine-readable predictions

A prediction stated BEFORE a run, in a form `pcrecbench interpret` can
score ([B13]; `docs/design/interpreter_v1.md` §6). One TSV per
prediction SET, named for the source that stated it. Before this
directory existed, every prediction in this project lived in prose — an
inbox item, a `NOTES.md` list, a ledger table — and was scored by hand,
which is the failure mode R-PRED-3 exists to close: a prediction nobody
re-read is a prediction nobody scored.

## The file

Fifteen tab-separated columns, in this order:

```
prediction_id  clause  source  source_ref  stated_utc  subbench  version
selector  quantity  reducer  op  lo  hi  unit  note
```

- **`prediction_id` + `clause`.** A COMPOUND prediction is decomposed at
  AUTHORING time into clause-suffixed sub-ids (`P5.a`, `P5.b`), one row
  each — required, not optional: ten of the thirteen real predictions
  this format was tested against were scored per clause. The parent's
  verdict is R-PRED-1/2/4's arithmetic roll-up (all-confirmed →
  confirmed, all-refuted → refuted, any mix → `partial`).
- **`selector`** — `;`-joined `key=glob` over the report TSV's own key
  columns (`pattern`, `subject_or_na`, `regime_or_na`, `form`, `testee`),
  `section`, and (catalogue 2.0, [B47]) `grain` (`set` | `subject`). `*`
  is the only wildcard; one field may carry a `|`-joined alternation. A
  testee glob may name a config without a pin (`pcrec_*_auto-caps-
  simdna`) so a prediction survives a re-pin.
- **`grain=subject`** routes the clause to the SECOND input,
  `--subject-grain PATH` (a committed `<report>.subject-grain.tsv`
  slice — `reports/CLAUDE.md`), instead of the primary report; with none
  supplied the clause is `not-evaluable` BY NAME ("the clause selects
  grain=subject but no --subject-grain input was supplied"). Absent this
  key (every predictions file committed before catalogue 2.0), nothing
  changes. **The DEFAULT section a selector with no `section=` clause
  reads is now `rank` UNION `excluded` for `n_wrong`/`n_gave_up`/
  `pass_rate`/`status`** (ruling (α)) — `rank` alone, as before, for
  every other quantity — closing a corpus-wide tautology under which
  such a clause could never see a failing cell (a wrong-answer or
  give-up cell is EXCLUDED from ranking by construction, so `rank` rows
  never carry a positive failure count). An EVALUATED clause (confirmed
  or refuted, not only not-evaluable) is also annotated with what its
  own selector reaches OUTSIDE that default read — "; also present in:
  excluded (N)" (ruling (β)) — stating the tool's own population rather
  than leaving a reader to notice the gap. `docs/design/interpreter_v1.md`
  §6.7 is the full statement; `docs/design/interpret_subject_grain_v1.md`
  §5/§6 is the derivation and the eleven rulings.
- **`quantity`**, **`reducer`**, **`op`** — CLOSED SETS, validated at
  load (§6.3). A token outside one is a LOAD ERROR naming the closed
  set, never a silent skip.
- **`stated_utc`** — checked against the EARLIEST `store/index.tsv`
  timestamp for this (subbench, version), superseded rows INCLUDED
  (§6.5). What that proves and what it does not is stated plainly in the
  note: it proves the prediction predates this population's first-ever
  measurement, not that no other channel informed it.

## What a prediction CANNOT say

The report TSV carries `n_wrong` and `pass_rate`; it never carries an
answer, a span or a capture (§6.4). So "answers as the oracle says" is
expressible as `n_wrong eq 0`, "disagrees with the oracle" as `n_wrong
gt 0` on the named cell plus `eq 0` on its controls — and the SPECIFIC
answer or span is not expressible at all. Such a clause is a LOAD ERROR
with a named reason, never a silent `not-evaluable`;
`catalogue/fixtures/predictions-inexpressible.tsv` is the fixture that
proves it, and `make check-interpret` section 1 asserts the refusal.

## Files

- `syntax-0.1-first.tsv` — `bench/syntax/NOTES.md`'s **P1-P13**, the one
  committed, fully-scored prediction set this project has, transcribed
  per §6.6: 35 clause rows over 13 parents. The two INEXPRESSIBLE
  clauses (P9's `[4,9]` span, P12's "agrees with `bak-1`" answer
  equality) are ABSENT by construction and are the fixture above.
  Scored against
  `reports/2026-09-07-syntax-0.1-budu-ryzen1600-first-d34c9131.tsv` it
  reads 4 confirmed / 4 refuted / 5 partial. It does NOT reproduce the
  ledger's own 3/5/5 tally, and that is the intended outcome (§6.6): the
  per-clause verdicts are `interpret`'s output and are authoritative,
  the parent verdict is the stated arithmetic, and a ledger's tally is a
  human reading the tool must not try to reproduce.
- `capability-0.1-first.tsv` — `bench/capability/NOTES.md`'s **P1-P10**,
  transcribed 2026-09-16, 17 clause rows over 9 parents (P9 has no row —
  see below). Scored against `reports/2026-09-17-capability-0.1-budu-
  ryzen1600-first-a770139e.tsv`: 1 confirmed (P1), 1 refuted (P8), 6 not
  evaluable (P2/P3/P4/P6/P7/P10 — this report's grain is `set` only, no
  `.subject-grain.md` sibling `interpret` reads, and several clauses
  select a `subject_or_na` or `compile:`-scoped comparison the set-grain
  TSV structurally cannot answer). **P5 is a KNOWN FALSE-POSITIVE
  CONFIRM, read by the manager as REFUTED** (ledger `docs/dev/ledgers/
  2026-09-17-capability-0.1-first-a770139e.md` §3, §7.2): its selector
  names no `section`, so per §6.3's own rule it reads the `rank` section
  only — and a row with `n_wrong > 0` is by construction NEVER a `rank`
  row (R-STATUS-3 moves it to `excluded` instead), so `interpret`
  mechanically "confirms" P5 by being structurally blind to the very
  population (six `redos-nested` patterns' give-ups/wrong-answers/
  timeouts) it was meant to check. `evil-alt-nested` — one of P5's six
  named patterns — is wrong on `dfa-nocaps`/`auto-nocaps` and times out
  on three pcrec captures arms in this exact report (§1.2 Finding C),
  which the interpreter's own mechanical run cannot see.
  **VERIFIED FIX, not yet transcribed into this file** (lane `b42predhyg`,
  2026-09-17, scratch-tested against the real report, never committed):
  adding `section=excluded` to the selector and switching the clause to
  `quantity section; reducer set_of(pattern); op set-subset` (hi empty —
  P8's own mechanism, already committed above) correctly REFUTES on the
  real population (`measured: {email-nested-plus, evil-alt-nested}`,
  `R-PRED-2`) rather than false-confirming. Residual, honestly noted: the
  SAME mechanism reads a truly clean single-pattern population as
  **not evaluable** ("no row in this report matches the selector",
  `R-PRED-3`), not confirmed — `set-subset` of an empty target set has no
  way to distinguish "checked and clean" from "never checked", a property
  P8's own use of the identical mechanism never exposed because P8's
  measured set was never empty. **Predictions are stated-PRE-RUN
  artifacts (this file's own "Writing one" section, `interpreter_v1.md`
  §6.5) and this format defines no revision mechanism for an
  already-scored file** — the fix above is therefore NOT applied to this
  committed file (which stays the historical record of what was
  predicted and how it was actually scored) and is instead the
  RECOMMENDED shape for a new, separately-dated predictions file stated
  before this set's next sample; full derivation and the exact proposed
  TSV rows are in `docs/dev/lanes/b42predhyg_report.md`.
  **SUPERSEDED, catalogue 2.0 ([B47], 2026-09-17, ruling (α)):** the
  false-confirm this note diagnoses is now fixed MECHANICALLY, without
  editing this file's own selector — `_select`'s default section for
  `n_wrong`/`n_gave_up`/`pass_rate`/`status` widened from `rank` alone
  to `rank` UNION `excluded`, so P5's ORIGINAL committed clause (no
  `section=` clause at all) now reads REFUTED against this exact report:
  `measured: worst evil-alt-nested/(set)/short-subject-search/plain/
  libpcre2_10.46_dfa-nocaps-simdna = 10.000 over 207 value(s)` — the
  verdict the manager reached by hand, from the ORIGINAL file, no
  transcription needed. `b42predhyg`'s `section=excluded` +
  `set-subset` shape remains the RECOMMENDED way to state a NEW P5-style
  clause going forward (it is more precise about the population and
  names the set of offending patterns rather than only their worst
  ratio), but is no longer required to avoid the false-confirm hazard.
  `docs/design/interpreter_v1.md` §6.7 / `interpret_subject_grain_v1.md`
  §5 are the full derivation.
  **P9 (NOTES.md: `mojibake-curly-quote`'s record omits
  `patterns[].canonical_text`) has NO row and is INEXPRESSIBLE by this
  format, more fundamentally than syntax's own P9/P12 fixture cases
  above**: `canonical_text`'s presence or absence is a fact about the
  RECORD's own `patterns[]` array, which neither the report TSV nor
  `store/index.tsv` carries at any grain — there is no `quantity` in
  §6.3's closed set that could even be attempted (syntax's P9, by
  contrast, could at least name `n_wrong` as a wrong-but-unattributable
  signal; this claim has no analogous foothold). NOTES.md's own text
  anticipates this ("checkable once the schema promotion (CB3) and a
  future measurement land") — P9 was never meant to be `interpret`-scored
  today, and the recommended new file above should carry it as a
  documented ABSENT-by-construction line (ledger §7.3), not a load-error
  fixture case (it is not a "wrong quantity token" mistake to guard
  against — the format simply has no vocabulary for a schema-presence
  claim).

- `capability-0.1-ext-roster.tsv` — lane `b51preds`, 2026-09-18: the
  predictions for the NEXT sample of the five new [B7]/L6b engines
  (`re2-default`, `re2-longest`, `onig-default`, `tre-default`,
  `vectorscan-block-nosom`) on `bench/capability@0.1`, so that sample is
  machine-scored instead of reading `not-evaluable` on every clause the
  way `docs/dev/ledgers/2026-09-18-capability-window-cf0962e3.md` §5.5
  found for the FIRST ext-roster sample (P1-P10 there were authored
  against the original seven-testee roster and name no testee_id this
  five-engine population contains). **19 clause rows over 9 parents**:
  P1 (the did-not-compile SET stability for tre-default/vectorscan-
  block-nosom -- the two engines whose refusal population survived a
  ranking-group check, see below), P2 (TRE's `high-byte-run` correctness
  gap reproducibility, plus three related raw-high-byte/no-unusual-
  construct patterns, each stating what a reproduction vs. a one-off box
  artifact would read), P3/P4 (the family-11 semantics-divergence trio
  wrong on both leftmost-longest engines, clean on both non-boolean-
  grain leftmost-first engines), P5 (vectorscan's boolean-grain
  rendering: structurally clean on the trio, and its entire
  excluded-pattern census staying a strict subset of what the
  non-boolean engines' census shows), P6 (re2-longest's full wrong-
  answer population as an exhaustive four-pattern set), P7 (onig's
  `-17:retry` give-up on `evil-alt-nested` reproducing by its NUMERIC
  facts -- `n_gave_up`/`n_wrong` -- with the specific code text named as
  inexpressible, the same class of limit as an answer/span claim), P8/P9
  (tre-default's and the two clean engines' full excluded-pattern census
  as exhaustive sets). Dry-run verified (bypassing check_stated_utc
  below, via `interpret.evaluate_predictions` called directly): **19/19
  clauses evaluate against the committed
  `reports/2026-09-18-capability-0.1-budu-ryzen1600-ext-first-cf0962e3.tsv`**
  -- all CONFIRMED today (expected and correct for a stability/
  reproducibility claim scored against the exact report it describes;
  the real test is the NEXT sample), zero `not-evaluable`.

  **TWO STRUCTURAL FINDINGS this lane made while authoring against real
  data, both left as findings rather than worked around:**

  1. **`check_stated_utc` (interpret.py:1700) cannot pass for ANY
     prediction about a population that has ever been measured before,
     which is every population this project could plausibly write a
     SECOND predictions file for.** It anchors to the EARLIEST
     `store/index.tsv` timestamp ever recorded for `(subbench,
     version)`, a fixed point in the past; `capability@0.1`'s is
     `2026-09-17T00:50:53Z` (`bench/capability`'s own first sample). Any
     `stated_utc` honestly dated after that -- which an honest re-sample
     prediction always is, by definition, since the population already
     exists -- fails `check_stated_utc` and aborts the WHOLE
     `pcrecbench interpret --predictions <file> <report>` call before a
     single clause is scored (reproduced live against a one-line scratch
     predictions file dated 2026-09-18, `PredictionError`, exit before
     `evaluate_predictions` runs). This file's own `stated_utc` values
     are the honest authoring date and WILL trip this check the same
     way -- the clause-level evaluability above was verified by calling
     `interpret.evaluate_predictions` directly (skipping only
     `check_stated_utc`, not the selector/reducer/op machinery), which is
     the only way to see this file's clauses resolve today. The check's
     own design note (`interpreter_v1.md` §6.5) already names its
     "residual limit" honestly ("it cannot see a prediction informed by
     ... outside knowledge... it has no anchor for a population never
     measured before") but does not name THIS consequence: a population
     measured even ONCE can never again receive a scorable predictions
     file through the CLI's default path, full stop, regardless of how
     genuinely pre-run the new file is. Filed for a ruling, not fixed
     here (a docs-only predictions-authoring lane is not the place to
     change `interpret.py`'s semantics); candidates a ruling could pick:
     anchor per-testee/per-selector-population instead of per-
     `(subbench, version)`, add an explicit CLI acknowledgment flag for
     "this file is about a population that already exists", or accept
     that `check_stated_utc` is a first-sample-only instrument and score
     later files with it disabled by convention.
  2. **`render_tsv`'s `did_not_compile` section only lists a refusal for
     a (pattern, regime) RANKING GROUP that already exists** -- i.e. at
     least one OTHER testee in the same query ranks a match row for that
     pattern (`report.py`'s `did_not_compile_by_pattern` loop is nested
     inside the per-ranking-group loop, `report.py:4555-4564`). A
     pattern where EVERY testee in the query's own roster fails to
     compile (a real `did-not-compile`, or the pre-compile
     `unsupported-by-declaration` policy intercepting it first) has NO
     ranking group at all, so it is invisible to any `section=
     did_not_compile` selector -- even though the record's own JSONL
     carries `compile_outcome: did-not-compile` in full (confirmed by a
     direct read of the record). This is what happened to
     `balanced-parens-rec` (onig-default's only real did-not-compile
     pattern, `requires-recursion`'s `(?R)` spelling gap): every OTHER
     engine in the five-engine ext-roster query either declines it by
     declaration or (onig) also fails to compile it, so no ranking group
     for this pattern exists in `reports/2026-09-18-capability-0.1-*-
     ext-first-cf0962e3.tsv` at all, and a `section=did_not_compile;
     testee=oniguruma_*` selector reads "no row in this report matches
     the selector" -- not a defect in the selector, a genuine gap this
     file's original P1.a clause hit live. The SAME shape blocks a
     "RE2's did-not-compile set is EMPTY" claim for a different reason
     (`set-subset` of a target the population never populates any row
     for is indistinguishable from "never checked", the identical
     residual gap `docs/dev/lanes/b42predhyg_report.md` already named for
     the original P8 mechanism -- now independently reproduced against
     real all-engines-refuse data rather than argued from the empty-set
     case alone). **Three originally-drafted clauses (onig's
     `balanced-parens-rec` did-not-compile stability; RE2-default's and
     RE2-longest's "did-not-compile stays empty" claims) were DROPPED
     from the committed file for this reason** rather than committed as
     clauses fated to always read `not-evaluable` -- per this project's
     own "must not happen" rule for a predictions file (the same
     posture `docs/dev/predictions/CLAUDE.md`'s own P9/P12 precedent
     takes for an inexpressible claim). `docs/dev/lanes/b51preds_report.md`
     has the exact selectors that were tried and the specific rows they
     failed to find.

## Writing one

By hand, by the person who states it, before the run, committed before
the run. A prediction stated in an inbox item is TRANSCRIBED by the
manager session at ack time — the same motion that already moves an
inbox item into a plan row. **Parsing inbox prose is explicitly
rejected**: a regex over English is a second source of truth for what
pcrec predicted, and getting it wrong would be worse than not having it.

    python3 -m pcrecbench interpret --render \
        --predictions docs/dev/predictions/<slug>.tsv reports/<name>.tsv

Maintenance: update this file when a prediction set is added or retired.
