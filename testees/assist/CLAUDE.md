# testees/assist/ -- the ASSISTED configs and the assist RUNNER ([B148] b148aw)

Design: docs/design/unusual_set_v1.md 5 (the budget, the identity token, the
capability declaration) and 7.1-7.4 (the tokens, the record). The authoring
loop: bench/unusual/assists/AUTHORS.md; build/count/self-test:
pcrecbench/assists.py.

An assisted config is its BASE config (same engine adapter, library and
version) plus one assist per member the engine lacks. Each assist is a file,
bench/unusual/assists/<member>/<engine>/assist.<ext>, recorded in
assists.tsv. Ids: `<base>-assist-v01`. Each one's `config_extra` is the
base's plus the token `assist-v01`, appended LAST. All of them are
`unusual_only`.

| file | role |
|---|---|
| `adapter.py` | `Adapter` (`name = "assist"`). `describe` = the base block + `assist-v01` + `testee.assist`, built from the ASSISTED ledger rows, each RE-COUNTED (a ledger the counter disagrees with is refused by name; fence drift too) + `ASSIST_DECL` + `callees.CALLOUT_DECL`. `compile` builds an ASSISTED member's driver (`assists.build`; for callouts also the counting twin, for the fire pass) and times `ub_setup` as the base's first compile phase. Every other pattern goes to the BASE adapter, with its handle tagged `_assist_base` so `measure`/`fire_handle`/`mem_method` route back to the base. `pattern_scope` = this engine's assisted members, their `-twin` arms and the floor. `capability_grants` = `unusual-<member>` per ASSISTED row. `declaration_ref_for` gives a NOT-CAPABLE row's `<ledger ref> tokens=N budget=300`. `$PCRECBENCH_ASSISTS_DIR` forces the scratch tier. |
| `configs.toml` | the five configs: `pcre2-jit`, `onig-default`, `re2-default`, `rust-default`, `vectorscan-block-som` + `-assist-v01` |
| `ub_assist.h` | THE C ABI an assist implements: `ub_setup`, `ub_find` (recursion/callouts/netstr), `ub_vars` + `ub_reset` (vars), `ub_span`, `ub_var`, `UB_N`/`UB_M`/`UB_R`, negative = an engine give-up. The runner provides `ub_pred` (callouts: the member's SHARED callee, via callees.o and `--callees`), `ub_lookup`, `ub_fail`, `ub_main`. |
| `ub_runner.c` | the driver protocol around one assist: argv, the compile lines (setup timed), `--mode search` (+ `--find-all`), `--mode calls` (3-column lists, or 4-column for VARS), the subject timeout, `--skip`. `--prime`/`--utf8`/`--deep`/`--mem-pass`/`--anchor-explicit` are refused BY NAME. Compiled twice: `-DUB_CALLOUTS` (with `ub_bind.o` and `ub_pred`) and without. |
| `ub_timed.c` / `ub_timed.h` | the TIMED loops in a translation unit of their own (BD16), calling the assist through function pointers: `ub_timed_search`, `ub_timed_calls`, `ub_timed_vcalls` (resets the vars cache after each replay's clock stops). The object is built once (`build/assist/runner-<key>/`) and linked unchanged into every assist driver. |
| `ub_defaults.c` | the default `ub_find`/`ub_vars` (they abort by name) and a no-op `ub_reset`, compiled into `libub_defaults.a` and linked AFTER the assist, so an assist defines only its own family's functions. |
| `rust/Cargo.toml.in`, `rust/Cargo.lock` | the per-build staticlib crate for a Rust assist (edition 2021, `regex` = the same 1.13.1 lock as testees/rust), built `--offline --locked`, linked with gcc using `--print native-static-libs`. |

Owed (not built here): the 6.4 high-water pass for an assisted row (the runner refuses `--mem-pass`; `mem_method` is None), and the deep arm for an assisted config.
