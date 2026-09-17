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
  columns (`pattern`, `subject_or_na`, `regime_or_na`, `form`, `testee`)
  and `section`. `*` is the only wildcard; one field may carry a
  `|`-joined alternation. A testee glob may name a config without a pin
  (`pcrec_*_auto-caps-simdna`) so a prediction survives a re-pin.
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
