# Lane b148aw -- the assist wiring for [B148] (before L6)

Branch `lane/b148aw`. Tier: code, checks and scratch smokes only. No timing
window ran, nothing was written to store/, and ~/pcrec was only read. The
design is docs/design/unusual_set_v1.md 5 and 7.1-7.4.

## What was built

| brief item | where | status |
|---|---|---|
| 1. Templates, one per engine | `bench/unusual/assists/templates/{pcre2.c,onig.c,vectorscan.c,re2.cc,rust.rs}` | done |
| 1. The runner speaks `--mode calls` | `testees/assist/ub_runner.c` (search, find-all, calls, VARS 4-column calls) | done |
| 1. BD16: no existing timed code changed | see "BD16 proof" below | proved |
| 1. Fences pass tokcount; the empty assist counts near zero | 16/16 template x family: 6 tokens (C, C++), 7 (Rust), nothing smuggled | done |
| 2. Assisted configs `<engine>-assist-v01`, `unusual_only` | `testees/assist/configs.toml` + `adapter.py` (5 configs) | done |
| 2. `testee.assist` recorded | `describe()`, built from the re-counted ASSISTED ledger rows; X50 accepts it | done |
| 2. Runs call-stream, search_short, throughput | scratch `run_cell` on all 5 configs, validator-accepted | done |
| 2. A NOT-CAPABLE row becomes a declared refusal | `declaration_ref_for` -> `unsupported-by-declaration`, ref `<ledger>:<line> tokens=N budget=300` | done |
| 3. `pcrecbench assist-selftest --member M --engine E` | `pcrecbench/assists.py` `selftest`; also `assist-init` | done |
| 4. Proof with DUMMY assists (fixture dir, never under assists/<member>/) | `build/check-assist/fx` via `$PCRECBENCH_ASSISTS_DIR` | done, per language |
| 5. Checks in check-harness | `tools/check_assist.py`, `selfcheck.check_assist_set` | 17 checks |
| AUTHORS.md | `bench/unusual/assists/AUTHORS.md` | done |
| CLAUDE.md updates | testees/, testees/assist/ (new), bench/unusual/, bench/unusual/assists/, pcrecbench/, tools/ | done |

## How it fits together

- **The assist file** holds the counted logic plus its fenced boilerplate.
  The runner owns `main`, argv, I/O, the clock and the answer tokens, and
  the template's fenced `main` just calls `ub_main`. The ABI is
  `testees/assist/ub_assist.h`.
- **Built per (member, engine, source sha).** `pcrecbench/assists.py`
  `build()` builds these pieces:
  - the runner objects and `ub_timed.o`, built once under
    `build/assist/runner-<key>/`;
  - the assist itself: C, C++, or a Rust staticlib built with
    `cargo --offline --locked` against the same regex 1.13.1 lock as
    testees/rust;
  - the engine library;
  - for callouts, `testees/common/ub_bind.o` and the ONE `callees.o` from
    `pcrecbench/callees.py`. With `count=True` it also builds the counting
    twin used by the fire pass.
- **Compile = `ub_setup`.** It is timed once per compile trial and
  attributed to the base testee's first compile phase.
- **The adapter** (`testees/assist/adapter.py`):
  - Non-member patterns (the floor, the `-twin` arms) go to the BASE
    adapter, and their handles are tagged so measure, fire and mem route
    back to it.
  - `pattern_scope` limits a cell to this engine's assisted members, their
    twins and the floor.
  - Each ledger row is RE-COUNTED at describe time. A disagreement, a sha
    mismatch, smuggling or fence drift is refused by name.
- **Harness hooks** (all optional and absent on every pre-existing adapter):
  `pattern_scope`, `capability_grants`, `declaration_ref_for`.
- **Capability.** `missing_capabilities(..., grants=)` unions the grants
  into the testee's tokens. The SUBSUME rule: if the testee holds the
  `unusual-<member>` token a pattern requires, nothing is missing, because
  the assist supplies the feature tokens.
  - `members.py`/`gen_patterns.py` add `requires-unusual-<member>` to every
    member an assist can cover. That is cscan, wild-sexp-balanced,
    wild-json-validate and the callout REAL arms, beside the existing vars
    ones.
  - `ASSIST_ARMS` adds the five assisted ids to the roster;
    bench/capability's `EXCLUDED_TESTEES` lists them.
  - Census over the 15 existing configs: 0 admission changes (snapshot
    `/var/tmp/pcrecbench/b148aw/cap_before.json` vs after).
  - `gen_patterns.py --check` passes on both sets; `check_set.py` 17/17.

