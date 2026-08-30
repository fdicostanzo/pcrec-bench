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
| `2026-08-30-abi12-after-96e44c2.md` | the abi-12 AFTER sample at pcrec 96e44c2 ([OPT-4] ruling B) against the 36d5963 BEFORE, all three sets: the `sel=` census (bounded 32 selected / 14 collapsed-prefilter, loglines 20/2, email 6/0; no size-cap rescue anywhere), [OPT-4] SPLITS — the ctx band 2.2-3.1× and level-context 4.60× faster (13.4× → 2.9× behind the JIT; the rescued fallback beats pcrec's own forced VM 2.2-4.6×) where structure survives the collapse, `[a-z]{0,32768}` 3.6× SLOWER where the collapsed language `[a-z]*` is nullable and can never dismiss (even the digits subject ×1.65); the controls flat (+216/224 B stamp block everywhere; `year4` +4,096 B unattributed; http-5xx's ×1.03 flag retired); the 18-point checklist scored 12/3/2/1; the emit/code-bytes survey (the class ladder's growth is 100 % table data, code flat at 11.6-12.7 KB); the R8 Δ column fired nowhere (one pin per report); the [OPT-5] frame (the DFA loses 5.1-5.9× to the VM on letters at EVERY rung from 256 and wins 1.75× on digits at every rung — the knee is a property of the subject, not the count). Source of outbox O-10 |

Maintenance: update this file when a ledger is added.
