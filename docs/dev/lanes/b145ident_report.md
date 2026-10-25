# b145ident report -- [B145] dual program hash (v2 + v3), one chooser

Branch lane/b145ident, built on lane/b144spread (schema 1.10 shared, no second bump).
STATE: code done and committed; ALL suite runs OWED (box rule: pcrec heavy suite active).

## Charter-vs-committed checklist

| Charter item | Committed artifact | State |
|---|---|---|
| 1. field `program_sha256_v3`, sha256 type, every pcrec compile row from 1.10 | testees/pcrec/adapter.py (declaration + `pairs["program_sha256_v3"]`), tools/program_identity.py `program_sha256_v3_of_files`, tools/trend_snapshot.py META_KEYS | done; runtime proof OWED (check_identity_chooser part B) |
| 1. X rule | schema/validate.py X46 (two-directional: required with `program_sha256` at >=1.10, forbidden below), record_schema.md X46 row + field row + version row, good example + bad control via schema/examples/gen_example_ident110.py (in `make check-schema`) | done; check_rules 46 rules / 91 controls and check_fields OK, ident110 --check OK (cheap, run) |
| 2. ONE chooser | pcrecbench/identity.py `same_program` (+ `compared_hashes`, `criterion_summary`); callers: nullband.field_identity[_criterion] (-> report.py), tools/trend.py deltas / compile deltas / deny twins | done |
| 2. no raw comparison left | tools/selfcheck.py `check_identity_chooser` guard (regex over pcrecbench/ tools/ testees/ schema/, positive + negative control); dry-run found 0 hits. viewer_export.py and frontpage.py never read the field (nothing to route) | done; run OWED |
| 3. criterion labelled | trend: per-row `identity_crit` column, summary `identity_criterion` = `program_sha256-v2`/`-v3`/`mixed`, header text per comparison; reporter: `criterion v3 ... on N cell(s), v2 on M` clause in the identity-from-records line and the `identity_field` TSV row | done. DECISION to confirm: to keep committed outputs byte-identical, the new column/clause appears ONLY where some comparison used v3 (all-v2 outputs are unchanged, and name `program_sha256`, which is v2 by BD13). So until the first 1.10 record the v2 criterion is implicit in the existing text |
| 3. byte-identical proof | OWED: regenerate reports + trend detached once cleared, `git diff` must be empty |
| 4. docs | decisions.md BD13 amendment (plain-language paragraph first), record_schema.md, tools/CLAUDE.md, reports/trend/CLAUDE.md, pcrecbench/CLAUDE.md, schema/CLAUDE.md, root CLAUDE.md | done |
| 5. chooser checks | check_identity_chooser: 8 cases (the four required + v3-differs-v2-equal control, v2-fallback differs, v2 never meets v3, None), criterion_summary, guard controls; pcrecbench/tests/test_report.py `test_b145_...`; tools/tests/test_trend.py 5 b145 asserts | written, NOT run |
| 5. real-artifact abc check | check_identity_chooser part B (abc at the pin vs build pcrec-6b2dbd3e: changed/v2, identical/v3; adapter compile row carries both == census) | written, OWED (needs builds) |
| 5. validator sabotage | schema/examples/bad/x46-v3-absent-on-110-compile-row.jsonl; validate.py rejects it with [X46] (run, 1 invalid) | done |
| 6. report | this file; check counts OWED |

## Check counts
OWED: make check-harness (+ the new section), check-report, trend tests, make check-schema.
Run so far (seconds, no build): check_rules, check_fields, gen_example_ident110 --check, validate.py on the two new records, chooser one-liner.

## Notes
- program_sha256_v3 on a pre-77 artifact (pcrec-local below the pin) is computed over its text anyway; normalize_v3 is a no-op on scaffold-free text.
- Old snapshots are unaffected (META_KEYS skips absent keys); DIGEST_VERSION unchanged since the digest keeps full engine_metadata.