The (member, engine) pairs, 43 in all (`assists.PAIRS`):

| engine | members |
|---|---|
| pcre2 | va-tenant, va-route, va-term, va-term-bang, co-netstr |
| onig | va-tenant, va-route, va-term, va-term-bang, co-netstr |
| vectorscan, re2, rust | cscan, wild-sexp-balanced, wild-json-validate, co-luhn, co-isbn, co-member, co-netstr, va-tenant, va-route, va-term, va-term-bang |

## Signatures per family (what an author fills)

**C (pcre2, onig, vectorscan).** `ub_span` is `{long s, e, g1s, g1e}`.
- setup: `int ub_setup(const unsigned char *pattern, size_t plen, const char *member)`
- recursion / callouts / netstr: `int ub_find(const unsigned char *subj, size_t n, size_t start, ub_span *m)`
- callouts: `ub_find` also calls the fenced wrapper `pred(subj, n, g1s, g1e)`
- vars: `int ub_vars(const unsigned char *line, size_t n, const ub_var *v, size_t nv, ub_span *m)`, with `ub_lookup(v, nv, name)` and the fenced `ub_map cache`
- returns: `UB_M`, `UB_N`, `UB_R` (a vars refusal), or negative = the engine's give-up

**C++ (re2).**
- setup: `static int setup(std::string_view pattern)`
- find: `static int find(std::string_view s, size_t start, ub_span *m)`
- callouts: `pred(s, b, c)`
- vars: `static int vars(std::string_view line, const Binding &b, ub_span *m)`, where `b.get(name)` returns `std::optional<std::string_view>`, with the cache `unordered_map<string, unique_ptr<RE2>>`

**Rust.**
- state: `struct State {}`
- setup: `fn setup(pattern: &[u8]) -> Result<State, String>`
- find: `fn find(st: &mut State, s: &[u8], start: usize, m: &mut Span) -> i32`
- callouts: `pred(s, b, c) -> bool`
- vars: `fn vars(st, cache: &mut Cache, line: &[u8], b: &Binding, m: &mut Span) -> i32`, with `type Cache = HashMap<Vec<u8>, Regex>`

## Template token counts (tokcount-1, empty assist)

| engine | lang | per family |
|---|---|---|
| pcre2 | c | vars 6, netstr 6 |
| onig | c | vars 6, netstr 6 |
| vectorscan | c | recursion 6, callouts 6, netstr 6, vars 6 |
| re2 | cpp | recursion 6, callouts 6, netstr 6, vars 6 |
| rust | rust | recursion 7, callouts 7, netstr 7, vars 7 |

Nothing is smuggled. The Rust vars shim had to be split across extra fenced
regions to keep each region at or under the 200-token shim cap.

## BD16 proof

1. **No existing driver or timed file changed.**
   `git diff 78bb39fd HEAD -- testees/{pcre2,pcrec,onig,re2,rust,vectorscan,tre,common,tools}`
   is EMPTY. The only testees/ changes are the new `testees/assist/` files.
2. **The assisted timed loops are in their own translation unit.**
   `ub_timed.c` calls the assist only through function pointers. It is
   compiled once (`ub_timed.o`, sha256 `7bc53872477b08a9...`, identical in
   both runner build keys) and linked unchanged into every assist driver.
3. **The linked loops are identical across drivers.** I disassembled
   `ub_timed_search`, `ub_timed_calls` and `ub_timed_vcalls` in all 10
   built assist drivers, normalising rip-relative displacements and call
   targets. They are byte-identical across every engine and language, with
   one exception: `ub_timed_vcalls` in the Rust-linked cscan driver differs
   only in its alignment-padding NOPs (`cs nopw` + `nop` vs two `nopl`).
   Those come from the final link, not from the code.

## Checks (make check-harness, `check_assist_set`, 17 PASS, ~15 s warm)

- **Templates.** All 16 template x family instantiations have valid fences,
  nothing smuggled, and an empty assist of at most 10 tokens (worst 7).
  - Control: a statement smuggled into an `includes` fence is counted.
  - Control: an edited fence is reported as drift, and the unedited
    template is not.
