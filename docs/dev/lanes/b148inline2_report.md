# Lane b148inline2 -- the INLINE pcrec callout arm, part 2 of 2 (2026-11-01)

Branch `lane/b148inline2`, worktree `worktrees/b148inline2`, off master a6b6660d. Sonnet writer.
Tier: code + checks, **written, nothing run that needs a build** (box held by window `b149w2`).
Run here: `py_compile` of every touched module, `python3 -m pcrecbench testees`, `gen_patterns.py
--check` x2 (pure Python), and one in-process script exercising `inline_route` /
`inline_argv_tail` / `inline_user_source` / `validate.derive_testee_id` against the committed files.
No pcrec exec, no C compile, no driver, no `make check*`.
Macro-shim form only (the single-callees.c form stays PARKED, O-114).

## 1. Charter vs committed (b148inline_report.md section 4 items 1-6, section 5 items 1-5)

| item | state | artifact |
|---|---|---|
| 4.1 `pcrec-auto-inline` config, `callout_spelling = "inline"` | DONE | `testees/pcrec/configs.toml` (flags `--features all --allow-code=c`, `unusual_only`) |
| 4.1 `pcrec-vm-inline` sibling | DONE (cheap) | same file (`--engine=vm`) |
| 4.1 new LAST `compose_config_extra` token `inline` | DONE | `adapter.py` describe(): 10th part, after `lim-`; token only when `callout_spelling == "inline"` |
| 4.1 every pre-existing testee_id provably UNCHANGED | WRITTEN, UNRUN | selfcheck `check_encoding_axis` arm 1b: new `elif callout_spelling == inline` branch composes `frozen + inline`; every config without the key still falls to the last arm, held to the FROZEN four-part renderer. The key defaults to absent, so the part is `None` and `compose_config_extra` drops it (by construction). Arm 1c (committed records re-derive) is untouched. |
| 4.1 print and freeze the real new id | PARTIAL, see 2 | `pcrecbench testees` does not print ids and `describe()` needs the pinned binary (pin.sh would BUILD from the worktree). Derived through `schema/validate.derive_testee_id`; frozen by `check_inline_pcrec` section "ids". |
| 4.2 adapter route `--allow-code=c --include-block FRAG:LINE ENTRY` from blocks.tsv | DONE | `adapter.py`: `inline_rows`, `inline_route`, `inline_argv_tail`, branch in `_compile_one`; fragment digest recomputed vs blocks.tsv (stale table = AdapterError). Twin / `-nofn` / assisted arms and non-callout patterns keep `--pattern`. |
| 4.3 no binding unit | DONE | `if inl:` branch: `bind_syms` non-empty on an inline artifact is an AdapterError; no `callout_binding.c`. |
| 4.3 `inline_user.c` for `ub_inline_user` (member arm) | DONE | `inline_user_source()`: `void *ub_inline_user` + constructor `ub_member_new(<abs users.tsv>)`, linked with `callees.o` (`_co.ensure()`); only when blocks.tsv `member_arg != "-"`. |
| 4.4 metadata `callout_binding = inline` via RX_CODE_LANGS | DONE | `TEXT_STAMPS["code_langs"]`; METADATA_DECL `code_langs` + `callout_binding` enum gains `inline`; the compile errors unless `code_langs == "c"` and `callout_bindings` empty. |
| 4.4 `sha256` declarations | DONE | `inline_entry_sha256`, `inline_fragment_sha256` declared (type sha256, pattern scope) in the pcrec `unusual_metadata_decl`, set on the compile row. |
| 4.5 no `callout_fires` on inline rows, stated | DONE | stated in the `callout_binding`, `inline_*_sha256` declarations, configs.toml comment, testees/pcrec/CLAUDE.md; mechanism: `count_gargv`/`count_lib` stay None so `fire_handle` returns None. No `callees_sha256` either (asserted by the check). |
| 4.6 CLAUDE.md files | DONE | testees/pcrec, tools, bench/unusual, bench/unusual/inline, docs/dev/lanes |
| 5 (1) compile the 14 blocks, rc 0 + 3 stamps | WRITTEN, UNRUN | `tools/check_inline_pcrec.py` "compile" (auto and vm: 28 pcrec execs) |
| 5 (2) three refusal controls through pcrec + positive control | WRITTEN, UNRUN | "refusal" arms (stale pin, dropped sha256, no grant) |
| 5 (3) gcc AND clang, user-region warnings | WRITTEN, UNRUN | "cc axis" arms: -Wall -Wextra, no diagnostic naming a `.rxt` |
| 5 (4) answers == separate-TU arm, first-candidate-fails | WRITTEN, UNRUN | "answers" / "mapping" arms, auto and vm, real + pass arms of luhn/isbn/member + real netstr |
| 5 (5) emit-size / program-identity census | WRITTEN, UNRUN | "census": table printed; inline != separate-TU program on every real arm |
| check chain | DONE, NOT RUN | `docs/dev/lanes/b148inline2_check.sh` (symlinks `build/pcrec-*` from the main tree, runs `check_unusual.py --only inline inline-pcrec`, then `make -k check`; logs `/var/tmp/pcrecbench/b148inline2win/`, `*.rc`, always exit 0) |

