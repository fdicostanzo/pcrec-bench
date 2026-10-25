# b144spread — report ([B144], rule `v1.10-group`, record schema v1.10)

Lane b144spread, 2026-10-25. Frank's ruling on b140drv F1 (option (a)): a
spread rule across trials for the one-iteration `substitution` regime.
STATUS: code and docs committed; **checks OWED** (the manager holds the box
for a pinned window; no suite, build or generation was run).

## What changed, by file

- `pcrecbench/reduce.py` — `TRIAL_AGREEMENT_RULE = "v1.10-group"`,
  `TRIAL_AGREEMENT_RULE_V14`; `_ns_per_iter_judged(r, rule)` counts a
  `substitution` trial at `iterations >= 1` (others `> 1`);
  `judge_trial_agreement(..., rule=)` stamps the rule it applied.
- `schema/validate.py` — the SECOND, independent implementation
  (`judge_trial_agreement(rows, k, d_min, share_c, rule)`), `ta_rule_for(minor)`;
  X32 now requires `trial_agreement.rule` to be the one the record's own
  `schema_version` names (v1.4-group for 1.4..1.9, v1.10-group from 1.10) and
  recomputes under that text. No shared source with reduce.py (V6).
- `schema/record.schema.json` — `x-record-schema-version` 1.10, `rule` is an
  enum of the two ids, history in `$comment`.
- `pcrecbench/record.py` — `SCHEMA_VERSION = "1.10"` (new records stamp
  `v1.10-group` through the default).
- `pcrecbench/report.py` — the policy line prints the records' OWN rule(s)
  (`trial_agreement.rule`, sorted; both when a query mixes), with one extra
  clause only when `v1.10-group` is present. With no 1.10 record the line is
  byte-identical, so no reporter version bump and no committed report moves;
  `pcrecbench/tests/test_report.py` pins stay valid unchanged (fixtures carry
  `v1.4-group` blocks). Docstring R3 updated.
- `tools/selfcheck.py` — `check_trial_agreement_subst_fixture` (new, called
  after `check_trial_agreement_fixture`): hand-computed 4-row substitution
  group (s1,s4 clean; s2 two 1.6x; s3 one 0.6x => d=2,n=4 disagree), the
  s1+s2 subset (d=1,n=2 agree), the same rows under `short-subject-search`
  (4 `few_timed_trials`), and under `rule=v1.4-group` (unjudged); each
  cross-checked against validate.py's implementation; the record written
  through `store.write` validates, a block claiming `agree` is rejected by X32,
  and `v1.4-group` on a 1.10 record is rejected by X32. `_assemble` now
  re-stamps at `SCHEMA_VERSION` (its callers stamp with the default rule);
  two literal `(v1.4-group` status-sentence expectations became
  `(v1.10-group`.
- `tools/check_subst.py` — four `schema_version == "1.9"` asserts now read
  `record.SCHEMA_VERSION`.
- `schema/examples/gen_example_110.py` (new) + the generated good example
  `subst-example@0.1__...__20261025T120000Z.jsonl` + the sabotage
  `schema/examples/bad/x32-v110-subst-claims-agree.jsonl` (a 1.10 subst record
  whose rows disagree, block claims `agree`; fires X32 only). `--check` added
  to `make check-schema` (Makefile). `gen_example_14.py` stamps
  `rule="v1.4-group"` (output byte-identical, verified with `--check`).
- Docs: `docs/design/gate_shape_v14.md` new §3.7 + §3.3 row + a §8 check row;
  `docs/design/record_schema.md` §4.1 history row 1.10 and the "1.9 -> 1.10"
  rule-revision paragraph, §6.9 sentence, the `trial_agreement.rule` field row,
  X32 row (versioned); CLAUDE.md files: root (schema v1.10), `schema/`,
  `schema/examples/`, `schema/examples/bad/`, `docs/design/`, `pcrecbench/`.
  The constants (k=1.5, d_min=2, share_c=3, N>=5 odd) are unchanged; the text
  states they were measured on in-process loops, not whole-pass walls, and the
  first substitution window's spread is their check.

## Run in-lane (light, under the box rule)

`schema/check_fields.py` OK (setup 159 fields); `schema/check_rules.py` OK
(45 rules, 90 controls); `gen_example_14.py --check` and
`gen_example_110.py --check` OK; `validate.py` accepts the new 1.10 example and
both 1.9 subst examples, rejects the sabotage for X32 (3 X32 problems, no other
rule); the two fixture functions `check_trial_agreement_subst_fixture` and
`check_trial_agreement_fixture` called directly: all PASS (0.6 s).

## Charter vs committed

| promise | artifact |
|---|---|
| rule id `v1.10-group`, schema v1.10, only change = subst at iterations>=1 | reduce.py, validate.py, gate_shape_v14.md 3.7 |
| older records judged by v1.4-group forever (X32 versioned); new records stamped | `ta_rule_for`, `SCHEMA_VERSION` |
| both implementations changed identically, no shared source | reduce.py / validate.py |
| hand-computed fixture, subst judged / non-subst `few_timed_trials`, both agree in check-harness | `check_trial_agreement_subst_fixture` (in-lane run PASS; check-harness run OWED) |
| bad sabotage rejected for X32 | `bad/x32-v110-subst-claims-agree.jsonl` (verified by validate.py; check-schema OWED) |
| design text, constants caveat | gate_shape_v14.md 3.7, record_schema.md 4.1 |
| reporter policy line prints record's own rule + pinning tests | report.py (tests unchanged: single-rule output byte-identical) |
| CLAUDE.md for touched dirs, root v1.10 | done |
| check counts | OWED |

## OWED (manager, after the window)

1. `make check-schema` (expect +1 good example, +1 sabotage, +1 `--check` line).
2. `make check` (check-harness gains 15 PASS lines from the new fixture; the
   quick-cell check is the known load flake). Then `check-report` should be
   unchanged.
3. Not done, by design: committed reports under `reports/` still print
   `rule v1.4-group` (correct for their records); no store record is
   re-stamped. The first 1.10 substitution record is the first to print
   `v1.10-group`.
4. Watch item: the `docs/methodology.md` / frontpage line "Trial-agreement rule
   in these records: v1.4-group" is generated by `tools/frontpage.py` from the
   store and was not touched; check it when the first 1.10 records land.
