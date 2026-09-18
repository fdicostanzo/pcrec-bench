# lane b51preds — the ext-roster predictions file

Branch `lane/b51preds`. Docs-only: one new file
(`docs/dev/predictions/capability-0.1-ext-roster.tsv`), one CLAUDE.md
update (`docs/dev/predictions/CLAUDE.md`), this report. No code changed,
no report/store touched, nothing merged.

## Task

`docs/dev/ledgers/2026-09-18-capability-window-cf0962e3.md` §8 checklist
item 1: author a predictions file for the next `bench/capability@0.1`
sample of the five new [B7]/L6b engines (`re2-default`, `re2-longest`,
`onig-default`, `tre-default`, `vectorscan-block-nosom`), covering at
minimum: compile/refusal census stability against the corrected
(b46tags) capability tags, TRE's `high-byte-run` correctness-gap
reproducibility (stated honestly as a reproduction-vs-one-off
distinction), the family-11 divergence trio on both leftmost-longest
engines, onig's `-17:retry` give-up on `evil-alt-nested`, vectorscan's
boolean-grain rendering, and re2-longest's wrong-span population on the
divergence family.

## The file

`docs/dev/predictions/capability-0.1-ext-roster.tsv`, 19 clause rows
over 9 parent predictions (P1-P9), `stated_utc 2026-09-18T00:00:00Z`,
`source docs/dev/ledgers/2026-09-18-capability-window-cf0962e3.md`. Per
parent, its evidential base (the exact ledger section/report figures it
transcribes) and its dry-run result:

