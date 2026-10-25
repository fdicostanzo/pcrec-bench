# kb36rep report -- KB-36, the dropped-triple header (reporter v28)

Lane `kb36rep`, branch `lane/kb36rep`, 2026-10-25. Status: code committed; the
checks are OWED to the manager (box rule: no `make check*`, no store load).

## What changed
- `pcrecbench/report.py`: `REPORTER_VERSION` v27 -> v28; `ReportData.dropped_triples`
  ({(sb, pattern, subject, regime): rows}) filled in `build_report` from every
  included record's rows via `reduce._is_no_expectation_row` (KB-27's predicate);
  `_dropped_triples_header_value`; TSV header key `dropped_triples:` (after
  `null_band`) and a markdown bullet.
- Value: `2 triples, 22 rows (by name: email-nested-plus x t-evil-match-60k, email-nested-plus x t-evil-nearmiss-16k)`
  (shape; the row count is over all included records). No `; ` inside.
- Derivation source: the records' own `no expectation exists` rows, NOT `bench/`
  or a sidecar: the reporter never reads `bench/`, and the dropped list was
  stderr-only at derivation time (`pcrecbench/expectations.py`). No pcrec-specific
  or set-specific shape (R-BENCH-4). Limitation (in the docstring): a triple every
  included testee gave up on shows no such row. Checked by hand on the 00c97769
  capability@0.2 pcrec-auto record: exactly the 2 triples, 5 rows each.
- Choice: the key is OMITTED when there are none (not `0`), so every report
  without a dropped triple is byte-identical except the version line.
- `pcrecbench/interpret.py`: `HEADER_KEYS` + `CONDITIONAL_HEADER_KEYS` gain the key;
  verified `header_keys_from_source() == HEADER_KEYS`. `check-interpret`'s header
  check treats it as optional like `null_band`; the goldens are derived from
  committed v27 reports, which are untouched, so they cannot move. Not run.
- `pcrecbench/tests/test_report.py`: new `test_kb36_dropped_triples_header_key`
  (positive: 2 triples, 8 rows over two records, sorted names, placement after
  `floor_pattern`, markdown bullet; control: a set with none carries neither);
  version assertions v27 -> v28. Ran this test and
  `test_floor_pattern_header_key_p1` directly: pass. The whole file loads the
  real store in places, so it was NOT run.
- Docs: `known_issues.md` KB-36 FIXED; `pcrecbench/CLAUDE.md`; `interpreter_v1.md` 2.1 key table.

## Regeneration list (manager, detached)
The five capability@0.2 groups, each of .md/.tsv/.subject-grain.md/.subject-grain.tsv/.matrix.tsv (+ `make check-interpret`'s sidecar freshness, then `/pcrec-bench-interpret` sidecars):
`2026-10-08-...-first-255bcdd8`, `2026-10-10-...-revend-7388f1c0`, `2026-10-11-...-landing-b8337c33`, `2026-10-13-...-handoff-6b2dbd3e`, `2026-10-13-...-handoff5-6b2dbd3e`.
Every other committed report is unchanged by the code except its version line (precedent: a bump on rendering-code change without regenerating, as v26/v27); no other committed non-matrix TSV mentions a no-expectation row.

## Charter vs committed
| Promise | State |
|---|---|
| header key from derivation output, no hard-coding, no pcrec shapes | done (record rows) |
| every set; none -> omit or 0, say which | omit; byte-identical |
| version bump | v28 |
| interpreter known-key list; check-interpret passes | key added, derivation equality verified; `make check-interpret` OWED (manager) |
| regeneration list | above; regeneration OWED (manager) |
| test with control | done, ran 2 tests green |
| KB-36 FIXED, CLAUDE.md files | done |
| `make check`, check-report | OWED to manager |
