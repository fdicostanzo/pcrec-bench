# Lane b148land report -- L3 landed on L1+L2 master

Branch `lane/b148land` (worktree `worktrees/b148land`). Tier: code + checks, no timing, no downloads.

## What changed
- Merge of `lane/b148l3` onto master f135cff2 (L1 + L2). One conflict, `docs/dev/lanes/CLAUDE.md` (both sides were
  list additions; both kept). `bench/unusual/assists/` (L2) untouched.
- (1) Tags: the four va-* members now carry `requires-vars` + `requires-unusual-<member>` (via `req=` in
  `members.py`; the interim `needs-*` tags are gone). L3's `twin_of` dependency is also switched: the callout
  arms (co-luhn/isbn/member x real/pass/twin; co-netstr/-assist/-twin) carry `twin_of-<root>`; `twin_groups()`
  loads clean (4 groups). `gen_patterns.py` re-run, `--check` 0 differences; `patterns.rxt` differs by one comment line.
  cscan-onig / wild-json-validate-onig are variants, deliberately NOT twin_of-tagged (not a pass==twin pair).
- (2) `UNUSUAL_GATE_SKIPS` in `tools/selfcheck.py`, keyed by set id (`UNUSUAL_SET`), consumed by `subbench_dirs(gate)`;
  `check_unusual_gate_skips` self-test (drops exactly unusual, unnamed gate keeps it, every name has a call site, the
  table is exactly the three reported gates); the pre-existing subst self-test adjusted to ignore unusual.

| gate | reason it does not apply to bench/unusual |
|---|---|
| `rxt-export` | cscan is multi-line; an .rxt `pattern` line cannot carry a newline (needs `pattern-esc`) |
| `capability-policy-noop` | the set declares requires-* tags by design (per-pattern gating, design 5.5) |
| `vars-surface` | the va-* members contain `${` by design. NARROWED, not blanket: check_vars_surface still asserts the `${` patterns of unusual are exactly its va-* members and all are `requires-vars` |

No other generic gate was skipped. Self-tests run standalone: all PASS (`check_unusual_gate_skips`, `check_subst_gate_skips`).

## Findings
- `vars` and `unusual-<member>` are declared by NO config's capability block yet, so under fail-closed policy the
  va-* patterns are unsatisfied everywhere until L5/L7 declare them (expected, not a defect).

## make check -- OWED
Command (worktree root `/home/pcrec/projects/pcrec-bench/worktrees/b148land`): `make check`, log
`/var/tmp/pcrecbench/b148land/check.log`, completion line `DONE rc=N` (also file `/var/tmp/pcrecbench/b148land/check.done`).
Counts: OWED. Known load-sensitive red: "a real quick cell on bench/email writes a MEASURED scratch record".