| id | claim | evidential base | dry-run |
|---|---|---|---|
| P1.a | tre-default's did-not-compile set stays exactly {wild-datetime-datefinder-alternation, wild-secrets-username-password-pair, wild-waf-crs-942500-comment-obfuscation} | ledger §5.1's compile census (41/20/3) + `testees/tre/CLAUDE.md` (d).4's POSIX-bracket-hyphen hazard naming all three; verified directly against the report's `did_not_compile` section rows (grepped) | confirmed |
| P1.b | vectorscan-block-nosom's did-not-compile set stays exactly {wild-codegrammar-json-number-extended, wild-codegrammar-json-stringcontent-escape} | ledger §5.1 (40/22/2) + `testees/vectorscan/CLAUDE.md`'s "free-spacing is more nuanced than its witness" finding | confirmed |
| P2.a/.b | tre-default's `high-byte-run` cell reproduces `n_wrong=15` (throughput, all 3 subjects x 5 trials) and `n_wrong=195` (search, 39/75 subjects x 5 trials) exactly | ledger §5.4's table (pass_rate 0.0000 / 0.4800) + `testees/tre/CLAUDE.md`'s correctness section, cross-checked against the report's own `n_wrong` column directly (not just pass_rate) | confirmed |
| P2.c/.d/.e | tre-default stays wrong on exactly 5 trials for tag-pair-match, wild-waf-crs-942360-concat-sqli, mojibake-curly-quote | ledger §5.4's table (all three at pass_rate 0.9867, n_wrong=5) | confirmed |
| P3.a/.b | the family-11 trio (file-ext-order, keyword-prefix-order, router-prefix-order) stays wrong (n_wrong=5 each) under re2-longest and tre-default | ledger §5.4's family-11 table, both POSIX-leftmost-longest rows | confirmed |
| P4.a/.b | the same trio stays clean (n_wrong=0) under re2-default and onig-default | ledger §5.4's family-11 table, both perl-leftmost-first rows | confirmed |
| P5.a | vectorscan reads n_wrong=0 on the trio too, STATED as a structural consequence of boolean grain (`testees/vectorscan/CLAUDE.md`'s governing ruling), never a real convention claim | ledger §5.3 + §5.4 | confirmed |
| P5.b | vectorscan's entire excluded-pattern census is exactly {evil-alt-nested} -- never grows to include the trio | direct report query (`section=excluded;testee=vectorscan_*`), cross-checked by hand against the TSV | confirmed |
| P6 | re2-longest's entire excluded-pattern census is exactly {evil-alt-nested, file-ext-order, keyword-prefix-order, router-prefix-order} | direct report query, cross-checked by hand | confirmed |
| P7.a/.b | onig-default's evil-alt-nested cell reproduces n_gave_up=10, n_wrong=0 | ledger §5.4's give-up table + the record's own `giveup_smallest` row (`-17:retry`, byte 18); the CODE ITSELF is stated as inexpressible by this format's closed quantity vocabulary, not attempted | confirmed |
| P8 | tre-default's entire excluded-pattern census is exactly these 8: {evil-alt-nested, file-ext-order, high-byte-run, keyword-prefix-order, mojibake-curly-quote, router-prefix-order, tag-pair-match, wild-waf-crs-942360-concat-sqli} | union of every tre-default finding in ledger §5.4, cross-checked directly against the report | confirmed |
| P9.a/.b | re2-default's and onig-default's entire excluded-pattern census is exactly {evil-alt-nested} (a control pair) | direct report query | confirmed |

**Dry-run method.** `pcrecbench interpret --predictions <file> <report>`
(the CLI path the brief names) cannot be run against this file at all --
see Finding 1 below. Instead, `pcrecbench.interpret.evaluate_predictions`
was called directly (the exact same selector/reducer/op/section-default
machinery `interpret()` calls, skipping only `check_stated_utc`) against
the committed
`reports/2026-09-18-capability-0.1-budu-ryzen1600-ext-first-cf0962e3.tsv`
and `store/index.tsv`. Result: **19/19 clauses CONFIRMED, 0
not-evaluable.** All-confirmed is the correct and expected outcome for a
stability/reproducibility prediction set scored against the exact report
it transcribes (per the team lead's own brief: "confirmed or refuted
TODAY is fine and expected for stability claims"); the clauses' real job
is to be re-scored, unedited, against the NEXT ext-roster sample, where a
`refuted` verdict on any of them is itself the finding.

`make check-interpret`: 149 passed, 0 failed (unchanged in shape; the
new predictions file does not touch the fixture/golden machinery
`check-interpret` gates, and the run confirms it does not break
determinism there).

## Two structural findings, not worked around

Both are written up in full in `docs/dev/predictions/CLAUDE.md`'s new
`capability-0.1-ext-roster.tsv` entry; summarized here for the handback.

**1. `check_stated_utc` (pcrecbench/interpret.py:1700) cannot pass for
ANY predictions file about a population `bench/capability@0.1` has ever
measured before -- which, after 2026-09-17, is every predictions file
this task could produce.** Reproduced live:

```
$ python3 -m pcrecbench interpret --predictions /tmp/scratch_pred_test.tsv \
      reports/2026-09-18-capability-0.1-budu-ryzen1600-ext-first-cf0962e3.tsv
interpret: /tmp/scratch_pred_test.tsv:2 (TEST.a): stated_utc 2026-09-18T00:00:00Z
does not precede the earliest store/index.tsv timestamp for capability@0.1
(2026-09-17T00:50:53Z), superseded rows included (§6.5)
```

The check anchors to the population's absolute first-ever measurement,
which never moves forward; any later file's honest `stated_utc` --
including this one's -- fails it and aborts the WHOLE `interpret` call
before a single clause is scored, every time, forever. This is a real
consequence the design note's own "residual limit" paragraph
(`interpreter_v1.md` §6.5) does not name: it discusses what the check
CANNOT prove, not that it makes a whole future class of legitimate files
mechanically unscoreable via the CLI's own default path. Not fixed here
(out of a docs-only lane's scope to change `interpret.py`'s semantics);
flagged for a ruling, with three candidate directions named in the
CLAUDE.md entry.

**2. `render_tsv`'s `did_not_compile` section only fires inside an
EXISTING ranking group** (`report.py:4555-4564`, nested inside the
per-ranking-group loop) -- a pattern every testee in the query's roster
fails to compile has no ranking group at all, so it is invisible to
`section=did_not_compile`, even though its record's `compile_outcome`
reads `did-not-compile` in full. This cost the file three originally-
drafted clauses (onig's `balanced-parens-rec`, RE2's two "stays empty"
claims), all removed rather than committed as clauses fated to always
read `not-evaluable`. The RE2 half is also the SAME residual gap
`docs/dev/lanes/b42predhyg_report.md` already named for the original
P8 mechanism ("set-subset of an empty target set has no way to
distinguish checked-and-clean from never-checked") -- this lane
reproduces it against real all-engines-refuse data for the first time,
rather than only the argued case.

## What is NOT done

- The file is not merged (per the brief: "Do not merge").
- Neither structural finding is fixed; both are filed as findings for
  the manager/Frank to rule on, per the lane's own docs-only scope.
- No report/store/interpret code was touched.

## Delivery bar

Branch `lane/b51preds`, committed, this report committed, targeted
validation (the direct-API dry-run above, 19/19 clauses; `make
check-interpret` 149/0) with numbers inline. COMPLETE, nothing OWED.
