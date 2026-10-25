# b140drv2 report ([B140] build-order step 3, continued: rust + RE2 `--mode subst`, lane b140drv2, 2026-10-25)

Branch `lane/b140drv2` (worktree `worktrees/b140drv2`, base 43b65a3c). No timing run, no `store/` or `reports/` write, no install, no download, `~/pcrec` untouched, `testees/pcrec/` and `catalogue/` untouched. Cargo built `--offline` from the registry already on the box (no crate was missing). Scratch: `/var/tmp/pcrecbench/b140drv2/` (acc-small copy, driver builds, trial-1 outputs, the additivity workdir, logs). The charter is `docs/design/subst_bench_v1.md` 3.1 (rust and re2 rows), 3.1.1, 3.1.2 with 8a's rulings; the shared harness is b140drv's (`pcrecbench/substrun.py`, `Adapter.subst_support/measure_subst`, the `out` line, the gate, X44 compile rows) and was REUSED, not forked.

## Charter-vs-committed checklist

| # | item | committed artifact / status |
|---|---|---|
| 1 | rust driver `--mode subst`: `regex::bytes::Regex::replace_all(&[u8], &[u8])`, `unicode(false)`, `Cow` allocation inside the clock (a reading note), `out` line outside the clock, iters 1 | `testees/rust/src/main.rs` (`run_subst`, `--template`, `--out-dir`, `--bound` accepted/ignored, `--subst-flags` validated/ignored, `--no-unicode`; refuses `--find-all`/`--prime`/`--utf8`/`--iters>1`/no `--template` by name). Adapter: `subst_support` (dialect `rust`, competitor `rust-regex`, only `rust-default`), `measure_subst`, compile builds `unicode(false)` and only the PLAIN form for a substitution set (`options["substitution"]`). |
| 2 | RE2 driver `--mode subst`: `RE2::GlobalReplace` on a FRESH subject copy made OUTSIDE the clock | `testees/re2/driver.cc` (`--mode subst` branch: `new std::string(s.buf)` before the timed call; same refusals); adapter `subst_support` (dialect `re2`, competitor `re2`, only `re2-default`), `measure_subst`. The substitution count is `GlobalReplace`'s return value. |
| 3 | neutral template rendered per dialect; cases divergences.tsv declares unsupported (6, 7) are `unsupported-by-declaration` compile rows, never a run | uses `pcrecbench/subst_template.py` unchanged. Both dry-run records carry compile rows `unsupported-by-declaration` for `6-upper` (`unsupported:no-case-operators`) and `7-url-tld-fix` (`unsupported:pattern-syntax`), each citing its `divergences.tsv` row, and no match rows for them (check_subst section 10). |
| 4 | every case that runs matches `expectations.tsv` by sha256 on acc-small | YES for both engines, all six runnable cases (1, 2, 3, 4, 5, 5b): sha256 + count + length equal (driver called directly, and through `run_cell`, gate `agrees`). No mismatch, so no finding to file on that axis. |
| 5 | BD16: NEW unit/function, existing instrument byte-identical, additivity proof archived, OWED sentinel read noted | `testees/rust/timed-subst/` (crate `rust-timed-subst`) and `testees/re2/timed_subst.{cc,h}`; proof `docs/dev/measurements/2026-10-25-b140drv2-instrument-additivity.{py,txt}`; accounting below. |
| 6 | `tools/check_subst.py`: direct-driver sha256 equality per runnable case for rust-regex and re2, plus the by-declaration rows | section 10 (`_rust_re2`), +19 checks (43 = 24 + 19 standalone; list below). |
| 7 | full `make check-harness`, counts reported | see "Check counts". |
| 8 | one scratch dry run per engine on acc-small (`--tier scratch`), validator-accepted | below. |
| 9 | CLAUDE.md files; the adapters.py protocol doc if it changes | `testees/rust`, `testees/re2`, `tools`, `pcrecbench`, `docs/dev/measurements`, `docs/dev/lanes` CLAUDE.mds; `pcrecbench/adapters.py` header (`--no-unicode`; rust/RE2 ignore `--bound`/`--subst-flags`). |

### Scratch dry runs (acc-small, `run --subbench subst --testee T --tier scratch --subjects 1 --trials 5`)

