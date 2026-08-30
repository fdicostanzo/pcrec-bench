# docs/dev/ledgers/ — the manager's READINGS of a report (the outbox's source)

A LEDGER is what a report is read INTO before its findings go to pcrec:
item by item, every number with its regime / pattern / testee and the
ratio's direction stated, the set's predictions (its NOTES.md, the inbox's
predictions on our subjects) confirmed or refuted with the number,
adapter-side findings, the ranked optimization candidates (pcrec D86, one
row at a time), the asks, and a CHECKLIST the NEXT sample of the same set
is read against. The outbox item (`docs/dev/outbox_to_pcrec.md` O-n) is
the distilled, durable form; the ledger is the full derivation, with
report line citations, so a number in the outbox can be traced to a table.

Rules: one file per (set, sample, pin), named `YYYY-MM-DD-<set>-<version>-
<label>-<pin>.md`, never edited after its outbox item is sent (a later
reading is a new file); extracted by a READ-ONLY lane from the committed
report(s) + the records, then read by the manager; numbers only — the
manager's interpretation lives in plan.md / the journal / the outbox.
Not a measurement (D35 does not apply), not a ranking input.

| file | what |
|---|---|
| `2026-08-30-bounded-0.1-first-sample-36d5963.md` | bench/bounded@0.1's first sample at pcrec 36d5963 (abi 11), the [OPT-4] BEFORE: the compile axis (engine per rung and form, the DFA→VM transitions per skeleton, the refusal rows, compile phases, the ×315-×687 wasted DFA builds, `RX_UNROLL_K`'s first movement), the match axis per regime (auto 1st-or-2nd on 10/13/7 of 22 members; the ×18,400 / ×65,500 backtracking cliffs; the `search-filter` ×37 penalty; the counted-DFA ×5.96 inversion; the ctx band 4-5× behind the JIT), 25 predictions ledgered, ten adapter/harness findings, six ranked candidates, six asks, an 18-point AFTER checklist for the 96e44c2 sample. Source of outbox O-9 |

Maintenance: update this file when a ledger is added.
