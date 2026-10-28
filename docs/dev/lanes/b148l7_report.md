# Lane b148l7 report -- [B148] L7: the caller-variables members

Branch `lane/b148l7` (worktree `worktrees/b148l7`), base master 05560ed9. Tier: code + set construction + checks +
scratch smokes (scratch store under `/var/tmp/pcrecbench/b148l7/` and `build/check-vars/`; NO timing, NOTHING in
`store/`). ~/pcrec read-only (vars.md, variables_pattern.md read; `build/pcrec-614d45eb3` used). No downloads.
Callouts untouched.

## 1. Checklist (charter -> committed artifact)

| item (source) | state | where |
|---|---|---|
| value streams, DETERMINISTIC, stream length fixed across d4/d64/d4096, miss count printed (note 3.3, P13, C6) | DONE: 16,384 calls on all three rungs; miss count = distinct resolved patterns, in `values/streams.tsv`, the manifest description, NOTES s8 | `gen_vars.py`, `gen_streams.py`, `values/` |
| other members' streams (route, term, term-bang) | DONE: route-zipf, term-zipf (shared by va-term and va-term-bang) | same |
| expectations: libpcre2 with the value interpolated + ESCAPED per vars semantics (note 8, C6) | DONE: `gen_vars.resolve` (vars.md 2/5 in Python) -> libpcre2 10.46; second method Python `re` over `re.escape`; every call agrees or the derivation aborts | `gen_expectations.py` (`stream_rows`, `--streams-only`) |
| default words literal + escaped; `${!name}`; nested chain DROPPED (Q-C open) | DONE: hand-table cases; `parse` REFUSES `${a:-${b}}` (control) | `gen_vars.py`, `check_vars.py` |
| pcrec NATIVE vars path: `rx_var`, rx_ctx vars members, PCREC_ERR_UNSET_VAR as a named outcome | DONE: the search entries' trailing `vars, nvars` pair (vars.md 4); -8 -> token `r` (a REFUSED call, not a give-up); old `pb_search` on a var-bearing artifact answers -8 (control); a vars list on a var-free artifact refused by name | `shim.c`, `driver.c`, `timed_calls_vars.c/.h`, `testees/common/vars_io.h` |
| pcrec-auto/vm run them natively in `--mode calls` (the regime the note gives them: `call-stream`) | DONE: `pcrec-auto`, `pcrec-vm-in`, `pcrec-vm-deep` through `run_cell` (check), plus `-nocaps` and `-vm`/`-vm-deep` in dev runs | `tools/check_vars.py` |
| declare `vars` + `unusual-<member>` on supporting pcrec configs, fail-closed | DONE: six configs (`pcrec-auto/-nocaps/-vm/-vm-in` + the two `deep` arms); 8 others checked closed (libpcre2 x2, onig, re2, rust, vectorscan-som, pcrec-auto-utf8, pcrec-dfa) | `gen_patterns.py` (`VARS_NATIVE`), `patterns.rxt` |
| PROBLEM STATEMENT + sample inputs/outputs for each L6 author, engine-neutral, no pcrec internals | DONE: `assists/problems/vars.md` + `vars-samples.tsv` (80 cases, 20 per member, all of m/n/r per member, disjoint from the held-out streams); check asserts no "pcrec"/`rx_var` in the text | `bench/unusual/assists/problems/`, `gen_vars_samples.py` |
| wire checks into check-harness | DONE: `check_vars_set()` after `check_calls_set()` | `tools/selfcheck.py`, `tools/check_vars.py` |
| ASSISTED engines' code | NOT MINE (L6) | -- |

## 2. The call, and a deviation from the note's text