Not in the brief but forced by the testees existing (found by grep for `pcrec-auto-deep`):
`bench/capability/gen_patterns.py` `EXCLUDED_TESTEES` (the two inline ids, `unusual_only`),
`bench/unusual/gen_patterns.py` `INLINE_ARMS` (sibling capability block copied; `patterns.rxt`
regenerated, `--check` 0 differences), and the b149 selfcheck "never passes `--allow-code`" scan, which
would have failed on the adapter's own grant check (one line marked `INLINE_GRANT_OK` is exempted, plus a
new config-level iff: grant <=> `callout_spelling = inline`).

## 2. Frozen new testee ids

Derived, not read from `describe()` (see above), with `engine_version` assumed to be the 9-char pin as
at the last re-pin:

* `pcrec_cb32eda28_auto-caps-simdna_inline`  (`config_extra` = `inline`)
* `pcrec_cb32eda28_vm-caps-simdna_inline`

Note the separator: `config_extra` joins with `_` after the `simd` slug (existing ids look like
`pcrec_d34c9131_auto-caps-simdna_noclsfold`), so the b148inline_report's guess
`...-simdna-inline` was wrong. `check_inline_pcrec` "ids" asserts `get == "<mode>-caps-simdna_inline"`
from the real `describe()` and prints the full id; if the pin length differs, only the prefix moves.

## 3. UNVERIFIED until the chain runs

* **Everything that executes**: no pcrec has compiled any block; the 14 compiles, the three stamps, the
  refusal wording, the gcc/clang results, the answers and the census are all predictions.
* `describe()` of the two new configs (the `--allow-code` pair in `runtime_options`, the id) and the
  frozen-renderer arm with the new branch.
* The METADATA/decl plumbing: X15 (every recorded key declared) is satisfied only if
  `unusual_metadata_decl` is what the record's declaration is built from for the pcrec adapter. `code_langs`
  is in the global `METADATA_DECL`, so it is declared for EVERY pcrec testee although stamped only on inline
  rows; I did not check that some selfcheck gate (e.g. a declared-key-must-appear census) objects to a
  declaration that is absent on all non-inline rows.
* The text stamp regex for an EMPTY `RX_CALLOUT_BINDINGS ""`: `TEXT_STAMP_RES` accepts `"([^"]*)"`, so
  empty is read as `""` (falsy, no unit linked). If pcrec omits the macro instead, the result is the same.
  `check_inline_pcrec` reads it with its own regex that treats absent and `""` alike only for the third stamp
  (`CALLOUT_BINDINGS`), not for `CODE_LANGS` / `CALLOUTS`.
* The `-Wall -Wextra` run in section 3 of the check compiles the artifact `.c` alone (`-c`, `-I` its dir);
  the shim and its `#include` shape are not used, so a diagnostic only the shim TU would show is out of
  reach. The `#line`-to-`.rxt` attribution assumes pcrec's `#line` names the fragment path.
* `ub_member_new` linkage: `callees.o` is built with `-fPIC` (callees.py FLAGS), so linking it into the
  `.so` is expected to work, but the member inline arm has never loaded.
* The capability matrix: `patterns.rxt` of bench/unusual now lists the two inline testees on the roster.
  I did not run the cell-admission matrix; the inline testees get the sibling's block (callouts included),
  so every cell admitted to `pcrec-auto` is admitted to them. vars members are NOT declared for them
  (`VARS_NATIVE` untouched), which makes those cells not-capable for the inline testees -- intended.

## 4. What I had to guess

