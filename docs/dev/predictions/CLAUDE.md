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