The note's 7.3 says `--bindings FILE`; as built the bindings table is a FOURTH column of the `--list` line
(`id subject calls bindings`), because a list holds several streams (same reason L4 made `--calls` a per-subject
third column). Its value column is `hex | UNSET | EMPTY` (a zero-length hex field is not a reliable TSV cell). A vars
call is ONE LINE of the subject matched ALONE (so the members' own `^` means the line start; offsets are
line-relative). Amended in the note's 7.3 and in `adapters.py`'s protocol docstring. The harness change is two small
edits (`Subject.bindings_path`, `write_list`'s 4th column); every non-vars stream is byte-for-byte as before.

## 3. Stream table (`values/streams.tsv`; `gen_streams.py` also puts them in `manifest_streams.tsv`)

| stream | members | calls | line bytes | bindings | distinct resolved (= misses) | refused | reuse |
|---|---|---|---|---|---|---|---|
| tenant-d4 | va-tenant | 16,384 | 516,826 | 4 | 4 | 0 | round-robin |
| tenant-d64 | va-tenant | 16,384 | 517,577 | 64 | 64 | 0 | round-robin |
| tenant-d4096 | va-tenant | 16,384 | 533,320 | 4,096 | 4,096 | 0 | round-robin |
| route-zipf | va-route | 4,096 | 81,847 | 108 | 40 | 983 | zipf-s1.1 |
| term-zipf | va-term, va-term-bang | 4,096 | 136,485 | 49 | 47 | 201 | zipf-s1.1 |

Oracle tokens (matched / nomatch / refused): d4 11,818/4,566/0; d64 11,790/4,594/0; d4096 11,706/4,678/0; route
1,064/2,049/983; term 2,137/1,758/201 (both spellings identical hash). `expectations_stream.tsv` now has 10 rows
(4 F1 + 6 vars). Subject trees (`streams/`, `calls/`) are gitignored as before; `values/*.tsv` (115 KB) are
COMMITTED and hashed. `manifest_streams.tsv` column `local_refusals` carries the host-refused count for a vars stream.

## 4. Native path: result (scratch, dev runs + the check)

pcrec answered every (stream, member) pair `matched-as-expected` against the libpcre2 oracle -- NUL values, EMPTY, UNSET
refusals, metacharacters -- on `pcrec-auto`, `-nocaps`, `-vm`, `-vm-in` (the `_in` entry), `-vm-deep`; 0 give-ups.
The unescaped-interpolation control changes 5,014 of 16,384 tenant-d64 answers and 1,266 of 4,096 term answers (or
fails to compile), so the as-itself rule is decided by the expectations, not a no-op.

Edits to shared/pcrec files (all small, as asked): `testees/pcrec/shim.c` (+`PB_NOVARS` in the two existing wrappers,
code identical for a var-free artifact; four new exports at the END of the file), `testees/pcrec/driver.c`
(`run_calls_vars`, 4 dlsyms, one dispatch line), `testees/pcrec/adapter.py` (the extra source in two places),
`tools/selfcheck.py` (the hand-built driver's source list + `check_vars_set`), `gen_patterns.py` (additive block;
L5 will touch the same function -- expect a trivial merge), `subbench.py`/`driverrun.py` (the 4th column).
`testees/*/timed_calls.*`, `calls_io.h` and every callee file are untouched. BD16: `timed.c`/`timed_calls.c` untouched;
the new replay is its own translation unit.

## 5. Checks

- `tools/check_vars.py`: 23/23 PASS (~47 s): resolver vs 25 hand cases + the nested-chain control; ladder fixed at
  16,384 and misses 4/64/4096; `values/streams.tsv` and manifest rows equal the recomputation; route memo key = resolved
  pattern (108 -> 40); `gen_streams.py --check`, `gen_expectations.py --streams-only --check`, `gen_vars_samples.py
  --check`; escaping controls (2); sample shape + held-out disjointness + problem-statement hygiene; native path x3
  configs (6 rows each); wrong-hash control; refused-is-not-a-give-up; old `pb_search` control; var-free refusal by
  name; capability closed/open.
- `bench/unusual/check_set.py`: 15/16; the one FAIL is `fetch_sqlite.py refuses by name`, PRE-EXISTING (the table is now
  pinned and the fetch ran after L3 wrote that check; not touched by this lane). Two of its assertions were updated
  (stream-expectation rows 4 -> 10; the vars-rows assertion reworded).
- `gen_patterns.py --check`: 25 files, 0 differences.
- FULL `make check`: OWED (launched detached at hand-back, see 7).

## 6. Findings

1. `\b` around a metacharacter-ended term needs a word byte beside it: ~all of the hand-picked sample terms like
   `c++`, `(foo)` first answered `n`. The term stream now places word neighbours per term (`_fit`), so metacharacter
   terms MATCH most of the time and near-misses are boundary failures by design.
2. pcrec resolves names by `strlen`+`memcmp` against the caller array on EVERY call (rx_vars_resolve): its per-call cost
   grows with the number of mentioned variables (va-route: 3), not with the distinct-value count. D-5 predicts the
   tenant ladder flat for pcrec.
3. `pb_err_name(-8)` returns no name through the shim's table (the stream line's `first_limit` is `-` for a pcrec
   give-up of -8, `first_code` -8 is there): it is only reachable via the non-vars path (a var-bearing artifact called
   without variables) -- harmless here, noted for the L8 reporter.
4. 983/4,096 route-zipf calls (24%) are refused: zipf puts weight on the UNSET `res` bindings; the share is declared, not
   tuned.
5. check_set.py's `fetch_sqlite` FAIL (above) is the manager's to fix or retire.

## 7. OWED

- Full `make check` at the branch tip: command `make check` from `worktrees/b148l7`, log
  `/var/tmp/pcrecbench/b148l7/makecheck.log`, completion line `DONE rc=N`.
- The full `gen_expectations.py --check` (minutes; part of the generic gate inside `make check`).
- The `--grain stream` reporter view and the miss count's PRINTING in a report (L8): the numbers are in
  `values/streams.tsv`; nothing in the reporter reads them yet.
- Assisted-engine drivers' vars support (they refuse a vars binding row by name today; `vars_io.h` is the shared loader
  for L6).