Both validated with `schema/validate.py --check-filename`: `1 valid, 0 invalid`. Records (gitignored, in the scratch store, not committed):

* `/var/tmp/pcrecbench/b140drv2/store/records/subst@0.1/rust_1.13.1_default-caps-simdna/subst@0.1__rust_1.13.1_default-caps-simdna__ryzen7700x__20261025T054025Z.jsonl`
* `/var/tmp/pcrecbench/b140drv2/store/records/subst@0.1/re2_11.0.0_default-caps-simdna/subst@0.1__re2_11.0.0_default-caps-simdna__ryzen7700x__20261025T054039Z.jsonl`

Each: 62 rows (32 compile = 6 cases x 5 trials + the 2 by-declaration rows, 30 match = 6 cases x 5 trials); every match row `matched-as-expected` / gate `agrees`; status `measured` (the box was quiet; the scratch tier does not gate). The agreement block reads `agree 0/0 groups -- nothing judged (6 rows unjudged)`, the b140drv F1 blindness, unchanged. Timings are NOT numbers: no pin, a scratch run (rust: 1-23 ms, re2: 5-45 ms per call on 3.9 MB).

### The section-10 checks (19, `tools/check_subst.py`)

Per engine (rust-default, re2-default), x2: the driver called DIRECTLY on acc-small, the 6 runnable cases' output sha256 + count + length == `expectations.tsv` and exactly 2 cases declared unsupported (1); `--find-all`/`--prime`/`--utf8` refused in `--mode subst` by name (3); `--iters 2` refused by name (1); no `--template` refused by name (1); `run_cell` into a scratch store: a schema-1.9 record, 12 substitution rows (6 cases x 2 trials) all `agrees`, `invocation: library` (1); cases 6 and 7 are compile rows `unsupported-by-declaration` citing the engine's `divergences.tsv` row (7's the pattern-level token), no match rows for them, 14 compile rows in all (1). Once: `re2-longest` refused by name (not the chartered config) (1); the gate through the rust driver: a deliberately WRONG template fails BY NAME, not timed (1); `plan_case` accepts the pattern-level `pattern-syntax` row beside a different renderer token (1).

## BD16 accounting

`testees/re2/timed.cc`/`timed.h` and the whole `testees/rust/timed/` crate are NOT edited (diff-empty against 43b65a3c, asserted in the probe), so BD16 (2)'s trigger for the EXISTING instruments does not fire. The new instruments are new units: `timed_subst.cc` (RE2, own translation unit, `noinline` + `aligned(64)`, 0 mod 64) and the crate `rust-timed-subst` (`#[inline(never)]`, own `.text.rust_timed_subst` section with `.balign 64`, 0 mod 64). Evidence (`2026-10-25-b140drv2-instrument-additivity.txt`): RE2 `timed_run` 227 insns, sha `d442b4a1f49a6268` old = new, address mod 64 = 0 in both; rust `run_subject` 341 insns, sha `cee097a619eb342e` old = new, mod 64 = 0 in both; `main` differs in both drivers (the positive control: 976 -> 1654 insns RE2; 3645 -> 4897 rust); 6 RE2 + 6 rust existing-mode invocations (search, match, find-all, `--prime`, `--longest`, `--utf8`/`--encoding utf8`, `--subject-timeout`) have identical stdout on every column but SECONDS. Item by item:

* (1) an instrument change is recorded: `run.harness_commit` differs from here on; the RE2 build line lists `timed_subst.cc`, the cargo build line is unchanged (`--locked`; the new crate is in the lock). DONE by construction.
* (2) plan row = the existing `[B140]` (not edited here); BD16 named in the first commit message and in both new units' headers; the re-pin-control timing run is OWED and, for the existing instruments, NOT required (nothing they measure moved: the disassembly proof). For the NEW instruments there is no previous version to A/B against.
* (3) the sentinel reads the instrument every window: OWED to the first window containing rust/RE2 subst cells (owner manager; trigger: that window). `bench/sentinel`'s rust and re2 cells run unchanged; a flat sentinel is the evidence that `run_subject`/`timed_run` did not move.
* (4) re-pin timing: unaffected (no pcrec re-pin here). (5) the isolation proof is the probe above.

Note on the rust binary: adding the `rust-timed-subst` dependency changes `Cargo.lock` and the driver's link (the crate-disambiguator hashes in mangled names), so the rust driver's `binary_identity` sha changes; nothing in a matching cell reads that except provenance.

## Findings the manager should rule on

1. **`substrun.plan_case` was pcre2-shaped, fixed generically (R-BENCH-4).** It raised "the renderer's token is X" whenever the table's `unsupported:<token>` differed from the renderer's refusal token. Every non-pcre2 dialect on case 7 differs (table: `pattern-syntax`; renderer: `no-conditional` first), so rust and RE2 would have been refused with a SubstError. A PATTERN-level token (`PATTERN_LEVEL_TOKENS = ("pattern-syntax",)`) now governs over the template renderer's, which never sees the pattern; any other disagreement is still an error by name (pre-existing check retained). The same fix serves sed/sd/rg later.
2. **rust's substitution count is an UNTIMED SECOND PASS** (`find_iter(..).count()` after the clock): the `regex` API returns no count and a counting closure would be a different, non-idiomatic competitor. Cost: one extra scan per subject per trial; on acc-main (362 MB) that is a window-length item (order of seconds for the dense case 3), never a timing one. RE2 gets its count free.
3. **The v1.4 trial-agreement blindness (b140drv F1) applies to both new testees identically** (iters = 1 -> every group "unjudged"); still the manager -> Frank ruling before the first pinned subst window.
4. **`options["substitution"]`** is a new, generic way for `run_cell` to tell an adapter it is compiling for a transform (`harness.py`, 4 lines); every adapter that ignores `options` is unaffected (the check-harness counts below). Only rust uses it, to skip the whole-subject artifact (a subst set has no `match` regime) and to build `unicode(false)`.
5. **Only `rust-default` and `re2-default` support the substitution set.** `re2-longest` (POSIX leftmost-longest, a different answer on ambiguous alternations) and `re2-utf8` are refused by name on `subst`; the cases are unambiguous so `re2-longest` would probably agree, but the charter names `re2-default` and a wider roster is the manager's call.
6. **Memory on acc-main (not run):** RE2 holds the subject, the fresh copy and (briefly) the file-write path: ~1.1 GB; rust holds the subject (Arc), the output `Vec` and `Cow` temporaries: ~0.8 GB. The 7.6 GB tmpfs is not involved (outputs go to `$PCRECBENCH_SUBST_OUT`).

## OWED

| item | owner | trigger |
|---|---|---|
| BD16 (3): sentinel read of rust-default and re2-default in the first window with subst cells | manager | that window |
| acc-main gate + timing for rust/RE2 (362 MB); JIT-stack-type probes do not apply | manager's window | window grant via pcrecdev1 |
| Finding 3 (spread-rule blindness at iters = 1) and b140drv findings 1, 2, 4, 5 | manager -> Frank | before the first pinned subst window / plan [B140] step 5 |
| pcrec driver, TOOLS tier, reporter | later lanes (steps 4-5) | the charter order |
| a short-call sentinel analogue for `timed_subst` (not asked) | manager | optional |

## Check counts

`make check-harness` (= `LC_ALL=C python3 tools/selfcheck.py`; log `/var/tmp/pcrecbench/b140drv2/checkh.log`, ends `DONE rc=0`): **900 check(s) passed, 0 FAILED** on the branch tip, run once, clean first time (the base was 881/0 after b140drv; the +19 are section 10). No inconclusive-load item occurred (load average 0.2 at launch, the box quiet). Standalone, `check_subst.py`'s driver slice (sections 9 + 10) = 43 ok / 0 bad in 65 s. The additivity probe: 6 + 6 existing-mode invocations identical, `timed_run` and `run_subject` unchanged. Not run (nothing they read changed): `make check-report`, `check-interpret`, `check-upstream`, `check-schema`.

Expected merge conflict: `tools/selfcheck.py` was not touched by this lane at all (the new checks live in `tools/check_subst.py`), so the conflict the brief anticipated with b142prep should not arise from here; `testees/rust/Cargo.lock` and `Cargo.toml` are the files most likely to meet another lane.