- **Fixture ledger.** Five ASSISTED dummies plus one padded NOT-CAPABLE row
  (404 tokens) agree with `tokcount ledger_check`.
- **Dummy self-tests, one per language.** Each dummy builds, counts, and
  passes exactly its `n` cases:
  - co-netstr/pcre2: 9 of 27
  - va-tenant/onig: 9 of 20
  - co-luhn/vectorscan: 7 of 16
  - cscan/re2: 8 of 44
  - co-member/rust: 7 of 16
- **Echo controls (the answer path is live).** cscan/re2, cscan/rust and
  va-term/onig each get back exactly the token they answered, find-all
  counts included, on every case.
- **CLI.** `pcrecbench assist-selftest` exits 1 when a case fails, and
  prints the count line.
- **`run_cell` on re2-default-assist-v01 (scratch).**
  - The record is validator-accepted, with testee id
    `re2_11.0.0_default-caps-simdna_assist-v01`.
  - `testee.assist` = [cscan], and the compile row's `assist_tokens` equals
    the counter's number.
  - wild-sexp-balanced is `unsupported-by-declaration`, and
    `parse_not_capable` gives (404, 300).
  - call-stream rows are present.
- **X50 control.** The same record with `testee.assist` removed is
  rejected by X50.
- **Capability.** An `unusual-cscan` grant admits cscan alone; without it,
  recursion and the other feature tokens are missing.
- **Tier and grants.** The real (empty) ledger is pinned-tier and grants
  nothing; the fixture dir forces scratch and grants its ASSISTED rows.

The full `make check` was launched DETACHED. The result is in "make check"
below.

## Findings / owed

1. **High-water (mem) pass.** The 6.4 high-water pass does not run for an
   assisted row. The runner refuses `--mem-pass` by name and `mem_method`
   is None, so assisted match rows carry no `deep_mem_bytes`. OWED if the
   note wants memory for assisted cells.
2. **No deep arm.** There is no `deep` arm for an assisted config; the
   runner refuses `--deep` by name.
3. **The dummies never call `pred`.** So `callout_fires` reads 0 on the
   co-member/rust scratch cell. The counting build and the fire pass are
   wired and ran; a real assist that calls `pred` is what will show fires
   above 0.
4. **Give-up names.** An assist's negative return is reported as
   `giveup:<n>`. The handle declares the range (-2^31, -1) but no names,
   so a give-up is reported by number, not by limit name.
5. **`run.driver_compiler` is one slug per record.** The adapter reuses the
   base testee's registered compiler string. The assist is built with the
   same gcc/g++, and for Rust the rustc version goes in `build_flags`.
6. **The live `assists.tsv` is still header-only.** So every assisted
   config, at the pinned tier, grants nothing. Until L6 lands, every member
   in it reads `unsupported-by-declaration`.
7. **Selftest exits 1 if a member has no public sample.** No such member
   exists today (the four families' samples cover all 43 pairs).

## make check -- HANDED OFF (longer than 4 min)

Launched detached at 2075ee8b+ (the AUTHORS/CLAUDE.md commit), still running at hand-off:

- command: `setsid nohup bash -c "gnutimeout 7200 make check > LOG 2>&1; echo \"DONE rc=\$?\" >> LOG; touch LOG.done"`
- cwd: `/home/pcrec/projects/pcrec-bench/worktrees/b148aw`
- log: `/var/tmp/pcrecbench/b148aw/make_check.log`; marker `/var/tmp/pcrecbench/b148aw/make_check.log.done`
- PID of `gnutimeout 7200 make check`: 1560865
- done so far: check-schema 12 accepted / 104 rejected / 0 WRONG.
- OWED: check-harness count (expect the previous total + 17 from `check_assist_set`), check-report, check-interpret, check-upstream, and the final `DONE rc=`.

Run before hand-off, standalone, all green: `tools/check_assist.py` 17/17; `bench/unusual/check_set.py`
17/17; `check_capability_roster_coverage` + `check_unusual_vocab_and_twin_of` 13/13 PASS;
`check_unusual_gate_skips` all PASS; `gen_patterns.py --check` on unusual and capability. NOT run
standalone: check_calls / check_vars / check_callouts (the members.py tag change could touch them);
the full make check covers them.