1. **Form name mapping**: blocks.tsv says `plain`/`whole`; the harness says `plain`/`whole-subject`
   (`INLINE_FORM`). Pattern id == blocks.tsv `arm` (e.g. `co-luhn-pass`); taken from the file names and the
   existing check_callouts `_co(sb, pid)` usage.
2. **Assisted / `-nofn` / twin arms on an inline testee** run the ordinary route (separate-TU callee for an
   assisted pcrec pattern, `--pattern` for twins). The alternative -- refusing or skipping them -- would
   change the cells an inline run produces; I kept them so the inline testee covers the full pattern set
   and the harness `unusual_only` rule is the only filter. Worth a manager ruling.
3. **`callout_spec`** on an inline row is still the set's table text (via `_co.compile_metadata(co, None)`),
   although no binding spec is bound. Kept so reports group inline rows with their arms.
4. The id's `engine_version` slug (9 chars at cb32eda28, as the prior ids at 8-9 chars suggest).
5. `unusual_only = true` on both testees (the brief said nothing); without it they would run on every set,
   where the route is inert and the grant pointless.
6. Check design: `check_inline_pcrec` section 4 builds drivers via `ad.prepare` (compiles the shared C
   driver) and uses `ad.measure(..., "search_short", ...)` copied from check_callouts; attribute names on
   `CompileResult` (`engine_metadata`) are taken from the constructor keywords.

## 5. Owed / trigger

* Run `docs/dev/lanes/b148inline2_check.sh` once the box is free (manager queues Monday): expect the first
  run to need fixes (this is the first execution of all of it). Logs `/var/tmp/pcrecbench/b148inline2win/`
  (`chain.log` marker `CHAIN_DONE`, `inline.rc`, `check.rc`).
* After a green chain: merge, then a scratch `quick` cell of `pcrec-auto-inline` vs `pcrec-auto` on
  `co-luhn` for the first look at the timing delta, and the reporter/interpreter treatment of
  `callout_binding = inline` (not touched: reporter has no clause for it).
* Not built: the single-callees.c form (parked, O-114); a counting twin segment (needs the
  `--code-header` fix).

## 6. Fix (lane b148inline2fix, 2026-11-01): the three reds of the check chain

Chain logs: `/var/tmp/pcrecbench/b148inline2win/{inline,check}.log`. Re-run green afterwards:
`check_unusual.py --only inline-pcrec w1fix` = 36 passed, 0 failed.

1. **`answers: pcrec-{auto,vm}-inline == pcrec-{auto,vm}` ("differ: []; real-vs-twin 0")**.
   Cause: the short-subject tree (`bench/unusual/subjects/`, generated and gitignored) did not exist when the
   section ran: `--only inline-pcrec` does not run `check_set.py`, which is what generates it. The driver
   answers a missing subject path `crashed` (measured: five `/nonexistent` subjects -> five `crashed`), on
   BOTH arms, so the comparison saw two identical all-`crashed` maps: no differences, and real-vs-twin 0
   (the control correctly refused to pass). Not a wrong subject list, form, row key or arm filter. Fix
   (`tools/check_inline_pcrec.py`): the section runs `gen_subjects.py` when any short file is absent and
   then fails BY NAME if one is still missing; `answers()` raises on any row that is not `match`/`nomatch`
   (or a short row count), so a crashed pair can never compare equal again; the pass line now prints the
   rows compared. **Rows compared: 1,127 per testee pair** (161 short subjects x 7 arms: luhn, isbn,
   member real + pass, netstr real; the inline side; the separate-TU side is the same count); real != twin
   on 26 subjects (8 luhn + 2 isbn + 3 member + 13 netstr). No check was loosened.
2. **w1fix "live matrix drifted from AFTER"**. Cause: `_live()` enumerates every testee in the capability
   matrix, which now includes `pcrec-{auto,vm}-inline`, five rows (cscan, cscan-onig, wild-sexp-balanced,
   wild-json-validate, wild-json-validate-onig) x `pcrec-auto-inline` among the 5 differing cells reported.
   The matrix is a frozen BEFORE/AFTER over b148w1fix's own roster (the 500 cells = 20 patterns x 25
   testees in the committed TSVs), not meant to cover every testee. Fix (`tools/check_w1fix.py`): the live
   side is cut to the testees the committed AFTER names; the AFTER file is unchanged. Still 500 cells, 12
   flips, 12 renames, 476 identical.
The brief's "three reds" are 1 (auto and vm, two rows) and 2. `make check*` was not run in this lane; OWED: the manager's `make check` re-run.
