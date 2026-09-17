# lane l6bre2 report — the RE2 adapter (`testees/re2/`)

**Task**: [B42] L6b's first lane (`docs/design/capability_set_v1.md` §11.1) —
build a full RE2 testee adapter: `re2-default` and `re2-longest`, a direct
RE2 C++ driver, capability declarations from a real compile census, the
I-72 raw-bytes lesson, and validated `make check` counts.

**Branch**: `lane/l6bre2`, committed at `23722a3` (`worktrees/l6bre2`).

## What was built

- `testees/re2/driver.cc` — a direct RE2 C++ driver implementing the
  shared protocol (`pcrecbench/adapters.py`'s docstring) byte for byte
  against `testees/pcre2/driver.c`'s reference shape: same argv, same
  per-subject clock discipline, the same S3.1 find-all advance rule, the
  same per-subject alarm/timeout mechanism. RE2-specific: every `RE2`
  object built with `EncodingLatin1` (byte mode, matching the project's
  convention and enabling family 12's non-UTF-8 members); `--longest`
  toggles `set_longest_match`; `--max-mem` is a real flag (unused by v1's
  two configs, future-proofing `re2-bigmem`); `giveup:<code>` never fires
  (RE2's `Match()` has no per-call resource-refusal signal — stated
  explicitly in the file header so nobody goes looking for one).
- `testees/re2/adapter.py` — `describe`/`prepare`/`compile`/`measure`;
  `prepare_driver` runs its own `g++ -std=c++17 $(pkg-config --cflags
  --libs re2)` build (never `driverrun.build_driver()`, which assumes a C
  compiler); `_probe_version` reads `pkg-config --modversion re2`
  (`engine_version`, the soname/ABI version) plus the Debian package
  version (`build_flags`, RE2's own date-based release identifier) since
  RE2 exposes no runtime version API at all; `classify_refusal` maps
  RE2's own closed `ErrorCode` names (embedded in the driver's `error`
  line) to `refusal_class` (`size-limit` for `ErrorPatternTooLarge`,
  `syntax` for every other code).
- `testees/re2/configs.toml` — `re2-default` (max_mem 8 MiB, library
  defaults) and `re2-longest` (`set_longest_match(true)`) only;
  `re2-bigmem` is explicitly `later` per capability_set_v1.md §8 and is
  not built.
- `testees/re2/CLAUDE.md` — the four required deliverable sections (a-d:
  compile-cost definition + its eager-jit caveat, `consumed_length`
  convention, the two configs' exact option objects, the match
  convention and its expectation consequence), the capability
  declaration with its full census evidence, the I-72 raw-bytes
  argument, and the harness fix this lane needed (below).
- `bench/capability/gen_patterns.py`'s `EXT_BENCH_ROSTER` gains
  `re2-default`/`re2-longest` (identical capability lists — confirmed by
  census, `set_longest_match` changes selection, never the parser).
  `patterns.rxt` regenerated and re-verified (`gen_patterns.py --check`,
  INCLUDING the `--list-source` round-trip through the real pinned pcrec
  binary — exit 0). `gen_provenance.py --check`, `gen_variants.py
  --check`, `gen_expectations.py --check` (after regenerating
  `subjects/`/`throughput/`) all pass unchanged.
- `docs/dev/measurements/probe_re2_capability_census.py` +
  `2026-09-17-re2-capability-census.txt` — the witness census (one
  minimal pattern per `REQUIRES_VOCAB` token) AND a corpus census over
  BOTH `bench/capability@0.1` (64 patterns) and `bench/syntax@0.1` (95
  patterns, "other sets' patterns as available"), all compiled through
  the real adapter path. Numbers: capability 39/64 compiled, 25 refused;
  syntax 47/95 compiled, 48 refused; every refusal's `ErrorCode` accounted
  for by one of the eleven excluded REQUIRES tokens or a PCRE-only
  escape/production outside this vocabulary entirely (`\Z`, `\G`, `\h`,
  `\N`, `(?#...)`, `(?|...)`) — zero unexplained refusals.
- `docs/dev/known_issues.md` KB-18, `docs/dev/measurements/CLAUDE.md` and
  `testees/CLAUDE.md` updated.

## The I-72 lesson (mandatory item 4)

The driver protocol delivers the pattern as a **FILE** (`--pattern
FILE`), never a subprocess argv element, so this adapter cannot hit the
fsencode/latin-1 mojibake class pcrec's own argv-based delivery did
(`testees/pcrec/adapter.py`'s I-72 fix). `adapter.compile()` still writes
the file in **binary** unconditionally (`open(patfile, "wb")`), and
`driver.cc`'s `slurp()` reads it back as raw bytes with no
text-mode step in between. Verified end to end on the SAME high-byte
shape the pcrec-side guard uses (`\x93[\x20-\x7e]*\x94` over
`\x93hello\x94`, matching `[0,7)`), and this set's own three real
witnesses (`non-utf8-subject` in the vocabulary census, `high-byte-run`
and `mojibake-curly-quote` in the corpus census) all COMPILED and were
not the source of any of the 25 refusals in `bench/capability`'s census.

## A harness bug this lane found and fixed (KB-18)

`pcrecbench/driverrun.py`'s `DRIVER_BUILDS` dict is process-global and
`driver_build_provenance()` read it unscoped — every driver any adapter
had built so far in the current PROCESS, not just the current record's
own. Silent no-op for the project's whole prior history (every testee's
driver used the same compiler family, `gcc`); RE2's `g++` driver is the
first different family, and `quick --vs` between an `re2-*` and a
`pcre2-*` testee (one process, both prepared before either record is
built) produced `run.driver_compiler = "g-15.2.0, gcc"` — invalid against
the schema's single-token pattern. Fixed at the one call site that
matters: `pcrecbench/harness.py` now clears `DRIVER_BUILDS` immediately
before `adapter.prepare(testee_id, workdir)` for the CURRENT testee (a
strict no-op for every existing single-compiler-family testee, since
`prepare()` always re-registers its own entry right after); separately,
`testees/re2/adapter.py` registers `env.canon_compiler(env.compiler_raw
(cxx))` rather than the raw `"g++"` string (which cannot satisfy the
schema pattern at all — the `+` characters). Full writeup: KB-18,
`docs/dev/known_issues.md`; the mechanism and evidence: `testees/re2/
CLAUDE.md`'s own section.

**Verified**: `python3 -m pcrecbench quick --subbench email --pattern
orig --regime search --testee re2-default --vs pcre2-interp --subjects 5`
now writes two valid scratch records. Numbers from that run (scratch
tier, 3 trials, NOT a ranking claim — box was not quiet):
`re2-default` median 1395.4 ns/call vs `pcre2-interp` 3205.3 ns/call —
`re2-default` 2.30× faster on this pattern/subject set, a plausible
result for a linear-time automaton engine against a backtracker on an
ordinary pattern.

## Validation status

- **`gen_patterns.py --check`** (with the pcrec `--list-source`
  round-trip): **exit 0**.
- **`gen_provenance.py --check`**: 64 rows re-derive, gate clears —
  **exit 0**.
- **`gen_variants.py --check`**: 0 variant rows (unchanged) — **exit 0**.
- **`gen_expectations.py --check`**: 4,990 expectations re-derive
  byte-identical — **exit 0** (two pre-existing, unrelated oracle
  give-ups on `evil-alt-nested`, not touched by this lane).
- **`pcrecbench.tests.test_quick`**: 7/7 passed.
- **`pcrecbench.tests.test_report`** and **`make check-harness`**: both
  launched in the background, then STOPPED mid-run (killed by verified
  PID, cwd checked first) on the manager's explicit instruction once
  pcrecdev1's ~7.5h solo battery started on the shared box (BD3: one
  heavy suite at a time). **Both are OWED, to be run by the manager
  after the battery**, exact commands:

      python3 -m pcrecbench.tests.test_report
      make check-harness

  Neither owed run touches `store/`, measures a pinned cell, or adds a
  pcrec config — both are read-only validation of code already
  committed on this branch. No test in `test_report`'s suite targets
  `run.driver_compiler` rendering, so no regression is expected from
  this lane's `harness.py` change; `make check-harness`'s generic
  `bench/*/` gates were already run individually and pass (below), so
  `check-harness` itself is expected to be a formality, not a discovery
  step.
  (Caveat: `test_report`'s background-task notification reported
  "completed, exit 0" at the moment it was killed — this is the pipe
  closing on SIGTERM, not a real pass/fail summary; the output file has
  no summary line. Treat it as NOT run, per the command above.)

## What was NOT done

- No pinned cell was measured (out of scope per the brief; scratch-tier
  `quick` only).
- No `tools/selfcheck.py` section was added. This adapter's only
  RE2-specific stamps (`refusal_class`, `ncapturegroups`/
  `program_size`/`reverse_program_size`) are asserted by the compile
  census script rather than a selfcheck function — `testees/re2/
  CLAUDE.md`'s "Smoke coverage" section states this choice and names the
  promotion-to-selfcheck path as a natural scoped follow-up if the
  manager wants `make check-harness` itself to fail on a future RE2
  capability regression.
- `re2-bigmem` (capability_set_v1.md §8, `later`) is not built.
- Family 11's cross-convention scoring for `re2-longest` (the missing
  per-testee/variant expectation override) is NOT built — out of scope,
  named explicitly in `testees/re2/CLAUDE.md` as capability_set_v1.md
  §5.6's own future lane, not this one's.

## Handback

Branch `lane/l6bre2` is ready for the manager to review and merge. Two
numbers are OWED (test_report and check-harness completion) — both are
read-only verification of already-committed code, not blocking on any
further edit from this lane. This lane does not intend to poll further;
a fresh agent (or the manager) should check the two marker files above
and fold the final counts in before or during merge.
