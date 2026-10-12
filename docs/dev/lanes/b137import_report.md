# b137import report (lane b137import, 2026-10-12, Sonnet)

Branch lane/b137import. Charter: team-lead brief; O-90 (multi-host design), O-98 Q7.

## Charter vs committed

| # | promise | artifact |
|---|---|---|
| 1 | `pcrecbench import <foreign-store> [--store]`: validate, refuse by name with nothing written (scratch tier; unknown / inconsistent machine; set version or manifest sha256 differing from the committed set; differing duplicate record_id; identical duplicate = no-op), canonical layout, re-index | `pcrecbench/importer.py`, `__main__.py` (`import`, exit 5 on refusal), `store.validate_file_batch`, `subbench.content_hash_of` (hash a set without loading it, so no engine binary is needed) |
| 1b | a documented way to register `dev-7700x` | `python3 -m pcrecbench machines register --machine-id dev-7700x --hostname H --cpu-model <canonical slug> --cores N` (hostname/cpu_model/cores must be the values in the foreign records), or `import --register-machine dev-7700x` which adopts the foreign store's own machines.tsv row, committed only if the whole import passes. `env.register_machine`; store/CLAUDE.md |
| 2 | `environment.cpu_isa`, schema v1.7 -> v1.8, field table, validator rule, examples + bad example | `schema/record.schema.json` (1.8), `record_schema.md` (1.8 row, field row, X35, 6.11), `validate.py` X35 (present only at >= 1.8; sorted), good example `boolgrain-example...20261012T120000Z`, two bad `x35-*`; `env.py` `parse_cpu_isa`/`cpu_isa()` (allowlist + every avx512*; x86 `flags`, arm64 `Features`; omitted when absent); `record.SCHEMA_VERSION` 1.8. Old records valid unchanged. |
| 3 | per-host readers | see table below |
| 4 | tests in `make check` | `tools/selfcheck.py` `check_b137_import` (17 rows, wired into `main()`): synthetic foreign store under `build/b137-import/` (smallest committed record re-stamped as `selfcheck-host2`); clean import + registration + index + no-op re-import; 8 refusals by name each with a byte-identical store snapshot; two-host report refused / per-`--machine` reports / viewer refused; cpu_isa parse. check-schema counts 7 accepted / 76 rejected. |
| 5 | CLAUDE.md rows + this report | pcrecbench/, schema/, schema/examples/, schema/examples/bad/, store/, root CLAUDE.md |

## Readers with a second machine_id (item 3)

| reader | before | now |
|---|---|---|
| `pcrecbench/report.py` | dedup is per (set, testee, machine) but the kept records of two hosts then fed ONE cell (pooled) | `build_report` returns an error naming `--machine` when the selected records span >1 machine_id (localized: one block after `valid = dedup_valid`). `--machine` already filtered. Cross-host RATIO view: NOT built (O-90 says a ratio between two per-host reports; follow-up). |
| `reduce.py` | no machine logic; callers decide | unchanged (reached only through report/quick) |
| `tools/trend.py` | filters on `cfg["machine"]` (default budu-ryzen1600), other hosts `excluded-machine` | already splits; unchanged |
| `tools/frontpage.py` | picked newest by timestamp across hosts | refuses (SystemExit) when the index holds >1 machine_id; no `--machine` yet |
| `tools/viewer_export.py` | keys carry machine_id but the viewer pools testee columns | new `--machine`; refuses without it when >1 host |
| `interpret.py` | reads the report's `machines:` header and index tuples | unchanged; a per-host report names its one machine |

Not tested: the front-page refusal (code path is a 4-line guard; frontpage.py needs the full committed store layout). `quick` (scratch tier) is single-host by construction.

## Validation run

- `make check-schema`: 7 accepted, 76 rejected for the intended rule, 0 wrong; check_fields OK, check_rules OK (X35 has controls).
- `check_b137_import` alone: 17/17 PASS. `check_run_smoke` + `check_v11_fields`: PASS (a real harness record validates at 1.8 carrying cpu_isa).
- OWED to the manager: full `make check` (check-harness is >20 min; check-report result below if recorded; check-interpret golden/fixtures use a FROZEN snapshot and were not touched). Merge note: report.py touch is one block at "valid = dedup_valid"; no testees/ or adapter file touched.
